---
page_type: deep-dive   # evidence-dense: the Steiner/Ringelmann table plus the three-rater gradient
parent: Teams
title: Team Performance
nav_order: 1
layout: default
---

# Team Performance

A team's **actual productivity is its potential productivity minus the losses caused by working
together** {% cite steiner_models_1966 %} (p. 274). Potential depends only on the task and on what
the members bring to it; everything a manager can influence sits in that second term.

## 1. Steiner's equation

Steiner splits the losses in two (p. 275). **Motivation losses** are people trying less hard in a
group — the subject of [Social Loafing](loafing.html). **Coordination losses** are the effort spent
keeping the work in step. Adding a person raises the potential *and* creates new losses at the same
moment, so whether a bigger team wins is a question about the task, not a property of teams.

His illustration is Ringelmann's rope-pulling experiment (p. 276). Individuals pulling alone
averaged 63 kg, so groups of 2, 3 and 8 ought to manage 126, 189 and 504 kg:

| Pullers | Potential | Actual | Shortfall |
|---|---|---|---|
| 2 | 126 kg | 118 kg | 8 kg |
| 3 | 189 kg | 160 kg | 29 kg |
| 8 | 504 kg | 248 kg | 256 kg |

At eight pullers the group delivers under half of what its members can do individually, and the
shortfalls track the pairwise links between them — 1, 3 and 28.

Steiner's task typology says which loss to expect: an **additive** task sums efforts
(rope-pulling), a **disjunctive** task succeeds if the best member succeeds, and a **conjunctive**
task is limited by its weakest member. Software work is mostly conjunctive and divisible, which is
the direction Brooks's Law comes from.

## 2. Do teams outperform individuals?

This handbook used to answer **yes**, under the heading *Synergy*. No source in this bibliography
supports it, and the two large software studies used below cannot settle it, because **neither
compares a team with an individual**: Hoegl and Gemuenden interviewed 575 people in 145 German
teams {% cite hoegl_teamwork_2001 %} and Lindsjørn and colleagues surveyed 477 members of 71 agile
teams {% cite lindsjorn2016teamwork %}, both correlating teamwork quality with performance *within*
teams.

## 3. What does predict performance

Three variables have been measured in software teams — **psychological safety**, team **autonomy**
and **stable membership** — and all three are available to whoever runs the team, while none of
them is composition. Safety is much the strongest of the three and now has its own page:
[Psychological Safety](safety.html), which also carries the other two.

## 4. Whose performance?

Teamwork quality — communication, coordination, balance of contributions, mutual support, effort,
cohesion — is measurable and associated with performance. The size of that association depends
entirely on **who is asked**. For example, 71 agile teams in 26 Norwegian companies gave three
different answers about themselves {% cite lindsjorn2016teamwork %}:

| Rater | Teamwork quality → performance | Variance explained |
|---|---|---|
| Team members | β = 0.68 | R² = 0.466 |
| Team leaders | β = 0.32 | R² = 0.104 |
| Product owners | **β = 0.06** | **p = .593 — no effect** |

On project quality, owners and members agree at r = 0.03. The earlier study this replicates used a
**line manager** as third rater and found the link significant for all three groups — 41%, 11% and
7% of the performance variance {% cite hoegl_teamwork_2001 %}. So before improving a team's
performance, settle **whose** definition of performance is being optimised; that question returns
in [Tracking](../../track/).

## 5. Does diversity improve decisions?

Often asserted, rarely sourced. In the largest software study — 1,118 members of 161 teams — **only
age diversity** predicted effectiveness (β = .213, p = .041); gender, cultural background and role
diversity did not, on effectiveness or on relational conflict {% cite verwijs2024diversity %}.
Take this as a reason to stop *asserting* the diversity–performance link, not as proof that
composition is irrelevant — and note what did outrank every composition variable in the same
study: [psychological safety](safety.html). The other half of that study, on conflict, is on
[Conflict](conflict.html).

## How solid is this?

- **Where the rope numbers come from.** Steiner never saw Ringelmann's data — he takes it "as
  reported by Dashiell (1935)", the 1913 experiment was never published, and only a few groups of
  each size were observed. Thompson reports the same experiment as force *per person*: 63 / 53 /
  31 kg at 1, 3 and 8 pullers {% cite thompson2015makingtheteam %} (p. 47). Say which chain you use.
- **The largest coefficient is the weakest.** Members rated both predictor and outcome, so
  common-source bias is a leading explanation for β = 0.68 and for the 41%; Lindsjørn found "no
  empirical distinction between the two concepts". Hoegl never investigated the *antecedents* of
  teamwork quality, so neither study says how to produce it, and both are cross-sectional.
- **Rater substitution is our reading, not theirs.** Lindsjørn offers a vantage-point explanation —
  owners see functionality and lead time, members see internal code quality — and declines to
  choose between it and rater bias.
- **Self-report throughout.** Verwijs recruited through an Agile self-diagnosis tool and measured
  effectiveness as perception. The same caveat applies to every study behind
  [Psychological Safety](safety.html), where it is set out in full.

---

### Acknowledgments

This page adapts material from lectures by **Eduardo Miranda** and **David Root**
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
