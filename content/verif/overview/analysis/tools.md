---
parent: Analysis
nav_order: 4
title: Static Analysis Tools
---



|**Technique**|**Description**|**Example Tools**|**Comments**|**Links**|
|---|---|---|---|---|
|**Static Analysis**|Analyzes source code without executing it; detects bugs, code smells, patterns.|FindBugs, ESLint, SonarQube, CodeQL, PyLint|Widely used for style, security, maintainability, reliability checks.|[SonarQube](https://www.sonarqube.org/) [CodeQL](https://securitylab.github.com/tools/codeql)|
|**Abstract Interpretation**|A mathematical framework for approximating program behavior to verify properties.|PolySpace, Astrée|Used for sound but possibly incomplete static analysis, often in safety-critical systems.|[PolySpace](https://www.mathworks.com/products/polyspace.html)|
|**Model Checking**|Exhaustive exploration of state space of models/programs to verify properties.|SPIN, Java PathFinder, NuSMV|Useful for concurrency bugs and protocol verification; suffers from state explosion.|[SPIN](http://spinroot.com/) [Java PathFinder](https://github.com/javapathfinder/jpf-core)|
|**Bug Patterns**|Pattern matching for common coding mistakes or risky constructs.|FindBugs, PMD, ESLint|Fast, scalable, but may produce false positives and miss semantic bugs.|[PMD](https://pmd.github.io/)[ESLint](https://eslint.org/)|
|**Data Flow Analysis**|Tracks how data moves through program variables and memory to detect errors.|Clang Static Analyzer, CodeSonar|Useful for detecting uninitialized variables, resource leaks, and security flaws.|[Clang Static Analyzer](https://clang-analyzer.llvm.org/)|
|**Formal Proofs**|Mathematically proving correctness properties using logic and theorem provers.|Coq, Isabelle, PVS, Dafny|Requires expert knowledge; highest assurance but costly and time-consuming.|[Coq](https://coq.inria.fr/)[Isabelle](https://isabelle.in.tum.de/)|
|**Petri Nets**|Graph-based models for concurrent system behavior and workflow verification.|PIPE (Platform Independent Petri net Editor)|Useful for modeling and analyzing distributed and concurrent processes.|[PIPE](https://pipe2.sourceforge.net/)|




## 🛠️ Methods and Approaches

### 🔍 Static Analysis

- Works **directly on source code**.
    
- Detects basic but important properties.
    
- Examples:
    
    - `lint`, `FindBugs`, `SonarQube`, `CodeQL`, `CodeSense`
        

### 🔄 Model Checking

- Uses a **formal model** of the system.
    
- Exhaustively explores all possible states (like brute force).
    
- Mostly **automated**, but model creation is manual.
    
- Example: **SPIN**
    

### 🧠 Theorem Proving

- Uses mathematical logic to **prove correctness**.
    
- Requires **expert human guidance**.
    
- Suitable for very critical systems.
    
- Examples: **PVS**, **ESC/Java**



---
# Modern Static Analysis Tools
## 🐍 Python

### Code Quality & Linting

- **Pylint**: A comprehensive static code analyzer that checks for coding standards, errors, and code smells. It supports customization and integrates with various IDEs. 
    
- **Pyflakes**: Focuses on identifying logical errors in Python code without enforcing coding style.
    
- **Flake8**: Combines Pylint, Pyflakes, and McCabe for style guide enforcement and complexity checks.([Wikipedia](https://en.wikipedia.org/wiki/SonarQube "SonarQube"), [Wikipedia](https://en.wikipedia.org/wiki/Pylint "Pylint"))
    

### Metrics & Maintainability

- **PyExamine**: Detects code smells across architectural, structural, and code-level aspects, providing insights into code health. 
    
- **Radon**: Analyzes code complexity, maintainability index, and raw metrics.([arXiv](https://arxiv.org/abs/2501.18327 "PyExamine A Comprehensive, UnOpinionated Smell Detection Tool for Python"))
    

### Security

- **Bandit**: Scans for common security issues in Python codebases.
    
- **Semgrep**: A fast, open-source static analysis tool that supports custom rules for detecting security vulnerabilities. 
    

---

## 🌐 JavaScript / TypeScript

### Code Quality & Linting

- **ESLint**: A highly configurable linter for JavaScript and TypeScript, supporting custom rules and integrations with various editors. 
    
- **JSHint**: Detects errors and potential problems in JavaScript code, offering a balance between flexibility and strictness. 
    
- **JSLint**: The original JavaScript linter, enforcing a strict coding standard. ([Wikipedia](https://en.wikipedia.org/wiki/ESLint "ESLint"))
    

### Security

- **Semgrep**: Supports JavaScript and TypeScript for identifying security vulnerabilities and enforcing best practices. 
    
- **CodeSonar**: Provides deep static analysis for JavaScript, identifying quality and security defects. ([OWASP Foundation](https://owasp.org/www-community/Source_Code_Analysis_Tools "Source Code Analysis Tools - OWASP Foundation"))
    

---

## ☕ Java

### Code Quality & Linting

- **Checkstyle**: Ensures Java code adheres to coding standards and style guidelines. 
    
- **PMD**: Detects common programming flaws like unused variables, empty catch blocks, and unnecessary object creation.
    
- **SpotBugs**: Successor to FindBugs, it uses static analysis to look for bugs in Java code.([Wikipedia](https://en.wikipedia.org/wiki/Checkstyle "Checkstyle"), [arXiv](https://arxiv.org/abs/2405.12333 "Efficacy of static analysis tools for software defect detection on open-source projects"))
    

### Metrics & Maintainability

- **DR-Tools**: Provides lightweight tools to measure and visualize Java source code metrics, aiding in maintainability assessments. ([arXiv](https://arxiv.org/abs/2008.03547 "DR-Tools: a suite of lightweight open-source tools to measure and visualize Java source code"))
    

### Security

- **Fortify Static Code Analyzer**: Analyzes Java code for security vulnerabilities, integrating with development pipelines. 
    
- **CodeSonar**: Offers static analysis for Java, focusing on detecting quality and security defects. ([ISHIR Software Development India](https://www.ishir.com/blog/132331/9-best-code-quality-tools-in-2024-boost-your-development-efficiency.htm "9 Best Code Quality Tools in 2025: Boost Your Development Efficiency"), [OWASP Foundation](https://owasp.org/www-community/Source_Code_Analysis_Tools "Source Code Analysis Tools - OWASP Foundation"))
    

---

## 💻 C / C++

### Code Quality & Linting

- **Clang-Tidy**: A linter tool for C/C++ based on the Clang compiler, providing diagnostics and automatic fixes.
    
- **Cppcheck**: A static analysis tool for C/C++ code that detects bugs and focuses on code safety.([Wikipedia](https://en.wikipedia.org/wiki/SonarQube "SonarQube"))
    

### Metrics & Maintainability

- **Understand**: Analyzes C/C++ codebases to provide metrics, helping in understanding and maintaining large codebases. ([Wikipedia](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis "List of tools for static code analysis - Wikipedia"))
    

### Security

- **CodeSonar**: Performs deep static analysis on C/C++ code to identify security vulnerabilities and quality issues. 
    
- **Fortify Static Code Analyzer**: Scans C/C++ code for security vulnerabilities, integrating with CI/CD pipelines. 
    

---

## 🧰 Cross-Language Tools

- **SonarQube**: Supports over 27 languages, including Java, Python, JavaScript, and C++, providing comprehensive code quality and security analysis. 
    
- **Semgrep**: A versatile static analysis tool supporting multiple languages, enabling custom rule definitions for code scanning. 
    
- **CodeSonar**: Offers static analysis across various languages, focusing on detecting quality and security defects. ([ISHIR Software Development India](https://www.ishir.com/blog/132331/9-best-code-quality-tools-in-2024-boost-your-development-efficiency.htm "9 Best Code Quality Tools in 2025: Boost Your Development Efficiency"), [OWASP Foundation](https://owasp.org/www-community/Source_Code_Analysis_Tools "Source Code Analysis Tools - OWASP Foundation"))
    

---
# Model Checking

---

## 🐍 Python

### Model Checking Tools

- **PyNuSMV**: A Python interface to the NuSMV model checker, allowing users to define and verify finite state systems within Python.([Wikipedia](https://en.wikipedia.org/wiki/NuSMV "NuSMV"))
    
- **SPIN**: While not Python-specific, SPIN can be used to model and verify concurrent systems, and Python scripts can generate Promela models for analysis.
    

---

## 🌐 JavaScript / TypeScript

### Model Checking Tools

- **TLA+**: Though not JavaScript-specific, TLA+ can model algorithms and systems that can be implemented in JavaScript. Tools like PlusCal can help bridge the gap between algorithm design and implementation.([Wikipedia](https://en.wikipedia.org/wiki/BLAST_model_checker "BLAST model checker"))
    
- **Alloy Analyzer**: A lightweight formal modeling tool that can be used to model and analyze systems, including those implemented in JavaScript.
    

---

## ☕ Java

### Model Checking Tools

- **Java PathFinder (JPF)**: An explicit-state model checker for Java programs, capable of detecting concurrency issues, deadlocks, and other runtime errors.([Wikipedia](https://en.wikipedia.org/wiki/Mur%CF%86 "Murφ"))
    
- **KeY**: A formal verification tool for Java programs, allowing for the specification and verification of program properties using dynamic logic.([NMSU Computer Science](https://www.cs.nmsu.edu/~jcook/posts/static-analysis-tools/ "Static Analysis Tools • Jonathan Cook - Computer Science"))
    
- **OpenJML**: Integrates with Java to allow for the specification and checking of formal properties using the Java Modeling Language (JML).
    

---

## 💻 C / C++

### Model Checking Tools

- **SPIN**: A widely-used model checker for verifying the correctness of distributed software models in C.
    
- **BLAST**: A software model checker for C programs that uses counterexample-driven automatic abstraction refinement to verify program properties.([Wikipedia](https://en.wikipedia.org/wiki/BLAST_model_checker "BLAST model checker"))
    
- **CBMC (C Bounded Model Checker)**: A tool for verifying array bounds, pointer safety, exceptions, and user-specified assertions in C programs.
    
- **NuSMV**: A symbolic model checker that can be used to verify finite state systems, including those implemented in C.
    

---
# 🔧 Modern Theorem Proving Tools for Static Analysis

### 1. **Rocq (formerly Coq)**

- **Overview**: Rocq is an interactive theorem prover designed for formalizing mathematical proofs and verifying software correctness. It allows for the development of mathematical proofs and formal specifications, ensuring that programs comply with their specifications.
    
- **Key Features**:
    
    - Supports the calculus of inductive constructions.
        
    - Can extract executable programs from specifications in OCaml or Haskell.
        
    - Includes automatic theorem proving tactics and decision procedures.
        
- **Use Cases**: Formal verification of software, development of certified programs, and educational purposes in formal methods.
    
- **Website**: [rocq-prover.org](https://rocq-prover.org/) ([Rocq](https://rocq-prover.org/ "Welcome to a World of Rocq"), [Wikipedia](https://en.wikipedia.org/wiki/Rocq "Rocq"))
    

### 2. **Isabelle**

- **Overview**: Isabelle is a generic proof assistant that supports various logical formalisms, including higher-order logic. It provides a framework for developing formal proofs and is widely used in academia and industry.
    
- **Key Features**:
    
    - Supports higher-order logic and other formalisms.
        
    - Offers a rich set of tools for proof development and automation.
        
    - Includes the Isabelle Archive of Formal Proofs (AFP) for sharing verified theories.
        
- **Use Cases**: Formal verification of software and hardware systems, mathematical theorem proving, and education in formal methods.
    
- **Website**: [isabelle.in.tum.de](https://isabelle.in.tum.de/) ([Wikipedia](https://en.wikipedia.org/wiki/Isabelle_%28proof_assistant%29 "Isabelle (proof assistant)"))
    

### 3. **KeY**

- **Overview**: KeY is a formal verification tool tailored for Java programs. It uses dynamic logic to specify and verify program properties, allowing for both interactive and automated proofs.
    
- **Key Features**:
    
    - Integrates with Java Modeling Language (JML) for specifying program behavior.
        
    - Supports verification of Java programs through symbolic execution and deductive reasoning.
        
    - Provides a user-friendly interface for proof construction and analysis.
        
- **Use Cases**: Verification of Java applications, ensuring compliance with specifications, and detecting potential bugs or security vulnerabilities.
    
- **Website**: [key-project.org](https://www.key-project.org/) ([Wikipedia](https://en.wikipedia.org/wiki/KeY "KeY"))
    

### 4. **Z3**

- **Overview**: Z3 is a high-performance theorem prover developed by Microsoft Research. It is used for checking the satisfiability of logical formulas and is widely employed in software verification and analysis.
    
- **Key Features**:
    
    - Supports various theories, including arithmetic, bit-vectors, arrays, and more.
        
    - Provides APIs for multiple programming languages, facilitating integration into different tools.
        
    - Efficiently handles large and complex verification problems.
        
- **Use Cases**: Static analysis, formal verification, constraint solving, and symbolic execution in software development.
    
- **Website**: [github.com/Z3Prover/z3](https://github.com/Z3Prover/z3) ([Wikipedia](https://en.wikipedia.org/wiki/Z3_Theorem_Prover "Z3 Theorem Prover"), [arXiv](https://arxiv.org/abs/1907.03890 "Manticore: A User-Friendly Symbolic Execution Framework for Binaries and Smart Contracts"))
    

### 5. **Frama-C with Jessie Plugin**

- **Overview**: Frama-C is a static analysis framework for C programs. The Jessie plugin within Frama-C allows for deductive verification using formal specifications and theorem proving.
    
- **Key Features**:
    
    - Supports the ANSI/ISO C Specification Language (ACSL) for annotating C code.
        
    - Integrates with various theorem provers like Coq, Z3, and Alt-Ergo for verifying proof obligations.
        
    - Provides a modular architecture with multiple analysis plugins.
        
- **Use Cases**: Formal verification of safety-critical C programs, ensuring adherence to specifications, and detecting potential runtime errors.
    
- **Website**: [frama-c.com](https://frama-c.com/) ([Wikipedia](https://en.wikipedia.org/wiki/Frama-C "Frama-C"))
  
 ---
 
# More Techniques and Tools

---

## Techniques in Static Analysis

### 1. **Abstract Interpretation**

- **Description**: A mathematical framework for analyzing programs by interpreting them over abstract domains. It provides sound approximations of program behaviors, enabling the detection of potential errors without executing the code.
    
- **Example**: Polyspace utilizes abstract interpretation to prove the absence of critical runtime errors in C, C++, and Ada programs. ([Wikipedia](https://en.wikipedia.org/wiki/Polyspace "Polyspace - Wikipedia"))
    

### 2. **Model Checking**

- **Description**: A formal verification technique that systematically explores all possible states of a system to verify whether certain properties hold. It is particularly effective for concurrent systems.
    
- **Example**: SPIN is a widely used open-source model checker that verifies the correctness of distributed systems described in Promela. It uses Linear Temporal Logic (LTL) to specify properties and checks them against the model. ([spinroot.com](https://spinroot.com/ "Spin - Formal Verification"), [Wikipedia](https://en.wikipedia.org/wiki/SPIN_model_checker "SPIN model checker"))
    

### 3. **Bug Patterns**

- **Description**: Static analysis tools often detect recurring coding mistakes or patterns that are known to lead to errors. Identifying these patterns helps in early detection of potential bugs.
    
- **Example**: FindBugs analyzes Java bytecode to identify bug patterns such as null pointer dereferences and infinite recursive loops. ([methodsandtools.com](https://www.methodsandtools.com/tools/findbugs.php "Findbugs - Static Code Analysis of Java - Methods & Tools"))
    

### 4. **Data Flow Analysis**

- **Description**: Analyzes the flow of data through variables in a program to detect potential issues like uninitialized variables or unreachable code.
    
- **Example**: Tools like CodeSonar perform data flow analysis to detect complex bugs in C, C++, Java, and other languages. 
    

### 5. **Formal Proofs**

- **Description**: Involves mathematically proving that a program satisfies certain correctness properties. This is the most rigorous form of verification.
    
- **Example**: ESC/Java uses formal methods to verify Java programs annotated with JML (Java Modeling Language) specifications. ([MathWorks](https://www.mathworks.com/products/polyspace.html "Polyspace - MATLAB & Simulink"))
    

### 6. **Petri Nets**

- **Description**: A graphical and mathematical modeling tool used to describe and analyze the flow of information in systems, especially useful for modeling concurrent systems.
    
- **Example**: PIPE (Platform Independent Petri net Editor) is an open-source tool for creating, simulating, and analyzing Petri nets, including Generalized Stochastic Petri nets. ([GitHub](https://github.com/sarahtattersall/PIPE "sarahtattersall/PIPE - Platform Independent Petri Net Editor - GitHub"))
    

---

## Modern Static Analysis Tools

### 1. **SPIN**

- **Description**: An open-source model checker for verifying the correctness of distributed systems. It uses Promela for modeling and LTL for property specification.
    
- **Example**: SPIN has been used to verify protocols like the Alternating Bit Protocol and the Dining Philosophers Problem. ([Wikipedia](https://en.wikipedia.org/wiki/SPIN_model_checker "SPIN model checker"), [spinroot.com](https://spinroot.com/spin/Doc/Book_extras/ "The SPIN MODEL CHECKER -- Primer and ..."))
    

### 2. **Java Pathfinder (JPF)**

- **Description**: An extensible software analysis framework for Java bytecode. It performs model checking to detect defects such as deadlocks and unhandled exceptions.
    
- **Example**: JPF has been used to verify Java applications in aerospace and automotive industries. ([GitHub](https://github.com/javapathfinder "Java Pathfinder - GitHub"), [software.nasa.gov](https://software.nasa.gov/software/ARC-17487-1 "Java Pathfinder (JPF) core system(ARC-17487-1)"))
    

### 3. **FindBugs**

- **Description**: An open-source static analysis tool that detects potential bugs in Java programs by analyzing bytecode.
    
- **Example**: FindBugs identifies issues like null pointer dereferences and infinite recursive loops in Java applications. ([Wikipedia](https://en.wikipedia.org/wiki/FindBugs "FindBugs - Wikipedia"))
    

### 4. **JLint**

- **Description**: A static analysis tool for Java that detects potential concurrency issues and other bugs.
    
- **Example**: JLint has been used to detect synchronization issues in multi-threaded Java applications.
    

### 5. **ESC/Java**

- **Description**: A static analysis tool that attempts to find common runtime errors in Java programs at compile time using formal verification techniques.
    
- **Example**: ESC/Java has been used in academic settings to teach formal verification methods. ([Wikipedia](https://en.wikipedia.org/wiki/ESC/Java "ESC/Java"))
    

### 6. **CodeSonar**

- **Description**: A static code analysis tool that helps find and fix bugs and security vulnerabilities in source and binary code.
    
- **Example**: CodeSonar is used in industries like aerospace and automotive for safety-critical applications. ([Wikipedia](https://en.wikipedia.org/wiki/CodeSonar "CodeSonar - Wikipedia"))
    

### 7. **Polyspace**

- **Description**: A static code analysis tool that uses formal methods to prove the absence of critical runtime errors in C, C++, and Ada programs.
    
- **Example**: Polyspace is used in the development of embedded systems to ensure software reliability. ([MathWorks](https://www.mathworks.com/products/polyspace.html "Polyspace - MATLAB & Simulink"))
    

### 8. **Fortify 360**

- **Description**: A static application security testing tool that helps developers find and fix code vulnerabilities early with automated static code analysis.
    
- **Example**: Fortify 360 is used by enterprises to secure their software applications during development. ([OpenText](https://www.opentext.com/products/static-application-security-testing "OpenText™ Static Application Security Testing (Fortify)"))
    

### 9. **Klocwork**

- **Description**: A static code analysis tool that identifies software security, quality, and reliability issues in C, C++, Java, JavaScript, Python, and Kotlin code.
    
- **Example**: Klocwork is used in DevSecOps pipelines to enforce coding standards and detect vulnerabilities. ([perforce.com](https://www.perforce.com/video-tutorials/kw/static-code-analysis-and-why-klocwork-different "Static Code Analysis and Why Klocwork is Different | Perforce"), [perforce.com](https://www.perforce.com/products/klocwork "Perforce Klocwork"))
    

### 10. **Microsoft PREfast & SDV**

- **Description**: PREfast is a static verification tool that detects basic coding errors in C and C++ programs. SDV (Static Driver Verifier) is a compile-time static verification tool that detects errors in Windows kernel-mode drivers.
    
- **Example**: SDV has been used by Microsoft to improve the reliability of Windows device drivers. ([Download Center Microsoft](https://download.microsoft.com/download/a/f/7/af7777e5-7dcd-4800-8a0a-b18336565f5b/prefast_steps_80.doc "[DOC] PREfast Step-by-Step - Microsoft"))
    

### 11. **PIPE (Platform Independent Petri net Editor)**

- **Description**: An open-source tool for creating, simulating, and analyzing Petri nets, including Generalized Stochastic Petri nets.
    
- **Example**: PIPE is used in academic research for modeling and analyzing concurrent systems. ([GitHub](https://github.com/sarahtattersall/PIPE "sarahtattersall/PIPE - Platform Independent Petri Net Editor - GitHub"))
    
