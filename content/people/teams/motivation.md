---
parent: Teams
title: Motivation
nav_order: 4
layout: default
---

# Teams Problems & Motivation
_*Adapted from David Root (2014)_

## The Classic Team Story

A very common scenario in teams:

> "This is the story of four people named Everybody, Somebody, Anybody, and Nobody.  
> There was an important job to be done and Everybody was asked to do it.  
> Anybody could have done it, but Nobody did it. Somebody got angry about that because it was Everybody's job.  
> Everybody thought Anybody could do it, but Nobody realized that Everybody wouldn't do it.  
> Consequently, it wound up that Nobody told Anybody, so Everybody blamed Somebody."

**Lesson:**  
Lack of clarity in roles and accountability leads to confusion, frustration, and blame.

**Software Example:**  
In a Scrum team, if “Everybody” assumes someone else will write unit tests, tests never get written. The sprint fails, and “Somebody” complains—but no one feels directly responsible.

---

## Social Loafing & The Freerider Problem

**Social loafing** is the phenomenon that people in groups often do not work as hard as they do
when working alone {% cite thompson2015makingtheteam %} (p. 47). Team performance still increases
with team size, but "the rate of increase is negatively accelerated, such that the addition of new
members to the team has diminishing returns on productivity" (p. 47). A few motivated members
carry the workload while others contribute less.

The origin is **Ringelmann's** rope-pulling experiment, which this page taught for years without
naming him. Greenberg reports it as the classic demonstration: "as more people pulled the rope,
the total force exerted by the group as a whole rose but the average force exerted per person
dropped" {% cite greenberg2011behavior %} (p. 296). The potential-versus-actual arithmetic behind
it — 126 / 189 / 504 kg of potential against 118 / 160 / 248 kg actually pulled — is on
[Teams Basics](index.html), together with the caveats about where those numbers come from.

**The mechanism has a name too: social impact theory.** The social force acting on a group is
divided among its members, so "the responsibility for doing the job is diffused over more people"
and the larger the group, the less pressure any individual feels {% cite greenberg2011behavior %}
(p. 296).

{: .warning }
**Social loafing is not established as a human universal, and this matters in an international
cohort.** Greenberg's own section *"Is Social Loafing a Universal Phenomenon?"* reports that
"social loafing occurred in the United States" but that **the effect reversed** in the People's
Republic of China and in Israel — both collectivistic cultures, where working in a group produced
*more* effort rather than less (p. 297). That is one reported study rather than a meta-analysis,
so it is not a finding about any individual student either. Teach the effect as contingent on
context, not as a property of people.

{: .note }
**Citation fix.** This page used to attribute the material to "Greenberg, 1996, *Managing
Behaviors in Organizations*", its own source list said 1999 (2nd ed.), and the bibliography held
2010 — one book, three years, and a title that does not exist. The copy this handbook works from
is **Jerald Greenberg, *Behavior in Organizations*, 10th ed., Pearson, 2011** — singular
"Behavior", no "Managing". The wording of the older text on this page in fact tracked Thompson
pp. 47–48, whose own exhibit credits a 1996 Greenberg edition; that is how the misattribution
travelled.

![Dilbert Freerider](image.png)

### What is the Freerider Problem?

- **Free riders** are team members who contribute less, relying on others to carry the workload.

{: .note }
**The classic definition no longer covers the modern case.** In a study of 2,755 open-source
repositories around the introduction of AI coding assistance, peripheral contributors did **not**
withdraw effort — they produced **43.5% more commits** and 17.7% more pull requests, while **core**
developers reviewed **6.5% more** code and their own commit output fell **19%**
{% cite xu2025debt %}. The cost still landed on the core, through **volume** rather than idleness.
Free riding here is structural: nobody has to feel anything for the imbalance to appear, and the
resource being consumed — senior attention — appears on no dashboard. Read the paper carefully
before quoting it: it is observational, the treatment is *a programming language in a period*
rather than observed tool use, `*` denotes p < 0.1 throughout, and its own headline "42.9%" is
miscomputed (for the stated coefficient the change is −30.0%).

#### Causes of Social Loafing

Thompson gives **three** {% cite thompson2015makingtheteam %} (p. 49):

- **Diffusion of responsibility:**  
  It is difficult to distinguish individual contributions, so people feel less accountable.
- **A reduced sense of self-efficacy:**  
  Members come to believe their own effort cannot make a difference to the outcome.
- **Sucker aversion:**  
  Fear of being taken advantage of — doing all the work and getting little credit.

{: .note }
This page previously listed **four** causes, splitting the second into "lack of recognition" and
"dispensability of effort" and citing nothing. Both are readings of reduced self-efficacy; the
three above are what the cited source says.

**Software Example:**  
In a hackathon, one person ends up coding all night while others just brainstorm, then all claim equal credit.

---

## Enhancing Team Performance

The seven remedies below are Thompson's own headings, in her order
{% cite thompson2015makingtheteam %} (pp. 50–53).

- **Increase identifiability:**  
  Make individual contributions visible and recognized.
- **Promote involvement:**  
  Encourage active participation and engagement from all members.
- **Reward team members for performance:**  
  Use incentives and recognition to motivate effort.
- **Strengthen team cohesion:**  
  Build trust, shared goals, and a sense of belonging.

### How to Strengthen Teams

- **Increase personal responsibility:**  
  Assign clear roles and tasks.
- **Provide team performance and review feedback:**  
  Give constructive feedback regularly.
- **Maintain appropriate staffing levels:**  
  Avoid teams that are too large or too small for the task.

{: .warning }
**The qualification this page used to drop.** "The key is **not identifiability per se**, but
rather the **evaluation that identifiability makes possible**" (p. 51). Publishing a dashboard of
who committed what does not reduce loafing on its own; somebody has to act on it. In a team where
a growing share of the work is generated rather than written, the evaluation that identifiability
was supposed to enable is the first thing to degrade.

**Tip:**  
Feedback and accountability should be positive and supportive, not punitive.  
Celebrate successes and address issues constructively.

---

## Additional Motivational Theories for Teams

### 1. Herzberg's Two-Factor Theory

- **Motivators** (intrinsic to the work): achievement, recognition for achievement, the work
  itself, responsibility, advancement, growth.
- **Hygiene factors** (extrinsic): company policy and administration, supervision, work
  conditions, salary, relationships with supervisor, peers and subordinates, status, security.
  Removing dissatisfaction is not the same as motivating.

*Example:*  
Developers stay motivated when trusted to design solutions (motivator), but poor tooling (hygiene) can frustrate them.

**Where the theory comes from** — a provenance this page has never stated, and it is a good one
for a software course. Herzberg's Exhibit 1 pools **12 investigations** across samples of
**1,685 employees**, characterising 1,844 events that led to extreme dissatisfaction and 1,753
that led to extreme satisfaction; of the factors contributing to satisfaction **81% were
motivators**, and of those contributing to dissatisfaction **69% involved hygiene**
{% cite herzberg1968motivate %}. The theory "was first drawn from an examination of events in the
lives of **engineers and accountants**" (p. 6) — a closer population to a software team than most
of the classics this area relies on.

{: .warning }
**Method, not just age.** All of it rests on the **critical-incident interview**: people are asked
what made them extremely happy or unhappy at work. That design invites attribution bias — credit
the self, blame the environment — which would produce this exact 81/69 pattern whether or not the
two-factor structure is real. Herzberg reports no effect sizes, no significance tests, no
confidence intervals and no replication failures. The pooled populations run from nurses and food
handlers to Finnish foremen and Hungarian engineers; **software developers are not among them.**

**The software-specific layer.** Beecham and colleagues reviewed **92 papers spanning 1980–2006**
across 16 countries and extracted **21 motivators** and 15 de-motivators
{% cite beecham2008motivation %}. The most-cited motivator is not on Herzberg's list at all:

| Motivator | Studies reporting it |
|---|---|
| **Identify with the task** — clear goals, personal interest, knowing the purpose | **20** |
| Good management | 16 |
| Employee participation | 16 |
| Career path | 15 |
| Rewards and incentives · variety of work · sense of belonging | 14 each |
| Recognition | 12 |
| Autonomy | 9 |

Top de-motivators: poor working environment and lack of resources (9), poor management (7),
uncompetitive pay (6), stress (5), poor communication (5). Herzberg's *frame* survives — Beecham
places working conditions and resources as hygiene — but the *content* shifts: this page's older
emphasis on pay and recognition sits at 6 and 12 studies, well behind identifying with the task.

{: .warning }
Beecham's window closes at **2006**, before agile went mainstream and before distributed work was
normal, and the method is frequency counting: no effect sizes, no pooling, and the authors warn
that the aggregated frequencies "need to be treated with caution". It tells you what has been
*studied*, not how large anything is. It also found **no dominant motivation model** in software
engineering, and reports that 56% of studies find software engineers distinguishable from other
occupational groups — which means roughly half do not.

### 2. Self-Determination Theory (Deci & Ryan)

People are motivated when three needs are met:
- **Autonomy:** Control over work.
- **Competence:** Ability to grow skills.
- **Relatedness:** Belonging to a team.

*Example:*  
Giving a developer freedom to choose a framework (autonomy), providing learning resources (competence), and fostering supportive stand-ups (relatedness).

### 3. Expectancy Theory (Vroom)

Motivation depends on:
- **Expectancy:** Effort → performance link.
- **Instrumentality:** Performance → reward link.
- **Valence:** Value of the reward.

*Example:*  
If a developer knows that fixing bugs quickly (effort) will be noticed (performance) and lead to recognition or promotion (reward), they’re more motivated.

{: .warning }
**These last two are presented as vocabulary, not as evidence, because this handbook does not hold
their primary sources.** Deci and Ryan's statement of self-determination theory and Vroom's
*Work and Motivation* are both absent from the bibliography, so no citation is offered here in
place of one — inventing a plausible reference would be worse than the gap. Herzberg
{% cite herzberg1968motivate %} and Beecham {% cite beecham2008motivation %} are the two
frameworks on this page whose evidence you can go and check. Note that the AI studies below
*measure* SDT's constructs without being a source for the theory itself.

---

## Practical Motivation Techniques in Software Teams

- **Gamification:** Use leaderboards for bug fixes, coding challenges, or test coverage.
- **Visible progress:** Kanban boards or burndown charts to show team achievements.
- **Celebrating wins:** End-of-sprint demos and pizza Fridays to acknowledge progress.
- **Peer recognition:** “Kudos” channels in Slack or Trello cards highlighting contributions.
- **Job rotation:** Switch between front-end, back-end, and testing tasks to keep skills fresh.
- **Team rituals:** Regular stand-ups, retrospectives, or fun check-ins to build team spirit.

{: .note }
Most of these are *identifiability* measures. Thompson's caveat applies to all of them: visibility
only reduces loafing if it is followed by evaluation (p. 51) {% cite thompson2015makingtheteam %}.

---

## Motivation when the collaborator is a model

Two 2025–26 studies asked whether generative AI helps or harms intrinsic motivation and reached
**opposite answers**. Both are sound. They measured different things, and separating them is the
transferable skill.

**Wu and colleagues** ran four pre-registered randomized experiments, **N = 3,562**
{% cite wu2025motivation %}. Performance on the AI-assisted task improved. But when participants
then moved **back to working unassisted**, their sense of control and intrinsic motivation fell
and boredom rose. The authors had hypothesised a *positive* spillover from AI-assisted work to
independent work; **their own hypothesis was not supported.**

**Corgnet and colleagues** compared collaborating with AI against collaborating with a person —
**n = 1,091** analysed, plus 180 independent raters {% cite corgnet2026aimotivation %}. Perceived
relatedness, competence, autonomy, job satisfaction and interest were all **higher** with AI
(Cohen's d = 0.2–0.5), with a performance advantage of d = 0.33 on a creative task. Workers
reported higher relatedness toward the AI than toward a human coworker.

| | Wu et al. 2025 | Corgnet et al. 2026 |
|---|---|---|
| Compares | AI-assisted work → **then unassisted** | Working with **AI** vs with **a human** |
| Question | What does the *handoff back* cost? | Which *partner* is more motivating? |
| Finding | Sense of control and intrinsic motivation fall | Relatedness, competence, autonomy rise |
| Team | Individual tasks; writing and idea generation | **Newly formed** teams of strangers; creative tasks |
| Status | *Scientific Reports* | SSRN working paper, **not peer-reviewed** |

Read with their own bounds attached, the two are consistent: **collaborating with AI is motivating
while it lasts, and losing it costs something.** Neither says AI raises or lowers "motivation" as
a property of anything.

{: .warning }
**Do not stretch either one.** Wu's effect is about the **handoff back to unassisted work**, not
about AI use in general, and the tasks were writing and idea generation — not software.
Corgnet's authors state their result does **not** extend to replacing a *familiar* teammate, which
"would likely reduce perceived relatedness", nor to analytical or expert-judgment work; the arms
were unbalanced (698 human–human against 393 human–AI) and the paper is not peer-reviewed.

Herzberg predicts the shape of Wu's result by his own mechanism, which is why the classic and
modern halves of this page are one argument rather than two eras stapled together: three of his
six motivators are **the work itself**, **responsibility** and **achievement**. Strip the
intellectual challenge and the responsibility out of a job and intrinsic motivation goes with
them. **That reading is a synthesis, not a claim either paper makes.**

### Loafing with a machine in the loop

Stieglitz and colleagues measured social-loafing tendencies when the collaborator is a **virtual
assistant** {% cite stieglitz2022loafing %}. A self-reported tendency to loaf in human groups
predicted low-effort behaviour with the assistant (r = 0.344, about 12% of variance) — but the
traits that protect a human team stopped predicting altogether: conscientiousness fell from
r = −0.496 (p < .001) to −0.125 (ns), need for cognition from −0.406 to −0.187 (ns). With no
colleague to feel the slack, agreeableness has nothing to act on. Effort correlated negatively
with loafing (r = −0.309) while frustration did not move (r = −0.034, ns), which the authors read
as **task offloading rather than disengagement** — *smart loafing*, which they argue may be benign.

{: .warning }
**Two caveats that must travel with those numbers.** **There is no control condition**: every
participant had the assistant and nobody worked alone, so no effort decrement against a solo
baseline was ever measured. And two of the six loafing items measure *tool usefulness* ("enabled
me to complete the task more quickly"), so a participant who was genuinely helped scores as a
loafer. The sample was 102 people, 81.4% still studying. The authors also carve out an exception
worth saying aloud in a university: "smart loafing in, for instance, **learning environments**
might be hindering and not 'smart'."

Put in sequence with the free-rider finding above: **offloading effort is smart only if nobody
downstream is paying for it.** Stieglitz's argument that "no other human team member needs to
compensate" is exactly what {% cite xu2025debt %} tests at scale and does not find.

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
