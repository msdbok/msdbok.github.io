---
parent: Testing
nav_order: 4
title: Targeted faults
layout: default
---


### Target fault model

Partition based testing. 

Assumptions about where the faults are most likely located or systematic exploration of the software. Points belonging to a partition are assumed to be “revealing” or equivalents

    Boundary value analysis
    Combinatorial
    Data flow
    States
    Negative testing

Random testing. 

All input points are unique. Effort is put into finding a suitable random distribution

    Random testing
    Fuzz testing

#### Partition testing

A partition is the division of the input domain of the software under test into a number of subsets (called equivalence classes) for which the behavior is assumed to be the same for all values belonging to the each of them

The partition criteria utilized is what differentiates one test design technique from another

> To keep down our testing costs, we don’t want to write several test cases that test the same aspect of our program. A good test case uncovers a different class of errors (e.g., incorrect processing of all character data). Equivalence partitioning is a strategy that can be used to reduce the number of test cases that need to be developed. Equivalence partitioning divides the input domain of a program into classes. For each of these equivalence classes, it is hypothesized that the set of data must be treated the same by the module under test and should then produce likely answers, if it does not then the test fails.

#### Random testing

The systematic variation of values through the input space with the purpose of identifying abnormal output patterns. 
When such patterns are identified a root cause analysis is conducted to identify the source of the problem. In this case the “state 3” outputs seem to be missing

(from. When Only Random Testing Will Do Dick Hamlet, 2006)

> Random testing is a technique which systematically explores the input space of the software under testing. This use of the term random is very different from other disciplines where random testing means selecting a few cases just by “chance”. To be effective and efficient random testing relies on the automatic generation of test inputs. The problem with random testing is how to verify that the results are those expected. This is known as the “oracle problem”.

> The solutions to the oracle problem fall into three categories: the use of a proxy to produce the correct results against the values produced by the new application will be checked. The proxy could be an existing system or a simple computational form. The second category is based on the recognition of patterns. Pattern recognition can take the form of curve fitting algorithms followed by a study of discontinuities in the output of the application or it can be in the form of assertions where a relation between variables is a specified and a violation of the assertion denotes a failure of the software. The breaking of a pattern can also be detected by visual inspection of a summary input like in the example shown. A third category consist in analyzing the states which result after the execution of the software with a certain data. A common example for this is fuzz testing in which the expected output from the test are that after processing the data the software exits normally. The software raises an exception indication an abnormal condition or the software crashes revealing an abnormal situation that it was not programmed to handle.


------------------------

------------------------

## 🎯 Target Fault Model in Software Testing

Software testing aims to uncover faults by targeting likely problem areas using systematic or randomized strategies. Two main approaches are:

* **Partition-Based Testing**
* **Random Testing**

---

### 🧩 Partition-Based Testing

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

### 🎲 Random Testing

_Reference: When Only Random Testing Will Do Dick Hamlet, 2006 {% cite hamlet2006random %}_

**Definition**:
Random testing systematically selects inputs from the entire input space using a random distribution. The goal is to explore software behavior without bias.

> This is not just picking a few inputs by chance. It's a **deliberate**, **automated**, and **systematic** method of testing.

#### Advantages:

* Helps identify **abnormal outputs** or patterns not considered during design.
* Especially useful when input space is large or poorly understood.

#### The Oracle Problem:

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

### 🧪 Fuzz Testing

**A form of random testing** where malformed or unexpected inputs are sent to the system to discover:

* Crashes
* Unhandled exceptions
* Security vulnerabilities

> **Expected outcome**: Software should reject bad input or fail gracefully, never crash or behave unpredictably.

---

### ✅ Summary Table

| Category              | Key Idea                            | Examples                                | Goal                                      |
| --------------------- | ----------------------------------- | --------------------------------------- | ----------------------------------------- |
| **Partition Testing** | Divide inputs into classes          | Boundary values, data flow, state tests | Efficiently test different behavior types |
| **Random Testing**    | Sample inputs across the full space | Random input, fuzzing                   | Detect unexpected behavior or crashes     |
| **Oracle Mechanism**  | Know what correct output should be  | Proxy, assertions, pattern analysis     | Determine whether a test passed or failed |

---

### References

{% bibliography --cited %}