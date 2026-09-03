---
title: "Private Still Means Copied: Where My Unfinished Notes Are Allowed to Live"
date: 2026-09-03T02:00:00+02:00
draft: false
tags: ["claude-code", "obsidian", "syncthing", "privacy", "workflow"]
summary: "I wanted my half-formed ideas in Obsidian on my phone and Claude Code on them at my desk. Connecting the two turned out not to be a technical question at all — and the checker I wrote afterwards found a bug in the thing I had just built."
---

## TL;DR

- I keep blog post ideas in Obsidian and wanted Claude Code to work on them with me.
- The Claude app on my phone cannot reach a local Obsidian vault.
  There are three ways around that, and each one is technically sound.
- Two of them fell away for reasons that have nothing to do with technology.
- A *private* repository is still cloned onto a machine that isn't mine.
  The visibility setting was never the point.
- What finally worked had been running on my own private network for years.
  Nobody had looked at it for this purpose.
- Then I wrote a small checker for the notes, and its very first run found a bug in the thing I had just built.

---

## The part I thought would be hard

An idea for a blog post rarely arrives at a desk.
It arrives on a walk, in a queue, halfway through a sentence about something else.
So the ideas live in an Obsidian vault that I carry on my phone.

Claude Code, meanwhile, lives at my desk.
It reads files, runs commands, and can talk through a half-formed thought until it either holds up or falls apart.
That is exactly what an idea needs, and it was happening in a different place from where the ideas were.

I assumed the hard part would be connecting the two systems.
It wasn't.
Connecting them has several good answers.
The hard part was a question I had not thought to ask: **where am I willing to let these notes be?**

## Can Claude reach my Obsidian vault? No.

Start with the obvious attempt.
There is a Claude app for the phone.
The Obsidian vault is a folder of Markdown files on the same phone.

The app cannot open it.
It has no filesystem of its own to browse, no way to run a helper alongside itself, and no mechanism for Obsidian to hand it a folder.
What it can do is accept a file you attach by hand through the system picker, one at a time.
That is not working on a vault.
That is emailing yourself an attachment.

So the direct route is closed, and the interesting part begins: there are three indirect ones.

## Way one: put the vault in a repository

Claude Code works well on code repositories, and a vault of Markdown files is, structurally, a repository.
Push it to a hosting service, and from the phone you can start a session against it: Claude Code clones the repository into a sandbox, works there, and pushes a branch back.
No extra cost beyond the subscription I already pay, no keys to manage, and the phone becomes a genuine remote control.

I got as far as thinking "well, I'll make it private" before the actual objection arrived.

A private repository is not a place my notes stay.
It is a place my notes are *stored*, and every session then **clones them into a virtual machine that belongs to someone else**.
The privacy setting governs who can browse to the page.
It says nothing about where the working copy goes.

That distinction is easy to slide past, because "private repo" sounds like a decision you've already made about confidentiality.
It isn't.
It's a decision about the audience of a web page.

And it mattered here in a way it would not have for source code.
Half-formed ideas are not source code.
Some of them are wrong in ways I'd rather not have on record.
Some are about people.
Some are about things I may never publish at all.
That is the whole point of a place to put unfinished thoughts: it has to be somewhere nobody is watching.

## Way two: bring Claude into Obsidian

There is a community plugin — Vault Companion for Claude — that puts a chat panel inside Obsidian itself, on the phone as well as the desktop, with real access to the vault: read, search, create, update, with an approval card for every write.
That is exactly the shape of the thing I originally imagined.

It has two backends.
One relays through a desktop machine running Claude Code; that one wanted hardware I don't have.
The other talks straight to the model provider using **an API key of your own**, billed per token.

And that is where it stopped, for a reason that is boring and completely decisive: I already pay a monthly subscription, and I had no idea what adding a second, usage-metered billing relationship would do to my costs.
Not "I estimated it and it was too much" — I couldn't estimate it at all.
Token consumption for conversational work is genuinely hard to predict before you've done it, and the honest answer to "what will this cost me per month?" was a shrug.

Introducing a second way to be charged, whose size you can't predict, is not a thing to do casually on a Tuesday evening for a hobby project.

## Way three: keep Claude Code at home

The third way is the one I liked most and still didn't take.

Claude Code can expose a session running **on your own machine** so that you can steer it from a phone or a browser.
The work happens locally: your filesystem, your tools, your files, none of it copied anywhere.
It's available on every plan, needs no API key and no repository hosting, and you connect it by scanning a QR code.

For the confidentiality question, this is the good answer.
Nothing is cloned.
Nothing is hosted.
The files stay exactly where they were.

Two things held me back, and only one of them is technical.

The technical one: a session has to be *running*, on a machine that is *awake and reachable*, at the moment I'm standing somewhere with an idea.
My laptop is closed most of the time I'm out.
That means a machine that stays on, reachable from outside, which is a small infrastructure project of its own.

The non-technical one is worth saying plainly, because it's the honest limit of this whole approach: the files don't leave, but **the conversation does**.
Anything Claude Code reads and discusses with me goes to the provider like any other prompt.
That's the same exposure I already accept at my desk, so it isn't a new problem — but "the files stay on my machine" is a narrower promise than it first sounds, and I'd rather state it than let it be implied.

## What was already running

Here is the deflating part.

The folder holding all my Obsidian vaults is synchronised across my devices by **Syncthing**, and has been for years.
It is peer-to-peer, it runs on my own hardware, it has no cloud component, and it was already copying that exact directory to my phone every time I walked in the door.

The reason it never came up is that I had been asking "how do I connect Claude Code to my phone?"
The right question was "where do the notes need to be so that both of us can reach them?"
And the answer was: exactly where they already were.

Claude Code reaches them at my desk because they're a folder on my disk.
I reach them on the phone because the folder is synchronised.
Nothing new was needed.
I put a new vault inside a directory that was already being copied around, and that was the entire integration.

What I gave up is immediacy.
If I write an idea on the phone in a café, it doesn't reach my desk until I'm home.
I spent about ten seconds deciding that this is fine.
An idea is not a deployment.
Nothing depends on it arriving within the hour, and the pressure to make notes sync instantly is mostly borrowed from tools where latency actually matters.

## One single source of truth, and no second one

The design decision that saved me the most trouble was refusing to be clever.

There is exactly **one** place the notes live: the vault.
A single source of truth — one version that counts, with no second one quietly drifting beside it.
The project folder where the tooling sits contains a symlink pointing at it, and nothing else that could drift.
No mirror, no export step, no script that copies notes from one place to the other and reconciles them afterwards.

This matters because of something worth knowing about file synchronisers in general: **they do not merge.**
If the same file changes in two places between syncs, you don't get a combined version and you don't get an error.
You get a second file with `sync-conflict` and a timestamp in its name, sitting quietly next to the original, and it will keep sitting there until somebody notices.

With one single source of truth and one editor at a time, that case is rare.
With a mirror and a copy script, I'd have been manufacturing it on purpose.

## Then I checked the thing I had just built

With the Obsidian vault in place — a template for new notes, an index, a small set of conventions in the frontmatter — I wrote a script to check it.

That may sound like overkill for a pile of Markdown files.
The reasoning was this: the rules only exist in my head and in a README, some of the checks are genuinely tedious (does every note appear in the index? does every link resolve? is any status value one I actually defined?), and one of them is invisible until it hurts, which is the conflict files above.
A conflicting note doesn't announce itself.
It just sits there while I read the stale version.

The first run failed.

Not on my old notes.
It failed on the **template I had written twenty minutes earlier**, the one every future note would be created from.

The template fills in the creation date automatically, using Obsidian's placeholder syntax:

```yaml
angelegt: {{date:YYYY-MM-DD}}
```

That line is not valid YAML.
Curly braces open a flow mapping, so the parser reads it as a structure, chokes on the colon inside, and gives up on the whole frontmatter block.
Every note made from that template would have started with a metadata block the editor couldn't read.

The fix is a pair of quotes.
The point isn't the fix.

The point is that this had been written, reviewed, and looked at by two of us on the way past, and it looked *completely fine*, because it looks like every other templating placeholder in the world.
It took a program that doesn't know what the line is supposed to mean, and only checks whether it parses, to catch it.

There's a version of this evening where I don't write the checker, and instead find out weeks later, on my phone, when a note I've just created renders its own metadata as body text.

Whether that checker is any good is a separate question, and one I want to look at properly — a test that can't fail is worth nothing, and this one had been written in the same sitting, by the same hands, as the thing it was checking.
That's a post of its own.

## Lessons learned

1. **Ask where the data is allowed to live before asking how to connect anything.**
   Every route I looked at was technically fine.
   The two that fell away, fell away on confidentiality and on billing.
   If I'd started with connecting the systems I'd have built the wrong thing competently.
2. **"Private" describes a web page, not a workflow.**
   A private repository is still copied into infrastructure you don't own, every session.
   If that matters for your content, the setting doesn't help you and it's easy to mistake for a decision you've made.
3. **An unpredictable cost is a real objection, not a lazy one.**
   "I can't estimate this" is a legitimate reason to decline a second billing relationship.
   It doesn't need to be dressed up as a technical concern.
4. **Look at what's already running.**
   The answer had been synchronising that exact directory to my phone for years.
   I nearly built a second mechanism next to a working one because I was asking a question shaped around a product rather than around my files.
5. **Asynchronous is usually enough.**
   Ideas do not need to arrive within the minute.
   Much of the pressure toward instant sync is inherited from tools where latency genuinely matters, and it isn't free — it's what pushes you toward hosted storage in the first place.
6. **One single source of truth.**
   No mirrors, no export steps.
   Synchronisers don't merge; they leave a conflict file and say nothing.
   Don't create the conditions on purpose.
7. **Check the thing you just made, not just the thing you had.**
   The bug was in the newest, smallest, most obviously correct file in the project.
   New code is the code nobody has looked at yet, including the person who wrote it ten minutes ago.

## The order I'd ask the questions in

If you keep notes and you've wondered whether to let Claude Code near them, the useful thing I can offer isn't a setup.
It's the order of the questions.

Start with what's actually in your notes.
Not "is this sensitive" in the abstract, but: is there anything in here I'd be uncomfortable having copied onto a machine I don't control, even briefly, even privately?
For a vault of recipes, probably not, and the hosted routes are excellent and you should use them.
For anything half-formed, personal, or about other people, the answer changes, and it changes *before* you get to the tooling.

Then look at what you already run.
File synchronisation, a home server, a device that's already awake — these are unglamorous and they don't appear in anybody's integration guide, which is precisely why they're easy to miss.

And accept the boring option when it's the right one.
The thing I built is a folder in a directory that was already being copied, plus a symlink, plus a script that reads some YAML.
It is not clever.
It has no cloud component, no second bill, and no ongoing decisions to make.
It also took an evening, most of which was spent working out what I actually wanted — which was, as usual, the real work.
