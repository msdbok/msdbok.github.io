---
parent: Revision Questions
title: RQ3
nav_order: 3
page_type: question-set
layout: default
---

# RQ 3 — Needs: Expectations, Requirements and Risks

Covers **L3a** (how a customer judges you, what counts as success, whose expectations they are,
educating the customer, involving them, when it goes wrong), **L3b** (what a requirement is,
elicitation, writing one so it can be checked, the process and the document, change, and
requirements with LLMs, plus the PBJ exercise) and **L3c** (what risk management is, finding risks,
writing one down, deciding which matter, doing something about them, and the Comair case).
Summaries at [SN L3a](sn3a.html), [SN L3b](sn3b.html) and [SN L3c](sn3c.html); the detail is in the
[Needs](../needs/) area.

Answer each in a short paragraph: state your claim first, then the reasoning or the evidence, then a
concrete software example where one is asked for.

---

## 1. Lecture Questions — L3a

### 1.1 How a customer judges you

1. Explain *customer perception = project performance ÷ expectations*. Which half of the ratio can a project manager move more cheaply, and why?
2. Two customers receive the same three-second response time and give opposite verdicts. What did the project do differently for each?
3. The zone of tolerance moves from the bottom. What does that mean for the levers a manager holds?
4. Why is an explained outage treated differently from an unexplained one, and what does that make a postmortem?
5. A team delivered every requirement and the customer is unimpressed. Use Kano's classes to explain how that happens, and give a software example of each class.
6. Why does a Kano classification belong to a customer segment rather than to a feature, and why does it have a half-life?

### 1.2 What counts as success

1. The same projects are 36% successful under one CHAOS definition and 29% under another. What should you ask before you believe any failure rate?
2. Why does the Conditions of Satisfaction loop stop only when neither side corrects the other?
3. "If two honest people can disagree about whether you met it, it is not a criterion." Rewrite a vague success criterion from a project you know so that it passes this test.
4. Why is a threshold of success written as failure statements first and then inverted, rather than as goals?

### 1.3 Whose expectations are they?

1. Why is an empty slot in the stakeholder onion a finding, when a missing person is merely invisible?
2. Practitioners put stakeholder skill and commitment ahead of finding stakeholders. What does that change about where you spend elicitation effort?
3. A survey reports 82% of customers satisfied. Why is the useful reading "52% are up for grabs"?

### 1.4 Educating the customer

1. Explain the relation of the expectation space — Hoover's quadrant — to expectation management. Which side controls which axes?
2. Why does a customer who cannot see relative cost ask for the impossible, and mean it?
3. Two changes, both "must have", cost half a day and six staff months. How did stating the costs settle the argument without a negotiation?
4. What goes on a simplifier and complicator list, and which half do teams forget to write?
5. A prototype turned a $100M requirement into a $30M one. What made the prototype more persuasive than two years of specification?

### 1.5 Involving them

1. Involvement usually helps and sometimes makes things worse. Turn that finding into the four decisions a manager must make.
2. Why is "we involved the users" not a checkable claim, and what would be?
3. Place a team you know on the continuum from on-site customer to extreme undercover. What does its position cost the team?
4. Why is showing the software better than reporting on it? Use the 40% prototype as your example.

### 1.6 When it goes wrong

1. Why should the customer hear bad news from you, and early? Connect your answer to the zone of tolerance.
2. How does a price list set expectations that no roadmap mentions?
3. Why is a change request the moment a customer learns what things cost?

---

## 2. Lecture Questions — L3b

### 2.1 What a requirement is

1. A requirement narrows the design space without picking a point in it. Give one requirement that narrows nothing and one that picks a point, and repair both.
2. The same security requirement, reworded, becomes functional. What does that tell you about the *what versus how* rule, and what do you ask instead?
3. Discuss the relation between functional requirements and quality attributes. Give an example.
4. Which of Wiegers's quality criteria can be checked on one sentence, which only on the whole set, and why does the split matter in a review?
5. Why is a specification template descended from IEEE 830 a citation problem even when its content is sound?

### 2.2 Getting them out of people's heads

1. Seven of the ten classic elicitation problems are problems of understanding. What does that rule out as a fix?
2. Why do structured interviews beat unstructured ones, and what do you prepare before one?
3. The most frequently cited requirements problem is not the one most blamed for failure. Which is which, and what should a manager do with the difference?
4. Real end users took part in 2 of 24 projects. What happens to a requirement each time it is relayed?
5. What did the PBJ exercise show about writing instructions for someone who shares none of your assumptions?

### 2.3 Writing one so it can be checked

1. Rewrite "the system shall be reliable" as a quality-attribute scenario. Which slot is the one teams skip?
2. What is the difference between verifying and validating requirements? Be specific, and say who you ask in each case.
3. Why must validation be able to fail, and what does a review where everyone nods tell you?

### 2.4 The process, and the document

1. Why are the five requirements-engineering activities a cycle and not a pipeline?
2. A story card is deliberately thin. Where does the requirement actually live, and what does the card promise?
3. Why group requirements before ranking them, and why rank on the cost of being wrong?

### 2.5 Requirements move

1. Word processors grew from 300 to 5,000 function points in a decade. Why is that not a requirements failure?
2. What three fields should a change log carry, and what does the *origin* field tell a manager?
3. "Late changes must be worth more." Explain the rule, and who should decide whether a late change is worth its price.

### 2.6 RE with LLMs

1. Where does a language model help with requirements work, and where did one make a requirement worse without saying so?
2. Explain the Specification Paradox. Why is a specification not a prompt?

---

## 3. Lecture Questions — L3c

### 3.1 What risk management is

1. Why is risk management a filter rather than a list?
2. Is a missing GDPR assessment, found mid-project, a risk or an issue? Split the situation into its entries and name the verb for each.
3. Which classification of risk — by what is threatened or by how much you know — tells you what a contingency reserve is for?
4. Paying $500,000 was the cheapest option. Explain the comparison, and answer a colleague who says the probabilities were made up.
5. Why is addressing risks at the third level of maturity still a lost schedule battle?
6. Name the steps of the SEI risk paradigm. Why is communication at the centre rather than a sixth step?

### 3.2 Finding them

1. Describe the role of the threshold of success in risk identification.
2. Why should the project manager not attend the risk identification session, and what does the SEI field study say about it?
3. Why does a premortem surface risks that an ordinary planning meeting does not?
4. What are the three classes of the SEI taxonomy for, and which ones does a team skip when left alone?
5. Boehm's number-one risk item is personnel shortfalls. Why might that surprise an engineer, and what does it change about a register?

### 3.3 Writing one down

1. Write a risk as condition and consequence, where the condition is something you could check this afternoon.
2. Why does the consequence need a number and a unit?
3. "If the team does not test properly, defects will escape." Why is that not a risk?
4. Sixty risks, five people. How do drivers and riders decide where the mitigation effort goes?

### 3.4 Deciding which ones matter

1. Why is a band without a threshold just a word? Use two scales that disagree.
2. Explain how the Pareto principle applies to risk management, with a software example.
3. A risk matrix painted the smallest expected loss red. What is the matrix good for, and what settles the order instead?
4. Half of IT projects land on budget and the average is 80% over. What does that mean for sizing contingency?

### 3.5 Doing something about it

1. Why do the bands on a response matrix run diagonally? Place one risk in each band and name its response.
2. Why is last week's rank the most important column on a top-ten list?
3. "Meetings do not burn down risks." What does, and why does work already in the plan not count?
4. A risk register's total exposure rose for two months. Good news or bad, and what shape is the real warning?
5. An agile team mitigated nothing for several iterations. What was wrong with how its risk work entered the backlog, and what does the fix cost?

### 3.6 The case

1. Write the register entry for Comair that nobody wrote in 1997, including how its probability changed over time.
2. The storm was the trigger. What was the cause, and whose risk was it?

---

## 4. Reading Questions

Cite the reading you used, with a page number where you have one.

### 4.1 Boehm, "The Art of Expectation Management" (2000)

1. Would Tom Bauer's response have been different if the client had no software-engineering knowledge? What might he have said instead, and which other client characteristics shape a response?
2. What were Boehm's priorities for his request, and how did Bauer's answer serve them?
3. Give an example from your own experience of managing a customer's expectations. Does it support Boehm's position?

### 4.2 Heskett, Sasser & Wheeler, *Put Customers to Work*

1. Which software development activities suit customer involvement, which do not, and why?

### 4.3 Pressman, *Software Engineering* (7th ed., ch. 5–9; 8th ed., ch. 8–13)

1. What problems do you see in using Quality Function Deployment as Pressman defines it? Give specifics.

### 4.4 Christel & Kang, *Issues in Requirements Elicitation* (1992)

1. The report defines requirements engineering, its activities, its goal and elicitation. Are these definitions useful to a manager? Test one against a project you know.
2. Which of the elicitation problems it cites would hurt your current project most, and why?

### 4.5 Barbacci et al., *Quality Attribute Workshops* (2003)

1. How does the Christel and Kang report treat quality-attribute requirements, and does a QAW address any of the elicitation problems it identifies? If not, why not?

### 4.6 Fricker, Glinz & Kolb, "A Case Study on Overcoming the Requirements Tar Pit" (2006)

1. What key issues did the ABB team face, how were they addressed, why were those approaches chosen, and what was the net effect?

### 4.7 Wiegers, "In Search of Excellent Requirements" (1995)

1. Wiegers names customer involvement as the most critical factor in software quality. Argue for or against, with a software example.

### 4.8 Van Scoy, *Software Development Risk: Opportunity, Not Problem* (1992)

1. Van Scoy puts communication at the centre of the paradigm's steps. Which step does a team most often run badly, and what does that cost the others?
2. Why does Van Scoy frame risk as opportunity, and what would a team do differently if it believed him?

### 4.9 Will, *Software Risk Management*

1. Apply the Pareto principle to risk management with two original software examples, not the article's.
2. Do you agree with the "magical software development triangle"? Support your view.

### 4.10 Pressman, *Software Engineering* (7th ed., ch. 28; 8th ed., ch. 35)

1. How would you assess the true impact of a risk on a project as a whole? Give an example.

### 4.11 Taran, *How Successful Are You, If You Can't Define It?*

Answer from the [Threshold of Success](../needs/exp/tos) page if you do not have the paper.

1. What is the difference between a threshold of success and project goals, and why does the difference matter when you identify risks?

---

### Acknowledgments

These questions build on the Fall 2025 study-notes selection and on lectures by Eduardo Miranda and
David Root; the expectation-space and threshold-of-success questions draw on the work of Carol
Hoover and Gil Taran.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
