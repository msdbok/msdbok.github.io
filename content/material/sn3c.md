---
parent: Study Notes
title: SN L3c — Risk Management
nav_order: 8
page_type: study-notes
layout: default
---

# SN L3c — Risk Management

A revision summary of the third Needs lecture. Its one claim is that risk management is a **filter,
not a list**: any team can name forty things that might go wrong before lunch, and the discipline is
deciding which few deserve its time and what to do about each. Every technique below either gets a
risk onto the list or gets one off it again. Each section links to the handbook page carrying the
detail and the sources.

## 1. What a risk is, and what it is not

A risk is *"uncertainty that, if it occurs, will affect achievement of objectives"*
{% cite hillson2009risk %}. The useful half is the second: risk is the subset of uncertainty that
matters, and it matters only if you can **name the objective it threatens**. If you cannot, it may
be interesting, but it is not yours.

<img src="/content/needs/risks/uncertainty-rings.svg" alt="Three nested rings: all uncertainty, the part that could affect an objective, and the part that would breach your threshold" style="max-width:100%; margin:1.5em 0;" />

Three tests keep the register clean, and each takes seconds. **Is there still uncertainty?** If
not, it is an **issue**. **Has it already happened?** Then it is certainly an issue. **Is this a
cause, or the risk itself?** If it is a cause, write the consequence instead
{% cite thompson2017riskstatement %}. You **mitigate** a risk and you **resolve** an issue.

For example, halfway through a build somebody notices that the system stores personal data and
nobody has done a GDPR assessment. The missing assessment is certain, so it is an issue: go and do
it. What the assessment will find is not certain, so there is also a risk: *if the assessment finds
a problem, the launch slips.* One situation, two entries, two different logs.

Two independent classifications help sort what survives {% cite pressman2010risk %}. By **what is
threatened**: project, technical or business risk. By **how much you know**: known, predictable or
unpredictable. Only the first two can go in a register. The third is what a contingency reserve is
for, so a project with no reserve has quietly decided that category is empty.

Exposure is the arithmetic: **RE = probability × loss** {% cite boehm1991risk %}. Its job is to
**compare options**, not to measure the world. One risk worth $20M, 40% likely, has an exposure of
$8M. Coaching the team drops the probability to 10%, an exposure of $2M. Buying independent
verification for $500,000 drops it to 4%, which is $1.3M all in. Paying half a million was the
cheapest option, because the comparison is cost **plus the exposure left behind**. The scenario is
constructed, but the decision survives the numbers being well off: that is the answer to *"you made
the probabilities up"*.

Risk itself is not bad; **unmanaged** risk is {% cite vanscoy1992risk %}. The maturity ladder runs
crisis management, fix on failure, mitigation, prevention, elimination of root causes — and at the
first three levels the schedule battle is already lost {% cite mcconnell_rapid_1996 %}.

The SEI paradigm is the loop the rest of the lecture follows: **identify → analyse → plan → track →
control**, with **communication** at the centre rather than as a sixth step
{% cite vanscoy1992risk dorofee1996crm %}. The frameworks you will meet elsewhere — ISO 31000, PMI,
NASA, DoD, NIST's AI framework — share that loop and differ mainly in their menu of responses.

→ [Risks](../needs/risks/)

## 2. Finding them

**Most of your risks are already known, to someone not in the room.** The tester knows; the person
who ran the last migration knows. In fifteen SEI field tests across eleven organisations, sessions
raised issues that surprised project management every time {% cite carr1993taxonomy %}. So a long
register is not a failing project, and the belief that it is keeps risks off the list.

Who is in the room decides what is said. The same report: *"the presence of a reporting relationship
in an interview group always had an inhibiting effect on the subordinates"*
{% cite carr1993taxonomy %}. Run groups of at most five **peers**, send one unattributed copy of the
output to the manager, and treat fewer than fifteen statements from a session as a sign it did not
work — not as a sign the project is safe. This is the psychological-safety finding from L1b,
reached from a different direction.

Four techniques get things onto the list:

- **Write the threshold of success first.** From L3a: without it every worry looks the same size. A
  concern that would breach the threshold is a risk; one that would not is an event
  {% cite hoover_evaluating_2010 %}.
- **The premortem.** *"Team members assume that the project they are planning has just failed"*,
  then write reasons privately and read them round-robin {% cite klein2007premortem %}. Dissent
  becomes the assigned task, so it costs nothing to voice.
- **The taxonomy-based questionnaire.** One question per attribute, with cues ready. It exists to
  make a team ask about its development environment and its external constraints, not only about
  the product it is building {% cite carr1993taxonomy %}.
- **Boehm's top ten** as a checklist. Number one is **personnel shortfalls** — people, not
  technology {% cite boehm1991risk %}.

→ [Identification](../needs/risks/identification)

## 3. Writing one down

A usable risk starts from a **condition** you could check this afternoon, followed by the
**consequence** if nothing changes {% cite gluch1994risk %}. *Twenty-five per cent of the code is
written and half the time is gone.* *Ten developers share five workstations.* *The vendor's
compiler is two weeks late.* Each is a measurement, not an opinion; that is what separates a risk
from a worry.

If–then, condition–consequence and because–event–consequence carry the same three elements. Pick
one and be consistent. Whichever you pick, **the consequence carries a number and a unit** — *a
30-day delay to acceptance*, not *program delays* {% cite williams1999sre %}.

A well-formed risk can still be a bad one {% cite thompson2017riskstatement %}. *If the customer
changes the requirements, the schedule slips* points at a lever you do not hold; rewrite it towards
your own. *If the team does not test properly, defects escape* is not a risk at all, but a decision
not to do the work.

Sixty statements do not become sixty plans. Consolidate into seven to eleven areas grouped by
**shared mitigation**, then draw which area makes which worse. Areas with arrows mostly out are
**drivers**; spend on them, and the riders improve on their own {% cite williams1999sre %}.

→ [Capturing, owning and mitigating](../needs/risks/capturing)

## 4. Deciding which ones matter

**A band without a threshold is just a word.** This course's scales call probability high above
70% and impact high at a schedule slip over 20% {% cite root2014lectures %}; a government standard
calls more than 10% cost overrun catastrophic {% cite us_department_of_energy_software_2000 %}. They
disagree, which is the point: write your numbers beside the words.

Then the **vital few**: roughly 80% of project risk sits in 20% of the identified risks
{% cite pressman2010risk %}. Compute exposure, sort, draw a line and act above it. Most identified
risks never enter the mitigation plan, and writing down what you chose to ignore is what makes that a
decision rather than an oversight. Do not mitigate when the mitigation costs more than the exposure
it removes.

<img src="/content/needs/risks/matrix-vs-el.svg" alt="A risk matrix against expected loss: the outcome the matrix paints red has the smallest expected loss" style="max-width:100%; margin:1.5em 0;" />

The one corrective in the Needs block: **a red-amber-green matrix is a conversation device, not an
assessment**. NASA says so about its own {% cite nasa_nasa_2007 %}. In Cox's oil-well example, the
matrix paints the severe-loss outcome red and the blowout yellow — yet the blowout's expected loss
is about twice as large {% cite cox2008matrices %}. Keep the matrix for the conversation; settle the
order with ranges and expected loss.

The distribution behind all of this is fat-tailed. Across 5,392 IT projects the **median** cost
overrun is zero and the **mean** is 80% {% cite flyvbjerg2022overruns %}: half the projects are
fine, and the average is made of disasters. Size contingency to the tail, not to the middle.

→ [Analysis and prioritisation](../needs/risks/analysis) · [Why we misjudge risk](../needs/risks/biases)

## 5. Doing something about it

<img src="/content/needs/risks/response-matrix.svg" alt="A five by five matrix banded diagonally into prevent, prepare and monitor, with three example risks placed on it" style="max-width:100%; margin:1.5em 0;" />

**Where a risk sits decides the kind of response.** The bands run diagonally because exposure is a
product: a near-certain nuisance and a remote catastrophe can be worth the same. **Prevent** the
high band — attack the cause while the plan still moves. **Prepare** for the middle — you cannot
make the GDPR review find nothing, so write the contingency and its **trigger**. **Monitor** the low
band — owned, re-read each sprint, no work done {% cite root2014lectures nasa_nasa_2007 %}. The
matrix is used here to choose a response, never to score one.

Tracking has three instruments. A **top-ten list with last week's rank beside this week's** shows
whether anything is moving {% cite mcconnell_rapid_1996 %}. A **burn-down plan** of dated
activities, each with a test for done, because *"meetings do not burn down risks"*
{% cite dod2023rio %} — and testing you were always going to do mitigates nothing. And the
**exposure trend** for your sponsor: on one tracked project total exposure rose from 43 to 46.5 days
in the first two months, as identification caught up, then fell to 3
{% cite shrivastava2012pmi %}. A rising line early is good news; a flat line late is the warning.

Agile teams manage risk implicitly, by ordering work and delivering early. But *"simply placing a
higher priority on riskier tasks is not managing risk"* {% cite nelson_explicit_2008 %}: one team
with a risk manager and a spreadsheet mitigated **nothing** for several iterations, because the work
sat in the backlog as one generic task nobody could estimate. The recipe: **half a day once** to
identify against the threshold of success, about 20 risks, five to action planning; then **10–15
minutes per iteration review**, with triggers checked at the boundary and mitigations as small,
named backlog items.

→ [Risk management in agile](../needs/risks/agile)

## 6. The case: Comair, Christmas 2004

Comair's crew-scheduling system, built in 1986, had a hard ceiling of **32,000 trip transactions a
month**. A replacement was proposed in 1997 and rejected on good grounds, then deferred again and
again — Y2K, an acquisition, a strike, 9/11 {% cite dotoig2005comair %}. A storm before Christmas
2004 added more than 6,000 changes to a month already in progress, and on Christmas Eve the system
stopped: **89% of flights cancelled or delayed**, about 269,000 passengers affected
{% cite dotoig2005comair %}.

<img src="/content/needs/risks/comair-timeline.svg" alt="The Comair crew-scheduling failure, from the 1986 build to the December 2004 shutdown" style="max-width:100%; margin:1.5em 0;" />

Three lessons carry to any project. The storm was the **trigger**; the cause was a limit nobody
re-examined. The **probability rose every year** as the airline grew, with no decision taken, so a
register with one static probability column could not have shown it. And *we are already replacing
it* is a schedule, not a mitigation: the approved replacement was in testing when the outage came.

→ [Capturing, owning and mitigating](../needs/risks/capturing)

## Where this goes next

This closes the Needs block. **C3** asks you to write a threshold of success and a risk register on
a real case, where a risk is exactly what §2 said: a concern that would breach your own threshold.
**Q3** examines all three Needs lectures together.

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
