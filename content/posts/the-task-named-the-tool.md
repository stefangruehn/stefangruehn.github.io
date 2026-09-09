---
title: "\"build a blog with hugo\": the task that contained its own answer"
date: 2026-09-08T09:00:00+02:00
draft: false
tags: ["claude-code", "hugo", "CI", "tooling", "measurement", "self-reference", "Essay"]
topics: ["shipping"]
summary: "The first task I gave the agent was six words long, and one of them was already the answer. The tool was settled before anyone had asked, and it was never measured. Here I make up for that, with the uncomfortable finding that Hugo ranks second, first, or nowhere at all, depending on which list you open."
---

*"build a blog with hugo"*

That was the task.
Six words, and one of them was already the answer.

The agent did not object.
It started building.

## In short

- The very first task I handed the agent already contained the tooling decision.
  There was no research, no comparison, no reasoning, just a name in the prompt.
- That's the sore spot: this blog claims in two places that things here get **measured** rather than asserted.
  The one decision everything else rests on was never measured at all.
- You can in fact look this up without crawling half the web yourself. There are at least three public rankings.
- But no two of them measure the same thing. **Hugo ranks second, ranks first, and doesn't appear at all**, depending on which one you open.
- Each ranking structurally favours a particular kind of tool: GitHub stars reward age, the `generator` meta tag rewards whoever leaves it switched on, npm downloads only see what ships through npm.
- The choice was still right, and I can now say what I base that on, namely four properties that actually carried their weight day to day.
- Nobody asked for the fourth one: because the whole chain is text files and commands, it could be driven entirely **from the outside**, from a phone. That part is untested.

---

## Six words, one of them the answer

I wrote "with hugo" into the prompt because I knew Hugo.
Not because I had compared anything.
The agent took the constraint as it stood and started building: structure, theme, bilingual setup, deployment.

That is, first of all, correct behaviour.
An agent that responds to "build X with Y" by opening a market survey is exhausting and usually in the way; a tooling constraint in the prompt is there to be followed, not relitigated at every turn.

Still, an uncomfortable gap remains.
The [topics page](/topics/) of this blog names two recurring themes: that AI-assisted tools are standard equipment, and that things here get measured rather than asserted.
On this task, the first one worked cleanly.
The second one never came into play.

So I'm making up for it.
I am not out to overturn the decision, it was a good one.
What interests me is what "good" can even mean here.

## What could have been in that slot

Netlify's collection lists over 500 static site generators.
For a bilingual text blog, maybe a handful were serious contenders, roughly sorted by construction:

- **One binary, no runtime:** Hugo (Go), Zola (Rust).
- **The ancestors:** Jekyll (Ruby) — GitHub Pages still builds it with no setup at all — and Middleman.
- **Python:** Pelican, MkDocs with the Material theme, which has effectively become the default for documentation.
- **JavaScript, content-first:** Astro, Eleventy, Docusaurus, VitePress.
- **JavaScript, app frameworks with static export:** Next.js, Nuxt, SvelteKit, Gatsby.

Gatsby is the cautionary tale here: acquired by Netlify in 2023, stable in maintenance ever since, and declining in adoption throughout.
A tool can be well kept and still be on its way out.

## Three rankings, three different quantities

The real question was whether any of this can be *looked up* rather than surveyed from scratch.
It can, in at least three places, all freely accessible, as of 8 September 2026:

| Source | measures | where Hugo lands |
|---|---|---|
| [jamstack.org/generators](https://jamstack.org/generators/) (Netlify, 500+ entries, sortable by GitHub stars) | **attention** | **second**, around 82,900 stars, behind Next.js (around 133,900), ahead of Docusaurus (around 61,400) |
| [W3Techs](https://w3techs.com/) | **websites actually served** | **first** among generators, on the order of 0.0x percent of all websites |
| npm downloads, e.g. via npm trends | **installs in JavaScript projects** | **nowhere**, because Hugo is a Go binary and simply doesn't exist on npm |

Three sources, three results, all three correct.
They don't contradict each other because one of them is wrong, but because they **count different things**.

And each one counts in a way that favours a particular kind of tool:

**GitHub stars are cumulative and practically never taken back.**
A star from 2016 weighs as much as one from yesterday.
So the list measures something closer to age times visibility than current use.

**W3Techs identifies a generator essentially by a meta tag.**
Hugo emits `<meta name="generator" content="Hugo …">` out of the box, and so does Jekyll, and plenty of themes strip it right back out again, for leanness or for discretion.
Switch the tag off and you vanish from the statistics.
Astro and Next.js, by contrast, leave runtime artefacts in the served HTML that nobody configures away by accident.
So the ranking doesn't measure use, it measures the **visibility of use**, and it systematically penalises exactly those generators whose output is cleanest.

**npm downloads are the most honest number and the narrowest one.**
They are reproducible and current, and Astro, for instance, sat at around 2.7 million weekly downloads in May 2026.
But they measure one ecosystem and mistake its edge for the edge of the world.
Anything not shipped as an npm package doesn't exist there.

Then there's a fourth kind, the kind you hit first when you search: "The 20 best static site generators of 2026".
That one measures nothing at all.
It is nonetheless the most widely quoted, and it is why this question passes for answered when it isn't.

That's the finding, and it's less comfortable than a ranking would be:
**there is no number for "the best tool", and there isn't even one for "the most used".**
There are three proxies you can look up, provided you say which one you mean.

## Why the choice holds up anyway

What you can measure is your own experience, and after a few weeks and a dozen or so posts it is clear enough.
Four properties actually carried their weight:

**One: fast.**
The build isn't a wait, it's a keystroke.
That sounds like convenience and is really a change in behaviour: a preview server that re-renders on every save makes proofreading in the browser the normal case rather than the exception.
Wait a minute for each build and you proofread in the editor instead, and miss everything that only shows up in the layout.

**Two: lightweight.**
A single static binary. No runtime, no `node_modules`, no supply chain of hundreds of transitive packages you neither read nor update.
What comes out the other end is HTML — no server, no database, no attack surface to maintain.

**Three: bilingual content and taxonomies are built in, not bolted on.**
Per-file language variants, a shared `translationKey`, custom taxonomies and series, all of it without a single plugin.
This blog depends on that completely: German and English aren't a special case here, they are the unit in which every post exists.
A generator where multilingual support is a plugin from 2019 would have become a problem by the third post.

**Four: checkers are cheap — and so are checkers for checkers.**
This is the one I hadn't counted on, and it has become the most important.
Because the input is text files and the output is HTML with no runtime, a checker is a short script.
Build twice and compare the text of every page against the text of the same page. Or hold the front matter of every post against a rule.
No headless browser, no test environment, no server that has to be running.

That produced, by 7 September, five checkers and four self-tests, which deliberately feed the checkers broken input and have to go red, or they aren't checking anything.
One of them found the incident that [the only other post in this topic so far](/posts/green-locally-broken-on-the-web/) is about: a single quotation mark that threw the minifier off course and wrecked a published page, with nothing whatsoever visible locally.

This is where the two themes meet.
"Measure, don't assert" stays a posture as long as measuring is expensive.
With this kind of construction, a new checker costs half an hour and then runs in under a second before every deploy.
That's the difference between an intention and a habit.

The honest counterweight belongs here too: Hugo's template language is awkward, and you notice the moment you reach into it yourself.
Anyone doing a lot of layout work will be less happy with it than someone writing text.

## What nobody asked for

What stands at the end is a chain made entirely of text files, Git and a CI run.
No click path, no interface, no program that has to be running for anything to happen.

From that follows a property that appeared in no prompt: the whole chain **could be driven from the outside**.
Capture an idea, write a draft, check the preview, run the checkers, publish: every one of those is a file operation or a command, and every one of them could be done remotely, through Claude Code Remote Control or from a phone via the Claude app.
The only prerequisite would be that the machine is reachable from outside.

Conditional, and the conditional stays: **I haven't tested this.**
The machine isn't reachable from outside so far, and until it is, that paragraph is a plausibility argument and not a measurement.
In a post whose thesis is "measure, don't assert", that is exactly the thing to say out loud.

It's interesting regardless, because it shows how a tooling choice keeps having effects.
A chain of files and commands can be operated remotely.
A chain of clicks cannot.
That was no part of the decision.
It's a by-product, and it's worth more than most of the criteria I could have written down.

## What's left

The tooling choice was never a choice.
It was in the prompt, it was right, and it was unexamined — three things that can all be true at once.

What I take away is less about Hugo than about the question itself.
If you want to know whether a tool is "leading", you can look it up, in several places, without running your own survey.
You will then get three different answers and have to decide for yourself which quantity you actually meant.
That isn't a shortcoming of the sources. That's the normal case for any number you didn't collect yourself.

And yes: the numbers in this post were fetched by the same agent that didn't ask back then.
I opened each source myself before they went in here.
That needs checking too — otherwise this post would be precisely the mistake it describes.
