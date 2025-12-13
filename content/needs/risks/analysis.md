---
parent: Risks
title: Analysis
nav_order: 4
layout: default
---

## Risk Analysis
_Adapted from David Root (2014)_

---

### What to Watch Out For (Language & Assumptions)

- Avoid vague modifiers without clarity: e.g. **“may”, “probably”**. These are acceptable if backed by data, but can hide uncertainty.
- If using experience or historical data, _state that_ explicitly (“In prior projects …”, “Historically …”).
- Always consider and record:
    1. **Probability** – How likely is the risk to happen?
    2. **Time frame** – When might it occur?
    3. **Impact** – What’s the magnitude of consequence if it happens?

---

### Probability & Impact, Risk Exposure

| Concept                    | Description                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------------------|
| **Probability / Likelihood** | Could be subjective or based on historical data. Measures how likely a risk will materialize. Use scales (binary, “low-medium-high”, percentages, etc.). |
| **Impact / Consequence**     | What happens if the risk occurs: e.g. schedule delays, cost overruns, quality loss. Needs to be measurable or at least categorized. |
| **Risk Exposure (RE)**       | Combines probability and impact: **RE = Probability × Impact**. Helps compare risks quantitatively. |

---

### Granularity of Measures

- Fewer levels (e.g., High/Low) are easier to agree on but less precise.
- More levels (e.g., 5-point scale) increase resolution but may cause disagreement.
- Common scales:
    - Binary (High / Low)
    - Three-level (Low / Medium / High)
    - Five-level (Very Low / Low / Medium / High / Very High)
- Use terms that make sense for your project (e.g., “Critical”, “Major”, “Minor”).

---

### Example Value Ranges

Possible definitions / thresholds (adjust to your project):

| Measure        | Sample Levels / Thresholds                                  |
|--------------- |------------------------------------------------------------|
| **Probability**| High > 70% <br> Medium ~ 50% <br> Low < 30%                |
| **Timeframe**  | Soon (< 2-4 weeks) <br> Later / Future (> 4 weeks)         |
| **Impact**     | High: Schedule slip > 20%, Cost overrun > 25% <br> Medium: Schedule slip 10-20%, Cost overrun 10-25% <br> Low: Schedule slip 5-10%, Cost overrun 5-10% |

---

### Sources for Estimating Values

- Historical data from past projects (best)
- Voting / expert judgment among your team
- Statistical measures: average, median, mode (when you have data)
- Remove outliers when appropriate (highest / lowest)
- Intuition / domain knowledge when hard data is lacking

---

### Prioritization of Risks

How to decide which risks to focus on:

1. **Set minimum thresholds** — e.g., only address risks that are at least “Medium” in probability _and/or_ impact.
2. **Risk Exposure (RE):** Compute RE for each risk, then sort. The higher the exposure, the earlier you address it.
3. **Priority Matrix / Probability-Impact Matrix:** Plot risks visually (likelihood vs. impact) to see which ones are in the “red” (high/high)—these need action first.

---

### Prioritization Techniques

- **Voting / Ranking:** Everyone assigns ranks or votes to top risks; sum up to see which risk gets the most concern.
- **Multi-voting:** Each person gets several votes (e.g., ⅓ of total number of risks + 1) to distribute among the most important risks; aggregate to focus.
- **Matrix:** Use a grid (e.g., 5×5) with probability (Low to Very High) vs. impact (Low to Very High). Risks in High × High get prioritized.

---

### Example Matrix / Risk Exposure Example

| Risk ID                  | Probability     | Impact                       | Risk Exposure (qualitative or numerical) | Priority |
|--------------------------|-----------------|------------------------------|------------------------------------------|----------|
| R1: Team inexperienced in C# | Medium (50%)    | High (Schedule slip ~20%)     | RE = 0.5 × 20% = 10% (or “Medium-High”)  | High     |
| R2: Key vendor delay         | High (80%)      | Medium (Cost +10%, schedule +15%) | RE = 0.8 × 15% = 12%                     | High     |
| R3: Regulatory change        | Low (20%)       | High (Major rework)           | RE = 0.2 × 30% = 6%                      | Medium   |

Plot these in a matrix: Risks like R1 & R2 land in upper right (“urgent”), R3 may be monitored but not first priority.

---

## Sources & References

- PMI / PMBOK: Probability and impact matrix is a standard tool in qualitative risk analysis.  
- ISO/IEC 31010: Standard for risk assessment techniques; includes probability, impact, and various assessment tools.
- PlaybookTeam: “Risk Exposure = Impact × Probability”.
- AuditBoard: “What is a Risk Assessment Matrix?”
- SafetyCulture: “5x5 Risk Matrix”.

- [Project Management Academy](https://projectmanagementacademy.net/resources/blog/risk-matrix/)
- [ISO/IEC 31010 - Wikipedia](https://en.wikipedia.org/wiki/ISO/IEC_31010)
- [PlaybookTeam](https://playbookteam.com/resources/blog/calculate-risk-exposure)
- [AuditBoard](https://auditboard.com/blog/what-is-a-risk-assessment-matrix)
- [SafetyCulture](https://safetyculture.com/topics/risk-assessment/5x5-risk-matrix/)

---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.

---

## Sources

- Root, David. *Managing Software Development*. Lecture materials, 2014.

---

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
