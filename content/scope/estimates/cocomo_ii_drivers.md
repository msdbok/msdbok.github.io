---
parent: Estimates
title: COCOMO II Drivers
nav_order: 8
layout: default
---

# COCOMO II Drivers

**COCOMO II drivers** are the ratings that adjust the model's estimate: five **scale factors**, which
set the exponent on size and so matter more the larger the system, and seven or seventeen **effort
multipliers**, which scale the result up or down. This page gives their values; the equations are
on [COCOMO](cocomo).

## 1. Scale factors

Each factor is rated from Very Low to Extra High, the five values are summed, and the exponent is
`E = 0.91 + 0.01 × ΣSF` {% cite usc2000cocomo %}:

| Scale factor | Very Low | Low | Nominal | High | Very High | Extra High |
|---|---|---|---|---|---|---|
| **PREC** precedentedness | 6.20 | 4.96 | 3.72 | 2.48 | 1.24 | 0.00 |
| **FLEX** development flexibility | 5.07 | 4.05 | 3.04 | 2.03 | 1.01 | 0.00 |
| **RESL** architecture / risk resolution | 7.07 | 5.65 | 4.24 | 2.83 | 1.41 | 0.00 |
| **TEAM** team cohesion | 5.48 | 4.38 | 3.29 | 2.19 | 1.10 | 0.00 |
| **PMAT** process maturity | 7.80 | 6.24 | 4.68 | 3.12 | 1.56 | 0.00 |

PMAT follows the SW-CMM: Very Low and Low split Level 1, Nominal is Level 2, and so on up to
Level 5.

The table divides into what a manager inherits and what a manager chooses. PREC and FLEX are
*"largely intrinsic to a project and uncontrollable"*, while *"The next three scale factors identify
management controllables by which projects can reduce diseconomies of scale by reducing sources of
project turbulence, entropy, and rework"* {% cite usc2000cocomo %}. One level on one factor moves
effort by about **6%**. Across the whole range the effect is large: at 100 KSLOC, every factor at
Extra High gives **194** person-months and every factor at Very Low gives **832** — a factor of
about four from the exponent alone.

## 2. Effort multipliers

Post-Architecture uses 17 multipliers in four groups, which can be rated per module, except SCED
{% cite usc2000cocomo %}:

| Group | Multipliers |
|---|---|
| Product | RELY required reliability · DATA database size · CPLX product complexity · RUSE developed for reusability · DOCU documentation match to life-cycle needs |
| Platform | TIME execution time constraint · STOR main storage constraint · PVOL platform volatility |
| Personnel | ACAP analyst capability · PCAP programmer capability · PCON personnel continuity · APEX applications experience · PLEX platform experience · LTEX language and tool experience |
| Project | TOOL use of software tools · SITE multisite development · SCED required development schedule |

Early Design, used before the architecture exists, merges them into seven: **PERS** (ACAP, PCAP,
PCON), **RCPX** (RELY, DATA, CPLX, DOCU), **RUSE**, **PDIF** (TIME, STOR, PVOL), **PREX** (APEX,
PLEX, LTEX), **FCIL** (TOOL, SITE) and **SCED**.

SCED is the one a sponsor changes most often. Schedules of 75%, 85%, 100%, 130% and 160% of nominal
multiply effort by **1.43, 1.14, 1.00, 1.00 and 1.00**: compression costs effort, and *"Stretch-outs
do not add or decrease effort"* {% cite usc2000cocomo %}.

## 3. Example: rating a 50 KSLOC booking platform

**Example.** A team is to build a fictional clinic-booking platform of about 50 KSLOC. It resembles
earlier products (PREC Nominal, 3.72), the client allows some freedom (FLEX High, 2.03), architecture
risks are partly resolved (RESL Nominal, 4.24), the team works well together (TEAM High, 2.19), and
the organisation is at CMM Level 2 (PMAT Nominal, 4.68).

ΣSF = 16.86, so E = 1.0786. With every multiplier at Nominal, effort is `2.94 × 50^1.0786` ≈
**200 person-months**, and the schedule ≈ **19.3 months** with about 10 people. Asking for the
platform in 75% of that time costs 1.43 × 200 ≈ **286 person-months** in about 14.5 months.

Read TEAM and PMAT one column to the right — 1.10 and 3.12 — and ΣSF drops to 14.21, E to 1.0521,
and effort to about **180** person-months: **11% less** from two misread cells — the 6%-per-level
rule at work.

## 4. When to rate which, and the main pitfall

Use the seven Early Design drivers while the architecture is still open, and the seventeen once it
exists {% cite usc2000cocomo %}. The pitfall is treating ratings as facts. Each is a judgment, and a
project can tune them until the expected number appears — using the model *"as a disguise for expert
estimation"* {% cite jorgensen_software_2009 %}. Record why each rating was chosen.

## How solid is this?

- **Where it comes from.** Every value here is from the COCOMO II.2000 manual — the scale-factor
  table, the SCED multipliers and the Early Design groupings — calibrated on 161 affiliate projects
  {% cite usc2000cocomo %}.
- **How to read the range.** 194 versus 832 person-months is the manual's extreme case, every
  factor at one end; the 6% per level is the usable figure.
- **What we do not hold.** The rating values of the sixteen multipliers other than SCED are in the
  manual's §3.2 and are not reproduced here. The worked example is computed from the manual's
  constants, not taken from a project.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
