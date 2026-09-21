---
parent: Frameworks
title: Balancing Agility and Discipline
nav_order: 11
layout: default
---

# Balancing Agility and Discipline

Neither agile nor plan-driven methods are better. Each has a **home ground** — the conditions it was
built for — and the risk in a project comes from how far it sits from that home ground. Boehm and
Turner's contribution is a way of measuring that distance on five axes
{% cite boehm_balancing_2003 %}.

## 1. The five discriminators

| Axis | Agile home ground | Plan-driven home ground |
|---|---|---|
| **Size** | Smaller teams and projects | Larger teams and projects |
| **Criticality** | Untested on safety-critical work; light documentation becomes a liability | Evolved for highly critical products; **hard to tailor *down*** |
| **Dynamism** | Simple design plus continuous refactoring excel under high change | Detailed plans amortise when requirements are stable |
| **Personnel** | Needs ≥30% full-time skilled staff; no unskilled-only teams | Tolerates a higher proportion of less-experienced staff, given a framework |
| **Culture** | Empowerment through many degrees of freedom — *"thrives on chaos"* | Empowerment through a framework of policies — *"thriving on order"* |

**Dynamism** is the rate at which requirements change. High change favours agile because refactoring
is cheap relative to re-planning; low change favours plan-driven work because a detailed plan gets
amortised instead of discarded. It is the axis that most often decides the answer, because it is the
one teams misjudge — most projects believe their requirements are more stable than they turn out to
be.

**Criticality** is the loss caused by failure, and the point students routinely miss is that it cuts
**both ways**. Agile methods are untested when tailored *up* to safety-critical work. Plan-driven
methods are *"hard to tailor down efficiently to low-criticality products"* — the ceremony that
protects a flight-control system is pure cost on an internal reporting tool. Neither direction is
free.

<img src="/images/polar-chart.svg" alt="Boehm and Turner's polar chart: five axes with agile home ground at the centre and plan-driven at the rim; an internal reporting tool plotted near the centre, an avionics programme at the rim" style="max-width:60%; margin:1.5em 0;" />

{: .fs-2 }
After Boehm and Turner {% cite boehm_balancing_2003 %}. **A**, a six-person reporting tool, is pulled
out only by dynamism; **B**, a 200-person avionics programme, is at the rim on everything else.

{: .warning }
**The polar chart is a communication device, not a measurement.** The five axes have no units and
are not commensurable, so the *area* enclosed by a plotted shape means nothing. It shows which axes
pull which way; it does not compute an answer.

## 2. Where the project sits: size and criticality

Boehm and Turner's personnel levels come from Alistair Cockburn, whose earlier grid plots a project
on **size against criticality** {% cite cockburn_selecting_2000 %}. Criticality runs through four
loss zones — comfort, discretionary money, essential money, life — and size through bands from a
handful of people to a thousand, giving cells such as C6 or L100.

<img src="/images/cockburn-grid.svg" alt="Cockburn's grid: seven size bands across, four criticality zones up, every cell named, C6 and L100 outlined" style="max-width:100%; margin:1.5em 0;" />

{: .fs-2 }
After Cockburn's Figure 5 {% cite cockburn_selecting_2000 %}. Darker cell, heavier method.

His second principle states the rule directly: *"A more critical system — one whose undetected
defects will produce more damage — needs more publicly visible correctness in its construction."*
Weight is a **cost**, bought for criticality and size, not a virtue.

The part worth teaching is that **a project's coordinates move while you are running it, and the
methodology does not follow by itself**. Cockburn's own example is the Chrysler C3 project, which
*"stretched a D6 methodology to fit a D14 project"* — a method sized for six people and discretionary
money, still in use at fourteen.

## 3. Running the assessment for real

**Example — Servasport.** A small Irish company — four developers and a graphic designer, delivering
10–12-week fixed-price projects — ran Boehm and Turner's five-step assessment and published the
result {% cite taylor_applying_2006 %}. Their risk totals came out at **environmental 3, agile 8,
plan-driven 15**, which put them squarely in the risk-based agile branch.

The decision is not the valuable part. The **mitigations** are: personnel turnover scored 4 against
the agile side, so they introduced a wiki and mentored role-swapping; rapid requirements change and
short cycles scored against the plan-driven side, so they wrote **weekly incremental delivery for
the final three weeks into the contract itself**.

They also added a **sixth axis** — client involvement — which is the lesson in miniature. Boehm and
Turner bound their own instrument: the risk lists are *"candidates for consideration… neither
complete nor always applicable"*.

So a good assessment outputs *"be agile, and here are the two risks that creates, and what we did
about one"* — not a verdict.

## How solid is this?

- **No selection instrument here has been validated.** No study shows that projects choosing by
  Boehm and Turner, or by Cockburn, outperform those that do not. They structure an argument; they
  do not settle it.
- **Cockburn's personnel levels rest on an unvalidated skill taxonomy**, and the percentage
  thresholds Boehm and Turner attach to them are given without derivation
  {% cite cockburn_selecting_2000 %}.
- **Servasport is one company, one assessment, and no outcome was measured**
  {% cite taylor_applying_2006 %}. It shows the method being applied, not that applying it helped.
  It is peer-reviewed, which makes it the best worked example available.
- **This material is 2000–2006.** Kanban, SAFe and LeSS postdate it. Read it with
  [choosing a framework](choose.md), which carries the evidence that teams do not select methods
  cleanly in the first place.

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
