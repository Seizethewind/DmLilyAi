#!/usr/bin/env python3
"""
VeteranReader -- turn a veteran (a trainee that finished its career) into a Simulator build.

The screenshot is read by the AI, not by this file. The AI turns the screenshot into a
small "veteran JSON" (see --prompt for the exact instructions to give it). This file then:

  1. checks that JSON (stats are numbers, aptitude letters are S..G, skills are present),
  2. picks the aptitudes that matter for the race (distance + turf/dirt + running style),
  3. checks every skill name against skills.json and swaps names for ids,
  4. returns a build that Simulator.py can run.

Veteran JSON (what the AI should produce)
-----------------------------------------
    {
      "name": "Oguri Cap",                                  # optional
      "stats": {"speed": 1200, "stamina": 900, "power": 1000, "guts": 450, "wisdom": 700},
      "aptitudes": {
        "distance": {"short": "C", "mile": "A", "medium": "A", "long": "B"},
        "surface":  {"turf": "A", "dirt": "B"},
        "strategy": {"front": "G", "pace": "A", "late": "A", "end": "C"}
      },
      "skills": ["Corner Recovery ○", "Straight Accel", "Professor of Curvature"]
    }
A value the AI cannot read must be null, never a guess.

Usage
-----
    python VeteranReader.py --prompt                         # text to give the AI with the screenshot
    python VeteranReader.py oguri.json                       # validate + print normalised veteran
    python VeteranReader.py oguri.json --course 10506 --style pace    # print a Simulator build
    python VeteranReader.py --expand config.json | python Simulator.py --config -

In a Simulator config, a build may point at a veteran instead of spelling everything out:
    "builds": {
      "A": {"veteran": "oguri.json", "style": "pace"},
      "B": {"veteran": "oguri.json", "style": "pace", "add_skills": ["Corner Accel ○"]}
    }
`--expand` (or expand_config() from Python) replaces those with real builds. "style" is optional;
without it the veteran's best strategy aptitude is used. "add_skills" is optional.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path

APT_LETTERS = "SABCDEFG"
STAT_KEYS = ("speed", "stamina", "power", "guts", "wisdom")
STAT_ALIASES = {"wit": "wisdom", "int": "wisdom", "intelligence": "wisdom", "stam": "stamina", "pow": "power"}
DIST_KEYS = ("short", "mile", "medium", "long")
DIST_ALIASES = {"mid": "medium", "middle": "medium"}
DIST_BY_TYPE = {1: "short", 2: "mile", 3: "medium", 4: "long"}   # Simulator courses.json distance_type
SURF_KEYS = ("turf", "dirt")
SURF_BY_ID = {1: "turf", 2: "dirt"}
STRAT_KEYS = ("front", "pace", "late", "end")
STRAT_ALIASES = {
    "nige": "front", "front": "front", "runner": "front", "front runner": "front",
    "senkou": "pace", "pace": "pace", "pace chaser": "pace",
    "sasi": "late", "sashi": "late", "late": "late", "late surger": "late",
    "oikomi": "end", "end": "end", "end closer": "end",
}

PROMPT = """You are reading a screenshot of a finished Uma Musume trainee (a veteran). Reply with ONE JSON
object and nothing else, in exactly this shape:

{
  "name": "<character name, or null>",
  "stats": {"speed": 0, "stamina": 0, "power": 0, "guts": 0, "wisdom": 0},
  "aptitudes": {
    "distance": {"short": "?", "mile": "?", "medium": "?", "long": "?"},
    "surface":  {"turf": "?", "dirt": "?"},
    "strategy": {"front": "?", "pace": "?", "late": "?", "end": "?"}
  },
  "skills": ["<skill name>", "..."]
}

Rules:
- Stats are the five whole numbers (Speed, Stamina, Power, Guts, Wisdom). Do not add or convert them.
- Aptitudes are single letters S, A, B, C, D, E, F or G. Front = Front Runner, Pace = Pace Chaser,
  Late = Late Surger, End = End Closer.
- List EVERY skill shown, including unique and inherited skills, copied exactly as written, with the
  circle symbols (○ and ◎) kept. One entry per skill.
- If something is cut off or unreadable, use null for it. Never guess.
- If the screenshot has several screens (stats, aptitudes, skills), combine them into the one object.
"""


# --------------------------------------------------------------------------
# Loading and checking the veteran JSON
# --------------------------------------------------------------------------
def _norm_key(text) -> str:
    return re.sub(r"\s+", " ", str(text).strip().lower())


def _letter(v, where: str, warnings: list):
    if v is None:
        return None
    s = str(v).strip().upper()
    if s in tuple(APT_LETTERS):
        return s
    warnings.append(f"{where}: '{v}' is not an aptitude letter (S..G); treated as unreadable")
    return None


def normalize_veteran(raw) -> tuple[dict, list]:
    """Check a veteran JSON (dict or path) and return (clean_veteran, warnings).
    Raises ValueError for problems that make the veteran unusable."""
    if isinstance(raw, (str, Path)):
        with open(raw, encoding="utf-8") as fh:
            raw = json.load(fh)
    if not isinstance(raw, dict):
        raise ValueError("veteran JSON must be an object")
    warnings: list = []

    # stats
    st_in = raw.get("stats")
    if not isinstance(st_in, dict):
        raise ValueError("veteran needs a 'stats' object")
    st = {}
    for k, v in st_in.items():
        k2 = STAT_ALIASES.get(_norm_key(k), _norm_key(k))
        if k2 in STAT_KEYS:
            st[k2] = v
    missing = [k for k in STAT_KEYS if st.get(k) is None]
    if missing:
        raise ValueError(f"stats missing or unreadable: {', '.join(missing)}")
    for k in STAT_KEYS:
        try:
            st[k] = int(float(str(st[k]).replace(",", "").strip()))
        except ValueError:
            raise ValueError(f"stat {k} = '{st[k]}' is not a number") from None
        if st[k] < 1:
            raise ValueError(f"stat {k} = {st[k]} is below 1; probably misread")
        if st[k] > 2000:
            warnings.append(f"stat {k} = {st[k]} is unusually high; check the screenshot reading")

    # aptitudes
    ap_in = raw.get("aptitudes") or {}
    apt = {"distance": {}, "surface": {}, "strategy": {}}
    for k, v in (ap_in.get("distance") or {}).items():
        k2 = DIST_ALIASES.get(_norm_key(k), _norm_key(k))
        if k2 in DIST_KEYS:
            apt["distance"][k2] = _letter(v, f"distance.{k2}", warnings)
    for k, v in (ap_in.get("surface") or {}).items():
        k2 = _norm_key(k)
        if k2 in SURF_KEYS:
            apt["surface"][k2] = _letter(v, f"surface.{k2}", warnings)
    for k, v in (ap_in.get("strategy") or {}).items():
        k2 = STRAT_ALIASES.get(_norm_key(k))
        if k2:
            apt["strategy"][k2] = _letter(v, f"strategy.{k2}", warnings)
    for cat, keys in (("distance", DIST_KEYS), ("surface", SURF_KEYS), ("strategy", STRAT_KEYS)):
        gone = [k for k in keys if apt[cat].get(k) is None]
        if gone:
            warnings.append(f"aptitudes.{cat} missing: {', '.join(gone)}")

    # skills
    skills, seen = [], set()
    for item in raw.get("skills") or []:
        if isinstance(item, dict):
            item = item.get("id") or item.get("name")
        if item is None or not str(item).strip():
            continue
        s = re.sub(r"\s+", " ", str(item).strip())
        if s.lower() not in seen:
            seen.add(s.lower())
            skills.append(s)
    if not skills:
        warnings.append("no skills listed")

    return {"name": raw.get("name"), "stats": st, "aptitudes": apt, "skills": skills}, warnings


# --------------------------------------------------------------------------
# Skills and courses (use Simulator's own data loader)
# --------------------------------------------------------------------------
def load_data(data_dir: str | None = None):
    """Simulator.Data, or None when Simulator.py / skills.json / courses.json cannot be found."""
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from Simulator import Data
        return Data.load(data_dir)
    except (ImportError, FileNotFoundError):
        return None


def resolve_skills(names: list, data, owner=None) -> tuple[list, list]:
    """Names (or ids) -> skill ids. Returns (ids, problems).
    Names may be the in-game (Global) name, the upstream English name, the Japanese name or an id; case, punctuation and
    the circle mark's spelling do not matter. `owner` is the veteran's name: it picks the character's own unique skill
    over its inherited copy. A name that does not resolve is reported with the closest matches, and a real skill the
    simulator cannot model is reported as that, not as unknown."""
    ids, problems = [], []
    for ref in names:
        try:
            found = data.resolve_skill(ref, owner=owner)
        except ValueError as exc:
            if exc.__class__.__name__ == "UnmodelledSkill":
                problems.append(f"skill '{ref}' is not simulated: its effect is not modelled (it acts on other runners "
                                f"or on the start), so it is left out")
                continue
            hints = data.suggest_skills(ref, 3) if hasattr(data, "suggest_skills") else []
            why = str(exc).split(". ")[0]
            problems.append(f"skill '{ref}' name not recognised ({why})"
                            + (f"; closest: {', '.join(hints)}" if hints else "")
                            + "; look it up with sim_find_skill and use its id")
            continue
        if found not in ids:
            ids.append(found)
    return ids, problems


def _course_info(course, data) -> dict:
    if isinstance(course, dict):
        return course
    if data is None:
        raise ValueError("cannot look up the course: Simulator.py or courses.json not found (use --data-dir)")
    cid = str(course)
    if cid not in data.courses:
        raise ValueError(f"Unknown course '{cid}'. Try Simulator.py --list-courses")
    return data.courses[cid]


# --------------------------------------------------------------------------
# Veteran -> Simulator build
# --------------------------------------------------------------------------
def best_style(vet: dict) -> str:
    ranked = [(APT_LETTERS.index(vet["aptitudes"]["strategy"][s]), i, s)
              for i, s in enumerate(STRAT_KEYS) if vet["aptitudes"]["strategy"].get(s)]
    if not ranked:
        raise ValueError("no strategy aptitudes readable; pass a style explicitly")
    return min(ranked)[2]


def to_build(veteran, course, style=None, add_skills=None, data=None, strict=False) -> tuple[dict, list]:
    """Build for Simulator.py. `course` is a course id (or a course dict), `style` any of
    front/pace/late/end (or nige/senkou/sasi/oikomi); default is the veteran's best style.
    Returns (build, warnings). With strict=True an unresolved skill raises instead of being skipped."""
    vet, warnings = normalize_veteran(veteran)
    if data is None:
        data = load_data()
    c = _course_info(course, data)
    dist = c.get("distance_type")
    dist_key = DIST_BY_TYPE.get(dist)
    if dist_key is None:                                           # fall back to the metres
        m = c["distance"]
        dist_key = "short" if m <= 1400 else "mile" if m <= 1800 else "medium" if m <= 2400 else "long"
    surf_key = SURF_BY_ID[c["surface"]]

    if style is None:
        style_key = best_style(vet)
    else:
        style_key = STRAT_ALIASES.get(_norm_key(style))
        if style_key is None:
            raise ValueError(f"Unknown running style '{style}' (front, pace, late, end)")
    letters = {"distance": vet["aptitudes"]["distance"].get(dist_key),
               "surface": vet["aptitudes"]["surface"].get(surf_key),
               "strategy": vet["aptitudes"]["strategy"].get(style_key)}
    for cat, label in (("distance", dist_key), ("surface", surf_key), ("strategy", style_key)):
        if letters[cat] is None:
            raise ValueError(f"aptitude for {cat} '{label}' is missing or unreadable; fix the veteran JSON")

    skills = list(vet["skills"]) + [s for s in (add_skills or [])]
    if data is not None:
        ids, problems = resolve_skills(skills, data, owner=vet["name"])
        if problems and strict:
            raise ValueError("; ".join(problems))
        warnings += problems
        skills = ids
    else:
        warnings.append("skills not checked: skills.json not found, names are passed through as written")

    build = {"_veteran": vet["name"], "stats": vet["stats"], "style": style_key,
             "aptitudes": letters, "skills": skills}
    return build, warnings


def expand_config(cfg: dict, data=None, base_dir=None, strict=False) -> tuple[dict, list]:
    """Replace every {"veteran": ...} build in a Simulator config by a real build."""
    cfg = copy.deepcopy(cfg)
    base = Path(base_dir) if base_dir else Path.cwd()
    if data is None:
        data = load_data()
    warnings: list = []
    for label, spec in cfg.get("builds", {}).items():
        if "veteran" not in spec:
            continue
        vet = spec["veteran"]
        if isinstance(vet, str):
            p = Path(vet)
            vet = p if p.is_absolute() else base / p
        build, w = to_build(vet, cfg["course"], spec.get("style"), spec.get("add_skills"), data, strict)
        warnings += [f"{label}: {x}" for x in w]
        cfg["builds"][label] = build
    return cfg, warnings


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Turn a veteran JSON into a Simulator build")
    ap.add_argument("veteran", nargs="?", help="veteran JSON file")
    ap.add_argument("--prompt", action="store_true", help="print the instructions to give the AI with the screenshot")
    ap.add_argument("--course", help="course id; prints a Simulator build instead of just checking")
    ap.add_argument("--style", help="front / pace / late / end (default: best aptitude)")
    ap.add_argument("--add-skill", action="append", default=[], metavar="SKILL")
    ap.add_argument("--expand", metavar="CONFIG", help="Simulator config with veteran builds ('-' = stdin); prints the expanded config")
    ap.add_argument("--strict", action="store_true", help="fail on a skill that cannot be resolved")
    ap.add_argument("--data-dir")
    args = ap.parse_args(argv)
    try:
        if args.prompt:
            print(PROMPT)
            return 0
        if args.expand:
            if args.expand == "-":
                cfg, base = json.load(sys.stdin), None
            else:
                with open(args.expand, encoding="utf-8") as fh:
                    cfg = json.load(fh)
                base = Path(args.expand).resolve().parent
            out, warns = expand_config(cfg, load_data(args.data_dir), base, args.strict)
            for w in warns:
                print(f"warning: {w}", file=sys.stderr)
            print(json.dumps(out, ensure_ascii=False, indent=2))
            return 0
        if not args.veteran:
            ap.error("give a veteran JSON file, or use --prompt / --expand")
        if args.course:
            result, warns = to_build(args.veteran, args.course, args.style, args.add_skill,
                                     load_data(args.data_dir), args.strict)
        else:
            result, warns = normalize_veteran(args.veteran)
        for w in warns:
            print(f"warning: {w}", file=sys.stderr)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (KeyError, ValueError, TypeError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
