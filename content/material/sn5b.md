---
parent: Study Notes
title: SN L5b — Activities, Critical Path and Critical Chain
nav_order: 12
page_type: study-notes
layout: default
---

# SN L5b — Activities, Critical Path and Critical Chain

A revision summary of the second Planning lecture. An **activity plan** is the work under the
milestones: who does which task, in what order, and when. The lecture follows **Quill**, the invented
word processor from the requirements and risk lectures, nine weeks before it goes live at the
publisher. Three streams merge into one acceptance run: Ana integrates a new PDF engine, then tunes it
for 500-page documents; Ivan sets up the EU data centre, then cloud sync; Dana writes ten citation
styles, then a reviewer checks the citation dialog. Each section links to the handbook page carrying
the detail and the sources.

## 1. How teams plan activities

The first question is **who commits to a task**. The lecture calls the two answers pull and push.

In Scrum the team **pulls**. Sprint planning starts from the hours the team really has; stories are
broken into tasks, estimated, and taken only if they fit. During the sprint nobody assigns work: each
person takes the next task at the daily scrum. The team commits *"at the last responsible
moment—the sprint planning for that sprint"* {% cite rubin_essential_2012 %}. For example, a team
averaging 40 points plans about 20 for a sprint with two public holidays.

In a plan-driven project the manager **pushes**: *"Every task that is scheduled should be assigned
to a specific team member."* Its companion is **effort validation**, so that nobody is double-booked
{% cite pressman2010incremental %}. The detail is still planned late, one wave at a time, close to
when each milestone's work starts {% cite andersen_warning_1996 githens_rolling_1998 %}.

Pull buys **autonomy**, and its typical failure is that nobody takes the awkward task. Push buys
**accountability**, and its failure is a plan that outruns what people can do. A team can mix them,
but everyone should know which one runs and who answers when a task is late.

→ [Activity planning](../plan/activities)

## 2. Networks and the critical path

An **activity network** records which task waits for which, and nothing else: *"Considerations of
available manpower and equipment are conspicuous by their absence"* {% cite kelley1959cpm %}. Brooks
warns that *"The first chart is always terrible"* {% cite brooks_mythical_1995 %}; draw it anyway,
because drawing it forces every dependency into the open.

Each link has a type and a reason. **Finish-to-start** is the safe default: tuning starts when the
PDF engine is in. **Start-to-start**, **finish-to-finish** and the rare **start-to-finish** buy time at
the price of rework risk {% cite wysocki2003needs %}. A technical dependency cannot be argued away; a
management one can. Start with finish-to-start everywhere and relax a link only when the date demands
it.

The **critical path** is *"the sequence of activities that must be completed on schedule in order
for the project to be completed on schedule"* {% cite wysocki2003needs %}. In Quill it is Ana's stream
and the acceptance run, nine weeks. These tasks have **zero float**: a week lost on the PDF engine is
a week lost on go-live.

<img src="/content/plan/quill-network.svg" alt="Quill's activity network: Ana's PDF engine and tuning, then the acceptance run, form the nine-week critical path; Ivan's stream has one week of float and Dana's four" style="max-width:100%; margin:1.5em 0;" />

A manager does three things with it. Spend money only on critical tasks: speeding up Dana's styles
buys nothing. Recheck the path after every change, because it moves. And watch the **nearly
critical** paths: Ivan's stream is one week short. On DuPont's first test, a chemical plant with 393
jobs, only about one job in ten was critical {% cite kelley1959cpm %}. Without the network you
expedite everything; with it you pay only for what moves the date. Two passes over the network give
each task a **window**, earliest start to latest finish; the window minus the work is its float.

→ [Activity planning](../plan/activities) · [Critical path and float](../plan/critical-path)

## 3. Float and levelling

Float comes in two kinds that belong to different people {% cite wysocki2003needs %}. **Free float**
is how far a task can slip without delaying any successor: it belongs to the task owner. **Total
float** is how far it can slip without delaying the project's finish: it belongs to the path, and the
first task to spend it takes it from the ones after.

Dana's citation styles and the accessibility review both have four weeks of total float. But the
review starts the moment the styles end, so every week Dana takes comes out of the reviewer's four.
The styles have no free float; the review's four weeks are its own. Before you tell someone they have
float, say which kind.

The network has no people in it, so the plan may need more people than exist. **Levelling** moves
work to fit them, in a fixed order: spend free float, then total float; when float runs out, move the
finish date; use overtime last {% cite noauthor_scheduling_nodate wysocki2003needs %}. For example,
the publisher asks for a two-week citation-engine fix that only Dana can make. Levelled, the fix goes
first and her styles move later, spending two weeks of their float; go-live holds. Often there is no
float: *"It should be obvious to you that resource leveling almost always stretches the schedule"*
{% cite wysocki2003needs %}. The network date is what the logic allows; the levelled date is what the
team can deliver.

→ [Critical path and float](../plan/critical-path) · [Resource planning](../plan/resources)

## 4. Views of a plan

One plan has several drawings, and each answers one question.

A **Gantt chart** shows when: tasks as bars on a calendar, milestones as diamonds
{% cite pressman2010incremental %}. Anyone reads it in seconds, so it belongs in a status meeting.
But *"you cannot tell from the Gantt chart what must come before and after what"*
{% cite wysocki2003needs %}, and it shows who is assigned, not whether they are free. Report with the
Gantt chart; decide with the network.

A network cannot draw a loop, and design work loops. A **Design Structure Matrix (DSM)** lists the
tasks as both rows and columns; in Browning's convention, *"Subdiagonal elements indicate
feedback—the potential for iteration and rework in the process"* {% cite browning2001dsm %}. In
Quill's typesetting design, pagination and footnotes need each other: a citation reading *see page
12* needs the page break, and long footnotes move it. Steward's original matrix is the transpose
{% cite steward1981dsm %}, so check the convention first.

To handle a loop, **partition** the matrix so the coupled tasks form blocks, then **tear** each block
by guessing the least risky missing input, and review the guess at the end {% cite browning2001dsm %}.
Quill estimates the footnote space per page, paginates on that guess, and checks it after the
citations are laid out. The sorted, torn matrix is an ordinary network.

| View | Answers | For |
|---|---|---|
| Milestone chart | What must be true, and by when | Sponsor |
| Gantt chart | What runs when, by whom | Team |
| Network | Which slip moves the date | Planner |
| DSM | Where work loops back | Design lead |

→ [Gantt charts](../plan/gantt) · [Design Structure Matrix](../plan/dsm)

## 5. Why schedules run late

The critical-path calculation assumes known durations, free people, no loops and kept safety. Real
projects break all four, so the computed finish is a **floor**, never the forecast.

**The most likely date is not a likely date.** Durations are skewed: *"while you can do only a
limited number of things to shorten the duration of a task, the number of things that can go wrong is
almost unlimited"* {% cite miranda_planning_2002 %}. A task with a best case of 10 days, a most likely 20
and a worst 40 has under a 40% chance of finishing by day 20. Ask for a range, as PERT's three estimates do
{% cite malcolm1959pert %}, and commit at a stated confidence.

**Where paths merge, delays pass on.** A merge point waits for the latest path, so the real finish is
always later on average than the calculated one {% cite maccrimmon1964pert %}. The merged path
*"passes on delays but seldom passes on savings"* {% cite miranda_planning_2002 %}. That is why Ivan's
stream is tracked as closely as Ana's.

**Best guesses run short, even with a record.** Students forecasting their honours theses guessed
33.9 days and took 55.5; even their worst case was short half the time. *"It seems that people can
know the past and yet still be doomed to repeat it"* {% cite buehler1994fallacy %}. Start from how
long similar work took, and ask someone who is not the doer.

**Safety gets spent.** *"It is a commonplace observation that work expands so as to fill the time
available for its completion"* opens Parkinson's 1955 satire about officials; project management
borrowed only that line {% cite parkinson1955law %}. *Student syndrome*, *"leaving everything to the
last minute"*, is Goldratt's term from a novel, with no study behind it, as Rand's review reports
{% cite rand_critical_2000 %}; Herroelen and Leus later tested the method built on it
{% cite herroelen2001ccpm %}. Buehler and colleagues measured the deadline effect: a one-hour task
took 4.3 days on average with a week's deadline and 9.1 with two {% cite buehler1994fallacy %}. Keep
safety out of task deadlines.

**Juggling makes everything late.** In Zultner's example, three projects share three people; switching
project after every task makes all three finish late, while one at a time finishes each earlier
{% cite lynch_critical_2003 %}. Finish before you switch, and start fewer things.

→ [PERT and merge bias](../plan/pert) · [Critical chain](../plan/chain)

## 6. Critical chain

Goldratt's diagnosis, in Rand's summary, is that safety is added and then wasted: estimates are
padded, work starts late, people are pulled away, and early finishes go unreported
{% cite rand_critical_2000 %}. His remedy, **critical chain project management**, takes the safety out
of each task and puts it where the date needs it; Herroelen and Leus tested its rules in simulation
{% cite herroelen2001ccpm %}.

What survives is **pooling**: tasks rarely all go badly at once, so one shared buffer protects the
date in less time than a pad on every task. Tasks are planned at 50/50 estimates, so half will
overrun, and that must be acceptable: *"The only way you will get accurate 50% likely expected task
times is if it is OK to exceed them"* {% cite lynch_critical_2003 %}.

The **critical chain** is the longest path once shared people are counted, a *"leveled critical
path"* {% cite raz2003ccpm %}. For example, before a Quill release build, Ana's PDF export is the
longest path by dependencies alone. But Dana has a fix and her citation styles, and in sequence they
take longer. The manager watches Dana's queue, not Ana's progress.

<img src="/content/plan/quill-chain.svg" alt="Dana's citation-engine fix and citation styles in sequence form the critical chain; Ana's PDF export joins through a feeding buffer, and a project buffer protects the release" style="max-width:100%; margin:1.5em 0;" />

Three buffers guard the chain: a **project buffer** at the end, a **feeding buffer** where a side
path joins, and **resource buffers** that warn the next person to be ready. There are no task dates;
the manager watches the project buffer instead. Leach's rule reads it in thirds: do nothing, plan a
response, act {% cite leach1999ccpm %}. Raz and colleagues warn that the "days remaining" reports
behind it can carry the same inflated safety the method set out to remove {% cite raz2003ccpm %}.

Both methods share the same risks: merge bias, biased estimates, heuristic levelling, political
pressure, and tasks that run late together because they share a cause. A buffer manages the
uncertainty that is left; risk management still has to remove the causes.

The evidence says **keep the buffers, drop the arithmetic**. In Herroelen and Leus's simulation,
sizing the project buffer at half the chain asked for 65% of the planned schedule, measured before
execution, against 42% when sized from the tasks' risk {% cite herroelen2001ccpm %}. And estimates are
not uniformly padded: in one IS department of over 500 tasks, 60% finished early, 8% on the estimate
and 32% late {% cite raz2003ccpm %}. Size buffers from risk, re-plan when the chain changes, and cut
estimates from your own record, not by half.

{: .exam-tip }
> **Exam tip:** the critical-chain evidence is thin. Of 140 papers, 8% are empirical, and no
> comparative study shows adopters perform better {% cite ghaffari_current_2015 raz2003ccpm %}. Argue
> for the buffer, not for the method's claimed savings.

→ [Critical chain](../plan/chain) · [Resource planning](../plan/resources)

## Practice questions

**1. Why say which kind of float a developer has before granting it?**

<details markdown="1"><summary>Answer</summary>

Free float belongs to the task: spending it delays nobody. Total float is shared along the path, so
spending it may take a colleague's margin {% cite wysocki2003needs %}.

</details>

**2. Why is the computed critical-path date a floor and not a forecast?**

<details markdown="1"><summary>Answer</summary>

Durations are skewed late, merge points pass on delays but not savings, levelling stretches the plan,
and safety gets spent {% cite maccrimmon1964pert miranda_planning_2002 %}.

</details>

**3. What from critical chain would you keep, and what would you drop?**

<details markdown="1"><summary>Answer</summary>

Keep one visible, pooled buffer and watch it instead of single tasks. Drop the fixed rules: size
buffers from risk and re-plan when the chain moves {% cite herroelen2001ccpm %}.

</details>

## Where this goes next

Buffers protect a date. In release planning the date is fixed, so something else has to give: the
scope. The next lecture applies the buffer idea to features instead of days.

---

### Acknowledgments

This content is adapted from lectures by **Eduardo Miranda** {% cite miranda_managing_2014 %} on
software project management. The two-level view of planning, the three-buffer figure and the risks
shared by critical path and critical chain are his.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
