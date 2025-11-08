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

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
