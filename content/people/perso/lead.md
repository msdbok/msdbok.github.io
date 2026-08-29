---
page_type: deep-dive   # evidence-dense: six-style table plus Hay/McBer provenance and the EI dispute
parent: Personality
title: Leadership
nav_order: 4
layout: default
---

# Leadership styles by Daniel Goleman

_Adapted from lecture materials by David Root {% cite root2014lectures %}._

Leadership style is the habitual way a leader makes decisions, motivates people, manages change and
handles crises. Daniel Goleman describes **six**, each built on different emotional-intelligence
competencies and each moving team climate in a different direction {% cite goleman2000leadership %}.
The best leaders are flexible: they know several and switch to the one the situation asks for.
Applying them is the companion page, [Leading in Practice](lead_practice.html).

## The six styles

Each row gives the style's characteristic sentence, the situation it fits, what it costs when
overused, and its measured effect on climate.

| Style | When it fits | What it costs | Climate | In a software team |
|---|---|---|---|---|
| **Coercive** — "Do what I say" | Real crisis, turnaround, a problem employee | Kills creativity and initiative once it outlasts the crisis | **−.26** | Incident commander driving a rollback during an outage |
| **Authoritative (visionary)** — "Come with me" | A new direction or strategic pivot | Falls flat if the leader lacks credibility with experts | **.54** | CTO sets the mission and OKRs; squads choose the implementation |
| **Affiliative** — "People come first" | Repairing trust; high stress; after layoffs | Hard feedback goes unsaid, mediocrity is tolerated | **.46** | Team lead protecting wellbeing after a punishing release |
| **Democratic** — "What do you think?" | Buy-in is needed, or the ideas are not yet in the room | Slow decisions, sometimes none | **.43** | Architecture settled in cross-functional design reviews |
| **Pacesetting** — "Do as I do, now" | A short, defined push with proven self-starters | Burnout; teamwork and learning erode | **−.25** | Founder demanding rapid MVPs in one sprint |
| **Coaching** — "Try this" | Growing people toward the next level | Slow; needs leader skill and a willing person | **.42** | One-on-one mentoring, pairing, development plans |

The **climate** column is not an adjective chosen here: it is the correlation reported in the
"Getting Molecular" exhibit. Each style was scored against six *drivers of organizational climate* —
flexibility, responsibility, standards, rewards, clarity, commitment — and climate is reported to
account for "nearly a third" of financial results {% cite goleman2000leadership %}.

## The result the researchers did not expect

**Pacesetting, at −.25, is essentially as damaging as coercive at −.26**, and it is negative on five
of the six climate drivers. The authors say so themselves: *"That's not what we expected to find.
After all, the hallmarks of the pacesetting style sound admirable"* {% cite goleman2000leadership %}.
The style that reads best on paper measured second-worst in the data.

That is why the numbers are worth teaching rather than the six labels, and it matters most for
readers arriving from a technical role, where the instinct is exactly *"set a high standard and show
them how."* Two smaller inversions vanish when the ratings become adjectives: **democratic (.43)
ranks below affiliative (.46)** — the article notes its impact "is not as high as you might imagine"
— and **coaching (.42) is the style used least often**.

## What the software-specific evidence adds

The six styles come from a general executive population. The one leadership study in this handbook's
corpus collected **from technical staff** finds a factor that is not among them. Thite surveyed
Australian IS/IT project managers, their subordinates and senior IT managers with an extended
Multifactor Leadership Questionnaire {% cite thite1999leadership %}; principal-components analysis
produced five scales, one new and domain-derived: the **"organisational catalyst"** — shield the
team from organizational bureaucracy, satisfy the desire for autonomy, align individual goals with
organizational ones, implement upper management's decisions dispassionately. Subordinates on the
*more* successful projects rated their managers highest on that scale, ahead of the transformational
one. For example, "prevent organizational bureaucracy from interfering with the work of your
subordinates" is a better opening line for this course than any of the six styles.

## How solid is this?

{: .warning }
**A serious number attached to a study nobody can inspect.** The research behind the six styles is
proprietary Hay/McBer work that was never published, so nothing here can be replicated — and every
figure in the table is a **correlation**, not a causal effect.

- **Where it comes from.** "Leadership That Gets Results", *Harvard Business Review*, March–April
  2000, reprint R00204 {% cite goleman2000leadership %}; the 2006 and 2017 dates attached to it
  elsewhere are Routledge anthology reprints, not later research. Hay/McBer — colleagues of David
  McClelland, the work headed by Mary Fontaine and Ruth Jacobs — sampled **3,871 executives at
  random** from a database of **more than 20,000 worldwide**. No method, instrument, confidence
  intervals or industry breakdown are given; endnote 1 discloses that *"Daniel Goleman consults
  with Hay/McBer on leadership development"*; and the article hedges that "economic conditions and
  competitive dynamics matter enormously." Same shape as the Standish CHAOS numbers in
  [Why Projects Fail](../why.html) {% cite standish2015chaos %}, and the same answer: still the best
  numbers on style and climate, quoted with their provenance attached.
- **What does not transfer.** The population is executives in large organizations, c. 1999: no
  software teams, no individual contributors, no distributed work.
- **What is contested.** McCleskey's review of the emotional-intelligence debate
  {% cite mccleskey2014emotional %} separates the Mayer–Salovey **ability** model of EI, the family
  with the strongest academic standing, from the Boyatzis–Goleman **mixed** model of workplace
  competencies that the six styles rest on. The evidence for EI is real but modest — a meta-analysis
  of 43 studies, n = 5,795 for job performance, showing incremental validity over the Five-Factor
  Model and IQ — while Antonakis and colleagues conclude that either "EI researchers are using the
  wrong measures or the wrong methodology, or EI does not matter for leadership". The styles are
  usable without the theory of mind beneath them.
- **How to read Thite.** 111 organisations were invited and 36 took part, each contributing one
  more- and one less-successful team: 70 project managers, 228 subordinates, 18 senior IT managers.
  One country, one snapshot, self- and subordinate-report only; success is a senior manager's
  judgement, not a measured outcome; one significance test reported; a six-page conference summary
  whose author says it "indicated the direction for" a validated model rather than delivering one.
  Its scale runs 5 = low to 1 = high, so *lower* means are better.

---

### Acknowledgments

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
