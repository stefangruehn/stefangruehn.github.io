#!/usr/bin/env python3
"""Check that `hugo --minify` leaves the pages intact.

The minifier is the only stage between the local picture and the published
page: the local build runs without it, CI builds with `--minify`. When it
loses track — a single unpaired `"` in an SVG text node is enough — spaces
around inline tags go missing and closing tags are dropped. Neither is
visible in the source, and neither shows up locally.

So we build twice and compare. Two checks per page:

  Text       Inline tags count as nothing, block tags as a space.
             If a space is lost, the two versions differ.
  Structure  Start and end tags must be equally frequent per element name.
             If a `</a>` is dropped, it shows up here.

Usage:  tools/check-minify.py [--hugo PATH]
Returns: 0 if both versions agree, 1 otherwise.
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

# Elements without a line box of their own. Dropping them must not change the
# text, and their presence must not create a space — otherwise the comparison
# would swallow the very defect it is meant to find.
INLINE = (
    "a abbr b bdi bdo cite code data dfn em i kbd mark q s samp small span "
    "strong sub sup time u var wbr"
).split()

# void: never have an end tag, so they must not be counted as missing one.
VOID = (
    "area base br col embed hr img input link meta param source track wbr"
).split()

WEG = re.compile(r"(?is)<(script|style|head)\b.*?</\1>")
# In SVG and MathML `<path/>` really does close; in HTML it does not. The
# structure check therefore covers HTML only; foreign elements are stripped
# beforehand.
FREMD = re.compile(r"(?is)<(svg|math)\b.*?</\1>")
KOMMENTAR = re.compile(r"(?s)<!--.*?-->")
INLINE_TAG = re.compile(r"(?is)</?(%s)(\s[^>]*)?/?>" % "|".join(INLINE))
TAG = re.compile(r"(?s)<[^>]+>")
LEER = re.compile(r"[ \t\r\n]+")


def text(html_quelle: str) -> str:
    """Visible text, the way the browser assembles it."""
    s = WEG.sub(" ", html_quelle)
    s = KOMMENTAR.sub(" ", s)
    s = INLINE_TAG.sub("", s)
    s = TAG.sub(" ", s)
    return LEER.sub(" ", html.unescape(s)).strip()


class Zaehler(HTMLParser):
    """Counts start and end tags per element name."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.auf: Counter[str] = Counter()
        self.zu: Counter[str] = Counter()

    def handle_starttag(self, tag, attrs):
        self.auf[tag] += 1

    def handle_endtag(self, tag):
        self.zu[tag] += 1

    def handle_startendtag(self, tag, attrs):
        # `<a/>` is not a closed element in HTML: the browser parser ignores
        # the slash and leaves the element open. Only for void elements does it
        # mean anything. Otherwise Python would count an end tag that does not
        # exist — and the finding would go unnoticed.
        self.auf[tag] += 1
        if tag in VOID:
            self.zu[tag] += 1


def struktur(html_quelle: str) -> Counter[str]:
    """Element names whose start and end tags do not add up."""
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
    """The spot where two text versions first diverge."""
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
