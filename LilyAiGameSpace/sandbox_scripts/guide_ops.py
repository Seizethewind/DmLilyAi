"""Guide helpers. Runs INSIDE a PandaStack sandbox (or in-process as the fallback), never as model code. Standard library only.

    /workspace/params.json   {"op": "prep" | "verify", ...}
Prints one JSON object: {"ok": true, "text": "<a JSON document, as a string>"} or {"ok": false, "error": "..."}.

op "prep"   For every guide section: pick the parts of the raw doc passages that best match the section (paragraphs and
            whole tables, not the first N characters), within a character budget, and compute exact figures for the
            numeric tables (highest / lowest / average / total). Facts get tags C1, C2... that the writer may cite.
    in : {"op":"prep","budget":3000,"max_facts":3,
          "sections":[{"title","queries":[...],"passages":[{"tag","doc","section","text"}]}]}
    out: {"sections":[{"passages":[{"tag","text"}],"facts":[{"tag","source","from","text"}]}]}

op "verify" Drop every sentence of a drafted section whose numbers are not in the passages it was written from, and
            every citation the passages don't have. This is the same rule as guide_builder.verify_section.
    in : {"op":"verify","sections":[{"text","tags":["S1","C1"],"allowed":["passage text", ...]}]}
    out: {"sections":[{"text","dropped"}]}

KEEP numbers_in / verify_section IN STEP with LilyAiGameSpace/number_check.py and guide_builder.verify_section:
tests/test_guide_ops.py checks that they agree.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

PARAMS = Path("/workspace/params.json")

# ----------------------------------------------------------------------------- numbers (same rules as number_check.py)
_TAG = re.compile(r"\[([SC]\d+)\]")
_NUM = re.compile(r"(?<![\w.])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?!\d)(?!(?:st|nd|rd|th)\b)")
_LIST_MARK = re.compile(r"(?m)^\s*(?:[-*\u2022]|\d+[.)])\s+")
_BULLET = re.compile(r"^\s*(?:[-*\u2022]|\d+[.)])\s+")


def _canon(n: str) -> str:
    n = n.replace(",", "")
    return n.rstrip("0").rstrip(".") if "." in n else n


def numbers_in(text: str) -> set[str]:
    """Every number in `text` (ignoring [S1] / [C1] tags and list numbering), normalised for comparison."""
    text = _LIST_MARK.sub("", _TAG.sub(" ", text))
    return {_canon(m) for m in _NUM.findall(text)}


def verify_section(text: str, tags: set[str], allowed_texts: list[str]) -> tuple[str, int]:
    """Returns (cleaned text, number of dropped sentences/lines). `allowed_texts` = the passages' title, section and text."""
    allowed: set[str] = set()
    for t in allowed_texts:
        allowed |= numbers_in(t)
    text = _TAG.sub(lambda m: m.group(0) if m.group(1) in tags else "", text)

    kept: list[str] = []
    dropped = 0
    for line in text.splitlines():
        if not line.strip() or numbers_in(line) <= allowed:
            kept.append(line.rstrip())
            continue
        parts = re.split(r"(?<=[.!?])\s+", line.strip())
        if len(parts) == 1:
            dropped += 1
            continue
        good = [p for p in parts if numbers_in(p) <= allowed]
        dropped += len(parts) - len(good)
        if good:
            joined = " ".join(good)
            m = _BULLET.match(line)
            if m and not _BULLET.match(joined):
                joined = m.group(0) + joined
            kept.append(joined)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip(), dropped


# ----------------------------------------------------------------------------- prep: choosing passages
_STOP = frozenset("the and for with from that this are was how what who why into over per not you your can its".split())
_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
_NUM_CELL = re.compile(r"^[+-]?\d[\d,]*(?:\.\d+)?\s*(?:%|x|pt|pts)?$", re.IGNORECASE)
_STRIP_MD = re.compile(r"[*_`]+")


def _terms(queries: list) -> set[str]:
    words = re.findall(r"[a-z0-9]+", " ".join(str(q) for q in queries if q).casefold())
    return {w for w in words if len(w) >= 3 and w not in _STOP}


def _is_table(block: str) -> bool:
    return block.lstrip().startswith("|")


def split_blocks(text: str) -> list[str]:
    """Paragraphs and whole tables, in order. A heading line is kept with the block that follows it."""
    blocks: list[str] = []
    cur: list[str] = []
    in_table = False

    def flush() -> None:
        if cur:
            blocks.append("\n".join(cur).strip("\n"))
            cur.clear()

    for line in text.splitlines():
        if not line.strip():
            flush()
            in_table = False
            continue
        is_table = line.lstrip().startswith("|")
        if is_table != in_table:
            flush()
            in_table = is_table
        cur.append(line)
    flush()
    merged: list[str] = []
    carry = ""
    for b in blocks:
        if not b.strip():
            continue
        if "\n" not in b and b.lstrip().startswith("#"):
            carry = (carry + "\n" + b).strip("\n")
            continue
        merged.append((carry + "\n" + b).strip("\n") if carry else b)
        carry = ""
    if carry:
        merged.append(carry)
    return merged


def _score(block: str, terms: set[str]) -> int:
    low = block.casefold()
    return sum(min(low.count(t), 3) for t in terms)


def _clip_table(block: str, room: int) -> str:
    lines = block.splitlines()
    if len(lines) < 3 or room < 80:
        return ""
    out = lines[:2]
    used = sum(len(x) + 1 for x in out)
    for row in lines[2:]:
        if used + len(row) + 1 > room:
            break
        out.append(row)
        used += len(row) + 1
    return "\n".join(out) if len(out) > 2 else ""


def _clip_text(block: str, room: int) -> str:
    if len(block) <= room:
        return block
    cut = block[:room].rsplit(" ", 1)[0].rstrip()
    return cut + " ..." if cut else ""


def select_passages(passages: list[dict], terms: set[str], budget: int) -> list[dict]:
    entries: list[list] = []     # [score, passage index, block index, text]
    for pi, p in enumerate(passages):
        for bi, block in enumerate(split_blocks(str(p.get("text") or ""))):
            entries.append([_score(block, terms), pi, bi, block])
    if not entries:
        return []
    chosen: set[int] = set()
    if sum(len(e[3]) + 2 for e in entries) <= budget:
        chosen = set(range(len(entries)))
    else:
        used = 0
        for i in sorted(range(len(entries)), key=lambda k: (-entries[k][0], entries[k][1], entries[k][2])):
            block = entries[i][3]
            if used + len(block) + 2 <= budget:
                chosen.add(i)
                used += len(block) + 2
                continue
            room = budget - used - 2
            clipped = _clip_table(block, room) if _is_table(block) else (_clip_text(block, room) if used == 0 else "")
            if clipped:
                entries[i][3] = clipped
                chosen.add(i)
                used += len(clipped) + 2
    by_passage: dict[int, list[str]] = {}
    for i in sorted(chosen, key=lambda k: (entries[k][1], entries[k][2])):
        by_passage.setdefault(entries[i][1], []).append(entries[i][3])
    return [{"tag": passages[pi].get("tag"), "text": "\n\n".join(blocks)} for pi, blocks in sorted(by_passage.items())]


# ----------------------------------------------------------------------------- prep: exact figures from tables
def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    return [c.replace("\\|", "|").strip() for c in re.split(r"(?<!\\)\|", line)]


def parse_tables(text: str) -> list[dict]:
    tables: list[dict] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and _SEP_RE.match(lines[i + 1]):
            header = _split_row(lines[i])
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append((_split_row(lines[j]) + [""] * len(header))[: len(header)])
                j += 1
            tables.append({"columns": header, "rows": rows})
            i = j
        else:
            i += 1
    return tables


def _num(cell: str):
    c = _STRIP_MD.sub("", cell).strip()
    if not _NUM_CELL.match(c):
        return None
    c = re.sub(r"(?i)\s*(%|x|pts?)$", "", c).replace(",", "")
    try:
        return float(c)
    except ValueError:
        return None


def _fmt(x: float) -> str:
    x = round(x, 2)
    return str(int(x)) if x == int(x) else f"{x:g}"


def table_facts(text: str, source: str, max_facts: int) -> list[str]:
    facts: list[str] = []
    for t in parse_tables(text):
        rows = t["rows"]
        if len(rows) < 4:
            continue
        numeric_cols = []
        for ci in range(1, len(t["columns"])):
            vals = [_num(r[ci]) for r in rows]
            if sum(v is not None for v in vals) >= max(3, int(len(rows) * 0.75)):
                numeric_cols.append(ci)
        parts = []
        for ci in numeric_cols[:2]:
            pairs = [(v, _STRIP_MD.sub("", r[0]).strip()) for r in rows for v in [_num(r[ci])] if v is not None]
            hi, lo = max(pairs, key=lambda p: p[0]), min(pairs, key=lambda p: p[0])
            vals = [v for v, _ in pairs]
            parts.append(f"{t['columns'][ci]}: highest {hi[1]} ({_fmt(hi[0])}), lowest {lo[1]} ({_fmt(lo[0])}), "
                         f"average {_fmt(sum(vals) / len(vals))}, total {_fmt(sum(vals))} over {len(vals)} rows")
        if parts:
            facts.append(f"{source}: a table of {len(rows)} rows (columns: {', '.join(t['columns'])}). " + "; ".join(parts) + ".")
        if len(facts) >= max_facts:
            break
    return facts


def op_prep(params: dict) -> dict:
    budget = int(params.get("budget") or 3000)
    max_facts = int(params.get("max_facts") or 3)
    out_sections = []
    counter = 0
    for sec in params.get("sections") or []:
        passages = [p for p in sec.get("passages") or [] if isinstance(p, dict)]
        terms = _terms(sec.get("queries") or [sec.get("title")])
        chosen = select_passages(passages, terms, budget)
        facts = []
        for p in passages:
            if len(facts) >= max_facts:
                break
            source = f"{p.get('doc')} > {p.get('section')}".strip(" >")
            for text in table_facts(str(p.get("text") or ""), source, max_facts - len(facts)):
                counter += 1
                facts.append({"tag": f"C{counter}", "source": source, "from": p.get("tag"), "text": text})
        out_sections.append({"passages": chosen, "facts": facts})
    return {"sections": out_sections}


def op_verify(params: dict) -> dict:
    out = []
    for sec in params.get("sections") or []:
        text, dropped = verify_section(str(sec.get("text") or ""), set(sec.get("tags") or []),
                                       [str(a) for a in sec.get("allowed") or []])
        out.append({"text": text, "dropped": dropped})
    return {"sections": out}


OPS = {"prep": op_prep, "verify": op_verify}


def run(params: dict) -> dict:
    op = str(params.get("op") or "").lower()
    if op not in OPS:
        return {"ok": False, "error": f"op must be one of {', '.join(OPS)}"}
    try:
        return {"ok": True, "text": json.dumps(OPS[op](params), ensure_ascii=False)}
    except Exception as e:
        return {"ok": False, "error": f"{type(e).__name__}: {e}"}


def main() -> None:
    try:
        params = json.loads(PARAMS.read_text(encoding="utf-8"))
        result = run(params if isinstance(params, dict) else {})
    except Exception as e:
        result = {"ok": False, "error": f"{type(e).__name__}: {e}"}
    sys.stdout.write(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
