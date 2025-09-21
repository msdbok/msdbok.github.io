---
parent: Requirements
title: Methods
nav_order: 7
layout: default
---

# Requirements Engineering Methods Overview

## IEEE 830 SRS (and its successor)

**What it is.** IEEE Std 830 defined what a good Software Requirements Specification (SRS) looks like: structure + quality attributes (correct, unambiguous, complete, consistent, ranked, verifiable, modifiable, traceable). It’s now superseded by ISO/IEC/IEEE 29148, which generalizes to systems + software and formally defines “good requirement” constructs.

**Typical structure (830-style):**

- Introduction (purpose, scope, definitions)
- Overall description (users, constraints, assumptions)
- Specific requirements (functional, interfaces, non-functional, design constraints) + appendices & index.

**When to use:** Regulated/contract work, complex interfaces, and rigorous traceability (with an RTM). 29148 is the current standard to cite.

**Mini-example (SRS NFR):**  
“Search must return results within **200 ms p95** for a catalog of **10M items**.”

---

## User Stories (Agile)

**What they are.** Thin, user-value slices for planning and collaboration (XP/Scrum): _“As a <user>, I want <capability> so that <benefit>.”_ Ron Jeffries framed the **3Cs**: Card, Conversation, Confirmation. Bill Wake’s **INVEST** gives quality checks (Independent, Negotiable, Valuable, Estimable, Small, Testable).

**Good practice:**

- Write acceptance criteria; prefer **Given-When-Then** (BDD/Gherkin).
- Slice vertically; keep stories small; refine via conversation.

**Mini-example (story+AC):**  
_As a_ shopper, _I want_ to save items to a wishlist _so that_ I can buy them later.  
**AC:** Given I’m logged in, When I click “Save”, Then the item appears in My Wishlist.

---

## User Scenarios (Scenario-Based Design)

**What they are.** Narrative task descriptions capturing actor goals, context, main path + alternatives; used from discovery through design and evaluation. Also central to architecture reviews (e.g., SAAM/ATAM) via **quality attribute scenarios**.

**Typical elements:** Actor & goal, context, preconditions, main success path, alternatives/exceptions, postconditions; often storyboarded or prototyped.

**Mini-example (scenario):**  
“On a crowded train (spotty 4G), _Aisha_ opens the app to pull up a QR ticket; when offline, the pass must still render and validate.”

---

## Quick comparison

| Dimension   | IEEE 830 SRS                | User Stories                   | User Scenarios                        |
|-------------|-----------------------------|-------------------------------|---------------------------------------|
| Purpose     | Complete, auditable specification | Planning & collaboration units | Understand work/context; drive design & tests |
| Form        | Document with structured sections + RTM | “As a… I want… so that…” + AC | Narrative with context, paths, outcomes |
| Validation  | Reviews vs. SRS qualities; traceability | Acceptance criteria / BDD     | Walkthroughs, usability, architecture stress |
| Strengths   | Completeness & traceability  | Speed, value focus, testability | Empathy, context, edge cases, NFR discovery |
| Limits      | Heavy to maintain            | Can be vague without 3Cs/INVEST | Not a spec alone; needs translation   |
| Best when   | Regulated/contract, complex NFRs | Agile delivery, evolving scope | Early discovery, UX/HCI, architecture eval |

---

## Methods at a glance

- **SRS (830/29148-aware):** glossary → stakeholders & constraints → functional reqs grouped by feature → interfaces → measurable NFRs → RTM.
- **User stories:** goal first → write story + acceptance criteria → check **INVEST** → automate via BDD/Gherkin.
- **Scenarios:** identify personas/tasks → write main & alternate paths with context → storyboard/prototype → (optionally) convert to acceptance tests or quality attribute scenarios.

---

## Sources

- IEEE 830 (historic text / outline): _IEEE Recommended Practice for Software Requirements Specifications_.  
  [math.uaa.alaska.edu](https://www.math.uaa.alaska.edu/~afkjm/cs401/IEEE830.pdf)
- Current standard: _ISO/IEC/IEEE 29148:2018 — Requirements engineering_. ISO catalog: [ISO](https://www.iso.org/standard/72089.html) • IEEE summary: [IEEE Standards Association](https://standards.ieee.org/ieee/29148/6937/)
- User stories — 3Cs: Ron Jeffries, “Essential XP: Card, Conversation, Confirmation” (2001) + “Three-C’s Revisited.” [ronjeffries.com](https://ronjeffries.com/xprog/articles/expcardconversationconfirmation/)
- INVEST: Bill Wake, “INVEST in Good Stories, and SMART Tasks.” [xp123.com](https://xp123.com/invest-in-good-stories-and-smart-tasks/)
- BDD/Gherkin reference: Cucumber docs — Gherkin Reference. [cucumber.io](https://cucumber.io/docs/gherkin/reference)
- User stories overview: Agile Alliance — _User Stories_ and _Three C’s_. [agilealliance.org](https://agilealliance.org/glossary/user-stories/)
- User scenarios (SBD): Rosson & Carroll, “Scenario-Based Design” (handbook chapter, PDF). [TU Delft OCW](https://ocw.tudelft.nl/wp-content/uploads/2_RossonCarrollSBDforHandbook2002.pdf)
- Scenario-based architecture analysis: SEI — SAAM/ATAM history page; SAAM paper (PDF). [SEI](https://www.sei.cmu.edu/history-of-innovation/evaluating-system-architecture/)

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
