---
title: "Shortcuts as an input aid: when the parser forgives the errors the hand makes"
date: 2026-09-05T12:00:00+02:00
draft: false
tags: ["claude-code", "workflow", "shortcuts", "accessibility", "Field Notes"]
series: ["Codebook"]
summary: "The first version of my shortcut list used round brackets — which made it wrong for exactly the case where saved keystrokes matter most. The fix was meant as a second form for hard cases. It has since become the main form for everyone."
---

Part one measured what shared context [costs](/posts/the-most-expensive-answer-is-yes/).
Part two [built a codebook](/posts/a-codebook-from-my-own-corpus/) out of it.
This part is about the people for whom that codebook is not a convenience.

## TL;DR

- My first shortcut list used round brackets.
  Those need Shift — a held modifier plus a second key.
- That is the most expensive movement there is for anyone whose hand does not land precisely.
  The list meant to save typing was built wrong for exactly the case where saving typing matters most.
- The fix was an unshifted form: `[x]` instead of `(x)`.
  Three keystrokes with no modifier instead of four with two Shift holds.
- The real idea is not brevity but **tolerant parsing**: the parser forgives exactly the errors an imprecise hand produces.
- The bigger lever is fewer inputs rather than shorter ones anyway.
  It is cheaper for the agent to guess and me to correct than for it to ask and me to answer.
- And the punchline is at the end: the second form for the hard case has become the main form for everyone.

---

## The design flaw

The first list looked like this: `(?)` for "interview me", `(i)` for "file this as an idea", `($)` for "take the frugal route".

Round brackets look tidy.
On my US keyboard they cost Shift, and Shift is not a keystroke like any other.
It is a modifier that has to be **held** while a second key is hit.

For most people that is not worth mentioning.
For someone with tremor, dystonia or another movement disorder, that combination is the most expensive movement on the keyboard — which is why "sticky keys" exists as an operating-system setting in the first place.

So the list was built past its own justification.
It was there to save keystrokes.
For the person to whom every keystroke matters most, it demanded the worst one.

The fix is banal: `[x]` counts the same as `(x)`.
On a US layout the square brackets sit next to each other, unshifted.
Three keystrokes, no modifiers.

## The errors are predictable

The bracket shape was the obvious part.
The more interesting part sits one level down.

A hand that does not land precisely does not make arbitrary errors.
It makes the same four over and over: a key repeats because it was held too long; a stroke arrives twice; the neighbouring key gets hit; the closing bracket never comes.

So the parser forgives exactly those four.
All of this is the same token:

```
[i]    (i)    [[i]    [i]]    [ i ]    [ii]    [i
```

The sentence this is all about sounds obvious and historically is not:

> An input aid for a movement disorder should forgive exactly the errors that disorder produces.

Classical input aids cannot do this.
A text expander, a macro, a key combination — all of them need exact input, because their parser has to be exact.
One wrong character and nothing happens.
You notice, you correct it, you type it again, which often enough reproduces the error.

In front of a language model that requirement disappears.
It has a prior: what was meant can be reconstructed from the sentence around it.
It degrades gracefully instead of failing — the same property that makes [typos cost nothing](/posts/typos-are-cheap/) in the first place.

That shifts the design goal.
It is no longer about an unambiguous grammar but about **recoverable intent**.
And the tolerance has to be written down, or it only happens by accident: which errors get absorbed is part of the list — along with the rule that an absorbed error is never remarked on.

## The bigger lever: fewer, not shorter

Making the input shorter is the obvious gain, and the smaller one.

The bigger one is reducing how many inputs are needed at all.
If you pay for every keystroke, a round of questions costs more than a wrong first attempt — it is cheaper for the agent to guess and me to correct than for it to ask and me to answer.

Which is why `[$]` of all things — "take the shortest route, even at the cost of thoroughness" — is an input aid.
It does not say "be faster".
It says: "don't ask me three more times."

And here this post meets part one in a way I had not planned.
There the finding was: a question costs one full pass over the entire conversation, however short the answer.
Here the finding is: a question costs keystrokes somebody may not have.

Two completely different arguments — one economic, one physical — and both land on the same optimisation.
When two independent arguments point at the same design, that is the strongest signal you are going to get.

## A pause needs a token too

A shortcut list usually describes work instructions.
The most obvious thing was what I was missing longest: the stage directions around them.

```
[m]   One moment — please hold off, I need a short break and will be right back.
[b]   I'm back, we can carry on.
```

`[m]` means: start nothing new, kick off no long run, acknowledge briefly and wait quietly.
`[b]` picks the thread back up without my having to restate where we were.

Two keystrokes for something that otherwise takes two sentences.

Someone who can choose their breaks freely simply takes one.
Someone who cannot has to announce it — and pays for the announcement with exactly the resource that is scarce at that moment.
Having a token for that is not a convenience.

Incidentally it is token economics again: the waiting should not cost a turn.
The same optimisation, for the third time, from a third direction.

## An old field with a new target

None of this is my invention.
The field is called AAC — augmentative and alternative communication — and the sub-family is *abbreviation expansion*.
Word prediction, letter boards, systems like EZ Keys or Dasher: this has been researched and built for decades.

Exactly one thing is new.
Until now the target of an abbreviation was always a **string** — a word, a sentence, a paragraph.
Which meant the compression ratio was bounded by the length of the text you wanted to end up with.

Now the target is an **instruction to an agent**, and that bound falls away.
`[s]` is three keystrokes and half an hour of work.
For someone whose body can take only a fixed number of keystrokes a day, that is more than an incremental improvement.

## What is not evidenced here

These are design arguments, not a user study.

I have not measured error distributions in anybody else's typing, questioned test subjects, or read a study quantifying the four error classes named above.
What I have is a list built along those assumptions, and the observation that it pays off for the ordinary case as well.

Anyone making more of that is making too much of it.

## The second form became the main form

`[x]` was meant as a second form.
The actual notation was going to stay `(x)`, and the square bracket would have been the variant for people to whom holding Shift is expensive.
Special case, side entrance, well meant.

It replaced the round form the same day.

Not out of consideration, but because it was simply better: one key instead of two, the same meaning, nothing given up.
The round form still counts — it is just not the one anybody writes in any more.

That is the curb cut effect, on fast-forward.
Dropped kerbs were built for wheelchairs, and today everyone with a wheeled suitcase, a pram or a bicycle uses them without sparing it a thought.
Only there, the road from special case to default took decades and a lot of concrete.

Here it took an afternoon, because a codebook is negotiable rather than poured.

Which turns the opening around too.
The design flaw was not that the list had forgotten a special case.
It was that the list had been built past its own point — and the correction aimed at the special case turned out to be an improvement for everyone who does not need it.

## Lessons learned

- **For every abbreviation, ask what it demands of the hand.**
  Not just how many characters it saves. A held modifier costs more than an extra keystroke.
- **Tolerance has to be written down.**
  A model forgives a lot anyway. Which errors it *should* forgive — and that it never remarks on them — is written nowhere else.
- **Count the turns, not the characters.**
  The most expensive input is the one that only became necessary because an answer was missing.
- **Two independent arguments for the same design beat one good one.**
  Here the token arithmetic and the economics of movement point at the same rule.
- **The exception can be the better default.**
  If the variant built for the hard case is better in every case, it was never a variant.

## What transfers

All of this is about a shortcut list, but the move behind it is more general, and it works at any interface somebody operates with their hands.

**Build in the tolerance, not the precision.**
Don't ask how to make your input unambiguous; ask which four errors your users actually produce — and absorb exactly those, silently.

**Count interactions, not clicks.**
A form with fewer fields is good. A form that never appears because the answer was derivable is better.

**And when you build an accessible variant, look at it again.**
If it is better for everybody else too, it is not a variant.
It is what you should have started with.
