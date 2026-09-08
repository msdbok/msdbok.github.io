---
parent: Lifecycles
title: Prototyping and RAD
nav_order: 5
layout: default
---

# Prototyping and RAD

A prototype is software built to answer a question rather than to be delivered. You build it when the
cheapest way to resolve an uncertainty — what the users actually want, whether an approach will
perform, whether an integration is feasible — is to make something and look at it.

The decision that governs everything else is what happens to it afterwards.

## 1. Throwaway or evolutionary — decide before you build

**Throwaway prototyping** builds the artefact to learn from, then discards it and builds the real
system with what was learned. The prototype is optimised for speed of construction: no error
handling, no scale, no security, whatever language is fastest to sketch in.

**Evolutionary prototyping** builds a first version intending to grow it into the product. It has to
be built to production standards from the start, because it will *be* the production system.

These are different projects, and the expensive failure is deciding late. A throwaway prototype that
someone decides to ship inherits every shortcut taken on the understanding that it would be thrown
away — and those shortcuts were the whole reason it was fast. Prototyping is a legitimate way of
retiring requirements risk, and it is also how systems acquire foundations nobody would have chosen.

Boehm's [spiral](spiral.md) treats prototyping as the standard instrument for resolving whichever
risk dominates a given cycle {% cite boehm_spiral_1988 %} — which is the disciplined version of the
same idea: prototype against a named uncertainty, and stop when it is resolved.

**Example — the look-and-feel question.** A team building a scheduling tool cannot get agreement on
the calendar interaction from a specification; three stakeholders read the same paragraph three
ways. A clickable mock with no backend at all settles it in two sessions, and is then deleted. The
requirement it produced — direct manipulation with undo, not a form-and-submit dialogue — is what
goes into the build. The prototype answered a question and had no further business existing.

## 2. Expectations are the real risk

A prototype that looks finished is assumed to be nearly finished. Showing a stakeholder a
convincing interface over no implementation reliably produces the question *so why can't we have it
next month?*, and the honest answer — that the visible 10% was the cheap part — is rarely believed.

Say what the prototype is for and what it omits, every time it is shown. Where the omission is
structural — no persistence, no permissions, no error paths — say that too.

## 3. RAD is prototyping on a timebox

**Rapid Application Development** takes evolutionary prototyping and adds a fixed, short calendar,
heavy user involvement, small teams and aggressive reuse of existing components. Delivery is
compressed into short cycles with users co-designing in workshops rather than reviewing documents.

It fits business applications with urgent time-to-value — internal tools, dashboards, workflow
systems assembled largely from existing parts. It fits poorly where the system is large, where the
components have to be built rather than assembled, or where safety or regulatory rigour cannot be
compressed. The timebox is the mechanism: scope flexes to protect the date, which is only acceptable
when partial scope is genuinely useful.

RAD is a 1990s formulation, and the parts of it that worked — short cycles, continuous user contact,
reuse — were absorbed into agile practice, where they now live. Treat it as an ancestor to recognise
rather than a method to select.

## How solid is this?

- **This page describes established practice rather than reporting evidence.** The throwaway /
  evolutionary distinction is standard in the textbook literature; no source in this review measures
  either against the other.
- **The spiral connection is Boehm's** {% cite boehm_spiral_1988 %} and is the best-grounded claim
  here: prototyping as a risk-resolution technique with a stopping condition, rather than as a phase.
- **RAD is not separately evidenced in this review.** It is covered here because it appears in the
  course's model list and in the comparison table, and because it is prototyping with a timebox
  rather than an independent lifecycle. There is no reviewed primary source behind it, so the page
  makes no claim about how well it performs.

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
