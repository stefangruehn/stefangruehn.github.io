---
title: "The most expensive answer is yes: what a usage limit actually measures"
date: 2026-09-05T11:00:00+02:00
draft: false
tags: ["claude-code", "workflow", "performance", "agents", "context", "Field Notes"]
series: ["Codebook"]
summary: "At 10:07 my five-hour allowance was gone and three agents were dead. The obvious explanation was the three agents. The measurement says they were 7.8 per cent. The rest was a session remembering itself."
---

All parts, with a diagram up front showing what you are getting into: [Codebook](/series/codebook/).

## TL;DR

- On a September morning my five-hour allowance ran out at 10:07 — after two hours and 27 minutes out of five.
- Seconds earlier three research agents had died, each on its own next call, twelve seconds apart.
- The obvious explanation was right there: three agents at once.
  The measurement says otherwise.
  The three were **7.8 per cent** of the spend.
- The rest was the session itself: 394 requests whose carried-along context grew from 68,000 to 388,000 tokens.
- The requests halved over the morning; the spend per quarter hour stayed the same.
  Per request that is a factor of five — for demonstrably less activity.
- More than thirty turns consisted of "yes", "flash" or "yes, flash".
  Three characters in, 388,000 tokens on the bill.
- The next day, with context cuts in the right places: nearly twice the turns, a third less context, the same amount of work done.

---

## Seven minutes past ten

I had sent out three agents, each with its own research task around a display that kept losing its picture.
Seven minutes later they were dead.

They did not die together but one by one, each on the next call it made of its own accord:

```
10:06:45   Agent terminated early due to an API error
10:06:46   Agent terminated early due to an API error
10:06:57   Agent terminated early due to an API error
```

What sat behind that was in the main session's transcript:

```
rateLimitType: "five_hour"   status: "rejected"   HTTP 429
"You've hit your session limit · resets 12:40pm (Europe/Berlin)"
```

The window ran from 07:40 to 12:40.
It was empty at 10:07, after two hours and 27 minutes.

The session could no longer process the death of its own children.
The notice arrived at 10:07:01, and the answer to it was the limit message again.
My own note at 10:07:27 that the limit had been reached ran into the same wall.

## The explanation that offers itself

Three agents in parallel, seven minutes later the allowance is empty.
I think anyone would draw the same conclusion, and I drew it too.

It is wrong.

This is not one hunch against another, because the numbers are right there.
Every line in a session file states how many tokens that request read, and the agents write their own files alongside.
All you have to do is add them up.

| | Context tokens | Output |
|---|---|---|
| main session, 394 requests | 94.7 M | 734 k |
| three agents together | 8.0 M | 44 k |
| **agents' share** | **7.8 %** | **5.7 %** |

The three visible suspects were one thirteenth.
The other twelve thirteenths were the session I was sitting in.

## What the measurement says

More interesting than the total is the shape of it.
Here is the same morning, broken into quarter hours:

| Time | Requests | Context per request | Spend |
|---|---|---|---|
| 07:45 | 59 | 68 k | 4.0 M |
| 08:00 | 63 | 141 k | 8.9 M |
| 08:15 | 51 | 205 k | 10.4 M |
| 08:30 | 44 | 252 k | 11.1 M |
| 08:45 | 33 | 289 k | 9.6 M |
| 09:00 | 36 | 320 k | 11.5 M |
| 09:15 | 25 | 343 k | 8.6 M |
| 09:30 | 32 | 363 k | 11.6 M |
| 09:45 | 30 | 388 k | 11.6 M |
| 10:00 | 21 | 353 k | 7.4 M (partial) |

Read the first and the last full row side by side.
At 07:45, **59** requests cost four million tokens.
At 09:45, **30** requests cost eleven point six million.

The activity halves, the bill triples.
Per request that is a factor of five, and it moves in one direction only: the middle column rises in every single row.

Early on I did a lot and paid little.
Late on I did little and paid a lot.
Nothing happened in between except the thing that always happens: the session got longer.

## The rule underneath

A language model has no memory between two requests.
What looks like memory is the entire conversation so far, sent again and read again with every new request.

From that follows an arithmetic that explains all the rest:

> Spend ≈ number of requests × average context per request.

So a limit does not measure how much an agent works.
It measures how much it has to remember.

And because the second factor grows with every turn, the same question costs a multiple at the end of a session that it cost at the start — without the answer getting any better.

## The same measurement, four hours later

If the lesson were "agents are cheap", this post would end here and the lesson would be wrong.

Three and a half hours after the cut-off the same constellation died a second time: fresh session, three agents again, a limit again.
This time the measurement comes out the other way round.

| Second window | Requests | Context read |
|---|---|---|
| main session 12:48–13:19 | 128 | 11.6 M |
| agent 1 | 102 | 10.2 M |
| agent 2 | 113 | 8.9 M |
| agent 3 | 97 | 8.1 M |
| **agents' share** | **71 %** | **70 %** |

7.8 per cent in the morning, 70 per cent at lunchtime.
Same tools, same day, same machine.

So the first number is not a property of agents but a property of that one morning.
What does not change is the rule underneath.
In the morning it was the session turning many turns with a large context; at lunchtime it was the agents — 312 requests between the three of them against a freshly emptied session.

An agent is not cheap.
**It merely starts small**, and then it grows like everything else.

One honest aside, because it forces itself on you while adding things up: the first window took 102.7 million tokens, the second broke off at 38.8 million — and in that second window there was no spend outside this one session.
So a limit is not expressed in tokens read, at least not linearly.
You can measure your own consumption.
You cannot measure the boundary where it stops.

## Thirty turns of "yes"

What are you working on at ten past ten, when one request costs 388,000 tokens?

Hardware.
Flash the firmware, look at it, report back, confirm — and round again.
That cycle produces exactly the kind of short turn where the ratio between what you type and what you are billed for tips over completely.

More than thirty of my messages that morning consisted of "yes", "flash" or "yes, flash".

Three characters.
And every one of them drags the entire conversation so far through the bill one more time.
By the end that was 388,000 tokens for a word that carries no information at all, only a permission.

This is where it turns practical: a confirmation turn is not cheap because it is short.
It costs exactly as much as any other turn.

And a permission you can grant once costs once instead of thirty times.
Whatever a project should always be allowed to do belongs in its configuration, not in a question per occurrence.
For anything dangerous or visible to the outside world the question stays right — just not for flashing the same chip for the thirty-first time.

## The remedy, measured

So far this is a diagnosis.
The remedy is unspectacular: throw the context away as soon as the state of things is written down somewhere else.

The next morning I measured it.
Two mornings, the same project, almost the same length — one without cuts, one with:

```
04 Sep  07:48–10:07   394 requests   94.7 M context   734 k output   240 k/request
05 Sep  05:03–07:34   713 requests   61.7 M context   682 k output    87 k/request

requests ×1.81     context ×0.65     output ×0.93     context per request ×0.36
```

Nearly twice the turns.
A third less context.
And the output — the part that was actually work getting done — came in at 93 per cent.

I paid 65 per cent for that.
Per request the second day was **2.8 times cheaper**, and the single most expensive request halved.

You can see the cuts in the file system.
Every cut starts a new session file, and on the second day the gaps between them are seconds rather than hours:

```
04:06:13 → 04:06:33 → 04:06:50        04:55:33 → 04:55:45
```

Two caveats, so the numbers do not claim more than they hold.
These are two different days with different tasks, so n = 2; the only robust figure is context per request, because it does not depend on how much there was to do that day.
And the first day is still counted too kindly — its curve was still climbing when the limit cut it off.

The obvious counter-argument is that seven sessions instead of three also means resuming six times, and that the saving is lost exactly there.
I noticed nothing of the sort.
The new sessions were productive immediately, and the reason is the same as the saving: you are only allowed to cut once the state is written down.
Once it is written down, resuming costs nothing.

## Who has to propose the cut

The cut cannot be automated, and the reason is uncomfortably clean.

**The agent sees the size of the context but not whether the thought is finished.
I see whether the thought is finished but not the size of the context.**

Neither side knows enough on its own to decide.
So the cut has to be *proposed* by the side that holds the number and *decided* by the side that owns the work.

Something follows from that which I had not expected.
An agent proposing to empty the context is proposing to delete its own memory.
There is no incentive for it that comes out of the situation itself.
It only happens if it is written down as a rule — that morning it was not, and the result was three agents in an almost empty allowance.

## What the cut-off actually destroyed

Almost nothing, and the exception is the more interesting half.

The commits from 09:54 and 09:57 were intact, and so were the 71 uncommitted lines in the working tree.
The three agents' transcripts are there in full, 296, 361 and 446 kilobytes.

What was lost was not information but condensation.
All three were still reading; none had reached the point of drawing conclusions.
The material was there, the conclusion was never drawn.

Exactly one finding survived, and only because the agent happened to have written it down as a sentence before it died: that the factory firmware's initialisation ends without the command that switches the display on.
Precisely the thing we were after.

That turned into a working rule.
Agents should write their findings into a file as they go, not report them at the end.
What exists only inside an agent's transcript dies with it.
What exists in a file does not.

## Lessons learned

- **It is not the work that costs, it is the remembering.**
  A session that does nothing but remember gets more expensive with every turn.
- **The way out is not restraint but forgetting at the right moment.**
  A commit is a context cut too: what is documented does not have to be remembered.
- **Confirmation turns are the actual line item.**
  Every avoided "yes" saves a full pass. One standing permission turns thirty turns into one.
- **The frugal tool belongs at the start.**
  When I launched those three agents, 87 of the 102 million were already gone. I reached for the cheap tool at the most expensive possible moment.
- **Intuition points at the wrong thing.**
  Three agents in parallel are visible and feel like effort. The context that silently rides along on every request is invisible — and it was 92 per cent of it.
- **One measurement is not a law.**
  The same figure, taken twice on the same day, came out at 7.8 per cent once and 70 per cent the other time. Measure once and you write down half of it.

## Where I'd start

If the same thing has happened to you and you want to know what caused it, this is the order I would ask the questions in.

1. **How long had the session been running when it got expensive?**
   Not how much you had done. How long you had been having the same conversation.
2. **How many of your last thirty messages were confirmations?**
   Count them. There are almost always more than you think, and they cost the same as any other message.
3. **Which of those can you permit once instead of confirming every time?**
   Everything that recurs and is neither dangerous nor visible to the outside world.
4. **When was your state last written down in full?**
   That was the right moment to cut. For me it was a commit at 09:57 — ten minutes before the cut-off, by which point every further request already cost 388,000 tokens.
5. **And only then: would agents have been right here?**
   They would have been — but at the beginning of the research, not at the end of a long morning.

The uncomfortable half of that is the fourth question, and in the end it has little to do with tokens.
If you want to throw the context away, you have to have written down what you know.
The saving is only the receipt for that.
