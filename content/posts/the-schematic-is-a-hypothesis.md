---
title: "The schematic is a hypothesis: what paper really says about a board"
date: 2026-09-06T14:00:00+02:00
draft: true
tags: ["claude-code", "hardware", "esp32", "reverse-engineering", "debugging", "Technical Deep Dive"]
topics: ["machine"]
series: ["Toolchains"]
summary: "A board with no usable documentation answers no question by itself. For every question you assemble a short chain out of standard tools, and the first group of those chains ends on paper. Three times, the paper here was wrong."
---

The schematic for this board has been refuted three times.
Once about the loudspeaker, once about the vibration motor, once about the serial link between the two processors.
Not in some detail, but each time in exactly the statement you had opened it for.

## TL;DR

- The device is a Waveshare ESP32-S3 Knob Display: a rotary knob with a round screen, **two microcontrollers** and documentation consisting of a wiki page and a ZIP archive.
- Every question gets its own **short chain** of existing standard parts, and each one ends in exactly one fact.
  What is new about that is not the technique, every link is old.
  What is new is that such a chain takes minutes instead of an afternoon.
- This part covers the three chains that end on **paper**: the datasheet, the schematic, somebody else's source code.
- The datasheet settled a question that had been guessed at for two days, in a single `grep`.
- The schematic delivered the complete pin map and a **negative result** that closed off an entire line of suspicion.
- The source code delivered a negative too: the suspected cause does not exist there.
  A negative is a result, not a failure.
- The rule at the end: **vendor paper is a hypothesis.** It is believed where a measurement agrees with it, and not otherwise.

---

## Refuted three times

The three places where the paper was wrong come first, because they set the tone for everything after.

**GPIO0 and the loudspeaker.**
The board carries an analogue switch that hands the digital-to-analogue converter to one microcontroller or the other.
The schematic calls its control input `I2S_SWITCH_IN`, routes it to GPIO0, and Waveshare's own example code writes `gpio_set_level(GPIO_NUM_0, 1)` in its very first line, supposedly to give the converter to the ESP32-S3.
Measured: no level on GPIO0 changes anything.
Nor does any other free pin.
The loudspeaker belongs to the other chip, by way of a mute line that lives on a sheet the S3 does not appear on.

**`HAPTIC_EN` and the vibration motor.**
The schematic ties the motor driver's enable input permanently to 3.3 volts, so it is always on and needs no pin.
Measured: unless GPIO38 is actively driven high, the driver reports `0xE9` in its diagnostic register, meaning the output stage is off.
As soon as the pin goes high it reports `0xE0`, and a click is felt in the case.
Low, `0xE9`. High, `0xE0`. Three times within one boot, identical across two consecutive runs.

**The serial link.**
The schematic labels GPIO38 `ESP32S3_TX` and GPIO48 `ESP32S3_RX`, that would be the line the two processors talk over.
Both pins are in fact connected to nothing that speaks.
The factory firmware uses GPIO40 and GPIO39.

Three claims, three refutations.
What follows for the rest of the paper?
Not that it is worthless — of 23 measured pins, 20 agree with the plan.
But that every single claim in it stays a **hypothesis** until the device agrees.

## Chain 1: the datasheet

The screen showed a picture that faded within one or two seconds.
The backlight stayed on, the pixel data was provably correct, and trying to read a register back from the display controller returned nothing but zeros.

The chain:

```
web search -> dl.espressif.com -> PDF (264 pages) -> text -> grep/sed -> register table
```

The datasheet for the ST77916 display controller is public; it is just not where you look for it, not with the chip's maker but with Espressif, at `dl.espressif.com/AE/esp-iot-solution/ST77916_SPEC_V1.0.pdf`.
Once downloaded, the rest is ordinary text work: PDF to text, then search.

Four answers fell out of it, three of which had been standing around as guesses for days.

**The chip is off after every reset.**
Page 171 says it in plain words: command `29h` — "Display On" — is the only way out of the *display off* state, and power-on, software reset and hardware reset all land there.
The vendor driver's initialisation table never sends that command.
It ends at waking the chip from sleep.

**The fading has a named physics.**
Sleep mode, page 161: "In this mode the DC/DC converter is stopped, internal oscillator is stopped, and panel scanning is stopped."
A panel whose scanning has stopped while its backlight keeps burning holds its charge for about a second and then relaxes.
It *fades*. A display that has been switched off, by contrast, *snaps* to black within one frame.
The difference between fading and snapping stops being a nuance of observation and becomes a distinguishing feature with a page number.

**Reading registers is gated.**
Page 145, command `F4h`: reads of the manufacturer registers sit behind a toggle you have to write first.
Without it, what comes back is what came back: nothing.
Two pages further on it also says the read opcode is `0x0B` and not `0x03`.
`0x03` is the read opcode of flash memory chips and not a command on this controller at all.
Every read attempt so far had been sending the wrong number.

**And there is a silent failure mode.**
The interesting registers (charge pumps, gate voltages, VCOM) live in a second command page that has to be unlocked first.
Written with the page closed, the writes are **discarded without anything reporting an error**.
The initialisation "succeeds" and the chip carries on with its factory defaults.

One side finding that cost time and therefore belongs here: Waveshare's wiki page answers a program fetching it with **HTTP 403**.
With `curl -A "Mozilla/5.0"` it comes.
That is no insight about the board, but it is the difference between "the source does not exist" and "the source wanted to see a browser".

## Chain 2: the schematic as an image

The second chain is the only one here in which nothing is searched and something is **looked at**.

```
curl -A "Mozilla/5.0" -> ZIP -> five PNG sheets -> look -> netlist
```

A schematic as a raster image has no text to search.
What makes it readable is something else: a net — an electrical connection — carries the same name on every sheet, and the work consists of following that name from sheet to sheet and writing down where it appears.
Five sheets, one name after another, a table at the end.
That is dull work and therefore easy to delegate, but it is not a search; it is a transcription.

Two results justified it.

The first is the complete pin map: which pin of the microcontroller hangs on which line of the display, where the touch controller sits, where the rotary encoder, where the memory card.
Twenty rows that had previously been guessed together from forum posts.

The second is a **negative result**, and it was worth more.
The line of suspicion ran: perhaps the panel has its own supply rail that must be released through a load switch, and that switch stays off.
A very similar board from another vendor has exactly such a pin, active low, and a rail decaying through leakage would be an excellent explanation for a picture that slowly disappears.

On sheet 1, the display module's two supply pins go straight to 3.3 volts.
No switch, no transistor, no enable net.
The trail is dead, in thirty seconds instead of half a day of probing.

The same pass produced the explanation for the silent loudspeaker anticipated above: the mute input of the digital-to-analogue converter hangs on a pin of the *other* microcontroller and on nothing else.
It sits on a sheet the ESP32-S3 does not appear on, which is why searching for "S3" would never have turned it up.

## Chain 3: source code instead of documentation

The third paper chain reads code somebody else wrote as if it were the missing documentation.

The question was: why do transfers to the screen above a certain size apparently not arrive, even though the library returns `Ok`?
Suspicion fell on the hardware abstraction layer `esp-hal`, and that is already on disk anyway, unpacked in the package cache:

```
/home/stefan/.cargo/registry/src/index.crates.io-.../esp-hal-1.1.2/src/spi/master/
```

No cloning, no searching: the source of the exact version that was built, line by line.

The result was a negative, and a thorough one.
The only size limit anywhere in the path sits at 32,736 bytes, far above anything being sent here.
The split into memory descriptors changes at 4,092 bytes, also above the size in question, and later overrun experimentally anyway.
And checking which values change with the transfer size at all yielded exactly two, both harmless.

Then came the cross-check against the project's changelog and its issue tracker.
One reported bug looked like an exact match at first glance, until you read it to the end: it occurs at 33,000 bytes, not at 3,600, and describes precisely the 32 KB ceiling already known from the source.
A report that *almost* matches your own observation is the most expensive find such a search can produce, and the only remedy is to read it down to the number.

The cause turned out to lie elsewhere, and that belongs to the honesty of this chain: the original measurement had sized the transfer, the memory buffer and an array on the stack with *one* number.
It could not carry a statement about any single cause.
Once the three were separated, every size came through, from 720 to 21,600 bytes.
Reading the source did not find the cause.
It ruled out a wrong one before anything was built on it, and it did so in an hour.

## The cross-check

At the end of this part stands the rule that follows from the three chains and holds for everything after.

Vendor paper (datasheet, schematic, example code) is a good **hypothesis** and not a measurement.
It describes what somebody intended at design time, and the design may have changed, the sheet may be one revision old, the example code may come from a sibling board.
None of that is malice; it is the ordinary half-life of documentation.

In practice that means two things.

**First**: paper is excellent for generating candidates and shrinking search spaces.
The pin map from the schematic cut the later search for the memory card from "every pin" down to "these seven", and the device answered the search itself.

**Second**: paper is no good for closing a question.
Of 23 measured pins, 20 agree with the plan — a good rate, and still no reason to believe the twenty-first unchecked.
The three deviations did not turn up where you expect deviations. They turned up in exactly the three functions you wanted to know about.

The next part goes one step further: away from paper, towards what is actually on the device, the two firmware images that were saved before the first write of our own.
An image does not lie about its intent.
It contains what gets executed.
