---
parent: Analysis
nav_order: 2
title: Software Properties
---

---

## 🔐 Software Properties Verified by Static Analysis

**Definition:**  
Safety properties ensure that _nothing bad happens_ during program execution. These properties guarantee the system does **not reach an undesirable state**.

**Examples:**

- No **deadlocks** (e.g. multiple processes waiting forever for each other).
    
- No attempt to **access an empty buffer** (e.g. removing an item that isn’t there).
    

**Purpose:**  
Used to ensure the **consistency of program state**.

**How?**

- Enforce **mutual exclusion**: Shared resources must be accessed atomically (only one thread/process at a time).
    
- Use **condition synchronization**: Certain actions are delayed until the system is in a safe state.
    

---

### ✅ Liveness Properties

**Definition:**  
Liveness properties ensure that _something good eventually happens_. They are used to guarantee **progress** in the system.

**Prevents:**

- **Starvation**: A process never gets needed resources (like CPU time).
    
- **Dormancy**: A waiting process is never resumed.
    
- **Premature termination**: A process ends before it should.
    

---

### ⚖️ Fairness Properties

**Definition:**  
A subset of liveness properties. **Fairness** means that every process or action gets its fair share _infinitely often_.

**Example:**

- A process is guaranteed to be activated repeatedly (e.g. each thread gets a turn in a scheduler).
    

---

### ⏳ Temporal Properties

**Definition:**  
Temporal properties describe how states are related **over time**. Unlike **state properties** (which describe a single point), **temporal properties** describe **paths or sequences of states**.

**Example:**  
“If a message is sent in one state, it will eventually be received in a future state.”

**Notation (common temporal logic):**

- **α**: α holds in the current state
    
- **Xα**: α holds in the _next_ state
    
- **Fγ**: γ holds _eventually_ (in the future)
    
- **Gλ**: λ holds _always_ from now on
    
- **α U β**: α holds _until_ β becomes true
    

---

## 🧰 Analysis Fault Taxonomy (Common Issues Detected by Static Analysis)

### 🧵 Concurrency Errors

- **Race conditions**: Multiple threads access shared data unsafely.
    
- **Deadlock**: Processes wait on each other in a cycle.
    
- **Improper lock usage**
    

### ⚠️ Exceptional Conditions

- Integer overflow/underflow
    
- Division by zero
    
- Unhandled exceptions
    
- Incorrect type conversions
    

### 🛡️ Input Validation Issues

- **Command injection**
    
- **Cross-site scripting (XSS)**
    
- **Format string vulnerabilities**
    
- Use of **tainted data** (untrusted user input)
    

### 🧹 Code Quality Issues

- Poor **code metrics**
    
- **Unused variables**
    

### 💾 Memory Errors

- **Buffer overruns**
    
- **Null or invalid pointer dereference**
    
- **Double free** or freeing unallocated memory
    
- **Memory leaks**
    
- Use of **uninitialized variables**
    

### 🔄 Resource/Protocol Misuse

- Incorrect function call order
    
- Forgetting to initialize or free resources
    

### 🧠 Design & Structural Issues

- Complex **dependencies**
    
- Complicated **heap structures**
    
- Incomplete or messy **call graphs**
    

### 🔐 Security Weaknesses

- **Privilege escalation**
    
- **Denial of service (DoS)**
    
- Execution of **dynamic code**
    
- **Insecure randomness**
    
- Violating **least privilege principle**
    

---

## 🧪 How does the Analysis work?

**Software analysis** involves creating a **model** of the system (either manually or automatically), and then **verifying properties** of the system using the model—**without running** the actual software.

> By abstracting away unnecessary details, we can prove or disprove whether certain properties hold.

---

## 🎯 Precision of Static Analysis

- **Soundness**:  
    If the tool says the program is **correct**, it truly is.  
    ✅ No false negatives (i.e. no missed bugs).
    
- **Completeness**:  
    If the tool reports an **issue**, it’s real.  
    ✅ No false positives (i.e. no bogus warnings).
    

> ❗ In practice, **no static analysis can be both sound and complete** and still **terminate** on all programs.

### Reality of Static Analysis:

- **Perfect static analysis is undecidable**: it’s impossible to create one that works perfectly for all programs.
    
- All analyses **use abstraction** to approximate behavior.
    
- Still, static analysis tools are extremely **useful in practice**.
    

---

# Soundness and Completeness in Static Analysis

## What is Soundness?

- A **sound** static analysis _over-approximates_ the behaviors of a program.
    
- This means it **guarantees to find all violations** of a given property — if a bug exists, the tool will catch it.
    
- However, because it is conservative, it may report **false alarms** — warnings about issues that **cannot actually happen** in the real program.
    

**In short:**  
Sound analysis → _No real bugs missed_ but may have _false positives_.

---

## What is Completeness?

- A **complete** static analysis _under-approximates_ the program's behavior.
    
- This means that **every violation it reports is real** — no false alarms.
    
- But it **might miss some real bugs** because it only reports violations it can confidently confirm.
    

**In short:**  
Complete analysis → _All reported bugs are real_ but may _miss some bugs_.

---

## Why Can't We Have Both Soundness and Completeness?

- According to **Rice’s Theorem**, there are fundamental limits on what automated program analysis can achieve.
    
- It is impossible for a static analysis to be **sound, complete, and always terminate** on all programs with arbitrary complexity (such as unbounded memory structures).
    

In other words, no tool can:

- Miss no errors (sound)
    
- Have no false alarms (complete)
    
- Automatically analyze every program and always finish (terminating)
    

---

## Practical Implications

- **For high assurance (critical systems), soundness is vital:**  
    If a tool says _no errors_, then there really are none. This means we accept some false alarms.
    
- **For general software development, bug finding is the main goal:**  
    Most tools prioritize reducing the number of bugs over guaranteeing to find all bugs.  
    Users often cannot tolerate many false alarms, so tools sacrifice soundness to be more practical.
    
- Some tools trade **automation for accuracy** by requiring **user annotations** or guidance.
    

---

## Examples of Commercial Tools

- Tools like **Coverity**, **CodeSonar**, **Fortify**, **KlocWork**, and **LDRA** are **neither sound nor complete**.
    
- Despite this, they are **effective in practice** at finding real bugs.
    
- They each use different methods and balance between false alarms and missed bugs differently.
    

---

## What About Simpler Tools Like Lint and FindBugs?

- These tools use **pattern matching** rather than deep semantic analysis.
    
- They are **neither sound nor complete**, but they are still useful and widely used.
    
- They help catch common bugs quickly and easily.
    

---

### Summary Table

|Property|What it Means|Pros|Cons|
|---|---|---|---|
|**Sound**|No bugs missed (no false negatives)|High assurance|May report false alarms (false positives)|
|**Complete**|No false alarms (no false positives)|Accurate warnings|May miss real bugs|
|**Neither**|Mix of both|Practical and efficient|Some bugs missed, some false alarms|


# Limitations of Static Analysis and Formal Verification

Static analysis and related verification methods are powerful tools for improving software quality, but they come with inherent limitations. Understanding these limitations helps set realistic expectations about what these tools can and cannot do.

---

## 1. Non-Functional Verification

- **What it means:**  
    Most static analysis tools focus on verifying _functional correctness_ (e.g., no null-pointer dereferences, race conditions, or deadlocks). However, many important _non-functional_ properties are not easily verified, such as:
    
    - Performance (e.g., execution speed, responsiveness)
        
    - Memory usage or power consumption
        
    - Usability or maintainability
        
    - Security properties that depend on runtime environment or configuration
        
- **Example:**  
    A static analyzer may verify that a program never accesses out-of-bounds memory but cannot guarantee that it will run efficiently under all circumstances.
    
- **Implication:**  
    Non-functional properties often require other tools or runtime monitoring.
    

---

## 2. False Positives (Spurious Warnings)

- **What it means:**  
    A **false positive** occurs when the tool reports a bug or violation that _does not actually exist_ in any real execution.
    
- **Why it happens:**  
    To ensure soundness (catching all real bugs), tools often over-approximate program behavior, which can cause them to flag safe operations as risky.
    
- **Example:**  
    A static analyzer might warn about a potential null pointer dereference on a variable that is, in fact, guaranteed to be initialized correctly, but the tool cannot prove it precisely.
    
- **Impact on developers:**  
    False positives can cause "alert fatigue," making developers ignore or disable the tool, reducing its effectiveness.
    

---

## 3. False Negatives (Missed Bugs)

- **What it means:**  
    A **false negative** occurs when the tool fails to detect a real bug or violation.
    
- **Why it happens:**  
    Tools that aim for completeness or to reduce false positives often under-approximate behaviors and thus may miss some bugs.
    
- **Example:**  
    A heuristic-based security scanner might fail to detect a subtle injection vulnerability because it cannot analyze all code paths precisely.
    
- **Risk:**  
    False negatives reduce confidence in the tool and might allow critical bugs to remain undetected.
    

---

## 4. Performance and Scalability

- **What it means:**  
    Static analysis, especially exhaustive techniques like model checking or formal proofs, can be very computationally expensive.
    
- **Why it happens:**  
    Analyzing all possible execution paths, states, or program behaviors grows exponentially with program size (state explosion problem).
    
- **Example:**  
    Model checkers like SPIN or Java PathFinder might run out of memory or time when analyzing large, complex programs with many concurrent threads.
    
- **Trade-off:**  
    Tools often limit the depth of analysis or abstract details to improve performance, trading off completeness or soundness.
    

---

## 5. Trade-offs Between Soundness, Completeness, and Automation

- The ideal tool would be:
    
    - **Sound**: never miss real bugs
        
    - **Complete**: never report false bugs
        
    - **Fully automatic**: require no human guidance
        
- **Rice’s theorem and related results** show this is impossible for all non-trivial properties in programs.
    
- **Thus, practical tools must compromise**, choosing which properties to check, which false alarms to tolerate, or which user inputs to require.
    

---

## Summary

|Limitation|Explanation|Example|Impact|
|---|---|---|---|
|Non-functional|Can't verify performance, usability, etc.|Can't guarantee program runs fast enough|May need runtime profiling|
|False Positives|Warns about issues that aren't real|Warns on safe null pointer usage|Can overwhelm developers|
|False Negatives|Misses real bugs|Misses subtle security flaw|Bugs slip into production|
|Performance/Scalability|Analysis can be very slow or impossible on large code|Model checking runs out of memory/time|Limits tool use on large projects|

---

## Real-World Examples

- **Coverity** and **Fortify** balance false positives and negatives by configurable heuristics and human-in-the-loop review.
    
- **SPIN model checker** is powerful but may not scale well for very large or highly concurrent systems without abstraction.
    
- **Lint and FindBugs** are fast and scalable but often produce many false positives due to their pattern-based approach.
    

---

## Final Note

Despite limitations, static analysis and formal verification remain critical in improving software reliability and security. Combining multiple tools and techniques — static analysis, dynamic testing, code reviews, and runtime monitoring — provides the best overall assurance.

---

