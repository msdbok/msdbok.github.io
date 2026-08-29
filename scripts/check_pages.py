#!/usr/bin/env python3
"""
Check content pages against templates/page-standard.md.

Why this exists: the site drifted to both extremes. Some areas are ~80% bullets with
nothing explained; reviewed areas grew into essays. Seven pages hold 38% of all site
words, and most pages carry no worked example at all - which is the defect that
actually stops a student understanding the material.

This reports, it does not fix. Treat it like check_citations.py: run it before
committing a page, and use --summary to see where the site stands.

Budgets (body words, excluding front matter, References, Acknowledgments, Disclaimer):
    hub           100-250    index pages: orientation and links only
    topic-hub     250-500    framing + comparison table + links to detail pages
    method        400-800    the default
    deep-dive       <=1200   evidence-carrying, must be marked
    study-notes   800-2200   one lecture summarised for revision (SN)
    question-set  200-2200   revision questions (RQ); the prose rules do not apply
    case          300-1600   a case description or assignment brief
    any             >1500    must be split (>3000 for the three Materials types)

Page type is inferred: `index.md` is a hub (topic-hub if it holds a table and links),
and everything else is a method page. Override per page with `page_type:` in the front
matter - study-notes, question-set and case must always be declared, since nothing in a
page's shape reliably distinguishes them.

Usage:
    python scripts/check_pages.py                 # problems, page by page
    python scripts/check_pages.py --summary       # distribution and per-area stats
    python scripts/check_pages.py --quiet         # problems only, no OK lines
    python scripts/check_pages.py content/proc    # limit to a subtree

Exit codes: 0 clean - 1 at least one page outside the standard
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / 'content'

BUDGETS = {             # type: (min, max, hard_split)
    'hub':          (100, 250, 1500),
    'topic-hub':    (250, 500, 1500),
    'method':       (400, 800, 1500),
    'deep-dive':    (400, 1200, 1500),
    # Materials pages are not method pages, and judging them as one made all six
    # report as broken - which is the same as having no check at all.
    'study-notes':  (800, 2200, 3000),   # SN: one lecture, summarised for revision
    'question-set': (200, 2200, 3000),   # RQ: questions, so the prose rules do not apply
    'case':         (300, 1600, 2500),   # a case description or assignment brief
}

# Types whose content is deliberately not explanatory prose. The bullet-ratio,
# worked-example and lead-sentence rules exist to stop a *teaching* page turning
# into a list of labels; a question set is a list by definition.
NON_PROSE = {'question-set', 'case'}

BULLET_RE = re.compile(r'^\s*([-*+]|\d+\.)\s')
FM_RE = re.compile(r'^---\s*$(.*?)^---\s*$', re.S | re.M)


def split_page(text: str) -> tuple[dict, str]:
    """Return (front matter dict, body with footer material removed)."""
    fm: dict[str, str] = {}
    m = FM_RE.match(text)
    body = text
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, _, v = line.partition(':')
                # Strip a trailing YAML comment, as YAML does for unquoted scalars.
                # Without this, `page_type: deep-dive  # why` parses as the whole
                # string and silently fails to match a known type - so a declared
                # exemption looked like no declaration at all.
                v = re.sub(r'\s+#.*$', '', v)
                fm[k.strip()] = v.strip()
        body = text[m.end():]
    # Drop the footer: acknowledgments, references, disclaimer.
    #
    # The disclaimer must be matched by its OWN text, not by the `{: .highlight }`
    # marker that usually precedes it. An earlier version split on the first
    # `.highlight` anywhere in the file, so any page using that callout mid-body
    # had everything after it silently dropped from the word count - culture.md
    # was reported as 621 words when it was really ~2,570. Measurement bugs that
    # under-report are worse than none at all: they make a page look compliant.
    body = re.split(r'^#{2,4}\s*Acknowledg', body, flags=re.M)[0]
    body = re.split(r'^#{2,4}\s*(References|Further Reading)', body, flags=re.M)[0]
    body = re.sub(r'(\{:\s*\.highlight\s*\}\s*)?\n\s*\*\*Disclaimer:.*\Z', '',
                  body, flags=re.S)
    return fm, body


def classify(path: Path, fm: dict, body: str) -> str:
    # `deep-dive` must be DECLARED in front matter (`page_type: deep-dive`).
    # It used to be inferred from the presence of a `## How solid is this?`
    # section, which was exactly backwards: adding the evidence section - the
    # thing meant to make pages leaner - silently bought a 50% bigger budget.
    # Claiming the larger allowance should be a visible, reviewable decision.
    if fm.get('page_type') in BUDGETS:
        return fm['page_type']
    if path.name == 'index.md':
        has_table = bool(re.search(r'^\|', body, re.M))
        has_links = len(re.findall(r'\]\([^)]+\)', body)) >= 3
        return 'topic-hub' if (has_table and has_links) else 'hub'
    return 'method'


def analyse(path: Path) -> dict:
    text = path.read_text(encoding='utf-8', errors='replace')
    fm, body = split_page(text)

    lines = body.splitlines()
    bullets = [l for l in lines if BULLET_RE.match(l)]
    words = len(re.findall(r'\w+', body))
    bullet_words = len(re.findall(r'\w+', '\n'.join(bullets)))

    # first 40 words after the H1, ignoring blockquotes/italic attributions
    after_h1 = re.split(r'^#\s+.*$', body, maxsplit=1, flags=re.M)
    lead = after_h1[1] if len(after_h1) > 1 else body
    lead = re.sub(r'^\s*[_*].*?[_*]\s*$', '', lead, flags=re.M)   # attribution lines
    lead = re.sub(r'^\s*[#>|].*$', '', lead, flags=re.M)
    lead_words = re.findall(r'\w+', lead)[:40]

    # an example is a marked Example, or a "for example"/"e.g." with a concrete noun
    examples = len(re.findall(r'\*Example|^\s*\*\*Example|:\s*\*Example', body, re.M))
    examples += len(re.findall(r'\bFor example,|\be\.g\.,', body))

    return dict(
        path=path.relative_to(ROOT).as_posix(),
        area=path.relative_to(CONTENT).parts[0],
        type=classify(path, fm, body),
        words=words,
        bullet_pct=round(100 * bullet_words / words) if words else 0,
        n_bullets=len(bullets),
        lead=' '.join(lead_words),
        examples=examples,
        callouts=len(re.findall(r'\{:\s*\.(note|warning)\s*\}', body)),
        h1=len(re.findall(r'^#\s+', body, re.M)),
        h4=len(re.findall(r'^#{4,}\s+', body, re.M)),
        cites=len(re.findall(r'\{%\s*cite', text)),
        has_bib='{% bibliography' in text,
        hand_refs=bool(re.search(r'^#{2,4}\s*References', text, re.M))
                  and '{% bibliography' not in text,
        has_disclaimer='Disclaimer' in text,
        fragment_pct=fragment_ratio(bullets),
    )


def fragment_ratio(bullets: list[str]) -> int:
    """
    Percentage of bullets that are bare labels rather than statements.

    This is the "rough ideas" defect: `- Autonomy` teaches nothing, while
    `- Autonomy predicts psychological safety more reliably than role clarity`
    is information. A fragment is a short bullet with no verb-like content once
    the marker, bold label and trailing colon are stripped.

    An earlier version flagged any list that followed a heading directly. That
    fired on 68 of 74 pages and was simply wrong - a descriptive heading is a
    perfectly good lead-in. Measure the bullets, not their position.
    """
    if not bullets:
        return 0
    frags = 0
    for b in bullets:
        text = BULLET_RE.sub('', b).strip()
        text = re.sub(r'^\*\*[^*]+\*\*:?\s*', '', text)   # drop a bold label
        words = re.findall(r"[\w'-]+", text)
        if len(words) < 6:
            frags += 1
    return round(100 * frags / len(bullets))


def problems(r: dict) -> list[str]:
    out = []
    lo, hi, split = BUDGETS[r['type']]

    if r['words'] > split:
        out.append(f"{r['words']} words - SPLIT into a summary page + one page per method")
    elif r['words'] > hi:
        out.append(f"{r['words']} words - over the {r['type']} budget ({lo}-{hi})")
    elif r['words'] < lo:
        out.append(f"{r['words']} words - under the {r['type']} budget ({lo}-{hi}); "
                   f"likely missing example or explanation")

    if r['type'] in ('method', 'deep-dive', 'study-notes'):
        if r['examples'] == 0:
            out.append('no concrete example')
        if r['bullet_pct'] > 60:
            out.append(f"{r['bullet_pct']}% bullets - explain, do not list")
        if not r['lead']:
            out.append('no lead sentence after the H1')

    if r['type'] not in NON_PROSE and r['n_bullets'] >= 5 and r['fragment_pct'] > 60:
        out.append(f"{r['fragment_pct']}% of bullets are bare labels - make them statements")
    if r['callouts'] > 2:
        out.append(f"{r['callouts']} callouts - at most 2")
    if r['h4']:
        out.append(f"{r['h4']} H4+ heading(s) - split instead")
    if r['h1'] != 1:
        out.append(f"{r['h1']} H1 headings - expected exactly 1")
    if r['hand_refs']:
        out.append('hand-numbered References - use {% bibliography --cited %}')
    if r['cites'] and not r['has_bib']:
        out.append('cites sources but has no bibliography block')
    if not r['has_disclaimer']:
        out.append('missing Disclaimer footer')
    return out


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    quiet = '--quiet' in sys.argv
    summary = '--summary' in sys.argv

    roots = [ROOT / a for a in args] or [CONTENT]
    # Accept a single file as well as a directory - `rglob` on a file yields
    # nothing, so passing one used to check zero pages and report success.
    pages = sorted({p for r in roots
                    for p in ([r] if r.is_file() else r.rglob('*.md'))})
    if not pages:
        sys.exit('no pages found')

    rows = [analyse(p) for p in pages]

    if summary:
        import statistics as st
        print(f'{len(rows)} pages - {sum(r["words"] for r in rows):,} body words\n')
        print(f'{"type":<11}{"pages":>6}{"median":>8}{"bullet%":>9}{"no example":>12}')
        for t in BUDGETS:
            g = [r for r in rows if r['type'] == t]
            if not g:
                continue
            print(f'{t:<11}{len(g):>6}'
                  f'{st.median([r["words"] for r in g]):>8.0f}'
                  f'{st.median([r["bullet_pct"] for r in g]):>9.0f}'
                  f'{sum(1 for r in g if r["examples"] == 0):>12}')
        print(f'\n{"area":<11}{"pages":>6}{"median":>8}{"bullet%":>9}{"no example":>12}{"cited":>7}')
        for a in sorted({r['area'] for r in rows}):
            g = [r for r in rows if r['area'] == a]
            print(f'{a:<11}{len(g):>6}'
                  f'{st.median([r["words"] for r in g]):>8.0f}'
                  f'{st.median([r["bullet_pct"] for r in g]):>9.0f}'
                  f'{sum(1 for r in g if r["examples"] == 0):>12}'
                  f'{sum(1 for r in g if r["cites"]):>7}')
        print()

    flagged = 0
    for r in sorted(rows, key=lambda r: -r['words']):
        probs = problems(r)
        if probs:
            flagged += 1
            print(f'{r["path"]}  [{r["type"]}, {r["words"]}w]')
            for p in probs:
                print(f'    - {p}')
        elif not quiet and not summary:
            print(f'{r["path"]}  [{r["type"]}, {r["words"]}w]  ok')

    print(f'\n{flagged} of {len(rows)} pages outside the standard.')
    return 1 if flagged else 0


if __name__ == '__main__':
    sys.exit(main())
