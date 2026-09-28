---
title: "Your impression is right: how I talk to an agent"
date: 2026-09-28T10:45:00+02:00
draft: false
tags: ["claude-code", "language", "workflow", "Essay"]
topics: ["agent"]
summary: "Twice I asked an agent to check the shadows in my app. The first time I got a confirmation, a number and an explanation, and the explanation was wrong. The second time I got a measurement. The model was the same; the sentence was a different one."
---

## TL;DR

- I had the impression that the cards in one menu of my app cast heavier shadows than all the others, and asked the agent to check.
- The answer began with "Your impression is right" and came with an explanation and a number. It had measured in the emulator; I had seen it on the phone.
- Almost five hours later I gave the same task again, this time naming the device, the scope, the critical spot, the method and a rule for the finding. The result was a measurement, and the morning's explanation fell over.
- What neither instruction had asked for I then saw myself: two long pages suddenly scrolled sluggishly.
- What I learned was less about shadows than about my sentences. I now try to see in advance where a misunderstanding can arise.

---

## An impression

The app I am building with Claude Code shows almost everything on cards: lists, settings, help pages.
Some menus open as a panel that slides up from the bottom, a so-called bottom sheet.
That is where the shadows caught my eye.

I wrote (translated from German here and below):

> Check the shadows of the cards on the bottom sheets visually. I have the impression that they are stronger than those of other cards.

The answer arrived just under half an hour later and began like this:

> Your impression is right. The shadow itself is equally strong, it darkens by about 20 % on the page as in the sheet. In light mode, though, the sheet was white like the cards […] That is why it looked heavier.

With it came a change after which "the edge profile there is now the same as on the page".
It read as thorough: a confirmation, a number, a cause, a fix.

The agent had measured all this in the emulator, a simulated phone on the computer.
My impression came from the real phone in my hand.
For checks that don't need my hands, I had even set the emulator as the default myself.
We had both looked, just at different devices.

In hindsight my sentence left more room than I saw at the time.
"Visually" doesn't say on which device.
"I have the impression" invites confirmation, and a confirmation only needs a plausible explanation.
I had not asked for a measurement.

## The same request, once more

Almost five hours later I wrote:

> Compare on the phone the shadows of all cards in the lists, options, settings, pages and the bottom sheets (and wherever I may have forgotten it in this list). Pay particular attention to the bottom edge of the lowest cards. Measure visually instead of claiming. If you find differences, use the shadow of the lowest card in a list for all cards.

It is the same request.
Only now it says on which device, where and with what gap, which spot is the critical one, how to check, and what happens to a finding before there is one.
The middle sentence is an imperative in the grammatical sense: it allows no answer that gets by without a measurement.

The agent took screenshots on the phone and read the brightness pixel by pixel outward from the card's edge.
Result: in the bottom sheet the shadow was twice as dark as on the pages.
The cause was that the sheet is technically a window of its own, for which Android draws shadows by different rules.
So my impression from the morning was right, the explanation for it was wrong, and the "20 %" held only for the page.
The rule in my last sentence settled the fix as well: all cards got the shadow of the lowest list card.

## What no measurement had asked

Afterwards I picked up the phone again and wrote:

> With all cards expanded, Terms and Changelog now scroll very sluggishly and stutter, as if something were needlessly being redrawn all the time. All other pages with long content seem to scroll as fast as before, but check that yourself anyway.

Screenshots show still images.
How scrolling feels is on none of them, and my instruction hadn't asked for it either.
The agent then measured how long the phone took for each frame while swiping: on the two pages about 350 milliseconds instead of a fraction of that.
The new shadow was computed as an image the full size of each card, and that image was sent to the graphics unit anew with every frame.
My guess was right down to the wording.
After a second rework the pages were as fast as before, and the shadows stayed the same.

The tail "but check that yourself anyway" paid off.
I gave the finding and the suspicion, yet left the cross-check open.
It showed that a small remainder of slowness on those pages had been there before and comes from the text, not from the shadow.

## What I took from it

The model was the same at both times of day.
What changed was my sentence.

I take two things away.
The first is discipline in language: place, yardstick and a decision rule belong in the instruction before there is a result, and a word like "impression" belongs there when I want confirmation, and not when I want a finding.
The second weighs more: seeing in advance where a misunderstanding can arise.
Emulator or real phone, still image or scrolling: both times these were differences that were clear to me and not to the agent, because I hadn't said them.

These days I read every sentence, before I send it, the way an agent would read it.
A person next to me would have known that I was holding the phone.
The agent knows only what is written, and what is missing it fills in with whatever it has at hand.

A little over a week ago I [wrote about this change in my language](/posts/language-follows-suit/), back then more as an observation.
The day of the shadows turned it into a way of working.

## And your sentences?

If you work with an agent, it is worth looking back at your own instructions.
Which words in your sentences leave room you don't notice, because you already know the answer?
Has the way you phrase tasks changed over the past months, and in which direction?
And do you now write differently to people, too?
