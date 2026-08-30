---
title: Home
layout: home
nav_order: 1
page_type: home
---

<div align="center">
  <img src="/images/msdbok_logo.png" alt="MSDBOK Logo" style="width:180px; margin-bottom: 1em;" />
</div>

# Managing Software Development

A handbook for the people who have to decide: what to build, how big it is, in what order, and
whether it is going well. It accompanies the MSD course at Innopolis University and is written to
be read on its own — one page per method, self-contained, with its sources on it.

---

## The six areas

Each area answers one question, and each supplies the next. You cannot scope what you never
elicited, plan what you never scoped, or track what you never planned — which is why so many
"planning failures" were settled much earlier.

<div align="center">
  <img src="/images/msd-areas.svg" alt="The six areas as a chain: People, Process, Needs, Scope, Planning, Tracking" style="max-width:100%; margin: 1.5em 0;" />
</div>

**[People](/content/people/) — who does the work.** What a technical person gives you and how
to stop measuring the wrong thing; the limits of personality models; how teams form, why effort
per person falls as they grow, and how groups decide worse than their members. *After it, you can tell which team problems are fixable by a manager.*

**[Process](/content/proc/) — how work flows.** Lifecycle stages and process frameworks, and
how to choose between them by context rather than by fashion. *After it, you can justify a
process choice instead of inheriting one.*

**[Needs](/content/needs/) — what to build.** Customer expectations and how they are set;
requirements that can be tested; risks named early enough to act on. *After it, you can write a
requirement someone can disagree with.*

**[Scope](/content/scope/) — how big it is.** Work breakdown structures, and estimation from
analogy, counting, judgement and parametric models. *After it, you can produce an estimate with
its assumptions attached.*

**[Planning](/content/plan/) — in what order.** Agile against plan-driven, milestones and
activities, the critical path, and release planning under a fixed date. *After it, you can say
which slip matters and which does not.*

**[Tracking](/content/track/) — is it on track.** Progress monitoring, earned value, burndown,
and reporting that survives the person being reported to. *After it, you can read a
green dashboard sceptically.*

---

## Start here

- **Revising for a session or a quiz** → [Materials](/content/material/) — a study note per
  lecture and a set of revision questions per area.
- **Looking up a method** → open its area above, or use the search box.
- **Wondering whether to believe a page** → its **How solid is this?** section, at the bottom.

---

## How this handbook is built

It began as the skeleton of **Eduardo Miranda**'s and **David Root**'s *Managing Software
Development* at Carnegie Mellon, together with the classics that course rests on — Brooks,
Herzberg, Tuckman, Steiner, Goleman.

That skeleton is re-grounded one topic at a time. Each gets a literature search and a read of
what it turns up — the corpus stands at **24 books and 153 papers** and grows as the review moves
through the areas. What survives becomes a short brief: one method per page, under 800 words,
with a worked software example and at least one limitation.

Two consequences show on every page. Sources are cited **where the claim is made**, not gathered
in a bibliography nobody opens. And each page ends with **How solid is this?** — what the claim
rests on and where it is thin. Some of the best-known ideas here are the least evidenced, and the
handbook says so.

---

## Contributing

Corrections and additions are welcome, from students and practitioners alike.

- **Fix a content issue** — typos, wrong facts, a citation that does not check out →
  [guidelines](https://github.com/msdbok/msdbok.github.io/blob/main/CONTRIBUTING.md)
- **Add a method page** — one technique, following the
  [method template](https://github.com/msdbok/msdbok.github.io/blob/main/templates/method-template.md)
- **Write an analysis** — a comparison across methods, following the
  [analysis template](https://github.com/msdbok/msdbok.github.io/blob/main/templates/analysis-template.md)

Every page is held to [the page standard](https://github.com/msdbok/msdbok.github.io/blob/main/templates/page-standard.md).

---

## Acknowledgments

Much of this handbook is heavily inspired by and adapted from lectures by **Eduardo Miranda** and
**David Root** on software project management — the structure, examples and pedagogical approach
throughout reflect their teaching materials. Pages built on that material name them in an
**Acknowledgments** section, with full citations in **References**.

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
