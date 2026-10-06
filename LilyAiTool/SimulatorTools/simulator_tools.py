"""Chat-model tools for Simulator Mode: list a user's veterans, look up skills and courses, run the race simulator.

The model only supplies parameters (a veteran, a course id, optional skills). It never supplies code, and the numbers it
quotes come straight from LilyAiGameSpace/Umamusume/Simulation (via sim_service). Veterans are the CURRENT user's, read
from the database by ctx.user_id, so one user can never simulate or list another user's veterans.

Only registered when the simulator's data files exist (see sim_service.is_available), so the model never sees a tool
that cannot run.
"""
from __future__ import annotations

from typing import Any

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiCore.Logging.logger import get_logger
from LilyAiMemory.Veteran.veteran_store import VeteranStore
from LilyAiTool.Models.tool_models import ToolContextData, ToolSpec

CATEGORY = "simulator"
log = get_logger("tool.simulator")


def _opt(args: dict, key: str):
    v = args.get(key)
    if isinstance(v, str):
        v = v.strip()
    return v if v not in (None, "") else None


def _stats(vet: dict) -> str:
    s = vet["stats"]
    return f"{s['speed']}/{s['stamina']}/{s['power']}/{s['guts']}/{s['wisdom']}"


def simulator_tools(store: VeteranStore) -> list[ToolSpec]:
    # Imported here, not at module level: a problem in the Simulation folder must cost Simulator Mode, not the whole bot.
    try:
        from LilyAiGameSpace.Umamusume.Simulation import sim_service
        if not sim_service.is_available():
            log.info("simulator data (skills.json/courses.json) not found: Simulator Mode tools are off")
            return []
    except Exception:
        log.exception("simulator could not be loaded: Simulator Mode tools are off")
        return []

    def need_user(ctx: ToolContextData) -> str:
        if not ctx.user_id:
            raise ToolError("No user in this context, so there are no saved veterans to use.")
        return ctx.user_id

    def sim_list_veterans(ctx: ToolContextData, args: dict) -> str:
        rows = store.list(need_user(ctx))
        if not rows:
            return ("This user has no saved veterans yet. Tell them to send screenshots of the veteran's \"Umamusume "
                    "Details\" screen (skills tab, scrolled if the list is long) and they will be saved automatically.")
        lines = []
        for r in rows:
            vet = r["vet"]
            try:
                style = sim_service.best_style(vet)
            except ValueError:
                style = "?"
            lines.append(f"#{r['vet_id']} {vet.get('name') or 'Unnamed'}: stats {_stats(vet)} (speed/stamina/power/guts/wit), "
                         f"{len(vet['skills'])} skills, best style {style}, {store.result_count(ctx.user_id, r['vet_id'])} saved results")
        return "\n".join(lines)

    def sim_find_skill(ctx: ToolContextData, args: dict) -> str:
        query = _opt(args, "query")
        if not query:
            raise ToolError("query is required")
        try:
            hits = sim_service.find_skills(query, 15)
        except sim_service.SimulationError as e:
            raise ToolError(str(e))
        if not hits:
            return f"No skill name contains {query!r}. Try a shorter word."
        return "\n".join(f"{h['id']}: {h['name']}" + (f" ({h['name_jp']})" if h.get("name_jp") else "")
                         + (" [partly modelled]" if h["partial"] else "") for h in hits)

    def sim_list_courses(ctx: ToolContextData, args: dict) -> str:
        try:
            rows, total = sim_service.list_courses(_opt(args, "query") or "", 30)
        except sim_service.SimulationError as e:
            raise ToolError(str(e))
        if not rows:
            return "No course matches that. Try the track name alone (e.g. 'tokyo') or a distance."
        out = "\n".join(f"{r['id']}: {r['course']}" for r in rows)
        return out + (f"\n...{total - len(rows)} more; narrow the query." if total > len(rows) else "")

    async def sim_run(ctx: ToolContextData, args: dict) -> str:
        uid = need_user(ctx)
        ref, course = _opt(args, "veteran"), _opt(args, "course")
        if ref is None or course is None:
            raise ToolError("veteran and course are required (use sim_list_veterans and sim_list_courses to find them)")
        matches = store.find(uid, ref)
        if not matches:
            raise ToolError(f"No saved veteran matches {ref!r}. Call sim_list_veterans to see the saved ones.")
        if len(matches) > 1:
            raise ToolError("More than one veteran matches: " + ", ".join(f"#{m['vet_id']} {m['name']}" for m in matches)
                            + ". Ask the user which one, or pass the # number.")
        row = matches[0]
        add = args.get("add_skills") or []
        if isinstance(add, str):
            add = [s.strip() for s in add.split(",") if s.strip()]
        kw: dict[str, Any] = {"style": _opt(args, "style"), "add_skills": add[:10] or None}
        if _opt(args, "ground") is not None:
            kw["ground"] = args["ground"]
        if _opt(args, "mood") is not None:
            kw["mood"] = args["mood"]
        if _opt(args, "runs") is not None:
            kw["runs"] = args["runs"]
        try:
            text, _ = await sim_service.run_simulation_async(row["vet"], str(course), **kw)
        except sim_service.SimulationError as e:
            raise ToolError(str(e))
        store.add_result(uid, row["vet_id"], str(course), text)
        return f"Veteran #{row['vet_id']}. " + text

    return [
        ToolSpec(
            "sim_list_veterans",
            "List the veterans (finished trainees) this user has saved, with their stats and number. Call this first in "
            "Simulator Mode to see what can be simulated.",
            {"type": "object", "properties": {}, "required": []},
            sim_list_veterans, category=CATEGORY,
        ),
        ToolSpec(
            "sim_find_skill",
            "Search the simulator's skill list by name. Skill names must match exactly, so use this to find the exact name "
            "(with its ○ or ◎) before passing it as add_skills.",
            {"type": "object", "properties": {"query": {"type": "string", "description": "Part of a skill name, e.g. 'corner recovery'"}},
             "required": ["query"]},
            sim_find_skill, category=CATEGORY,
        ),
        ToolSpec(
            "sim_list_courses",
            "Search the simulator's race courses by track and distance, e.g. 'tokyo 2400'. Returns course ids to pass to sim_run. "
            "A track can have both a turf and a dirt course, so check the surface.",
            {"type": "object", "properties": {"query": {"type": ["string", "null"], "description": "Track and/or distance, e.g. 'tokyo 2400'"}},
             "required": []},
            sim_list_courses, category=CATEGORY,
        ),
        ToolSpec(
            "sim_run",
            "Run the Monte Carlo race simulator on one of the user's saved veterans on a course and return finish-time statistics. "
            "Optionally add skills to compare 'as saved' (A) against 'with these extra skills' (B). Quote the numbers exactly as "
            "returned and mention any warnings. It models a single runner, so results are for comparing builds, not predicting a real race.",
            {"type": "object", "properties": {
                "veteran": {"type": "string", "description": "The veteran's # number (e.g. '2') or name"},
                "course": {"type": "string", "description": "Course id from sim_list_courses"},
                "style": {"type": ["string", "null"], "description": "front, pace, late or end; default is the veteran's best style"},
                "add_skills": {"type": ["array", "null"], "items": {"type": "string"}, "description": "Exact skill names to add as build B"},
                "ground": {"type": ["string", "null"], "description": "good (default), yielding, soft or heavy"},
                "mood": {"type": ["integer", "null"], "description": "-2 (awful) to 2 (great); default 2"},
                "runs": {"type": ["integer", "null"], "description": "Races to simulate, 50-1000; default 300"},
            }, "required": ["veteran", "course"]},
            sim_run, category=CATEGORY, timeout=120.0,
        ),
    ]
