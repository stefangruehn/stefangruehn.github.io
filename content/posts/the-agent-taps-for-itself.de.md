---
title: "Der Agent tippt selbst: Android-Apps mit adb und Emulator"
date: 2026-09-25T10:55:00+02:00
tags: ["claude-code", "android", "emulator", "tooling", "workflow", "Field Notes"]
themen: ["denken"]
summary: "Ein Satz je Wunsch, und der Agent baut, installiert, tippt und sieht sich das Ergebnis selbst an. Am Telefon und im Emulator schließt sich die Schleife, die bei Firmware an meiner Hand hängt. Gehakt hat es an den Rändern: an einem Push, einer Überschrift im Changelog und einem Fenster."
---

## Kurzfassung

- Bei einer Android-App ist das Gerät am Kabel Bildschirm, Eingabe und Prüfstand zugleich.
  Claude Code baut mit Gradle, installiert, tippt über `adb` und sieht sich das Ergebnis selbst an.
- An einem Morgen wurden aus sieben Sätzen von mir ein Theme, ein App-Icon, eine Hilfeseite, ein Impressum und ein Release.
- Wo niemand aufs Telefon sehen muss, übernimmt der Emulator.
  Dort braucht es nicht einmal meinen Finger für die Displaysperre.
- Gehakt hat es nie im Code, sondern am Rand: an einem Push, an einer Überschrift im Changelog und an einem Fenster, das ein anderes verdeckt.
  Für das Fenster steht das Werkzeug am Ende dieses Beitrags.

## Sieben Sätze an einem Morgen

Die TeeToTum-App ist die Begleit-App zu einem Drehknopf mit rundem Display.
Sie ist in Kotlin mit Compose Multiplatform geschrieben und läuft bisher nur unter Android.
Version 0.1.0 war einen Tag alt, als ich mich gegen Viertel vor sechs Uhr morgens an den Rechner setzte.
Gut vierzig Minuten später war 0.2.0 veröffentlicht.

Dazwischen lagen sieben Wünsche, jeder ein Satz auf Deutsch:

- Ein drittes Theme, das dem roten Theme auf dem Knopf entspricht, auch im hellen Modus.
- Alle Icons in der Farbe der Auswahlpunkte.
- Menüeinträge mit derselben Rundung wie die Buttons und ein App-Icon wie das Favicon des Knopfs.
- Etwas größere Schrift auf den Buttons.
- Eine Hilfeseite.
- Ein Impressum.
- Committen, pushen, die App deinstallieren und aus dem Repo neu installieren.

Das Theme stammt aus einer Rust-Konstante der Firmware.
Claude übersetzte sie in ein Material-Farbschema und rechnete die Kontraste nach.
Weiß auf dem Rot des Knopfs, `#F0283A`, liegt bei 4,2:1 und damit unter den 4,5:1, die für Text empfohlen sind.
Die Schrift auf den Buttons wurde deshalb fast schwarz.
Eine helle Fassung gibt es auf dem Knopf nicht, sie ist abgeleitet: ein dunkleres Rot, `#C41E2E`, auf Weiß.

Das App-Icon ist nicht nachgezeichnet.
Ein kleines Python-Skript liest das SVG des Favicons und schreibt daraus ein Vector Drawable mit 14 Pfaden.
Auf dem Startbildschirm sieht das Icon aus wie der Drehknopf selbst.

## Die Schleife am Gerät

Das Telefon hing per USB am Rechner.
Nach jedem Wunsch lief dieselbe Schleife: `./gradlew installDebug`, dann startet `adb` die App.
`uiautomator dump` liefert den Baum der sichtbaren Oberfläche mit den Koordinaten jedes Texts, `input tap` tippt darauf, `screencap` fotografiert.
Vor jedem Tippen prüfte Claude, ob die App noch vorn war.

Die Bildschirmfotos setzte es zu Montagen zusammen, verkleinert auf 30 %, dunkel und hell nebeneinander.
Umgeschaltet wurde mit `cmd uimode night yes` und danach zurückgestellt.
An diesen Bildern fand es zwei Dinge selbst:
ein doppeltes Leerzeichen in der Hilfe, das aus einem Zeilenumbruch in einem Kotlin-String kam,
und dass der Link im Impressum wirklich den Browser öffnet.
Beim ersten Versuch traf der Tipp daneben, beim zweiten nicht.

Aus zwei Wünschen wurden Tests.
„Alle Icons in dieser Farbe“ wurde eine Funktion `AppIcon` und ein Test, der jeden Aufruf von Materials `Icon(` außerhalb dieser Funktion meldet.
„Dieselbe Rundung“ wurde eine gemeinsame Konstante.
So bleibt ein Wunsch auch beim nächsten Button erfüllt, ohne dass ich ihn wiederhole.

Rückgefragt hat Claude an diesem Morgen ein einziges Mal, und die Frage war berechtigt.
„Aus dem Repo installieren“ konnte heißen: frisch geklont bauen, das alte Release nehmen oder ein neues schneiden.
Ich klickte auf das neue Release.
Danach ging es in einem Zug: Version 0.2.0, Tag, die CI baut und signiert in 2 Minuten 40 Sekunden, APK laden, Prüfsumme vergleichen, `adb install`.

## Der Emulator, wenn niemand hinsehen muss

Am Telefon sehe ich zu, wenn ich will, und manchmal muss ich es.
Für vieles ist das nicht nötig: ob ein Formular speichert, ob eine Liste filtert, ob ein Hinweis erscheint.

In einem zweiten Projekt, dem Neubau einer älteren Android-App, gilt deshalb seit dem 24. September eine Regel:
Was sich ohne meine Hand und ohne meinen Blick prüfen lässt, prüft Claude im Emulator.
Das Telefon bleibt für das, was ich selbst sehen soll, und für Text mit echter Schrift.

Die Werkzeuge sind dieselben.
Der Emulator ist für `adb` ein Gerät wie jedes andere, mit eigener Seriennummer.

Ein Unterschied betrifft die Displaysperre.
Die App verschlüsselt einzelne Felder mit einem Schlüssel, den Android an die Sperre des Geräts bindet.
Ohne Sperre verfällt er, und mit ihm die Testdaten.
Am Telefon bestätige ich jede Abfrage mit dem Finger.
Im Emulator setzt ein Skript eine Test-PIN und tippt sie selbst ein.

## Was an den Rändern hakte

**Der Push.**
Vor dem Push sah Claude nur die eigenen Änderungen auf Privates durch, nicht alles seit dem letzten Push.
Drei ältere Commits gingen ungeprüft mit.
Die Durchsicht kam danach und fand nichts, aber sie kam in der falschen Reihenfolge.

**Das Changelog.**
Das Release trägt eine leere Überschrift „Unreleased“, und die App zeigt ihr Changelog selbst an.
Aufgefallen ist das erst nach dem Tag.

**Das Fenster.**
Ohne Fenster stürzte der Emulator auf meinem Rechner ab, also läuft er mit.
Unter GNOME mit Wayland besteht er aus zwei Fenstern: dem Gerät und einer schmalen Werkzeugleiste, die er rechts daneben setzt.
Steht das Gerät am rechten Bildschirmrand, schiebt GNOME die Leiste in das Gerät hinein.
Ausblenden lässt sie sich nicht, einen Schalter dafür kennt `emulator -help` nicht.

Ich sehe dem Emulator gern zu, und dafür muss das Gerät frei liegen.
Also bat ich Claude um ein Werkzeug, das den Emulator startet, falls er nicht läuft, beide Fenster nach vorn holt und das Gerät so weit nach links rückt, dass die Leiste daneben passt.
`xdotool` und `wmctrl` waren nicht installiert.
Das Skript spricht deshalb über Pythons `ctypes` direkt mit der X11-Bibliothek, denn der Emulator läuft unter Wayland als X11-Programm.

Getestet hat Claude es in drei Fällen: Lage schon richtig, Leiste absichtlich ins Gerät geschoben, Emulator beendet und kalt gestartet.
Beim Kaltstart vergingen 18 Sekunden bis zum fertigen Boot.

Die erste Fassung lief, aber ein Linter mit allen Regeln fand 60 Stellen.
Die X11-Verbindung öffnete sich schon beim Import, Argumente wurden von Hand aus `sys.argv` gelesen, es fehlten Typen.
Die Fassung unten besteht Ruff mit allen Regeln und mypy im strikten Modus.
Für ein Hilfsskript ist das mehr als nötig, aber es ist dieselbe Prüfung wie für den Code der App.

## Was ich daraus mitnehme

- Ein Gerät, das der Agent selbst bedienen kann, spart mir die Runde, in der ich hinsehe und beschreibe, was ich sehe.
- Was ich sehen will, zeige ich mir am Telefon.
  Was nur geprüft werden muss, läuft im Emulator.
- Ein Wunsch, der als Test festgehalten ist, muss nicht wiederholt werden.
- Was noch hakt, liegt im Verfahren um den Code herum, also gehören die Prüfungen dorthin: vor den Push, vor den Tag, vor das Fenster.

## Das Werkzeug

`tools/emulator.py` startet ein bestimmtes virtuelles Gerät, holt es nach vorn und legt die Werkzeugleiste neben das Gerät.
Name des Geräts, Seriennummer und Pfad zum SDK stehen oben als Konstanten.
Es braucht Python ab 3.12, `xprop` und eine X11-Sitzung oder XWayland.

```python
#!/usr/bin/env python3
"""Start the AVD ut-nolock unless it runs, raise it and keep its toolbar beside it.

    tools/emulator.py [--no-boot-wait]

The emulator runs as two X11 windows under XWayland: the device and its toolbar, which
it places right of the device. Near the right screen edge the window manager pushes the
toolbar into the device; moving the device left lets the toolbar follow beside it.
Talks to libX11 through ctypes and reads window names with xprop: no packages needed.
"""

from __future__ import annotations

import argparse
import ctypes
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import TYPE_CHECKING, NamedTuple

if TYPE_CHECKING:
    from collections.abc import Callable

AVD = "ut-nolock"
SERIAL = "emulator-5554"
SDK = Path.home() / "Android" / "Sdk"
ADB = SDK / "platform-tools" / "adb"
EMULATOR = SDK / "emulator" / "emulator"
DEVICE_TITLE = f"Android Emulator - {AVD}:5554"
TOOLBAR_TITLE = "Emulator"
GAP = 8  # px between device and toolbar
WINDOW_TIMEOUT = 120
BOOT_TIMEOUT = 300

CLIENT_MESSAGE = 33
SUBSTRUCTURE_NOTIFY_AND_REDIRECT = (1 << 19) | (1 << 20)
SOURCE_PAGER = 2  # _NET_ACTIVE_WINDOW source that window managers honour


class Rect(NamedTuple):
    """Absolute position and size of a window's client area."""

    x: int
    y: int
    width: int
    height: int

    @property
    def right(self) -> int:
        """First column right of the window."""
        return self.x + self.width


class ClientMessage(ctypes.Structure):
    """XClientMessageEvent with 32-bit data."""

    _fields_ = (
        ("type", ctypes.c_int),
        ("serial", ctypes.c_ulong),
        ("send_event", ctypes.c_int),
        ("display", ctypes.c_void_p),
        ("window", ctypes.c_ulong),
        ("message_type", ctypes.c_ulong),
        ("format", ctypes.c_int),
        ("l", ctypes.c_long * 5),
    )


class XEvent(ctypes.Union):
    """XEvent, padded to the size libX11 expects."""

    _fields_ = (("xclient", ClientMessage), ("pad", ctypes.c_long * 24))


class X11:
    """The few libX11 calls this tool needs, bound to one display connection."""

    def __init__(self) -> None:
        """Open the default display."""
        lib = ctypes.cdll.LoadLibrary("libX11.so.6")
        ptr, win, i = ctypes.c_void_p, ctypes.c_ulong, ctypes.c_int
        lib.XOpenDisplay.restype = ptr
        lib.XOpenDisplay.argtypes = [ctypes.c_char_p]
        lib.XDefaultRootWindow.restype = win
        lib.XDefaultRootWindow.argtypes = [ptr]
        lib.XInternAtom.restype = win
        lib.XInternAtom.argtypes = [ptr, ctypes.c_char_p, i]
        lib.XGetGeometry.argtypes = [ptr, win, ptr, ptr, ptr, ptr, ptr, ptr, ptr]
        lib.XTranslateCoordinates.argtypes = [ptr, win, win, i, i, ptr, ptr, ptr]
        lib.XSendEvent.argtypes = [ptr, win, i, ctypes.c_long, ptr]
        lib.XRaiseWindow.argtypes = [ptr, win]
        lib.XMoveWindow.argtypes = [ptr, win, i, i]
        lib.XFlush.argtypes = [ptr]
        self.lib = lib
        self.display = lib.XOpenDisplay(None)
        if not self.display:
            sys.exit("no X display (DISPLAY unset?)")
        self.root = lib.XDefaultRootWindow(self.display)

    def geometry(self, window: int) -> Rect:
        """Return where a window's client area sits on the screen."""
        root, x, y = ctypes.c_ulong(), ctypes.c_int(), ctypes.c_int()
        width, height = ctypes.c_uint(), ctypes.c_uint()
        border, depth = ctypes.c_uint(), ctypes.c_uint()
        self.lib.XGetGeometry(
            self.display,
            window,
            *map(ctypes.byref, (root, x, y, width, height, border, depth)),
        )
        abs_x, abs_y, child = ctypes.c_int(), ctypes.c_int(), ctypes.c_ulong()
        self.lib.XTranslateCoordinates(
            self.display,
            window,
            self.root,
            0,
            0,
            *map(ctypes.byref, (abs_x, abs_y, child)),
        )
        return Rect(abs_x.value, abs_y.value, width.value, height.value)

    def activate(self, window: int) -> None:
        """Ask the window manager to focus a window and raise it."""
        event = XEvent()
        event.xclient.type = CLIENT_MESSAGE
        event.xclient.send_event = 1
        event.xclient.window = window
        event.xclient.message_type = self.lib.XInternAtom(
            self.display, b"_NET_ACTIVE_WINDOW", 0
        )
        event.xclient.format = 32
        event.xclient.l[0] = SOURCE_PAGER
        self.lib.XSendEvent(
            self.display,
            self.root,
            0,
            SUBSTRUCTURE_NOTIFY_AND_REDIRECT,
            ctypes.byref(event),
        )
        self.lib.XRaiseWindow(self.display, window)
        self.lib.XFlush(self.display)

    def move(self, window: int, x: int, y: int) -> None:
        """Move a window's top-left corner."""
        self.lib.XMoveWindow(self.display, window, x, y)
        self.lib.XFlush(self.display)


def run(*command: str | Path) -> str:
    """Run a command and return its output; failures show up as empty output."""
    return subprocess.run(  # noqa: S603 - fixed commands, no user input
        [str(part) for part in command], capture_output=True, text=True, check=False
    ).stdout


def find_windows() -> tuple[int, int] | None:
    """Return the device and toolbar window ids once both exist."""
    listing = run("xprop", "-root", "_NET_CLIENT_LIST")
    ids = listing.partition("#")[2].split(",")
    names = {}
    for wid in filter(None, map(str.strip, ids)):
        name = run("xprop", "-id", wid, "_NET_WM_NAME").partition("=")[2]
        names[name.strip().strip('"')] = int(wid, 16)
    if DEVICE_TITLE in names and TOOLBAR_TITLE in names:
        return names[DEVICE_TITLE], names[TOOLBAR_TITLE]
    return None


def running() -> bool:
    """Tell whether adb lists the emulator as a ready device."""
    lines = run(ADB, "devices").splitlines()
    return any(line.split() == [SERIAL, "device"] for line in lines)


def booted() -> bool:
    """Tell whether Android has finished booting."""
    return (
        run(ADB, "-s", SERIAL, "shell", "getprop", "sys.boot_completed").strip() == "1"
    )


def start() -> None:
    """Start the emulator detached from this process, logging into the temp dir."""
    log = Path(tempfile.gettempdir()) / f"emulator-{AVD}.log"
    with log.open("w") as out:
        subprocess.Popen(  # noqa: S603 - fixed command
            [EMULATOR, "-avd", AVD, "-no-snapshot-save", "-no-audio", "-no-boot-anim"],
            stdout=out,
            stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL,
            start_new_session=True,
        )
    print(f"started {AVD}, log {log}")


def wait_for[T](what: str, check: Callable[[], T | None], timeout: int) -> T:
    """Poll once a second until check returns something truthy, or exit."""
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        if result := check():
            return result
        time.sleep(1)
    sys.exit(f"timed out after {timeout}s waiting for {what}")


def place(x11: X11, device: int, toolbar: int) -> None:
    """Move the device left until the toolbar fits right of it on the screen."""
    screen = x11.geometry(x11.root).width
    dev = x11.geometry(device)
    target = min(dev.x, screen - dev.width - GAP - x11.geometry(toolbar).width)
    if target < dev.x or x11.geometry(toolbar).x < dev.right:
        x11.move(device, max(target, 0), dev.y)
        time.sleep(1)  # the emulator moves its toolbar after the device


def main() -> None:
    """Start, place and raise the emulator, then wait for it to boot."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--no-boot-wait", action="store_true", help="return once the windows are placed"
    )
    args = parser.parse_args()

    x11 = X11()
    if not running():
        start()
    device, toolbar = wait_for("the emulator windows", find_windows, WINDOW_TIMEOUT)
    place(x11, device, toolbar)
    x11.activate(device)
    x11.activate(toolbar)
    dev, bar = x11.geometry(device), x11.geometry(toolbar)
    print(f"device  {dev}\ntoolbar {bar}")
    if bar.x < dev.right:
        sys.exit("toolbar still covers the device")
    if not args.no_boot_wait:
        wait_for("boot", booted, BOOT_TIMEOUT)
        print(f"{SERIAL} booted")


if __name__ == "__main__":
    main()
```
