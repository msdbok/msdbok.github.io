---
parent: Requirements
title: Requirement Documentation
nav_order: 6
layout: default
---

# Requirements Documentation

### Types of Artifacts

These are common artifacts produced in Requirements Engineering:

| Artifact                              | Definition / Purpose                                                                                      | Example                                                                                                                |
|----------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| **Statement of Work (SOW)**            | Outlines who does what, when, how, for what cost, and under what acceptance criteria. Often part of contract/planning. | “SOW: Vendor A delivers module X by Date Y; Customer reviews within 10 business days; payment upon acceptance.”        |
| **Requirements Specification (SRS / Req Spec)** | Detailed document recording functional & non-functional requirements, constraints, interfaces, quality attributes, environment, etc. | “System shall support concurrent logins by 1000 users; system shall operate on Windows + Linux; response time under load <2s.” |
| **Concept of Operation (ConOps)**      | Narrative describing how the system will be used in its operational environment: stakeholders, use cases, external system interactions. | “Teachers will upload assignments; students view assignments; system interacts with legacy LMS; operates during school hours.” |
| **Initial Software Project Plans**     | Early plan for scheduling, resources, budget, risk, work breakdown; reference for what must be in the SRS / what must be delivered. | “Phase 1: requirements & design in Month 1–2; Phase 2: implementation Month 3–5; risk review at end of phase 1.”       |
| **Acceptance Criteria**                | Conditions that must be met for the solution (or parts, user stories, features) to be accepted by stakeholders. | “Feature X is accepted when under peak load, average response time <3 seconds; no security breach in a defined penetration test.” |

In **Agile**:

- **Epics & User Stories** — High-level requirements (epics) broken down into smaller user stories.
- **User Scenarios with Personas** — Narrative flows using user/role personas to explore how features are used and how the system behaves.

---

### What Matters in Requirements Artifacts

Key questions to ensure your documentation is useful (not just verbose):

- How does the system work in its operational environment?
- How will you build the system? (implementation plan, architecture hints)
- What does it mean to be successful? (acceptance criteria, definition of done)
- What must the system do? (functional requirements)
- Why must it do this? (business drivers, mission, stakeholder value)
- What quality attributes must it possess? (performance, reliability, usability, etc.)
- What are the constraints? (legal, technical, budget, time)
- Who is responsible for what? (roles, responsibilities, sign-offs)

---

### Statement of Work (SOW)

- Usually one of the first documents created.
- Assigns responsibilities: who builds, tests, approves, pays, and reports.
- Defines how and when changes are authorized.

**Example:**

> “Vendor shall deliver prototype by 30 June. Customer shall review & provide feedback by 14 July. Payment 30% at prototype delivery, 50% at beta, 20% on final acceptance.”

---

### Requirements Specification

A good requirements specification should include:

- Context: environment, user base, systems it interacts with.
- Identification of internal vs. external parts (system boundaries).
- Functional requirements: what the system must do.
- Constraints: technical, legal, budget, schedule.
- Technical, cost, and schedule estimates.
- Quality attributes (non-functional requirements).
- Prioritization: essential vs. optional requirements.

---

### After Development / Longevity of Documentation

- Documents may be reused after system delivery for maintenance, audits, or future enhancements.
- Frequency of reuse depends on domain: highly regulated or mission-critical systems reuse heavily; smaller or agile projects less so.
- Value: orientation, onboarding, bug fixing, compliance, and change management.
- Improvements: lighter-weight docs, better traceability, living documents, linking with test plans & architecture, keeping them updated.

---

## Examples

**User Story (Agile):**

> _As a_ registered user, _I want_ to reset my password via email link _so that_ I can regain access when I forget it.  
> **Acceptance criteria:** email link expires in 30 minutes; link is HTTPS; user is notified of successful reset.

**ConOps snippet:**

> “In operational environment, students will access the system via browser on school-provided devices between 8-16h; in case of network outage, system should degrade gracefully to cached mode for read-only tasks.”

**Prioritization in SRS:**

> Must have: user authentication, course scheduling, report generation.  
> Should have: automated reminders, multi-language support.  
> Optional: dark-mode UI, third-party integrations.

---

## Sources

- Atlassian: User Stories & Epics definitions, examples.  
  [https://www.atlassian.com/agile/project-management/epics](https://www.atlassian.com/agile/project-management/epics)
- Agile Business Consortium / DSDM framework: Requirements and User Stories definitions, guidelines.  
  [https://www.agilebusiness.org/dsdm-project-framework/requirements-and-user-stories.html](https://www.agilebusiness.org/dsdm-project-framework/requirements-and-user-stories.html)
- ServiceNow: Writing effective user stories, including acceptance criteria.  
  [https://www.servicenow.com/docs/bundle/zurich-it-business-management/page/product/agile-development/concept/how-to-write-stories.html](https://www.servicenow.com/docs/bundle/zurich-it-business-management/page/product/agile-development/concept/how-to-write-stories.html)
- Academic studies: Documenting Non-Functional Requirements in Agile; test cases as requirements artifacts.  
  [https://arxiv.org/abs/1711.08894](https://arxiv.org/abs/1711.08894)

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
