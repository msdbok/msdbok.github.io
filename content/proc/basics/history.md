---
parent: Basics
title: Where Process Came From
nav_order: 1
layout: default
---

# Where Process Came From

Process thinking arrived in software from manufacturing, and it arrived with assumptions attached.
Knowing which ones travelled and which ones did not explains most of the arguments in this block.

## 1. Two ideas from the factory

Adam Smith's pin factory is the first statement of the case. Making a pin, he observed, is *"divided
into about eighteen distinct operations"*, each performed by a different hand — and the output of ten
specialists dwarfs what ten generalists could produce {% cite smith1776wealth %}. The claim is that
**dividing work into defined steps raises output**.

Frederick Taylor turned that into a management programme: study the task scientifically rather than
by rule of thumb, select and train the worker for it, supervise the execution, and split the work so
that managers plan and workers execute {% cite taylor1911scientific %}. The first three of those
ideas are the ancestor of every process definition in this handbook. The fourth — planning separated
from doing — is the one that keeps causing trouble, and it is exactly what
[defining a process](define.md) rejects when it insists you ask the doers.

## 2. Deming moved quality upstream

Early quality control was terminal: design, build, test, discard the rejects. Quality was something
you inspected for at the end, and defects were a cost of doing business.

W. Edwards Deming's argument, carried into Japanese manufacturing from the 1950s, was that this is
backwards {% cite deming1986crisis %}. If defects come from the process, then analysing the process
and removing the causes prevents defects that inspection can only catch. **Analyse processes, not
just products; collect data to find the sources of defects; act before the defect occurs.** The
Plan-Do-Check-Act loop on [defining a process](define.md) is this idea in operational form.

Does that transfer to software, which is not stamped out in identical units? The SEI's answer, and
this course's, is that it does — because the *process* repeats even when the *product* does not.

## 3. Why software needed it anyway

Software has properties that make an undefined process expensive. Two competent developers solve the
same problem differently, and without an agreed process that variation reaches the product. You
cannot see a software system, so you cannot spot a defect the way you can spot a bent pin.
Requirements move underneath the work. And — the decisive one — defects propagate.

**Example — a requirements defect that survives to release.** A misunderstanding written into a
requirements statement is copied into the design, honoured by the code, and confirmed by tests
written from the same misunderstanding. Every stage does its job correctly; the error is carried, not
caught. It surfaces in production as a system that works exactly as specified and not as needed —
and by then the fix touches the specification, the design, the code and the tests
{% cite boehm_understanding_1988 %}.

That is why the work products *before* the code — estimates, requirements, architecture, test
plans — are worth reviewing: each is a place a defect can enter and then be propagated.

<img src="/images/defect-cost.svg" alt="Relative cost of correcting a defect, on a log scale: 1× at requirements rising to 40–1000× in the field. Each stage is drawn as the interval between the lowest and highest reported multiplier." style="max-width:100%; margin:1.5em 0;" />

## 4. So quality assurance is about the process too

The consequence is that QA cannot mean only testing the finished product. What limits how many
defects were injected in the first place is the process that built it — so audits, inspections,
standards such as CMMI, and formalised process definitions are quality activities in the same sense
that testing is.

## How solid is this?

- **This is intellectual history, not evidence for a method.** Smith, Taylor and Deming explain
  *where* process thinking comes from; none of them studied software, and none of the claims here
  rests on them being right about software.
- **Smith and Taylor are cited for the origin of the idea**, and both are read today as much for
  what they got wrong as for what they got right — Taylor's separation of planning from execution
  in particular.
- **The defect-propagation argument is well supported in principle and contested in its numbers.**
  That cost rises with the stage at which a defect is found is not disputed; the multipliers vary
  enormously by study and context {% cite boehm_understanding_1988 %}.
- **Read the chart as a shape, not a measurement.** The figures are the widely reproduced ones from
  Pressman's textbook {% cite pressman2005software %}, drawn from Boehm-era data. They are drawn as
  **intervals, not bars** — that is how they are reported, and on a log axis a bar's length is not
  proportional to its value. The last spans 40× to 1000×: twenty-five-fold for one stage, which
  means the studies disagree.

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
