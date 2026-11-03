---
parent: Case Materials
title: TRS Case 6: the release plan
nav_order: 4
page_type: case
layout: default
---
# C6 — Time Reporting System: the release plan

**Tracking block — case day.** Read the **Case rules** (on Moodle) and the
**Case rules, part 2** (on Moodle) first. They give the shape of the day, the slide format
and the grading. This sheet has only what is specific to this case. Date, time and room are on
Moodle.

**Case:** [*Time Reporting System — System Description*](trsd.html) (from C4), with this sheet.
The contract, the payments, the team and the deadline are in §7 and §9 of the description.
Adapted from Eduardo Miranda's TRS milestone assignment (2013) and his *Buffered MoSCoW Rules*
(2011).

**Before the day.** Read Miranda's paper — five pages. Sketch which features depend on which.
Check whether the safe total in Tables 1 and 2 fits the capacity at all. Bring both to slot 1.

## Readings

Everything you need is in the description, this sheet and these.

- **L6a — Release planning.** Releases and iterations, Buffered MoSCoW, infrastructure as a
  feature, contracts and incentives.
- **L5a — Planning and milestones.** A milestone is a result with an owner; the four tests; hard
  dates belong to someone else.
- **L6b — Tracking.** A binary milestone shows the week it slips; set the threshold before the
  number arrives.
- **Miranda, E.** (2011). *Time-boxing planning: Buffered MoSCoW rules.* ACM SIGSOFT Software
  Engineering Notes 36(6), 1–5.
  [PDF](https://mse.s3d.cmu.edu/facstaff/faculty1/faculty-publications/miranda/mirandabufferedmoscowrules.pdf)
- **MSDBOK** — [Release planning](https://msdbok.github.io/content/plan/release/index.html) ·
  [Buffered MoSCoW](https://msdbok.github.io/content/plan/release/moscow.html) ·
  [Contracts and incentives](https://msdbok.github.io/content/plan/release/incentives.html) ·
  [Milestone planning](https://msdbok.github.io/content/plan/milestones.html) ·
  [Controlling a project](https://msdbok.github.io/content/track/control.html) ·
  [Burndown and burn-up](https://msdbok.github.io/content/track/burndown.html)

## Objectives

Decide what TRS can promise for 1 June, and set the plan up so that a slip shows in the week it
happens. In C5 the scope was fixed and you found the date. **Here the date is fixed, and the
scope moves.**

## Your situation

It is **Monday 11 January 2027**, the kick-off. TRS must be live no later than **Tuesday 1 June
2027** (§9). Instead of C5's plan-driven increment, the work runs in **three time boxes of four
weeks**. Your C5 chain took about eight weeks for ten features. A time box has four.

**Calendar.** Ignore public holidays.

| Step | Fact |
|---|---|
| Specification | Your team writes it in **2 weeks**. The client approves it in **1 week**. These hours are outside the iterations |
| Iterations | Three, **4 weeks** each, back to back, from the Monday after approval. Each ends with a demonstration |
| Acceptance | The client's IT department tests for **2 weeks**. It needs the test procedure **1 week** before |
| Training | The client's HR department trains for **1 week**, before launch. It needs the material **2 weeks** before |
| Data migration | The client's IT department sends the CSV files **1 week** before launch |
| Support | **30 days** after launch |

**Capacity.** The team of §9. The two developers give **320 hours per iteration**
(2 × 40 h × 4 weeks). Out of those hours, each iteration also needs **30 hours** of requirements
and design and **20 hours** for the demonstration. Testing and documentation, **40 hours** per
iteration, are the tester's.

**Two estimates per feature.** *Normal* has a fair chance of being enough. *Safe* is enough
except in a few really bad cases.

### Table 1 — Features, ranked by the client by business value

| Rank | Feature | Normal (h) | Safe (h) |
|---|---|---|---|
| 1 | Login | 24 | 32 |
| 2 | Grant Account Access | 24 | 32 |
| 3 | Create Pay Code | 24 | 32 |
| 4 | Create Charge Authorization | 40 | 56 |
| 5 | Report Time | 40 | 56 |
| 6 | Submit Time Sheet | 32 | 40 |
| 7 | Approve Time Sheet | 32 | 40 |
| 8 | Block Account | 24 | 32 |
| 9 | Reset Password | 24 | 32 |
| 10 | Revoke Account Access | 24 | 32 |
| 11 | Update Pay Code | 24 | 32 |
| 12 | Delete Pay Code | 24 | 32 |
| 13 | Modify Time Sheet | 32 | 40 |
| 14 | Recall Time Sheet | 32 | 40 |
| 15 | Delete Charge Authorization | 24 | 32 |
| 16 | Delegate Approval | 32 | 40 |
| 17 | Revoke Delegation | 32 | 40 |
| 18 | Supervisor Report | 40 | 56 |
| 19 | Employee Report | 40 | 56 |

### Table 2 — Features the client did not rank

The description requires them (§2, §7). The client treats them as given.

| Feature | Normal (h) | Safe (h) |
|---|---|---|
| Synchronize Employee Data | 40 | 56 |
| Export Approved Time Sheets | 40 | 56 |
| Import Legacy Data | 32 | 48 |

The dependencies among the first ten features are in C5's Table 1. The rest are yours.

## Questions to answer

1. **Plan the release with Buffered MoSCoW.** Draw the feature dependency graph, and place the
   three features of Table 2 in it. Decide whether you commit per iteration or once for the
   release, and say why. Then fill each time box as Miranda does: Musts at their safe estimates,
   then the Must buffer, then Shoulds and Coulds inside the buffer above them. Give the iteration
   planning table in the format of Table 3.
2. **Build the milestone plan**, from kick-off to the end of support. Each milestone is a result,
   not an activity, and has a date and an owner, the client's own milestones included. Attach
   every payment in §7.1 to a milestone. Use the format of Table 4.
3. **Decide what ships by 1 June.** Which features are Musts, which are at risk, and which will
   not make it? Is a four-week time box long enough to demonstrate something useful each time?
   Do you renegotiate the date, the scope or the team, and what does each option cost?
4. **Track it.** Which milestone or buffer do you watch, what reading makes you act, and what do
   you drop first? How should the contract reward the Shoulds and Coulds, so that a buffer left
   over is not simply spent?

Every reason must rest on a concept from L6a, L5a or L6b, used the way the lecture defines it.

### Table 3 — Iteration planning table (format)

| Feature | Rank | Normal (h) | Safe (h) | Must / Should / Could / Won't | Iteration |
|---|---|---|---|---|---|
| … | | | | | |

### Table 4 — Milestone chart (format)

| Date | Path / results / stakeholder | … | Path / results / stakeholder | Description | Responsible |
|---|---|---|---|---|---|
| Project start | | | | | |
| … | | | | | |
| Project end | | | | | |

## Minto on this case

Your answer to question 3 is slide 2. Questions 1 and 2 give the reasons under it. Question 4 is
slide 7. Slide 8 is the assumption that would change your answer, for example safe estimates hit
in every feature at once.

The full iteration table and the full milestone chart go in backup and in the appendix.

## Deliverables

**Slides** (8 max) on Moodle before the presentations start, Fri 4 Dec. **Report** (5 pages max)
and final slides **Thu 10 Dec, 23:59**. Both PDF. See the **Case rules** (on Moodle) and
**part 2**.

## Where teams lose points on this case

- **Musts planned at normal estimates.** Musts are planned at safe estimates. The buffer is the
  difference.
- **The client's order changed by the team.** The client owns the order; the estimates decide
  where the line falls. A prerequisite moves up with the feature that needs it, and only then.
- **The Table 2 features left out, or put last.** Nothing reaches Payroll, and nothing is billed,
  without the export.
- **Milestones that are activities:** "Iteration 2", "Testing". A milestone is a result someone
  can check.
- **Client milestones with no owner and no lead time.** The CSV files, the training material and
  the test procedure each have a date set by someone else.
- **"We will monitor progress."** Say what you watch, and the reading that makes you act.

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
