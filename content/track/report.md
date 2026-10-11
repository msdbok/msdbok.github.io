---
parent: Tracking
title: Reporting progress
nav_order: 1
layout: default
page_type: method
---

# Reporting progress

A progress report tells the people who fund and steer a project where it stands against the plan,
and what they must decide. It goes wrong in two ways: progress was counted badly, or it was known
and not said.

## 1. Why "90% done" lasts so long

The 90% syndrome is a project that reaches about 90% on schedule, then stalls and finishes at about
twice the planned duration {% cite ford2003ninety %}. Subjective reporting is the second cause. The
first is **rework nobody has found yet**.

Ford and Sterman's Python project, a chip design rather than software, counted progress in lines of
design code. It was 73% complete at its week-39 deadline, its rate halved, and it finished in
week 69. Work was marked done, its errors surfaced later in testing, and everything built on it went round
again: *"the downstream phases outrun the discovery of inherited rework requirements."*

For example, in our software reading, a word-processor team marks export features done when merged.
Integration testing in week 30 finds the file layer mishandles three character encodings, and every
feature that writes a file goes back. The board said 90%; nothing about the count was subjective.

So "done" has to include tested. Brooks wants milestones *"defined with knife-edge sharpness"*
{% cite brooks_mythical_1995 %}; McConnell makes them binary, done or not done
{% cite mcconnell_rapid_1996 %}. Percent complete is calculated, never asked for: finished tasks
over all tasks, work under way counting zero {% cite wysocki2003tracking %}.

## 2. Reports fail more from silence than from ignorance

Snow and Keil split status error in two: the project manager may *misperceive* the true status, or
perceive it and *report it better* {% cite snow2002status %}. Under moderate good-news bias, their
model has a truly Red high-risk project reach the executive as Green about half the time, and halving
the perception error barely changes that. Distortion is *"likely to be significantly higher in
organizations where 'bad news gets you killed.'"* The reader of the reports owns the climate.

Silence is the norm. 85% of Milliken's interviewees had held back an important issue, most often
someone's competence, mostly for fear of being labelled a troublemaker
{% cite milliken_exploratory_2003 %}. In Keil's experiment, willingness to report fell at each step
up the hierarchy, and further where messengers had been punished {% cite keil2004badnews %}.

A manager can change four things:

- Walk around and ask *"can you show me?"*, which turns a percentage into done or not done.
- Act on what you hear, or say why not; people stop telling a manager who does nothing.
- Ask for one light per dimension (cost, schedule, function), since one overall colour is easy to
  round up {% cite snow2002status %}.
- Print what the colours mean: Yellow comes with a get-well plan, Red has none and asks for help
  {% cite wysocki2003tracking %}.

## 3. Example: a status report that answers first

A status report asks its reader to decide, so it takes the [Minto pyramid](../people/perso/minto.md):
answer, then reasons, then evidence. The usual template puts the decision needed in its last line.
Reordered, the word processor's report opens:

> **Schedule Yellow: export slips two weeks unless release 1 drops RTF import. Decision needed by
> Friday. Cost and function Green.**
>
> *Schedule, Yellow.* 9 of 12 milestones done; integration found an encoding defect, two weeks of
> rework. Get-well plan: move RTF import to release 2.
>
> *Cost, Green.* 410 hours spent on work budgeted at 450.
>
> *Function, Green.* Every release 1 feature but export passes its acceptance tests.

Below the lights, the standard contents become evidence: forecasts, baseline and change requests,
indicators such as [earned value](evm.md), issues, risks, and the period's chronicle last. Nothing is
added or cut; only the order changes.

**Milestone trend analysis** belongs there too. At each report, plot every milestone's forecast
date. A flat line is stable; a climbing line is a milestone slipping in small steps, which is how a
project gets a year late, *"one day at a time"* {% cite brooks_mythical_1995 %}.

## 4. When to use it, and when not

Use answer-first for any report that asks a sponsor to decide. Do not use it where chronology is the
content, such as an incident timeline. And no ordering rescues a climate where Red is unsafe.

## How solid is this?

- **Where it comes from.** Ford and Sterman's cases are chip projects and a simulation; the software
  readings are ours. Brooks, McConnell and Wysocki assert their rules from practice.
- **What is contested.** Snow and Keil's figures come from a model built on five experts' estimates:
  "about half" is a direction, not a measured rate. Keil's study is a role-play; Milliken's, 40
  interviews.
- **What we do not hold.** Evidence that answer-first reports or walking around reduce distortion, or
  that binary milestones prevent the syndrome rather than reveal it sooner. Applying Minto to status
  reports is our step.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite miranda_managing_2014 root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
