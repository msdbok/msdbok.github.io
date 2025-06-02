---
parent: Testing
nav_order: 4
title: Targeted faults
layout: default
---

# Testing Target Fault Model

Software testing aims to uncover faults by targeting likely problem areas using systematic or randomized strategies. Two main approaches are:

* **Partition-Based Testing**
* **Random Testing**

---

## Partition-Based Testing

**Definition**:
Partition testing involves dividing the input domain into subsets called **partitions** or **equivalence classes**, where each class is assumed to behave similarly for all its values. A single representative value from each class is tested.

**Why use partitioning?**
We want to minimize the number of test cases without missing potential faults. Each partition represents a "class" of behavior—if one test fails, it likely indicates a fault in handling that whole class.

> “A good test case uncovers a different class of errors. Testing the same behavior repeatedly wastes effort.”

**Common Partition-Based Techniques**:

| Technique                   | Description                                                                |
| --------------------------- | -------------------------------------------------------------------------- |
| **Boundary Value Analysis** | Tests values at the edges of input ranges (e.g., min/max).                 |
| **Combinatorial Testing**   | Tests combinations of input parameters, often using pairwise combinations. |
| **Data Flow Testing**       | Focuses on variable definitions and their usage paths.                     |
| **State-Based Testing**     | Tests transitions and behavior of systems with state machines.             |
| **Negative Testing**        | Tests how the system handles invalid, unexpected, or out-of-range inputs.  |

---

## Random Testing

_Reference: When Only Random Testing Will Do, Dick Hamlet, 2006 {% cite hamlet2006random %}_

**Definition**:
Random testing systematically selects inputs from the entire input space using a random distribution. The goal is to explore software behavior without bias.

> This is not just picking a few inputs by chance. It's a **deliberate**, **automated**, and **systematic** method of testing.

### Advantages:

* Helps identify **abnormal outputs** or patterns not considered during design.
* Especially useful when input space is large or poorly understood.

### The Oracle Problem:

A core challenge in random testing is knowing the **correct output** for the randomly chosen inputs. This is called the **oracle problem**.

#### Oracle Solutions:

1. **Reference (Proxy) Oracle**
   Use a trusted system or computation to compare results (e.g., a legacy system or formula).

2. **Pattern Recognition**
   Use:

   * Curve fitting to identify anomalies
   * Assertions or constraints (e.g., "total must always be positive")
   * Visual inspection for unexpected output changes

3. **State-Based Oracles**
   Analyze the system's final state:

   * Does it **exit normally**?
   * Does it raise an **error/exception**?
   * Does it **crash**? (useful in **fuzz testing**)

---

###  Fuzz Testing

**A form of random testing** where malformed or unexpected inputs are sent to the system to discover:

* Crashes
* Unhandled exceptions
* Security vulnerabilities

> **Expected outcome**: Software should reject bad input or fail gracefully, never crash or behave unpredictably.

---

## Summary Table

| Category              | Key Idea                            | Examples                                | Goal                                      |
| --------------------- | ----------------------------------- | --------------------------------------- | ----------------------------------------- |
| **Partition Testing** | Divide inputs into classes          | Boundary values, data flow, state tests | Efficiently test different behavior types |
| **Random Testing**    | Sample inputs across the full space | Random input, fuzzing                   | Detect unexpected behavior or crashes     |
| **Oracle Mechanism**  | Know what correct output should be  | Proxy, assertions, pattern analysis     | Determine whether a test passed or failed |

---

### References

{% bibliography --cited %}