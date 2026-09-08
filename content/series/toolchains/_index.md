---
draft: true
title: "Toolchains"
badge: "Technical Deep Dive"
summary: "Thirteen short tool chains on a board with no usable documentation. Each assembled from existing standard parts, each ending in exactly one fact, and what separates them is not the technique but who answers at the end."
---

{{< serienbadge >}}

Three posts about the same board: a rotary knob with a round screen, two microcontrollers and documentation consisting of a wiki page and a ZIP archive.

They belong together because they split up a catalogue.
Thirteen chains were actually run on this device, and they sort themselves by **who answers at the end**:
part one asks paper, part two asks firmware images, part three asks the device itself.

{{< kettenschema >}}

## Whether this is for you

The way from left to right is the story: a question, a chain of tools that are lying around anyway, a fact, a file.

**The arrow going back** is the reason to read.
None of these chains is new: reading a datasheet, disassembling firmware, trying pin assignments until something answers, all of that is decades old.
What is new is the price: a chain takes minutes to assemble, so it pays to build one per question instead of building a fixed measurement rig and then working out what it can answer.

> If you enjoy watching a vendor document break against a measurement, you are in the right place.
> Part one opens with a schematic refuted three times — each time in exactly the statement you had opened it for.

**The three boxes below** are the structure, not a ranking.
Paper says what somebody intended; an image says what gets executed; the device says what is.
All three are needed, and confusing them is expensive.

No ESP32 knowledge is assumed.
Registers, the literal pool, non-volatile memory and the first command of a memory card are explained in passing, and you can follow along having never held a soldering iron.
There are command lines in here, with the real numbers, but as evidence, not as a recipe.
