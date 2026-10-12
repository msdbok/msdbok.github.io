---
parent: Study Notes
title: SN L6b — Tracking, Reporting and Controlling
nav_order: 14
page_type: study-notes
layout: default
---

# SN L6b — Tracking, Reporting and Controlling

A revision summary of the tracking lecture. **Tracking** finds out where the project really is;
**reporting** tells the people who depend on it, at fixed intervals; **controlling** does something
about what the report shows. The lecture returns to **Quill 1.0**, the invented word processor from
the earlier lectures, nine weeks before its 1 February release: six people, a publisher as the
customer, and a critical path through the new PDF engine, tuning for 500-page documents and the
acceptance run. Quill is invented, and every number about it is an example. The publisher asks
whether Quill is on track, and the team answers *"about 90%"*: no unit, no evidence, no decision.
Each section links to the handbook page carrying the detail and the sources.

## 1. Measuring progress

**Progress is a curve, not a straight line.** Output rises, peaks and tails off, so a straight line
drawn through the first weeks promises a date the project will not keep. The **90% syndrome** is a
project that reaches about 90% on schedule, then stalls and finishes at about twice the planned
duration {% cite ford2003ninety %}. Ford and Sterman's Python project, a chip design rather than
software, was 73% complete at its week-39 deadline; its rate then halved, and it finished in week 69.

**The first cause is rework nobody has found yet.** Python counted lines of design code, an objective
count, and still stalled. Work was marked done, its errors surfaced later in testing, and everything
built on it went round again: *"the downstream phases outrun the discovery of inherited rework
requirements."* For example, Quill's Ana has reported her 500-page performance prototype at 90% for
three weeks, because every larger test document shows more to tune. Nobody is lying. Optimistic
reporting is the second cause: it keeps the stall hidden. So put rework in the plan, and test and
integrate early.

**Done has to mean done.** Brooks wants milestones *"defined with knife-edge sharpness"*
{% cite brooks_mythical_1995 %}; McConnell makes them binary, done or not done
{% cite mcconnell_rapid_1996 %}. A **milestone trend chart** plots every milestone's forecast date at
each report, so a small slip repeated every week shows as a slope rather than a surprise. Quill's
milestone B, the 500-page result, moved from 18 to 26 January over the last four reports; four slips
in a row is a signal to act {% cite wysocki2003tracking %}.

**Calculate percent complete; never ask for it.** Count finished tasks over all tasks, or running,
tested features over all features, with work under way counting zero {% cite wysocki2003tracking %}.
Asked for a percentage, a person's first thought is *"What percent should I be?"* For Quill, count
the 1.0 features that run and pass their tests, and divide by all of them: the publisher can recount
that herself.

→ [Reporting progress](../track/report.md)

## 2. Getting the bad news

**Good news finds you; bad news has to be fetched.** *"positive information is likely to flow up
organizational hierarchies much more readily than negative information"*
{% cite milliken_exploratory_2003 %}. In Keil's experiment,
willingness to report fell at each step up the hierarchy, and further where messengers had been
punished {% cite keil2004badnews %}.

**Silence is the default.** 85% of Milliken's interviewees had held back an important issue, most
often someone's competence, mostly for fear of being labelled a troublemaker
{% cite milliken_exploratory_2003 %}. That is the topic behind many a task stuck at 90% on the board:
a colleague who is struggling. A quarter thought speaking up was futile.

**Ask to see it, then act.** The manager walks around, often and unannounced, and asks *"can you show
me?"* Asking Ana to open a 500-page document in front of you turns a percentage into done or not
done. Then act on what you hear, or say why not: people stop telling a manager who does nothing.
But keep the status meeting separate from the problem-solving one, or every report becomes an
intervention {% cite brooks_mythical_1995 %}.

→ [Reporting progress](../track/report.md)

## 3. Earned value

**Earned value is the budget of the work actually finished.** It uses three numbers, in money or in
person-hours. **Planned value** (PV) is the budget of the work scheduled by now, **earned value**
(EV) the budget of the work finished by now, and **actual cost** (AC) what the finished work cost
{% cite humphreys__associates_basic_2012 %}. SPI = EV / PV reads schedule; CPI = EV / AC reads cost;
below 1.0 is worse than plan. A task planned at 10 hours that took 14 earns 10.

**Spending on plan says nothing about progress.** PV and AC are both spending curves, so comparing
them is *"an indicator only of spending and not of overall project performance"*
{% cite nasa_nasa_2007 %}. In the lecture's eight-week example, at week 4 the plan called for 16
hours of work, the finished tasks were budgeted at 12, and the team had spent 18. Against PV alone,
the spend looks a little over plan; EV shows the project behind *and* over.

**Value is earned by a rule fixed before work starts.** Under 0/100 a task earns its budget only when
finished; under 50/50, half at the start and half at the finish. Neither can be talked up.
Self-reported percent complete can, and it carries the 90% syndrome straight into the curve. But
0/100 removes the optimism, not the rework: an honestly finished task can still come back. And keep
the baseline still: *"Lack of baseline control can doom a project."*
{% cite humphreys__associates_basic_2012 %}

**Read the two indices together, and forward.** Behind schedule and under budget is a cost warning,
not a saving: *"because schedule problems are often resolved by additional spending, an adverse SPI
is also predictive of later cost problems"* {% cite christensen1998evm %}. In one project Lipke
charts, CPI stayed above 1.1 for four months while SPI sat near 0.8, then fell below 1 and finished
near 0.7 {% cite lipke2003schedule %}. An SPI above 1 can mislead too, if the extra work is off the
critical path: check the float {% cite lukas_earned_2008 %}. Act early, because cumulative CPI
settles by about 20% complete {% cite christensen1998evm %}.

**A late project ends with a perfect SPI.** SPI is measured in money. When a late project finishes,
all its planned value has been earned, so SPI returns to 1.0 whatever the delay; the schedule
indices say little in the final third {% cite lipke2003schedule %}. **Earned schedule** reads the gap
in months instead: when did the plan expect today's earned value?

→ [Earned value](../track/evm.md)

## 4. Reading agile charts

**Two burndowns answer two questions.** The sprint burndown holds hours of task work left, updated
daily, and belongs to the team: will we finish this sprint? The release burndown holds story points
left, updated once per sprint, and belongs to the product owner and stakeholders: when is the release
done, and with what? {% cite rubin2012tracking %} A sprint line that goes up is usually an estimate
getting better: in Rubin's example, remaining work rose from 180 to 190 hours because one task was
re-estimated from 8 to 16.

**A flat release burndown has two causes.** Remaining work is total scope minus work done, and both
terms move. Slow work flattens the line; so does scope added as fast as the team finishes it. They
need opposite responses: a slow team needs its impediment found, while growing scope is the product
owner's call, to cut scope or move the date. The **burn-up** draws work done and total scope as
separate lines, so it tells the two apart. On a Slovenian newspaper site, the team completed about
155 points in six sprints while remaining work fell only from about 64 to about 52, because the
product owner kept adding requirements; the company shipped a reduced release after 9 sprints
{% cite mahnic2012scrum %}. When the publisher moved comments into Quill 1.0, Quill's
burndown flattened too, and the burn-up shows the team still delivering. **Before you push the team,
check whether the target moved.**

→ [Burndown and burn-up charts](../track/burndown.md)

**Velocity forecasts until it becomes a target.** Velocity is the size of the items finished in a
sprint; partly done counts zero. Points left divided by velocity gives a range: 200 points at 17 to
20 a sprint is 10 to 12 sprints, not 10 {% cite rubin2012tracking %}. Re-forecast every sprint. As a
target, it stops measuring the work. At ThoughtWorks,
managers *"excused the developers from writ[ing] tests, and the testers cut on the thoroughness of
the testing in hopes to maintain the velocity"* {% cite kupiainen2015agilemetrics %}.

**Flow shows where work waits.** In a cumulative flow diagram, a widening middle band means work
started and waiting. It suits maintenance and support, where there is no release to burn down; BBC
Worldwide cut lead time by 37% after starting fewer features at once {% cite middleton2012kanban %}.

→ [Velocity and flow](../track/agile.md)

## 5. Choosing and controlling

**Only earned value sees the money.** On a Scrum project, SPI is the burndown's gap written as a
ratio, and both forecast the same release date: on two projects the dates were
*"indistinguishable"* {% cite sulaiman2006agileevm %}. What earned value adds is CPI: a burndown
never holds effort spent, so it cannot show cost. Project A,
*"a one-half million dollar web application project"* run in Scrum, burned points at the planned
rate, yet *"the CPI index clearly shows the erosion of this buffer that the burndown doesn't
recognize."* So the deciding question is not agile or plan-driven but **who owns a budget**. Quill's
publisher bought it on an incentive contract in the release-planning lecture, so she gets earned
value at release level, and the team keeps its burndown.

→ [Choosing a tracking instrument](../track/choosing.md)

**Decide in advance which variance gets action.** A magnitude line catches a large gap: Wysocki
treats a 10% cost variance as *"the most allowed"* {% cite wysocki2003tracking %}. A trend line, such
as Quill's four slips in a row, fires earlier. Crossing a line starts an analysis, not an action:
*"the conditions must be analyzed to identify why the variance exists"* {% cite nasa_nasa_2007 %}.

**Every corrective action spends something.** Overtime gives a short gain, then *"an aggressive
decline in velocity along with a simultaneous decline in quality"* {% cite rubin2012tracking %}: it
buys a week now and rework later. Adding people has the same shape {% cite brooks_mythical_1995 %}.
Wysocki's ladder orders the alternatives by who pays, cheapest first: leave a slip alone if
the task has float, overlap tasks, reassign people from non-critical work, ask resource managers for
more, offer the customer the key features on the date, and only last ask for more time, which
*"offers the customer nothing in trade."* {% cite wysocki2003tracking %} Quill's B has no float, but
E, Dana's citation styles, has four weeks of it, so effort moves from E to B before anyone asks the
publisher.

Predictive control holds scope fixed and steers cost and schedule back to the baseline; agile
control holds the time box fixed and steers scope.

**Stopping is the hardest action.** CONFIG, an expert system, was funded for more than a decade while its usage fell from about 2.3% of quotations to about 0.1%
{% cite keil1995escalation %}. A sales rep said *"The problem is nobody is willing to kill it."* That
is escalation of commitment. Write a stop rule on what the project is for, before anyone is
attached: escalate the problem early, so nobody escalates the commitment later.

→ [Controlling a project](../track/control.md)

## 6. Reporting: answer first

**A Red project is often reported Green.** Status error has two parts, not knowing and not saying
{% cite snow2002status %}. Under moderate good-news bias, their model has a truly Red high-risk
project reach the executive as Green about half the time, and halving the perception error barely
changes that. Distortion is *"likely to be significantly higher in organizations where 'bad news gets
you killed.'"* The reader of the reports owns the climate.

**Red is a request for help, not a confession.** Print what the colours mean: Yellow comes with a
get-well plan, Red has none and asks for help {% cite wysocki2003tracking %}. Ask for one light per
dimension, cost, schedule and function, because one overall colour is easy to round up
{% cite snow2002status %}. Across many projects, count the colours and show the worst; traffic lights
are ordinal, so never average them {% cite stevens1946scales %}.

**Open the report with its colour and the decision.** A status report asks its reader to decide, so
it takes the Minto pyramid: answer, then reasons, then evidence {% cite minto_pyramid_2009 %}. The
usual template opens with the period's chronicle and puts the decision in its last line. Reordered,
with nothing added and nothing cut, Quill's report opens:

> *Schedule Yellow: B, the 500-page work, has slipped at four reports and has no float. We are moving
> effort to B to hold 1 February. If B slips again, we need your agreement that the grammar checker
> moves to 1.1. Cost and function Green.*

The three lights follow, then the evidence, with the period's chronicle last. The grammar checker is
a Could in Quill's release plan, so dropping it is the release plan working. The shape gets the bad news read;
the climate gets it written.

→ [Reporting progress](../track/report.md)

## Where this goes next

The tracking case applies these instruments to a project of its own, with the earned-value
arithmetic and the burndown reading this lecture left out.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and
**David Root** {% cite miranda_managing_2014 root2014lectures %} on software project management. The
earned-value worked example, the overtime loop, the milestone trend chart's structure, the
status-report template and the planning–tracking table are theirs.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
