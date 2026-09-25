---
title: "The Agent Taps for Itself: Android Apps with adb and the Emulator"
date: 2026-09-25T10:55:00+02:00
tags: ["claude-code", "android", "emulator", "tooling", "workflow", "Field Notes"]
topics: ["thinking"]
summary: "One sentence per wish, and the agent builds, installs, taps and looks at the result itself. On the phone and in the emulator, the loop closes that hangs on my hand with firmware. Where things caught was at the edges: a push, a heading in the changelog and a window."
---

## In short

- For an Android app, the device on the cable is screen, input and test bench at once.
  Claude Code builds with Gradle, installs, taps through `adb` and looks at the result itself.
- One morning, seven sentences from me turned into a theme, an app icon, a help page, an imprint and a release.
- Where nobody needs to look at the phone, the emulator takes over.
  There it doesn't even need my finger for the screen lock.
- Things never caught in the code, only at the edges: a push, a heading in the changelog and a window covering another.
  For the window, the tool is at the end of this post.

## Seven sentences one morning

The TeeToTum app is the companion app to a rotary knob with a round display.
It is written in Kotlin with Compose Multiplatform and so far runs only on Android.
Version 0.1.0 was one day old when I sat down at the computer at about a quarter to six in the morning.
A little over forty minutes later, 0.2.0 was released.

In between were seven wishes, each one sentence in German:

- A third theme matching the red theme on the knob, including light mode.
- All icons in the colour of the selection dots.
- Menu entries with the same rounding as the buttons, and an app icon like the knob's favicon.
- Slightly larger text on the buttons.
- A help page.
- An imprint.
- Commit, push, uninstall the app and install it again from the repo.

The theme comes from a Rust constant in the firmware.
Claude translated it into a Material colour scheme and checked the contrasts.
White on the knob's red, `#F0283A`, comes to 4.2:1, below the 4.5:1 recommended for text.
So the text on the buttons became almost black.
There is no light version on the knob; it is derived: a darker red, `#C41E2E`, on white.

The app icon isn't redrawn.
A small Python script reads the favicon's SVG and writes a vector drawable with 14 paths from it.
On the home screen, the icon looks like the knob itself.

## The loop on the device

The phone was connected over USB.
After every wish the same loop ran: `./gradlew installDebug`, then `adb` starts the app.
`uiautomator dump` returns the tree of the visible interface with the coordinates of every text, `input tap` taps on it, `screencap` takes a picture.
Before every tap, Claude checked that the app was still in front.

It put the screenshots together into montages, scaled down to 30 %, dark and light side by side.
It switched with `cmd uimode night yes` and set it back afterwards.
In these pictures it found two things by itself:
a double space in the help, which came from a line break in a Kotlin string,
and that the link in the imprint really opens the browser.
The first tap missed, the second one didn't.

Two wishes became tests.
"All icons in this colour" became a function `AppIcon` and a test that reports every call to Material's `Icon(` outside that function.
"The same rounding" became a shared constant.
That way a wish stays fulfilled for the next button too, without my repeating it.

Claude asked back exactly once that morning, and the question was fair.
"Install from the repo" could mean: build from a fresh clone, take the old release or cut a new one.
I clicked the new release.
After that it went in one go: version 0.2.0, tag, CI builds and signs in 2 minutes 40 seconds, download the APK, compare the checksum, `adb install`.

## The emulator, when nobody needs to look

On the phone I watch when I want to, and sometimes I have to.
Much of it doesn't need that: whether a form saves, whether a list filters, whether a notice appears.

So in a second project, a rebuild of an older Android app, there has been a rule since 24 September:
whatever can be checked without my hand and without my eyes, Claude checks in the emulator.
The phone stays for what I'm meant to see myself, and for text in a real font.

The tools are the same.
To `adb`, the emulator is a device like any other, with its own serial number.

One difference concerns the screen lock.
The app encrypts single fields with a key that Android ties to the device's lock.
Without a lock the key expires, and the test data with it.
On the phone I confirm each prompt with my finger.
In the emulator, a script sets a test PIN and types it in itself.

## What caught at the edges

**The push.**
Before pushing, Claude checked only its own changes for anything private, not everything since the last push.
Three older commits went out unchecked.
The check came afterwards and found nothing, but it came in the wrong order.

**The changelog.**
The release carries an empty heading "Unreleased", and the app shows its own changelog.
That was noticed only after the tag.

**The window.**
Without a window the emulator crashed on my computer, so it runs with one.
Under GNOME on Wayland it consists of two windows: the device and a narrow toolbar, which it places to the right.
If the device sits at the right edge of the screen, GNOME pushes the toolbar into the device.
It can't be hidden; `emulator -help` knows no switch for it.

I like watching the emulator, and for that the device has to be uncovered.
So I asked Claude for a tool that starts the emulator if it isn't running, brings both windows to the front and moves the device far enough left for the toolbar to fit beside it.
`xdotool` and `wmctrl` weren't installed.
So the script talks to the X11 library directly through Python's `ctypes`; under Wayland the emulator runs as an X11 program.

Claude tested it in three cases: position already right, toolbar deliberately pushed into the device, emulator stopped and cold-started.
The cold start took 18 seconds to a finished boot.

The first version worked, but a linter with every rule enabled found 60 issues.
The X11 connection opened on import, arguments were read from `sys.argv` by hand, types were missing.
The version below passes Ruff with all rules and mypy in strict mode.
For a helper script that's more than needed, but it's the same check as for the app's code.

## What I take from it

- A device the agent can operate itself saves me the round in which I look and describe what I see.
- What I want to see, I look at on the phone.
  What only needs checking runs in the emulator.
- A wish recorded as a test doesn't need repeating.
- What still catches lies in the process around the code, so that's where the checks belong: before the push, before the tag, before the window.

## The tool

`tools/emulator.py` starts one particular virtual device, brings it to the front and puts the toolbar beside the device.
The device name, serial number and SDK path sit at the top as constants.
It needs Python 3.12 or later, `xprop` and an X11 session or XWayland.

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
