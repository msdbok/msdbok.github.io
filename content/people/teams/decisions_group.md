---
parent: Teams
title: Group Decisions
nav_order: 9
layout: default
---

# Group Decisions

A decision style is the rule a team agrees *in advance* for how a choice gets settled: majority, consensus, or something worse nobody chose.

## 1. Five styles, two of them choices

Groups often cannot tell **when a decision was made**: "I don't recall us making an actual decision on that" {% cite rebori1998decisionstyles %}. Of Rebori's five styles **three are failure modes** — "common situations that many boards may fall into", not recommended procedures — never teach the five as parallel options.

- **No decision.** Topic-jumping, and **"the plop"** — a proposal met with no response. Avoiding a decision is still a decision.
- **Self-appointed decision maker.** One member states a decision, nobody objects, and so decides for everyone: fast, but one view not the group's.
- **Minority rule.** Three or four agree while the rest stay silent, usually with no vote, leaving them "the impression their opinion does not count."

**Two are styles you can adopt.** **Majority rule** takes at least 51% after brief discussion: quick, but on complex or high-stake decisions it is competitive and "often produces a win/lose solution". **Consensus** means every member supports it — not compromise, not unanimity, but mutual agreement; slow and difficult, yet it builds empowerment, cohesion, relationships and accountability. Groups also fail by rushing, poor listening, and seeming unfair.

## 2. Majority or consensus?

Three criteria apply, only here: **timeliness** — one meeting forces the quickest workable method; **appropriateness** — lunch needs no consensus, an architecture does; **relationship** — where a style could imperil working relationships, lean collective.

## 3. Techniques

To soften a majority: a **70/30 vote** needs 70% rather than 51% — unreachable without talking, so it "borrows from consensus"; a **blind vote** is a secret ballot, anonymity reducing divisiveness; a **devil's advocate** argues every opposite possibility, against [groupthink](decisions_groupthink.html).

The most reusable consensus tool is the **five levels**, each member rating their position: **1** easily accept · **2** accept, not my preference · **3** accept with minor changes · **4** accept the group, though I disagree · **5** cannot accept. Anyone at 5 means no consensus; 4 or better all round means it is reached. Agree it beforehand: it turns "does everyone agree?", which invites silence, into an answerable question. A **consensus log** records what was agreed; **distilling concerns** writes every concern up visibly and groups similar ones; a **straw man** is drafted *to be attacked* — taking it apart and rebuilding produces ownership.

## 4. Seven steps, in order

Rebori's seven {% cite rebori1997problemsolving %}: **define the problem** as current facts plus a desired objective, implying no solution or cause; **identify root causes**, not symptoms, brainstormed under ground rules (no criticism · quantity · wild ideas · build on others'); **generate alternatives** without evaluating: doing both at once "reduces the number of potentially viable solutions"; **evaluate** against criteria established *first*, objective and preferably measurable; **agree the best solution** by a rule fixed beforehand; **plan the action** with goal, strategy, timeframe, owner and outcome; **implement and evaluate**, status on a standing agenda.

Two steps carry the rest. Criteria fixed before scoring are the remedy for deciding without them: criteria invented while looking at candidates describe the favourite. And step 7 exists at all: Rebori calls evaluation "probably the step most groups underemphasize", for political not procedural reasons — "time, cost, political climate, uneasiness in evaluation, and fear of being challenged in their decided upon solution." A team that never reaches step 7 cannot tell a good decision from a lucky one — the reason this topic ends by judging the process, not the outcome (see [Cognitive bias](decisions_bias.html)).

## 5. Evaluation tools

Options can be scored with a **T-chart**, **SWOT**, **Pareto analysis**, **pair-wise comparison** or **cost-benefit analysis**. Two more: a **fishbone diagram** structures root-cause discussion by repeatedly asking "what is a potential cause of…?", best when you know which area is failing but not which part; **dot voting** gives each member 3–5 dots to spread across the options: fast, active, agreement visible {% cite rebori1997problemsolving %}.

**Example.** A team sorts a quarter's bug reports by user-reported incidents, finds a handful of defects behind most complaints, and pair-codes those with regression tests.

## How solid is this?

- **Practitioner guidance, not evidence.** Both Rebori fact sheets are four-page extension leaflets with no study, data or peer review, written for community boards, not engineering teams. The 51% and 70% thresholds are conventions, and Rebori is candid that matrices and dot votes are not "formulas that will automatically produce correct answers."
- **The devil's advocate is unvalidated.** One of six proposed debiasing techniques in software engineering, with **no empirical evaluation** — see [Cognitive bias](decisions_bias.html).
- **Pareto’s 80/20 is a heuristic.** "20% of bugs cause 80% of errors" says where to look first; measure the concentration in your own defect data. No figure is quoted above; none is held here.

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
