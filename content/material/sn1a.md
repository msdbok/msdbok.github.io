---
parent: Study Notes
title: SN L1a — The Technical Person
nav_order: 1
page_type: study-notes
layout: default
---

# SN L1a — The Technical Person

A revision summary of the first People lecture, which is about **one engineer at a time**:
what you are actually paying for, what personality models can and cannot tell you, how
distance and culture change the work, what moves motivation, and which leadership style to
reach for. Each section links to the handbook page that carries the detail and the sources.

## 1. What you are paying for is thought

The output of an engineer is a decision that has already been made in their head. You cannot
inspect it the way you inspect a weld, and every attempt to manage it by controlling
behaviour — activity targets, hours present, process compliance — measures the wrong thing
and tends to reduce the thing you wanted.

The working archetype is a person who trusts reasoning over rank, wants the problem before
the solution, treats self-expression as communication, values autonomy and the good opinion
of peers, and is loyal to the craft rather than to the firm. Use it as **vocabulary** for
what you see in the room. Do not use it to predict who you hired: forty years of personality
research in software engineering has found no consistent profile.

The practical consequence is **interruption**. The work happens in flow, one long assembled
context, so a day cut by three meetings is not half a day of output — the cost is re-entry,
not the length of the meeting. What you do about it is unglamorous: blocked focus time
defended like a customer meeting, one meeting-free day for the whole team rather than per
person, and interruptions batched into a window instead of trickling through the afternoon.

→ [Geeks](../people/perso/glen.html) · [Leading in Practice](../people/perso/lead_practice.html)

## 2. Personality models, and what they do not do

MBTI sorts people on four preferences — energy from activity or reflection, information as
facts or patterns, decisions by logic or values, the world met scheduled or open — giving
sixteen codes. Four preferences is the whole of what the instrument claims.

Engineers do self-select. Compared with the general population, ISTJ is roughly twice as
common and INTJ about three times; the sociable, harmony-oriented types thin out sharply.
That tells you something about the **room's default**, and nothing whatever about the person
in front of you.

What it must not be used for is staffing. A review covering twenty-two years retrieved
thirty-five studies, of which twelve addressed team composition and nine measured
personality — and **none** found an association with team performance. So "mix the
personality types", "pair an ISTJ with an INTJ", and choosing how to give someone feedback
from a four-letter code are folk practice.

Three things *are* associated with performance, and a manager can change all three:
**psychological safety**, **team autonomy**, and **stable membership**. Personality type is
not on that list.

→ [MBTI](../people/perso/mbti.html) · [Team Performance](../people/teams/performance.html) ·
[Psychological Safety](../people/teams/safety.html)

## 3. Culture scores a country, never a person

Hofstede's six dimensions come from workplace values aggregated **by country**, scored 0–100,
and are only meaningful read relatively. France scores 76 on uncertainty avoidance against
48 for the United States. That predicts that the French half of a team will want the test
plan written down. It does not tell you that any particular French engineer does.

Cultural difference bites in five recognisable places: whether a decision needs written
approval before work starts, who will disagree in public, how much detail a specification
carries before anyone codes, whether credit is individual or shared, and how a slipping
deadline gets reported and how early.

**Example.** A mixed US–French squad hit a mid-sprint scope swap. One half started that
afternoon; the other wanted an impact assessment and a schedule change, and the sprint
stalled in an argument about process rather than about the work. The fix was not cultural
training. It was two lanes: changes inside a squad's own code go the fast lane, priced at a
rollback plan and a test; anything touching a cross-team API needs a one-page change request
with a named approver. No national attribution was made, and the argument stopped recurring.

Everything that works here is cheap and serves both halves of the team — agendas circulated
in advance, decisions recorded after, architecture decision records, who decides and by when
named in the ticket, and an anonymous channel wherever public dissent is unlikely.

→ [Culture](../people/perso/culture.html)

## 4. Listening is a technique

Procedure settles who decides; everything before that depends on whether people heard each
other. Listening breaks in predictable ways — attending only to the facts and missing the
concern underneath, composing your reply while the other person is still speaking, finishing
their sentences. Thought runs far faster than speech, and the gap fills with your own
argument.

The repairs are mechanical: **paraphrase** — say back in your own words what you think was
said; send meeting notes and invite correction; ask questions that are not challenges.

The same message can be delivered constructively or destructively with identical content —
only the delivery changes, and with it whether you get morale or resentment. Two moves carry
most of it: choose the **approach** (the when and the where, which is the first thing dropped
in a busy week), and **build bridges** by naming the behaviour rather than the person.

For meetings, the test is whether people need to **build something together** or to be
**told something**. Retrospectives, planning and technical design want a room; large
information-sharing is better remote. Do not fill office days with back-to-back meetings —
that kills the informal conversation you came in for.

→ [Communication](../people/perso/comm.html)

## 5. Motivation: two lists, not one scale

Herzberg's separation is the one to hold. **Motivators** are intrinsic to the work —
achievement, recognition for it, the work itself, responsibility, advancement, growth.
**Hygiene** factors are the surroundings — policy and administration, supervision, working
conditions, salary, relationships, status, security. Fixing hygiene stops you losing people;
it does not buy effort. Repairing a flaky test suite buys back attention, but being trusted
to design the service is what keeps someone.

Asked directly, engineers rank **identifying with the task** first — clear goals, knowing
what the work is for — ahead of good management, a career path, rewards, recognition and
autonomy. The leading de-motivator is a poor environment with no resources. Pay and
recognition rank behind purpose, so opening every assignment with what it is for is free and
sits at the top of both lists.

Two theories are worth carrying as diagnostic tools rather than measurements.
**Self-determination**: people engage when autonomy, competence and relatedness are met — so
ask which of the three is missing for this person. **Expectancy**: effort leads to
performance leads to reward, and is the reward worth having — one belief at zero makes the
whole chain zero, which is why a bonus nobody believes will pay out motivates nobody however
large it is.

{: .note }
Working with an AI assistant scored better than working with a person on relatedness,
competence, autonomy and interest — but performance rose while the sense of control fell,
and on the **handoff back** to unassisted work motivation dropped and boredom rose. Treat
that handoff as a real transition, and never return only the tedious remainder.

→ [Motivation](../people/teams/motivation.html)

## 6. Leadership: switch styles, do not have one

Goleman's six styles are a repertoire to move between, not personality types. **Coercive**
("do what I tell you") fits a real crisis and kills creativity if it outlasts one.
**Authoritative** ("come with me") sets a new direction but falls flat without credibility
among experts. **Affiliative** ("people come first") repairs trust and lets hard feedback go
unsaid. **Democratic** ("what do you think?") buys commitment and decides slowly.
**Pacesetting** ("do as I do, now") suits a short defined push and burns people out.
**Coaching** ("try this") grows people and is slow.

Pacesetting is the trap for anyone arriving from a technical role, because the instinct is
exactly *set a high standard and show them how*. Timebox it or do not start it. The general
move is to announce the mode and how long it lasts: "intense delivery for two weeks, then a
refactoring pause" costs nothing and removes most of the resentment a crunch generates.

One finding sits outside that list and comes from technical staff rather than executives.
Subordinates on the more successful projects rated their managers highest as an
**organisational catalyst** — shielding the team from bureaucracy, satisfying the desire for
autonomy, aligning individual with organisational goals, and implementing upper management's
decisions dispassionately.

→ [Leadership](../people/perso/lead.html) · [Leading in Practice](../people/perso/lead_practice.html)

## 7. The measurement lesson

Experienced developers working on repositories they had maintained for years forecast that
AI assistance would cut task time by about a quarter. Afterwards they believed it had cut it
by about a fifth. Measured, it **added** about a fifth. A separate trial inside a large
company found the opposite sign — AI shortened time on task by roughly a fifth, with wide
uncertainty.

The lesson is about management, not about AI: three different answers about the same work,
and only one of them was a measurement. Anyone who tells you what AI does to productivity is
quoting one of these studies and not the other. If it matters to your plan, measure it on
your own team.

The same habit applies to everything above. Before repeating a number to your team, name the
**population**, the **task**, and **who measured**. The geek archetype is one practitioner's
experience; the MBTI figures are a small sample from one country in 2003; the six leadership
styles were never published and studied executives rather than engineers. The psychological
safety, autonomy and stable-membership results, and the review of what engineers report
wanting, carry more weight.

## Where this goes next

L1a is one person. L1b is five, and little of this survives the addition unchanged: adding
people subtracts output, effort per person falls, and groups can decide worse than any of
their members alone. See [SN L1b](sn1b.html), then test yourself with
[RQ1](rq1.html).

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
