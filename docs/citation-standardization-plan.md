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
- content/plan/activities.md
- content/plan/milestones.md
- content/material/trscp.md
- content/material/trsd.md
- content/material/trswbs.md

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

### B. Header Standardization

**Change all instances of:**
- `## References` → `## Sources`
- `## Source` (singular) → `## Sources`
- `## Sources & References` → `## Sources`

**Files to update:**
- content/proc/frameworks/overview.md
- content/proc/frameworks/details.md
- content/track/burndown.md
- content/scope/wbs/*.md (check all)
- Others identified in analysis (5+ pages)

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

### D. Eduardo Miranda Full Citation

**Add to all pages with "Adapted from Eduardo Miranda":**

```markdown
## Sources

- Miranda, Eduardo. *Managing Software Development Projects*. Lecture materials, Carnegie Mellon University, 2014.
```

**Note:** Verify exact title and affiliation

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

## Success Metrics

- [ ] All pages have `## Sources` (not References/Source)
- [ ] 0 pages with missing citations on methodology content
- [ ] Eduardo Miranda cited in all 6 "Adapted from" pages
- [ ] Hoover citations standardized (1 canonical format)
- [ ] All high-priority missing citations added
- [ ] Templates updated with citation standards

---

## Notes

- Keep "Adapted from" headers - they signal heavy inspiration
- Acknowledgments section provides context and transparency
- This improves academic rigor and transparency
- Supports fair use by proper attribution
