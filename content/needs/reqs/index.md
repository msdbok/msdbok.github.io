---
parent: Needs
title: Requirements
nav_order: 2
layout: default
page_type: topic-hub
---

# Requirements

A **requirement** is *"a property that must be exhibited to solve a real-world problem"*
{% cite swebok2024v4 %}. **Requirements management** is the set of activities that identify, control
and track those properties, and changes to them, for as long as the project runs
{% cite root2014lectures %}.

SWEBOK splits the work in two, and the split is worth holding on to: requirements *development* is
**reaching an agreement on what software is to be constructed**; requirements *management* is
**maintaining that agreement over time**.

## 1. Where a requirement stops

Two boundaries do more work than the definition, and both can be checked by reading a sentence.

- **A requirement is not a design.** It *"limits the range of valid designs, but does not specify any
  particular design"* {% cite iso2018req %}. *"Must comply with GDPR"* and *"must run on Android 11
  and above"* are requirements. *"Use a three-tier architecture with a Redis cache"* is a design
  decision wearing a requirement's clothes. A requirement narrows the design space; one that narrows
  it to a single point has stopped being a requirement.
- **A requirement is not a project constraint.** Cost, delivery schedule, staffing, reporting
  procedures and the QA plan are all real constraints, and none of them belongs in a requirements
  specification — that document is about the product, not about the process that builds it.

A third distinction saves arguments later: an **implied requirement** is one everybody assumes and
nobody writes down. *"The system shall be secure"* is implied until it becomes *"all traffic shall
use TLS 1.2 or later"*.

## 2. What the pages cover

| Page | The question it answers |
|---|---|
| [Stakeholders](stakeholders) | Who gets to state a requirement, and who did you miss? |
| [Elicitation](elicitation) | How do you find out what is needed, when nobody can just tell you? |
| [Requirement statements](stmts) | How do you write one, and classify it? |
| [Requirements engineering](eng) | What are the activities, and what is validation versus verification? |
| [Methods](methods) | User stories, use cases, scenarios — which and when? |
| [Documenting requirements](doc) | What goes in an SRS, a backlog, a statement of work? |
| [Validation, traceability and change](more) | What happens once a requirement changes? |
| [Organising requirements](org) | How do you structure and prioritise a large set? |
| [Requirements with LLMs](ai) | What can a language model do here, and where does it fail? |

One word is worth correcting before any of them. The activity is **elicitation**, not capture:
*"the term 'elicitation' is preferred to 'capture', to avoid the suggestion that requirements are
out there to be collected simply by asking the right questions"* {% cite nuseibeh2000roadmap %}.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
