---
title: "Who built the chain: material, shape and method"
date: 2026-09-18T10:40:00+02:00
draft: true
tags: ["claude-code", "writing", "self-reference", "reverse-engineering", "authorship", "Essay"]
topics: ["author"]
series: ["Authorship"]
summary: "In “How much of this is really mine” I wrote that the material was mine without exception and the shape was Claude's. The series about an undocumented board is the first case where that split does not hold, because there the method came from Claude as well. What stays with the human then is the question and the judgement, and three obligations."
---

On 6 September a post here laid out a clean division of labour.
[How much of this is really mine](/posts/how-much-of-this-is-mine/) says: the content is mine, the structure is usually Claude's.
Its summary adds a phrase I took for emphasis at the time: **so far without exception**.

The same day, the [Toolchains](/series/toolchains/) series came into being, three posts about forensics on a board with no usable documentation.
It is the first case in which that sentence no longer holds.
The "so far" did its job sooner than I expected.

## Summary

- *How much of this is really mine* splits the work in two: the material is mine, the shape is Claude's.
  The *Toolchains* series is the first case where that does not add up.
- I had hardly any prior knowledge of hardware forensics.
  Without what Claude contributed, there would have been nothing to give shape to.
- The missing third share is **method**: knowing which chain to build to answer a question.
  Register values are in the datasheet, the method is nowhere.
- The old rule *keep the material, give away the shape* still holds, but only under a condition that was invisible until now: that the material is already there.
- Where it is missing, I supply the question and the judgement.
  In exchange I owe three things: checkability, disclosed provenance, and keeping the question and the judgement for myself.
- The old test passes its own exception, and of all things through the sound.
  It proves less than I had credited it with, though.

---

## Where the split stops working

The series covers thirteen chains on a rotary knob with a round screen and two microcontrollers.
Each one is plugged together from tools that exist anyway and ends in exactly one fact.
Which command is missing from the vendor's initialisation table.
Which pins the two processors use to talk to each other.
Which lines the memory card actually uses.

I could not have named a single one of those chains beforehand.
I did know to read out the factory firmware before writing anything of your own to the chip: I had done it once, months earlier, without Claude.
What you do with such an image afterwards, I did not know.
I did not know that the log strings in a firmware image make good anchors, from which you can find the function that prints them.
And it would not have occurred to me to try 840 pin assignments instead of guessing one.

By the arithmetic of *How much of this is really mine*, I should have supplied the material here.
But there was no material before the chains ran.
What the three posts tell is the results of those chains.
Without them the series would have had no subject.

## The third share is called method

The obvious name for the missing share would be knowledge.
That misses it.

What a register of the display driver does is in the datasheet.
What a literal pool is, any introduction to machine code explains.
Which command a memory card expects first is in its specification.
All of that can be looked up, slowly, but in principle by anyone.

What cannot be looked up is **which chain to build** to reach a particular answer.
A datasheet answers the question you put to it.
Which question to put to which source, in what order, and how to tell that an answer is wrong, is in none of them.
The series sorts its chains by who answers at the end: paper, an image or the device.
That sorting is already a method.

So two shares become three: **material, shape and method.**

## What becomes of the rule

*Keep the material, give away the shape.*
The rule holds, but not everywhere.

It holds as long as the material is already there.
With the laptop and its silent speakers in the [Reverberations](/series/reverberations/) series, the symptom was mine, the machine was mine and so was the sound.
I could give the shape away because there was something that could take a shape.

In a field I do not command, the line moves.
There I do not supply the material.
I supply the **question** and the **judgement**: what gets measured, what counts as evidence and what goes into the text.

That is not a retraction.
It is a condition that was invisible before because it was always met.

## Where the line blurs

It is not quite as clean as the last few paragraphs sound.
In *Reverberations*, too, not everything came from what I already knew.
The symptoms were mine, but the controls that `amixer` shows and the configuration files under `wireplumber.conf.d` were new to me.

So the difference between the two series is probably more gradual than the formula claims.
In *Reverberations* I at least knew where to start: with the sound that was missing.
In *Toolchains* I did not.
The knob series is probably not the only case in which the method came from Claude.
It is the first one in which that can no longer be overlooked.

## What I owe when the material is not mine

This is the uncomfortable half.
Whoever writes about a field they do not command cannot vouch for its correctness from their own expertise.
But they can do three things.

**First: enforce checkability.**
Every claim carries evidence that someone without expertise can follow: a log line, a command, a number.
Whatever cannot be backed up does not go into the text.
The findings notes behind the series already do this line by line.
Every entry is marked `EVIDENCE` or `INFERENCE`, that is, as measured or as inferred.
That difference can be read even by someone who would never have built the chain.
Me, for instance.

**Second: disclose the provenance.**
The front page says that every post here is written with Claude Code and that the numbers come from real sessions.
That discloses where the shape comes from.
About the substance it says nothing.
Counted on 18 September: in the three *Toolchains* posts, Claude appears only as the tag `claude-code`, not once in the text.
Anyone reading the series has to assume I knew the chains.
This post supplies what was missing.

**Third: keep the question and the judgement.**
Which question gets asked and which answer counts stays with the human, even if they could not have found the answer themselves.
The questions of the series came from my desk, from a board on which my own firmware could not produce a stable picture.
And the rule it ends on is a judgement: a schematic is believed where a measurement agrees with it.
Whether the measurement is enough is my call.

I considered a fourth obligation and left it out for now, the **cross-check**.
It asks for two independent routes to the same result, because you cannot tell from a single route whether it is right.
The series does it once: the protocol between the two processors was read separately from both firmware images, and both agreed.
It is the next candidate if three obligations turn out not to be enough.

## The test and its exception

*How much of this is really mine* ends on a test: does your text contain at least one number, one date or one sound that nobody but you could have contributed?

For *Toolchains*, after everything above, the answer ought to be no.
It is yes, and through the sound.

Part three had a question no register could answer: whether the vibration motor gets weaker when its enable line is sending data at the same time.
The diagnostic register reported values that could not be read on their own.
The fingertip decided it.
The clicks under traffic were **shorter and slightly quieter**.
For the speaker it was the ear.
While music played from the phone, my own firmware toggled every remaining pin, and its own tone was never heard.

So the old test passes its own exception.
But it proves less than I had credited it with.
It shows that somebody was sitting at the device.
It does not show who knew the way there.
For the material the test is enough, for the method it takes the three obligations.

## What carries over

Keep the material, give away the shape.
Where you have no material, keep the question and the judgement, and hand over the method only in a way that leaves a trace at every step, one you can check.

*How much of this is really mine* warns against the reverse: if the machine supplies the substance and the human polishes the wording, you get text that looks like a post and has nobody who needs it.
By that warning, *Toolchains* should not exist.
That it does comes down to the question.
It was there before there was any text.

This is the first part of the [Authorship](/series/authorship/) series.
The next one asks what this division of labour is called when the material very much is mine.
