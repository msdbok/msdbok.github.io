---
parent: Frameworks
title: Scrum
nav_order: 5
layout: default
---

# Scrum

Scrum is *"a lightweight framework that helps people, teams and organizations generate value through
adaptive solutions for complex problems"* {% cite schwaber2020scrumguide %}. It works by fixing the
*time* — a Sprint of a month or less — and letting the scope inside it settle, then inspecting the
result and adapting before the next one.

It is deliberately incomplete. The Guide describes Scrum as *"a container for other techniques,
methodologies, and practices"*: it tells you when to inspect and who is accountable, and says nothing
about how to design, test or deploy.

## 1. The framework in one pass

A **Scrum Team** is one team with three accountabilities and no sub-teams: the **Product Owner**,
accountable for maximising value and for the Product Backlog; the **Scrum Master**, accountable for
the team's effectiveness and for the framework being understood; and the **Developers**, accountable
for a usable Increment each Sprint {% cite schwaber2020scrumguide %}.

Inside each Sprint sit four events — **Sprint Planning**, the **Daily Scrum**, the **Sprint Review**
and the **Sprint Retrospective** — and three artefacts, each of which carries a commitment that makes
it checkable:

| Artefact | Commitment |
|---|---|
| Product Backlog | Product Goal |
| Sprint Backlog | Sprint Goal |
| Increment | Definition of Done |

The commitments are the part most often dropped, and the part that does the work. A backlog with no
Product Goal is a list; an Increment with no Definition of Done cannot be said to be finished, only
stopped.

## 2. What adopting it actually changes

Scrum's cost is rarely the ceremonies. It is the commitment structure. A team moving to Scrum from a
pull-when-free discipline moves to committing to a Sprint Goal and holding scope stable within the
Sprint — and an environment of genuinely changing priorities is what makes that hard, not the length
of the stand-up.

**Example — a support team asked to adopt Scrum.** A team handling interrupt-driven maintenance
adopts two-week Sprints. The Sprint Goal is agreed on Monday; on Tuesday a production incident
consumes two developers for three days. The Sprint Goal is now unreachable, and the team has a
choice between abandoning it and pretending. Repeat that fortnightly and the commitment becomes
ceremonial. Rubin's advice for exactly this case is to use [Kanban](kanban.md) instead — *"Scrum is
not well suited to highly interrupt-driven work"* — and to run both in one organisation where the
work genuinely differs {% cite rubin_essential_2012 %}.

That is the question to ask before adopting Scrum: **is our work predictable enough to hold a goal
still for a Sprint?**

## 3. The immutability clause, and the argument about it

The Guide is explicit that Scrum is not a menu: *"The Scrum framework, as outlined herein, is
immutable. While implementing only parts of Scrum is possible, the result is not Scrum"*
{% cite schwaber2020scrumguide %}.

Set against that, the empirical picture is that almost nobody adopts a method whole. Hybrid
approaches *"have become reality for nearly all companies"* and are *"neither planned nor designed
but emerge from the evolution of different work practices"* {% cite kuhrmann2019hybrid %}, and
customising the agile approach is one of eleven named **success factor** categories in the largest
review of large-scale transformations {% cite dikert2016scaling %}.

The sharpest form of the objection comes from inside the agile literature rather than from its
critics: Abrahamsson and colleagues make *straightforwardness* — a method being **easy to learn and
to modify** — one of four properties that make a method agile {% cite abrahamsson2002agile %}. On
that definition a framework forbidding modification scores badly on its own family's terms.

This handbook does not resolve that. Both positions are citable and the disagreement is real: read
[choosing a framework](choose.md) with both in hand.

## How solid is this?

- **Interested party.** The Guide is a normative document written by the framework's owners and
  distributed by organisations that certify people in it {% cite schwaber2020scrumguide %}. That is
  provenance rather than an accusation, but it is a definition and a claim, not evidence.
- **Editions differ**, so say which one you mean. This page uses the **2020** Guide; the **2016**
  edition had a separate *Development Team* inside the Scrum Team and worded immutability more
  broadly — *"Scrum's roles, artifacts, events, and rules are immutable"*
  {% cite schwaber2016scrumguide %}. Course material written before 2020 will use the older roles.
- **Kuhrmann is 69 respondents**, self-selected and European, surveyed in 2016. Quote its percentages
  as *of 69 respondents*; its own 19.6%/83.9% split does not sum to 100. It shows hybrids are
  **used**, not that they work better — there is no outcome data {% cite kuhrmann2019hybrid %}.
- **Dikert is mostly experience reports** — roughly 90% by its authors' own count, and they state
  they *"decided not to make quantitative interpretations"* {% cite dikert2016scaling %}.
- **Abrahamsson's four criteria are proposed**, not validated: there is no instrument and no scoring
  behind them {% cite abrahamsson2002agile %}.

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
