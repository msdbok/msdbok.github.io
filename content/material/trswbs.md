---
parent: Materials
title: TRS WBS Case
nav_order: 3
layout: default
---

# Time Reporting System (TRS) — WBS & FPA Assignment
_Adapted from Eduardo Miranda (2014)_

## 1. Introduction

Your company is bidding on a **turnkey** contract to replace an *existing* **mainframe** time reporting application with a modern **web-based** TRS. Employees report hours against **Pay Codes** (project+task) for **customer billing**. TRS integrates **inbound** with the **Personnel System** (HR master data) and **outbound** with the **Payroll System** (approved timesheets). The client is a large consulting firm with **four offices nationwide**. **Customer training** is in scope but **subcontracted**. TRS must support **remote access** and run on **Chrome, Safari, and Firefox**. Use the document **TimeReportingSystemDescription** as the source of truth.

---

## 2. Tasks

1. Build the WBS (see NASA Hybrid Orientation)
2. Apply Function Point Analysis (FPA) → Person-Months
3. Update the WBS with Estimates and check consistency

---

## 3. Deliverables

### 3.1 Slides (15 min)
- Problem context & scope boundary
- Key assumptions
- **WBS** (NASA hybrid)
- **FPA** method, counts, and PM conversion
- **Mapped WBS with estimates**
- Key risks

### 3.2 Report (max 5 pages, excl. appendices)
- 1: Introduction & assumptions 
- 2: WBS (NASA hybrid)
- 3: FPA (ILF/EIF, EI/EO/EQ tables, UFP, PM conversion)
- 4: Estimated WBS (effort, duration, skills, dependencies)
- 5: Consistency & risk summary (incl. approval policy and delegation scope)
- Appendices: Individual contribution declaration, diagrams, detailed counts, optional WBS dictionary

---

# From UML to FPA (Quick Instructions)

## 4. Set the Boundary

- Mark what’s **inside** (your application) vs. **outside** (actors, external systems).
- Only data crossing this boundary creates **transactions** (EI/EO/EQ) or **external files** (EIF).

---

## 5. Identify Logical Files (from Class/ER diagrams)

- **ILF** (Internal Logical File): a logical, user-recognizable group of data that your app **maintains** (create/update/delete).
    - Usually aggregates: a main class + tightly coupled children (e.g., Header ↔ Rows).
    - One ILF per logical group—not per table.
- **EIF** (External Interface File): a logical, user-recognizable group your app **reads** but is **maintained elsewhere**.
    - If your app ever **creates/updates** it → it’s an **ILF**, not EIF.
- For each ILF/EIF, note:
    - **RETs** (Record Element Types): logical subgroups/child collections a user can recognize (e.g., “Header”, “Line items”).
    - **DETs** (Data Element Types): unique, user-recognizable, non-derived fields (count once per file).

---

## 6. Derive Transactions from Use Case / Class diagrams

Treat each **user goal completed at the boundary** as one elementary process:

- **EI** (External Input): data comes **into** the app and **maintains** an ILF (create, update, delete, status change).
    - Examples: create entity, submit, approve/reject (if it updates an ILF), import feed that persists.
- **EO** (External Output): data goes **out** with **derived calculations**/summaries or controls an external action; may update nothing.
    - Examples: exports, notifications, formatted reports, API pushes.
- **EQ** (External Inquiry): **read-only** request/response with **no derived** totals; simple query/look-up/detail view.
- For each transaction, list:
    - **FTRs** (File Types Referenced): ILFs/EIFs read/maintained by this process (maintained = counted once as FTR).
    - **DETs**: distinct input/output fields crossing the boundary (exclude purely derived and hidden technical fields).

---

## 7. Classify Complexity (use standard IFPUG matrices)

- Use **(DETs × FTRs)** to select **Low/Average/High** for each EI/EO/EQ.
- Use **(DETs × RETs)** to select **Low/Average/High** for each ILF/EIF.

---

## 8. Count & Convert

- Sum function points: **UFP = Σ(ILF/EIF/EI/EO/EQ)** with their weights.
- Convert to effort (PM) using your **stated productivity rate** (e.g., FP per PM).

---

## 9. Practical Rules of Thumb (avoid common errors)

- **One logical file, many tables:** count **1 ILF** if the user sees it as one thing.
- **Reference lists/enums:** ILF if your app maintains them; EIF if read-only from outside; else **don’t count** if static/constant.
- **Status flips (approve/submit/recall):** if they **update** an ILF, count as **EI** (not EO).
- **Reports vs inquiries:** if it includes **derived totals/formatting** → **EO**; if plain retrieval → **EQ**.
- **Batch/API feeds:** inbound that **persists** → **EI**; outbound extract → **EO**.
- **Avoid double counting:** multiple screens/steps that fulfill **one user goal** = **one transaction**.
- **DETs are logical, not technical:** count what a user recognizes; exclude keys repeated across segments, system-generated IDs, or purely derived fields.

Tip: Make three short tables before counting: **Files (ILF/EIF with RETs/DETs)**, **Transactions (EI/EO/EQ with FTRs/DETs)**, and **Assumptions** (what you considered derived/static/external).

---

## 10. Practical conversion rate FP→PMs

**Practical bracket for coursework:** use **~10 FP/PM** as a plausible range.
Source: [Risky Business: Navigating the World of Software Productivity](https://www.iceaaonline.com/wp-content/uploads/2024/06/SWR09-Brown-Risky-Business-Software-Productivity-Paper.pdf)

---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.

---

## Sources

- Brown, William H. "Risky Business: Navigating the World of Software Productivity." *International Cost Estimating and Analysis Association (ICEAA)*, 2024. [https://www.iceaaonline.com/wp-content/uploads/2024/06/SWR09-Brown-Risky-Business-Software-Productivity-Paper.pdf](https://www.iceaaonline.com/wp-content/uploads/2024/06/SWR09-Brown-Risky-Business-Software-Productivity-Paper.pdf)

- Miranda, Eduardo. *Managing Software Development Projects*. Lecture materials, Carnegie Mellon University, 2014.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.