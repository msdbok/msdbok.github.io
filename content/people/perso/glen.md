---
parent: Personality
title: Geeks
nav_order: 2
layout: default
---

# Paul Glen: "Leading Geeks"

This page summarises the framework set out in Paul Glen's *Leading Geeks: How to Manage and Lead
the People Who Deliver Technology* {% cite glen2003leadinggeeks %}. The characteristics,
motivators, de-motivators and leadership principles below are his; the examples and
software-specific framing are ours.

{: .warning }
**This is a practitioner framework, not a research finding.** Glen states that his account rests
on "more than fifteen years working with, leading, managing, coaching, and cajoling geeks in
academic and business environments" — experience presented as argument, with no study behind it.
It is a well-made framework and a useful vocabulary. It is not evidence, and the archetype it
describes is a **2003** characterisation of a workforce that has changed considerably since.
Where the claims below have been tested, this page says so.

**General Characteristics:**
- Respect for technology and rational thinking
- Prefer logical, analytical decisions; dislike emotional reasoning
- May struggle with ambiguity and "grey areas"
- Driven by problem-solving, sometimes more than solutions
- Dislike rote, non-creative work
- Value autonomy and personal space

**Flow (Csikszentmihalyi):**
- Thrive when moving from problem to solution
- Dislike open-ended tasks and interruptions
- Disruption of flow can be disastrous (e.g., constant meetings, unclear goals)

---

## Communication

![Dilbert communication](image-6.png)

- May equate self-expression with communication, but not always recognize miscommunication
- Can be blunt or direct; value intelligence and quick thinking
- Sometimes struggle to distinguish facts, inferences, and assumptions
- Loyalty often to job type or immediate manager, not company
- Distrust of authority and rigid rules
- May not always understand the business domain, leading to gaps in communication

---

## Groups & Authority

- Seek peer recognition and acceptance
- Competitive, which can challenge teamwork
- Prefer working alone but recognize group dynamics
- Often ignore rules, dress codes, and standards unless respected
- Value domain expertise over formal authority
- Rebels in spirit; value autonomy and personal space
- Defacto leaders may emerge based on expertise, not title

---

## Motivation & De-motivators

**What motivates technical people?**
- Inclusion in decision making
- Clear understanding of the big picture and project goals
- Consistent rewards and recognition
- Responsibility matched to control
- Effective use of technical skills
- Positive work environment and perks (e.g., flexible hours, free food)
- Opportunities for growth and learning

**De-motivators:**
- Exclusion from decisions
- Lack of transparency or hiding the big picture
- Inconsistent rewards/punishments
- Favoritism ("pet" focus on individuals)
- Responsibility without authority or control
- Poor use of extrinsic motivators (e.g., meaningless bonuses)
- Micromanagement
- Focus on tasks and "how" instead of results
- Evaluations without clear criteria
- Assigning blame for issues outside their control

*Examples of poor extrinsic motivators:*  
Giving gift cards for attendance, but not for innovation or problem-solving.  
Rewarding only those who work overtime, rather than those who deliver quality solutions.

---

## Leadership: Glen’s Ideas

- Mentor, don’t boss—guide and support rather than control
- Manage by goals, not quotas—focus on outcomes, not just numbers
- Recognize and use technical competency—let experts lead in their domain
- Accentuate the positive—be honest, not superficial
- Foster a supportive physical and social environment—address annoyances and create space for focused work
- Promote healthy interdependencies—encourage collaboration where appropriate

---

## Common Obstacles

- **Conflict resolution:**  
  Glen's advice is to address root causes rather than symptoms, on the reasoning that most issues
  stem from a few sources. *(The "80/20" framing is a rule of thumb here, not a measured
  distribution of team conflict — treat it as a heuristic.)*
- **Annoying tasks:**  
  HR paperwork, parking, and other non-technical hassles can demotivate teams.
- **Culture building:**  
  Promote honesty, fairness, and a helping team spirit. Encourage open feedback and learning from mistakes.
- **Communication flows:**  
  Facilitate open communication—avoid secrecy and silos. Make information accessible.
- **Trust and ambiguity:**  
  Build trust through transparency and consistency. Help teams manage uncertainty and change.
- **Patience and intervention:**  
  Know when to step in and when to let teams solve problems independently. Practice patience and support.

---

## Does this still hold?

Glen's central claim is that technical people "deliver most of their value through thought, not
behavior, so eliminating thought from the work reduces the value." Twenty years on, that turns
out to be the sharpest available lens on AI-assisted development:

- Vibe coding **does not remove programming expertise** — it redistributes it toward context
  management, rapid evaluation of generated code, and deciding when to take manual control
  {% cite sarkar2025vibe %}.
- Experienced developers describe AI as a **junior colleague**; less experienced ones describe it
  as a **teacher** {% cite zakharov2025teacher %}. Awareness of the tools is essentially unrelated
  to experience, so senior reluctance is a considered position rather than an information gap.
- The review work that verification requires lands on **core** developers, who in one large study
  reviewed 6.5% more code while their own output fell 19% {% cite xu2025debt %}.

Read together with Glen: if the thinking is what produces the value, then work that removes the
thinking and adds verification burden is a de-motivator by his own account — and it falls hardest
on the people the team can least afford to lose.

**Where the evidence points elsewhere.** Glen's motivator list is a framework, not a measurement.
For evidence on what actually motivates software engineers, see Beecham and colleagues'
systematic review {% cite beecham2008motivation %}; and note that Herzberg's original
motivator–hygiene work {% cite herzberg1968motivate %} — 12 investigations, 1,685 employees — was
carried out on **engineers and accountants**, which makes it unusually well-matched to this
audience.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.