---
parent: Needs
title: Risks
nav_order: 3
layout: default
page_type: topic-hub
---

# Risk Management

A **risk** is *"uncertainty that, if it occurs, will affect achievement of objectives"*
{% cite hillson2009risk %}. Not every uncertainty is a risk: the test is whether you can **name the
objective it would affect**. If you cannot, it does not belong in the register. Two components
follow, the same in every standard: a **probability** that it occurs and a **loss** if it does
{% cite vanscoy1992risk %}.

![Three nested rings: all uncertainty, the part that could affect an objective, and the part that would breach your threshold](uncertainty-rings.svg)
_Risk is the subset of uncertainty that matters._ {% cite hillson2009risk %}

## 1. Risk, issue, cause

Three things routinely get filed as risks and are not.

![Where a cause becomes a risk and a risk becomes an issue](risk-or-issue.svg)
_No uncertainty left: an issue._ {% cite hillson2009risk %}

- **An issue has already happened**, or is certain to. With no probability left to reduce, an issue
  is *resolved* rather than *mitigated*: a 100-percent-probable risk is a constraint
  {% cite pressman2010risk %}.
- **A cause is not a risk.** *"Inadequate staffing"* may produce several risks — reduced quality,
  delays, turnover — and only those can be mitigated {% cite thompson2017riskstatement %}.
- **The meteor is not a risk either.** Uncertainty that could not breach your
  [threshold of success](../exp/tos) is just an event.

The SEI adopted the dictionary definition — *risk is the possibility of suffering loss* — after
printing two scholarly alternatives beside it {% cite dorofee1996crm %}: a documented choice.

## 2. Risk is not bad. Unmanaged risk is

*"Risk in itself is not bad; risk is essential to progress, and failure is often a key part of
learning"* {% cite vanscoy1992risk %}. The manager balances a risk's consequences against the
opportunity attached to it — which is why the SEI's continuous practice manages **opportunities as
well as threats** {% cite higuera1996risk %}.

![Five levels of risk-handling maturity, from crisis management to elimination](five-levels.svg)
_Risk is not bad. Unmanaged risk is._ {% cite vanscoy1992risk %}

The failure mode has a name: the *"Indiana Jones school of risk management"* — never worry about a
problem until it happens, then react heroically {% cite pressman2010risk %}. The ladder out runs
crisis management → fix on failure → mitigation → prevention → elimination of root causes; at the
first three levels the schedule battle is already lost {% cite mcconnell_rapid_1996 %}.

## 3. The paradigm

Five steps in a loop, with **communication running through all of them**: **identify → analyse →
plan → track → control** {% cite vanscoy1992risk %}. Communication sits at the centre rather than as
a sixth step; without it the approach fails.

![Five steps round a wheel, with communication through the hub](crm-wheel.svg)
_Communicate is the hub, not a step._ {% cite dorofee1996crm %}

Three named practices sit on that loop {% cite higuera1996risk %}: a **Software Risk Evaluation** is
an event, **Continuous Risk Management** is a habit, **Team Risk Management** adds the customer. The
frameworks a student will meet — SEI, ISO 31000, PMI, NASA, DoD, NIST's AI framework — are that same
loop with different governance; NIST adopts ISO's definition {% cite nist2023airmf %}. And risk management *"cannot be an audit, a check mark on a standard, or
something done only during 'risk management season.'"*

## 4. What the pages cover

| Page | The question it answers |
|---|---|
| [Identification](identification) | How do you find risks nobody has said out loud? |
| [Capturing, owning and mitigating](capturing) | How do you write one, own it and track it? |
| [Analysis and prioritisation](analysis) | Which few do you act on? |
| [Why we misjudge risk](biases) | Why is the estimate optimistic, and what do you do? |
| [Risk management in agile](agile) | What does this look like inside a two-week cycle? |

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
