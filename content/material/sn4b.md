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
**Workopolis**, a job board with fifteen user stories for job seekers, recruiters and the site owner,
and the lecture estimates it four ways. Each section links to the handbook page carrying the detail and the sources.

## 1. Why estimates go wrong

A review of ten surveys puts the typical cost overrun between 30 and 40%; Standish's famous 89% is the
outlier {% cite molokken2003surveys eveleens2010chaos %}. So a 1,000-hour estimate means 1,300 to
1,400 hours expected: carry the difference, or say why you will beat the average.

Three numbers have three owners. The **estimate** is what you believe, the **target** is what they
want, the **commitment** is what you promise, the estimate plus contingency. The estimate feeds the
budget; it is not the budget {% cite miranda_managing_2014 %} {% cite grimstad2006babel %}.

An early estimate is a range. At the initial concept, the real effort can be anywhere from 0.25 to 4
times the most likely number, a spread of 16 to 1; after requirements it is still about ±50%, and it
narrows only as the work is done {% cite mcconnell_rapid_1996 %}. Give every estimate as a range, say
the phase, and name the milestone of the next one.

When the budget comes first, the estimate's job changes. *You are given 600 hours to build Workopolis
with Scrum*: call 600 the budget, estimate independently at six effective hours a day, and if the
estimate is bigger, cut stories in the product owner's order {% cite mcconnell_rapid_1996 %}. Section
6 answers the question.

{: .exam-tip }
> **Exam tip:** given a sponsor's number, first say which of the three it is. A deadline is a target.

→ [Estimates](../scope/estimates/) · [Estimation approaches](../scope/estimates/approaches)

## 2. The map of methods

Scope becomes size, size becomes effort, effort becomes schedule. The size is the box everything
hangs from: *"the most significant input to the COCOMO II model is Size"* {% cite usc2000cocomo %}.

Miranda groups estimation methods into six families {% cite miranda_managing_2014 %}, and each sits
somewhere on that chain:

| Family | The number comes from | Gives |
|---|---|---|
| Judgment | a person: alone, in a group, or comparing pairs | size in points, or hours |
| Engineering | a cost function built from what drives the work | effort |
| Counting | a weighted count of what the user gets | size |
| Industry norms | a published ratio | effort, from a size |
| Analogy | the nearest finished projects (10 to 12 of them) | effort |
| Parametric | a formula fitted to past projects | effort, from a size |

What separates them is the last step: *"the quantification step—that is, the final step that
transforms the input into the effort estimate"* {% cite jorgensen_software_2009 %}. A person takes
it, or a formula does.

→ [Estimates](../scope/estimates/) · [Estimation approaches](../scope/estimates/approaches)

## 3. Expert judgment

An expert works top-down, against finished projects, or bottom-up, summing the WBS activities. Across
seven teams, bottom-up was off by 23% and top-down by 45%; top-down did well only when the estimator
recalled a very similar project {% cite jorgensen2004topdown %}. Know a similar project? Go top-down.
If not, decompose.

Judgment has known biases. In one experiment, a single sentence from a manager who admitted having
no experience moved the mean estimate from 8.3 months to 17.4 with a 20-month anchor
{% cite aranda2005anchoring %}. So nobody, the sponsor included, says a number before the estimators
have written theirs.

Each bias has a fix that changes the input: a checklist against availability, a number-free brief
against anchoring, many past tasks against representativeness, an independent second estimate against
confirmation. All four feed overconfidence: professionals' 90% ranges held only 35% of the time
{% cite halkjelsvik2012origami %}.

→ [Expert judgment](../scope/estimates/expert)

## 4. Estimating as a group

**Planning Poker** gives each estimator a card to pick privately; all cards turn over together; if
they differ, the highest and lowest explain, and the team votes again. Grenning's deck is 1, 2, 3, 5, 7, 10 and ∞, where ∞ means
*split it*, and his purpose is plain: *"Precision of individual estimates is not the goal. Determining
the project scope is"* {% cite grenning2002poker %}. No averages, no numbers off the deck
{% cite rubin_essential_2012 %}.

**Eduardo's Variation**, this course's version, agrees a medium story as the baseline first,
discusses coincidences as well as differences, records every estimator's final card, and probes
unusual disagreement instead of averaging blindly {% cite miranda_managing_2014 %}.

A uniform-looking backlog is not. One senior developer sized all fifteen Workopolis stories; with *Search jobs* at 5, *Register* came out 14 times *Log out*, and the same expert gave *Register*
14.4 in one session and 13.0 in the next {% cite miranda2009sizing %}.

Poker removes the first speaker's anchor and brings in the quiet members, but not the first round's: *"We found no story having the final planning poker estimate outside these boundaries"*
{% cite mahnic2012poker %}. Matching cards end the talk even when the reasons differ, and on
unfamiliar stories Poker did worse than plain discussion {% cite haugen2006poker %}. If the talk
reveals new work, vote again from zero.

**Paired comparisons** ask only *how much bigger is X than Y?* and then check how consistent the
answers are {% cite miranda_improving_2001 %} {% cite miranda2009sizing %}. For an architecture item
unlike the rest of the backlog, compare it with an item of known size, or estimate it bottom-up.

**Story points** are easy to agree on, because people compare better than they measure, and hard to
compare: a point means something in one team against one reference, becomes a date only through
velocity, and inflates once velocity is rewarded {% cite rubin_essential_2012 %}. On ten Workopolis
stories, comparing each with all the others gave a project total of 44.6; comparing each with only
two gave 99.7 {% cite miranda2009sizing %}. Compare each story with at least four others. And 65
points is not a number of hours, and another team's 65 is a different 65. When the sponsor needs hours,
or a size an outsider can check, you need a different unit.

{: .exam-tip }
> **Exam tip:** "Poker prevents anchoring" is half right. It removes the first speaker's anchor; the
> first round's cards then fence the result.

→ [Planning Poker](../scope/estimates/poker) · [Paired comparison](../scope/estimates/pair)

## 5. Function points

Lines of code are a poor size for an estimate: they do not exist when the estimate is due, and they
differ for the same function in another language {% cite park1992size %}. **Function points** count what the user gets (inputs, outputs, inquiries and files), from the requirements, and
the same screens score the same in C++ or in Clarion {% cite longstreet2002fpa %}.

Two questions classify every transaction. Does it change a stored file? Then it is an external input
(EI) {% cite longstreet2002fpa %}. If not, does it derive data? Then an external output (EO); otherwise an
external inquiry (EQ). For files, count kinds of subgroup, never records: a department holding 20
employees has two record types {% cite gunti_function_nodate %}.

**Example: Workopolis, counted.** User stories carry no field lists, so every item is rated Average (the
count is constructed for the course; the stories are Miranda, Bourque & Abran's
{% cite miranda2009sizing %}):

| Type | Workopolis | n × weight | FP |
|---|---|---|--:|
| ILF, kept | job seeker (profile and resume as two record types), career alert, job announcement | 3 × 10 | 30 |
| EIF, only read | recruiter accounts: no story creates or changes them | 1 × 7 | 7 |
| EI | register; upload, delete resume; create, suspend, delete alert; post, edit, delete job | 9 × 4 | 36 |
| EQ | search jobs; two log-ins | 3 × 4 | 12 |
| EO | notify job seekers: an e-mail with the count of matches | 1 × 5 | 5 |
| | log-outs move no data: not counted | | **90** |

The choices move the count a little: alerts folded into the job seeker give 80, Notify without a count (EQ) 89, recruiters as a kept file 93. Write
each choice down.

**From size to hours, with your own rate.** At an example company's 8 to 12 FP per person-month,
90 FP is 7.5 to 11.3 person-months, or **1,200 to 1,800 hours** at 160 hours a month. Say what the
rate covers: here requirements to acceptance, management included, but not deployment, training or
support. Read backwards, the sponsor's 600 hours buys 30 to 45 FP, a third to a half of Workopolis.

**A second route: COCOMO II.** Effort is *PM = A × Size^E × ΠEM*, with A = 2.94 fitted to 161
projects {% cite usc2000cocomo %}. COCOMO wants lines of code, so it converts function points per
language: 53 lines per point in Java, so 90 FP is 4.8 KSLOC. With every driver nominal, E = 1.10 and
the effort is 2.94 × 4.8<sup>1.10</sup> ≈ **16 person-months, about 2,500 hours**. E above one means
twice the system is more than twice the work. Uncalibrated, the model applies other projects'
productivity to yours; recalibrate A on five of your own before quoting it {% cite usc2000cocomo %}.

The count is reliable; an estimate from it is not. Two trained counters differ by a median of 12%
{% cite kemerer1993fp %}, while Albrecht's formula from function points to effort typically missed one
project by about 85% {% cite albrecht1983fpa %}. Quote the effort as a range.

→ [Function Point Analysis](../scope/estimates/fpa) · [FPA explained](../scope/estimates/fpa_explained) · [COCOMO](../scope/estimates/cocomo) · [Workopolis, rated in full](workopolis_fp)

## 6. Combining methods

In the 2009 debate, Jørgensen argued that an expert uses what no model takes in, and Boehm that a
model *"doesn't modify its estimates when customers, managers, or marketers apply pressure"*
{% cite jorgensen_software_2009 %}. Across fifteen studies the score was five, five and five
{% cite jorgensen2004expert %}. Use a calibrated model to check the expert, not to replace them.

Rules of thumb are checks, not estimates. Capers Jones's rules turn function points into schedule
(FP<sup>0.4</sup> months), team size (FP ÷ 150) and defects (FP<sup>1.25</sup>), and he warns that
they *"should not be used for contracts, bids, or other serious business purposes"*
{% cite jones1996rules %}. On Workopolis: 90<sup>0.4</sup> ≈ 6 months × 90 ÷ 150 ≈ 0.6 people, about
3.6 staff months or 580 hours. Before trusting a norm, ask which hours and activities it counts.

Combine independent estimates, then read the spread. On one real project, individuals averaged 1,088
hours, mixed groups 1,548, and the project took 2,365 {% cite molokken2004group %}. A wide spread usually means the scope was misread or the
productivity data is wrong {% cite pressman2010estimation %}. With little history: two or three people
estimate alone, top-down from a norm and bottom-up over the WBS, check with a model or a rule, report a
range, and start recording actuals.

**Workopolis, side by side.** Planning Poker: 65 points, no hours until the team has a velocity.
Jones's rules: about 580 hours. Function points at the team's own rate: 1,200 to 1,800 hours. COCOMO,
nominal and uncalibrated: about 2,500 hours. A fourfold spread is a diagnosis, not something to
average: the norm counts less work, the model carries other people's productivity. Build the estimate
on your own history and use the others as its fences. The 600 hours is what a rule of thumb gives,
so the honest options are to commit the range or to cut to the stories worth 30 to 45 FP.

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

**3. What does Planning Poker fix, and what does it leave unfixed?**

<details markdown="1"><summary>Answer</summary>

Private cards remove the first speaker's anchor and bring in the quiet members. The first round still
fences the final estimate {% cite mahnic2012poker %}, and matching cards end the discussion even when
the reasons differ, which Eduardo's Variation targets by discussing coincidences
{% cite miranda_managing_2014 %}.

</details>

**4. Workopolis came out at 580, 1,200–1,800 and 2,500 hours by three methods. Which do you report, and why not the average?**

<details markdown="1"><summary>Answer</summary>

The 1,200–1,800 range, because it rests on the team's own delivery rate. The spread says the methods
count different things: Jones's norm an unstated set of activities, COCOMO other organisations'
productivity until it is calibrated {% cite usc2000cocomo %}. Averaging hides that diagnosis
{% cite pressman2010estimation %}.

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
