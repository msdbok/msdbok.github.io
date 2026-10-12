---
parent: Estimates
title: Function Point Analysis
nav_order: 5
layout: default
---

# Function Point Analysis

**Function Point Analysis (FPA)** measures the size of software by what it does for its user — the
data it keeps and the transactions that move data across its boundary — rather than by the lines of
code that implement it. Allan Albrecht of IBM made the method public in 1979 and published its
counting rules in a journal in 1983 {% cite albrecht1983fpa %}; the International Function Point
Users Group (IFPUG), founded in 1986, maintains them {% cite longstreet2004fundamentals %}.

Its appeal is timing: a count can be made from the requirements, in discussion with the user,
long before anyone knows how many lines the system will need {% cite albrecht1983fpa %}.

## 1. When to use it — and when not

FPA earns its cost where size must mean the same thing to several parties.

- **An early estimate, bid or contract for a business system** — Korea's government makes FPA the
  standard size measure for public software procurement {% cite kang_estimating_2018 %}.
- **Productivity comparisons** across languages or teams, and **scope creep**: count at
  requirements and at delivery — *"If the project has grown, there has been scope creep"*
  {% cite longstreet2004fundamentals %}.

It fits badly where function is not where the work is.

- **Algorithm-heavy or scientific software**, whose internal processing the weights barely credit
  {% cite symons1988fpa %}, and **embedded, real-time systems** {% cite park1992size %}.
- **Defect fixing and performance tuning** {% cite longstreet2002fpa %}, R&D projects, and
  projects under USD 50,000 {% cite kang_estimating_2018 %}.
- **Tracking progress inside a build** — a count cannot say what share is coded or tested
  {% cite park1992size %}.

## 2. How it works

The analyst draws a boundary from the user's side and classifies everything inside it as one of
five components {% cite longstreet2002fpa %}:

| Component | What it is | Low / Avg / High |
|---|---|---|
| **ILF** internal logical file | data the application maintains | 7 / 10 / 15 |
| **EIF** external interface file | data it only reads; another application maintains it | 5 / 7 / 10 |
| **EI** external input | data crossing inward that changes a stored file | 3 / 4 / 6 |
| **EO** external output | data crossing outward that includes derived values | 4 / 5 / 7 |
| **EQ** external inquiry | stored data retrieved without calculation | 3 / 4 / 6 |

Each component is rated Low, Average or High from a few counting units, and the weights add up to
the **unadjusted function points (UFP)**. Fourteen general system characteristics, each rated 0–5,
give a value adjustment factor `VAF = 0.65 + 0.01 × total`, between 0.65 and 1.35; the adjusted
size is `FP = UFP × VAF` {% cite albrecht1983fpa %}. Two rules cause most counting errors: **only an
input maintains a file**, and **count types, never occurrences** {% cite longstreet2002fpa %}. The
matrices, the 14 characteristics and a full count are on [FPA explained](fpa_explained).

## 3. Example: a library system

For example, a small library application, counted at Average except the supplier file:

| Function | Type | Rating | FP |
|---|---|---|---|
| Add new book | EI | Avg | 4 |
| Register member | EI | Avg | 4 |
| Borrow book | EI | Avg | 4 |
| Return book | EI | Avg | 4 |
| Search books | EQ | Avg | 4 |
| Books file | ILF | Avg | 10 |
| Members file | ILF | Avg | 10 |
| Supplier catalogue, read only | EIF | Low | 5 |

UFP = **45**. With the characteristics totalling 30, `VAF = 0.65 + 0.30 = 0.95` and FP = 42.75 ≈
**43**. At an assumed historical rate of 12 FP per person-month, that is about **3.6 person-months**.

Borrowing and returning each change the stored loan details, so each is an **EI** — even if Return
computes a late fee, because *"A calculation (or derived data) does not make the transaction an
external output"* {% cite longstreet2002fpa %}. Counting them as one High output (7 FP) is the
classic misreading.

## 4. From size to effort, and its limits

Size becomes effort through a productivity rate, ideally your own. Albrecht fitted
`W = 54 × F − 13,390` work-hours to 24 IBM projects, and still advised: *"It is recommended that
such "formula" estimates be used only to validate and provide perspective on primary estimates"*
{% cite albrecht1983fpa %}.

The weights also compress size: a component with over 100 data elements gets at most twice the
points of one with a single element {% cite symons1988fpa %}.

## How solid is this?

- **Where it comes from.** Albrecht and Gaffney's 24 projects are one company's business portfolio.
  Function points correlate with work-hours at **r = 0.935** across them, yet the relative error on
  a single project has a standard deviation of about **85%**; the weights were *"determined by
  debate and trial"* {% cite albrecht1983fpa %}.
- **How reliable a count is.** Two trained counters of the same system differ by a median of about
  **12%**, and counting costs roughly one work-hour per 100 FP. The sites volunteered, so 12% is
  closer to a floor than a typical value {% cite kemerer1993fp %}.
- **What is contested.** *"function points are not a technology-independent measure of system size,
  which was one of Albrecht's stated claims"* {% cite symons1988fpa %}: independent of language,
  not of the weights' calibration.
- **What we hold.** Longstreet's article reports no data; the rules here come from his IFPUG
  4.1-era training booklet {% cite longstreet2002fpa %}. Later IFPUG releases are not held.

---

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
