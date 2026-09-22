---
parent: Requirements
title: Elicitation
nav_order: 2
layout: default
---

# Elicitation

Elicitation is *"the process of identifying needs and bridging the disparities among the involved
communities for the purpose of defining and distilling requirements"* {% cite christel1992elicitation %}.
It is a **bridging** activity, not a collecting one — hence *elicitation*, not *capture*.

Brooks gives the reason it is hard, and it is not the analyst's fault
{% cite brooks1987silverbullet %}: *"the clients do not know what they want… they almost never have
thought of the problem in the detail that must be specified."* Elicitation is therefore not a phase
before the work; it is the work.

## 1. Three classes of problem, and they fail differently

Christel and Kang group elicitation problems into **scope**, **understanding** and **volatility**,
then classify ten published problems into those three. **Seven of the ten are problems of
understanding.** Two are scope; one is volatility.

Each class has a different repair:

- **Scope** — the requirements address too much or too little. Go back to the system boundary.
- **Understanding** — users do not fully know their needs, misjudge what computers can do, and speak
  a different language from the analysts; "obvious" information goes unsaid. Get a glossary, a
  prototype, or someone who will ask the obvious question.
- **Volatility** — requirements change. See [change control](more).

*"Our requirements are a mess"* says nothing; naming the class says what to do next.

## 2. Why understanding fails: assumptions nobody knows they hold

*"Among experts, a common disease is the presence of unstated assumptions. Because they are
unstated, no one seems to notice them"* {% cite berry_importance_1995 %}. The assumption is invisible
**because it is shared widely enough that nobody notices it is an assumption**.

For example, hardware engineers building an Ethernet switching hub spent four months failing to
produce a requirements document. They knew the technology thoroughly; the blocker was that *"they
were all using the same vocabulary in slightly different ways."* An analyst who knew nothing about
Ethernet resolved it in six hours.

## 3. What the evidence says about technique choice

A systematic review of 30 empirical studies supports three narrow statements
{% cite dieste2011elicitation %}:

1. **Interview by default** — the most effective of all techniques tested, though not always the
   most efficient.
2. **Write the questions first** — structured interviews produce more customer needs than
   unstructured ones.
3. **Avoid protocol analysis**; it came last on all three measures.

Then the result that reorders the topic: when respondents do not know the domain, *"it is unimportant
which elicitation technique is used."* The first question is not *which technique* but **have I got
the right people in the room**.

{: .warning }
**The best-evidenced family and the most-used family are not the same family.** The review
deliberately excluded group techniques, while a practitioner study found **83% of projects using
group interaction** — and only 2 of 20 using it alone {% cite palomares2021elicitation %}. There is
no technique ranking to memorise.

## 4. What actually goes wrong, ranked

A survey of **228 organisations across 10 countries** names the top three problems: **incomplete or
hidden requirements** (109), **communication flaws with the customer** (93) and **moving targets**
(76) {% cite mendez2017napire %}. None is a technique problem.

**Frequency and damage rank differently.** Communication flaws are cited less often than incomplete
requirements but blamed for failure more often — 48% of citations against 39% — and moving targets
convert at 51%. The most common problem is not the one that kills projects.

## 5. Two moves that work whatever technique you chose

**Run a type check on what people say** {% cite berry_importance_1995 %}. Read an imperative
sentence as a procedure call — verb as procedure, objects as arguments. *"Archive the record."*
*"Archive the record to the vault."* *"Archive the record for the auditor."* When the same verb takes
different arguments from different speakers, something is wrong. **You need no domain knowledge for
this check**, which is why an outsider can run it.

Hence a staffing rule: every requirements team wants *"at least one domain expert and at least one
smart ignoramus"*. Failing that, build a **glossary** with all stakeholders first, and treat every
disagreement about a definition as a finding.

**Build the model first and let its holes drive the interview** {% cite fricker2006tarpit %}: *"gaps
in knowledge and understanding became evident by the missing parts of the model."* Interviewing
first and modelling after tells you nothing about what you forgot to ask.

## How solid is this?

- **Where it comes from.** One systematic review (30 studies, search closed 2005, mostly student
  experiments), two practitioner surveys, and two experience reports.
- **What is contested.** The review's section text and its own code table disagree about which
  interview type is labelled structured, so only the narrower claim above is safe. Its authors bound
  their results to experienced participants.
- **What we do not hold.** No measured effect for the type check, the glossary or the model-first
  approach — two projects and one case study, whose authors report the method did not transfer.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
