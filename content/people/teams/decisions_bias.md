---
parent: Decisions
title: Cognitive Bias
nav_order: 6
layout: default
---

# Cognitive Bias

A cognitive bias is a systematic, predictable deviation of judgment from a norm — anchoring on the first number you hear, or seeking the evidence that confirms what you already believe. The useful question for a manager is which of them are actually established in software engineering.

## 1. What has actually been studied

The systematic mapping study by Mohanani and colleagues is the best answer available {% cite mohanani2018biases %}. Across **65 primary studies** published 1990–2016 it identifies **37 distinct cognitive biases**, and they are very unevenly studied.

| | |
|---|---|
| Anchoring and adjustment | **26** studies |
| Confirmation bias | **23** studies |
| Overconfidence | **16** studies |
| Biases resting on one or two studies each | **21 of the 37** |
| The **`Social`** category — biases where social relationships undermine judgment | **2** studies, covering **one** bias |
| Biases with any proposed debiasing technique | **6 of 37**, and **none empirically evaluated** |

**Example.** Anchoring is both the best studied and the easiest to catch in the act. A product owner opens sprint planning with "this should be about three days", and the estimates that follow cluster around three days whether or not the work resembles anything the team has built before. The remedy is procedural: collect estimates before any number is said out loud.

## 2. Two consequences

**The group pathologies are the thinnest-evidenced part of decision making.** `Social` is the least-studied category of all. **Groupthink is not among the 37 biases mapped** — it appears in the paper only as the *target* of an unvalidated proposed remedy, designating a devil's advocate — and **the Abilene paradox does not appear at all**. See [Group decisions](decisions_group.html) for what that material does rest on.

**The best-evidenced biases are individual, and they land on estimation.** Anchoring, confirmation and overconfidence are failures of judgment about numbers and evidence, which is where [Scope](../../scope/) and [Planning](../../plan/) pick them up. A treatment that stops at group dynamics misses the part of the literature that has been measured.

## 3. The other side of the argument

Klein rejects the premise of the bias literature outright, and the disagreement is worth staging rather than hiding. Chapter 16 of *Sources of Power* argues that "those who favor analytical approaches to decision making believe poor decisions are caused by biases in the way we think. Naturalistic decision-making researchers disagree" {% cite klein1998sourcesofpower %}. The methodological charge is that the classic stimuli were **selected to produce the error**: of the twenty possible consonants, twelve are more common in first position, and the famous availability demonstration used the eight that are not.

The two classics also conflict directly. Groupthink measures decision quality against a procedural standard — canvass all alternatives, weigh all costs, search out new information — and **Klein disputes exactly that standard**, arguing experts do not compare options and the prescription is unworkable under time pressure. The field disagrees about what a good decision even *is*.

## 4. Judge the process, not the outcome

**A poor outcome is not the same as a poor decision, and a good one is not proof of a good decision.** A team can reason badly and get lucky, or reason well and be overtaken by something nobody could have known. The only thing you can inspect afterwards is *how* the decision was made — what was considered, what was assumed, what risk was accepted. That is why [PEAK](decisions_peak.html) insists on recording the assumed risk.

**Practically:** review a decision against what was known *then*, not what you know now. A release that shipped fine with no rollback plan was a bad decision that got lucky — and only the record will say so.

## How solid is this?

- **Three literatures reach §4's conclusion independently** — *"poor outcomes are different from poor decisions"* {% cite klein1998sourcesofpower %}, *"bad procedures need not always produce bad results"* {% cite thart1991groupthink %}, and *"demonstrating a bias in a lab is not the same as establishing a significant effect on real projects"* {% cite mohanani2018biases %}. That convergence is the strongest support anything here has.
- **The mapping study maps research, not projects.** 30 of its 65 studies are controlled experiments, and the authors are explicit that demonstrating a bias in a lab is not the same as establishing an effect on a real project.
- **It supplies no fix.** Six of thirty-seven biases have any proposed debiasing technique, none tested, and the authors warn debiasing "may have unintended consequences".
- **Its own coding is uncertain.** Inter-rater agreement on a bias's category was **55%**. Treat the counts as a map of where the evidence is, not a ranking of what will go wrong.
- **Klein's counter-argument is partisan.** He is defending his own research programme, and "do not occur in experienced decision makers" claims more than his evidence carries. It is here because the disagreement is real, not because he wins it.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and
**David Root** {% cite root2014lectures %} on software project management. The structure,
examples, and pedagogical approach reflect their teaching materials and frameworks.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
