---
parent: Tracking
title: Choosing a tracking instrument
nav_order: 6
layout: default
page_type: method
---

# Choosing a tracking instrument

A tracking instrument is a chart or measure that turns project data into a status answer.
Earned value, burndown charts and milestone charts each answer a different reader's question, so
the choice starts from who reads the chart and what they can act on.

## 1. Same date, different money

On a Scrum project, [earned value](evm.md) can be computed from the team's own data: release budget,
planned sprints and planned points as the baseline, then points completed, points added and cost
each sprint {% cite sulaiman2006agileevm %}. Planned percent complete becomes the
[burndown](burndown.md)'s ideal line, and the schedule index SPI is the burndown's gap written as a
ratio. So earned value's release date is the same velocity-based forecast the burndown gives, and
on two projects the dates were *"indistinguishable"*. Inside a sprint, SPI falls below 1 exactly
when the burndown sits above its ideal line {% cite mahnic2012scrum %}.

What earned value adds is the cost index, CPI. A burndown holds estimated work remaining, never
effort actually spent, so it cannot show money {% cite rubin2012tracking %}.

## 2. What each instrument sees

Every instrument sees something and misleads somewhere, so read the last column as carefully as
the second.

| Instrument | What it sees | Who reads it | What it needs | Where it misleads |
|---|---|---|---|---|
| **Earned value**, release level | schedule in money (SPI); **cost** (CPI), which nothing else sees | sponsor, contract | a baseline, a budget, actual costs | the baseline is wrong or moving; late on, SPI drifts to 1.0 |
| **Release burn-up / burndown** | scope (burn-up only); a date as a velocity range | product owner, team | an estimated backlog, a few sprints of velocity | added scope flattens the burndown like slow work |
| **Sprint burndown** | work left this sprint | the team, daily | task estimates updated daily | a re-estimate looks like a slowdown to outsiders |
| **Milestone chart** | committed dates, in days | sponsor, steering committee | sharp, binary milestones | fuzzy milestones stay *"90 percent finished"* |

Each failure has a fix. Earned value needs a release-level baseline and, late on, earned schedule
{% cite lipke2003schedule %}; added scope is what the burn-up shows; the sprint chart stays with the
team; and a [milestone](../plan/milestones.md) must be an event that either happened or did not
{% cite brooks_mythical_1995 %}.

## 3. Example: the buffer the burndown missed

Project A was *"a one-half million dollar web application project"*, a Scrum team of five to seven
in one-week sprints {% cite sulaiman2006agileevm %}. Points burned at the planned rate, so the
burndown looked healthy, but they cost more than planned: *"This project had a 30% budget buffer
and the CPI index clearly shows the erosion of this buffer that the burndown doesn't recognize."*
The burndown was not wrong; it was not built to see money.

The product owners on both projects found earned value told them nothing new about the schedule,
and they had no budget responsibility. The authors draw the line themselves: *"without the need to
manage cost performance, AgileEVM does not add significant value above traditional burndown
methods."*

## 4. The deciding question: who owns the budget?

The common answer, earned value for plan-driven projects and burndown for agile ones, misses the
variable that decides. Both projects ran Scrum; **the difference was whether the reader was
accountable for the money.**

Ask three questions before adding earned value. Does anyone own a budget or a fixed price? Is
there a plan to measure against? An estimated release backlog is enough, while an up-front planned
value over moving scope is invalid from the start {% cite cabri2006agilereporting %}. Can actual
cost be collected? If nobody owns a budget, the burndown, burn-up and [velocity](agile.md) are enough.

## 5. When to use both

A project with a sponsor's budget or a contract gets **earned value at release level in the
sponsor's report**, updated each sprint, and **the burndown inside the team**, as the AgileEVM
authors recommend. Milestones add the calendar view, their estimated dates taken from the burn-up's
velocity range. Each reader gets their own chart; see [reporting](report.md). Interrupt-driven
maintenance fits none of the four and is tracked by [flow](agile.md).

## How solid is this?

- **Where it comes from.** AgileEVM is a consultants' conference paper on two of the authors' own
  projects; Mahnič adds one project measured by its coach. The shared forecast is an algebraic
  identity: it shows the instruments agree, not that either is accurate.
- **What is contested.** Cabri and Griffiths reject an up-front planned value on agile work, but not
  relating finished work to cost, so the dispute is about the baseline, not the concept.
- **What we do not hold.** No field study compares milestones, earned value and burndown head to
  head. The milestone row rests on Brooks's prescriptions, and no source tests whether choosing by
  budget ownership improves outcomes.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite miranda_managing_2014 root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
