---
parent: Requirements
title: Requirements engineering
nav_order: 4
layout: default
---

# Requirements Engineering

Requirements engineering is *"the process of discovering that purpose, by identifying stakeholders
and their needs, and documenting these in a form that is amenable to analysis, communication, and
subsequent implementation"* {% cite nuseibeh2000roadmap %} — where *that purpose* is what the system
is intended for, because *"the primary measure of success of a software system is the degree to
which it meets the purpose for which it was intended."*

## 1. Five activities, and they are not a pipeline

The activities are **eliciting**, **modelling and analysing**, **communicating**, **agreeing** and
**evolving**. The authors name them in order and then immediately say the order is not real: *"while
these activities are described independently and in a particular order, in practice, they are
actually interleaved, iterative, and may span the entire software systems development life cycle."*

Three words this list depends on are commonly used interchangeably, and separating them makes the
rest easier. A **process** is an instance of a process model; a **technique** *"prescribes how to
perform one particular activity"*; a **method** *"provides a prescription for how to perform a
collection of activities"* by integrating a related set of techniques.

Nothing here is specific to a lifecycle. SWEBOK puts the point sharply
{% cite swebok2024v4 %}: *"downstream maintainers should not be able to discern the life cycle used
in earlier development from the form of those requirements alone."* Agile does not remove
requirements work; it redistributes it.

## 2. Validation asks the stakeholders. Verification asks the build

The two words are routinely swapped, and the distinction is not cosmetic — the two questions need
**different techniques** {% cite nuseibeh2000roadmap %}.

- **Validation** asks whether these are the **right** requirements: *"the process of establishing
  that the requirements and models elicited provide an accurate account of stakeholder
  requirements."* It is a question about stakeholders, answered before and during the build.
- **Verification** asks whether the delivered system **meets** them. It is a question about the
  build, answered on delivery.

The technique families follow from that, and a review meeting that has not decided which of the two
it is doing will accomplish neither:

| Question | What it checks | How |
|---|---|---|
| **Coherence of the description** | Are the requirements consistent and structurally complete? | Inspection, formal analysis, automated consistency checking |
| **Correspondence with the real world** | Have all the aspects stakeholders regard as important been covered? | Prototyping, specification animation, scenarios |

The sharpest instruction in the paper is about stance: *"validation should adopt the same stance
that software testers take: it should devise experiments to attempt to refute the current statement
of requirements."* Not walk through the document and confirm it — which is what a requirements
review usually looks like in practice. **A validation activity that cannot fail has not validated
anything.**

One edge case is worth knowing because it is miscalled every time it appears: where a requirement
disagrees with a **higher-level** document — a contract, a system specification, a regulation — that
is not an inconsistency, it is an **incorrectness** {% cite iso2018req %}.

## 3. Quantification is where it gets hard

Raw requirements arrive qualitative. For example, *"the system shall be modifiable"* has no context
and no measure; it becomes checkable only as something like *"a mid-grade engineer shall be able to
modify the logic of module X within one engineering week."* A specification should say **how big, how much,
how fast, how often** — and the useful discipline is to start writing the test cases in parallel
with the requirements, because a test case that cannot be written is a requirement that is not
finished.

Where no such method exists, the standard's rule is to stop pretending: if no process can determine
whether the software meets a requirement, **remove or revise it** {% cite iso2018req %}.

## 4. What this does not achieve

The field's own conclusion is that completeness is not available. Nuseibeh and Easterbrook report as
settled that *"the attempt to build consistent and complete requirements models is futile"*, and
that RE instead has to *"analyse and resolve conflicting requirements, to support stakeholder
negotiation, and to reason with models that contain inconsistencies."*

So the practical goal is not a perfect document. It is to **manage the inconsistency** — record it,
identify its cause, and decide what action it implies. Which is also why
[change control](more) is a requirements activity rather than an admission of failure.

## How solid is this?

- **Where it comes from.** A roadmap paper written to frame a research field, and a normative body
  of knowledge. Neither reports a study; both establish definition and method.
- **What is contested.** The claim that front-loading requirements pays is well accepted but is
  **not measured here** — the roadmap cites others for it rather than offering a figure of its own,
  which is the right level of confidence to carry.
- **What we do not hold.** No evidence in these sources that any particular validation technique
  outperforms another.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
