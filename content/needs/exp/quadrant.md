---
parent: Expectations
title: Hoover Quadrant
nav_order: 2
layout: default
---

# The Hoover Approach: Customer vs. Developer Views

**Source:** Hoover, Carol L., Mel Rosso-Llopart, and Gil Taran, _Evaluating Project Decisions: Case Studies in Software Engineering_. Addison-Wesley Professional, 2010. ISBN-13: 978‐0321544568. [O'Reilly Media](https://www.oreilly.com/library/view/evaluating-project-decisions/9780321685629/)

---

![Quadrant](<quad.png>)

## Customer’s View – _Expectation Space_

Customers typically define project success using **four core dimensions**:

- **Scope** – What will be delivered.
- **Budget** – How much it will cost.
- **Time** – When it will be finished.
- **Quality** – How good the outcome will be.

Together, these form the **expectation space**—the lens through which customers measure project success.

---

## Developer’s View – _Solution Space_

Developers, on the other hand, focus on how to _make the project work_:

- **Technology** – Tools, platforms, architectures.
- **People** – Skills, team members, availability.
- **Process** – Development practices, workflows, methods.

This is the **solution space**—the factors developers can directly control and adjust.

---

## Bridging the Two Views

Projects succeed when developers **translate solution decisions into customer expectations**.

- **Example:**  
  - _Team selection_ (People) → affects _Time_ (delivery schedule).
  - _Choice of technology_ → affects _Budget_ (costs for licenses, training, maintenance).
  - _Process maturity_ → affects _Quality_ (defect rates, reliability).

When issues arise, customers want to know **how the impact shows up in their terms** (scope, time, budget, quality).

---

## Case Example – Hoover et al.

In _Evaluating Project Decisions_, a team faced performance problems after adopting a new technology stack.

- **Developer view:** The technology was innovative but required more training.
- **Customer view:** The delay led to **missed deadlines (Time)** and **increased training costs (Budget)**.
- **Resolution:** By explaining the trade-off in customer terms, the team gained agreement to extend the timeline, since the new technology promised **higher long-term Quality**.

---

## Impact of Project Time on Customer–Developer Views

![[Pasted image 20250915184445.png]]

*Source: Hoover et al., Evaluating Project Decisions*

The diagram shows how the **focus of a project shifts over time** across three layers:

### 1. Problem Space (Customer’s Expectations)

Customers define the project in their terms:

- **Requirements (Scope):** What features or outcomes are expected.
- **Cost (Budget):** How much they are willing to spend.
- **Time (Schedule):** When they need it delivered.
- **Quality (Defects):** What level of reliability they expect.

This is the **expectation space**—what success means to the customer.

---

### 2. Solution Space (Developer’s View)

Developers respond with their levers of control:

- **Technology:** Tools, frameworks, platforms.
- **People:** Skills, team composition.
- **Process:** Methods, workflows, standards.

For each area of the problem space, developers adjust these three factors to design a solution.

---

### 3. Decision Space (Where Trade-offs Are Made)

Ultimately, every project decision reduces to either:

- **Task focus:** Optimize work to meet objectives (technical, efficiency-driven).
- **Relationship focus:** Manage expectations, communicate impacts, maintain trust.

---

## The Role of Time

- **Early in the project:** Focus is broad and strategic (Requirements, Scope). Customers want clarity; developers explore technology, process, and people options.
- **Mid-project:** Attention shifts to Cost and Schedule. Are we on budget? Are we still on track?
- **Late in the project:** The dominant concern becomes **Quality**. Customers care less about promises and more about whether the delivered product works without defects.

**In summary:**

- **Start:** “What will we get?” (Scope)
- **Middle:** “Will it be on time and on budget?”
- **End:** “Does it actually work well?” (Quality)

---

## Illustration – Mini Case

**Mobile Banking App Project:**

- **Early phase:** Customer wants clarity on features (scope). Developers select a cross-platform framework (technology) to efficiently cover requirements.
- **Mid-project:** Training costs for the framework increase. Customers push back: _“Will this stay in budget and still hit our deadlines?”_
- **End of project:** The app is delivered but has bugs. Now, **quality dominates expectations**: customers care less about missed deadlines and more about _“Can we trust this app with real money?”_

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining, and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
