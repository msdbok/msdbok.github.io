"""Import the L3b and L3c lecture figures into the Needs pages.

Same convention as `import_l3a_figures.py`: the SVG is copied beside the page that uses it and
referenced relatively, with a one-line italic caption and a `{% cite %}` naming the source. Every
key used here is already cited on its target page, except Nuseibeh on `reqs/more.md`, which the V&V
figure brings with it.

Placement is after the *first paragraph* of the named section, not immediately under the heading,
so the reader meets the claim and then the picture. The script prints where each landed.
"""
import re
import shutil
import sys
from pathlib import Path

L3B = Path(r"C:\_code\_EDU\msd_review\lectures\MSD\L3b_Needs_Requirements\media")
L3C = Path(r"C:\_code\_EDU\msd_review\lectures\MSD\L3c_Needs_Risks\media")
CONTENT = Path(__file__).resolve().parent.parent / "content" / "needs"

# (source dir, svg, page, section heading it goes into, alt text, caption)
PLAN = [
    # ---- L3b -> needs/reqs ------------------------------------------------------------------
    (L3B, "re-cycle.svg", "reqs/eng.md", "## 2.",
     "Elicit, model and analyse, communicate, agree, evolve, drawn as a cycle",
     "_The five activities are a cycle, not a pipeline._ {% cite nuseibeh2000roadmap %}"),

    (L3B, "elicitation-problems.svg", "reqs/elicitation.md", "## 1.",
     "Ten elicitation problems sorted into scope, understanding and volatility",
     "_Seven of the ten are problems of understanding._ {% cite christel1992elicitation %}"),
    (L3B, "elicitation-evidence.svg", "reqs/elicitation.md", "## 3.",
     "What the evidence tested against what practitioners actually use",
     "_What has been tested, against what is used._ {% cite dieste2011elicitation %}"),
    (L3B, "napire.svg", "reqs/elicitation.md", "## 4.",
     "Requirements problems: how often cited, and how often blamed for failure",
     "_Frequency is not damage._ {% cite mendez2017napire %}"),

    (L3B, "qa-scenario.svg", "reqs/stmts.md", "## 3.",
     "A quality-attribute scenario in four slots, with the five-second example",
     "_The fourth slot, the response measure, is the one teams skip._"
     " {% cite barbacci2003qaw %}"),

    (L3B, "vmodel-vv.svg", "reqs/more.md", "## 1.",
     "A V, with validation on the way down and verification on the way up",
     "_Validation asks the stakeholders; verification asks the build._"
     " {% cite nuseibeh2000roadmap %}"),
    (L3B, "maintenance-split.svg", "reqs/more.md", "## 3.",
     "Maintenance effort: fixing defects against adding what users now want",
     "_Most maintenance is enhancement, not repair._ {% cite kelly2004change %}"),
    (L3B, "change-threshold.svg", "reqs/more.md", "## 4.",
     "The cost of change rises, and with it the bar a change must clear",
     "_The door does not close; the price goes up._ {% cite kelly2004change %}"),

    (L3B, "layer-cake.svg", "reqs/doc.md", "## 2.",
     "A story as a vertical slice through the layers, not one layer",
     "_A story is a vertical slice, not a layer._ {% cite wake_invest_2003 %}"),

    (L3B, "ready-done.svg", "reqs/methods.md", "## 4.",
     "Definition of Ready and Definition of Done, either side of a sprint",
     "_The completeness check moved; it did not go away._ {% cite swebok2024v4 %}"),

    (L3B, "re-tools-timeline.svg", "reqs/ai.md", "## 1.",
     "Published studies on automating requirements work, by era",
     "_The fourth generation of requirements automation._ {% cite cheng2026genaire %}"),

    # ---- L3c -> needs/risks -----------------------------------------------------------------
    (L3C, "risk-or-issue.svg", "risks/index.md", "## 1.",
     "Where a cause becomes a risk and a risk becomes an issue",
     "_No uncertainty left means it is an issue, not a risk._ {% cite hillson2009risk %}"),
    (L3C, "five-levels.svg", "risks/index.md", "## 2.",
     "Five levels of risk-handling maturity, from crisis management to elimination",
     "_Risk is not bad. Unmanaged risk is._ {% cite vanscoy1992risk %}"),
    (L3C, "crm-wheel.svg", "risks/index.md", "## 3.",
     "Five steps round a wheel, with communication through the hub",
     "_Communicate is the hub, not a sixth step._ {% cite dorofee1996crm %}"),

    (L3C, "known-unknown.svg", "risks/identification.md", "## 1.",
     "Known and unknown risks, against who in the organisation knows them",
     "_Most risks are already known, to someone who is not you._"
     " {% cite carr1993taxonomy %}"),
    (L3C, "risk-digraph.svg", "risks/identification.md", "## 4.",
     "Sixty risks reduced to a few clustered areas",
     "_Mitigate areas, not rows._ {% cite williams1999sre %}"),

    (L3C, "decision-tree.svg", "risks/analysis.md", "## 1.",
     "A decision tree comparing the cost of prototyping against the exposure it removes",
     "_Paying $500,000 was the cheaper option._ {% cite boehm1991risk %}"),
    (L3C, "pareto.svg", "risks/analysis.md", "## 3.",
     "A Pareto curve separating the vital few from the useful many",
     "_The vital few, and the useful many._ {% cite mcconnell_rapid_1996 %}"),
    (L3C, "matrix-vs-el.svg", "risks/analysis.md", "## 4.",
     "A five by five risk matrix against expected loss, showing where they disagree",
     "_Two risks in the same cell can differ by orders of magnitude._"
     " {% cite cox2008matrices %}"),

    (L3C, "overrun-histogram.svg", "risks/biases.md", "## 2.",
     "The distribution of IT project cost overruns, with its long right tail",
     "_Half are on budget. The average is 80% over._ {% cite flyvbjerg2022overruns %}"),

    (L3C, "comair-timeline.svg", "risks/capturing.md", "## 3.",
     "The Comair crew-scheduling failure, hour by hour",
     "_A storm did not stop the airline. A hard-coded limit did._"
     " {% cite dotoig2005comair %}"),
    (L3C, "emv-trend.svg", "risks/capturing.md", "## 4.",
     "Expected monetary value across one project, March 2011 to February 2012",
     "_A risk list growing early is good news._ {% cite shrivastava2012pmi %}"),
    (L3C, "burndown.svg", "risks/capturing.md", "## 4.",
     "A risk burndown, showing exposure falling as mitigations land",
     "_Meetings do not burn down risks; mitigations do._ {% cite dod2023rio %}"),
]

PARA_STOP = re.compile(r'^\s*(#|\||[-*>]\s|\{:|!\[|<img|\d+\.\s)')


def insert_after_first_paragraph(body: str, heading: str, block: str) -> str | None:
    """Put `block` after the first ordinary paragraph under `heading`."""
    i = body.find("\n" + heading)
    if i == -1:
        return None
    lines = body[i + 1:].split("\n")
    j = 1                                   # skip the heading line itself
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j >= len(lines) or PARA_STOP.match(lines[j]):
        j -= 1                              # section opens with a list/table/figure
    else:
        while j < len(lines) and lines[j].strip():
            j += 1
        j -= 1
    at = i + 1 + sum(len(l) + 1 for l in lines[:j + 1])
    return body[:at] + "\n\n" + block + body[at:]


def main() -> int:
    ok = True
    for src_dir, svg, page, heading, alt, caption in PLAN:
        src = src_dir / svg
        p = CONTENT / page
        if not src.exists():
            print(f"MISSING SOURCE {src}")
            ok = False
            continue
        s = p.read_text(encoding="utf-8")
        if svg in s:
            print(f"{svg:26s} -> {page:26s} already present, skipped")
            continue
        block = f"![{alt}]({svg})\n{caption}"
        out = insert_after_first_paragraph(s, heading, block)
        if out is None:
            print(f"HEADING {heading!r} NOT FOUND in {page}")
            ok = False
            continue
        shutil.copyfile(src, CONTENT / Path(page).parent / svg)
        p.write_text(out, encoding="utf-8")
        print(f"{svg:26s} -> {page:26s} {heading}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
