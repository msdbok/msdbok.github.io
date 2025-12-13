---
parent: Planning
title: Milestones
nav_order: 2
layout: default
---

# Milestone Planning

_Adapted from Eduardo Miranda (2014)_

---

## 1. What Is a Milestone

A **milestone** is an **outcome or state** —  
**verifiable** and **relevant to the project sponsor** —  
that results from completing one or more tasks which the project should **reach or deliver by a specific time**.

**Examples**

- **Outcome:** a document, a partial or total system capability
- **Desired state:** an approval or measurable attainment (e.g., throughput, number of users trained)

**Milestone planning** defines:

1. The **order** in which outcomes or states must occur
2. The **dates** by which they must be achieved

This plan is what **sponsors and stakeholders** should see and use to track progress.  
If a milestone’s **date** or **success criteria** change, the plan must be **re-negotiated** and the change made **visible**.

---

## 2. Not Milestones – Bad Examples

### 2.1 Iterations Sequence

```mermaid
graph LR
    A["Iteration 1"] --> B["Iteration 2"] --> C["..."] --> D["Iteration n-1"] --> E["Iteration n"]
    style A fill:#bfbfbf,stroke:#999
    style B fill:#bfbfbf,stroke:#999
    style C fill:#bfbfbf,stroke:#999
    style D fill:#bfbfbf,stroke:#999
    style E fill:#bfbfbf,stroke:#999
```

**Why not milestones?**

Iterations mark **timeboxes of work**, not **verifiable outcomes**.  
Completing “Iteration 2” just ends a cycle — it doesn’t mean the project achieved something the sponsor can verify.

- **No clear outcome:** “Iteration complete” isn’t tangible
- **Not verifiable:** Sponsors can’t confirm progress
- **Process-focused:** Tracks _effort_, not _achievement_

**Good milestone examples:**  
“Prototype approved by client” or “Core capability demo completed.”

---

### 2.2 Development Phases

```mermaid
graph LR
    A["High level design"] --> B["Low level design"] --> C["Code & unit testing"] --> D["Integration"] --> E["System testing"]
    style A fill:#ff3b30,stroke:#c00,color:#fff
    style B fill:#0066ff,stroke:#0033aa,color:#fff
    style C fill:#bb33ff,stroke:#660099,color:#fff
    style D fill:#00c37a,stroke:#007a4f,color:#fff
    style E fill:#002b6f,stroke:#001d4f,color:#fff
```

Phases describe **activities**, not **project states**.

- **Activity-oriented:** “Low-level design done” is internal work, not a verified deliverable
- **Not sponsor-relevant:** Reflects _how_ the team works, not _what_ the sponsor gets
- **No clear success criteria:** Completion is subjective

**Good milestone examples:**  
“System design approved,” “Beta version deployed,” “Acceptance test passed.”

---

## 3. A Better Example – Sponsor-Oriented Plan

| **Date** | **Client** | **Team** | **Milestone Description** |
|---|---|---|---|
| Oct-1 | ⬤ | | Project kick-off |
| Nov-15 | ⬤──▶ | | Design concept approved |
| Nov-30 | | ⬤ | Infrastructure selected |
| Dec-15 | | ⬤ | Design completed |
| Jan-30 | | ⬤ | Release 1: CL*, BD, AC, CO, Data Base |
| Feb-15 | ⬤──▶ | | Cloud infrastructure available |
| Mar-1 | | ⬤ | Release 2: CBL, RC, SM |
| Mar-10 | | ⬤ | Beta testing launched |
| Mar-30 | ⬤──▶ | | Beta testing results reviewed |
| Apr-15 | | ⬤ | Release 3: PD, PP |
| Apr-20 | ⬤──▶ | | Acceptance testing procedure approved |
| May-15 | | ⬤ | Acceptance test completed |
| May-30 | | ⬤ | System deployed |
| Jun-30 | ⬤ | | Customer sign-off |
| _* Features listed in the WBS_ | | | |

**Why this works**

- **Outcome-oriented:** Each milestone marks a verifiable state (e.g., “Design concept approved”)
- **Verifiable:** Sponsors can see tangible proof (documents, software, approvals)
- **Stakeholder-focused:** Represents business value, not internal effort
- **Transparent:** Any change in dates or criteria must be re-negotiated and visible

---

## 4. Activity Planning vs Milestone Planning

| **Aspect** | **Activity Planning** | **Milestone Planning** |
|---|---|---|
| **Definition** | Decomposes project into tasks and their execution order | Breaks project into logical states or outcomes |
| **Requires** | Detailed project knowledge | High-level outcome understanding |
| **Volatility** | Highly volatile | Relatively stable |
| **Focus** | Task execution | Deliverables, approvals, commitments |
| **When used** | Later in lifecycle | Early in lifecycle |

**In short:**  
_Activities_ describe what the team **does**.  
_Milestones_ describe what the project **achieves and can verify**.

---

### 4.1 Example

| **Milestones** | **Activities** |
|---|---|
| Statement of Work signed | Identify requirements <br> Document major deliverables <br> Negotiate termination conditions <br> Write SOW <br> Legal review |
| Architecture approved | Perform Quality Attribute Workshop <br> Identify architectural drivers <br> Design <br> Study trade-offs <br> Review document |
| “Must-have” features completed | Design <br> Code <br> Test <br> Integrate |

---

## 5. Milestone Plan Semantics

- Milestone dependencies are often **Finish-to-Finish (FF)**
- To reach Milestone 4, the project must have reached the **state** of Milestone 2
- Tasks for Milestone 4 can start **before** all work in 2 is done

```mermaid
graph LR
    %% Finish-to-Finish (FF) dependencies between milestones
    M1(("1<br/>Hard<br/>Milestone")) -.-> M2(("2<br/>Soft<br/> Milestone"))
    M1 -.->  M3(("3<br/>Hard<br/>Milestone"))
    M2 -.->  M3
    M2 -.->  M4(("4<br/>Hard<br/>Milestone"))
    M3 -.->  M5
    M4 -.->  M5(("5<br/>Hard<br/>Milestone"))   
    %% Styling
    style M1 fill:#ff4d4d,stroke:#c00,color:#fff
    style M2 fill:#ffffff,stroke:#ff4d4d,stroke-dasharray:4 2
    style M3 fill:#ff4d4d,stroke:#c00,color:#fff
    style M4 fill:#ff4d4d,stroke:#c00,color:#fff
    style M5 fill:#ff4d4d,stroke:#c00,color:#fff
```

---

## 6. Defining a Milestone Plan

```mermaid
flowchart TD
  %% Compact Milestone Planning (grouped)

  subgraph G1["Define scope & order"]
    direction LR
    A1["Identify outcomes<br/>(milestones)"] --> A2["Sequence them"]
  end

  subgraph G2["Commit dates"]
    direction LR
    B1["Add resource demands<br/>and <b>hard</b> dates"] --> B2["Add <b>soft</b> milestone dates"]
  end

  subgraph G3["Protect & refine"]
    direction LR
    C1["Add buffers"] --> C2["Iterate"] --> C3["<i>(Optional)</i> planning waves"]
  end

  G1 --> G2 --> G3

  %% Styling
  classDef step fill:#fff7d6,stroke:#f39c12,stroke-width:1.5px,color:#333;
  classDef hard fill:#ffe8e6,stroke:#e74c3c,stroke-width:2px,color:#2c3e50;
  classDef soft fill:#e8f4ff,stroke:#1f78d1,stroke-dasharray:6 3,stroke-width:2px,color:#2c3e50;

  class A1,A2,C1,C2,C3 step;
  class B1 hard;
  class B2 soft;
```

---

## 7. Before Starting

### 7.1 What Is Needed

- The **outcome** or **state** to be achieved (think WBS)
- The **evaluation criteria** to judge realization (exit criteria or Definition of Done)
- A **delivery date**
    - **Hard date:** imposed by a third party or loses value if late
    - **Soft date:** mutually agreed and flexible
- The **beneficiary or area of work**
- The **individual or organization** responsible for the milestone (think resource plan)

---

## 8. Milestone Exit Criteria / Definition of Done

**Origin:**

- Based on **ETVX (Entry, Task, Verification, eXit)**, Radice et al. (1985)
- Reintroduced by Agile as **Definition of Done (DoD)** around 2006

**DoD must be objectively decidable**, and includes:

- List of work items to be completed
- State or quantity to achieve
- Defined quality level, such as:
    - Acceptable bug counts
    - Quality attributes at required levels
    - Passing specific test cases
    - Reaching required test coverage

---

### 8.1 Example – Evolving Definition of Done

_Source: Sumeet Madan, 2019 ([https://www.scrum.org/](https://www.scrum.org/resources/blog/done-understanding-definition-done))_

| **Initial DoD** | **Mature DoD** | **Stringent DoD** |
|---|---|---|
| **All acceptance criteria met** | **All business functionality and acceptance criteria met** | **All business functionality and acceptance criteria met** |
| Unit test coverage > 85% | **No dependence unattended** | **No dependence unattended** |
| Functional test passed | Unit test coverage > 85% | No build failures |
| No known defects | No coding-standard errors | Integration testing passed |
| Peer code review | Technical debts < 5 days (subjective) | Unit test coverage > 85% |
| Peer code review passed | Maintainability index > 90 | No coding-standard errors |
| Documentation completed | Functional test automation > 75% | Technical debts < 5 days (subjective) |
| | Functional test passed | Maintainability index > 90 |
| | No known defects | Functional test automation 75% |
| | Peer review passed | Functional test passed |
| | Documentation completed | Regression, PEN, Load, and Performance tests passed |
| | | No known defects |
| | | Peer review passed |
| | | Documentation completed |
| | | Compliance and regulatory documents complete |
| | | UAT approved |

---

## 9. Guidance: Milestone Selection

Milestones must be:

- **Specific** – clearly defined outcome
- **Verifiable** – objectively measurable
- **Relevant** – meaningful to sponsor or customer
- **Timely** – achieved at the right moment in the schedule

**Typical examples**

- Life Cycle Objective (LCO)
- Life Cycle Architecture (LCA)
- Core Capability Demo (CCD)
- Initial Operational Capability (IOC)
- Incremental deliveries
- Proof-of-concept demos
- Key documents completed
- Technical performance levels reached
- Risk mitigation actions done
- Stakeholder commitments fulfilled

---

## 10. Creating the Resource Plan

- Draw the **resource-use curve** over time, _y = f(t) = number of FTEs_
- The **area under the curve** equals total effort
- Account for **holidays, absences, and training**
- Match **available skills** to **task needs**

---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.

---

## Sources

- Radice, R. A., et al. "A Programming Process Architecture." *IBM Systems Journal*, vol. 24, no. 2, 1985, pp. 79–90.

- Madan, Sumeet. "Done - Understanding Definition of Done." *Scrum.org*, 2019. [https://www.scrum.org/resources/blog/done-understanding-definition-done](https://www.scrum.org/resources/blog/done-understanding-definition-done)

- Miranda, Eduardo. *Managing Software Development*. Lecture materials, 2014.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.