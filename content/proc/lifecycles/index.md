---
parent: Process
title: Lifecycles
nav_order: 2
layout: default
page_type: topic-hub
---

# Lifecycles

A software lifecycle is the cradle-to-grave existence of a product — initial development, repairs
and enhancements, and eventual decommissioning. A **lifecycle model** generalises that into phases
with associated activities and artefacts, so that a team can say where it is and what comes next.

That is most of the value: a shared model lets the team discuss progress, lets management see
status, and tells a customer what happens next.

## 1. Process, lifecycle model, framework

These three words are used loosely and are examined precisely, so it is worth putting them on one
ladder from most abstract to most concrete:

- **Lifecycle model** — the phases a product passes through and the go/no-go points between them.
  Waterfall, spiral, incremental.
- **Framework** — a reusable structure of roles, events and practices that a team adopts. Scrum
  describes itself as *"a container for other techniques, methodologies, and practices"*
  {% cite schwaber2020scrumguide %}, which is exactly what a framework is and exactly what a
  lifecycle model is not.
- **Process** — what one organisation actually does, in detail: the specific steps, at the level
  [ETVX](../basics/etvx.md) describes them.

Process definitions carry more detail than lifecycle models, and a process is often defined *within*
a lifecycle model. SWEBOK's caution belongs here too: *"There is no best software process… No ideal
process, or set of processes, exists"* {% cite bourque_swebok_2014 %}.

## 2. Which model, and what it optimises

| Model | Structure | Feedback | Choose it when |
|---|---|---|---|
| [Waterfall](waterfall.md) | Linear, once through | Late | Requirements are stable and the work must be contractible and audited |
| [V-Model](vmodel.md) | Waterfall, drawn to show V&V | Late, but tests designed early | Verification must be demonstrated to a regulator or customer |
| [Incremental](incremental.md) | Usable slices, staged | Per increment | You know what to build but cannot build it all at once |
| [Iterative](iterative.md) | Whole product, repeated | Every iteration | You do not yet know exactly what to build |
| [Prototyping and RAD](prototyping.md) | Build to answer a question | Immediate | A specific uncertainty is cheaper to resolve by building than by analysis |
| [Spiral](spiral.md) | Risk-driven loops | Every cycle | Risk should decide what happens next, and you control the commitment points |

This is a map, not a menu. In practice teams combine them — incremental delivery developed
iteratively, with prototypes for the risky parts — and the spiral is best read as a rule for
choosing among the others one cycle at a time.

## How solid is this?

These models are well-established vocabulary, and that is the right claim for them. **No source in
this review compares lifecycle models on measured outcomes**, so the "choose it when" column is
reasoned from what each model does, not from evidence that it wins. Each page states its own
sourcing; the weakest are prototyping and RAD, taught here as practice with no primary study behind
them. The ladder in §1 is a convention drawn from SWEBOK, Pressman and the Scrum Guide — citable,
but a convention rather than a finding, and other authors draw the lines differently.

---

### Acknowledgments

These pages adapt material from lectures by **Eduardo Miranda** and **David Root**
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
