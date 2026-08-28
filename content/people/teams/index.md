---
parent: People
title: Teams
nav_order: 3
layout: default
---

# Teams Basics
_*Adapted from David Root (2014)_

## What is a Team?

A **team** is a cohesive group of individuals with diverse skill sets and shared objectives, working collaboratively within an organizational culture.  
Unlike a simple group, a team is united by a common goal, leveraging mutual support and compatible interactions to achieve results.

### Do teams outperform individuals?

This page used to answer **yes**, twice, under the heading *Synergy* — "teams often outperform
individuals by combining strengths" and "collective efforts produce results that exceed
individual capabilities". **No source in this bibliography supports that claim**, and the
textbook the Teams pages already rely on is more careful: teams "can outperform the best member
of the group, **but there are no guarantees** … Teams are not a panacea for organizations; they
often fail and are frequently overused or poorly designed" {% cite thompson2015makingtheteam %}
(p. 29).

The two large software-team studies below do not settle it either, because **neither ever
compares a team with an individual**. Hoegl and Gemuenden interviewed 575 people across 145
German software teams {% cite hoegl_teamwork_2001 %}; Lindsjørn and colleagues surveyed 477
members of 71 agile teams {% cite lindsjorn2016teamwork %}. Both correlate the *quality of
teamwork* with performance **within** teams. Neither measures synergy.

What does exist is an arithmetic that explains why the question has no general answer.

---

## Steiner's equation: potential minus process losses

Steiner {% cite steiner_models_1966 %} states it as

> **Actual productivity = potential productivity − losses due to faulty process** (p. 274)

and splits the losses into **motivation losses** and **coordination losses** (p. 275). Potential
productivity depends only on the task's demands and the members' resources; everything else is
lost in the process of working together. Adding people raises the potential **and** creates the
losses at the same time, so which effect wins is an empirical question about the task — not a
property of teams.

His illustration is Ringelmann's rope-pulling experiment (p. 276). Individuals pulling alone
averaged **63 kg**, so groups of 2, 3 and 8 ought to manage 126, 189 and 504 kg:

| Pullers | Potential | Actual | Shortfall |
|---|---|---|---|
| 2 | 126 kg | 118 kg | 8 kg |
| 3 | 189 kg | 160 kg | 29 kg |
| 8 | 504 kg | 248 kg | 256 kg |

At eight pullers the group delivers under half of what its members are individually capable of.
The shortfalls track the number of pairwise coordination links — 1, 3 and 28.

{: .warning }
**Check the citation chain before quoting these numbers.** Steiner never saw Ringelmann's data:
he takes it "as reported by Dashiell (1935)", a textbook chapter, and Ringelmann's own
experiment (French agricultural engineering, around 1913) was never published. Steiner adds his
own caveats on the spot — Ringelmann "observed only a few groups of each size", coordination
losses will not always be proportional to the number of links, and the task was so demanding
that optimal motivation could be assumed, whereas "few experimental tasks will warrant this
assumption". Thompson reports the same experiment with different figures — force *per person* of
63 / 53 / 31 kg at 1, 3 and 8 pullers {% cite thompson2015makingtheteam %} (p. 47). Say which
chain you are using.

Steiner's other durable contribution is the **task typology**: an **additive** task sums the
members' efforts (rope-pulling), a **disjunctive** task succeeds if the best member succeeds, and
a **conjunctive** task is limited by the weakest member. Software work is mostly conjunctive and
divisible — which is the direction Brooks's Law comes from, and the reason process losses are not
a footnote here.

Social loafing, on [Motivation](motivation.html), is the *motivation loss* half of this equation.
The two pages are not in tension once the equation is on the table.

---

## What does predict how a software team performs

Teamwork quality (TWQ) — communication, coordination, balance of member contributions, mutual
support, effort and cohesion — is measurable, and it is associated with performance. The size of
that association depends entirely on **who is asked**.

| Rater | TWQ → team performance | Variance explained |
|---|---|---|
| Team members | **β = 0.68** | R² = 0.466 |
| Team leaders | **β = 0.32** | R² = 0.104 |
| Product owners | **β = 0.06** | **p = 0.593 — no effect** |

Source: {% cite lindsjorn2016teamwork %}, 477 respondents in 71 agile teams across 26 Norwegian
companies. On project quality, product owners and team members agree at **r = 0.03** — the
authors call the agreement non-existent.

The earlier study this replicates found no such collapse. Hoegl and Gemuenden's third rater was a
traditional **line manager**, and TWQ predicted performance for all three rater groups —
explaining **41%** of member-rated, **11%** of leader-rated and **7%** of manager-rated
performance variance, all significant at the 1% level — with the raters agreeing with each other
at r ≈ 0.50 (leader↔members), 0.40 (leader↔managers) and 0.35 (managers↔members)
{% cite hoegl_teamwork_2001 %}.

{: .note }
**The role-substitution reading is a synthesis, not either paper's claim.** Put side by side, what
changed between 2001 and 2016 looks less like the correlation weakening than like the *rater
being replaced*: a line manager judging efficiency and quality was swapped for a product owner
judging delivered features and cadence, and those are different definitions of success. **Neither
paper says this.** Lindsjørn's own §5.1 offers a vantage-point explanation — product owners see
functionality, lead time and cost, while members see internal code quality, which is invisible to
the customer — and explicitly declines to choose between it and rater bias.

Both papers volunteer the same warning about their own largest number. Team members rated the
predictor and the outcome, so **common source bias** is a leading explanation for β = 0.68 and for
the 41%; Lindsjørn reports finding "no empirical distinction between the two concepts". Hoegl adds
that the **antecedents** of teamwork quality were not investigated, so neither study can tell you
how to *produce* good teamwork — only that where it is reported, performance tends to be reported
with it. Both are cross-sectional surveys; neither licenses a causal claim.

**What to take from it:** before trying to improve a team's performance, settle **whose** view of
performance is being optimised. That question returns in [Tracking](../../track/).

---

## Characteristics of a Successful Team

- **Common Goal:** Unified objective guiding the team's efforts toward collective success.
- **Interdependence:** Members rely on each other's skills, emphasizing collaboration.
- **Open Communication:** Transparent, frequent dialogue fosters trust and resolves conflicts efficiently.
- **Leadership & Support:** Strong leadership motivates and supports team members, ensuring cohesion.
- **Psychological safety:** The strongest measured predictor of team effectiveness in the software
  studies below — β = .660, three times any composition variable {% cite verwijs2024diversity %}.

{: .note }
The fifth item used to read "**Synergy:** Collective efforts produce results that exceed
individual capabilities." It has been replaced rather than re-worded, because it was the same
unsourced claim as above and the first four items are the ones the literature actually attaches
numbers to.

---

## Does diversity improve decisions?

This page previously asserted "*Enhanced decision-making: diverse perspectives lead to better
solutions*", uncited. The largest study of the question in software teams does not support it as
stated. Verwijs and Russo surveyed **1,118 members of 161 teams** and modelled four kinds of
diversity {% cite verwijs2024diversity %}:

- **Only age diversity** predicted team effectiveness — β = .213, p = .041. **Gender, cultural
  background and role diversity were not significant** on effectiveness or on relational conflict.
  The authors read age as a likely proxy for tenure and experience.
- **Psychological safety outranked every diversity variable** (β = .660 on effectiveness,
  β = −.636 on relational conflict), and it acts **directly** rather than by buffering diversity:
  all eight moderation tests failed. The common lecture claim that safety works by absorbing the
  friction of a diverse team is the one most likely to be stated backwards.
- **Relational conflict did not reduce effectiveness** — β = .081, p = .747, against the authors'
  own hypothesis.

{: .warning }
One study; a self-selected sample recruited through an Agile self-diagnosis tool, with no
computable response rate; effectiveness measured as self-reported perception (team morale loads
.873, perceived stakeholder satisfaction only .389). It sits between meta-analyses that disagree
with each other. Read it as a reason to stop *asserting* the diversity–performance link, not as
proof that composition is irrelevant.

---

## Types of Teams

- **Problem-Solving Teams:**  
  Diverse members address specific organizational issues collaboratively.  
  *Example:* A team formed to improve software deployment processes.

- **Cross-Functional Teams:**  
  Members from different departments collaborate to achieve specific objectives.  
  *Example:* Developers, designers, and marketers working together on a product launch.

- **Self-Managed Teams:**  
  Autonomous teams manage day-to-day operations without direct supervision.  
  *Example:* An Agile Scrum team planning and executing sprints independently.

- **Virtual Teams:**  
  Geographically dispersed members work together through digital tools, enabling remote collaboration.  
  *Example:* International team members collaborating via Slack and Zoom.

---

## Common Challenges Teams Face

This list used to be an unsourced inventory. There is a measured one: Hoffmann and colleagues had
**192 practitioners** rate **33 human challenges** for frequency (0–4) and criticality (0–3), and
ranked them by the product of the two {% cite hoffmann2021humanside %}. The five highest:

| Rank | Challenge | Freq. | Crit. | Mitigation in place |
|---|---|---|---|---|
| 1 | Insufficient analysis at the beginning of a task | 2.43 | 2.07 | 46% |
| 2 | Lack of leadership | 2.21 | 1.91 | 39% |
| 3 | Missing documentation of the project | 2.59 | 1.59 | 49% |
| 4 | Demotivation | 2.04 | 1.92 | 37% |
| 5 | Information is not made known to the team | 2.06 | 1.86 | 38% |

Three findings from that study matter more than the ranking itself:

- **Organisations mitigate the challenges that blame nobody.** Lack of qualification 58%, lack of
  experience 57%, missing documentation 49% — against **conflicts of interest at management level
  13%**, over-confidence 16%, and certain people dominating discussions 21%. The problems that
  require a difficult conversation are the ones left almost untouched.
- **Distance and churn are different failure modes.** Across six virtualization dimensions,
  remote and distributed working raised the **frequency** of challenges and almost never their
  **criticality**. One dimension — "is your team occasionally recomposed?" — moved seven
  challenges, and it is the only one that raised *frequently changing team members* (+0.929,
  p = 0.0001), *missing respect in the workplace* (+0.634), *people getting angry in discussions*
  (+0.396) and *harassment* (+0.220). **Distance degrades coordination; membership churn degrades
  civility.** They need different interventions, and only one of them is helped by better tooling.
- **Rare is not mild.** Missing respect, frequently changing members and harassment sit in the
  bottom nine by impact, yet each carries a criticality **median of 2 — the same as the
  top-ranked challenge**. The impact ranking is for prioritising process work; it is the wrong
  lens for anything with a floor.

{: .warning }
Descriptive and non-causal by the authors' own positioning. Convenience sample, 75.5%
Germany-based; both the challenge and its frequency are self-reported by one member per team; the
"occasionally recomposed" item is undefined, so the strongest result rests on the vaguest
question. Impact is normalised by scale *points* rather than observed maxima — do not quote it as
a percentage.

The familiar groupings below are still useful as vocabulary; where evidence exists it is attached.

- **Communication Breakdown:**  
  - Misunderstandings and lack of clarity can lead to confusion and inefficiency.  
  - Differences in communication styles can create barriers to effective collaboration.  
  - *Measured:* "Information is not made known to the team" ranks 5th and "misunderstandings in
    communication" 7th of 33 {% cite hoffmann2021humanside %}.

- **Conflict and Tension:**  
  - Diverse perspectives can lead to disagreements and interpersonal conflicts.  
  - *Measured, and it points the other way:* relational conflict had **no** effect on
    effectiveness (β = .081, p = .747), while low psychological safety strongly **produced**
    conflict (β = −.636) {% cite verwijs2024diversity %}. The lever is safety, not conflict
    suppression.

- **Lack of Clear Goals:**  
  - Ambiguity in objectives can cause misalignment and reduce team effectiveness.  
  - Without a clear direction, members may struggle to prioritize tasks.

- **Ineffective Leadership:**  
  - Poor leadership can lead to a lack of motivation, unclear direction, and disorganization.  
  - *Measured:* lack of leadership is the **2nd** most impactful challenge of 33, with mitigation
    reported by only 39% of respondents {% cite hoffmann2021humanside %}.

- **Imbalance in Workload:**  
  - Uneven distribution of tasks can lead to burnout for some members while others may be
    underutilized.  
  - *Measured, with a modern shape:* after AI coding assistance entered open-source projects,
    peripheral contributors produced **43.5% more commits** while core developers reviewed
    **6.5% more** code and their own commit output fell **19%** {% cite xu2025debt %}. The
    imbalance appeared without anyone withdrawing effort. See
    [Motivation](motivation.html) for the caveats — this is observational, nobody's tool use was
    observed, and in that paper `*` means p < 0.1.

- **Resistance to Change:**  
  - Teams may struggle to adapt to new processes, technologies, or organizational changes.  
  - Resistance can slow down progress and lead to frustration among team members.

- **Virtual Team Challenges:**  
  - Time zone differences, cultural barriers, and lack of face-to-face interaction can hinder
    collaboration.  
  - *Measured:* virtualization raises how **often** challenges occur, essentially never how
    **bad** they are — across six dimensions and 33 challenges there was exactly one criticality
    increase and one decrease {% cite hoffmann2021humanside %}.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and
**David Root** {% cite root2014lectures %} on software project management. The structure,
examples, and pedagogical approach reflect their teaching materials and frameworks.

---

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
