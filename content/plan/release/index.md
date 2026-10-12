---
parent: Planning
title: Release planning
nav_order: 10
layout: default
page_type: topic-hub
has_children: true
---

# Release planning

**Release planning** decides which features go into which release, across a sequence of releases,
under limits of effort, budget and dependencies {% cite ruhe2005release %}. A release is *"a
collection of features that the customer values"*; the plan commits firmly to the next one and
sketches the rest {% cite greer_software_2004 %}.

## 1. Release or iteration

A release is what the customer gets: *"a coherent deliverable to customers or users"*. An iteration,
or sprint, is how the team gets there: *"a short-duration, timeboxed iteration"*, and *"a release is
typically composed of multiple sprints"*. Rubin gives typical ranges of three (or fewer) to nine
months for a release and one week to one calendar month for a sprint {% cite rubin_essential_2012 %}.
An iteration must end in working software; a release must be useful. Some teams release every
timebox, as one e-store did every three weeks {% cite jalote2004timeboxing %}.

![Three release cadences: one release made of several sprints, a release at the end of every sprint, and a release of every single feature](fig-release-cadences.svg)

*Rubin 2012, Fig. 18.1.*

Both are timeboxes, so in both **the date holds and the scope moves**. Take Quill, a fictional word
processor due for its publisher's spring list. After the third sprint's demo the customer moves
*comments* above *mail merge*. The change waits for the next sprint's planning, the customer decides
on value while the team advises on cost and risk {% cite racheva2010agileprio %}, *mail merge* drops
below the release line, and the spring-list date stays put. Moving the date is the sponsor's separate
decision, never a side-effect of reprioritising.

Releasing early also changes when the money comes back. In Denne and Cleland-Huang's example, one
year of development has a net present value of −$24K as one release and +$205K as four quarterly ones
{% cite denne_incremental_2004 %}.

## 2. Approaches compared

| Approach | What it optimises | Inputs needed | Main cost |
|---|---|---|---|
| **MoSCoW** {% cite clegg_case_1994 dsdm2014moscow %} | a guaranteed minimum plus contingency | a category per feature; Musts at most 60% of effort | the Should/Could line is judgement |
| **Buffered MoSCoW** {% cite miranda_time_2011 %} | delivery certainty by a fixed date | the customer's order; a normal and a safe estimate per feature | conservative; promises stop at *"short of a calamity"* |
| **Cost–value (AHP)** {% cite karlsson1997costvalue %} | value per unit of cost | pairwise value (customers) and cost (engineers) judgements | n(n−1)/2 comparisons; ignores dependencies |
| **EVOLVE** {% cite greer_software_2004 %} | stakeholder urgency against business value, increment by increment | weighted stakeholders' ranks; effort; precedence | data collection; a person picks among several plans |
| **IFM** {% cite denne_incremental_2004 %} | the project's net present value | Minimum Marketable Features; cost and revenue per period | per-feature revenue forecasts from the business |

Buffered MoSCoW simplifies SPID, which plans the first increment at about 95% confidence and
re-plans it at 50% {% cite miranda_planning_2002 %}.

## 3. Pages

| Page | The question it answers |
|---|---|
| [Prioritising features](prioritisation) | When not everything fits, what goes in first? |
| [Buffered MoSCoW](moscow) | How many features can a fixed date honestly promise? |
| [Contracts and incentives](incentives) | Who pays when only part of the release arrives? |

## How solid is this?

- **Where it comes from.** Rubin's ranges are typical values from practice. Denne and
  Cleland-Huang's project is hypothetical.
- **What is thin.** Of 24 published release-planning models, four have reports of full-scale
  industrial use {% cite svahnberg2010release %}.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda {% cite miranda_managing_2014 %}
on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
