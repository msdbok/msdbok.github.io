---
parent: Tracking
title: Control
nav_order: 3
layout: default
---

#  Tracking

_* adapted from Miranda, 2104_

## 1. Purpose of Tracking

Tracking, or monitoring, is the process of **determining the current status** of a project. It answers questions like:

- Are we where we expected to be?  
- How much work has been completed?  
- How efficiently are we performing?

In project management, tracking creates the factual basis for control and reporting. Without reliable tracking, all other management activities are speculative.

> Core idea: Planning defines the path; tracking tells you whether you’re still on it.

---

## 2. Common Challenges in Tracking

### 2.1 The “When will we be finished?” problem

Project managers often face uncertainty in predicting completion because estimates are based on assumptions, not data. Tracking provides objective evidence to refine those estimates over time.

### 2.2 The “90% Complete” Syndrome

Many teams report they are “almost done” but stay at 90% forever. This happens when progress is assessed subjectively rather than by measurable deliverables. A task is _only complete_ when it meets its defined exit criteria — tested, reviewed, and accepted.

> Lesson: Progress must be measured quantitatively, not intuitively.

---

## 3. What to Track

Tracking focuses on five main dimensions:

| Dimension                 | Examples of Measures               |
| ------------------------- | ---------------------------------- |
| Progress                  | Milestones completed, earned value |
| Performance               | Schedule and cost variance         |
| People                   | Availability, workload, morale     |
| Product Quality          | Defect rates, test results         |
| Customer Satisfaction    | User feedback, complaints          |

A balanced tracking approach combines objective data and direct observation.

---

## 4. How to Track

### 4.1 Management by Walking Around (MBWA)

Managers should observe work directly, talk to people, and listen.

- Data dashboards reveal what is happening.  
- Conversations reveal why it is happening.

> A visible, approachable manager receives bad news sooner — which is far more valuable than getting good news early.

### 4.2 Overcoming Employee Silence

Silence can hide problems. Create a culture where team members can speak up about delays, quality concerns, or risks without fear. Psychological safety is a precondition for honest tracking.

---

## 5. Measurement: Reducing Uncertainty

Measurement is not about bureaucracy — it is about reducing uncertainty in decision-making. Even imperfect measures are better than ignoring factors because they seem unquantifiable.

### 5.1 Levels of Measurement

1. Nominal: Categories (defect types).  
2. Ordinal: Ordered classes (priority: high, medium, low).  
3. Interval: Numeric scale without true zero (temperature).  
4. Ratio: Numeric scale with zero (duration, cost).  
5. Absolute: Simple counts (number of bugs).

The level determines which analyses are valid.

---

## 6. What to Measure: SEI Core Measures

The Software Engineering Institute recommends a small set of core measures:

| Measure Type | Typical Metrics |
|--------------|------------------|
| Size         | Source lines of code (SLOC), Function Points |
| Defects      | Open/closed counts, defect density |
| Effort       | Planned vs. actual person-hours |
| Schedule     | Planned vs. actual milestones |

Use the Goal–Question–Metric (GQM) approach:
1. Define the Goal.  
2. Ask the Questions that reveal progress.  
3. Choose the Metrics that answer them.

---

## 7. Effort Tracking

Every recorded hour should be traceable:

- Project, deliverable, and task  
- Person and organization  
- Type of work (design, testing, rework, etc.)  
- Date and duration

This enables productivity analysis and supports earned value calculations later.

---

## 8. Leading and Lagging Indicators

- Leading indicators predict future outcomes (e.g., open defects, velocity trends).  
- Lagging indicators confirm results (e.g., total defects found, time to release).

A good tracking system uses both: lead indicators for proactive control, lag indicators for post-mortem learning.

---

## 9. Dashboards and Visual Indicators

Project dashboards consolidate key data in one view, combining progress, cost, and quality metrics.

Common visuals include:

- Milestone charts  
- Earned value curves (PV, EV, AC)  
- Burndown or burnup charts  
- Task boards or Kanban views  
- Trend reports

Dashboards are not for decoration — they help identify early warning signs.

---

## 10. Assessing Progress

Effort spent is not the same as progress made. True progress equals verified deliverables. A project may be busy but still behind schedule if its output is incomplete or defective.

Always relate “percent complete” to measurable outcomes — not to time spent.

---

## 11. Earned Value Management (EVM)

EVM integrates scope, schedule, and cost into one performance view.

Key terms:
- Planned Value (PV): What you planned to achieve.  
- Earned Value (EV): What you actually accomplished.  
- Actual Cost (AC): What you spent to do it.

Key formulas:
- Schedule Variance (SV) = EV − PV  
- Cost Variance (CV) = EV − AC  
- Schedule Performance Index (SPI) = EV / PV  
- Cost Performance Index (CPI) = EV / AC

If SPI or CPI < 1 → performance below expectation. If SPI or CPI > 1 → performance exceeds plan.

EVM allows managers to predict completion dates and final cost early.

---

## 12. Minimum Requirements for EVM

EVM only works if:
- Tasks and costs are clearly defined and scheduled.  
- Data is collected at the same granularity as the plan.  
- Rules exist for how value is “earned.”  
- Baseline changes are documented and controlled.

Without these, EVM results can mislead rather than inform.

---

## 13. Tracking Agile Projects

Agile projects use different but conceptually similar techniques:

- Burndown charts show remaining work.  
- Cumulative flow diagrams visualize stability and bottlenecks.  
- Task boards track progress by workflow state.

Agile tracking emphasizes flow and feedback, rather than predictive forecasting.

---

## 14. Testing and Fixing Metrics

Testing progress can be tracked by:
- Tests executed vs. planned  
- Pass/fail ratios  
- Defects discovered and fixed over time

Fix tracking looks at:
- Average time to fix  
- Defect backlog  
- Reopen rates

These metrics reflect both product quality and process efficiency.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.
