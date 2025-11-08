---
parent: Release
title: Incentives
nav_order: 2
layout: default
---

# Part III – Contracts, Incentives, and Estimation Limits

_adapted from Miranda, 2104_

---

## 1. Incentives and Economic Motivation

**Why clients accept less and developers do more**  
- Sellers (vendors/employees) want maximum payment for minimum delivery.  
- Buyers want maximum delivery for minimum payment.  
- Balanced incentives align both parties.  
- Goal: reward delivery beyond the “Must Have” scope.

---

## 2. Contract Example

**Assumptions**  
- Time box = 4,000 h @ $100/h → $400,000 cost  
- Target margin 30% → price = $520,000  
- Must = 2,000 h (p≈1.0), Should = 1,000 h (p≈0.5), Could = 1,000 h (p≈0.25)

### 2.1 Fixed Price with Incentives

| Deliverables | Client Pays (K$) | Gross Margin |
|:-------------|:----------------:|:------------:|
| Must only    | 400              | 0 %          |
| + Should     | 500              | 25 %         |
| + Could      | 550              | 38 %         |

### 2.2 Fixed Price with Penalties

Client pays less if fewer deliverables are completed.

---

## 3. Employee Incentives

- Tie bonuses to release completion, not overtime.  
- Encourage productivity and ownership.  
- Non-monetary rewards: training, recognition, or time off.

---

## 4. Estimation and Uncertainty

### 4.1 Two- vs Three-Point Estimates

Using only worst-case estimates is conservative — you might safely promise more with PERT-style estimates.

### 4.2 Independent vs Correlated Effort Variables

When all tasks share a common cause of error (e.g., underestimated complexity), total effort behaves like the **sum of worst cases**.

#### Figure 4 – Correlated vs Independent Effort Distributions

```
Independent → small total variance → optimistic OK
Correlated  → large total variance → acts like sum of worst cases
```

---

## 5. Summary and Key Takeaways

- **Buffered MoSCoW** = simple, reliable prioritization method.  
- Captures customer preferences and manages uncertainty.  
- “Must Have” scope constrained by estimate confidence.  
- Partial delivery must be acceptable in contracts.  
- Employee engagement prevents free riding.  

| Principle                  | Meaning                                         |
|:---------------------------|:-----------------------------------------------|
| **Scope flexes, time does not** | Maintain delivery rhythm; reduce stress.   |
| **Plan for uncertainty**        | Use buffers to absorb estimation error.     |
| **Align incentives**            | Reward realistic, incremental success.      |
| **Transparency and learning**   | Track buffer use; refine estimates over time.|

#### Figure 5 – Release Planning Cycle

```
Rank features → Estimate effort → Allocate Must/Should/Could →
Execute within time-box → Review → Adjust priorities for next release
```

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.