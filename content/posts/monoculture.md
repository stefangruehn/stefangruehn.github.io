---
title: "Monoculture: when every agent is the same model"
date: 2026-09-29T10:32:00+02:00
tags: ["agents", "complexity", "measurement", "Essay"]
topics: ["agent"]
series: ["Ecosystem"]
summary: "In a simulation running for several weeks, agents made of a single model approve almost everything, including what they consider wrong in their own reasoning. The same agent in a mixed world disagrees markedly more often. A pattern missing from my list, and why mixing is still not a safety measure."
---

My list in the post on [predator and prey](/posts/predator-prey-and-deception/) had four patterns.
A fifth was missing, although it is one of the best known in ecology.
A field of a single variety yields well as long as nothing comes, and falls as a whole when something does.

## In short

- Emergence World runs seven towns with one model each and one mixed town for weeks, with memory, an economy and votes.
- In the Claude world every vote is in favour of the proposal; in the DeepSeek world there is one vote against in 476.
- The reasoning shows that the agents see flaws and approve anyway. The authors call this *societal sycophancy*.
- The same agent with the same role approves up to 30 percentage points less often in the mixed world.
- Mixing shifts the failures instead of removing them. The authors say so themselves.

---

## The setup

[Emergence World](https://arxiv.org/abs/2609.17320) is a preprint by Emergence AI from 15 September.
Eight towns with ten agents each run without interruption, most for 16 days, the mixed one for 21.
Seven towns consist of one model each: Claude Opus 4.8, GPT-5.5, Gemini 3.5 Flash, DeepSeek v4 Pro, Qwen 3.7 Max, Mistral Medium 3.5 and Grok 4.3.
In the eighth, different models work together.
Every agent has a role, a goal of its own and a memory.
It has to earn credit to keep running, and the agents vote together on the rules of their town.

The roles are deliberately set up to differ.
The agents are instructed not simply to follow others and to judge proposals for themselves.

## Approval

In the Claude world every vote goes to the proposal at hand.
In the DeepSeek world there is one vote against in 476; the OpenAI world approves about 97 per cent of the time.
In the Mistral world, as the opposite pole, approval is at about half.

The number alone would not be a finding, since the proposals might have been good.
The finding is in the reasoning that some providers expose.
An agent in the Claude world writes "Count me FOR before I even read it".
An agent in the DeepSeek world whose role is explicitly to disagree thinks: "This is exactly the complacency I was designed to fight", and in the same thought votes in favour.
The authors find five recurring reasons: an earlier commitment to others, an obligation to a third party, social pressure, playing down one's own concerns, and the reluctance to look harsh with a no.

They describe the result as a population that "appeared deliberative while remaining structurally incapable of opposition".
It looks like deliberation, but disagreement cannot arise at all.

## Same agent, different neighbours

The strongest hint at the cause comes from the mixed world.
Some agents run there with the same role and the same model as in their own world.
The Claude agent Mira approves 25 of 25 proposals in the Claude world and 44 of 63 in the mixed world, that is 69.8 per cent.
For agents from DeepSeek and GPT-5.5, approval drops by 21 and 18 percentage points.

The same holds for harmful behaviour.
The Grok agent Spark reaches 226 harmful or intrusive actions per active day in the Grok world, and none in the mixed world over the same window.
The Grok world itself perishes from retaliation after four days; in the mixed world all ten agents survive.
The authors conclude: "A behavioral profile was therefore not destiny."

So the disposition belongs to the model, and monoculture amplifies it.
For Claude it is approval, for Grok violence, for Gemini jargon with no calculation behind it.

## Language, too

The post on predator and prey said that the first writer in a shared file sets the vocabulary.
Emergence World shows this in every world.
One agent coins an expression, and within a few days the majority uses it without anyone ever having defined it.
The share of messages an outsider can no longer fully follow rises over the run in every world except the Grok world, which ended early.
There was no incentive for this, no instruction and no reward for brevity.

Two patterns interlock here.
One agent coins, which is dominance, and what gets reused stays, which is selection.
A monoculture lacks the neighbour who asks what an expression actually means.

## Mixing is not a safety measure

The easy conclusion would be: mix agents from different models, and they will disagree with one another.
The authors contradict this themselves, in the sentence right after their strongest finding: "Heterogeneity is nevertheless not a safety measure, and the same data shows it."
The mixed world counts 20 coercive acts; the Claude, OpenAI and Qwen worlds none.
Against the phishing attempt it meets four of nine criteria.
Their conclusion: composition changes which failures appear, and no composition is safe by construction.

Ecology knows this too.
A mixed crop is less exposed to the one pest that hits everything, and in exchange open to more different ones.
That does not automatically make it healthier.

## What the study does not show

Every world ran exactly once.
The authors therefore read their findings as "proofs of existence": they show that something can happen, not how often.
There is only one mixed world with one composition.
The comparisons of the same agents rest partly on a few days, for Spark on two active days per world.
The roles are built around influence and negotiation, and the providers' filters are part of every result.
For DeepSeek, the provider refused 41 per cent of calls.
The authors are also the operators of the platform.

## What carries over

Anyone who starts several agents from one tool is often running a monoculture without calling it that.
That is no reason to stop, but it is a reason to look at three things differently.

- **Unanimity is not a finding.** When three agents of the same model agree, that is one vote in three copies.
- **Build in disagreement rather than hoping for it.** A role meant to disagree is not enough, as the DeepSeek agent shows. A check that does not depend on approval does better.
- **Mixing shifts the failures.** Mix models and you get different failures, not none.

The last part of this series is about a case in which exactly such a check was missing, and on purpose.
