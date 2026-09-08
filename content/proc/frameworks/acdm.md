---
parent: Frameworks
title: ACDM
nav_order: 2
layout: default
---

# Architecture Centric Development Method

ACDM is a framework that puts the software architecture, rather than the process, at the centre of a
project. The architecture is designed early, reviewed against the risks it carries, and refined until
the team believes the system can be built — and it is then the artefact the plan, the schedule and
the progress tracking are all derived from.

Anthony Lattanze set it out at Carnegie Mellon: ACDM *"places the software architecture at the center
of a development effort rather than software processes"* {% cite lattanze_acdm %}.

## 1. Which lifecycle does it fit under?

None, and that is the point — ACDM is a **framework**, so it fits *inside* whichever lifecycle you
run. One of its stated goals is to *"create, refine, and update the architecture in an iterative way
throughout the lifecycle whether the lifecycle is waterfall or iterative"* {% cite lattanze_acdm %}.
Placing it on the [ladder](../lifecycles/) is the whole answer: it supplies reusable structure —
stages, roles, a review, a decision gate — and it never names the phases a product passes through.

If a shape must be named, the one ACDM's stages describe is **iterative and risk-driven** — review,
decide, resolve, review again — which is [the spiral](../lifecycles/spiral.md)'s logic applied to the
architecture rather than to the whole project.

## 2. Seven stages and one gate

ACDM *"essentially follows seven prescribed stages"* {% cite lattanze_acdm %}, and the fifth is a
gate rather than an activity: the risks the review found are prioritised, and the team decides
whether the architecture is ready to build. Stages 6 and 7 then mean **different things depending on
the answer**.

<img src="/images/acdm.svg" alt="ACDM's seven stages. Discovering architectural drivers, establishing scope, creating a notional architecture and reviewing it lead into a stage-5 Go/No-Go gate. No-Go runs experiments to resolve the open risks and returns to the review; Go plans and executes production, then iterates back to stage 1." style="max-width:100%; margin:1.5em 0;" />

The loop between stages 4, 6 and 7 is where the method earns its keep. A review that finds a risk
does not produce a caveat in a document — it produces an **experiment**, a targeted prototype that
settles one technical question, after which the architecture is reviewed again.

## 3. The plan comes out of the architecture

The consequence worth teaching is what happens to the schedule. ACDM's preliminary plan carries no
construction schedule at all, because one made *"before any architecting"* has, in Lattanze's words,
a *"very slim indeed"* chance of resembling the real cost {% cite lattanze_acdm %}. The detailed plan
waits for stage 6, and is built from the architecture's elements.

**Example — estimating and tracking a system by its architectural elements.** Each element gets a
named owner who sees its construction through. The team estimates every element, then re-estimates
the ones that disagree until each sits inside an agreed tolerance — *"a tolerance of 20% from the
mean is reasonable value for most systems in most domains, but experience is the best guide"*. Those
estimates become the work breakdown and the schedule, and progress is then tracked with earned value
per element: in a project whose estimates roll up to 1,000 hours, a 15-hour task carries an earned
value of 1.5, credited only when it is finished. The failure Lattanze wants the arithmetic to prevent
is *"the situation where the last 10% of the project takes 150% of the schedule and budget"*
{% cite lattanze_acdm %}.

## How solid is this?

- **This is a method proposal, not an evaluation.** The report describes ACDM and argues for it, with
  no trial, no comparison against another method and no outcome data. It supports *how the method
  works*, never *that it works better*.
- **It emerged from small teams.** *"While ACDM emerged from small teams and projects (4 to 6 team
  members, 1 to 2 year projects), it is designed to scale up"* {% cite lattanze_acdm %}. *Designed
  to* is the operative phrase: larger projects are meant to run a core-architecture cycle and
  partition the work, but that is intent rather than reported practice.
- **Its numbers are heuristics, and it says so.** The 20% tolerance defers to *"experience is the best
  guide"*, and the ceiling on the refinement loop — *"more than three refinement iterations are
  probably too many"* — is a warning sign, not a threshold. A further claim that pre-architectural
  estimates deviate by up to 500% is attributed to unnamed *"some studies"*.
- **Watch the citation.** Cite the document that exists — **CMU-ISRI-05-103, February 2005**. The MSD
  reading list gives ACDM as *"ICSOFT 2009"*, which is not this report and most likely means
  Lattanze's 2009 book *Architecting Software Intensive Systems*. Secondary accounts also miscount the
  stages as eight; the primary source says seven.

---

### Acknowledgments

ACDM reaches this course through the MSD reading assignments compiled by **Eduardo Miranda** and
**David Root** {% cite root2014lectures %}. The content of this page is drawn from Lattanze's report,
not from their lecture material.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
