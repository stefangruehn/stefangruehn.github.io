---
title: "Reading Needs Only a Path: When an Agent with a Shell Needs an MCP, and When It Doesn't"
date: 2026-09-24T18:00:00+02:00
tags: ["claude-code", "mcp", "linux", "privacy", "workflow", "Field Notes"]
topics: ["data"]
summary: "I wanted to know whether a support request had been resolved, and Claude answered from nine years of mail without touching the mailbox over the network. Closing the ticket afterwards was beyond it. The same session shows where the line between shell and MCP runs: between reading and acting."
---

## Summary

- An agent with a shell reads whatever is on the disk, and there is a lot there: mail, browser history, notes, configuration.
  For that it needs only a path, no password and no MCP.
- One day Claude answered a question about my mailbox purely from Thunderbird's local copy.
  1203 messages from almost nine years, searched in seconds, without a connection to the mail server.
- In the same task it was supposed to close the ticket, and that did not work.
  Sending and clicking need credentials, a session or an API.
- The line runs between reading and acting.
  An MCP could have done the sending here; it would not have made the reading any better.

## A question for the mailbox

I had filed a support request with GitHub about a clean-up on one of my repositories.
The answers came by mail, and at some point I no longer knew whether the matter was settled.
So I asked Claude Code whether the request in my Gmail mailbox had been closed.

Claude has no access to Gmail.
There is no MCP for mail in this environment, that is, no service through which an agent could talk to a mailbox over a fixed protocol.
But there is Thunderbird, and Thunderbird keeps a complete copy of the mailbox on disk.

## The way in

The first assumption was wrong.
The profile was not where Thunderbird traditionally puts it, nor under the name the Flatpak app used to carry.
It is now called `net.thunderbird.Thunderbird`; Claude found that with `flatpak list`.

The second place where one gets stuck is `profiles.ini`.
The profile marked as default there was an empty shell from the day of installation.
Which profile Thunderbird actually uses was written in a different section of the same file.

After that it was craft.
In `prefs.js` a chain of entries leads from the account via the identity to the address, and from the account via the server to the folder.
Only that chain proves which folder belongs to which address.
The folder itself is an mbox, a single text file with all messages one after another, 80 MB in this case.

`grep` gave the order of magnitude: 1203 messages, two relevant senders.
The actual analysis ran through the `mailbox` module from Python's standard library.
There were two traps: umlauts in the subject are encoded in the header and must be decoded first, and the body of a message is often Base64 until one explicitly unpacks it with its character set.

What did not happen was a connection to the mail server.
Claude needed no password and did not touch Thunderbird's password store; it installed no extension and used no MCP.
It read files.

The mail was only the source, though, not the proof.
Whether the clean-up had really been done was only established by a `curl` on the old addresses: 404 on the web page, 422 through the API.

## Where it stopped

In the same task the ticket was to be closed.
That did not work.

A reply by mail had no way out.
No mail server runs on the machine that could send it, and Claude would have had to take the Gmail password from Thunderbird's store.
That was not an option.

Operating the support portal in the browser did not work either.
Browser control was not available in this session, and the portal has no API.
The token Claude otherwise uses with `gh` to work on GitHub did not help, because the tickets live in a different system.

Nine years of mailbox searched in seconds, and not one line sent out.
I closed the ticket by hand.

## The line between reading and acting

One distinction from that day has stayed in my memory.
It sorts tasks by their direction; easy and hard ones occur on both sides.

**Reading needs only a path.**
Almost every program keeps its state in files whose format is documented: mbox, SQLite, JSON, INI, Markdown.
Add the tools that are logged in anyway, in my case `gh` and `git`, and `curl` on public addresses.
Browsers, for instance, keep their history in an SQLite file, and something similar holds for calendars and note-taking apps.
For this post I only demonstrated it on the mailbox.

**Acting outwards needs more**, and that is where an MCP earns its keep:

- where credentials for a third-party service are needed that one does not want to pull from another program's password store;
- where the state of a running program is written to: reading Thunderbird's index is harmless, changing it is risky;
- where a service leaves no local trace because it only exists behind a web interface;
- where a fixed contract is better than a guessed format.

This is not a criticism of MCPs.
They are built for acting; for looking things up, an agent with a shell rarely needs them.

## The uncomfortable side

The way in is neither a trick nor a security hole.
This is how a tool works that runs in one's own user account: it can reach everything I can reach.
That is exactly why it should be said out loud.

The scale belongs in the picture.
On a casual question, 1203 messages from November 2017 to September 2026 lay open, fully searchable.
Where my notes are allowed to go I described in [Private Still Means Copied](/posts/private-still-means-copied/).
This was about the other direction: what a local agent can reach anyway.

And the copy on disk is not the mailbox on the server.
Whatever was never synchronised is missing from it, and deleted messages can linger for a while.
Claude checked that in this case: of the 1203 messages, 639 carried a status field at all, and none of them was set to deleted.

## What I take from it

- Before I connect an agent to a service, I ask whether the service already leaves a trace on my disk.
  Often it does.
- Reading and acting are different questions.
  One needs a path, the other credentials, and those I want to hand out deliberately.
- An MCP pays off where the agent is supposed to do something I would otherwise do by hand.
- What the agent can read is roughly everything I can read.
  That is convenient, and it is the reason to look more closely.
