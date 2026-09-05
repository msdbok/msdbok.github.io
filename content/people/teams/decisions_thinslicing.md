---
parent: Decisions
title: Thin Slicing
nav_order: 3
layout: default
---

# Thin Slicing

Thin slicing "refers to the ability of our unconscious to find patterns in situations and behavior based on very narrow slices of experience" {% cite gladwell2005blink %} — ordinary cognition, not a rare talent. Malcolm Gladwell's *Blink* is where most managers meet the idea, and it argues both halves of it.

## 1. The cases for it

Gladwell's illustrations all share one shape: a very short exposure carries most of the signal a long one does.

- **Gottman's "Love Lab"** filmed over 3,000 couples in disagreement, coding 20 emotion categories a second, and Gladwell reports prediction of divorce 15 years out at 95% accuracy from an hour of tape.
- **Wartime Morse interceptors** recognised individual German senders by rhythm and spacing — the operator's "fist" — without decoding a word of the traffic.
- **Levinson** found that never-sued physicians spent **18.3 minutes** per patient against 15 and made more orienting comments, with **no difference in the amount or quality of medical information given**. Manner, not content, predicted the lawsuit.
- **Ambady** rated unfamiliar professors from 10-, 5- and even 2-second silent clips about as a full semester's evaluations did, then cut the physicians' tapes to **two 10-second clips per surgeon**, filtered to tone alone — a dominant tone marked the sued group.

{: .warning }
**Do not put the 95% on a slide.** It is Gladwell's report of someone else's result, with no confidence interval and no out-of-sample test: the *direction* is defensible, the percentage is not.

**Example.** A reviewer opens a pull request, sees 41 files changed with a build-config edit buried among them, and flags it as risky before reading a line of logic. The shape of the diff is the thin slice, and it is usually right — which is exactly why the same reviewer will wave through a small, tidy diff that quietly changes a retry limit.

## 2. The half that fails

Roughly half of *Blink* is snap judgment going wrong, and this is the half a manager needs.

- The **Warren Harding error** — a face that looks the part, read as competence.
- **Amadou Diallo** — extreme arousal collapsing rapid cognition into "temporary mind-blindness" at roughly **115–145 bpm**.
- **Priming** — behaviour moved by cues the actor never noticed.
- **New Coke** — the sip test is the wrong instrument: sweetness wins a sip and loses a can.
- **Blind auditions** — a screen removes a bias listeners sincerely denied holding.
- **Explaining ruins it** — asked to give reasons, non-experts' jam rankings fell from **r = .55** to **r = .11** against expert judgment.

## 3. When to trust a slice, and when not

Trust the slice when the judge has genuine experience of *this* pattern, when the cue is behaviour rather than appearance, and when arousal is low. Distrust it when the judgment concerns a person's competence from their appearance, when the instrument does not resemble the real use (the sip versus the can), and when the situation is physiologically hot. Structure — a screen, a rubric, a checklist — is what removes the cues that mislead, and it works even on judges who honestly report no bias.

The disciplined version of the same phenomenon, with its boundary conditions stated, is Klein's [Intuition and expertise](decisions_intuition.html).

## How solid is this?

- **This page is second-hand.** *Blink* is trade non-fiction; Gladwell runs no studies. The underlying work — Gottman, Ambady and Rosenthal, Levinson, Nigel West — reaches this page through his retelling rather than from the original papers, which his Notes list. Check anything you intend to quote against those originals. "Absolute certainty" about the Morse operators is a historian's phrase, not a measurement.
- **Levinson and Ambady are two different studies.** The 18.3-versus-15-minute consultation finding is not itself a thin-slicing result; thin slicing enters only when Ambady re-slices those same tapes down to forty seconds.

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
