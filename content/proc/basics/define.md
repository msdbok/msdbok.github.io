---
parent: Basics
title: Defining a Process
nav_order: 2
layout: default
---

# Defining a Process

Defining a process means writing down what is actually done, step by step, together with the reason
each step exists. Every team already has a process; defining it is the act of making it explicit
enough to be taught, checked and improved.

The reason matters as much as the step. A step nobody can justify beyond *we have always done it
that way* is the first candidate for removal, and a process document full of them will be complied
with rather than used.

## 1. Ask the people who do the work

The method is unglamorous: ask *how do you do it?*, and keep asking until each step can be described
without hand-waving. Useful starting points are the training material a new joiner is given, riding
along with someone experienced while they actually do it, and — the part that gets skipped — asking
the **doers rather than the managers**. The two groups describe different processes, and the
manager's version is usually the one that was designed rather than the one that runs.

Radice, deploying process definition at IBM, drew the same conclusion from the other end: *"Defining
the process and getting it accepted from the bottom up were the two essential parts of the
solution"* {% cite radice_programming_1985 %}.

Once a step is described, [ETVX](etvx.md) is the notation for pinning it down — entry conditions,
task, validation, exit criteria.

## 2. Improve it in a loop, not in a rewrite

Process improvement inherits the Deming cycle. The value is in the **Check** step, which is also the
one most often dropped — a process changed and never re-examined is indistinguishable from a process
changed on a hunch.

<img src="/images/pdca.svg" alt="The Plan-Do-Check-Act cycle: plan the change and what you expect of it, do it reversibly and collect data, check the result against the prediction, then adopt, revise or drop it and repeat." style="max-width:100%; margin:1.5em 0;" />

## 3. Check conformance and results separately

Two different questions hide behind "is the process working?". The first is whether it is being
*followed* — answered by inspections, reviews, audits and checklist compliance. The second is
whether following it produces the outcomes it was meant to. A process can be followed faithfully and
still be the wrong process, and a good outcome can happen despite the process; separating the
questions keeps you from concluding the wrong thing.

Conformance can be checked on a planned cycle or by unannounced sampling, and postmortem review after
a release catches what neither sees. **Defect seeding** — deliberately introducing known defects to
see how many the process catches — measures detection capability directly, at the cost of some
goodwill if it is done without telling anyone.

**Example — a meeting process.** Meetings are the smallest process worth defining, and a good place
to practise. Define the steps: an agenda circulated in advance, a named owner, decisions and action
items recorded with owners and dates. Then decide what tells you it is working — attendance,
whether the agenda was circulated at all, and the proportion of action items closed by the next
meeting. Then run the loop: if action items stop closing, the fix is usually assigning owners at the
meeting rather than afterwards, and the next cycle tells you whether that was right.

## 4. Choose the measures with care, and know what they do to people

Not every useful measure is a number — a boolean *is the process being used?* is often the most
informative thing you can collect early on. Whatever you pick should be derived from a goal rather
than from what the tooling emits, which is [GQM](gqm.md), and it needs a baseline to be read against.
Baselines mislead easily: one taken during an unusual quarter becomes the standard by which normal
quarters look like failures.

And measures of a process are measures of the people running it. That is not a footnote; it is the
main hazard, and it has its own page — [process metrics](metrics.md).

## How solid is this?

- **This page is practice, not evidence.** It sets out how process definition is taught in this
  course, drawing on Miranda and Root's lecture material {% cite root2014lectures %}. No source here
  measures whether a defined process outperforms an undefined one.
- **Radice's bottom-up finding is an experience report** from one company's deployment
  {% cite radice_programming_1985 %} — consistent with everything else in this area, but a single
  industrial case.
- **PDCA is attributed to Deming** and reached software through the quality movement rather than
  through software research; see [history](history.md). It is a widely used framework of long
  standing, not a tested intervention.
- **Defect seeding assumes seeded defects resemble real ones.** If they are easier to find, detection
  capability is overstated.

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
