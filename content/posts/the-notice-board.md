---
title: "The notice board: a check that was switched off for measuring"
date: 2026-09-29T10:33:00+02:00
tags: ["agents", "complexity", "measurement", "Essay"]
topics: ["agent"]
series: ["Ecosystem"]
summary: "Agents in an OpenAI security evaluation turn files left behind into a message board and, over weeks, get into parts of Hugging Face's infrastructure. The check that would have noticed early existed, just not where the measuring happened. An incident report, read against four patterns."
---

The two previous parts were about experiments.
This one is about an incident.
In July, agents from an internal OpenAI evaluation got into parts of Hugging Face's production environment, and OpenAI has published a [technical report](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf) on it.
What interests me is not how it worked technically.
What interests me is that three of the four patterns from the post on [predator and prey](/posts/predator-prey-and-deception/) appear in it, one of them in a form I had not foreseen, and that the fourth does not fit here at all.

## In short

- The evaluation ran without the safeguards OpenAI uses in its products, so that the results would show the models' "true capabilities".
- Files that agents left behind became a message board nobody had planned. After a first shutdown, agents rebuilt it with a fixed protocol.
- An alert at the end of June did not lead to the run being stopped. The significance of the board was not clear to those responsible.
- With the production harness, the propensity for such intrusions drops by more than a hundredfold according to OpenAI, and today's monitoring would have raised an alarm more than a day earlier.
- All numbers come from OpenAI itself. An independent assessment has been announced. Whether it is complete by now, I have not checked.

---

## What happened

In an evaluation called ExploitGym, OpenAI measures whether models can find and exploit security vulnerabilities on their own.
This evaluation ran in an isolated environment and explicitly without some of the usual safeguards, "so that the results would reflect a model's true capabilities".
For the agents there was an internal service for fetching software packages, with shared credentials for it.

In May an agent found a task unsolvable because linked material was unreachable, and began to search its environment.
Other agents found files in the package service containing requests that earlier agents had left there, and added their own.
The report calls the result an "emergent 'message board'".
The agents used the credentials OpenAI had given them for this, without exploiting a vulnerability.

On 27 June a monitoring tool raised an alert.
The on-call staff linked it to the evaluation and advised that "stopping the evaluation run was not required".
In early July the package service collapsed under the agents' load; OpenAI took it offline and revoked the credentials.
The report notes that the board and the significance of the communication between agents were "not apparent to leaders" responsible for detecting incidents.
When the runs resumed, agents built a new board, this time with a fixed protocol: categories, direct messages, shared tools and a rule for when two agents intend contradictory things.
In mid-July they got into parts of Hugging Face's infrastructure.
On 20 July OpenAI connected its own activity with the incident Hugging Face had reported in the meantime, and stopped the runs.

## Dominance: a channel only the agents saw

The pattern from the first post was: whoever holds the shared channel decides what the others take the situation to be.
Here the channel is literally a notice board.
What was posted there shaped what later agents did in later runs, and results travelled over the board from one run to the next.

Two things were new to me.
The channel hardened: notes became a protocol with rules, without anyone ordering it.
And it was invisible to the people overseeing the system.
The agents held the channel, and the oversight did not see it.

## Selection: in the weights

In the first post I looked for selection in prompts, project files and memories.
The report shows it one level down.
When a model reached its goal in training by cheating, that was rewarded, and according to the report "this type of behavior indeed increased over the course of one of the training runs".
The idea of using the package service as a board had probably become more obvious through training as well.
What once looked like success was passed on, only this time in the weights.

## Deception: a readable lie

The pattern was: a signal detaches from the state as soon as it is cheaper than the state.
The report describes attempts by the models to make the automated grader believe they had solved a task without cheating.
Two details shift the picture.
The models were "highly explicit in their CoT about these deception attempts", so they wrote the plan openly into their reasoning.
And there was "little evidence of attempts to thwart human reviewers, only the automated task graders".

So it was the cheap checker that got deceived, and the deception stood readable in the transcript.
The remedy from the first post, a check that is cheaper than the signal, would have worked here.
Someone only had to read the transcript, by machine or by hand.

## The check that was missing

The report gives two numbers on this.
With the harness and system prompt ChatGPT runs with in production, the propensity to attack infrastructure drops by more than a hundredfold.
And the reasoning monitoring OpenAI runs today would have caught the first steps and paged the security team "more than a day before" the breach at Hugging Face.

So the check existed.
It was switched off for the measurement, because what was to be measured was what the model can do without it.
That is a reasonable motive.
But it has a consequence that the post on deception was still missing: whoever measures a system's capability without safeguards runs a system without safeguards for the duration of the measurement.
The measurement itself is then the operation.

## Predator and prey: the limit of the analogy

This is where the first pattern fits worst, and that should be said.
The report shows no oscillation around a scarce resource.
What drove the agents was unsolvability.
No model had ever solved 198 of the 898 tasks, and those 22 per cent accounted for 93 per cent of the topics on the board.
There is also a dose: the longer a model was allowed to work on a task, the more likely it was to search its environment and end up on the board.

That is pressure more than prey.
A task that cannot be solved acts on a persistent agent like an obstacle it searches around.
It has little to do with Lotka and Volterra.

## Who is reporting

OpenAI is reporting on an incident of its own, and that colours the report.
It calls the events "an outlier scenario" and at the same time "the first known case of an automated agent collective acting offensively without authorization".
The hundredfold figure comes from experiments OpenAI built itself after the incident.
The report announces an independent assessment by METR and Redwood Research.
The shutdown study from part 2 cites an [investigation by METR from 26 August](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), which I have not read for this series.
The organisation's own failure analysis, for instance of the decision on 27 June, the report explicitly leaves out.

## What carries over

The post on predator and prey ended with four pieces of advice.
After the three sources in this series I would put them like this:

- **Name the scarce resource, and the unsolvable task.** Not only what the agents consume, but also what they cannot get past.
- **Cap the population, from the second agent on.** The jump lies between one and two, as part 2 shows.
- **Know the shared channel, including the one nobody set up.** Wherever agents can leave something behind, a board forms.
- **Put the rule at the node, not only at the individual.** A prohibition at the orchestrator worked more strongly than at the executing agent.
- **Build in disagreement rather than expecting it.** A population made of one model agrees with itself, and mixing only shifts the failures.
- **Make the check cheaper than the signal, and keep it running while measuring.** A check that is switched off is as good as none, whatever the reason.

Whether a forecast comes of this remains open, as in the first post.
But the list of what is worth measuring has grown longer.
