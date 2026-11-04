---
parent: Case Materials
title: TRS Case 5: the first increment
nav_order: 3
page_type: case
layout: default
---
# C5 — Time Reporting System: the first increment

**Planning block — case day.** Read the **Case rules** (on Moodle) and the
**Case rules, part 2** (on Moodle) first. They give the shape of the day, the slide format
and the grading. This sheet has only what is specific to this case. Date, time and room are on
Moodle.

**Case:** [*Time Reporting System — System Description*](trsd.html) (from C4), with this sheet.
The team, the start date and the payment for each demonstration are in §7 and §9 of the
description. Adapted from Eduardo Miranda's TRS critical-path assignment (2013).

**Before the day.** Read Tables 1 and 2. The features' order is given. The order of the eight
increment activities is not: draft it, one reason per dependency. Bring the draft to slot 1. The
recitation shows how to turn it into a network.

## Readings

Everything you need is in the description, this sheet and these.

- **L5a — Planning and milestones.** A milestone is a result, the four tests it must pass, hard
  and soft dates.
- **L5b — Activities, critical path and critical chain.** Networks, the two passes, free and total
  float, levelling, why schedules run late, buffers.
- **MSDBOK** — [Milestone planning](https://msdbok.github.io/content/plan/milestones.html) ·
  [Activity planning](https://msdbok.github.io/content/plan/activities.html) ·
  [Critical path and float](https://msdbok.github.io/content/plan/critical-path.html) ·
  [Resource planning](https://msdbok.github.io/content/plan/resources.html) ·
  [PERT and merge bias](https://msdbok.github.io/content/plan/pert.html) ·
  [Critical chain](https://msdbok.github.io/content/plan/chain.html)

## Objectives

Turn one increment into a schedule the client can rely on, and promise the date of its
demonstration. This case is about **order, time and people**. What goes into the increment is
fixed below. Choosing it is C6.

## Your situation

Your company won the contract. Development starts **Monday 1 February 2027**. The client pays
**20% at the demonstration of each increment**, and asks you for the date of the first one.

The first increment carries the ten features in Table 1. This plan is **plan-driven**: the scope
is fixed, and the date is what you must find. Each feature is scheduled separately, to make
tracking and reprioritisation easier. Integration happens as each feature is finished, inside its
estimate.

The team is in §9: **two developers and one tester**. Day 1 is Monday 1 February. Count working
days, Monday to Friday, and ignore public holidays.

**Two estimates per task.** *Normal* has a fair chance of being enough. *Safe* is enough except
in a few really bad cases.

### Table 1 — Features: effort, duration and dependencies

Each feature is built by **one developer**. *Requires* lists the features that must be finished
first.

| Feature | Effort (person-hours) | Normal (days) | Safe (days) | Requires |
|---|---|---|---|---|
| Login | 24 | 3 | 4 | — |
| Grant Account Access | 24 | 3 | 4 | Login |
| Revoke Account Access | 24 | 3 | 4 | Grant Account Access |
| Block Account | 24 | 3 | 4 | Grant Account Access |
| Reset Password | 24 | 3 | 4 | Grant Account Access |
| Create Pay Code | 24 | 3 | 4 | Grant Account Access |
| Create Charge Authorization | 40 | 5 | 7 | Create Pay Code |
| Report Time | 40 | 5 | 7 | Create Charge Authorization |
| Submit Time Sheet | 32 | 4 | 5 | Report Time |
| Approve Time Sheet | 32 | 4 | 5 | Submit Time Sheet |

In this increment, employee data is loaded by hand from a file. The interfaces of §2 come later.

### Table 2 — Increment activities: who, effort and duration

The order of these eight activities is **yours** to decide.

| Activity | Who | Effort (person-hours) | Normal (days) | Safe (days) |
|---|---|---|---|---|
| Requirements review | one developer | 16 | 2 | 3 |
| Increment design | both developers | 80 | 5 | 7 |
| Design review | whole team | 24 | 1 | 1 |
| System test case design | tester | 40 | 5 | 7 |
| System test execution | tester | 16 | 2 | 3 |
| Update documentation | tester | 24 | 3 | 4 |
| Conduct demonstration | whole team | 24 | 1 | 1 |
| Fix remaining problems | whole team | 24 | 1 | 2 |

## Questions to answer

1. **Build the network.** Use the dependencies in Table 1. Add your own for Table 2, one reason
   each, tagged `[A]`. Draw it, or give it as a dependency table.
2. **Find the critical path.** Make the two passes at normal durations. For every task give early
   start, early finish, late start, late finish, total float and free float. Which tasks are
   critical? How long could the design review start late without moving the demonstration? How
   long could *Approve Time Sheet* start late without delaying the task after it? Would a shorter
   test case design shorten the increment? Say why.
3. **Find the critical chain.** Now count the people. Where would one person be needed in two
   places at once? Sequence those tasks. The longest path through tasks *and* people is the
   critical chain. Is it the same as the critical path? If not, who sets the date?
4. **Promise the date.** Plan the chain at normal durations. Size a project buffer from the gap
   between safe and normal, and say how you sized it. Put feeding buffers where other paths join
   the chain. Then give the demonstration date **on the calendar**. Show that it passes the four
   tests of a milestone, and say whether it is a hard or a soft date, and for whom. How will you
   watch the buffer, and what will you do as each third of it is used?

Every reason must rest on a concept from L5a or L5b, used the way the lecture defines it.

## Minto on this case

The date in question 4 is slide 2. Questions 2 and 3 give the reasons under it. The buffer rule
in question 4 is slide 7: who watches it, how often, and what happens at each third. Slide 8 is
the assumption that would move the date most.

The full network and the full table of values go in backup and in the appendix.

## Deliverables

**Slides** (8 max) on Moodle before the presentations start, Fri 20 Nov. **Report** (5 pages
max) and final slides **Thu 26 Nov, 23:59**. Both PDF. See the **Case rules** (on Moodle) and
**part 2**.

## Where teams lose points on this case

- **The critical-path date promised as it is.** It is a floor, not a forecast. Half of the tasks
  will run longer than their normal estimate.
- **A chain that ignores the people.** Three people cannot run four tasks at once, and the
  demonstration needs all of them.
- **A buffer of "plus 20%", or half the chain.** Size it from the safe estimates, and show how.
- **A feeding buffer placed on the chain itself.** It belongs where a side path joins the chain.
- **Free float and total float mixed up.** Free float belongs to one task. Total float belongs to
  the path.
- **"Day 46" given to the client.** The client needs a calendar date.

---

## Acknowledgments

The Time Reporting System, its description and the three assignments are adapted from
**Eduardo Miranda**'s course material on estimating and planning software projects (TRS
description 2009; critical-path and milestone assignments 2013), taught with **David Root**.

## Sources

- Miranda, Eduardo. *Time Reporting System — System Description.* Course material, 2009.
- Miranda, Eduardo. *Critical Path* and *Developing a Milestone Plan.* Assignments, 2013.
- Miranda, Eduardo. "Time-boxing planning: Buffered MoSCoW rules." *ACM SIGSOFT Software
  Engineering Notes* 36(6), 2011, 1–5.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
