---
title: "Typos are cheap: what actually matters when you talk to Claude Code"
date: 2026-09-04T00:23:36+02:00
draft: false
tags: ["claude-code", "rookie", "workflow"]
summary: "Over one continuous stretch of sessions I typed some four hundred messages to Claude Code, and one in ten contains a German umlaut. Nothing was ever corrected, and everything was understood anyway. What costs you is not the spelling — it is the sentence that allows two outcomes."
---

## TL;DR

- I type fast and sloppily: no umlauts, swapped letters, missing words.
- Counted over one continuous stretch, with more than a hundred messages on the busiest day: one message in ten contains an umlaut. That is 10.3 per cent.
- None of it was ever remarked upon. All of it was understood anyway.
- What creates work is not the wrong spelling. It is the sentence that allows two different outcomes.
- A single word can carry an entire claim. A clean replacement is then formally right and factually wrong.
- The rule that resolves both: say what should be **true afterwards**, not which text you want swapped.

---

## Ten per cent

I type on a US keyboard.
Many German developers do, and the reason is unremarkable: `[ ] { } \ | @ ~` sit there unshifted or behind Shift, while a German layout puts them behind AltGr.
On a German layout the backtick and the acute accent are dead keys as well — you press them twice, or follow them with a space.
Anyone writing paths, code blocks and command-line options all day pays that tax on every line.

The price is the umlauts.
I have a compose key set up, on the right Ctrl: compose, then `"`, then `a` gives ä.
Three keystrokes instead of one.
Most of the time I cannot be bothered.

"Most of the time" was a feeling, so I had it counted.
The count covers one continuous stretch across every project, with more than a hundred messages on its busiest day.
Some four hundred messages from me, 43 of them with at least one umlaut.
Ten point three per cent.
The word I write instead most often is `fuer` — forty-eight times.

In not one of them did anything come back suggesting I spell it differently.

## Why a swapped letter costs nothing

In those sessions I wrote "haeufugen", "beginen", "teiner", "vu verwenden".
None of it produced a question, and none of it was misread.

The reason is unromantic: in each case only one word can be meant.
"haeufugen" sits in a sentence about my typos, which makes it "häufigen" with no guesswork involved.
Language carries enough redundancy that a slipped letter does not take the meaning with it.
The surrounding sentence holds it.

So a correction would have cost me attention and gained nothing.
It would have pulled the focus from the matter to the spelling, in the middle of work where the matter is the expensive part.

This is not leniency and not a character trait, but a default.
Say "please correct my German along the way" and it gets corrected from then on.
The other direction holds too: there is nothing you need to tighten up for while typing.

## Two readings cost you immediately

One evening in September I wrote this:

> der technical deep dive tag sollte immer mit grossbuchstaben beginen

"beginen" went unmentioned.
A question came back anyway — about something else entirely: should it read *Technical Deep Dive* or *Technical deep dive*?

That is fair.
"Beginning with capital letters" allows both, and the tag sits on six posts in two languages.
Two readings, two different results, one round of work between them.

The typo in that same sentence was irrelevant.
The ambiguity was not.
That is where the line runs — not between tidy and sloppy writing, but between one reading and two.

## A word that carries a claim

The expensive kind looks harmless, because it is cleanly written.

Picture a manual containing this sentence:

> The service writes no **personal** data to the log.

You find "personal" too bureaucratic and would rather read "sensitive" everywhere.
So you say: *replace "personal" with "sensitive" throughout.*

The instruction is unambiguously executable.
Four occurrences, four replacements, no mistake among them.
Three are harmless: a heading, a bullet point, an explanatory sentence.

The fourth sat inside a negation, and there it tips over:

> The service writes no **sensitive** data to the log.

That is a different statement.
It can be false while the old one was true — the service may well write names and identifiers to the log, just nothing anyone would call sensitive.
Nobody got anything wrong here: the replacement was correct, and afterwards the sentence was not.

The mistake was in the instruction.
It named a **string** and meant a **result**.

A typo in that instruction, by the way, would have changed nothing.
"replce personal with sensitive everywhere" would have been carried out just the same, ending in the same false sentence.

## How to spot it beforehand

Three places where a single word carries more than itself:

- **Negations.** "no", "not", "never", "without". The negated word is the claim.
- **Comparisons.** "faster than", "more than", "the only". Swap what is being compared and the comparison becomes a different assertion.
- **Restrictions.** "only", "just", "except", "from … onwards". They fence something in, and what is fenced hangs on the word.

If your search term sits in one of those places, the second sentence is worth it.
It is no longer than the first, it just describes something else — the state rather than the action:

> I want the manual to say "sensitive" throughout, except where a statement depends on the data being personal.

That is no longer an instruction anyone can follow blindly.
It forces every occurrence to be read, which was the point all along.

## Lessons learned

- **Spelling mistakes are free.** They cost nothing because the context carries the meaning. Tightening up while typing is saving in the wrong place.
- **Unambiguous is not the same as correct.** A grammatically clean sentence can allow two outcomes; a hastily typed one can allow exactly one.
- **Count the readings, not the errors.** If your own sentence could produce two different results, you will either get a question or get a guess.
- **State the condition, not the operation.** "Replace X with Y" can be executed. "Afterwards it should hold that …" can be checked.
- **Negations are the most dangerous spot in any text.** There a single word carries the whole claim, and a correct replacement turns it into a different one.

## If you're facing the same question

You are starting out and wondering how carefully you have to phrase things.
The answer has two halves, and the pleasant one comes first.

1. **Type the way you type.** Dropped umlauts, swapped letters, changing direction mid-sentence — none of it needs to slow you down. It costs nothing.
2. **Read your instruction once more, with a single question in mind:** can this turn out two ways? Not: is this nicely written.
3. **If it can, name the result.** One sentence describing what should be true afterwards is worth more than three cleanly phrased commands.
4. **Watch negations, comparisons and restrictions in particular.** That is where the meaning sits in a single word.
5. **Answer the question when one comes back.** It is not a reproach; it is the cheapest point in the whole process.

So the effort is not where beginners expect it.
It is not in the spelling and not in the grammar, but in one single question you can ask yourself before any larger instruction.
And you can ask it with your letters in the wrong order.
