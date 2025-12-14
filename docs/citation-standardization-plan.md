# Citation Standardization Plan

## Objective

Establish consistent citation and attribution practices across all MSDBOK content pages.

---

## Standard Patterns Established

### 1. **Acknowledgments Section** (For Heavily Inspired Content)

**When to use:** Pages heavily based on lectures or teaching materials

**Format:**
```markdown
## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.
```

**Placement:** After main content, before Sources section

**Pages that need this:**
- ✅ content/plan/index.md (DONE)
- ✅ content/plan/activities.md (DONE)
- ✅ content/plan/milestones.md (DONE)
- ✅ content/material/trscp.md (DONE)
- ✅ content/material/trsd.md (DONE)
- ✅ content/material/trswbs.md (DONE)
- ✅ content/people/index.md (DONE)
- ✅ content/people/teams/*.md (DONE - 4 files)
- ✅ content/people/perso/index.md (DONE)
- ✅ content/needs/reqs/*.md (DONE - 4 files)
- ✅ content/needs/risks/*.md (DONE - 4 files)
- ✅ content/needs/exp/index.md (DONE)

---

### 2. **Sources Section** (Standard for All Pages)

**Header:** `## Sources` (standardized - not "References", "Source", etc.)

**Format:**
```markdown
## Sources

- Author, Name. *Title of Work*. Publisher, Year. ISBN. [Link](URL)
- Author, Name. "Article Title." *Journal*, vol. X, Year, pages. [Link](URL)
```

**Placement:** After Acknowledgments (if present), before Disclaimer

---

### 3. **Attribution Phrases**

| Phrase | Use Case | Placement |
|--------|----------|-----------|
| `_Adapted from X (Year)_` | Major restructuring/rewriting of X's content | After frontmatter, before first heading |
| `*Based on X*` | Derived from or inspired by X's framework | Near title or in intro paragraph |
| `**Source:** X` | Direct reference/quote from X | Inline or near title |

---

## High Priority Fixes

### A. Missing Citations

| File | Issue | Action |
|------|-------|--------|
| content/plan/gantt.md | Mentions Henry Gantt, no citation | Add Gantt, Henry L. citation |
| content/people/perso/glen.md | Extensive Paul Glen content | Add Glen, Paul. *Leading Geeks* citation |
| content/scope/wbs/index.md | References NASA handbook | Add NASA citation |

### B. Header Standardization - UPDATED APPROACH

**New best practice: Dual-header pattern**

When content cites BOTH academic papers AND educational materials, use BOTH headers:

```markdown
## References

1. [Academic papers, journal articles with DOI]

---

## Acknowledgments

[Standard acknowledgments text]

---

## Sources

- [Books, handbooks, lecture materials]
```

**When to use each:**
- **References** = Academic papers, journal articles (IEEE/ACM style, with DOI)
- **Sources** = Books, handbooks, lecture materials, websites
- Files can have both if they cite both types

**Files already using dual-header pattern:** ✅
- content/plan/release/index.md (References + Sources)
- content/plan/release/moscow.md (References + Sources)

**Files with only "References" - need review:**
- content/proc/frameworks/overview.md (check if needs Sources too)
- content/proc/frameworks/details.md (check if needs Sources too)
- content/track/burndown.md (check if needs Sources too)

### C. Duplicate Citations - Hoover et al.

**Current variations:**
1. "Source: Hoover et al, Evaluating Project Decisions"
2. Full citation with ISBN
3. Parenthetical inline
4. In Sources section

**Standard format to use:**
```markdown
## Sources

- Hoover, Carol L., Mel Rosso-Llopart, and Gil Taran. *Evaluating Project Decisions: Case Studies in Software Engineering*. Addison-Wesley Professional, 2010. ISBN-13: 978‐0321544568. [O'Reilly Media](https://www.oreilly.com/library/view/evaluating-project-decisions/9780321685629/)
```

**Pages to update:**
- content/needs/exp/quadrant.md
- content/needs/exp/tos.md
- content/people/teams/decisions.md
- Others using Hoover reference

### D. Eduardo Miranda and David Root Full Citations

**Standard format for Miranda:**
```markdown
- Miranda, Eduardo. *Managing Software Development*. Lecture materials, 2014.
```

**Standard format for Root:**
```markdown
- Root, David. *Managing Software Development*. Lecture materials, 2014.
```

**Note:** University affiliation removed as lectures were not at CMU. Title confirmed as "Managing Software Development" (not "Projects").

---

## Medium Priority Fixes

### E. Inline Citations Cleanup

**Pages with both inline AND end Sources section:**
- Ensure inline citations match Sources section format
- Remove redundant entries
- Keep inline only for specific claims/quotes

### F. Citation Format Consistency

**Standardize to:**
- Academic citations in Sources section
- Include URLs as markdown links
- Use consistent punctuation and italics

**Before:**
```markdown
Thompson, Leigh L. Making the Team: A Guide for Managers, 3rd ed. Pearson Education, 2008.
```

**After:**
```markdown
- Thompson, Leigh L. *Making the Team: A Guide for Managers*, 3rd ed. Pearson Education, 2008.
```

---

## Implementation Plan

### Phase 1: Template Updates (Week 1)

1. ✅ Update templates/method-template.md with standard citation format
2. ✅ Update templates/analysis-template.md with Acknowledgments + Sources sections
3. ✅ Update CONTRIBUTING.md with citation guidelines

### Phase 2: High Priority Pages (Week 2)

1. Add missing citations (gantt.md, glen.md, wbs/index.md)
2. Standardize all section headers to "## Sources"
3. Add Acknowledgments + Miranda citation to 5 remaining pages
4. Standardize Hoover citations

### Phase 3: Medium Priority Pages (Week 3)

1. Clean up inline citation redundancies
2. Format all Sources sections consistently
3. Review and fix remaining inconsistencies

### Phase 4: Verification (Week 4)

1. Automated check: grep for "## Reference" (should be 0)
2. Automated check: grep for "## Source\n" singular (should be 0)
3. Manual spot-check 10 random pages
4. Update citation analysis document

---

## Automation Opportunities

### Scripts to Create:

1. **find-citation-headers.sh**
   ```bash
   # Find all non-standard headers
   grep -r "^## Referen" content/ --include="*.md"
   grep -r "^## Source$" content/ --include="*.md"
   ```

2. **list-missing-sources.sh**
   ```bash
   # Find pages without Sources section
   for file in content/**/*.md; do
     if ! grep -q "^## Sources" "$file"; then
       echo "$file"
     fi
   done
   ```

3. **check-miranda-citations.sh**
   ```bash
   # Find "Adapted from" without corresponding Sources entry
   grep -l "Adapted from Eduardo Miranda" content/**/*.md | while read file; do
     if ! grep -q "Miranda, Eduardo" "$file"; then
       echo "Missing Miranda citation: $file"
     fi
   done
   ```

---

## Template Standard (Copy-Paste Ready)

### For Pages with Acknowledgments:

```markdown
---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management. The structure, examples, and pedagogical approach reflect their teaching materials and frameworks.

---

## Sources

- [Author citations here]

- Miranda, Eduardo. *Managing Software Development Projects*. Lecture materials, Carnegie Mellon University, 2014.

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
```

### For Pages without Acknowledgments:

```markdown
---

## Sources

- [Author citations here]

---

{: .highlight }
**Disclaimer:** AI is used for text polishing and explaining. Authors have verified all facts and claims. In case of an error, feel free to file an issue.
```

---

## Progress Status (Updated 2025-01-XX)

### ✅ Completed

**Format standardization (10 files):**
- Changed format from `_Adapted from Author (Year)_` to `_* adapted from Author, Year_`
- Added Acknowledgments sections
- Added proper Sources citations

**Miranda-based (6 files):**
1. ✅ content/track/index.md
2. ✅ content/plan/release/moscow.md
3. ✅ content/plan/release/index.md
4. ✅ content/plan/release/incentives.md
5. ✅ content/scope/estimates/index.md
6. ✅ content/scope/wbs/index.md

**Root-based (4 files):**
1. ✅ content/proc/basics/index.md
2. ✅ content/proc/index.md
3. ✅ content/proc/lifecycles/index.md
4. ✅ content/proc/frameworks/index.md

### 🔄 Remaining Work

**21 files still need format update:**
- All have old `_Adapted from Author (Year)_` format
- Most already have Acknowledgments sections
- Just need format change to `_* adapted from Author, Year_`

**Files to update:**
- content/plan/index.md, activities.md, milestones.md (3 files)
- content/material/trscp.md, trsd.md, trswbs.md (3 files)
- content/needs/reqs/*.md (4 files)
- content/needs/risks/*.md (4 files)
- content/needs/exp/index.md (1 file)
- content/people/index.md, teams/*.md, perso/*.md (6 files)

---

## Success Metrics

- [x] Dual-header pattern (References + Sources) established
- [x] Miranda citation standardized (removed CMU, fixed title)
- [x] Root citation standardized
- [x] 10 files updated with new format
- [ ] All 31 files use new `_* adapted from Author, Year_` format
- [ ] Hoover citations standardized (1 canonical format)
- [ ] All high-priority missing citations added
- [ ] Templates updated with citation standards

---

## New Citation Rules (2025 Update)

### 1. Inline Source Attribution

**Rule:** When sources are mentioned close to section headers or specific content, keep explicit attribution inline.

**Format:**
```markdown
## Section Title

_Based on Author (Year, Title)_ • [Link](URL)

Content here...
```

**Examples:**
- `_Based on Boehm (1988, Spiral Model)_ • [IEEE](URL)`
- `_Based on Miranda (2014, Release Planning lecture)_`

### 2. Image/Figure Sources

**Rule:** Always include source attribution directly under images.

**Format:**
```markdown
![Description](image.png)

_Source:_ Author, Title • [Link](URL)
```

**Example:**
```markdown
![CHAOS 2015 Data](image.png)

_Source:_ Standish Group (2015, CHAOS Report) • [standishgroup.com](URL)
```

### 3. End-of-Page Citation Structure

**For lecture-adapted content:**

```markdown
---

## Acknowledgments

This content is heavily inspired by and adapted from lectures by **Eduardo Miranda** and **David Root** on software project management.

---

## References

1. [Academic papers with DOI - if any]

---

## Sources

- [Books, handbooks, websites]
- Miranda, Eduardo. *Managing Software Development*. Lecture materials, 2014.

---

{: .highlight }
**Disclaimer:** ...
```

**Rules:**
- Lecture citations ALWAYS in Sources section
- Academic papers in References section
- References section to be generated from inline citations (future automation via Zotero)
- Images/figures keep inline source attribution

### 4. Zotero Workflow

**Master list:** `docs/zotero-import-list.md` (125 unique citations grouped by topic)

**Process:**
1. Update Zotero library with all citations from master list
2. Tag citations by topic in Zotero
3. Generate References sections from Zotero (future automation)
4. Keep Sources section manual (lecture materials, handbooks)

---

## Notes

- Keep "Adapted from" headers - they signal heavy inspiration
- Acknowledgments section provides context and transparency
- This improves academic rigor and transparency
- Supports fair use by proper attribution
- Inline sources preserved for context-specific attributions
- Image sources always inline for immediate visibility
