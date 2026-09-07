---
title: "The smallest change is two: what 57 commits say about this blog's coupling"
date: 2026-09-07T02:17:00+02:00
draft: false
tags: ["claude-code", "workflow", "complexity", "chaos", "measurement", "self-reference", "Essay"]
topics: ["writing"]
series: ["Feedback"]
summary: "In seven days, 39 post files were created and 86 existing ones changed. Most changes touch two files; one touched eighteen. That distribution is why a blog behaves like a coupled system — and it marks the place where I adjust it in passing."
---

The smallest possible change to this blog is two files.
There is no change in one place, because every post is bilingual.

## TL;DR

- Counted across 57 commits from 31 August to 6 September: 39 new post files, 86 changes to existing ones.
  The existing text was worked on more than twice as often as the new.
- 29 of the 57 commits touch no existing post at all.
  When one does, it touches 3.1 files on average, 2 at the median — and once, 18.
- The 18 come from a single decision: to make topic pages the first entry point.
  One sentence in conversation, eighteen posts in the commit.
- What I adjust in doing that is not the pace but the coupling.
  Every structural decision permanently raises the number of places a later decision has to touch.
- That puts three of the four ingredients in place that turn a loop into an oscillation: feedback, delay, amplification.
  The fourth would be a limited resource, and that one is measured: 7.8 per cent in the morning, 70 per cent at midday.
- What is not measured here: chaos.
  Seven days are not a time series, and a count of changed files is not a population.
- What could be measured is at the end: the ratio of maintenance to new work, over weeks rather than days.

---

## The count

The first commit is on 31 August 2026, the last one in this count on 6 September.
57 commits lie between them.

They create 39 new post files — which, because every post exists twice, is just under twenty posts including drafts.
And they change existing post files 86 times.

The ratio is surprising at first glance: for every newly written file there are a good two changes to already written ones.
From the outside, a blog in its first week looks like a collection that grows.
From the inside it is two thirds rebuilding.

Per day it looks like this:

| Day | new | changed |
|---|---|---|
| 31 Aug | 3 | 3 |
| 1 Sep | 0 | 8 |
| 2 Sep | 6 | 14 |
| 3 Sep | 6 | 24 |
| 4 Sep | 0 | 2 |
| 5 Sep | 6 | 3 |
| 6 Sep | 18 | 32 |

On 3 September, six new files come with 24 changes; on 5 September, six new files come with three.
Same blog, two days apart, with a ratio that jumps by a factor of eight.

## How far a change reaches

More interesting than the total is how the 86 spread across the commits.

29 of the 57 commits touch no existing post at all: new posts, layout work, tools, configuration.
Among the rest, the median is 2 and the mean 3.1.

The median of 2 is this blog's ground note.
Two means: German version, English version, nothing else.
A correction to one sentence is never one change here, it is always two.

{{< ausbreitung >}}

The five largest excursions look different:

| Files | Occasion |
|---|---|
| 18 | making topic pages the first entry point |
| 8 | publishing the series and fixing the ordering |
| 7 | writing "KI" instead of "AI" on the German pages |
| 6 | letting the closing headings say what each section does |
| 4 | grouping the two laptop posts under a shared tag |

None of those five occasions is a post.
All five are decisions about form, and every one of them touched more posts than were written that day.

## The parameter

The sentence that started the 18 was not a technical instruction.
It amounted to this: readers should not be met by a list ordered by date, but by questions — what is actually at stake here.

A rule follows from that wish: every post belongs to exactly one topic, and every topic has a page.
Eighteen post files had to acquire a field for it.

That is the one-off price, and it is not the point.
The point is the standing one: since that day, every new post is coupled to the topic ordering.
Rename a topic page and you touch everything hanging off it.
Split a topic and every post needs deciding again.

The same holds for series.
A series is not just a field in the front matter; it has a page saying what the individual parts do.
Change one part and that description no longer holds.

I did not decide those couplings as couplings.
I said what I wanted for the reader, and the coupling was the consequence.
That is exactly what adjusting a parameter in passing means: the sentence is about how readers arrive, its effect is on how densely the system is wired.

## Three of four ingredients

For a loop to swing rather than settle, four things are needed.

**Feedback.** Documented: the bracket rule sits in the file the next session reads.

**Delay.** Documented: a rule applies from the next session, a hook from the next start.
Between insight and effect there is always at least one cut.

**Amplification.** Measured: the median is 2, the maximum 18.
An amplification factor swinging between two and eighteen is not linear.

**A limited resource.** Measured too, elsewhere: [the same three agents](/posts/the-most-expensive-answer-is-yes/) accounted for 7.8 per cent of consumption in the morning and 70 per cent at midday.
Nothing new lay in between except a larger context.

Four out of four.
That is not nothing, and it is not proof either.

## What these numbers do not show

They do not show chaos.

The logistic map, where that would show, demands a repeated measurement of the same quantity over many steps: x today, x tomorrow, x the day after, and then you see whether it settles, oscillates or flies apart.
57 commits over seven days are too few for that, and "changed post files per commit" is not a population that limits itself.
It is a by-product of how I work, not a state of the system.

The peak at 18 is not an excursion in the oscillating sense either.
It is a one-off retrofit, the kind any project sees when an ordering principle gets added late.

What the numbers do show is more modest and still worth noting: that the conditions are met.
Whether the system makes use of them is something only a longer measurement can say.

## What could be measured

The quantity I consider meaningful is the ratio of changes to existing files against new files, measured per week rather than per day.

If it stays around two to one, the rebuilding is healthy maintenance.
If it climbs over several weeks, structure is eating the writing: the work goes into ordering the existing texts instead of new ones.
If it falls towards zero, the ordering has frozen — also not a good sign, just a different one.

The number sits in every repository; it only has to be computed once.
In seven days I will know more; today's count is the starting value I will compare against later.

## Lessons learned

- **The smallest change is rarely one.** Bilingualism turns every finding into two edits. That is not an annoyance but the system's base amplification, and worth knowing before estimating effort.
- **Structural decisions cost twice.** Once at installation, visible in the commit. And then permanently, invisibly, in every post created afterwards.
- **Talking about the reader is deciding about coupling.** The sentence sounded like design and was a statement about wiring density.
- **The conditions for an oscillation are met more easily than it looks.** Feedback, delay, amplification and a scarce resource — four things a blog of fourteen posts already has in place.
- **Conditions met is not effect demonstrated.** Keeping those apart is the whole difference between a measurement and a good story.

## What carries over

If you want to know how tightly your own project is coupled, you need no theory, just a line of analysis: count, for each commit, how many existing content files it touches, and look at the median and the maximum.

The median tells you what an ordinary change costs.
The maximum tells you what a decision can cost.
If the two are far apart, you have a system in which rare decisions are expensive — and in which pausing before the next one pays.

The number itself is harmless.
It gets interesting when you compute it again in four weeks.
