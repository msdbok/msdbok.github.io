---
parent: Case Materials
title: TRS Case 4: the bid
nav_order: 2
page_type: case
layout: default
---
# C4 — Time Reporting System: the bid

**Scope block — case day.** Read the **Case rules** (on Moodle) and the
**Case rules, part 2** (on Moodle) first. They give the shape of the day, the slide format
and the grading. This sheet has only what is specific to this case. Date, time and room are on
Moodle.

**Case:** [*Time Reporting System — System Description*](trsd.html), §1–§8. About 1,400 words, with a use-case
diagram, four class diagrams and a state diagram. On Moodle. Adapted from Eduardo Miranda's TRS description. The
same system is the case for C4, C5 and C6, so **keep your work.**

**Read it before the day.** Make two lists, each with the section: *what TRS keeps* (the data it
creates and updates), and *what it only reads or sends* (the Personnel and Payroll systems). Those
two lists are the start of your count. As a team, bring a draft Level 2 of your WBS to slot 1.

## Readings

Everything you need is in the description and in these.

- **L4a — Work breakdown structure.** The 100% rule, orientation, the product plus its enabling
  work, work packages, the WBS dictionary.
- **L4b — Estimation.** Sizing with function points, expert judgment, COCOMO, and how to combine
  two estimates and read the spread.
- **MSDBOK** — [WBS](https://msdbok.github.io/content/scope/wbs/index.html) ·
  [Building a WBS](https://msdbok.github.io/content/scope/wbs/building_wbs.html) ·
  [Orientation](https://msdbok.github.io/content/scope/wbs/orient.html) ·
  [NASA](https://msdbok.github.io/content/scope/wbs/nasa.html) ·
  [Estimation approaches](https://msdbok.github.io/content/scope/estimates/approaches.html) ·
  [Function point analysis](https://msdbok.github.io/content/scope/estimates/fpa.html) ·
  [FPA explained](https://msdbok.github.io/content/scope/estimates/fpa_explained.html) ·
  [COCOMO](https://msdbok.github.io/content/scope/estimates/cocomo.html) ·
  [Expert judgment](https://msdbok.github.io/content/scope/estimates/expert.html)

## Objectives

Find all the work in TRS, size it, and turn the size into a bid you can defend. This case is
about **what the work is and how big it is**. It is not about when it is done. That is C5.

## Your situation

It is **October 2026**. Your company bids for the TRS contract in §7 of the description. The bid
manager needs your answer by Monday: **how much effort to bid, as a range, and what the price
covers.**

Your company's records give one more fact. On similar web systems it delivered **8 to 12
function points per person-month**. That rate covers the software work from requirements to
acceptance, project management included. It does not cover deployment, training material or
support after launch. A person-month is **160 hours**.

## Questions to answer

1. **Draw the boundary, then count.** Which data does TRS keep, and which does it only read or
   send? Classify every function in §8 as an external input, output or inquiry. Classify every
   group of data as an internal or external file. Rate each one with the IFPUG tables and add up
   the unadjusted function points. At least one classification depends on a choice the
   description leaves open. Find it, say what you chose, and give the count the other way.
2. **Build the WBS.** Put the product and its enabling work at Level 2, as in the NASA hybrid.
   Break it down to work packages one person could own. Every function in §8 and every
   obligation in §7 must leave work in **exactly one** place. Write one WBS dictionary entry for
   your riskiest work package: what "done" means for it.
3. **Make two estimates, then read the spread.** Convert your count to effort with the company's
   rate range. Then estimate your WBS work packages, bottom-up, by expert judgment, Planning Poker
   or COCOMO. Compare the two. Do not force them to agree. Say which work one of them did not see.
4. **Set the bid.** Give the range, and the number you bid inside it. Say what the bid includes
   and excludes. Name the one assumption that would change the price most.

Every reason must rest on a concept from L4a or L4b, used the way the lecture defines it.

## Minto on this case

Your bid in question 4 is slide 2. Questions 1 to 3 give the reasons under it. Slide 7 is the
bid as a contract would state it: inclusions, exclusions and the conditions the price depends
on, with an owner for each Level 2 branch. Slide 8 is the assumption that would re-price the bid.

The full WBS and the full count go in backup and in the appendix. On the slides, show the part
that carries your number.

## Deliverables

**Slides** (8 max) on Moodle before the presentations start, Fri 30 Oct. **Report** (5 pages max)
and final slides **Thu 12 Nov, 23:59**, after the reading week. Both PDF. See the
**Case rules** (on Moodle) and **part 2**.

## Where teams lose points on this case

- **The Payroll System counted as an external file.** TRS sends data to it and never reads it.
  Check what crosses the boundary, and in which direction.
- **A WBS by phase only:** Requirements, Design, Coding, Testing. Then a change to one function
  touches every branch, and the sponsor cannot see what it costs.
- **Training material, data migration and support left out**, because the count does not see them.
  §7 is part of the scope.
- **Screens counted instead of transactions.** One user goal is one transaction, however many
  screens it takes.
- **One number, with no range.** An early estimate is a range. Say where in it you bid, and why.

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
