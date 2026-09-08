---
parent: Frameworks
title: ACDM
nav_order: 2
layout: default
---

# Architecture Centric Design Method

ACDM puts the software architecture, rather than the process, at the centre of a project. The
architecture is designed early, evaluated against the risks it carries, and refined until the team
believes the system can be built — and it is then what the plan, the schedule and the tracking are
all derived from. Anthony Lattanze developed it at Carnegie Mellon {% cite lattanze2009architecting %}.

## 1. Which lifecycle does it fit under?

None, and the book answers that in its own words: ACDM *"is not a development process, but rather a
design process that is intended to complement organizational development processes"*, whose goal is
*"a design process framework that can easily be used with an organization's existing development and
life cycle processes"* {% cite lattanze2009architecting %}. So it is a **framework** on
[the ladder](../lifecycles/) — reusable structure, with no phases of its own — and it sits inside
whichever lifecycle you are running.

What ACDM's own stages describe is iterative and risk-driven, which is
[the spiral](../lifecycles/spiral.md)'s logic pointed at the architecture rather than at the whole
project.

## 2. Eight stages, one gate, and a loop

<img src="/images/acdm.svg" alt="ACDM's eight stages: discover architectural drivers, establish project scope, create or refine the architecture, review it, then a stage-5 Go/No-Go. No-Go runs experiments in stage 6 and returns to stage 3; Go proceeds to production planning and production. Stages 1 to 6 are the period of uncertainty, stages 7 and 8 the period of certainty." style="max-width:100%; margin:1.5em 0;" />

Stage 5 is a decision, not an activity. On No-Go the team runs experiments in stage 6 — *"the
purpose of the experiments is to address specific issues that arose during the evaluation; thus, the
architecture guides the team in discovering and mitigating risk"* — and then returns to stage 3.
*"The team will iterate in stages 3 to 6 until the architecture is deemed fit for production"*
{% cite lattanze2009architecting %}.

The tenet that makes this work is speed over polish: *"not dwell on the initial architecture design,
but rather create the initial architecture quickly, review it to uncover technical issues, and
refine it."*

## 3. Uncertainty first, then a plan worth believing

Stages 1–2 and the 3–6 loop are the **period of uncertainty**, where precise production estimates
are not possible. Once the architecture is baselined the team enters the **period of certainty**,
and *"higher fidelity estimates and project plans can be created"* {% cite lattanze2009architecting %}.
That is the method's real claim — not that it produces better architectures, but that it tells you
**when your estimates are worth anything**.

**Example — estimating and tracking by architectural element.** Each element gets a named owner. The
team estimates every element, then re-estimates the ones that disagree until each sits inside an
agreed tolerance — *"a tolerance of 20% from the mean is reasonable value for most systems in most
domains, but experience is the best guide"*. Those estimates become the work breakdown and the
schedule, and progress is tracked with earned value per element: in a project rolling up to 1,000
hours, a 15-hour task earns 1.5, credited only when it is finished. The failure this is meant to
prevent is *"the situation where the last 10% of the project takes 150% of the schedule and
budget"* {% cite lattanze_acdm %}.

## How solid is this?

- **There are two versions and they differ.** The 2009 book prescribes **eight** stages and calls
  the method the Architecture Centric **Design** Method. The earlier CMU report
  (CMU-ISRI-05-103, 2005) prescribes **seven** and says **Development**, with experimentation
  branching off the gate rather than sitting in the loop {% cite lattanze_acdm %}. A source counting
  eight stages is not miscounting — it is reading the book. **Cite the version you read.**
- **Both are method proposals, not evaluations.** Neither carries a trial, a comparison or outcome
  data. The book says ACDM *"emerged from small teams of four to six team members and projects of one
  to two years in duration"* and that *"as ACDM was tested in industry use, the method has evolved to
  accommodate larger teams"* — evolution asserted, with no project counts and no measures.
- **Its numbers are heuristics, and it says so.** The 20% tolerance defers to *"experience is the
  best guide"*, and the report's ceiling of three refinement iterations is a warning sign rather
  than a threshold.
- **Watch the citation.** The MSD reading list gives ACDM as *"ICSOFT 2009"*. The **year is right for
  the book** — © 2009, Auerbach, though the publisher's own deposit dates it 18 November 2008 — but
  no ICSOFT paper matches it: neither DBLP's ICSOFT proceedings nor OpenAlex lists one.

---

### Acknowledgments

ACDM reaches this course through the MSD reading assignments compiled by **Eduardo Miranda** and
**David Root** {% cite root2014lectures %}. The content of this page is drawn from Lattanze's book
and report, not from their lecture material.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
