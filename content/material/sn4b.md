---
parent: Study Notes
title: SN L4b — Estimation
nav_order: 10
page_type: study-notes
layout: default
---

# SN L4b — Estimation

A revision summary of the second Scope lecture. An **estimate** is *"the information we use to
evaluate the cost of a future decision"* {% cite hoover_evaluating_2010 %}, so every number in the
lecture answers two questions: **how much, and how sure are you?** The running example is
**Workopolis**, a job board with fifteen user stories for job seekers, recruiters and the site owner.
Each section links to the handbook page carrying the detail and the sources.

## 1. Why estimates go wrong

A review of ten surveys puts the typical cost overrun between 30 and 40%; Standish's famous 89% is the
outlier {% cite molokken2003surveys eveleens2010chaos %}. So a 1,000-hour estimate means 1,300 to
1,400 hours expected: carry the difference, or say why you will beat the average. And before
believing any overrun figure, ask what it was measured against {% cite grimstad2006babel %}.

Three numbers have three owners. The **estimate** is what you believe, the **target** is what they
want, the **commitment** is what you promise, the estimate plus contingency. The estimate feeds the
budget; it is not the budget {% cite miranda_managing_2014 %}. *"Do not mix estimation of most likely
effort with planning, budgeting or pricing"* {% cite grimstad2006babel %}.

An early estimate is a range. At the initial concept, the real effort can be anywhere from 0.25 to 4
times the most likely number, a spread of 16 to 1; after requirements it is still about ±50%, and it
narrows only as the work is done {% cite mcconnell_rapid_1996 %}. Give every estimate as a range, say
the phase, and name the milestone of the next one.

When the budget comes first, the estimate's job changes. *You are given 600 hours to build Workopolis
with Scrum*: call 600 the budget, estimate independently at six effective hours a day, and if the
estimate is bigger, cut stories in the product owner's order. You can *"negotiate the inputs to the
estimate … but not the estimate itself"* {% cite mcconnell_rapid_1996 %}.

{: .exam-tip }
> **Exam tip:** given a sponsor's number, first say which of the three it is. A deadline is a target.

→ [Estimates](../scope/estimates/) · [Estimation approaches](../scope/estimates/approaches)

## 2. Sizing the product

Scope becomes size, size becomes effort, effort becomes schedule. The size is the box everything
hangs from: *"the most significant input to the COCOMO II model is Size"* {% cite usc2000cocomo %}.

Lines of code are a poor size for an estimate. They do not exist when the estimate is due, they
differ for the same function in another language, and even after the fact a report of *"163,000
source code instructions"* can be misread by a factor of three {% cite park1992size %}. **Function
points** count what the user gets (inputs, outputs, inquiries and files), from the requirements, and
the same screens score the same in C++ or in Clarion {% cite longstreet2002fpa %}.

Two questions classify every transaction. Does it change a stored file? Then it is an external input
(EI): *"The only component that maintains an internal logical file is an external input"*
{% cite longstreet2002fpa %}. If not,
does it derive data? Then an external output (EO); otherwise an external inquiry (EQ). For example,
on Workopolis *Upload a resume* writes a file, so it is an EI; *Search job announcements* only
retrieves, so it is an EQ. For files, count kinds of subgroup, never records: a department holding 20
employees has two record types {% cite gunti_function_nodate %}.

The count is reliable; an estimate from it is not. Two trained counters of the same system differ by
a median of 12% {% cite kemerer1993fp %}. Albrecht's line from function points to effort fits 24 IBM
projects closely, yet its typical error on one project is about 85%, and he advised that such
formula estimates *"be used only to validate and provide perspective on primary estimates"*
{% cite albrecht1983fpa %}.

→ [Function Point Analysis](../scope/estimates/fpa) · [FPA explained](../scope/estimates/fpa_explained)

## 3. Expert judgment

Miranda groups estimation methods into six families: judgment, engineering (a cost function built
from what drives the work), counting, industry norms, analogy and parametric models
{% cite miranda_managing_2014 %}. What separates them is the last step: *"the quantification
step—that is, the final step that transforms the input into the effort estimate"*
{% cite jorgensen_software_2009 %}. A person takes it, or a formula does.

An expert works top-down, against finished projects, or bottom-up, summing the WBS activities. Across
seven teams, bottom-up was off by 23% and top-down by 45%, but the two top-down
teams that recalled a very similar project with known effort were among the most accurate, at 12%:
*"the recall of very similar previously completed projects seemed to be a pre-condition for accurate
top-down strategy based estimates"* {% cite jorgensen2004topdown %}. Know a similar project? Go
top-down. If not, decompose.

Judgment has known biases. In one experiment, 23 people read the same brief, with one sentence from a
client's manager: *"I admit I have no experience with software projects, but I guess this will take
about 2 months to finish."* With a 20-month anchor the mean estimate was 17.4 months, with none 8.3,
with 2 months 6.8 {% cite aranda2005anchoring %}. So nobody, the sponsor included, says a number
before the estimators have written theirs.

Each bias has a fix that changes the input. Availability: an activity checklist and searchable
history. Anchoring: strip numbers from the brief. Representativeness (*"it's just like the last
one"*): many past tasks, not the closest one. Confirmation: an independent second estimate. All four
feed overconfidence; professionals' 90% ranges held the actual only 35% of the time
{% cite halkjelsvik2012origami %}. Warning people does not remove a bias; changing what they see
does.

→ [Expert judgment](../scope/estimates/expert)

## 4. Estimating as a group

**Planning Poker** gives each estimator a card to pick privately; all cards turn over together; if
they differ, the highest and lowest explain, and the team votes again. With no consensus: *"Defer the
story, split it, or take the low estimate."* Grenning's deck is 1, 2, 3, 5, 7, 10 and ∞, where ∞ means
*split it*, and his purpose is plain: *"Precision of individual estimates is not the goal. Determining
the project scope is"* {% cite grenning2002poker %}. No averages, no numbers off the deck
{% cite rubin_essential_2012 %}.

**Eduardo's Variation**, this course's version, adds four rules {% cite miranda_managing_2014 %}:
agree a medium story as the baseline first; discuss coincidences too, since the same card can rest on
different reasons; play one more round and record every estimator's final card; and after all
stories, probe unusual disagreement rather than averaging blindly. The rules are untested course
practice.

A uniform-looking backlog is not. One senior developer sized all fifteen Workopolis stories; with *Search jobs* at 5, *Register* came out 14 times *Log out*, and the same expert gave *Register*
14.4 in one session and 13.0 in the next {% cite miranda2009sizing %}.

Poker removes the first speaker's anchor and brings in the quiet members, but not the first round's: *"We found no story having the final planning poker estimate outside these boundaries"*
{% cite mahnic2012poker %}. Matching cards end the talk even when the reasons differ, and on
unfamiliar stories Poker did worse than plain discussion {% cite haugen2006poker %}. If the talk
reveals new work, vote again from zero.

**Story points** are easy to agree on, because people compare better than they measure, and hard to
compare: a point means something in one team against one reference, becomes a date only through
velocity, and inflates once velocity is rewarded {% cite rubin_essential_2012 %}. On ten Workopolis
stories, comparing each with all the others gave a project total of 44.6; comparing each with only
two gave 99.7 {% cite miranda2009sizing %}. Compare each story with at least four others.

**Paired comparisons** ask only *how much bigger is X than Y?* and then check how consistent the
answers are {% cite miranda_improving_2001 %}. In one example, fixing a single bad judgment took the
inconsistency index from 0.94 to 0.27, under the acceptable 0.35 {% cite miranda2009sizing %}. For an
architecture item unlike the rest of the backlog, compare it with an item of known size, or estimate
it bottom-up.

{: .exam-tip }
> **Exam tip:** "Poker prevents anchoring" is half right. It removes the first speaker's anchor; the
> first round's cards then fence the result.

→ [Planning Poker](../scope/estimates/poker) · [Paired comparison](../scope/estimates/pair)

## 5. Parametric models

A parametric model is a regression of effort on size, of the form *E = A + B × size^C*, with the
constants fitted to somebody else's past projects {% cite pressman2010estimation %}.

**COCOMO II** fits A = 2.94 and B = 0.91 to 161 projects, with seventeen effort multipliers once the
architecture exists and seven before {% cite usc2000cocomo %}. Its exponent is usually above one:
*"If E > 1.0, the project exhibits diseconomies of scale"*, from growing communication and integration
overhead {% cite usc2000cocomo %}. Run it with its drivers: without them COCOMO landed within 1.3 times the actuals 29% of the
time, with them 78% {% cite jorgensen_software_2009 %}.

Three of the five scale factors are a manager's choice: architecture and risk resolution, team
cohesion and process maturity. The same 100 KSLOC product costs 194 person-months with every factor at
its best and 832 at its worst. Compressing the schedule to 75% of nominal costs 43% more effort,
while *"Stretch-outs do not add or decrease effort"*. And integration and test take 19% of the effort
on a small project but 31% on a large one {% cite usc2000cocomo %}.

Calibrate before you trust a model. On one CAD system from Pressman's textbook, the seven published
models his chapter lists give 42 to 323 person-months; *"Estimation models must be calibrated for
local needs!"* {% cite pressman2010estimation %}. Five of your own finished projects are enough to
refit the constant A {% cite usc2000cocomo %}; until then, a model is a cross-check.

→ [COCOMO](../scope/estimates/cocomo) · [COCOMO II drivers](../scope/estimates/cocomo_ii_drivers)

## 6. Combining methods

The 2009 debate sets the two sides out. Jørgensen: an expert can use what no model takes in, *"a
serious conflict between the project leader Peter and his best programmer Paul"*, and a model's inputs
are judgments anyway. Boehm: *"A major
advantage of a parametric model is that it doesn't modify its estimates when customers, managers, or
marketers apply pressure"* {% cite jorgensen_software_2009 %}. Across fifteen studies, five favoured
experts, five models and five found no difference {% cite jorgensen2004expert %}. Use a calibrated
model to check the expert, not to replace them.

Rules of thumb are checks, not estimates. Capers Jones's rules turn function points into schedule
(FP<sup>0.4</sup> months), team size (FP ÷ 150) and defects (FP<sup>1.25</sup>), and he warns that
they *"should not be used for contracts, bids, or other serious business purposes"*
{% cite jones1996rules %}. His article's rules and his book's table disagree by 2.4 times on the same
100,000 lines of C {% cite miranda_managing_2014 %}, so ask which hours and activities a norm counts.

Combine independent estimates, then read the spread. Twenty professionals estimating one real project
alone averaged 1,088 hours; in five mixed groups, 1,548; the project took 2,365, and one expert alone
had said 220. The groups *"sometimes even identified necessary activities that none of the individuals
had reported"* {% cite molokken2004group %}. A wide spread usually means the scope was misread or the
productivity data is wrong {% cite pressman2010estimation %}. With no history, as for L4a's invented
Quill: three people estimate alone, top-down from a norm and bottom-up over the WBS, check with a rule,
report a range, and start recording actuals.

→ [Estimation approaches](../scope/estimates/approaches) · [Expert judgment](../scope/estimates/expert)

## Practice questions

**1. Why should an estimator never hear the budget before estimating, and what should happen when the budget is fixed first?**

<details markdown="1"><summary>Answer</summary>

A budget is a target, and a number heard first anchors the estimate {% cite aranda2005anchoring %}.
Estimate independently,
then treat the gap as a scope decision for the product owner {% cite mcconnell_rapid_1996 %}.

</details>

**2. Why is a function-point count more trustworthy than an effort estimate made from it?**

<details markdown="1"><summary>Answer</summary>

Trained counters differ by a median of 12% {% cite kemerer1993fp %}. The step from size to effort
leaves out the team, the technology and hidden complexity, so on one project Albrecht's formula
typically missed by about 85% {% cite albrecht1983fpa %}.

</details>

**3. Compare top-down and bottom-up expert estimation. When would you choose each?**

<details markdown="1"><summary>Answer</summary>

Top-down works only when the estimator recalls a very similar project and its actual effort; bottom-up
forces an understanding of the work but loses whatever activity was forgotten
{% cite jorgensen2004topdown %}. Without a close analogue, decompose, and protect the sum with a
checklist.

</details>

**4. What does Planning Poker fix, and what does it leave unfixed?**

<details markdown="1"><summary>Answer</summary>

Private cards remove the first speaker's anchor and bring in the quiet members. The first round still
fences the final estimate {% cite mahnic2012poker %}, and matching cards end the discussion even when
the reasons differ, which Eduardo's Variation targets by discussing coincidences
{% cite miranda_managing_2014 %}.

</details>

**5. "Our team tried COCOMO and it was useless." What would you ask before agreeing?**

<details markdown="1"><summary>Answer</summary>

Was it calibrated on our own projects, and run with its cost drivers? Without drivers it landed within 1.3 times the actuals 29% of the time; with them, 78%
{% cite jorgensen_software_2009 %}. An uncalibrated model is a cross-check at best.

</details>

## Where this goes next

Workopolis has a range; the sponsor still wants a date. Do you commit to the whole scope up front,
or one sprint at a time? That is the next lecture.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David
Root** {% cite root2014lectures %} on software project management. The commitment-level planning
picture, the six families, the 600-hour exercise, the Workopolis stories and Eduardo's Variation of
Planning Poker are Miranda's {% cite miranda_managing_2014 %}.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
