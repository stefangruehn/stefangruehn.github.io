---
title: "Language Follows Suit: What a Reader Who Takes Everything Literally Does to My Sentences"
date: 2026-09-19T11:00:00+02:00
draft: true
tags: ["claude-code", "language", "writing", "shortcuts", "Essay"]
topics: ["thinking"]
summary: "Since I started working with an agent every day, it is not only my thinking that has changed but my language too, and faster than ever before. It is getting more precise, poorer in contradictions, and it carries words from the work into everyday life. The direction is that of a programming language: syntax, semantics and pragmatics come apart, even where no agent is reading along."
---

## TL;DR

- Working with an agent has changed how I think.
  It has changed my language as well, faster than ever before and in a particular direction.
- The direction is that of a programming language.
  A counterpart that takes every word literally exposes mistakes a human reads past: a verb with no direction, a word with two meanings, an "is on hold" that does not say what it hangs on.
- My process now separates what linguistics separates.
  `->` means literal and is checked by a program, `~>` means paraphrased and is not.
  That is the line between syntax and semantics, and it grew out of practice.
- Some words have migrated from the work into everyday life: "it's on disk", "context", "diff", "paraphrased or literal".
- More precise does not mean easier to understand.
  A vocabulary sharpened against a single counterpart can drift away from everyone else's.
- Nothing becomes free of contradictions this way.
  Poor in contradictions is what can be achieved.

---

## Free or poor

When I noted down this idea, I wrote "contradiction-free" and after it, in parentheses, "(-poor?)".
The note corrected itself while it was being written.

Being free of contradictions promises something no text and no tool can deliver.
Being poor in them is within reach: fewer of them, and the remaining ones where you can find them.
The question mark in the parentheses is the observation this post is about, in miniature.
I did not use to write like that.

I have written about thinking [elsewhere](/posts/many-memories-one-person/): which memory lives where, now that an agent works alongside me.
This post continues it, on a different level.
It is about the language I think in and speak.

## A reader who takes you at your word

Claude Code reads my sentences differently from a human.
A human fills in what is missing and reads past what is crooked.
A language model fills in too, but it shows me what it filled in through its answer, and there I see what I actually said.

On the same day as the note, a sentence in the post linked above came up.
It read "My vault does not inherit into my head".
What I meant was: what is in the vault does not get into my head by itself, the way Claude's instructions are loaded automatically at the start of a session.
The sentence does not say that, because "inherit" has a direction.
You inherit from something, not into something.
That is a valency error, and it is exactly the kind of mistake a type checker finds: the verb expects an argument of one kind and gets another.
Today the sentence reads "My vault does not load itself into my head".
Since then, the style rules of this blog carry a note: a technical verb used as a metaphor keeps its direction.

Other cases from the same process have the same shape.
The German word "Laufzeit" means both how long a program runs and the environment that has to run alongside it.
One word, two meanings, like an overloaded identifier where only the caller decides which version is meant.
The German version of a post about Hugo, which ships as a single binary without such an environment, therefore says "Runtime" today.
And "Two weeks later I still know that an idea is on hold" became "that an idea is waiting".
"On hold" says that something is not moving.
"Waiting" says that it hangs on something, and that something was the point of the paragraph.

None of these mistakes would have stopped a human reader.
They stand out because I now read every sentence once the way a program would read it.

## Syntax, semantics and what is missing in between

The change requests for this blog have a small notation of their own.
On the left is the current passage, on the right the desired one, with an arrow in between.
There are two arrows.
`->` means literal: the left side is the exact text, and a checking script looks for it in the post.
`~>` means paraphrased: the left side is what is meant, and nobody checks it.

The distinction did not come from a textbook.
It grew because the literal form can be verified and the paraphrased one cannot, and because I wanted to know which lines the script could take over.
In hindsight it is the line between syntax and semantics.
A program can compare the form of a sentence.
What it means, it cannot.

The same line runs through the style rules of this blog.
Most entries are word lists and target values a script counts: dashes per thousand words, an anglicism where a German word is available.
Recently, notes have joined them that no script checks, because every pattern would be too narrow or too broad.
The rule about the direction of verbs is one of those notes.
Syntax can be measured, the rest is read.

In 1938 the semiotician Charles W. Morris distinguished three dimensions of signs: syntax, the relation of signs to one another, semantics, their relation to what they designate, and pragmatics, their relation to whoever uses them.
My process is missing the third, and that is exactly the level a prompt works on.
[The first task for this blog](/posts/the-task-named-the-tool/) was six words long, and one of them was already the answer to a question nobody had asked.
Syntactically the sentence was fine, semantically too.
What it did was neither in its form nor in its meaning but in its effect on whoever read it.

## A small language with a grammar

I give recurring instructions as [shortcuts](/posts/shortcuts-as-an-input-aid/): a character in square brackets, `[+]` for "commit", `[?]` for "interview me about this".
Over time a list of abbreviations has turned into a small language.
It has a binding rule (a shortcut applies to the sentence it stands in, at the end of a message to the whole message), an escape rule (a backslash in front means the character, not the instruction) and a precedence rule: if the doubled form is a shortcut in its own right, it counts as that shortcut and not as a typo of the single one.
Those are the building blocks you write a parser from.
Nobody wrote one; the rules sit in a text file, and the language model follows them.

Two of these shortcuts separate something that had no key of its own before.
`[,]` means "this passage is clumsy".
`[-]` means "I see that differently".
One is about the form, the other about the substance.
In conversation between people the two often collapse into one sentence, and the other person has to guess whether to rephrase or to rethink.

The flip side is in [another post](/posts/typos-are-cheap/): my messages to Claude are full of typos, and they are understood anyway.
The form is blurry, the meaning arrives.
That is a tolerant parser, and it works in both directions.
I get more precise where the meaning hangs, not in the letters.

## What migrates outside

All this could stay a workshop language that holds at the computer and not at the kitchen table.
It does not stay there.
I notice it in my own writing, in messages and notes, and when I speak.

Some words have come along.
"It's on disk" now means to me: recorded, can no longer get lost, as opposed to what was only said.
"Context" is what the other person currently has in front of them, and a "cut" is the moment you deliberately clear it and start over.
"Diff" is the question of what has actually changed, and "commit" means to make something binding.
And with everything I pass on, there is now the question of whether it was paraphrased or literal.

That is a larger everyday vocabulary, but not an arbitrary one.
The words that migrated name distinctions I had no short word for before: saved or not, in view or not, changed or merely said again, quoted or paraphrased.
Kenneth E. Iverson titled his 1979 Turing lecture *Notation as a Tool of Thought*.
His thesis was that a good notation does not just depict thinking but shapes it.
He meant programming languages, and he was right; I just did not expect it to hold for the language I talk to people in as well.

## More precise, but for whom

This is the tension I cannot resolve.
[A post about my abbreviations](/posts/a-codebook-from-my-own-corpus/) was about Basil Bernstein's restricted code: people who share a lot of background can speak more briefly, because the rest is assumed.
Is my language getting more precise, or only shorter and readable only by insiders?
Probably both, depending on who I am talking to.
"It's on disk" is an exact term for Claude and me.
For someone who has never worked with an agent, it is jargon.

There is a public counterpoint.
Under the name [Semantic Anchors](https://llm-coding.github.io/Semantic-Anchors/), Ralf D. Müller collects established technical terms that call up an entire field in a language model at once and that humans understand just as well.
When I had Claude check on 19 September which instructions in its memory could be replaced by such a term, the notes from thirteen projects, around 35,000 words, did not contain a single such passage.
My vocabulary has grown, but it has become my own and not the textbook's.

So more precise does not mean easier to understand.
A language sharpened against a single reader who takes every word literally becomes more precise for that reader.
Whether it becomes so for everyone else is a different question, and the answer depends on whether I only carry my words outside or also explain what they mean.

## Poor, not free

At the start there was the parenthesis "(-poor?)".
It is the shortest version of what has changed in my language.
Not that it is free of contradictions.
Rather that, while writing, I notice where one stands and name it in the same breath instead of leaving it there.

A program that contradicts itself does not run.
A sentence that contradicts itself keeps running, and for a long time that was its advantage.
Since I work every day with a reader who takes both literally, I notice the difference more often.
Whether that is a gain, I do not know yet.
That it is happening, I notice every day.
