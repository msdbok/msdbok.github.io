---
parent: Tracking
title: Release
nav_order: 2
layout: default
---

# Release Planning

_adapted from Miranda, 2104_

---

## 1. The Problem

Release dates are often fixed — but the content is not.  
This tension exists in both *predictive* (“Big Up-Front”) and *Agile* approaches.

- Sponsors must accept that they may get **less functionality** than initially hoped.  
- The management challenge: deciding **where to focus effort** and **what to give up** while keeping the project on schedule.

---

## 2. Objectives

By the end of this part, you should be able to:

1. Explain the purpose of release planning.  
2. Describe major release planning approaches.  
3. Understand how uncertainty and prioritization interact.

---

## 3. Releases vs Iterations

| Concept               | Purpose                                         | Typical Duration         |
|:----------------------|:-----------------------------------------------|:------------------------|
| **Iteration / Sprint**| Deliver incremental progress and collect feedback. | 1–4 weeks           |
| **Release**           | Combine multiple iterations into a deliverable version for customers. | Several weeks–months |

**Key benefit:** Limits *Work in Progress (WIP)* and enforces pacing and feedback.

---

## 4. Defining Release Content

> **Release planning** = deciding *when* and *with what features* to deliver working software.

It must balance:
- **Business objectives** (value and urgency)
- **Technical and functional dependencies**
- **Resource constraints** (people, time, budget)

---

### Figure 1 – Knapsack Analogy

Each feature = item with **value** (importance) and **weight** (effort).  
Project time box = *knapsack* with limited capacity.  
→ Goal: **maximize total value** within limited resources.

---

## 5. Overview of Release Planning Methods

| Method                       | Description                                                                 | Notes                    |
|:-----------------------------|:---------------------------------------------------------------------------|:-------------------------|
| **MoSCoW** (Clegg 1994, DSDM Consortium) | Qualitative ranking: *Must / Should / Could / Won’t Have.* Three releases within a fixed time box. | Simple, customer-focused. |
| **SPID** (*Statistically Planned Incremental Delivery*, Miranda 2002) | Quantitative method using subjective probabilities to guarantee delivery consistent with *worst-case* estimates. | Adds statistical confidence. |
| **EVOLVE** (Greer & Ruhe 2003) | Uses a genetic algorithm to maximize value-benefit function; produces *k* optimal release plans. | Complex optimization. |
| **IFM** (*Incremental Funding Method*, Denne & Cleland-Huang 2004) | Divides system into *Minimal Marketable Features (MMFs)* and *Architectural Elements (AEs)*; maximizes Weighted Sequence-Adjusted NPV. | Financially oriented. |
| **Buffered MoSCoW Rules** (Miranda 2011) | Simplified quantitative approach for Agile teams; combines MoSCoW priorities with buffered estimates. | Focus on most valuable functionality within a fixed time box. |

---

## References

[1] M. Denne and J. Cleland-Huang, “The incremental funding method: data-driven software development,” IEEE Software, vol. 21, no. 3, pp. 39–47, May 2004, doi: 10.1109/MS.2004.1293071.
[2] D. Greer and G. Ruhe, “Software release planning: an evolutionary and iterative approach,” Information and Software Technology, vol. 46, no. 4, pp. 243–253, Mar. 2004, doi: 10.1016/j.infsof.2003.07.002.
[3] E. Miranda, “Improving subjective estimates using paired comparisons,” IEEE Software, vol. 18, no. 1, pp. 87–91, Jan. 2001, doi: 10.1109/52.903173.
[4] E. Miranda, “Planning and executing time-bound projects,” Computer, vol. 35, no. 3, pp. 73–79, Mar. 2002, doi: 10.1109/2.989933.
[5] E. Miranda, “Time boxing planning: buffered moscow rules,” SIGSOFT Softw. Eng. Notes, vol. 36, no. 6, pp. 1–5, Nov. 2011, doi: 10.1145/2047414.2047428.


{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
