---
page_type: topic-hub
parent: People
title: Decisions
nav_order: 4
layout: default
---

# Decisions

A decision is a commitment to a course of action taken before the evidence is complete. This page covers what every decision has in common; the six pages beneath it carry the detail, from how an expert decides alone to how a group decides badly.

## 1. Three levels of decision

The level sets how much machinery a decision earns.

- **Operational** — everyday, quick, little structure. *Example:* approving a pull request.
- **Tactical** — medium-term, directing resources in support of strategy. *Example:* choosing the project's testing framework.
- **Strategic** — long-term direction, goals and values. *Example:* adopting Agile across the organization.

## 2. Analysis paralysis

The characteristic team failure is not deciding badly but not deciding at all. Buridan's ass starves between two equal bales: options too alike to separate prevent any being taken. Overweighting drawbacks does the same, since every option has some. The cost is delay, lost opportunity and wasted energy; the question underneath is never fully answerable — how much information is *enough*?

## 3. What a decision is made of

Hoover, Rosso-Llopart and Taran model a decision as inputs, process and outputs {% cite hoover_evaluating_2010 %}: in go the problem, its constraints, the assumptions, the knowledge and the experience; a technique is applied; out come the solution **and its assumed risks, written down**. A decision recording no assumed risks cannot be reviewed.

## 4. Which page to read next

| Page | What it covers | The core claim | How well evidenced |
|---|---|---|---|
| [Intuition and expertise](decisions_intuition.html) | Recognition-primed decisions | Experts recognise one action rather than compare options | Described well, transferred badly; coded by its own team |
| [Thin slicing](decisions_thinslicing.html) | Snap judgment, and where it misfires | Short exposures carry the signal — and the bias | Trade non-fiction; no primary source held |
| [Group decisions](decisions_group.html) | Styles, techniques, the seven-step method | Agree *how* you will decide before you decide | Extension leaflets: guidance, no data |
| [Groupthink](decisions_groupthink.html) | Janis's construct, and the Abilene paradox | Hierarchy, not friendliness, silences dissent | Weakest: its reviewer called it only partly confirmed |
| [Cognitive bias](decisions_bias.html) | 37 biases mapped across software engineering | The measured biases are individual, and land on estimation | Strongest: 65 primary studies, but lab-heavy |
| [Deciding with AI](decisions_ai.html) | Reliance on model recommendations | Miscalibration runs in *both* directions | Two small studies, one an unreviewed preprint |

## How solid is this?

- **Where it comes from.** The levels, analysis paralysis and the input–process–output model are lecture material {% cite root2014lectures %} — vocabulary, not research findings.
- **What we do not hold.** The "decision-driven organization" advice behind this topic is Rogers and Blenko's *Who Has the D?* and Blenko, Mankins and Rogers, *The Decision-Driven Organization*. Neither is held here, so both are named rather than cited.
- **What is contested.** CHAOS 2015 says the opposite about ambiguity: **vague objectives 38% successful against precise 22%** {% cite standish2015chaos %}. That crosstab has no size control and no significance testing, so it is no evidence that ambiguity helps either. CHAOS figures need {% cite eveleens2010chaos %} beside them — see [Why projects fail](../why.html).

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and
**David Root** {% cite root2014lectures %} on software project management. The structure,
examples, and pedagogical approach reflect their teaching materials and frameworks.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
