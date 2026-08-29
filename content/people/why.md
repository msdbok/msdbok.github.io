---
page_type: deep-dive   # evidence-dense: both CHAOS tables plus the Eveleens critique, moved verbatim
parent: People
title: Why Projects Fail
nav_order: 1
layout: default
---

# Why Projects Fail

_Adapted from lecture materials by David Root {% cite root2014lectures %}._

A software project counts as failed when it is cancelled or delivered outside its own forecast of
time, cost and result — which, on the most-quoted industry figures, is what happens to most of them
{% cite standish2015chaos %}. Read those figures closely: not because they are dependable, but
because seeing why they are not is the first lesson of this course.

{: .warning }
**Neither number below measures what it appears to measure.** Both definitions score a project
against its own *forecast*, so an organization can raise its score by inflating estimates
{% cite eveleens2010chaos %} — detail in [How solid is this?](#how-solid-is-this) below.

## The same projects, two answers

Standish reports outcomes under **two definitions**, and the choice moves the headline by seven
percentage points across the same 25,000 projects:

| Definition | What counts as success | FY2015 result |
|---|---|---|
| **Traditional** | OnTime, OnBudget, **OnTarget** — the required features | 36% successful · 45% challenged · 19% failed |
| **Modern** | OnTime, OnBudget, **with a satisfactory result** | **29%** successful · **52%** challenged · 19% failed |

The report states that "for the rest of this report CHAOS Resolution will refer to the Modern
Resolution definition." Quoting a size breakdown beside a "36% succeed" headline therefore mixes the
two — a mistake this handbook previously made.

## Outcomes by project size

In CHAOS 2015, under the Modern definition, larger projects do fare worse: 6% of Grand projects are
recorded successful against 61% of Small ones.

| Project Size | Successful | Challenged | Failed | Total |
|--------------|-----------|-----------|---------|-------|
| **Grand** | 6% | 51% | 43% | 100% |
| **Large** | 11% | 59% | 30% | 100% |
| **Medium** | 12% | 62% | 26% | 100% |
| **Moderate** | 24% | 64% | 12% | 100% |
| **Small** | 61% | 32% | 7% | 100% |

None of this shows that software projects go well. It shows what to ask of any project metric you
are handed: **who chose the definition, and what happens to them if the number moves.** That
question returns in [Tracking](../track/).

Despite decades of experience — Carnegie Mellon's computer science department was founded in 1965,
NASA has been building software since the 1950s — software remains harder to predict than most
engineering disciplines. Two reasons recur.

## Software is different

![Dilbert complexity](image-1.png)

Software systems reach orders of magnitude more complexity than physical ones, and none of it is
visible: product and process are both abstract, and many stakeholders fully understand neither.
Because software is perceived as "soft" — easy to change — changes are requested casually and then
have consequences nobody anticipated. Every project differs enough that few solutions transfer.
*For example,* code written in BASIC and in C# compiles to the same machine code when both target
the same architecture, yet the two development processes and their efficiency differ enormously.

## The human variable

![Dilbert motivation](image-2.png)

The number-one problem managers report is how to motivate people, and people resist
standardization: experience varies, the ability to learn and execute a task differs, and
interpersonal relationships change what a team can do. Behaviour is hard to predict and harder to
control, and matching a person to a task — the *first fit* problem — is rarely right first time.

## Constraining the human variable

![Dilbert process](image-3.png)

Management's usual answer is process: define acceptable norms of behaviour, direct actions,
standardize responses — "see A, do B". Process improvement then refines how the work is done, and
process checking confirms the process is followed and effective. Over-standardization has its own
pitfall, the assembly-line problem: creativity and adaptability disappear. Communication in software
teams has historically been poor, and no amount of process fixes that on its own.

## Why study management of software development?

To understand why projects fail and how to improve the odds; to manage complexity and human factors
rather than hope they behave; to apply engineering discipline while recognizing what makes software
unlike other engineering; and to build skills in process design, team leadership and communication.

## How solid is this?

- **What is contested.** Eveleens and Verhoef {% cite eveleens2010chaos %} analysed 5,457 forecasts
  across 1,211 real projects and showed what follows from scoring a project against its own
  estimate: the portfolio with the **worst** forecasting — half its projects out by 233% or more —
  scored **67% "successful"**, because its managers systematically overstated budgets. Two datasets
  with *identical* forecast quality scored 5.8% and 94.2%, differing only in the direction of the
  bias.
- **Three checks before using any figure like this.** Who chose the definition? Standish's own
  disclaimer, quoted by Eveleens and Verhoef, says its reports "should be considered Standish
  opinion and the reader bears all risk in the use of this opinion". Does the publisher sell the
  remedy? The top-weighted success factor is "Optimization", the name of Standish's own paid
  service, and the text beside the size table offers to "break up large software projects into
  multiple small projects". Does the report agree with itself? This one gives "25,000-plus projects"
  on page 1 and 50,000 on page 13.
- **What we do not hold.** "Software is different", the human variable and the process response to
  it come from the Miranda and Root lectures {% cite root2014lectures %}: teaching frameworks with
  practice behind them, not measured findings. No study here quantifies any of them.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
