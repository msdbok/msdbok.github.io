---
parent: Basics
title: GQM
nav_order: 4
layout: default
---

# Goal Question Metric (GQM)

GQM is a method for deciding what to measure. You state a goal, derive the questions that would tell
you whether the goal is met, and only then choose metrics that answer those questions — so that
every number on the dashboard traces back to something someone wanted to know.

It was developed by Victor Basili, Gianluigi Caldiera and Dieter Rombach out of defect-evaluation
work at NASA Goddard, and it is the measurement step inside their wider Quality Improvement Paradigm
{% cite basili1994gqm %}.

## 1. The point is the direction of derivation

Most measurement fails in the opposite direction: a team collects what the tooling happens to emit,
then looks for a story in it. GQM insists the goal comes first and the metric last, which means a
metric with no question above it has no reason to exist and should be dropped.

The three levels are deliberately different in kind {% cite basili1994gqm %}:

- **Goal** — conceptual. What are we trying to achieve, and for whom?
- **Question** — operational. What would we have to know to tell whether we are achieving it?
- **Metric** — quantitative. What data answers that question?

A goal in GQM is not a slogan. It is stated for an **object**, for a **purpose**, with respect to a
**quality model**, from a **viewpoint**, in an **environment** — for instance: *improve* (purpose)
*the timeliness* (quality model) *of change-request processing* (object) *from the project manager's
viewpoint* (viewpoint) *in our maintenance team* (environment).

## 2. Name the object of measurement before choosing the number

Basili and colleagues divide objects of measurement into **products** (specifications, designs,
programs, test suites), **processes** (specifying, designing, testing) and **resources** (personnel,
hardware, office space) {% cite basili1994gqm %}.

This is the most useful ten seconds of the method. A team whose goal concerns a *process* will often
propose metrics about the *code*, and naming the object exposes the mismatch immediately.

**Example — a goal that produces its own metrics.** Take the goal *improve the defect-catching
effectiveness of code review, from the team's viewpoint*. The object is a **process**, so the
questions are about that process, not about the codebase: what proportion of defects are found at
review rather than in test? How long does a review take, and does that correlate with what it finds?
Metrics follow directly — defects found per review, review duration, and the share of released
defects that had passed through a review untouched. Note what this excludes: total lines of code and
total open bugs are both easy to collect and answer neither question.

Metrics may be **objective or subjective**, and GQM treats the frame for interpreting them as part of
the model rather than an afterthought {% cite basili1994gqm %} — which matters when the thing you
care about is not countable at all (see [the scoreboard](scoreboard.md)).

## 3. Where it falls down

The founding paper states no limitations, so the honest ones come from elsewhere — including from
Basili himself. Writing sixteen years later on why measurement programmes fail, he and his
co-authors describe *"disillusionment about metrics on the part of developers and managers"* ending
in *"the eventual failure of the measurement program"* {% cite basili2010gqmstrategies %}.

The precondition GQM assumes and rarely gets is a **shared** goal. A goal can be stated, written down
and still not be held in common, and every question derived from it then inherits the disagreement.
And GQM says nothing about who sees the resulting numbers — which is the failure mode that does the
real damage, covered under [process metrics](metrics.md).

## How solid is this?

- **GQM is well established.** It came out of a decade of empirical work at the NASA Goddard Software
  Engineering Laboratory, its authors are among the founders of empirical software engineering, and
  it has been applied across industry and standards practice for thirty years. Treat it as settled
  method, not as a proposal.
- **The founding text is a method description, not an evaluation.** The 1994 entry runs to roughly
  3,000 words, sets out the method, and — verified by search — states **no limitation of any kind**. That is normal for the genre, and it is why the drawbacks
  above are cited to later work rather than to it. Looking past a method's founding paper for its
  weaknesses is the general habit worth copying.
- **The drawbacks come from the same author.** The 2010 paper introduces a successor
  method, GQM+Strategies, and its account of measurement programmes ending in disillusionment is a
  first-hand observation from the people who built the original.
- **Attribution.** GQM is Basili, Caldiera & Rombach 1994. It is sometimes credited to Park, Goethert
  & Florac's SEI work on goal-driven measurement (1996), which is a real but **separate** publication.

---

### Acknowledgments

This page adapts material from lectures by **Eduardo Miranda** and **David Root**
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
