---
title: "The watermark that does exist after all"
date: 2026-09-18T11:55:00+02:00
draft: true
tags: ["claude-code", "writing", "authorship", "Essay"]
topics: ["author"]
series: ["Authorship"]
summary: "On 6 September I asked Claude whether its texts carry a watermark. The answer was no, and it was wrong: Anthropic had announced the watermark three weeks earlier. The second half of the answer was right. Changing one word sets off nothing elsewhere in the text. Something can now be detected, but not what the question was after, and not by me."
---

On 6 September I asked Claude a question that had come to me while proofreading:

> Do the texts you generate or revise contain watermarks? Then changing just one word would automatically create side effects in other places in the text, and that could be shown with a diff, right?

The answer began like this:

> **Watermarks (point 6): no — and the proof idea would not hold even then.** Anthropic does not embed a watermark in Claude's text output, neither a statistical sampling watermark (that does exist, but at Google for Gemini: SynthID-Text) nor invisible characters.

The first half of that answer was wrong.
The second was right.
This post is about both.

## Summary

- On 14 August 2026 Anthropic announced that Claude's text carries a watermark.
  The answer of 6 September came three weeks later and denied it.
- A watermark of this kind is a pattern in word choice.
  It is laid down while writing and then sits still in the text.
- That is why a changed word sets off nothing elsewhere.
  The idea of proving it with a diff does not hold, not even now.
- Only authorised parties can check, not me.
  And the result says that Claude was involved, not which sentence is whose.
- The English versions of this blog are translated by Claude.
  If anything here is marked, it is more likely them than the German ones.
- Without the key, all that is left is style, and style is a clue, not proof.

---

## What was already known on 6 September

On 14 August 2026 Anthropic explained [how Claude's text watermark works](https://www.anthropic.com/news/claude-text-watermark).
The first sentence reads: "Future Claude models will generate text that contains a watermark."
The reason is the EU's AI Act.
In July 2026 Anthropic signed an EU code of practice that requires providers to mark AI-generated text.
A [help article](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) lists the models this applies to.

The answer I got came from Claude Opus 5.
The help article names marking explicitly for that model.
Whether the answer itself was marked, I cannot check.

Why the answer was wrong can still be said.
It came from what the model had learned in training, and the announcement was more recent.
Nobody looked it up at the time, neither Claude nor I.
The wrong half sounded just as certain as the right one.

## How the mark gets into the text

A language model writes word by word.
At each point it has a list of possible next words, and often several fit equally well.
A watermark uses exactly those choices.

The basic method was [described in 2023](https://arxiv.org/abs/2301.10226) by John Kirchenbauer and colleagues.
Before each word, the preceding words and a secret key determine a random "green" half of the vocabulary.
The model then slightly prefers green words.
Whoever holds the key counts afterwards how many words of a text are green.
For a human it is roughly half, for a marked text clearly more.
Beyond a set threshold the text counts as marked, and the chance of misjudging a human text in the process is, in the paper's example, three in a hundred thousand.

Anthropic describes the same principle.
The key and the few words before it decide which word the model picks among equivalent ones.
"Nothing is added to the text and there are no hidden characters."
Google has marked Gemini's answers this way since 2024, with a method called SynthID-Text, [described in Nature](https://www.nature.com/articles/s41586-024-08025-4).

## Why a changed word sets off nothing

My question of 6 September rested on a picture: that a watermark links the places in a text like a checksum, so that a change in one place causes something in others.

That is not how it works.
The mark is a pattern in choices that were made once, while writing.
After that the text no longer computes anything.
Changing a word changes the count at that spot and at the few following words whose green list depended on it.
Nothing happens anywhere else.
According to Kirchenbauer, removing the mark from a long text takes changing roughly a quarter of the words.
Anthropic says much the same for its own case: light editing probably won't remove it, a complete rewrite will.

The effect I had seen in the diff was real all the same.
It just has another cause.
Whoever revises a sentence touches the neighbouring ones too, because rhythm and connection no longer fit otherwise.
In a diff that revision looks like action at a distance.
This half of the old answer still stands.

## Who can check, and what comes out

Anthropic offers checking through an interface that, in September 2026, runs as a private preview.
Access is for parties provided for under EU law: regulators, law enforcement, media, fact-checkers, researchers, educational organisations and civil society groups.
I am not one of them.
I cannot look at my own texts to see whether, or how strongly, they are marked.

And whoever can look learns less than my question wanted.
By Anthropic's own description, the mark only shows that Claude was likely involved "at some point".
"It cannot distinguish 'Claude wrote this' from 'Claude heavily edited this.'"
On short texts the signal is weak, and on facts as well, because there is little equivalent choice of words there.

The [second part](/posts/retouched-by-my-hand/) of this series was about the grades of the auction catalogue.
The watermark delivers one of them: "Workshop of".
Which hand painted which passage, it does not deliver.

## Which version of this blog would be marked

The entry pages say that the writing style of the German pages is mine and that the English versions are translated from them.
Claude translates them.

On this Anthropic writes: "A translation produced by Claude carries a watermark, because in this case every word is chosen by Claude."
The German pages are made with Claude as well.
But what I rearrange and reword while proofreading weakens a mark, if there is one.
Claude brings the English version into line after every change, and every one of its words was chosen by Claude.

So if anything on this blog is marked, it is more likely the version that follows my style only as far as English allows.
The content is the same in both.
Whether the models used here actually mark text on the route I use cannot be checked from outside.
That is the state of things on 18 September.

## Without the key, style is what remains

Whoever lacks the key can only look at style.
Anthropic draws that line in the same explanation: detection services look for telltale phrasing, such as the construction "this isn't [X], it's [Y]" or the word "quietly".
"Picking up on these patterns is fundamentally different from checking for a watermark."

That is an old method.
In the 19th century the art historian Giovanni Morelli attributed paintings by incidentals, the shape of ears and fingernails that a copyist would not attend to.
He himself objected, though, when people said he recognised a painter by the ear alone.
In the [English edition](https://archive.org/details/gri_33125000150405) he writes that the forms "aid us in distinguishing the works of a master from those of his imitators".
They help; they do not decide.

For text the numbers are sobering.
OpenAI [withdrew](https://openai.com/index/new-ai-classifier-for-indicating-ai-written-text/) its own classifier for AI-written text in July 2023.
It had identified 26 per cent of AI-written texts and labelled 9 per cent of human-written texts as AI-written.
A [study in Patterns](https://doi.org/10.1016/j.patter.2023.100779) ran seven detectors over TOEFL essays written by people who did not grow up with English.
On average they took 61.3 per cent of them for machine text.

## What remains

On 6 September I got two answers in one paragraph.
One was wrong, the other right, and both sounded the same.
The [first part](/posts/who-built-the-chain/) of this series asks for verifiability when the material does not come from me.
A statement about what a provider does today belongs to that, even when it comes from the provider's own model.
The model does not know what was announced after its training, and it does not say so unprompted.

The series began with the question of who is writing here.
Something can now be detected, but not by me, and not at the level of sentences.
The seam between my hand and Claude's stays invisible in the text.
It only becomes visible where someone declares it.

This is the third and final part of the series [Authorship](/series/authorship/).
