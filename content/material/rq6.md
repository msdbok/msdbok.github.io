---
parent: Revision Questions
title: RQ6
nav_order: 6
page_type: question-set
layout: default
---

# RQ 6 — Tracking

Covers both Tracking lectures. **L6a**, release planning: releases and iterations, choosing what
goes in, Buffered MoSCoW, running the time box, contracts and incentives, and when two estimates are
not enough. **L6b**, tracking, reporting and controlling: measuring progress, getting the bad news,
earned value, reading agile charts, choosing and controlling, and reporting answer first. Summaries
at [SN L6a](sn6a.html) and [SN L6b](sn6b.html); the detail is in the
[Release planning](../plan/release/) and [Tracking](../track/) areas.

Answer each in a short paragraph: state your claim first, then the reasoning or the evidence, then a
concrete software example where one is asked for.

---

## 1. Lecture Questions — L6a

### 1.1 Releases and iterations

1. Compare a release and an iteration. Who receives each, and what does planning decide for each?
2. Every sprint ends potentially shippable, yet the team may not ship it. Who decides how often to release, and on what grounds?
3. Why does a fixed-date plan answer with a range (will have, might have, won't have) instead of one feature list? What does McConnell mean when he says a time box's end date "is not a due date"?
4. Why commit to the next release but only sketch the ones after it? Take two of the four forces that release planning balances and give a software example of each.
5. Why pick a release strategy before picking features? Why does a backlog still need a reason for its order in an agile project?
6. The same work in four quarterly releases gave a gain where one yearly release gave a loss. Explain why without calculating.

### 1.2 Choosing what goes in

1. Why is release planning a knapsack problem with dependencies? What makes it harder than filling one bag?
2. In one cost–value study, dropping three of fourteen requirements kept almost all the value. What does this say about treating requirements as roughly equal?
3. Each planning method optimises a different goal. Pick two methods and describe a project that suits each. Why should a person, not the computer, choose the final plan?
4. DSDM tests a Must by asking whether you would stop the deployment without it. Why is this a better test than "is it important"? Give a Must and a Should for an app you know.
5. Why does DSDM cap the Musts at about 60% of the effort? When may a team go above it?

### 1.3 Buffered MoSCoW

1. Compare the DSDM meaning of a Must with the Buffered MoSCoW meaning. Who decides the order of the features, and what decides where the line falls?
2. Why plan the Musts at their safe estimates but run them at their normal ones? Where does the Must buffer come from?
3. How are the Shoulds chosen? Why is their budget the Must buffer, and not whatever capacity is left?
4. Why does each category down roughly halve the chance of delivery? What should you tell the sponsor instead of fixed percentages?
5. Why does it help to keep the Musts near 60% and to split big features into small ones?

### 1.4 Running the time box

1. A Must overruns. Why does this cost the Could and not the date? Why does nobody need to renegotiate?
2. After a demo the customer reorders the priorities. When does the change enter, who decides, and what gives? Why does reprioritising never move the date?
3. Why treat infrastructure as a feature that other features depend on? Give a software example.
4. How should critical, major and minor defects be handled inside a time box? Why does the customer choose between fixes and new features?
5. Compare committing once for the whole project with committing once per increment. Why can a Could missed in release 1 become a Must in release 2?

### 1.5 Contracts and incentives

1. Compare fixed-price, time-and-materials and incentive contracts. Who carries the risk of partial delivery in each?
2. Why price a contract on its expected outcome and not on its best case? Explain without calculating.
3. Why is there no bonus for delivering the Musts? Why is an unlikely reward a lottery rather than an incentive?
4. How do Parkinson's Law and the student syndrome waste unused buffer? How can rewards for the Should and Could releases make the team hand that time on?

### 1.6 When two estimates are not enough

1. Why do shared causes make features overrun together? What does this do to the protection a buffer gives?
2. When is Buffered MoSCoW enough, and when do you need SPID? What does SPID ask for that Buffered MoSCoW does not?

---

## 2. Lecture Questions — L6b

### 2.1 Measuring progress

1. Python counted lines of design code, an objective measure, and still stalled at 73% on its deadline. Why does an objective count not prevent the 90% syndrome?
2. Compare asking a developer for percent complete with calculating it from finished tasks. Why never accept the first? Give a calculated measure for a software release.
3. Why does a milestone trend chart show a slip earlier than a list of current forecasts? Why must its milestones be binary?

### 2.2 Getting the bad news

1. Why does good news travel up a hierarchy faster than bad news, even when nobody lies?
2. People keep quiet mostly for fear of being labelled, and a quarter think speaking up futile. Which of these can a manager change, and how?
3. Why do a manager who never acts and one who acts on every report both stop getting honest reports?

### 2.3 Earned value

1. Why does comparing planned value with actual cost say nothing about progress?
2. CPI is above 1 and SPI below 1. What do you expect next month, and what do you check first? Explain without calculating.
3. Why can SPI mislead mid-project, and why does it reach 1.0 at the end of every late project?
4. Compare the 0/100 earning rule with self-reported percent complete. Which cause of the 90% syndrome does 0/100 remove, and which does it leave?

### 2.4 Reading agile charts

1. Compare the sprint and release burndowns. Who reads each, and what question does each answer?
2. Why does a flat release burndown have two possible causes that need opposite responses? How does a burn-up tell them apart?
3. Why does velocity forecast well and judge badly? What happens when it becomes a target?

### 2.5 Choosing and controlling

1. Compare how earned value and a burndown chart answer "are we on schedule?" What does earned value see that the burndown cannot, and why does budget ownership decide whether that matters?
2. Why set variance thresholds before the first report, and why should crossing one start an analysis rather than an action?
3. Why does overtime buy a week now and rework later? Why does Wysocki's ladder ask the customer for more time last?
4. Why did nobody stop CONFIG? What would a stop rule written at the start have measured?

### 2.6 Reporting: answer first

1. In Snow and Keil's model, halving the perception error barely changes how often Red is reported Green. Why does this put the responsibility on the reader of reports?
2. Why does defining Red as "help needed" make it easier to report? Why one light per dimension, and never an average across projects?
3. Why should a status report open with its colour and the decision needed, not the period's chronicle? When is chronological order right?

---

## 3. Reading Questions

Cite the reading you used, with a page number where you have one.

### 3.1 Miranda, "Time Boxing Planning: Buffered MoSCoW Rules" (2011)

*ACM SIGSOFT Software Engineering Notes* 36(6), 1–5 {% cite miranda_time_2011 %}.

1. Miranda says a time box without agreed partial outcomes and justified certainty is "an expression of good will". Which of his three conditions for a working time box does plain MoSCoW fail to provide, and why does that matter to a sponsor?
2. Miranda calls classic MoSCoW "either unconstrained or arbitrarily constrained". Explain both problems. What constraint does his method add?
3. In his method a feature's category is "not an a priori decision". What decides it, and what does the customer still decide?
4. Why does Miranda refuse to call his two estimates the 50% and the 90% estimates? What would such numbers require?
5. In the paper's execution example, one Must feature takes its worst case. What happens to the Should and the Could features, and why does the date hold?
6. How does the paper handle a change request, and how does it handle defects? What does each choice cost the customer?
7. Miranda argues that a business is better off knowing what it can realistically expect than being "promised the moon". What must a contract accept for this to work, and why would a contract that puts all the risk on one party fail?
8. Miranda says the method's simplicity "is not free". What does it cost, and when should a planner use a more detailed approach such as SPID?

### 3.2 Humphreys & Associates, "Basic Concepts of Earned Value Management (EVM)" (2012)

EVMS Education Center primer, Humphreys & Associates, 7 pp. {% cite humphreys__associates_basic_2012 %}.

1. The primer says budget against actual cost "lacks an adequate indicator of progress". What is missing, and how does earned value supply it?
2. Why choose each task's earning rule (milestones, 50/50, 0/100 or percent complete) before the work starts? Which resists the 90% syndrome least?
3. The primer lists benefits and no limits. How should that shape the way you use it as a source?

### 3.3 Lukas, "Earned Value Analysis – Why it Doesn't Work" (2008)

*2008 AACE International Transactions*, paper EVM.01 {% cite lukas_earned_2008 %}.

1. Despite its title, Lukas argues for earned value. What does he blame when it fails?
2. In his Figure 2 a spending report shows the project under budget, while earned value shows it in trouble. Why do the two readings disagree? Explain without calculating.
3. Why does "a SPI > 1.0 does not necessarily mean you are ahead of schedule"? What must you check instead?

### 3.4 Barton, Schwaber & Rawsthorne, "Reporting Scrum Project Progress to Executive Management through Metrics" (2005)

Unpublished white paper summarising a Scrum Gathering, January 2005 {% cite barton_reporting_nodate %}.

1. Their burn-up plots business value earned against planned, not work done against total scope. What can it show that cost-based earned value cannot, and why can it not tell scope growth from slow work?
2. Why can value earned run ahead of work burned when the most valuable features are built first?
3. Why should an executive distrust a report that never shows "negative progress compared to a previous report"?

### 3.5 Hoffman, "The Darker Side of Metrics" (2000)

Pacific Northwest Software Quality Conference (PNSQC) 2000 {% cite hoffman2000metrics %}.

1. Using his defect find/fix ratio, explain how a team can improve the number without improving the product.
2. Twenty-five defect reports were marked as duplicates of one new defect to cut the count. Which L6b tracking measure could be bent the same way, and how would you notice?
3. His examples are altered consulting cases, and he tests no remedy. What can such evidence show, and what not?

### 3.6 Milliken, Morrison & Hewlin, "An Exploratory Study of Employee Silence" (2003)

*Journal of Management Studies* 40(6), 1453–1476 {% cite milliken_exploratory_2003 %}.

1. Why does it matter to a manager that people fear "being viewed or labeled negatively" more than punishment?
2. The issues withheld most were someone's competence and broken processes. Why are these what a project manager most needs to hear?
3. Many silent respondents said colleagues knew and also kept quiet. What does this say about how silence is learned?

### 3.7 Kasunic, "A Data Specification for Software Project Performance Measures" (2008)

Technical Report CMU/SEI-2008-TR-012, Software Engineering Institute, Carnegie Mellon University {% cite kasunic_data_2008 %}.

1. Kasunic defines six measures for completed projects and none of progress. Why can none answer "where is the project now?"
2. Why must project effort include "compensated and uncompensated overtime"? What goes wrong in the next estimate if it does not?
3. Why measure schedule slip against the baselined plan rather than the latest re-plan, and report it next to the requirements delivered?

---

### Acknowledgments

These questions build on lectures by Eduardo Miranda and David Root
{% cite miranda_managing_2014 root2014lectures %} on release planning and on tracking, reporting and
controlling. The MoSCoW categories come from the DSDM Agile Project Framework.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
