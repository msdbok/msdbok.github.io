---
parent: Estimates
title: COCOMO
nav_order: 7
layout: default
---

# COCOMO

**COCOMO** (Constructive Cost Model) is a parametric model that turns an estimate of software size
into effort and schedule through a calibrated equation, adjusted by ratings of the product, platform,
people and project. Barry Boehm published the first version, COCOMO 81, in 1981
{% cite boehm1981economics %}; COCOMO II, defined in its 2000 Model Definition Manual
{% cite usc2000cocomo %}, is the version in use.

## 1. From COCOMO 81 to COCOMO II

COCOMO 81 came in a Basic form — size and a development mode — and an Intermediate form that added
15 cost drivers {% cite jorgensen_software_2009 %}. In COCOMO II, five **scale factors** set the
exponent on size, and two models share one equation: **Early Design**, before an architecture
exists, and **Post-Architecture**, once it does {% cite usc2000cocomo %}.

## 2. The equations

Effort in person-months, the exponent, and the schedule in months are {% cite usc2000cocomo %}:

```
PM   = A × Size^E × Π EM_i
E    = B + 0.01 × Σ SF_j          (five scale factors)
TDEV = C × PM_NS^F × SCED% / 100,  F = D + 0.2 × (E − B)
```

`Size` is thousands of source lines (KSLOC), or unadjusted function points converted to lines.
`PM_NS` is the effort computed without the schedule driver. COCOMO II.2000 sets **A = 2.94,
B = 0.91, C = 3.67, D = 0.28**, calibrated on **161 projects**; a person-month is 152 hours.

The exponent is usually above 1 — diseconomies of scale, from the *"growth of interpersonal
communications overhead and growth of large-system integration overhead"*. And *"the most
significant input to the COCOMO II model is Size"* {% cite usc2000cocomo %}.

## 3. Early Design or Post-Architecture

The two models differ only in the effort multipliers: *"There are seven multiplicative cost drivers
for the Early Design model and seventeen multiplicative cost drivers for the Post-Architecture
model"* {% cite usc2000cocomo %}. Both counts include **SCED**, the required development schedule;
the nominal-schedule form leaves it out and has 6 and 16. Every rating value is on
[COCOMO II drivers](cocomo_ii_drivers).

## 4. Example: an average 100 KSLOC system

**Example.** The manual's own case is a 100 KSLOC system of average difficulty: E = 1.15 and every
multiplier at 1.0. It needs `2.94 × 100^1.15` = **586.6 person-months**, over **29.7 months**,
with about **20 people** on average {% cite usc2000cocomo %}.

Ask for it in 75% of that schedule and effort is multiplied by 1.43: about **839 person-months** in
about 22 months — nearly **38 people**, almost twice the team.
Stretching it saves nothing: *"Stretch-outs do not add or decrease effort"* {% cite usc2000cocomo %}.

## 5. Where the effort goes

COCOMO also splits effort by phase, and the split moves with size. From the small project to the
large one, Product Design takes 17%, Detailed Design 27% falling to 23%, Code and Unit Test 37%
falling to 29%, and Integration and Test **19% rising to 31%**; Plans and Requirements (7%) and
Transition (12%) are added on top {% cite usc2000cocomo %}. The manual calls these figures
provisional — *"a stimulus to thought, and not as a substitute for thought."*

## 6. Calibrate before you trust it

Out of the box, the constants encode other organisations' history. *"It is recommended that
at least A and C be calibrated to the local development environment to increase the model's
accuracy"*, from at least five completed projects {% cite usc2000cocomo %}. Pressman agrees:
*"Estimation models must be calibrated for local needs!"*
{% cite pressman2010estimation %}

## 7. When to use it — and when not

Run COCOMO when you can defend a size estimate, the model is calibrated on projects like yours,
and the estimate must survive negotiation or be rerun for many scenarios:
*"A major advantage of a parametric model is that it doesn't modify its estimates when customers,
managers, or marketers apply pressure"* {% cite jorgensen_software_2009 %}. It is the wrong tool
with no size basis and no local data, outside the size range it was calibrated on, or as a
single-pass estimate for incremental development {% cite pfleeger2005rand %}.

Jørgensen's reply is the main limitation: *"All meaningful estimation models require judgment to
produce the input to the models"* {% cite jorgensen_software_2009 %}. A model moves judgment into the
size and ratings, where it is written down. So *"Use multiple models to 'triangulate' a
reasonable estimate. In addition, verify reasonableness with expert judgment"*
{% cite pfleeger2005rand %}.

## How solid is this?

- **Where it comes from.** The manual is a specification, not a study: 161 affiliate projects, a
  fictitious calibration example, and a phase table carried forward from COCOMO 81
  {% cite usc2000cocomo %}.
- **What the drivers are worth.** Within a factor of 1.3 of actuals on 63 projects, Basic COCOMO 81
  landed 29% of the time and Intermediate COCOMO, with its cost drivers, 78% — Boehm's own figures,
  quoted in a debate he was arguing {% cite jorgensen_software_2009 %}. Used off the shelf, COCOMO
  produced average errors of over 600% in Kemerer's 1987 test {% cite shepperd1997analogy %}.
- **What is contested.** The effort–size relation varied across the 12 data sets Dolado tested, so a
  calibrated model is a good cross-check, not an objective answer {% cite jorgensen_software_2009 %}.
- **What we do not hold.** The book *Software Cost Estimation with COCOMO II* (Boehm et al., 2000)
  and COCOMO II's first journal publication. The reuse equations are not reproduced here.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
