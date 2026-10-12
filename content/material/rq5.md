---
parent: Revision Questions
title: RQ5
nav_order: 5
page_type: question-set
layout: default
---

# RQ 5 — Planning: Milestones, Activities and Critical Chain

Covers **L5a** (why plan, predictive and agile planning, sponsor plans, milestones and how to date
them) and **L5b** (activity planning, the critical path, float and levelling, views of a plan, why
schedules run late, and critical chain). Summaries at [SN L5a](sn5a.html) and [SN L5b](sn5b.html);
the detail is in the [Planning](../plan/) area.

Answer each in a short paragraph: state your claim first, then the reasoning or the evidence, then a
concrete software example where one is asked for.

---

## 1. Lecture Questions — L5a

### 1.1 Why plan

1. A plan is coordination prepared in advance. Compare it with the other three mechanisms: reference to a higher level, shared representations and communication. Give a software-team example of each.
2. "We plan to stop the client changing course." Why is this a wrong reason to plan, and what does a plan let you do when a change arrives?
3. A good plan has the properties of a good program. Pick two of them and show what a bug of each kind looks like in a plan.

### 1.2 Predictive and agile planning

1. Both approaches decide what, when and who. Compare when each approach takes these decisions, and who takes them.
2. Predictive control acts on deviations from a baseline; Scrum inspects an increment each sprint. Which suits a project whose requirements change often, and why?
3. "Agile teams do not plan." Use the five planning levels to argue against this claim.
4. Why are commitments planned before activities? What goes wrong when a team plans tasks before it agrees what it will deliver?

### 1.3 Two plans, two readers

1. What separates a sponsor-oriented plan from a developer-oriented one? Why is a changed task order the team's business, but a changed date a renegotiation?
2. Why do "Iteration 2 completed" and "Low-level design finished" tell a sponsor nothing? Rewrite one as a result she could check.
3. Why does a sponsor-oriented plan such as AmazonLite's list the client's milestones beside the team's?

### 1.4 What a milestone is

1. Andersen defines a milestone as a result, not the end of a task. How does writing each milestone as "When…" enforce this?
2. Compare milestone planning and activity planning on focus, information needed and stability. Why can milestones be planned early when activities cannot?
3. Milestones depend on each other finish-to-finish. Why does this stop a milestone plan from becoming a waterfall?
4. Why assign responsibility per milestone rather than per task? What does a responsibility chart that is hard to fill in tell you?

### 1.5 Writing good milestones

1. Why does a team need control milestones a day or two apart, when the sponsor needs result milestones weeks apart? Connect your answer to reporting "done" or "not done", never percentages.
2. A milestone must be specific, verifiable, relevant and timely. Write one for a software project that fails one test, then repair it.
3. Exit criteria and Scrum's Definition of Done do the same job. What is that job, and what happens in a milestone review without them?
4. Boehm says: do not start full-scale development before the LCA milestone is met. What does LCA check that LCO does not, and why is skipping it dangerous?
5. "Ownership decides, not the calendar." Explain this rule for hard and soft dates, with one software example of each.

### 1.6 Planning milestones, worked

1. Why start from the hours that actually exist, not from headcount times forty? What does a resource plan show that a headcount hides?
2. Why place the hard-milestone work first? Why is white space in a schedule not a buffer?
3. Drawn to scale, AmazonLite needed one more month. Why did drawing it show this, and what other options did the planner have?
4. Programme managers hold a reserve out of sight. Why not hand it out with the schedule?

---

## 2. Lecture Questions — L5b

### 2.1 How teams plan activities

1. Compare pull in Scrum with push in plan-driven planning. Who picks a task, who answers for it, and how does each typically fail?
2. Why is the sprint backlog a commitment of the team, not a list of personal tasks? Why does the team commit only to hours it has measured?
3. Why is rolling wave the plan-driven answer to early ignorance? How does it match Andersen's advice on when to plan activities?

### 2.2 Networks and the critical path

1. A network records who waits, not who works. What does it leave out, and why does that matter when you read its finish date?
2. Why is finish-to-start the safe default between tasks? What do you buy, and risk, when you relax a link to start-to-start?
3. Why do tasks on the critical path have zero float? What does that mean for the risks on those tasks?
4. On DuPont's first test only about one job in ten was critical. Why does that make the network worth drawing?
5. Without formulas, explain what the forward and backward passes give each task. Why must you recheck the critical path after every change?

### 2.3 Float and levelling

1. Distinguish free float from total float. Why is free float safer to give away to a developer?
2. Why does levelling almost always stretch the schedule? Why spend free float first and overtime last?

### 2.4 Views of a plan

1. "Report with the Gantt chart; decide with the network." Explain why, and say what a Gantt chart cannot show about resources.
2. Why can a DSM show a design loop that a network cannot draw? Give a software example of two tasks that need each other's outputs.
3. Which view answers which question: what the sponsor gets by March, which slip moves the date, where design work loops back? Say what each view leaves out.

### 2.5 Why schedules run late

1. Why is the CPM finish date a floor and not a forecast? Take two of its assumptions that fail in software work, and say what answers each.
2. Why is the most likely duration not a likely date? What should you ask an estimator for instead?
3. Explain merge bias. Why do merging paths pass on delays but seldom pass on savings?
4. Students' best guesses ran short even when they knew their past record. What does this suggest about how to get a better estimate?
5. Explain Parkinson's Law and the student syndrome. How much evidence stands behind each?
6. Why does juggling three projects make all three late, with the same people and the same work?

### 2.6 Critical chain

1. What does critical chain count that CPM does not? Why does the longest path move once shared people are counted?
2. Why does pooled safety protect the date in less time than safety padded into each task? Which assumption must hold for pooling to work?
3. Name the three buffers and the threat each one guards against. How does the feeding buffer answer merge bias?
4. Critical chain removes task dates and asks people to work like relay runners. How does this weaken Parkinson's Law and the student syndrome?
5. With no task dates, how does a manager control the project? Why is one late task not news, while a fast-burning buffer is?
6. Pick two risks that CPM and critical chain share. Why does switching method not remove them?
7. What survives of critical chain after the simulation and the data on estimates, and what does not? Answer for buffer size and for cutting every estimate by half.

---

## 3. Reading Questions

Cite the reading you used, with a page number where you have one.

### 3.1 Andersen, "Warning: Activity Planning is Hazardous to Your Project's Health!" (1996)

*International Journal of Project Management* 14(2), 89–94 {% cite andersen_warning_1996 %}.

1. Why does Andersen argue that early, detailed activity planning is hazardous to a project? Does the argument hold for software?
2. Why does the uniqueness of a project make it impossible to list its activities meaningfully at the start? Give a software example.
3. Andersen gives four reasons why planners still draw full activity networks early. Which two are most dangerous on a software project, and why?
4. How does activity planning pull attention away from results? What does a team lose when it reports on tasks instead?
5. How does Andersen's milestone differ from the common "end of an activity" view? Use his Figure 2 or a software example.
6. What are result paths? Why do the dependencies between paths matter?
7. How does a milestone responsibility chart improve accountability compared with responsibility per task?
8. How can a time schedule be made without listing every activity first? Explain the two ways Andersen allocates time between milestones.
9. Andersen does not reject activity planning. When should it be done, and why close to the work on each milestone?
10. The 1996 paper never mentions iterative methods. Which of its ideas would an agile team recognise, and where does the comparison break down?

### 3.2 Browning, "Applying the Design Structure Matrix to System Decomposition and Integration Problems: A Review and New Directions" (2001)

*IEEE Transactions on Engineering Management* 48(3), 292–306 {% cite browning2001dsm %}.

1. What problem in design and development work does the Design Structure Matrix (DSM) help to solve? Use Browning's explanation of where rework comes from.
2. How does a DSM show a dependency between two activities? How can you tell a feed-forward mark from a feedback mark?
3. Browning says the activity DSM shows iteration and coupled activities, which PERT/CPM cannot. How does a feedback loop appear in the matrix, and what does a coupled block look like?
4. Browning treats activities as steps that receive and produce information. How does this view lead to a better order of activities? What happens when planners overlap activities without checking their information needs?
5. What is the goal of partitioning an activity DSM? How does the result help planners decide which activities must be planned together?
6. Browning separates static DSMs (components, teams) from time-based DSMs (activities, parameters). Why are static DSMs clustered, while time-based DSMs are sequenced? Use the Ford or the engine-team example.
7. Partitioning can leave a block of coupled activities. Explain aggregation, decomposition and tearing. Why does Browning not recommend aggregation?
8. Why does Browning see DSM as better suited than PERT/CPM to design and development work? Does a DSM replace the CPM schedule, or feed it?
9. Whom should you ask to build an activity DSM, and which four questions do you ask them? Why can the answers be unreliable?
10. Browning names two things a single DSM does not show. What are they, and how do a Gantt chart or a simulation fill the gap?

### 3.3 *Cutter IT Journal*, "Critical Chain Project Management: Coming to a Radar Screen Near You!" (2003)

*Cutter IT Journal* 16(3), a themed issue edited by Bill Lynch {% cite lynch_critical_2003 %}. Name the article's author when you cite it.

1. Why was critical chain slow to spread among project managers, despite claims of large improvements? Use Higgins's article.
2. What weaknesses of traditional activity-based planning does critical chain try to overcome?
3. How do the student syndrome and Parkinson's Law make safety margins in task estimates fail?
4. How does pooling safety into a project buffer make a schedule both shorter and more reliable?
5. What does relay-runner behaviour mean, and how does it differ from managing tasks against Gantt-chart dates?
6. In a multiproject setting, why does bad multitasking cut throughput even when every resource looks fully used?
7. What cultural and structural changes did Abbott Diagnostics need to make critical chain work across several sites?
8. How did the Segway project combine agile iterations with critical-chain scheduling, and what did the combination give it?
9. What is the difference between Newbold's Old Game and New Game of project management? How does critical chain support the New Game?
10. Zultner separates a 50%-likely estimate from a 90%-likely commitment. Why does critical chain plan tasks at 50% estimates, and why must people be allowed to overrun them without blame?

---

### Acknowledgments

These questions build on the Fall 2025 study-notes selection (SN5) and on lectures by Eduardo
Miranda {% cite miranda_managing_2014 %}.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
