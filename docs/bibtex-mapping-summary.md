# BibTeX Mapping Summary

**Generated:** 2025-12-14

## Overview

Complete mapping between unique citations and existing BibTeX entries has been created using cleaned data.

## Key Statistics

### Coverage
- **Total unique citations:** 101
- **Total BibTeX entries:** 173
- **High confidence matches:** 32 (31.7%)
- **Potential matches (need verification):** 56 (55.4%)
- **No match found:** 13 (12.9%)
- **Overall coverage:** 31.7%

### Gap Analysis
- **Citations with BibTeX entries:** 32 confirmed
- **Citations needing verification:** 56
- **Citations needing new entries:** 13
- **Unused BibTeX entries:** 69 (entries in .bib not matched to citations)

## Match Quality Levels

### ✅ High Confidence (32 citations)
**Criteria:** Match score ≥ 6/10
- Strong author + year + title match, or
- Strong title + URL match
- Can be used immediately in content
- Examples:
  - Canva Whiteboards → `canva_canva_nodate`
  - Boehm (2003) → `boehm_balancing_2003`
  - Brown (2024) → `brown_risky_2024`

### ⚠️ Potential Matches (56 citations)
**Criteria:** Match score 3-5/10
- Partial match on author/year/title/URL
- **Action required:** Manual verification needed
- May need adjustment or new entry
- Examples:
  - altexsoft.com → `altexsoft_extreme_nodate` (URL match only)
  - 6sigma.us → `sixsigmaus_7_2024` (URL match only)

### ❌ No Match (13 citations)
**Criteria:** Match score < 3/10
- **Action required:** Create new BibTeX entry
- Priority candidates for adding to references.bib

## Files Created

### 1. `bibtex-unique-mapping.md`
**Purpose:** Detailed one-to-one mapping
**Content:**
- All 101 unique citations
- Match status for each (✅/⚠️/❌)
- Suggested BibTeX keys
- Match scores and reasons
- Side-by-side comparison of citation vs BibTeX info

**Use for:**
- Finding which BibTeX key to use for a citation
- Verifying potential matches
- Understanding why matches were made

### 2. `citations-needing-bibtex.md`
**Purpose:** Action list for missing entries
**Content:**
- 69 citations needing BibTeX entries (13 no match + 56 potential)
- Structured TODO format with citation metadata
- URLs included where available
- Ready for systematic entry creation

**Use for:**
- Creating new BibTeX entries
- Verifying potential matches
- Prioritizing which citations to add/verify next
- Tracking completion of BibTeX entry creation

### 3. `bibtex-keys-list.md`
**Purpose:** Reference list of all BibTeX entries
**Content:**
- All 173 BibTeX entries with full details
- Includes URLs and DOIs where available
- Sortable and searchable

**Use for:**
- Finding existing BibTeX entries
- Checking if an entry already exists
- Getting full citation details

## Recommended Workflow

### Phase 1: Use Existing Matches (Immediate)
1. Review high-confidence matches in `bibtex-unique-mapping.md`
2. Start using the 32 confirmed BibTeX keys in content
3. Replace inline citations with `[@key]` format

### Phase 2: Verify Potential Matches (Priority)
1. Review 56 potential matches manually
2. Focus on entries with URL matches (easiest to verify)
3. Confirm or reject each match
4. For confirmed matches:
   - Add to "high confidence" list
   - Start using in content
5. For rejected matches:
   - Add to "needs entry" list
   - Create new BibTeX entry

### Phase 3: Create Missing Entries (As Needed)
1. Use `citations-needing-bibtex.md` as checklist
2. Prioritize by:
   - Citations with URLs (easier to create entries)
   - Citations used in multiple sections
   - Academic papers and books (higher priority than URLs)
   - Foundational works (seminal papers, standards)
3. Create entries manually or via Zotero
4. Add to `references.bib`
5. Re-run mapping to verify

### Phase 4: Update Content (Final)
1. Replace all inline citations with BibTeX keys
2. Verify all references resolve correctly
3. Generate final bibliography

## Match Score Interpretation

Scores are based on multiple factors:

| Factor | Points | Notes |
|--------|--------|-------|
| Author in key | +3 | First author last name appears in BibTeX key |
| Author match | +2 | Author names overlap significantly |
| Year exact match | +3 | Years match exactly |
| Year in key | +2 | Year appears in BibTeX key |
| Strong title match | +4 | >50% word overlap in titles |
| Partial title match | +2 | 30-50% word overlap |
| URL match | +5 | URLs match |
| DOI match | +5 | DOIs match (definitive) |

**Total possible:** 10+ (can exceed 10 with multiple factors)

## Common Issues and Solutions

### Issue 1: URL-only citations
**Example:** "[6sigma.us](https://...)"
**Solution:**
- Check if URL matches existing entry
- If not, create `@misc` entry with URL
- Extract title from webpage if needed

### Issue 2: Partial matches needing verification
**Example:** altexsoft.com → `altexsoft_extreme_nodate`
**Solution:**
- Visit URL to confirm it matches the BibTeX entry
- Check title and content match
- Verify or create new entry

### Issue 3: Multiple potential matches
**Example:** Generic titles like "Software Development"
**Solution:**
- Use URL to disambiguate
- Check author and year
- Verify full citation details

## Quality Metrics

Track progress with these metrics:

- **Coverage rate:** Currently 31.7%, target 95%+
- **Match confidence:** Currently 32/101 high confidence, target 95+/101
- **Pending verification:** Currently 56, target <5
- **Missing entries:** Currently 13, target <3

## Tips for Efficiency

1. **Start with URL matches:** Easiest to verify by visiting the URL
2. **Batch similar citations:** Process all URLs together, all books together, etc.
3. **Use Zotero browser extension:** Auto-capture citation metadata from URLs
4. **Verify before committing:** Check URL/DOI when available
5. **Maintain consistent naming:** Follow existing key patterns (author_title_year)
6. **Re-run mapping after changes:** Track progress and verify matches

## Next Steps

### Immediate Actions
1. ✅ Review high-confidence matches (32 citations)
2. ⚠️ Verify potential matches with URLs (highest priority)
3. Start using confirmed keys in content

### Short-term Actions (This Week)
1. Verify top 20 potential matches (those with URLs)
2. Create BibTeX entries for 13 missing citations
3. Re-run mapping to update coverage

### Long-term Actions (Ongoing)
1. Systematically verify all 56 potential matches
2. Create any additional missing entries
3. Maintain synchronization as citations are added/updated
4. Update content to use BibTeX keys

---

**Last Updated:** 2025-12-14
**Next Review:** After completing Phase 2 verification
