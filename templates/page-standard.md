# MSDBOK Page Standard

**What this site is.** MSDBOK accompanies the MSD lectures and slides. A page gives a student
**brief extra information** around what was taught — enough to understand the idea without the
lecturer in the room, and not one word more. It is not a textbook and not a literature review.

Target: a method page is read in **two to four minutes**, standing up, the evening after the
lecture.

---

## 1. Page types and budgets

| Type | Body words | Purpose |
|---|---|---|
| **Hub / index** | 100–250 | Orientation and links only. No teaching content |
| **Topic hub** | 250–500 | One paragraph of framing + a comparison table + links to detail pages |
| **Method / concept** | **400–800** (aim ~600) | The default page. One method, one page |
| **Deep dive** | ≤1,200 | Evidence-carrying. Must be labelled as such |
| — | **>1,500 → split** | Hard cap. See §2 |

Body words exclude front matter, the References block, Acknowledgments and the Disclaimer.

Run `python scripts/check_pages.py` to see where a page sits.

---

## 2. Long topics: summary page + one page per method

**Do not put eight methods on one page.** When a topic covers several comparable methods, use
hub-and-spoke:

```
proc/frameworks/
├── index.md        ← topic hub: what frameworks are for, comparison table, links
├── rup.md          ← one method, 400–800 words, full method template
├── xp.md
├── scrum.md
└── …
```

**The hub carries the comparison**, because that is the thing a reader cannot get from any single
spoke: one row per method, three to five columns (*What it optimises · Best fit · Main cost ·
Where to read more*). The hub is where someone decides which spoke to open.

**Each spoke is self-contained** and follows §3. A reader arriving from a search engine must not
have to visit the hub first.

This is the fix for any page over 1,500 words. Splitting is preferred to cutting: the material is
usually fine, it is the packaging that fails.

---

## 3. Required elements — a method page

Every method/concept page has all six. The first four are what make a page *understandable*; the
data says they are what is usually missing.

1. **A one-sentence definition in the first 40 words.** Before any history, any caveat, any list.
   The reader must know what the thing *is* before the page asks anything of them.
2. **When to use it — and when not.** Two short lists, or two sentences.
3. **At least one concrete example, in software.** Not "*Example:* choosing a tool" but an actual
   worked instance with real nouns: a sprint, a defect count, a specific decision. **This is the
   most common defect on the site** — most pages have no example at all. A page without one is
   incomplete, however tidy its bullets look.
4. **At least one limitation or pitfall.** What the method does *not* do, or where it misleads.
5. **A source.** A `{% cite %}` where the area has been reviewed; a named book or author
   otherwise. If nothing is held, say so plainly rather than implying evidence that is not there.
6. **The standard footer** (§6).

---

## 4. Style caps

These exist because the site drifted to both extremes: some areas are 81% bullets with nothing
explained, while reviewed areas grew into essays.

| Rule | Why |
|---|---|
| **Bullets ≤60% of body words** | A wall of bullets is notes, not explanation. It reads as complete and teaches nothing |
| **Every bullet list needs a lead-in sentence** | Say what the list *is* before listing it |
| **A bullet is a full clause** | "Autonomy" is a label; "Autonomy predicts psychological safety more reliably than role clarity does" is information |
| **≤2 callouts** (`.note` / `.warning`) per page | When everything is flagged, nothing is. Callout fatigue is real — one page reached thirteen |
| **Heading depth ≤ H3** | H4 means the page should have been split |
| **Keep the numbered-H2 template** | `method-template.md`; already used by 30 pages |

---

## 5. Evidence goes at the bottom, not in the flow

Reviewed areas carry real evidential nuance — sample sizes, contested figures, constructs that did
not replicate. **That nuance is worth keeping and must not interrupt the teaching text.**

Teaching text stays lean and confident. Everything about *how well established* the material is
goes into one section, second-to-last, with the same heading everywhere:

```markdown
## How solid is this?

- **Where it comes from.** Tuckman's 1965 review covered 50 articles, 26 of them therapy groups
  and 11 human-relations training groups — not work teams.
- **What is contested.** Only one study in twelve years was designed to test the stages, and its
  observers were given the stage descriptions and asked to fit observations to them.
- **What we do not hold.** Janis 1982 is not in this bibliography, so no remedy list is given.
```

A reader who wants the caveats finds them in the same place on every page. A student following the
slides is never interrupted by them.

**Inline exception:** where a *specific number on the page* would actively mislead if quoted — a
contested accuracy figure, a statistic whose source says the opposite — flag it in one short
sentence where it appears and put the detail below. That is the only reason to break the flow.

---

## 6. Structure and footer

```markdown
---
parent: [Section]
title: [Page Title]
nav_order: [N]
layout: default
---

# [Page Title]

[One-sentence definition. Then the body — numbered H2 sections per method-template.md.]

## How solid is this?          ← reviewed pages only

---

### Acknowledgments             ← any page derived from Miranda / Root material

This page adapts material from lectures by Eduardo Miranda and David Root
{% cite root2014lectures %} on software project management.

### References

{% bibliography --cited %}

---

{: .highlight }
**Disclaimer:** AI is used for text summarization, polishing and explaining. Authors have verified
all facts and claims. In case of an error, feel free to file an issue.
```

- **Exactly one H1**, matching `title`.
- **References always use `{% bibliography --cited %}`** — never a hand-numbered list. jekyll-scholar
  fails *silently* on an unknown key, so run `python scripts/check_citations.py` too.
- **Acknowledgments are required** on anything derived from the Miranda/Root lectures.

---

## 7. Checklist before committing a page

- [ ] Definition in the first 40 words
- [ ] At least one concrete software example
- [ ] At least one limitation or pitfall
- [ ] Word count inside the budget for its type
- [ ] Bullets under 60%; every list has a lead-in
- [ ] No H4; at most two callouts
- [ ] Evidence in *How solid is this?*, not scattered inline
- [ ] `python scripts/check_pages.py` clean
- [ ] `python scripts/check_citations.py` clean
- [ ] `bundle exec jekyll build` succeeds, and the page was **read in the rendered HTML**
