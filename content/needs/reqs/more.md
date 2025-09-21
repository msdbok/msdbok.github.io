---
parent: Requirements
title: More activities
nav_order: 4
layout: default
---

# More Requirements Engineering Activities

## Requirements Validation & Verification

> (Focus: checking requirements docs for quality and suitability)

**What to examine / fix:**

- Ambiguity — wording that can be interpreted more than one way
- Inconsistencies, omissions, and errors — missing requirements, contradictory statements
- Conformance to standards — does it follow company / domain / regulatory / style standards
- Scalability issues — will the requirements work as the system grows (users, data, load)
- Done typically via formal reviews (peer review, stakeholder review)

**Validation vs Verification (briefly):**

- _Verification_ of requirements means checking _that the requirements document is well-formed_: unambiguous, complete, testable, consistent.
- _Validation_ means checking _that the requirements are correct from stakeholders’ perspective_: they reflect the real needs, that nothing essential is missing, that what is specified matches what users/biz expect.

**Example:**

- Requirement: “Users should be able to search quickly.” → ambiguous.
- Better version (after verification + validation): “The system shall return search results on up to 1,000 items in under 2 seconds for 95% of searches; stakeholder X agrees that ‘search quickly’ means ≤ 2 seconds.”

---

## Validation Checklist (Pressman-style)

For _each requirement_, check:

| Check | What it means | Example |
|---|---|---|
| Stated clearly | No vague modifiers; simple clear language | Avoid “fast”, “intuitive”; use “≤ 2 seconds under load” etc. |
| Source identified | Know where this requirement comes from (stakeholder, document, regulation) | “From user interviews”, or “Requirement derived from business goal 3.” |
| Original source concurs | That stakeholder agrees requirement as documented | Show prototype or description and get confirmation from stakeholder. |
| Measurable / Testable | There is a way to test or measure it | “Error rate ≤ 2%”, “uptime 99.9% over 30 days” etc. |
| Cross referenced | It's linked to related requirements / constraints / interfaces | If requirement A depends on B, have references. |
| Doesn’t violate domain constraints | It respects the rules / limits of domain (legality, safety, technology) | E.g. GDPR, safety regulation. |
| Traceable to system objectives / model | The requirement maps to higher-level goals, or system architecture / business objectives | If business goal is “customer satisfaction”, this requirement improves that. |
| Spec is understandable | Different stakeholders (dev, biz, users) can read and understand it | Perhaps have non-tech and tech descriptions if needed. |
| Indexed | Requirements have unique IDs / numbering so they can be referenced | R-001, R-002 … etc. |
| Association with non-functional / quality attributes | If applicable, requirement shows which qualities it's concerned with (e.g. performance, security) | “Search requirement” annotated: performance; “User login” annotated: security & usability. |

---

## Traceability

**Definition**:

- Requirements traceability means tracking the life of each requirement: where it came from (source), what it led to (design, test, code), what depends on it, whether it's still needed, etc.

**Types of traceability**:

| Traceability Type | Meaning |
|---|---|
| Source traceability | Mapping a requirement back to stakeholder / document / origin |
| Forward traceability | From requirement → design, test cases, implementation |
| Backward traceability | From implementation or feature back to requirement, ensuring nothing extra is implemented without requirement |
| Bidirectional traceability | Both forward + backward: full lifecycle mapping |
| Interface traceability | Requirements connected to interfaces (external systems, APIs, UI) |
| Dependency traceability | Requirements that depend upon one another |

**Tool / artifacts used**:

- Requirements Traceability Matrix (RTM) — table that maps requirements to tests, design items, code, etc.
- Traceability graphs, lists or via ALM / requirements tools.

**Example**:

- Req “R-005: System must encrypt user data at rest” → traced to design component “Encryption Module”, traced to test case “Verify data at rest is encrypted using AES-256”, traced to code module implementing storage/encryption.

---

## Requirements Change & Change Management

**Why changes happen:**

- Stakeholder needs evolve
- New domain constraints discovered
- Business priorities shift
- Technology changes

**Change impacts:**

- The later in the project, the more expensive changes tend to be
- But change isn’t always bad (can improve product, fix issues)

**Managing changes (process):**

1. Establish a **baseline** (e.g. version 1.0 of requirements)
2. Set a cut-off, or “no more good ideas” date (for formal changes)
3. Collect proposed changes: include **source**, **classification** (functional / non-functional / constraint etc.), **dates** of request and review
4. Analyze impact: on scope, schedule, cost, quality etc.
5. Use traceability to see what other parts are affected
6. Renegotiate priorities, scope etc.

**Best practices:**

- Keep a trail (version history, who requested change, what was approved)
- Involve stakeholders (customer, dev, QA) in deciding whether to accept changes
- Have formal review of changes (Change Control Board or similar)
- Communicate changes to all as needed

---

## Sources

- [Wikipedia: Requirements Traceability](https://en.wikipedia.org/wiki/Requirements_traceability)
- [GeeksforGeeks: Traceability and its Types](https://www.geeksforgeeks.org/software-engineering/traceability-and-its-types/)
- [SAVIOM: Requirement Traceability Matrix](https://www.saviom.com/blog/requirement-traceability-matrix-and-why-is-it-important/)
- [Edge Delta: What is System Traceability](https://edgedelta.com/company/blog/what-is-system-traceability)
- [Jama Software: Traceability](https://www.jamasoftware.com/blog/traceability-in-requirements-management/)
  
---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
