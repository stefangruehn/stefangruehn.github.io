---
title: "Many Memories, One Person: Who Remembers What When an Agent Works Alongside You"
date: 2026-09-19T04:00:00+02:00
tags: ["claude-code", "context", "memory", "obsidian", "workflow", "Essay"]
topics: ["thinking"]
summary: "I have been outsourcing my memory for as long as there has been paper, these days into an Obsidian vault. Since an agent started working with me, it outsources too, into files of its own. Afterwards the same decision stood in three places for three readers, and nothing held them together. Nine days later the agent's copy was the stale one."
---

## TL;DR

- My memory lives only partly in my head.
  The rest is on slips of paper, in the calendar and, for a while now, in an Obsidian vault.
- Claude Code outsources as well: into a `CLAUDE.md` per project and a collection of small memory notes.
- Both sides build stores the other cannot see.
  My vault is not context for Claude, and I don't read its notes in everyday work.
- One afternoon in September the same decision had to be written to three places, because each place has a different reader.
- Nothing held the three together except discipline.
  Nine days later 22 memory notes were deleted, and one of them still claimed a state the vault had contradicted for three days.
- What I take from it: a fact gets one place, and the place follows the reader who needs it.

---

## The pile on the desk

I have never kept everything in my head.
Nobody does.
There is the note stuck to the monitor, the calendar on the wall, the notebook, and the pile on the desk whose order is itself the information.
Digitally, add the open browser tabs, the shell history, a `TODO` in the code.

For this blog it is an Obsidian vault.
It records what I still want to write about, what needs changing in things already published, and how far along each idea is.
I mostly read it on my phone.
How it gets there is in [Private Still Means Copied](/posts/private-still-means-copied/).
What is in there my head does not have to hold, and it doesn't.
So the vault is not an accessory to my memory.
It is part of it.

## The agent knows nothing about it

Claude Code, which I work with on this blog, sees nothing of that part unless someone brings it in.
A vault is not context.
It only enters a session when a file from it is read, and that happens because I trigger it.
My [shortcuts](/posts/shortcuts-as-an-input-aid/) for "file this as an idea" or "rate the matching posts" are exactly that pipe, triggered by hand every time.

The reverse holds too.
Claude keeps a memory of its own: a global `CLAUDE.md` for all projects, one per project, and a directory of small notes, one file per matter, with an index called `MEMORY.md`.
That is its note on the monitor.
I don't read it in everyday work.

So two sides build stores the other cannot see.
That alone is not a problem.
It becomes one as soon as one side takes what it has outsourced to be shared.

## Three stores, three readers

On September 7 I restructured the vault.
Ideas got status folders, `1 Notiert` through `5 Abgelegt`, so that Obsidian's file list on the phone shows how far along each idea is.
Frontmatter is invisible there, folders are not.
A field `wartet_auf` ("waiting on") was added, dates disappeared from file names, and since then a check script makes sure status and folder agree.

Each of these decisions had to be written to three places:

| Store | Who reads it | When |
|---|---|---|
| the vault itself: README, template, frontmatter | me, mostly on the phone | when taking notes |
| the project's `CLAUDE.md` | Claude | at every session start in this project |
| Claude's memory notes | Claude | when needed, in other projects too |

The split followed reach.
The vault got the instance: this vault, these folders.
Claude's memory got the construction rule for the next vault.
Within one minute, five memory notes came out of it: status folders, `wartet_auf`, no date in the file name, checker with self-test, and how to set up a neighbouring vault.

That sounds tidy.
It had a gap you only notice on second look.

## Nothing holds the three together

The check script checks the vault.
It does not check `CLAUDE.md`, let alone Claude's memory.
That all three stores said the same thing after the restructuring was discipline, not mechanism.
In the end the same rule stood in two vault READMEs, in `CLAUDE.md` and in a memory note.
Four versions of one fact, and no reconciliation.

How quickly that drifts apart showed two days later.
On September 9 I merged the two vaults into one, because Obsidian resolves links only within a vault, and ideas and change requests kept pointing at each other.
The note "set up a neighbouring vault" now described a path we had just left.
It was replaced the same day.
That went well because the note was in view at the moment the world changed.

With another note it did not go well.
On September 16 I had Claude go through its memory, asking what of it now lives permanently somewhere else.
22 notes totalling 47.6 kilobytes were deleted, among them all the ones from the restructuring.
Their content had long been in the vault and in the project's `CLAUDE.md`.
Three of them needed no move at all, and Claude gave its reason in a sentence that has stayed with me:
*"the vault is more current than my memory".*
One of those three still claimed that a repository had no public remote.
The vault had said the opposite for three days.

Nobody had written the note wrong.
On the day it was written, it was right.
It just wasn't read anymore when things changed, and a memory nobody reads does not notice that it is going stale.

## What a head loses first

Time works differently on my memory than on Claude's.
Claude's note stays word for word and quietly becomes wrong.
With me it is the other way round: the state stays, the reason goes.
Two weeks later I still know that an idea is on hold.
Why it is on hold, I no longer know.

That is exactly what `wartet_auf` is for.
The field records what something hangs on, such as "the repository is not public" or "not legally checked".
It is outsourced memory in its purest form, and it is the kind of knowledge a head loses first.

Writing also costs the two sides differently, and that shaped the vault.
The date went out of the file names because I had to type it on the phone, while the same date appeared in the frontmatter anyway.
A memory note costs Claude nothing comparable to write.
Every line on the phone costs me keystrokes.
That is why my outsourced memory follows different rules than its: few fields, much structure in folders, and whatever can be derived is derived.

## No inheritance into the head

Claude's stores have a property mine lack.
When a session starts, the global `CLAUDE.md`, the project's and the index of the memory notes are loaded automatically.
What is in them is there without anyone asking for it.

My vault does not inherit into my head.
It wants to be read, and it is read only when I open it.
That is why it has to be readable on the phone, and why its state lives in folder names rather than in fields you first have to expand.

Automatic inheritance has a price in turn, which I wrote about [elsewhere](/posts/the-most-expensive-answer-is-yes/): whatever is loaded at every start is paid for with every request.
Each memory note has a line in the index, and the index always comes along.
A memory that is always there is always expensive, too.

## One place per fact

What I take from this is not a rule for more reconciliation.
Reconciliation is discipline, and discipline is what was missing.
It is a rule for fewer copies:

- **A fact gets one place.**
  If it stands in two, sooner or later one of them is the stale one.
- **The place follows the reader.**
  What only Claude needs belongs in its files, what only I need in the vault.
  What we both need belongs where we both look anyway.
  For me that is the vault, because Claude can read it and I don't read Claude's files.
- **Where possible, a program checks.**
  The vault has a checker, Claude's memory has none.
  That is one more reason the rules now live in the README rather than in five notes.
- **The agent's memory gets cleaned out regularly.**
  With the question of what now lives permanently somewhere else.
  Only what has a place to go gets deleted.

## Where I would start

If you work with an agent that keeps a memory of its own:

1. **Read it once, all of it.**
   The index and the notes behind it.
   You will find things you took to be shared, and others that stopped being true long ago.
2. **Look for facts that stand in two places.**
   One of them is the stale one, or will be.
3. **For each, ask who reads it.**
   The answer tells you where it belongs.

The agent does not forget.
It remembers a state that no longer exists.
That is the opposite of my forgetting, and it is harder to notice.
