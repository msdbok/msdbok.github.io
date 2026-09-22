---
parent: Requirements
title: Stakeholders
nav_order: 1
layout: default
---

# Stakeholders

*"A stakeholder is a person or organization who influences a system's requirements or who is
impacted by that system"* {% cite glinz2007stakeholders %}. Note what the definition does **not**
require: a stakeholder need not use the system, pay for it, or want it to exist.

Stakeholder identification comes first, and the source says so plainly: *"stakeholder identification
precedes any other RE activity: we must first determine who they are and how important they are."*

## 1. Seven categories to scan

The two that a wish-gathering exercise never produces are the last two.

1. People with an active interest in the system.
2. People who will **operate or maintain** it after deployment.
3. People who develop it.
4. People responsible for the **business process** it supports.
5. People with a financial interest.
6. **Regulators** — legal, safety, standards, audit.
7. People who are **negatively affected** by it.

## 2. The onion: draw the missing people rather than forgetting them

Alexander and Robertson model stakeholders as four rings around the thing being built
{% cite alexander2004onion %}: **the kit** (the product itself), **our system** (the kit *plus* the
people who operate, maintain and deliver its results, and the rules they work to), **the containing
system** (plus beneficiaries who never touch it), and **the wider environment**.

The ring that does the work is *our system* versus *the kit*, and the authors make the case in one
sentence: *"even an automatic product such as a missile only works when people test, install, and
launch it."*

The mechanism that makes the model useful is the **slot**. A slot is a generalised role; a filled
slot is drawn solid, an unfilled one greyed out. **An empty slot is a finding; a missing person is
just invisible.** A model with 11 slots, 5 roles filled and 7 empty tells you where the next
conversation goes. It also exposes slots that are wrong rather than merely empty. For example, one
model showed two departments each believing they held purchasing authority; another hid workplace
safety, airworthiness certification and radio regulation inside one generic *regulator* slot.

## 3. Prioritise on the risk of neglect, not on seniority

Once the roles exist, rank them by what happens if you ignore them
{% cite glinz2007stakeholders %}: **critical** — neglect might kill the project or render the system
useless; **major** — significant negative impact; **minor** — marginal. Then, and only then, pick
the individuals who will represent each role.

The order matters because the loudest stakeholder is rarely the one whose neglect is most expensive.

## 4. Finding them is the easy part

This is the finding that reframes the topic. Asked to name the *single* stakeholder concern causing
the biggest problem in their own work, **541 practitioners** answered
{% cite alexander2004onion %}:

| Concern | Responses |
|---|---|
| **Skill** — stakeholders cannot take part usefully; they describe solutions, and change their minds | **208 (38%)** |
| **Commitment** — people with authority will not commit time or budget | **186 (34%)** |
| Discovery — we cannot find the appropriate stakeholders | 72 (13%) |
| Maintaining the stakeholder set | 48 (9%) |
| Other | 27 (5%) |

Discovery came **fourth**. Together, skill and commitment account for **72%**. The hard part is not
locating people; it is getting the people you located to engage usefully — which is what
[elicitation](elicitation) and [customer involvement](../exp/involvement) are about.

## 5. The model rots, and here is how you notice

A stakeholder model is not a one-off exercise. Four indicators say it needs revisiting:
reorganisations and renamed departments; **hiring and firing** — *"when an occupant leaves a role,
he or she often forgets to inform the new role occupant of his or her stakeholder
responsibilities"*; boundary changes such as new functionality or a new law; and missing feedback
loops, because *"unless you can keep your project in the limelight, people lose interest."*

The consequence is stated flatly: *"missing stakeholders result in missing requirements and
escalating project costs."*

## How solid is this?

- **Where it comes from.** A three-page IEEE editorial supplying a definition and a prioritisation
  rule, and a practitioner article presenting the onion model with a survey. Both are method rather
  than measurement.
- **What is contested.** Nothing in the models themselves — but running two of them is recommended
  by their own authors, *"because people who have been using one model might overlook a role that
  the other model immediately suggests."*
- **What we do not hold.** The 541-response survey is a convenience sample gathered at 12
  requirements workshops and tutorials — people who chose to attend a requirements session, and so
  the group most likely to name requirements problems as their biggest concern.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
