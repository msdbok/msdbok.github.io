#!/usr/bin/env python3
"""
Check every {% cite %} key in content/ against _bibliography/references.bib.

Why this exists: jekyll-scholar fails *quietly* on an unknown key - the citation
renders as a broken marker and `{% bibliography --cited %}` simply omits it, so a
page can look finished while citing nothing. A local `bundle exec jekyll build`
would catch it, but the Ruby toolchain is not always available (native gem
extensions need a devkit). This check needs only Python and catches the failure
that actually matters.

It also reports:
  * bibliography entries that nothing cites (dead weight, or a page that forgot)
  * duplicate keys in the .bib (jekyll-scholar silently takes one)
  * pages with citations but no `{% bibliography --cited %}` footer, and vice versa

Usage:
    python scripts/check_citations.py            # from the repo root
    python scripts/check_citations.py --quiet    # only problems

Exit codes: 0 clean - 1 at least one unresolved key or footer mismatch
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / '_bibliography' / 'references.bib'
CONTENT = ROOT / 'content'

CITE = re.compile(r'\{\%\s*cite\s+([^\%]+?)\s*\%\}')
BIBTAG = re.compile(r'\{\%\s*bibliography\b')
KEYDEF = re.compile(r'^@\w+\s*\{\s*([^,]+),', re.M)


def main() -> int:
    quiet = '--quiet' in sys.argv

    if not BIB.is_file():
        sys.exit(f'no bibliography at {BIB}')

    bibtext = BIB.read_text(encoding='utf-8', errors='replace')
    defined = [k.strip() for k in KEYDEF.findall(bibtext)]
    dupes = sorted({k for k in defined if defined.count(k) > 1})
    known = set(defined)

    used: dict[str, list[str]] = {}
    no_footer: list[str] = []
    footer_no_cites: list[str] = []
    pages = 0

    for md in sorted(CONTENT.rglob('*.md')):
        text = md.read_text(encoding='utf-8', errors='replace')
        rel = md.relative_to(ROOT).as_posix()
        pages += 1

        keys: list[str] = []
        for group in CITE.findall(text):
            # `{% cite a b %}` and `{% cite a,b %}` are both legal
            keys += [k for k in re.split(r'[\s,]+', group.strip()) if k]

        for k in keys:
            used.setdefault(k, []).append(rel)

        has_footer = bool(BIBTAG.search(text))
        if keys and not has_footer:
            no_footer.append(rel)
        if has_footer and not keys:
            footer_no_cites.append(rel)

    unresolved = {k: v for k, v in used.items() if k not in known}
    uncited = sorted(known - set(used))

    if not quiet:
        print(f'{pages} pages - {len(used)} distinct keys cited - '
              f'{len(known)} entries in references.bib')

    problems = 0

    if unresolved:
        problems += len(unresolved)
        print(f'\nUNRESOLVED KEYS ({len(unresolved)}) - these render broken:')
        for k in sorted(unresolved):
            print(f'  {k}')
            for p in sorted(set(unresolved[k])):
                print(f'      {p}')

    if dupes:
        problems += len(dupes)
        print(f'\nDUPLICATE KEYS IN .bib ({len(dupes)}) - one is silently ignored:')
        for k in dupes:
            print(f'  {k}')

    if no_footer:
        problems += len(no_footer)
        print(f'\nCITES BUT NO BIBLIOGRAPHY FOOTER ({len(no_footer)}) - '
              f'references will not render:')
        for p in no_footer:
            print(f'  {p}')

    if footer_no_cites and not quiet:
        print(f'\nFooter but no citations ({len(footer_no_cites)}) - '
              f'renders an empty reference list:')
        for p in footer_no_cites:
            print(f'  {p}')

    if not quiet:
        print(f'\nUncited bibliography entries: {len(uncited)}')

    if problems == 0:
        print('\nOK - every cited key resolves.')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
