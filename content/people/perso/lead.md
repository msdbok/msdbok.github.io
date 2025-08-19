---
parent: Personality
title: Leadership
nav_order: 4
layout: default
---

# Leadership styles by Daniel Goleman

Source: Goleman, Daniel. "Leadership that gets results." Leadership perspectives. Routledge, 2017. 85-96.

## Brief

Leadership style is the habitual way a leader interacts with their team — how they make decisions, motivate people, manage change and handle crises. Daniel Goleman identifies **six** distinct styles (coercive, authoritative, affiliative, democratic, pacesetting, coaching); each arises from different emotional-intelligence competencies and affects team climate and performance differently. The best leaders are flexible: they know multiple styles and switch to the style(s) that fit the situation.

---

## The six styles (Goleman)

1. **Coercive** — _“Do what I say”_  
    Commanding, top-down control. Fast decisions, high discipline; damages flexibility and morale if overused. Good for real crisis or problem employees.
    
2. **Authoritative (visionary)** — _“Come with me”_  
    Sets direction and purpose while allowing people to choose how to achieve it. Highly positive effect on clarity, commitment and innovation. Great for change or when vision is needed.
    
3. **Affiliative** — _“People come first”_  
    Emphasizes emotional bonds, harmony and morale. Useful for repairing trust and boosting team cohesion; beware of letting poor performance go uncorrected.
    
4. **Democratic** — _“What do you think?”_  
    Builds consensus and ownership by involving team members in decisions. Increases responsibility and buy-in but can produce slow decision-making.
    
5. **Pacesetting** — _“Do as I do, now”_  
    Leader sets very high performance standards and leads by example. Works for small teams of highly capable self-starters, but often demotivates others and erodes climate.
    
6. **Coaching** — _“Try this”_  
    Focuses on individual development and long-term performance improvement; builds skills and engagement over time. Highly positive but time-consuming and only effective when people want to grow.
    

---

## Comparative table

|Style|When to use|Short-term effect|Long-term climate impact|Typical software-team example|
|---|---|---|---|---|
|Coercive|Crisis, incident response, flop/turnaround|Quick compliance|Negative if prolonged (low morale, less innovation)|Emergency incident commander during a major outage (silos, fast rollback).|
|Authoritative|New vision, strategic pivots|Aligns and energizes|Very positive (clarity, commitment)|CTO sets product mission and OKRs; teams choose implementation.|
|Affiliative|Repair trust, high stress / post-layoffs|Immediate morale boost|Positive for relationships but may allow slack|Team lead emphasizes wellbeing after stressful release; organizes socials/hack days.|
|Democratic|Need buy-in, generate solutions|Slower decisions, more ideas|Positive (ownership) if team is competent|Facilitating architecture decisions in cross-functional squads (retros, design reviews).|
|Pacesetting|High-performing, short-deadline tasks|Fast delivery from top talent|Often negative (burnout) if long-term|Startup founder demanding rapid MVPs; specific sprints where speed > process.|
|Coaching|Talent growth, next-level capabilities|Slower immediate output|Positive (skills, retention)|One-on-one mentoring, pairing, career development plans, internal training.|

_(Table based on Goleman; impact ratings drawn from his climate research)._

---

## Strengths & weaknesses

- **Coercive**
    
    - (+) Rapid alignment under pressure; decisive.
            
    - (−) Kills creativity, lowers morale; stifles initiative.
        
- **Authoritative**
    
    - (+) Strong alignment, clarity, motivates innovation.
            
    - (−) Can alienate teams of experts if leader lacks domain credibility.
        
- **Affiliative**
    
    - (+) Raises trust and team cohesion.
            
    - (−) Risk of avoiding hard feedback; may tolerate mediocrity.
        
- **Democratic**
    
    - (+) Generates buy-in, surfaces ideas.
            
    - (−) Time-consuming; can create indecision.
        
- **Pacesetting**
    
    - (+) Excellent short-term throughput with elite teams.
            
    - (−) Causes burnout; undermines teamwork and learning.
        
- **Coaching**
    
    - (+) Builds long-term capability and engagement.
            
    - (−) Requires time and leader skill; not fast for immediate crises.
        

---

## How to choose and combine styles — practical advice for project managers

1. **Diagnose the situation first.** Is it a production outage, a strategic pivot, a morale problem, or individual development? Match the style to the need: coercive for outage; authoritative for new product direction; affiliative after stressful releases; democratic for design choices; pacesetting for short, critical pushes with proven talent; coaching for long-term growth.
    
2. **Use blends, not bans.** Most effective leaders regularly mix authoritative + coaching + democratic + affiliative depending on people and timing. Pacesetting and coercive are occasional emergency tools.
    
3. **Be explicit with the team.** If you shift to a pacesetting mode for a crunch, say so: “We’ll be in intense delivery mode for two weeks, then we’ll pause for refactor and recovery.” Explicit signals reduce confusion and resentment.
    
4. **Measure outcomes, not just activity.** Use OKRs / measurable goals to retain authoritative clarity while letting teams decide the “how.” (Google-style OKRs are widely used for this purpose). [Rework](https://rework.withgoogle.com/en/guides/set-goals-with-okrs)
    
5. **Protect flow and focus.** For software engineers, interruptions harm output. Use authoritative style to set the mission and boundaries, and affiliative/coaching to protect developer time (e.g., blocked calendar for “focus time”). Research & industry practice emphasize dedicated maker time and protected uninterrupted work. _(See the “maker time” / focus-day patterns in many tech orgs.)_ 
    

---

## Concrete software-engineering examples & mini-case studies

### 1. Incident response — **Coercive + Authoritative (short burst)**

- Scenario: Critical production outage (major customer-facing failure).
    
- What to do: Assign a single incident commander who issues concise directives to stop the bleeding (coercive for the moment), then immediately convert to authoritative to align on post-incident vision (prevent recurrence).
    
- Why: Speed matters in outage; later you need clarity & learning to restore resilience.
    

### 2. Setting product direction — **Authoritative + Democratic**

- Scenario: Company pivots to a new product-market fit.
    
- What to do: Senior tech leader articulates the vision and OKRs; squads are invited to propose technical approaches and own delivery plans (democratic input but authoritative ends).
    
- Example: Many organizations use OKRs to set objectives while teams decide implementation details (a Google best-practice).
    

### 3. Sparking innovation & cross-team learning — **Affiliative + Coaching**

- Scenario: Want to boost engagement, creativity, and cross-pollination.
    
- What to do: Run hackathons or “innovation days” where teams can work on pet projects; leaders support and celebrate participation rather than micromanage. Atlassian’s ShipIt hackathons are an industry model for this practice.
    

### 4. Scaling engineering organizations — **Democratic + Coaching + Authoritative**

- Scenario: Growing from a few teams to many (scale pains: duplication, inconsistent practices).
    
- What to do: Use democratic forums (tribe/chapters) to share practices, coaching to develop tech leads, and authoritative vision to unify priorities — similar to the Spotify “squads & tribes” approach of granting autonomy while preserving alignment.
    

### 5. Short-term push (release sprint) — **Pacesetting (careful)**

- Scenario: Launch deadline that truly requires speed and excellence.
    
- What to do: Use pacesetting with volunteer, highly competent teams for a short, defined window; explicitly plan for post-sprint recovery and tech debt remediation to avoid long-term harm.
    

---

## Practical checklist for student / junior PMs to apply these styles

- Before acting, **choose the outcome** you need in 24–72 hours: survival, clarity, morale, buy-in, speed, or growth.
    
- Map outcome → style(s) using the comparative table above.
    
- Announce the mode and expected duration to the team (transparency reduces resistance).
    
- If choosing coercive/pacesetting, **timebox** it and schedule follow-up restorative actions (retro, refactor).
    
- Use **retrospectives** and one-on-ones to switch into coaching and affiliates modes after high-pressure phases.
    
- Track _team climate_ metrics (e.g., engagement survey, velocity trends, defect rates) to notice negative drift and switch styles earlier.


---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.