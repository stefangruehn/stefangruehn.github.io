---
title: "The Frozen Fader: 23 Decibels Nobody Corrects Any More"
date: 2026-09-03T12:20:00+02:00
draft: false
tags: ["claude-code", "linux", "audio", "alsa", "pipewire", "wireplumber", "systemd", "debugging", "chuwi", "Technical Deep Dive"]
series: ["Reverberations"]
summary: "After a reboot every audio source was 23 dB too quiet. The cause was an ALSA control that nobody has touched since an earlier fix — and the repair failed the first time because this laptop's card names swap places between boots."
---

Part one of this series found a [hardware problem](/posts/measure-dont-guess/) and fixed it.
Part two found what the [debugging had left behind](/posts/a-remembered-zero/) — a remembered zero.
This is what the *fix* left behind.

## TL;DR

- After a reboot everything was too quiet: YouTube, music player, system sounds.
  No application spared, so not a per-stream problem like part two.
- The ALSA control `Master` sat at **-23 dB**, and since the soft-mixer fix from part one nobody touches it any more.
  WirePlumber no longer tracks it, because it is no longer *supposed* to.
- The target value was measured, not calculated.
  Nominal and acoustic differ by 3 dB, and the arithmetic would have pointed at a different control.
- The first repair did **not** survive its test reboot.
  Both HDA controllers in this laptop are called `HD-Audio Generic`, and the ALSA names swap places between boots.
  `asound.state` is keyed by name, and so was my systemd unit — both landed on the wrong card.
- The second version resolves the card by PCI address and waits for it to be enumerated.
  That the wait loop is genuinely needed is recorded nowhere as an error.
  It is recorded in one second between two log lines.

## Uniformly too quiet

Fedora 44, GNOME 50, PipeWire 1.6.8, a Chuwi CoreBook X with a Conexant SN6180.

The symptom was dull this time, and instructive for exactly that reason: after a reboot everything was simply too quiet.
Browser, music player, system sounds, the same loss in every application.
That uniformity rules out what caused part two.
A remembered stream volume hits one role and leaves the rest alone.
Whatever attenuates every source equally sits behind the mixer, not in front of it.

The slider in the GNOME sound settings was at maximum, and the sink dutifully reported that all was well:

```
Volume: front-left: 65536 / 100% / 0.00 dB,   front-right: 65536 / 100% / 0.00 dB
Base Volume: 65536 / 100% / 0.00 dB
Mute: no
```

Zero attenuation, not muted, full level.
The hardware underneath told a different story:

```
$ amixer -c1 sget Master
  Limits: Playback 0 - 74
  Mono: Playback 51 [69%] [-23.00dB] [on]
```

Twenty-three decibels.
The control PipeWire displays and the control that actually attenuates had nothing left to do with each other.

## Switch off the mixer and you freeze it

That is not a coincidence but the aftermath of the fix from part one.
That fix moved volume and balance out of the sound chip and into software, so that each channel's gain arrives at its own speaker:

```
# ~/.config/wireplumber/wireplumber.conf.d/51-chuwi-corebook-x-soft-mixer.conf
api.alsa.soft-mixer = true
```

With that, PipeWire applies volume and balance to the samples and leaves the ALSA controls alone.
It was the right call, it still works, and it has exactly one consequence I had not thought about:
if WirePlumber stops touching the control, *nobody* touches it.

Before, `Master` was part of a control loop.
The desktop slider moved it, `alsactl` saved it at shutdown, the next boot restored it.
Any value that drifted in got corrected the next time round.
After the change, nothing drifts in.
Whatever stood there at that moment stands there forever, and it comes back at every boot.

Whether -23 dB is the slider position from before the fix or simply the value the codec settles on, I cannot tell apart.
`alsactl init` puts the control at 54 rather than 51 on a running system, which argues against a plain driver default but proves nothing.
Telling the two apart would need the machine's state from before the fix, and that no longer exists here.
For the symptom it makes no difference: the value returns at every boot, and nothing raises it.

The delay is the remarkable part.
While that earlier session was still running, the level was fine — the control was still where WirePlumber had last pushed it.
The fix broke nothing that could have been noticed the same day.
It froze a value, and the bill arrived at the next reboot.

## Measuring the target instead of calculating it

The requirement was precise: what used to require the slider at maximum should from now on be reached at 50 %.

You can calculate that.
PulseAudio and PipeWire map the slider cubically, `dB = 60 · log₁₀(v)`, so 100 % → 50 % is exactly -18.06 dB.
`Master` moves in 1 dB steps, hence 51 + 18 = **69**.

Except a speaker is not an equation.
The measuring rig from part one is still there: play a 1 kHz tone with `paplay`, record the built-in microphone at the same time, then read the band around 1 kHz out of the FFT.
Two minutes of work, and it answers the question the arithmetic only asserts.

| `Master` | Slider | 1 kHz, mean | n | sd |
|---|---|---|---|---|
| 51 (-23 dB) | 100 % | -29.95 dB | 6 | 0.09 |
| **69 (-5 dB)** | **50 %** | **-29.96 dB** | 6 | 0.10 |
| 51 (-23 dB) | 50 % | -45.06 dB | 4 | 0.18 |
| 69 (-5 dB) | 100 % | -24.31 dB | 4 | 0.15 |

The first and second rows are **0.01 dB** apart.
That is the whole answer: 69 is right.

The `n` and `sd` columns are there because I owed them to myself.
Two single readings of the same setting had landed two decibels low shortly before, and five in a row scattered by 1.3 dB.
One measurement from this rig simply does not answer the question "are these two equally loud".
Only interleaved — A, B, A, B, six times each, so that slow drift hits both sides alike — does the scatter drop to 0.1 dB, and only then does the comparison hold.
The first attempt had happened to produce the same number twice and let me mistake that for precision.

The intermediate numbers are not.
The slider from 100 % to 50 % costs **15.11 dB** acoustically; the mixer from 51 to 69 delivers **15.10 dB** — nominally both would be 18.06.
The curve is compressed by the same amount on both paths, and *that* is why it cancels.
Had the compression appeared on only one side, the arithmetic would have pointed at a different control.
Towards the top it gets starker: from 50 % to 100 % at `Master` 69 there are only **5.6 dB** of headroom left, not the nominal 18.
The amplifier or the speaker limits there, and no datasheet figure predicts it.

## Two cards, one name

The rest should have been routine: set the value at every login, done.

```ini
# ~/.config/systemd/user/chuwi-master-volume.service
[Service]
Type=oneshot
ExecStart=/usr/bin/amixer -c Generic -q sset Master 69
```

Card by name rather than by index, with a comment above it explaining that indices can move between boots.
Plus `alsactl store`, so the value is recorded system-wide as well.

The test reboot refuted all of it.
Afterwards `Master` was back at 51, and here a single measurement was enough: -45.1 dB at 50 %, fifteen decibels below target.
The machine was exactly where it had been.

Both HDA controllers in this device announce themselves as `HD-Audio Generic`, and ALSA assigns the IDs in probe order:

| Boot | analog, `0000:03:00.6` | HDMI, `0000:03:00.1` |
|---|---|---|
| 11:27 | card1, id `Generic` | card0, id `Generic_1` |
| 11:53 | card1, id `Generic_1` | card0, id `Generic` |

The index stayed. The name moved.
I had picked the name because I considered the index to be the shaky half.

That takes down the second safeguard too, for the same reason:
`asound.state` is organised by card **name**, in sections `state.Generic` and `state.Generic_1`.
The stored 69 sat under `state.Generic` and, after the swap, was applied to the HDMI card, which has no `Master` at all.
Running `alsactl store` again does not repair this, it only moves the problem:
the section belonging to the other name gets overwritten with whatever currently runs under it.
After the next clean shutdown the 69 sits under `Generic_1` — and at the next name swap the restore misses again.

On a machine with two identically named cards, `asound.state` is not a usable home for a particular control.

## The PCI address is the only stable thing

What does not move is the address on the bus.
So stop asking what the card is called and ask which card hangs off `0000:03:00.6`:

```bash
for d in /sys/class/sound/card*; do
    [ -e "$d/device" ] || continue
    [ "$(basename "$(readlink -f "$d/device")")" = "$PCI" ] || continue
    idx=${d##*/card}
    amixer -c "$idx" sget Master >/dev/null 2>&1 || continue
    amixer -c "$idx" -q sset Master "$LEVEL"
    exit 0
done
```

All of it inside a loop that retries once a second for up to thirty seconds, and the unit now calls nothing but this script.

## One second in the journal

The wait loop was an aside while writing.
Two lines, added from the memory of an error message, with no evidence that they were needed.

The second test reboot held: unit ran cleanly, two measurements at 50 % landing at -30.2 and -30.3 dB, inside the reference range.
The interesting part is not the result but how it came about:

```
12:01:50.304347  Starting chuwi-master-volume.service...
12:01:51.335420  Finished chuwi-master-volume.service.
```

One thousand and thirty-one milliseconds for a single `amixer sset`.
Scanning the cards takes milliseconds — the second is the `sleep 1` between a failed pass and a successful one.
At login the analog card is not yet enumerated.
Without the loop this version would have failed too.

And that finally makes the first attempt's error message readable.
It said:

```
amixer[3682]: Invalid card number 'Generic'.
```

I had taken it as evidence of the name swap — the name was right there in it.
It is nothing of the sort.
At that moment card0 really was called `Generic`; the card existed, it was merely the wrong one.
Because this is what the name error actually sounds like, checked on the same machine:

```
$ amixer -c Generic sget Master
amixer: Unable to find simple control 'Master',0
```

`Invalid card number` means something else: no card of that name existed yet.
The message was reporting the timing.
I found the name swap independently, in `/sys/class/sound` and in the section headers of `asound.state`.

Two defects in a single `ExecStart` line, and they masked each other.
Fixing only the name would not have been enough, because the card is still missing at login.
Fixing only the timing would not have been either, because the level would then have landed on the HDMI card.

## What I learned

- **Switch a component off and you freeze its state.**
  "Nobody touches this any more" also means "nobody corrects this any more".
  The soft mixer was right and has stayed right — the value it froze was never something it could clean up.
  Disabling a control loop comes with the question of who owns the last value from then on.
- **An error message names *a* fault, not *the* fault.**
  `Invalid card number 'Generic'` contained the very word my theory pointed at, and it was reporting something else.
  Finding your own hypothesis in the text of a message is recognition, not confirmation.
  The counter-check cost one command: look at what the suspected fault actually sounds like.
- **Casual caution can be load-bearing, and only the timestamp shows it.**
  The wait loop was an aside while writing and is the reason the thing works.
  The result does not reveal that: the unit reports `Finished` with or without the loop.
  A green run tells you that it worked, not how narrowly.

## Where I'd start

If everything on your machine is uniformly too quiet and the desktop slider is already at maximum, in this order:

1. **Look at the hardware mixer directly**, not at the sink.
   `amixer -c<n> scontents` shows what actually attenuates; `pactl list sinks` shows only what PipeWire believes.
   If the two disagree, the question is no longer "how loud" but "who writes in there".
2. **Check whether anyone still writes in there at all.**
   With `api.alsa.soft-mixer = true` the answer is: nobody.
   The same holds for any UCM profile or rule that takes a control out of management.
3. **Count how many cards share a name.**
   `cat /proc/asound/cards` next to `readlink -f /sys/class/sound/card*/device`.
   If two names are interchangeable, every name-based configuration — yours and `asound.state` alike — is a bet on probe order.
4. **Measure the target value, don't compute it.**
   A tone, the built-in microphone and an FFT are enough.
   The curve between slider and sound pressure is not the one in the datasheet, least of all at the ends.
5. **Reboot before you call it done.**
   The simulated test — turn the value back, restart the unit — was green both times, including for the version that did not survive the reboot.

The fix is three lines in a shell script.
The two reboots before it cost more and showed more.
