---
parent: Release planning
title: Contracts and incentives
nav_order: 3
layout: default
---

# Contracts and incentives

An **incentive contract** pays a base price for the release the plan guarantees and rising premiums
for the releases it does not, so that buyer and supplier share the risk of a partial delivery
{% cite miranda_time_2011 miranda2022moscow %}.

## 1. Who carries the risk

A [Buffered MoSCoW](moscow) plan is honest: it guarantees only the Musts. The risk of delivering
less than everything does not go away, so the only choice is who carries it. Under a fixed price the
supplier carries it and charges for it; under time-and-materials the buyer does. Miranda's contract
splits it, so that incentives *"prevent the developer from charging a premium price to protect
itself from not delivering all features"* while the buyer is assured of its best effort
{% cite miranda2022moscow %}. The contract
must therefore treat *"an agreed partial delivery"* as *"an acceptable, although not preferred,
outcome"* {% cite miranda_time_2011 %}.

Promising everything only hides the risk: when every requirement is a Must, *"typically time (the
end date) will slip"* {% cite dsdm2014moscow %}.

## 2. Pricing a release by its odds

**Example.** A publishing house buys Quill, a fictional word processor, as a 4,000-hour time box at $100 an hour:
a cost of $400K. The figures are Miranda's lecture example {% cite miranda_managing_2014 %}. The Must
release is 2,000 hours and certain; the Should release, 1,000 hours, has about even odds; the Could
release, 1,000 hours, about one in four: the method's double-and-quadruple rule of thumb.

A traditional fixed price of $520K is a 30% **markup** on cost, not a 30% margin. The incentive
version pays on delivery:

| The project delivers | The client pays | Markup on cost | Chance of this outcome |
|---|---|---|---|
| Must only | $400K | 0% | 50% |
| Must + Should | $500K | 25% | 25% |
| Must + Should + Could | $550K | 37.5% | 25% |

At these odds the **expected price is about $462.5K**, an expected markup of about 16%, against
$520K fixed. The gap is the price of the delivery risk. So the supplier sets the base and premiums
on the expected price, not the best case: it raises them, or knowingly accepts less money for a
lower-risk deal. Framing the same payments as $550K less deductions changes nothing.

## 3. Team rewards

Miranda applies the same logic inside the team: *"No reward will be associated with delivering the
'must have' release since the team members are simply doing their jobs"* {% cite miranda_time_2011 %}.
Rewards attach to the Should and Could releases and are sized by expected value. A large reward with
a small chance backfires, because *"the team members might perceive this reward as a lottery they
are unlikely to win"*; a $5,000 reward on a release with about even odds is worth $2,375
{% cite miranda_planning_2002 %}. The lecture adds: tie bonuses to release completion, not
overtime, and use non-monetary rewards such as training and time off
{% cite miranda_managing_2014 %}. Motivation itself is on [Motivation](../../people/teams/motivation).

## 4. Why the buffer needs an incentive

Two behaviours spend buffers, and both are defined on [Critical chain](../chain). Work expands *"so
as to fill the time available for its completion"* {% cite parkinson1955law %}, and it starts when
the deadline comes into view. Given the same one-hour task, students finished at 4.3 days with a
one-week deadline and 9.1 days with a two-week one {% cite buehler1994fallacy %}. And nobody hands
time back when an early finish earns no reward and only brings more work {% cite leach1999ccpm %}.

Linking these to the contract is this page's synthesis, not Miranda's. The time a Must does not use
belongs to the next feature the customer wanted, and a reward for the Should and Could releases gives
the team a reason to hand it on.

## 5. When to use it, and when not

Use it when the buyer can accept a partial delivery and the plan states its odds. If the buyer
needs everything, there is nothing to attach a premium to. The pitfall is the odds: the expected
price is only as good as the likelihoods behind it.

## How solid is this?

- **Where it comes from.** Miranda's contract and reward rules are argument, with no data. The
  pricing example is lecture material; the markup and expected price are recomputed from its
  inputs.
- **What is contested.** Parkinson's line is the opening of a 1955 satire, and the student syndrome
  is a term from Goldratt's novel *Critical Chain*. Buehler's participants were psychology
  undergraduates. Raz and colleagues note that the padding and Parkinson assumptions behind buffer
  methods lack *"any supporting scientific evidence"* {% cite raz2003ccpm %}.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda {% cite miranda_managing_2014 %}
on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
