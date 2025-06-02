---
title: Multiple Conditions
parent: Coverage
nav_order: 4
layout: default
---


Here’s your slide content reformatted into clear, structured, and student-friendly study notes. I've explained key ideas, corrected grammar, added examples, and included Mermaid diagrams for control flow graphs (CFGs).

---

# Multiple Condition Coverage & MC/DC

## Motivation

Branch and Basis Path Coverage are not always sufficient. For example, consider a fault in a compound condition:

### Intended behavior

```fortran
input (A, B)
if (A .OR. B) then
    Z = Z + 1
else
    Z = Z + 2
end if
```

### Actual (Faulty) Implementation

```fortran
input (A, B)
if (A .AND. B) then
    Z = Z + 1
else
    Z = Z + 2
end if
```

### Test Suite:

```text
{ (A=T, B=T), (A=F, B=F) }
```

- **Branch coverage**: 100%
    
- **Basis path coverage**: 100%
    
- ❌ **Fails to detect the bug**
    

**Why?**  
Because the compound predicate uses multiple conditions (`A` and `B`), but the test cases don’t independently evaluate each one. We need **Multiple Condition Coverage** or **MC/DC** to reveal such faults.

---

## Multiple Condition Coverage

### Definition

**Multiple Condition Coverage** requires that:

- Every possible combination of **conditions** in a decision is evaluated **at least once**.
    
- Each **decision** in the program takes **all possible outcomes** (true and false).
    

### Pros and Cons

✅ Very thorough — detects faults missed by simpler coverage  
❌ Requires **2ⁿ** test cases for **n** conditions — exponential growth

### Example: All Combinations for `A` and `B`

```fortran
if (A .OR. B) then
    Z = Z + 1
else
    Z = Z + 2
end if
```

**All combinations (2² = 4):**

- (A=F, B=F)
    
- (A=T, B=F)
    
- (A=F, B=T)
    
- (A=T, B=T)
    

This test suite **does** reveal the fault.

---

## Unfeasible Combinations

Some combinations are logically or practically impossible.

### Example:

```fortran
if (y == 2 .OR. (y == 6 .AND. A == .TRUE.)) then
    ...
end if
```

**Conditions:**

- `C1: y == 2`
- `C2: y == 6`
- `C3: A == .TRUE.`
    
There are 2³ = 8 combinations, but some are **unfeasible**, like `y == 2` and `y == 6` being true at the same time.

|y==2|y==6|A|Feasible?|
|---|---|---|---|
|F|F|F|✅|
|F|F|T|✅|
|F|T|F|✅|
|F|T|T|✅|
|T|F|F|✅|
|T|F|T|✅|
|T|T|F|❌|
|T|T|T|❌|

---

## Example: AND Decision

```fortran
if (A .AND. B .AND. C) then
    ...
end if
```

**All 2³ = 8 combinations:**

|A|B|C|A AND B AND C|
|---|---|---|---|
|T|T|T|T|
|F|T|T|F|
|T|F|T|F|
|T|T|F|F|
|F|F|T|F|
|F|T|F|F|
|T|F|F|F|
|F|F|F|F|

Notice: once any condition is false, the decision is false — many combinations don't provide new insights.

---

## Modified Condition Coverage (MC/DC)

### Definition

**Modified Condition/Decision Coverage (MC/DC)** requires:

1. Every **decision** takes all possible outcomes.
    
2. Every **condition** takes all possible outcomes.
    
3. Each condition is shown to **independently affect** the decision outcome.
    

✅ **Required in safety-critical systems**, such as aerospace (DO-178C)  
✅ Requires **n + 1** test cases instead of 2ⁿ

---

### How Does MC/DC Work?

To show that a **condition affects the decision**, we:

- Change that **one condition**
    
- Keep **others fixed**
    

---

### Example

```fortran
input (A, B)
if (A .OR. B) then
    Z = Z + 1
else
    Z = Z + 2
end if
```

Let’s test 3 cases to see the effect of each condition.

| A   | B   | Expected | Faulty Output | Pass |
| --- | --- | -------- | ------------- | ---- |
| F   | F   | Z + 2    | Z + 2         | ✅    |
| T   | F   | Z + 1    | Z + 2         | ❌    |
| F   | T   | Z + 1    | Z + 2         | ❌    |
| T   | T   | Z + 1    | Z + 1         | ✅    |

Any 3 of the first 4 tests would be sufficient to meet **MC/DC**.

---

### Example for AND

```fortran
if (A .AND. B) then
    Z = Z + 1
else
    Z = Z + 2
end if
```

**Test Suite for MC/DC:**

| A   | B   | Expected | Faulty Output | Pass |
| --- | --- | -------- | ------------- | ---- |
| F   | F   | Z + 2    | Z + 2         | ✅    |
| T   | F   | Z + 2    | Z + 1         | ❌    |
| F   | T   | Z + 2    | Z + 1         | ❌    |
| T   | T   | Z + 1    | Z + 1         | ✅    |

To show **independent effect**, any 3 of the first 4 tests would be sufficient to meet **MC/DC**.


## Summary

| Coverage Type              | # Tests Needed | Detects Faults | Strength    |
| -------------------------- | -------------- | -------------- | ----------- |
| Branch Coverage            | 2ⁿ             | Sometimes      | Weak        |
| Basis Path Coverage        | ~n +1          | Sometimes      | Moderate    |
| Multiple Condition         | 2ⁿ             | Yes            | Very Strong |
| Modified Condition (MC/DC) | ~n + 1         | Yes            | Strong      |

---

## References

* \[RTCA DO-178C] Software Considerations in Airborne Systems and Equipment Certification

