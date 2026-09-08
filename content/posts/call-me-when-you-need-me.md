---
title: "Call me when you need me: two sounds that turn waiting into leaving"
date: 2026-09-06T02:17:32+02:00
tags: ["claude-code", "workflow", "hooks", "linux", "Field Notes"]
topics: ["cost"]
summary: "An agent that runs for twenty minutes only frees me if it can call me back. Otherwise I check every two minutes and stay tied to the screen anyway. Two lines of configuration turn the checking into a callback, and I measured the baseline for it just before switching it on."
---

## TL;DR

- Two events, two sounds: `Stop` means "done, take a look", `Notification` means "I'm stuck and need a decision".
- The second one is the expensive state. Until it is answered, nothing moves.
- Without a callback the human polls: a glance every two minutes, mostly for nothing. With one, the human may walk away.
- The baseline, from my own transcripts: 471 waits over two weeks, 20.2 hours in total. 14 per cent of them longer than five minutes, the longest 48.
- Whether the sound shortens that, I don't know yet. Eleven waits have accumulated since I switched it on, which proves nothing.
- What goes silent is the single session, not the machine. The script reads the session ID out of the hook payload for that.
- The built-in trap: hooks are read at session start. The automation you are entering right now does not yet apply to you.

---

## Who is waiting for whom here

When I hand over a larger task, the agent works for minutes.
In theory I am free during that time.
In practice I wasn't, because I had no way of knowing which of three states it was in: finished, still computing, or stopped eight minutes ago on a question I could answer with three characters.

So I kept checking.
Every few minutes, and mostly for nothing.

That pattern has a name, and it comes from hardware: it is polling.
You ask regularly whether there is anything new, and you pay for every ask, including all the empty ones.
The alternative is the interrupt: the device pulls a line when it has something, and until then the CPU is busy elsewhere.
At a front door we take this for granted — nobody walks to the door every two minutes to check whether someone is standing outside.

At my terminal I did it the other way round for two weeks.

## Two events, two meanings

Claude Code can run a command on certain events.
Two of them matter to me:

- **`Stop`** fires when an answer is finished.
- **`Notification`** fires when the program needs attention. For me that is almost always a permission question.

Both get a sound, and pointedly **not the same one**:

```json
"hooks": {
  "Notification": [{ "hooks": [{ "type": "command",
    "command": "~/.claude/hooks/ton.sh /usr/share/sounds/freedesktop/stereo/message-new-instant.oga" }] }],
  "Stop":         [{ "hooks": [{ "type": "command",
    "command": "~/.claude/hooks/ton.sh /usr/share/sounds/freedesktop/stereo/complete.oga" }] }]
}
```

Two distinct sounds are the entire trick.
A single tone would mean "something happened, come and look" — and I would be back to looking.
Two tones carry the one piece of information that matters, namely whether it is urgent.
"Done" can sit there for five minutes; the coffee comes first.
"I need a decision" means that nothing at all is happening while I stand in the kitchen.

The sound files are already lying around on any Fedora system, courtesy of the freedesktop sound theme.
They are played with `paplay`, which PipeWire brings along anyway.
Nothing installed, nothing downloaded, no custom sound designed.

## Twenty hours of waiting

Before switching this on I wanted to know what we are actually talking about.
Claude Code writes a transcript per session as JSON lines, with a timestamp on every line.
That gives you exactly the quantity in question: the span between the last line of an answer and my next message.
Tool output and automatic insertions don't count, only real messages from me.

Across all projects, from 23 August to 5 September:

| | |
|---|---|
| waits in total | 471 |
| sum | 20.2 hours |
| median | 67 seconds |
| longer than 2 minutes | 32 per cent |
| longer than 5 minutes | 14 per cent |
| longer than 10 minutes | 5 per cent |
| the longest | 48 minutes |

The number that hurts is not the median.
A good minute of thinking before I answer is not lost time, that is the work.
The interesting ones are the 5 per cent over ten minutes: 23 cases in which I was simply away and had no idea I was needed.

To be fair about it: those 20.2 hours are not all idle time.
In many of those spans I was reading, checking or thinking.
The timestamp doesn't know whether I was in the kitchen or studying some output, it measures the agent's waiting, not the human's idleness.

And the second honest note: whether the sound changes any of this, I cannot say yet.
It has been running since just after six yesterday evening.
Eleven waits have accumulated since, all under two minutes, and eleven values support exactly nothing.
The value of this measurement is that it happened **beforehand**.
In two weeks the same script runs again, and then there is a comparison instead of a feeling.

## The session goes silent, not the machine

The first draft was a one-liner in the configuration, with no script in between.
It survived until the evening two sessions were running at once: one that was computing away and supposed to call me, and a second one alongside whose sounds were in the way.
A global switch would have silenced both, including the one I was waiting for.

So there is a small script between hook and speaker.
The hook payload arrives as JSON on `stdin`, and the session ID is in there:

```sh
sid=$(printf '%s' "$eingabe" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')

[ -n "$sid" ] && [ -e "$HOME/.claude/mute-$sid" ] && exit 0
[ -e "$HOME/.claude/mute-all" ] && exit 0

paplay "$klang" >/dev/null 2>&1 &
```

A session stays quiet as long as a file carrying its ID exists.
Two shortcuts create and delete it — `[x]` off, `[o]` on — and that is the whole user interface.
Other open sessions stay audible, and I never have to type an ID anywhere.

The script has a second branch that I'll leave in here, because it is a general pattern: older versions supply only the path to the transcript instead of the ID.
The ID is then part of the file name, and `basename` pulls it back out.
Four lines for the case that something underneath me changes.

## The hook that doesn't apply when you write it

One thing cost me twenty minutes, and it is typical of automations that concern themselves.

Hooks are read **at session start**.
If I add one mid-session, nothing happens in that session, not until `/hooks` or a restart.
Of all sessions, the one in which you set up the notification is the one without a notification.
And because it is the session you are working in, it is also the one you want to test it in.

The stopgap is inelegant and works: while the hook is not yet live, the agent plays the sound itself, as the last command of its answer.
That is the same `paplay` call, one level up.
If you build yourself an automation, build it so it can also be triggered by hand.
Then "not active yet" is not a special case, just one extra step.

## What the sound can't do

It does not make questions cheaper.
A question to me costs the agent a full round trip with the entire context it carries, and that is the [most expensive item](/posts/the-most-expensive-answer-is-yes/) in the whole operation — no sound changes that.
What it changes is the waiting in front of it.

That is exactly why it stayed at two events.
There could be more: before every tool call, after every tool call, at the end of every session.
A sound that arrives constantly stops being heard after two hours — and then I no longer hear the one that counts either.

## What I learned

- **An agent only frees you if it can pull you back.**
  Otherwise you trade waiting at the screen for checking in passing, and you have gained very little.
- **Two states need two sounds.**
  "Done" and "stuck" cost you different amounts. A shared sound throws away the very information you are listening for.
- **The switch belongs to the session, not the machine.**
  Muting globally means turning off precisely the thing you are waiting for.
- **Automations that concern themselves don't yet apply to themselves.**
  The hook takes effect from the next start. Keep the manual trigger around.
- **Measure first.**
  The baseline costs ten minutes while the data is still untouched. Afterwards it cannot be had at all.

## The same thing on your machine

If you work with an agent that runs longer than you care to watch:

1. **Take two events, not eight.** Done, and needs-you. Anything else dilutes both.
2. **Take two distinct sounds.** They are already on your system; you don't have to install anything or pick something beautiful, just two you can tell apart.
3. **Build the mute right away, and build it per session.** The day you run two sessions in parallel arrives sooner than you think.
4. **Test it in a new session.** The one you configure it in is the only one where it won't work.
5. **Measure your waits before you switch it on.** Your transcripts are already there, with a timestamp on every line.

Since yesterday my machine rings when it needs me.
Before that I called on it, every two minutes, and mostly it had nothing to say.
