---
parent: Decisions
title: The PEAK Model
nav_order: 1
layout: default
---

# The PEAK Model

PEAK is a way of laying out what went into a decision and what came out of it, so the decision can
be examined later. Four inputs — **P**roblem, **E**xperience, **A**ssumptions, **K**nowledge —
feed a decision process, which produces two outputs {% cite hoover_evaluating_2010 %}.

## 1. The four inputs

| | The input | The question it makes you ask |
|---|---|---|
| **P** | Problem | What must be resolved? What are the requirements and the constraints? |
| **E** | Experience | Have you seen or solved something like this before? How relevant is that history? |
| **A** | Assumptions | What are you taking as fact without evidence — and what have you set aside as irrelevant? |
| **K** | Knowledge | What facts do you actually have, and what is the environment around the problem? |

The **A** is the one that repays attention. It asks two things, not one: what you are assuming *to
be true*, and what you have decided *not to look at*. The second is where decisions quietly go
wrong, because nobody writes down what they excluded.

## 2. Two outputs, not one

Out come the **solution** — and the **assumed risk**, which is what may not work as envisioned.

Teams reliably produce the first and skip the second. That is what makes a decision impossible to
review: with no assumed risk on record, the only thing left to judge it by is how it happened to
turn out. A release that shipped fine with no rollback plan was a bad decision that got lucky, and
nothing in the record will say so.

**Example.** A team picks a managed queue over running their own. *Problem:* delivery spikes are
dropping messages. *Experience:* two people have operated the self-hosted option before.
*Assumptions:* traffic stays inside the paid tier; the vendor's region matches ours.
*Knowledge:* current throughput, the vendor's published limits. *Solution:* adopt the managed
queue. **Assumed risk:** if volume doubles, the cost model breaks and migrating back takes a
quarter — and nobody has checked what the vendor's export looks like.

Six months later that last sentence is the difference between a review and an argument.

## 3. What it does not do

The model **does not tell you what to decide.** Its authors are explicit that it "does not
indicate what a particular decision should be" — it exists so that the process can be examined.
Expect it to make a decision *reviewable*, not correct.

That is the same conclusion the [cognitive bias](decisions_bias.html) page reaches from the
research side: judge the process, not the outcome. PEAK is what makes that possible, because a
process with no recorded inputs and no assumed risk cannot be judged at all.

## 4. Using it on a case

PEAK was built for case teaching, which is what makes it practical. A case study hands you the
**problem**, states some **assumptions** and supplies many facts; you bring the **knowledge** and
the **experience**. Writing the four inputs out before arguing about the answer usually exposes
that the disagreement in the room is about an assumption, not about the solution.

## How solid is this?

- **This is a framework, not a finding.** It organises thinking; whether teams using it decide
  better is still to be verified. Treat it as a checklist for making a decision inspectable.
- **The value is in the discipline, not the diagram.** Naming assumptions and recording assumed
  risk is the work. A team can draw the boxes and still skip both.
- **It says nothing about how experts actually decide under time pressure** — for that, see
  [intuition and expertise](decisions_intuition.html), which describes a process that does not
  enumerate inputs at all.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and
**David Root** {% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
