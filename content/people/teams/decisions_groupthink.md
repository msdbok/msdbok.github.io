---
parent: Decisions
title: Groupthink
nav_order: 5
layout: default
---

# Groupthink

Groupthink is conformity pressure inside a cohesive group that suppresses dissent, so alternatives go unvoiced and the group converges early on a poor option. It is the most famous idea in this topic and the most thinly supported.

## 1. Where it comes from

Irving Janis named it in 1972 from foreign-policy fiascos — the Bay of Pigs, Pearl Harbor, Korea, Vietnam, Watergate — against two successes he judged it avoided, the Marshall Plan and the Cuban missile crisis. It is not settled: ’t Hart's review essay found the replications "modest, their quality mixed and their findings only partially conclusive" {% cite thart1991groupthink %}.

## 2. What survived testing

Each component of Janis's model fared differently by 1991 {% cite thart1991groupthink %}.

| Component | Evidence as of 1991 |
|---|---|
| **Cohesiveness**, Janis's one group-level cause | **Repeatedly unsupported.** Flowers, Fodor & Smith and Leana all found leadership mattered and cohesiveness did not; Raven found the Nixon group conflict-laden — cohesion *absent* in one of Janis's own cases |
| **Directive leadership** | **Supported** across four independent studies |
| **Stress**, which Janis ranked *first* | **Largely untested**: experiments "rarely succeeded in creating the kind of decisional stress" the theory requires |
| **Stereotyped out-group images** | **Disconfirmed** by Tetlock — no more negative references to adversary states |
| **The founding cases** | Mixed: Barrett argued groupthink played **no role at all** in Vietnam |

## 3. Circularity, and a better mechanism

’t Hart charges **circularity**: Janis picked policy failures first, then looked for groupthink, so "groupthink is inferred from policy failure and failure is explained in terms of groupthink." His alternative is **anticipatory compliance** — low-status members conforming to what they take the leader to want. Power and hierarchy, not friendliness: a better fit to a software team than cohesion.

**Example.** At a release go/no-go meeting the principal engineer opens with "I think we ship." The two juniors holding the flaky-test data say nothing and the release goes out. Nobody pressured them and the team is not especially close-knit — they read the room and complied in advance. Cohesion explains none of it; the reporting line explains all of it.

## 4. The Abilene paradox

The **Abilene paradox** is a different failure: a group unanimously agrees on a course *no member privately favours*, each believing the others want it (Harvey, 1974). Groupthink is dissent suppressed by pressure; the Abilene paradox is dissent nobody realises exists. The remedy differs accordingly — pressure needs cover for the dissenter, false consensus needs only that someone ask.

## 5. Judge the process, not the outcome

’t Hart is blunt that a bad process can still end well: "bad procedures need not always produce bad results; decision-makers may get lucky." A shipped release is therefore no evidence that the meeting which approved it worked — the same convergence reached from three directions on [Cognitive bias](decisions_bias.html).

## 6. A warning about pages like this one

’t Hart's closing charge lands on handbooks, this one included:

> "the very popularity of groupthink may, in fact, act as an impediment to careful
> interdisciplinary integration. This emerges clearly from the uncritical adoption of sections on
> 'the dangers of groupthink' in many policy analysis and management handbooks."

Read the sections above as an account of a contested construct, not as a hazard list to check your team against.

## How solid is this?

- **Scope, stated in his words.** ’t Hart holds groupthink meaningful only for **high-level groups facing consequential, non-routine choices**: "it is not really interesting to perform groupthink analyses of regular problem-solving groups at some lower level of management or policy-making." Applying it to a sprint team is an extrapolation nobody has tested.
- **Vintage.** His record stops at **1991**, so do not call the evidence weak full stop; say that as of 1991 its own reviewer described the replications as modest, mixed and only partially conclusive.
- **Not among the measured biases.** Groupthink is not one of the 37 cognitive biases mapped in software engineering, and the Abilene paradox does not appear there at all {% cite mohanani2018biases %}.
- **Rebori's groupthink is not Janis's.** The gloss used in the [group-decision](decisions_group.html) leaflets — dissent withheld "because they believe no one will agree with them" — is closer to the Abilene paradox, dropping cohesion, stress and structural faults.
- **What we do not hold.** Janis's own books: *Victims of Groupthink* (1972) and *Groupthink* (1982), the second carrying the systematic statement, so 1972 dates the naming not the model. The eight symptoms come via ’t Hart, **no remedy list is given** because he reproduces none, and Harvey is not held either — the Abilene paradox is the least-sourced claim here.

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
