---
parent: Frameworks
title: Choosing a Framework
nav_order: 9
layout: default
---

# Choosing a Framework

Choosing a framework looks like picking from a menu and is not. The evidence is that teams accrete
practices rather than adopt methods whole — so the useful question is not *which framework* but
*which practices, and what will we stop doing?*

## 1. What teams actually do

Hybrid approaches *"have become reality for nearly all companies"*, are used *"even in the presence
of company-wide policies"*, and are *"neither planned nor designed but emerge from the evolution of
different work practices"* {% cite kuhrmann2019hybrid %}. Only about a fifth of the hybrids surveyed
came out of a planned improvement programme.

More striking is **what** travels. In the same survey the most widely adopted **practices** — code
review at 69.6%, continuous integration at 63.8%, unit testing at 59.4% — are adopted more widely
than the most popular **methods**, Scrum at 53.6% and waterfall at 34.8%.

**The unit of decision is the practice, not the method.** Practices move between contexts; methods
do not. SWEBOK says the same from the standards side: there are *"new methods arising from
combinations of agile and plan-based methods"*, and business needs *"should and do drive the choice…
or in constructing a new method from the best features of a combination"* {% cite bourque_swebok_2014 %}.

That is not evidence that management has failed to decide. It is evidence that the thing being
decided is **smaller than a framework**.

## 2. A scoring instrument, and its flaw

Where a genuine selection is required, a tally makes the reasoning auditable. Rockwood scores five
methods — RUP, Microsoft's [Synchronize and Stabilize](syncstab.md), [TSP](tsp.md), [XP](xp.md) and
[Scrum](scrum.md) — against eleven questions in four groups, marking each **1 = inherent weakness,
2 = neutral, 3 = inherent strength** {% cite rockwood_choose_2003 %}.

**Example — running the tally on Scrum.** Asked about artefact overhead, *"Scrum would score a 3…
but TSP may score a 1"*: Scrum prescribes few documents, TSP prescribes many. Asked about team size,
Scrum scores badly — it is optimal at **seven or fewer**, and beyond that the prescription is to
split into multiple Scrums, which shifts the coordination problem rather than solving it. Asked about
traceability, Scrum again scores low, because nothing in the framework requires a requirement to be
traceable to the work that satisfied it. A team needing an audit trail reads those two rows and stops.

The flaw is visible in the instrument's own words: *"the order of presentation does not imply the
order of importance"* — in a scheme that weights every question **equally**. A project where
criticality dominates everything else cannot say so in the total.

Set that beside [Boehm and Turner](balance.md), who use five continuous axes where Rockwood uses
eleven equal discrete questions. **The shape of the instrument changes the decision it produces**,
which is the most transferable thing on this page. Neither is objective; both make reasoning
inspectable, which is a different and more achievable goal.

## 3. Four questions worth answering

1. **What is the team already doing?** There is always an existing process, explicit or not, and it
   is the thing being changed.
2. **What does the risk profile demand?** Size, criticality and dynamism decide how much weight the
   project can afford — see [balancing agility and discipline](balance.md).
3. **Which practices close the gap?** Name the specific practices, because the practice is the unit
   that actually travels between teams.
4. **What will you stop doing?** This is the question nobody asks, and the one that makes the other
   three real.

The fourth is the one that makes the others real. Adopting practices without retiring any produces a
process with two of everything. And it happens by default if left undecided: on a large XP project
tracked over eighteen months, *"almost all the practices have evolved"* — the **engineering**
practices survived while the **social** ones eroded {% cite elssamadisy_xp_2001 %}. Nobody chose
that. A manager who does not ask what to stop finds out afterwards which practices the organisation
was actually willing to pay for.

## How solid is this?

- **`kuhrmann2019hybrid` is 69 self-selected European respondents**, surveyed in 2016. Quote its
  figures as *of 69 respondents*, and note its own 19.6%/83.9% split does not sum to 100. It shows
  hybrids are **used** — it has no outcome data and cannot show they work better.
- **Rockwood is grey literature** — a technical report, undated in the document, whose weights are
  one author's judgement {% cite rockwood_choose_2003 %}. **Do not present the tally as objective.**
- **`elssamadisy_xp_2001` is a participant's report on one project**, unpublished and self-dated.
  Read the erosion pattern as a plausible mechanism, not a measured rate.
- **No instrument on this page has been validated.** No study shows teams that select a method
  formally do better than teams that do not.

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
