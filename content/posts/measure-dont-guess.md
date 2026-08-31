---
title: "Measure, Don't Guess: Debugging a Laptop Speaker With Claude Code"
date: 2026-08-31T06:00:00+02:00
draft: false
tags: ["claude-code", "linux", "hardware", "debugging", "audio"]
summary: "A wrong theory, a public retraction, and a small measurement tool — what I learned about using AI assistance for problems that aren't about code at all."
---

## TL;DR

- My laptop has a speaker that Linux doesn't drive correctly. Someone else had already
  done the deep work; I started from their fix and hit a different problem on my unit.
- I formed a theory by listening, published it, and it was **wrong**.
- Instead of arguing about what we heard, Claude Code and I built a small measuring
  instrument out of the laptop's own microphone. It contradicted my theory within an hour.
- I retracted my published claim and replaced it with measured facts.
- The useful part was not speed. It was that a vague complaint — "this speaker sounds
  wrong" — became something with numbers attached, in an afternoon, without me being a
  hardware engineer.
- I ran the whole thing in a mode where I approved the plan before anything executed. The
  control is explicit, which is exactly why the common security worry deserves a calmer look.

---

## Starting from someone else's work

The laptop is a Chuwi CoreBook X. On Linux, its left speaker is silent out of the box. The
chip driving it — an AWINIC AW88298 amplifier, hanging off an undocumented output on the
audio codec — has no mainline Linux driver.

I did not solve that. **Francisco Montañés García ([@pacomont](https://github.com/pacomont))
did**, across roughly five weeks of genuinely hard work: probing the chip over I2C, proving
which part of the system was feeding it audio, and eventually finding why every notification
sound started with a glitch. His project log is
[worth reading on its own](https://github.com/pacomont/chuwi-corebook-x-left-speaker), and
everything below sits on top of it. I installed his daemon and both speakers worked.

Then I noticed something on my machine that his notes didn't describe, and that is where my
part starts.

## A theory built out of listening

Audio came out of the left edge of the laptop, and also from somewhere near the right. That
suggested a **third** speaker — a middle one — that his fix was accidentally silencing.

I tested it the obvious way: play sound, mute one output at a time, note what I heard. The
results looked consistent. I wrote it up and filed it as an issue on the upstream project,
proposing a change so other owners could get their middle speaker back.

The problem is that I had built a conclusion out of my ears, and I had no idea how weak an
instrument that is.

## Ears are not a measuring device

When we tried to nail the behaviour down precisely, the results stopped agreeing with each
other. One test run through six configurations produced this from me:

> silence, right, silence, right, silence, silence, right

Run it again, and it came out differently. Two of the speakers sit close together on the
mainboard, so "which side is that coming from" is a question my hearing genuinely could not
answer. Every run gave a confident-feeling answer, and the confident answers disagreed.

Claude Code called this out rather than continuing to collect my reports:

> The ear reports are contradicting each other across runs. Let me stop relying on that.

That sentence is the whole post, really. The failure wasn't a lack of effort. It was that
we were measuring with the wrong instrument, and no amount of careful listening was going to
fix that.

## Building an instrument instead

The first alternative was direct: record the laptop's own microphones while each channel
plays, and compare levels. That nearly worked, but the microphone noise floor swamped the
quiet speaker.

So the approach sharpened. Rather than measuring loudness in general, measure the *specific
tone* being played and ignore everything else — a Goertzel filter, which locks onto one
frequency and rejects the rest. Two frequencies were used: 1 kHz to gauge level, and 6 kHz to
ask a different question entirely — *can this speaker even produce high frequencies?*

A note on how ordinary this was: numpy wasn't working in that environment, so the analysis
was written in plain Python instead. No lab equipment. A laptop microphone, a test tone, and
about forty lines of arithmetic.

The results were immediately more useful than anything I had heard:

| Playing | Level at 1 kHz | Anything at 6 kHz? |
|---|---|---|
| Right channel | +60 dB over baseline | Yes |
| Left channel | +15 dB over baseline | **Nothing** |

A 45 dB gap, and one output that produced no treble at all. That is not a stereo pair. That
is a full-range speaker and a woofer.

## The part where I put my finger on it

One question remained: *where* is that quiet, dull speaker physically located? The microphone
array's stereo separation was too poor to say.

Rather than fight that, Claude Code proposed a method that doesn't require locating anything:

> You block one opening at a time while the mic measures the level drop. That identifies the
> source objectively; you only have to place a finger.

So I sat there sealing speaker slots with a fingertip while a tone played and a script
recorded the difference. It felt faintly ridiculous. It also worked, because a covered
speaker gets measurably quieter and the microphone doesn't have opinions.

I want to highlight this specific progression, because it's the thing I found genuinely
impressive — not any single clever step, but the *direction of travel*:

1. **"Tell me what you hear."** — unreliable, and we found that out.
2. **"Cover this opening with your hand."** — crude, but objective.
3. **"Here's a tone-locked analyzer; the microphone reads the answer."** — repeatable, with numbers.

Each step made me less central to the measurement. That is what progress looks like on a
problem like this, and I would not have got there alone.

## Being wrong in public, then fixing it

The measurements said there is no middle speaker. The quiet output is a woofer under the
chassis. And the specific setting my proposed fix relied on turned out to do nothing at all on
this codec.

My published issue was wrong, and worse, following it would have degraded other people's
audio. So I retracted it — a warning banner at the top, the original text left visible
underneath, and the measured findings in its place.

I'd rather have been right. But I'd much rather be corrected by a measurement in an afternoon
than by a stranger's bug report in six months.

## The pause is part of the method

There's a usage limit in Claude Code that rolls over on a five-hour window. Hitting it sounds
like pure friction. In practice it was one of the more useful things that happened.

The problem stopped being available to poke at, so I stopped poking and started thinking. I
came back to the next session with a specific new idea rather than another variation on the
last thing I tried.

This matters because tools that answer instantly encourage you to keep asking instead of
keep thinking. A forced gap turns out to be a reasonable feature for a problem you don't yet
understand — and unlike a human collaborator, the session picks up exactly where it left off,
with the full context intact. Nothing had to be re-explained.

## On control, calmly

The hesitation I hear most often is some version of: *I'm not letting an AI run commands on
my computer.* That concern deserves a straight answer rather than reassurance.

I had three worries going in: it would need administrator access, it might break something
irreversibly, and I wasn't sure what left the machine.

What resolved them wasn't trust. It was that the control is explicit and adjustable. I worked
in **plan mode**: Claude Code lays out what it intends to do and why, and nothing executes
until I approve it. For the routine steps that's a formality. For the ones touching hardware
registers with administrator rights, I read them properly. I could tighten or loosen that at
any point, and I could stop.

Here's the moment that did the most for my confidence, though — and it isn't a reassuring one.
Late in the session, the left speaker went silent and didn't come back. Unprompted, Claude
Code wrote this:

> I should be straight about my part: to get measurable levels I ran the path at its calibrated
> maximum with sustained full-scale sine tones, which is louder and harsher than your normal
> use, so I can't rule that out as a contributor.

It then laid out the evidence pointing the other way — the amplifier reported no over-current,
over-temperature or clipping faults. (After a reboot the speaker came back, and it's been
stable since.)

An assistant that flags its own possible contribution to a problem is more useful than one that
never worries you. I'd call the fear of *losing control* unfounded, because control is a setting
you choose. The risks themselves are real, manageable, and worth reading the plan for.

## Lessons learned

1. **A confident impression is not evidence.** My ears gave a different answer each run and
   felt certain every time.
2. **Ask what you can measure before deciding what to change.** Days of theorising lost to an
   afternoon of measurement.
3. **The instrument can be improvised.** A built-in microphone, a test tone and plain Python
   replaced equipment I don't own.
4. **Publishing a wrong conclusion is recoverable.** Retracting it clearly costs less than
   leaving it up.
5. **Step away on purpose.** The break produced the idea; the screen time produced variations.
6. **Approve the plan, not just the outcome.** Reading what will happen before it happens is
   where the control actually lives.

## If you're on the fence

You do not need to be a developer for this. I could not have written that analyzer, and I
didn't need to — I needed to describe a symptom accurately, run what I was asked to run,
and put my finger over a speaker hole when that turned out to be the best available
instrument.

If you have a device with something quietly broken on it — a speaker, a sensor, a fan that
never spins, some feature that silently stopped working — the honest situation is that these
problems are usually *solvable* and just not worth anyone's time to solve. That calculation
has changed. Not because the assistance is infallible; mine helped me build a theory that
turned out to be wrong. It changed because the loop from "something's off" to "here are the
numbers" got short enough to be worth walking.

Start with the symptom. Ask what could be measured. Read the plan before you approve it.
