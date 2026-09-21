---
parent: Frameworks
title: Process Under AI Agents
nav_order: 12
layout: default
---

# Process Under AI Agents

Every framework on these pages was designed when a human wrote each line of code. That assumption is
now unreliable, and the most useful thing this page can do is say precisely what the evidence
supports and where it stops.

*Reviewed September 2026. This page will date faster than anything else in this area.*

## 1. The outcome is unresolved, and that is the finding

The only systematic review available covers 39 peer-reviewed studies from 2014 to 2024 and concludes
that whether LLM-based assistants *"improve or degrade code quality remains unresolved, as existing
studies report contradictory outcomes contingent on context and evaluation criteria"*
{% cite mohamed2025llm %}. **59% of those studies are exploratory**, and few are longitudinal or
measure teams rather than individuals.

That last gap is the one that matters here. Measured against the SPACE dimensions, satisfaction is
studied in 77% of the work, while **communication appears in 26% and activity in 31%** — the
team-level dimensions a manager actually owns are the least studied.

Self-assessment is not a substitute. In a randomised trial, experienced open-source developers were
**19% slower** when using AI tooling while believing they had been **20% faster**
{% cite becker2025metr %}. That is the counterweight to any "the team says it helps" argument.

## 2. Expertise moves rather than disappearing

The first empirical study of vibe coding finds it *"does not eliminate the need for programming
expertise but rather redistributes it toward context management, rapid code evaluation, and decisions
about when to transition between AI-driven and manual manipulation of code"*
{% cite sarkar2025vibe %}. Trust is built *"through iterative verification rather than blanket
acceptance"*.

Practice also varies enormously between individuals — a grounded-theory study of 254 prompts finds a
spectrum from accepting generated code without inspecting it through to examining and adapting
everything {% cite chou2025dice %}. **Two developers on one team may be doing different jobs with the
same tool**, which is a management problem rather than a tooling one.

## 3. The manager's question is where the constraint moves

The useful question is not *does AI make developers faster* but **where does the constraint go when
generation gets cheap** — and this area already owns the tools to answer it.

**Example — the pipeline that got faster at one end.** A team adopts generation tooling and its
developers open roughly twice as many pull requests a week. The reviewers are the same people, doing
the same reading, at the same rate. Within a month the review queue holds two weeks of work, and the
time from *first line written* to *running in production* is longer than it was before the tooling
arrived — even though every individual developer is measurably faster and reports feeling more
productive.

<img src="/images/ai-review-queue.svg" alt="A board where AI-assisted development opens twenty pull requests a week, review clears ten with no WIP limit, and the review queue grows by ten a week" style="max-width:100%; margin:1.5em 0;" />

{: .fs-2 }
The [Kanban board](kanban.md) run backwards. The numbers are an illustration; the source says only
*"roughly twice as many pull requests"*.

That is [Kanban's](kanban.md) argument run backwards. The BBC team limited work in progress and cycle
time fell; here, generation outpaces a downstream stage and cycle time does not improve however fast
the code appears. It is also an [ETVX](../basics/etvx.md) exit-criterion problem — a pull request is
not finished output until it has cleared review, test, security and deployment.

Sarkar and Drosos independently identify **rapid evaluation of code you did not write** as the scarce
skill, which is the same conclusion from the other direction.

Practical consequences, where the evidence changes the claim:

- **[Kanban](kanban.md)** — the WIP limit that binds moves to the review stage.
- **[Scrum](scrum.md)** — sprint capacity assumes review capacity; a commitment set on generation
  speed is set on the wrong constraint.
- **[XP](xp.md)** — pairing and collective ownership were review mechanisms first. Ask what replaces
  them.

Everywhere else, this handbook says nothing, because there is nothing evidenced to say.

## How solid is this?

- **The systematic review reviews; it does not measure** {% cite mohamed2025llm %}. It reports no new
  effect size, and its December 2024 cut-off means it covers *assistants*, not the multi-file,
  tool-running **agents** this page is named for. That gap is real.
- **The vibe-coding study is five videos and four people**, publicly broadcast — creators performing
  for an audience, which is a stronger reactivity problem than ordinary observation. State the
  sample size wherever you cite it {% cite sarkar2025vibe %}.
- **The grounded-theory study is 20 self-selected streamed videos** {% cite chou2025dice %}; opinion
  videos are advocacy.
- **The naming of these phenomena — throughput paradox, verification tax — comes from an unrefereed,
  single-author preprint** that produces no numbers of its own {% cite bhati2026agentic %}. The
  vocabulary is useful; the reasoning above rests on Kanban and ETVX, which are far better evidenced
  and already in this handbook. Do not cite it as warrant.
- **The research-agenda paper is a vision paper** {% cite terragni2024future %} — position, not
  finding.
- **Write for the mechanism, not the specifics.** Where the constraint moves will outlast any
  particular tool named here.

---

### Acknowledgments

This page adapts material from lectures by **Eduardo Miranda** and **David Root**
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
