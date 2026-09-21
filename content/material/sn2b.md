---
parent: Study Notes
title: SN L2b — Frameworks and Choosing
nav_order: 4
page_type: study-notes
layout: default
---

# SN L2b — Frameworks and Choosing

A revision summary of the second Processes lecture. Where L2a gave the lifecycles, this gives the
named frameworks — XP, Scrum, Kanban, the RUP family, the scaling frameworks — and how to choose
between them. Its answer: **the unit of decision is the practice, not the method.** Each section
links to the handbook page carrying the detail and the sources.

## 1. Why adopt a framework, and what it costs

A framework is bought structure. You get a shared vocabulary, defined roles, calibrated estimates
and easier hiring. You pay a learning curve, everything **pre-decided** whether or not it fits, and
a vocabulary that can be **performed without being used** — a stand-up where everyone speaks and
nobody listens has every artefact of Scrum and the purpose of none.

**Adoption fails on people, not on method.** It is hard *"because people are often resistant to
change"*, and needs *"management support… to obtain the authority and budget"*
{% cite lattanze2009architecting %}. The measured version agrees: across 42 large-scale cases the
most-reported success factors are **management support**, **choosing and customising the approach**,
**training and coaching**, and **mindset and alignment** {% cite dikert2016scaling %}. **None is a
practice or a tool.**

So **adopt it whole, then tailor**. Customising is itself a named success factor, so tailoring later
is the plan — what fails is tailoring **before** you understand what the framework was for. Drop the
retrospective in week two and you have removed the only part of Scrum whose job was to change Scrum.

**Frameworks sit on a spectrum of how much they decide for you** — roughly XP, Kanban, Scrum,
AUP/OpenUP, SAFe, RUP, TSP. The light end prescribes less and **adapts by changing the work**; the
heavy end prescribes more and **adapts by changing the plan**. Position is not quality: **weight is
a cost**, bought for size and criticality.

<img src="/images/spectrum.svg" alt="XP, Kanban, Scrum, AUP/OpenUP, SAFe, RUP and TSP on a spectrum from more agile to more disciplined" style="max-width:100%; margin:1.5em 0;" />

→ [Frameworks](../proc/frameworks/index.html) · [Choosing](../proc/frameworks/choose.html)

## 2. Agile, and where it stops

Agile is the ability to **change development in response to changing requirements** — a property you
can check, not a manifesto. A method is agile when it is **incremental**, **cooperative** (customer
and developers in constant contact), **straightforward** (easy to learn **and to modify**) and
**adaptive** {% cite abrahamsson2002agile %}. Four properties, not a values statement — so a
two-week release cadence satisfies one of four and is a cadence, not agility.

**Three of the four standard objections are assumptions agile makes about your situation.**

| Objection | The real content |
|---|---|
| **No structure** | Architecture deferred; short-term focus loses the end state; "agile" as an excuse for no process |
| **It assumes the room** | On-site customer, pairing and osmotic communication all assume co-location |
| **It assumes the work** | Poor fit for maintenance, long lifecycles, fixed price and scope, safety-critical work, heavy documentation |
| **It assumes the org** | Centralised control, inflexible environments and big up-front specifications all fight it |

Each row is the mirror image of a home-ground condition in §6, so learn them together.

**Example —** a 2002 analyst report predicted both that two-thirds of large development shops would
adopt agile within eighteen months, and that agile would **fail to scale**
{% cite narsu2002lessons %}. Neither happened: organisations run Scrum and a phase model at once (§6),
so a hybrid is the normal state rather than a stage on the way to agile.

{: .exam-tip }
> **Exam tip:** be ready to give **two** negatives of agile with an example of each. And read the
> date and the claim type before quoting a number — a *forecast* is not an adoption rate.

→ [XP](../proc/frameworks/xp.html) · [Frameworks](../proc/frameworks/index.html)

## 3. XP, Scrum, Kanban — three frameworks that limit different things

**XP is review, integration and testing with the delay removed.** Its practices group by the loop
each closes: **seconds** — pairing, TDD; **minutes to hours** — CI, collective ownership, coding
standard; **days** — small releases, simple design, refactoring; **weeks to months** — planning game,
on-site customer, sustainable pace {% cite xp_gentle_intro %}. They **hold each other up** —
refactoring is only safe with tests — so partial adoption behaves differently from the whole. XP says
how software is written and almost nothing about how a team is organised.

**Under pressure the social practices go first.** A ThoughtWorks project of 35+ developers tracked its
twelve practices over 18 months: the **engineering** ones survived and the **social** ones eroded —
pairing, on-site customer {% cite elssamadisy_xp_2001 %}. Practices with tooling persist; those
needing human attention decay unless somebody protects them.

**Scrum fixes the time and lets the scope settle.** One team, **three accountabilities** — Product
Owner (the product's value, ordering the Backlog), Scrum Master (establishing Scrum, and the team's
effectiveness), Developers (a usable Increment each Sprint). **Four events** inside the Sprint, itself
a container of a month or less: Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective.
**Three artefacts, each with a commitment**: Product Backlog → **Product Goal**, Sprint Backlog →
**Sprint Goal**, Increment → **Definition of Done** {% cite schwaber2020scrumguide %}. The commitments
are the part most often dropped and the part that does the work — a backlog with no Product Goal is a
list, and an Increment with no Definition of Done was not finished, only stopped.

<img src="/images/scrum-framework.svg" alt="The Scrum framework after the 2020 Guide: artefacts with their commitments, the Sprint container with its events, and the three accountabilities" style="max-width:100%; margin:1.5em 0;" />

What adopting Scrum changes is the **commitment structure**: scope holds still for a Sprint. So ask
whether your work is predictable enough for that — a support team taking an incident on Tuesday
cannot. And note the tension: the Guide says implementing only parts of Scrum means *"the result is
not Scrum"*, while hybrids *"have become reality for nearly all companies"*
{% cite kuhrmann2019hybrid %} and customising is a named success factor {% cite dikert2016scaling %}.
A normative document by a framework's owners is a different kind of thing from evidence.

**Kanban puts a number on each column, and that number is the method** — WIP limits over whatever
process a team runs, with no roles and no ceremonies. A pipeline taking 10 requirements a week,
developing 10 and testing 5 has nobody idle and a queue growing by five a week for ever, **and adding
developers makes it worse**. Cap the test column and the constraint becomes visible.

<img src="/images/kanban-board.svg" alt="A Kanban board with WIP limits on the Ready, In Development and In Test columns; Development is full at 3 of 3, so the pull from Ready is blocked" style="max-width:100%; margin:1.5em 0;" />

**Little's Law**: **lead time = WIP ÷ throughput**, so with throughput fixed, WIP is
the only lever. **Example —** nine people at BBC Worldwide cut features **started** from 84 to **64**
and lead time by **37%** over twelve months {% cite middleton2012kanban %}; the gain is **flow and
predictability, not volume**.

**Scrum caps *time* and lets scope settle; Kanban caps *queue depth* and lets time settle.** That one
distinction generates the whole comparison, and timeboxing is itself a WIP limit, so they are
complements. Kanban suits *"the software maintenance and support areas"* because *"Scrum is not well
suited to highly interrupt-driven work"* {% cite rubin_essential_2012 %}.

→ [Scrum](../proc/frameworks/scrum.html) · [Kanban](../proc/frameworks/kanban.html)

## 4. Scaling: the problem, and what the frameworks sell

**"Scale" is not headcount. It is what grows faster than headcount.** **Interactions** — ten people
have 45 pairs, forty have 780, and past about thirty metres apart spontaneous communication collapses
toward the rate it has between continents {% cite herbsleb_global_2007 %}. **Complexity** —
integration becomes the work. **Concurrent requirements** — one ordered backlog no longer exists.
**Supply chain** — dates you do not control. **The unchanging organisation** — finance and compliance
are adopting nothing. And who is even involved is unknown at the outset
{% cite edison_comparing_2022 %}. Distance bites first, appearing in **76%** of 21 studies
{% cite alzoubi_empirical_2016 %} — hence the rule: **do not distribute a single team.**

**What the frameworks add is structure above the team**, and the two poles show the real choice.
**SAFe** adds Agile Release Trains, **PI planning** and about **twenty named metrics**; **LeSS** adds
**Requirement Areas** with an Area Product Owner each, and specifies **no metrics**
{% cite edison_comparing_2022 %}. So SAFe answers scale with cadence, roles and measurement; LeSS
answers it by **refusing to add structure**. What actually helps is managerial — the success factors
from §1 {% cite dikert2016scaling %}.

{: .warning }
**No scaling framework has been shown to outperform another**, and the best-evidenced review declines
to rank them deliberately {% cite edison_comparing_2022 %}. Adopt one without support and coaching
and you have bought a **vocabulary**.

→ [Scaling and SAFe](../proc/frameworks/safe.html)

## 5. RUP, and the same question SAFe answers

**Every discipline runs through every phase — only the proportion changes.** Requirements, design,
implementation and test are **disciplines**, not phases in sequence: requirements work does not stop
when Construction starts, there is simply less of it. That is what separates *iterative* from
waterfall with more meetings {% cite kruchten2003rup %}.

<img src="/images/rup-humps.svg" alt="The RUP hump chart: four phases across the top, nine disciplines as rows, each hump a teaching schematic of how much of that discipline happens in each phase" style="max-width:100%; margin:1.5em 0;" />

**A phase ends when a class of risk is retired, not when work is done.** Inception asks whether this
should exist at all; **Elaboration** whether the architecture is provable, via an executable skeleton
on the risky paths; **Construction** builds against a settled structure; **Transition** gets it to
users. The gates are named for what they **settle** — LCO, LCA, IOC, PR — not for a quantity of work
delivered, which is the difference from a waterfall milestone. **AUP** and **OpenUP** keep the shape
and cut the artefacts {% cite balduino2007openup %}: the weight is a dial. Use RUP where
**architecture is the dominant risk**; an untailored RUP on a small team is the standard failure.

**RUP and SAFe answer the same question, twenty years apart.** RUP (1999): too many people to
coordinate informally, so define **roles and artefacts** and gate on **architecture**. SAFe (2011):
too many teams, so define **cadence and ceremonies** and gate on a **planning increment**. Same
structure-above-the-team, different material — **you buy coordination and pay in ceremony**.

→ [RUP and the Unified Process](../proc/frameworks/rup.html) · [ACDM](../proc/frameworks/acdm.html)

## 6. Choosing — and what you are actually choosing

**Practices travel; methods don't.** The most adopted **practices** beat the most adopted
**methods**: code review **69.6%**, CI **63.8%**, unit testing **59.4%**, against Scrum **53.6%** and
waterfall **34.8%**. And only about **one process in five** came from a planned improvement
programme; the rest **emerged** {% cite kuhrmann2019hybrid %}. That is evidence the thing being
decided is **smaller than a framework**.

**Size and criticality set the weight.** Cockburn's grid crosses seven size bands with four
criticality zones — **C**omfort, **D**iscretionary money, **E**ssential money, **L**ife — so a project
lands in a named cell such as **C6** or **L100**, and heavier methods belong up and to the right
{% cite cockburn_selecting_2000 %}: *"A more critical system… needs more publicly visible correctness
in its construction."* And **coordinates move while you run the project** — Chrysler's C3 *"stretched
a D6 methodology to fit a D14 project."*

<img src="/images/cockburn-grid.svg" alt="Cockburn's grid: seven size bands across, four criticality zones up, every cell named, C6 and L100 outlined" style="max-width:100%; margin:1.5em 0;" />

**Five axes, and the distance from home ground is the risk** {% cite boehm_balancing_2003 %}:

| Axis | Agile home ground | Plan-driven home ground |
|---|---|---|
| **Size** | Smaller teams and projects | Larger teams and projects |
| **Criticality** | Untested on safety-critical work | Evolved for critical products; **hard to tailor *down*** |
| **Dynamism** | Refactoring is cheap under high change | Detailed plans amortise when requirements are stable |
| **Personnel** | Needs a core of skilled staff, full time | Tolerates less-experienced staff, given a framework |
| **Culture** | *"Thrives on chaos"* | *"Thriving on order"* |

**Dynamism** is the *rate of requirements change*. **Criticality** is *loss due to failure*, and it
cuts **both** ways: agile is untested tailored *up* to safety-critical work, and plan-driven methods
are hard to tailor *down* to low-criticality products. Most people give only the first half. Plotted
on those axes the centre is agile home ground and the rim plan-driven — but it is a **communication
device, not a measurement**, since the axes share no unit and the enclosed *area* means nothing.

<img src="/images/polar-chart.svg" alt="Boehm and Turner's polar chart: agile home ground at the centre, plan-driven at the rim; a six-person reporting tool near the centre, a 200-person avionics programme at the rim" style="max-width:60%; margin:1.5em 0;" />

**Example —** Servasport, four developers and a designer on fixed-price projects, scored environmental
risk 3, agile 8, **plan-driven 15** → risk-based agile {% cite taylor_applying_2006 %}. **The
mitigations are the point, not the verdict**: turnover risk produced a wiki and mentored
role-swapping, and rapid change produced **weekly incremental delivery for the final three weeks,
written into the contract.**

**The four questions for any recommendation.** **1** What is the team already doing? **2** What does
the risk profile demand — size, criticality, dynamism? **3** Which practices close the gap? **4** What
will you stop doing? Adopt practices without retiring any and you get a process with two of
everything; if you do not decide, **attrition decides** — which is what happened to pairing in §3.

→ [Choosing a framework](../proc/frameworks/choose.html) ·
[Balancing agility and discipline](../proc/frameworks/balance.html)

## 7. What AI generation does to all of this

Across **39 studies**, whether LLM assistants *"improve or degrade code quality"* remains
**unresolved** {% cite mohamed2025llm %} — and developers are unreliable witnesses about it: in a
randomised trial they were **19% slower** while believing they had been **20% faster**
{% cite becker2025metr %}. So do not ask whether the tool is fast; ask **where the constraint moved.**

Generation doubles what enters review and nothing doubles review, and nobody ever capped the review
column — so the queue absorbs the difference and lead time gets **longer** while every developer is
faster. That is §3's Kanban argument run backwards. The per-framework consequence, and the bound on
what is known, is on the handbook page.

<img src="/images/ai-review-queue.svg" alt="A board where AI-assisted development opens twenty pull requests a week, review clears ten with no WIP limit, and the queue grows by ten a week; the numbers are an illustration" style="max-width:100%; margin:1.5em 0;" />

→ [Process under AI agents](../proc/frameworks/agentic.html)

## Where this goes next

**C2 TARTAN** asks for a **recommendation, not a preference**: the four questions from §6, plus the
risks your choice creates. The lifecycle half is [SN L2a](sn2a.html), and revision
questions for both lectures are in [RQ2](rq2.html).

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David
Root** {% cite root2014lectures %} on software project management. The structure, examples, and
pedagogical approach reflect their teaching materials and frameworks.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
