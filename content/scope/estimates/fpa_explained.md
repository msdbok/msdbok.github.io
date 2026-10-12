---
parent: Estimates
title: FPA Explained
nav_order: 6
layout: default
page_type: deep-dive   # the three IFPUG matrices plus one complete, correct worked count; cutting either loses the page's purpose
---

# FPA Explained

A **function-point count** sizes an application in five steps: draw its boundary, classify what lies
inside as five kinds of component, rate each component from a few counting units, add up the
weights, and adjust for fourteen system characteristics. Why and when to use FPA is on
[Function Point Analysis](fpa).

## 1. Why count functions, not lines

Lines of code are unknown when the estimate is due and ill-defined afterwards: without a counting
rule, *"Our software activity produced 163,000 source code instructions on that job"* can be
misunderstood *"by a factor of three or more"* {% cite park1992size %}. Function points count what the user gets, so the same screens, reports and files score the same whether the
system is written in C++ or in Clarion {% cite longstreet2002fpa %}.

## 2. Step 1 — Draw the boundary

*"This boundary must be drawn according to the user’s point of view"*
{% cite longstreet2004fundamentals %} — the user being someone *"that would provide requirements or
does acceptance testing"*. A web client and its server sit inside one boundary; a new front end is
not a new application {% cite longstreet2002fpa %}. The boundary decides what a file is: a customer
file that application A maintains is internal to A and external to B, which only reads it.

## 3. Step 2 — Find the five components

Files are **data at rest**; transactions are **data in motion** {% cite longstreet2002fpa %}. A
transaction is an *elementary process*, *"similar to an acceptance test case"* — the smallest
activity meaningful to the user.

| Component | Rule |
|---|---|
| **ILF** internal logical file | a user-recognisable group of data, maintained inside the boundary |
| **EIF** external interface file | the same, but only referenced; another application maintains it |
| **EI** external input | data crossing inward that maintains a file; add, change and delete are three EIs |
| **EO** external output | data crossing outward with derived values; never maintains a file |
| **EQ** external inquiry | retrieval only — no calculated values, no update |

Two questions classify every transaction. *Does it change a stored file?* Then it is an **EI**,
whatever else it computes: *"The only component that maintains an internal logical file is an
external input."* If not, *does it derive data?* Then it is an **EO**; otherwise an **EQ**
{% cite longstreet2002fpa %}.

## 4. Step 3 — Count DETs, RETs and FTRs

*"A record element type is a user recognizable subgroup of data elements within an ILF or EIF. A
data element type is a unique user recognizable, nonrecursive, field"*
{% cite longstreet2004fundamentals %}. A **file type referenced (FTR)** is an ILF or EIF that a
transaction reads or maintains. Three rules follow.

- **RETs count subgroup types, not records.** A department holding 20 employees has **2** RETs —
  department and employee — not 21 {% cite gunti_function_nodate %}. A file with no subgroups is
  itself one RET {% cite kang_estimating_2018 %}.
- **DETs count each field once.** *"If a DET is recursive then only the first occurrence of the
  DET is considered not every occurrence"* {% cite longstreet2002fpa %}.
- **A transaction's DETs include its buttons and messages**, and an EO or EQ counts the unique
  fields of its input and output sides together {% cite longstreet2002fpa %}.

The rules are not pedantry. A customer file with 5 fields, holding three credit cards of 7 fields
each, counted per instance is 26 DETs and 4 RETs — Average, 10 FP. Counted by Longstreet’s rules it
is 12 DETs and 2 RETs — Low, 7 FP: a **43% overcount** on one file.

## 5. Step 4 — Rate and weigh

Each component is rated from its counting units {% cite longstreet2002fpa kang_estimating_2018 %}.
Early in a project, rate everything Average and refine later.

| ILF, EIF | 1–19 DET | 20–50 DET | 51+ DET |
|---|---|---|---|
| 1 RET | Low | Low | Average |
| 2–5 RET | Low | Average | High |
| 6+ RET | Average | High | High |

| EO, EQ | 1–5 DET | 6–19 DET | 20+ DET |
|---|---|---|---|
| 0–1 FTR | Low | Low | Average |
| 2–3 FTR | Low | Average | High |
| 4+ FTR | Average | High | High |

| EI | 1–4 DET | 5–15 DET | 16+ DET |
|---|---|---|---|
| 0–1 FTR | Low | Low | Average |
| 2 FTR | Low | Average | High |
| 3+ FTR | Average | High | High |

Weights, Low / Average / High: **ILF 7/10/15 · EIF 5/7/10 · EI 3/4/6 · EO 4/5/7 · EQ 3/4/6**. The
sum is the unadjusted count, UFP.

## 6. Step 5 — Adjust for the 14 characteristics

The fourteen general system characteristics are data communications, distributed data processing,
performance, heavily used configuration, transaction rate, on-line data entry, end-user efficiency,
on-line update, complex processing, reusability, installation ease, operational ease, multiple
sites and facilitate change. Each is rated 0 (no influence) to 5 (strong influence throughout); the
total gives `VAF = 0.65 + total / 100`, between 0.65 and 1.35, and `FP = UFP × VAF`
{% cite longstreet2002fpa %}.

## 7. A worked count: an online bookshop's customer accounts

**Example.** The customer-account module of a fictional online bookshop stores each customer's
details (name, surname, phone, gender, date of birth), their credit cards (number, type, issue date,
valid-thru date, valid flag, owner ID, name on card) and their addresses (street, town, country). It
checks each new card against a card-issuer table that the payment provider maintains. The example is
adapted from Miranda {% cite miranda_managing_2014 %}.

A card or an address means nothing without its customer, so the module has **one** customer ILF with
three subgroups — however many cards and addresses a customer holds.

| Component | Type | DET | RET / FTR | Rating | FP |
|---|---|---|---|---|---|
| Customer file | ILF | 5 + 7 + 3 = 15 | 3 RET | Low | 7 |
| Card-issuer table | EIF | 3 | 1 RET | Low | 5 |
| Register customer | EI | 5 + 3 fields, Save, message = 10 | 1 FTR | Low | 3 |
| Change customer details | EI | 10 | 1 FTR | Low | 3 |
| Delete customer | EI | name, surname, Delete, *"Are you sure?"* = 4 | 1 FTR | Low | 3 |
| Add credit card | EI | 5 card fields, Save, message = 7 | 2 FTR | Average | 4 |
| Remove credit card | EI | card number, Remove, message = 3 | 1 FTR | Low | 3 |
| View profile | EQ | 8 customer fields + 2 card fields = 10 | 1 FTR | Low | 3 |
| Card-expiry report | EO | 4 stored fields + days left = 5 | 1 FTR | Low | 4 |

UFP = 12 for files + 23 for transactions = **35**. On-line data entry and on-line update rate 5,
multiple sites 0, and the fourteen total 34, so `VAF = 0.99` and the module is about
**35 FP**. Counted per instance instead — a customer with three cards and two addresses — the
customer file becomes 6 RETs and 32 DETs, High, 15 FP, and the module grows to 43: a 23% overcount
from one file.

## 8. When it is worth the effort

Count when the size must be defended to someone else — a bid, a contract, a productivity
comparison; a trained counter needs about one work-hour per 100 FP {% cite kemerer1993fp %}. A team
planning its own sprints is better served by a relative unit such as story points
{% cite rubin_essential_2012 %}.

## How solid is this?

- **Where it comes from.** Longstreet sells FPA training; the rules here come from his IFPUG
  4.1-era booklet, which goes beyond IFPUG in places {% cite longstreet2002fpa %}. The core rules
  match Albrecht 1983, Gunti and Kang {% cite albrecht1983fpa %}.
- **Modelling is a judgement call.** Treating cards as a second ILF is defensible if a card means
  something without its owner. Such choices are part of the median **12%** between two trained
  counters {% cite kemerer1993fp %}.
- **What not to copy.** Gunti rates an EQ by the higher of its input and output sides — Albrecht's
  1983 rule, since superseded {% cite gunti_function_nodate %}.
- **The 43% and 23% overcounts** are computed from the rules, not measured.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
