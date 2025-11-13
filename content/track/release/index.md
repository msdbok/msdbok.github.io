---
parent: Tracking
title: Release
nav_order: 2
layout: default
---

# Release Planning

_* adapted from Miranda, 2104_

---

## 1. The Problem: Fixed Dates, Flexible Content

In most real-world projects, **release dates are fixed** — the customer or sponsor expects delivery at a specific time.  
However, **what** will be ready by that date is uncertain.

This situation creates tension in both **predictive** (“big up-front”) and **Agile** approaches:

- The **sponsor** must accept that they may get **less functionality** than they initially hoped for.  
- The **development team** must decide how to use limited time and resources most effectively.  
- The **manager’s challenge** is to choose **where to focus** and **what to postpone**, while still meeting business goals.

Think of it as *negotiating the content of a fixed delivery box.*

---

## 2. Releases vs. Iterations

Modern software projects deliver value **incrementally**, not all at once.

| Concept | Purpose | Typical Duration |
|:--|:--|:--|
| **Iteration / Sprint** | A short cycle that delivers partial progress and collects feedback. | 1–4 weeks |
| **Release** | A bundle of several iterations that becomes a usable product version for customers. | Several weeks to a few months |

### Why this matters

- Each **iteration** helps manage technical and requirement uncertainty.  
- Each **release** provides a **sense of accomplishment** and customer validation.  
- Working in short cycles **limits Work in Progress (WIP)** — preventing teams from spreading effort too thin.  

> **Key principle:** Deliver *something valuable soon* and *learn from it.*

---

### Example

A university develops a **Student Portal** in two major releases per year.
Each release includes four short iterations:

1. Login and dashboard
2. Course registration
3. Grades and transcripts
4. Notifications and helpdesk

After each **iteration**, students test new features and give feedback.
Each release delivers a usable version with progressively richer functionality.

---

## 3. Defining Release Content

> **Release planning** means deciding *when* and *with what features* a working version of the software will be released.

Each release must balance three competing forces:

1. **Business objectives** – What’s most valuable to the customer or business?  
2. **Technical dependencies** – Which features depend on others?  
3. **Resource constraints** – How much time, money, and people do we have?

In other words, *what gives the most value for the effort we can afford?*

---

###  The Knapsack Analogy

Imagine you are packing a **backpack (knapsack)** for a trip:

- Each item (feature) has a **value** (importance) and a **weight** (effort or cost).  
- The backpack (time box) has a **limited capacity** (e.g., 3 months or 500 hours).  

Your goal is to **maximize the total value** of items that fit **without exceeding** the available time.

> 💭 _“You can’t take everything on the trip — so take what’s most valuable.”_

This analogy explains why **release planning** is both a **technical** and **strategic** decision.

---

## 4. Overview of Release Planning Methods

Over time, several methods have been developed to help managers balance value and effort.

| Method | Description | Typical Use |
|:--|:--|:--|
| **MoSCoW** (Clegg, 1994; DSDM Consortium) | Qualitative ranking of features into **Must**, **Should**, **Could**, and **Won’t Have**. Usually applied across three releases. | Simple prioritization for Agile or incremental projects. |
| **SPID** (*Statistically Planned Incremental Delivery*, Miranda 2002) | Quantitative method using subjective probabilities to ensure that the most important features fit within the worst-case estimates — without wasting buffer time. | Projects needing statistical confidence in delivery. |
| **EVOLVE** (Greer & Ruhe 2003) | Uses a **genetic algorithm** to search for the best combination of features maximizing value and minimizing risk. | Research and optimization-based planning. |
| **IFM** (*Incremental Funding Method*, Denne & Cleland-Huang 2004) | Breaks the system into **Minimal Marketable Features (MMFs)** and **Architectural Elements (AEs)**, maximizing **Weighted Sequence-Adjusted NPV**. | Financially-driven product planning. |
| **Buffered MoSCoW Rules** (Miranda 2011) | Simplified quantitative approach that combines MoSCoW prioritization with **buffers** for uncertainty. | Practical for Agile teams — the focus of this lecture. |

---

### Summary of Method Evolution

| Generation | Example | Key Idea |
|:--|:--|:--|
| **Qualitative (1990s)** | MoSCoW | Rely on expert judgment and clear communication with stakeholders. |
| **Quantitative (2000s)** | SPID, EVOLVE | Add mathematical/statistical assurance for better predictability. |
| **Value-Based (2004+)** | IFM | Combine economic metrics with release planning. |
| **Practical Hybrid (2011+)** | Buffered MoSCoW | Bring structure and realism to Agile planning by buffering for uncertainty. |

---

###  Why “Buffered” Matters

The Buffered MoSCoW approach recognizes that **estimates are never exact**.  
By explicitly reserving some capacity for the unexpected, the team avoids late stress and broken promises.

> “Plan for uncertainty — don’t pretend it doesn’t exist.”


## References

1. M. Denne and J. Cleland-Huang, “The incremental funding method: data-driven software development,” IEEE Software, vol. 21, no. 3, pp. 39–47, May 2004, doi: 10.1109/MS.2004.1293071.
2. D. Greer and G. Ruhe, “Software release planning: an evolutionary and iterative approach,” Information and Software Technology, vol. 46, no. 4, pp. 243–253, Mar. 2004, doi: 10.1016/j.infsof.2003.07.002.
3. E. Miranda, “Improving subjective estimates using paired comparisons,” IEEE Software, vol. 18, no. 1, pp. 87–91, Jan. 2001, doi: 10.1109/52.903173.
4. E. Miranda, “Planning and executing time-bound projects,” Computer, vol. 35, no. 3, pp. 73–79, Mar. 2002, doi: 10.1109/2.989933.
5. E. Miranda, “Time boxing planning: buffered moscow rules,” SIGSOFT Softw. Eng. Notes, vol. 36, no. 6, pp. 1–5, Nov. 2011, doi: 10.1145/2047414.2047428.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.
