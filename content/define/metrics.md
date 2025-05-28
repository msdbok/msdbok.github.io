---
parent: Define Quality
nav_order: 4
title: Quality Metrics
---


## Learning Goals

By the end of this lecture, students should be able to:
1. Define **measurement** and **metrics**, especially in the context of software quality.
2. Recognize common pitfalls in measurement and how to avoid them.
3. Evaluate measurement data in terms of scale, precision, reliability, and validity.
4. Develop valid metrics for specific quality concerns.
5. Critically assess new metrics for their usefulness and applicability.
6. Design and implement a successful metrics program while mitigating potential risks.

# Part 1: Why metrics?

## Everything is Measurable

> *(D. Hubbard, How to Measure Anything, 2010) {% cite hubbard_how_2014 %}*  
> "Everything is measurable."

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
> “A software quality metric is a function whose inputs are software data and whose output is a single numerical value that can be interpreted as the degree to which software possesses a given attribute that affects its quality.”

### Measurement
**D. Hubbard (2010)**:  
> “Measurement is a quantitatively expressed reduction of uncertainty based on one or more observations.”

**W. Sarle (1997) {% cite sarle_measurement_1995 %}**:  
> “Measurement of some attribute of a set of things is the process of assigning numbers or other symbols to the things in such a way that relationships of the numbers or symbols reflect relationships of the attributes of the things being measured.”

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

## Summary

Understanding and applying software quality metrics is essential for delivering reliable, maintainable, and user-friendly systems. By focusing on measurable attributes, setting appropriate goals, and critically evaluating measurement techniques, software engineers can ensure their products meet the highest quality standards.

# Part 2: What Can Go Wrong with Metrics

## Common Pitfalls in Using Metrics

### **"Dilbert Gets Rich" Comic**
![Dilbert gets rich](http://dilbert.com/strips/comic/1995-11-13/)  
This comic humorously illustrates how metrics, when misunderstood or misapplied, can lead to absurd outcomes.  

### Key Issues:
1. **Bad Statistics**  
   - Misunderstanding of measurement theory or what is actually being measured.  
   - Examples: Using averages without considering distribution, or treating ordinal data as interval data.

2. **Bad Decisions**  
   - Misinterpreting data, leading to decisions with unintended consequences.  
   - Example: Releasing a product based on incomplete metrics without accounting for critical quality gaps.

3. **Bad Incentives**  
   - Ignoring human factors and cultural dynamics in the organization.  
   - Example: Employees gaming metrics to meet targets rather than improving actual outcomes.

---

## The Dangers of Using Software Metrics to (Mis)Manage

Metrics can have unintended consequences when misused in organizational management.  
- **Behavioral Changes**: People often modify their behavior to meet metrics rather than to achieve real objectives.  
- **Unintended Side Effects**: Misguided focus on metrics may overshadow the true goals of quality and productivity.  
- **Productivity and Quality Risks**: Metrics misuse can lead to reduced productivity and lower quality, negating the original intent of the metrics.

### **Example from the Field**  
> “The Darker Side of Metrics,” Eighteenth Ann. Pacific Northwest Software Quality Conf., 2000. {% cite hoffman_darker_2000 %} 

This research highlights how metrics, while well-intentioned, can lead to counterproductive outcomes:
- **Metrics Compliance Over Goals**: Teams focusing on meeting numerical targets instead of solving real problems.
- **Cultural Resistance**: Negative reactions to being monitored can result in mistrust and lower morale.

**Takeaway**: Organizations must consider the broader implications of metrics and design systems that encourage genuine improvement without harmful side effects.

---

## Metrics Biases and Fallacies

Several biases and logical fallacies can lead to the misinterpretation or misuse of metrics. Understanding these is crucial to avoid pitfalls.

### **1. Streetlight Effect**  
> Looking for answers only where it is easiest to measure, ignoring more relevant but harder-to-measure factors.  
**Example**: Prioritizing easily quantifiable metrics like lines of code over less tangible but critical aspects like code maintainability or team morale.

### **2. McNamara Fallacy**  
> Relying solely on quantifiable data while ignoring qualitative insights.  
- **Step 1**: Measure what is easy to quantify.  
- **Step 2**: Disregard what cannot be quantified.  
- **Step 3**: Assume what cannot be measured is unimportant.  
**Example**: Judging software quality solely by defect count while ignoring user experience feedback.

### **3. Wrong Correlations**  
> Mistaking correlation for causation.  
**Example**: Assuming that a higher number of commits directly leads to higher productivity without considering the nature of those commits.

### **4. Confounding Variables**  
> Ignoring external factors that influence metrics.  
**Example**: A team’s productivity drops after introducing a new tool. The metric ignores the learning curve required for the new tool.

### **5. Misrepresentation**  
> Presenting metrics in misleading ways.  
**Example**: Using pie charts to compare metrics with vastly different scales, making differences appear smaller than they are.

---

## Summary

To use metrics effectively, avoid common biases and consider the broader context in which metrics are applied. When metrics are carefully selected, properly applied, and paired with qualitative understanding, they can drive significant improvements. However, without careful thought, they can lead to poor decisions, counterproductive behaviors, and unintended consequences.

**Discussion**:
1. How might the "streetlight effect" influence decision-making in software projects?
2. Can you think of examples where metrics-driven incentives backfired in real-life scenarios?  
3. How can organizations strike a balance between measurable outcomes and intangible quality goals?


# Part 3: Are Your Measurements Right?

## Representation Condition
A numerical model should make sense in terms of the real-world entity it describes.  
### Formal Definition:  
A measurement should map real-world entities into numbers and real-world relations into numerical relations, ensuring that the real-world relations are preserved in the numerical ones.  
**Example**: Lines of Code (LOC) satisfies the representation condition for physical program size but not for functional program size.

### Key Measurement Properties:
- **Resolution**: The smallest change in a quantity that can be detected by a measurement.
- **Accuracy**: How close a measured value is to the true value.
- **Precision**: How consistently a measurement produces the same result under the same conditions.

---

## Scale. Based on Stevens (1946) {% cite stevens_theory_1946 %} 
The **scale** of data dictates the type of analysis and arithmetic that is meaningful.  

### Types of Scales:
1. **Nominal**: Categories without any order (e.g., defect priority levels: high, medium, low).
2. **Ordinal**: Ordered categories without magnitude (e.g., 1st, 2nd, 3rd in a race).
3. **Interval**: Ordered with magnitude, but no true zero (e.g., temperature in Celsius).
4. **Ratio**: Ordered with magnitude and a true zero (e.g., defect discovery-to-resolution ratio).
5. **Absolute**: A special case of ratio scales, where the values are fixed and countable (e.g., number of test cases).

### Example Application:
- A **ratio scale** is used to calculate the number of defects found versus fixed during testing. A ratio greater than 1 indicates more defects are being found than fixed.
- A **nominal scale** is used when categorizing defect severity in a defect-tracking database.

**Important Rule**: Do not mix values from different scales (e.g., combining ratio and ordinal values) as it can render measurements meaningless.

---

## Understanding Data

### Averages: Mean, Median, and Mode
- **Arithmetic Mean**: The sum of values divided by the count. Commonly referred to as the "average."  
- **Median**: The middle value in a sorted dataset. Useful for skewed distributions.  
- **Mode**: The most frequently occurring value in the dataset.  

#### Additional Types:
- **Geometric Mean**: Useful when averaging rates or ratios. It normalizes differences in numeric ranges.
- **Harmonic Mean**: Appropriate for averaging rates (e.g., speed, productivity). It is always the smallest of the three Pythagorean means (arithmetic, geometric, harmonic).

**Example of Geometric Mean**:  
Comparing two companies based on environmental sustainability (0–5 scale) and financial viability (0–100 scale). The geometric mean prevents the larger numeric range (financial viability) from dominating the result.

---

### Range, Standard Deviation, Skewness, and Kurtosis

1. **Range**: The difference between the largest and smallest values in the dataset.  
2. **Standard Deviation**: Measures the amount of variation or dispersion from the mean.  
3. **Skewness**: Indicates the symmetry of the data distribution.  
   - Positive skew: Tail extends to the right.
   - Negative skew: Tail extends to the left.
4. **Kurtosis**: Measures the "peakedness" of a distribution.  
   - **Normal Distribution**: Kurtosis = 3 (or 0 in Fisher's definition).  
   - Higher kurtosis: More flat.
   - Lower kurtosis: More peaked.

---

### Correlations

**Definition**: Correlation describes whether two variables are associated.  
- **Key Insight**: Correlation does not imply causation.  
  **Example**: Children's height and vocabulary are correlated due to age, but one does not cause the other.

**Scatter Plots**: A vital tool for visualizing relationships between two variables.  
Questions to ask when interpreting scatter plots:
- Are variables X and Y related?  
- Is the relationship linear or non-linear?  
- Are there outliers or influential points?  

#### Common Issues with Correlations:
1. **Confounding Variables**: A third variable influencing both X and Y.  
   - Example: Khaled El Emam et al. (1999) found that only 4 out of 24 commonly used object-oriented metrics were useful for predicting software module quality when controlling for module size.
2. **Spurious Correlation**:  
   - Both variables change over time.  
   - Incorrectly swapping response and explanatory variables.  

**To Establish Causation**:
- Provide a theory supported by domain knowledge.
- Show correlation between variables.
- Validate the model with new, independent data.

---

### Statistical Significance

**Definition**: Statistical significance measures the probability that an observed effect is not due to random chance.  

**Best Practices**:
- Blindly calculating statistics is dangerous without assessing their significance.
- Sanity check your data and results before drawing conclusions.
- Use replication and validation to ensure results hold for new cases.

---

## Key Takeaways

1. Measurements must preserve real-world relationships to be valid.
2. Understanding the scale of data is critical for meaningful analysis.
3. Averages and measures of variation must be used appropriately, with attention to skewness and kurtosis.
4. Correlation is not causation. Always investigate deeper to avoid misleading conclusions.
5. Ensure statistical significance and sanity check results before acting on them.

**Discussion**:
1. Why is it important to distinguish between scales of measurement in software quality metrics?  
2. How can confounding variables impact the validity of a software quality model?  
3. What strategies can you use to establish causation, not just correlation, in your metrics?


# Part 4: How to Develop Metrics or Measurements

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

# Part 5.  Examples and Discussions

## McCall Model Mapping

![McCall Use-Factor-Criteria-MetricsMap](http://www.plantuml.com/plantuml/png/ZL9jQiCm3FtVK_Xt87VeQ3SOhAoqtG4yvMK872T8Ic6tdw2XhYc4_KY8NfxUX_5MBOeDdBiXJfic76WNKmfVYlOjaetIxeGDmh4zm8H9DqqJZZ9sCrdud23HUCmEDhuKlpcn_VhausuSXZapEU6A3DKR_4BatroOuOJ4rQPJPebqrydAQiXKXAS4ksk6rxvduaBOuyg49xXsVknnyWLTQlWmwqgSiuclp8AkTFA8n8e2B0dUSuS9_ig4suyF_F2ZzXcfR_TG4fxgSxgu9MBXXaFaRFuKxBzfQjDm7CMAI7sWw_d31Mhh_hNTSvEjootNxGy0)

*Figure. McCall Use-Factor-Criteria-Metrics Mapping*

### For Product Operation:
- **Usability**:  
  - Communicativeness: How easily users can communicate with the software.  
  - Accessibility: How easily users with disabilities can interact with the software.

- **Reliability**:  
  - Accuracy: The correctness of the software's outputs.  
  - Consistency: The ability of the software to perform in the same way across different environments.  
  - Completeness: The extent to which the software meets its functional requirements.

- **Efficiency**:  
  - Device Efficiency: The ability of the software to function across different devices (e.g., desktop, mobile).  
  - Accessibility: Ensuring that performance is consistent, even with accessibility features enabled.

### For Product Revision:
- **Reusability**:  
  - Accuracy: The accuracy of reused components.  
  - Structuredness: How organized the code is for easy reuse.  
  - Conciseness: The brevity and clarity of reusable components.  
  - Device Independence: The software’s ability to function on various platforms without requiring significant adaptation.

- **Maintainability**:  
  - Structuredness: Organized code that is easy to navigate and modify.  
  - Conciseness: Code that avoids redundancy and is more maintainable.  
  - Legibility: Clear and easy-to-read code that facilitates understanding.

- **Portability**:  
  - Completeness: Ensuring all necessary dependencies are included for portability.  
  - Device Independence: How well the software operates across various devices.

- **Testability**:  
  - Structuredness: Code that is easy to test by ensuring a clear structure.  
  - Legibility: Readable code makes it easier to design and execute tests.  
  - Traceability: The ability to trace tests back to specific requirements or components.

---

## Metric Decomposition

![Metrics Decomposition Example](http://www.plantuml.com/plantuml/png/LP31QiCm44Jl-GgTVUal1De4UYY493-mjSRkWhGogrL9-_ML8eFhWozlPhoZEMOZjSZY8os7mNqGYzMFFZcm_Ho6mRqcLOosaS6TgGJBLIbY3LHJIBaet9qZEddFAP3XvSoFZVQakvBX-QFJD2MrBbsHKz4HxgBmF1edwK8tkTDZWNYsecYrxiYxJc-O5N1fUYeiSm_VZ0mHOhNjDvJc5bxZxX98AezBW46GyxvKEqdYroixhJtvYsH67w45DzHDEtJZN_m7VO8ZnA_R_m40)

*Figure. Metrics Decomposition*

### Maintainability

Maintainability can be broken down into several key sub-metrics:

1. **Correctability**:  
   - Measures how easy it is to fix faults in the software.  
   - Includes sub-metrics like:  
     - **Faults count**: Number of faults found.  
     - **Closure time**: Time taken to close a fault.  
     - **Isolate/Fix time**: Time spent diagnosing versus fixing issues.  
     - **Fault rate**: Faults per 1,000 lines of code.

2. **Effort**:  
   - Measures the resources required to make corrections or improvements.  
   - Includes:  
     - **Resource prediction**: Estimating the effort required.  
     - **Effort expenditure**: Actual resources spent.

3. **Testability**:  
   - Focuses on the extent and quality of testing.  
   - Sub-metrics include:  
     - **Degree of testing**: E.g., statement coverage and test plan completeness.  
     - **Effort**: Resources spent on testing.

4. **Expandability**:  
   - Measures how easily changes can be made to the software.  
   - Includes:  
     - **Effort**: Time or resources for implementing changes.  
     - **Change counts**: Number of modifications.  
     - **Change effort**: Average effort per change.  
     - **Change size**: Volume of code modified.

---

## Object-Oriented Metrics

When working with object-oriented programming, several key metrics help evaluate software quality:

1. **Number of Methods per Class**: Indicates the complexity of a class.  
2. **Depth of Inheritance Tree**: Measures how deeply a class is inherited.  
3. **Number of Child Classes**: Tracks the number of subclasses for a class.  
4. **Coupling Between Object Classes**: Evaluates how interconnected different classes are.  
5. **Calls to Methods in Unrelated Classes**: Measures the extent of cross-class interactions.

---

## Maintainability Index

### Definition

The **Maintainability Index** is a single number representing the maintainability of code, calculated using:

Maintainability Index = MAX(0, (171 -  
      5.2 * log(Halstead Volume) -  
      0.23 * (Cyclomatic Complexity) -  
      16.2 * log(Lines of Code)) * 100 / 171)

Where:
- **Halstead Volume** relates to the complexity of code based on distinct operators and operands.  
- **Cyclomatic Complexity** measures the number of independent paths through a program’s code.  
- **LOC** refers to Lines of Code.

### Origins

The Maintainability Index was introduced in 1992 by Paul Oman and Jack Hagemeister. It was based on statistical regression analysis across various metrics in systems coded in C and Pascal.

### Practical Use

- Low values (close to 0) indicate hard-to-maintain code.
- High values (approaching 171) suggest well-structured, maintainable code.

### Design Considerations

From Microsoft’s design rationale:
- If the index shows **red**, it indicates a high likelihood of maintainability issues.
- The focus is on identifying problematic areas with a high degree of confidence.


> "We noticed that as code tended toward 0 it was clearly hard to maintain code and the difference between code at 0 and some negative value was not useful."

> "The desire was that if the index showed red then we would be saying with a high degree of confidence that there was an issue with the code."

[Source. MSDN blog](https://learn.microsoft.com/en-us/visualstudio/code-quality/code-metrics-maintainability-index-range-and-meaning)

---

## Examples of Commonly Used Automated Metrics

### Development Metrics:
- **Lines of Code (LOC)**: A simple yet widely used productivity metric.  
- **Test Coverage**: Ensures the completeness of tests, with variants like line coverage or branch coverage.  
- **Cyclomatic Complexity**: Highlights potential maintenance issues by measuring complexity.

### Performance Metrics:
- **Response Time**: Measures how quickly the system responds to user requests.  
- **Throughput**: The number of transactions or tasks handled in a given time.

### Reliability Metrics:
- **Mean Time to Failure (MTTF)**: Average time until a failure occurs.  
- **Mean Time to Repair (MTTR)**: Time taken to recover from failures.

### Security Metrics:
- **Code Reviews**: Evaluating adherence to security practices like input validation and secure coding standards.  
- **Static Analysis Tools**: E.g., Bandit, Snyk, used for automated security checks.

### Maintainability Metrics:
- **Cyclomatic Complexity**: Again used to assess maintainability.  
- **Tech Debt**: Metrics like SQALE and SONAR evaluate technical debt.  
- **Dependency Analysis**: Helps to understand and manage code dependencies and change impacts using methods like Design Structure Matrix.


## Example: ISO 25002 Attributes-Metrics Mapping

In software engineering, quality attributes such as **reliability**, **usability**, or **maintainability** require **metrics** to measure the extent to which these attributes are present in a system. Metrics allow us to analyze quality during development and validate it during release.

![Attributes-metrics mapping example](http://www.plantuml.com/plantuml/png/RLXjSjou4VtlKtHLeggrQosDlLOYgrAfbLPIhIghsD67_qDW3mSn2J3enaZZ6-GUkK2kaAFa90iqcn-Kvzy83Ju-l7xTQEfdOXEvTRvgJVVg3VmZcSRn3iwOetjCZ0G_NDzzWlV7gzNxrw_Ul86hv2sxu6LVNdW3TycnUNJwTrxu9SI8bfTRJ-40mXeOYS4QGeBE4645F-1XVVWZV3m-U3qytdQDCzuYF3dUp63W5l-LNCGMFTCf_A40jex8-HhMQ3X5f05lzLr4uE7CsXIDLQgV8rf76Rn0tIAbfW1VuDOPBglh65h0vmujOmLRqoGSNl2__wuEL-yWUSSqClVaYD7RtGBlYucAvpn4xD0Kj92uIpmI_ilxNW2uzemnT1XLr4cLZD4lzS9SFZF68ilTZXZRGH7d6Uke_8rhvggyEtgtccyWsQ7qBmoR36etnjSu2gM9gqgGe_6qnXYn0YDnncOtfl3ZuKSzmvJ37lgisc34ab8ESCV6LoPMLA3jYsndjnrTN_u2f9icwglLu91Rh5DZECJTx4Lw-ZZ5jYuqSih953sxEypKLLbn11ALv74CJU6Kl4cy2T5zatDAs31Zsp515t6Bdh6Q4riew6tSTUMzft3k61hqDMyADnmZa2Rhv-Bwqzj7nt1sUQSuNrBZn_p3ZV6c5jEVmhrhHSE859ej0kbHO3jxnE7agWydi0afPek-4kKQDxDLXkQP4bUzM-3MCAgR9WTr6A4DdZSZxJ5s9ElA_Q7Zml4pHekUCt4ra3XQwrXsp5mZjX42gM6u3mt6oJkNCOQOcTkmnRWJ1KxX1eq77iMGc5PhsJwTF_kTSjXNMgHQB1FUNOTOpOMLbWXcpHZrX2FNdvPW2h8ir7DZlwOEZAzoc3X4LChZ6tJLm3er3JpA_abKoHQiGuHtz-U3hnmPOfnKAFBcBMrl_8E-EbK6h9HyfK_Db3uvw7tmG7CNFFWAenJS_2GZuT_GnEpbNuLOx5jmLG8SZVDWmECJ99fUz44jfvshCT6nTCIBO5FniVX0AesmO1ekZRgQHy7gOt_zS7Gyda0hhQUq95ku59H9x0LNOpSEjmWdgmFeObWxwwHF3vbTKFwR3qyDLZLcmHczifNxoz1NwfiMSaQs_LtNx5Jpz_24-7Mqtycn4lxqifzV6i82-7UpTRNg8GLd6sSp08VnBM3AppPuUVi0_Vz__-SdtQoixqjK6Y8MF5NYh1YqHYcM1UfNtEbnzhjRXW1ZsMtH8v5MDs7iRwYriGWNIAxsS2i9_2wX3zVBxAaOYd9ds5564QvtAMvnHnDTcaV9XeYZkmx_V7JSs_XoFUJnrMZOSznaIKCShWhgWgUNDTZ5q7TryGWIJ_r2DHWqtSIGwasNMBhYQGQK_GGRuwi6gz8NzP6nXbUh0PQEScZe5HHIj0WFx1htJLAk1VBveHHaFILBl2RhIJPZDUKeXpnyU2kAaFGofNg3RNyZUagjt38JNYknnQrpd5dUdEjrRJfZHslUc6VNfXP-2wQ2Nyin9Rbv6IW76ZOUGoBDDQMk2t5n7_wuMgqaElPSQvhnDaD3AQ9S_jtKnQ32Efggh_tagr9Bpz1a2cDgZhLvtHZdsRXv_SEPDytkswB2Bl0nrNNnuJBtJR16Ygh2DTfPvgK5l9vVEjTLAVxiCQ6b3f3Sw2tZT0DMKAKeJMnyw-Hw5LdcgWN5cr1Dw4kMBbUftFbWvJaQUUeLKSJJc78-gqp7WbKA8qG-pMOWBdHD2HLI7AHRnscG7e7_c1qXe3emwwp42yPNvSbfmAqZaepFvwccSG8RLxCK1Cvp35MoaqDM4X3yGHQuRZjZkSyZENevVZe9puVEBcBbxCnt7qzKw7ka1MbPo5BqjQ20DbG8mttvk0EJEBIcm34IBngugYiRHDqhDAIJ-BwRHf70J5yxinRREfyOTHxx7E94TKpXSkxtQrUdA6_EyNycOh75qYwIOFaX-KM_TJ5usJYK9LHcfsUvQl1P3o3NCdPDs9NDciBPutiA_7WH7pvQY4tJBAZhsbvtzo6WiEOd4t4aEUcp1qEASgn2DmkHV3nyD_kDNoDlytc9KMVAgHdBr8z-KTrnYDaiVUCi5mi3RKp4QgdCyijj_qVQ9zvW7B_Gn7lQjfVABdl5BNQDiRXtOj3OY-y1MTHHeGi-1qTwa-dsqbn2Ib2ULxO3z7upwDVFp-Wh_I_2xm00)

*Figure. Mapping ISO 25002 Software Quality Attributes to Metrics*


---
### References

{% bibliography --cited %}