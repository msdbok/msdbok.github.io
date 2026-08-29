---
parent: Study Notes
title: SN L1b — Teams and Decisions
nav_order: 2
page_type: study-notes
layout: default
---

# SN L1b — Teams and Decisions

A revision summary of the second People lecture. Where L1a was one engineer, this one is
five: what a team costs, how one forms, what makes it safe enough to report bad news, why
effort per person falls, and how decisions go wrong — alone and in groups. Each section
links to the handbook page carrying the detail and the sources.

## 1. Interdependence makes a team, and it is expensive

A team is a small group with complementary skills working to one goal, whose members
**depend on each other's work** to reach it. That dependence is the whole definition, and it
is also the cost: it buys shared knowledge and pays in coordination. A group that shares a
manager and a stand-up is not a team; it is a queue with a meeting.

Steiner's equation is the frame for everything else: **actual productivity = potential
productivity − process losses**. Potential depends only on the task and the people;
everything a manager can influence sits in the loss term. The losses come in two kinds —
**motivation losses**, people easing off, and **coordination losses**, the time spent keeping
in step. Adding a person adds communication links faster than it adds hands: two, three and
eight people carry 1, 3 and 28 pairwise links. Software work is largely conjunctive and
divisible, so the weakest link paces the whole, which is where Brooks's Law comes from.

Before staffing, ask whether the work actually **interlocks**. If two people can each finish
alone, give each an owner and skip the coordination bill. Team up when the knowledge needed
is held in several heads at once.

→ [Teams](../people/teams/index.html) · [Team Performance](../people/teams/performance.html)

## 2. Who you ask changes the answer

The same agile teams were asked about teamwork quality and performance from three vantage
points. Members reported a strong link — but they rated both the teamwork and the result, so
the two were never independent. Team leads reported a moderate one. The product owner,
looking at delivered functionality, saw essentially **nothing**.

A squad can honestly score itself nine out of ten in the week its product owner drafts the
cancellation memo. Both readings are sincere. So never run a team on self-report alone, and
settle **whose** definition of "performing" you are optimising before you start improving it.

→ [Team Performance](../people/teams/performance.html)

## 3. Forming: settle task, people and relationships

Team building events are not what forms a team. Three things are. **Task** — what work the
team owns, how much authority it has over it, how interdependent the work is. **People** —
sized to the task, generally three to seven, with the technical depth and the willingness to
raise a problem early. **Relationships** — these get negotiated whether or not you plan them,
so state them: onboarding, acceptable review tone, and what happens when a date is missed.
Trust grows through **reliability** and is rebuilt through **transparency**.

Tuckman's sequence gives the vocabulary: forming, storming, norming, performing, with
adjourning added later. Naming the stage out loud is the move — it stops an argument being
taken personally.

**Example.** A new squad of four began an eight-week migration. In week 1 everyone agreed to
the plan at kickoff, with no objections at all. By week 3 two of them were quietly building
incompatible retry semantics. In week 6 it surfaced as a rejected pull request, and by then
it was personal. The lead should have asked for the objection in week one by name — *"Marta,
what breaks first if we do it this way?"* — put the contested decision in writing with an
owner and a date, and treated the first real argument as on schedule. A team that skips
storming does not skip the conflict; it pays for it later, in review tone.

Distance and churn are not the same problem. Spreading a team across sites made its problems
happen more often but almost never made them worse, and what suffers is coordination — the
part tooling actually helps. Re-composing a team raised **missing respect** and **anger in
discussions**, and nothing in the toolchain repairs that. Distance degrades coordination;
churn degrades civility. Price the churn before you re-org.

→ [Formation](../people/teams/formation.html)

## 4. Psychological safety buys disclosure, not invention

Psychological safety is the belief that you can raise a problem without being punished for
it. What it buys **first and most reliably** is disclosure: the broken migration script
reported on Tuesday rather than discovered on Friday. What it buys least is a full ideas
backlog — proposing improvements moves the least of all the behaviours measured. So do not
sell safety upstairs as innovation; sell it as early bad news, which is what it delivers.

The lever that moves it is **autonomy** — the team choosing its own tools, branching model
and definition of done. Role clarity and interdependence did not. A RACI chart is not a
safety intervention; handing the team a real decision is.

Composition matters far less than climate. In the largest study, gender, cultural background
and role mix did not predict team effectiveness; only age mix did, and weakly. Relational
conflict did not reduce effectiveness either, against the authors' own hypothesis. Safety
acted **directly** rather than by buffering a diverse team against its own friction. Diversity
is worth having on its own terms — stop defending it with a performance claim nobody has
measured, and spend the effort on the climate.

The cheapest move a lead has: say what **you** got wrong this week, first and out loud.

→ [Psychological Safety](../people/teams/safety.html)

## 5. Social loafing: effort per person falls with size

People in groups do not work as hard as they do alone. Output still rises with group size,
but at a diminishing rate. The mechanism has a name — **social impact theory**: the social
force on a group is divided among its members, so the larger the group, the less pressure any
individual feels.

Three reasons people coast, each with its own fix. **Diffusion of responsibility** —
contributions cannot be told apart, so nobody feels accountable. **Reduced self-efficacy** —
"my effort cannot change the outcome". **Sucker aversion** — the fear of doing all the work
for a fifth of the credit. At a hackathon, one person codes all night, three brainstorm, and
all four put the project on their CV.

What removes it: make contributions visible **and then act on what you see**, give each
person something they own by name, reward performance and feed results back to the team, and
staff to the task rather than generously. The key is not identifiability itself but the
evaluation identifiability makes possible — a dashboard nobody reads reduces nothing.

{: .note }
Two AI findings belong here. When assistants arrived, contributors at the edge shipped far
more commits while **core developers' own output fell about a fifth** as they absorbed the
review load — free riding with nobody free-riding, consuming senior attention and appearing
on no dashboard. Separately, people who coast in human groups still put in less effort with
an AI assistant, but reported **effort saved** rather than frustration. Budget review
capacity before celebrating throughput, and watch the review queue rather than the commit
count.

→ [Social Loafing](../people/teams/loafing.html) · [Deciding with AI](../people/teams/decisions_ai.html)

## 6. Deciding is not one process

A decision commits you before the evidence is in, and the **level** sets the machinery it
earns. **Operational** — approving a pull request: decide and move, the cost of being wrong
is one revert. **Tactical** — choosing a testing framework: write down the alternatives you
rejected. **Strategic** — adopting agile across the organisation: name the stakeholders, the
criteria and the review date before you choose. The common failure is not deciding badly but
**not deciding at all**, because every option has drawbacks and overweighting them stalls
everything.

Experts under pressure do not compare options. In **Recognition-Primed Decision**, a pattern
fires, one workable action arrives with it, and it is simulated forward in the head before
acting. Expectancies make it self-correcting: a violated expectation is how an expert learns
the reading was wrong. Time pressure is an interaction, not a main effect — in chess, blunder
rates barely moved for masters between blitz and regulation play, while weaker players
roughly doubled theirs. Squeezing the clock on an inexperienced team is a different act from
squeezing an experienced one.

Trust a snap judgement when you have genuine experience of **this** pattern, the cue is
behaviour rather than appearance, and you are calm. Distrust it when you are reading
competence off a face, when the instrument does not resemble the real use, or when you have
been asked to explain the judgement — non-experts talk themselves out of judgements that were
right. Structure beats willpower: a screen at a blind audition removed a bias the listeners
sincerely denied holding.

→ [Intuition and Expertise](../people/teams/decisions_intuition.html) ·
[Thin Slicing](../people/teams/decisions_thinslicing.html)

## 7. Group decisions, bias, and what to do about them

Five group decision styles are described, but **three are traps you fall into rather than
options you choose**: no decision at all (topic-jumping, or *the plop* — a proposal met with
silence), the self-appointed decision maker, and minority rule, which leaves the rest with
the impression their opinion does not count. Only two are adoptable: **majority rule**, quick
but apt to produce a win/lose result on complex decisions, and **consensus**, which is mutual
agreement — not compromise and not unanimity. Agree which one you are using **before** you
have to decide.

Rank, not friendliness, is what silences dissent. When the principal engineer opens a
go/no-go with "I think we ship", the juniors holding the flaky-test data comply in advance —
nobody pressured them, they read the room. The chair's moves: speak last, ask the least
senior person first and for their data rather than their view, give someone the job of
arguing the other side out loud, and write every concern up where the room can see it.

The biases that are actually established in software engineering are **individual**:
anchoring, confirmation and overconfidence. The group pathologies — groupthink, the Abilene
paradox — are not among the biases anyone has measured here. Anchoring is the one you will
catch in the act: sprint planning opens with "this should be about three days" and every
estimate clusters there. The fix is procedural, not personal — collect estimates before any
number is said aloud.

On AI advice, the failure runs **in both directions**. One study found incorrect AI
recommendations adopted just over half the time, with a short AI-literacy lesson making
people reject *correct* advice more often. Another found people changing their minds when the
AI was right less often than chance would predict. So "people trust AI too much" gets it
backwards. Reliance is a behaviour, not an attitude: count how often the team takes AI advice
that was wrong **and** how often it refuses advice that was right. Only the first ever
surfaces, as a defect — refusals leave no trace, which is why a team failing at under-reliance
feels appropriately sceptical.

→ [Group Decisions](../people/teams/decisions_group.html) ·
[Groupthink](../people/teams/decisions_groupthink.html) ·
[Cognitive Bias](../people/teams/decisions_bias.html)

## 8. A decision has two outputs

**PEAK** organises a decision so it can be examined later. Four inputs — **P**roblem,
**E**xperience, **A**ssumptions, **K**nowledge — feed a process that produces two outputs:
the **solution** and the **assumed risk**, meaning what may not work as envisioned. Teams
reliably produce the first and skip the second, and with no assumed risk on record the only
thing left to judge a decision by is how it happened to turn out.

That is why you judge the process, not the outcome. A careful decision can end badly and a
careless one can get lucky: a release that shipped fine with no rollback plan was a bad
decision with a good outcome. Record the assumptions and the alternatives that were on the
table, and review the decision against **what was known then**. If nothing was written down,
there is nothing to review — and that is already the finding.

→ [The PEAK Model](../people/teams/decisions_peak.html) · [Decisions](../people/teams/decisions.html)

## Where this goes next

These two lectures are assessed together. The SATERA case asks you to define a problem,
decide, and show the process you used; PEAK is the structure to show it in. Revise with
[RQ1](rq1.html), and see [SN L1a](sn1a.html) for the individual half of the material.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and
**David Root** {% cite root2014lectures %} on software project management. The structure,
examples, and pedagogical approach reflect their teaching materials and frameworks.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
