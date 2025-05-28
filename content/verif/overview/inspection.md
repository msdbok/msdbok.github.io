---
parent: Overview
nav_order: 2
title: Inspection
layout: default
---


## 📖 **What is Inspection?**

### INCOSE Definition:
> **Inspection** is a verification method that determines performance by examining:  
> - **(a)** Engineering documentation produced during development or modification.  
> - **(b)** The item itself using **visual means** or **simple measurements** without requiring precision instruments.

### Practitioner’s Perspective:
> **Inspection** is the **systematic scrutiny of development artifacts** (e.g., code, design documents) by individuals **other than the creator**. This aims to:  
> - Meet contractual or project obligations.  
> - Detect non-conformities with standards.  
> - Uncover defects based on the idea that creators may overlook certain flaws in their own work.

---

### 🧰 **Uses of Inspection**
- **Complements testing**: Occurs earlier in the process and identifies issues before testing begins.  
- Suitable for detecting:  
  - **Faults of omission** (e.g., missing features).  
  - **Design problems** (e.g., structural inefficiencies).  
  - **Style issues** (e.g., improper formatting).  

---

### 🔍 **Examples of Inspection**
- Reviewing source code for proper commenting and adherence to style guidelines.  
- Identifying:  
  - Duplications in design.  
  - Misunderstandings or ambiguities in documentation.  
  - Incomplete functionality.  

---

## 🌟 **Benefits of Inspection**

1. **Early Defect Detection**:  
   - Reduces the cost and time required to fix issues later.  

2. **Quantifiable Business Impact**:  
   - Hewlett-Packard: **10:1 ROI**; savings of **$21.4 million/year**.  
     *(Source: Grady & Van Slack, IEEE Software, 1994)*  
   - AT&T Bell Labs: **10x improvement in quality**; **14% productivity gain**.  
     *(Source: Watts Humphrey, Managing the Software Process, 1989)*  
   - Bell Northern Research: Average savings of **33 hours/defect**.  
     *(Source: Russell, IEEE Software, 1991)*  
   - Cisco: Practical outcomes aligned with academic research.  
     *(Source: J. Cohen, Code Review at Cisco Systems, 2006)*  

3. **Comprehensive Defect Discovery**:  
   Identifies issues that may be **impossible or difficult to find** through testing alone.  

4. **Enhanced Team Collaboration**:  
   Encourages knowledge sharing and improves team communication.

---

## 🛠️ **Family of Inspection Techniques**

> **Adapted from K. Wiegers, Peer Reviews in Software: A Practical Guide (2002).**  

Below is a timeline of inspection techniques ranging from **most formal** to **least formal**:
 

```mermaid
timeline

    title Inspection Techniques (From Most Formal to Least Formal)
    Fagan inspections: A technique with well-defined entry and exit conditions, where somebody other than the author of the artifact presents it to the participants. There are many types of inspections: Fagan’s, N-fold, Phased, Gilb’s.
    Team review: A process or meeting during which a software product is presented to project personnel, managers, users, customers, user representatives, or other interested parties for comment or approval.
    Walkthrough: A technique in which a designer or programmer leads members of the development team and other interested parties through a software product. Participants ask questions and make comments about possible errors, violation of development standards, and other problems.
    Tool-assisted code review: An integral part of the coding process. One developer writes code, another developer is asked to review that code providing a line-by-line critique. Assisted by tools, e.g., diff, annotations, email, review history, online commenting.
    Pair programming: Two developers work together at one workstation, sharing the task of writing and reviewing code in real-time.
    Adhoc review: The least formal technique, involving unstructured and spontaneous reviews without predefined rules or documentation.
```

### References

{% bibliography --cited %}