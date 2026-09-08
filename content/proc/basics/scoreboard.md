---
parent: Basics
title: Scoreboard
nav_order: 6
layout: default
---

# Scoreboard

A scoreboard collects the team's own judgement — on a short, recurring, usually anonymous
questionnaire — and tracks it as a **trend** rather than a number. It is what you use when the thing
that matters most is real, consequential and not countable: morale, trust, whether estimates are
believed, whether a role is working.

The method as taught here is Pedro Mota's, written up from a student team at Carnegie Mellon
{% cite mota2009scoreboard %}.

## 1. The trend carries the signal, not the score

A single week's average is close to meaningless. Two identical scores a fortnight apart mean
something quite different from a score that has fallen three weeks running. So questions are asked
repeatedly and in the same words, and it is the direction that triggers a conversation.

Two kinds of question run side by side {% cite mota2009scoreboard %}. **General** questions cover
every role and stay in the survey permanently, so their trend becomes that role's baseline.
**Specific** questions track a current risk and are retired once the risk closes. Mota describes the
division by what each is for: the general set acted *"like a smoke detector just to signal something
wrong, while the specific approach focused on the concrete problems"*.

Questions that had been consistently good for several weeks were removed, to keep the survey short
enough that people kept answering it honestly.

<img src="/images/scoreboard-cycle.svg" alt="The scoreboard cycle in four steps: Think — define goals, write general questions per role and specific ones per risk, fix a 5-point scale; Act — send the same short survey anonymously; Reflect — aggregate the trend and spread, pick the worst and falling items, meet and assign actions; Maintain — add questions for new risks, retire stable ones, watch the response rate. The cycle then repeats." style="max-width:100%; margin:1.5em 0;" />

The short gap between answering and discussing is deliberate: Mota's team collected on Thursday and
held the reflection meeting on Friday. Data nobody acts on within the week teaches the team that
answering is pointless.

## 2. Cover every role, including the ones that look minor

**Example — the role that was left out.** Mota's team, the Mappers project, ran roughly 35 questions
across roles and general team issues. The **Training Manager** was deliberately omitted from the
scoreboard as *"a minor role not relevant to measure"*. That omission itself became a problem: it
*"was a reason for some debate and concern inside the team"* {% cite mota2009scoreboard %}. The
lesson he draws is a coverage rule — evaluate every role, because *"even minor or less relevant
roles/activities can be the source of major problems"*.

What you decline to measure is a message too. A role left off the board has been told, in public,
where it ranks.

## 3. Anonymity is a trade, not a free good

The Mappers scoreboard kept answers anonymous, which buys candour. The cost is that responses can
only be reported in aggregate, and Mota records the consequence plainly: *"averages can (and did)
hide dispersed values, preventing problems from being detected"* {% cite mota2009scoreboard %}.

A team split evenly between *very good* and *very bad* produces the same mean as a team that is
uniformly indifferent, and the second is a far less urgent problem than the first. If you keep
anonymity, watch the spread and the comment field, not the mean alone.

## How solid is this?

- **This is grey literature.** Mota's paper is a CMU Master of Software Engineering
  reflection paper describing the author's own team — a careful method walkthrough, not evidence
  that the method works. There is no comparison group and no outcome measure.
- **The ratings are ordinal.** A 4 is not twice a 2, so averaging them is not strictly meaningful.
  Mota raises the averaging problem in terms of hidden dispersion; the measurement-scale objection is
  ours, and it points the same way — read the distribution.
- **A scoreboard measures people's judgement of a process, which makes it exactly the kind of data
  that degrades when used to appraise individuals.** Mota's role-level framing is what keeps it
  pointed at roles rather than persons; see [process metrics](metrics.md) for why that matters.
- **The course's slides have carried two sourcing errors** here — a "Fiber Team" and a date of 2014.
  Neither appears anywhere in Mota's paper; the team is Mappers and the work is 2009 or later.

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
