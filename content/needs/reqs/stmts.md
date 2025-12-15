---
parent: Requirements
title: Statements
nav_order: 2
layout: default
---

# Requirement Statements
_*Adapted from David Root (2014)_

## Types of Requirements

- **Functional Requirements** (“What”):  
    These define _what_ the system must do. They specify behaviors, inputs → outputs, transformations, business rules.  
    _Example:_ “Input X produces Y” → “When user submits form A, system validates the input fields, stores data in database, and shows confirmation message.”
    
- **Non-Functional Requirements / Quality Attributes** (Christel & Kang etc.):  
    These describe _how_ well the system performs its functions, under what conditions, with what constraints. Sometimes called “the ilities.”
    
- **Interfaces**:  
    Requirements about how the system interacts with external actors or other systems: user interfaces, APIs, hardware, databases, etc.
    
- **Design Constraints**:  
    Restrictions or mandatory conditions on design/implementation choices: technology stack, platforms, standards, regulatory constraints, performance limits, etc.
    
- **Implied Requirements** (Very Nebulous):  
    Things the stakeholders _assume_ will be there but do not explicitly state. These might cover usability, security, performance levels, maintainability. It’s dangerous to leave them implicit.
    

---

## Good Requirement Statements

What makes a requirement “good”? Key qualities:

|Property|What it Means / Why It’s Important|Examples / What to Avoid|
|---|---|---|
|**Unambiguous**|Must mean only one thing—no confusion. Avoid vague modifiers.|Don’t use: _best, fastest, highly, etc._ Instead: “Response time shall be ≤ 2 seconds under peak load.”|
|**Non-decomposable**|A requirement should be atomic: not mixing several things; each requirement expresses one distinct thing.|Bad: “Windows-like GUI” mixes UI style + platform reference. Better: “Provide a GUI supporting menus, dialog boxes, drag & drop.”|
|**Testable / Measurable**|You must be able to verify whether the requirement is met; specify metrics.|“System shall handle 100 requests per second with 95 % success rate.”|
|**Traceable**|You can map each requirement back to its source (stakeholder, business driver) and what problem it solves. Also track dependencies among requirements.|Each req has an ID, mentions “originated from stakeholder X” or “to satisfy business goal Y.”|
|**Has Constraints / Dependencies**|Requirements often depend on or interact with other requirements; must note them explicitly.|“Requires database version 5.4”; “Depends on payment gateway being available.”|

---

## Quality Attributes (the “ilities”)

Common “non-functional” / quality attributes. These are often architecturally significant.

- Performance
- Modifiability / Maintainability
- Reusability
- Reliability
- Stability
- Security

Additional ones:

- Extendibility
- Portability
- Usability (User friendly)
- Scalability
- Data integrity

Also provocative or informal ones:

- “Buildability” (ease with which it can be built)
- “Wowability” (user delight / aesthetic or “wow” factor) — these are useful signals but must be made concrete if used.

---

## Functional vs Quality Attributes

- Are they connected? **Yes** — functional requirements define _what_ a system does; quality attributes define _how_ those functions behave (performance, reliability, etc.). Some functional requirements may themselves be “architecturally significant” because they trigger or interact heavily with quality attributes.
- How to describe Quality Attributes: via **scenarios** or **quality attribute scenarios** (six-part pattern): stimulus, stimulus source, artifact, environment, response, response measure.
- Are they all testable? Ideally yes — quality attribute requirements should be specified so that they can be measured. If vague (“the system shall be fast”) they are _not testable_.
- Traceable? Yes — each quality attribute requirement should be linked to stakeholder concerns / business drivers. Often test cases or architecture decisions depend on them.

---

## Requirement Statements / Scenarios

### Pattern: Stimulus, Environment, Response (plus source, artifact, measure etc.)

- **Simplified**: Stimulus → Environment → Response
- **Complete**: Stimulus; Source of stimulus; Environment; Artifact stimulated; Response; Response measure

### Types of Scenarios (Examples)

|Scenario Type|Purpose / Use|Example|
|---|---|---|
|**Use-case scenario**|For functional requirements or quality under normal operation|_“Remote user requests a database report via the Web during peak period and receives it within 5 seconds.”_|
|**Growth scenario**|To capture evolution / scale over time|_“Add a new data server to reduce latency from 5 seconds to 1 to 2.5 seconds within 1 person-week.”_|
|**Exploratory / Fault / Failure scenario**|To check for robustness, fault tolerance, edge cases|_“Half of the servers go down during normal operation without affecting overall system availability.”_|

### Quality Attribute Scenarios

- Use the same kind of scenario to specify _non-functional_ requirements. E.g.:
    - **Modifiability scenario**:
        > “After receipt and analysis of a requirement change, a mid-grade software engineer will be able to modify logic module X in system Y in one engineering week.”
- Must define stimulus, source, artifact, environment, etc., and how you measure success.

---

## Testing & Predicting Quality Attributes

- For QA requirements, think **ahead**: how will you test them? Can you simulate under load? Can you inject failures? Will automated tests cover this?
- Role of Architecture: architecture decisions strongly affect whether quality attributes can be met (e.g. redundancy, modularity, caching, separation of concerns). If architecture cannot support the required reliability / modifiability etc., adding the requirement later is expensive.
- Use trade-off analysis: quality attributes often conflict (e.g. security vs performance; ubiquity vs portability vs speed). You must prioritize and make conscious trade-offs. SEI’s “Generic Taxonomy for Quality Attributes” is useful for seeing how attributes interact.

---

## Sources / References

- Christel, M. & Kang, K. (1992). _Issues in Requirements Elicitation_, SEI-CMU-TR-12. (issues of scope, ambiguity, volatility, etc.)  
  [SCIRP](https://www.scirp.org/reference/referencespapers?referenceid=1144853&utm_source=chatgpt.com)
- SEI CMU - _Software Quality Attribute Taxonomy / Generic Taxonomy_ (Barbacci et al.) — for definitions and trade-offs among quality attributes.  
  [sei.cmu.edu](https://www.sei.cmu.edu/documents/1142/1995_005_001_16427.pdf)
- “Quality Attributes in Software Architecture” (Priyal Walpita) — good summary of how to treat QAs, scenario-based specification.  
  [Medium](https://priyalwalpita.medium.com/quality-attributes-in-software-architecture-cacffe0995aa)
- UBC “System Qualities & Scenarios (Non-functional Requirements)” lecture — defines concrete vs general scenarios, gives the 6-part scenario pattern.  
  [Electrical and Computer Engineering](https://people.ece.ubc.ca/matei/EECE417/BASS/ch04lev1sec4.html)

---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.

---

## Sources

- Root, David. *Managing Software Development*. Lecture materials, 2014.

---

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
