---
parent: Study Notes
title: SN L3b — Requirements Engineering
nav_order: 7
page_type: study-notes
layout: default
---

# SN L3b — Requirements Engineering

A revision summary of the second Needs lecture. L3a ended on a customer saying the system must be
*"intuitively easy to use"*; this lecture is about writing that down. Two things stand in the way:
people cannot tell you what they need, and the words they do use will not survive contact with a
test case. Each section links to the handbook page carrying the detail and the sources.

## 1. What a requirement is

Start with the sentence students find uncomfortable {% cite brooks1987silverbullet %}:

> "For the truth is, the clients do not know what they want. They usually do not know what
> questions must be answered, and they almost never have thought of the problem in the detail that
> must be specified."

That is not a complaint about customers; it is a description of the task, and it is why elicitation
is a skill rather than a form. If a requirement ever does arrive fully formed, somebody has already
made your design decisions for you.

A requirement is **"a property that must be exhibited to solve a real-world problem"**
{% cite swebok2024v4 %}. The useful way to hold it: a requirement **narrows the design space
without picking a point in it**. *"The interface shall be user-friendly"* narrows nothing — every
design satisfies it. *"The system shall use a mouse-driven window environment"* picks a point, when
the actual problem was ease of use. Keep **product** requirements (what the system must do or be)
apart from **project** requirements (how the work is run): the first go in the specification, the
second in the plan.

Do not trust the old *what versus how* rule for sorting functional from non-functional. Glinz shows
one security requirement written three ways, and the third — *"the database shall grant access only
to those users authorized by user name and password"* — comes out **functional** while remaining a
security requirement {% cite glinz2007nfr %}. His conclusion is the thing to remember: *"the kind
of a requirement depends on the way we represent it."* So ask **why it was stated**, stopping at the
first yes: behaviour or data → functional; timing or volume → performance; a specific quality →
quality; anything else → constraint.

Wiegers gives ten quality criteria, and the split matters more than the list
{% cite wiegers1999quality %}. **Six you can check on a single sentence** — correct, feasible,
necessary, prioritized, unambiguous, verifiable. **Four only on the whole set** — complete,
consistent, modifiable, traceable. Words to ban outright: *user-friendly, easy, simple, rapid,
efficient, several, state-of-the-art, improved, maximize, minimize.*

One piece of hygiene: almost every SRS template in circulation descends from **IEEE 830**, which was
**withdrawn in 2011**. Its substance is uncontroversial and survives in
**ISO/IEC/IEEE 29148:2018**; its status does not. Cite 29148 {% cite iso2018req %}.

→ [Requirements engineering](../needs/reqs/eng) · [Requirement statements](../needs/reqs/stmts)

## 2. Getting them out of people's heads

Christel and Kang sort the ten classic elicitation problems into three classes — scope,
understanding, volatility — and **seven of the ten are problems of understanding**
{% cite christel1992elicitation %}. That is the finding that redirects effort: understanding
problems are not fixed by a better form or a longer template.

<img src="/images/elicitation-problems.svg" alt="Ten elicitation problems sorted into scope, understanding and volatility" style="max-width:100%; margin:1.5em 0;" />

On technique, the evidence supports a short list {% cite dieste2011elicitation %}: **interviews beat
the alternatives tested**, and **structured beats unstructured** — so write the questions in
advance. Thinking-aloud protocol analysis performed worst. Two moves work whatever technique you
chose. **Check the verb**: *spread the butter*, *spread the butter on the bread*, *spread the bread
with the butter* are three different argument lists behind one word, and only one is what they meant
{% cite berry_importance_1995 %}. **Model first, then let the gaps ask the questions** — the
structure produces questions you would never have thought to ask.

Two numbers about where requirements actually come from. Practitioners in 228 organisations across
10 countries cite **incomplete or hidden requirements** most often (109 times), but
**communication flaws with the customer** are cited less (93) and blamed for failure *more*
{% cite mendez2017napire %} — frequency is not damage. And in a study of industrial projects,
**real end-users took part in 2 of 24**, with **21% having no external stakeholder at all**
{% cite palomares2021elicitation %}. Sales, account and product managers stand in, and every relay
is a translation. Before trusting a requirement, ask who it came from and how many people it passed
through.

The onion model from L3a returns in requirements vocabulary: **every empty slot is a requirement
you have not collected** {% cite alexander2004onion %}.

→ [Elicitation](../needs/reqs/elicitation) · [Stakeholders](../needs/reqs/stakeholders)

## 3. Writing one so it can be checked

Quality attributes are not a second list running beside the functional one. They are **a relation to
it** — the manner in which the functional requirements must be achieved. *Produce the monthly
report* **within 5 seconds at peak**; *authenticate a user* **with fewer than 10⁻⁵ false grants**. A
floating *"the system shall be reliable"* attaches to nothing and tests nothing.

So the repair for a vague requirement is not to rewrite it more carefully. It is to put it in a
**quality-attribute scenario**, which has slots you can see are empty
{% cite barbacci2003qaw %}.

<img src="/images/qa-scenario.svg" alt="A quality-attribute scenario in four slots, with the five-second example" style="max-width:100%; margin:1.5em 0;" />

The fourth slot — the **response measure** — is the one teams skip, and it is the only one that
makes the sentence testable. For example, *"the product shall provide status messages at regular
intervals not less than every 60 seconds"* is ambiguous about whether 60 is a floor or a ceiling,
which messages, and displayed where. Repaired, it becomes *"display status messages in a designated
area of the user interface at intervals of 60 ± 10 seconds"* — and it splits into **four**
requirements, each needing its own test case {% cite wiegers1999quality %}.

**The thirty-second test for any requirement: could you write the test case?** If not, you have an
adjective where a number should be.

Keep **validation** and **verification** apart: validation asks the stakeholders whether this is the
right system; verification asks the build whether it matches the specification. And validation has
to be able to fail — it *"should devise experiments to attempt to refute the current statement of
requirements"* {% cite nuseibeh2000roadmap %}. A review where everyone nods produced no information.

→ [Requirement statements](../needs/reqs/stmts) · [Methods](../needs/reqs/methods)

## 4. The process, and the document

The five activities — elicit, model and analyse, communicate, agree, evolve — are **a cycle, not a
pipeline** {% cite nuseibeh2000roadmap %}. Three words that get used interchangeably and should not
be: a **process** is the shape of the work, a **technique** is one way to do a step, a **method**
packages techniques with a notation. And a **scenario is a particular path through a use case**,
which is why you can test a scenario and cannot test a use case.

In agile documentation, a story card is deliberately thin. The **three Cs** are Card, Conversation,
Confirmation, and the requirement actually lives in the conversation
{% cite jeffries_essential_2001 %}. Writing the card carries *"an implicit promise: 'I understand
what I want well enough that I could write a test for it.'"* Use **INVEST** —
independent, negotiable, valuable, estimable, small, testable — to check one
{% cite wake_invest_2003 %}. Note what did *not* disappear: the **Definition of Ready** is the
requirements completeness check, moved rather than abolished, and run one story at a time.

For a set of requirements, **group before you rank**. Sort cards into affinity piles and name the
piles afterwards — the names are the output, not the input — then turn piles into a hierarchy, and
read the shape for gaps. A branch with one leaf is a question. You cannot see what is missing from a
flat list of two hundred sentences; you can see it in a tree of twelve branches. Then rank **on the
cost of being wrong**, not on how much anyone wants it.

→ [Organising requirements](../needs/reqs/org) · [Documenting requirements](../needs/reqs/doc)

## 5. Requirements move, and most of the movement is not a mistake

Word processors grew from **under 300 function points to over 5,000** in a decade
{% cite jones1996creep %}. Bug fixing is **10–15%** of maintenance; enhancement is **over 60%**, and
roughly **40%** of that comes from users learning what the system could do. Using software teaches
people what to ask for — that is the system working, not the requirements failing.

Which is why a change log needs three fields, not one: **type** (added, deleted, modified),
**reason**, and **origin**. A study that examined the forms found two free defects: **no rationale
field**, so six months later nobody remembers why, and **no impact analysis**, so the cost was never
written down. Its volatility peaked at **16.85% at the end of requirements analysis** — the review
is where change gets *discovered*, not created {% cite nurmuliani2004volatility %}.

On late change, the honest position {% cite kelly2004change %}:

> "Changes that come along later are more disruptive but this doesn't imply they are valueless,
> only that they must be worth more if they are to be worthwhile implementing."

The door does not close; the **price goes up**, and the decision to pay it belongs to the requestor.
Finally, **traceability runs both ways**. Forward tells you what implements a requirement; backward
tells you which stakeholder need a piece of code exists for — the direction teams skip, and the one
that tells you what is safe to delete. Set a **"no more good ideas" date** at the start, because
without one there is always one more good idea.

→ [Validation, traceability and change](../needs/reqs/more)

## 6. Requirements engineering with LLMs

Where the tools help: **drafting** a first set from notes, **reformatting** to a template, and
**classifying or checking** an existing set — few-shot prompting beats zero-shot by roughly
**15–25%** on classification {% cite arora2024llmre %}. Where one hurt: asked to *improve* a
performance requirement, a model **raised the response-time threshold** and said nothing about it
{% cite krishna2024llmsrs %}. Read every corrected requirement against the original; the failure
mode is a confident, fluent, wrong sentence.

The argument underneath matters more than either list. A human reading an ambiguous requirement
notices and asks which reading you meant. A model picks one and ships it — *"AI does not eliminate
ambiguity; it transforms ambiguity into executable behavior"* {% cite sirqueira2026specparadox %}.
Two consequences get names worth carrying: **Specification Overfitting**, where generated code
satisfies your sentence precisely and misses the problem it was about; and **Specification Debt**,
which unlike technical debt bites *before* any code exists, because the specification is what the
generator reads.

And the distinction to take away: **a specification is not a prompt.** A prompt steers one
conversation; a specification must stay consistent, verifiable and traceable for the life of the
system. Hence the **Specification Paradox** — the better the model gets at writing code, the more
your specification decides whether that code is right. Treat this as an argument rather than a
measured effect: the source is an eight-page position paper, not a study.

→ [Requirements with LLMs](../needs/reqs/ai)

## Where this goes next

The **PBJ exercise** runs straight after this session, and it is where you find out how hard §3
actually is on something you have done a hundred times. **L3c** turns to what this lecture excluded:
a requirement is a statement about the system you are going to build, and your best developer
leaving, a late GDPR review or a vendor missing a date are none of them requirements — yet any of
them can end the project. All three Needs lectures are examined together in **Q3**.

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
