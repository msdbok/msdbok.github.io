---
parent: Needs
title: Risks
nav_order: 4
layout: default
---

# Risk Management

---

### What is a Risk?

Definitions become more specific in software and engineering contexts:

| Source | Definition / Key Elements |
|---|---|
| **Webster’s** | • Possibility of loss or injury  <br>• The chance of loss  <br>• To expose to hazard or danger |
| **SEI (CMU / SEI-99-TR-029)** | “Possibility of suffering loss.” Loss means impact on project: scope, quality, cost, schedule, or failure. |
| **Charette, _Software Engineering Risk Analysis and Management_, 1989** | • Future event only  <br>• How the past can inform us  <br>• Involves change  <br>• Involves mind, opinion, actions, places  <br>• Involves choice  <br>• Uncertainty of that choice |
| **DAU / Program Management** | Risks = potential future events or conditions with negative effect on achieving program objectives (cost, schedule, performance). |

---

### Key Properties of Risk

- Risk is about _future_ possibilities; until something happens, it remains a risk, not a problem.
- Involves _uncertainty_ (we don’t know whether/when, or how bad).
- Has both _impact_ (if it happens) and _likelihood_ (probability).
- In software projects, risks often affect _scope_, _quality_, _cost_, _schedule_, and sometimes _market_ or _reputation_.

---

### Risk vs Issue / Problem

- **Risk:** Something that _might_ happen; may be positive or negative.  
  _Example_: Adopting a new third-party library might introduce bugs or integration issues.
- **Issue / Problem:** A risk that _has happened_—the uncertainty resolved negatively.  
  _Example_: The third-party library fails on some interactions; now you must fix it (wrappers, patch, etc.).

---

### Types / Categories of Risks

Risk dimensions especially relevant to requirements/specification and software engineering:

| Axis / Type | Examples in Requirements Context |
|---|---|
| **Technical Risks** | Ambiguous requirement leads to wrong interpretation; new technology doesn’t support needed non-functional constraints (e.g., performance, scalability). |
| **Project / Managerial Risks** | Requirements creep (scope increases), poor prioritization, insufficient resources for detailed requirements specification or review. |
| **Business / Strategic Risks** | Market shifts, business goals change so original requirements become obsolete; regulatory changes rendering some requirements noncompliant. |
| **People / Organizational Risks** | Key stakeholder unavailable, miscommunication between requirements engineers and users, staff turnover. |
| **Known / Unknown Risks** | Known from past projects (e.g., poor API documentation), unknown when entering new domains. |

Also consider internal vs. external, tactical vs. strategic risks.

---

### Why Do Risk Management?

- **Prevent** or reduce delays, cost overruns, and quality problems.
- **Reduce surprises** for stakeholders (increase transparency).
- Balance risk vs. opportunity—calculated risks can lead to innovation, but unchecked risk can cause failure.
- Document decisions and mitigation so everyone agrees on what-ifs.
- Improve overall project confidence and planning.

---

### Pitfalls / Downsides of Risk Management

- Risk planning and mitigation can seem like overhead—sometimes “insurance” you never “use.”
- Overly negative mindset: focusing too much on what _can_ go wrong may hinder creativity.
- If management or stakeholders think “we already know the risks,” they may skip proper process—leading to blind spots.
- Mitigation itself has cost and risk; trade-offs are always needed.

---

## Sources

- CMU / SEI’s work on risk (e.g., CMU/SEI-99-TR-029) for definitions.
- _Software Risk Management: A Practical Guide_ (DOE/SQAS), for process templates and metrics.
- Risk Management overviews in project/program management (e.g., DAU / governmental sources) define risk with respect to cost, schedule, and performance.
- Industry blogs and recent articles for up-to-date examples and practice:
    - “9 Risks in Software Development” (clockwise.software)
    - “20 Common Project Risks” (TechnologyAdvice)
    - [content1.dau.edu](https://content1.dau.edu/DAUMIG_se-brainbook_189/content/Management%20Processes/Risk-Management.html)
    - [energy.gov](https://energy.gov/sites/prod/files/cioprod/documents/Risk_Management.pdf)
    - [clockwise.software](https://clockwise.software/blog/software-development-risks/)
    - [technologyadvice.com](https://technologyadvice.com/blog/project-management/project-risks-examples/)

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
