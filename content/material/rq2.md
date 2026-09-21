---
parent: Revision Questions
title: RQ2
nav_order: 2
page_type: question-set
layout: default
---

# RQ 2 — Processes: Defining, Measuring, Lifecycles and Frameworks

Covers **L2a** (defining a process, ETVX, measurement, the process/lifecycle/framework ladder, the
six lifecycle models, choosing one) and **L2b** (agile and its limits, XP, Scrum, Kanban, scaling,
the RUP family, choosing, and process under AI agents). Summaries at [SN L2a](sn2a.html) and
[SN L2b](sn2b.html); the detail is in the [Processes](../proc/) area.

Answer each in a short paragraph: state your claim first, then the reasoning or the evidence, then a
concrete software example where one is asked for.

---

## 1. Lecture Questions — L2a

### 1.1 Why define a process

1. Why is an error entered in a requirement *honoured* by every later stage rather than caught by one?
2. Why can a test suite pass completely while the wrong product is being built?
3. Why ask the people who do the work rather than their managers, and what differs between the two accounts?
4. Which step of Plan–Do–Check–Act do teams drop, and what two different questions hide behind "is the process working?"

### 1.2 ETVX

1. Define the four activities in the ETVX model.
2. Write an ETVX definition for proofreading a case-cracking presentation.
3. Why is **Exit** the part that changes behaviour, when Entry and Task are usually written down already?
4. Students read ETVX as a chain of gates. What does Radice say it constrains instead, and why does that let it sit under iterative work?
5. Oerlikon's estimation step exits on "a list of the alternatives considered". Why can that item not be produced retrospectively?

### 1.3 Measuring the process

1. State GQM's three levels and say why they are different in kind.
2. Why does naming the **object** — product, process or resource — expose a bad metric in seconds?
3. What are some potential drawbacks of using the Goal Question Metric approach?
4. Why does pointing a process metric at individuals stop it measuring anything, and why is precision no defence?
5. When something matters and cannot be counted, what do you track instead, and why read the trend rather than the score?

### 1.4 Process, lifecycle, framework

1. What is the difference between a lifecycle and a process framework? Be specific.
2. Place Scrum on the ladder and justify it from the Guide's own description of itself.
3. SWEBOK says no ideal process exists. What does that licence, and what does it not excuse?

### 1.5 The lifecycle models

1. Discuss one advantage and one disadvantage of the Waterfall model.
2. What was Royce's own fix, and why is it *not* iterative development?
3. Is there a difference between iterative and incremental models? Explain.
4. What assumptions should you make about stakeholders when choosing an incremental model?
5. List the main characteristics of the Spiral lifecycle model, and state its **major focus**.
6. Give an example of a project for which the spiral is most appropriate, and say what makes it so.
7. Why must you decide a prototype's fate before building it, and what happens if you decide late?

### 1.6 Choosing a lifecycle

1. Which selection criterion is most often forgotten, and why does it decide the answer in practice?
2. Only about one process in five came from a planned improvement programme. What follows for how you read a team's stated method?
3. No source in this material compares lifecycle models on measured outcomes. What can you still defend, and what should you refuse to claim?

---

## 2. Lecture Questions — L2b

### 2.1 Why a framework

1. Name three things a framework buys and two it costs.
2. The named success factors for adoption are managerial, not technical. What does that imply for an adoption budget?
3. "Adopt it whole, then tailor" and "customising is a success factor" appear to conflict. Resolve them.

### 2.2 Agile and its limits

1. Explain some characteristics of agile methodologies.
2. Give two negatives of agile, each with an example.
3. Three of the four standard objections are assumptions agile makes about your situation. Which three, and what does each assume?
4. A 2002 report predicted both agile's takeover and its failure to scale. What actually happened, and what does that teach about quoting figures?

### 2.3 XP, Scrum, Kanban

1. Why is XP describable as review, integration and testing with the delay removed?
2. Under pressure, which XP practices survive and which erode? What explains the pattern?
3. Name Scrum's three accountabilities, four events and three artefacts, with the commitment attached to each artefact.
4. What does adopting Scrum actually change, and what question should a team ask before adopting it?
5. Discuss the Kanban process framework. For what kinds of projects is it most suitable? Provide an example.
6. In a pipeline taking 10 requirements a week, developing 10 and testing 5, why does adding developers make things worse?
7. Scrum and Kanban both cap work in flight. What does each cap, and why does that make them complements?

### 2.4 Scaling

1. Why is scale not headcount? Name three things that grow faster.
2. Why does distance break agile's coordination first, and what blunt rule follows?
3. SAFe and LeSS answer scale in opposite ways. Contrast them, and say what each thinks the problem is.

### 2.5 RUP and the Unified Process

1. What are the four phases of the Rational Unified Process?
2. RUP's gates are named for what they settle. How does that differ from a waterfall milestone?
3. Where does RUP fit, and where does it fit badly?
4. RUP and SAFe answer the same question twenty years apart. What is the question, and how does each answer differ?

### 2.6 Choosing

1. Code review is adopted more widely than Scrum. What does that tell you about the unit of decision?
2. How do size and criticality set the weight of a method? Use Cockburn's cells in your answer.
3. (Boehm) Explain how **criticality** affects process selection, and give an example. Cover *both* directions.
4. (Boehm) Explain how **dynamism** affects process selection, and give an example.
5. A good assessment outputs mitigations rather than a verdict. Why, and what does a verdict-only answer leave out?
6. Select **two** process frameworks. Summarise each, list its strengths and weaknesses, and state the conditions under which you would use it and why.
7. State the four questions you would answer for any framework recommendation, and say which one teams skip.

### 2.7 Process under AI agents

1. Whether AI assistants improve code quality is unresolved, and developers misjudge their own speed. What follows for evaluating a tool?
2. Generation doubles what enters review and nothing doubles review. Which framework assumption breaks, and where does the constraint move?

---

## 3. Reading Questions

Cite the reading you used, with a page number where you have one.

### 3.1 Radice et al., "A Programming Process Architecture" (1985)

1. Radice reached bottom-up process definition as a solution to *acceptance*, not as a research method. Why does that matter?
2. The paper rules out reading ETVX as strict serialisation. Quote the clause and explain its consequence.

### 3.2 Basili, Caldiera & Rombach, *The Goal Question Metric Approach* (1994), with Basili et al. (2010)

1. The founding paper states no limitation of any kind. Where would you look for one, and what does that habit generalise to?
2. What does the 2010 paper name as GQM's missing support, and what does a manager do about it before deriving questions?

### 3.3 Humphrey (1988) and Hoffman (2000) on metrics

1. Pressman and Humphrey both identify misuses of process metrics. Which misuse do you believe is the most harmful, and why?
2. Twenty-five defect reports were closed as duplicates of one. Nobody falsified anything. Explain how the number improved and the product did not.

### 3.4 Mota, *Scoreboard: A Support for Management Information Needs* (2009)

1. Identify the critical questions you would ask at the beginning of a project, and justify your choices.
2. Anonymity buys candour and costs resolution. How would you design around that trade?

### 3.5 Pressman, *Software Engineering* (7th ed., ch. 25)

1. Pressman defines correctness as the degree to which a program performs its required function, and offers defects per KLOC as the common measure. Do you agree that this is appropriate? Explain.
2. Pressman identifies four critical attributes of baseline data. Which is the most critical, and why? Be specific.

### 3.6 Royce, "Managing the Development of Large Software Systems" (1970)

1. Royce calls his own content "prejudices" and presents no data. How should that shape the way you cite him?
2. He budgets ten months of thirty to a version nobody ships. Argue for or against that trade on a project you know.

### 3.7 Boehm, "A Spiral Model of Software Development and Enhancement" (1988)

1. Boehm's *Difficulties* section says the model suits internal development and needs work for contract acquisition. Why is that the opposite of what most people guess?
2. The spiral subsumes the other models under certain conditions. Name one such condition and the model it reduces to.

### 3.8 STSC, *System Life Cycle and Methodologies* (1996), and Walton (2004)

1. A 1996 acquisition guidebook reports that most programmes use a combination of models. Why do people read "combination" as a compromise?
2. Walton asks why companies do not adopt iterative development. Which of his reasons still holds, and which has dated?

### 3.9 Tsui & Karam, *Essentials of Software Engineering*

1. Which development activity would you add first to the simplest possible process model, and why that one?
2. Compare the book's account of agile characteristics with Abrahamsson's four criteria. Where do they differ?

### 3.10 Abrahamsson et al., *Agile Software Development Methods* (2002), and the Scrum Guide (2020)

1. Abrahamsson's four criteria are proposed, not validated. What are they still good for?
2. The Guide calls Scrum immutable while the evidence calls customising a success factor. Take a position and defend it.

### 3.11 Middleton & Joyce (2012), and Rubin (2012)

1. The BBC team's throughput was not measured, only its cycle time. Which claims does the paper support, and which does it not?
2. Rubin is a Scrum trainer writing about Kanban in roughly twenty-five lines. How does that affect how you use his comparison?

### 3.12 Cockburn, "Selecting a Project's Methodology" (2000), and Boehm & Turner (2003)

1. Cockburn draws his grid twice, for productivity and for legal liability. What does the second copy change?

### 3.13 Rockwood, "Choose Your Weapon Wisely" (2003)

1. Discuss Scrum with respect to the parameters Rockwood introduces, and provide an example.
2. Compare Rockwood's eleven equally-weighted questions with Boehm and Turner's five continuous axes. How does the shape of an instrument change the decision it produces?

### 3.14 Lattanze, *Architecting Software Intensive Systems* (2009)

1. Under which lifecycle does the ACDM framework fit? Explain.
2. Lattanze calls the untailored use of a method "naive at best". What is his argument, and does the survey evidence support it?

### 3.15 Kuhrmann et al. (2019), Dikert et al. (2016), Edison et al. (2022)

1. Dikert's factors are frequencies of mention across 42 cases, roughly 90% experience reports. What can and cannot be concluded?
2. Edison screened 35,215 articles and declines to rank the frameworks. Why is a refusal to answer a useful result?

### 3.16 The AI evidence — Mohamed et al. (2025) and others

1. A systematic review of 39 studies reviews but does not measure, and its cut-off covers assistants rather than agents. What does the gap mean for a manager reading it?
2. In a randomised trial developers were 19% slower while believing they were 20% faster. What does that rule out as evidence?

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
