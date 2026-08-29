---
parent: Decisions
title: Cognitive Bias
nav_order: 5
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

**The best-evidenced biases are individual, and they land on estimation.** Anchoring, confirmation and overconfidence are all failures of judgment about numbers and evidence, which is where the [Scope](../../scope/) and [Planning](../../plan/) blocks of this handbook pick them up. A treatment of decision making that stops at group dynamics misses the part of the literature that has actually been measured.

## 3. The other side of the argument

Klein rejects the premise of the bias literature outright, and the disagreement is worth staging rather than hiding. Chapter 16 of *Sources of Power* argues that "those who favor analytical approaches to decision making believe poor decisions are caused by biases in the way we think. Naturalistic decision-making researchers disagree" {% cite klein1998sourcesofpower %}. His methodological charge, via Lopes, is that the classic stimuli were **selected to produce the error**: of the twenty possible consonants, twelve are more common in first position, and the famous availability demonstration used the eight that are not. He adds that the heuristics and biases "do not occur in experienced decision makers working in natural settings".

Students should also see a direct conflict between the two classics. Janis's standard for a good decision is the Janis & Mann procedural model — canvass all alternatives, weigh all costs, search out new information. **Klein disputes exactly that model**, arguing that experts do not compare options and that the prescription is unworkable under time pressure. The field's two best-known authorities disagree about what a good decision even *is*.

## 4. Where three sources converge

Klein and the mapping study come at the problem from opposite ends and reach the same conclusion; ’t Hart arrives there from a third direction.

| Source | The same claim |
|---|---|
| Klein {% cite klein1998sourcesofpower %} | "Poor outcomes are different from poor decisions." |
| ’t Hart {% cite thart1991groupthink %} | "Bad procedures need not always produce bad results; decision-makers may get lucky." |
| Mohanani et al. {% cite mohanani2018biases %} | "Demonstrating a bias in a lab is not the same as establishing a significant effect on real projects." |

**Judge the process, not the outcome — and do not assume the process research transfers.** That is the transferable lesson of this whole topic, and it is a project-management lesson rather than a psychology one. It is also why every page here carries its evidence separately from its teaching.

## How solid is this?

- **The mapping study maps research, not projects.** 30 of its 65 studies are controlled experiments, and the authors are explicit that demonstrating a bias in a lab is not the same as establishing an effect on a real project.
- **It supplies no fix.** Six of thirty-seven biases have any proposed debiasing technique, none tested, and the authors warn debiasing "may have unintended consequences".
- **Its own coding is uncertain.** Inter-rater agreement on a bias's category was **55%**. Treat the counts as a map of where the evidence is, not a ranking of what will go wrong.
- **Klein's counter-argument is partisan.** He is defending his own research programme against the heuristics-and-biases tradition, and "do not occur in experienced decision makers" claims more than his evidence carries. It is here because the disagreement is real, not because he wins it.

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
