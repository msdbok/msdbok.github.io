---
parent: Requirements
title: Requirements Organization
nav_order: 5
layout: default
---

# Requirements Organization
---

### Purposes of Organizing Requirements

- **Verification of Completeness**  
    Ensuring you have gathered _all_ necessary requirements; there are no holes.  
    _Example:_ After grouping features, you notice there is no requirement for user password reset — gap identified.
    
- **Verification of Compatibility**  
    Ensuring requirements do not conflict with each other; compatible in what they demand.  
    _Example:_ One requirement wants ultra-fast response times, another wants minimal hardware cost — possible trade-offs must be surfaced.
    
- **Not Contradictory**  
    Ensuring that no two requirements are mutually exclusive or create ambiguity.  
    _Example:_ “System shall use minimal memory” vs “System shall cache lots of data to speed up performance” might conflict unless clarified.
    
- **Communication to Implementers**  
    Organized requirements help developers, testers, designers understand what to do, how things depend, priorities.
    

---

### How to Organize Requirements

After gathering requirements, you should document _and_ organize them. Key techniques:

- **Affinity Groups**  
    Collections of related requirement items grouped by theme, functionality, feature area, or stakeholder concern. Helps make sense of many items.  
    _Definition:_ Grouping ideas/items that are conceptually similar.  
    _Example:_ Group all “report generation” requirements together; group all “user authentication / security” together.
    
- **Hierarchies**  
    Once grouped, structure each group so there are higher-level, more abstract requirements, and lower level, more detailed ones. Lower items elaborate on higher items, dependencies flow downward.  
    _Example:_ High level: “User authentication” → sub-requirements: password reset; OAuth integration; two-factor authentication.
    

---

### Steps to Organize

1. Divide requirements into **affinity groups** (themes).
2. Within each group, build **hierarchical structure**: general → detailed.
3. **Identify gaps**: missing requirements, unclear items, overlaps, conflicts.

---

### Grouping

- Scan all collected needs, ideas (sticky notes or cards help).
- Identify independent themes; each theme becomes a group.
- For each group:
    - Give a prose (short, narrative) description of the group.
    - Explain its high-level need or purpose (“why”).
    - Then list or describe specific requirements that belong.

---

### Requirements Hierarchy

In each group, organize as a tree/hierarchy:

- Levels of abstraction: higher (general, broad), lower (specific, detailed).
- Prioritize: some sub-items may be more urgent / essential than others.
- Identify constraints and dependencies.
- Keep refining: sometimes a general requirement needs more detail.

---

### Annotating & Clarifying Requirements

Requirements often need extra information to reduce ambiguity:

- **Annotations / supporting items**:
    - Use cases / user stories
    - Quality attribute scenarios
    - Prototypes / mockups
    - Equations or metrics (for performance, latency, throughput)
    - Usability studies

_Example:_ For requirement “System shall load dashboard quickly,” annotate with “Dashboard must load in ≤ 2 seconds under 500 concurrent users” (providing measurable metric).

---

### Identifying Gaps

Signs you have missing/incomplete requirements:

- Ideas or requirements that are ungrouped or hard to classify.
- Many miscellaneous groups or “Other” group.
- Frequent “etc.” or “and so on” in descriptions.
- Inconsistent terminology across requirements.
- Derived requirements: requirements that are inferred rather than explicitly stated.

---

### Adding Information & Regrouping

- Add new requirements or additional detail into existing hierarchy (do not restructure everything just because of one new item).
- Only reorganize major structure if many items no longer fit or if better themes become obvious.
- Regrouping can disrupt traceability, so do carefully.

---

### Prioritization

Because not all requirements are equally important or feasible:

- Some functionality or quality attributes are essential, others “nice-to-have”.
- Prioritization helps set stakeholder expectations, plan tradeoffs, manage schedule & resources.

Possible ways to prioritize:

|Priority Levels|What They Mean|
|---|---|
|**Must / High / Essential**|Core features & qualities without which system fails or is unacceptable.|
|**Medium / Should**|Important, but could be delayed or compromised.|
|**Low / Optional / Wishful-Thinking**|Nice extras; possible in later releases.|

- Methods / Tools: Voting (among stakeholders), Quality Attribute Workshop (e.g. QAW), using frameworks like QFD (Quality Function Deployment).

_Example:_ Stakeholders vote on top 5 “Must have” features out of a backlog of 20.

---

## Short Definitions + Examples

|Term|Definition|Example|
|---|---|---|
|**Affinity Group**|A set of requirements grouped by theme / similarity.|All security-related requirements (password, encryption, access control) grouped together.|
|**Hierarchy**|Structuring requirements by levels: general → specific.|“User interface” → “Login page design”, “Dashboard layout”, “Error message style” sub-items.|
|**Gap**|A missing or incompletely specified requirement, often discovered when you try to group or refine.|No requirement exists for performance under load, even though system expected to serve many users.|
|**Annotation**|Extra clarifying information attached to requirement statements: scenarios, metrics, prototypes.|For “system shall be reliable”, annotate: “99.9% uptime, measured over 30-day period”—gives clarity.|
|**Prioritization**|Deciding which requirements are most important / urgent.|Must have: data backup; Should have: dark mode UI; Optional: custom theme.|

---

## Sources

- Affinity grouping is used in Agile as technique to organize brainstormed ideas into thematic clusters. [Dee Project Manager+1](https://deeprojectmanager.com/affinity-grouping-technique/)
- Classification of software requirements (functional / non-functional / design / interface etc.) helps in traceability, accountability, and clarity. [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/software-engineering-classification-of-software-requirements/)

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
