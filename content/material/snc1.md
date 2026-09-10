---
parent: Study Notes
title: SN C1 — Structured Communication
nav_order: 5
page_type: study-notes
layout: default
---

# SN C1 — Structured Communication

A revision summary of the C1 recitation, which teaches the **Minto pyramid** — the method behind the
slide and report rules every case in this course is judged against. It makes one move at three
scales: put the answer first, group the reasons so the grouping holds, and cut whatever supports
nothing. The handbook page underneath carries the detail and the sources.

Read this before a case presentation or before writing a case report. The rules in the case handout
are the output of this method; this note is the method.

## 1. Order is the problem, not vocabulary

Barbara Minto developed the pyramid at McKinsey in the 1960s while teaching consultants to write
{% cite minto_pyramid_2009 %}. Her diagnosis: unclear writing is rarely caused by long sentences or
poor word choice. It is caused by **order**. Most prose follows the sequence in which the thinking
happened — investigate, weigh, conclude — and that is the one sequence a reader cannot use, because
the reader wants to know the conclusion in order to judge whether the rest is worth reading.

The consequence is stronger than "it is harder to follow". Give a reader three true facts with no
stated relationship and they will *build* a relationship, because that is what comprehension is —
Minto defines an idea as *"a statement that raises a question in the reader's mind because you are
telling him something he does not know"*. The structure they build will not be yours, and they will
not know they got it wrong. **A reader's wrong conclusion is the writer's error.**

So you **think bottom-up**, from data to finding, and **present top-down**, from finding to data.
Those are two different orders and the second is not a summary of the first — it is a re-ordering of
the same material. Nothing is added; nothing is removed.

→ [The Minto Pyramid](../people/perso/minto.html)

## 2. Answer first, and what that does not mean

For example, take a proposal to replace a logging library. Bottom-up it arrives as: the library
handles a terabyte a day;
three services fail in a cascade at peak load; firefighting costs about sixteen engineer-hours a
week; a rewrite is two engineer-months; on balance we should probably rewrite it.

Answer first, same facts: **rewrite the logging library this quarter — two engineer-months, breaking
even in five**, because it causes cascading failures at peak load, it costs sixteen engineer-hours a
week, and it pays back inside five months.

Two things to notice. The recommendation moved from the last sentence to the first three words. And
*probably* disappeared — not because answer-first requires confidence, but because the evidence
always supported the stronger sentence. **Hedging is usually not caution; it is what you write when
you have not decided what you think.** The converse holds too, and matters more: if the evidence
only supports *probably*, write *probably*. Answer-first is a rule about order, never a licence to
claim more than you have.

## 3. The vertical relationship: a claim raises a question

Every claim that tells the reader something new forces a question — *why?*, *how?* — and the level
below the claim exists to answer it. That is what makes a pyramid readable rather than merely tidy,
and it gives one discipline worth memorising: *"refrain from raising any questions in the reader's
mind before you are ready to answer them"* {% cite minto_pyramid_2009 %}.

This is why a deck that opens with facts feels inert. No question is running through it, so nothing
pulls the audience to the next slide. It is also why a slide collecting assumptions *before* the
claim they support does nothing for a reader: they do not yet know what is being argued, so an
assumption cannot mean anything to them. Put each assumption under the claim it carries.

## 4. The horizontal relationship: chains break, groups do not

Reasons under a claim are joined one of two ways, and never both at once.

A **deductive** grouping is a chain: *every service on the shared database slowed* → *checkout runs
on the shared database* → *therefore checkout slowed*. A chain is how problems get **solved**, and it
is a poor way to **present**, for two reasons. It forces the audience to re-enact your whole analysis
before they learn anything, and it fails at its weakest link — if the first premise is wrong the
conclusion does not weaken, it vanishes. In cross-examination that means one good question can take
down the entire argument.

An **inductive** grouping is a set of independent points sharing one characteristic, from which you
draw an inference: *checkout p99 ×4*, *search p99 ×4*, *profile p99 ×4* → **the shared database is
the bottleneck**. Lose one observation and the inference still stands on the other two.

The practical test on your own draft: **does reason two only make sense after reason one?** If it
does, you have built a chain and dressed it as a group.

## 5. Grouping: the plural-noun test

A grouping holds only if you can name it. Minto's shortcut is that *"you can clearly label the ideas
with a plural noun"* {% cite minto_pyramid_2009 %} — reasons, problems, steps, options. If the only
word covering your list is *points* or *things*, the grouping is wrong, and the fix is in the
analysis rather than the wording. This is the requirement usually called **MECE** (mutually
exclusive, collectively exhaustive) in a form you can apply in seconds: no two of your reasons are
the same reason in different words, and together they answer the question *you* raised.

Three reasons is a convention, not a rule. Minto grounds the count in short-term memory — the mind
holds about seven items — and her line is *"a convenient number is three, but of course the easiest
number is one."* **Two reasons that genuinely cover the question beat three where one is a detail in
disguise, and a fourth real reason beats three plus filler.**

The order must also be one you can name. Minto allows exactly four: **deductive, chronological,
structural, or comparative** (by importance). An order chosen for convenience is not one of them —
and an order gives itself away. A list of criticisms that happens to run alphabetically tells the
reader immediately that nothing was reasoned.

## 6. Headings state claims, not categories

A heading must say what the material under it *implies*, not what kind of material it is.
*"Logging library analysis"* names a category and asserts nothing; *"the logging library costs
sixteen engineer-hours a week"* is a claim a reader can act on or dispute. A label cannot be wrong,
because it says nothing — which is exactly why it feels safe and earns nothing.

The fastest check on a finished deck or report: **read only your titles, in order, and nothing
else.** If that reads as your argument, the structure holds. If it reads as a table of contents, it
does not. And if a title would fit equally well on somebody else's slide, it is doing no work.

## 7. The so-what test

Go through the draft line by line and ask *"so what?"* of each sentence, meaning: **which reason or
which conclusion does this support?** Silence means cut. *"We traced the incidents"* narrates the
investigation rather than reporting the finding. A bare date supports nothing until you pair it with
what changed.

One exception, and it is important because a room told to cut aggressively will cut the wrong thing:
**risks, constraints and next steps are not reasons, and must not be deleted as though they were.**
They get a slot at the close — and a risk severe enough to change the recommendation belongs beside
the answer, not at the end.

## 8. The introduction, and the report

The answer should not arrive cold. Minto's introduction puts the reader on ground they already
accept, so your conclusion lands as the answer to a question they now hold: **S**ituation →
**C**omplication → **Q**uestion → **A**nswer.

The Question is usually never written down — a Complication that does its job raises it unaided, and
if you find you have to spell it out, the Complication was too weak. Keep the Situation short; a
bloated Situation is the commonest failure, because it is the safest part of a document to write.

The report is then **the same pyramid in sentences, in the same order as the slides** — not a
different document. Same claim, same reasons, same sequence.

## 9. Where it does not apply

The pyramid is for documents that ask a reader to accept a judgment or make a decision. It is the
**wrong** shape where chronology is the content — incident write-ups, runbooks, procedures, project
timelines — because time order is already the logical order there. It is also wrong for exploratory
work: it demands a conclusion, and forcing one you have not reached produces a confident-sounding
document resting on nothing.

Where an audience will reject your conclusion before hearing why, lead with the shared problem and
let the answer land a beat later — still in the first paragraph. And note that structure guarantees
nothing about correctness: a well-built pyramid over bad evidence only makes a wrong conclusion
easier to find.

## Four questions to run on any draft

1. **Is the first line an answer?** Not a topic, not a promise to analyse — a claim someone could disagree with.
2. **Can you put a plural noun on the reasons?** If only *points* fits, regroup.
3. **Does every reason answer the question the answer raises**, and does anything overlap?
4. **Ask "so what?" of each remaining line.** Silence means cut — then check the risk you owe the reader is still there.

→ [The Minto Pyramid](../people/perso/minto.html) · [Communication](../people/perso/comm.html)

---

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
