---
parent: Lifecycles
title: Iterative
nav_order: 4
layout: default
---

# Iterative

An iterative — or *evolutionary* — lifecycle repeats a full development cycle over the whole product,
each pass producing a more complete version than the last. You use it when you do not yet know
exactly what to build, and expect to find out by building.

Pressman states the output plainly: *"Evolutionary process models produce an increasingly more
complete version of the software with each iteration"* {% cite pressman2010incremental %}. The
motivation is uncertainty — *"there are many situations in which initial requirements are reasonably
well defined, but the overall scope of the development effort precludes a purely linear process"*
is the case for [incremental](incremental.md); evolutionary models exist for the case where the
requirements themselves move.

## 1. Iteration buys information, not just progress

The distinction from incremental delivery is what each pass is *for*. An increment delivers a slice
of an agreed system. An iteration produces a version whose purpose is partly to tell you what the
next version should be — the feedback is the deliverable, alongside the software.

That is why "how many iterations" is the wrong question to ask about a project. Both models repeat.
Only one of them repeats in order to learn.

**Example — the Space Shuttle primary avionics.** The flight software was developed across seventeen
iterations over roughly thirty-one months, each accommodating requirement changes that had emerged
since the last {% cite larman_iterative_2003 %}. The requirements were not withheld out of
carelessness: nobody yet knew what flying the vehicle would demand, and each iteration settled part
of that question.

## 2. It is much older than the agile movement

Iterative development is routinely presented as a reaction against [waterfall](waterfall.md), which
gets the chronology backwards. Larman and Basili document iterative practice from the late 1950s
onward — Gerald Weinberg's recollection of the IBM Service Bureau in **1957**, and Project Mercury in
the early 1960s running **half-day** increments with test-first development
{% cite larman_iterative_2003 %}. Michael Fagan's first-hand account of IBM in 1971 describes work
already running *"in a series of cycles, similar to what we call 'iterative development'… today"*
{% cite fagan2002inspections %}.

So iteration was never absent. What happened is that a sequential *documentation* of the process
became the standard being audited against, and the iteration stopped being written down.

## 3. What it costs

Iterating without a stopping rule is the failure mode, and it has a name — endless iteration.
Because each pass legitimately changes the target, there is no internal signal that says *done*;
that signal has to come from outside, as a fixed budget, a release date or an explicit acceptance
condition.

The second cost is that continuous change is hard to contract for and hard to audit. Someone paying
for a fixed deliverable cannot easily buy a process whose output is defined by what it learns, which
is the same tension [the spiral](spiral.md) runs into when it meets contract acquisition.

## How solid is this?

- **The iterative/evolutionary definition here is Pressman's** {% cite pressman2010incremental %} —
  a textbook distinction, chosen because it is clean and citable, not because a study established it.
  Other sources draw the line differently or not at all.
- **The historical claims are well sourced but secondary.** Larman and Basili's article is a history
  and reports no evidence of its own {% cite larman_iterative_2003 %}; the 1957 date rests on a
  personal recollection by Weinberg, related decades later. Attribute it to Weinberg and cite it to
  Larman and Basili.
- **Fagan's is an invited retrospective** {% cite fagan2002inspections %}, which is recollection
  rather than record.
- **None of this compares iterative development's outcomes to anything.** It establishes that the
  practice is old and widespread, not that it performs better.

---

### Acknowledgments

This page adapts material from lectures by **Eduardo Miranda** and **David Root**
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
