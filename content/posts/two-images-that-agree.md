---
title: "Two images that agree: forensics on somebody else's firmware"
date: 2026-09-06T14:05:00+02:00
draft: true
tags: ["claude-code", "hardware", "esp32", "reverse-engineering", "debugging", "Technical Deep Dive"]
topics: ["machine"]
series: ["Every Question Its Own Chain"]
summary: "A firmware image does not describe what somebody intended, it describes what gets executed. Three chains end in an image: one reads the factory firmware, one reads two of them against each other, and one reads the same one twice — and finds the difference."
---

Part one described three chains that end on [paper](/posts/the-schematic-is-a-hypothesis/), and refuted the schematic three times along the way.
Paper describes an intent.
A firmware image describes what gets executed — and this board carried two of them, each saved before the first write of our own.

## TL;DR

- The first question of this part: why does the factory firmware hold a stable picture on the same glass when ours does not?
  An image can answer that, because it contains the answer.
- **Anchor technique:** log strings inside the image are the fixed points.
  A string's address sits in a constant pool, and from there a single load instruction leads back into the function that prints it.
- Result: the factory firmware does **not** use the vendor driver's default initialisation table but one of its own with 184 entries — and that one ends with the command the default table is missing.
- **Two images against each other** yielded the protocol between the two processors in full: baud rate, pins, frame format, command vocabulary.
  Both ends read independently, both in agreement — and the pins contradict the schematic.
- **The same firmware read twice** and compared: byte-identical except for 1,985 bytes.
  The difference *is* the finding.
- Finally: writing things down as you go is not tidiness, it is a tool.
  Of three research runs that died at a usage limit, exactly what stood in the file at that moment survived.

---

## Chain 4: forensics on the factory firmware

The starting problem stood at the end of part one: the drawn picture fades within one or two seconds.
The datasheet had supplied the physics.
What stayed open was what the factory firmware does differently — because it holds a picture on the same panel.

The chain:

```
espflash read-flash -B 921600 0 0x1000000 backup/factory-flash-esp32s3-....bin
  -> read the image header at 0x10000 -> split the segments
  -> xtensa-esp32s3-elf-objdump -b binary --adjust-vma=<load address>
  -> log strings as anchors
```

The first step is cheap and irreversibly important: **the read comes before the first write.**
16 MB over the serial port at 921,600 baud, a few minutes.
After that the as-delivered state exists as a file, and everything else is work on a copy.

Two sentences on housekeeping, because this is the point at which the one file that never gets passed on comes into being.
The image is somebody else's firmware: it stays on the disk, `backup/*.bin` is in the `.gitignore`, and what appears in these posts are the findings from it and nothing else — no bytes.
The device is mine, secure boot and flash encryption are off as shipped; nothing is being circumvented here that anybody intended as protection.
Why this is the one place in the whole series where you can actually get something wrong is [a post of its own](/posts/the-wrong-statute/).

The second step splits the image into its parts.
At address `0x10000` there is a header listing which part of the file is later loaded to which address in memory — six segments, each with file offset, target address and length.
Without that mapping a disassembler is useless: it can decode instructions, but every jump and every reference to data points at an address it does not know.
With it — `--adjust-vma=<load address>` tells the disassembler where the piece lives in memory — all addresses line up again.

The third step is the actual trick.
Compiled code has no function names left, but it has **log strings**, and those have addresses.
On this processor architecture an instruction cannot carry a full address as a number; constants sit in a small pool next to the code and are fetched with a load instruction of their own.
So if you find the address of the string `ESP_PanelBus_QSPI` in that pool and then the load instructions reading that slot, you land on exactly the functions that print it.
A string becomes an entry point.

What that turned up:

**The factory firmware uses an initialisation table of its own.**
The library it is built against ships a default table 216 entries long — and that one is referenced only in a branch that never runs.
Instead the application installs its own with **184 entries**, sitting in a completely different place in the data section.
That is why an earlier pass, searching near the library's data, kept finding only the default.
The two differ in nearly every analogue register — and the custom one ends with `INVON`, `SLPOUT`, **`DISPON`**.
Exactly the command the default table is missing and which the datasheet names as the only way out of the off state.

**The bus configuration sits in the constructor's constants.**
From the disassembled constructor the entire setup of the data bus could be read back: maximum transfer size `0x8000` = 32,768 bytes, clock mode 0, 32-bit command width, quad-line operation, no dummy cycles.
And one detail that would never have surfaced without a disassembler: the constructor sets a 40 MHz clock, and three instructions later the application overwrites it with **80 MHz**, before the bus is ever started.

**And a negative that ends a whole hope.**
The question of how to read a register back from the display controller correctly was meant to be copied from the factory firmware.
Searching for the read function gave: it has exactly two callers in the entire image, and both belong to the touch controller.
**The factory firmware never reads the screen.**
There is nothing to copy.
That answer is unsatisfying and still worth a lot — it stops anybody looking for it again.

## Chain 5: two images against each other

The second chain is the most interesting one, because it needs no instrument at all and is still stronger than the schematic.

The board carries two microcontrollers that talk to each other over a serial line.
Both hold their factory firmware, both were read out, and both ends of the same conversation were disassembled **independently** — same anchor technique, different processor architecture, different toolchain.

What came out agrees on every point:

| | ESP32-S3 | classic ESP32 |
|---|---|---|
| source file per the logs | `src/driver/uart1.cpp` | `../main/uart1.c` |
| baud rate | **921,600** | **921,600** |
| frame | 8 data bits, no parity, 1 stop bit | the same |
| flow control | none | none |
| pins | **TX GPIO40, RX GPIO39** | **TX IO23, RX IO18** |
| cover-art buffer | 48 KiB | 48 KiB |

Two independently read images agreeing on the same baud rate, the same frame format and mutually consistent pins are stronger evidence than a schematic — and they contradict it.
The plan names GPIO38 and GPIO48 as the serial link.
The firmware uses GPIO40 and GPIO39, which are the two pins the plan had earmarked for the audio clock.

And then an older measurement falls into place.
A scan of all free pins had reported GPIO39 as "held high externally" and nobody knew by what.
A serial receive line whose peer is currently silent looks exactly like that: the other chip holds its transmit line high when idle, permanently, from power-on.
The finding had been there all along; it had merely been read the wrong way round.

The protocol itself could be recovered in full as well, from the dispatch tables on both sides:

```
 0   magic   0xA3  S3 -> ESP32          0xBD  ESP32 -> S3
 1   cmd     u8
 2   len     u16, little endian
 4   data    len bytes
```

Cover art travels in numbered packets, **and the receiver requests every single one** — the sender never runs ahead.
Both sides compute the same stride of 1,016 bytes per packet, at two places in two different images, and both cap the payload at the same value.

At that point none of it had been measured, only read, and the note said so.
A day later a receiver listened on GPIO39: **921,600 baud, 8N1, zero framing errors, zero dropped bytes**, magic byte `0xBD` as read.
And command `0x06` turned out to be the metadata frame, with four string lengths in its sub-header:

```
len 50:  11 0E 0F 00  "Artificial Being\0" "Alien Project\0" "Aztechno Dream\0"
len 39:  06 0E 0F 00  "Skunk\0"            "Alien Project\0" "Aztechno Dream\0"
```

`0x11` is 17, which is the length of "Artificial Being" plus its terminating zero.
The four lengths plus the four header bytes add up to exactly the stated total in every frame observed.
Two images had predicted the protocol; a receiver confirmed it.

## Chain 6: reading the same firmware twice

The third chain is the shortest and the one you are least likely to think of.

```
espflash read-flash ... run1.bin
espflash read-flash ... run2.bin
sha256sum run1.bin run2.bin
cmp -l run1.bin run2.bin | wc -l
```

Reading the same thing twice and comparing answers a question about the tool first: is the backup trustworthy at all?
A serial read running for minutes at a high baud rate is not an obviously error-free operation, and everything after it builds on it.

The answer was: byte-identical — **except in 1,985 places**, all within a single region, the one holding non-volatile settings.

And here the test tips over from a tool check into a finding.
The difference is not a transmission fault but a statement about the device: **the chip writes its own memory while booting.**
It does so every time the read tool resets it, and across 16 runs it is always the same not-quite-two kilobytes.
The firmware region, by contrast, is bit-stable.

So one command yields three things: that the read is reliable, which part of memory may be treated as constant, and that any future comparison of two backups has to ignore exactly that one region.
A difference that reproduces in the same place is not noise.
It is the answer to a question you had not asked.

## Writing things down is a tool

At the end of this part, a chain that sits above all the others.

Every one of the investigations above wrote its findings into a file **while working**, not afterwards.
The files in `scratch-findings/` start as a skeleton — the open questions as numbered headings, each with `(to fill)` beneath it — and next to that runs a source log: `S1`, `S2`, `S3`, every source with its address, a quotation, and a note on whether it supports or refutes something.
At the very bottom, a section headed "Dead ends (do not search again)".

The reason is not tidiness but an experience with a date attached.
On 4 September three research runs going in parallel died at a usage limit, mid-sentence.
What survived was exactly what stood in their files at that moment — and that was enough to carry on with.
What was lost was not information but **compression**: the summary that never got written.

From which follows a rule that holds for research in general and not just for hardware: saving your findings up for the final report bets everything on the ending.
Writing them down as you go risks only the summary, and the summary is the cheapest part.

The collection of dead ends is the underrated piece of this.
"The schematic has no enable pin for the panel", "the reported bug is about 33,000 bytes and not 3,600", "the factory firmware never reads the screen" — three sentences that answer no question and each save an hour the moment somebody picks up that trail a second time.

The last part leaves the images behind.
Paper says what was intended; an image says what gets executed.
What is actually soldered onto the board is said by neither — for that you have to ask the device.
