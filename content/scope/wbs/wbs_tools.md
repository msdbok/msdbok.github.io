---
parent: WBS
title: WBS Tools
nav_order: 6
layout: default
---

# WBS Tools

A **WBS tool** keeps the work breakdown as one coded, versioned structure, so that the tree, the
outline, the schedule and the cost report are all views of the same elements rather than separate
drawings that drift apart.

## 1. What the tool has to hold

A picture of boxes is not enough. Whatever the product, a working WBS needs four things.

- **A stable code for every element**, numbered to show its level and its parent
  {% cite nasa_nasa_2007 %}. Codes become charge codes, and NASA warns that an approved code
  *"cannot be removed"*, so do not load the preliminary tree into the finance system early
  {% cite nasa2019wbs %}.
- **A dictionary entry per element**: *"A document that describes the work content of each WBS
  element, in product-oriented terms, and relates each element to the respective, progressively
  higher levels of the structure, as well as to the Statement of Work"* {% cite nasa2019wbs %}
  {% cite woodward_project_2001 %}.
- **A baseline and change control.** A WBS *"will be permanently exposed to changes"*, so keep one
  master structure under configuration management and derive every party's view from it
  {% cite globerson_impact_1994 %}.
- **Attributes, or tags**, for the dimensions that are not in the hierarchy: release, stakeholder,
  location. The tree carries one dimension; tags let the tool regroup the same leaves by another
  {% cite miranda_managing_2014 %}.

## 2. One structure, several views

A tree and an indented outline carry the same content: *"Both convey exactly the same
information"* {% cite wysocki2003needs %}. Pick the view by the job the WBS is doing at the time.

| Use of the WBS | Best view | Kind of tool |
|---|---|---|
| Thinking: trying alternative decompositions | tree on a canvas | whiteboard or mind map (MindView, XMind) |
| Agreeing scope with a sponsor | tree, top two or three levels | diagram tool, or a dedicated WBS tool (WBS Schedule Pro) |
| Planning: owners, estimates, dictionary | coded outline with columns | spreadsheet, or a scheduler's outline (MS Project) |
| Tracking: progress rolling up | outline linked to the schedule | scheduler; in Scrum, the backlog tool's epic–feature–story levels {% cite rubin_essential_2012 %} |

The four uses come from Wysocki: a thought-process tool, an architectural design tool, a planning
tool and a status-reporting tool {% cite wysocki2003needs %}. A team usually starts on a canvas and
moves to an outline once the shape has settled.

## 3. Example: Quill 1.0 in a spreadsheet

Quill is an invented word processor for a publishing house. Its WBS lives in one sheet with one
row per element: code, element, owner, estimate, release tag, stakeholder tag, and a link to the
dictionary entry. Element **1.7 PDF export** carries its owner, its estimate and its acceptance
test: *a 500-page manuscript exports with all page breaks*.

Filtering on the release tag gives the release plan. Filtering on the stakeholder tag gives each
sponsor's view. Neither view needs a second tree. When tracked changes are added for Quill 2.0,
the new rows take new codes, and 1.7 keeps its code, so its actual costs still roll up.

## 4. When it does not help

- **A drawing is not a structure.** A WBS drawn in slides has no codes, no roll-up and no history;
  it cannot be kept up to date as a structure, which is why it is a bad place to keep one
  {% cite miranda_managing_2014 %}.
- **Tools disagree on vocabulary.** Some nest activities under tasks, some the other way round
  {% cite wysocki2003needs %}; fix the meaning of each level before you import.
- **No tool checks the 100% rule.** A tool adds up what you entered. Completeness comes from
  review, and NASA's cross-reference matrix of requirements against WBS elements does it
  explicitly: an empty row is unauthorised work, an empty column is missing work
  {% cite nasa2019wbs %}.
- **Tags can double-count.** Each leaf must sit in exactly one category of every dimension, or a
  regrouped total counts work twice {% cite miranda_managing_2014 nasa2019wbs %}.

## How solid is this?

- **Where it comes from.** NASA's and PMI's handbooks, a project-management textbook and one
  journal paper describe what a WBS must record; none of them evaluates a product.
- **What changes fast.** The products named in the table are examples of each kind, not
  recommendations; their features change between versions.
- **What we do not hold.** No study comparing WBS tools is in this bibliography.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
