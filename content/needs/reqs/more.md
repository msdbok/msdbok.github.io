---
parent: Requirements
title: Validation, traceability and change
nav_order: 7
layout: default
---

# Validation, Traceability and Change

Once requirements exist, three activities keep them useful: checking them, linking them to what they
produced, and deciding what to do when they change. The third is where the arguments happen, and the
one most often got backwards.

## 1. Checking a requirement set

Validation asks whether these are the right requirements; verification asks whether the system meets
them — the distinction is on [requirements engineering](eng). What a review looks for is narrower
than "read it carefully": **ambiguity**; **inconsistency and omission**,
including anything still marked *to be determined*, since a specification containing one is not
complete {% cite iso2018req %}; **a named source** who confirms the written form is what they meant;
and **a way to test it**. If no process can determine whether the software meets a requirement, the
rule is to **remove or revise it**.

## 2. Traceability

Traceability tracks a requirement in two directions: **backward** to the stakeholder, document or
regulation that motivated it, and **forward** to the design, code and tests that satisfy it. For example, *"R-005: user data shall be encrypted at rest"* traces back to a data-protection obligation,
and forward to an encryption component and an AES-256 storage test. The backward link lets you
re-decide the requirement when the obligation changes; the forward link tells you what breaks.

## 3. Change is what successful products do

Commercial word processors and spreadsheets grew from **under 300 function points to over 5,000 in
ten years** {% cite jones1996creep %} — not a failure of requirements discipline, but what a product
that survives looks like.

And most change is not repair. Corrective maintenance is only **10–15%** of maintenance work;
functional enhancements are **over 60%** of changes, and **40% of those enhancements come from
learning** {% cite kelly2004change %} — figures that are Edberg and Olfman's, relayed by Kelly.
Specifying a system also changes the system people want: interviewing people about their work
*"will cause people to reflect on what they are doing… and whether things can be done better."*

## 4. Measure change before arguing about it

**Volatility** is *"the ratio of requirements change… to the total number of requirements for a
given period of time"* — a number any project can produce from its change log
{% cite nurmuliani2004volatility %}.

Recording *what* changed is easy. Recording **why** and **where it came from** turns a change log
into an analysis: changes originating in design reviews mean the reviews are working; changes
originating in support calls mean the elicitation did not. In the studied release,
volatility peaked at **16.85%** as requirements analysis completed and the reviews ran — which is
discovery, not instability. **A project that schedules no review has the same changes, found later
and priced higher.**

## 5. What a late change actually costs

Three independent methods on real aerospace programmes agree that the cost to fix an error grows
**exponentially** with the phase in which it is found {% cite stecklein2004costs %}. One aircraft
programme's own accounting, over 231 true errors, gives it in money: an error caught in definition
cost **$22,632**; the same class of error found in operations cost **$3,558,215**.

{: .warning }
**There is no single multiplier.** The familiar figure carries its own hedge — a problem found after
delivery is *"**often** 100 times more expensive"* — and the same authors put small non-critical
systems *"more like 5:1 than 100:1"* {% cite boehm2001top10 %}. Measured escalation to operations
runs 29× on real spacecraft and 157–186× on real aircraft.

The mechanism is the useful part: projects spend about **40–50% of their effort** on *avoidable
rework*, one named source of which is *hastily specified requirements*.

## 6. The decision rule the cost curve licenses

Not refusal. As Kelly puts it: *"changes that come along later are more disruptive but this doesn't
imply they are valueless, only that they must be worth more if they are to be worthwhile
implementing."* The rule is a **rising value threshold**, not a closing door — read as a licence to
say no, it makes you *"the people who always say 'No'"*.

Two mechanisms implement it: a written **impact statement** listing alternatives with their costs,
so **the decision rests with the requestor, not the manager** {% cite wysocki2003needs %}; and a
**deferral** device, where ideas go into a bank and are decided at the next checkpoint rather than
inside a cycle.

## How solid is this?

- **Where it comes from.** One triangulated aerospace cost study, one single-release volatility
  case, one synthesis column, one opinion essay whose percentages belong to a study it cites.
- **What is contested.** The 100× figure: published studies disagree by a factor of nearly seven at
  the test phase alone, and Boehm's own 1981 operations figure is a range of 40–1000×.
- **What we do not hold.** The volatility percentages are one waterfall release at one company and
  are not a benchmark.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
