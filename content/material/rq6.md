---
parent: Revision Questions
title: RQ6
nav_order: 6
page_type: question-set
layout: default
---

# RQ 6 — Tracking: Release Planning

Covers **L6a** (releases and iterations, choosing what goes in, Buffered MoSCoW, running the time
box, contracts and incentives, and when two estimates are not enough). The **L6b** part, on
monitoring, earned value and burndown, will be added after that lecture. Summary at
[SN L6a](sn6a.html); the detail is in the [Release planning](../plan/release/) area.

Answer each in a short paragraph: state your claim first, then the reasoning or the evidence, then a
concrete software example where one is asked for.

---

## 1. Lecture Questions — L6a

### 1.1 Releases and iterations

1. Compare a release and an iteration. Who receives each, and what does planning decide for each?
2. Every sprint ends potentially shippable, yet the team may not ship it. Who decides how often to release, and on what grounds?
3. Why does a fixed-date plan answer with a range (will have, might have, won't have) instead of one feature list? What does McConnell mean when he says a time box's end date "is not a due date"?
4. Why commit to the next release but only sketch the ones after it? Take two of the four forces that release planning balances and give a software example of each.
5. Why pick a release strategy before picking features? Why does a backlog still need a reason for its order in an agile project?
6. The same work in four quarterly releases gave a gain where one yearly release gave a loss. Explain why without calculating.

### 1.2 Choosing what goes in

1. Why is release planning a knapsack problem with dependencies? What makes it harder than filling one bag?
2. In one cost–value study, dropping three of fourteen requirements kept almost all the value. What does this say about treating requirements as roughly equal?
3. Each planning method optimises a different goal. Pick two methods and describe a project that suits each. Why should a person, not the computer, choose the final plan?
4. DSDM tests a Must by asking whether you would stop the deployment without it. Why is this a better test than "is it important"? Give a Must and a Should for an app you know.
5. Why does DSDM cap the Musts at about 60% of the effort? When may a team go above it?

### 1.3 Buffered MoSCoW

1. Compare the DSDM meaning of a Must with the Buffered MoSCoW meaning. Who decides the order of the features, and what decides where the line falls?
2. Why plan the Musts at their safe estimates but run them at their normal ones? Where does the Must buffer come from?
3. How are the Shoulds chosen? Why is their budget the Must buffer, and not whatever capacity is left?
4. Why does each category down roughly halve the chance of delivery? What should you tell the sponsor instead of fixed percentages?
5. Why does it help to keep the Musts near 60% and to split big features into small ones?

### 1.4 Running the time box

1. A Must overruns. Why does this cost the Could and not the date? Why does nobody need to renegotiate?
2. After a demo the customer reorders the priorities. When does the change enter, who decides, and what gives? Why does reprioritising never move the date?
3. Why treat infrastructure as a feature that other features depend on? Give a software example.
4. How should critical, major and minor defects be handled inside a time box? Why does the customer choose between fixes and new features?
5. Compare committing once for the whole project with committing once per increment. Why can a Could missed in release 1 become a Must in release 2?

### 1.5 Contracts and incentives

1. Compare fixed-price, time-and-materials and incentive contracts. Who carries the risk of partial delivery in each?
2. Why price a contract on its expected outcome and not on its best case? Explain without calculating.
3. Why is there no bonus for delivering the Musts? Why is an unlikely reward a lottery rather than an incentive?
4. How do Parkinson's Law and the student syndrome waste unused buffer? How can rewards for the Should and Could releases make the team hand that time on?

### 1.6 When two estimates are not enough

1. Why do shared causes make features overrun together? What does this do to the protection a buffer gives?
2. When is Buffered MoSCoW enough, and when do you need SPID? What does SPID ask for that Buffered MoSCoW does not?

---

## 2. Reading Questions

Cite the reading you used, with a page number where you have one.

### 2.1 Miranda, "Time Boxing Planning: Buffered MoSCoW Rules" (2011)

*ACM SIGSOFT Software Engineering Notes* 36(6), 1–5 {% cite miranda_time_2011 %}.

1. Miranda says a time box without agreed partial outcomes and justified certainty is "an expression of good will". Which of his three conditions for a working time box does plain MoSCoW fail to provide, and why does that matter to a sponsor?
2. Miranda calls classic MoSCoW "either unconstrained or arbitrarily constrained". Explain both problems. What constraint does his method add?
3. In his method a feature's category is "not an a priori decision". What decides it, and what does the customer still decide?
4. Why does Miranda refuse to call his two estimates the 50% and the 90% estimates? What would such numbers require?
5. In the paper's execution example, one Must feature takes its worst case. What happens to the Should and the Could features, and why does the date hold?
6. How does the paper handle a change request, and how does it handle defects? What does each choice cost the customer?
7. Miranda argues that a business is better off knowing what it can realistically expect than being "promised the moon". What must a contract accept for this to work, and why would a contract that puts all the risk on one party fail?
8. Miranda says the method's simplicity "is not free". What does it cost, and when should a planner use a more detailed approach such as SPID?

---

### Acknowledgments

These questions build on lectures by Eduardo Miranda {% cite miranda_managing_2014 %}; the MoSCoW
categories come from the DSDM Agile Project Framework.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
