#!/usr/bin/env python3
"""Run the Guide search tests against the Umamusume docs engine.

Reads the question table in tools/docs_optimization/SearchTests.md and, for each question,
asks the real engine (LilyAiGameSpace/UmamusumeGameSpaceEngine.py) in three ways:

    search     engine.search(question)                              top 5 hits, all docs
    scoped     engine.search(question, category=<expected folder>)  top 5 hits, expected top folder only
    context    engine.context_for(question)                         what chat injects into the prompt

Each mode gets one status per question:

    pass   a hit is the expected doc AND its section matches an expected heading
           (or the expected doc, when the test names no heading, for example a table row)
    file   the expected doc is in the results, but not the expected section
    alt    only a file named under "also" in the Notes column is in the results
    fail   none of the above
    none   (context mode only) the message names no known doc, so nothing is injected

The number after @ is the rank of the first matching hit.

The report also measures section sizes (characters of text in each indexed section): the size of
each expected section, the size of the top search hit, the largest sections in the index, and how
many sections are too long for one read (more than 6,000 and more than 12,000 characters). This
tests the Phase 04d idea that very large sections outrank small, focused ones.

Usage:
    python tools/run_search_tests.py
    python tools/run_search_tests.py --markdown out.md --json results.json
    python tools/run_search_tests.py --compare baseline.json     # exit 2 if a pass became a non-pass

Standard library only. The engine and the test table are read, never written.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from LilyAiGameSpace.UmamusumeGameSpaceEngine import UmamusumeGameSpaceEngine  # noqa: E402

TESTS_FILE = REPO_ROOT / "tools" / "docs_optimization" / "SearchTests.md"
MODES = ("search", "scoped", "context")
TOP_N = 5
READ_DEFAULT = 6_000
READ_MAX = 12_000

_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|")
_TICK_RE = re.compile(r"`([^`]+)`")

# (doc id, section path) -> characters of section text. Filled in main().
SIZES: dict[tuple[str, str], int] = {}


def norm(text: str) -> str:
    """Case, punctuation and space insensitive key (same idea as the engine's)."""
    return re.sub(r"[\W_]+", "", text.casefold())


@dataclass
class TestCase:
    num: int
    question: str
    doc_id: str
    alt_ids: list[str] = field(default_factory=list)
    sections: list[str] = field(default_factory=list)   # empty = file-only check

    @property
    def category(self) -> str:
        return self.doc_id.split("/", 1)[0]


def doc_id_for(path: str) -> str:
    """Table path (relative to Guide/, or ../ for the folder above) -> engine doc id."""
    p = path.strip()
    p = p[3:] if p.startswith("../") else "Guide/" + p
    return re.sub(r"\.md$", "", p)


def parse_tests(path: Path) -> list[TestCase]:
    tests: list[TestCase] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not _ROW_RE.match(line):
            continue
        cells = [c.strip() for c in line[1:-1].split("|")]
        if len(cells) < 8:
            continue
        num, question, _generic, file_cell, section_cell, _base, _final, notes = cells[:8]
        files = [t for t in _TICK_RE.findall(file_cell) if t.endswith(".md")]
        if not files:
            continue
        primary = doc_id_for(files[0])
        alts = [doc_id_for(t) for t in _TICK_RE.findall(notes) if t.endswith(".md")]
        alts = [a for a in dict.fromkeys(alts) if a != primary]
        sections = [t.lstrip("#").strip() for t in _TICK_RE.findall(section_cell) if t.lstrip().startswith("#")]
        tests.append(TestCase(int(num), question, primary, alts, sections))
    return tests


def section_sizes(engine: UmamusumeGameSpaceEngine) -> dict[tuple[str, str], int]:
    """Size of every visible section. Reads the engine's index, so it returns {} if that changes."""
    sizes: dict[tuple[str, str], int] = {}
    for doc in getattr(engine, "_docs", {}).values():
        for s in doc.visible():
            sizes[(doc.id, s.path)] = len(s.text)
    return sizes


def expected_size(t: TestCase) -> int | None:
    """Largest section of the expected doc that matches an expected heading (whole doc if none named)."""
    found = [n for (d, p), n in SIZES.items()
             if d == t.doc_id and (not t.sections or any(norm(s) in norm(p) for s in t.sections))]
    return max(found) if found else None


def label(doc: str, sec: str) -> str:
    n = SIZES.get((doc, sec))
    return f"{doc} > {sec}" + (f" [{n:,} chars]" if n is not None else "")


def evaluate(hits: list[tuple[str, str]], t: TestCase) -> dict:
    first_pass = first_file = first_alt = None
    for rank, (doc, sec) in enumerate(hits, 1):
        if doc == t.doc_id:
            first_file = first_file or rank
            if not t.sections or any(norm(s) in norm(sec) for s in t.sections):
                first_pass = first_pass or rank
        elif doc in t.alt_ids:
            first_alt = first_alt or rank
    if first_pass:
        status, rank = "pass", first_pass
    elif first_file:
        status, rank = "file", first_file
    elif first_alt:
        status, rank = "alt", first_alt
    else:
        status, rank = "fail", None
    return {"status": status, "rank": rank, "hits": [label(d, s) for d, s in hits]}


def context_hits(engine: UmamusumeGameSpaceEngine, message: str) -> list[tuple[str, str]]:
    """(doc id, section path) pairs that context_for() would put into the chat prompt."""
    docs = engine.mentioned_docs(message)[:2]
    out: list[tuple[str, str]] = []
    for snippet in engine.context_for(message):
        for d in docs:
            prefix = d.title + " > "
            if snippet.startswith(prefix):
                out.append((d.id, snippet[len(prefix):].split(" (game docs):", 1)[0]))
                break
    return out


def run(engine: UmamusumeGameSpaceEngine, tests: list[TestCase]) -> list[dict]:
    results = []
    for t in tests:
        search_hits = [(h.doc_id, h.section) for h in engine.search(t.question, limit=TOP_N)]
        modes = {
            "search": evaluate(search_hits, t),
            "scoped": evaluate(
                [(h.doc_id, h.section) for h in engine.search(t.question, category=t.category, limit=TOP_N)], t),
        }
        ctx = context_hits(engine, t.question)
        modes["context"] = evaluate(ctx, t) if ctx else {"status": "none", "rank": None, "hits": []}
        results.append({
            "num": t.num, "question": t.question, "doc_id": t.doc_id,
            "sections": t.sections, "alts": t.alt_ids, "modes": modes,
            "expected_chars": expected_size(t),
            "top_hit_chars": SIZES.get(search_hits[0]) if search_hits else None,
        })
    return results


def cell(m: dict) -> str:
    return m["status"] + (f"@{m['rank']}" if m["rank"] else "")


def chars(n: int | None) -> str:
    return f"{n:,}" if n is not None else "?"


def size_report() -> list[str]:
    if not SIZES:
        return ["## Section sizes", "", "(not available: the engine's index could not be read)", ""]
    total = len(SIZES)
    over_read = sum(1 for n in SIZES.values() if n > READ_DEFAULT)
    over_max = sum(1 for n in SIZES.values() if n > READ_MAX)
    text_total = sum(SIZES.values())
    top = sorted(SIZES.items(), key=lambda kv: -kv[1])[:15]
    top_share = sum(n for _, n in top) / text_total * 100 if text_total else 0
    lines = ["## Section sizes", "",
             f"{total:,} sections, {text_total:,} characters of text. "
             f"{over_read:,} sections are longer than a default read ({READ_DEFAULT:,}), "
             f"{over_max:,} are longer than the maximum read ({READ_MAX:,}), so a read cuts them off. "
             f"The 15 largest hold {top_share:.0f}% of all text.", "",
             "| Rank | Section | Characters |", "|---|---|---|"]
    for i, ((d, p), n) in enumerate(top, 1):
        lines.append(f"| {i} | `{d}` > {p} | {n:,} |")
    lines.append("")
    return lines


def render(results: list[dict], regressions: list[str] | None = None) -> str:
    n = len(results)
    lines = ["# Search test results", "",
             f"{n} questions. Status: **pass** = expected doc and section in the top {TOP_N}; "
             "**file** = right doc, wrong section; **alt** = only an alternate doc; **fail**; "
             "**none** = chat context injects nothing. `@n` is the rank of the first match.", ""]
    lines += ["## Summary", "", "| Mode | pass | file | alt | fail | none |", "|---|---|---|---|---|---|"]
    for mode in MODES:
        c = {s: sum(1 for r in results if r["modes"][mode]["status"] == s)
             for s in ("pass", "file", "alt", "fail", "none")}
        lines.append(f"| {mode} | {c['pass']}/{n} | {c['file']} | {c['alt']} | {c['fail']} | {c['none']} |")
    if regressions is not None:
        lines += ["", f"**Regressions against the baseline:** {len(regressions)}"]
        lines += [f"- {r}" for r in regressions]
    lines += size_report()
    lines += ["## Per question", "",
              "Expected chars = size of the expected section. Top hit chars = size of the first `search` hit.", "",
              "| # | Question | Expected | search | scoped | context | Expected chars | Top hit chars |",
              "|---|---|---|---|---|---|---|---|"]
    for r in results:
        q = r["question"] if len(r["question"]) <= 70 else r["question"][:67] + "..."
        m = r["modes"]
        lines.append(f"| {r['num']} | {q} | `{r['doc_id']}` | {cell(m['search'])} | {cell(m['scoped'])} "
                     f"| {cell(m['context'])} | {chars(r['expected_chars'])} | {chars(r['top_hit_chars'])} |")
    lines += ["", "## Top hits where a mode did not pass", ""]
    for r in results:
        for mode in MODES:
            m = r["modes"][mode]
            if m["status"] == "pass":
                continue
            top = "; ".join(f"`{h}`" for h in m["hits"][:3]) or "(nothing returned)"
            lines.append(f"- Q{r['num']} {mode} ({cell(m)}): {top}")
    lines.append("")
    return "\n".join(lines)


def find_regressions(results: list[dict], baseline_path: Path) -> list[str]:
    base = {r["num"]: r["modes"] for r in json.loads(baseline_path.read_text(encoding="utf-8"))}
    out = []
    for r in results:
        for mode in MODES:
            before = base.get(r["num"], {}).get(mode, {}).get("status")
            now = r["modes"][mode]["status"]
            if before == "pass" and now != "pass":
                out.append(f"Q{r['num']} {mode}: pass -> {now}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tests", type=Path, default=TESTS_FILE, help="SearchTests.md to read")
    ap.add_argument("--markdown", type=Path, help="append the result tables to this file (for example $GITHUB_STEP_SUMMARY)")
    ap.add_argument("--json", type=Path, help="write full results as JSON")
    ap.add_argument("--compare", type=Path, help="baseline JSON; exit 2 if a passing question now fails")
    args = ap.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    tests = parse_tests(args.tests)
    if not tests:
        print(f"No test rows found in {args.tests}", file=sys.stderr)
        return 1
    engine = UmamusumeGameSpaceEngine()
    print(f"Indexed {len(engine.list_docs())} docs from {engine.root}")
    SIZES.update(section_sizes(engine))
    missing = [t for t in tests if engine.resolve(t.doc_id) is None]
    for t in missing:
        print(f"WARNING: Q{t.num} expects {t.doc_id}, which is not an indexed doc", file=sys.stderr)

    results = run(engine, tests)
    regressions = find_regressions(results, args.compare) if args.compare else None
    report = render(results, regressions)
    print(report)
    if args.markdown:
        with args.markdown.open("a", encoding="utf-8") as fh:
            fh.write(report + "\n")
    if args.json:
        args.json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    return 2 if regressions else 0


if __name__ == "__main__":
    sys.exit(main())
