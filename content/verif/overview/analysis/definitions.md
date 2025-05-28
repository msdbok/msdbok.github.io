---
parent: Analysis
nav_order: 1
title: Definitions
layout: default
---

## 📘 What is (Static) Analysis?

### Definition from INCOSE (International Council on Systems Engineering)

**Static analysis** refers to the evaluation of system requirements or design choices without actually executing the system. It often involves calculations, modeling, or simulations. The goal is to verify the performance of a system by:

- **(a)** Reviewing the design or documentation (called the _baseline_),
    
- **(b)** Performing calculations based on that baseline and analyzing the results,
    
- **(c)** Using empirical data (measured from real physical systems) and applying extrapolation or interpolation,
    
- **(d)** Or a combination of all of the above.
    

This process helps assess whether a system meets its requirements before building or testing it.

### Definition from Software Engineering Perspective

In software engineering, **static analysis** is a method to verify properties of software without running it. It uses information about:

- The **syntax** (code structure),
    
- The **behavior** (what the software is expected to do),
    
- The **structure** (such as control flow or data flow within the program).
    

Examples of analysis include checking the program’s **state space** (all possible states it can be in), **execution patterns**, or **abstract models** of how it works.

🔍 Unlike **testing**, which checks actual program outputs by running the code, static analysis draws conclusions from the code itself.

---

## 🧪 Types of Software Analysis

There are **two main types**:

1. **Static Analysis**
    
    - Performed **without executing** the code.
        
    - Focuses on code structure, logic, and syntax.
        
    - Used early in development (e.g. code review, linting tools).
        
2. **Dynamic Analysis**
    
    - Involves **executing the program**.
        
    - Observes program behavior at runtime.
        
    - Used for performance testing, memory usage tracking, etc.
        

---

## 🧰 Uses of Static Analysis

Static analysis is used to detect:

- **Style issues**  
    e.g. code formatting, naming conventions
    
- **Dangerous constructs**  
    e.g. uninitialized variables, use of unsafe functions
    
- **Verification of system properties**  
    These are often formalized and checked systematically:
    
    - **Safety properties**: Nothing bad happens (e.g. no crashes)
        
    - **Liveness properties**: Something good eventually happens (e.g. program eventually responds)
        
    - **Fairness properties**: Resources are allocated fairly (e.g. no thread is starved)
        
    - **Temporal properties**: Things happen in the correct order (e.g. login before access)
        

---

## 🛠️ Examples of Static Analysis Results

- Detecting **security vulnerabilities** (e.g. buffer overflows)
    
- Finding **memory leaks**
    
- Reporting **code non-compliance** (e.g. not following coding standards)
    
- Estimating **resource usage** (CPU, memory, bandwidth)
    

---
