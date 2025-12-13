---
parent: Risks
title: Identification
nav_order: 2
layout: default
---

## Risk Identification
_Adapted from David Root (2014)_

---

### Key Concepts

- A _concern_ is where risk identification starts — something uneasy, uncertain.
- Risks are uncertain future events or conditions, BEFORE they become issues. Once realized, they are issues/problems.
- Identification comes from many inputs: meetings, artifacts (design docs, requirements, test plans), past/historical data, stakeholder communication.

---

### Techniques & Process

| Technique                  | Description / Best Practices                                                                                                                      |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| **Brainstorming / Workshops** | Assemble group of people with different perspectives. Have a facilitator, scribe, timekeeper. Everyone contributes ideas without debate first; organize later. Use checklists/taxonomies to prompt ideas. |
| **Review of Artifacts**        | Requirements docs, design docs, test plans etc. Check for ambiguities, omissions, dependencies, constraints.                                   |
| **Interviews / Stakeholder Input** | Ask domain experts, end users, operational staff about things that worry them. Often uncover external or business risks.                  |
| **Historical / Lessons Learned**  | Examine past projects: what went wrong, what surprised people. Helps find known risk categories.                                           |
| **Formal Methods**               | SEI-SRE, risk taxonomy questionnaires, PROMPT lists. Quantitative/qualitative risk methods.                                                |

---

### When & Who

- Identification is ongoing: it should not be a one-time step. As project evolves, new risks can emerge.
- Everyone participates, not just project manager: technical team, QA, operations, stakeholders, customers.
- Could have dedicated risk‐identification meetings, but also leverage routine meetings (e.g. design reviews, requirements reviews) to spot risks.

---

## Risk Statements

---

### Structure of a Good Risk Statement

From several sources (DoD RIO, PRINCE2, DAU etc.) the attributes are:

| Component                   | What it is                                                                 |
|-----------------------------|----------------------------------------------------------------------------|
| **Condition / Cause / Root Cause** | The situation or trigger that gives rise to risk. A fact / internal or external cause. |
| **Event / Potential Event**        | The uncertain occurrence or situation that might happen (the risk itself).              |
| **Consequence / Effect / Impact**  | What will happen _if_ the risk event occurs. The negative outcomes.                     |

Sometimes cause may be optional or less known; event and consequence are essential.

---

### Formats & Templates

- **If-Then** format: “If [event/condition], then [consequence/impact].” Optionally include cause.  
    _E.g._ If key vendor fails to deliver components on time, then project schedule will slip by X days and costs will increase.
- **Cause-Event-Effect** (PRINCE2): “Due to [cause], there is a threat/event that [event] which would lead to [effect].”
- Sometimes other variants: “Because …, so …, which would …” to reflect PRINCE2 threat/opportunity format.

---

### Do’s and Don’ts in Risk Statements

| Do’s                                                                 | Don’ts                                                                                   |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Do** write short (< ~30 words), fact-based, actionable statements. Focus on what _is_ / what _could be_, not hypothetical “what if” speculation. Include cause when known. | **Don’t** use vague phrasing (“might”, “could” without clarity), lots of acronyms/abbreviations, generalizations. Don’t bundle multiple risks in one statement. Don’t put mitigation or solution into the statement. Don’t push consequence too far out (“in 5 years we’ll be bankrupt”) unless relevant. |
| Do ensure source of condition (internal or external).                | Don’t mix issues (past) with risks (future).                                             |
| Do focus on a single risk per statement.                             | Don’t include uncertain cause + effect in a muddled way; clarity suffers if cause/event/effect are not distinguishable. |

---

### Context & Supporting Information

- Risk statement gives the core elements, but _context_ gives background: what leads to the condition; related events; who is involved; environment / constraints; triggers if any.
- Also assign **owner** (who is responsible), timeframe (when risk might occur), probability / likelihood, impact scale.

---

### Examples

| Example                                                                                                          | Good / Bad | Why                                                                                                    |
|------------------------------------------------------------------------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------|
| “The budget for the project is not yet defined.”                                                                 | _Weak_     | It's more of a problem / missing plan. Doesn’t have event or consequence, and not clearly actionable.  |
| “Requirements might change.”                                                                                     | _Weak_     | Vague: which requirements, why, what impact.                                                           |
| “Because key vendor’s lead time is uncertain (cause), there is a risk that component delivery will be delayed (event), which would delay system integration and increase costs (effect).” | _Good_     | Clear cause, event, effect.                                                                            |
| PRINCE2 style: “Due to the heavy rain (cause), there is a threat that fields might be flooded (event), which would damage the crops (effect).” |            |                                                                                                        |

---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.

---

## Sources

- DEPARTMENT OF ENERGY software risk management guide (SQAS21.01.00) — gives process, forms, templates. [energy.gov](https://energy.gov/sites/prod/files/cioprod/documents/Risk_Management.pdf)
- PRINCE2 Risk Theme (Cause-Event-Effect) for how to articulate and manage risk statements. [prince2.wiki](https://prince2.wiki/practices/risk/) [projex.com](https://www.projex.com/identifying-prince2-risks/)
- DoD RIO Guide — best practices on risk statement including cause / event / consequence. [dau.edu](https://www.dau.edu/library/damag/november-december2017/how-write-good-risk-statement)

- Root, David. *Managing Software Development*. Lecture materials, 2014.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
