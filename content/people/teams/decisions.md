---
parent: Teams
title: Decision Making
nav_order: 5
layout: default
---

# Teams Problems: Decision Making
_*Adapted from David Root (2014)_

## Basics

### Decision Levels

- **Operational:**  
  Everyday decisions, often made quickly with little structure.  
  *Example:* Assigning today’s coding task or approving a pull request.

- **Tactical:**  
  Medium-term decisions that support strategy and direct resources.  
  *Example:* Choosing a testing framework for the project.

- **Strategic:**  
  Long-term decisions about direction, goals, values.  
  *Example:* Deciding to adopt Agile development across the organization.

---

### Major Problem – Analysis Paralysis

When teams spend too much time analyzing options, they fail to act.

- **Buridan’s Ass:** A paradox where too many choices prevent decision.
- **Focus on drawbacks:** Overemphasis on risks stalls progress.
- **Result:** Delay, lost opportunities, wasted energy.

---

### Basic Techniques

- **T-Chart (+/–):** Compare pros and cons.
- **SWOT Analysis:** Strengths, Weaknesses, Opportunities, Threats.
- **Pareto Analysis (80/20 Rule):** Focus on the small % of causes that yield big results.
- **Pair-Wise Comparison:** Compare options against each other, one by one.
- **Cost-Benefit Analysis:** Compare expected gains vs. expected costs.

**Software example:** Pareto Analysis helps software teams find the few issues that cause most pain. A team collects bug reports and measures user impact and frequency, sorts defects by cumulative user-reported incidents, and expects to find that a small minority of defects accounts for a large majority of the incidents and complaints. It then prioritizes those defects, pair-codes on the top items, adds regression tests, and watches the metrics to confirm the improvement.

{: .warning }
**The "20% of bugs cause 80% of errors" ratio is a heuristic, not a measurement.** Earlier
versions of this page stated it as an empirical finding. It is a way of deciding where to look
first, and the actual concentration on your own defect data is something to *measure*, not to
assume. Published work on defect and crash concentration in real systems does exist — it is not
held in this handbook's bibliography, so no figure is quoted here rather than a plausible one
being invented.


---

### Decision Making Model

Adapted from Hoover, Rosso-Llopart and Taran, *Evaluating Project Decisions*
{% cite hoover_evaluating_2010 %}.

**Inputs**
- Problem (requirements, constraints)
- Assumptions
- Knowledge (facts, data)
- Experience (skills, intuition)

**Decision Process**
- Select and apply a decision technique (e.g., SWOT, cost-benefit).

**Outputs**
- Solution chosen
- Assumed risks documented

---

## Influencing Factors

### Decision-Driven Organizations

(*Source: Rogers & Blenko*)

- Some decisions matter more than others → focus on high-impact ones.
- Ambiguity is the enemy → clarify.
- Speed & adaptability are crucial.
- Roles > org chart → empower decision-owners.
- Fear of overstepping must be overcome.
- Well-aligned organizations reinforce roles.
- Practice builds capability: “practicing beats preaching.”

**Core problem:**  
How much information is “enough” before deciding?

{: .warning }
**A bullet removed, and why.** This list previously carried "Action is the goal (Standish
Report)" directly above "Ambiguity is the enemy → clarify". No such claim is locatable in the
CHAOS 2015 report, and on goal clarity that report concludes the **opposite** of the neighbouring
bullet: it says the Group had believed clarity and focus were essential and "found the opposite to
be true" — **Vague objectives 38% successful against Precise 22%** — and recommends that teams
"reduce or give up control of the business objectives to encourage and promote innovation"
{% cite standish2015chaos %}. That recommendation is drawn from a bivariate crosstab with no
control for project size and no significance testing, so it is not evidence that ambiguity helps
either. The honest position is that **the disagreement is unresolved**: the advice to clarify is
Rogers and Blenko's, the contrary figure is Standish's, and neither is well-evidenced. The
Standish attribution has been dropped rather than left standing on a claim its own source
contradicts. See the [People overview](../) for why CHAOS figures need
{% cite eveleens2010chaos %} beside them.

---

### Intuitive Decision Making — the Recognition-Primed Decision model

The model behind this section has a name the page has never given it: Gary Klein's
**Recognition-Primed Decision (RPD)** model, developed from studies of fireground commanders and
other high-tempo professionals. Its chain is:

**Situation → Cues → Patterns → Action Scripts**, assessed by **Mental Simulation** against the
decision maker's **mental models**.

The claim is not that experts choose well among options — it is that they usually do not generate
options at all. A recognised pattern produces a single candidate action, which is then run
forward mentally; if the simulation exposes a problem, the action is modified or the next
candidate considered. This is why an expert's *first considered action* is so often workable.

{: .warning }
**We do not hold either Klein book.** This handbook's account of RPD comes through the course
lecture materials {% cite root2014lectures %}, and the lecture slide cites "Klein p. 16" without
naming the book; earlier versions of this page attributed the section to *The Power of Intuition*
(2003) in one place and *Sources of Power* (1998) in another. Neither is in our bibliography, and
neither has been read for this page — so no page-level citation is offered, and RPD is presented
here as **a described model whose primary source we have not verified**, not as a finding. That
matters more than usual for this section, because the page's negative account of decision making
(the biases below) now rests on a systematic review, while its positive account does not.

- **Definition:** Translating experience into action, often without formal analysis.
- **Origins:** Firefighters, military, police — high-pressure environments.
- **Premise:** Intuition is a skill → can be built, applied, safeguarded.

**Advantages**
- Very fast, based on pattern recognition.
- Allows action under uncertainty and time pressure.

**Risks**
- Over-reliance on familiar patterns → blind spots.
- Experienced people can still make fatal mistakes (“Deep Survival” – Gonzales).
- Low risk ≠ no risk.

**Barriers**
- Rigid policies, remote/distributed teams, turnover, constant change.
- Procedures, metrics-driven culture, IT constraints.

---

### Theory of Thin Slicing

(*Source: Malcolm Gladwell, Blink*)

- **Definition:** Ability to make accurate judgments based on very small “slices” of information.

**Examples**
- **John Gottman’s Love Lab:** Predicting relationship success by coding emotional signals (SPAFF).
- **Military interceptors:** Interpreting Morse code patterns.
- **Medical research (Levinson, Ambadi):** Malpractice risk depends on *tone* and *empathy*, not just content.

**Key Point:**  
Thin slicing is part of human cognition, not a rare talent.

---

### Time and Decision Making

(*Source: Gary Klein*)

**Chess Experiment**
- Blitz vs. regular → skilled players made similar % of good moves.

**Observations**
- Skilled decision makers can make good choices even under pressure.
- Often their *first considered action* is already a good one.

---

### Group Decision Making

(*Source: Marlene K. Rebori*)

**Common outcomes in groups:**
- No decision (paralysis)
- Self-appointed decision maker
- Minority rule
- Majority rule
- Consensus

**How to choose method?**
- Based on timeliness, appropriateness, relationships.

**Problems in group decisions**
- Deciding too soon (rushing).
- Analysis paralysis (stalling).
- No clear criteria.
- Poor listening → debate instead of dialogue.
- Perceptions of unfairness.
- **Groupthink** — conformity pressure inside a cohesive group suppresses dissent, so alternatives
  are never voiced and the group converges early on a poor option. Named by Irving Janis (1972)
  from case studies of foreign-policy fiascos.
- **The Abilene paradox** — a group unanimously agrees on a course of action that *no individual
  member privately favours*, each mistakenly believing the others want it. Described by Jerry B.
  Harvey (1974). It is not conformity to a majority; it is agreement in the absence of one.

{: .warning }
**Two different phenomena, and we hold neither primary source.** These were previously a single
bullet — "Groupthink / *Abilene Paradox* (agreement without real support)" — which is wrong twice
over: groupthink is dissent suppressed by pressure, the Abilene paradox is dissent that nobody
realises exists. Janis 1972 and Harvey 1974 are **not in this handbook's bibliography and have not
been read for this page**, so they are named and dated here and not cited. Both are useful
vocabulary from social psychology. Neither has software-engineering evidence behind it — see
below.

---

## What is actually known about bias in software engineering

The systematic mapping study by Mohanani and colleagues {% cite mohanani2018biases %} is the best
answer available to "how much of this is established?", and the answer is unflattering to the list
above. Across **65 primary studies** published 1990–2016 it identifies **37 distinct cognitive
biases** — and they are very unevenly studied:

| | |
|---|---|
| Anchoring and adjustment | **26** studies |
| Confirmation bias | **23** studies |
| Overconfidence | **16** studies |
| Biases resting on only one or two studies each | **21 of the 37** |
| The **`Social`** category — biases where social relationships undermine judgment | **2 studies**, covering **one** bias |
| Biases with any proposed debiasing technique | **6 of 37**, and **none empirically evaluated** |

Two consequences for this page:

1. **The group pathologies above are the thinnest-evidenced part of the topic.** `Social` is the
   least-studied category of all. **Groupthink is not among the 37 biases mapped** — it appears in
   that paper only as the *target* of an unvalidated proposed remedy (designating a devil's
   advocate) — and **the Abilene paradox does not appear at all.**
2. **The best-evidenced biases are individual, and they land on estimation.** Anchoring,
   confirmation and overconfidence are all failures of judgment about *numbers and evidence*, which
   is where the [Scope](../../scope/) and [Planning](../../plan/) blocks of this handbook pick them
   up. A decision-making section that stops at group dynamics misses the part of the literature
   that has actually been measured.

{: .note }
**What this does not license.** The mapping study maps research, not projects: 30 of its 65 studies
are controlled experiments, and the authors write that "demonstrating a bias in a lab is not the
same as establishing a significant effect on real projects." Nor does it supply a fix — six of
thirty-seven biases have any proposed technique, none of them tested, and the authors warn that
debiasing "may have unintended consequences". Its own inter-rater agreement on which category a
bias belongs to was **55%**. Treat the counts as a map of where the evidence is, not as a ranking
of what will go wrong on your project.

---

## Deciding alongside an AI

The failures above run human-to-human. The same question — *when should I take the advice?* — now
runs human-to-model, and it has been measured. The results point in **opposite directions**, and
that is the finding.

| Study | What was measured | Result |
|---|---|---|
| Puppart & Aru {% cite puppart2025overreliance %} | Adoption of **incorrect** ChatGPT recommendations. **n = 36 twelfth-grade Estonian school students**, math puzzles, **unreviewed preprint** | **Over-reliance: 52.1%** (SD 28.90) — bad advice taken just over half the time. A short AI-literacy intervention **did not reduce it**, and significantly *increased* rejection of correct advice (t(34) = 2.35, p = .025, d = 0.78) |
| Schemmer et al. {% cite schemmer2022reliance %} | Whether people **rightly change their mind** when the AI is correct (RAIR) and **rightly hold their ground** when it is wrong (RSR). 200 participants, deceptive-review classification, CHI '22 workshop paper | **Under-reliance: RAIR 0.30 — below chance.** Correct advice was ignored. RSR was 0.72. Adding explanations raised RAIR to 0.39 (p = .05) without inducing over-reliance |

**The lesson is miscalibration in both directions, not "people trust AI too much."** One study
found bad advice accepted; the other found good advice refused. Getting this backwards licenses
exactly the wrong intervention — and the intervention the second-guessing instinct reaches for
first, a short explanatory lesson about the tool, is the one that was tested and failed.

So the management question is not *"does the team trust the AI?"* Trust is an attitude; reliance is
a behaviour, and it is the behaviour that costs money. The useful question is whether people can
**tell good advice from bad and act on the difference** — two separate abilities, which can fail
independently and in opposite directions, and which a rise in overall team performance can hide
entirely {% cite schemmer2022reliance %}.

{: .warning }
**Carry the populations with the numbers.** The 52.1% figure comes from **36 school students
solving math puzzles in a preprint that has not been peer-reviewed** — not from software
engineers, not from code, not from a team under a deadline. It licenses a *direction*: a short
literacy intervention is a weak instrument against miscalibration. It is not an effect size for
professional developers. Schemmer's study is a **workshop** paper with a single illustrative
experiment, and its metric is defined only for classification tasks.

---

## Named on this page but not in our bibliography

These works are the acknowledged origin of sections above. **None of them has been obtained or
read for this page**, so they are named and dated here rather than cited, and no claim on this
page rests on a page number from any of them:

- **Rogers, P. & Blenko, M.** *Who Has the D? How Clear Decision Roles Enhance Organizational
  Performance*, and Blenko, Mankins & Rogers, *The Decision-Driven Organization* — *Harvard
  Business Review* — the "Influencing Factors" section.
- **Klein, G.** *Sources of Power* (MIT Press, 1998) and *The Power of Intuition* (2003) — the RPD
  material. The lecture slide the section derives from cites "Klein p. 16" without naming which.
- **Gladwell, M.** *Blink* (Little, Brown, 2005), and the Ambady & Rosenthal thin-slicing studies
  it popularises — the thin-slicing section. Gladwell is a secondary source throughout; the
  underlying studies have not been checked here.
- **Gonzales, L.** *Deep Survival* (W. W. Norton, 2003) — the "experienced people still have
  accidents" caution.
- **Rebori, M. K.** — the group decision-method list.
- **Janis, I.** *Victims of Groupthink* (1972) and **Harvey, J. B.**, "The Abilene Paradox" (1974)
  — see the warning above.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and
**David Root** {% cite root2014lectures %} on software project management. The structure,
examples, and pedagogical approach reflect their teaching materials and frameworks.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.