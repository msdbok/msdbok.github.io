---
parent: Estimates
title: Estimation approaches
nav_order: 1
layout: default
page_type: method
---

# Estimation Approaches

An **estimation approach** is the procedure that turns what is known about a piece of software — its
requirements, its size, past projects — into a number for its size, effort, duration or cost. What
separates the families is *"the quantification step—that is, the final step that transforms the input
into the effort estimate"* {% cite jorgensen_software_2009 %}: a person, or a formula.

## 1. What is estimated

Estimates come in a chain: first **size** (lines of code, function points, story points), then
**effort** from size and history, then **schedule** from effort, each wrapped in a range that is
refined as the project moves {% cite mcconnell_rapid_1996 %}. **Cost** is effort priced at a rate.
Size is the weakest link {% cite pfleeger2005rand %}.

## 2. Six families

Miranda groups the approaches into six families {% cite miranda_managing_2014 %}:

| Family | How the number is produced | Needs |
|---|---|---|
| **Judgment** | an expert's reasoning, unaided or structured — see [expert judgment](expert), [Planning Poker](poker), [paired comparison](pair) | people who know similar work |
| **Engineering** | a cost function built from what drives the effort, such as functions × process activities {% cite pressman2010estimation %} | knowledge of the process, not history |
| **Counting** | a weighted count of external characteristics — [function points](fpa) | a requirements specification |
| **Industry norms** | a published ratio, such as Jones's schedule in months ≈ FP^0.4 {% cite jones1996rules %} | a size; no local data |
| **Analogy** | the nearest completed projects in a case base, by Euclidean distance over known features, averaged {% cite shepperd1997analogy %} | *"a minimum of 10-12 projects"* |
| **Parametric** | a cost estimating relationship fitted by regression — [COCOMO](cocomo) | a size and a calibrated model |

A norm checks an estimate rather than making one: *"Simple rules of
thumb should not be used for contracts, bids, or other serious business purposes"*, Jones writes of
his own rules {% cite jones1996rules %}. Phase splits are
norms too, and they move with size: in COCOMO II, integration and test takes 19% of effort on a small
project and 31% on a large one — figures the manual calls *"provisional"* {% cite usc2000cocomo %}.

## 3. The cost estimating relationship

A parametric model has the general form `E = A + B × (ev)^C`: effort in person-months from a size
`ev` in lines of code or function points, with A, B and C *"derived using regression analysis on data
collected from past software projects"* {% cite pressman2010estimation %}. The simplest real one is
Albrecht's `W = 54F − 13,390` work-hours from function points {% cite albrecht1983fpa %}. The constants are someone else's history, so *"Estimation models must be
calibrated for local needs!"*

## 4. Bottom-up and top-down

**Top-down** estimates the project as a whole against completed projects; **bottom-up** sums
estimates of the activities in a WBS. The field evidence gives a simple rule: *"software companies
should apply the bottom-up strategy unless the estimators have experience from, or access to, very
similar projects"* {% cite jorgensen2004topdown %}. The numbers are on [expert judgment](expert).

## 5. Combining methods when requirements are vague and history is missing

*"Practice and the literature often recommend that several estimation methods be used in concert
(when possible) to mitigate the bias, shortcomings, or risks of using a single method"*
{% cite pfleeger2005rand %}. The gain depends on independence: *"A key assumption for accuracy
improvement is that the estimates are independent"* {% cite jorgensen2014know %}. With a vague
specification and no history, analogy and calibration are out, and five moves remain:

1. **Three to five estimators from different roles, each alone first** {% cite jorgensen2004expert %},
   then a group session to surface forgotten work.
2. **Top-down and bottom-up, run independently**: top-down from a published norm, bottom-up over a WBS
   with a checklist, which stands in for the missing history.
3. **One cross-check that needs no local data**, such as an uncalibrated model or a rule of thumb.
4. **Read the spread instead of averaging it away.** Wide divergence usually means misunderstood scope
   or wrong productivity data {% cite pressman2010estimation %}.
5. **Report a range, re-estimate as requirements firm up, and start recording actuals.**

For example, twenty professionals estimated a real web publication system alone: 220 to 2,286 hours,
mean 1,088. In five mixed-role groups the mean rose to 1,548, against an actual 2,365
{% cite molokken2004group %}. *"The groups sometimes even identified necessary activities that none
of the individuals had reported."*

## 6. Estimate, target, commitment

The **estimate** is the most likely effort, the **target** what the business wants, the
**commitment** what the project promises. DeMarco and Lister separate *"the goal (that which the project aims for), the estimate (the most
likely outcome) and the schedule (what the project commits to)"*, and the first guideline follows:
*"Do not mix estimation of most likely effort with planning, budgeting or pricing."*
{% cite grimstad2006babel %}

## How solid is this?

- **Combining is practice, not a measured effect.** Only 5 of 304 estimation papers study it
  {% cite jorgensen2007review %}; RAND and Pressman are syntheses.
- **The group result is one company, one project**, and groups who did not build the system.
- **Analogy's evidence is mixed**, and its first author concedes the founding study *"is not now
  reproducible"* {% cite shepperd2025reflections %}.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
