---
parent: Metrics
nav_order: 5
title: Development
layout: default
---

# How to Develop Metrics or Measurements

## Measurement Validity

### Key Types of Validity:

1. **Construct Validity**: Are we measuring what we intended to measure?  
2. **Predictive Validity**: To what extent can the measurement explain or predict another characteristic of the entity being measured?  
3. **External Validity**: Can the findings be generalized to other contexts and environments beyond the one studied?

---

## Basili’s Goal, Question, Metrics (GQM) Framework {% cite basili_applying_1993 %} 

### Framework Overview:

1. **Conceptual [Goal]**: Define the objectives (scope, purpose) for measurement.  
2. **Operational [Question]**: Identify what quantifiable information is required to assess progress toward the goal(s).  
   - Questions help refine the focus of metrics by defining required attributes and characteristics.  
   - Additional questions can minimize potential side effects of collected measures.  
3. **Quantitative [Metric]**: Specify the attributes, definitions, and observation frequency for measurement data.  
   - Metrics must include measurement theory, statistical design, and applicability.

---

## Operational Definition {% cite park_software_1992 %}

An **operational definition** explains a characteristic in terms of how it is measured.  
### Criteria for a Good Operational Definition:

1. **Communication**: Does the definition clearly describe what is being measured, how it is measured, and what is included/excluded?  
2. **Repeatability**: Can others replicate the measurement process and achieve the same results?

**Examples of Operational Definitions**:  

- Software Quality Measurement: Counting problems and defects.  
- Software Effort and Schedule Measurement: Counting staff-hours and reporting schedule data.  
- Software Size Measurement: Counting source statements.

References:

- *Software Quality Measurement* (CMU/SEI-92-TR-22, ADA258556)
- *Software Effort and Schedule Measurement* (CMU/SEI-92-TR-21, ADA258279)
- *Software Size Measurement* (CMU/SEI-92-TR-20, ADA258304)

---

## Measurement Development Process

### Stage 0: **GQM (Why Measure?)**

- Clearly define the purpose of the measurement and its goals.

### Stage 1: **Conceptual Definition**

- Define the characteristic in terms of familiar concepts.
- For complex characteristics, break them into sub-characteristics for clarity.

### Stage 2: **Operational Definition**

- Translate conceptual definitions into measurable terms.  
- Validate that the defined measures adequately describe the characteristic.  

### Stage 3: **Measurement Instrument Implementation**

- Implement operational measures into tools or instruments for data collection.  
- Address challenges like large data requirements, storage, and manipulation.  
- Ensure tools align with the defined measures for consistency and reliability.

### Iterative Process:

- Return to previous stages if revisions are needed.
- Update subsequent stages to reflect any changes.

---

## Validity and Reliability

### Definitions:

- **Validity**: The extent to which a measurement instrument measures what it is intended to measure.  
- **Reliability**: The extent to which an instrument produces consistent results under the same conditions on repeated trials.

---

## Six-Step Process for Developing Metrics

![Six-Steps](http://www.plantuml.com/plantuml/png/9SpFQiCm3CVnkvz2Bn33_co7x9AnGKw1hIszYqIX0biEbbn8dxvsUnCVlleDQfYjnE0UX-jVFFpIoa8m9WpwvVfN3oC9PJI2_q9gdAJvcuVZHZElEqo4MZ8rVM__LmffgpfVK5XZymyFPmoyj1MK1Ru5mtuZO843OUXE7Abcdnv-aYnbDlXBQjsKib5yrifrI2rjRg2Qn707)

*Figure.Six-Step Process for Developing Metrics*

1. **Develop Goals**: Define project business and measurement goals for productivity and quality.  
2. **Generate Questions**: Use models to generate questions that quantitatively define the goals.  
3. **Specify Measures**: Identify the data to be collected to answer the questions and track process/product conformance.  
4. **Develop Mechanisms**: Create tools and mechanisms for data collection.  
5. **Validate and Analyze in Real-Time**: Collect, validate, and analyze data to provide actionable project feedback.  
6. **Post-Mortem Analysis**: Analyze collected data after project completion to assess conformance and recommend future improvements.

---

## Key Takeaways

- Effective measurement requires clarity, validity, and repeatability.
- The GQM framework provides a structured approach to developing meaningful metrics.
- Measurement development is iterative, often requiring adjustments and refinements.
- Valid and reliable metrics form the foundation for actionable insights and continuous improvement.

**Discussion**:

1. How can construct validity affect the usefulness of a metric?  
2. What are some challenges in implementing measurement instruments for complex software characteristics?  
3. How can post-mortem data analysis inform future project planning?

---

### References

{% bibliography --cited %}