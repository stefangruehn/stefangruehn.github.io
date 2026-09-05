#!/usr/bin/env python3
"""Prüft, ob `hugo --minify` die Seiten unbeschädigt lässt.

Der Minifier ist die einzige Stufe, die zwischen dem lokalen Bild und der
veröffentlichten Seite liegt: gebaut wird lokal ohne, im CI mit `--minify`.
Verliert er dabei die Spur — ein ungepaartes `"` in einem SVG-Textknoten
genügt —, fehlen Leerzeichen an Inline-Tags und schließende Tags fallen weg.
Beides ist in der Quelle nicht zu sehen und lokal nicht zu bemerken.

Deshalb wird zweimal gebaut und verglichen. Zwei Prüfungen je Seite:

  Text      Inline-Tags gelten als nichts, Block-Tags als Leerzeichen.
            Fällt ein Leerzeichen weg, unterscheiden sich die Fassungen.
  Struktur  Start- und End-Tags je Elementname müssen gleich häufig sein.
            Fällt ein `</a>` weg, fällt es hier auf.

Aufruf:  tools/check-minify.py [--hugo PFAD]
Rückgabe: 0 wenn beide Fassungen übereinstimmen, sonst 1.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Elemente ohne eigene Zeilenbox. Ihr Wegfall darf den Text nicht verändern,
# ihr Vorhandensein kein Leerzeichen erzeugen — sonst schluckte der Vergleich
# genau den Fehler, den er finden soll.
INLINE = (
    "a abbr b bdi bdo cite code data dfn em i kbd mark q s samp small span "
    "strong sub sup time u var wbr"
).split()

# void: haben nie ein End-Tag, dürfen in der Strukturzählung nicht fehlen.
VOID = (
    "area base br col embed hr img input link meta param source track wbr"
).split()

WEG = re.compile(r"(?is)<(script|style|head)\b.*?</\1>")
# In SVG und MathML schliesst `<path/>` wirklich, in HTML nicht. Die
# Strukturpruefung gilt darum nur fuer HTML; Fremdelemente fliegen vorher raus.
FREMD = re.compile(r"(?is)<(svg|math)\b.*?</\1>")
KOMMENTAR = re.compile(r"(?s)<!--.*?-->")
INLINE_TAG = re.compile(r"(?is)</?(%s)(\s[^>]*)?/?>" % "|".join(INLINE))
TAG = re.compile(r"(?s)<[^>]+>")
LEER = re.compile(r"[ \t\r\n]+")


def text(html_quelle: str) -> str:
    """Sichtbarer Text, so wie der Browser ihn zusammensetzt."""
    s = WEG.sub(" ", html_quelle)
    s = KOMMENTAR.sub(" ", s)
    s = INLINE_TAG.sub("", s)
    s = TAG.sub(" ", s)
    return LEER.sub(" ", html.unescape(s)).strip()


class Zaehler(HTMLParser):
    """Zählt Start- und End-Tags je Elementname."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.auf: Counter[str] = Counter()
        self.zu: Counter[str] = Counter()

    def handle_starttag(self, tag, attrs):
        self.auf[tag] += 1

    def handle_endtag(self, tag):
        self.zu[tag] += 1

    def handle_startendtag(self, tag, attrs):
        # `<a/>` ist in HTML kein geschlossenes Element: der Parser im Browser
        # ignoriert den Schrägstrich und lässt das Element offen. Nur bei
        # void-Elementen bedeutet er etwas. Python zählte sonst ein End-Tag mit,
        # das es nicht gibt — und der Befund fiele unter den Tisch.
        self.auf[tag] += 1
        if tag in VOID:
            self.zu[tag] += 1


def struktur(html_quelle: str) -> Counter[str]:
    """Elementnamen, bei denen Start- und End-Tag nicht aufgehen."""
    z = Zaehler()
    z.feed(FREMD.sub("", WEG.sub("", html_quelle)))
    offen: Counter[str] = Counter()
    for name in set(z.auf) | set(z.zu):
        if name in VOID:
            continue
        d = z.auf[name] - z.zu[name]
        if d:
            offen[name] = d
    return offen


def bauen(hugo: str, ziel: Path, minify: bool) -> None:
    cmd = [hugo, "--gc", "--destination", str(ziel)]
    if minify:
        cmd.append("--minify")
    p = subprocess.run(cmd, cwd=REPO, capture_output=True, text=True)
    if p.returncode != 0:
        sys.stderr.write(p.stdout + p.stderr)
        raise SystemExit(f"FEHLER  hugo{' --minify' if minify else ''} schlug fehl")


def ausschnitt(a: str, b: str) -> str:
    """Die Stelle, an der sich zwei Textfassungen erstmals trennen."""
    i = 0
    while i < min(len(a), len(b)) and a[i] == b[i]:
        i += 1
    return f"ohne: …{b[max(0, i - 45):i + 45]}…\n         mit:  …{a[max(0, i - 45):i + 45]}…"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--hugo", default="hugo", help="Pfad zum hugo-Binary")
    args = ap.parse_args()

    if not shutil.which(args.hugo):
        raise SystemExit(f"FEHLER  {args.hugo} nicht gefunden")

    tmp = Path(tempfile.mkdtemp(prefix="check-minify-"))
    try:
        mit, ohne = tmp / "mit", tmp / "ohne"
        bauen(args.hugo, mit, minify=True)
        bauen(args.hugo, ohne, minify=False)

        fehler = 0
        seiten = 0
        for f in sorted(mit.rglob("*.html")):
            g = ohne / f.relative_to(mit)
            if not g.exists():
                print(f"FEHLER  {f.relative_to(mit)}: fehlt im Build ohne --minify")
                fehler += 1
                continue
            seiten += 1
            a, b = f.read_text(encoding="utf-8"), g.read_text(encoding="utf-8")

            ta, tb = text(a), text(b)
            if ta != tb:
                print(f"FEHLER  {f.relative_to(mit)}: --minify verändert den Text")
                print("         " + ausschnitt(ta, tb))
                fehler += 1

            sa, sb = struktur(a), struktur(b)
            if sa != sb:
                namen = sorted(set(sa) | set(sb))
                print(f"FEHLER  {f.relative_to(mit)}: --minify verliert Tags")
                for n in namen:
                    if sa[n] != sb[n]:
                        print(f"         <{n}>: offen ohne {sb[n]}, mit {sa[n]}")
                fehler += 1

        if fehler:
            print(f"\n{fehler} Befund(e) auf {seiten} Seiten. Nicht veröffentlichen.")
            return 1
        print(f"OK  {seiten} Seiten: --minify ändert nichts am Text und an keiner Struktur.")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
