---
parent: Materials
title: TRS Critical Path
nav_order: 4
layout: default
---


## 1. Time Reporting System – Critical Path and Critical Chain
_Adapted from Eduardo Miranda (2013)_

### 1.1 Context

Your company is developing the **Time Reporting System (TRS)** — a web-based application allowing employees to report hours worked on different projects so that customers can be billed.  
You are managing the **first increment**, which must demonstrate the core time reporting capabilities.

A preliminary list of development and integration activities is available below.  
Your team must plan, analyze, and improve the schedule using **Critical Path** and **Critical Chain** concepts.

---

### 1.2 Objectives

By completing this case study, your group will:

1. Build and analyze the **activity network** for the TRS increment.
2. Identify the **critical path** and compute float/slack values.
3. Propose **schedule improvements** applying the **Critical Chain method**, focusing on:
    - Resource contention and multitasking
    - Use of buffers (project, feeding, resource)
    - Task sequencing and prioritization
4. Reflect on how the proposed improvements would affect schedule reliability and delivery performance.

---

### 1.3 Case Inputs

The project team has identified the following tasks and feature developments.  
The **duration** and **effort** are estimated based on a standard development team working 8-hour days.

- **Feature development**
    - Each feature will be separately scheduled to facilitate tracking and reprioritization
    - Features duration, and effort are listed in **Table 1**
- **Integration** will be conducted in parallel with development

#### Table 1. Project Activities, Effort, and Duration

| Activity / Feature                | Effort (person-hours) | Duration (days) |
|-----------------------------------|----------------------|-----------------|
| **Requirements review**           | 16                   | 2               |
| **Increment design**              | 80                   | 5               |
| **Design review**                 | 24                   | 1               |
| **System test case design**       | 40                   | 5               |
| **System test execution**         | 16                   | 2               |
| **Update documentation**          | 24                   | 3               |
| **Conduct demonstration**         | 24                   | 1               |
| **Fix remaining problems**        | 24                   | 1               |
| **Feature: Login**                | 24                   | 3               |
| **Feature: Authorize Employee**   | 24                   | 3               |
| **Feature: Remove Authorization** | 24                   | 3               |
| **Feature: Block Employee**       | 24                   | 3               |
| **Feature: Reset Employee Password** | 24                | 3               |
| **Feature: Create Pay Code**      | 24                   | 3               |
| **Feature: Create Charge Authorization** | 40            | 5               |
| **Feature: Report Time**          | 40                   | 5               |
| **Feature: Submit Time Sheet**    | 32                   | 4               |
| **Feature: Approve Time Sheet**   | 32                   | 4               |

> 💡 **Note:** Dependencies are **not provided**. Your team must determine a logical order of execution for development, integration, and testing.

---

### 1.4 Tasks

#### 1.4.1 Model the Activity Network

- Define reasonable dependencies between tasks and features.
- Construct a dependency table, network diagram, or Gantt chart showing your assumptions.

#### 1.4.2 Calculate the Critical Path

- Compute Early Start (ES), Early Finish (EF), Late Start (LS), and floats (Free and Total).
- Identify and highlight the **critical path**.

#### 1.4.3 Analyze Schedule Risks

- Discuss potential issues such as task coupling, parallelism, and resource conflicts.
- Identify where multitasking or bottlenecks might occur.

#### 1.4.4 Apply the Critical Chain Method

- Assume that development and testing share limited resources.
- Suggest how to introduce **buffers**:
    - **Project buffer** at the end of the chain
    - **Feeding buffers** on non-critical paths
    - **Resource buffers** for constrained roles
- Propose how to monitor buffer consumption and project progress.

#### 1.4.5 Recommend Improvements

- Summarize how applying **Critical Chain principles** (focus, buffer management, elimination of multitasking) could improve:
    - Predictability
    - Lead time
    - Team throughput

#### 1.4.6 Deliverables

- Dependency table or network diagram
- Gantt chart
- Table of calculated schedule attributes (ES, EF, LS, floats)
- 15 minutes presentation (white background, bullet points, Minto style)
- 5 pages (max) report explaining:
    - Your dependency rationale
    - Critical path findings
    - Critical Chain adjustments
    - Expected impact on performance

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.