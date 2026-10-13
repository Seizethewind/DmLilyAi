"""my_parents_affinity: the user's saved parents scored for one trainee by the guide's priorities AND by affinity.

my_parents(action='find') ranks parents by the guide's priority (scenario white > pinks > white count) and says
compatibility is not checked. This tool adds it: for each saved parent it works out the affinity with the trainee (the pair
plus that parent's own grandparents), then the best two-parent combinations, using the game's own relationship data.
The affinity maths runs in the PandaStack sandbox, or in the bot with the same fixed script when the sandbox is unavailable.

It is read-only: it never changes the user's collection. Everything is keyed by ctx.user_id, which the system sets.
"""
from __future__ import annotations

import json
from typing import Any

from LilyAiCore.Exceptions.errors import ToolError
from LilyAiGameSpace.Umamusume import UmamusumeCatalog as cat
from LilyAiTool.Sandbox import sandbox_runner
from LilyAiGameSpace.Umamusume.Affinity import affinity_data
from LilyAiTool.Models.tool_models import ToolContextData, ToolSpec

from .parent_ranking import rank_parents

CATEGORY = "collection"
MAX_PARENTS = 60


def _opt_str(args: dict, key: str) -> str | None:
    value = args.get(key)
    if value is None:
        return None
    value = str(value).strip()
    return value or None


def _how(in_sandbox: bool) -> str:
    return "in a sandbox" if in_sandbox else "locally by the same fixed script, because the sandbox was unavailable"


def _label(parent: dict) -> str:
    nick = f' "{parent["nickname"]}"' if parent.get("nickname") else ""
    return f"#{parent['parent_id']} {cat.uma_name(parent['uma_id'])}{nick}"


def parent_affinity_tools(collection: Any) -> list[ToolSpec]:
    async def my_parents_affinity(ctx: ToolContextData, args: dict) -> str:
        if not ctx.user_id:
            raise ToolError("No Discord user in this context.")
        uid = ctx.user_id
        trainee = _opt_str(args, "trainee")
        if not trainee:
            raise ToolError("trainee is required (the character the career is for)")
        chars = cat.resolve_uma(trainee)
        if len(chars) != 1:
            hint = ("No character matches that name." if not chars
                    else "Several characters match: " + ", ".join(c.name for c in chars[:8]) + ". Ask the user which.")
            raise ToolError(hint)
        targets: dict[str, str | None] = {}
        for kind in ("distance", "track", "style"):
            raw = _opt_str(args, kind)
            targets[kind] = None
            if raw:
                targets[kind] = cat.norm_aptitude(kind, raw)
                if not targets[kind]:
                    raise ToolError(f"unknown {kind} {raw!r}")
        scenario = cat.norm_scenario(args.get("scenario")) if _opt_str(args, "scenario") else None
        try:
            limit = max(1, min(int(args.get("limit") or 5), 10))
            bonus = float(args["bonus"]) if args.get("bonus") not in (None, "") else 0.0
        except (TypeError, ValueError):
            raise ToolError("limit must be a whole number and bonus a number")

        parents = collection.list_parents(uid)
        if not parents:
            return ("No parents on file. Ask the user to describe their inheritance umas "
                    "(or save them after a career), then try again.")
        parents = parents[:MAX_PARENTS]

        try:
            data = affinity_data.load()
            main = data.resolve(chars[0].name)
        except affinity_data.AffinityError as e:
            raise ToolError(str(e))

        items: list[dict] = []
        ids = {main}
        unmatched: list[str] = []
        for p in parents:
            try:
                uma = data.resolve(cat.uma_name(p["uma_id"]))
            except affinity_data.AffinityError:
                unmatched.append(_label(p))
                continue
            gps: list[int] = []
            for g in p.get("grandparents") or []:
                name = str(g.get("name") or "").strip()
                if not name:
                    continue
                try:
                    gps.append(data.resolve(name))
                except affinity_data.AffinityError:
                    continue
            ids |= {uma, *gps}
            items.append({"id": p["parent_id"], "label": _label(p), "uma": uma, "gps": gps})
        if not items:
            return ("None of the saved parents are in the affinity data, so affinity can't be scored"
                    + (": " + "; ".join(unmatched[:10]) if unmatched else "") + ".")

        params: dict[str, Any] = {"op": "parents", "main": main, "parents": items, "top": limit,
                                  "names": {str(c): data.label(c) for c in ids}}
        if bonus:
            params["bonus"] = bonus
        try:
            text, in_box = await sandbox_runner.run_affinity_ex_async(
                params, json.dumps(data.subset(sorted(ids)), separators=(",", ":")))
        except sandbox_runner.SandboxError as e:
            raise ToolError(str(e))

        ranked = rank_parents(parents, trainee_uma_id=chars[0].uma_id, scenario=scenario, **targets)[:limit]
        goal = ", ".join(x for x in (scenario, targets["distance"], targets["track"], targets["style"]) if x) or "no target given"
        out = [f"Saved parents for {chars[0].name}, affinity calculated {_how(in_box)}:", text, "",
               f"Guide priority score ({goal}; scenario white > pinks > white count), best {len(ranked)}:"]
        out += [f"- {_label(p)}: {score:g}" for score, p, _ in ranked]
        if unmatched:
            out.append("Not in the affinity data (so not scored for affinity): " + "; ".join(unmatched[:10]))
        out.append("Not checked here: the Unique Skill Gate (does the unique activate on the target track? check the Skill docs). "
                   "Affinity is the game's base data; ask the user to confirm the rating they see in the game.")
        return "\n".join(out)

    return [
        ToolSpec(
            "my_parents_affinity",
            "Score the CURRENT user's SAVED inheritance parents (from my_parents) for a trainee by AFFINITY, next to the guide's "
            "priority score. Gives each parent's affinity with the trainee (pair + that parent's grandparents) and the best "
            "two-parent combinations with their tier (triangle / circle / double circle). Use it when the user asks which of "
            "their parents are compatible or best for a trainee. Pass the trainee, and optionally scenario, distance, track, "
            "style (for the guide score), bonus (extra affinity from shared G1 wins, only if the user gives a number) and limit. "
            "Read-only. Quote results exactly; the Unique Skill Gate still needs checking in the Skill docs.",
            {"type": "object", "properties": {
                "trainee": {"type": "string", "description": "The character the career is for"},
                "scenario": {"type": ["string", "null"], "description": "Ura Finale, Unity Cup, ..."},
                "distance": {"type": ["string", "null"], "description": "sprint, mile, medium or long"},
                "track": {"type": ["string", "null"], "description": "turf or dirt"},
                "style": {"type": ["string", "null"], "description": "front runner, pace chaser, late surger or end closer"},
                "bonus": {"type": ["number", "null"], "description": "Extra affinity from shared G1 wins, if the user gives a number"},
                "limit": {"type": ["integer", "null"], "description": "How many results (default 5, max 10)"},
            }, "required": ["trainee"]},
            my_parents_affinity, category=CATEGORY, timeout=60.0,
        ),
    ]
