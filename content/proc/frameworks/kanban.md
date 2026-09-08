---
parent: Frameworks
title: Kanban
nav_order: 6
layout: default
---

# Kanban

Kanban is a pull system with **explicit limits on work in progress**, laid over whatever process a
team already runs. It prescribes no roles and no ceremonies: work is visualised on a board, each
stage is given a cap, and nothing new is pulled into a stage until something leaves it.

The name is the Japanese 看板, *billboard*. The board is what people notice — but the board is not
the method. **The limit is the method.** A team that visualises its work and admits it without a cap
has a nicer wall and the same queue.

## 1. Cap the queue and the bottleneck shows itself

The mechanism is queueing, not effort. Consider a pipeline that accepts **10 requirements a week**,
develops **10 a week**, and tests **5 a week**. Nobody is idle or underperforming, yet work
accumulates in front of testing indefinitely — and adding developers makes it worse.

Cap the testing queue and development cannot pull new work once the cap is reached. Developers stop
starting things, and the constraint becomes visible to everyone rather than surfacing later as a
missed date.

A WIP limit is an **entry criterion on a stage**, which is exactly what
[ETVX](../basics/etvx.md) formalises {% cite radice_programming_1985 %} — the board just makes it
impossible to ignore. Limits come from the bottlenecks a team observes, not from a template
{% cite middleton2012kanban %}.

## 2. Start less, finish sooner

**Example — the BBC Worldwide Digi-Hub team.** Nine people in London adopted lean and Kanban and
were measured over twelve months {% cite middleton2012kanban %}:

| | Before | After |
|---|---|---|
| Features **started** | 84 | **64** (−24%) |
| Lead time | — | **−37%** |
| Lead-time variability | 70.7 days | 37.3 days |
| Customer-reported defects | 2.9/week | 2.2/week |

The first row explains the others. The team **started 24% fewer things** and cut them smaller — the
share classified as small rose from 52% to 75% — and lead time and predictability followed.

Read that carefully: the gain is **flow and predictability, not volume**. A manager who reads −37%
lead time as "more work done" has it backwards, and managers are usually rewarded for starting
things, which is what makes this worth teaching.

{: .note }
**Do not say throughput rose because WIP fell.** The paper states that output value *"cannot be
measured exactly"* and reports that the team *believed* more value was delivered. What was measured
is that **cycle time fell as WIP fell**.

## 3. Where it fits, and how it differs from Scrum

The graded question is what kind of project suits Kanban, and the cited answer is maintenance and
support. Ken Rubin puts the sweet spots for Kanban in *"the software maintenance and support areas"*,
and gives the reason from the other side: *"Scrum is not well suited to highly interrupt-driven
work… In interrupt-driven environments you would be better off considering an alternative agile
approach called Kanban"* {% cite rubin_essential_2012 %}. One organisation can reasonably run both —
[Scrum](scrum.md) for new-product development, Kanban for support.

Carry the hedge with it: Rubin notes in the next breath that some practitioners argue Kanban's focus
on eliminating overburden makes it appropriate in complex domains too.

The difference fits in one sentence: **both cap work in flight, but they cap different things.**
Scrum caps *time* — the sprint — and lets scope settle inside it; Kanban caps *queue depth* and lets
time settle. Timeboxing is itself a WIP limit {% cite rubin_essential_2012 %}, which makes them
complements rather than rivals. On adaptation they diverge sharply: Kanban starts from the existing
process, where the Scrum Guide calls its framework immutable {% cite schwaber2020scrumguide %}.

**Under AI agents.** If code generation accelerates while review does not, work accumulates at
**review** — so the WIP limit that binds moves downstream. This is the BBC result run backwards, and
it is the same law; see [agentic](agentic.md).

## How solid is this?

- **The evidence is one team, one company, twelve months, no control group.** The authors say the
  hypothesis was *"supported by this single case study"* {% cite middleton2012kanban %}. **Nothing
  here shows Kanban beats Scrum.**
- **It is confounded**, and that is our reading rather than theirs. In the same period the team also
  rewrote legacy code and reduced turnover — equally good candidate causes of the defect drop, which
  the authors hedge as *"possibly due to the improving structure of the code base"*.
- **One figure is reported two ways** — the abstract says consistency rose 47%, the body says
  lead-time variability fell 47%, from 70.7 to 37.3 days. Use the body's absolute numbers.
- **The release-frequency figure often quoted** from this paper (2/month to 16/month) compares two
  single months about two years apart, outside the study window. Leave it alone.
- **Rubin is a practitioner book by a Scrum trainer** {% cite rubin_essential_2012 %}; his Kanban
  material is definitional, not evidential.

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
