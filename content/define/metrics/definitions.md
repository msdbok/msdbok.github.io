---
parent: Metrics
nav_order: 1
title: Definitions
layout: default
---


# Why metrics?

## Everything is Measurable

{: .highlight }
"Everything is measurable."

*(D. Hubbard, How to Measure Anything, 2010) {% cite hubbard_how_2014 %}*  

If **X** is something we care about, then **X**, by definition, must be detectable. Consider concepts like “quality,” “risk,” “security,” or “public image.” If these concepts were entirely undetectable, how could we care about them? The very act of caring about these concepts implies they correspond to desirable or undesirable outcomes. 

### Key Principles:

1. **Detectability**: If we care about something, it must be detectable directly or indirectly.
2. **Observability**: If it is detectable, we can observe it in some amount. For example, we can observe "more" or "less" of quality.
3. **Measurability**: If we can observe it in some amount, it must be measurable.

### Example: Measuring Quality in Art

Consider Garvin's transcendental view of quality. Imagine comparing two famous artworks: a painting by **Manet** and another by **Picasso**.

- **Question for Discussion**: Which artwork is of higher quality?  
  - This question demonstrates the subjective and context-dependent nature of quality. In art, "quality" might depend on emotional impact, technical skill, historical importance, etc. The challenge lies in defining measurable criteria for such an abstract concept.

---

## How This Applies to Software Quality

### Key Points:

- **Control During Development**: Metrics provide a structured way to control quality throughout the software lifecycle.
- **Release Validation**: Before release, metrics act as quality gates to ensure the product meets predefined standards.
- **Goal Setting**: Companies set quality targets using metrics to ensure consistent outcomes.


For instance, the **usability** attribute might map to metrics like **task success rate** or **average time on task**.

### Importance of Metrics:

- Helps identify issues early.
- Enables comparison between current and past performance.
- Provides a common language for evaluating quality.

**Takeaway**: Learning to set up the right metrics in the right way is a critical skill for software engineers.

---

## Key Definitions

### Software Quality Metric

According to **IEEE 1061**:  

{: .highlight }
“A software quality metric is a function whose inputs are software data and whose output is a single numerical value that can be interpreted as the degree to which software possesses a given attribute that affects its quality.”

### Measurement

{: .highlight }
**D. Hubbard (2010) {% cite hubbard_how_2014 %}**:  
“Measurement is a quantitatively expressed reduction of uncertainty based on one or more observations.”

{: .highlight }
**W. Sarle (1997) {% cite sarle_measurement_1995 %}**:  
“Measurement of some attribute of a set of things is the process of assigning numbers or other symbols to the things in such a way that relationships of the numbers or symbols reflect relationships of the attributes of the things being measured.”

---

## Measurement Basics

When considering any measurement, ask the following:

1. **What does the measurement represent?**
2. **How accurate is the measurement?**
3. **How precise is the measurement?**
4. **What is the resolution of the measurement?**

### Key Concepts:

- **Accuracy**: How close the measurement is to the true value.
- **Precision**: The degree to which repeated measurements under unchanged conditions produce the same results.
- **Resolution**: The smallest detectable difference between values.

**Discussion**: Why are these factors critical for developing and using metrics in software quality? How might they affect decision-making in software projects?

---

## Final thoughts

Understanding and applying software quality metrics is essential for delivering reliable, maintainable, and user-friendly systems. By focusing on measurable attributes, setting appropriate goals, and critically evaluating measurement techniques, software engineers can ensure their products meet the highest quality standards.

---

### References

{% bibliography --cited %}