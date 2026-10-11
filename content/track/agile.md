---
parent: Tracking
title: Velocity and flow
nav_order: 5
layout: default
page_type: method
---

# Velocity and flow

Velocity is the amount of work a team completes in a sprint, found by adding the sizes of the backlog
items finished by its end {% cite rubin2012tracking %}. Flow metrics ask a different question: how long
one item takes, and where it waits.

A partly finished item counts zero. *"Velocity measures output (the size of what was delivered),
not outcome (the value of what was delivered)"* {% cite rubin2012tracking %}, which is why it plans
well and judges badly.

## 1. Why agile teams measure at all

Agile tracking is sometimes described as avoiding prediction. A review of 30 industrial studies says
otherwise: teams used metrics for planning, progress tracking, quality, fixing process problems and
motivation, and **velocity was the most reported metric, in 15 of the 30**
{% cite kupiainen2015agilemetrics %}. *"Projects and sprints need to be planned and tracked."*
Forecasting is one of the main reasons.

What differs is who owns the number: *"In Agile mindset, estimating is applied as a way to predict how
much the team can get done to guide sprint planning—not as a target that should be achieved as closely
as possible"* {% cite kupiainen2015agilemetrics %}.

## 2. What velocity forecasts: a range of sprints

Points left divided by velocity gives the sprints remaining. Quote it as a range: *"Using a range allows us to be accurate without being overly precise."*
For example, a 200-point release at 17 to 20 points a sprint needs **10 to 12 sprints**, not 10
{% cite rubin2012tracking %}.

A velocity forecast is the average so far, projected, so re-forecast every sprint and plan from
capacity when a sprint is unusual. WMS Gaming scoped a release at **half** its velocity, leaving room
for urgent defects {% cite kupiainen2015agilemetrics %}.

Use velocity to forecast a stable team's release from a sized backlog. Do not use it to compare teams,
to judge people, or where there is no release to burn down; there, use flow (§4).

## 3. How velocity stops forecasting

Once a metric is used to evaluate a team, *"the value of the metric moves toward the desired value"*
{% cite bouwers2012measure %}. Three pressures make velocity a target:

- **A target from above.** An executive tells Rubin: *"Last year my team's velocity averaged 30 points
  per sprint. This year I'm expecting the team to achieve 35 points per sprint."* Velocity rises to a
  plateau and dips with every change of people or tools {% cite rubin2012tracking %}, so the team can
  reach 35 only by inflating its point sizes {% cite rubin_essential_2012 %}.
- **Someone watching the number.** At ThoughtWorks, managers *"excused the developers from writ[ing]
  tests, and the testers cut on the thoroughness of the testing in hopes to maintain the velocity"*
  {% cite kupiainen2015agilemetrics %}. Velocity held and quality paid.
- **A deadline.** On a newspaper-site project, the team planned about 42 points in sprint 6 and
  finished about 29: it *"succumbed to the pressure of approaching deadline and promised to deliver
  more functionality than actually possible"* {% cite mahnic2012scrum %}.

In each case the number stopped describing the team, so it stopped forecasting. The general pattern
is on [Process metrics](../proc/basics/metrics.md). Here the rule is narrow: plan from the team's own
actuals, and when velocity drops, ask what changed before asking who is slow.

## 4. Flow: lead time, cycle time and cumulative flow

**Lead time** runs from an item's request to its delivery; **cycle time** from the start of work to
done. They matter most in maintenance and support, where work arrives continuously and no release
backlog exists to burn down {% cite rubin_essential_2012 %}.

A **cumulative flow diagram** stacks one band per state over time. The top edge is all the work, the
bottom band is done, and the bands between hold unfinished work: it is a burn-up with the middle
opened up {% cite cabri2006agilereporting %}. Read across a band for how long items stay in that
state, and up through it for how many sit there. **When a middle band widens, work is waiting there,
not progressing.** Little's Law links those two readings.

The remedy is usually to start less. BBC Worldwide cut lead time by 37% and delivery variance by 47% after
starting fewer features at once {% cite middleton2012kanban %}; Timberline limited work to two
features at a time {% cite kupiainen2015agilemetrics %}. The method behind this is
[Kanban](../proc/frameworks/kanban.md).

## How solid is this?

- **Where it comes from.** Definitions from a practitioner textbook {% cite rubin2012tracking %};
  industrial practice from a review of 30 studies, 60% of them single cases and a fifth from Ericsson
  {% cite kupiainen2015agilemetrics %}. ThoughtWorks is its only strong case of velocity as a target.
- **What is contested.** Whether extrapolating velocity forecasts well. A velocity date and an
  earned-value date are the same calculation {% cite sulaiman2006agileevm %}, and extrapolating either
  *"may be misleading"* on non-linear agile work {% cite cabri2006agilereporting %}. Hence a range,
  re-forecast every sprint.
- **What we do not hold.** No study showing that cumulative flow diagrams improve delivery; the BBC
  result is one team with no control group.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite miranda_managing_2014 root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
