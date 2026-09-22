---
parent: Expectations
title: Threshold of success
nav_order: 3
layout: default
---

# Threshold of Success

The **threshold of success** (ToS) is the set of criteria, agreed and written down in advance, that
decide whether a project succeeded — stated in terms of **product, process and people**
{% cite hoover_evaluating_2010 %}. It is written before the work starts, and it is what every later
argument about "was this a success?" is settled against.

## 1. Write the failure statements first, then invert them

Goal statements resist precision; failure statements do not. The practical route to a threshold is
therefore backwards:

1. **Gather the stakeholders** who will be affected — customer, users, sponsor, team.
2. **Write what failure looks like**, plainly: *"the migration ran past the December close"*,
   *"support tickets doubled in the first month"*.
3. **Invert each statement** into a positive criterion: *"cutover complete before 1 December"*,
   *"support volume within 20% of the pre-migration baseline after 30 days"*.
4. **Check each one is SMART** — specific, measurable, assignable, realistic, time-bound. The
   criteria are Doran's, from 1981, relayed by Wysocki {% cite wysocki2003needs %}; note that the
   **A is *assignable***, naming who is responsible, not "achievable".

## 2. The test that makes a criterion a criterion

Wysocki states the standard in one sentence {% cite wysocki2003needs %}: *"An ideal statement will
have only two results — the criteria were met or the criteria were not met. There can be no
in-between answer here."*

Applied to a real threshold, the test is quick. For example, *"the reporting module will be easy to
use"* fails — two honest people reading the same evidence could disagree. *"A new branch
administrator completes the month-end reconciliation report unaided, in under 15 minutes, on first
attempt"* passes, because it can only come out one way.

Wysocki adds a constraint that is more useful than it looks: a business success criterion reduces to
**increased revenue, reduced cost or improved service**. A criterion that reduces to none of the
three — *"we delivered 47 stories"* — is measuring the project, not its purpose. *Improved service*
usually needs a proxy measure, agreed with the sponsor before the project rather than at the review.

## 3. Agreeing it: a conversation with a stopping rule

The threshold lives inside a protocol Wysocki calls **Conditions of Satisfaction**: a **request**,
the provider's **clarification** of what they heard, a **response**, then the requestor's
**agreement** restating what they will get — repeated until neither side corrects the other. The
stopping rule is the point. Its deliverable is a one-page **Project Overview Statement** carrying
the problem, one goal in the language of the business, objectives, success criteria and assumptions.

The agreement is not an artefact you file. It is re-run at every milestone, and on a change of
sponsor or project manager — exactly when a project silently changes what success means without
anyone noticing.

## 4. Why risk management starts here

The threshold is also the instrument that makes risk identification finite
{% cite hoover_evaluating_2010 %}: *"The ToS serves as a catalyst in identifying risks that, if they
were to materialize, might prevent the project from being successful."*

Without it, every conceivable bad event is a candidate and the register grows until nobody reads it.
With it, a **risk is exactly a concern that would breach the threshold**, and everything else is an
event that might happen and would not matter. Wysocki supplies the other bound: an event you are
certain of is not a risk but a certainty. See [risk identification](../risks/identification).

## 5. Limitations and challenges

- **Agreement is hard.** Stakeholders bring differing priorities and hidden assumptions, and
  thresholds are where those surface — the point of the exercise, but it costs time.
- **Thresholds conflict.** High quality, low cost, fast delivery and broad scope cannot all be
  maximised; see [expectation space](quadrant).
- **Both extremes destroy credibility.** Set them too low and they are meaningless; too high and
  they are unachievable.
- **Real change forces renegotiation.** A threshold defended past the point where it made sense is
  the same failure as having none.
- **It assumes there is a goal to agree on.** Wysocki is explicit that the method *"loses its value
  as the goal becomes more and more elusive"* — on genuinely exploratory work, expect to re-run it
  rather than to get it right once.

## How solid is this?

- **Where it comes from.** Hoover, Rosso-Llopart and Taran is a software textbook built on case
  studies; Wysocki is a practitioner handbook. Both establish method, neither measures whether
  defining a threshold improves outcomes.
- **What is contested.** Nothing in the method — but the Conditions of Satisfaction dialogue is
  worked through a manufacturing scenario in the source, so the software reading above is ours.
- **What we do not hold.** Wysocki's project-failure statistics are asserted with no source, and the
  same ten-item list appears in his book once as success factors and once as failure factors. None
  of it is used here.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda, David Root and Gil Taran
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
