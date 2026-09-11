---
title: "Green locally, broken on the web: the build stage nobody sees"
date: 2026-09-08T05:00:00+02:00
draft: false
tags: ["claude-code", "hugo", "CI", "debugging", "deployment", "Technical Deep Dive"]
topics: ["shipping"]
summary: "The landing page of a freshly published series was wrecked on the web, locally everything looked fine, and the source was flawless. The culprit was a single quotation mark in a place nobody ever looks at, and a build stage that only runs in CI."
---

On 5 September, a few hours after publishing the series [Codebook](/series/codebook/), I looked at the German landing page in my browser.
It was broken.

## TL;DR

- Two symptoms: spaces were missing between bold and normal text, and further down text was overlapping itself.
  Both look like CSS.
  It was not CSS.
- The source was flawless.
  Every space was there in the Markdown, and locally the page looked fine in the browser.
- Between what I look at and what gets published sits a stage that exists on one side only: CI builds with `hugo --minify`, my machine builds without — and has done since the first commit.
- I did not find it by reading.
  It was a comparison: build twice, then put the text of each page next to the text of the same page.
- The cause was **a single quotation mark** in the description of a diagram, in a place nobody looks at, because it is meant for screen readers.
- From that character onwards the minifier loses the plot: spaces at inline tags went missing, and so did closing tags.
  An anchor that is never closed, sitting on top of an entire post card, swallowed everything that followed, that was the overlapping text.
- The English version of the same diagram came through intact.
  Not because it was better.
  It used two straight quotation marks: an even number, nothing left dangling.
- **None of this is specific to a blog.** It takes no Hugo, no Markdown and no agentic AI building a website.
  All it takes is a pipeline with a step that only runs in CI, where it goes by bundler, compression or image build instead.
- The fix is not the quotation mark.
  The fix is to remove the asymmetry: the CI stage now runs on my machine too, before every deploy.

---

## Two symptoms

The first one showed up in body text.
Where a bold sentence ending ran into normal text, the words stuck together: `…bottom right` and `are the reason` with nothing between them.
Not everywhere, but often enough that a typo was not a plausible explanation.

The second one was cruder.
Further down the page, blocks of text lay on top of each other, half hidden, in a way no browser window accounts for.

Both symptoms have the same handwriting: they look like layout.
Missing spacing and overlapping blocks — that is the kind of damage you go looking for in CSS.
That is exactly where I looked first.

## The plausible explanation that is wrong

It was not CSS.
No theme update, no changed rule, no font that had failed to load.

And then comes the part where debugging normally grinds to a halt: the source is flawless.
In the Markdown every space sits where it belongs.
The local Hugo server shows the page the way it was meant to be: no missing spacing, no overlap, nothing.

Keep searching at that point and you are searching the source for an error that is not in it.
You can do that for a long time.

## The stage you cannot see

The mistake hides inside a sentence I had said to myself several times: *it looks fine locally.*

Locally, Hugo builds the blog the way I wrote it.
CI builds it with `--minify`: the minifier throws away whitespace, shortens attributes, and omits closing tags wherever HTML does not strictly require them.
That is the standard route for production builds, not an exotic setting, and in this blog it had been in the deploy workflow since the first commit.

So there are two different outputs.
The page I look at is not the page that goes on the web.
"Checked locally" is a statement about a different file.

That is the argument of this post, and it is more uncomfortable than the bug: every stage that runs on one side only is untested — no matter how often you look at the other side.

## One character

I did not find the spot by reading, but by comparing.
Build twice, once with `--minify` and once without, then put the plain text of each page against the plain text of the other.
Where the two diverge, the damage is, and you do not need to know in advance what the page was supposed to look like.

The text diverged inside the diagram that sits on top of the series landing page.
It is an inline SVG, and its description contained a phrase saying that something "keeps growing".
In the German version, that phrase was typeset the German way:

```text
„wächst weiter"
```

A German opening quote at the bottom of the line in front, a straight quotation mark at the back.
To a human being, a cosmetic slip.
To a parser, a single unpaired `"`, one that is missing its partner.

The English version of the same diagram came through intact.
It says `"keeps growing"`: two straight quotation marks, an even number, everything pairs up.
And the second diagram in the same series had the very same defect twice over, and survived for exactly the same reason.

So the error was not rare.
It just happened to be invisible most of the time.

## How one character opens an anchor

From the unpaired quotation mark onwards, the minifier loses the plot.
It takes text for an attribute value, and from there its idea of the document no longer matches what is actually written.

The first kind of damage is harmless and explains symptom one: at the edges of inline elements, whitespace disappears that the browser would have needed.
That is why a bold sentence ending and normal text ended up glued together.
It also hit the footer, which suddenly claimed the site was "Powered byHugo&PaperMod".

The second kind of damage explains symptom two, and for that you need to know one rule.
An element that closes itself — the slash before the closing bracket — really does close in SVG.
In HTML the same slash has no effect: an anchor written that way counts as open, not as closed.

That is precisely what happened to the anchors of the three post cards on the landing page.
Their closing tag went missing, the slash stood there looking like an ending without being one, and the anchor stayed open.

These anchors are not ordinary links in running text.
They are absolutely positioned across the entire card so the whole surface is clickable.
An anchor that is never closed swallows everything that follows: the rest of the page moves inside an element that is meant to sit on top of a card, and lies down with it over the text below.

That is the overlap.
One quotation mark, three cards, one wrecked page.

## The text nobody sees

The character was sitting in a `<desc>` element.
That is the description a screen reader announces when it reaches the diagram; on screen it is invisible.

Which makes it roughly the last place on the page where anyone would notice a crooked quotation mark.
People who look at the page do not see it.
People who read the page do not read it.
It is there for readers who cannot see the diagram — and therefore never gets checked by anyone else.

Invisible text destroyed the visible page.

That is more than a punchline.
Accessibility additions are almost always text with no audience in your own daily work: alt texts, descriptions, labels you yourself never lay eyes on.
What nobody looks at, nobody corrects in passing either.
I have argued elsewhere that [this kind of attention](/posts/shortcuts-as-an-input-aid/) pays off for everybody; here, its absence cost everybody.

## The same suspect, three days earlier

On 2 September, `--minify` had already wrecked something.
Back then it hit the JSON-LD block, in a test run with a different base URL.

The production build was not affected, so the finding was filed away as a quirk of the test setup.
The minifier had bared its teeth, and I let it keep running.

This is the part I would rather not write, and the reason it is here: it was not a lack of care.
The evidence had been on the table three days earlier, and it was classified correctly, as a special case of a test setup.
What was missing was not attention, but a place where that suspicion gets re-examined on a regular basis.
That is exactly what a human being who has already looked three times will not provide.

## Who wrote the line

The faulty line is not mine.
The shortcode for the diagram was built by my agent, screen reader description included.
The commit is its work, so is the push, and the link checker ran green on that same commit: 52 seconds, no errors.
It checked links, and the links were fine.

It was noticed by a human being looking at a page in a browser.

I am not writing this as an accusation.
A German quotation mark in a German sentence is exactly right.
In a place that runs through a minifier, it is the break.
What is interesting is the combination: the line was written quickly, it was plausible, it passed a green check, and the one check that would have caught it ran on the other side only.

## A test with no expectation

The fix is not the quotation mark.
That took a minute.

The fix is `tools/check-minify.py`: it builds the blog twice, with and without `--minify`, and compares the plain text and the tag balance of every page.
145 pages in under a second.
It runs locally before every release.
The stage that used to run only in CI now runs on both sides.

*Update, added 2026-09-11:* until that day the checker also ran in the deploy workflow; since then it runs on my machine only.

The remarkable thing about this checker is what it does *not* know.
It has no expectation.
It knows no rule about how the page should look, and it would never complain about an ugly layout.
All it demands is that two build results that must be identical actually are.

A differential test needs no oracle.
That is the part that transfers better than the quotation mark bug, and it is why a checker like this takes an hour to write instead of a week.

Two traps were waiting in it all the same, and both show that a checker itself has to be checked first:

- In SVG a self-closing element really closes; in HTML it does not.
  Without that distinction, the structural check reported 89 false alarms from the diagrams.
- Python's `HTMLParser` treats a self-closing anchor as closed — browsers do not.
  Had that stayed in, the very finding that caused the overlap would have slipped straight through.

I verified the checker by putting the defect back: quotation mark in again, run the checker, finding right there.
A test that does not demonstrably fire has proved nothing.

## What I learned

- **"Checked locally" is a statement about a different file** as soon as a stage sits between local and published that only one side knows about.
- **An error in the output does not have to be in the source.** Read only the source and you will never find it, and eventually you will call it magic.
- **Accidentally invisible is not the same as rare.** The same defect was sitting in the same files several times over; it only showed where the count was odd.
- **What nobody looks at, nobody corrects in passing.** Screen reader descriptions are a page's blindest spot, quite literally.
- **A green check proves only what it checks.** The link checker was right: the links were fine.
- **A comparison beats an expectation.** A test with no expectation needs nobody who knows in advance what it should look like — and finds the break anyway.

## What transfers

This looks like a blog story, and it is not one.
No part of it hangs on Hugo, on Markdown, or on an agentic AI writing along, that one only appears because it helped hunt the bug down.
It hangs on a single property of the pipeline: **one step runs on one side only.**

Run `npm run dev` locally and `npm run build` in CI, and you have it.
Build your container image in CI with different flags than on your laptop, and you have it.
Compress, minify, sign or rewrite your assets at deploy time only, and you have it.
The broken character is interchangeable; the asymmetry is not.

Go and see which stages of your publishing pipeline run on one side only.
Almost every project has at least one: a minifier, a bundler, a compression step, an optimisation that is switched off locally because it makes development slow.

That stage is untested, permanently.
Not because it is bad.
Because nobody looks at its output regularly.

The move that pays off is smaller than a test: build both once and compare the results against each other.
You do not need to know what the outcome should be.
It is enough to demand that the outcome is the same twice.
