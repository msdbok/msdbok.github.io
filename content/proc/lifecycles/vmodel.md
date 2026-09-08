---
parent: Lifecycles
title: V-Model
nav_order: 2
layout: default
---

# V-Model

The V-model is [waterfall](waterfall.md) redrawn so that each development stage is paired with the
test stage that will check it. Requirements pair with acceptance testing, system design with system
testing, module design with unit testing. Bent into a V, the sequence shows *where verification and
validation attach* rather than merely what happens next.

<img src="/images/vmodel.svg" alt="The V-model: requirements, system design, architectural design and module design descend the left arm to implementation at the vertex, then unit, integration, system and acceptance testing ascend the right arm. Dashed lines join each design level to the test level that checks it — acceptance testing validates the requirements, the three lower pairs verify their design documents." style="max-width:100%; margin:1.5em 0;" />

## 1. It is not a different lifecycle

This is the point most worth making, and Pressman makes it: there is *"no fundamental difference"*
between the classic life cycle and the V-model — the V *"provides a way of visualizing how
verification and validation actions are applied to earlier engineering work"*
{% cite pressman2010incremental %}. Same phases, same order, same commitment structure. What changes
is what the picture makes you notice.

So everything true of waterfall is true here: the exit criteria make it contractible and auditable,
and they delay the first execution of real code to the same late point.

## 2. What the redrawing actually buys

Two things, and they are worth having.

**Test design moves early.** If acceptance tests are drawn against the requirements, they get written
when the requirements are written — and a requirement that cannot be turned into an acceptance test
is discovered at that moment rather than a year later. The dotted lines are a design obligation, not
just an illustration.

**Traceability becomes explicit.** Each test level has a named counterpart it is testing *against*.
For work that has to demonstrate coverage to a regulator or a customer, that mapping is the artefact
being demanded.

**Example — a medical infusion pump.** The submission has to show that every requirement is verified
by something. Structuring the project as a V means the acceptance protocol is drafted alongside the
requirements specification, the system-test plan alongside the architecture, and the unit-test plan
alongside module design. When the auditor asks which test covers requirement 4.2.7, the answer is a
line on a diagram rather than an archaeology exercise. Nothing about the V makes the software better;
it makes the *evidence* about the software producible.

## 3. When to use it, and when not

Use it where verification effort is large, mandated and has to be shown — safety- and
mission-critical software, regulated devices, avionics, automotive. Avoid it for the same reason you
avoid waterfall: it assumes the requirements are known and stable, and it inherits waterfall's late
feedback in full. A V-model project with volatile requirements re-plans both arms of the V every time
the requirements move, which is twice the churn for no extra information.

## How solid is this?

- **The definitional claim is Pressman's** {% cite pressman2010incremental %}, who credits the V-model
  formulation he reproduces to Bucanac (1999). The model's own origins are usually given as German
  and defence-standards practice in the 1980s.
- **This page cites no study of the V-model**, because this review found none worth the name. It is
  taught as a widely used convention for organising verification, which is what it is.
- **Falcão and colleagues (2024) is not evidence for the V-model as a lifecycle**, despite its title. It
  is about using the V's *shape* to structure applied doctoral research, and this review had it
  misfiled until it was read. It is cited here only as an instance of the shape being reused, not for
  any claim about software projects — an example of why you check that a source contains what you are
  citing it *for* {% cite falcao_experiences_2024 %}.
- **The traceability benefit is a property of the practice, not a measured outcome.** No source here
  shows V-model projects find more defects than the same phases drawn as a line.

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
