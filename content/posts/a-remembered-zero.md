---
title: "Silence Without an Error: The Zero My Sound Server Remembered"
date: 2026-09-02T16:40:00+02:00
draft: false
tags: ["claude-code", "linux", "audio", "pipewire", "debugging", "chuwi"]
summary: "The speaker test in my system settings played nothing while music and video were fine. The cause was not a broken driver but a single number my sound server had faithfully remembered — left over from the debugging session I wrote about last time."
---

Last time I wrote about [measuring instead of guessing](/posts/measure-dont-guess/),
a story about the speakers in this laptop and about being wrong in public and correcting it.
This is a short postscript to it.
Three days after that work was finished, the same laptop produced a new symptom — and it turned out to be a leftover from the debugging itself,
not from the hardware and not from the fix.

## TL;DR

- In Settings → Sound, the **Test speakers** dialog played nothing.
  Chrome, music and video were perfectly fine.
- Every layer reported success.
  The sound file was found, the stream was created, playback finished without an error. It was just inaudible.
- The cause was one line in a state file: my sound server had **remembered a volume of zero** for exactly the kind of stream that dialog creates.
- My first theory about how it got there was wrong, and a measurement said so within a minute.
  The eventual answer is honest but partial: I can reproduce the mechanism, not the exact original write.
- The repair took one command.
  Finding out *what* to repair took the rest.

## A success message and no sound

Fedora 44, GNOME 50, PipeWire.
Two little speaker icons in the sound settings, one per side; clicking either is supposed to play a short test tone into that speaker.
Nothing came out of either.
Everything else on the machine played audio normally, which rules out the obvious half of the problem space immediately.

What made this awkward is that nothing anywhere reported a failure.
The desktop plays these sounds through a small library that looks up a named sound in a theme and hands it to the audio server.
That library found the file, created the stream, played it to the end and returned success.
There was no error message to search for.

That is the uncomfortable class of bug: not "it broke", but "it did exactly what it said and nothing happened".

## Measuring instead of trusting the return code

The useful move here was to stop reading return codes and record what actually left the machine.
The audio server can be asked to hand you a copy of everything a given output is playing.
So: start recording, play the test sound, then look at the peak level of the recording.

Same sound file, two different players:

| how it was played | peak left | peak right |
|---|---|---|
| a plain audio player | 4301 | 4301 |
| the desktop's sound library, the way the settings panel calls it | 0 | 0 |

Exactly zero, not "quiet".
The file was fine, the device was fine, and the difference had to be something about *how* the desktop asked for it.

Looking at the live stream while it played gave the answer in one line:

```
media.role = "test"
Mute: no
Volume: mono: 0 / 0% / -inf dB
```

Not muted. Turned all the way down.

## What the sound server had written down

Audio servers remember per-application volumes so that the video player you turned down last week is still turned down today.
That memory lives in a plain text file, and it had this in it:

```
Output/Audio:media.role:Test={"channelMap":["FL"], "volume":1.0, "mute":false, "channelVolumes":[0.000000]}
```

The speaker test labels its audio with the role `test`.
That label had a stored volume of zero, and it had been applied faithfully every single time.
The neighbouring entries — `Music`, `Movie`, the browsers, the video player — were all at 1.0,
which is precisely why everything else sounded normal and only this one dialog was mute.

Nothing was broken.
A setting had been recorded once and honoured ever since.

## Did my own fix cause this?

That was my first question, because the previous post's work ended with a change to exactly this part of the system:
moving volume and balance out of the sound chip and into software, so that each channel's gain reaches its own speaker.

The honest answer has three parts.

**The fix itself cannot do this.** It is a one-line rule that changes a property of the *sound card*.
The zero sits on a *stream*, in a different mechanism entirely.
I tested the obvious bridge between them — driving the balance to its extreme and then running the speaker test — and checked whether that writes anything into the stored entry.
It does not. Hypothesis dead, one minute, no argument.

**The debugging around the fix is the plausible origin.** That whole session consisted of pushing the balance to both extremes
and then using *this very dialog* to work out which speaker was still playing.
I could reproduce the mechanism directly: give a `test` stream a channel volume of zero once, and the server stores it and hands it to every later test stream.
The next one comes up at `0 / 0% / -inf dB` on its own.

**What I cannot claim** is the exact original write.
Reproducing that would mean restoring the pre-fix state of the machine, which no longer exists here.
So: mechanism reproduced, specific event inferred.
I would rather write that sentence than a cleaner one that claims more than I measured.

There is a fourth part, and it is the one I find interesting.
The fix worked — that is *why* this stayed hidden for three days.
Everything the fix was responsible for came out right, so nothing pointed back at that session,
and the one stale number it could never have cleaned up sat there being obeyed.

## The repair

There is no settings dialog for this, but there is a supported path:
the value is stored when a stream's volume changes, so you make a stream with that label, set it back to 100 %, and let the server write it down.

```bash
# hold a stream open with the role the speaker test uses
paplay --property=media.role=test silence.wav &
# find it, and set it back to full
pactl set-sink-input-volume "$ID" 100%
```

Verified the same way it was diagnosed — record the output, play the test, read the peaks:

| test | peak left | peak right |
|---|---|---|
| left speaker | 4301 | 0 |
| right speaker | 0 | 4301 |

Each side plays on its own side, at the same level as the reference.
No restart, no logout.

## A second silence, with a different cause

While chasing this I ran into a second mute, and nearly filed it under the same heading.
A command-line tool refused to play the same sounds with `Sound disabled`.
Different reason entirely: system event sounds were simply switched off in the desktop settings, a deliberate on/off toggle that the speaker test does not go through.

Two silences, one panel, unrelated causes.
Turning the event sounds back on was one setting — and revealed a third small thing:
notification sounds were stored at 90.48 % rather than 100 %.
Setting that to full and re-measuring gave a level ratio of 1.1052 against the predicted 1 / 0.904817 = 1.1052.
Four digits is more agreement than the question deserved, but it is a nice way to be sure you changed the thing you meant to change.

## Lessons learned

- **"Success" is a claim about the code path, not about the world.**
  Every layer here returned success while producing silence. The recording was the only thing that could tell the difference.
- **Prefer a measurement that can embarrass you.** My causal theory was tidy and wrong.
  It cost a minute to find that out, and I would have written a confidently incorrect explanation otherwise.
- **A working fix and a clean system are not the same thing.**
  Debugging leaves sediment. The tools you use to investigate a problem have memories of their own,
  and they do not get rolled back when the actual repair lands.
- **State that persists silently deserves suspicion.** "It remembers your settings" is a feature right up to the moment
  it remembers something you never meant to keep, and then there is no error message anywhere, because nothing failed.
- **Partial answers are allowed.** "I reproduced the mechanism but not the specific event" is a real result.
  Rounding it up to a clean causal story would have been the only dishonest thing in this whole exercise.

## What transfers

None of this required deep audio knowledge going in.
It required refusing to accept a success message, and knowing that you can record what a machine is actually playing and just look at the numbers.
That is a general move, and it works far outside sound: when something claims it worked and reality disagrees,
find the place where you can observe the result directly rather than reading the report.

The fix was one command.
The three days of silence were the price of not having asked, once, what the machine was actually emitting.
