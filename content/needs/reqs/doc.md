---
parent: Requirements
title: Documenting requirements
nav_order: 5
layout: default
---

# Documenting Requirements

A requirements document records the agreement about what will be built, in a form that can be
reviewed, tested against and traced. Which document depends on who must act on it: a contract, a
specification and a backlog item answer different questions.

## 1. The artefacts, and what each one is for

| Artefact | What it settles | Example |
|---|---|---|
| **Statement of work** | Who does what, by when, for what payment, and how change is authorised | *"Vendor delivers the prototype by 30 June; customer reviews by 14 July; payment 30% at prototype, 50% at beta, 20% on final acceptance."* |
| **Requirements specification** | The properties the product must exhibit, with constraints and interfaces | *"Search returns results within 200 ms at the 95th percentile over a 10-million-item catalogue."* |
| **Concept of operations** | How the system will be used in its real environment | *"Students access the system from school devices between 08:00 and 16:00; on network loss it degrades to read-only cached mode."* |
| **Acceptance criteria** | What "done" means for one feature | *"The reset link expires in 30 minutes, is served over HTTPS, and the user is notified of a successful reset."* |
| **Epics and user stories** | A unit of work, and a promise to talk | *"As a registered user, I want to reset my password by email link so that I can regain access."* |

## 2. A story card is deliberately thin

A user story has *"three components: Cards (their physical medium), Conversation (the discussion
surrounding them), and Confirmation (tests that verify them)"* {% cite jeffries_essential_2001 %}.
The card is a token for the conversation, not a substitute — Wake calls the story a **pidgin
language**, the reduced vocabulary in which a customer and a programmer can agree enough to work
{% cite wake_invest_2003 %}.

**INVEST** is the usual check: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable,
**S**mall, **T**estable. *Testable* carries the most teaching: *"writing a story card carries an
implicit promise: 'I understand what I want well enough that I could write a test for it.'"* Ask the
customer how they would test the story; if they cannot say, you have learned something.

Two of Wake's own boundaries are worth knowing. **Independence does not fully hold** — price the
first report at 3 points and each subsequent one at 1, and the estimate depends on build order. And
INVEST says nothing about the *set*: six perfect cards can still duplicate each other and leave a
gap.

## 3. Six properties of a card, four of a backlog

The Quality User Story framework closes that gap with thirteen criteria in three dimensions —
syntactic, semantic and pragmatic {% cite lucassen2016qus %}. The split that matters is not the
three dimensions but **where each criterion can be checked**:

- **On one card:** well-formed, atomic, minimal, conceptually sound, **problem-oriented** (*"only
  specifies the problem, not the solution to it"*), unambiguous, full sentence, estimatable.
- **Only across the backlog:** unique, conflict-free, uniform, complete.

That is the same statement-level/document-level split that [requirement statements](stmts) makes for
an SRS, reached independently from the agile side. The most common substantive defect is
*problem-oriented* failing — a story that specifies the solution.

## 4. Slice vertically, and gate on readiness

Splitting a story means cutting **vertically through the layers** — network, persistence, logic,
presentation — so the customer gets *"the essence of the whole cake"* {% cite wake_invest_2003 %}. A
sprint that finishes "the database" and demos nothing has sliced horizontally.

Acceptance criteria are where the agreement becomes checkable, usually in **Given–When–Then** form
{% cite cucumber_gherkin_2025 %}. For example, *given I am logged in, when I click Save, then the
item appears in my wishlist.* And a **Definition of Ready** gates entry to a sprint as a Definition
of Done gates exit {% cite rubin2012needs %} — business goal, expected outcome, enough detail to
estimate.

Non-functional requirements are what agile documentation most often loses, since they belong to no
single story {% cite behutiye2017nfr %}. They need a home chosen deliberately — a definition of done,
a quality scenario, or a document.

## 5. What documentation does not do

A document records an agreement; it does not create one. Thirteen perfectly-formed user stories can
describe the wrong product — the criteria above are **intrinsic to the text** and say nothing about
whether the thing is worth building. That question belongs to [elicitation](elicitation) and
[validation](eng).

## How solid is this?

- **Where it comes from.** Two practitioner articles that contributed the 3Cs and INVEST and report
  no study, one empirical paper covering **1,023 user stories from 18 companies**, and a
  practitioner textbook.
- **What is contested.** Nothing tests whether user stories produce better outcomes than a
  specification; the defensible position is that the *form* should not be discernible downstream.
- **What we do not hold.** The user-story corpus is 17 Dutch vendors and one Brazilian — a narrow
  base for claims about processing English-language requirements.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
