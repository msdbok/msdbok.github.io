---
title: Planning
nav_order: 6
layout: default
---

# Introduction to Project Planning

_*Adapted from Eduardo Miranda (2014)_

---

## 1. Introduction: Why Planning? What Is Planning?

### 1.1 When Software Projects Go Bad

Software projects fail for many recurring reasons:

- **Lack of coordination** — teams work in isolation or at cross purposes.
- **Lack of planning** — no clear view of dependencies or priorities.
- **Lack of leadership** — unclear ownership or direction.

Good planning aims to **prevent these breakdowns** by aligning people, resources, and expectations.

---

### 1.2 Working Effectively as a Team

Effective teamwork depends on **coordination** — aligning the work of all individuals toward a common goal.

To achieve this, teams must:

- Understand the shared goal.
- Combine efforts efficiently.
- Fit all tasks together smoothly.
- Avoid bottlenecks or disruptions.
- Aim precisely for the agreed outcome.

> _“Coordination!... and not so much…” — a reminder that good teams act in sync._

---

### 1.3 How Coordination Happens

Coordination can occur through **hierarchies**, **shared artifacts**, and **communication**.

| **Reference to a Higher Level** | **Shared Representations** | **Communication** |
|---|---|---|
| Project manager | Code repositories | Meetings |
| Chief programmer teams | Kanban boards | Informal chats |
| Surgical teams | Posting test results | Stand-ups |
| Preparation and plans | “Living” documents | |
| Specifications and processes | | |

> Adapted from J. Herbsleb (2009), _Coordination and Congruence in Global Software Development._

---

### 1.4 Why We Plan

We plan not just because methodology requires it, but because planning:

- Clarifies **how** work will be done and coordinated.
- Estimates **how much** time and cost are needed.
- Communicates **when** results are expected.
- Lets stakeholders align their own plans.
- Defines the **impact of changes** on previous commitments.

> Planning converts knowledge and scope into coordinated action.

---

### 1.5 What Makes a Good Plan

A good plan shares qualities of a good program — it should be:

| **Property** | **Description** |
|---|---|
| **Free from Errors** | Internally consistent, no contradictions. |
| **Reliable** | No “race conditions” — dependencies are realistic. |
| **Extensible & Modifiable** | Can adapt as new information appears. |
| **Robust** | Handles uncertainty or changes gracefully. |
| **Efficient** | Not overly complex for the team’s needs. |
| **Manageable & Auditable** | Traceable, measurable, reviewable. |
| **Usable & Accessible** | Clear to all key stakeholders. |

> The purpose of planning is to **enable learning and adaptation**, not to freeze change.

---

### 1.6 What Is Planning?

Planning is the process of creating **documented agreements** about how, when, and by whom work will be done.

It defines:

- **Commitments** (who will do what, by when)
- **Dependencies** (how parts fit together)
- **Constraints** and **assumptions**
- **Expected outcomes**

> In short, planning aligns knowledge, effort, and responsibility.

---

## 2. Predictive vs. Agile Planning

Planning approaches differ in how they coordinate work and respond to change.

---

### 2.1 Emphasis on Predictability vs. Fast Turnaround

| **Characteristic**    | **Waterfall**              | **Spiral**                 | **Iterative**      | **Scrum**               |
| --------------------- | -------------------------- | -------------------------- | ------------------ | ----------------------- |
| **Defined processes** | Required                   | Required                   | Required           | Planning & closure only |
| **Final product**     | Determined during planning | Determined during planning | Set during project | Set during project      |
| **Project cost**      | Determined during planning | Partially variable         | Set during project | Set during project      |
| **Completion date**   | Determined during planning | Partially variable         | Set during project | Set during project      |

> Waterfall and Spiral emphasize **predictability**, while Iterative and Scrum emphasize **fast turnaround** and adaptability during execution.

---

### 2.2 The Plan: A Set of Documented Agreements

| | Predictive approaches | | Agile approaches (Scrum) | |
| ------------------------------------ | ------------------------------- | -------------------------------- | ------------------------------------------------------ | ---------------------------------------- |
| **Decision** | **Artifact** | **When** | **Artifact** | **When** |
| **What deliverables?** | Work breakdown structure (WBS) | Beginning of project (BOP) | Product Backlog | BOP (and later) |
| **When will they be delivered?** | Milestone plan | BOP | Item priority.  No firm commitment as to delivery date | Sprint Planning Meeting |
| **What tasks?** | WBS | BOP and at planning waves | Sprint backlog | Sprint Planning Meeting |
| | | | | |
| **When will the tasks be executed?** | Activity network, Gantt chart | BOP and at planning waves (Push) | Sprint Commitment | When a resource becomes available (Pull) |
| **How many people? When?** | Staffing plan | BOP | Cross-functional, fixed size team | BOP |
| **Who will do it?** | OBS,  <br>Responsibility matrix | BOP | Task board (Pull) | Scrum meeting |

---

### 2.3 Tracking: Where Are We in Relation to Where We Planned to Be?

| Concern          | Predictive approaches                                   |                        | Agile approaches <br>(Scrum)                            |               |
| ---------------- | ------------------------------------------------------- | ---------------------- | -------------------------------------------------------- | ------------- |
|                  | Artifact                                                | When                   | Artifact                                                 | When          |
| **Overall progress** | Milestone chart, Earned value                           | Reporting period       | Release burn-down chart                                  | End of Sprint |
| **Weekly/Daily**     | Activity plans, time reports, action items, bug reports | Project status meeting | Burn-down chart, Task board                              | Scrum meeting |
| **Expenses**         | Earned value                                            | Reporting period       | Actual effort is not tracked. Assumed to be 8h/day/person |               |

---

### 2.4 Coordination Emphasis

| **Approach** | **Primary Coordination Means** | **Goal** |
|---|---|---|
| **Predictive (Plan-Driven)** | Preparation, structure, defined roles | Predictability and control |
| **Agile (Adaptive)** | Shared artifacts, communication | Responsiveness and collaboration |

> Adapted from Sutherland & Schwaber (2007), _The Scrum Papers._

---

### 2.5 Comparing Planning Philosophies

| **Dimension** | **Predictive Approach** | **Agile Approach** |
|---|---|---|
| **Main reliance** | Documentation and preparation | Communication and shared visibility |
| **Control style** | Centralized and formal | Distributed and collaborative |
| **Planning timing** | Mostly up-front | Continuous and iterative |
| **Typical tools** | Gantt charts, baselines, formal reports | Backlogs, Kanban, stand-ups |
| **Goal** | Predictability | Adaptability |

Both approaches aim for coordination — they just use **different mechanisms** to achieve it.

---

### 2.6 The Role of the Plan

A plan is not a rigid prediction; it is a **shared commitment**.

It captures:

- What has been agreed upon
- How progress will be measured
- How changes will be evaluated

> A good plan helps manage expectations — it doesn’t eliminate uncertainty, it makes it visible.

---

## 3. Overview of Major Stages in Planning

Planning is part of a **continuous cycle**:

> **Plan → Track → Report → Adjust**

---

### 3.1 Why We Track

Tracking asks:

> _“Where are we now compared to where we planned to be?”_

We track to:

- Detect and correct deviations early.
- Decide whether to continue, modify, or stop a project.
- Communicate current status to stakeholders.
- Support re-planning and forecasting.
- Enable evidence-based decisions.

Tracking supports both **control** and **learning**.

---

### 3.2 Planning, Tracking, and Reporting Activities

| **Activity** | **Purpose** | **Example Tools** |
|---|---|---|
| **Planning** | Define how work will be done | WBS, backlog, Gantt chart |
| **Tracking** | Measure progress and performance | Burndown chart, earned value, dashboards |
| **Reporting** | Communicate results and status | Stand-ups, reviews, status reports |

> These activities interact continuously to ensure the plan stays aligned with reality.

---

### 3.3 Example: Commitment and Activity Planning in Scrum

- **Commitment Planning:** The team agrees on a sprint goal and selects backlog items that fit the goal.
- **Activity Planning:** Tasks are broken down and tracked daily (boards, digital tools).
- **Tracking:** Burndown and velocity charts visualize progress.
- **Reporting:** Sprint reviews and retrospectives communicate results and insights.

> Agile projects still plan — they simply plan _more often_ and in smaller increments.

---

### 3.4 Example: Sponsor-Oriented Planning

A **sponsor-oriented plan** links technical progress with business value.

It should:

- Highlight outcomes, not just activities.
- Map milestones to sponsor deliverables.
- Show readiness for delivery, not just task completion.

> _Example: the “AmazonLite” project — a plan viewed from a sponsor’s perspective, focused on results, not just development steps._

---

### 3.5 A Few Final Points About Planning

- Planning requires **knowledge** — if it’s missing, take time to learn.
- The fact that you don’t know everything doesn’t mean you know nothing.
- Planning doesn’t prevent change; it helps assess and manage it.
- There are many ways to achieve the same result — but not all are equally good.

> Planning, tracking, and reporting form the backbone of **disciplined project learning**.

---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.

---

## Sources

- Herbsleb, James D. "Global Software Engineering: The Future of Socio-Technical Coordination." *Future of Software Engineering (FOSE '07)*, 2007, pp. 188–98. IEEE Xplore, https://doi.org/10.1109/FOSE.2007.11.

- Sutherland, Jeff, and Ken Schwaber. "The Scrum Papers: Nut, Bolts, and Origins of an Agile Framework." Scrum Inc., 2007. https://www.scruminc.com/scrumpapers.pdf

- Miranda, Eduardo. "Managing Software Development." Lecture materials, 2014.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.
