"""Give every markdown figure in content/ exactly one blank line before and after its caption.

The L3a and L3b/L3c import scripts both inserted a figure at the end of a paragraph without
guaranteeing the blank line that follows it. In kramdown consecutive lines are one paragraph, so
the caption and the next paragraph merged, and in three places a `##` heading stopped being a
heading at all. Neither shows up in check_pages.py, check_citations.py or a clean jekyll build --
only in the rendered page.

The shape this enforces, which is what `exp/quadrant.md` already used for `quad.png`:

    <blank>
    ![alt](file.svg)
    _Caption._ {% cite key %}
    <blank>
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "content"
IMG = re.compile(r'^!\[[^\]]*\]\([^)]+\)\s*$')
CAPTION = re.compile(r'^\s*[_*].+')


def fix(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").split("\n")
    out: list[str] = []
    changed = 0
    i = 0
    while i < len(lines):
        line = lines[i]
        if not IMG.match(line):
            out.append(line)
            i += 1
            continue

        # exactly one blank line before
        before = len(out)
        while out and out[-1].strip() == "":
            out.pop()
        if out:                                     # not at the very top of the file
            out.append("")
        if len(out) != before:
            changed += 1

        out.append(line)
        i += 1
        # the caption, if there is one, stays glued to the image
        if i < len(lines) and CAPTION.match(lines[i]) and not IMG.match(lines[i]):
            out.append(lines[i])
            i += 1

        # exactly one blank line after
        n = 0
        while i < len(lines) and lines[i].strip() == "":
            i += 1
            n += 1
        if i < len(lines):
            out.append("")
            if n != 1:
                changed += 1

    text = "\n".join(out)
    if text != path.read_text(encoding="utf-8"):
        path.write_text(text, encoding="utf-8")
        return max(changed, 1)
    return 0


def main() -> int:
    total = 0
    for p in sorted(ROOT.rglob("*.md")):
        n = fix(p)
        if n:
            print(f"  {p.relative_to(ROOT)}")
            total += 1
    print(f"{total} file(s) normalised")
    return 0


if __name__ == "__main__":
    sys.exit(main())
