---
parent: Metrics
nav_order: 4
title: Measurements
layout: default
---


# Are Your Measurements Right?

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


---
### References

{% bibliography --cited %}