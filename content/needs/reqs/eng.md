---
parent: Requirements
title: Engineering
nav_order: 3
layout: default
---

# Requirements Engineering
_Adapted from David Root (2014)_

## Key Activities / Steps

Tsui & K include:

- Elicitation
- Definition, categorizing, and documentation
- Specification
- Prototyping
- Analysis
- Review and Validation
- Agreement and acceptance

Pressman includes:

- Gathering
- Modeling
- Management
- Validation

---

### What this all means

- It’s a **systematic process** for getting from a fuzzy “need” → clear, agreed, testable specifications.
- It must be **planned**: you can’t just collect requirements ad-hoc.

Key sub-activities:

1. **Elicit needs**
    - Ask the right questions: _What is the problem being solved?_ _Is there actually a problem?_
    - Engage stakeholders, use interviews, workshops, observation, prototyping, etc.
2. **Analyze**
    - Validate and quantify the functional requirements, quality (non-functional) attributes, and constraints.
    - Look for consistency, feasibility, completeness.
3. **Agree completion / acceptance criteria**
    - Define “done”: what criteria will show that the requirements are satisfied.
    - Establish a working agreement; define acceptance criteria, possibly statement of work.
4. **Document**
    - Produce the requirements specification: functional + non-functional + constraints + acceptance criteria + external interfaces + assumptions etc.

---

## Verification vs Validation

Verification ensures the _quality of the specification itself_. Validation ensures the _correctness of the specification with regard to stakeholder needs and business goals_.

|Term|Definition|Example|
|---|---|---|
|**Requirements Verification**|The process of checking whether the documented requirements _are correctly written_, consistent, complete, unambiguous, testable, and meet the specification standards. It is about ensuring the requirements reflect what was agreed upon and are well-formed. It is done before (or early in) development.|Example: A peer review of the requirements document to ensure that every requirement has a unique identifier, that each is measurable (e.g., “within 2 seconds” rather than “fast”), that there are no contradictory requirements.|
|**Requirements Validation**|The process of checking that the requirements _match stakeholder needs, business goals, and the real world environment_. It's about confirming that what has been specified really is what is needed. It often involves involving stakeholders, doing prototypes, or acceptance criteria.|Example: Showing a mock-up or prototype to end users to confirm that workflows meet their needs; verifying that the system will support peak usage as the business expects; stakeholder review to confirm all essential features are included.|

---

## Putting It All Together

- A **systematic way** of getting from need → specification.
- Must be planned: schedule, resources, stakeholder involvement, process of review/validation etc.
- **Elicit needs**: clarify problem, ensure real need, not just a proposed solution.
- **Analyze**: validate, put numbers where possible, quantify non-functional requirements and constraints.
- **Agree completion criteria**: define “done”, acceptance, criteria, sign-off.
- **Document**: produce a requirements spec or SRS that captures everything in a clear, testable form.

---

## Quantification / Testability — Not Easy!

- Raw requirements tend to be **unspecific** and qualitative (vague). Without quantification, you can’t test them well.
- You must be able to prove that a product satisfies requirement → must be testable, measurable.
- You should start thinking about the test plan early (often in parallel with requirements). It helps force clarity.
- Requirements spec should say **how big, how much, how fast, how often**, etc.
- If you omit these, you set yourself up for ambiguous expectations, failure, disappointment.

---

## Examples

### Example 1: “The System Shall Be Intuitive and Easy to Use”

- **Raw requirement (bad)**:
    > “The system shall be intuitively easy to use.” — un-testable, vague.
- **Improved version**:
    > _The system interface shall:_
    > - be learnable to 90% proficiency in 2 weeks;
    > - have an average user error rate of less than 2%;
    > - score at least 85% on a user satisfaction test.
- **Notes**: define what “average user” means; define context (tasks, domain, environment) so you can measure well.

---

### Example 2: “The system shall be modifiable”

- **Raw requirement (bad)**:
    > “The system shall be modifiable.” — vague, no context or measure.
- **Better version**:
    > _The system shall accommodate:_
    > - changes in the user interface without impact to other elements of the system;
    > - changes to element X in Y staff hours.
- **Again**: specify which “element X”, what “impact”, what is acceptable “staff hours”, in what environment / with what tools, etc.

---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.

---

## Sources

- GeeksforGeeks: _Requirements Engineering Process_ — definitions of verification vs validation, specification, elicitation etc.
  [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/software-engineering-requirements-engineering-process/)
- Visure Solutions: guide on requirements verification and validation.
  [visuresolutions.com](https://visuresolutions.com/alm-guide/requirements-verification-and-validation/)
- Xebrio: Requirements engineering, how raw requirements are refined, testability etc.
  [Xebrio | Project Management Software](https://xebrio.com/requirements-engineering/)
- SEBoK (Wikipedia entries also good summaries) for "Verification vs Validation", "Requirements Engineering" definitions.
  [Wikipedia](https://en.wikipedia.org/wiki/Verification_and_validation)

- Root, David. *Managing Software Development*. Lecture materials, 2014.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
