---
parent: Frameworks
title: Synchronize and Stabilize
nav_order: 2
layout: default
---

# Synchronize and Stabilize

Microsoft's synchronize-and-stabilize approach lets many small feature teams work in parallel, then
holds them together with two disciplines: **synchronize** by integrating continuously — historically
a daily build — and **stabilize** by stopping at milestones to fix defects until the product is
genuinely shippable {% cite cusumano1999internettime %}.

It was developed for Windows and Office in the 1990s, and it is the ancestor of a great deal of
modern practice.

![Feature teams work in parallel, synchronising through frequent builds and stabilising at milestone
boundaries](image-2.png)

## 1. The daily build is a coordination mechanism, not a build policy

The interesting claim is about **organisation**, not tooling. A large product cannot be built by one
team, and parallel teams diverge. Synchronize-and-stabilize's answer is to make divergence visible
every single day: if the build breaks or a feature is incompatible, that is known within hours rather
than at an integration phase months later.

Cusumano and Yoffie's summary of why it holds together is that *"projects remain under control
because teams frequently synchronize and periodically stabilize"* {% cite cusumano1999internettime %}.
Frequency substitutes for planning. Instead of specifying the interfaces precisely enough that
independent work will fit, you let it not fit and find out immediately.

The **milestone stabilisation** is the other half and the part usually forgotten. At each milestone
the product is driven to a working, testable state — feature work stops, defects are fixed, and the
result is something people can actually run. That is what makes alpha and beta releases possible and
what stops defect debt accumulating to the end.

## 2. Fixed dates, flexible features

The model treats the **schedule as fixed and the feature set as negotiable**. Features are
prioritised, teams have real autonomy over how they implement theirs, and anything not ready at a
milestone is cut rather than allowed to delay the milestone.

**Example — shipping a large desktop application.** A release is divided into three milestones of a
few months each, with the most valuable features scheduled into the first. Every night the whole
product is built and a test suite runs; a developer who breaks it fixes it that morning. At the end
of milestone one the teams stop adding features and spend three weeks driving the defect count down
until the build is usable internally — that build becomes the internal alpha. Features that slipped
are re-prioritised into milestone two or dropped. The date does not move.

If that sounds familiar, it should. Continuous integration, timeboxing, and scope-flexed releases are
all here in 1990s form.

## 3. What it costs

It demands infrastructure and slack that a small organisation does not have: build and test
automation maintained as a first-class asset, dedicated test capacity, and enough people that
parallel feature teams make sense at all. It also assumes a product where shipping a series of
preview versions is acceptable — commercial desktop software, not a regulated medical device.

And it tolerates a period where the product is knowingly unstable between stabilisation points,
which is only survivable because the milestones force it back to a working state on a schedule.

## How solid is this?

- **Cusumano and Yoffie is observational management research** — a study of how Microsoft and
  Netscape actually worked, published in IEEE Computer. It describes a practice and argues it is
  effective; it is not a controlled comparison against another way of organising, and the authors had
  privileged access to the companies concerned.
- **It is a snapshot of the 1990s.** Both the technology and the release model have moved on, and the
  practices this page describes now live inside continuous integration and continuous delivery, where
  they are far better tooled.
- **This page is here partly for a structural reason**, and it is worth being open about it: Microsoft
  Sync-and-Stabilize is one of the five methods in Rockwood's selection tally
  {% cite rockwood_choose_2003 %}, so [choosing a framework](choose.md) depends on it being explained
  somewhere.
- **No source in this review measures its outcomes.** Treat it as an influential historical practice
  whose descendants are what you would actually adopt today.

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
