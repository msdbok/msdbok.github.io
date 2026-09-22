---
parent: Risks
title: Analysis and prioritisation
nav_order: 3
layout: default
---

# Risk Analysis and Prioritisation

**Risk exposure** is probability times loss: `RE = P(UO) × L(UO)`, *"where RE is the risk exposure,
P(UO) is the probability of an unsatisfactory outcome and L(UO) is the loss to the parties affected
if the outcome is unsatisfactory"* {% cite boehm1991risk %}. Pressman writes it `RE = P × C`, where
**C is the cost to the project** — a monetary quantity, which is what makes exposures summable and
comparable to a budget {% cite pressman2010risk %}.

Analysis exists to answer one question: **which few risks do you act on?**

## 1. What the number is actually for

For example, a satellite experiment has $20 million at stake and a team inexperienced in software
development. Three options {% cite boehm1991risk %}:

| Option | Probability of an unsatisfactory outcome | Exposure |
|---|---|---|
| Do nothing | 0.4 | **$8M** |
| Help the team adopt better methods, at no extra cost | 0.1 | **$2M** |
| Buy independent verification and validation for **$500,000** | 0.04 | **$1.3M** *including the $500,000* |

Paying half a million is the **cheapest** option, because the comparison is not cost — it is cost
**plus residual exposure**. That is what exposure is for: **comparing options, not measuring the
world.**

It also answers the objection students raise immediately — *"you made those probabilities up."*
Re-run the comparison at its break-even points: the recommendation flips if the loss falls below
$13M, if the team reaches 0.065 on its own, or if the review costs more than $1.2M. The question is
not *are the numbers right* but **how far wrong would they have to be to change the decision.**

## 2. Bands need thresholds

A scale without defined bands is a vocabulary, not an instrument. The course teaches probability
high above 70% and impact high at a schedule slip over 20% {% cite root2014lectures %}; the
government version ties severity to numbers — **catastrophic is over 6 months' slip, over 10% cost,
over 10% functionality**, with critical, serious, minor and negligible below
{% cite us_department_of_energy_software_2000 %}.

The SEI's evaluation method bands impact against budget instead: roughly **more than 50%**, **about
30%**, **about 10%** {% cite williams1999sre %}. Use whichever you like, but write the numbers down —
an undefined band is a word two people will use differently.

Note one detail in that government table: **Medium and High prescribe exactly the same action**. A
five-level scale that acts on three levels is worth knowing about before you spend an hour arguing
which one something is.

## 3. The vital few

Prioritising means *"partitioning risks or groups of risks based on the **Pareto 'vital few' sense**
[Juran 89]"* — separating the vital few from the useful many {% cite dorofee1996crm %}. In software
terms: *"80 percent of the overall project risk… can be accounted for by only 20 percent of the
identified risks"* {% cite pressman2010risk %}.

The consequence is the part students resist: **some identified risks never enter the mitigation plan
at all.** Identification is cheap and capacity is not, so selection is the skill.

The mechanic is small — compute exposure, sort, draw a cutoff line, act above it. Two asymmetries
around that line matter. A **catastrophic but very improbable** risk should not absorb significant
management time, while both high-impact/moderate-probability and low-impact/high-probability items
carry forward. And cost-benefit the response: *"if RE for a specific risk is less than the cost of
risk mitigation, don't try to mitigate the risk but continue to monitor it."*

McConnell adds three cases where the sorted list is only **roughly** ordered
{% cite mcconnell_rapid_1996 %}: a catastrophic low-probability risk outranks its position if the
loss would end the project; synergistic risks compound beyond the sum of their rows; and *"because
the input is subjective, the prioritization is subjective too."*

## 4. What the scoring scheme hides

{: .warning }
**Multiplying two ordinal scores is not exposure.** A red-amber-green matrix is a communication
device, and NASA says so about its own: *"the risk matrix is not an assessment tool, but can
facilitate risk discussions"* {% cite nasa_nasa_2007 %}. A typical matrix compares **fewer than 10%**
of hazard pairs correctly and unambiguously, and where frequency and severity are negatively
correlated — the software case — it can be *"worse than useless"* {% cite cox2008matrices %}.

The repair is not to abandon scoring but to **rank by expected loss, carry the range, and keep the
matrix for the conversation**. Why the ranking goes wrong is on
[why we misjudge risk](biases).

## How solid is this?

- **Where it comes from.** A tutorial article whose worked case is a constructed scenario, a
  textbook, two government guidance documents and a method description. None reports a study.
- **What is contested.** The 80/20 split is a heuristic relayed from Juran, not a measured property
  of software risk; Pressman states it as *"experience indicates"*.
- **What we do not hold.** No source here validates any scale's thresholds — the government bands
  are sourced, not tested.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
