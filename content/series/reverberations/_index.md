---
title: "Reverberations"
badge: "Technical Deep Dive"
summary: "Three debugging stories about the speakers in one laptop. Each part is the aftermath of the one before it: the hardware problem, what the debugging left behind, and what the fix left behind."
---

{{< serienbadge >}}

Three posts about the same two speakers in the same laptop, written in the order the problems appeared.

They belong together because each one is the aftermath of the previous:
the first found a hardware problem and fixed it,
the second found what the *debugging* had left behind,
and the third found what the *fix* had left behind.

{{< erkenntnisschema >}}

## Whether this is for you

The path from left to right is ordinary.
What makes this series is the two arrows going back.

**The dashed arrow** is the reason to read.
Every part starts with a hypothesis that sounds good and ends with a measurement taking it away:
a theory built by listening, argued in public and retracted;
an explanation of a cause, dismissed in a minute;
an error message in which I recognised my own theory although it was reporting something else.

> If you enjoy watching a good explanation break against a number, you are in the right place.
> If decibel values, configuration keys and journal lines spoil your evening, less so.

**The solid arrow** is the argument of the series.
Every fix leaves behind a state it no longer corrects, and that state becomes the next part's symptom.

Familiarity with ALSA, PipeWire and systemd is assumed.
The posts name controls, configuration keys and journal timestamps directly and explain no fundamentals.
There are commands in them, but as evidence rather than instructions — if you want to repair your own speaker, what you will find here is a method, not a recipe.
