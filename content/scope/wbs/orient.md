---
parent: WBS
title: Orientation
nav_order: 2
layout: default
---

# WBS Orientation

## 1) Why Orientation Matters

**Orientation** is the rule you use to break work down in your WBS.  
Pick one main rule and apply it consistently—it shapes what people “see” when they read your WBS.

- **Sponsor view (outcomes):** “What am I getting?”
- **Delivery team view (tasks/phases/disciplines):** “How will we do it?”
- **Finance view (accounts):** “How will we budget/track it?”  
  Often, a **hybrid** is used (e.g., outcomes at Level 2, then tasks underneath).

---

## 2) Comparing Two LAS CAD WBSs

- **Diagram A (Call Taking / Allocation / Communication):**  
  **Outcome/product-oriented.** Decomposes by delivered subsystems/services.  
  Best for sponsors and scope conversations: boundaries and acceptance are visible.

- **Diagram B (Concept → Supplier Selection → PM → Design → Dev&Test → Deployment → Maintenance → Training):**  
  **Task/phase-oriented.** Decomposes by how you’ll execute.  
  Best for showing delivery approach, schedule planning, and staffing.

**Which presents outcomes and focuses on Sponsor needs?**  
**Diagram A (Outcome-oriented).**

**Which shows you know how to do the system (your know-how)?**  
**Diagram B (Task/phase-oriented).**

---

## 3) Main Orientations (Quick Cues)

| Orientation                | How it breaks down           | Great for                | Watch out for                                  |
|----------------------------|-----------------------------|--------------------------|------------------------------------------------|
| **Outcome / Deliverable**  | Features, subsystems, docs  | Sponsor alignment, scope | Must still show when/how work happens          |
| **Task / Phase**           | Concept, Design, Build, etc.| Process clarity, schedule| Can hide scope (what is delivered?)            |
| **Discipline / Functional**| Teams or skills             | Staffing, responsibility | Can obscure end-to-end deliverables            |
| **Accounting**             | Cost buckets                | Budgeting, reporting     | Not helpful for scope or execution nuance      |
| **Hybrid**                 | Mix of above                | Balancing audiences      | Be consistent, avoid mixing rules at one level |

> **Rule of thumb:** Use **outcomes** for Level 2 when negotiating scope with sponsors; use **tasks/phases** one level below for planning.

---

## 4) Book Project—Seeing Orientations

- **Outcome-oriented:** Chapters, front matter, index, compilation, proof reading, print, PM.  
  Sponsor can count deliverables; scope changes are easy to reason about.

- **Discipline-oriented:** Writer, Copyeditor, Printer—clarifies who does what, helpful for staffing/contracts.

- **Task-oriented:** Writing, Copyediting, Compiling, Gen&Verify, Proof, Printing, PM—shows process pipeline; good for schedule and dependencies.

---

## 5) Which WBS Answers Which Questions Fast?

| Scenario / Question                   | Outcome-oriented | Discipline-oriented | Task/phase-oriented |
|---------------------------------------|------------------|--------------------|---------------------|
| How many chapters?                    | **Easy**         | Hard               | Medium              |
| Who does copyediting?                 | Medium           | **Easy**           | Medium              |
| Drop Chapter 2 – impact on cost?      | **Easy**         | Medium             | Medium              |
| Which chapter is more expensive?      | **Easy**         | Medium             | Medium              |
| Add a new chapter – what changes?     | **Easy**         | Medium             | Medium              |
| Chapter 3 has heavy illustrations?    | Medium           | **Easy**           | Medium              |

> **Outcome orientation best answers scope & sponsor questions.**  
> **Discipline** best answers staffing/ownership.  
> **Task/phase** best answers “how/when” planning.

---

## 6) Choosing an Orientation (Quick Guide)

1. **Primary audience = Sponsor?** Choose **Outcome** (Level 2).
2. **Primary risk = execution complexity?** Add **Task/phase** at next level.
3. **Tight org boundaries or vendors?** Add a **Discipline** layer.
4. **Heavy finance reporting?** Mirror **Chart of Accounts** one level down or via codes.

---

## 7) Quality Rules for Any WBS

- **100% Rule:** Children fully cover (and only cover) the parent’s scope.
- **Mutual exclusivity:** No overlaps between siblings.
- **Consistent grammar:**  
    - Outcomes: noun-heavy (“Chapter 2”, “Index”).
    - Tasks: verb-noun (“Generate Index”).
    - Discipline: team/object (“Copyediting”, “Printing”).
- **Coding & traceability:** Use numbering (1.2.3) and keep a crosswalk (Outcome ↔ Phase ↔ Discipline ↔ Account).

---

## 8) Communicating with Orientation

- For **sponsors**: show the **Outcome WBS** plus milestones.
- For **engineers**: attach the **Task/phase breakdown** under each deliverable.
- For **management/finance**: tag work packages with **discipline** and **account codes**.

---

## 9) Resilience to Change

When scope changes (e.g., “Add Chapter 4”):

1. Add/modify the **outcome** node.
2. Link it to impacted **tasks**, **disciplines**, and **accounts** in the crosswalk.
3. Costs/schedule roll up cleanly—no need to reorganize the entire tree.

---

## One-Minute Recap

- **Orientation = the organizing rule.**
- **Outcome** shows _what you deliver_ (sponsor-first).
- **Task/phase** shows _how you deliver_ (planner-first).
- **Discipline** shows _who delivers_ (org-first).
- Use a **hybrid** thoughtfully and keep a **crosswalk**.

---

## Quick Check

Looking back at your **LAS CAD** diagrams, which would you show first to a **funding sponsor deciding scope**—Diagram A or Diagram B—and why?

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.
