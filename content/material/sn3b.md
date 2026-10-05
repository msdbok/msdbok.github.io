---
parent: Study Notes
title: SN L3b — Requirements Engineering
nav_order: 7
page_type: study-notes
layout: default
---

# SN L3b — Requirements Engineering

A revision summary of the second Needs lecture. The lecture follows one invented product, **Quill**,
a word processor sold to a publishing house and used by editors, students and lawyers, and one
sentence its customer said: *"Quill must be intuitively easy to use, and it must handle big
documents."* Six parts take that sentence from a wish to requirements a tester can check. Each
section links to the handbook page carrying the detail and the sources.

## 1. What a requirement is

Customers cannot simply tell you what they need {% cite brooks1987silverbullet %}: *"the clients do
not know what they want. They usually do not know what questions must be answered, and they almost
never have thought of the problem in the detail that must be specified."* That is a description of
the job, not a complaint. The customer knows the problem; finding the requirements is your skill.

A requirement is **"a property that must be exhibited to solve a real-world problem"**
{% cite swebok2024v4 %}. A good one rules out most designs and still leaves the designer a choice.
*"The interface shall be user-friendly"* rules out nothing. *"The system shall use a mouse-driven
window environment"* chooses one design, when the problem was ease of use.

There are three kinds, and a requirement set needs all three.

| Kind | Answers | Quill example | Quick test |
|---|---|---|---|
| **Functional** | What does it do? | Quill shall export a document as PDF | Does the system do something new? |
| **Quality** | How well does it do it? | Quill shall open a 500-page document within 2 seconds | Can you measure how well? |
| **Constraint** | What is already decided? | Quill shall store documents in the customer's EU data centre | Was the decision made outside the team? |

The old rule, *what the system does is functional and how it behaves is non-functional*, changes
its answer when a sentence is reworded {% cite glinz2007nfr %}. Classify by asking **why the
requirement was stated**, stopping at the first yes: behaviour or data, functional; time, speed or
volume, performance; a particular quality, quality; anything else, a constraint.

Wiegers gives ten properties of a good requirement, and the split matters more than the list
{% cite wiegers1999quality %}. Six can be checked on one sentence as you write it: correct,
feasible, necessary, prioritised, unambiguous, verifiable. Four exist only for the whole set and need
a reviewer: complete, consistent, modifiable, traceable. Words to avoid: *user-friendly, easy,
simple, rapid, efficient, several, state-of-the-art, improved, maximize, minimize*.

→ [Requirements engineering](../needs/reqs/eng) · [Requirement statements](../needs/reqs/stmts)

## 2. Finding out what people need

Christel and Kang sort the ten classic elicitation problems into scope, understanding and
volatility, and **seven of the ten are misunderstandings** {% cite christel1992elicitation %}. A
stricter template fixes scope problems and does nothing for the seven.

<img src="/images/elicitation-problems.svg" alt="Ten elicitation problems sorted into scope, understanding and volatility" style="max-width:100%; margin:1.5em 0;" />

Six techniques cover most situations, and the choice follows from who you can reach and what kind
of knowledge you need {% cite swebok2024v4 %}. **Interview** when you can reach the people, and
prepare the questions: *"show me the last document that was too big"*, not *"what do you need"*.
**Workshop** when several groups must agree. **Observe** when people cannot describe their own
work; watch a lawyer edit a contract for an hour. **Prototype** when people do not know what they
want until they see it; a paper mock-up gets you *"no, not like that"*. **Study documents** when an
old system or a competitor exists. **Questionnaire** when there are many users and few questions.
In controlled studies, interviews worked best and prepared questions beat improvised ones
{% cite dieste2011elicitation %}.

Two moves work whatever technique you chose {% cite berry_importance_1995 %}. **Check every
verb**: *"Quill shall save the document"* hides three systems, because *save* could mean locally or
in the cloud, on command or after every change, the file or a new version. **Draw a model before
you ask**, and let every hole in the drawing become a question. A network-switch specification that
had taken four months was written in six hours by an outsider who drew the model and asked.

The stakeholder onion returns from the previous lecture: **every empty slot is a group whose
requirements you have not collected** {% cite alexander2004onion %}. For Quill the publisher spoke;
the students, the lawyers and the support desk did not. And ask who a requirement came from.
*"Intuitively easy to use"* came from a product manager, not a user, and in one industrial study real
end-users took part in two projects out of twenty-four {% cite palomares2021elicitation %}. Each
hand-over is a translation, and translations lose things.

→ [Elicitation](../needs/reqs/elicitation) · [Stakeholders](../needs/reqs/stakeholders)

## 3. Writing a requirement you can test

A quality attribute is not a second list beside the functions. It **attaches to a function and
says how well that function must work**: nonfunctional requirements are *"the manner in which the
functional requirements must be achieved"* {% cite tsui2013essentials %}. *Open a document*: 500
pages within 2 seconds. *Save a document*: losing at most ten seconds of typing. *"Quill shall be
reliable"*, standing alone, belongs to nothing and tests nothing.

*"Quill must handle big documents"* is true and not finished: how big, on what machine, doing what,
how fast? The repair is not to rewrite it more carefully but to put it in a **quality-attribute
scenario** with four slots {% cite barbacci2003qaw %}: stimulus, environment, response, response
measure. For example, *a user opens a 500-page document; on a laptop in battery-saver mode; the
first page is displayed; within 2 seconds.* The fourth slot is the one teams skip, and the only one a tester can
act on.

<img src="/images/qa-scenario.svg" alt="A quality-attribute scenario in four slots" style="max-width:100%; margin:1.5em 0;" />

Write every requirement in the same shape {% cite iso2018req %}: **[condition] the [subject] shall
[action] the [object] [constraint]**. *When a document of up to 500 pages is opened on battery-saver
mode, Quill shall display the first page within 2 seconds.* One requirement per sentence, always
*shall*, never *and/or* {% cite wiegers1999quality %}. A fixed shape makes a missing slot visible.

Then the rewrite the lecture promised. *"Intuitively easy to use"* becomes three numbers: 90% of
new users complete the five basic editing tasks within two weeks unaided; fewer than 2% of editing
operations end in an error; at least 85% of users rate Quill 4 or 5 on the satisfaction survey. The
numbers force a conversation about what *easy* means for this product, and the customer may say
*"no, I meant something else"*. Good; now you know. The thirty-second test for any requirement:
**could you write the test case?** If not, there is an adjective where a number should be.

Keep **validation** and **verification** apart: validation asks the stakeholders whether this is the
right system; verification asks the build whether it matches the specification. And design every
review so it can say no. Validation *"should devise experiments to attempt to refute the current
statement of requirements"* {% cite nuseibeh2000roadmap %}. A review where everyone nods produced no
information; bring a prototype or a user.

→ [Requirement statements](../needs/reqs/stmts) · [Methods](../needs/reqs/methods)

## 4. The process and the document

The five activities, elicit, model and analyse, communicate, agree, evolve, form a **cycle, not a
pipeline** {% cite nuseibeh2000roadmap %}, and a team does four of them in the same week. The
document that comes out has a standard shape {% cite iso2018req %}: purpose and scope; stakeholders
and users; functional requirements, in the sentence shape; quality requirements, as scenarios;
constraints and interfaces; verification, how each requirement will be checked; and a glossary of
the customer's words. Schedule, cost and team go in the plan, not here. An empty section is a
question you have not asked yet.

The agile form of a requirement is the user story: **As a** role, **I want** goal, **so that**
benefit {% cite cohn2004stories %}. *As a law student, I want to insert a citation from my reference
list, so that I never type one by hand.* The card is deliberately thin. The requirement lives in the
conversation and in the confirmation, and a good story is **INVEST**: independent, negotiable,
valuable, estimable, small, testable {% cite wake_invest_2003 %}.

The confirmation is an acceptance criterion in **Given–When–Then** form {% cite north2006bdd %}.
*Given a document is open and the reference list has at least one entry, when the user chooses
Insert citation and picks an entry, then the citation appears at the cursor in the document's
citation style and the entry is added to the bibliography.* One criterion per behaviour, concrete
values, written before the code. A story with no Given–When–Then is one nobody can finish.

A **Definition of Ready** gates a story into the sprint and a **Definition of Done** gates it out
{% cite hoda2011customer %}. Ready is the requirements review, run one story at a time. For a
large set, **group before you rank**: sort cards into piles, name the piles last, turn them into a
tree, and read the tree for gaps. Then vote, and rank by the cost of getting it wrong rather than by
how much anyone wants it {% cite root2014lectures %}.

→ [Organising requirements](../needs/reqs/org) · [Documenting requirements](../needs/reqs/doc)

## 5. Requirements change

Quill's invented history runs from typing, saving and printing, through spell check and tables, to
tracked changes, comments, cloud sync and citations. None of those was a requirement on the first
day. The real number behind it: commercial word processors grew from **under 300 to over 5,000
function points** in ten years {% cite jones1996creep %}. Using software teaches people what to ask
for. That is the product succeeding, not the requirements failing, so plan for change instead of
treating it as a defect.

Handle every change in five steps. **Record** it with its type (added, deleted, modified), its
reason and its origin {% cite nurmuliani2004volatility %}. **Assess the impact**: effort, what it
displaces, which requirements and tests it touches. **Decide**: the requestor decides, knowing the
price. **Update** the document and the traces. **Tell** everyone affected. A late change costs more,
so it must be worth more {% cite kelly2004change %}: the door does not close, the price goes up.

**Traceability runs both ways.** Forward tells you which test and which code satisfy a requirement.
Backward tells you which need a piece of code exists for, which is the direction teams skip and the
one that says what is safe to delete. Set a last date for new ideas at the start, after which every
change needs an impact statement and a decision.

→ [Validation, traceability and change](../needs/reqs/more)

## 6. Requirements with AI tools

A language model is good at text tasks and knows nothing about your system. Use it to **draft** a
first set from interview notes, **reformat** requirements into the sentence shape, and **flag** vague
words; in one study *"considerable amounts of traffic"* became *"up to 10,000 concurrent users"*
{% cite krishna2024llmsrs %}. In the same study a model asked to *improve* a performance requirement
raised the response-time threshold and said nothing about it. Read every output against the
original {% cite arora2024llmre %}; the failure mode is a fluent, confident, wrong sentence.

The argument underneath matters more than either list. A developer reading an ambiguous requirement
asks which reading you meant. A model picks one and writes the code: *"AI does not eliminate
ambiguity; it transforms ambiguity into executable behavior"* {% cite sirqueira2026specparadox %}.
A prompt steers one conversation; a specification must stay consistent, verifiable and traceable
for the life of the system. The better the model gets at writing code, the more your specification
decides whether the code is right. This is a position paper's argument, not a measured effect.

→ [Requirements with LLMs](../needs/reqs/ai)

## Where this goes next

Everything here is about things you know you need. The next lecture turns to what might go wrong: a
key developer leaving, a late compliance review, a vendor missing a date. None of those is a
requirement, and any of them can end the project.

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
