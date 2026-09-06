---
title: "The wrong statute: the fear sits at the other end of the chain"
date: 2026-09-06T14:20:00+02:00
draft: true
tags: ["claude-code", "hardware", "law", "writing", "meta", "Essay"]
topics: ["author"]
summary: "Writing up hardware forensics raised the question of whether it is a criminal offence. The answer was a surprise: the statute everybody fears does not apply, for three reasons — and the one action where you can actually get it wrong feels entirely harmless."
---

While a three-part series on [forensics on an undocumented board](/series/every-question-its-own-chain/) was being written here, a question came up in the middle of the work: are we committing an offence by publishing this?

It is a fair question, and the answer surprised me.
Not because it was reassuring, but because it was reassuring in a completely different place from the one I had expected.

> **This is not legal advice.**
> I am not a lawyer. What follows is the check I ran for my own case, with the sources I pinned it to.
> It is German law, because that is where I am. Anyone who has to answer the same question should ask somebody who carries liability for the answer.

## TL;DR

- Germany's "hacker statute", § 202c StGB, covers **no texts**. It covers passwords and computer programs.
  A description of a method is neither.
- It also has no offence to prepare here: it is my own board, and secure boot and flash encryption are off as shipped.
  There is no protection to overcome.
- The one action carrying real risk is the one that feels most harmless: **passing on the 16 MB file** created when you take the backup.
- Dumping and disassembling are not merely tolerated, they are **expressly privileged** in copyright law — for interoperability and for fixing errors.
- Protocol structure and register values are facts and can be published; somebody else's schematic drawings cannot.
- The actual thought: **intuition follows the vocabulary, not the law.**
  "Disassembling" sounds like breaking in, "backup" sounds like housekeeping — and the risk lies exactly the other way round.

---

## The statute everybody fears does not apply

§ 202c StGB is known in Germany as the hacker statute, and it has a bad reputation it earned honestly: when it was introduced in 2007 it was genuinely unclear whether it criminalised part-time security research.

It simply does not apply to a post about your own board, for three reasons, each of which stands on its own.

**First, it covers no texts.**
What is punishable is producing and distributing *passwords and access codes*, or *computer programs whose purpose is the commission of an offence* under § 202a or § 202b.
An essay describing a method is neither.
Knowledge is not a tool in the sense of the statute — the Federal Constitutional Court read it narrowly in that direction in 2009 and took dual-use tools out of its scope in principle.

**Second, there is no offence to prepare.**
§ 202c is an inchoate offence; with no possible principal offence it has nothing to attach to.
§ 202a requires data that is *not intended for the perpetrator* and *specially protected against unauthorised access*.
Neither element is present here, and not by a narrow margin: the board is mine, and its flash is unencrypted because the manufacturer never switched secure boot on.
There is nothing to overcome.
§ 202b, intercepting data, fails at the same point — what was listened to was a conversation between two chips that both belong to me.

**Third, the intent to prepare such an offence is missing.**

The neighbouring provisions go the same way.
Data tampering and computer sabotage (§ 303a, § 303b) require somebody else's data.
And § 108b UrhG, circumventing technical protection measures, would need an *effective technical measure* — which demonstrably does not exist here.

What is remarkable is how little of this is a question of interpretation.
I had expected to be weighing things up, and found elements of the offence that are simply absent.

## Where the line actually runs

It runs through copyright, and it runs in exactly one place.

The first step of any firmware forensics is to save the as-shipped image before anything is written.
On this board that is 16 megabytes for one microcontroller and 4 for the other.
Those two files are somebody else's software.
They carry no licence, they are not meant to be passed on, and buying the device changes none of that.

Taking the backup is allowed — § 69d(2) UrhG gives a lawful user the right to a backup copy, and that right cannot be excluded by contract.
What is not allowed is handing it on.

That is the whole line.
It is sharp, it is easy to observe, and in this project's repository it consists of one rule:

```
# Flash images of the factory firmware — 16 MB binaries, nothing for Git.
backup/*.bin
```

The comment above it matters more than the rule itself.
A `.gitignore` entry with no reason attached does not survive the next tidying-up.

## Three things that are allowed and feel forbidden

**Disassembling.**
Copyright law privileges it explicitly.
§ 69d(3) permits observing, studying and testing a program in order to determine the ideas underlying it.
§ 69e permits decompilation where it is necessary to achieve **interoperability** — precisely the case when you want to find out how one chip talks to the other.
And in 2021 the Court of Justice of the European Union held that a lawful acquirer may also decompile in order to **correct errors**.
Both purposes applied here: talking to the second microcontroller, and repairing a picture that faded after two seconds.

**Reconstructing a protocol and publishing it.**
In *SAS Institute* in 2012 the Court of Justice held that a program's functionality, its programming language and its data file formats are **not** protected by copyright.
What is protected is the expression, not the idea.
A frame format with a four-byte header, a baud rate, the numbering of packets: those are facts about an interface, and facts belong to nobody.

**Brute force over a search space.**
In part three of the series a program works through 840 pin assignments until a memory card answers.
That sounds like an attack and is not one: it asks a device that belongs to me about its own wiring.
No password is guessed, no access is overcome.

## The paper you do not reprint

Two sources from part one deserve a closer look, because they have to be treated differently.

**The schematic** sits freely on the vendor's site — but *freely available* does not mean *freely usable*.
There is no licence attached, and with no licence the default is: all rights reserved.
A schematic is protected as a technical drawing.
What is protected, however, is the **drawing**, not its content.
That the display clock hangs on GPIO13 is a fact about a piece of copper and can be restated in a table of your own.
Reprinting the sheet itself would be something else — which is why the series contains no images at all.

**The datasheet** is quoted, and that is permitted.
§ 51 UrhG allows quotation where it serves as evidence for a statement of your own, is justified in extent by that purpose, and names the source.
That is exactly what the sentences in part one do: one sentence from the datasheet, with the page number and the location, as evidence for a claim about the fading picture.
The attribution is not a courtesy.
It is the condition under which the quotation is allowed at all.

## Why the fear sits at the wrong end

And here is the point I am writing this down for.

Everything about this work that feels dangerous is allowed.
The one thing that is forbidden feels like housekeeping.

I think that is down to the vocabulary.
The activities are called *dumping*, *disassembling*, *sniffing*, *brute force* — words that come from the world of break-ins and attacks, and which you say out loud because they sound like competence.
The risky act, by contrast, is called *backup*, *attachment*, *drop it in the repo*.
It is invisible, it takes a second, and it has no vocabulary that turns on a warning light.

Intuition follows the words instead of the matter.

This is not confined to hardware.
Data protection has the same shape: you agonise over whether you are allowed to *analyse* the data, and export a CSV to your desktop without a second thought while you do.
The analysis is visible and gets checked; the copy is incidental and does not.

From which follows a practical consequence, and it is the actual yield of this whole exercise: **the legal question does not belong at the end.**
Asking it before publishing — "am I allowed to write this?" — puts it at the point where nothing happens anyway.
It belongs at the point where the file comes into being.
That is why the rule in this project lives in the `.gitignore` and not in a checklist nobody reads.

One postscript, which shows that the check should not confine itself to law: part three carried the full MAC address of my board.
Legally entirely unobjectionable — my device, my identifier.
It is masked there now anyway, because a permanent device identifier in a public text proves nothing it would not equally prove with three `xx`.
Not everything that is allowed is something you want to have done.

## What I do not know

Honesty belongs here, on this subject especially.

I did not have this checked by a lawyer.
The sources are looked up and they fit my case, but I have no training in noticing which question I failed to ask.

§ 69e has narrower conditions than my summary above suggests: the decompilation must be indispensable, the information must not be otherwise available, and the result must not be used for a substantially similar program.
For my case that is uncontroversially satisfied.
For the general sentence "reverse engineering is allowed" it is not.

And the most uncomfortable point remains the vendor download with no licence attached.
For the schematic drawings the consequence is clear.
For the demo sources, from which the series quotes individual constants, the line between a fact and an excerpt of code is a soft one, and I drew it by feel.
