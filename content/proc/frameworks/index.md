---
parent: Process
title: Frameworks
nav_order: 3
layout: default
page_type: topic-hub
---

# Frameworks

A framework is a reusable structure of roles, events and practices that a team adopts and adapts.
Unlike a [lifecycle model](../lifecycles/), it says who does what and how often — and unlike a
process, it stops short of the detail of any one activity.

They sit on a spectrum from light to heavy. Weight is a **cost** bought for size and criticality, not
a virtue: see [balancing agility and discipline](balance.md).

<img src="/images/spectrum.svg" alt="XP, Kanban, Scrum, AUP/OpenUP, SAFe, RUP and TSP on a spectrum from more agile to more disciplined" style="max-width:100%; margin:1.5em 0;" />

{: .fs-2 }
Position is **how much the framework decides for you**, not quality. The ends are solid; the middle
ordering is a reading.

## Which page to read next

| Framework | What it optimises | Best fit | Main cost |
|---|---|---|---|
| [RUP and the Unified Process](rup.md) | Retiring architectural risk early | Large systems, architecture-dominant risk | Heavy unless deliberately tailored |
| [ACDM](acdm.md) | Deriving the plan from the architecture | Work where architectural risk dominates and estimates must be defensible | A method proposal — no trial, no comparison |
| [Synchronize and Stabilize](syncstab.md) | Parallel teams held together by frequent integration | Large commercial products, preview releases | Needs serious build and test infrastructure |
| [TSP and PSP](tsp.md) | Predictability through measurement | Long-lived teams, high-assurance work | Training and sustained data collection |
| [Extreme Programming](xp.md) | Very short engineering feedback loops | Small co-located teams, changing requirements | Social practices erode without protection |
| [Scrum](scrum.md) | Inspect-and-adapt on a fixed cadence | Product work that can hold a goal for a sprint | Poor fit for interrupt-driven work |
| [Kanban](kanban.md) | Flow and predictability | Maintenance, support, changing priorities | No roles or cadence supplied |
| [Lean](lean.md) | Removing waiting rather than working faster | Queue-constrained organisations | Manufacturing analogy transfers unevenly |
| [Scaling and SAFe](safe.md) | Coordinating many teams | Large multi-team programmes | Weakly evidenced; success factors are managerial |
| [Process Under AI Agents](agentic.md) | Naming where the constraint moves | Reading any of the above in 2026 | Evidence is early and unresolved |

Then two pages on deciding: [choosing a framework](choose.md) for what teams actually do, and
[balancing agility and discipline](balance.md) for matching weight to risk.

## How solid is this?

**No framework here has been shown to outperform another**, and the best-evidenced review of the
scaling frameworks declines to rank them deliberately {% cite edison_comparing_2022 %}. The "best
fit" column is reasoned from what each framework does, not from comparative outcome data. Evidence
quality varies sharply between these pages — Kanban has a measured case study, RUP and Sync-and-
Stabilize have no reviewed primary source at all — and each page states its own position.

---

### Acknowledgments

These pages adapt material from lectures by **Eduardo Miranda** and **David Root**
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
