---
parent: Metrics
nav_order: 6
title: Examples
layout: default
---

# Examples and Discussions

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