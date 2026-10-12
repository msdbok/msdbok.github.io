---
parent: Scope
title: Estimates
nav_order: 2
layout: default
page_type: topic-hub
---

# Estimates

An **estimate** turns scope into resources and time: how big the software is, how much effort it
takes, how long it runs and what it costs. Estimates are wrong by an amount known well enough to plan
for. Across ten industrial surveys, *"most projects (60-80%) are completed over budget and/or
schedule"*, and the likely average overrun is *"between 30 and 40%"* {% cite molokken2003surveys %}.

That is why no method is trusted alone. The pages below each describe one method;
[Estimation approaches](approaches) lays out the six families, the cost estimating relationship
behind every model, and how to combine methods when requirements are vague and there is no history.

## Which page to open

| Page | Good for | Best fit | Main cost |
|---|---|---|---|
| [Estimation approaches](approaches) | choosing and combining methods | vague requirements, no history | none: it is the map |
| [Expert judgment](expert) | knowledge no model can take in | early or unusual work | anchoring and over-optimism |
| [Planning Poker](poker) | fast team sizing of a backlog | release planning of familiar stories | the first-round cards fence the result |
| [Paired comparison](pair) | consistent relative sizes, with a check | early sizing; items unlike the rest | many comparisons, and a reference of known size |
| [Function point analysis](fpa) | a defensible size from requirements | a written specification | counting effort and trained counters |
| [FPA explained](fpa_explained) | the counting rules, worked through | learning to count | time to learn the rules |
| [COCOMO](cocomo) | effort and schedule from size and cost drivers | a size, and past projects to calibrate on | calibration data |
| [COCOMO II drivers](cocomo_ii_drivers) | the rating values for scale factors and effort multipliers | applying COCOMO II | rating each driver honestly |

The table has no accuracy column on purpose. Across 15 studies comparing experts with models, five
favoured experts, five found no difference and five favoured models {% cite jorgensen2004expert %}.
What decides is calibration: Basic COCOMO landed within a factor of 1.3 of actuals 29% of the time,
and the version with 15 cost drivers 78% {% cite jorgensen_software_2009 %}.

## How solid is this?

- **The 30–40% is an order of magnitude**, from surveys with no random samples, mostly of managers
  reporting on their own projects.
- **The 29% and 78% are Boehm's own figures**, quoted in a debate he was arguing, from 63 projects.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
