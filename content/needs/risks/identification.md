---
parent: Risks
title: Identification
nav_order: 1
layout: default
---

# Risk Identification

Risk identification is finding risks while there is still time to act — *"you can't manage what you
don't know about"* {% cite carr1993taxonomy %}. Most of what you are missing is already known to
someone on the project who has not been asked.

## 1. What identification can and cannot reach

Three bands, and naming them tells you what to expect from the effort
{% cite carr1993taxonomy %}:

- **Known** — risks *"one or more project personnel are aware of — if not explicitly as risks, at
  least as concerns."* The job is to get them onto one list.
- **Unknown** — risks that *"would be surfaced… if project personnel were given the right
  opportunity, cues, and information."* **This is the target of every structured method.**
- **Unknowable** — risks *"even in principle, none could foresee"*, and *"beyond the purview of any
  risk identification method."*

One caution belongs with them: *"no overall judgment can be made about the success or failure of a
project based solely on the number or nature of risks uncovered."* **A long register is not a failing
project**, and believing otherwise keeps risks off the list.

## 2. The barrier is the reporting line, not the technique

Across 15 field tests in 11 organisations, the SEI found something managers did not expect:

> Even in organizations where staff across the project hierarchy felt that they had open and honest
> communications, the presence of a reporting relationship in an interview group **always** had an
> inhibiting effect on the subordinates.

Teams that *believed* they communicated openly went quiet when a supervisor was present. So the
peer-group rule is engineering, not etiquette: interview groups of **three to five peers with no
supervisor**, four groups per project, one unattributed copy of the findings to the project manager
— and in the SEI's evaluation method, the flipcharts and numbering maps are **destroyed at closure**
{% cite williams1999sre %}. *"Confidentiality and non-attribution are non-negotiable issues."*

That method also supplies a quality gate no other source offers: a 2.5-hour peer interview should
produce **15 to 40 risk statements**, and fewer than 15 means the session is run again.

## 3. Three techniques, which fail in different places

**A taxonomy sweep buys coverage.** The SEI taxonomy is three classes — product engineering,
development environment, program constraints — with 13 elements and 64 attributes. Its value is that
somebody is forced to ask about the environment and the externals, not only about the product. The
questionnaire is deliberately semi-structured: a fully structured interview yields more comparable
and **less valid** data. For example, under *design → performance* it asks *"are there any problems
with performance?"*, offers six cues only after people have answered freely, then probes on a "no".
The question is a door, not a datum.

**A premortem buys the objection nobody will voice** {% cite klein2007premortem %}: *"team members
assume that the project they are planning has just failed—as so many do—and then generate plausible
reasons for its demise."* Four steps — declare the failure, write privately, read round-robin,
revise the plan. Its mechanism is social: raising an objection at a kickoff looks disloyal, and
inside a premortem it is the assigned task.

**A picture of success buys the boundary.** Ask *when will it be, what will it be, what makes it a
success* **before** any risk talk {% cite williams1999sre %} — because *"if I am focused on arriving
safely at my destination tomorrow, my list of risks will be completely different from the list I
would define if I were focused on successfully raising a family."* See
[threshold of success](../exp/tos).

The cheapest sweep of all is a checklist. Boehm's top-10, from a survey of experienced project
managers, still starts where a software team least expects: **personnel shortfalls at number one**,
ahead of every technical item {% cite boehm1991risk %}.

## 4. Shrinking the list

Identification is cheap and analysis is not — affinity grouping yields **more than a hundred
candidate ideas in 30 to 35 minutes** {% cite dorofee1996crm %}. Consolidate statements into **7 to
11 risk areas** sharing a mitigation strategy, then ask of each pair whether one area's conditions
drive another's. Areas with many outgoing arrows are the **drivers**, and those are what you mitigate
{% cite williams1999sre %}.

## How solid is this?

- **Where it comes from.** Two SEI technical reports and a method description reporting operating
  experience across more than 50 organisations. The field tests are evolutionary development, not a
  controlled study: the instrument changed between them.
- **What is contested.** The checklist tradition's provenance — earlier risk research *"relied on
  descriptions of good practice observed by the researchers"* {% cite schmidt2001delphi %}, so
  compare Boehm's list and the SEI taxonomy rather than merging them.
- **What we do not hold.** No source here shows that a structured method finds more risks than an
  unstructured one, and the one number attached to the premortem is third-hand.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
