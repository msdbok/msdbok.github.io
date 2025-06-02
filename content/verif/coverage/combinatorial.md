---
title: Combinatorial
parent: Coverage
nav_order: 5
layout: default
---

## Combinatorial Coverage

### Definition

Tests combinations of input values or conditions, especially useful when decisions are based on **multiple predicates**.

* **All Combinations**: Every possible combination of inputs is tested (exhaustive).
* **Pairwise Testing**: Every **pair** of input values occurs in at least one test.

### Advantages

* Systematic and covers interactions between inputs
* Reduces number of test cases vs full combination

### Disadvantages

* Full combination is exponential in number of inputs
* Assumes equal importance for all combinations

### Example

Conditions: A, B, C (Boolean)

**All combinations (2³ = 8):**

```text
A B C
-----
F F F
F F T
F T F
F T T
T F F
T F T
T T F
T T T
```

**Pairwise combinations (e.g.):**

```text
A B C
-----
F F F
F T T
T F T
T T F
```

✅ Covers all pairs (A-B, A-C, B-C)

---

