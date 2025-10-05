---
parent: Estimates
title: Expert
nav_order: 2
layout: default
---

# **Expert Judgment in Software Effort Estimation**

## 1. What It Is

Expert judgment (or _expert-based estimation_) means estimating effort or cost by relying on the **experience, intuition, and tacit knowledge** of one or more professionals.  
The reasoning process is usually **non-explicit and non-recoverable** — the expert cannot fully explain _how_ they arrived at the number.

> “Estimation conducted by persons recognised as experts where important parts of the estimation process are based on non-explicit, non-recoverable reasoning processes, i.e., intuition.” — Jørgensen (2004)

---

## 2. Why It Is Used

- It is **the most common software estimation approach** in both research and practice.
- Often **no formal model** fits the context or sufficient data are lacking.
- Expert methods are **flexible**, quick, and work with incomplete information.
- Empirical comparisons show **no consistent accuracy advantage** for formal models like COCOMO; roughly one-third of studies favour experts, one-third models, one-third show no difference (Jørgensen 2004).

---

## 3. Levels of Structure

| Form                   | Description                                                      | Example Methods                       |
|------------------------|------------------------------------------------------------------|---------------------------------------|
| **Unaided individual** | “Finger-in-the-wind” or gut feeling; based purely on personal experience. | A project manager gives a one-number estimate based on past projects. |
| **Structured individual** | Expert uses simple aids like checklists or historical tables.  | A developer adjusts a previous project’s effort by ±20%.              |
| **Structured group**   | Several experts reason together using explicit elicitation and aggregation rules. | **Wideband Delphi**, **Planning Poker**, **Paired Comparisons**.      |

All share the same cognitive basis — intuitive pattern-matching from past experience — but differ in how transparently that intuition is elicited and combined.

---

## 4. Levels of Application

Expert judgment can be applied at:

- **Project level** → estimate total effort or cost.
- **Task level** → estimate specific WBS activities.
- **Deliverable level** → estimate a feature, report, or module.

---

## 5. Top-Down vs Bottom-Up Expert Estimation

_(from Jørgensen 2004)_

| Aspect         | **Top-Down**                                         | **Bottom-Up**                                         |
|----------------|------------------------------------------------------|-------------------------------------------------------|
| **Basis**      | Analogy with whole projects (“This looks like our 2023 payroll app.”) | Sum of detailed task estimates (“UI = 200 h, DB = 100 h …”) |
| **When used**  | Early stages with vague specs.                       | Later stages with detailed WBS.                       |
| **Needs**      | Memory or database of **similar past projects**.     | Technical understanding of component activities.      |
| **Accuracy in study** | Less accurate unless close analogies found.   | Generally more accurate; promotes better understanding of requirements. |
| **Effort to produce** | Faster, cheaper.                              | Slower, more effortful.                               |

**Key empirical finding:**

> Top-down estimates were only accurate when estimators recalled _very similar previous projects_; otherwise bottom-up estimates performed better.

---

## 6. Strengths of Expert Judgment

- Works even with incomplete or qualitative data.
- Incorporates context, risks, and “soft” factors.
- Quick to produce; adaptable during re-estimation.
- Encourages discussion and consensus in teams (Delphi, Planning Poker).

---

## 7. Typical Weaknesses and Biases

- **Overconfidence:** experts give too-narrow ranges of uncertainty.
- **Anchoring:** early guesses influence final numbers.
- **Availability bias:** recall of recent or vivid projects skews judgment.
- **Regression toward the mean:** small projects often over-estimated, large ones under-estimated.
- **Limited transfer:** experience with dissimilar projects leads to large errors.

---

## 8. Improving Expert Estimation

- Use **structured group techniques** (Delphi, Planning Poker) to average biases.
- Provide **calibrated feedback** comparing past estimates vs actuals.
- Maintain a **searchable project history database** so experts can find valid analogies.
- Combine with **model or data-based approaches** (e.g., expert + COCOMO hybrid).
- Elicit and record **ranges** (minimum, most likely, maximum) instead of single points.

---

## 9. Example in Practice

A project manager estimating a new online-banking feature:

1. Thinks of a similar mobile-app feature (analogy).
2. Adjusts for added security layers (+20%).
3. Discusses with peers via Planning Poker; consensus ≈ 480 hours.
4. Adds ±25% uncertainty range.

This process is expert judgment: intuitive, experience-based, but made more reliable by structure and group reasoning.

---

## 10. Summary Table

| Criterion         | Expert Judgment         | Model-Based (e.g., COCOMO) |
|-------------------|------------------------|----------------------------|
| Input needed      | Informal experience    | Quantitative drivers       |
| Transparency      | Low (tacit reasoning)  | High (explicit formula)    |
| Flexibility       | High                   | Low–medium                |
| Accuracy (empirical median) | ≈ ±30 % MRE (typical) | Similar                  |
| Best suited for   | Early estimation, unique projects | Repetitive, data-rich domains |

---

## Source

Jørgensen, Magne. "Top-down and bottom-up expert estimation of software development effort." _Information and Software Technology_ 46.1 (2004): 3-16.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.
