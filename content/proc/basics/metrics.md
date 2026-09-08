---
parent: Basics
title: Process Metrics
nav_order: 5
layout: default
---

# Process Metrics

A process metric measures how work gets done — cycle time, defect-removal rate, review coverage —
rather than what was built. It exists to improve the process, and it stops working the moment it is
used to judge the people running it.

That last sentence is the whole difficulty. A product metric sits still while you measure it. A
process metric is attached to people who can see it, and who will respond.

## 1. Measure the process, but never the people

Watts Humphrey, writing the maturity framework the whole improvement movement is built on, states
the rule as an absolute: *"Process data must not be used to compare projects or individuals. Its
purpose is to illuminate the product being developed and to provide an informed basis for improving
the process"* {% cite fowler_software_1990 %}. He gives the consequence rather than a complaint —
*"When such data is used by management to evaluate individuals or teams, the reliability of the data
itself will deteriorate"* — and then the mechanism underneath it: *"Perhaps most important is that
the mere act of measuring human processes changes them."*

So the question a manager answers before choosing any metric is not *is this the right number* but
**who will see it, and what will happen to them because of it**.

## 2. Precision is not the defence

The intuitive fix is a better metric — define it more tightly, compute it more carefully. The
evidence says that misses the mechanism. Douglas Hoffman's account of metrics dysfunction is that it
appears *"whether or not our models are correct, and regardless of how well or poorly we collect and
compute"* the numbers {% cite hoffman2000metrics %}. Gaming is a response to what the number is
*used for*, and no amount of definitional care changes that.

**Example — closing twenty-five defects without fixing one.** A team was measured on defect reports
closed. Twenty-five open reports were
closed as *duplicates* of a single new report whose only shared property with them was the subsystem
it was filed against; the new "master" report's description simply pointed back at all twenty-five
{% cite hoffman2000metrics %}. Nobody falsified anything, the count improved, and the defects were
still there. A second team, measured on the age of open defects, reassigned a dozen long-running
ones — resetting the clock without touching the code.

The software-specific version students will meet is velocity. When a team's points-per-sprint
becomes a target, estimates inflate or work gets called *done* early {% cite rubin_essential_2012 %}.
Steve McConnell names the two failure modes directly — *"overoptimization of single-factor
measurements"* and *"misuse of measurements for employee evaluations"* — and notes that a badly run
metrics programme *"can actually damage developer morale"* {% cite mcconnell_rapid_1996 %}.

## 3. Two numbers are rarely comparable

Even honestly gathered, process data resists comparison. Humphrey puts task-complexity variation
across product types at more than five to one, small modifications at two to three times the cost of
new code per line, and variation from **differing definitions alone** at *"at least as high as seven
times"* {% cite fowler_software_1990 %}. Two teams reporting different numbers may be doing
different work, or counting differently. Ranking them says nothing.

## 4. What to do instead

Derive the metric from a goal rather than from what is easy to collect — that is
[GQM](gqm.md) {% cite basili1994gqm %}. Then decide the audience deliberately: data that reaches
the team improves the process, and the same data reaching an appraisal destroys it. Where the thing
that matters cannot be counted at all, [the scoreboard](scoreboard.md) tracks judgement as a trend
instead of inventing a number.

Measurement is also not free. Humphrey again: *"Measurements are both expensive and disruptive;
overzealous measuring can degrade the processes we are trying to improve."*

## How solid is this?

- **Nothing cited here measures a measurement programme's effect.** These sources establish that the
  behaviours happen, not how often, and not that metrics are harmful on balance. The conclusion is
  *choose the audience*, not *stop measuring*.
- **Hoffman's paper is a practitioner conference talk** (PNSQC 2000), and its cases are anecdotes he
  states he altered to protect the organisations involved. No frequencies, no sampling
  {% cite hoffman2000metrics %}.
- **Humphrey's material is from 1988**, reprinted as Appendix A of the SEI's SEPG Guide — so cite
  it to Humphrey, not to Fowler & Rifkin, who edited the volume {% cite fowler_software_1990 %}.
  His figures are a snapshot of that era's data.
- **McConnell and Rubin are practitioner books** — well-grounded advice, not studies
  {% cite mcconnell_rapid_1996 %} {% cite rubin_essential_2012 %}.

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
