---
title: "The silky sound of mechanical arithmetic: where the material comes from"
date: 2026-09-06T09:00:00+02:00
tags: ["chaos", "complexity", "hardware", "books", "Essay"]
topics: ["author"]
series: ["Self-Similarity"]
summary: "A Rubik's cube, four rules about neighbouring cells, a formula three symbols long, and a calculating machine you turn by hand. Four objects that all show the same thing, and one sentence from my own notes that I had to write out in full to get there."
---

A calculating machine once gave me gooseflesh.
That is an odd sentence, and it is the shortest route to what this blog is actually about.

## TL;DR

- Four objects set the direction: a Rubik's cube, Conway's *Life*, the Mandelbrot set, and a Curta.
- All four share the same property.
  A handful of rules that yield far more than they look like they contain, and no way to skip ahead to the result.
- Two books turned that into a concept: *Gödel, Escher, Bach* and *A New Kind of Science*.
- The sentence that holds it all together fits on one line: x → r · x · (1 − x).
- Getting there meant writing out a sentence from my own notes.
  As short as I had jotted it down, taken literally it was wrong — and the full version is the more interesting one.
- None of this is nostalgia.
  It is the toolkit I bring to agentic AI in the next part.

---

## Four objects

**The cube.**
Six faces, a handful of legal turns, some 43 quintillion reachable positions.
Out of almost nothing comes a space nobody can search.
Which is why you do not solve a cube by searching but by procedure: short sequences of moves that change exactly one thing and leave everything else the way it was.
Long before I knew the word, that was my first encounter with an algorithm.

**Conway's *Life*.**
The late eighties, my first own PC, Turbo Pascal, 5¼-inch floppies.
Four rules about when a cell lives and when it dies, and they depend on nothing but the number of living neighbours.
Out of those four rules fall gliders that travel across the grid, blinkers that beat in time, and constructions that build other constructions.
Not a word of that is in the rules.
You only see it once you let it run.

**The Mandelbrot set.**
z → z² + c, a single expression with a few lines of code around it.
The boundary is infinitely fine; you can zoom in as far as you like and keep finding structure, keep finding the whole thing again in miniature.
On the machine I had back then, an image at a useful resolution took long enough that you could leave the computer alone with it.
It was the second program I ever wrote, and the first whose output I had not foreseen.

**The Curta.**
That one gets its own section.

## An algorithm you can turn by hand

The Curta is a mechanical calculator small enough to hold in one hand, built around a stepped drum.
Curt Herzstark designed it; the decisive drawings were made while he was imprisoned in the Buchenwald concentration camp.
It went into production in 1948 at Contina AG in Liechtenstein.

You dial in a number, turn the crank, and inside, the arithmetic runs through the gears.
You can hear it while it happens.
It is a silky sound, very even, and you feel it in your hand as a fine vibration until it clicks home at the end of the turn.

The gooseflesh was not nostalgia.
It came from realising that a procedure can be an object.
An algorithm you can pick up, turn, and hear working — no power, no screen, and not one place where you would have to take its word for anything.

## Two books

*Gödel, Escher, Bach* by Douglas R. Hofstadter, 1979.
A book about recursion, self-reference and strange loops, and about how meaning can arise out of rules that mean nothing themselves.

*A New Kind of Science* by Stephen Wolfram, 2002.
The systematic version of the same thing: elementary cellular automata, numbered and worked through one after another — and among them rule 110, which turns one line of prescription into patterns you would never guess from the line.
That book is also where this series gets its key term: *computational irreducibility*.
For some processes there is no shortcut.
If you want to know how they come out, you have to let them run, step by step.

What both books left me with, above all, was astonishment at the sheer mental reach of their authors.
That I write Wolfram code for data analysis today is not a coincidence; it is a very long wire running from that book to my working day.

I dreamt about cellular automata for nights on end.
That is not a figure of speech.

## The one line

If I had to compress all of it into a single line, it would be this one:

    x → r · x · (1 − x)

The logistic map.
It describes how much of something there is next year given x of it this year: growth, multiplied by its own limit.
Two ingredients, one line.

For small *r* it settles on a fixed value.
Turn *r* up and at some point it starts alternating between two values, then four, then eight.
The gaps between those doublings shrink at a fixed ratio, the Feigenbaum constant, roughly 4.669.
And then, shortly after, it is chaos: no period, no return, and two starting values that differ in the eighth decimal place come apart completely within a few dozen steps.

Robert M. May wrote this up in *Nature* in 1976, under a title that still says everything: *Simple mathematical models with very complicated dynamics*.

### Where I have to be more precise

My notes for this post contained the claim that the logistic equation "still cannot be simulated or even adequately represented, all our computing power notwithstanding, except by the formula itself".

As noted, that is too short.
Taken literally it would be wrong: any pocket calculator can iterate the equation, as often as you like.

What it meant was two statements, each of which holds on its own.
First, for general *r* there is no closed-form solution that computes x after n steps directly; known exceptions such as *r* = 4 stay exceptions.
Second, with finite precision the specific trajectory is not predictable in the long run, because every rounding error grows along with it.

The second one is what I meant: "except by the formula itself" says there is no way past the steps.
The term that covers both is Wolfram's again: no shortcut.
You have to go through.

Written out, that is the stronger claim, not the weaker one — which is why this passage is here instead of the sentence I had abbreviated.

## What carries over

When people want to understand something complex, they look first for the formula that predicts the outcome.
For the systems this series is about, that formula does not exist.
What exists is the rule that produces the outcome.

The difference is entirely practical.
A prediction is something you can believe or doubt.
A rule is something you have to run while measuring it.

That is why so many posts on this blog end in a measurement rather than an explanation.
And it is the bridge to the next part: the same rules that govern a cellular automaton show up again the moment sufficiently complex agents start dealing with each other.
