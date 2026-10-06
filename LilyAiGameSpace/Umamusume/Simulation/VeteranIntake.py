#!/usr/bin/env python3
"""
VeteranIntake -- decide whether images a user uploads are veteran screens, and parse them.

The rule is simple: every uploaded image goes to the vision AI with INTAKE_PROMPT. If what comes
back parses into a complete veteran (all five stats readable), the image IS a veteran image. If
the AI says "not a veteran", or the reply has no usable stats, it is just an ordinary image and
the bot should carry on as usual. No keyword or filename guessing is involved.

Several screenshots of the same veteran (the skill list scrolls, so people send two or three) are
merged into one veteran: skills are combined and duplicates dropped. Screenshots of different
veterans stay separate.

This file does not import discord or call any AI itself. You pass in `ask(image_bytes, prompt) -> str`,
your existing vision call (it may be async). Example with discord.py:

    from VeteranIntake import intake_images, format_reply

    @client.event
    async def on_message(message):
        if message.author.bot or not isinstance(message.channel, discord.DMChannel):
            return
        images = [await a.read() for a in message.attachments
                  if (a.content_type or "").startswith("image/")]
        if not images:
            return
        outcome = await intake_images(images, ask_vision)    # ask_vision(image_bytes, prompt) -> str
        if outcome["is_veteran_upload"]:
            await message.channel.send(format_reply(outcome))
            # outcome["veterans"] are clean veteran dicts, ready for VeteranReader.to_build()
        else:
            ...  # not a veteran image: handle it like any other image

Needs VeteranReader.py in the same folder.
"""
from __future__ import annotations

import inspect
import json

from VeteranReader import (DIST_KEYS, PROMPT as _BASE_PROMPT, STAT_KEYS, STRAT_KEYS,
                           normalize_veteran)

DETECT_RULE = """First decide whether the image is the "Umamusume Details" screen of a finished veteran
(character name, the five stats, Track / Distance / Style aptitudes, a Skills list).
If it is NOT, reply with exactly {"is_veteran": false} and nothing else.
If it is, add "is_veteran": true to the object described below.
The skills list scrolls, so list only the skills you can actually see in THIS image.

"""
INTAKE_PROMPT = DETECT_RULE + _BASE_PROMPT


# --------------------------------------------------------------------------
# Reading the AI reply
# --------------------------------------------------------------------------
def extract_json(text) -> dict | None:
    """First JSON object in a reply, even if wrapped in ``` fences or chatter."""
    if not isinstance(text, str):
        return None
    start = text.find("{")
    while start != -1:
        depth, in_str, esc = 0, False, False
        for i in range(start, len(text)):
            ch = text[i]
            if in_str:
                if esc:
                    esc = False
                elif ch == "\\":
                    esc = True
                elif ch == '"':
                    in_str = False
            elif ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    try:
                        obj = json.loads(text[start:i + 1])
                        if isinstance(obj, dict):
                            return obj
                    except json.JSONDecodeError:
                        pass
                    break
        start = text.find("{", start + 1)
    return None


def parse_reply(text) -> dict:
    """Classify one AI reply. status is:
         "veteran"     a complete veteran was parsed (result["veteran"], result["warnings"])
         "unreadable"  it is a veteran screen but a stat could not be read (result["reason"])
         "not_veteran" anything else: not a veteran image, no JSON, or no stats at all"""
    obj = extract_json(text)
    if obj is None:
        return {"status": "not_veteran", "reason": "no JSON in the reply"}
    if obj.get("is_veteran") is False:
        return {"status": "not_veteran", "reason": "the AI said this is not a veteran screen"}
    stats = obj.get("stats")
    if not isinstance(stats, dict) or all(v is None for v in stats.values()):
        return {"status": "not_veteran", "reason": "no stats in the reply"}
    try:
        vet, warnings = normalize_veteran(obj)
    except ValueError as exc:
        return {"status": "unreadable", "reason": str(exc)}
    return {"status": "veteran", "veteran": vet, "warnings": warnings}


# --------------------------------------------------------------------------
# Several screenshots -> one veteran
# --------------------------------------------------------------------------
def merge_veterans(vets: list) -> tuple[list, list]:
    """Group screenshots of the same veteran (same name and same five stats) and combine them."""
    groups, order, warnings = {}, [], []
    for v in vets:
        key = (v.get("name"), tuple(v["stats"][k] for k in STAT_KEYS))
        if key not in groups:
            groups[key] = {"name": v.get("name"), "stats": dict(v["stats"]),
                           "aptitudes": {c: dict(d) for c, d in v["aptitudes"].items()},
                           "skills": list(v["skills"])}
            order.append(key)
            continue
        g = groups[key]
        seen = {s.lower() for s in g["skills"]}
        g["skills"] += [s for s in v["skills"] if s.lower() not in seen]
        for cat, d in v["aptitudes"].items():
            for k, letter in d.items():
                have = g["aptitudes"][cat].get(k)
                if have is None:
                    g["aptitudes"][cat][k] = letter
                elif letter is not None and letter != have:
                    warnings.append(f"{g['name'] or 'veteran'}: {cat}.{k} read as {have} and as {letter}; kept {have}")
    return [groups[k] for k in order], warnings


async def intake_images(images: list, ask) -> dict:
    """Run every image through `ask(image, INTAKE_PROMPT) -> str` (sync or async) and sort out the results.

    Returns {"is_veteran_upload": bool, "veterans": [...], "unreadable": [reason, ...],
             "not_veteran": int, "warnings": [...]}.
    is_veteran_upload is True when at least one image was a veteran screen, readable or not."""
    parsed = []
    for img in images:
        reply = ask(img, INTAKE_PROMPT)
        if inspect.isawaitable(reply):
            reply = await reply
        parsed.append(parse_reply(reply))
    found = [p["veteran"] for p in parsed if p["status"] == "veteran"]
    merged, warnings = merge_veterans(found)
    for p in parsed:
        if p["status"] == "veteran":
            warnings += p["warnings"]
    unreadable = [p["reason"] for p in parsed if p["status"] == "unreadable"]
    return {"is_veteran_upload": bool(found or unreadable), "veterans": merged, "unreadable": unreadable,
            "not_veteran": sum(1 for p in parsed if p["status"] == "not_veteran"),
            "warnings": list(dict.fromkeys(warnings))}


# --------------------------------------------------------------------------
# Discord message text
# --------------------------------------------------------------------------
def format_reply(outcome: dict) -> str:
    lines = []
    for v in outcome["veterans"]:
        s, a = v["stats"], v["aptitudes"]
        lines.append(f"**{v.get('name') or 'Veteran'}**  Speed {s['speed']} | Stamina {s['stamina']} | "
                     f"Power {s['power']} | Guts {s['guts']} | Wit {s['wisdom']}")
        lines.append("Track " + " ".join(f"{k.title()} {a['surface'].get(k) or '?'}" for k in ("turf", "dirt"))
                     + "  |  Distance " + " ".join(f"{k.title()} {a['distance'].get(k) or '?'}" for k in DIST_KEYS)
                     + "  |  Style " + " ".join(f"{k.title()} {a['strategy'].get(k) or '?'}" for k in STRAT_KEYS))
        lines.append(f"{len(v['skills'])} skills read.")
    if outcome["unreadable"]:
        lines.append("I could tell one image was a veteran screen but could not read it fully: "
                     + "; ".join(outcome["unreadable"]) + ". Could you send a clearer screenshot?")
    if outcome["warnings"]:
        lines.append("Check: " + "; ".join(outcome["warnings"]))
    return "\n".join(lines)
