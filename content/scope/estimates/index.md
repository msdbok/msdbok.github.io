---
parent: Scope
title: Estimates
nav_order: 3
layout: default
---

# Software Estimation Techniques

_* adapted from Miranda, 2014_

## 1. What Estimation Answers

Estimation helps us answer two core questions:

- **How big is it?** → _Sizing the system_ (e.g., number of features, modules, function points)
- **How much effort is needed?** → _Effort and cost estimation_ (staff months, budget)

Estimation converts **scope** into **resources and time**.

---

## 2. Two Basic Estimation Strategies

| Approach      | Process                                                      | Strengths                   | Weaknesses                      | Example                                              |
|---------------|--------------------------------------------------------------|-----------------------------|----------------------------------|------------------------------------------------------|
| **Bottom-Up** | Estimate cost/effort for each component, sum them, check total. | Accurate when WBS is detailed. | Time-consuming; depends on detailed scope. | Estimating each microservice and summing total developer hours. |
| **Top-Down**  | Start with total project budget → allocate to major subsystems → refine. | Fast; useful early in planning. | Risk of unrealistic breakdowns. | Management fixes total budget ($500k) and allocates to phases. |

Both require sanity checks: overhead, contingency, and lifecycle coverage (e.g., testing, maintenance).

---

## 3. Categories of Estimation Approaches

### (a) Judgment or Expert-Based Estimation

Estimation based on **experience and intuition**.

- **Unaided**: relies purely on expert intuition (e.g., senior engineer says “6 months”).
- **Structured**: uses formal elicitation and combination methods:
    - **Wideband Delphi** – iterative group consensus.
    - **Planning Poker** – agile team estimation.
    - **Paired Comparison** – experts rank or compare tasks pairwise.

_Example:_ Estimating sprint backlog effort using Planning Poker.  
_Use When:_ Project has little data, early stage planning.

---

### (b) Engineering Approaches

Estimate by **analyzing what drives effort**—build from known process characteristics.

_Example:_ Training project  
> Number of users × Hours per class × Locations + Fixed setup costs.

Used when no past project data exists.

_Variants:_
- **Process-based cost modeling** (breakdown by activities such as design, coding, testing).

_Use When:_ Understanding process mechanics is easier than collecting data.

---

### (c) Counting Approaches

Quantify system size via measurable functional elements.

| Technique         | Measure                                 | Example                                 |
|-------------------|-----------------------------------------|-----------------------------------------|
| Function Points   | User-visible inputs/outputs, files, interfaces | 10 inputs × 4 + 5 outputs × 5 → FP total |
| COSMIC Points     | Functional data movement                | Used in modern distributed systems      |
| Use Case Points   | Number and complexity of use cases      | UML-based                              |
| Web Object Points | Pages, scripts, media                   | Web apps                               |
| Test Points       | Test cases and complexity               | QA planning                            |

_Use When:_ Early requirement specs are available.

---

### (d) Industry Norms

Based on **historical distributions** across projects.

Typical averages:

- Requirements: 15%
- Design: 10%
- Coding: 35%
- Testing: 40%

Also includes **Function Point Backfiring**: converting function points to LOC based on historical ratios.

_Use When:_ Benchmarking effort allocation.

---

### (e) Analogy-Based Estimation

Estimate by comparing with **similar past projects**.

1. Find analog projects.
2. Adjust based on similarity.
3. Average or cluster results.

Variants:

- **Proxy-Based Estimation (PROBE)** in the _Personal Software Process_ (Humphrey)
- Academic systems: ESTOR, ACE, ANGEL use clustering.

_Example:_ A mobile app project estimated by comparing with a similar past app.  
_Use When:_ Reliable database of past projects exists.

---

### (f) Parametric Models

Statistical models linking effort to measurable drivers (Cost Estimation Relationship, CER).

**General Form:**  
Effort = a × (Size)^b × Π(cost drivers)

Famous examples:

- **COCOMO II** (Boehm): Effort = a × (KLOC)^b × EAF  
    _(EAF = effort adjustment factors like reliability, complexity)_
- **SLIM (Putnam)** – uses Rayleigh curve of manpower distribution.

_Example:_  
If estimated size = 20 KLOC, COCOMO predicts ~50 person-months.

_Use When:_ Large dataset available; detailed drivers known.

---

## 4. Comparison Summary

| Category    | Data Needed          | Typical Accuracy | Example Methods         | Best Used When         |
|-------------|---------------------|------------------|------------------------|------------------------|
| Judgment    | Expert opinion      | Low–Medium       | Delphi, Planning Poker | Early stages           |
| Engineering | Process decomposition| Medium           | Activity-based         | New, data-poor projects|
| Counting    | Measurable features | Medium–High      | Function Points        | Defined requirements   |
| Industry Norms | Historical ratios | Low              | Effort % by phase      | Benchmarking           |
| Analogy     | Similar projects    | High             | PROBE                  | Stable organization    |
| Parametric  | Statistical models  | High             | COCOMO, SLIM           | Mature data sets       |

---

## 5. Combining Techniques

In practice, estimators combine methods:

- Use **expert judgment** to calibrate **parametric models**.
- Use **counting** to size and **COCOMO** to predict effort.
- Apply **analogy** for cross-checks.

---

## 6. Example Integration

Suppose a company estimates a CRM system:

- Function points = 350 → size-based estimate.
- Apply COCOMO → 75 person-months.
- Experts adjust for complexity (+10%) → 83 PM.
- Add 15% contingency for uncertainty → final = 95 PM.

---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.

---

## Sources

- Miranda, Eduardo. *Managing Software Development*. Lecture materials, 2014.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.
