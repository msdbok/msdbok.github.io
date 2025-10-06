---
parent: Estimates
title: Function Point Analysis
nav_order: 5
layout: default
---



# Function Point Analysis (FPA)

## 1. Concept and Origin

**Function Point Analysis (FPA)** is a method for **measuring the functional size** of software — that is, what the software _does_ for the user, independent of how it is implemented.

- Introduced by **Allan J. Albrecht** at IBM in **1979** (_“Measuring Application Development Productivity”_, IBM Applications Development Symposium).
    
- Standardized by **IFPUG** (International Function Point Users Group) and formalized as **ISO/IEC 20926:2009**.
    
- The method assumes: _“The functionality delivered to the user determines the size of the software.”_
    

Function Points (FP) are used in **effort estimation models** (e.g., COCOMO II, regression-based models) as a normalized measure of software size.

---

## 2. The Counting Process

FPA divides the system into **five types of functions**:

|Category|Function Type|Description|Example|
|---|---|---|---|
|**Data Functions**|Internal Logical File (ILF)|Data maintained within the system|Customer or Order table|
||External Interface File (EIF)|Data used but maintained by another system|Currency rate file|
|**Transactional Functions**|External Input (EI)|Processes entering data|Order entry form|
||External Output (EO)|Processes producing data|Invoice report|
||External Inquiry (EQ)|Processes that retrieve data without change|Search customer details|

Each function type is assigned a **complexity weight** (Low, Average, High) depending on data element counts and file references.

### Typical IFPUG Weights

|Function Type|Low|Average|High|
|---|---|---|---|
|EI|3|4|6|
|EO|4|5|7|
|EQ|3|4|6|
|ILF|7|10|15|
|EIF|5|7|10|

The sum gives the **Unadjusted Function Point (UFP)**.

$$UFP = \sum \text{(Number of functions × Weight)}$$

---

## 3. Value Adjustment Factor (VAF)

To account for system characteristics, IFPUG defines **14 General System Characteristics (GSCs)**, rated 0–5 each, covering aspects like data communication, performance, complexity, reusability, and end-user efficiency.

$$\text{VAF} = 0.65 + 0.01 \times \text{(Total GSC Score)}$$

The **Adjusted Function Points** are then:

$$FP = UFP \times VAF$$

---

## 4. Estimation Based on Function Points

Once FP is known, **effort estimation** is done using **historical productivity rates**, typically expressed as:

$$\text{Effort (Person-Months)} = \frac{FP}{\text{Productivity (FP/PM)}}​$$

Example:  
If a team’s productivity is 10 FP/PM and the system size is 300 FP:  
→ Effort ≈ 30 person-months

To estimate **cost**:

$$\text{Cost} = \text{Effort} \times \text{Cost per Person-Month}$$

---

## 5.  Example

**System:** Simple Library Management System

|Function|Type|Complexity|Weight|
|---|---|---|---|
|Add new book|EI|Avg|4|
|Register user|EI|Avg|4|
|Borrow/Return book|EO|High|7|
|Search books|EQ|Avg|4|
|Books table|ILF|Avg|10|
|Members table|ILF|Avg|10|
|External supplier file|EIF|Low|5|

$$UFP = 4 + 4 + 7 + 4 + 10 + 10 + 5 = 44$$

Assume total GSC score = 30 ⇒ 

$$VAF = 0.65 + 0.01×30 = 0.95$$

$$FP = 44 × 0.95 = 41.8 ≈ 42$$

If the historical productivity is 12 FP/PM →

$$\text{Effort} = 42 / 12 ≈ 3.5 \text{ person-months}$$

---

## 6. Strengths and Limitations

|Strengths|Limitations|
|---|---|
|Independent of technology and language|Requires trained counters; subjective interpretation|
|Early estimation possible (before design)|Doesn’t capture algorithmic or non-functional complexity|
|Supports benchmarking and productivity tracking|Not ideal for scientific or embedded systems|
|Standardized by ISO/IFPUG|Manual and time-consuming for large systems|

---

## 7. Primary Sources

- **Albrecht, A. J.** “Measuring Application Development Productivity.” _IBM Applications Development Symposium_, 1979.
    
- **IFPUG.** _Function Point Counting Practices Manual (FPCPM)_, Release 4.3.1, 2010.
    
- **ISO/IEC 20926:2009.** _Software and Systems Engineering—Measurement of Software Size Using IFPUG FPA_.
    
- **Jones, C.** _Applied Software Measurement: Global Analysis of Productivity and Quality_. McGraw-Hill, 2008.
    
- Symons, Charles R. "Function point analysis: difficulties and improvements." _IEEE transactions on software engineering_ 14.1 (2002): 2-11.


{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.
