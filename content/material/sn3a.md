---
parent: Study Notes
title: SN L3a — Customer Expectations
nav_order: 6
page_type: study-notes
layout: default
---

# SN L3a — Customer Expectations

A revision summary of the first Needs lecture. Its one claim is that two teams can ship **identical
software** and collect opposite verdicts, because a customer does not judge what you delivered — they
judge it against what they were expecting. Everything below is a way of finding out what they expect,
or of moving it while that is still cheap. Each section links to the handbook page carrying the
detail and the sources.

## 1. A verdict is a comparison, not a measurement

The relationship that organises the whole lecture is a ratio {% cite boehm_requirements_1999 %}:

> **Customer perception = Project performance ÷ Expectations**

A customer expecting a four-second response calls three seconds a win. A customer expecting one
second calls the same three seconds a failure. So the first question about a "slow" system is never
*how slow* — it is **what did we tell them it would be**. The numerator is the half you were already
managing; the denominator is the half this lecture is about.

The denominator has structure. Customers hold **three** standards at once
{% cite zeithaml1993expectations %}: the **desired** level they hope for, the **adequate** level they
will accept, and the **predicted** level they think they will actually get. The gap between desired
and adequate is the **zone of tolerance** — land inside it and nobody complains at all.

<img src="/images/zone-of-tolerance.svg" alt="Desired, adequate and predicted service, with the zone of tolerance between the top two" style="max-width:100%; margin:1.5em 0;" />

Two consequences are worth memorising. The zone **moves from the bottom**: almost every lever a
manager holds acts on the adequate line, not on what the customer wants. And it **narrows with
history** — a second failure after a botched recovery, or a visible alternative supplier, tightens
it. The one move that widens it is a cause outside your control that they hear **from you**, which is
why a status page and a postmortem are project management rather than public relations.

→ [Expectations](../needs/exp/) · [Setting expectations](../needs/exp/setting)

## 2. Delivering everything they asked for still scores zero

Requirements do not all move satisfaction the same way, which is why a fully delivered backlog can
land flat. Kano sorts them into three classes {% cite sauerwein1996kano %}:

<img src="/images/kano.svg" alt="Three classes of requirement plotted against how fully they are met, with the migration over time" style="max-width:100%; margin:1.5em 0;" />

- **Must-be** — taken for granted, so meeting them buys nothing and missing one is punished hard.
  The login works, no data is lost, the page loads.
- **One-dimensional** — satisfaction is proportional to fulfilment. Speed, quota, rate limit. This is
  usually what was actually asked for, and the only class where *"we improved it 20%"* is a sentence
  worth saying.
- **Attractive** — never asked for, so their absence costs nothing and their presence delights.

The tie-break is **must-be beats one-dimensional beats attractive**: no amount of delight compensates
for a failed must-be, which is what "delivering everything gets you to zero" means. Two boundary
conditions carry as much weight as the model itself. The class belongs to the **customer segment**,
not the feature — single sign-on is a must-be for enterprise accounts and an irrelevance to a free
tier. And an attractive requirement **decays into a must-be**, so a classification has a half-life.

→ [Kano classes](../needs/exp/kano)

## 3. Somebody defines success — make sure it is not after delivery

Success is a definition before it is a number. The CHAOS reports publish two side by side, and for
the same FY2015 database they give **36%** successful under the traditional definition and **29%**
under the modern one {% cite standish2015chaos %}. Nothing about the projects changed. When you are
quoted a failure rate, the first question is which definition produced it.

For magnitudes, use better-sourced work: a McKinsey study with Oxford of **5,400 projects over $15
million** found an average **45% cost overrun** and **56% less value** than predicted — and that
software alone was worse, at **66% and 33%** {% cite bloch2012mckinsey %}.

The project-level answer is to write success down before the work starts. Wysocki's **Conditions of
Satisfaction** is a loop — request, clarification, response, agreement — repeated until neither side
corrects the other {% cite wysocki2003needs %}. The restatement *is* the test: a correction means you
had it wrong and did not know. Its deliverable is a one-page Project Overview Statement, and it
carries **no completion date**, which is negotiated after scope is agreed rather than before.

The **threshold of success** is built backwards, because goal statements resist precision and failure
statements do not {% cite hoover_evaluating_2010 %}: write what failure looks like, invert each
statement into a criterion, and check each is SMART — where the **A is *assignable***, naming who is
responsible. The payoff arrives in L3c: a **risk is exactly a concern that would breach the
threshold**, and everything else is an event that might happen and would not matter.

→ [Defining success](../needs/exp/success) · [Threshold of success](../needs/exp/tos)

## 4. Whose expectations are they?

You cannot manage the expectations of people you have not found. Alexander and Robertson model
stakeholders as four rings, and the useful mechanism is the **slot** — a generalised role, drawn
solid when filled and greyed out when not {% cite alexander2004onion %}. **An empty slot is a
finding; a missing person is just invisible.**

Finding them turns out to be the easy part. Asked to name the single stakeholder concern causing the
biggest problem in their own work, 541 practitioners put **skill** first at 38% and **commitment**
second at 34%; **discovery came fourth**, at 13%. The hard problem is getting the people you already
located to engage usefully.

Their satisfaction is also not linear. At Xerox, **completely** satisfied customers were **six times**
more likely to repurchase than merely satisfied ones {% cite jones_why_1995 %}. So a team reading
**82% in the top two boxes** as a pass has misread it: the correct reading is *"48% are completely
satisfied and 52% are up for grabs."* Stated intent flatters further — 60–80% of car buyers say they
will rebuy the brand, and 35–40% do.

→ [Stakeholders](../needs/reqs/stakeholders) · [Customer types](../needs/exp/cust_types)

## 5. Educating the customer is cheaper than negotiating with them

Each side can only trade what it controls. The customer holds **scope, time, quality and cost**; the
developer holds **people, process and technology** {% cite hoover_evaluating_2010 %}. An expectation
is a **point** in the customer's space, and the manager's job is the function that reaches it from a
space with different axes. A developer-side decision only becomes negotiable once restated in the
customer's four terms.

The reason the two sides cannot negotiate unaided is what Boehm calls the **Two Cultures**: neither
has a feel for what is cheap on the other's side {% cite boehm_requirements_1999 %}. A customer who
cannot see relative cost **prioritises on desire**, because desire is the only information they have.

The fix is information, not persuasion. For example, a Windows beta customer brought two changes,
both labelled *must have* {% cite mcconnell_rapid_1996 %}: a toolbar button at **half a day**, and hot-linked
drag-and-drop needing full OLE support at **six to nine staff months**. Told the two costs, the
customer withdrew the expensive one themselves — *"No way! It's not that important."* Nobody
negotiated and nobody refused. In the same spirit, one architecture estimated at **$100M came back at
$30M** after a single prototype.

→ [Expectation space and solution space](../needs/exp/quadrant)

## 6. Involving them: a lever with a setting, not a virtue

The largest synthesis available — **87 studies over 32 years** — splits **52 positive, 12 negative,
23 uncertain** {% cite bano2015involvement %}. Involvement usually helps and sometimes makes things
worse, which turns an exhortation into four design decisions: **which users**, at **what degree**
(informative → consultative → participative), for **which goal** (a sense of control, or moving
domain knowledge), and in **which phase**. Note also that **involvement is not participation** —
attendance is a behaviour, involvement is a psychological state, so *"we involved the users"* is not
a checkable claim.

When the customer will not give you the time, a three-year study of 30 practitioners mapped what
teams do instead, as a continuum ordered by directness: **on-site customer → story owner → just demos
→ e-collaboration → customer proxy → extreme undercover** {% cite hoda2011customer %}. Knowing which
rung you are on is more useful than any advice about collaboration. Two repairs are concrete enough
to copy — a **Definition of Ready**, and a **buffer sized from recorded velocity**.

The practical rule underneath all of it: **show the software, do not report on it**. One team ran the
customer hour as 15 minutes showing and 45 discussing. A prototype that read fine in every status
report turned out to be **40% correct**, and the fix was walking users through the build every two
weeks. As one agile coach put it, a customer can say *"I want to have Taj Mahal"* — but of granite or
marble? *"They don't even have time to talk about that."* Reacting is cheap; specifying is not.

→ [Customer involvement](../needs/exp/involvement)

## 7. When it goes wrong

Petter studied 12 project managers across 24 cases and found three strategies and 24 tactics, of
which only three risks are genuinely under your control {% cite petter2008expectations %}. The one to
remember: **they should hear it from you, and early**. Bad news you deliver first buys tolerance; bad
news they discover spends it.

Two quieter points close the lecture. You set expectations with your **price list**, not just your
roadmap — a premium price is a promise {% cite zeithaml1993expectations %}. And a **change request is
how a customer learns what things cost**, so every accepted change gets an impact statement in three
lines before anyone starts, which returns the conversation to §5.

## Where this goes next

**L3b** turns expectations into requirements a tester can hold you to; the PBJ exercise straight
after it shows how badly that goes when assumptions stay unwritten. **L3c** takes the concerns that
would breach your threshold and manages them as risks. All three are examined together in **Q3**.

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
