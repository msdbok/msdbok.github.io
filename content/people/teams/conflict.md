---
parent: Teams
title: Conflict
nav_order: 5
layout: default
---

# Conflict

Team conflict comes in two kinds. **Task conflict** is disagreement about the work — what to build
and how. **Relational conflict** is disagreement about each other. Telling the two apart is most of
a manager's job here, because the response differs.

## 1. The distinction that does the work

Task conflict is how a team reaches a decision: two designs argued to a conclusion, an estimate
challenged until it is believable. Relational conflict is friction between people, and it is what
teams usually mean when they say they have a conflict. The same argument can be both at once, which
is why the label has to be settled before the intervention is chosen.

The measured evidence is not what most teaching material assumes. Among 1,118 members of 161
software teams, **relational conflict did not reduce team effectiveness** — β = .081, p = .747,
against the authors' own hypothesis {% cite verwijs2024diversity %}. Nor did diversity of gender,
culture or role predict relational conflict. Do not read that as "conflict is harmless". Read it as
a warning that the confident causal story usually told about team conflict is not the one the data
tells.

## 2. Two good engineers who cannot work together

The course's C1 case is exactly this problem. In the Satera team at Imatron Systems, escalating
conflict arose from **the conflicting cognitive styles of two senior mechanical engineers**, taking
a toll on both project progress and team morale and endangering one of the company's most important
initiatives {% cite amabile_satera_2003 %}. After discussing the situation with the VP of R&D, team
leader Gary Pinto concludes he must take decisive action. The case is written to present "a common
problem that managers must face when working with creative people on creative projects".

Nothing in it is peculiar to hardware. For example, two senior engineers who are each individually
right — one wanting a six-week incremental refactor with tests at every step, the other a rewrite
behind a feature flag — can turn a design review into something the rest of the team stops
attending, and a release date nobody will commit to. The technical question is decidable in an
afternoon. The reason it has not been decided in three weeks is not technical.

## 3. Cognitive style is vocabulary, not a diagnosis

Differences in how people prefer to solve problems are real and visible in a review. A type
framework such as [MBTI](../perso/mbti.html) supplies shared vocabulary for that difference, which
is what makes the conversation possible at all: *you want the whole picture before you commit; I
want to try something today*. That is where its usefulness ends. Type distributions do not predict
team performance and do not license composing a team from four-letter codes — the MBTI page sets
out why. Use style language to describe a friction the team is already feeling, never to explain it
away, and never to assign work.

## 4. What a manager does

Storming is the phase where this is expected rather than exceptional, and [Formation](formation.html)
covers where it belongs in a team's development. When two capable people cannot work together, four
moves stay available:

- Name the behaviour and its effect on the work, not the person's character or preferences.
- Make the decision rule explicit — say who decides and by when, so the argument has an exit.
- Go after root causes rather than symptoms, and judge whether to step in or let the team settle it
  {% cite glen2003leadinggeeks %}.
- Separate the two questions: the technical disagreement can be closed today, while the working
  relationship is a longer job that closing it does not fix.

## How solid is this?

- **This page is thin on evidence, and that is its honest state.** The one measured finding
  available here is a *null* result — Verwijs and Russo's non-effect of relational conflict — from
  self-report data collected through an Agile self-diagnosis tool, with effectiveness measured as
  perception rather than delivery.
- **The Satera case is teaching material, not a study.** It describes one product-development team,
  carries no measurement, and generalises to nothing on its own.
- **The task-versus-relational distinction is imported.** The management literature that
  established it is not in this bibliography, so it is offered here as working vocabulary, not as a
  finding this course can vouch for.
- **No conflict-resolution technique in the corpus has been evaluated.** Glen's advice is a
  practitioner heuristic and he claims no measured distribution of conflict causes; the four moves
  above are teaching material of the same kind.

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
