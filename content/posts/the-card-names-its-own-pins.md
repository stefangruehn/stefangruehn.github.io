---
title: "The card names its own pins: when only the device will answer"
date: 2026-09-06T14:10:00+02:00
draft: true
tags: ["claude-code", "hardware", "esp32", "reverse-engineering", "debugging", "Technical Deep Dive"]
topics: ["machine"]
series: ["Every Question Its Own Chain"]
summary: "840 pin assignments tried until a memory card answered. A vibration motor measured by a fingertip. A cable whose plug direction decides which processor you are talking to. The four chains that end in the device itself — and what the whole thing was for."
---

Part one read [paper](/posts/the-schematic-is-a-hypothesis/) and refuted it three times.
Part two read [two firmware images](/posts/two-images-that-agree/) and got a complete protocol out of them.
Both are answers about what somebody intended or what a program does.
What is actually soldered onto this board is said by neither.

## TL;DR

- Four chains end in the device: **your own firmware as an instrument**, **hand and ear in the loop**, **the USB enumeration**, **the boot log**.
- A memory card whose pins are documented nowhere named its own: 840 combinations tried, **exactly one** answered, reproduced twice.
- Scanning every pin with the internal pull-up and pull-down separates the connected lines from the free ones in a single flash cycle — and the first version measured nothing because it read two milliseconds too early.
- A fingertip measured what no register would give up: that a click gets **shorter and quieter** under traffic.
- Two workbench traps that each cost a run are written down here on purpose.
- The point at the end: none of these chains is new. What is new is that every question builds its own in minutes.

---

## Chain 7: your own firmware as an instrument

The load-bearing chain of this part is the easiest to describe and the most productive.

```
src/bin/<question>.rs  ->  flash  ->  monitor log  ->  scratch-findings/logs/
```

Every question gets a small program of its own that does nothing except ask that one question, and its log is the measurement record.
Not one program with switches, but many small ones — `pullscan`, `sdprobe`, `switchhunt`, `uartsniff`, `pin38` — each with the question in its file header and the result in the log beside it.

**Scanning the pins.**
The first question to put to an unknown board is: which pins are connected to anything at all?
Every pin is read twice, once with the internal pull-up enabled, once with the pull-down.
A free pin follows whichever direction is applied; a pin that reads high both ways is held from outside.
Eight rounds, 23 pins, one flash cycle:

```
Pull: GPIO2  up 8/8 down 8/8  held HIGH externally
Pull: GPIO3  up 8/8 down 8/8  held HIGH externally
Pull: GPIO4  up 8/8 down 0/8  floating
Pull: GPIO5  up 8/8 down 8/8  held HIGH externally
```

The check on the method was built in: GPIO11 and GPIO12 are the known data bus, pulled up by resistors, and they came out as "held high externally".
The method reports what it claims to report.

**And then the memory card that names itself.**
After the scan, seven pins were left hanging on something unnamed.
A card in the slot has five pulled-up lines and one that is not pulled up — that is the pattern being searched for.
Rather than guess which is which, you can ask the card: it also speaks the simple serial protocol on the same contacts, and its first command, `CMD0`, has a known reply.

`sdprobe` worked through **840 assignments** — clock from the floating candidates, the three data lines from the pulled-up ones — and put the same question to each.

```
CLK GPIO4  CS GPIO2  MOSI GPIO3  MISO GPIO5  --  CMD0 0x01, CMD8 0x01 00 00 01 aa
```

Exactly one answered, and it answered twice, across two consecutive boots.
`0x01` means "idle, no error", and the reply to the second command echoes the test pattern `0x01AA` back unchanged — a card answering by accident does not do that.
Four pins that appear in no documentation, named by the card itself.

That is brute force over a search space paper could only have guessed at.
And it is cheap: 840 attempts is a program that runs for two minutes.
The card was later read over exactly those four pins — 480 MiB, one FAT32 partition, 119 files in 10 directories, 400 MiB of demo material that appears nowhere in the flash image because it was never there.

**Two corrections to the method**, both expensive enough to write down.

The first version of the scanner read the pin immediately after switching the internal pull — and reported every free pin as "held low externally".
An internal pull is weak and needs a moment against the line's own capacitance.
Two milliseconds of settling fixed it and invalidated every result before that.

The second concerns a program hunting for the loudspeaker switch by flipping one pin after another while music played.
It reported: nothing changed.
Except it had never left the candidate list — the rotary knob used to step through it was polled too slowly, and its pulses are shorter than the polling interval.
An entire run measured the same first candidate over and over.
**A negative result needs proof that the check happened.**
The fix was to acknowledge every step in the case: the vibration motor clicks as many times as the number of the candidate it moved to.
Without that, "found nothing" and "tried nothing" are the same sentence.

## Chain 8: hand and ear in the loop

Some questions no register answered.

The vibration motor shares its enable input with a transmit line — that was the GPIO38 from part one, the one the schematic ties permanently to 3.3 volts and which in fact has to be driven.
From which came a question: if the same line transmits *and* enables, what does that cost the motor?

A serial transmit line idles high, which is the enabled state.
But a stream of nothing but zero bytes is the worst case such a line can produce — a start bit and eight zero bits, so nine of every ten bit times are low, 78 microseconds at a stretch at 115,200 baud.
The diagnostic register then reported `0xE9` on the first of three attempts and `0xE0` on the two after, reproducible across two runs and undecidable from the register alone: does the enable really drop out, or is the diagnostic merely measuring its own chopping?

The fingertip settled it.
The three clicks under the zero stream were **shorter and slightly quieter** than the three with the line held steadily high.
So it is not the measurement that changes but the motor that is driven less.

For that the project has a small scaffold of its own: a sequence that halts before every step and waits — a press of the knob, a touch of the glass or a keypress at the computer are equivalent go-signals.
The answer arrives while the hand is still on the knob, instead of out of a log afterwards.

The loudspeaker was decided the same way, and there the ear was the instrument.
With music from a phone coming out of the jack over the second processor's Bluetooth link — which by itself proves that jack, converter, analogue supply and mute all work — our own firmware flipped each remaining pin in turn.
The music was disturbed by none of them, and our own tone was never audible.
The loudspeaker does not belong to this processor.
No register would have said so.

## Chain 9: the USB enumeration as a diagnosis

The shortest chain of the series is one command.

```
lsusb
```

This board has two USB sockets: one goes straight to the ESP32-S3, the other through a serial converter chip to the classic ESP32.
If a CH340 shows up on the computer, you are talking to the *other* microcontroller.

That sounds trivial, and it is — right up to the moment a tool reports an unfamiliar chip type and the explanation is not that something is broken but that the cable is in the other socket.
**The plug direction is this board's selector switch.**
On a board with two processors, the first question about any inexplicable behaviour is: which of the two am I talking to right now?
One command, one line of output, question answered.

## Chain 10: the boot log as ground truth

The last chain is the one all the others fall back on.

```
espflash board-info
espflash reset && cat /dev/ttyACM0
```

A reset and the log after it answer the question of whether what you believe is running is running at all: chip revision, MAC address, flash size, the partition table, the segments with their load addresses — and right at the end, the line saying the boot has finished.

```
Chip type:         esp32s3 (revision v0.2)
Flash size:        16MB
MAC address:       fc:01:2c:xx:xx:xx
```

(The MAC address is masked here; the real log prints it in full.)

Two workbench traps belong here, and each cost a measurement run.

**After flashing without a monitor, the application does not run.**
The chip sits in the flash tool's helper stub, and the log stays empty.
Once that cost a set of five revolutions of the knob that nobody was listening to; another time a dark screen was suspected of being a display fault for minutes when in fact nothing was running.
The reset is part of the measurement, not its preparation.

**And the monitor needs a terminal.**
From a shell with no terminal attached it aborts immediately — "Failed to initialize input reader" — and leaves an empty file behind.
The way around it is to read the serial port directly, after issuing a reset of your own.
That is no insight about the board.
It is the difference between "the device is silent" and "nobody was listening", and in a debugging session that difference is everything.

The principle behind it is unspectacular: before a measurement says anything about the device, it must be established that the device ran.
An empty log is not an observation.

## The session as a source

One chain is left that touches no hardware.

The sessions in which all of this happened are kept as transcripts in the project.
They are not documentation — that is what the finding notes from part two are for — but raw material: the numbers, the order of events and the dead ends nobody remembers come out of them later.
The sentence about the first pin scanner reading two milliseconds too early is not in this post because somebody remembered it.

That is the same movement as in all thirteen chains: the last stage is always **writing to a file**.
A datasheet ends in a register table, a schematic in a netlist, an image in a finding note, a measurement program in its log, a session in its transcript.
Anything that does not end in a file is not a measurement but a memory.

## What the whole thing was for

None of the thirteen chains is new.
Reading a datasheet is as old as datasheets.
Dumping and disassembling firmware has been done for decades.
Trying pin assignments until the far end answers is brute force and was always possible.

What has changed is the price.
A chain like this used to be a project: find the right tools, get them to work together, build the measurement rig — and because that was expensive, you built the rig and *then* worked out which questions it could answer.
The questions followed the tool.

Here it was the other way round.
Thirteen different chains in a few days, each assembled for exactly one question, none of them reused.
The search space of 840 pin combinations was not worked through because that is clever, but because the program for it was cheaper than thinking about how to avoid it.
That is the actual change: **the question no longer follows the measurement rig; the rig follows the question.**

And the order behind it is simple in the end.
Paper says what somebody intended.
An image says what gets executed.
The device says what is.
Confuse the three and you spend three days looking for an enable pin that does not exist.
