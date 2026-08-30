---
parent: Requirements
title: LLMs for Requirements Management
nav_order: 8
layout: default
---

# LLMs for Requirements Management

Large Language Models (LLMs) such as ChatGPT, DeepSeek, and other generative AI systems have shown significant potential in supporting various Requirements Engineering (RE) tasks. This emerging area explores how AI can assist requirements engineers throughout the entire RE lifecycle.

---

## Overview

Most requirements are specified using natural language, making LLMs particularly well-suited for requirements-related tasks. LLMs can process and generate human language by learning patterns from vast amounts of text data, enabling them to assist with requirements elicitation, specification, analysis, and validation.

**Key promise:** LLMs can help automate and streamline RE tasks, address communication challenges, and improve the efficiency and quality of requirements work.

---

## Applications Across RE Stages

### Requirements Elicitation

LLMs can assist in:
- **Domain analysis**: Rapidly processing domain-specific literature to provide foundational knowledge
- **Stakeholder communication**: Translating technical jargon into plain language and supporting multilingual stakeholders
- **Identifying unknowns**: Analyzing documentation to highlight areas of ambiguity or uncertainty
- **Generating requirements**: Creating preliminary requirements based on initial inputs and stakeholder personas

**Example use case:** Using LLMs to simulate stakeholder interviews by providing personas (e.g., "act as a 65-year-old retired patient with type-2 diabetes") to elicit requirements from different perspectives.

---

### Requirements Specification

LLMs can help with:
- **Formatting**: Converting unstructured requirements into structured formats (e.g., EARS template, user stories)
- **Classification**: Categorizing requirements into functional and non-functional requirements
- **Compliance checking**: Cross-referencing requirements against standards and regulatory guidelines
- **Generating artifacts**: Creating glossaries, examples, rationale, and user personas

**Example use case:** Converting informal requirements like "patients should not receive notifications when busy" into structured EARS format: "When patient is driving, ActApp shall not send notifications."

---

### Requirements Analysis

LLMs can support:
- **Quality evaluation**: Automatically assessing requirements for ambiguities, inconsistencies, or incompleteness
- **Risk identification**: Identifying potential risks and suggesting countermeasures
- **Conflict resolution**: Facilitating negotiation by simulating multiple stakeholder perspectives
- **Change impact analysis**: Providing real-time feedback during requirements refinement

**Example use case:** Using multiple LLM agents representing different stakeholders (e.g., patient vs. software architect) to negotiate and prioritize requirements, ensuring all perspectives are considered.

---

### Requirements Validation

LLMs can assist with:
- **Simulating stakeholder perspectives**: Anticipating potential misinterpretations or misalignments
- **Traceability**: Assisting in linking requirements to design documents and regulatory codes
- **Acceptance criteria**: Formulating clear and precise acceptance criteria based on documented requirements
- **Test scenarios**: Proposing test scenarios for comprehensive validation

**Example use case:** Generating acceptance criteria for a requirement: "R1.1-AC1: Accurately detect when the user has been sitting for 60 continuous minutes. R1.1-AC2: Notifications can be toggled on or off by user."

---

## Key Benefits

Based on comprehensive reviews of recent research, LLMs offer several key benefits in requirements engineering:

- **Automation**: Streamlining repetitive tasks like formatting, classification, and documentation
- **Consistency**: Providing uniform analysis and reducing human bias or fatigue
- **Efficiency and Accuracy**: Processing large volumes of requirements data quickly, with quality comparable to human-generated requirements
- **Enhanced Productivity**: Automating documentation processes allows developers to focus on more creative problem-solving tasks
- **Brainstorming and Idea Exploration**: Generating diverse ideas and suggestions, stimulating creativity and exploring different possibilities from multiple perspectives
- **Continuous Learning**: Adapting and improving through interactions and feedback, expanding knowledge base over time
- **Minimizing Human Error**: Reducing errors associated with manual transcription and interpretation, ensuring consistent documentation
- **Cost Savings**: Streamlining requirements gathering and analysis processes, reducing development time and manual effort
- **Accessibility**: Translating complex technical language for diverse stakeholders
- **Completeness**: Helping identify missing requirements or overlooked aspects

---

## Challenges and Limitations

Research has identified several critical challenges and limitations when using LLMs in requirements engineering:

- **Domain expertise**: LLMs may lack deep domain knowledge that human experts possess
- **Context limitations**: Limited context window may cause loss of information in large documents
- **Ambiguity handling**: Struggling with inherently ambiguous or conflicting requirements, leading to reasoning errors
- **Over-automation risk**: Risk of sidelining human expertise and missing critical nuances
- **Data security and privacy**: Concerns about sharing sensitive requirements with public LLM services; susceptibility to adversarial attacks (prompt injection, jailbreak attacks)
- **Bias**: Potential for introducing or perpetuating biases from training data, user interactions, algorithms, or contextual factors
- **Information hallucination**: LLMs may generate incorrect or purely fictional information when lacking sufficient knowledge
- **Lack of explainability and transparency**: Difficulty understanding how LLMs arrive at their decisions, which can undermine developer confidence
- **Over-reliance**: Temptation to rely too heavily on generated text without sufficient verification, potentially overlooking contextual nuances
- **Experience dependency**: Effective use requires experience in prompt engineering and RE practices

---

## Practical Considerations

**Prompt engineering** is crucial for effective LLM use in RE. Well-designed prompts should:
- Provide clear context about the project and domain
- Specify the expected output format (e.g., user stories, EARS template)
- Include examples (few-shot prompting) when needed
- Use appropriate prompt patterns (e.g., persona-based, chain-of-thought)

**Human-in-the-loop** approach: LLMs should complement, not replace, human requirements engineers. Domain experts bring essential intuition, cultural awareness, and nuanced understanding that LLMs cannot fully replicate.

---

## Research Evidence

Preliminary evaluations show that experienced requirements engineers achieve better results when using LLMs for elicitation tasks (e.g., precision rates of 53-82% vs. 15-29% for less experienced users). This highlights the importance of RE expertise in effectively leveraging LLM capabilities.

---

## References

1. C. Arora, J. Grundy, and M. Abdelrazek, "Advancing Requirements Engineering through Generative AI: Assessing the Role of LLMs," arXiv preprint arXiv:2310.13976, Nov. 2023. [arXiv](https://arxiv.org/abs/2310.13976)
2. N. Marques, R. R. Silva, and J. Bernardino, "Using ChatGPT in Software Requirements Engineering: A Comprehensive Review," Future Internet, vol. 16, no. 6, p. 180, May 2024, doi: 10.3390/fi16060180. [MDPI](https://www.mdpi.com/1999-5903/16/6/180)
3. L. Zhao et al., "Natural Language Processing for Requirements Engineering: A Systematic Mapping Study," ACM Computing Surveys, vol. 54, no. 3, pp. 55:1-55:41, Apr. 2021, doi: 10.1145/3444689.

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, explaining and formatting. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
