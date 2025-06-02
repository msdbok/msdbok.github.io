---
title: Multiple Conditions
parent: Coverage
nav_order: 4
layout: default
---


## Modified Condition/Decision Coverage (MC/DC)

### Definition

MC/DC requires that:

* Each **condition** in a decision has been shown to **independently affect** the decision's outcome.

Formally:

> Each condition in a decision has been shown to independently affect the outcome of the decision by varying just that condition while holding others constant.

### Motivation

* Stronger than simple branch coverage
* Used in **safety-critical systems** (e.g., aviation, automotive)

### Advantages

* Reveals errors in individual conditions within decisions

### Disadvantages

* Requires careful test case design
* More complex to analyze

### Example

**Decision:**

```fortran
if (A and B) then
    action
end if
```

To satisfy MC/DC:

* Show that **A** affects the outcome:

  * A = T, B = T → true
  * A = F, B = T → false
* Show that **B** affects the outcome:

  * A = T, B = T → true
  * A = T, B = F → false

**Test suite:**

* (A=T, B=T), (A=F, B=T), (A=T, B=F)
  ✅ Satisfies MC/DC

**CFG:**

```mermaid
flowchart TD
  Start((Start))
  D1{ A and B }
  S1[ action ]
  End((End))

  Start --> D1
  D1 -->|true| S1 --> End
  D1 -->|false| End
```

---

## Mutation Coverage

### Definition

Mutation testing introduces small changes (mutants) into the code and checks whether the existing test suite detects them.

**Goal:**
Check if test suite can "kill" mutants — i.e., produce different output from the original.

### Types of Mutation

```mermaid
flowchart TD
  MUT[Mutation Testing]
  Strong["Strong Mutation"]
  Firm["Firm Mutation"]
  Weak["Weak Mutation"]
  MUT --> Strong --> Firm --> Weak
```

* **Strong Mutation**: Test must cause a mutant to produce different output.
* **Firm Mutation**: Weaker than strong; detection at intermediate state.
* **Weak Mutation**: Only requires the mutant to reach a different internal state.

### Advantages

* Measures fault-detection ability of tests
* Can reveal test suite weaknesses

### Disadvantages

* Computationally expensive
* Mutant generation and analysis are complex

### Example

**Original code:**

```fortran
if x > 0 then
    y = 1
end if
```

**Mutant:**

```fortran
if x >= 0 then
    y = 1
end if
```

Test case: `x = 0`
✅ Kills the mutant (original skips, mutant executes)

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

## References

* \[Beizer 1990] Boris Beizer, *Software Testing Techniques*, 2nd ed.
* \[Roper 1994] Marc Roper, *Software Testing*
* \[McCabe] Thomas McCabe, *A Complexity Measure* (1976)
* \[RTCA DO-178C] Software Considerations in Airborne Systems and Equipment Certification

