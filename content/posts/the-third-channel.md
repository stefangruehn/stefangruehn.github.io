---
title: "The third channel: what is always true doesn't belong in the dialogue"
date: 2026-10-03T01:50:00+02:00
tags: ["claude-code", "workflow", "context", "measurement", "Field Notes"]
topics: ["cost"]
summary: "How full the context is, which model is running, how close the five-hour limit is: the terminal shows none of it, and every question about it costs a turn. A status line shows it without using anything up. While building it, it turned out the host had known every one of these numbers all along and simply displayed none of them."
---

## TL;DR

- The state of an agent session is invisible in the terminal: context fill, model, effort, limits, mute.
- Every way of finding it out is a turn, and a turn costs the full context carried along. Whoever asks about the context level pays in exactly the currency they are asking about.
- The status line is a third channel next to input and output. It shows state without using up tokens or turns.
- The first version computed the context fill itself and showed 45 percent. The host delivered the number ready-made: 11 percent, with a window of one million tokens instead of the assumed 200,000.
- The most important number was one nobody had been looking for: the five-hour limit, live, in percent.
- The line halves the asymmetry between human and agent. How full it is, I now see. Whether the state is saved, only the agent knows.
- It only takes effect through a threshold: from yellow on, the agent proposes the context cut on its own.

---

## 45 percent that were 11

On 7 September I wanted a status line for Claude Code, a line below the input field that always shows what currently applies.
Claude built it in an afternoon, and the first version was well made.
A Python script read the session transcript, added up the tokens, divided by the size of the context window and showed the result in percent.
It cached so it would stay fast, it was tested, and it showed 45 percent.

Then the first real input from the host landed on disk.
Claude Code calls the script on every refresh and hands it a JSON document, 1.7 kilobytes in size.
It contained `context_window.used_percentage`, already computed.
The value was 11, not 45.

The error was in the denominator.
Claude had calculated against a window of 200,000 tokens, because that was the size it knew from memory.
The window of this session was one million.
The calculation was careful work on a number that was already sitting two centimetres away.

The rule broken here comes from the hardware project we were working on at the same time: statements come from the device, not from the datasheet.
This time the datasheet was the agent's own memory, and the device was a small JSON file.

## The number was there, it just wasn't shown anywhere

The mistake shifted the idea behind the line.
I had assumed a measurement was missing.
None was.
The host knows its state completely, and it passes it on to the script: context fill, model, effort level, cost in dollars, cache hit ratio.
It just doesn't display any of it.
The status line adds no information, it makes existing information visible.

The biggest surprise was a field we hadn't been looking for at all: `rate_limits.five_hour`, the five-hour limit, live in percent, plus the weekly limit.
Exactly this limit had killed two sessions on 4 September.
Until then I could only get at the number through `/usage`, that is, through a turn of its own.
It had been in the JSON the whole time.
The line found it during the build, because the field list came from real input and not from the documentation.

There is a single field the host does not deliver: which plan I am on.
The subscription sits in the file `~/.claude.json`, in the client's state, not in the status channel.
What concerns the running session is passed through, what concerns the account is not.

## Every question is a turn

Why a line and not a question?
Because a question isn't free.
How expensive it is, I worked out in [The most expensive answer is yes](/posts/the-most-expensive-answer-is-yes/): a three-character "yes, flash" was billed at 388,000 tokens at the end of a long session, because every request sends the entire previous context along.
A turn that only fetches a state costs as much as one that does work.

This leads to an awkward bit of arithmetic.
Whoever asks the agent how full its context is makes it fuller by asking.
They pay for the answer in exactly the currency they are asking about.

The status line is neither input nor output.
It is a third channel that runs alongside the dialogue, and it uses up no turn, no token and no follow-up question.
The price is paid in a different currency.
The script starts as a process of its own on every refresh, reads the JSON and prints a line.
Measured, that is 26 milliseconds, and since the correction it no longer touches the transcript at all.

## Two workarounds for the same hole

Before the line there were two arrangements that contradicted each other.
My instructions to Claude said the agent has to announce when a context cut with `/clear` is due.
And there was a shortcut I used to report the context level to the agent.
So once the agent knew and told me, once I knew and told it.
Looking back, that is the evidence that the number simply wasn't anywhere: both sides knew it only roughly, and each had built a workaround in the opposite direction.

In the most expensive answer I had still described this as a division of labour:
"The agent sees the size of the context but not whether the thought is finished.
I see whether the thought is finished but not the size of the context."
Since 7 September the second half is no longer true.

The shortcut is gone.
The announcement stays, and the reason for that is the actual point.
The number says how full the context is.
It doesn't say whether the state is on disk, that is, whether a cut would throw something away right now.
The one I now see, the other only the agent knows.
The status line doesn't remove the asymmetry, it halves it.

## Sound for events, line for states

The first channel next to the dialogue was a sound.
[Call me when you need me](/posts/call-me-when-you-need-me/) was about the agent calling me back when it is done or needs a decision, instead of me checking every two minutes.
There, checking turned into a callback.
Here, asking turns into a display that is always present.
A sound reports that something happened.
A line shows what currently applies.

This is what it looks like:

```
Pro │ Opus 5 · high │ ctx 12% · cache 97% │ 5h 38% · 7d 68% │ snd
```

From the left: the plan, model and effort, context fill and cache, the two limits, and whether the sounds are on.
Context fill and limits change colour when things get tight.

Choosing the fields was mostly leaving things out.
Project and branch are in the JSON too, and so is the cost in dollars.
They stayed out, for the same reason there are only two sounds: a sound that always comes stops being heard, and a line that shows everything stops being read.

The least conspicuous field is the last one.
Until then a muted terminal looked exactly like a quiet one.
Anyone who had switched the sounds off for a session and forgotten was waiting for a callback that could not come.
Now it says `snd` or `mute`.

## Only the threshold makes the line effective

Three days after the build came the rule that turned the display into a tool.
When the context fill turns yellow, from 25 percent, Claude proposes the context cut in that same turn, even if the work isn't at a clean point.
And before that it saves whatever isn't on disk yet, without asking.

For the first time, human and agent see the same state at the same moment.
I see the colour change, and the agent has a rule attached to exactly that colour.
Because the threshold is both in the line and in the instructions, I can check whether it keeps to its own rule.

The second half of the rule is the more important one.
A threshold alone would have produced the most expensive case there is: a punctual cut through unsaved work.
The number only says how full it is.

A channel that measures correctly and displays correctly has no effect until someone attaches a threshold to it.

## What I learned

- **State doesn't belong in the dialogue.** Asking about what is always true costs a turn every time. A display costs a process start.
- **Look first, then calculate.** The first version carefully invented a number the host delivered ready-made. In the end the field list came from real input and not from memory.
- **Fewer fields are the decision.** Being in the JSON doesn't earn a field a place in the line.
- **The number doesn't replace judgement.** It says how full it is, not whether a cut costs something right now. That's why the announcement stays with the agent.
- **A display only works with a threshold.** Without a rule attached it is just an instrument, with one it is a trigger for both sides.

## The same thing on your machine

For the status line, Claude Code calls any command you like and hands it the session state as JSON.
Before you display anything, have the command write that input to a file once and look at it.
The fields change between versions, and what is in there is more reliable than any list from memory, including an agent's.
A change to the line takes effect immediately, by the way, without restarting the session.
