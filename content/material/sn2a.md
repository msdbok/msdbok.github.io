---
parent: Study Notes
title: SN L2a — Process and Lifecycles
nav_order: 3
page_type: study-notes
layout: default
---

# SN L2a — Process and Lifecycles

A revision summary of the first Processes lecture. It makes the same move at four scales: write down
what you do, decide what tells you it is working, name the level you mean, and pick the shape that
fits the work. Each section links to the handbook page carrying the detail and the sources.

## 1. Why a defined process pays for itself

A defined process is one you can **repeat, check and improve**. If you cannot repeat it you have a
performance; if you cannot check it you have a belief.

It pays because of a property specific to software. A misunderstanding written into a requirement is
**honoured** by the design, implemented faithfully by the code, and confirmed by tests written from
the same misunderstanding. Every stage does its job correctly and the error is *carried, not caught*
— which is why a green test suite is consistent with building the wrong thing. The cost of fixing a
defect rises steeply with the stage it is found in, steeply enough that the studies disagree about
the multiplier {% cite boehm_understanding_1988 %}, so treat the shape as the finding rather than the
number.

So the work products **before** the code — estimates, requirements, architecture, test plans — are
each a place a defect can enter, which is what makes them worth reviewing. Quality assurance
therefore covers **the product** and **the process that builds it**: the process limits how many
defects were *injected*, and inspection only catches what the process already let in. Rework runs
**30–80% of effort**; inspections cost **20–30% of first-half effort**, and Fagan calls the fear that
they delay a project *"a myth"* {% cite fagan2002inspections %}.

Two practical points. **Ask the doers, not the managers** — the manager's version is the process
*designed*, the doers' is the one that *runs* {% cite radice_programming_1985 %}. And **improvement
is a loop**: Plan, Do, **Check**, Act {% cite deming1986crisis %}. Check is the rung teams drop,
because two questions hide behind *"is it working?"* — whether the process is **followed**, and
whether following it **produces the outcome**. A process can be followed faithfully and still be
wrong.

→ [Process basics](../proc/basics/index.html) · [Defining a process](../proc/basics/define.html) ·
[History](../proc/basics/history.html)

## 2. ETVX: one activity, written so it can be checked

ETVX writes a single activity as four parts {% cite radice_programming_1985 %}: **Entry** — what must
be true before it starts; **Task** — what is actually done; **Validation** — how the result is
checked; **Exit** — what must hold before it may finish.

**Exit is the part that changes behaviour.** Entry and Task are usually written down somewhere
already; Exit is what stops work being declared complete because the calendar says so. An activity
whose exit criterion is *"the document exists"* has not been defined, it has been named — whereas
*"every interface has a named owner and a stated failure mode"* cannot be satisfied without having
done the design.

**ETVX is not a gate chain**, and that is the common misreading. Radice rules it out explicitly: the
notation *"does not imply that all activities or tasks in a later stage must wait for completion of
predecessor stages. The later stages may be functioning in parallel with previous stages"*. It
constrains the **handoff** between defined activities, not the calendar — which is why it sits
underneath plan-driven and iterative work alike.

**Example —** Oerlikon Aerospace built a laser-guided air-defence system with **60+ engineers** under
MIL-STD-2167A and chose ETVX *"because of its simplicity"* {% cite laporte_software_1996 %}. Their
estimation step exits on an approved WBS and OBS, a schedule, cost estimates — **and a list of the
alternatives considered**. That last item cannot be produced retrospectively, so requiring it at exit
forces the estimating to have actually happened.

{: .exam-tip }
> **Exam tip:** a good exit criterion is one you **cannot fake after the fact**.

→ [ETVX](../proc/basics/etvx.html)

## 3. Measuring the process, and what the number does to people

**GQM runs backwards from how measurement usually happens** {% cite basili1994gqm %}: **Goal**
(conceptual — what are we trying to achieve, and for whom) → **Question** (operational — what would
we have to know to tell) → **Metric** (quantitative — what data answers it). Most measurement runs
the other way, collecting what the tooling emits and then looking for a story in it. **A metric with
no question above it has no reason to exist.** Name the **object** first — a *product*, a *process*
or a *resource*: a team whose goal is about a process will reliably propose metrics about the code.

**GQM's drawback comes from its own author**, sixteen years on. Measurement programmes fail through
*"disillusionment about metrics on the part of developers and managers"*, and GQM *"does not provide
explicit support for motivating and integrating measurement at various levels of the organization"*
{% cite basili2010gqmstrategies %}. So check the goal is **held** in common before deriving a single
question: "improve quality" means fewer escaped defects to support and less time in legacy code to
the engineers, and every question derived from it inherits the disagreement.

**A metric aimed at people stops being a measurement.** Humphrey states it absolutely: *"Process data
must not be used to compare projects or individuals. Its purpose is to illuminate the product being
developed and to provide an informed basis for improving the process"* {% cite fowler_software_1990 %}.
Precision is no defence — dysfunction appears *"whether or not our models are correct"*
{% cite hoffman2000metrics %}.

**Example —** twenty-five open defect reports were closed as *"duplicates"* of one new report whose
only shared property was the subsystem it was filed against {% cite hoffman2000metrics %}. Nobody
falsified anything and every closure was defensible; the count improved and the defects were still
there. The modern version is **velocity**: make points-per-sprint a target and estimates inflate
{% cite rubin_essential_2012 %}. So the question is not *is this the right number* but **who will see
it, and what happens to them because of it**.

Where something matters and cannot be counted — morale, trust, whether estimates are believed — a
short recurring anonymous questionnaire tracks **judgement as a trend** {% cite mota2009scoreboard %}.
Read the direction, not one week's score, and cover every role: one team left the Training Manager
off as *"a minor role not relevant to measure"*, and the omission itself caused *"debate and concern
inside the team"*. What you decline to measure is a message too.

→ [GQM](../proc/basics/gqm.html) · [Metrics](../proc/basics/metrics.html) ·
[Scoreboard](../proc/basics/scoreboard.html)

## 4. Process, lifecycle, framework — four rungs

Three words get used as if they were one. They are rungs, each more concrete than the one above:

| Rung | What it is | Example |
|---|---|---|
| **Lifecycle model** | The phases, and the go/no-go points between them | Waterfall · Spiral · V |
| **Framework** | Reusable structure — roles, events, practices — to work *inside* those phases | Scrum · RUP · Kanban |
| **Process** | What one organisation actually does, in detail | This team's definition of done |
| **ETVX** | The unit any of them decomposes into | entry · task · validation · exit |

**The one-sentence version:** a lifecycle names the phases; a framework supplies reusable structure
to work within them. **Waterfall is a lifecycle; Scrum is a framework.** Scrum settles its own case,
describing itself as *"a container for other techniques, methodologies, and practices"*
{% cite schwaber2020scrumguide %} — it tells you how to organise a fortnight, not what order the
phases come in, and that fortnight can sit inside a waterfall phase or an iterative one.

SWEBOK licenses the whole block: *"There is no best software process… No ideal process, or set of
processes, exists"* {% cite bourque_swebok_2014 %}. The same entry defines a process as inputs →
activities → outputs which *"may also include its entry and exit criteria"* — ETVX restated in 2014.

A software **lifecycle** is the cradle-to-grave existence of a product. Most of a lifecycle *model's*
value is communication: the team can say where it is, management can see status, the customer can be
told what happens next. Those three want different things from the same phase name, so the rule is
**define, communicate, define, communicate**.

{: .exam-tip }
> **Exam tip:** the distinction is examined, not the words. Be ready to place a **named** example on
> the right rung and say why.

→ [Lifecycles](../proc/lifecycles/index.html) · [ETVX](../proc/basics/etvx.html)

## 5. Six shapes, and what each one buys

| Model | Structure | Feedback | Choose it when |
|---|---|---|---|
| **Waterfall** | Linear, once through | Late | Requirements are stable and the work must be contractible and audited |
| **V-Model** | Waterfall, drawn to show V&V | Late, tests designed early | Verification must be demonstrated to a regulator or customer |
| **Incremental** | Usable slices, staged | Per increment | You know what to build but cannot build it all at once |
| **Iterative** | Whole product, repeated | Every iteration | You do not yet know exactly what to build |
| **Prototyping / RAD** | Build to answer a question | Immediate | One uncertainty is cheaper to resolve by building than by analysis |
| **Spiral** | Risk-driven loops | Every cycle | Risk should decide what happens next, and you control the commitment points |

Three things the table cannot say, and they are the examined ones.

**Waterfall's advantage and its disadvantage are the same property.** Fixed phases with defined exit
criteria make it **contractible** — you can price a phase, staff it, audit it, hold someone to it,
which for fixed-scope procurement and regulated work is the point rather than bureaucracy. The same
property delays the first honest feedback to the end: testing is *"the first event for which timing,
storage, input/output transfers, etc., are experienced as distinguished from analyzed"*
{% cite royce1970waterfall %}. Royce's own fix was to **do it twice** — ten months of a thirty-month
effort on a pilot pass in the critical areas. One pass to retire originality risk, **not** iterative
development {% cite larman_iterative_2003 %}.

**Incremental adds parts; iterative improves parts.** Both repeat; the difference is **how well the
requirements are known when you start** {% cite pressman2010incremental %}. Incremental assumes
requirements *"reasonably well defined"* and ships an operational slice each pass, core product
first. Iterative expects requirements to move and produces *"an increasingly more complete version"*,
with the feedback part of the deliverable. So choosing incremental assumes stakeholders can tell you
*now* what the slices are — and will still want the same ones in six months.

**The spiral's defining property is not the loops.** It *"creates a **risk-driven approach** to the
software process rather than a primarily document-driven or code-driven process"*
{% cite boehm_spiral_1988 %}. Risk-driven does not mean the project is risky — the risks choose the
next step. Boehm's own *Difficulties* section says it suits **internal** development and needs
further work for **contract acquisition**, the opposite of what most people guess, so use it **where
you control the commitment points**.

In practice nobody runs one row: a 1996 acquisition guidebook already reported that *"most programs
use a combination of all three"* {% cite stsc1996lifecycles %}.

→ [Waterfall](../proc/lifecycles/waterfall.html) · [V-Model](../proc/lifecycles/vmodel.html) ·
[Incremental](../proc/lifecycles/incremental.html) · [Iterative](../proc/lifecycles/iterative.html) ·
[Prototyping](../proc/lifecycles/prototyping.html) · [Spiral](../proc/lifecycles/spiral.html)

## 6. Choosing one — and what the evidence does not say

Start from a **question, not a list**: what kind of software is this — a back-end component, a
service to an end user, or a visual interface {% cite ruparelia_software_2010 %}? Then the criteria
that move the answer: **stakeholders** (expertise, commitment, availability), **the environment**
(business, market, legal), and **requirements certainty**. Stakeholder availability is the one most
often forgotten and most often decisive, because an iterative model with an absent customer is a
plan-driven model with extra meetings.

**Do not make the project fit the lifecycle.** *"The puritan approach of using a method, framework,
process, and so forth without tailoring it to fit the specific organization's business, technical,
and marketing context is naive at best"* {% cite lattanze2009architecting %}. Find the model that
fits, then tailor it. In a survey of practitioners only about **one process in five** came from a
planned improvement programme — the great majority emerged from experience on the ground
{% cite kuhrmann2019hybrid %}. Hybrids are not a failure of discipline; they are what the population
actually does.

{: .warning }
**No study in this material says which lifecycle wins.** What the sources establish is **vocabulary
and mechanism**, not performance, and the *"choose it when"* column is reasoned from what each model
*does*. Two things follow: **say which argument you chose the model on**, because the argument is the
only part that can be examined; and **treat "this lifecycle outperforms that one" as unsourced**
until someone shows you the comparison.

The thread tying the block together is **risk**, which has been choosing the process since 1970 in
five notations: Royce's *do it twice* (originality risk), Boehm's spiral (risk as the **driver**),
STSC 1996 (risk as an **axis** for choosing) {% cite stsc1996lifecycles %}, Cockburn (risk as
**criticality** — *"a more critical system… needs more publicly visible correctness in its
construction"*) {% cite cockburn_selecting_2000 %}, and Boehm and Turner (risk as a **selector
between method families**) {% cite boehm_using_2003 %}. One question in five costumes: **what could
go wrong here, and which process is built to catch that?**

→ [Lifecycles](../proc/lifecycles/index.html) ·
[Balancing agility and discipline](../proc/frameworks/balance.html)

## Where this goes next

**L2b** makes the last row of that lineage its whole subject: the named frameworks — Scrum, XP,
Kanban, RUP, SAFe — and Boehm and Turner's five discriminators. See [SN L2b](sn2b.html).

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
