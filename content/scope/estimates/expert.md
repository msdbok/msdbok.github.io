---
parent: Estimates
title: Expert Judgment
nav_order: 2
layout: default
page_type: method
---

# Expert Judgment

**Expert judgment** is estimation in which a person, not a formula, produces the number: *"Expert
estimation can be described as estimation conducted by persons recognised as experts where important
parts of the estimation process is based on non-explicit, non-recoverable reasoning processes, i.e.
‘intuition’."* {% cite jorgensen2004topdown %}

It is how most software is estimated. At JPL, 83% of estimators named informal analogy as their
primary technique and 7% named models, and a review found no survey in which most estimates came from
models {% cite jorgensen2004expert %}.

## 1. Top-down or bottom-up

An expert works in one of two ways {% cite jorgensen2004expert jorgensen2004topdown %}:

| | Top-down | Bottom-up |
|---|---|---|
| **How** | the project as a whole, compared with completed projects | activities from a WBS, each estimated, then summed |
| **Strength** | fast, cheap, encourages the use of history | builds an understanding of how the work will be done |
| **Weakness** | needs a very similar past project | forgets activities and underestimates surprises |

Seven professional teams estimated two real projects each way. Bottom-up erred by 23% and 31%,
top-down by 45% and 55%. Only two of the seven top-down teams recalled a similar project whose actual
effort they knew, and theirs were among the most accurate, at 12%. The rule that follows:
*"software companies should apply the bottom-up strategy unless the estimators have experience from,
or access to, very similar projects."* {% cite jorgensen2004topdown %}

## 2. When to use it, and when not

Use it when the expert knows something no model has an input for — *"a serious conflict between the
project leader Peter and his best programmer Paul"* {% cite jorgensen_software_2009 %} — when no
model has been calibrated to your organisation, and when the specification is too vague to count. Do
not rely on it alone when the estimate must hold under pressure to lower it, or after someone has
already said a number.

## 3. Four biases, and a countermeasure for each

The countermeasures that survive the evidence change what the estimator sees, not who the estimator
is:

| Bias | What it looks like | Countermeasure |
|---|---|---|
| **Availability** | only the activities that come to mind are counted | an activity checklist and searchable project history {% cite jorgensen2004expert %} |
| **Anchoring** | a number heard first — the sponsor's guess, the budget | someone else removes numbers from the brief before it is estimated {% cite halkjelsvik2012origami %} |
| **Representativeness** | "it is just like the last one" | documented data from many past tasks, not the single closest {% cite jorgensen2004expert %} |
| **Confirmation** | the estimator argues for their own plan | an independent second estimate, and listing why your own could be wrong {% cite jorgensen2004expert %} |

All four feed **overconfidence**. Jørgensen's teams believed their ranges had an 86% chance of holding
the actual; 43% did {% cite jorgensen2004topdown %}. Set ranges from your own historical error, or
mechanically at 50% to 200% of the most likely value {% cite jorgensen2004expert %}.

For example, Aranda and Easterbrook gave 23 estimators the same brief for a statistics system,
changing one sentence from a client manager: *"I admit I have no experience with software projects,
but I guess this will take about 2 months to finish."* Mean estimates were 6.8 months with that
sentence, 8.3 with no guess, and 17.4 when the manager guessed 20 months
{% cite aranda2005anchoring %}. Forewarning barely helps: *"Ideally, estimators should be shielded
from anchors."*

## 4. Expert or model?

Of 15 studies comparing the two, five favoured experts, five found no difference and five favoured
models: *"there is no substantial evidence in favour of either model or expert-based estimates"*
{% cite jorgensen2004expert %}. The pattern matters more than the tally. Experts beat
**uncalibrated** models in every such experiment, and **calibrated** models matched or beat experts
in every one. A later count found judgment more accurate in 10 of 16 studies
{% cite jorgensen_software_2009 %}.

Jørgensen and Boehm's debate gives each side one sentence. Boehm: *"A major advantage of a parametric
model is that it doesn't modify its estimates when customers, managers, or marketers apply
pressure."* Jørgensen: *"All meaningful estimation models require judgment to produce the input to
the models."* Both conclude for combining the two, as [estimation approaches](approaches) describes.

## How solid is this?

- **The top-down and bottom-up figures** come from seven teams and two small projects that both
  strategies over-estimated; the process observations transfer better than the percentages.
- **The 15 studies** are convenience samples, many with students. The 5/5/5 and the 10 of 16 count
  different things and must not be merged.
- **The anchoring experiment** had 23 participants, mostly graduate students; the low anchor's effect
  was not significant, only the high one's.
- **The countermeasures rest mostly on psychology.** Training, feedback and asking an outside observer
  did not improve accuracy in the studies reviewed {% cite halkjelsvik2012origami %}.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
