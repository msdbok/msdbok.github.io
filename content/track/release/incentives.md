---
parent: Release
title: Incentives
nav_order: 3
layout: default
---

# Contracts, Incentives, and Estimation Limits

_* adapted from Miranda, 2014_

---


## 1. Incentives and Economic Motivation

Release planning is not only a **technical** problem — it is also an **economic** one.  
Both the client and the development team have different motivations, and good contracts must **align their incentives**.

| Role                | Typical Motivation                        | Risk                          |
|---------------------|-------------------------------------------|-------------------------------|
| **Client / Buyer**  | Wants maximum delivery for minimum payment.| May push for too much too soon.|
| **Vendor / Developer** | Wants maximum payment for minimum delivery.| May underdeliver if unmotivated.|

If both sides act purely on these instincts, the project fails.  
The solution is to establish **balanced incentives** that reward both parties for realistic, productive collaboration.

**Goal:** Reward delivery beyond the “Must Have” scope — without punishing honest effort or uncertainty.

---

### 1.1 Example: Aligning Interests

A client contracts a team to build a **Customer Self-Service Portal**.  
The contract defines:

- A guaranteed **core feature set** (“Must Have”)
- Optional “enhancement features” (“Should” and “Could”) with delivery bonuses
- Shared risk: if delays occur, scope reduces but the schedule remains fixed

The team now has a reason to finish early — they can earn more by delivering enhancements.  
The client benefits too: they get a better product without unplanned time or cost increases.

---

## 2. Contract Example

This example shows how incentives can work in a **time-boxed project**.

### 2.1 Assumptions

- Time box = 4,000 hours @ $100/h → $400,000 cost
- Target gross margin = 30% → price = $520,000
- Delivery probabilities:
    - Must = 2,000 h (≈100%)
    - Should = 1,000 h (≈50%)
    - Could = 1,000 h (≈25%)

---

### 2.2 Fixed Price with Incentives

| Deliverables | Client Pays (K$) | Gross Margin |
|--------------|:----------------:|:------------:|
| Must only    | 400              | 0%           |
| + Should     | 500              | 25%          |
| + Could      | 550              | 38%          |

**Interpretation:**

- Base payment covers the “Must Have.”
- Each additional scope level (“Should,” “Could”) earns an extra payment.
- The client pays only for what they actually receive.

---

### 2.3 Fixed Price with Penalties

If the project underdelivers, the client pays less.  
For example:

- Delivering only “Musts” → $400K
- Missing “Musts” → no bonus and possible penalty

Balanced contracts include both **incentives** (for exceeding expectations) and **penalties** (for underperformance).

---

## 3. Employee Incentives

Just as contracts motivate suppliers, **teams** need incentives as well.

- Tie bonuses to **release completion**, not overtime.
- Encourage ownership and accountability.
- Offer **non-monetary rewards** such as:
    - Additional training
    - Recognition
    - Time off

**Principle:** Reward sustainable performance, not burnout.

---

## 4. Estimation and Uncertainty

Accurate estimation is central to release planning — but uncertainty is inevitable.  
Miranda distinguishes between two estimation concepts that strongly affect reliability.

### 4.1 Two- vs. Three-Point Estimates

- **Two-point estimates (nominal and worst-case)** are simple but conservative.
- **Three-point estimates (optimistic, nominal, pessimistic)** capture uncertainty statistically (e.g., PERT).

If all features are estimated using worst cases, the plan becomes overly cautious — leading to **undercommitment**.  
Three-point estimation allows better use of available time while maintaining realism.

### 4.2 Independent vs. Correlated Effort Variables

Estimation errors are rarely independent.  
If one task is underestimated, others often are too — due to shared complexity or environmental factors.

- **Independent estimates:** overruns and underruns balance out; total variance is small.
- **Correlated estimates:** all tasks slip together; total effort behaves like the _sum of worst cases._

#### Figure 4 – Correlated vs. Independent Effort Distributions

```
Independent → small total variance → optimistic OK
Correlated  → large total variance → behaves like sum of worst cases
```

Correlation between tasks increases project risk and should be countered by appropriate buffering.

---

## 5. Summary and Key Takeaways

The **Buffered MoSCoW** approach links **technical discipline** with **economic realism**.  
It provides a structured way to manage uncertainty, reward performance, and ensure fairness between clients and suppliers.

- Captures customer preferences while managing estimation uncertainty.
- Keeps delivery time predictable by allowing scope to flex.
- Uses buffers instead of padded estimates.
- Encourages incentive-driven, fair contracts.
- Promotes teamwork and shared responsibility.

### 5.1 Principles to Remember

| Principle                       | Meaning                                         |
|----------------------------------|------------------------------------------------|
| **Scope flexes, time does not**  | Protect delivery rhythm and avoid schedule slip.|
| **Plan for uncertainty**         | Use buffers and realistic estimates, not blind optimism.|
| **Align incentives**             | Ensure both client and supplier benefit from good performance.|
| **Transparency and learning**    | Track buffer usage and refine estimates over time.|

#### Figure 5 – The Release Planning Cycle

```
Rank features → Estimate effort → Allocate Must/Should/Could →
Execute within time-box → Review → Adjust priorities for next release
```


---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.