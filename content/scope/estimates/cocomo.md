---
parent: Estimates
title: COCOMO
nav_order: 10
layout: default
---

# COCOMO II

## 1. What is COCOMO II (and motivation)

### 1.1 Origin & Primary Source

- COCOMO II (Constructive Cost Model II) is an updated, more flexible version of the original COCOMO model (Boehm, 1981) designed to better reflect modern software development practices (reuse, incremental development, COTS, object-oriented, etc.).
- The authoritative “primary source” is the **COCOMO II Model Definition Manual** (USC Center for Software Engineering), which describes the model, calibration, cost drivers, scale factors, and usage.
- Also, the book _Software Cost Estimation with COCOMO II_ (Boehm et al.) is a canonical reference.
- When using COCOMO II in academic or professional work, it’s good to reference the manual (e.g. version 2.1) or the Boehm et al. book.

### 1.2 Why COCOMO II (versus original COCOMO)

- The original COCOMO (“COCOMO 81”) was calibrated on older projects, with more rigid waterfall processes, little reuse, mainly monolithic systems.
- It lacked support for aspects of modern software engineering: reuse, object orientation, incremental/iterative development, commercial off-the-shelf (COTS), rapid application assembly, evolving architectures, and modern process maturity.
- COCOMO II addresses these by introducing new cost drivers, scale factors, and different estimation modes (e.g. Early Design, Post-Architecture).
- It is more modular, tailorable, and supports calibration to local data (i.e. you can adapt parameters to your organization’s history).

---

## 2. Structure of COCOMO II: Estimation Modes / Submodels

COCOMO II is not a single monolithic formula. It offers **three (main) submodels / modes**, suited to different stages of a software project’s lifecycle, with increasing detail as you know more.

| Submodel / Mode         | When used                                    | Size metric / inputs                    | Number of cost drivers / detail      |
|------------------------ |----------------------------------------------|-----------------------------------------|--------------------------------------|
| **Application Composition** | Very early prototyping, GUI builder, rapid composition / assembly of components | _Object points_ (screens, reports, third-gen modules) | Few, coarse drivers                  |
| **Early Design**        | After requirements are clearer but before architecture is fully fixed | KSLOC (or derived from function points) + coarse cost drivers | ~6 cost drivers + scale factors      |
| **Post-Architecture**   | After architecture is set, when enough detail is known | KSLOC (or SLOC) + detailed cost drivers + scale factors | ~17 cost drivers + 5 scale factors   |

- In early phases you may not know many details, so you use the simpler models (Application Composition → Early Design) and gradually refine them.
- Once architecture is stable, the **Post-Architecture** mode gives you the most accurate estimate, using detailed cost drivers (effort multipliers) and scale factors.
- The model supports _reuse / adaptation_ (i.e. not all code is written from scratch). It has provisions to adjust for reused code, modified code, etc.

---

## 3. Core Formulas and Terms

### 3.1 Effort (Person-Months) Formula (Nominal)

In COCOMO II (for Early Design or Post-Architecture), effort is estimated as:

$$
\text{Effort (PM)} = A \times (\text{Size})^E \times \prod_{i=1}^{n} EM_i
$$

Where:

- *A* is a calibration constant (nominal productivity)
- *Size* is measured in thousands of source lines of code (KSLOC) (after adjusting for reuse)
- *E* is the _scale exponent_, which captures economies/diseconomies of scale
- *EM_i* are the _effort multipliers_ (cost drivers) — multiplicative modifiers for various project attributes
- *n* is the number of cost drivers (e.g. ~6 for Early Design, ~17 for Post-Architecture)

The exponent *E* is computed as:

$$
E = B + 0.01 \times \sum_{j=1}^{5} SF_j
$$

Where:

- *B* is a base exponent (e.g. 0.91 in default calibration)
- *SF_j*$* for *j=1..5* are the 5 _scale factors_ (precedentedness, flexibility, architecture/risk resolution, team cohesion, process maturity) that capture how project scale interacts nonlinearly.

Thus:

$$
\text{Effort (PM)} = A \times (\text{KSLOC})^{B + 0.01 \sum SF_j} \times \prod EM_i
$$

Once you have effort in PM, you can compute schedule (in months) by:

$$
\text{Schedule (TDEV)} = C \times (\text{Effort})^F
$$

where

$$
F = D + 0.2 \times (E - B)
$$

and *C*, *D* are calibration constants.

---

### 3.2 Scale Factors (SF) — Influence Exponent

The 5 scale factors (sometimes also called _exponents factors_ or _scaling drivers_) in COCOMO II are:

1. **PREC** (Precedentedness) — degree to which the project is similar to past experience
2. **FLEX** (Development Flexibility) — how much freedom the developers have in how software is constructed
3. **RESL** (Architecture / Risk Resolution) — degree to which architecture and risk resolution is done early
4. **TEAM** (Team Cohesion) — how well the team works together
5. **PMAT** (Process Maturity) — the maturity of the organization’s processes (often aligned with CMM or similar)

Each is rated (Very Low, Low, Nominal, High, Very High, Extra High) and given a numeric weight. The sum of those weights (times 0.01) is added to the base exponent *B*.

These scale factors permit _nonlinear scale effects_ (i.e. larger projects may incur increasing overheads).

---

### 3.3 Effort Multipliers (EM) — Cost Drivers

These are multiplicative factors (>0) that adjust the nominal effort depending on project-specific attributes (product, platform, personnel, project, etc.). In Post-Architecture there are ~17 EMs; in Early Design a subset is used. Some examples:

- Personnel capability, experience, tool usage
- Required reliability
- Execution time constraints
- Memory constraints
- Platform volatility
- Reuse / adaptation factors
- Documentation requirements
- Development schedule (SCED) as a special driver to adjust for schedule compression or expansion

Each EM is rated on a scale (Very Low to Extra High) with associated numerical multipliers. The product of all $EM_i$ gives an adjustment to the base effort.

---

### 3.4 Reuse / Adaptation Model (Adjusting Size)

Not all code in a project is necessarily new. COCOMO II includes a reuse / adaptation adjustment to the effective size. This is often expressed via the **Adaptation Adjustment Factor (AAF)**, based on:

- DM: percentage of design modified
- CM: percentage of code modified
- IM: percentage of integration or understanding effort
- AT: percentage of the code that is _automatically translated_ (if doing reengineering)
- Productivity factor for automatic translation (ATPROD)

A formula modifies the effective “new code size” so that reused parts contribute less.

In short, the model can discount the effort for portions of code reused or translated automatically.

---

## 4. Example

Below is a (simplified) worked example adapted from standard textbook/case examples. Some cost driver values are simplified for clarity but retain core methodology.

### 4.1 Problem Definition

Suppose you are developing a software system which, after requirements and preliminary design, is estimated at **50,000 source lines of code** (i.e. 50 KSLOC) of new development (i.e. not counting reused modules). You will use the **Post-Architecture** model (i.e. detailed model). You assign scale factors and cost drivers as follows (just illustrative):

#### Scale Factors (SF):

| Factor | Rating   | Weight (example) |
|--------|----------|------------------|
| PREC   | Nominal  | 3.72             |
| FLEX   | High     | 2.03             |
| RESL   | Nominal  | 4.24             |
| TEAM   | High     | 1.10             |
| PMAT   | Nominal  | 3.12             |

$$\sum SF_j = 3.72 + 2.03 + 4.24 + 1.10 + 3.12 = 14.21$$

Let base *B = 0.91* (a typical default from calibration).

Hence:

$$
E = B + 0.01 \times \sum SF_j = 0.91 + 0.01 \times 14.21 = 0.91 + 0.1421 = 1.0521
$$

#### Cost Drivers (EM_i) — Example Values:

Suppose we pick, say, 10 cost drivers (for simplicity) and assign them multipliers (these are illustrative, not real calibration tables). For example:

- RELY (required reliability) = 1.10
- DATA (data complexity) = 1.00
- CPLX (product complexity) = 1.15
- TIME (execution time constraint) = 1.00
- STOR (memory constraint) = 1.00
- PVOL (platform volatility) = 1.05
- ACAP (analyst capability) = 0.90
- PCON (personnel continuity) = 1.00
- TOOL (use of software tools) = 0.85
- SCED (schedule compression) = 1.05

Multiply them:

$$
\prod EM_i = 1.10 \times 1.00 \times 1.15 \times 1.00 \times 1.00 \times 1.05 \times 0.90 \times 1.00 \times 0.85 \times 1.05
$$

Let’s compute that stepwise:

- 1.10 × 1.15 = 1.265
- × 1.05 = 1.32825
- × 0.90 = 1.195425
- × 0.85 = 1.01611125
- × 1.05 = 1.066 (approx)
- (plus the other cost drivers 1.00 don’t change)

So assume $\prod EM_i \approx 1.066$

#### Calibration Constant A

From the COCOMO II manual, a default value of A = 2.94 is often used.

Thus:

$$
\text{Effort (PM)} = 2.94 \times (50)^{1.0521} \times 1.066
$$

$$\text{Compute 50}^{1.0521}:$$

$$\ln(50) \approx 3.9120$$
$$1.0521 \times 3.9120 = 4.120$$
$$e^{4.120} \approx 61.58$$

Thus:

$$
\text{Effort} \approx 2.94 \times 61.58 \times 1.066 \approx 2.94 \times 65.60 \approx 192.82 \, \text{PM}
$$

So the estimate is about **193 person-months** of effort.

#### Schedule (TDEV)

Use the schedule formula:

$$
F = D + 0.2 \times (E - B)
$$

Let’s assume default values D = 0.28, B = 0.91 (from calibration).

We have *E = 1.0521*, so:

$$
F = 0.28 + 0.2 \times (1.0521 - 0.91) = 0.28 + 0.2 \times 0.1421 = 0.28 + 0.02842 = 0.30842
$$

Also, the constant *C* (schedule coefficient) is often about 3.67.

Hence:

$$
\text{TDEV} = 3.67 \times (192.82)^{0.30842}
$$

Compute exponent:

$$\ln(192.82) = 5.257$$
$$0.30842 \times 5.257 = 1.621$$
$$e^{1.621} \approx 5.06$$

Thus:

$$
\text{TDEV} \approx 3.67 \times 5.06 \approx 18.58 \, \text{months}
$$

So the projection is roughly **18.6 months** schedule.

Thus, summarizing:

- Effort ≈ **193 person-months**
- Time ≈ **18.6 months**

From that you could derive average staffing (193 / 18.6 ≈ 10.4 people) etc.

---

### 4.2 Interpretation, Caveats, and Further Adjustments

- The example above is illustrative; in practice you’d use real calibration tables for multipliers and scale factors from the manual, or better, from your organization’s own historical data.
- You may also refine by applying **reuse / adaptation** adjustments if portions of the software are reused or automatically translated (i.e. discount effort for reused parts).
- The schedule estimate TDEV is a _nominal schedule_; if you force compression or expansion beyond what is normal, additional adjustment may be needed (the SCED cost driver addresses schedule effects).
- You should treat these estimates as a **range** (best, most likely, worst) given uncertainty in the inputs.
- Calibration to local organization data often improves accuracy significantly. Many studies show that “off-the-shelf” default COCOMO II parameters can have nontrivial errors if local practices differ.
- Always validate your estimate by comparing with expert judgments, analogous estimates, or other models (e.g. function point estimation, parametric models, or machine learning models) to triangulate.
- Be especially cautious about estimating **size** (KSLOC) itself; size is often the largest source of uncertainty.

---

## 5. Strengths, Weaknesses, & Practical Tips

### 5.1 Strengths

- Well documented, with openly published formulas and calibration data (transparent).
- Supports modern software practices: reuse, COTS, iterative development, architectural risk resolution.
- Allows hierarchical estimation: early rough estimate progressing to refined estimate.
- Supports calibration (i.e. you can tune constants using your historical projects) to adapt the model to your environment.
- Incorporates nonlinear scaling (via scale factors) and multiplicative cost drivers to reflect interactions.

### 5.2 Weaknesses / Limitations

- Garbage in, garbage out: if your estimations of cost drivers, scale factors, or size are poor, the result will be poor.
- Sometimes difficult to assign true, objective ratings to cost drivers and scale factors (subjectivity).
- The calibration constants (A, B, C, D) from the standard database may not reflect your organization’s productivity or domain, so bias may creep in.
- In some domains (e.g. extremely small or extremely large systems, or highly experimental R&D), the model may be less accurate.
- The model is static (i.e. not dynamic over time); it does not inherently account for evolving scope, changing requirements, or schedule “creep” unless you explicitly model them.
- Estimating size (KSLOC or function points) is itself a major challenge and source of error, especially early in the project.
- The reuse / adaptation part, while useful, introduces additional complexity and uncertainty.

### 5.3 Practical Tips & Best Practices

1. **Use ranges** for inputs (size, cost drivers) and compute a range of estimates (optimistic, nominal, pessimistic).
2. **Calibrate**: whenever possible, calibrate A, B, and possibly cost driver multipliers to your historical projects.
3. **Update estimates iteratively**: start with Early Design, then refine with Post-Architecture once more details emerge.
4. **Cross-check**: use other estimation techniques (expert judgment, analogy, function point methods) to validate or sanity-check the COCOMO result.
5. **Document assumptions**: always record how you rated each cost driver and why, so you or others can review/adjust.
6. **Consider risk & uncertainty explicitly**: build buffers, sensitivity analysis, examine which cost drivers the estimate is most sensitive to.
7. **Use tool support**: many tools / spreadsheets exist to help apply COCOMO II formulas, reducing manual error.

---

## 6. Sources

1. Boehm, Barry W., et al. Software cost estimation with COCOMO II. Prentice Hall Press, 2009.

2. COCOMO II Model Definition Manual, Version 2.1 (2000).  
    USC Center for Software Engineering.  
    Official technical manual describing all formulas, cost drivers, and scale factors.  
    [https://www.rose-hulman.edu/class/cs/csse372/201310/Homework/CII_modelman2000.pdf](https://www.rose-hulman.edu/class/cs/csse372/201310/Homework/CII_modelman2000.pdf?utm_source=chatgpt.com)

3. Boehm, Barry, et al. "Cost models for future software life cycle processes: COCOMO 2.0." Annals of software engineering 1.1 (1995): 57-94.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue or fix with a pull request.
