---
parent: Decisions
title: Deciding with AI
nav_order: 7
layout: default
---

# Deciding with AI

Reliance is the *behaviour* of taking or refusing a model's recommendation, as distinct from trust, which is an attitude. The failures elsewhere in this topic run human-to-human; the same question — *when should I take the advice?* — now runs human-to-model, and it has been measured.

## 1. Two studies, pointing opposite ways

| Study | What was measured | Result |
|---|---|---|
| Puppart & Aru {% cite puppart2025overreliance %} | Adoption of **incorrect** ChatGPT recommendations. **n = 36 twelfth-grade Estonian school students**, math puzzles, unreviewed preprint | **Over-reliance: 52.1%** (SD 28.90) — bad advice taken just over half the time. A short AI-literacy intervention **did not reduce it**, and significantly *increased* rejection of correct advice (t(34) = 2.35, p = .025, d = 0.78) |
| Schemmer et al. {% cite schemmer2022reliance %} | Whether people **rightly change their mind** when the AI is correct (RAIR) and **rightly hold their ground** when it is wrong (RSR). 200 participants, deceptive-review classification, CHI '22 workshop paper | **Under-reliance: RAIR 0.30 — below chance.** Correct advice was ignored. RSR was 0.72. Adding explanations raised RAIR to 0.39 (p = .05) without inducing over-reliance |

## 2. Miscalibration runs in both directions

The pair of results is the finding. One study found bad advice accepted; the other found good advice refused. "People trust AI too much" gets this backwards and licenses exactly the wrong intervention — and the intervention the second-guessing instinct reaches for first, a short explanatory lesson about the tool, is the one that was tested and failed.

**Example.** A developer asks a model to review a patch. It flags a genuinely missing null check, and objects to a lock ordering that is deliberate and correct. Over-reliance accepts both changes; under-reliance rejects both and loses the real bug. Neither behaviour is a trust problem, and neither is fixed by telling the team the model is "usually reliable".

## 3. The management question

So the question is not *"does the team trust the AI?"* Trust is an attitude; reliance is a behaviour, and the behaviour is what costs money. The useful question is whether people can **tell good advice from bad and act on the difference** — two separate abilities, which can fail independently and in opposite directions, and which a rise in overall team performance can hide entirely {% cite schemmer2022reliance %}. Measuring the two separately, as RAIR and RSR do, is the practical contribution here: a single accuracy number for the human-plus-model pair tells you nothing about which of the two abilities is failing.

## How solid is this?

- **Carry the populations with the numbers.** The 52.1% figure comes from **36 school students solving math puzzles in a preprint that has not been peer-reviewed** — not from software engineers, not from code, not from a team under a deadline. It licenses a *direction*: a short literacy intervention is a weak instrument against miscalibration. It is not an effect size for professional developers.
- **The second study is a workshop paper.** Schemmer and colleagues report a single illustrative experiment, and the RAIR/RSR metrics are defined only for classification tasks — which is not what most software work looks like.
- **Two studies are not a literature.** They are the two this handbook holds. They agree that reliance is miscalibrated and disagree about the direction, which is enough to warn against a confident remedy and not enough to recommend one.

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
