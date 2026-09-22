"""One-off: import the L3a lecture figures into the Needs pages.

Each figure is copied beside the page that uses it and referenced relatively, which is the
convention `content/needs/exp/quadrant.md` already follows for `quad.png`. The caption carries the
source, because several of these are rebuilds of a paper's own figure rather than our inventions.

Where a page already carried a screenshot of the same figure, the rebuild **replaces** it:
`expectation-space.svg` takes over from `quad.png`, which is deleted. The rebuilds are vector, so
they stay sharp at any zoom and their labels are real text.

`quad_time.png` stays as it is -- we have no rebuild of the problem/solution/decision-space grid.
"""
import shutil
import sys
from pathlib import Path

SRC = Path(r"C:\_code\_EDU\msd_review\lectures\MSD\L3a_Needs_Expectations\media")
CONTENT = Path(__file__).resolve().parent.parent / "content" / "needs"

# (svg, page, anchor paragraph it goes after, markdown to insert)
PLAN = [
    ("zone-of-tolerance.svg", "exp/index.md",
     "no complaint at all — which is where a well-run project spends most of its time.",
     "![Desired, adequate and predicted service, with the zone of tolerance between the top two]"
     "(zone-of-tolerance.svg)\n"
     "_The three levels a customer holds at once, and the band between the top two._"
     " {% cite zeithaml1993expectations %}"),

    ("three-seconds.svg", "exp/index.md",
     'only a penalty for missing it, which is the principled version of "do not gold-plate the '
     'plumbing".',
     "![The same three seconds delivered against a four-second promise and a one-second promise]"
     "(three-seconds.svg)\n"
     "_Identical performance, opposite verdicts: the denominator is what was promised._"
     " {% cite boehm_requirements_1999 %}"),

    ("kano.svg", "exp/kano.md",
     "The software readings are ours; the source's examples are all skis.",
     "![Three classes of requirement plotted against how fully they are met, with the migration "
     "over time](kano.svg)\n"
     "_The three classes, the properties that identify each one, and the decay over time. Headings "
     "use the common industry names; Sauerwein's terms run along the bottom. **The migration arrows "
     "are not in the 1996 paper** -- they are Kano's later claim and the standard teaching of the "
     "model._ {% cite sauerwein1996kano %}"),

    ("chaos-definitions.svg", "exp/success.md",
     "When someone quotes you a failure rate, the first question is which definition produced it.",
     "![Traditional and modern resolution of the same FY2015 database](chaos-definitions.svg)\n"
     "_The same projects, scored two ways._ {% cite standish2015chaos %}"),

    ("mckinsey.svg", "exp/success.md",
     "is the figure this subject should carry, and it is the one a CHAOS-only slide does not give "
     "you.",
     "![Cost, schedule and value outcomes, all IT against software only](mckinsey.svg)\n"
     "_All large IT against software alone, on the same study._ {% cite bloch2012mckinsey %}"),

    ("threshold.svg", "exp/tos.md",
     "**A is *assignable***, naming who is responsible, not \"achievable\".",
     "![Concerns above and below the threshold line](threshold.svg)\n"
     "_A concern that would breach the threshold is a risk; everything else is an event._"
     " {% cite hoover_evaluating_2010 %}"),

    ("cos-loop.svg", "exp/tos.md",
     "**agreement** restating what they will get — repeated until neither side corrects the other. "
     "The\nstopping rule is the point.",
     "![Request, clarify, respond, clarify \u2014 repeated until it stops moving](cos-loop.svg)\n"
     "_Conditions of Satisfaction. The restatement is the test: a correction means you had it wrong "
     "and did not know._ {% cite wysocki2003needs %}"),

    ("loyalty-split.svg", "exp/cust_types.md",
     "60\u201380% of car buyers say they will repurchase the same\nbrand, and 35\u201340% actually "
     "do.",
     "![48% scored 5, 34% scored 4, 18% scored 3 or below](loyalty-split.svg)\n"
     "_The 82% headline, split. Only the top box predicts anything._ {% cite jones_why_1995 %}"),

    ("involvement-evidence.svg", "exp/involvement.md",
     "does not, and badly run involvement produces unrealistic expectations, communication "
     "breakdown and\nintergroup hostility.",
     "![52 studies positive, 23 uncertain, 12 negative](involvement-evidence.svg)\n"
     "_87 studies over 32 years. The direction is clear; the uniformity is not._"
     " {% cite bano2015involvement %}"),

    ("involvement-continuum.svg", "exp/involvement.md",
     "**On-site Customer \u2192 Story Owner \u2192 Just Demos \u2192 E-collaboration \u2192 "
     "Customer Proxy \u2192 Extreme\nUndercover.**",
     "![Six levels of customer involvement on one continuum, ordered by directness]"
     "(involvement-continuum.svg)\n"
     "_The study's Fig. 5. The levels are **not strictly linear and may occur simultaneously** --"
     " the authors say so explicitly, which is why this is a continuum and not a ladder._"
     " {% cite hoda2011customer %}"),

    ("covariance-chart.svg", "exp/involvement.md",
     "expected unlimited scope\nfreedom while resisting the full-time involvement that pays for it.",
     "![Causes, the condition they produce, the consequences, and the strategies that answer them]"
     "(covariance-chart.svg)\n"
     "_The study's Fig. 4. Read it across: the causes on the left produce the condition in the "
     "middle, the consequences on the right, and the strategies underneath are what you do about "
     "it._ {% cite hoda2011customer %}"),

    ("iceberg.svg", "exp/quadrant.md",
     "impact statement or a prototype, rather than explaining that software is hard.",
     "![The visible application above the waterline and the essential software below](iceberg.svg)\n"
     "_What the customer prices is what they can see. The half they cannot see is most of the "
     "cost._"),

    ("onion.svg", "reqs/stakeholders.md",
     "another hid workplace\nsafety, airworthiness certification and radio regulation inside one "
     "generic *regulator* slot.",
     "![Four rings of stakeholder roles, with the unfilled slots shown](onion.svg)\n"
     "_Slots, filled and empty. An empty slot is a finding._ {% cite alexander2004onion %}"),

    ("stakeholder-concerns.svg", "reqs/stakeholders.md",
     "locating people; it is getting the people you located to engage usefully",
     None),  # placed by hand below, because the anchor paragraph continues with links
]

# (svg, page, the whole image line it replaces, the line that replaces it, png to delete)
REPLACE = [
    ("expectation-space.svg", "exp/quadrant.md",
     "![The expectation space and the solution space](quad.png)\n"
     "_Customer-controlled and developer-controlled elements._"
     " {% cite hoover_evaluating_2010 %}",
     "![Four customer axes and three developer axes, each with a point marked, and f(x) mapping "
     "one to the other](expectation-space.svg)\n"
     "_Customer-controlled and developer-controlled elements. An expectation is a **point**, not a "
     "list, and **f(x)** is the manager's job: hitting it from a space with different axes._"
     " {% cite hoover_evaluating_2010 %}",
     "quad.png"),
]


def main() -> int:
    ok = True
    for svg, page, anchor, insert in PLAN:
        src, dst = SRC / svg, CONTENT / Path(page).parent / svg
        if not src.exists():
            print(f"MISSING SOURCE {src}")
            ok = False
            continue
        shutil.copyfile(src, dst)
        if insert is None:
            print(f"{svg:28s} -> {dst.parent.name}/  (reference inserted by hand)")
            continue
        p = CONTENT / page
        s = p.read_text(encoding="utf-8")
        if anchor not in s:
            print(f"ANCHOR NOT FOUND in {page}: {anchor[:60]!r}")
            ok = False
            continue
        if svg in s:
            print(f"{svg:28s} -> {page}  (already referenced, skipped)")
            continue
        s = s.replace(anchor, anchor + "\n\n" + insert, 1)
        p.write_text(s, encoding="utf-8")
        print(f"{svg:28s} -> {page}")

    for svg, page, old, new, stale in REPLACE:
        src, dst = SRC / svg, CONTENT / Path(page).parent / svg
        if not src.exists():
            print(f"MISSING SOURCE {src}")
            ok = False
            continue
        p = CONTENT / page
        s = p.read_text(encoding="utf-8")
        if svg in s:
            print(f"{svg:28s} -> {page}  (already swapped, skipped)")
            continue
        if old not in s:
            print(f"OLD FIGURE BLOCK NOT FOUND in {page}")
            ok = False
            continue
        shutil.copyfile(src, dst)
        p.write_text(s.replace(old, new, 1), encoding="utf-8")
        gone = CONTENT / Path(page).parent / stale
        if gone.exists():
            gone.unlink()
        print(f"{svg:28s} -> {page}  (replaced {stale}, deleted)")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
