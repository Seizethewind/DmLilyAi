"""Groq tools: run fixed table operations (top N, sums, filters, comparisons), game calculators and affinity maths.

They run in a PandaStack sandbox when one is configured. When it isn't (no key, SDK missing, rate limited, hourly cap)
the SAME fixed scripts run in the bot instead, so these tools are offered whenever sandbox_runner.can_run() is true and
the reply says which way the numbers were produced. Set LILYAI_SANDBOX_LOCAL_FALLBACK=0 to go back to "sandbox only":
then the tools are simply not offered without PANDASTACK_API_KEY and the pandastack package.

game_docs_process takes one operation, or a list ("ops") that runs in ONE sandbox boot, each op on its own doc section.
"""
from __future__ import annotations

import json

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiTool.Sandbox import sandbox_runner
from LilyAiGameSpace.Umamusume.Affinity import affinity_data
from LilyAiTool.Models.tool_models import ToolSpec

CATEGORY = "gamespace"

_PARAM_KEYS = ("op", "column", "columns", "n", "order", "agg", "names", "name", "name_column",
               "where_column", "where_op", "where_value", "where", "sort", "derive", "group_column", "contains",
               "table_index", "limit")


def _opt(args: dict, key: str):
    value = args.get(key)
    if isinstance(value, str):
        value = value.strip()
    return value if value not in (None, "") else None


def _how(in_sandbox: bool) -> str:
    """Where the numbers were produced, so the model (and the user) can tell. Same script and rules either way."""
    return "in a sandbox" if in_sandbox else "locally by the same fixed script, because the sandbox was unavailable"


def _params(item: dict) -> dict:
    params = {k: _opt(item, k) for k in _PARAM_KEYS}
    return {k: v for k, v in params.items() if v is not None}


async def _process_batch(args: dict, ops_arg) -> str:
    if isinstance(ops_arg, str):
        try:
            ops_arg = json.loads(ops_arg)
        except json.JSONDecodeError:
            raise ToolError("ops must be a list of operations")
    if not isinstance(ops_arg, list) or not ops_arg:
        raise ToolError("ops must be a non-empty list of operations")
    if len(ops_arg) > sandbox_runner.MAX_BATCH_OPS:
        raise ToolError(f"At most {sandbox_runner.MAX_BATCH_OPS} operations per call.")
    sources: dict[str, str] = {}
    seen: dict[tuple[str, str], str] = {}
    notes: list[str] = []
    ops: list[dict] = []
    try:
        for item in ops_arg:
            if not isinstance(item, dict):
                raise ToolError("each operation must be an object")
            doc = _opt(item, "doc") or _opt(args, "doc")
            if not doc:
                raise ToolError("every operation needs a doc")
            doc_id, title, path, text = sandbox_runner.raw_section_text(
                doc, _opt(item, "section") or _opt(args, "section"), _opt(item, "category") or _opt(args, "category"))
            name = seen.get((doc_id, path))
            if name is None:
                name = f"d{len(seen) + 1}"
                seen[(doc_id, path)] = name
                sources[name] = text
                notes.append(f"{name} = {title}" + (f" > {path}" if path else "") + f" [{doc_id}]")
            params = _params(item)
            if "op" not in params:
                raise ToolError("every operation needs an op")
            params["source"] = name
            ops.append(params)
        result, in_box = await sandbox_runner.run_table_batch_ex_async(ops, sources)
    except sandbox_runner.SandboxError as e:
        raise ToolError(str(e))
    return (f"Computed from {'; '.join(notes)} ({len(ops)} operations, exact values from the docs tables, "
            f"calculated {_how(in_box)}):\n{result}")


async def _process(ctx, args: dict) -> str:
    if _opt(args, "ops") is not None:
        return await _process_batch(args, args["ops"])
    doc = _opt(args, "doc")
    if not doc:
        raise ToolError("doc is required")
    params = _params(args)
    if "op" not in params:
        raise ToolError("op is required")
    try:
        doc_id, title, path, text = sandbox_runner.raw_section_text(doc, _opt(args, "section"), _opt(args, "category"))
        result, in_box = await sandbox_runner.run_table_op_ex_async(text, params)
    except sandbox_runner.SandboxError as e:
        raise ToolError(str(e))
    where = f"{title} > {path}" if path else title
    return f"Computed from {where} [{doc_id}] (exact values from the docs table, calculated {_how(in_box)}):\n{result}"


CALCULATORS = ["help", "pvp_score", "legacy_blue_bonus", "blue_spark_odds", "white_spark_odds", "start_delay",
               "rush_duration", "stat_effective", "wit_effectiveness", "race_phases", "length_convert",
               "speed_boost", "acceleration_gain"]


async def _calculate(ctx, args: dict) -> str:
    calc = _opt(args, "calculator")
    if not calc:
        raise ToolError("calculator is required")
    inputs = args.get("inputs")
    if isinstance(inputs, str):
        try:
            inputs = json.loads(inputs)
        except json.JSONDecodeError:
            raise ToolError("inputs must be a JSON object")
    if inputs is None:
        inputs = {}
    if not isinstance(inputs, dict):
        raise ToolError("inputs must be an object")
    try:
        result, in_box = await sandbox_runner.run_calc_ex_async(str(calc), inputs)
    except sandbox_runner.SandboxError as e:
        raise ToolError(str(e))
    return f"Calculated {_how(in_box)} with the game docs' rules ({calc}):\n{result}"


_AFFINITY_SLOTS = ("legacy1", "legacy2", "sub11", "sub12", "sub21", "sub22")


async def _affinity(ctx, args: dict) -> str:
    op = str(_opt(args, "op") or "total").lower()
    if op not in ("total", "best", "partners"):
        raise ToolError("op must be total, best or partners")
    try:
        data = affinity_data.load()
        main_ref = _opt(args, "main")
        if not main_ref:
            raise ToolError("main (the character being trained) is required")
        params: dict = {"op": op, "main": data.resolve(main_ref)}
        for slot in _AFFINITY_SLOTS:
            if _opt(args, slot):
                params[slot] = data.resolve(_opt(args, slot))
        if _opt(args, "bonus") is not None:
            params["bonus"] = float(_opt(args, "bonus"))
        if _opt(args, "top") is not None:
            params["top"] = int(_opt(args, "top"))
        ids = {params["main"], *(params[s] for s in _AFFINITY_SLOTS if s in params)}
        if op == "total":
            payload, used = data.subset(sorted(ids)), sorted(ids)      # a few numbers are enough for one total
        else:
            payload, used = {"chars": data.chars, "aff2": data.aff2, "aff3": data.aff3}, data.chars
        params["names"] = {str(c): data.label(c) for c in used}
        result, in_box = await sandbox_runner.run_affinity_ex_async(params, json.dumps(payload, separators=(",", ":")))
    except affinity_data.AffinityError as e:
        raise ToolError(str(e))
    except sandbox_runner.SandboxError as e:
        raise ToolError(str(e))
    except ValueError:
        raise ToolError("bonus and top must be numbers")
    return f"Affinity from the game's own relationship data, calculated {_how(in_box)}:\n{result}"


_OP_PROPS = {
    "doc": {"type": "string", "description": "Doc title, alias or id, e.g. 'Support Cards'"},
    "op": {"type": "string", "enum": ["tables", "table", "top", "filter", "stat", "compare", "rank", "group", "lists"],
           "description": "tables=list tables, table=show, top=sort+limit, filter=where only, stat=aggregate, "
                          "compare=named rows, rank=where one named row ranks, group=group by a column, "
                          "lists=bullet/numbered list items (no table needed)"},
    "section": {"type": ["string", "null"], "description": "Section heading holding the table (recommended)"},
    "column": {"type": ["string", "null"], "description": "Column to sort, aggregate or rank by"},
    "columns": {"type": ["string", "null"], "description": "Comma-separated columns to show"},
    "n": {"type": ["integer", "null"], "description": "Rows to keep for top (default 5)"},
    "order": {"type": ["string", "null"], "description": "desc (default) or asc, for top and rank"},
    "agg": {"type": ["string", "null"], "description": "sum, avg, min, max or count, for stat and group"},
    "names": {"type": ["string", "null"], "description": "Comma-separated row names, for compare (2+) or rank (1)"},
    "name_column": {"type": ["string", "null"], "description": "Column holding row names (default: first column)"},
    "where_column": {"type": ["string", "null"], "description": "Column for an optional row filter"},
    "where_op": {"type": ["string", "null"], "description": "eq, ne, contains, gt, gte, lt or lte"},
    "where_value": {"type": ["string", "null"], "description": "Value for the filter"},
    "where": {"type": ["array", "null"], "description": "Several filters that must ALL hold: [{column, op, value}]",
              "items": {"type": "object"}},
    "sort": {"type": ["array", "string", "null"], "description": "Sort by several columns: [{column, order}] or 'A, B'",
             "items": {"type": "object"}},
    "derive": {"type": ["object", "null"], "description": "Add a computed column: {name, numerator, denominator, scale}; "
                                                          "then use its name as a column"},
    "group_column": {"type": ["string", "null"], "description": "Column to group by, for op=group"},
    "contains": {"type": ["string", "null"], "description": "For op=lists: only items containing this word"},
    "table_index": {"type": ["integer", "null"], "description": "Which table in the section (0-based), if several"},
    "limit": {"type": ["integer", "null"], "description": "Max rows to print"},
    "category": {"type": ["string", "null"], "description": "Optional category to disambiguate the doc"},
}


def sandbox_tools() -> list[ToolSpec]:
    if not sandbox_runner.can_run():
        return []
    return [
        ToolSpec(
            "game_docs_process",
            "Calculate on a TABLE in an Umamusume game doc: top N by a column (or several), sum/avg/min/max/count, filter rows "
            "(several conditions), compare named rows, rank one row, group by a column, add a ratio column, or list a section's "
            "bullet items. Use this instead of doing arithmetic yourself or reading long tables. Start with op='tables' if you "
            "don't know the columns. For a question with several parts, or one that spans docs, pass 'ops': a list of up to 8 "
            "operations (each with its own doc, section and op fields); they run together in one go. Quote the numbers exactly "
            "as returned.",
            {"type": "object", "properties": {
                **_OP_PROPS,
                "ops": {"type": ["array", "null"], "description": "Several operations in one call; each item has the same "
                        "fields as above (doc, section, op, column...). Top-level doc/section are used when an item has none.",
                        "items": {"type": "object"}},
            }, "required": []},
            _process,
            category=CATEGORY,
            timeout=60.0,
        ),
        ToolSpec(
            "game_calculate",
            "Exact Umamusume calculations from the game docs' rules: Team Trials (PvP) score, legacy/inheritance blue-spark "
            "bonus and spark odds, start-delay and rush odds, effective stat for races, race phases, length/speed/acceleration. "
            "Use it for ANY number the user wants worked out, never do the maths yourself. Call with calculator='help' to see "
            "each calculator's inputs. Compatibility (triangle/circle) is NOT available. Quote results exactly.",
            {"type": "object", "properties": {
                "calculator": {"type": "string", "enum": CALCULATORS, "description": "Which calculator; 'help' lists inputs"},
                "inputs": {"type": ["object", "null"], "description": "Inputs for that calculator, e.g. {\"final_stat\": 850} or "
                           "{\"sparks\": [{\"stat\": \"Speed\", \"stars\": 3}]}"},
            }, "required": ["calculator"]},
            _calculate,
            category=CATEGORY,
            timeout=60.0,
        ),
        ToolSpec(
            "game_affinity",
            "Umamusume affinity (compatibility) for inheritance, from the game's real relationship data. op='total': the "
            "total for a main character with legacies and sub-legacies (names, e.g. main='Grass Wonder', legacy1='Vodka', "
            "sub11='El Condor Pasa'). op='best': the best theoretical legacy setups for a main character. op='partners': "
            "the characters with the highest pair affinity. Result shows the tier (triangle / circle / double circle: "
            "50 or less, 51-150, 151+). G1 race-win bonuses are NOT included unless you pass bonus. To score the user's "
            "SAVED parents for a trainee, use my_parents_affinity instead. Quote results exactly.",
            {"type": "object", "properties": {
                "op": {"type": "string", "enum": ["total", "best", "partners"], "description": "total, best or partners"},
                "main": {"type": "string", "description": "The character being trained"},
                "legacy1": {"type": ["string", "null"], "description": "First legacy (parent)"},
                "legacy2": {"type": ["string", "null"], "description": "Second legacy (parent)"},
                "sub11": {"type": ["string", "null"], "description": "Sub-legacy (grandparent) under legacy1"},
                "sub12": {"type": ["string", "null"], "description": "Second sub-legacy under legacy1"},
                "sub21": {"type": ["string", "null"], "description": "Sub-legacy under legacy2"},
                "sub22": {"type": ["string", "null"], "description": "Second sub-legacy under legacy2"},
                "bonus": {"type": ["number", "null"], "description": "Extra affinity from shared G1 wins, if the user gives a number"},
                "top": {"type": ["integer", "null"], "description": "How many results for best/partners"},
            }, "required": ["op", "main"]},
            _affinity,
            category=CATEGORY,
            timeout=60.0,
        ),
    ]
