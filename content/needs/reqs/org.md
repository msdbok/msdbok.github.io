---
parent: Requirements
title: Organising requirements
nav_order: 8
layout: default
---

# Organising Requirements

A few dozen requirements can be read as a list. A few hundred cannot, and the structure you impose on
them decides whether anyone can find a gap, judge a change or agree a priority. Organising is not
filing — it is how the omissions become visible.

## 1. The four moves

| Move | What it does | Example |
|---|---|---|
| **Affinity grouping** | Collects requirements by theme, so a theme can be reviewed as a whole | All access-control requirements — password rules, session expiry, role permissions — read together |
| **Hierarchy** | Structures general to specific, so the level of a statement is explicit | *Reporting* → *month-end reconciliation report* → *report is produced within five seconds at peak* |
| **Annotation** | Attaches the measure, scenario or prototype that makes a statement checkable | *"The system shall be reliable"* annotated with *99.9% uptime measured over 30 days* |
| **Prioritisation** | Decides what gets built first, and what is dropped when time runs out | See [release planning](../../plan/release/) |

## 2. Grouping is how you find the gaps

The reason to group before reviewing is that **a gap is visible in a group and invisible in a
list**. For example, collect every requirement touching the reporting module and the missing one
stands out because its neighbours are all there — nobody specified what happens when a report is
requested while the nightly batch is running.

The same applies to levels. A requirement set that mixes *"the system shall support regional
reporting"* with *"the report header shall show the region code"* has lost the distinction between a
business goal and a detail, and reviewers will argue about the wrong one. Stating the level makes
that visible.

## 3. Annotation is where a quality requirement becomes real

Most requirement sets carry a handful of statements that are aspirations rather than requirements —
*reliable*, *maintainable*, *usable*. The repair is not to delete them but to annotate each with the
scenario and **response measure** that says what it means here
{% cite barbacci2003qaw %}: *modifiable* is meaningless until it reads *"a mid-grade engineer can
modify this module in under two person-weeks."*

That is a per-project judgement, not a lookup. As the source puts it, *"it doesn't matter what we
call a particular quality attribute, as long as there's a scenario that describes what it means."*
Where the attributes are contested or architecturally significant, a **quality attribute workshop**
is the structured way to produce those scenarios with the stakeholders in the room — a one-day
event with 5 to 30 participants, which is heavyweight for a small team. What transfers at any scale
is the scenario form.

## 4. Prioritisation belongs to planning

Requirements work produces the input to prioritisation — what each item is, who wants it, what it
depends on — but the decision is a release decision and is made against capacity, sequence and
value. The methods live under [release planning](../../plan/release/); this page's job is to make
sure each requirement arrives there with its source, its level and its measure attached.

One thing does belong here: **prioritisation is only meaningful over comparable items**. A set
mixing business goals with field-level details cannot be ranked, because the two are not
alternatives to each other. That is a consequence of §2, and it is the most common reason a
prioritisation session stalls.

## 5. What organising does not achieve

Structure makes a set reviewable; it does not make it correct or complete. A perfectly grouped,
annotated, three-level requirement set can still describe the wrong product, and no amount of
reorganisation surfaces a stakeholder nobody talked to — that is
[stakeholder](stakeholders) and [elicitation](elicitation) work.

There is also a cost. A deep hierarchy on a small project is overhead, and annotation is only worth
doing where the statement would otherwise be untestable. Annotate the aspirations; leave the
already-measurable ones alone.

## How solid is this?

- **Where it comes from.** The scenario and response-measure material is an SEI method description;
  the grouping and hierarchy practices are conventional requirements-engineering craft rather than
  measured findings.
- **What is contested.** Nothing here — but note that no source in this bibliography compares
  organising schemes or measures their effect.
- **What we do not hold.** No evidence on how large a requirement set has to be before structure
  pays for itself; treat the depth as a judgement about your own project.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
