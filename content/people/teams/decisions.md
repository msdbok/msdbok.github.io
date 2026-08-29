---
parent: Teams
title: Decision Making
nav_order: 5
layout: default
---

# Teams Problems: Decision Making
_*Adapted from David Root (2014)_

## Basics

### Decision Levels

- **Operational:**  
  Everyday decisions, often made quickly with little structure.  
  *Example:* Assigning today’s coding task or approving a pull request.

- **Tactical:**  
  Medium-term decisions that support strategy and direct resources.  
  *Example:* Choosing a testing framework for the project.

- **Strategic:**  
  Long-term decisions about direction, goals, values.  
  *Example:* Deciding to adopt Agile development across the organization.

---

### Major Problem – Analysis Paralysis

When teams spend too much time analyzing options, they fail to act.

- **Buridan’s Ass:** A paradox where too many choices prevent decision.
- **Focus on drawbacks:** Overemphasis on risks stalls progress.
- **Result:** Delay, lost opportunities, wasted energy.

---

### Basic Techniques

- **T-Chart (+/–):** Compare pros and cons.
- **SWOT Analysis:** Strengths, Weaknesses, Opportunities, Threats.
- **Pareto Analysis (80/20 Rule):** Focus on the small % of causes that yield big results.
- **Pair-Wise Comparison:** Compare options against each other, one by one.
- **Cost-Benefit Analysis:** Compare expected gains vs. expected costs.
- **Fishbone (cause-and-effect) diagram:** Structure a discussion of *root causes* by repeatedly
  asking "what is a potential cause of…?" {% cite rebori1997problemsolving %}. Best used when you
  know which area is failing but not which part of it.
- **Dot voting:** Give each member 3–5 adhesive dots to allocate across the listed options in any
  pattern. Fast, keeps everyone active, and makes areas of agreement visible
  {% cite rebori1997problemsolving %}.

### A structured method for group problem solving

Rebori's extension guidance {% cite rebori1997problemsolving %} sets out **seven** steps, and the
ordering carries the substance:

1. **Define the problem** — state the current situation as *facts* and the desired situation as an
   *objective*. The statement "should not imply any solutions or causes."
2. **Identify and define root causes** — causes, not symptoms. Brainstorm under explicit ground
   rules: no criticism · go for quantity · encourage wild ideas · build on others'.
3. **Generate alternative solutions** — generate, do not evaluate. Doing both at once "reduces the
   number of potentially viable solutions."
4. **Evaluate the alternatives** — **establish criteria first**, objective and preferably
   measurable. Then score, by weighted matrix or by dot voting.
5. **Agree on the best solution** — using a decision rule the group agreed *beforehand*.
6. **Develop an action plan** — goal, strategy, timeframe, owner, expected outcome.
7. **Implement and evaluate the solution** — put status on a standing agenda; scale the evaluation
   to the complexity of the problem.

Two of these are worth more than the rest. **Step 4 precedes step 5**: criteria are fixed before
options are scored, which is the remedy for the "no clear criteria" failure listed below. And
**step 7 exists at all** — Rebori observes that evaluating whether the solution actually worked is
"probably the step most groups underemphasize", and that the reasons are political rather than
procedural: "time, cost, political climate, uneasiness in evaluation, and fear of being challenged
in their decided upon solution." A team that never reaches step 7 cannot tell a good decision from
a lucky one, which is the thread running through the whole of this page.

{: .warning }
**This is practitioner guidance, not evidence.** Fact Sheet 97-26 is a four-page university
extension leaflet with no study, no data and no peer review behind it, written for community and
organizational groups rather than software teams. Cite it for *what the method is*; it establishes
nothing about the method working. Rebori is candid about the tools in it: evaluation matrices and
dot votes "should not be thought of as formulas that will automatically produce correct answers."

**Software example:** Pareto Analysis helps software teams find the few issues that cause most pain. A team collects bug reports and measures user impact and frequency, sorts defects by cumulative user-reported incidents, and expects to find that a small minority of defects accounts for a large majority of the incidents and complaints. It then prioritizes those defects, pair-codes on the top items, adds regression tests, and watches the metrics to confirm the improvement.

{: .warning }
**The "20% of bugs cause 80% of errors" ratio is a heuristic, not a measurement.** Earlier
versions of this page stated it as an empirical finding. It is a way of deciding where to look
first, and the actual concentration on your own defect data is something to *measure*, not to
assume. Published work on defect and crash concentration in real systems does exist — it is not
held in this handbook's bibliography, so no figure is quoted here rather than a plausible one
being invented.


---

### Decision Making Model

Adapted from Hoover, Rosso-Llopart and Taran, *Evaluating Project Decisions*
{% cite hoover_evaluating_2010 %}.

**Inputs**
- Problem (requirements, constraints)
- Assumptions
- Knowledge (facts, data)
- Experience (skills, intuition)

**Decision Process**
- Select and apply a decision technique (e.g., SWOT, cost-benefit).

**Outputs**
- Solution chosen
- Assumed risks documented

---

## Influencing Factors

### Decision-Driven Organizations

(*Source: Rogers & Blenko*)

- Some decisions matter more than others → focus on high-impact ones.
- Ambiguity is the enemy → clarify.
- Speed & adaptability are crucial.
- Roles > org chart → empower decision-owners.
- Fear of overstepping must be overcome.
- Well-aligned organizations reinforce roles.
- Practice builds capability: “practicing beats preaching.”

**Core problem:**  
How much information is “enough” before deciding?

{: .warning }
**A bullet removed, and why.** This list previously carried "Action is the goal (Standish
Report)" directly above "Ambiguity is the enemy → clarify". No such claim is locatable in the
CHAOS 2015 report, and on goal clarity that report concludes the **opposite** of the neighbouring
bullet: it says the Group had believed clarity and focus were essential and "found the opposite to
be true" — **Vague objectives 38% successful against Precise 22%** — and recommends that teams
"reduce or give up control of the business objectives to encourage and promote innovation"
{% cite standish2015chaos %}. That recommendation is drawn from a bivariate crosstab with no
control for project size and no significance testing, so it is not evidence that ambiguity helps
either. The honest position is that **the disagreement is unresolved**: the advice to clarify is
Rogers and Blenko's, the contrary figure is Standish's, and neither is well-evidenced. The
Standish attribution has been dropped rather than left standing on a claim its own source
contradicts. See the [People overview](../) for why CHAOS figures need
{% cite eveleens2010chaos %} beside them.

---

### Intuitive Decision Making — the Recognition-Primed Decision model

The model behind this section has a name the page has never given it: Gary Klein's
**Recognition-Primed Decision (RPD)** model {% cite klein1998sourcesofpower %}, developed from
studies of fireground commanders and other high-tempo professionals.

The claim is not that experts choose well among options — it is that they usually do not generate
options at all. A recognised pattern produces a single candidate action, which is then run
forward mentally; if the simulation exposes a problem, the action is modified or the next
candidate considered. Klein ties this to Herbert Simon's **satisficing**: options are evaluated
**one at a time**, and the first workable one is taken. This is why an expert's *first considered
action* is so often workable.

- **Definition:** "I define intuition as the way we translate our experience into action"
  {% cite klein2003intuition %}.
- **Origins:** Firefighters, military, police — high-pressure environments.
- **Premise:** Intuition is a skill → can be built, applied, safeguarded.

**The chain**, as *The Power of Intuition* states it: cues let us recognise **patterns** →
patterns activate **action scripts** → action scripts are assessed by **mental simulation** →
driven by **mental models**.

Two pieces this handbook used to omit, both from the research monograph:

- **RPD has three variations, not one chain.** *(1) Simple match* — situation recognised, action
  taken. *(2) Diagnose the situation* — cues do not match cleanly, so the decision maker gathers
  more, feature-matches, or builds a story. *(3) Evaluate a course of action* — the recognised
  action is simulated, then modified or rejected.
- **Expectancies are a first-class element**, alongside cues, goals and actions — and they are
  the *safeguard*. A violated expectancy is how an expert discovers the interpretation was wrong.
  Leaving them out makes the model merely fast; including them makes it self-correcting.

**How often experts actually work this way** {% cite klein1998sourcesofpower %} — across **more
than six hundred decision points**, RPD accounted for **46% to 96%** of them depending on domain
and expertise: urban fireground commanders **80%** of 156 decision points, design engineers
**60%**, AEGIS commanders **95%**, tank-platoon *trainees* **42%**.

{: .warning }
**This is a strategy count, not a quality count, and Klein is grading his own programme.** The
table above establishes that experts do not compare options. It does **not** establish that they
are right. The studies are Klein's own, coded by his own team, and the independent replications
he cites are the ones that agreed — so read 46–96% as the range *this research programme* found.
RPD is also explicitly **descriptive, not prescriptive**: it does not license "train people to
satisfice." And it does not transfer to domains without consistent, fast feedback — Klein names
stock selection, public policy and clinical psychology. **Software estimation has weak feedback
loops, so the transfer to this course's subject matter is a question, not a given.**

**Advantages**
- Very fast, based on pattern recognition.
- Allows action under uncertainty and time pressure.

**When singular evaluation beats comparing options** — Klein's own boundary conditions
{% cite klein1998sourcesofpower %}, which read as a decision rule about decision rules:

| Recognition works when… | Compare options when… |
|---|---|
| Time pressure is high | The choice must be justified to others |
| The decider is experienced **in this domain** | Competing interests must be reconciled |
| Conditions are dynamic | The decider is optimizing, not satisficing |
| Goals are ill defined | The problem is computationally complex |

**Where intuition fails.** *The Power of Intuition* names the conditions
{% cite klein2003intuition %}, and four of them describe software estimation:

- **Unstable or random domains** — roulette, the stock market. Patterns cannot form.
- **No fast, accurate feedback** — e.g. hiring judged on time-to-fill rather than hire quality.
- **A distorted experience base** — experience of the wrong thing, repeatedly.
- **Fixation, or "bending the map"** — expertise closing off the anomaly that should have
  stopped you.
- **Arithmetic** — "you're sunk if you don't whip out the calculator."
- **Conflicting interests** to reconcile, and **decisions that must be auditable**.

{: .note }
**Klein is not an escape from the analysis paralysis above.** This page once implied he was. He
writes plainly: "**Neither analysis nor intuition alone is sufficient for effective decision
making**" {% cite klein2003intuition %}. The claim is that experts *start* from recognition, not
that analysis is dispensable.

**Barriers**
- Rigid policies, remote/distributed teams, turnover, constant change.
- Procedures, metrics-driven culture, IT constraints.

{: .note }
**Which Klein book?** They do different jobs, and earlier versions of this page cited them
interchangeably. **Cite *Sources of Power* (1998/2017) for anything with a number in it; cite
*The Power of Intuition* (2003) for anything a manager is supposed to do.** The confusion is
forgivable — chapter 4 of the 1998 book is itself titled "The Power of Intuition". Note also
that our copy of *Sources of Power* is the **20th Anniversary Edition (MIT Press, 2017)**, a
revised edition whose retrospective preface does not exist in the 1998 original.

---

### Theory of Thin Slicing

- **Definition:** "'Thin-slicing' refers to the ability of our unconscious to find patterns in
  situations and behavior based on very narrow slices of experience"
  {% cite gladwell2005blink %}.

{: .warning }
**Everything in this section is second-hand.** *Blink* is trade non-fiction, and Gladwell
conducts no studies in it — every example below is him reporting someone else's work, and **this
handbook holds none of those primary sources**: not Gottman, not Ambady, not Levinson, not Nigel
West. Treat the section as vocabulary and illustration, never as evidence. Gladwell's own Notes
section gives full journal citations for all of them; that is where to go before any of this
reaches a slide.

**Examples**
- **John Gottman's Love Lab:** more than 3,000 couples filmed discussing a point of contention,
  with SPAFF coding 20 emotion categories every second. Gladwell reports prediction of divorce
  15 years out at "95 percent accuracy" from an hour of tape.
- **Military interceptors:** WWII operators recognised individual German senders by rhythm and
  spacing — the "fist".
- **Levinson on malpractice:** never-sued primary care physicians spent **18.3 minutes** per
  patient against 15, and made more orienting comments — with **no difference in the amount or
  quality of medical information given**.
- **Ambady:** silent video of unfamiliar professors at 10, 5 and even 2 seconds produced ratings
  essentially the same as a full semester's student evaluations. She later took Levinson's tapes,
  cut them to **two 10-second clips per surgeon** and content-filtered them so only tone
  survived — a dominant tone marked the sued group.

{: .note }
**Two corrections this page carried for years.** The name is **Ambady**, not "Ambadi". And
Levinson and Ambady are **two different studies**: Levinson's 18.3-versus-15-minute finding is
not itself a thin-slicing result — thin slicing enters only when Ambady re-slices the same tapes
down to forty seconds.

{: .warning }
**Do not put the 95% on a slide.** Gladwell's wording is "Gottman has *proven* something
remarkable" — with no confidence interval, no cross-validation, and no statement of whether the
equation was ever tested on couples outside the sample it was fitted to. That last point is the
entire question for any accuracy figure of this kind, and the book does not address it. Gottman's
prediction accuracies are among the most contested numbers in popular psychology. The
*direction* — that tone carries signal, that brief clips carry signal — is ordinary and
defensible. The percentages are what will not survive checking. Likewise "absolute certainty"
about Morse operators is a historian's phrase, not a measurement.

**Key Point:** Thin slicing is part of human cognition, not a rare talent.

**And it fails, roughly half the book.** *Blink* is not a case for trusting snap judgment; about
half of it is snap judgment going wrong, and the handbook used to teach only the flattering half:

- **The Warren Harding error** — a face that looks the part is read as competence.
- **Amadou Diallo** — under extreme arousal rapid cognition collapses into "temporary
  mind-blindness"; Gladwell puts the degradation band at roughly **115–145 bpm**.
- **Priming** — behaviour moved by cues the subject never notices.
- **New Coke** — the sip test is the wrong instrument; sweetness wins a sip and loses a can.
- **Blind auditions** — a screen removes a bias the listeners sincerely denied holding.
- **Explaining ruins it** — asked to give reasons, non-experts' jam rankings fell from
  **r = .55** to **r = .11** against expert judgment.

---

### Time and Decision Making

**Chess under time pressure** {% cite klein1998sourcesofpower %} — blitz at **6 seconds** a move
against roughly **2¼ minutes** under regulation:

| | Blunder rate, blitz | Blunder rate, regulation |
|---|---|---|
| **Masters** | 7% | 8% |
| **Class B players** | **25%** | 11% |

**The result is an interaction, not a main effect.** Time pressure barely touches masters and
roughly *doubles* the error rate of weaker players. The lesson is therefore not "people decide
fine under pressure" — it is that **expertise is what buys immunity to time pressure**, and that
squeezing the clock on an inexperienced team is a different act from squeezing it on an
experienced one. The primary study is Calderwood, Klein and Crandall
{% cite calderwood1988chess %}, not the trade books.

**Observations**
- Skilled decision makers can make good choices even under pressure.
- Often their *first considered action* is already a good one.

---

### Group Decision Making

Rebori {% cite rebori1998decisionstyles %} starts from a problem every team recognises: groups
often cannot tell **when a decision was made**, which surfaces as "I don't recall us making an
actual decision on that" or "I thought we already made this decision." Her remedy is to agree the
decision *style* in advance. Five styles, and the split between them matters more than the list.

**Three are failure modes — things groups fall into, not methods to choose:**

- **No decision.** Deciding not to decide. It shows up as *topic-jumping*, and as **"the plop"** —
  a member proposes something and the group simply does not respond. "Avoiding or ignoring actions
  or decisions is a decision, it is just a decision not to decide."
- **Self-appointed decision maker.** One member states a decision, nobody agrees or disagrees, and
  so that member decides for everyone. Fast, but it reflects one person's view, not the group's.
- **Minority rule.** Three or four members agree while the rest stay silent, usually with no vote.
  It "can cause frustration among silent members creating the impression their opinion does not
  count."

**Two are styles you can deliberately adopt:**

- **Majority rule.** At least 51%, usually brief discussion then a show of hands. It moves a group
  forward quickly, but on complex or high-stake decisions it "often produces a win/lose solution
  and is considered a competitive style of decision-making."
- **Consensus.** All members support the decision. Not a compromise — "members work to seek mutual
  agreement" — and not unanimity either. It is slow and genuinely difficult, and it "fosters board
  empowerment, builds group cohesion, and improves interpersonal relationships and accountability."

{: .warning }
**Do not teach these five as parallel options.** Rebori is explicit that the first three are "**not
recommended** as organized procedures" and "really refer to common situations that many boards may
fall into." Earlier versions of this page listed all five flat under "common outcomes", which
inverts her point: three of them are pathologies to recognise and name, and only two are choices.

**How to choose — and this applies only to the majority-versus-consensus choice:**

- **Timeliness** — how much time the group has. One meeting to decide forces the quickest workable
  method.
- **Appropriateness** — how complex the decision is. Choosing when to break for lunch does not
  need consensus; approving an architecture or a release does.
- **Relationship** — how the decision will affect working relationships. If a style could put
  those in peril, lean collective.

#### Techniques worth stealing

Over half of Rebori's fact sheet is technique, and this is the part the lecture never taught.

**To soften a majority decision:**

- **70/30 vote** — require 70% agreement rather than 51%. Because you cannot reach 70% without
  talking, it "borrows from consensus" and blunts the divisiveness a bare majority creates.
- **Blind vote** — a secret ballot for high-stakes calls; anonymity reduces divisiveness.
- **Devil's advocate** — one member argues every opposite possibility, specifically to stop the
  group sliding into groupthink.

**To build consensus:**

- **Levels of consensus** — the single most reusable item here. Rate each member's position 1–5:
  **1** easily accept · **2** accept, though not my preference · **3** accept with minor changes ·
  **4** accept the group, though I don't agree · **5** cannot accept. **Anyone at 5 means there is
  no consensus; everyone at 4 or above means consensus is reached.** Agree the scale in the ground
  rules before you need it. This converts "does everyone agree?" — which invites silence — into a
  question people can answer honestly and quickly, and it makes disagreement cheap to voice.
- **Consensus log** — a running record of what was agreed, so "what did we decide about X?" stops
  recurring.
- **Distill concerns** — write every concern up visibly, then group the similar ones to expose what
  actually needs resolving.
- **Straw man** — draft a proposal *in order to have it attacked*. Letting the group pull it apart
  and rebuild it is what produces ownership.

{: .warning }
**Practitioner guidance, not evidence — and from a different world.** Fact Sheet 98-56 is a
four-page extension leaflet with no study behind it, written for **community and municipal boards**:
volunteers advising city councils, not paid engineers making technical decisions. The 51% and 70%
thresholds are conventions, not findings. Use it for vocabulary and procedure, which is what it is
good for, and do not claim any of it has been measured on software teams.

{: .note }
**Two things to notice about the devil's advocate.** Rebori recommends it against groupthink in
1998; {% cite mohanani2018biases %} finds the same technique still circulating in software
engineering as a proposed debiasing method **with no empirical evaluation** — one of six proposed
remedies across thirty-seven biases, none of them tested. A technique can be in practitioner
guidance for nearly thirty years and still be unvalidated. Note too that Rebori's own gloss on
groupthink — members suppressing dissent "because they believe no one will agree with them" — is
closer to the **Abilene paradox** than to Janis's construct, and drops cohesion, stress and
structural faults entirely. It is a tidy live specimen of what ’t Hart complained about above. For
the definition, use the groupthink section, not this one.

**Problems in group decisions**
- Deciding too soon (rushing).
- Analysis paralysis (stalling).
- **No clear criteria** — the remedy is procedural and cheap: fix the criteria *before* scoring
  the options, not after {% cite rebori1997problemsolving %}. Criteria invented while looking at
  the candidates tend to describe the favourite.
- Poor listening → debate instead of dialogue.
- Perceptions of unfairness.
- **Never checking whether it worked.** Groups routinely stop at the decision and skip evaluation,
  for reasons that are political rather than practical {% cite rebori1997problemsolving %}.
- **Groupthink** — conformity pressure inside a cohesive group suppresses dissent, so alternatives
  are never voiced and the group converges early on a poor option. Named by Irving Janis in 1972
  from case studies of foreign-policy fiascos — the Bay of Pigs, Pearl Harbor, Korea, Vietnam,
  Watergate — against two successes where he judged it avoided, the Marshall Plan and the Cuban
  missile crisis.
- **The Abilene paradox** — a group unanimously agrees on a course of action that *no individual
  member privately favours*, each mistakenly believing the others want it. Described by Jerry B.
  Harvey (1974). It is not conformity to a majority; it is agreement in the absence of one.

{: .note }
**Two different phenomena.** These were previously a single bullet — "Groupthink / *Abilene
Paradox* (agreement without real support)" — which is wrong twice over: groupthink is dissent
suppressed by pressure, the Abilene paradox is dissent that nobody realises exists.

#### Groupthink is contested in its own discipline

Groupthink is the most famous construct in this whole block, and it is taught almost everywhere as
settled. It is not. Paul ’t Hart's review essay for *Political Psychology*'s "Classics" series
{% cite thart1991groupthink %} assessed the evidence nineteen years on and found the replications
"their number is modest, their quality mixed and their findings only partially conclusive".

| Component | State of the evidence as of 1991 |
|---|---|
| **Cohesiveness** — the one group-level cause Janis names | **Repeatedly unsupported.** Flowers found leadership mattered and cohesiveness did not; Fodor & Smith and Leana likewise. Raven's study of Watergate found the Nixon group **conflict-laden and competitive** — cohesion was *absent* in one of Janis's own cases |
| **Directive leadership** | **Supported**, across four independent studies |
| **Stress** — which Janis ranked *first* among causes | **Largely untested.** Experiments "have rarely succeeded in creating the kind of decisional stress" the theory requires |
| **Stereotyped out-group images** — one of the eight symptoms | **Disconfirmed** by Tetlock: groupthink decision makers made no more negative references to adversary states |
| **The founding cases** | Mixed. Barrett re-examined Vietnam escalation and argued groupthink played **no role at all** |

’t Hart's own charge is **circularity**: Janis selected policy failures first and then looked for
groupthink, so "groupthink is inferred from policy failure and failure is explained in terms of
groupthink." His alternative mechanism is **anticipatory compliance** — low-status members
conforming to what they take the leader to want. Power and hierarchy, not friendliness, do the
work. That is a considerably more plausible fit to a software team than cohesion is.

{: .warning }
**Two limits before using any of this.** First, **scope**: ’t Hart states that groupthink analysis
is meaningful only for **high-level groups facing consequential, non-routine choices**, and says
outright that analysing "regular problem-solving groups at some lower level of management" is not
interesting. Applying it to a sprint team is an untested extrapolation — scope it to
architecture, go/no-go and release decisions, or say plainly that the transfer is an assumption.
Second, **vintage**: this record stops at **1991**. Do not say "the evidence for groupthink is
weak" full stop; say that as of 1991 its own reviewer described the replications as modest, mixed
and only partially conclusive. A current claim needs a recent meta-analysis, which this handbook
does not hold.

{: .note }
**Which Janis, and what is still missing.** The 1972 first edition is *Victims of Groupthink*; the
1982 second edition is *Groupthink*. ’t Hart notes the **systematic** statement of the theory —
the flow chart, the antecedent/symptom/effect boxes — is in the **1982** edition. 1972 is the
right date for the naming, the wrong one for the model. **Janis's own book is still not held
here**, and neither is Harvey — so the eight symptoms are reported above via ’t Hart, and **no
remedy list is given**, because ’t Hart does not reproduce one and inventing it is exactly the
error this page is trying to stop making. The same applies to the Abilene paradox, which does not
appear in ’t Hart at all and remains the least-sourced named claim on this page.

And there is a closing line worth quoting against ourselves. ’t Hart's verdict is that the very
popularity of groupthink impedes careful work, and that this "emerges clearly from the uncritical
adoption of sections on 'the dangers of groupthink' in many policy analysis and management
handbooks." This is a management handbook, and that is what the section above used to be.

---

## What is actually known about bias in software engineering

The systematic mapping study by Mohanani and colleagues {% cite mohanani2018biases %} is the best
answer available to "how much of this is established?", and the answer is unflattering to the list
above. Across **65 primary studies** published 1990–2016 it identifies **37 distinct cognitive
biases** — and they are very unevenly studied:

| | |
|---|---|
| Anchoring and adjustment | **26** studies |
| Confirmation bias | **23** studies |
| Overconfidence | **16** studies |
| Biases resting on only one or two studies each | **21 of the 37** |
| The **`Social`** category — biases where social relationships undermine judgment | **2 studies**, covering **one** bias |
| Biases with any proposed debiasing technique | **6 of 37**, and **none empirically evaluated** |

Two consequences for this page:

1. **The group pathologies above are the thinnest-evidenced part of the topic.** `Social` is the
   least-studied category of all. **Groupthink is not among the 37 biases mapped** — it appears in
   that paper only as the *target* of an unvalidated proposed remedy (designating a devil's
   advocate) — and **the Abilene paradox does not appear at all.**
2. **The best-evidenced biases are individual, and they land on estimation.** Anchoring,
   confirmation and overconfidence are all failures of judgment about *numbers and evidence*, which
   is where the [Scope](../../scope/) and [Planning](../../plan/) blocks of this handbook pick them
   up. A decision-making section that stops at group dynamics misses the part of the literature
   that has actually been measured.

{: .note }
**What this does not license.** The mapping study maps research, not projects: 30 of its 65 studies
are controlled experiments, and the authors write that "demonstrating a bias in a lab is not the
same as establishing a significant effect on real projects." Nor does it supply a fix — six of
thirty-seven biases have any proposed technique, none of them tested, and the authors warn that
debiasing "may have unintended consequences". Its own inter-rater agreement on which category a
bias belongs to was **55%**. Treat the counts as a map of where the evidence is, not as a ranking
of what will go wrong on your project.

### The other side of that argument

Klein rejects the premise of the bias literature outright, and the disagreement is worth staging
rather than hiding. Chapter 16 of *Sources of Power* argues that "those who favor analytical
approaches to decision making believe poor decisions are caused by biases in the way we think.
Naturalistic decision-making researchers disagree" {% cite klein1998sourcesofpower %}. His
methodological charge, via Lopes, is that the classic stimuli were **selected to produce the
error**: of the twenty possible consonants, twelve are more common in first position, and the
famous availability demonstration used the eight that are not. He adds that the heuristics and
biases "do not occur in experienced decision makers working in natural settings".

Klein is not a neutral party — he is defending his own research programme, and he overclaims. But
he and the mapping study arrive at the **same conclusion from opposite ends**, which is why they
belong on the same page rather than in separate sections:

| Source | The same claim |
|---|---|
| Klein {% cite klein1998sourcesofpower %} | "Poor outcomes are different from poor decisions." |
| ’t Hart {% cite thart1991groupthink %} | "Bad procedures need not always produce bad results; decision-makers may get lucky." |
| Mohanani et al. {% cite mohanani2018biases %} | "Demonstrating a bias in a lab is not the same as establishing a significant effect on real projects." |

**Judge the process, not the outcome — and do not assume the process research transfers.** That
is the transferable lesson of this entire page, and it is a project-management lesson rather than
a psychology one.

There is also a direct conflict students should see. Janis's standard for a good decision is the
Janis & Mann procedural model — canvass all alternatives, weigh all costs, search for new
information. **Klein disputes exactly that model**, arguing that experts do not compare options
and that the prescription is unworkable under time pressure. The two classics of this topic
disagree about what a good decision even *is*.

---

## Deciding alongside an AI

The failures above run human-to-human. The same question — *when should I take the advice?* — now
runs human-to-model, and it has been measured. The results point in **opposite directions**, and
that is the finding.

| Study | What was measured | Result |
|---|---|---|
| Puppart & Aru {% cite puppart2025overreliance %} | Adoption of **incorrect** ChatGPT recommendations. **n = 36 twelfth-grade Estonian school students**, math puzzles, **unreviewed preprint** | **Over-reliance: 52.1%** (SD 28.90) — bad advice taken just over half the time. A short AI-literacy intervention **did not reduce it**, and significantly *increased* rejection of correct advice (t(34) = 2.35, p = .025, d = 0.78) |
| Schemmer et al. {% cite schemmer2022reliance %} | Whether people **rightly change their mind** when the AI is correct (RAIR) and **rightly hold their ground** when it is wrong (RSR). 200 participants, deceptive-review classification, CHI '22 workshop paper | **Under-reliance: RAIR 0.30 — below chance.** Correct advice was ignored. RSR was 0.72. Adding explanations raised RAIR to 0.39 (p = .05) without inducing over-reliance |

**The lesson is miscalibration in both directions, not "people trust AI too much."** One study
found bad advice accepted; the other found good advice refused. Getting this backwards licenses
exactly the wrong intervention — and the intervention the second-guessing instinct reaches for
first, a short explanatory lesson about the tool, is the one that was tested and failed.

So the management question is not *"does the team trust the AI?"* Trust is an attitude; reliance is
a behaviour, and it is the behaviour that costs money. The useful question is whether people can
**tell good advice from bad and act on the difference** — two separate abilities, which can fail
independently and in opposite directions, and which a rise in overall team performance can hide
entirely {% cite schemmer2022reliance %}.

{: .warning }
**Carry the populations with the numbers.** The 52.1% figure comes from **36 school students
solving math puzzles in a preprint that has not been peer-reviewed** — not from software
engineers, not from code, not from a team under a deadline. It licenses a *direction*: a short
literacy intervention is a weak instrument against miscalibration. It is not an effect size for
professional developers. Schemmer's study is a **workshop** paper with a single illustrative
experiment, and its metric is defined only for classification tasks.

---

## Named on this page but not in our bibliography

These works are the acknowledged origin of sections above. **None of the works listed below has
been obtained or read for this page**, so they are named and dated here rather than cited, and no
claim on this page rests on a page number from any of them:

- **Rogers, P. & Blenko, M.** *Who Has the D? How Clear Decision Roles Enhance Organizational
  Performance*, and Blenko, Mankins & Rogers, *The Decision-Driven Organization* — *Harvard
  Business Review* — the "Influencing Factors" section.
- **Janis, I.** *Victims of Groupthink* (1972) / *Groupthink* (1982) — reported here only through
  {% cite thart1991groupthink %}, which is a review essay, not Janis.
- **Harvey, J. B.**, "The Abilene Paradox" (1974) — see the note above.
- **Gladwell's primary sources** — Gottman, Ambady & Rosenthal, Levinson, Nigel West. *Blink*
  itself is now held and cited, but the studies it reports are not.

**Resolved since this list was written.** Klein's *Sources of Power* and *The Power of Intuition*,
Gladwell's *Blink*, ’t Hart's review essay, and **both** Rebori fact sheets — *Decision-Making
Styles and Techniques* (98-56) for the taxonomy and *Effective Problem-Solving Techniques for
Groups* (97-26) for the method — are now held, read and cited above. Gonzales's *Deep Survival*
was dropped rather than obtained: Klein's named failure conditions do the same job with evidence
behind them.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and
**David Root** {% cite root2014lectures %} on software project management. The structure,
examples, and pedagogical approach reflect their teaching materials and frameworks.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.