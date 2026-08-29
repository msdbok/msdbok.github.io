---
parent: Decisions
title: Intuition and Expertise
nav_order: 2
layout: default
---

# Intuition and Expertise

Intuition is "the way we translate our experience into action" {% cite klein2003intuition %} — a skill that can be built, applied and safeguarded, not a gift. Gary Klein's **Recognition-Primed Decision (RPD)** model describes how experts decide under pressure.

## 1. What RPD claims

Klein built RPD from studies of fireground commanders, later military and police {% cite klein1998sourcesofpower %}. The claim is not that experts choose well among options — they usually generate none. A recognised pattern produces one candidate action, run forward mentally; if the simulation exposes a problem, it is modified or the next candidate considered. Klein ties this to Simon's **satisficing**: options are evaluated one at a time and the first workable one taken — hence the expert's good-enough *first considered action*.

The chain: cues → **patterns** → **action scripts** → **mental simulation**, all driven by **mental models** {% cite klein2003intuition %}.

## 2. Three variations, and the safeguard

RPD is not one chain but three.

1. **Simple match** — the situation is recognised and the action taken.
2. **Diagnose the situation** — cues do not match cleanly, so the decider gathers more, feature-matches, or builds a story.
3. **Evaluate a course of action** — the recognised action is simulated, then modified or rejected.

**Expectancies** are a first-class element alongside cues, goals and actions, making the model self-correcting: a violated expectancy is how an expert discovers the interpretation was wrong. Without them RPD is merely fast.

**Example.** A tech lead sees the nightly build fail on three unrelated tests. The pattern *shared fixture state* fires, with an expectancy: those three should pass in isolation. They do not, so she drops it within a minute for a clock-dependent assertion — variation 2.

## 3. How often experts work this way

Across **more than six hundred decision points** {% cite klein1998sourcesofpower %}, RPD accounted for **46% to 96%** of decisions by domain and expertise: urban fireground commanders **80%** of 156 points, design engineers **60%**, AEGIS commanders **95%**, tank-platoon *trainees* **42%**.

## 4. When to recognise, when to compare

Recognition is fast and allows action under uncertainty; comparison buys justification. Klein's boundary conditions {% cite klein1998sourcesofpower %}:

| Recognition works when… | Compare options when… |
|---|---|
| Time pressure is high | The choice must be justified to others |
| The decider is experienced **in this domain** | Competing interests must be reconciled |
| Conditions are dynamic | The decider is optimizing, not satisficing |
| Goals are ill defined | The problem is computationally complex |

{: .note }
**Klein is no escape from analysis paralysis.** "**Neither analysis nor intuition alone is sufficient for effective decision making**" {% cite klein2003intuition %} — experts *start* from recognition; analysis is not dispensable.

## 5. Where intuition fails

*The Power of Intuition* names the failure conditions {% cite klein2003intuition %}; four describe software estimation: **unstable or random domains** where patterns cannot form (roulette, the stock market); **no fast, accurate feedback** — hiring judged on time-to-fill, not hire quality; **a distorted experience base**, the wrong experience repeated; **fixation, or "bending the map"**, expertise closing off the anomaly that should stop you; **arithmetic** — "you're sunk if you don't whip out the calculator"; and decisions with **conflicting interests** or needing an **audit trail**.

Organisations add barriers: rigid policies, distributed teams, turnover and constant change thin the experience base, while procedure, metrics-driven culture and IT constraints remove room to act.

## 6. Time pressure hits novices, not experts

Chess at **6 seconds** a move against roughly **2¼ minutes** under regulation {% cite klein1998sourcesofpower %}:

| | Blunder rate, blitz | Blunder rate, regulation |
|---|---|---|
| **Masters** | 7% | 8% |
| **Class B players** | **25%** | 11% |

An interaction, not a main effect: time pressure barely touches masters and roughly *doubles* the error rate of weaker players. The lesson is not "people decide fine under pressure" but **expertise buys immunity to it**: squeezing the clock on an inexperienced team is a different act from squeezing an experienced one. The primary study is Calderwood, Klein and Crandall {% cite calderwood1988chess %}, not the trade books.

The popular version, and the half that misfires, is [Thin slicing](decisions_thinslicing.html).

## How solid is this?

- **A strategy count, not a quality count.** The 46–96% range shows experts do not compare options, not that they are right. The studies are Klein's own, coded by his team, and the independent replications he cites are the ones that agreed.
- **Descriptive, not prescriptive.** RPD does not license "train people to satisfice", and Klein says it does not transfer without consistent, fast feedback — he names stock selection, public policy and clinical psychology. Software estimation has weak feedback loops, so the transfer is a question.
- **Which Klein book.** *Sources of Power* (1998/2017) for anything with a number in it, *The Power of Intuition* (2003) for anything a manager should do — chapter 4 of the 1998 book is itself titled "The Power of Intuition", which is where the confusion starts.

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
