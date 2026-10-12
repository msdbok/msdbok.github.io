---
parent: Study Notes
title: SN L6a — Release Planning
nav_order: 13
page_type: study-notes
layout: default
---

# SN L6a — Release Planning

A revision summary of the release-planning lecture. **Release planning** decides which features go
into which release when the date is fixed and the backlog is longer than the time. The lecture
follows **Quill 1.0**, the invented word processor from the requirements and risk lectures: six
people, a publisher as the customer, a release due on 1 February that will not move, and a backlog
(open and save, a spell checker, track changes, comments, autosave, mail merge, a grammar checker…)
longer than six people can build by then. Two questions run through all six parts: what can you
**promise** for the date, and what can you only hope for? And when something goes wrong, **what
gives**, and who decides? Each section links to the handbook page carrying the detail and the
sources.

## 1. Releases and iterations

**The date holds; the scope moves.** The release date is fixed, or may be; its content is not, at
least not at first. The sponsor may get less than they would like, and the two sides choose together
what to protect and what to give up. Rubin: *"the variables of date and scope are constantly playing
a game of chicken with each other!"* {% cite rubin_essential_2012 %}. In release planning you decide
in advance that the scope swerves. This is not only agile: Miranda calls such projects *time-bound*,
where the timing of the delivery matters as much as the delivery {% cite miranda_planning_2002 %}.

A **release** ends in *useful* software, for the customer; an **iteration** (sprint) ends in
*working* software, for the team. Release planning decides which features go in which release;
iteration planning decides how this batch gets built. Typical lengths are three to nine months for a
release and one week to one month for a sprint {% cite rubin_essential_2012 %}. For example, after
Quill's first sprint open and save works and the team can demo it, but the publisher's editors cannot
work in a word processor that only opens and saves.

**How often to release is a business decision.** Every sprint ends potentially shippable; shipping it
is the business's choice. One e-store was delivered after 6 weeks and then every 3 weeks, with several
time boxes running at once {% cite jalote2004timeboxing %}. Is an iteration a release? Ask who
receives it.

A fixed-date plan answers *how much?* with a **range**: will have, might have, won't have. Keep the
must-haves at 60–70% of the time, so something can still give {% cite rubin_essential_2012 %}.
*"The end-date for the timebox is not a due date. It's a deadline."* {% cite mcconnell_rapid_1996 %}

Release planning assigns features to a **sequence** of releases, balancing business objectives,
technical dependencies, resource limits and stakeholders who are not equally important
{% cite ruhe2005release %}. **Commit to the next release; sketch the ones after it**, and re-plan
after each delivery {% cite greer_software_2004 %}. Pick a strategy before picking features: a single
release, or incremental ones ordered by threshold of success, themes, risk or return on investment
{% cite miranda_managing_2014 %}. A backlog still needs a reason for its order.

Releasing early also changes **when the money comes back**. In Denne and Cleland-Huang's example, a
year of development has a net present value of −$24K as one release and +$205K as four quarterly
ones: with one release, *"the business is drained of value if it undertakes the project, despite the
positive ROI."* {% cite denne_incremental_2004 %}

→ [Release planning](../plan/release/)

## 2. Choosing what goes in

Release planning is a **knapsack with dependencies**: each feature has a value and a cost, each
release a capacity, and features depend on each other. Values are far from equal: in one Ericsson
project the top requirement was worth about twenty times the least. In Karlsson and Ryan's
**cost–value** approach, customers compare requirements in pairs by value and engineers by cost;
dropping 3 of 14 requirements kept 94% of the value at 78% of the cost. The price is n(n−1)/2
comparisons, and dependencies are ignored {% cite karlsson1997costvalue %}.

**Each method optimises a different goal**: MoSCoW a guaranteed minimum plus contingency, cost–value
value per unit of cost, EVOLVE stakeholder urgency against business value
{% cite greer_software_2004 %}, the Incremental Funding Method net present value, Buffered MoSCoW and
SPID delivery certainty by a fixed date. The computer proposes; a person chooses. Name the factors
your situation needs, then pick the cheapest method that covers them {% cite svahnberg2010release %}.

**MoSCoW**, coined by Clegg and Barker {% cite clegg_case_1994 %}, has four categories, which DSDM
defines by consequence, not importance {% cite dsdm2014moscow %}. A **Must** is the *"Minimum Usable
SubseT"* the project guarantees. A **Should** is important but not vital: a painful workaround exists.
A **Could** is *"the main pool of contingency"*. A **Won't** is agreed not to be delivered *this
time*. For Quill: open and save is a Must, autosave a Should (you can save by hand), the grammar
checker a Could, mail merge a Won't. The test for a Must: *"if I come to you the night before
Deployment and tell you there is a problem with a Must Have requirement and that we can't deliver it
– will you stop the Deployment?"*

DSDM gives Musts **"no more than 60%"** of the effort and Coulds **"around 20%"**, and **no figure for
the Shoulds**: the "60/20/20" you meet in industry infers the middle number. More than 60% is
acceptable only when estimates are accurate, the approach known, the team performing and the risks
low {% cite dsdm2014moscow %}.

→ [Prioritising features](../plan/release/prioritisation)

## 3. Buffered MoSCoW

**Why 60%?** Miranda simulated DSDM's rule: with Musts at 60% of the budget and every feature
overrunning by up to double its estimate, all Musts were delivered about 99% of the time; at 70%,
about a third of the time. It holds when each category has at least five features and none takes more
than a quarter of it {% cite miranda2022moscow %}. Split big features.

**Buffered MoSCoW asks how likely, not how important** {% cite miranda_time_2011 %}. A Must is
delivered *"short of a calamity"*; a Should has *"a fair chance of being delivered"*; a Could arrives
only *"if everything went extraordinarily well"*; a Won't has no budget left at its safe estimate.
The customer still ranks; the **estimates** decide how far down the ranking the time box can promise.

Each feature gets a **normal** estimate, with a fair chance of being enough, and a **safe** one,
enough except in a few really bad cases: Quill's spell checker might take two weeks normally and four
safely. Then the rule:

1. The **customer ranks** the features; the team gives each a normal and a safe estimate.
2. **Musts:** in rank order, with their prerequisites, at their **safe** estimates, until the
   development budget is used. Re-plan them at **normal**; the time freed is the **Must buffer**.
3. **Shoulds:** in the customer's order, at their **safe** estimates, **inside the Must buffer**;
   re-planned at normal, they free the **Should buffer**. **Coulds** go inside the Should buffer.
4. What fits nowhere at its safe estimate is a **Won't**.

Miranda: *"We will repeat the process for the 'should have' and 'could have' requirements using the
size of the buffer protecting the previous category as the initial budget for the current one"*
{% cite miranda_time_2011 %}. Every category is planned at its safe estimate; what differs is whose
overruns it absorbs.

**There are no fixed percentages.** Wide gaps between safe and normal give a small Must set and big
buffers; narrow gaps the opposite. A Should ships only if the Musts come in at or under normal,
roughly half the time; a Could needs the Musts *and* the Shoulds to. So the relative odds are **Must
4 · Should 2 · Could 1**. Tell the sponsor exactly that.

{: .exam-tip }
> **Exam tip:** the common mistake is "the Shoulds take whatever is left, at normal". They are chosen
> in the customer's order, at their **safe** estimates, inside the Must buffer.

→ [Buffered MoSCoW](../plan/release/moscow)

## 4. Running the time box

**A Must overrun costs the Could, not the date.** If Quill's spell checker takes its safe estimate,
the overrun eats the Must buffer and every Must still ships; the Should keeps a fair chance; the Could
becomes unlikely {% cite miranda_time_2011 %}. Nobody renegotiates: the plan said on day one what
would go first.

**A change waits for the next sprint and costs scope.** *When?* At the next iteration boundary; the
running sprint is frozen. *Who?* The customer decides on value; the team advises on cost and risk
{% cite racheva2010agileprio %}. *What gives?* The lowest-priority scope; growth in the Musts goes to
the sponsor {% cite dsdm2014moscow %}. After a demo, Quill's publisher moves comments above mail
merge. At the next sprint planning comments comes in, mail merge drops below the line, and 1 February
stays. Moving the date is a separate decision, by the sponsor, taken last.

**Infrastructure is a feature the others depend on.** Split it into the part each release strictly
needs: Quill's PDF engine comes in with export and print preview {% cite miranda_managing_2014 %}.
**Defects** follow the same logic: critical and major ones are fixed in the time box where they are
found, minor ones later, and the customer chooses between fixes and new features
{% cite miranda_time_2011 %}.

The commitment can be made **once for the project or once per increment**. Per increment means
smaller promises, kept more often; a Could missed in release 1 can become a Must for release 2
{% cite dsdm2014moscow %}.

→ [Buffered MoSCoW](../plan/release/moscow)

## 5. Contracts and incentives

An honest plan promises only the Musts. The risk of partial delivery does not go away; the only
choice is who carries it. Under a **fixed price** the supplier does, and charges a premium, cuts
quality or fights later. Under **time and materials** the buyer does, with no limit on cost. An
**incentive contract** splits it: a base for the Musts, premiums for the Should and Could releases.
*"the incentives and disincentives will prevent the developer from charging a premium price to
protect itself from not delivering all features"* {% cite miranda2022moscow %}.

**Price the contract on its odds, not its best case.** For example, a 4,000-hour time box at $100 an
hour costs $400K; a fixed price of $520K is a 30% markup. Paid on delivery, the client pays $400K for
the Musts only, $500K with the Shoulds and $550K for everything. At odds of one half, one quarter and
one quarter, the expected price is about **$462.5K** {% cite miranda_managing_2014 %}. The supplier
sets the base and premiums on that, or knowingly accepts less money for a lower-risk deal.

Inside the team: *"No reward will be associated with delivering the 'must have' release since the
team members are simply doing their jobs."* {% cite miranda_time_2011 %} Bonuses go to the Should and
Could releases, sized by expected value: $5,000 at even odds is worth about $2,400. A big reward
nobody believes in is a lottery {% cite miranda_planning_2002 %}. Tie bonuses to release completion,
not overtime; training and time off count too.

**Unused buffer gets spent unless handing it on pays.** *"work expands so as to fill the time
available for its completion"* {% cite parkinson1955law %}, and the student syndrome starts work only
when the deadline comes into view: given the same one-hour task, students finished at 4.3 days with a
one-week deadline and 9.1 with two {% cite buehler1994fallacy %}. In Buffered MoSCoW, time a Must does
not use belongs to the next feature the customer wanted. Miranda names these behaviours only to
explain why effort runs late {% cite miranda2022moscow %}; **tying them to rewards is the lecture's
own step**. Reward the Should and Could releases, and the team has a reason to hand the buffer on.

→ [Contracts and incentives](../plan/release/incentives)

## 6. When two estimates are not enough

Independent overruns partly cancel. A **shared cause** does not: an immature open-source library
slows the testing and debugging of every feature that uses it, so they overrun together. With
low-confidence estimates and overruns that move together, all Musts were delivered only about three
times in four {% cite miranda2022moscow %}. Keep features small and independent.

When the sponsor needs a stated probability, use **SPID**, Statistically Planned Incremental
Deliveries: three-point estimates, the first increment filled to about 95% confidence, re-planned at
50%, and the difference handed to the next increment {% cite miranda_planning_2002 %}. Buffered MoSCoW
is its simple version. For "short of a calamity", two estimates are enough; for "95% sure", model it.

{: .exam-tip }
> **Exam tip:** these methods are well argued and thinly measured. Buffered MoSCoW comes from a
> five-page essay, the 4 : 2 : 1 odds are argued, and the 60% simulation covers estimation error, not
> scope change. Quote them as reasoning, never as industry rates.

→ [Buffered MoSCoW](../plan/release/moscow)

## Where this goes next

Quill now has a plan with buffers in it. The next question is how to see, week by week, whether the
buffer is being used up faster than the work is getting done: monitoring and control.

---

### Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda**
{% cite miranda_managing_2014 %} on software project management. Buffered MoSCoW, SPID, the release
strategies, the incentive contract and its pricing example are Miranda's.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
