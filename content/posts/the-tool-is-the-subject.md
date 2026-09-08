---
title: "The tool is the subject: when a blog writes about its own machinery"
date: 2026-09-07T02:16:00+02:00
draft: false
tags: ["claude-code", "workflow", "writing", "tooling", "self-reference", "Essay"]
topics: ["writing"]
series: ["Feedback"]
summary: "Of fourteen published posts, six are about tools that came out of working on this blog. That is not a choice of topic, it follows from where the material comes from, and it has a limit worth knowing about."
---

Fourteen posts are published here.
Six of them are about tools that would not exist without this blog.

## TL;DR

- Sounds, shortcuts, quota, note storage, questions back: six of the fourteen posts describe tools or procedures that came out of working on this blog.
- That is not a choice of topic.
  It follows from where the material comes from: what can be measured is what accumulates while working.
- Four checking programs and two measuring tools now belong to it, plus three self-tests that check the checkers.
  Every one of them exists because something had gone wrong.
- The purest case is a change request about the procedure for change requests.
  The field for the affected post stays empty there. What is affected is the procedure.
- There is a separate origin marker for suggestions nobody noticed while reading, but while working on the existing text.
  Only a system that observes itself needs one.
- The loop closes with a delay: a rule I enter today applies from the next session onwards.
- The limit is navel-gazing.
  Four posts hold against it, whose material comes from a laptop rather than from the work on the text.

---

## Six out of fourteen

The six are quickly listed: [why typos cost nothing](/posts/typos-are-cheap/), [what a usage limit measures](/posts/the-most-expensive-answer-is-yes/), [how a shortcut list comes out of your own corpus](/posts/a-codebook-from-my-own-corpus/), [why the brackets have to be square](/posts/shortcuts-as-an-input-aid/), [where half-finished notes are allowed to live](/posts/private-still-means-copied/) and [two sounds that turn waiting into leaving](/posts/call-me-when-you-need-me/).

Four more are about a laptop and its speakers, four are essays.

Six to four to four is not a ratio I planned.
It follows from a plain condition: I only write down what I can measure, and what I can measure is what accumulates while working.
What accumulates while working on a blog is how the blog gets made.

The baseline in the sounds post does not come from a study.
It comes from my own transcripts: 471 waits in two weeks, 20.2 hours in total, 14 per cent of them longer than five minutes, the longest 48.
The shortcut list comes out of 764 messages across 13 projects.
Both numbers are by-products.
They were not collected, they were lying there.

## Five checkers, two measuring tools, four self-tests

The tools directory of this blog and the neighbouring one next to it now hold eleven programs.

Five check: whether every post carries exactly one topic and every topic has a page; whether a series overview only goes public once none of its parts is a draft; whether minifying the output leaves the text untouched; whether the idea notes match the published state; whether the change requests point at anything real.
Two measure: token consumption across a session, the waits between my inputs.
Four check the checkers.

None of them was planned.
Each came about after something had gone wrong that you would have called impossible beforehand — a post that appeared on no topic page and was still missing nowhere, because a page that was never built leaves no gap behind.

The fifth arrived on 7 September: the overview page of a series stood online while all three of its parts were still drafts.
A series was announced; there was nothing to open.

And every one of them has been checking the blog that tells their story ever since.

## A suggestion about the procedure for suggestions

Change requests for published posts do not live in this repository but in a store of their own: one note per incoming request, front matter with status and channel, a section of replacements, an index.

On 6 September a request came in there that concerned the replacement pattern itself.
It proposed a second form next to the literal one, a paraphrasing form, because the literal one does not work away from the desk: reading on a phone, you do not have the text in front of you and rarely hit the wording.

The front matter of such a note has a field for the affected post.
It is empty.
What is affected is not a post but the procedure the note itself sits in — and the change rewrote the template that the next note gets created from, along with the checker and its self-test.

That is the same step as the brackets, one level further in.

## The marker only self-observation needs

Every note records where the suggestion came from: my own re-reading, a conversation, a messenger, an email, a discussion under the post.

One value in that list is unlike the others.
It is called `intern` and means: noticed while working on the blog itself, without anyone having read it.
Nobody looked at the text and stumbled; the system tripped over an inaccuracy of its own while working on something else.

Four of the eight notes so far carry that marker.
In one of them, the display surface of a rotary knob was called "glass" instead of "screen" in four places — across two posts, in two languages, found while rebuilding something else.

No blog that only publishes needs a marker like that.
It is needed once the same work that produces the text also checks it.

## The delay

The loop does not close immediately.

The sounds that call me hang on hooks, and hooks are read at session start.
Enter a hook mid-session and you do not have it in that session.
It applies from the next one.

The same holds for every rule in the rules file: entered now, read at the next start.
Between the insight and its effect there is always at least one session.

That sounds like a footnote and is not one.
Feedback without delay converges on a fixed value.
Feedback with delay can overshoot.

## Where the circle stops

A blog that writes about its own production has a foreseeable end: at some point everything is described, and what comes after that is posts about posts about posts.

Against that stand four texts about a Chuwi laptop, in which a good theory breaks against a measurement every single time, and an as yet unpublished series about a rotary knob with a screen, whose board carries two microcontrollers.
Their material does not come from working on the text.
It comes from a device that does not know anybody is writing about it.

Four out of fourteen is the counterweight at the moment.
The number is too small to be reassuring, and it stands here so that it stays checkable.

## Lessons learned

- **Tools that come out of your own work bring their measurements with them.** I had to collect nothing for any of those six posts. The numbers were in transcripts, logs and commits.
- **Checking programs are the cheapest part of a feedback loop.** They cost an hour and then find, every day, what would otherwise cost attention.
- **A procedure that admits itself as a subject is finished.** As long as there is no way to change the procedure by its own means, it is not one.
- **Self-observation needs markers of its own.** A finding while working is a different thing from a finding while reading, and filing both the same way loses the distinction exactly when it gets interesting.
- **The delay is the part you forget.** Not because it is hidden. It only registers once a rule has failed to bite twice.

## What carries over

The test is a single question: is there a way to change your procedure by the means of the procedure itself?

For a wiki that reads: is the page about creating pages in the wiki?
For a codebase: does the formatter run over its own source?
For a store of feedback: can a piece of feedback concern the store?

If the answer is no, that is not a fault — just a boundary, beyond which every improvement stays manual.
If it is yes, the delay is worth a second look: from when does what you just changed apply?
That number decides whether your system settles quietly or starts to swing.
