---
parent: Requirements
title: Methods
nav_order: 6
layout: default
---

# Requirements Methods

Three families of method dominate practice, and they answer different questions: a **specification**
says what the product must do in auditable form, a **user story** is a unit of work and a promise to
talk, and a **scenario** describes the work in context. Most projects use more than one.

## 1. Quick comparison

| Dimension | Specification (29148) | User stories | Scenarios |
|---|---|---|---|
| **Purpose** | Complete, auditable statement of requirements | Planning and collaboration units | Understanding work and context; driving design and tests |
| **Form** | Structured document plus a traceability matrix | *"As a … I want … so that …"* plus acceptance criteria | Narrative with context, paths and outcomes |
| **Validation** | Review against the quality criteria; traceability | Acceptance criteria, often Given–When–Then | Walkthroughs, usability testing, architecture evaluation |
| **Strengths** | Completeness and traceability | Speed, value focus, testability | Empathy, context, edge cases, discovering quality requirements |
| **Main cost** | Heavy to write and to keep current | Vague without the conversation and the confirmation | Not a specification on its own; needs translating |
| **Best when** | Regulated or contract work, complex interfaces | Evolving scope, frequent delivery | Early discovery, interaction design, architecture evaluation |

## 2. Specification: cite 29148, not 830

**ISO/IEC/IEEE 29148:2018** is the current standard {% cite iso2018req %}. It supersedes
**IEEE Std 830**, which was **withdrawn in 2011** — worth knowing because almost every SRS template
in circulation descends from 830's outline, and course materials still cite it as current. Its
substance on the design boundary, the project boundary and verifiability is reproduced in 29148.

A typical structure: introduction (purpose, scope, definitions) → overall description (users,
constraints, assumptions) → specific requirements (functional, interfaces, quality, design
constraints) → appendices. For example, a quality requirement in that form reads: *"search shall
return results within 200 ms at the 95th percentile for a catalogue of 10 million items."*

Use it where an auditor, a regulator or a contract will read the result.

## 3. User stories

*"As a &lt;user&gt;, I want &lt;capability&gt; so that &lt;benefit&gt;."* Ron Jeffries framed the
**3Cs** — Card, Conversation, Confirmation {% cite jeffries_essential_2001 %} — and Bill Wake's
**INVEST** gives the quality checks: Independent, Negotiable, Valuable, Estimable, Small, Testable
{% cite wake_invest_2003 %}. The checkable, thirteen-criterion version is on
[documenting requirements](doc) {% cite lucassen2016qus %}.

In practice: write acceptance criteria, prefer **Given–When–Then** {% cite cucumber_gherkin_2025 %},
slice vertically, and keep the conversation rather than the card as the artefact.

*Example.* *As a shopper, I want to save items to a wishlist so that I can buy them later.*
**Given** I am logged in, **when** I click Save, **then** the item appears in My Wishlist.

## 4. Scenarios

A scenario is a narrative task description — actor and goal, context, preconditions, the main
success path, alternatives and exceptions, postconditions {% cite rosson_scenario-based_2002 %}. It
is worth distinguishing from a use case: a use case describes outwardly visible behaviour, and a
scenario is *"a particular path through a use case"* {% cite nuseibeh2000roadmap %}.

*Example.* *On a crowded train with intermittent mobile data, Aisha opens the app to show her QR
ticket; when offline, the pass must still render and validate.* That one sentence surfaces an
availability requirement no feature list would have produced.

The same form specifies quality attributes, with a **response measure** attached — which is where
scenarios stop being narrative and become requirements {% cite barbacci2003qaw %}. See
[requirement statements](stmts).

## 5. Choosing between them

The honest position is that the form should not be discernible afterwards:
*"downstream maintainers should not be able to discern the life cycle used in earlier development
from the form of those requirements alone"* {% cite swebok2024v4 %}. Agile does not remove
requirements work; it redistributes it.

So the choice is driven by who must read the result and how stable the scope is — not by
methodological preference. The failure mode of each is predictable: a specification goes stale, a
backlog of stories loses the properties only visible across the whole set, and a scenario reads well
and specifies nothing until a measure is attached.

## How solid is this?

- **Where it comes from.** A current standard, two practitioner articles that report no study, a
  design-methods handbook chapter, and one empirical paper on user-story quality.
- **What is contested.** Nothing compares these methods' outcomes against each other — no source
  here shows that any one produces better software.
- **What we do not hold.** IEEE 830 is withdrawn, so anything citing it as current is describing
  a template's ancestry rather than a standard in force.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
