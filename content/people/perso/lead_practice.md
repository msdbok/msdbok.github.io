---
page_type: deep-dive   # five worked cases plus page-specific caveats on three unsourced practices
parent: Personality
title: Leading in Practice
nav_order: 4
layout: default
---

# Leading in Practice

_Adapted from lecture materials by David Root {% cite root2014lectures %}._

Leading in practice means diagnosing the situation in front of you and picking the leadership style
that fits it, rather than defaulting to the one that suits your temperament. The six styles this
page draws on — coercive, authoritative, affiliative, democratic, pacesetting and coaching — are
Goleman's {% cite goleman2000leadership %}; their definitions, measured effects on team climate and
evidential standing are on [Leadership styles](lead.html).

## Choosing a style

Start from the outcome you need in the next 24 to 72 hours — survival, clarity, morale, buy-in,
speed or growth — and work back to the style, rather than starting from the style that suits you.
Most effective leaders mix authoritative, coaching, democratic and affiliative depending on people
and timing; pacesetting and coercive are emergency tools, not settings you leave on. Say which mode
you are in and how long it lasts. *For example,* announcing "we are in intense delivery mode for two
weeks, then we pause for refactoring and recovery" costs nothing and removes most of the confusion
and resentment a crunch generates. Keep authoritative clarity by measuring outcomes rather than
activity — measurable goals or OKRs set the *what* while the team decides the *how* — and use the
affiliative and coaching modes to protect developer time: blocked focus time, meeting-free days,
batched interruptions.

## Five software situations

Each row is a situation a software manager actually meets, the blend that fits it, and what running
that blend looks like.

| Situation | Blend | What it looks like |
|---|---|---|
| **Incident response** — a customer-facing production outage | Coercive, then authoritative | One incident commander issues concise directives to stop the bleeding; the moment the site is up, switch to authoritative and align the team on preventing recurrence. Speed first, then clarity and learning |
| **Setting product direction** — a pivot to a new product-market fit | Authoritative + democratic | The senior technical leader states the vision and the OKRs; squads propose technical approaches and own their delivery plans. Democratic input, authoritative ends |
| **Sparking innovation** — engagement and cross-team learning are flat | Affiliative + coaching | Run hackathons or innovation days on which teams work on their own projects; leaders support and celebrate participation instead of directing it |
| **Scaling the organization** — many teams, duplicated work, inconsistent practice | Democratic + coaching + authoritative | Chapters, guilds and communities of practice share practice; coaching develops the tech leads; an authoritative vision keeps priorities unified |
| **Release push** — a launch deadline that genuinely requires speed | Pacesetting, timeboxed | A short, defined window with volunteers who are already strong performers, and a scheduled recovery: retrospective, refactoring, tech-debt repayment |

## A participative mechanism you can run

Democratic leadership is easy to describe and hard to operate; here is one documented mechanism. A
team of 26 engineers needed a new Operations Project Leader. Rather than a manager-to-manager
placement, a **six-engineer selection sub-team** built a weighted list of traits and skills **by
consensus rather than by vote**, scored each candidate 0–10 against each trait × its weight, and
**committed in advance to offering the job to the top scorer** — moving the decision authority,
though not the accountability, off the manager. Eight candidates applied; the top two finished less
than ten points apart {% cite mccarthy2003participative %}.

## Checklist for a junior project manager

Name the outcome you need, then map it to a style using the table on
[Leadership styles](lead.html). Announce the mode and its expected duration. If you choose coercive
or pacesetting, timebox it and schedule the restorative work — a retrospective, a refactoring window
— at the same time. After any high-pressure phase, switch deliberately into coaching and affiliative
mode through retrospectives and one-on-ones. And watch team climate rather than waiting for it to
break: engagement surveys, velocity trends and defect rates all drift before people resign.

## How solid is this?

Everything on this page is practice rather than measurement. Nothing here has been tested on
software teams, and two of the illustrations are weaker than their popularity suggests.

- **The participative selection is an n = 1 experience report.** One team, one company, no control,
  written by the manager who ran it — who records a colleague's objection that the outcome "could
  have been predicted all along, without the complex process". His answer is the teachable part:
  the choice was a by-product, and the value lay in what the discussions revealed about the team's
  value system. A practice with a case behind it, never a measured effect. (The title word is
  "Formulation", not "Formation" — the misquotation is common.)
- **Protected focus time is a practice, not a finding.** That interruptions harm developer output
  is plausible and widely repeated, but **this handbook holds no study supporting it** — measure it
  on your own team. The nearest sourced thing is Glen's account of [flow](glen.html), itself a
  practitioner framework.
- **Two popular illustrations are not templates.** A company describing its own innovation days is
  marketing, and no study here measures what they produce. The Spotify "squads and tribes" model is
  routinely cited for the scaling row above, yet its own authors have since said it described an
  aspiration, was never fully implemented, and had been abandoned by the time it spread — and this
  handbook holds no source for the model or the disavowal.
- **The style ratings** are correlational, from an unpublished proprietary study of executives,
  c. 1999 {% cite goleman2000leadership %} — provenance on [Leadership styles](lead.html).

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
