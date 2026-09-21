---
parent: Lifecycles
title: Incremental
nav_order: 3
layout: default
---

# Incremental

An incremental lifecycle delivers the system as a series of **increments**, each one a usable slice
of the finished product. The requirements are understood well enough at the start to say what the
slices are; what is staged is the *delivery*, not the *understanding*.

Pressman is explicit about the output: *"The incremental process model focuses on the delivery of an
operational product with each increment"*, and the increments *"provide progressively more
functionality for the customer as each increment is delivered"* {% cite pressman2010incremental %}.

## 1. What makes it incremental rather than iterative

The two models are constantly confused, and the difference is **not** how often you repeat. Both
repeat. They repeat for different reasons, and the axis is **how well the requirements are known when
you start** {% cite pressman2010incremental %}:

| | Incremental | [Iterative](iterative.md) (evolutionary) |
|---|---|---|
| Requirements at the start | reasonably well defined | expected to change while you build |
| Each pass produces | an **operational product** — stripped down but usable | an increasingly **more complete version** |
| Process flow | linear sequences applied in a staggered fashion | iteration around the whole product |
| Driver | scope too large for one pass; staffing; a deadline | uncertainty |

<img src="/images/inc-vs-iter.svg" alt="The requirements-certainty axis: incremental ships operational slices when requirements are known; iterative produces increasingly complete versions when they are not" style="max-width:100%; margin:1.5em 0;" />

{: .fs-2 }
The axis is requirements certainty, after Pressman {% cite pressman2010incremental %}.

Because each increment is a small linear pass, Pressman also calls the incremental model *"the
iterative waterfall"* — an accurate and slightly mischievous name.

## 2. Why you would choose it

You choose incremental when you know roughly what to build but cannot build it all at once. The
usual reasons are practical rather than epistemic: staff are not all available at the start, the
deadline requires *something* in the users' hands early, or the scope is simply too large for a
single pass to be manageable.

That gives it two real advantages. Value arrives early, and integration happens repeatedly in small
amounts rather than once, catastrophically, at the end. The first increment is normally the **core
product** — the functionality without which nothing else is useful.

**Example — an enterprise system delivered by module.** A customer-management replacement is staged
as core customer accounts first, then billing, then reporting. Each increment goes to production and
is used; the account records exist before there is anything to bill against, and billing exists
before there is anything to report on. If the reporting increment slips a quarter, the organisation
is still running on the first two — which would not be true had the whole system been scheduled to
land at once.

The cost is that the increments have to be planned to fit together. Slicing badly produces an
increment nobody can use without the next one, which is a release schedule pretending to be a
lifecycle.

## 3. Where it struggles

The model assumes the requirements you slice up are broadly right. When they are not, incremental
delivery gets you to the wrong system faster and in stages — each increment is built, delivered and
then reworked when the misunderstanding surfaces. That is the condition
[iterative](iterative.md) development exists for.

It also needs architectural room. An increment that requires the foundations to be rebuilt is a sign
the earlier increments committed to a structure that the later ones cannot live with.

## How solid is this?

- **The distinction taught here is Pressman's** {% cite pressman2010incremental %}, and it is a
  textbook definition rather than an empirical finding. It is used because it is clean and
  citable — not because a study established it.
- **The vocabulary is genuinely contested.** Ruparelia treats iterative and incremental as
  effectively interchangeable {% cite ruparelia_software_2010 %}, and other sources split them by
  rework or by risk instead of by requirements certainty. Know which definition you are being
  examined on.
- **Section numbers are edition-specific.** The quotations above are from the 7th edition, ch. 2
  §2.3.2; the 8th edition renumbers them.
- **No source here compares incremental delivery against a single-pass alternative** on measured
  outcomes.

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
