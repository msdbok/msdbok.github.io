---
parent: Frameworks
title: Lean Software Development
nav_order: 8
layout: default
---

# Lean Software Development

Lean software development adapts ideas from Toyota's production system to building software: identify
what the customer values, remove everything that does not contribute to it, and make work flow rather
than sit in queues {% cite poppendieck2003lean %}.

It is less a method than a lens. [Kanban](kanban.md) is the operational form most teams actually
adopt; lean is where its reasoning comes from.

## 1. Waste is mostly waiting, not working

The core move is to look at the **time work spends idle** rather than at how fast people work. In
most software organisations a change spends far longer waiting — for review, for a test environment,
for a release window, for a decision — than being worked on. Effort spent making the working parts
faster leaves the waiting untouched.

The forms of waste that translate best to software are partially done work, extra features nobody
asked for, handoffs, delays, and defects. Each is inventory of some kind: something started, not
finished, and losing value while it sits.

Two consequences follow, and both are counterintuitive to managers rewarded for starting things:

- **Starting less finishes more.** Work in flight is inventory, and inventory hides problems.
- **Small batches beat large ones.** A large change waits longer, is riskier to integrate, and takes
  longer to diagnose when it fails.

## 2. The evidence, and what it actually shows

**Example — BBC Worldwide.** A nine-person team adopted lean and Kanban and was measured over twelve
months: lead time fell **37%**, lead-time variability fell from 70.7 to 37.3 days, and
customer-reported defects fell from 2.9 to 2.2 per week {% cite middleton2012kanban %}.

The row that explains the rest is that the team **started 24% fewer features** — 84 down to 64 — and
cut them smaller, with the share classified as small rising from 52% to 75%.

Read that precisely. What improved is **flow and predictability**. The paper is explicit that output
value *"cannot be measured exactly"*, so this is not a demonstration that more got done. The team
started less, and what it started finished sooner and more predictably.

## 3. Where it applies, and where the reasoning stops

Lean thinking is most useful where the constraint is a queue rather than a skill — long review
backlogs, slow release cadence, work sitting in "ready for test". It has least to say where the
bottleneck is genuinely a hard technical problem that one person has to solve by thinking.

Its manufacturing ancestry is also its main hazard. Software is not identical units flowing down a
line: each change is unique, estimates are unreliable, and "inventory" is a metaphor rather than a
count of physical things. The parts that transfer well are the ones about **queues and batch size**,
which are properties of any flow system. The parts that transfer badly are the ones assuming
repeatable, measurable unit work.

## How solid is this?

- **The evidence base here is one team, one company, twelve months, no control group.** The authors
  say the hypothesis was *"supported by this single case study"* {% cite middleton2012kanban %}.
- **It is confounded.** In the same period the team rewrote legacy code and reduced turnover — both
  plausible causes of the defect improvement, which the authors themselves hedge as *"possibly due to
  the improving structure of the code base"*.
- **Do not say throughput rose because waste fell.** Cycle time fell as work in progress fell.
  Throughput was not measured.
- **Poppendieck and Poppendieck's book is named as the origin** of lean software development
  {% cite poppendieck2003lean %} and was not read for this review; no claim here is attributed to it.
- **The underlying lean literature is industrial, not software-specific.** Its transfer to software
  is argued by analogy and has not been tested against an alternative.

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
