---
title: "A post becomes a rule: how this blog writes the way it gets written"
date: 2026-09-07T02:15:00+02:00
draft: false
tags: ["claude-code", "workflow", "writing", "recursion", "self-reference", "Essay"]
topics: ["writing"]
series: ["Feedback"]
summary: "A post about my keyboard shortcuts did not only describe how I work — it changed it. The correction now sits in the file my agent reads at the start of every session. Which makes this blog one of the things it reports on."
---

Yesterday Claude explained to me that several passages in this blog change at the same time when it works on structure and content after a conversation with me.
I had asked a technical question and got a technical answer.
The sentence describes more than it answers.

## TL;DR

- The sentence sounds like tooling trivia.
  It is a statement about how this blog is built: an intention of mine does not land in one place, it lands in several at once.
- The first case is harmless.
  On 6 September a series got a new name; four files in two languages had to follow, two of them directories.
  That is coupling, the way any software project has it.
- The second case is not harmless.
  A post about my keyboard shortcuts changed the file Claude Code reads at the start of every session.
- Which means this blog is no longer only a report about how I work.
  It is part of how I work.
  The Chuwi laptop does not get quieter because I write about its speakers — the shortcuts, by contrast, change the machine that produces the next post.
- The loop has five steps.
  On 5 September thirty minutes lay between the two posts, and the rule applied the same day.
- What is not being claimed: that the blog writes itself.
  Every turn of the loop passes through a decision of mine.
- What is new is not the feedback.
  Manuals, wikis and tooling repositories have had it for decades.
  What is new is its cycle time, and the fact that the rule is a sentence in prose rather than code.

---

## The first case: a name

On 6 September 2026, at 9:30, a series on this blog was still called *The Same Rules*.
After that moment it is called [Self-Similarity](/series/self-similarity/).

At that point the old name sat in four places: in both language versions of the first part, and on the two series pages.
Two of those were not passages of text but directories, because in Hugo the directory name is the address.
And since the blog is bilingual, every name exists twice — a German one and an English one, spelled differently and addressed differently.

Publishing added more.
Four texts only read as one text if they have an order, so two new layout files appeared, along with entries in both translation files.
Before that, the series was a field in the front matter of four posts.
Afterwards it was a page of its own with navigation of its own.

Nothing remarkable about it yet.
Every software project knows it, it is called coupling, and it is the reason renaming has a reputation for being dangerous.
One name in one place, effects in many — which is why programs carry names for years that nobody considers right any more.

## The second case: a bracket

On 5 September two posts on this blog are half an hour apart.

At 11:30 came [A codebook from my own corpus](/posts/a-codebook-from-my-own-corpus/).
It describes how my shortcut list came about: not guessed but counted, out of 764 distinct messages across 13 projects.
The most frequent word was `commit` with 28 hits, and the guessed list did not contain it.

At 12:00 came [Shortcuts as an input aid](/posts/shortcuts-as-an-input-aid/).
The occasion was a design flaw that surfaced while the first post was being written: the list used round brackets.
Round brackets need Shift — a held modifier plus a second key, exactly the most expensive input for any hand that does not land accurately.
A list meant to save typing was built wrong for the case where that matters most.

The correction is square: `[x]` instead of `(x)`.

And this is where the resemblance to the first case ends.
The correction did not stay inside the post.
Since that same day it sits in `CLAUDE.md`, the file Claude Code reads at the start of every session.
What sits there is not only the new form but also the sentence that the agent itself should write square brackets, in replies as in documentation.

## The difference

Three posts on this blog are about a Chuwi laptop and its speakers.
The laptop takes nothing from that.
It gets neither quieter nor louder because somebody writes about it; the text sits beside the thing it reports on.

With the shortcuts it does not sit beside it.
The rule stated in the post is also the rule in the file that steers the next session.
The post does not describe how I work — it sets how I work.

The loop has five steps:

1. I work with an agent. Transcripts accumulate as a by-product.
2. The transcripts get counted for instructions I repeat. That count becomes a shortcut list.
3. The list becomes a post. While writing it, a flaw in the list surfaces.
4. The correction goes into `CLAUDE.md` and applies from the next session onwards.
5. The next post comes about under the new rule — and produces transcripts again.

{{< schleife >}}

On 5 September thirty minutes lay between the two posts, and the rule in step 4 applied the same day.

## The rule is a sentence, not code

Programs that change themselves are old.
A Makefile that generates a Makefile, a formatter that formats its own source, a compiler that compiles itself: all of that has been around for decades, and nobody calls it alive.

The difference is the material.
`CLAUDE.md` is not a configuration format.
It is prose — German prose, in my case — with reasons, examples and a table, and the reasons do work of their own: they tell the agent not only what applies but why, which is how the rule reaches cases nobody anticipated when writing it.

That makes one and the same sentence two things: readable text and effective instruction.
Anyone reading the shortcut post reads roughly what the agent reads.
Between what is explained here and what steers here, there is no translation step left — and that is the real difference from every manual I have ever written.

## What is not being claimed

The blog does not write itself.

Each of the five steps above passes through a decision of mine.
I decided to count the transcripts.
I noticed the design flaw — more precisely: it surfaced while I was talking about the list, and I decided it mattered more than the post I was writing at the time.
I decided the correction belonged in the rules file and not only in the text.

Without those decisions the loop does not turn.
It has not become automatic; it has become cheap.
That distinction goes missing easily, and it is the whole distinction.

The cycle time is not that short everywhere, either.
It was short for the shortcuts because observation, post and rules file happened to be on the same screen on the same afternoon.
For a rule that only turns out to be wrong after two weeks, the cycle is two weeks long.

## Lessons learned

- **There are two kinds of post, and you cannot tell them apart by looking.** One reports on something outside; the other changes the tool that produces the next one. The Chuwi laptop is the first kind, the shortcuts are the second.
- **A rule only takes effect once it sits in the place that gets read.** The same insight in a post is an anecdote; in `CLAUDE.md` it is behaviour.
- **Reasons belong in the rule.** A rule without a reason covers exactly the cases somebody wrote down. A rule with a reason also covers the ones beside them.
- **A short cycle changes the kind of system, not only its speed.** A loop that turns once per release goes unnoticed. One that turns twice in an afternoon is noticeable in everything.
- **Bilingualism is the amplifier.** Every decision that touches the text touches it twice. That is why one intention immediately becomes several simultaneous changes.

## What carries over

Anyone working with an agent already has this loop, whether they use it or not.
There is a file that gets read at the start of every session, and everything not in it has to be said again every time.

The step worth taking is small: next time something about your own work strikes you while you are working — a phrasing you needed three times, a question that comes back identical — do not put it in your notes, put it in the rules file.
With the reason, in full sentences.

The difference does not show up immediately.
It shows up a fortnight later, in the sentences you no longer type.
