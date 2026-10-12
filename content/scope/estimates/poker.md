---
parent: Estimates
title: Planning Poker
nav_order: 3
layout: default
page_type: method
---

# Planning Poker

**Planning Poker** is a group estimation game: each estimator picks a card privately, all cards are
turned over together, and the holders of the highest and lowest cards explain before the team
estimates again {% cite grenning2002poker rubin_essential_2012 %}. Its inventor's purpose:
*"Precision of individual estimates is not the goal. Determining the project scope is."*

## 1. Grenning's game and Cohn's deck

James Grenning invented it for two problems: estimates took too long, and the whole team was not
involved {% cite grenning2002poker %}. The customer reads a story; each programmer writes a card
without discussing it; all are turned over at once. If they agree, the number is recorded. If not,
the programmers at the extremes start the discussion, and with no consensus, *"Defer the story, split
it, or take the low estimate."* His deck was **1, 2, 3, 5, 7, 10 and ∞**, not Fibonacci; the
infinity card sends a story longer than two weeks back to be split.

Most teams now use Cohn's *"modified Fibonacci sequence: 1, 2, 3, 5, 8, 13, 20, 40, and 100"*, and the
rules forbid averaging: *"In Planning Poker we don't take averages or use any number not on the
scale/cards."* Consensus usually comes in two or three rounds {% cite rubin_essential_2012 %}.

Poker belongs to the Delphi family. Classic Delphi is anonymous. Boehm's **Wideband Delphi**
{% cite boehm1981economics %} is not: *"the experts meet for group discussions both prior to, and
during the estimation iterations"* {% cite molokken2004group %}. Poker gives up anonymity altogether
for a light, interactive process {% cite molokken2008poker %}.

## 2. When to use it, and when not

Use it for release planning of a long backlog, by the team that will build it, on familiar kinds of
work. Do not rely on it for stories in unfamiliar territory,
where it did worse than plain discussion {% cite haugen2006poker %}; for a homogeneous junior team,
whose estimates it made more optimistic {% cite mahnic2012poker %}; or for architecture and
infrastructure items unlike the rest of the backlog, which [paired comparison](pair) can size against
a reference.

## 3. Example

For example, Grenning's own worked hand: six cards read **1, 3, 2, 3, 5, 3**. Only the 1 and the 5
speak. One recalls that changing the communications protocol last time *"cost us four days alone!"*;
the other thinks *"all we have to do is add another message class"*. The table settles on 3. Most
stories took *"a minute or so"*, against *"10, 20, or 30 minutes"* before {% cite grenning2002poker %}.

## 4. What it fixes, and what it does not

Turning cards over together removes the first speaker's [anchor](expert). Making both extremes explain
*"introduces compensating anchors"* {% cite haugen2006poker %}. Two weaknesses remain:

- **The first round fences the answer.** The lowest and highest first-round cards bound the consensus:
  *"We found no story having the final planning poker estimate outside these boundaries."*
  {% cite mahnic2012poker %} If discussion reveals new work, vote again from scratch.
- **Matching cards hide disagreement.** The agreement rule ends the discussion, yet identical numbers
  can rest on different assumptions. On unfamiliar stories a team *"might feel a false sense of
  security"* {% cite haugen2006poker %}, and initial agreement did not predict accuracy
  {% cite molokken2008poker %}.

## 5. Story points: the advantage and the trade-off

The advantage is Rubin's observation that *"people are much better at relative size estimation than
absolute size estimation"* {% cite rubin_essential_2012 %}. The trade-off: a point means something only inside one team, against one reference, and
becomes a date only through velocity — 200 points at 17–20 per sprint is 10–12 sprints. Rewarded,
velocity inflates. And relative sizing needs enough comparisons: sizing each story against only two
others gave a project total of 99.7 points where a full comparison gave 44.6 {% cite miranda2009sizing %}.

## 6. Eduardo's Variation

Eduardo Miranda's variation adds a baseline and a look at agreement {% cite miranda_managing_2014 %}:

1. With story points, first agree a medium-complexity story as the baseline and give it a 3 or a 5.
2. Discuss differences and also coincidences, because people may pick the same number for different
   reasons.
3. Re-estimate one more time, and record each estimator's final card.
4. After all stories, assign the mean and probe the stories with unusual disagreement: *"Beware of the
   blind application of procedures such as averaging."*

Rules 1 and 4 echo his paired-comparison reasoning: a mid-range reference, and reviewing inconsistent
judgments {% cite miranda_improving_2001 %}.

## How solid is this?

- **Three studies, each one team or one class.** Haugen: median error 0.25 against 0.33 for
  unstructured discussion, but mean error 0.48 against 0.35 {% cite haugen2006poker %}.
  Moløkken-Østvold and colleagues: slightly less optimistic than the average of private cards, and no
  more accurate than the team's usual method, though the team believed it was
  {% cite molokken2008poker %}. Mahnič and Hovelja: worse for students, slightly better for experts
  {% cite mahnic2012poker %}. Haugen co-authored the second study.
- **Grenning and Rubin report practice, not data.**
- **Eduardo's Variation is untested** and appears in no paper; its source is Miranda's lecture
  material.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
