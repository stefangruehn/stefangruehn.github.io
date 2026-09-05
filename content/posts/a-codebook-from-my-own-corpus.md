---
title: "A codebook from my own corpus: the shortcuts you cannot guess"
date: 2026-09-05T11:30:00+02:00
draft: false
tags: ["claude-code", "workflow", "shortcuts", "language", "Field Notes"]
series: ["Codebook"]
summary: "Work with an agent for long enough and you repeat yourself. What you repeat can be abbreviated — but the good abbreviations cannot be guessed. They are in your own transcripts, and the most frequent word of all was missing from my guessed list."
---

Part one measured what shared context [actually costs](/posts/the-most-expensive-answer-is-yes/) — and that an avoided question saves a full pass.
This is the attempt to avoid them on purpose.

## TL;DR

- One shortcut for "please interview me about this first" turned into a list over an afternoon, and the list turned into a small grammar.
- I guessed the first list.
  Then I counted: 764 distinct messages of mine across 13 projects.
- By far the most frequent word was `commit`, 28 times — and it was **not on** the guessed list.
- Checking the list found three defects that nobody notices while writing one: a genuine contradiction, an escape character that collides with itself, and a token that was already taken.
- A shortcut that merely repeats a standing rule is dead syntax.
  It only works as an amplifier.
- What makes this different from any text expander: the target of the expansion is not a string but an instruction.
  Three keystrokes can set off half an hour of work.

---

## One token became a list

It started as a convenience.
I often write "please interview me about this before you write anything" — the same sentence every time, in the same situation every time.

So it became a token: `[?]`.

That was meant as typing saved and stayed that way for less than an hour.
Once one token works, eight more occur to you immediately, and then you face the question of which ones are worth having.
That is where the interesting work starts, because that is where guessing stops working.

## What I actually repeat

The frequencies are in your own transcripts.
Claude Code stores every session as a file, and every message I have ever typed is in there.

```sh
cd ~/.claude/projects
jq -r 'select(.type=="user") | .message.content | strings' ./*/*.jsonl \
  | grep -viE 'toolu_|/tmp/|exit_code' | awk 'length($0)<300' \
  | sort | uniq -c | sort -rn
```

The leading `./` is not decoration.
Without it `jq` takes the directory names that begin with a hyphen for options and gives up.

What came out was 764 distinct messages across 13 projects, with this on top:

```
commit    28×      hugo      14×      serie     13×
test      13×      merke dir  7×
```

My guessed list had caught `hugo` and `serie`.
`commit`, the most frequent of them all, was not on it.

That is the whole point of measuring.
Intuition reliably catches what stands out — the special instructions, the new tools, the thing you learned last week.
It does not catch what is so ordinary that you read straight past it while thinking about your own work.

A codebook you guess is a codebook about your self-image.
One you measure is a codebook about your work.

## What you don't notice while guessing

The guessed list had three defects, and none of them was visible while writing it.

**A genuine contradiction.**
`[-]` was meant to say "I see this differently" and at the same time "correct me".
Those are two opposite directions in one token: who is wrong here, you or I?
A token that can mean both means nothing.
It now says only the one thing — "I see this differently, argue your position again or revise it" — and that also settles whose move it is.

**An escape character that collides with itself.**
You need a way to say: *this time I really do mean just the character.*
The proposal was a slash in front of it.
Except the slash is itself one of the shortcuts, `[/]` for "give me an alternative" — and at the start of a line it is Claude Code's prefix for slash commands.
Two collisions in one character.
It became the backslash.

**A token that was already taken.**
`[?]`, the thing that started all of this, already appeared eight times in the transcripts — with a different meaning.

> "connected via code scan -> connected via QR code scan (?)"
>
> "posts show cards, series only badges. (?)"

That does not mean "interview me".
That means "is that right?".

It was resolved without loss: those cases are now `[&]` — "I suspect that …, check it rather than adopting it".
The old meaning moved house, and the new meaning got the token.
A reassignment, not a collision.

All three defects have one thing in common: they only become visible when you hold the list against what you actually wrote rather than against what you think you write.

## A shortcut that does nothing

`[$]` was meant to say "take the most token-frugal route".

That sounds useful and did nothing.
Frugality has long been a standing rule in my global configuration, which is read before every session.
A token that repeats a rule that already applies switches nothing on.
It is dead syntax: you type it, it feels effective, and nothing changes.

What saved it was making it say more rather than the same:

> Take the most token-frugal route — **even at the cost of thoroughness.**

Now the token settles a trade-off the standing rule leaves open, and it is a switch again.
So the test for any entry on a list like this is not "is this useful?" but: *what would be different if I did not type it?*

## Why this abbreviates more than a text snippet

Text expansion has been around for decades, and its compression ratio is always bounded by the length of the phrase.
Four characters become forty, and that is the ceiling.

Here the target of the expansion is not a string but an instruction.

`[s]` means: *look at the posts on the blog that fit this idea, drafts included, assess them, and if there are more than two, propose a series.*
That is three keystrokes and half an hour of work.

This is what makes the list something other than a convenience — and it ties it back to the arithmetic from part one.
A question does not cost what it weighs in characters; it costs one full pass over the entire conversation so far.
A token that makes a question unnecessary does not save three keystrokes.
It saves a whole turn.

## Two halves of the same document

A codebook is only worth having if both sides read the same thing in it.
Mine lives in two files.

`SHORTCUTS.md` is the half I read: with reasons, examples, and an explanation of why a token means one thing and not another.
The agent's configuration and memory are the half it reads: terse, no reasons, but with the rules for parsing.

The same document in two directions, and both have to be kept in step by hand, because there is no shared store.
That is the weak point of the whole construction, and I have no elegant fix for it.
What helps is one sentence at the end of both files: *if something changes, it goes in this file and in the other one.*

## Where you have seen this before

None of this is new; it has just gone by other names.

- **Source coding.**
  Short codes for frequent symbols, long codes for rare ones — that is the idea behind every compression scheme.
  Here the codebook is the shared context, and the distribution is the frequency of my own instructions.
- **Restricted code.**
  Basil Bernstein described how groups with a lot of shared background can speak more briefly, because the rest is taken as given.
  Only here that shared background grows over sessions rather than over generations.
- **Grammaticalisation on fast-forward.**
  Frequently used content words collapse into function markers over time — in natural languages that takes centuries.
  Here it takes an afternoon, because both sides can write the dictionary down instead of having to negotiate it.
- **A shared working vocabulary.**
  In software design this is old advice: settle the terms first, then build.
  The only new part is that the other party can help settle them.

## Lessons learned

- **Measuring beats guessing, reproducibly.**
  The most frequent word in my own work was missing from the list I had written about my own work.
- **A shortcut is a design and it has defects.**
  Contradictory meaning, colliding escape, a token assigned twice — those are ordinary design errors, not details.
- **Test every entry by what would be different without it.**
  Anything that merely repeats an existing rule has no effect. Anything that shifts a trade-off does.
- **A meaning that is already in use gets reassigned, not overwritten.**
  What you already say is inventory. It gets a new token, and the free one keeps the new meaning.
- **The gain is not in the keystrokes.**
  It is in the turn that no longer happens.

## If you want to build one yourself

It is worth it as soon as you notice you are repeating yourself — and you notice that later than it starts.

1. **Count first, write second.**
   Take your own transcripts, sort by frequency, and look at the top twenty lines. They will surprise you.
2. **Only take what occurs often enough.**
   A token for something you write three times a year is something you have to remember without it ever saving you anything.
3. **Check whether the token is already taken.**
   In your own material, not in theory. If it is, the old meaning moves.
4. **Write down, for each entry, what would be different without it.**
   If that line stays empty, the entry does not belong on the list.
5. **Put it somewhere both sides read.**
   A codebook only one side knows is not one.

The whole thing costs an afternoon, and most of it goes into step three.
What you end up with is no longer a set of abbreviations but a small shared language — and it has one property I had not counted on.
For someone who needs it more badly than I do, it is something else entirely than a convenience.
