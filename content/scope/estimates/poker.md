---
parent: Estimates
title: Poker
nav_order: 3
layout: default
---

# Planning Poker – Structured Expert Estimation Technique

## 1. Why We Need Structured Estimation

Unaided expert estimation often fails because it depends on **intuition and tacit knowledge** that’s hard to explain or verify. This leads to **cognitive and group biases**:

| **Bias Type**         | **Description**                                 | **Example**                                      |
|-----------------------|-------------------------------------------------|--------------------------------------------------|
| **Availability**      | Recent or vivid experiences dominate judgment.  | “This sprint took forever; this one will too.”   |
| **Anchoring**         | First number mentioned influences others.       | “Last project was 100 days → probably similar.”  |
| **Representativeness**| Ignoring actual data, assuming similar tasks take similar time. | “It’s another login feature, so same effort.”    |
| **Confirmation**      | Seeking only evidence that supports initial belief. | “My estimate seems right; I’ll skip checking.”   |
| **Groupthink / Conformity** | People align with the dominant opinion.   | Junior devs agree with senior’s estimate.        |

**Structured group estimation methods**—like _Wideband Delphi, Successive Approximations, Planning Poker,_ and _Paired Comparisons_—are designed to **counter these biases** by making reasoning explicit, collective, and repeatable.

---

## 2. Purpose of Group Estimation

Group estimation works only if everyone shares a **common understanding** of what’s being estimated:

- Are **assumptions** and **ground rules** clear?
- Is the **definition of “done”** shared?
    > e.g., “Work is done when code is checked in, unit tests pass, and documentation is written.”
- Does the estimate include **rework** and **support tasks**?
- Is the work **broken down enough** to avoid missing or double-counting tasks?

This shared understanding prevents many classic estimation errors.

---

## 3. What Is Planning Poker

- **Proposed by:** _James Grenning (2002)_
- **Popularized by:** _Mike Cohn (2005)_
- **Type:** Group, iterative estimation process.
- **Origin:** A simplified version of _Wideband Delphi_ for Agile teams.
- **Use:**
    - Early in _release planning_ (for sizing and prioritizing stories).
    - Complemented later by detailed _task planning_ at iteration start.

---

## 4. What It Estimates

| **Mode**        | **What It Measures**                  | **Best For**                        | **Example Unit**                |
|-----------------|--------------------------------------|-------------------------------------|----------------------------------|
| **Ideal Days**  | Pure effort assuming no interruptions or dependencies. | Non-recurrent tasks (e.g., system design, integration). | “3 ideal days” = full-time work for one dev. |
| **Story Points**| Relative size/complexity vs. a reference story. | Comparable, recurring tasks (e.g., coding features). | “Story A = 3 points, Story B = 8 points.”    |

> _Start by agreeing on a baseline story_ (medium complexity).  
> Example: assign it **3 or 5 points** and compare all others against it.

---

## 5. Planning Poker Procedures: Standard vs. Miranda’s Enhanced Version

| **Step**                   | **Standard Planning Poker (Grenning 2002 / Cohn 2005)**                                                                   | **Eduardo Miranda’s Enhanced Version (2008)**                                                                                                                                                 |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. Preparation**         | Each estimator receives a deck of cards showing possible estimates (typically Fibonacci numbers: 1, 2, 3, 5, 8, 13, 20…). | Same, but first select a _baseline story_ of medium complexity (assigned 3 or 5 points) to ensure consistent relative sizing.                                                                 |
| **2. Story presentation**  | Product Owner reads the user story; team discusses scope, assumptions, and acceptance criteria briefly.                   | Same, but emphasize clarifying what is included in the estimate (e.g., testing, documentation, integration).                                                                                  |
| **3. Private estimation**  | Each estimator secretly selects one card representing their estimate.                                                     | Same — estimators select a card individually and privately.                                                                                                                                   |
| **4. Reveal**              | All cards are revealed simultaneously to avoid anchoring bias.                                                            | Same simultaneous reveal, but note that identical numbers may come from _different reasoning_.                                                                                                |
| **5. Discussion**          | Discuss differences — particularly highest and lowest values — to uncover differing assumptions.                          | Discuss _both differences and coincidences_, ensuring shared understanding even when estimates match.                                                                                         |
| **6. Re-estimate**         | A new round of estimation and reveal occurs until estimates converge or reach consensus.                                  | Re-estimate **one more time**, allowing estimators to reconsider based on the discussion.                                                                                                     |
| **7. Final check**         | Team agrees on a consensus value (or uses an average).                                                                    | After one final reflection, estimators may _change their estimates one last time_ before recording final values.                                                                              |
| **8. Recording results**   | Record the final team estimate.                                                                                           | Record _each estimator’s final individual estimate_ to retain spread information.                                                                                                             |
| **9. Post-session review** | None formally prescribed.                                                                                                 | After all stories are estimated, review recorded values:  <br>• Compute a **mean** for each story.  <br>• Investigate stories showing **unusual disagreement** rather than averaging blindly. |
| **Focus**                  | Efficiency and quick team convergence.                                                                                    | Deeper understanding, validation of reasoning, and identification of inconsistent judgments.                                                                                                  |

---

## 6. Strengths of Planning Poker

- Uses the **collective knowledge** of the whole team.
- **Reduces anchoring and conformity** by keeping initial estimates secret.
- Builds a **shared understanding** of the work.
- Encourages **relative thinking** (compare against known stories).
- Focuses discussion only where there are **real differences**.
- Builds **commitment and ownership** among estimators.

---

## 7. Weaknesses and Limitations of Planning Poker

1. **Lack of External Calibration**  
    Planning Poker depends entirely on the **team’s internal experience**. There is no external benchmark or use of historical data, which makes estimates subjective and potentially inconsistent across projects.
2. **Relative Sizing Drift**  
    Because Planning Poker uses **relative estimation**, the meaning of a “3” or “5” can shift over time. If the baseline story isn’t well defined or periodically revisited, the team gradually loses consistency in how it interprets story points.
3. **Hidden Disagreement**  
    Even when all team members choose the same number, they may have **different reasons** for doing so. Without probing those rationales, agreement on the number can hide genuine differences in understanding of scope or complexity.
4. **Lack of Cross-Project Consistency**  
    Since estimates are relative and team-specific, they **cannot be compared** reliably across different teams or projects. A “5” in one team might represent a very different effort than a “5” in another.
5. **No Formal Method for Combining Estimates**  
    The process doesn’t specify **how to merge or average** estimates once they’re collected. Simple averaging can distort results, especially when there are outliers or wide uncertainty ranges.
6. **Poor Fit for Architectural or Infrastructure Work**  
    Planning Poker works best for **user stories of similar type and scope**. Architectural tasks, infrastructure setup, or research spikes are difficult to relate to story size, making relative estimation unreliable for those items.

---

## 8. Example

**User Story:** “As a user, I can reset my password by email.”

**Team Process:**

1. Discuss dependencies (email API, UI form, validation).
2. Everyone chooses a card →
    - Dev A: 3, Dev B: 5, Dev C: 8.
3. Reveal cards → discuss why C chose 8 (mentions multi-language templates).
4. New round → all pick 5.
5. Final estimate: **5 story points.**

---

## 9. Summary Table

| **Aspect**         | **Planning Poker**         | **Wideband Delphi**         |
|--------------------|---------------------------|-----------------------------|
| Participants       | Whole team                | Selected experts            |
| Rounds             | Few (1–3)                 | Several (3–5)               |
| Communication      | Open discussion           | Anonymized feedback between rounds |
| Output             | Consensus or mean estimate| Aggregated expert estimate  |
| Typical Context    | Agile sprint/release planning | Early project estimation   |

---

## Sources

Cohn, Mike. _Agile estimating and planning_. Pearson Education, 2005.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.
