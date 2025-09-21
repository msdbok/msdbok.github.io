parent: Needs
title: Requirements
nav_order: 3
layout: default
---

## Requirements Management

- **Definition:**  
    > “A set of activities that help a project team to identify, control, track requirements and changes to requirements at any time as the project proceeds.”

- **Expanded definition (Pressman et al.):**  
    Requirements management also includes _elicitation, validation, negotiation, traceability, baselining_.

- **Key activities in Requirements Management:**
    1. **Elicitation** – Gathering requirements from stakeholders.
    2. **Analysis / Negotiation** – Resolving conflicts, prioritizing, checking feasibility.
    3. **Specification / Documentation** – Writing down requirements clearly.
    4. **Validation** – Ensuring requirements reflect what stakeholders actually need, with no omissions or contradictions.
    5. **Change Control** – Managing changes to requirements as the project evolves.
    6. **Traceability** – Establishing links between requirements and business goals, designs, and tests.
    7. **Baselining** – Freezing a version of requirements at certain milestones.

- **Benefits:**  
    Reduced rework, clearer scope, better alignment between business/user and development, and ability to assess change impact.

---

## More Definitions

### Requirements

- **Webster’s:** Something required, wanted, needed, or essential.
- **Tsui & K:** “Set of statements that describe the users’ needs and desires.”
- **IEEE:**  
    - “A condition or capability needed by a user to solve a problem or achieve an objective.”  
    - “A condition or capability that must be met or possessed by a system or system component to satisfy a contract, standard, specification, or other formally imposed documents.”  
    - “A documented representation of a condition or capability as in (1) or (2).”

- **Implied requirements:**  
    Requirements not explicitly stated but expected (e.g., usability, reliability, “it should be fast,” “it should not leak memory”). Good practice is to elicit these explicitly.

---

### Constraints

- **Definition:**  
    - From Webster’s: Acts of constraining; state of being restricted or compelled.
    - From Davis: Limits imposed on the software due to users, customers, developers, technology, laws, and standards.

- **Examples:**
    - Legal or regulatory (GDPR, safety standards)
    - Technology constraints (must run on specific hardware/OS, network limitations)
    - Cost/budget constraints
    - Time constraints (delivery deadline)
    - Legacy system compatibility

---

### Business Drivers

- **Definition / Purpose:**  
    Business drivers are the forces (internal or external) that initiate, influence, and support activities or decisions for the business. They define _why_ a project exists and what value it should create (profit, efficiency, compliance, reputation, social good, etc.).

- **Why they matter:**
    - Inform mission and business context.
    - Drive prioritization of requirements.
    - Ensure alignment: requirements, design, and implementation should align with drivers.
    - Without explicit business drivers, teams may build less relevant features or waste time on “nice-to-haves.”

- **Examples:**
    - Increase revenue (new product or service)
    - Reduce costs (automation, efficiency)
    - Improve customer satisfaction/experience
    - Comply with regulation/legal requirements
    - Gain competitive advantage
    - Improve quality or reliability
    - Expand into new markets

- **Role in Requirements Specification:**
    - Frames business drivers as a “north star” for decision-making.
    - Helps identify constraints and priorities.

- **Artifacts:**
    - Strategy papers, mission/vision statements, market analyses, SWOT analyses, business plans.

- **Concept of Operations (ConOps):**  
    A document describing how a system will be operated from a user/operational viewpoint. It bridges business context to high-level requirements.

---

## How about a Specification?

- **Requirements** are the “what” and “why” (needs, desires, problems to be solved).
- A **Specification** (often “Software Requirements Specification,” SRS) is a formal document that describes those requirements in structured form, adding detail, organizing them, and specifying acceptance criteria, interfaces, quality attributes, etc.
- **Specification is more structured:** Organized by sections (functional, non-functional, interfaces, constraints), with numbering, traceability, diagrams, and examples.
- **Specification does not imply “built”:** It describes future behavior and constraints.
- **Includes requirements + constraints:** Good specifications include both, as well as external interfaces, assumptions, dependencies, and non-functional concerns.

---

## To Get Started

**Questions to ask before beginning requirements:**

- Who is the customer? (Who pays, who owns the product)
- What does the company do? (Domain, mission, focus)
- What is the problem the software will solve? (Always get to the _why_; avoid “solution without a problem”)

---

### Know Before You Start

**Things to analyze before writing requirements:**

- **Company:** Focus, vision/mission, business drivers, core competencies.
- **Past problems:** Prior failed or partially successful projects, existing specifications.
- **In-house expertise:** Available skills (domain experts, software, security, UI/UX, etc.).
- **Ties to other vendors/systems:** Dependencies, interfaces, standards, or tech required due to vendor constraints.

---

### Stakeholders

- **Definitions:**
    - Webster’s: Person entrusted with stakes.
    - Sommerville: “Anyone who benefits in a direct or indirect way from the system being developed.”
    - Wikipedia: Sponsor of project, or someone who has an interest or a gain upon successful completion.

- **Can all provide requirements?**  
    Some can, some cannot. Some are users with direct input, others more indirect (e.g., regulatory bodies). Some define needs; others define constraints.

- **Typical stakeholders:**
    - Users (end-users)
    - Customers (buyer, payer)
    - Sponsors (funders)
    - Management/project sponsors
    - Marketing
    - Developers
    - Operations/maintenance
    - Others (regulatory, legal, domain experts)

- **Organization hierarchy:**  
    Requirements often come from different levels: strategic goals → business requirements → user requirements → system requirements.

- **Problems mis-identifying intentions:**
    - Stakeholders may not agree.
    - Users may state desires in vague terms.
    - Customers may give a “solution” rather than a problem.
    - Hidden stakeholders: ignoring some may lead to missing requirements.

---

### Examples

- **Implied requirement:**  
    “The system shall be secure.” If not quantified (e.g., “shall use TLS 1.2 or better”), it’s vague and “implied.”
- **Constraint:**  
    “Must comply with GDPR”; “Must run on Android 11 and above”; “Maximum memory usage 512MB.”
- **Specification:**  
    Use “acceptance criteria” for each requirement: e.g., “when user clicks ‘Submit’, system shows confirmation message within 2 seconds.”
- **To Get Started:**  
    In a hospital software project, understand whether the customers are the hospital administration, doctors, nurses, patients; what regulatory constraints apply; what legacy systems are in place; what hardware is available.
- **Stakeholders:**  
    In a travel booking system: customers (bookers), airline partners, accommodation providers, payment gateway providers, marketing team, legal/regulation, users (travelers vs travel agents).

---

## Sources

- Pressman, R. _Software Engineering: A Practitioner’s Approach_ — especially the chapter on Requirements Engineering tasks: inception, elicitation, elaboration, negotiation, specification, validation, requirements management.  
  [Scribd](https://www.scribd.com/presentation/92670417/Pressman-Ch-7-Requirements-Engineering)
- IEEE/ANSI Standard 830-1998 “Software Requirements Specification (SRS)” — template & structure for specification sections.  
  [software-engineering-book.com](https://software-engineering-book.com/web/requirements-standard/)
- IEEE/ISO 29148-2018: Requirements Engineering standard — includes definition of requirements, processes for elicitation, specification, validation, traceability, etc.  
  [cwnp.com](https://www.cwnp.com/req-eng/)
- IBM article “What is requirements management?” — general description of RM processes: document, trace, analyze, prioritize, agree, managing change.  
  [IBM](https://www.ibm.com/think/topics/what-is-requirements-management)

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
