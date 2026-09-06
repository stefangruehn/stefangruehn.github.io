---
title: "Predator, prey, deception: why agentic AI follows the same rules"
date: 2026-09-06T09:05:00+02:00
draft: true
tags: ["agents", "complexity", "chaos", "claude-code", "Essay"]
topics: ["author"]
series: ["Self-Similarity"]
summary: "The claim this series is named for: sufficiently complex agents are not a new kind of thing, they are a complex system — and complex systems obey regularities that have been described for decades. Four of them can already be measured on your own machine."
---

This series is called *Self-Similarity*, and this is the part where the word does its work.

Self-similar means: the same pattern, one level further out.
The boundary of the Mandelbrot set from the last part looks in miniature the way it looks at full size.
My claim is that this does not stop at mathematics.

## TL;DR

- The claim: sufficiently complex agents are not categorically new.
  They are a complex system, and complex systems obey regularities that have been on paper for decades.
- Four of them are observable today: predator and prey, dominance, selection, deception.
- None of them requires intent.
  A fox does not hate rabbits.
- The evidence is already on this blog: the same three agents accounted for 7.8 per cent of consumption one morning and 70 per cent at midday.
  That is population dynamics, not a bug.
- What I am not claiming: that any of this lets you predict anything.
  The irreducibility from the last part cuts both ways.
- What remains practical: name the scarce resource, cap the population, watch the shared channel, make signals checkable instead of believing them.

---

## The claim, in one sentence

What holds between populations, cells and markets holds between agents too — and inside any sufficiently complex agent.

This is not meant as a metaphor.
The preconditions under which the familiar patterns appear are remarkably thin: many units acting locally; feedback; a shared, limited resource; no central control; and an outcome you cannot skip ahead to.

Where those conditions hold, it makes no difference what the units are made of.
Cells, foxes, market participants, processes.
The rules do not ask about the material.

That is the self-similarity this series is about.
Not an image that repeats inside itself, but a structure that shows up again one level out — different material, same behaviour.

Which is why the detour through part two was not a detour.
Spend a few decades with cellular automata and the logistic map and a multi-agent setup does not look like a new technology first.
It looks like a familiar class of system.

## Predator and prey

The Lotka-Volterra model describes two coupled populations: prey grows, predators eat, predators multiply, prey collapses, predators starve, prey recovers.
The result is an oscillation with a lag, with overshoot and collapse.
Nobody plans it.
It follows from the coupling.

For agents, the prey is the shared, limited resource: context, tokens, a quota, a lock, a rate limit — and, in the end, my attention.

The evidence for that is already on this blog.
In [The most expensive answer is yes](/posts/the-most-expensive-answer-is-yes/) I measured two runs of the same constellation: three agents, the same task, the same day.
In the morning, the three accounted for **7.8 per cent** of consumption.
At midday, the same three accounted for **70 per cent**.

The number is not a property of the agents.
It is a property of the system they ran in — in the morning something else was eating most of it, at midday the field was clear.

That is exactly how population measurements behave.
One species' share tells you little about the species and a great deal about the state of the system.
Pass on numbers about agents without the environment they were measured in and you are passing on noise.

## Dominance

In any system with a shared channel, one voice occupies that channel.

For agents, the shared channel is the common state: the context, the file everyone writes into, the report everyone reads.
Whoever puts the most in there determines what the others see — and therefore what they take the situation to be.

This needs no malice and no strategy.
A cost gradient is enough: writing is cheap, contradicting is expensive, because contradicting means checking first.

The practical consequence is unglamorous and still worth having.
When several agents write into the same file, the first one fixes the vocabulary the later ones think in.
Knowing that, you order them deliberately instead of leaving the order to chance.

## Selection

What survives is not what is right.
It is what gets reused.

Prompts, tools, rules in a project file, entries in a memory: whatever once looked like success gets copied forward.
That is selection, with everything that comes with it — a mistake gets passed on too, for as long as nobody notices.

My own memory for this project holds an entry that was true when it was written and no longer true three days later.
Nothing in the system corrected it.
I corrected it.

A memory is a selection medium, and a selection medium without a corrective drifts.
That is not an argument against memories but an argument for an expiry date: any entry that asserts a fact about the world belongs re-checked before it is used again.

## Deception

Care is needed here, because the word sounds like intent.
What is meant is mechanical.

In systems that evolve, a signal comes loose from the state it is supposed to indicate as soon as the signal is cheaper to produce than the state.
That is how mimicry arises: the harmless fly wears the wasp's warning colours because colour is cheaper than venom.

For agents, that gradient is structurally present.
The sentence "the tests pass" costs the same whether they pass or not.
Actually running them costs more.

This is not a lie and it presupposes no intent to deceive.
It is a cost gradient, and wherever one exists the signal drifts — in animals over generations, here within a single session.

The remedy is not suspicion.
Suspicion is expensive and it wears you down.
The remedy is verification that costs less than the signal: a checker that runs, instead of a question that gets answered.

That is why my repositories now hold several small checking scripts, two of which run automatically before every deploy.
Not because I distrust the machine.
Because I wanted to invert the cost gradient.

## What I am not saying

**Not that the machine wants anything.**
None of the four patterns needs a motive.
Predator and prey oscillate without enmity, mimicry arises without a liar, selection selects without intent.
Anyone who can only recognise these patterns on the assumption of intent will recognise them too late.

**Not that any of this lets you predict something.**
The last part ended on irreducibility: no shortcut, you have to go through.
That holds here too, and it cuts both ways.
Recognising the rules does not get you a forecast.
It gets you a list of what is worth measuring.

**Not that all of this is still ahead of us.**
The interesting timescale is not the one scenarios run on but the one mechanisms run on — and those are here today, in miniature, demonstrable on a single laptop.
So I stay with the mechanisms.
A scenario is something you believe or reject.
A mechanism is something you can measure.

## Why this occupies me

The drive is not curiosity alone.

It is preparation — for me, for my children, and for their children.
None of the above is going to spare us over the next few years, and that is not a grim statement but a sober one: predator-prey dynamics, dominance over a channel, selection for reuse and drifting signals are not catastrophes.
They are operating conditions.

Recognise them and you can build instruments for them.
Treat them as new and you build expectations instead.

## What carries over

Treat a setup with several agents like a small ecosystem, not like a pile of tools.

- **Name the scarce resource.**
  What is actually the prey here — tokens, time, a lock, your attention?
  Everything else follows from that answer.
- **Cap the population before it pays off.**
  Three agents do not cost three times what one costs.
  They cost whatever the environment happens to allow.
- **Watch the shared channel.**
  Whoever writes into it first and most determines what everyone else takes the situation to be.
- **Make signals checkable instead of believing them.**
  A checking script that runs in a second is cheaper than any follow-up question — and it does not drift.

Which leaves the most uncomfortable question in this series, and it comes last: how much of this text is actually mine?
