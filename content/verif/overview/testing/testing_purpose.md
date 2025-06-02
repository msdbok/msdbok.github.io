---
parent: Testing
nav_order: 5
title: Purpose-based
layout: default
---


# Purpose-Based Testing

**Purpose-based testing** focuses on **why** we are testing—not just whether code runs, but what characteristics of the software we want to validate. This approach ensures the system behaves correctly, efficiently, and robustly under a variety of conditions and usage scenarios.

---

Here’s a non-exhaustive list of **software characteristics** typically targeted in purpose-based testing:

## Functional Correctness

- **Functions:**  
    Ensure each function:
    - Does **what it’s supposed to do**.
    - **Does not** do what it’s **not supposed to do**.

- **Data Handling:**
    - Analyze both **inputs and outputs**.
    - Consider:
        - **Typical values** (normal cases)
        - **Boundary values** (limits)
        - **Invalid values** (incorrect or out-of-range inputs)
        - **Convenient values** (for setup or debugging)

- **Input Combinations:**
    - Explore combinations of values that are **likely to interact**, such as:
        - Form fields submitted together
        - Configurations in tandem
        - State transitions

## Regression Testing

> Re-testing previously working features to ensure they still behave correctly after changes.

- Typically done using **existing test cases**.
- Helps confirm system integrity after:
    - Bug fixes
    - Feature enhancements
    - Version upgrades or builds

---

## Scenario-Based Testing

**Test a realistic usage flow**, not just isolated actions:

- Develop test cases that form a **coherent story**.
    - Example: "User logs in → updates profile → logs out"
- Link **multiple activities** end-to-end into one test.
- Avoid **resetting system state** between steps—test as a real user would.
- **Vary the timing and order** of events:
    - E.g., submit form before all fields are filled, or perform actions in a different sequence.

This kind of testing helps uncover **integration issues** and **state-related bugs**.

---

## Efficiency and Performance Testing

> "Does the system use resources wisely under expected conditions?"

### Performance Testing

- Assesses:
    - **Response time**
    - **Throughput** (how much work is done in a time frame)
    - **Resource usage** (CPU, memory, bandwidth)
- Done under **normal load conditions**.

Goal: verify the system performs **within acceptable thresholds**.
    

### Load Testing

> “How does the system behave under **maximum expected usage**?”

- Simulate **realistic peak usage scenarios**, such as:
    - Maximum number of concurrent users
    - Large data inputs

Objective: ensure system does not slow down or fail.

### Stress Testing

> “What happens when the system is **pushed beyond its limits**?”

- Intentionally overwhelm or **deprive the system of resources**:
    - CPU, memory, network, disk I/O

- Observe if the system:
    - **Fails gracefully**
    - **Recovers** once conditions return to normal

Helps ensure **stability and fault tolerance**.
    

---

## Robustness Testing

> “How well does the system **handle the unexpected**?”

- Imagine and simulate **unexpected or extreme events**:
    - Power failure
    - Disk full
    - Malformed input
    - System API misbehavior

Goal: assess the system’s **resilience and recovery behavior**.
