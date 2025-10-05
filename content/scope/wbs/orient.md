---
parent: WBS
title: Orientation
nav_order: 2
layout: default
---

# WBS Orientation

## 1) Why orientation matters

**Orientation** = the rule you use to break work down.  
Pick one main rule and apply it consistently; it shapes what people “see” when they read your WBS.

- **Sponsor view (outcomes):** “What am I getting?”
- **Delivery team view (tasks/phases or disciplines):** “How will we do it?”
- **Finance view (accounts):** “How will we budget/track it?”  
  Often you’ll use a **hybrid** (e.g., outcomes at Level 2, then tasks underneath).

---

## 2) Compare your two LAS CAD WBSs

- **Diagram A (Call Taking / Allocation / Communication):**  
  **Outcome / product-oriented.** It decomposes by **delivered subsystems/services**.  
  Best for sponsors and scope conversations: boundaries and acceptance are visible.

```mermaid
flowchart TB
  %% Root
  ROOT["London Ambulance Service CAD system"]

  %% Columns / Groups
  subgraph CT["Call Taking System"]
    direction LR
    CT1["Call information collection system"]
    CT2["Call logger & duplicate removal"]
    CT3["Incident Location Identification System (Gazetteer)"]
  end

  subgraph AA["Ambulance Allocation"]
    direction LR
    AA1["Interface with call taking system"]
    AA2["Ambulance Vehicle Location System (AVLS)"]
    AA3["Allocation Optimization System"]
  end

  subgraph AC["Ambulance Communication"]
    direction LR
    AC1["RIFS Integration System"]
    AC2["MDT real-time status update system"]
    AC3["Resource availability map"]
  end

  %% Connections
  ROOT --> CT
  ROOT --> AA
  ROOT --> AC

  %% Styling
  classDef root fill:#FFD54F,stroke:#F9A825,stroke-width:3,color:#000;
  classDef group fill:#FFF176,stroke:#FBC02D,stroke-width:2,color:#000;
  classDef leaf fill:#FFF9C4,stroke:#FDD835,color:#000;

  class ROOT root;
  class CT,AA,AC group;
  class CT1,CT2,CT3,AA1,AA2,AA3,AC1,AC2,AC3 leaf;
```

- **Diagram B (Concept → Supplier Selection → PM → Design → Dev&Test → Deployment → Maintenance → Training):**  
  **Task/phase-oriented.** It decomposes by **how you’ll execute**.  
  Best for demonstrating delivery approach, schedule planning, and staffing.

```mermaid
flowchart TB
  %% Root
  ROOT["London Ambulance CAD system"]

  %% Groups
  ROOT --> CON["Concept"]
  ROOT --> SUP["Supplier Selection"]
  ROOT --> PM["Project Management"]
  ROOT --> DES["Design"]
  ROOT --> DEV["Development & Testing"]
  ROOT --> DEP["Deployment"]
  ROOT --> MAI["Maintenance"]
  ROOT --> TRN["Training"]

  %% Concept (chain)
  subgraph CON["Concept"]
    direction LR
    C1["Requirements Specification"] 
    C2["System Constraints"]
  end

  %% Supplier Selection (chain)
  subgraph SUP["Supplier Selection"]
    direction LR
    S1["Selection Process"] 
    S2["Publish Tenders"] 
    S3["Review Tenders"] 
    S4["Accept Bid"]
  end

  %% Project Management (chain)
  subgraph PM["Project Management"]
    direction LR
    P1["Define Project Milestones"] 
    P2["Order Hardware"] 
    P3["Training Plans"]
  end

  %% Design (parallel)
  subgraph DES["Design"]
    direction LR
    D1["Functional Requirements"]
    D2["Technical Specifications"]
  end

  %% Development & Testing (parallel)
  subgraph DEV["Development & Testing"]
    direction LR
    V1["Development"]
    V2["Testing"]
  end

  %% Deployment
  subgraph DEP["Deployment"]
    direction LR
    DP1["Deploy"]
  end

  %% Maintenance
  subgraph MAI["Maintenance"]
    direction LR
    M1["Handle Service Requests"]
  end

  %% Training
  subgraph TRN["Training"]
    direction LR
    T1["Train Users"]
  end

  %% Styling (yellow theme)
  classDef root fill:#FFD54F,stroke:#F9A825,stroke-width:3,color:#000;
  classDef group fill:#FFF176,stroke:#FBC02D,stroke-width:2,color:#000;
  classDef leaf fill:#FFF9C4,stroke:#FDD835,color:#000;

  class ROOT root;
  class CON,SUP,PM,DES,DEV,DEP,MAI,TRN group;
  class C1,C2,S1,S2,S3,S4,P1,P2,P3,D1,D2,V1,V2,DP1,M1,T1 leaf;
```

**Answers to your questions**

- _Which presents outcomes and focuses on Sponsor needs?_ **Diagram A (Outcome-oriented).**
- _Which shows you know how to do the system (your know-how)?_ **Diagram B (Task/phase-oriented).**

---

## 3) The main orientations (with quick cues)

| Orientation                   | How it breaks down                | Great for                    | Watch out for                                 |
|-------------------------------|-----------------------------------|------------------------------|-----------------------------------------------|
| **Outcome / Deliverable / Product** | Features, subsystems, documents, releases | Sponsor alignment, scope control, acceptance criteria | You must still show when/how work happens (use a crosswalk to schedule) |
| **Task / Phase**              | Concept, Design, Build, Test, Deploy, etc. | Process clarity, scheduling, resource loading | Can hide scope (what exactly is delivered?)   |
| **Discipline / Functional**   | Teams or skills: Analysis, UX, Backend, QA, Ops | Org staffing, cost centers, responsibility | Can obscure end-to-end deliverables           |
| **Accounting**                | Chart of accounts, cost buckets   | Budgeting, reporting         | Not helpful for scope or execution nuance      |
| **Hybrid**                    | e.g., Level 2 outcomes → Level 3 tasks | Balancing audiences          | Be consistent and avoid mixing rules at the same level |

> **Rule of thumb:** Use **outcomes** for Level 2 when negotiating scope with sponsors; use **tasks/phases** one level below for planning the work.

---

## 4) The Book project—seeing orientations

- **Outcome-oriented (your first Book WBS):** top level = chapters, front matter, index, compilation, proof reading, print, PM.  
  Sponsor can count deliverables (e.g., “3 chapters + ToC + LoF + Index”). Scope changes (add chapter) are easy to reason about.

```mermaid
flowchart TB
  %% Root
  ROOT["Book"]

  %% Columns / Groups
  subgraph CH1["Chapter 1"]
    direction LR
    CH1W["Writing"]
    CH1C["Copyediting"]
  end

  subgraph CH2["Chapter 2"]
    direction LR
    CH2W["Writing"]
    CH2C["Copyediting"]
  end

  subgraph CH3["Chapter 3"]
    direction LR
    CH3W["Writing"]
    CH3C["Copyediting"]
  end

  subgraph FM["Front matter"]
    direction LR
    subgraph TOC["Table of Content"]
      direction LR
      TOC_G["Generation"]
      TOC_V["Verification"]
    end
    subgraph LOF["List of Figures"]
      direction LR
      LOF_G["Generation"]
      LOF_V["Verification"]
    end
  end

  subgraph IDX["Index"]
    direction LR
    IDX_G["Generation"]
    IDX_V["Verification"]
  end

  subgraph COM["Compilation"]
    direction LR
    COM1["Compilation"]
  end

  subgraph PRF["Proof Reading"]
    direction LR
    PRF1["Proof Reading"]
  end

  subgraph PRT["Print"]
    direction LR
    PRT1["Print"]
  end

  subgraph PM["Project Management"]
    direction LR
    PM1["Project Management"]
  end

  %% Connections
  ROOT --> CH1
  ROOT --> CH2
  ROOT --> CH3
  ROOT --> FM
  ROOT --> IDX
  ROOT --> COM
  ROOT --> PRF
  ROOT --> PRT
  ROOT --> PM

  %% Styling
  classDef root fill:#FFD54F,stroke:#F9A825,stroke-width:3,color:#000;
  classDef group fill:#FFF176,stroke:#FBC02D,stroke-width:2,color:#000;
  classDef leaf fill:#FFF9C4,stroke:#FDD835,color:#000;

  class ROOT root;
  class CH1,CH2,CH3,FM,IDX,COM,PRF,PRT,PM,TOC,LOF group;
  class CH1W,CH1C,CH2W,CH2C,CH3W,CH3C,TOC_G,TOC_V,LOF_G,LOF_V,IDX_G,IDX_V,COM1,PRF1,PRT1,PM1 leaf;
```

- **Discipline-oriented (Writer / Copyeditor / Printer):** clarifies **who** does **what**, helpful for staffing and contracts.

```mermaid
flowchart TB
  %% Root
  ROOT["Book"]

  %% Columns / Groups
  subgraph WR["Writer"]
    direction LR
    WR1["Write"]
    WR2["Proof reading"]
  end

  subgraph CE["Copyeditor"]
    direction LR
    CE1["Project Management"]
    CE2["Copyediting"]
    CE3["Compiling"]
    CE4["Proof reading"]
  end

  subgraph PR["Printer"]
    direction LR
    PR1["Generate Table of Content"]
    PR2["Generate List of Figures"]
    PR3["Generate Index"]
    PR4["Prepare proof"]
    PR5["Print"]
  end

  %% Connections
  ROOT --> WR
  ROOT --> CE
  ROOT --> PR

  %% Styling
  classDef root fill:#FFD54F,stroke:#F9A825,stroke-width:3,color:#000;
  classDef group fill:#FFF176,stroke:#FBC02D,stroke-width:2,color:#000;
  classDef leaf fill:#FFF9C4,stroke:#FDD835,color:#000;

  class ROOT root;
  class WR,CE,PR group;
  class WR1,WR2,CE1,CE2,CE3,CE4,PR1,PR2,PR3,PR4,PR5 leaf;
```

- **Task-oriented (Writing / Copyediting / Compiling / Gen&Verify / Proof / Printing / PM):** shows the **process** pipeline; good for schedule and dependencies.

```mermaid
flowchart TB
  %% Root
  ROOT["Book"]

  %% Columns / Groups
  subgraph WR["Writing"]
    direction LR
    WR1["Chapter 1"]
    WR2["Chapter 2"]
    WR3["Chapter 3"]
  end

  subgraph CE["Copyediting"]
    direction LR
    CE1["Chapter 1"]
    CE2["Chapter 2"]
    CE3["Chapter 3"]
  end

  subgraph CO["Compiling"]
    direction LR
    CO1["Chapter 1"]
    CO2["Chapter 2"]
    CO3["Chapter 3"]
  end

  subgraph GV["Generation & Verification"]
    direction LR
    GV1["Table of Content"]
    GV2["List of Figures"]
    GV3["Index"]
  end

  subgraph PRF["Proof reading"]
    direction LR
    PRF1["Proof"]
  end

  subgraph PRT["Printing"]
    direction LR
    PRT1["Printing"]
  end

  subgraph PM["Project Management"]
    direction LR
    PM1["Project Management"]
  end

  %% Connections
  ROOT --> WR
  ROOT --> CE
  ROOT --> CO
  ROOT --> GV
  ROOT --> PRF
  ROOT --> PRT
  ROOT --> PM

  %% Styling
  classDef root fill:#FFD54F,stroke:#F9A825,stroke-width:3,color:#000;
  classDef group fill:#FFF176,stroke:#FBC02D,stroke-width:2,color:#000;
  classDef leaf fill:#FFF9C4,stroke:#FDD835,color:#000;

  class ROOT root;
  class WR,CE,CO,GV,PRF,PRT,PM group;
  class WR1,WR2,WR3,CE1,CE2,CE3,CO1,CO2,CO3,GV1,GV2,GV3,PRF1,PRT1,PM1 leaf;
```

---

## 5) Which WBS answers which questions fast?

| Scenario / Question                           | Outcome-oriented | Discipline-oriented | Task/phase-oriented |
|-----------------------------------------------|------------------|--------------------|---------------------|
| **How many chapters?**                        | **Easy**         | Hard               | Medium              |
| **Who does copyediting?**                     | Medium           | **Easy**           | Medium              |
| **Drop Chapter 2 – impact on total cost?**    | **Easy**         | Medium             | Medium              |
| **Which chapter is more expensive (2 vs 3)?** | **Easy**         | Medium             | Medium              |
| **Add a new chapter – what changes?**         | **Easy**         | Medium             | Medium              |
| **Chapter 3 has heavy illustrations – where does that work live?** | Medium | **Easy** | Medium |

> Takeaway: **Outcome orientation best answers scope & sponsor questions.**  
> **Discipline** best answers staffing/ownership.  
> **Task/phase** best answers “how/when” planning.

---

## 6) Choosing an orientation (quick decision guide)

1. **Primary audience = Sponsor?** Choose **Outcome** (Level 2).
2. **Primary risk = execution complexity?** Add **Task/phase** at the next level.
3. **Tight org boundaries or vendors?** Add a **Discipline** layer (but not at the same level as outcomes).
4. **Heavy finance reporting?** Mirror the **Chart of Accounts** one level down or via codes.

---

## 7) Quality rules for any WBS

- **100% Rule:** Children fully cover (and only cover) the parent’s scope.
- **Mutual exclusivity:** No overlaps between siblings.
- **Consistent grammar with orientation:**
    - Outcomes: noun-heavy (“Chapter 2”, “Index”).
    - Tasks: verb-noun (“Generate Index”).
    - Discipline: team/object (“Copyediting”, “Printing”).
- **Coding & traceability:** Use numbering (1.2.3) and keep a **crosswalk** (Outcome ↔ Phase ↔ Discipline ↔ Account) so you can pivot without rebuilding the WBS.

---

## 8) Communicating with orientation

- For **sponsors**: show the **Outcome WBS** plus a milestone view.
- For **engineers**: attach the **Task/phase breakdown** under each deliverable.
- For **management/finance**: tag work packages with **discipline** and **account codes**.

---

## 9) Resilience to change

When scope changes (e.g., “Add Chapter 4” or “Color figures in Chapter 3”):

1. Add/modify the **outcome** node.
2. In the crosswalk, link it to the impacted **tasks**, **disciplines**, and **accounts**.
3. Costs/schedule roll up cleanly—no need to re-organize the entire tree.

---

### One-minute recap

- **Orientation = the organizing rule.**
- **Outcome** shows _what you deliver_ (sponsor-first).
- **Task/phase** shows _how you deliver_ (planner-first).
- **Discipline** shows _who delivers_ (org-first).
- Use a **hybrid** thoughtfully and keep a **crosswalk**.

---

### Quick check (one question)

Looking back at your **LAS CAD** diagrams, which would you show first to a **funding sponsor deciding scope**—Diagram A or Diagram B—and why?

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.