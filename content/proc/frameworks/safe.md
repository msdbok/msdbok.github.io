---
parent: Frameworks
title: Scaling Agile and SAFe
nav_order: 9
layout: default
---

# Scaling Agile and SAFe

Agile methods were built for small co-located teams. Scaling frameworks — SAFe, LeSS, Nexus,
Scrum@Scale — exist to handle what those methods do not address: synchronising many teams, meeting
parts of the organisation that are not changing, and reconciling team autonomy with an existing
hierarchy {% cite leffingwell2020safe %}.

The honest position is that we know a good deal about **what breaks** and very little about **which
framework fixes it**.

## 1. Scaling breaks the practices that need people in the room

The damage is not evenly distributed. On a large XP project tracked over eighteen months, the
**engineering** practices — continuous integration, testing, refactoring — survived, while the
**social** ones — pairing, on-site customer — eroded {% cite elssamadisy_xp_2001 %}.

There is a mechanism behind that. The coordination agile relies on is *co-located* coordination, and
it decays with distance faster than people expect: beyond roughly thirty metres, spontaneous
communication collapses toward the rate it has between continents {% cite herbsleb_global_2007 %}.
A team on another floor is, for these purposes, already distributed.

The frequency data agrees. Across 21 studies of distributed agile development, **distance appears as
a communication challenge in 76%**, ahead of organisational factors at 52% and team configuration at
48% {% cite alzoubi_empirical_2016 %}. The same body of work yields a blunt practical rule: do not
distribute a *single* team — split along boundaries that need less talking.

The largest review of large-scale transformations catalogues **35 challenges in 9 categories**,
including coordination across multi-team environments, divergent approaches emerging between teams,
hierarchical management and organisational boundaries, and integrating functions that are not
development {% cite dikert2016scaling %}.

## 2. What helps is managerial, not technical

The same review names **29 success factors**, and the most salient categories are **management
support, choosing and customising the agile approach, training and coaching, and mindset and
alignment** {% cite dikert2016scaling %}. None of them is a practice or a tool.

Two things follow. First, **the framework is the cheap part** — an organisation that adopts SAFe
without management support or coaching has bought a vocabulary. Second, **customising the approach is
an evidenced success factor**, not a deviation from it, which sits awkwardly beside frameworks that
present themselves as complete.

## 3. Read the method, not the sentence

**Example — two reviews, two answers.** Students ask which framework to pick, and the literature
contains both an answer and a refusal.

| | A comparative review {% cite almeida_large-scale_2021 %} | A systematic review {% cite edison_comparing_2022 %} |
|---|---|---|
| Claim | SAFe is *"the most suitable for working in large organizations with geographically distributed teams"* | *"there is no one method that suits a particular type of company"* |
| Method | Qualitative review of secondary sources; **no search protocol, no corpus size, no inclusion criteria, no inter-rater check** | **35,215 articles screened → 191 primary studies** |
| Venue | A journal in its second volume | IEEE Transactions on Software Engineering |

And the first paper **walks its own claim back**: the mapping appears in the body, while the
conclusion retreats to *"a framework that presents good results in one organization can be a failure
in another"*.

That is the useful lesson, and it is more useful than "nobody says this". The confident sentence
exists, it is weakly evidenced, and its own conclusion does not support it. **Ask what method
produced the sentence.**

## How solid is this?

- **Nothing here outperforms anything.** No scaling framework has been shown to beat another, and
  the best-evidenced review available declines to rank them deliberately
  {% cite edison_comparing_2022 %}.
- **Dikert is mostly experience reports** — roughly 90% by its authors' own count, and they state
  they *"decided not to make quantitative interpretations"*. Its challenge and success-factor lists
  are frequencies of *mention*, not effect sizes {% cite dikert2016scaling %}.
- **Almeida has no stated protocol**, and its single outcome figure is borrowed from another study.
  Cite it as an example of a weakly supported claim, not as support for one
  {% cite almeida_large-scale_2021 %}.
- **Herbsleb is a research roadmap**, not a study; the thirty-metre finding comes from older
  communication research that it summarises {% cite herbsleb_global_2007 %}.
- **Elssamadisy is one project** reported by a participant, unpublished and internally dated
  {% cite elssamadisy_xp_2001 %}.
- **SAFe's own text is cited only for what SAFe is** {% cite leffingwell2020safe %} and for nothing
  else. It is written by the framework's creator and was not read for this review.

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
