---
parent: Study Notes
title: SN L3c — Risk Management
nav_order: 8
page_type: study-notes
layout: default
---

# SN L3c — Risk Management

A revision summary of the third Needs lecture. It follows the invented **Quill** project from the
requirements lecture, four months before release 1.0, with four worries on the team's whiteboard:
the 2-second target was only tested with 100-page documents; only one developer understands the
citation engine; the PDF engine vendor is late; the EU data-centre contract is unsigned. Six parts
take those worries through the loop: find, write, size, respond, track. Each section links to the
handbook page carrying the detail and the sources.

## 1. What risk management is

A risk is *"uncertainty that, if it occurs, will affect achievement of objectives"*
{% cite hillson2009risk %}. The second half does the work: a risk has to **threaten a named
objective**, and a worry that threatens none is news, not a risk. The threshold of success from the
expectations lecture is a second filter: a concern that would not break it is an event the project
can absorb.

<img src="/content/needs/risks/uncertainty-rings.svg" alt="Three nested rings: all uncertainty, the part that could affect an objective, and the part that would breach your threshold" style="max-width:100%; margin:1.5em 0;" />

**If there is no uncertainty left, it is an issue.** For example, halfway through a build somebody
notices the system stores personal data and nobody has done a GDPR assessment. The missing
assessment is certain, so it is an issue: resolve it. What the assessment will find is uncertain,
so there is also a risk: *if it finds a problem, the launch slips.* One situation, two entries, two
verbs: a risk is mitigated, an issue is resolved {% cite gluch1994risk %}.

Risks come in three degrees of knowing {% cite pressman2010risk %}. **Known**: somebody can name it
today, so write it down. **Predictable**: past projects saw it, so go and look. **Unpredictable**:
nobody can name it, and the only answer is a **reserve**. A project with no reserve has decided the
third category is empty, and it never is.

**Exposure is probability times impact** {% cite boehm1991risk %}. Quill's performance risk is 0.4
likely with three weeks of delay, so 1.2 weeks of exposure; the developer leaving is 0.2 likely
with six weeks, also 1.2. Exposure lets you compare risks that look nothing alike, and compare what
you could do about them: the right option is the one that leaves the least exposure **plus** its own
cost, which is why paying for an independent review can be the cheapest choice. The number is an
estimate, not a measurement; its job is to survive being argued with.

Risk is not bad; unmanaged risk is {% cite vanscoy1992risk %}. Five levels of maturity run from
crisis, through fixing and mitigating, to preventing and anticipating, and at the first three the
schedule battle is already lost. The SEI loop is the spine of the lecture: **identify, analyse,
plan, track, control**, with communication in the middle {% cite dorofee1996crm %}. Every
framework you will meet has this loop and differs only in its menu of responses.

→ [Risks](../needs/risks/)

## 2. Finding risks

Five techniques, chosen by where the knowledge is. **Write the threshold of success first**: when
will it be, what will it be, what makes it a success. A concern that would break it is a risk
{% cite hoover_evaluating_2010 %}. **Run a premortem**: declare the project failed, in the past
tense; write reasons privately for two minutes; read them round-robin; revise the plan. Dissent
becomes the assigned task, so it costs nothing to voice {% cite klein2007premortem %}. **Ask
taxonomy questions** when a team lists only product risks: the questions exist to make it ask about
its development environment and the constraints it does not control, and the cues under each
question turn *fine* into *we have not measured that* {% cite carr1993taxonomy %}. **Use a
checklist** for a fast first pass; Boehm's ten most common risks start with personnel shortfalls,
people before technology {% cite boehm1991risk %}. And **interview peers only**: in the SEI's field
study a reporting relationship in the room *always* inhibited the subordinates, so run groups of at
most five without a supervisor and give the manager an unattributed copy. Fewer than fifteen
statements from a session means it did not work, not that the project is safe.

Most of a project's risks are already known to somebody who is not in the meeting. Sessions
surprised management every time in fifteen field tests, so a long register is evidence of honest
identification, not of a failing project.

→ [Identification](../needs/risks/identification)

## 3. Writing a risk down

Start from a **condition you can check today**, then the **consequence** if nothing changes
{% cite gluch1994risk %}. *The 2-second target has only been tested with 100-page documents*, so
*acceptance fails on big documents and release 1.0 slips.* *Only one developer understands the
citation engine*, so *if she leaves, citations slip by six weeks.* Each condition is a fact in the
test log or the team list, not an opinion, and that is what separates a risk from a worry.

Condition-then-consequence, if–then and because–event–consequence carry the same elements; use the
first unless your team has a standard, and whichever you use, **the consequence carries a number
and a unit** {% cite williams1999sre %}. *Delays* is not a consequence; *three weeks* is, because
Part 4 is nothing but comparisons.

A register row holds the statement; probability, impact and exposure; **one named owner**; the
response; a **trigger and contingency**; and the status with its last change
{% cite nasa_nasa_2007 %}. Quill's row R-01 reads: statement as above; 0.4, 3 weeks, 1.2 weeks;
owner the tech lead; response *reduce: build a 500-page test set and run it this sprint*; trigger
*if the test shows more than 2 seconds on 1 November, switch to lazy page loading*; open. A row
without an owner is a worry. A row without a trigger is a plan that never starts.

Two well-formed statements are still useless {% cite thompson2017riskstatement %}. *If the publisher
changes the requirements, the schedule slips* points at a lever you do not hold; rewrite it towards
your own change process. *If we do not test with big documents, performance fails* is not a risk
but a decision not to do the work.

→ [Capturing, owning and mitigating](../needs/risks/capturing)

## 4. Deciding which risks matter

**Use scales with numbers, and write them down**: probability high above 70%, medium about 50%,
low below 30%; impact high at a schedule slip over 20% or cost over 25% {% cite root2014lectures %}.
Two people scoring the same row then land on the same band. Other organisations draw the lines
elsewhere, and a government standard calls a 10% overrun catastrophic
{% cite us_department_of_energy_software_2000 %}; the words never agree, the numbers beside them do.

Finding a hundred risks takes half an hour and analysing thirty takes an hour, so **vote first**:
each person gets a third of the count plus one votes, spends them anywhere, and the most-voted rows
are analysed first. Estimate probability **by convergence**, polling the team round-robin until the
estimate stops moving, never by the most senior person's announcement {% cite williams1999sre %}.

Then **sort by exposure and draw the line**. Roughly 80% of the exposure sits in 20% of the risks
{% cite pressman2010risk %}: compute, sort, draw, and write down what you will not do. Most of the
risks you found never get a plan, and that is the method working as long as the decision is
recorded.

<img src="/content/needs/risks/matrix-vs-el.svg" alt="A risk matrix against expected loss: the outcome the matrix paints red has the smallest expected loss" style="max-width:100%; margin:1.5em 0;" />

**A colour is not a number.** NASA says of its own matrix that it *"is not an assessment tool, but
can facilitate risk discussions"* {% cite nasa_nasa_2007 %}. In Cox's oil-well case the matrix
paints severe losses red and the rarer blowout yellow, while the blowout's expected loss is twice as
large {% cite cox2008matrices %}. Start the conversation with the matrix; settle the order with
exposure.

The distribution behind all this is fat-tailed. Across 5,392 IT projects half come in on budget or
better and the average is 80% over, because a few go catastrophically wrong
{% cite flyvbjerg2022overruns %}. Size the reserve for the tail, not the average, and fund the
components everything else depends on.

→ [Analysis and prioritisation](../needs/risks/analysis) · [Why we misjudge risk](../needs/risks/biases)

## 5. Responding and tracking

Every register row has one of **four responses** {% cite dod2023rio %}. **Avoid**: change the plan
so the risk cannot happen; load pages lazily, so document size stops mattering. **Reduce**: lower the
probability or the impact now; build the 500-page test set this sprint. **Transfer**: make someone
else carry it; a delivery date and a penalty in the vendor's contract. **Accept**: live with it and
watch; re-check the EU contract on the first of every month. Whatever you choose, write a
contingency with a trigger, and respond only if the response costs less than the exposure it
removes.

<img src="/content/needs/risks/response-matrix.svg" alt="A five by five matrix banded diagonally into prevent, prepare and monitor, with three example risks placed on it" style="max-width:100%; margin:1.5em 0;" />

Where a risk sits decides the **kind** of response: prevent the high band, prepare for the middle,
monitor the low band {% cite root2014lectures %}. The bands run diagonally because exposure is a
product. The band picks the kind; the exposure number picks the order.

Tracking has three instruments. A **top list with last week's rank beside this week's**
{% cite mcconnell_rapid_1996 %}: the *was* column is the meeting, reviewed weekly with the project
manager's boss present, and the trend of total exposure is what the sponsor sees. A **burn-down
plan** of dated actions, each with a test for done, because *"meetings do not burn down risks"*
{% cite dod2023rio %}; testing you were always going to do mitigates nothing. And a cost: **half a
day once**, identifying against the threshold of success, then **ten to fifteen minutes a sprint**,
with mitigations as real backlog items and triggers checked at the sprint boundary
{% cite nelson_explicit_2008 %}. One team with a risk manager and a spreadsheet mitigated nothing
for several sprints, because the work sat in the backlog as one generic task nobody could estimate.

→ [Risk management in agile](../needs/risks/agile)

## 6. The case: Comair, Christmas 2004

Comair's crew-scheduling system, built in 1986, had a hard ceiling of **32,000 trip transactions a
month**. A replacement was proposed in 1997 and rejected on good grounds, then deferred again and
again: Y2K, an acquisition, a strike, 9/11 {% cite dotoig2005comair %}. A storm before Christmas 2004
added more than 6,000 changes to a month already in progress, and on Christmas Eve the system
stopped: 89% of flights cancelled or delayed, about 269,000 passengers affected.

<img src="/content/needs/risks/comair-timeline.svg" alt="The Comair crew-scheduling failure, from the 1986 build to the December 2004 shutdown" style="max-width:100%; margin:1.5em 0;" />

Three lessons carry to any project. The storm was the **trigger**; the cause was a limit nobody
re-examined. The **probability rose every year** as the airline grew, with no decision taken, so a
register with one static probability column could not have shown it. And *we are already replacing
it* is a schedule, not a mitigation: the approved replacement was in testing when the outage came.

→ [Capturing, owning and mitigating](../needs/risks/capturing)

## Where this goes next

This closes the Needs block. The case session that follows asks for a threshold of success and a
register on a real case, where a risk is exactly what §2 said: a concern that would breach your own
threshold, written as a row with an owner and a trigger.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David
Root** {% cite root2014lectures %} on software project management. The structure, examples, and
pedagogical approach reflect their teaching materials and frameworks.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
