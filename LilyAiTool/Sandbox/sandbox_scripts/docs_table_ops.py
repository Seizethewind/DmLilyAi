"""Fixed table-processing script. It runs INSIDE a PandaStack sandbox (or in-process as the fallback), never as model code.

LilyAi uploads these files and runs this script:
    /workspace/input.md        the raw (unclipped) text of one docs section (optional when every op names a source)
    /workspace/src_<name>.md   more docs sections, for batches that touch several docs (optional)
    /workspace/params.json     what to do (chosen by the chat model, validated here)
    /workspace/docs_table_ops.py   this file

It prints exactly one JSON object to stdout: {"ok": true, "text": "..."} or {"ok": false, "error": "..."}.
Standard library only, so it works on any template. The model never supplies code, only parameters.

Operations (params["op"]):
    tables    list the markdown tables found
    table     re-emit a table (optionally only some columns, sorted) as clean markdown
    top       sort by a column (or several: "sort") and keep the first n rows
    filter    keep rows matching one or more conditions
    stat      sum / avg / min / max / count of a column
    compare   put the named rows side by side and show the difference for numeric columns
    rank      where one named row ranks by a column ("rank 3 of 12")
    group     group rows by a column and count / sum / avg / min / max another column
    lists     bullet and numbered list items (no table needed), optionally only those containing a word

Any table op can also take:
    where_column/where_op/where_value   one condition (the original form), and/or
    where: [{"column","op","value"}, ...]   several conditions, all of which must hold
    derive: {"name","numerator","denominator","scale"}   adds a computed column (numerator / denominator * scale)
    sort: [{"column","order"}, ...]   or a comma-separated string of columns (each descending)

A batch is {"ops": [ {op params, "source": "<name>"} , ... ]} (at most 8): one boot, one result per op. An op with no
"source" uses input.md.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

INPUT = Path("/workspace/input.md")
PARAMS = Path("/workspace/params.json")
SOURCES_DIR = Path("/workspace")

MAX_ROWS = 200
MAX_BATCH = 8
_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
_NUM_RE = re.compile(r"^[+-]?\d[\d,]*(?:\.\d+)?\s*(?:%|x|pt|pts)?$", re.IGNORECASE)
_STRIP_MD = re.compile(r"[*_`]+")
_ITEM_RE = re.compile(r"^\s*(?:[-*\u2022]|\d+[.)])\s+(.*\S)\s*$")
_WHERE_OPS = ("eq", "ne", "contains", "gt", "gte", "lt", "lte")
_AGGS = ("sum", "avg", "min", "max", "count")


class OpError(Exception):
    pass


# ----------------------------------------------------------------- parsing
def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells = re.split(r"(?<!\\)\|", line)
    return [c.replace("\\|", "|").strip() for c in cells]


def parse_tables(text: str) -> list[dict]:
    tables: list[dict] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|") and i + 1 < len(lines) and _SEP_RE.match(lines[i + 1]):
            header = _split_row(lines[i])
            rows: list[list[str]] = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                row = _split_row(lines[j])
                row = (row + [""] * len(header))[: len(header)]
                rows.append(row)
                j += 1
            tables.append({"columns": header, "rows": rows})
            i = j
        else:
            i += 1
    return tables


def to_number(cell: str):
    c = _STRIP_MD.sub("", cell).strip()
    if not _NUM_RE.match(c):
        return None
    c = re.sub(r"(?i)\s*(%|x|pts?)$", "", c).replace(",", "")
    try:
        return float(c)
    except ValueError:
        return None


def fmt_num(x: float) -> str:
    x = round(x, 4)
    return str(int(x)) if x == int(x) else f"{x:g}"


def _norm(s: str) -> str:
    return re.sub(r"[\W_]+", "", _STRIP_MD.sub("", s).casefold())


def find_column(columns: list[str], name: str) -> int:
    q = _norm(str(name))
    if not q:
        raise OpError("column name is empty")
    norm = [_norm(c) for c in columns]
    for test in (lambda c: c == q, lambda c: c.startswith(q), lambda c: q in c):
        hits = [i for i, c in enumerate(norm) if test(c)]
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:
            raise OpError(f"column '{name}' is ambiguous: {', '.join(columns[i] for i in hits)}")
    raise OpError(f"no column '{name}'. Columns: {', '.join(columns)}")


# ----------------------------------------------------------------- helpers
def _csv(value) -> list[str]:
    if not value:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    return [p.strip() for p in str(value).split(",") if p.strip()]


def _conditions(params: dict) -> list[dict]:
    conds: list[dict] = []
    if params.get("where_column"):
        conds.append({"column": params["where_column"], "op": params.get("where_op"), "value": params.get("where_value")})
    extra = params.get("where")
    if extra is not None:
        if not isinstance(extra, list) or not all(isinstance(c, dict) for c in extra):
            raise OpError("where must be a list of {column, op, value}")
        conds.extend(extra)
    return conds


def sort_specs(params: dict) -> list[dict]:
    raw = params.get("sort")
    if raw is None:
        return []
    if isinstance(raw, str):
        raw = [{"column": c} for c in _csv(raw)]
    if not isinstance(raw, list) or not all(isinstance(x, dict) and x.get("column") for x in raw):
        raise OpError("sort must be a list of {column, order} (order: desc by default, or asc)")
    return [{"column": x["column"], "order": str(x.get("order") or "desc").lower()} for x in raw]


def _wanted_columns(params: dict) -> list[str]:
    d = params.get("derive") if isinstance(params.get("derive"), dict) else {}
    derived = str(d.get("name") or "").strip()
    wanted = [params.get("column"), params.get("group_column"), d.get("numerator"), d.get("denominator")]
    wanted += _csv(params.get("columns"))
    wanted += [c.get("column") for c in _conditions(params)]
    wanted += [s["column"] for s in sort_specs(params)]
    return [str(w) for w in wanted if w and str(w) != derived]


def choose_table(tables: list[dict], params: dict) -> dict:
    if not tables:
        raise OpError("no markdown table found in this section")
    idx = params.get("table_index")
    if idx is not None:
        if not isinstance(idx, int) or not (0 <= idx < len(tables)):
            raise OpError(f"table_index must be 0-{len(tables) - 1}")
        return tables[idx]
    wanted = _wanted_columns(params)
    if wanted:
        for t in tables:
            try:
                for w in wanted:
                    find_column(t["columns"], w)
                return t
            except OpError:
                continue
    return tables[0]


def apply_derive(table: dict, params: dict) -> dict:
    d = params.get("derive")
    if not d:
        return table
    if not isinstance(d, dict):
        raise OpError("derive must be {name, numerator, denominator, scale}")
    name = str(d.get("name") or "").strip()
    if not name:
        raise OpError("derive needs a name for the new column")
    ni = find_column(table["columns"], d.get("numerator") or "")
    di = find_column(table["columns"], d.get("denominator") or "")
    try:
        scale = float(d.get("scale", 1))
    except (TypeError, ValueError):
        raise OpError("derive scale must be a number")
    rows = []
    for r in table["rows"]:
        a, b = to_number(r[ni]), to_number(r[di])
        rows.append(r + [fmt_num(a / b * scale) if a is not None and b not in (None, 0) else ""])
    return {"columns": table["columns"] + [name], "rows": rows}


def md_table(columns: list[str], rows: list[list[str]]) -> str:
    esc = lambda s: str(s).replace("|", "\\|")
    out = ["| " + " | ".join(esc(c) for c in columns) + " |",
           "| " + " | ".join("---" for _ in columns) + " |"]
    out += ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def apply_where(table: dict, params: dict) -> tuple[list[list[str]], str]:
    rows = table["rows"]
    labels: list[str] = []
    for cond in _conditions(params):
        col = cond.get("column")
        if not col:
            raise OpError("each where condition needs a column")
        ci = find_column(table["columns"], col)
        op = str(cond.get("op") or "eq").lower()
        if op not in _WHERE_OPS:
            raise OpError("where_op must be one of eq, ne, contains, gt, gte, lt, lte")
        value = cond.get("value")
        if value is None or str(value).strip() == "":
            raise OpError("where_value is required with where_column")
        value = str(value).strip()
        vnum = to_number(value)

        def keep(cell: str, op=op, value=value, vnum=vnum) -> bool:
            cnum = to_number(cell)
            if op in ("gt", "gte", "lt", "lte"):
                if cnum is None or vnum is None:
                    return False
                return {"gt": cnum > vnum, "gte": cnum >= vnum, "lt": cnum < vnum, "lte": cnum <= vnum}[op]
            a, b = _STRIP_MD.sub("", cell).casefold().strip(), value.casefold()
            if op == "eq":
                return (cnum == vnum) if (cnum is not None and vnum is not None) else a == b
            if op == "ne":
                return (cnum != vnum) if (cnum is not None and vnum is not None) else a != b
            return b in a   # contains

        rows = [r for r in rows if keep(r[ci])]
        labels.append(f"{table['columns'][ci]} {op} {value}")
    return rows, " and ".join(labels)


def sort_rows(table: dict, rows: list[list[str]], specs: list[dict]) -> list[list[str]]:
    """Stable multi-key sort. A numeric column sorts by value (cells that aren't numbers go last); others by text."""
    out = list(rows)
    for spec in reversed(specs):
        ci = find_column(table["columns"], spec["column"])
        desc = spec["order"] != "asc"
        present = [r for r in out if to_number(r[ci]) is not None]
        if present and len(present) >= max(1, len(out) // 2):
            missing = [r for r in out if to_number(r[ci]) is None]
            present.sort(key=lambda r: to_number(r[ci]), reverse=desc)
            out = present + missing
        else:
            out.sort(key=lambda r: _STRIP_MD.sub("", r[ci]).casefold(), reverse=desc)
    return out


def select(table: dict, rows: list[list[str]], params: dict) -> tuple[list[str], list[list[str]]]:
    wanted = _csv(params.get("columns"))
    if not wanted:
        return table["columns"], rows
    idxs = [find_column(table["columns"], w) for w in wanted]
    return [table["columns"][i] for i in idxs], [[r[i] for i in idxs] for r in rows]


def clip(rows: list[list[str]], limit) -> tuple[list[list[str]], str]:
    cap = MAX_ROWS if not isinstance(limit, int) or limit <= 0 else min(limit, MAX_ROWS)
    if len(rows) > cap:
        return rows[:cap], f"(showing {cap} of {len(rows)} rows)"
    return rows, ""


# -------------------------------------------------------------------- ops
def op_tables(tables, params):
    if not tables:
        return "No markdown tables in this section."
    lines = []
    for i, t in enumerate(tables):
        lines.append(f"- table_index {i}: {len(t['rows'])} rows; columns: {', '.join(t['columns'])}")
    return "\n".join(lines)


def op_table(table, params):
    rows, cond = apply_where(table, params)
    specs = sort_specs(params)
    if specs:
        rows = sort_rows(table, rows, specs)
    cols, rows = select(table, rows, params)
    rows, note = clip(rows, params.get("limit"))
    head = f"{len(rows)} rows" + (f" where {cond}" if cond else "")
    return "\n".join(x for x in (head, md_table(cols, rows), note) if x)


def op_top(table, params):
    specs = sort_specs(params)
    rows, cond = apply_where(table, params)
    n = params.get("n")
    n = n if isinstance(n, int) and n > 0 else 5
    if specs:
        chosen = sort_rows(table, rows, specs)[:n]
        cols, chosen = select(table, chosen, params)
        head = "Top {} sorted by {}".format(len(chosen), ", ".join(
            f"{table['columns'][find_column(table['columns'], s['column'])]} ({'asc' if s['order'] == 'asc' else 'desc'})"
            for s in specs))
        if cond:
            head += f", where {cond}"
        return "\n".join(x for x in (head, md_table(cols, chosen)) if x)
    col = params.get("column")
    if not col:
        raise OpError("column is required for top")
    ci = find_column(table["columns"], col)
    scored = [(to_number(r[ci]), r) for r in rows]
    numeric = [(v, r) for v, r in scored if v is not None]
    if not numeric:
        raise OpError(f"column '{table['columns'][ci]}' has no numeric values")
    desc = (params.get("order") or "desc").lower() != "asc"
    numeric.sort(key=lambda p: p[0], reverse=desc)
    chosen = [r for _, r in numeric[:n]]
    cols, chosen = select(table, chosen, params)
    skipped = len(rows) - len(numeric)
    head = f"Top {len(chosen)} by {table['columns'][ci]} ({'highest' if desc else 'lowest'} first)"
    if cond:
        head += f", where {cond}"
    note = f"({skipped} rows skipped: not numeric)" if skipped else ""
    return "\n".join(x for x in (head, md_table(cols, chosen), note) if x)


def op_filter(table, params):
    if not _conditions(params):
        raise OpError("where_column, where_op and where_value (or a where list) are required for filter")
    return op_table(table, params)


def op_stat(table, params):
    agg = (params.get("agg") or "").lower()
    if agg not in _AGGS:
        raise OpError("agg must be one of sum, avg, min, max, count")
    rows, cond = apply_where(table, params)
    suffix = f" where {cond}" if cond else ""
    if agg == "count":
        return f"count{suffix} = {len(rows)}"
    col = params.get("column")
    if not col:
        raise OpError("column is required for sum/avg/min/max")
    ci = find_column(table["columns"], col)
    vals = [v for v in (to_number(r[ci]) for r in rows) if v is not None]
    if not vals:
        raise OpError(f"column '{table['columns'][ci]}' has no numeric values")
    result = {"sum": sum(vals), "avg": sum(vals) / len(vals), "min": min(vals), "max": max(vals)}[agg]
    return f"{agg} of {table['columns'][ci]}{suffix} = {fmt_num(result)} (over {len(vals)} numeric values)"


def _pick_row(table, rows, name: str, ki: int) -> list[str]:
    q = _norm(name)
    exact = [r for r in rows if _norm(r[ki]) == q]
    part = exact or [r for r in rows if q and q in _norm(r[ki])]
    if len(part) != 1:
        why = "not found" if not part else f"matches {len(part)} rows"
        raise OpError(f"'{name}' {why} in column '{table['columns'][ki]}'")
    return part[0]


def op_compare(table, params):
    names = _csv(params.get("names"))
    if len(names) < 2:
        raise OpError("names needs at least two comma-separated row names")
    key_col = params.get("name_column")
    ki = find_column(table["columns"], key_col) if key_col else 0
    picked = [_pick_row(table, table["rows"], name, ki) for name in names]
    cols, shown = select(table, picked, params)
    out = [md_table(cols, shown)]
    if len(picked) == 2:
        diffs = []
        for ci, c in enumerate(table["columns"]):
            if c not in cols or ci == ki:
                continue
            a, b = to_number(picked[0][ci]), to_number(picked[1][ci])
            if a is not None and b is not None:
                diffs.append(f"- {c}: {picked[1][ki]} minus {picked[0][ki]} = {fmt_num(b - a)}")
        if diffs:
            out.append("Differences (second minus first):\n" + "\n".join(diffs))
    return "\n\n".join(out)


def op_rank(table, params):
    names = _csv(params.get("names")) or _csv(params.get("name"))
    if len(names) != 1:
        raise OpError("rank needs exactly one row name (names or name)")
    col = params.get("column")
    if not col:
        raise OpError("column is required for rank")
    ci = find_column(table["columns"], col)
    key_col = params.get("name_column")
    ki = find_column(table["columns"], key_col) if key_col else 0
    rows, cond = apply_where(table, params)
    numeric = [v for v in (to_number(r[ci]) for r in rows) if v is not None]
    if not numeric:
        raise OpError(f"column '{table['columns'][ci]}' has no numeric values")
    desc = (params.get("order") or "desc").lower() != "asc"
    target = _pick_row(table, rows, names[0], ki)
    tv = to_number(target[ci])
    if tv is None:
        raise OpError(f"'{names[0]}' has no numeric value in '{table['columns'][ci]}'")
    ahead = sum(1 for v in numeric if (v > tv if desc else v < tv))
    return (f"{target[ki]} ranks {ahead + 1} of {len(numeric)} by {table['columns'][ci]} "
            f"({'highest' if desc else 'lowest'} first): {fmt_num(tv)}" + (f" (where {cond})" if cond else ""))


def op_group(table, params):
    gcol = params.get("group_column")
    if not gcol:
        raise OpError("group_column is required for group")
    gi = find_column(table["columns"], gcol)
    agg = (params.get("agg") or "count").lower()
    if agg not in _AGGS:
        raise OpError("agg must be one of sum, avg, min, max, count")
    col = params.get("column")
    ci = None
    if agg != "count":
        if not col:
            raise OpError("column is required for sum/avg/min/max")
        ci = find_column(table["columns"], col)
    rows, cond = apply_where(table, params)
    groups: dict[str, tuple[str, list[list[str]]]] = {}
    for r in rows:
        label = _STRIP_MD.sub("", r[gi]).strip() or "(blank)"
        groups.setdefault(label.casefold(), (label, []))[1].append(r)
    results = []
    for label, grp in groups.values():
        if agg == "count":
            v = float(len(grp))
        else:
            vals = [x for x in (to_number(r[ci]) for r in grp) if x is not None]
            v = None if not vals else {"sum": sum(vals), "avg": sum(vals) / len(vals), "min": min(vals), "max": max(vals)}[agg]
        results.append((label, v))
    results.sort(key=lambda t: (t[1] is None, -(t[1] or 0), t[0].casefold()))
    head_col = "count" if agg == "count" else f"{agg} of {table['columns'][ci]}"
    shown, note = results[:50], ("(showing 50 groups)" if len(results) > 50 else "")
    body = md_table([table["columns"][gi], head_col], [[label, "n/a" if v is None else fmt_num(v)] for label, v in shown])
    head = f"{len(results)} groups by {table['columns'][gi]}" + (f" where {cond}" if cond else "")
    return "\n".join(x for x in (head, body, note) if x)


def op_lists(text, params):
    items = [m.group(1) for m in (_ITEM_RE.match(line) for line in text.splitlines()) if m]
    needle = str(params.get("contains") or params.get("where_value") or "").strip().casefold()
    if needle:
        items = [i for i in items if needle in _STRIP_MD.sub("", i).casefold()]
    if not items:
        raise OpError("no list items found" + (f" containing '{needle}'" if needle else " in this section"))
    limit = params.get("limit")
    cap = MAX_ROWS if not isinstance(limit, int) or limit <= 0 else min(limit, MAX_ROWS)
    head = f"{len(items)} list items" + (f" containing '{needle}'" if needle else "")
    note = f"(showing {cap} of {len(items)})" if len(items) > cap else ""
    return "\n".join(x for x in (head, *[f"- {i}" for i in items[:cap]], note) if x)


OPS = {"tables": op_tables, "table": op_table, "top": op_top, "filter": op_filter,
       "stat": op_stat, "compare": op_compare, "rank": op_rank, "group": op_group}
ALL_OPS = (*OPS, "lists")


def run_one(text: str, params: dict) -> dict:
    op = str(params.get("op") or "").lower()
    if op not in ALL_OPS:
        return {"ok": False, "error": f"op must be one of {', '.join(ALL_OPS)}"}
    try:
        if op == "lists":
            return {"ok": True, "text": op_lists(text, params)}
        tables = parse_tables(text)
        if op == "tables":
            return {"ok": True, "text": op_tables(tables, params)}
        table = apply_derive(choose_table(tables, params), params)
        return {"ok": True, "text": OPS[op](table, params)}
    except OpError as e:
        return {"ok": False, "error": str(e)}


def run_batch(text: str, items: list, sources: dict) -> dict:
    if not items:
        return {"ok": False, "error": "ops is empty"}
    if len(items) > MAX_BATCH:
        return {"ok": False, "error": f"at most {MAX_BATCH} ops per batch"}
    parts: list[str] = []
    failures = 0
    for i, item in enumerate(items, 1):
        if not isinstance(item, dict):
            parts.append(f"[{i}] error: each op must be an object")
            failures += 1
            continue
        src = item.get("source")
        label = f"[{i}] {item.get('op')}" + (f" on {src}" if src else "")
        if src:
            if src not in sources:
                parts.append(f"{label}: error: unknown source {src!r}")
                failures += 1
                continue
            body = sources[src]
        else:
            body = text
        r = run_one(body, item)
        if r["ok"]:
            parts.append(f"{label}:\n{r['text']}")
        else:
            failures += 1
            parts.append(f"{label}: error: {r['error']}")
    if failures == len(items):
        return {"ok": False, "error": "\n".join(parts)}
    return {"ok": True, "text": "\n\n".join(parts)}


def run(text: str, params: dict, sources: dict | None = None) -> dict:
    if isinstance(params.get("ops"), list):
        return run_batch(text, params["ops"], sources or {})
    return run_one(text, params)


def _read_sources() -> dict:
    out = {}
    for p in sorted(SOURCES_DIR.glob("src_*.md")):
        out[p.stem[len("src_"):]] = p.read_text(encoding="utf-8")
    return out


def main() -> None:
    try:
        params = json.loads(PARAMS.read_text(encoding="utf-8"))
        text = INPUT.read_text(encoding="utf-8") if INPUT.exists() else ""
        result = run(text, params if isinstance(params, dict) else {}, _read_sources())
    except Exception as e:  # always answer with JSON
        result = {"ok": False, "error": f"{type(e).__name__}: {e}"}
    sys.stdout.write(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
