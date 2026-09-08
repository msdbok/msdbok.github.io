---
parent: Lifecycles
title: Spiral
nav_order: 6
layout: default
---

# Spiral

The spiral is a **risk-driven** lifecycle: each cycle identifies objectives and alternatives,
evaluates them against the risks, resolves the dominant risk — often by prototyping — and only then
commits to the next phase. Risk decides what happens next.

That is the answer to *what is its major focus?*, and it is what distinguishes the model. Barry
Boehm states it as the defining property: *"The major distinguishing feature of the spiral model is
that it creates a risk-driven approach to the software process rather than a primarily
document-driven or code-driven process"* {% cite boehm_spiral_1988 %}.

![The spiral model: four quadrants traversed repeatedly — determine objectives, identify and resolve
risks, develop and test, plan the next iteration — with cumulative cost increasing outward from the
centre](image.png)

{: .fs-2 }
Diagram after Boehm 1988 {% cite boehm_spiral_1988 %}; this rendering is reproduced from Wikimedia
Commons.

## 1. One cycle, four moves

Each loop repeats the same four steps, and the third is the one students skip:

1. **Objectives, alternatives, constraints** — what are we trying to achieve on this pass, and what
   are the candidate ways of doing it?
2. **Evaluate alternatives, identify and resolve risks** — the risk-resolution quadrant. Prototype,
   simulate, benchmark or model until the dominant uncertainty is retired.
3. **Develop and verify** the deliverable for this cycle.
4. **Plan the next phase, and commit** — or decide not to.

McConnell's shorthand is that it is *"a risk-oriented lifecycle model that breaks a software project
up into miniprojects"* {% cite mcconnell_rapid_1996 %}. The US Air Force guidebook makes the other
useful point — the spiral is *"an overlay of either incremental or evolutionary with the addition of
risk management"* {% cite stsc1996lifecycles %}, so it is not a rival to
[incremental](incremental.md) delivery but a discipline laid over it.

**Risk-driven does not mean the project is risky.** It means the risks choose the next step. That
distinction is the whole content of the model, and it is what the loops in the diagram obscure.

## 2. It subsumes the other models

A cycle in which product risk is low and budget or schedule risk is high *"becomes equivalent to"*
the waterfall; one dominated by requirements uncertainty becomes evolutionary development
{% cite boehm_spiral_1988 %}. So the spiral is less a seventh model than a rule for choosing among
the others, one cycle at a time.

{: .note }
**"Degenerates to" is not Boehm's word**, and the condition is two-sided — low user-interface and
performance risk *together with* high budget or schedule risk, not simply "low risk".

## 3. Where it does not fit

Boehm devotes a section to **Difficulties**, and it is more candid than most method papers
{% cite boehm_spiral_1988 %}:

- **Contract software.** *"The spiral model currently works well on internal software developments
  like the TRW-SPS, but it needs further work to match it to the world of contract software
  acquisition."* Deferred options and stage-by-stage commitment are hard to write into a
  fixed-deliverable contract.
- **Risk-assessment expertise.** The model is only as good as the judgement of whoever ranks the
  risks, and no procedure supplies that judgement.
- **Elaboration.** *"Some difficulties must be addressed before it can be called a mature,
  universally applicable model."*

**Example — where it was actually run.** Boehm's worked instance is TRW's Software Productivity
System: an internal environment of more than 300 tools and around 1,300,000 instructions, used by
25 or more projects, developed over a series of spiral cycles in which each pass funded the next
{% cite boehm_spiral_1988 %}.

So the "appropriate project" answer is a condition rather than a domain: **use the spiral where you
control the commitment points.** Students usually guess large government programmes; Boehm says
roughly the opposite — it works on internal development and needs further work for contract
acquisition.

Boehm later extended the model with **WinWin**, which adds an explicit stakeholder-negotiation step
at the start of each cycle to establish whose objectives the risks are being judged against.

## How solid is this?

- **One internal project, no control group.** TRW-SPS is a detailed case, not an evaluation of the
  model against alternatives.
- **The headline productivity claim needs its qualifier.** Boehm reports gains of *"at least 50%;
  indeed, most have doubled"* — measured **against cost-estimation model predictions**, not against
  a measured baseline. Never repeat the figure without that. The separate 93% reuse figure describes
  SPS itself, not the 25+ projects; keep the two apart.
- **McConnell's *Rapid Development* is a practitioner book** — a clean definition, not evidence.
- **The STSC guidebook is grey literature** — a US Air Force acquisition guide with no named author.
- **Nothing here shows risk-driven selection produces better outcomes** than any other basis for
  choosing a process. It is a coherent and influential tradition, not a measured one.

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
