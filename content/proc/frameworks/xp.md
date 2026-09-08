---
parent: Frameworks
title: Extreme Programming
nav_order: 4
layout: default
---

# Extreme Programming

Extreme Programming is a set of engineering practices held together by very short feedback loops. Its
premise is that a handful of practices known to help — testing, review, integration, design
improvement — should be applied continuously rather than periodically {% cite beck2004xp %}.

Where [Scrum](scrum.md) describes how a team organises and says nothing about how software is
written, XP is almost entirely about how software is written. The two are routinely combined for
exactly that reason.

## 1. The practices, grouped by the loop they close

XP's practices are usually listed flat, which hides the structure. Each one shortens a specific
feedback loop {% cite xp_gentle_intro %}:

| Loop | Practices |
|---|---|
| Seconds | Pair programming, test-driven development |
| Minutes to hours | Continuous integration, collective code ownership, coding standard |
| Days | Small releases, simple design, refactoring, metaphor |
| Weeks to months | Planning game, on-site customer, sustainable pace |

Read that way, the famous ones stop looking like ideology. **Pair programming** is code review with
the delay removed. **Continuous integration** is the integration phase with the delay removed.
**Test-driven development** is specification and testing with the delay removed. The practices are
mutually supporting — refactoring is only safe with tests, collective ownership is only safe with a
coding standard and integration — which is why partial adoption behaves differently from the whole.

## 2. Practices erode unevenly, and that tells you something

**Example — a large XP project over eighteen months.** A ThoughtWorks project of more than 35
developers and 15 analysts tracked its twelve XP practices at four points in time. *"Almost all the
practices have evolved over 18 months"*, and the pattern was not random: the **engineering** practices
— continuous integration, testing, refactoring, coding standards — survived, while the **social**
ones — pairing, on-site customer — eroded {% cite elssamadisy_xp_2001 %}.

That is worth more than a list of practices. It suggests the practices with tooling and visible
mechanics persist, while the ones that depend continuously on human attention and management support
decay unless someone actively protects them. It is also the concrete instance of the question
[choosing a framework](choose.md) ends on: *what will you stop doing?* — answered by default, by
attrition, rather than by decision.

## 3. Where it fits

XP's home ground is small co-located teams, changing requirements, and code that will be lived with
for a long time. Abrahamsson and colleagues' survey places it among the most fully specified of the
agile methods at the level of engineering practice, and among the least specified at the level of
project and organisational management {% cite abrahamsson2002agile %} — which is precisely why teams
graft it onto Scrum rather than choosing between them.

It fits poorly where the team is distributed enough that pairing and an on-site customer are
fictions, where regulation demands documentation XP does not produce, or where the codebase is one
nobody is permitted to refactor.

**Under AI agents.** Pair programming and collective ownership were **review mechanisms** before they
were anything else. If generation accelerates and review does not, the question is what plays their
part — see [agentic](agentic.md).

## How solid is this?

- **The practices are described here from secondary sources.** This review read Wells' widely used
  introduction {% cite xp_gentle_intro %} and Abrahamsson's survey {% cite abrahamsson2002agile %},
  not Beck's book, which is named as the origin {% cite beck2004xp %}. No claim on this page is
  attributed to Beck.
- **`xp_gentle_intro` is a personal website**, maintained 1999–2013 — the most widely linked
  plain-English statement of the practices, and not peer reviewed.
- **Elssamadisy's report is one project, reported by a participant**, unpublished and internally
  dated. The erosion pattern is a plausible mechanism observed once, not a measured rate. It is
  *probably* the same engagement an analyst report of the period describes as a success — the two
  documents do not name each other, so treat the pairing as likely rather than established.
- **Abrahamsson and colleagues' survey classifies methods; it does not evaluate them.** Its criteria are proposed
  rather than validated.
- **No source here compares XP's outcomes to an alternative.**

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
