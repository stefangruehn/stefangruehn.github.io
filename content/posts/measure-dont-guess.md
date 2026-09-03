---
title: "Measure, Don't Guess: Debugging a Laptop Speaker With Claude Code"
date: 2026-08-31T06:00:00+02:00
draft: false
tags: ["claude-code", "linux", "hardware", "debugging", "audio", "chuwi", "nerd fodder", "technical deep dive"]
series: ["Reverberations"]
summary: "A wrong theory, a public retraction, and a small measurement tool — what I learned about using AI assistance for problems that aren't about code at all."
---

*Postscript, added 2026-09-02:* this story has a footnote.
Three days after the speakers were working, the speaker test in my own sound settings went silent —
and the cause turned out to be a leftover from this very debugging session, not from the hardware and not from the fix.
I wrote that up separately: [Silence Without an Error](/posts/a-remembered-zero/).

## TL;DR

- My laptop has a speaker that Linux doesn't drive correctly.
  Someone else had already done the deep work;
  I started from their fix and, in the process, hit a further problem on my unit.
- I formed a first theory by listening, published it, and it was **wrong**.
- Instead of arguing about what we heard, Claude Code and I built a small measuring instrument out of the laptop's own microphone.
  It disproved my first theory about the problem within an hour.
- I retracted my published claim and replaced it with measured facts.
- The most useful part was not speed.
  It was that a vague complaint — "this speaker sounds wrong" — became something solid, with numbers attached, in an afternoon, without me being a hardware engineer in a measurement lab.
- I ran the whole thing in a safe mode where I approved the plan before anything executed locally.
  The control is explicit, which is exactly why a common worry about agentic AI deserves a calmer look.

---

## Starting from someone else's work

The laptop is a Chuwi CoreBook X.
On Linux, its left speaker is silent out of the box.
The chip driving it — an AWINIC AW88298 amplifier, hanging off an undocumented output on the audio codec — has no mainline Linux driver.

I did not solve that.
**Francisco Montañés García ([@pacomont](https://github.com/pacomont)) did**, across roughly five weeks of genuinely hard work: probing the chip over I2C, proving which part of the system was feeding it audio, and eventually finding why every notification sound started with a glitch.
His project log is [worth reading on its own](https://github.com/pacomont/chuwi-corebook-x-left-speaker), and everything below sits on top of it.

I installed his daemon and both speakers worked.
Then, though, I noticed something on my machine that his notes didn't describe — and that is where my contribution to the topic starts.

## A theory built by listening

To me, audio came clearly out of the front left edge of the laptop, and also from somewhere at the lower right, towards the back.
That suggested a **third**, full-range speaker — one his fix was using instead of the front right speaker.

I tested it the obvious way: play sound, mute one output at a time, note what I heard.
The results looked consistent.
I wrote it up and filed it as an issue on the upstream project, proposing a change so other owners could get their third speaker back.

The problem is that I had built a conclusion "with my ears", and I had no idea how weak an instrument that is.

## Ears are not a measuring device

When Claude and I later tried to nail the behaviour down more precisely, the results stopped agreeing with each other.
One test run through six configurations produced this from me:

> silence, right, silence, right, silence, silence, right

Run it again, and it came out differently.
Two of the speakers sit close together on the mainboard, so "where is that coming from" is a question my hearing genuinely could not answer.
Every run gave an answer that felt certain to me, but the seemingly certain answers contradicted each other.

Claude Code called this out rather than continuing to collect my reports:

> The ear reports are contradicting each other across runs.
> Let me stop relying on that.

Our shared failure at that point in the session wasn't down to a lack of effort on my part.
It was rather that we were measuring with the wrong instrument — and no amount of careful listening, or younger ears, would have changed that.

## Building an instrument instead

The next approach was to record the signals from the laptop's built-in microphones while each channel played noise, and compare the levels.
That nearly worked too, but the microphone noise floor swamped the quiet speaker.

So the approach sharpened.
Rather than measuring loudness in general, measure the *specific tone* being played and ignore everything else — a Goertzel filter, which locks onto one frequency and rejects the rest.
Two frequencies were used: 1 kHz to gauge level, and 6 kHz to ask a different question entirely — *can this speaker even produce high frequencies?*

A note on how strikingly flexibly Claude handled this: numpy, a Python library for signal analysis, wasn't installed in that environment, so the analysis was simply written in plain Python instead.
No lab equipment needed.
Just a laptop microphone, a test tone, and about forty lines of arithmetic over the measured data.

The results were immediately more useful than anything I thought I had heard:

| Playing | Level at 1 kHz | Anything at 6 kHz? |
|---|---|---|
| Right channel | +60 dB over baseline | Yes |
| Left channel | +15 dB over baseline | **Nothing** |

A 45 dB gap and one output that produced no treble at all.
That is not a stereo pair.
That is a full-range speaker and a woofer.

## The part where I put my finger on it

One question remained: *where* is that quiet, dull speaker physically located in the chassis?
The microphone array's stereo separation was too poor to say.

Rather than fight that, Claude Code proposed a method that doesn't require locating anything:

> You block one opening at a time while the mic measures the level drop.
> That identifies the source objectively; you only have to place a finger.

So I sat there sealing speaker slots with my finger while a tone played and a script recorded the difference.
Incidentally: it felt faintly ridiculous.
It also worked, because a covered speaker gets measurably quieter and a microphone has no opinions of its own.

I want to highlight this specific progression, because it's the thing I found genuinely impressive — not just any single clever step, but the logical *direction* in which our findings developed:

1. **"Tell me what you hear."** — unreliable, and we found that out quickly.
2. **"Cover this opening with your hand."** — crude and hands-on, but objectively measurable by Claude.
3. **"Here's a tone-locked analyzer; the microphone reads the answer."** — repeatable, with numbers.

Each step took me, the biological part of the setup, further out of the measurement.
That is what real progress looks like on a problem like this.
I would not have got that far alone.

## Being wrong in public, then fixing it

Now we knew: there is no third full-range speaker.
The third transducer is a woofer at the underside vent, rear right — 45 dB down and silent at 6 kHz.
That is exactly why it read as "a quiet speaker on the left channel".
And the setting my first upstream-filed fix relied on isn't inert, as I had thought, but harmful:
my observation had only ever watched the front right speaker, and setting it to zero silences the front left speaker completely.

That made the issue I had published upstream wrong, and worse: anyone following it would have degraded their audio.
So I retracted it.
A warning banner at the top, the original text left visible underneath, and the current measured findings added below it as a comment.

I'd rather have been right.
But I'd much rather be corrected by a measurement in an afternoon than by a stranger's bug report in six months.

## The pause is part of the method

There's a usage limit in Claude Code that rolls over on a five-hour window.
Hitting it for the first time felt like slamming on the brakes.
It was, though, one of the best experiences I had in that Claude session.

The problem stopped being available to poke at, so I stopped poking and started thinking.
I came back to the next session with Claude with a specific new idea rather than another variation on the last thing I tried.

This matters because tools that answer instantly can tempt us to keep asking instead of stopping to think first.
That is how we are socially conditioned as humans, and not answering an agentic AI straight away feels odd at first.

A forced break does turn out to be genuinely useful on a problem you don't yet understand — and unlike a human collaborator, the session picks up exactly where it left off, with the full context intact.
Nothing had to be re-explained to Claude.

## Keeping control

A reservation I often hear in connection with agentic AI is some version of: *I'm not letting AI run commands on my computer.*
That concern deserves a straight answer rather than reassurance.

Going into this project I had three worries at first: it would need administrator access, it might break something irreversibly, and I wasn't sure what data left the machine.

What resolved those worries wasn't blind trust in Claude, but that the control is explicit and adjustable.
I worked in **plan mode**: Claude Code lays out what it intends to do and why, and nothing executes until I approve it.
For the routine steps the call is easy, and it can be automated if the same step comes up again later in the session.
For the ones touching hardware registers with administrator rights, though, I read Claude's plan very carefully.
I could tighten or loosen that at any point, and I could stop.

The moment in that session that did the most for my confidence is this one.
Late in the session, the left speaker went very loud, then silent, and didn't come back.
Unprompted, Claude Code wrote this:

> I should be straight about my part: to get measurable levels I ran the path at its calibrated maximum with sustained full-scale sine tones, which is louder and harsher than your normal use, so I can't rule that out as a contributor.

It then laid out the evidence pointing the other way, too — the amplifier reported no over-current, over-temperature or clipping faults.
After a reboot of the machine the speaker was back, incidentally, and it has been stable since.

An assistant that proactively flags its own possible contribution to an acute problem is more useful than one that would rather not worry you and withholds information as a result.
I consider the fear of losing control when running agentic AI locally unfounded.
Control is first of all a question of how you approach the problem, and that is in your own hands.
The technical risks are real but manageable, as long as you read the plan first and then decide.

## Lessons learned

1. **A confident impression is not evidence.**
   My ears gave a different answer each run and felt certain every time.
2. **Ask what you can measure before deciding what to change.**
   Potential days of theorising together, replaced by an afternoon of measuring together.
3. **A measuring instrument can be improvised.**
   A built-in microphone, a test tone and plain Python replaced lab equipment I don't own.
4. **Publishing a wrong conclusion is recoverable.**
   Retracting it clearly costs less in the end than leaving it up in public.
5. **Take deliberate breaks when working with AI.**
   The restful break gave me a new idea, and the screen time afterwards produced new variations of the debugging.
6. **Approve the plan, not just the outcome.**
   Reading what will happen before it happens, and then deciding — that is where the control actually lives.

## Whether this is worth it for you

You do not need to be a developer for this.
I could not have written that tone analyzer in Python as fast as Claude did, and I didn't need to — I only needed to describe a symptom accurately and run what Claude asked me to run.
And to put a finger over a speaker hole when that turned out to be the best instrument available at the time.

If you have a device with something quietly broken on it — a speaker, a sensor, a fan that never spins, some feature that silently stopped working —
the situation is this: these problems are usually *solvable*; it just hasn't been worth anyone's while, so far, to go and solve them.
That calculation has visibly changed.
Not because assistance from agentic AI is infallible.
Mine initially helped me build a theory about the problem that later turned out to be wrong.
The calculation changed because the loop from "something's off" to "here's something solid, with numbers" got short enough to be worth actually walking.
Thanks for that, Claude!

Start with the symptom.
Ask what could be measured.
Read the plan before you approve it.
