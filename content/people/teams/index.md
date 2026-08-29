---
parent: People
title: Teams
nav_order: 3
layout: default
---

# Teams

A **team** is a small group with complementary skills whose members share one goal and depend on
each other's work to reach it. That interdependence is what separates a team from a set of people
who merely report to the same manager.

Interdependence also makes a team expensive: it buys shared knowledge at the price of coordination.
Thompson is careful about the trade — teams "can outperform the best
member of the group, **but there are no guarantees** … Teams are not a panacea for organizations;
they often fail and are frequently overused or poorly designed"
{% cite thompson2015makingtheteam %} (p. 29).

## Types of teams

Four shapes recur in software organisations, formed for different reasons:

- **Problem-solving teams** are convened around one issue and disband when it is fixed.
  *Example:* a group pulled together for six weeks to cut deployment from a day to an hour.
- **Cross-functional teams** put developers, designers and marketers under one objective, so
  hand-offs happen in the room rather than between departments.
- **Self-managed teams** own their day-to-day work without a supervisor allocating it; a Scrum team
  running its own sprints is the everyday case.
- **Virtual teams** are spread across sites and time zones, coordinating through chat, video and
  shared boards rather than face to face.

## What goes wrong

Most lists of team problems are folklore; there is a measured one. **192 practitioners** rated
**33 human challenges** for frequency (0–4) and criticality (0–3), ranked by the product of the two
{% cite hoffmann2021humanside %}. The top five:

| Rank | Challenge | Freq. | Crit. | Mitigated |
|---|---|---|---|---|
| 1 | Insufficient analysis at the start of a task | 2.43 | 2.07 | 46% |
| 2 | Lack of leadership | 2.21 | 1.91 | 39% |
| 3 | Missing documentation of the project | 2.59 | 1.59 | 49% |
| 4 | Demotivation | 2.04 | 1.92 | 37% |
| 5 | Information is not made known to the team | 2.06 | 1.86 | 38% |

Two readings matter more than the ranking. **Organisations mitigate the challenges that blame
nobody** — lack of qualification 58%, missing documentation 49% — against conflicts of interest at
management level 13% and dominating discussions 21%. And **rare is not mild**: missing respect,
changing members and harassment sit in the bottom nine by impact, yet each carries a criticality
median of 2, the same as the top-ranked challenge.

{: .warning }
That study is descriptive, self-reported by one member per team and 75.5% Germany-based; its impact
score is normalised by scale points, so do not quote it as a percentage.

## Where to go next

| Page | The question it answers | Anchor evidence |
|---|---|---|
| [Team Performance](performance.html) | Does a team beat its members working alone, and what predicts it? | Steiner; safety |
| [Formation](formation.html) | What to settle before the work starts, and how a team develops | Thompson; Tuckman |
| [Motivation](motivation.html) | What makes engineers want to do the work | Herzberg; Beecham |
| [Social Loafing](loafing.html) | Why effort per person falls as a team grows | Ringelmann |
| [Decision Making](decisions.html) | How teams decide, and how that goes wrong | Groupthink; Klein |

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
