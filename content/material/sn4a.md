---
parent: Study Notes
title: SN L4a — Work Breakdown Structure
nav_order: 9
page_type: study-notes
layout: default
---

# SN L4a — Work Breakdown Structure

A revision summary of the first Scope lecture. A **work breakdown structure (WBS)** is the whole
project cut into pieces that someone can own, estimate and track. The lecture gives one to **Quill
1.0**, the invented word processor from the requirements and risk lectures: a publishing-house
customer, six people, release due 1 February, 500-page documents open within 2 seconds, citations,
PDF export, cloud sync, documents in the customer's EU data centre. Three worries come with it: the
vendor of the PDF engine is late, only Dana understands the citation engine, and tracked changes are
already requested for Quill 2.0. Each section links to the
handbook page carrying the detail and the sources.

Why bother? One software project, followed for 42 weeks and reported in a review of time
prediction, planned **96** development tasks, then
**added 83** and **deleted 46** {% cite halkjelsvik2012origami %}. So list every piece of work you
can foresee, and plan to keep the list up to date.

## 1. What a WBS is

PMI defines it as *"a deliverable-oriented grouping of project elements that organizes and defines
the total work scope of the project"* {% cite woodward_project_2001 %}. A bicycle splits into frame
set, crank set and wheels, the frame set into frame, fork and seat; an outline (1, 1.1, 1.1.1)
carries the same tree.

One rule holds it together, the **100% rule**: every level holds all the work of its parent, and
nothing else. It fails two ways, with two victims. Leave work out and the project
pays: it *"will almost certainly be delayed and may experience cost overruns"*. Put work in twice,
or unasked, and the customer pays: *"the customer's time and money will be wasted"*
{% cite woodward_project_2001 %}. In a first draft of Quill's tree the document store appears under
both Citations and Cloud sync, so it is estimated twice; the acceptance run at the publisher appears
nowhere. NASA's cardinal rule faces the contract: *"Work scope not contained in the project WBS
should not be considered part of the project"* {% cite nasa2019wbs %}. If in doubt, include it, and
let the customer confirm or discard it {% cite miranda_managing_2014 %}.

A network of tasks is not a WBS. *"The WBS is NOT a schedule, and is developed before the project
team develops a timeline for the project"* {% cite githens_rolling_1998 %}. The WBS says **what, and
whose**; the network says **how, and when**, and its tasks come from the WBS leaves.

Scrum builds the same tree with size labels {% cite rubin_essential_2012 %}: epic (months), feature
(weeks), story (days), task (hours). For example, epic *Citations*, feature *Publisher styles*, story
*"As an editor I want references in the house style"*. Stories say what, tasks say how, so the scope
tree ends at the story. A theme is a group of related stories, not a level.

The unit of the tree is the **work package**: one deliverable plus the work that makes it, with one
owner. In the new-bike WBS, *Fork: design, build, test* is one. Design and integration serve all
the bicycle's parts, so they sit beside them; project management serves everything, so it sits at
the top {% cite miranda_managing_2014 %}.

<img src="/content/scope/wbs/new-bike-wbs.svg" alt="A new-bike project as a WBS: the bicycle and its assemblies, manufacturing instructions, sourcing, a marketing campaign and project management" style="max-width:100%; margin:1.5em 0;" />

→ [WBS](../scope/wbs/) · [Building a WBS](../scope/wbs/building_wbs)

## 2. Orientation

The criterion that splits the top is the **orientation**: by deliverable (what will I get, what does
each piece cost?), by task or phase (what happens when?), by discipline (who does the work?), by
account, or a hybrid {% cite miranda_managing_2014 %}. Globerson calls the WBS *"the taxonomy of a
project"* {% cite globerson_impact_1994 %}: the leaves stay the same, and the top decides what one
glance shows.

**Sponsors read deliverables.** An ambulance-dispatch system drawn by product (call taking,
ambulance allocation, ambulance communication) tells the sponsor *you understand the scope of my
project*; drawn by phase, it says only *you know how to do your job*. Drop ambulance communication
and the product tree loses one branch with its cost; in the phase tree, fractions of design,
development, deployment and training must be dug out. A book makes the same point:
chapter 2 sits in one branch of the deliverable tree, three places in the task tree, and nowhere you
can point to in the discipline tree. Of six questions about the book, the deliverable tree answers
five; the discipline tree wins only *who does the copyediting?*

There is a case for verbs. Progress is measured on work, and deliverables on a summary Gantt chart
*"would simply look like the stripes on a prison uniform"* {% cite wysocki2003needs %}. PMI answers
that *"WBS elements that are not deliverable-focused may lead to project failure"*
{% cite woodward_project_2001 %}. Both are right, at different levels: **nouns at the top, verbs at
the leaves**. An outcome may contain activities; an activity never contains outcomes. *PDF export →
set up the vendor engine* is fine; *Testing → Citations* is not.

The grouping also becomes the organisation. Thirty course packages of an MBA curriculum, flat, report
to one project manager who must know all thirty subjects; grouped, they sit under six managers who
settle most changes themselves {% cite globerson_impact_1994 %}. The choice is usually made at
proposal time, *"sometimes without being aware of it"*.

{: .exam-tip }
> **Exam tip:** argue orientation from the reader's question, not from taste: name the question,
> then show where each tree puts the answer.

→ [Orientation](../scope/wbs/orient)

## 3. Product plus enabling work

NASA's answer is the hybrid. A **product breakdown structure** holds only the parts you deliver; the
WBS adds the work of putting them together: management, systems engineering, integration and
verification, logistics support. *"The whole takes more work than the sum of the parts"*
{% cite nasa_nasa_2007 %}. So the WBS has elements that are not parts.

<img src="/content/scope/wbs/nasa-product-plus-enabling.svg" alt="A system broken into product components A to D, alongside management, systems engineering, integration and verification, and logistics support" style="max-width:100%; margin:1.5em 0;" />

NASA's template puts shared enabling work at Level 2, beside the products, with system integration
and testing as its own element {% cite nasa2019wbs %}. For Quill: management, systems engineering
and QA; then editor, big-document engine, citations, PDF export, cloud sync and document store; then
system integration and test, and the release.

The payoff shows when a function is added. In NASA's sample software project, a new functional unit
is **one new branch** under development, carrying its own design, code and unit test. Four existing
elements grow by a visible amount (integration testing, user manuals, the help desk, training), and
the nine Level 2 elements stay nine. The new function's cost reads off a few lines; in a phase tree
it spreads across every phase.

Shared work sits beside what it serves. Quill's document store serves the editor, citations and cloud
sync, so it goes at Level 2 beside them; the acceptance run goes under system integration and test;
the citation dialog's design serves citations only, so it goes under Citations. Draw the branch points
where you will integrate, or integration has no owner and no cost line {% cite nasa_nasa_2007 %}.

→ [NASA](../scope/wbs/nasa)

## 4. Building a WBS

Know five things before drawing a box {% cite miranda_managing_2014 %}: the start and end point
(Quill ends at acceptance by the publisher), what kind of system it is, its functions and
stakeholders, its quality attributes, and a notional architecture. What you do not know, assume, and
write the assumption down. Then seven steps: check the scope; split by outcome; add architectural
elements that are not features, such as the document store; refine into pieces you can drop; add
activities and tasks; review for gaps, overlaps and wrong nesting; and update as you learn.

**Every requirement and risk leaves work behind.** The 2-second target adds a layout cache and a
performance test at 500 pages. The EU data centre adds a set-up package. The vendor's PDF engine must
be selected, learned, set up, adapted and interfaced, and licensed: reused code is not free. And the
mitigation for Dana's knowledge, pairing on citations, is work: if it is not in the tree, nobody does
it.

Stop when a leaf has **one owner**, can be estimated and its status measured, can be prioritised,
scheduled or **dropped on its own**, and runs under about two weeks, Wysocki's rule of thumb
{% cite wysocki2003needs %}. Depth follows risk: go deeper on the big-document engine than on editor
styles. Every extra level costs maintenance and reporting {% cite woodward_project_2001 %}.

Estimates miss the work nobody codes: *"when they've been ordered to develop a product in the
shortest possible time, they don't go out of their way to look for extra tasks"*
{% cite mcconnell_rapid_1996 %}: cutover, data conversion, installation, demos, QA coordination,
meetings, training, holidays. Quill's first draft forgot the demos, the QA coordination and the
winter break. Give each a branch before anyone estimates.

→ [Building a WBS](../scope/wbs/building_wbs) · [PMI](../scope/wbs/pmi)

## 5. Rolling wave

**Detail the next wave, keep the rest coarse**: the
top covers the whole project from day one, and the bottom fills in one wave at a time
{% cite githens_rolling_1998 %}. A wave is as long as you can see. Githens's boat crosses 90 to 110
miles of unknown sea with a 20-mile horizon, so it re-charts its course at least five times.

Far-term work is a **planning package**: *"A WP provides further detail on work content that is
considered near-term, while a PP defines far-term work at a summary level"* {% cite nasa2019wbs %}.
It has an owner, a **budget** and a date, and is estimated top-down; without the budget the estimate
has a hole that looks like a plan. Quill 2.0's tracked changes is one. Because it threatens the
2-second promise, wave 1 carries one work package under it, a prototype on a 500-page document: do
not detail the guess, schedule the learning. The replanning itself is a work package with a fixed
date, or it never happens.

<img src="/content/scope/wbs/quill-rolling-wave.svg" alt="Quill as a rolling-wave WBS: version 1.0 decomposed, version 2.0 a dashed planning package with one prototype work package, and a replanning work package with a fixed date" style="max-width:100%; margin:1.5em 0;" />

→ [Planning waves](../scope/wbs/waves)

## 6. Keeping the WBS alive

Every element gets a **dictionary** entry, which exists for *"ensuring that all work scope has been
identified and to eliminate duplication and overlap"* {% cite nasa2019wbs %}. Quill's 1.7 PDF export:
content, the vendor engine's five kinds of work and the licence; owner, Lev; depends on the vendor's
next release; done when a 500-page manuscript exports with all page breaks.

Projects have several dimensions, and a tree shows one per level. With two sponsors and three
releases, either order works, but the second axis repeats under the first. The cleaner answer:
**put one dimension in the tree and tag the rest**. Each leaf belongs to exactly one category in
every dimension, so any grouping adds up {% cite miranda_managing_2014 nasa2019wbs %}.

Keep **one master WBS** in a tool with stable codes, and change it only through a decision. *"If the
various WBS structures used are not strictly derived from one basic structure, it will obviously
bring chaos to the project"* {% cite globerson_impact_1994 %}. The 96-task project is why.

{: .exam-tip }
> **Exam tip:** the rules here are consensus practice from standards and handbooks, not tested
> results, and the 96-task project is one project. Quote it as a warning, never as a rate.

→ [Building a WBS](../scope/wbs/building_wbs) · [Orientation](../scope/wbs/orient)

## Practice questions

**1. Why does a sponsor prefer a deliverable-oriented WBS, and what does a phase-oriented one do better?**

<details markdown="1"><summary>Answer</summary>

The sponsor's questions are about deliverables: what do I get, what does it cost, what if I drop it.
A deliverable tree answers each in one branch; a phase tree spreads every answer across all phases.
The phase tree shows what happens when, which progress reporting needs, so the hybrid puts those
verbs at the leaves {% cite wysocki2003needs %}.

</details>

**2. Compare the two halves of the 100% rule. Who pays when each is broken?**

<details markdown="1"><summary>Answer</summary>

Omitted work still has to be done, unplanned, so the project pays in delay and overrun. Duplicated or
unrequested work inflates the price, so the customer pays {% cite woodward_project_2001 %}. Either
error also makes every total above it wrong.

</details>

**3. Why should a shared component sit beside the features that use it, not under one of them?**

<details markdown="1"><summary>Answer</summary>

Under one feature it is owned by the wrong team; under several it is estimated twice. Beside them it
is counted once, with one owner, and its integration has a cost line {% cite nasa_nasa_2007 %}.

</details>

**4. "We use Scrum, so we do not need a WBS." How would you answer?**

<details markdown="1"><summary>Answer</summary>

The backlog already is one: epic, feature, story {% cite rubin_essential_2012 %}. It ends at the
story because tasks say how, not what, and its lower levels are detailed just in time, which is
rolling wave by another name.

</details>

**5. Why is a planning package more than a placeholder?**

<details markdown="1"><summary>Answer</summary>

It carries an owner, a budget and a date for decomposition. The budget keeps the total honest while
the detail waits, so scope is complete without paying for guesses {% cite nasa2019wbs %}.

</details>

## Where this goes next

Every leaf of Quill's WBS now has an owner and a definition of done. The publisher asks when, and
how much. A WBS tells you what to estimate, not how; that is the next lecture.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David
Root** {% cite root2014lectures %} on software project management. The ambulance-dispatch,
book-publishing and new-bike examples, the orientations, the building steps and the two-sponsor
exercise are Miranda's {% cite miranda_managing_2014 %}.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
