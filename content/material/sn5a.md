---
parent: Study Notes
title: SN L5a — Planning and Milestones
nav_order: 11
page_type: study-notes
layout: default
---

# SN L5a — Planning and Milestones

A revision summary of the first Planning lecture. It asks two questions: what does a project
promise, and to whom; and how does it know the dates? The running example is **Quill 1.0**, the
invented word processor from the requirements and risk lectures, twelve weeks before release: six
people, a publishing house as the customer, release due 1 February. The publisher asks: *what will I
be able to check, and when?* The team answers: *we are in sprint 6 of 9.* That is true, and she
cannot check it. Six parts close the gap. Each section links to the handbook page carrying the
detail and the sources.

## 1. Why plan

*"By coordination, I mean managing dependencies among tasks"* {% cite herbsleb_global_2007 %}. If
nobody's work depended on anyone else's, nobody would need to plan. In a telecom release built at two
sites, two network elements *"worked well individually, but not together because the specs were
misinterpreted"*, and testing slipped six weeks {% cite espinosa2007coordination %}. Nobody was
lazy; each site built what it understood. One company said of itself: *"Planning was difficult,
cross-functional planning was even more difficult, and honest cross-functional planning was the
hardest of all"* {% cite lynch_critical_2003 %}.

Teams coordinate in **four** ways, and every real team uses all four
{% cite espinosa2007coordination herbsleb1995ooad %}:

- **Reference to a higher level**: the tech lead rules on an interface dispute, and becomes the
  bottleneck.
- **Preparation**: the release plan or the interface specification, agreed in advance. It breaks on
  the uncertain parts of the work.
- **Shared representations**: the code, the task board, the CI dashboard. Someone must keep them
  current.
- **Communication**: the stand-up, the design review. It breaks first when the team is split across
  sites.

A plan is the second: **coordination prepared in advance**. Routine dependencies are cheapest to
coordinate this way, which leaves talk free for the uncertain ones.

We do not plan to use a tool, or to stop the client changing course. We plan to coordinate the work,
to know the cost, to tell people when to expect results, and to see what a change does to our
promises. A plan's purpose is *"to help assess and measure the impact of changes on previous
commitments so that informed decisions can be made"* {% cite miranda_managing_2014 %}. At DuPont in
1957, a change to about 40% of a critical-path plan took about 10% of the original effort to re-plan
{% cite kelley1959cpm %}.

A good plan has the properties of a good program {% cite miranda_managing_2014 %}: no race
conditions (nobody booked on two things at once), no deadlock (no circular dependency), modifiable in
hours, robust through buffers, and readable by a sponsor. For example, if two plans each book Dana,
Quill's only citation-engine expert, for forty hours in the same week, neither plan has a bug on its
own. Together they have a race condition.

→ [Planning approaches](../plan/approaches)

## 2. Predictive and agile planning

Both approaches plan. They take the same decisions at different moments and by different people.
Schwaber's 1995 comparison shows when the commitments are fixed: in a waterfall, product, cost and
date are determined during planning; in iterative development and Scrum they are set during the
project {% cite sutherland_scrum_origins %}. A predictive manager acts on deviations from a baseline
{% cite kelley1959cpm %}; a Scrum team inspects a working increment every sprint.

A plan records agreements on **what, when and who** {% cite miranda_managing_2014 %}. A predictive
project answers with a WBS, a milestone plan and a responsibility matrix, mostly at the start and
revised at planning waves. Scrum answers with the product backlog, item priority and the task board,
decided sprint by sprint. The key row is *when executed?* In a predictive plan the manager assigns
the task, which is **push**: *"Every task that is scheduled should be assigned to a specific team
member"* {% cite pressman2010incremental %}. In Scrum, people take the next task when they are free,
which is **pull**.

Agile teams do not plan less. Rubin describes five levels: portfolio (a year or more), product (many
months), release (three to nine months), sprint (one week to one month) and daily
{% cite rubin_essential_2012 %}. Scrum defines only the last two; most organisations need all five.

Scrum also has two levels of planning {% cite miranda_managing_2014 %}. Story points and velocity
give a duration for the backlog: **commitment-level** planning, what is promised. Sprint planning
splits the top items into tasks, estimates them in hours and commits to what fits, and each day
people pull the next task: **activity-level** planning, how the work gets done. *"The Sprint Backlog
is a plan by and for the Developers"* {% cite schwaber2020scrumguide %}. In any project, commitments
come first and feed the activity plan; small deviations stay in the activity plan, large ones climb
back and change the commitments.

{: .exam-tip }
> **Exam tip:** "agile decides continuously, predictive decides once" is too strong. Predictive
> tasks are revised at planning waves, and agile releases are planned months ahead. Contrast *when*
> and *by whom*, never *whether*.

→ [Planning approaches](../plan/approaches)

## 3. Two plans, two readers

Every project needs two plans. The **sponsor-oriented plan** lists results the sponsor can check:
what will exist, by when, and who answers for it. The **developer-oriented plan** lists iterations,
phases, tasks and owners: how, in what order, by whom. A changed task order is the team's business. A
changed result or date is a renegotiation with the sponsor, done in the open.

So *iteration 3 done* tells the publisher nothing. An iteration names an interval of the team's
work, and it would be equally true if the iteration delivered nothing. Ask instead: what can the
publisher do today that she could not do yesterday? Rewritten as results she can check, Quill's plan
reads *When the publisher has agreed the Quill 1.0 feature list* and *When a 500-page manuscript
opens in two seconds on the publisher's laptop*. An iteration can carry a milestone only if its goal
is a checkable result {% cite miranda_managing_2014 %}.

Miranda's **AmazonLite**, a teaching example of an online bookshop, shows the format
{% cite miranda_managing_2014 %}. Each row is a date and a result, in a client column or a team
column, with arrows for dependencies. The client's own obligations, such as approving the design
concept, are milestones too, so the sponsor sees where she could delay the project herself.

→ [Planning approaches](../plan/approaches) · [Milestone planning](../plan/milestones)

## 4. What a milestone is

*"A milestone describes what is to be fulfilled, but not the method to fulfil it"*
{% cite andersen_warning_1996 %}. Andersen writes each milestone as a state beginning *When…*, and
the first word is the test. *Coding finished* is an activity; *When a 500-page manuscript opens in two
seconds on the publisher's laptop* is a result. If it will not start with *When*, it is probably an
activity.

Hence the rule **plan results early and activities late**. A milestone plan needs only the logic of
the results, so it can cover the whole project from the start. An activity plan needs the outcomes
of earlier work, which do not exist yet, so it is drawn one milestone ahead. *"The milestone plan is
in this sense a robust plan: impervious to alterations concerning activities"*
{% cite andersen2006milestone %}. A team that plans every task of a twelve-month project in January
and finds a better architecture in March must abandon its plan or follow the worse route. With a
milestone plan, the results stay and only the route changes.

Milestones depend **finish-to-finish** {% cite miranda_managing_2014 andersen2006milestone %}: to
reach milestone 4 the project must have reached state 2, but work towards 4 may start long before.
Quill's release cannot pass acceptance before the citation styles are done, yet performance tuning
does not wait for them. A milestone gates a result, not the start of work, so a milestone plan does
not become a waterfall.

Andersen groups milestones into **result paths**, one per kind of result
{% cite andersen_warning_1996 %}. Rolling out an information system has three: the system, educated
users, and a changed organisation. A responsibility chart then has milestones as its rows, not
tasks.

→ [Milestone planning](../plan/milestones)

## 5. Writing good milestones

**Result milestones** are for the sponsor and sit weeks or months apart: *when the publisher has
agreed the feature list*. **Control milestones** are for the team and sit a day or two apart:
*citation export passes its tests*. Both obey one rule: *"The only two statuses are 'done' and 'not
done.' Percentages are not used"* {% cite mcconnell_rapid_1996 %}. An underestimated task looks on
schedule until about three weeks before it is due {% cite brooks_mythical_1995 %}, so check every day
or two.

Every milestone must pass **four tests**. *Specific*: one named state, a 500-page manuscript in two
seconds, not "performance is good". *Verifiable*: anyone can check it the same way, with a test the
publisher can rerun. *Relevant*: the sponsor cares; she asked for big documents. *Timely*: it lands
while it can still change a decision, before the editors start the spring list. *"Milestones must be
concrete, specific, measurable events, defined with knife-edge sharpness"*
{% cite brooks_mythical_1995 %}. *Unit-test coverage reaches 80%* is specific and verifiable, but
tells the publisher nothing she cares about.

Sharpness is written down as **exit criteria**: the work items, their state and the quality reached,
decidable without asking the team {% cite radice_programming_1985 %}. Scrum's Definition of Done
plays the same role: *"The Definition of Done is a formal description of the state of the Increment
when it meets the quality measures required for the product"* {% cite schwaber2020scrumguide %}. For
Quill's two-second milestone: the 500-page test set exists, the test passes on the publisher's laptop
model three runs in a row, and no open defect is critical.

Boehm's three **anchor points** fit any process {% cite boehm1996anchoring %}. At **LCO**, life-cycle
objectives, the stakeholders agree objectives and scope, and at least one feasible architecture
exists. At **LCA**, life-cycle architecture, one architecture is chosen and all major risks are
resolved or covered: *"If you haven't satisfied the LCA milestone criteria, do not proceed into
full-scale development."* At **IOC**, initial operational capability, the software, the site and the
people are ready. For Quill, LCA means the two-second promise, tested only on 100-page documents, is
proven on 500 pages, or covered, before the full build.

A **hard date** is imposed by a third party or owed to one, and a late result loses most of its
value: a regulatory go-live, a release launched at a conference. A **soft date** is agreed between
the parties and can move by negotiation {% cite miranda_managing_2014 rubin_essential_2012 %}. Is
Quill's 1 February hard? If the publisher has announced its spring list to booksellers, the date
belongs to someone else and is hard; if it is the team's own target, it is soft. Ownership decides,
not the calendar.

→ [Milestone planning](../plan/milestones)

## 6. Planning milestones, worked

Seven steps take you from results to dates {% cite miranda_managing_2014 %}:

1. List the results and the release content.
2. Mark each milestone hard or soft, and draw the dependencies.
3. Draw the resource plan: the hours that actually exist.
4. Subtract cross-cutting work: management, configuration management, quality assurance.
5. Place the hard-milestone work and its safety, and name an owner.
6. Fit the soft-milestone work around it, and set the soft dates.
7. Move the safety to protect the milestones, and iterate.

The dates come last. For Quill, six people at forty hours for twelve weeks make 2,880 hours on paper;
after training, holidays and cross-cutting work, about 2,000 are left for milestone work. Plan on
those, never on the headcount.

With many imposed dates, work backwards from them; with few, work forward along the most logical
path. Put buffers in front of hard dates: *"Beware white space != buffers"*
{% cite miranda_managing_2014 %}. White space has no owner, so it gets spent; a buffer is sized,
owned and placed. Programme managers hold about 10% in reserve, out of sight
{% cite noauthor_scheduling_nodate %}.

AmazonLite shows the whole method {% cite miranda_managing_2014 %}. Kick-off is 1 October, with at
most four developers; no programming before the infrastructure is chosen, no deployment before the
acceptance test passes. The work comes to 2,100 hours. Drawn to scale, holidays included, it did not
fit the 1 March time box, so the project took one more month; a smaller third release was the other
option. Only then were the dates read off the plan: acceptance test 1 March, deployment 31 March,
customer sign-off 1 April.

A real plan has the same shape. MegaM@Rt2, a 36-month European research programme with partners in
six countries, ran three tracks: project phases, technology development and case studies. Its seven
milestones sit where one track hands a result to another, such as prototypes ready for the case
studies' first evaluation at month 15.

{: .exam-tip }
> **Exam tip:** most of this lecture is practice and definition, not measurement. The seven steps
> are Miranda's practice, DuPont's figure is one project, the three weeks come from one 1967 study
> outside software, and Quill's numbers are invented. Argue with them; never quote them as rates.

→ [Milestone planning](../plan/milestones) · [Resource planning](../plan/resources)

## Where this goes next

Quill now has dated results the publisher can check, and hours to back them. The milestone plan says
what will exist, and by when. Who does which task, in what order, is activity planning, the critical
path and the Gantt chart: the next lecture.

---

### Acknowledgments

This content is adapted from lectures by **Eduardo Miranda** {% cite miranda_managing_2014 %} on
software project management. The what-when-who comparison, the good-plan analogy, the hard and soft
dates, the seven steps and the AmazonLite example are his. The MegaM@Rt2 example is the course
instructor's own project, © Andrey Sadovykh et al.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
