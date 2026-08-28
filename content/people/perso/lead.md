---
parent: Personality
title: Leadership
nav_order: 4
layout: default
---

# Leadership styles by Daniel Goleman

_Adapted from lecture materials by David Root {% cite root2014lectures %}._

The source is "Leadership That Gets Results", *Harvard Business Review*, March–April 2000,
reprint R00204 {% cite goleman2000leadership %}. The 2006 and 2017 dates attached to this
article elsewhere — including in an earlier version of this page — are Routledge anthology
reprints of the same text, not later research.

## Brief

Leadership style is the habitual way a leader interacts with their team — how they make decisions, motivate people, manage change and handle crises. Daniel Goleman identifies **six** distinct styles (coercive, authoritative, affiliative, democratic, pacesetting, coaching); each arises from different emotional-intelligence competencies and affects team climate and performance differently. The best leaders are flexible: they know multiple styles and switch to the style(s) that fit the situation.

**The evidence behind the six styles.** The research is by the consulting firm **Hay/McBer** —
colleagues of David McClelland, the work headed by Mary Fontaine and Ruth Jacobs — on a **random
sample of 3,871 executives** drawn from a database of **more than 20,000 executives worldwide**.
Each style is scored against six *drivers of organizational climate* — flexibility,
responsibility, standards, rewards, clarity, commitment — and climate is reported to account for
**"nearly a third" of financial results** {% cite goleman2000leadership %}. That last figure is a
variance share from correlational data, and the article's own hedge travels with it: "economic
conditions and competitive dynamics matter enormously."

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

The **overall impact on climate** column is not an adjective chosen here: it is the correlation
reported for each style in the "Getting Molecular" exhibit of the HBR article
{% cite goleman2000leadership %}.

|Style|When to use|Short-term effect|Overall impact on climate|Typical software-team example|
|---|---|---|---|---|
|Coercive|Crisis, incident response, flop/turnaround|Quick compliance|**−.26**|Emergency incident commander during a major outage (silos, fast rollback).|
|Authoritative|New vision, strategic pivots|Aligns and energizes|**.54**|CTO sets product mission and OKRs; teams choose implementation.|
|Affiliative|Repair trust, high stress / post-layoffs|Immediate morale boost|**.46**|Team lead emphasizes wellbeing after stressful release; organizes socials/hack days.|
|Democratic|Need buy-in, generate solutions|Slower decisions, more ideas|**.43**|Facilitating architecture decisions in cross-functional squads (retros, design reviews).|
|Pacesetting|High-performing, short-deadline tasks|Fast delivery from top talent|**−.25**|Startup founder demanding rapid MVPs; specific sprints where speed > process.|
|Coaching|Talent growth, next-level capabilities|Slower immediate output|**.42**|One-on-one mentoring, pairing, career development plans, internal training.|

### The result the researchers did not expect

**Pacesetting, at −.25, is essentially as damaging as coercive at −.26**, and it is negative on
five of the six climate drivers. The authors say so themselves: *"That's not what we expected to
find. After all, the hallmarks of the pacesetting style sound admirable"*
{% cite goleman2000leadership %}. The style that reads best on paper — set an extremely high bar
and exemplify it — measured second-worst in the data.

This is the reason to teach the numbers rather than the six labels, and it matters most for
readers arriving from a technical role, where the instinct is exactly *"set a high standard and
show them how."* Two smaller inversions sit in the same table and are lost when the ratings are
turned into adjectives: **democratic (.43) ranks below affiliative (.46)** — the article's own
summary notes that this style's impact "is not as high as you might imagine" — and **coaching
(.42) is the style used least often**.

---

## What this evidence is, and what it is not

{: .warning }
**A serious number attached to a study nobody can inspect.** 3,871 executives is a large sample,
and the study behind it is **proprietary Hay/McBer work that was never published**: the article
gives no method, no measurement instrument, no confidence intervals and no industry breakdown, so
none of it can be replicated from what is on the page. Every figure in the table is a
**correlation**, not a causal effect. And endnote 1 of the article discloses that *"Daniel Goleman
consults with Hay/McBer on leadership development"* {% cite goleman2000leadership %} — the author
reporting the results is a paid consultant to the firm that produced them.

The shape of that problem is the same one the [People](../) opening section meets in the Standish
CHAOS figures {% cite standish2015chaos %}: a substantial corpus, an uninspectable method, and a
vendor with a commercial interest in the conclusion. The response in both cases is neither
credulity nor refusal. These are still the best numbers anyone has on leadership style and
climate; they are quoted here **with their provenance attached**, which is what the course asks of
any management figure.

Two further limits on transfer:

- **The population is executives in large organizations, c. 1999.** No software teams, no
  individual technical contributors, no distributed work.
- **The construct underneath the six styles is contested.** McCleskey's review of twenty years of
  the emotional-intelligence debate {% cite mccleskey2014emotional %} separates the
  Mayer–Salovey **ability** model of EI — the family with the strongest academic standing — from
  the Boyatzis–Goleman **mixed** model, expanded to workplace competencies, which is the family the
  six styles actually rest on. The best evidence for EI is real but modest (a meta-analysis of 43
  studies, n = 5,795 for job performance, finding incremental validity over the Five-Factor Model
  and IQ), and the critique is blunt: Antonakis and colleagues conclude that either "EI
  researchers are using the wrong measures or the wrong methodology, or EI does not matter for
  leadership". McCleskey reports the debate rather than settling it. A manager can use the styles
  without buying the theory of mind beneath them — but should know that the two are separable.

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

## What the software-specific evidence adds

Goleman's six styles come from a general executive population. The only leadership study in our
corpus collected **from technical staff** finds a factor that is not among the six and does not
resemble any of them.

Thite surveyed Australian IS/IT projects — 111 organisations invited, **36 participated**, each
contributing one more-successful and one less-successful team, with **70 project managers, 228
subordinates and 18 senior IT managers** responding to an extended Multifactor Leadership
Questionnaire {% cite thite1999leadership %}. Principal-components analysis produced five scales,
one of them new and domain-derived: the **"organisational catalyst"**. Subordinates on the *more*
successful projects rated their managers highest on precisely that scale — ahead of the
transformational scale. Its items are concrete and managerial:

- **shield the team from organizational bureaucracy**
- satisfy the desire for autonomy
- align individual goals with organizational ones
- implement upper management's decisions dispassionately

"Prevent organizational bureaucracy from interfering with the work of your subordinates" is a
better opening line for a software-management course than any of the six styles — and it is the
one claim here with a technical sample behind it.

{: .note }
**Read Thite with its limits.** One country, one snapshot, self- and subordinate-report only;
project success is a senior manager's judgement rather than a measured outcome; only one
significance test is reported; and it is a six-page conference summary whose author says it
"indicated the direction for" a validated model of technical project leadership rather than
delivering one. Note also that the rating scale runs 5 = low to 1 = high, so *lower* means are
better — easy to misread.

### A participative mechanism you can actually run

A team of 26 engineers needed a new Operations Project Leader. Rather than a manager-to-manager
placement, a **six-engineer selection sub-team** built a weighted list of traits and skills **by
consensus rather than by vote**, scored each candidate 0–10 against each trait × its weight, and
**committed in advance to offering the job to the top scorer** — moving the decision authority,
though not the accountability, off the manager. Eight candidates applied; the top two finished
less than ten points apart {% cite mccarthy2003participative %}.

{: .warning }
**This is an n = 1 experience report, not evidence.** One team, one company, no control, no
comparison project, written by the manager who ran it — and he records a colleague's objection
that the outcome "could have been predicted all along, without the complex process". His answer
is the teachable part: the choice was a by-product, and the value was in what the selection
discussions revealed about the team's own value system. Cite it as a practice with a case behind
it, never as a measured effect. (The article's title word is "Formulation", not "Formation" — the
misquotation is common.)

---

## How to choose and combine styles — practical advice for project managers

1. **Diagnose the situation first.** Is it a production outage, a strategic pivot, a morale problem, or individual development? Match the style to the need: coercive for outage; authoritative for new product direction; affiliative after stressful releases; democratic for design choices; pacesetting for short, critical pushes with proven talent; coaching for long-term growth.
    
2. **Use blends, not bans.** Most effective leaders regularly mix authoritative + coaching + democratic + affiliative depending on people and timing. Pacesetting and coercive are occasional emergency tools.
    
3. **Be explicit with the team.** If you shift to a pacesetting mode for a crunch, say so: “We’ll be in intense delivery mode for two weeks, then we’ll pause for refactor and recovery.” Explicit signals reduce confusion and resentment.
    
4. **Measure outcomes, not just activity.** Use OKRs / measurable goals to retain authoritative clarity while letting teams decide the “how.” (Google-style OKRs are widely used for this purpose). [Rework](https://rework.withgoogle.com/en/guides/set-goals-with-okrs)
    
5. **Protect flow and focus.** Use the authoritative style to set the mission and boundaries, and affiliative/coaching to protect developer time — blocked "focus time" in the calendar, meeting-free days, batched interruptions.
    
    {: .note }
    **This is a practice, not a finding.** "Maker time" and protected uninterrupted work are widespread industry patterns, and the claim that interruptions harm developer output is plausible and widely repeated — but **this handbook holds no study supporting it**, and no citation is offered here in place of one. Treat it as a recommendation to try and to measure on your own team, not as evidence. The nearest thing in this area that *is* sourced is Glen's account of [flow among technical people](glen.html), itself a practitioner framework rather than a measurement.
    

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
    
- What to do: Run hackathons or “innovation days” where teams can work on pet projects; leaders support and celebrate participation rather than micromanage. Atlassian’s ShipIt days are the best-known published example — but note that a company describing its own practice is marketing, not evidence, and no study here measures what such days produce.
    

### 4. Scaling engineering organizations — **Democratic + Coaching + Authoritative**

- Scenario: Growing from a few teams to many (scale pains: duplication, inconsistent practices).
    
- What to do: Use democratic forums (chapters, guilds, communities of practice) to share practices, coaching to develop tech leads, and authoritative vision to unify priorities.
    
    {: .warning }
    **The Spotify "squads and tribes" model is not a template.** It is routinely cited for exactly this pattern, and the people who published it have since said publicly that it described an aspiration at one moment rather than a working system, that it was never fully implemented, and that Spotify had moved on by the time it spread. This handbook holds no source for the model or for the disavowal — both circulate as conference talks and blog posts, never as a study — so it appears here as an illustration to be sceptical of, not as an approach to copy.
    

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

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.