---
parent: Release
title: Buffered MoSCoW
nav_order: 2
layout: default
---

# Part II – The Buffered MoSCoW Method

_adapted from Miranda, 2104_

---

## 1. MoSCoW vs Buffered MoSCoW

| Priority      | Classic Definition                                 | Buffered MoSCoW Interpretation                      |
|:-------------|:---------------------------------------------------|:----------------------------------------------------|
| **Must Have**| Essential for success; without them the project fails. | Features almost certainly deliverable within the time box. |
| **Should Have**| Important but not vital.                          | Features with a fair chance of delivery.            |
| **Could Have**| Desirable improvements.                            | Delivered only if higher priorities finish early.    |
| **Won’t Have**| Out of scope.                                      | Deferred to later releases.                         |

---

### Figure 2 – DSDM Buffering Scheme

```
|<------60% Must------>|<---20% Should--->|<---20% Could--->|
                ^ buffer absorbs uncertainty ^
```

The buffer protects the *Must Have* scope by absorbing estimation variability.

---

## 2. Six-Step Buffered MoSCoW Process

1. **List & rank** features by business value.  
2. **Estimate** nominal and worst-case effort for each.  
3. **Fill the time box** (using worst-case estimates) to define the Must Have set.  
4. **Assign remaining capacity** to Should and Could features.  
5. **Execute** with nominal estimates.  
6. **Adjust scope, not schedule**, as variation occurs.

---

## 3. Numerical Example

**Budget:** 180 hours total  
- 60 h management/design/technical  
- 120 h for feature development

| Feature | Nominal | Worst | Dependencies |
|:--------|-------:|------:|:------------|
| A       | 20     | 40    | B, C        |
| B       | 7      | 9     | –           |
| C       | 20     | 30    | –           |
| D       | 5      | 7     | E           |
| E       | 6      | 7     | –           |
| F       | 5      | 6     | –           |
| G       | 20     | 40    | –           |
| H       | 10     | 20    | J, K        |
| I       | 15     | 30    | –           |
| J       | 12     | 15    | –           |
| K       | 8      | 10    | –           |
| L       | 10     | 18    | –           |

**Preferred order:** F, D, A, G, K, E, L, J, H, I, B, C

---

### Step 1 – Must Have (120 h budget, worst-case)  
F + D + E + A + B + C + K ≈ 109 h used.  

### Step 2 – Should & Could  
- G → Should (40 h worst case)  
- L → Could (18 h worst case)  
- H, I, J → Won’t Have  

---

### Figure 3 – Buffered MoSCoW Project Structure

```
 ---------------------------------------------------------
|                TIME BOX  (180h total)                   |
|  Must Have (worst-case filled)  |  Should  |  Could  |→|
|  <-- buffer zone absorbs overrun -->                     |
 ---------------------------------------------------------
```

---

## 4. Behavior During Execution

Example: Feature “A” takes **40 h** instead of 20 h.  
→ Buffer absorbs the overrun; schedule stays fixed.  
Lower-priority features (Could) may be dropped.

Buffered MoSCoW can be applied at project or increment level.

---

## 5. Handling Uncertainty and Changes

**Technical / Infrastructure Work**  
- Consume capacity but not prioritized by business value.  
- Can be distributed across releases or done upfront.

**Changes**  
- Accepted only by removing other features.  
- Include rework effort in estimates.

**Defects**  
- Critical defects fixed immediately.  
- Minor defects postponed or deferred.

---

## 6. Extent of the Guarantee

Results at project level are consistent with lower-level assumptions.  
If assumptions are wrong → results will be consistently wrong.

---

## 7. References

[1] E. Miranda, “Time boxing planning: buffered moscow rules,” SIGSOFT Softw. Eng. Notes, vol. 36, no. 6, pp. 1–5, Nov. 2011, doi: 10.1145/2047414.2047428.


---
{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.