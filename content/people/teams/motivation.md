---
page_type: deep-dive   # evidence-dense: Herzberg + Beecham tables, Wu vs Corgnet comparison
parent: Personality
title: Motivation
nav_order: 6
layout: default
---

# Motivation

Motivation is what makes a person willing to spend effort on the work — and in software teams the
strongest reported source of it is not pay or praise but **identifying with the task**: knowing
what the work is for and finding it interesting {% cite beecham2008motivation %}.

## 1. Herzberg's two factors

Herzberg separates what makes people satisfied from what makes them dissatisfied, and argues they
are different lists {% cite herzberg1968motivate %}. **Motivators** are intrinsic to the work:
achievement, recognition for achievement, the work itself, responsibility, advancement and growth.
**Hygiene factors** are the surroundings: company policy and administration, supervision, working
conditions, salary, relationships with colleagues, status and security. Removing dissatisfaction is
not the same as motivating. *Example:* a developer trusted to design a service stays engaged
(motivator) while a flaky test suite grinds them down (hygiene) — fixing the suite buys back
attention but does not create commitment.

His evidence pools **12 investigations** across **1,685 employees**: of the factors contributing to
satisfaction **81% were motivators**, and of those contributing to dissatisfaction **69% involved
hygiene**. The theory "was first drawn from an examination of events in the lives of **engineers
and accountants**" (p. 6) — a closer population to a software team than most classics here.

## 2. What software engineers actually report

Beecham and colleagues reviewed **92 papers spanning 1980–2006** across 16 countries and extracted
21 motivators {% cite beecham2008motivation %}. The most-cited one is not on Herzberg's list:

| Motivator | Studies reporting it |
|---|---|
| **Identify with the task** — clear goals, personal interest, knowing the purpose | **20** |
| Good management · employee participation | 16 each |
| Career path | 15 |
| Rewards and incentives · variety of work · sense of belonging | 14 each |
| Recognition | 12 |
| Autonomy | 9 |

The leading de-motivators are a poor working environment and lack of resources (9), poor management
(7), uncompetitive pay (6), stress (5) and poor communication (5). Herzberg's *frame* survives —
working conditions sit on the hygiene side — but the *content* shifts: pay and recognition rank
well behind identifying with the task.

## 3. Two frameworks worth the vocabulary

**Self-determination theory** (Deci and Ryan) holds that people are motivated when three needs are
met — **autonomy** over how the work is done, **competence** at it, and **relatedness** to the
people doing it. Choice of framework, time to learn it and a stand-up worth attending address all
three.

**Expectancy theory** (Vroom) multiplies three beliefs: **expectancy** that effort produces
performance, **instrumentality** that performance produces a reward, and **valence** that the
reward is worth having. One term at zero zeroes the product, which is why a bonus scheme nobody
believes in motivates nobody.

## 4. Practical techniques

Most workable techniques make effort visible and tie it to the goal: progress on a board or
burndown, end-of-sprint demos, peer-recognition channels, rotation between front-end, back-end and
test work, and rituals such as retrospectives that mark what changed. These are largely
*identifiability* measures, so Thompson's qualification applies to all of them — visibility only
changes behaviour if somebody acts on what it shows (p. 51) {% cite thompson2015makingtheteam %}.
See [Social Loafing](loafing.html).

## 5. When the collaborator is a model

Two recent studies asked whether generative AI helps or harms intrinsic motivation and reached
**opposite answers**. Both are sound; they measured different things, and separating them is the
skill worth taking away.

| | Wu et al. {% cite wu2025motivation %} | Corgnet et al. {% cite corgnet2026aimotivation %} |
|---|---|---|
| Compares | AI-assisted work → **then unassisted** | Working with **AI** vs with **a human** |
| Design | 4 pre-registered experiments, **N = 3,562** | **n = 1,091** plus 180 raters |
| Finding | Performance rose, but sense of control and intrinsic motivation fell and boredom rose on the handoff back | Relatedness, competence, autonomy, satisfaction and interest all higher with AI (d = 0.2–0.5) |

With their bounds attached the two are consistent: **collaborating with AI is motivating while it
lasts, and losing it costs something.** Herzberg predicts the shape of Wu's result by his own
mechanism — three of his six motivators are the work itself, responsibility and achievement, so
stripping the challenge out of a job takes intrinsic motivation with it. That reading is a
synthesis, not a claim either paper makes.

## How solid is this?

- **Herzberg is a method problem, not just an old one.** It rests entirely on the critical-incident
  interview — what made you extremely happy or unhappy at work — which invites attribution bias
  (credit the self, blame the environment) and would produce the 81/69 pattern whether or not the
  two-factor structure is real. No effect sizes, significance tests or replication failures are
  reported, and software developers are not among the pooled populations.
- **Beecham counts studies, not effects.** Its window closes at **2006**, before agile and
  distributed work were normal, and the authors warn the aggregated frequencies "need to be treated
  with caution". It found **no dominant motivation model** in software engineering, and 56% of
  studies distinguish software engineers from other occupations — so roughly half do not.
- **What we do not hold.** Deci and Ryan's statement of self-determination theory and Vroom's *Work
  and Motivation* are absent from this bibliography, so §3 is vocabulary with no citation rather
  than an invented one.
- **Do not stretch the AI studies.** Wu's effect concerns the **handoff back** to unassisted work,
  on writing and idea generation, not software. Corgnet's authors state their result does not
  extend to replacing a *familiar* teammate, nor to analytical work; the arms were unbalanced
  (698 human–human against 393 human–AI) and the paper is **not peer-reviewed**.

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
