#!/usr/bin/env python3
"""
Build the slim data files used by LilyAiGameSpace/Umamusume/Simulation/Simulator.py.

Source: alpha123/uma-skill-tools (GPL-3.0), data/ folder -- datamined skill and
course data that powers Umalator. The raw files are ~760 KB; we keep only what
the simulator needs and convert units (durations in seconds, modifiers in
m/s, m/s^2 or fraction of max HP).

Usage:
    python tools/build_sim_data.py                      # download from GitHub
    python tools/build_sim_data.py --source some/dir    # use local copies
    python tools/build_sim_data.py --dry-run            # print stats, write nothing

Outputs (default): tools/sim_data/{skills,courses}.json (outside the indexed docs folder)
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

UPSTREAM = "https://raw.githubusercontent.com/alpha123/uma-skill-tools/master/data/"
RAW_FILES = ("skill_data.json", "skillnames.json", "course_data.json", "tracknames.json")
DEFAULT_OUT = Path("tools/sim_data")

# Effect types the simulator understands (see RaceSolver.ts SkillType upstream):
#   1-5  stat up (speed, stamina, power, guts, wisdom)   9 HP recovery
#   21   current speed   22 current speed (natural decel)
#   27   target speed    31 acceleration
SUPPORTED_EFFECTS = {1, 2, 3, 4, 5, 9, 21, 22, 27, 31}
TARGET_SELF = 1
SCALE = 10000.0

MIN_SKILLS = 1000   # sanity checks so a bad download fails loudly
MIN_COURSES = 100


def load_raw(source: str | None) -> dict:
    data = {}
    for name in RAW_FILES:
        if source:
            text = (Path(source) / name).read_text(encoding="utf-8")
        else:
            req = urllib.request.Request(UPSTREAM + name, headers={"User-Agent": "DmLilyAi-sim-data/1.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                text = resp.read().decode("utf-8")
        data[name] = json.loads(text)
        print(f"loaded {name}: {len(data[name])} entries")
    return data


def slim_skills(skill_data: dict, names: dict) -> dict:
    out = {}
    for sid, skill in skill_data.items():
        alts, partial = [], False
        for alt in skill.get("alternatives", []):
            effects = []
            for e in alt.get("effects", []):
                if e["type"] in SUPPORTED_EFFECTS and e.get("target") == TARGET_SELF:
                    effects.append({"type": e["type"], "modifier": round(e["modifier"] / SCALE, 6)})
                else:
                    partial = True
            if not effects:
                partial = True
                continue
            alts.append({
                "duration": round(alt.get("baseDuration", 0) / SCALE, 6),
                "condition": alt.get("condition", ""),
                "precondition": alt.get("precondition", ""),
                "effects": effects,
            })
        if not alts:
            continue
        jp, en = (names.get(sid) or ["", ""])[:2] if isinstance(names.get(sid), list) else ("", "")
        entry = {
            "name": en or jp or sid,
            "rarity": skill.get("rarity", 1),
            "wisdom_check": bool(skill.get("wisdomCheck", 0)),
            "alternatives": alts,
        }
        if jp:
            entry["name_jp"] = jp
        if partial:
            entry["partial"] = True   # some effects/alternatives were dropped (other-runner or unsupported)
        out[sid] = entry
    return out


def slim_courses(course_data: dict, tracknames: dict) -> dict:
    out = {}
    for cid, c in course_data.items():
        track = tracknames.get(str(c.get("raceTrackId")), ["", ""])
        out[cid] = {
            "track_id": c["raceTrackId"],
            "track": (track[1] or track[0]) if track else "",
            "distance": c["distance"],
            "distance_type": c["distanceType"],   # 1 short, 2 mile, 3 mid, 4 long
            "surface": c["surface"],              # 1 turf, 2 dirt
            "turn": c["turn"],
            "course_set_status": c.get("courseSetStatus", []),
            "corners": [{"start": x["start"], "length": x["length"]} for x in c.get("corners", [])],
            "straights": [{"start": x["start"], "end": x["end"]} for x in c.get("straights", [])],
            "slopes": sorted(
                ({"start": x["start"], "length": x["length"], "slope": x["slope"]} for x in c.get("slopes", [])),
                key=lambda x: x["start"],
            ),
        }
    return out


def dump(path: Path, obj: dict) -> int:
    text = json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    path.write_text(text, encoding="utf-8")
    return len(text.encode("utf-8"))


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", help="folder holding local copies of the upstream data files")
    ap.add_argument("--out", default=str(DEFAULT_OUT), help="output folder")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    raw = load_raw(args.source)
    skills = slim_skills(raw["skill_data.json"], raw["skillnames.json"])
    courses = slim_courses(raw["course_data.json"], raw["tracknames.json"])
    partial = sum(1 for s in skills.values() if s.get("partial"))
    print(f"skills kept: {len(skills)} ({partial} partial)   courses kept: {len(courses)}")

    if len(skills) < MIN_SKILLS or len(courses) < MIN_COURSES:
        print("ERROR: far fewer skills/courses than expected - upstream format may have changed.", file=sys.stderr)
        return 1
    if args.dry_run:
        print("dry run: nothing written")
        return 0

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    print(f"wrote skills.json  ({dump(out / 'skills.json', skills):,} bytes)")
    print(f"wrote courses.json ({dump(out / 'courses.json', courses):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
