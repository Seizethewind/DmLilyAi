#!/usr/bin/env python3
"""
Uma Musume race simulator (v2) -- single-runner Monte Carlo time trials.

Compares two builds (A vs B) on a real course using the real skill data. Many
seeded races are run and finish-time statistics come out as JSON on stdout.

Model and data are a Python re-implementation of the approach used by
alpha123/uma-skill-tools (GPL-3.0): the physics (speed, acceleration, HP,
last spurt), the skill condition language and the datamined skill/course data
all come from that project. Keep that attribution if you share this file.

Data files (built by tools/build_sim_data.py, via the "Build simulator data"
workflow) are looked up in, in order: --data-dir, $SIM_DATA_DIR, ./data next to
this file, then tools/sim_data/ in any parent folder.

Usage
-----
    python Simulator.py                       # demo comparison
    python Simulator.py --config build.json   # your own ('-' = stdin)
    python Simulator.py --runs 2000 --seed 7 --workers 4
    python Simulator.py --find-skill "corner recovery"
    python Simulator.py --list-courses tokyo

Config (JSON)
-------------
    {
      "course": "10606",            # course id (see --list-courses)
      "ground": 1,                  # 1 good, 2 yielding, 3 soft, 4 heavy
      "mood": 2,                    # -2 .. 2
      "wisdom_checks": true,        # skills with a wit check can fail to activate
      "runs": 500, "seed": 1,
      "builds": {
        "A": {"stats": {"speed": 1200, "stamina": 800, "power": 1000,
                        "guts": 500, "wisdom": 600},
              "style": "pace",      # front/pace/late/end/runaway or 1-5
              "aptitudes": {"distance": "A", "surface": "A", "strategy": "A"},
              "skills": ["200352", "Sprinting Gear"]},   # ids or exact names
        "B": {...}
      }
    }

What is and is not modelled
---------------------------
Modelled: start dash, per-phase target speed and acceleration, stat and
aptitude adjustments, HP drain and exhaustion, last-spurt decision, uphill
penalties, section speed randomness (from wisdom), skill activation windows
(static, random-position and dynamic conditions), wisdom checks, skill
alternatives and preconditions, speed/acceleration/current-speed/recovery/stat
effects aimed at yourself.
NOT modelled (same limits as upstream): other runners (conditions about order,
gaps, blocking, overtaking are ASSUMED TRUE and the skill is reported as
approximate), position keep / pace down, rushing (kakari), downhill mode, lane
changes, skill cooldowns, scaling effects, effects that target other runners.
Skills that use a condition this file cannot evaluate are skipped and listed
under "warnings".
"""
from __future__ import annotations

import argparse
import difflib
import json
import math
import os
import random
import re
import statistics
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

DT = 1.0 / 15.0
MAX_SIM_SECONDS = 600.0

# --------------------------------------------------------------------------
# Constants (from upstream RaceSolver.ts / HpPolicy.ts / RaceSolverBuilder.ts)
# --------------------------------------------------------------------------
SPEED_STRAT_PHASE = {1: (1.0, 0.98, 0.962), 2: (0.978, 0.991, 0.975), 3: (0.938, 0.998, 0.994),
                     4: (0.931, 1.0, 1.0), 5: (1.063, 0.962, 0.95)}
ACCEL_STRAT_PHASE = {1: (1.0, 1.0, 0.996), 2: (0.985, 1.0, 0.996), 3: (0.975, 1.0, 1.0),
                     4: (0.945, 1.0, 0.997), 5: (1.17, 0.94, 0.956)}
DIST_APT_SPEED = (1.05, 1.0, 0.9, 0.8, 0.6, 0.4, 0.2, 0.1)
SURF_APT_ACCEL = (1.05, 1.0, 0.9, 0.8, 0.7, 0.5, 0.3, 0.1)
DIST_APT_ACCEL = (1.0, 1.0, 1.0, 1.0, 1.0, 0.6, 0.5, 0.4)
STRAT_APT_WISDOM = (1.1, 1.0, 0.85, 0.75, 0.6, 0.4, 0.2, 0.1)
PHASE_DECEL = (-1.2, -0.8, -1.0)
BASE_ACCEL = 0.0006
UPHILL_BASE_ACCEL = 0.0004
HP_STRATEGY = (0, 0.95, 0.89, 1.0, 0.995, 0.86)
HP_GROUND = {1: (0, 1.0, 1.0, 1.02, 1.02), 2: (0, 1.0, 1.0, 1.01, 1.02)}   # [surface][ground]
GROUND_SPEED_MOD = {1: (0, 0, 0, 0, -50), 2: (0, 0, 0, 0, -50)}
GROUND_POWER_MOD = {1: (0, 0, -50, -50, -50), 2: (0, -100, -50, -100, -100)}
START_DASH_ACCEL = 24.0

STYLE_NAMES = {"nige": 1, "front": 1, "runner": 1, "senkou": 2, "pace": 2, "sasi": 3, "sashi": 3,
               "late": 3, "oikomi": 4, "end": 4, "oonige": 5, "runaway": 5}
GROUND_NAMES = {"good": 1, "yielding": 2, "soft": 3, "heavy": 4}
SKILL_EFFECT_STAT = {1: "speed", 2: "stamina", 3: "power", 4: "guts", 5: "wisdom"}


# --------------------------------------------------------------------------
# Data loading
# --------------------------------------------------------------------------
def find_data_dir(explicit: str | None = None) -> Path:
    cands = []
    if explicit:
        cands.append(Path(explicit))
    if os.environ.get("SIM_DATA_DIR"):
        cands.append(Path(os.environ["SIM_DATA_DIR"]))
    here = Path(__file__).resolve().parent
    cands.append(here / "data")
    cands += [p / "tools" / "sim_data" for p in here.parents]
    for c in cands:
        if (c / "skills.json").is_file() and (c / "courses.json").is_file():
            return c
    raise FileNotFoundError(
        "skills.json / courses.json not found. Run the 'Build simulator data' workflow "
        "(tools/build_sim_data.py) or pass --data-dir.")


# Level marks on skill names. A vision model often reads the single circle as the letter "O".
_MARK_MAP = {"◎": "◎", "⊚": "◎", "◉": "◎", "⦾": "◎",
             "○": "○", "◯": "○", "〇": "○", "⚪": "○", "◦": "○", "⭘": "○",
             "×": "×", "✕": "×", "✖": "×", "╳": "×"}
_MARKS = "".join(sorted(set(_MARK_MAP.values())))


def skill_key(text) -> str:
    """Comparison key for a skill name: ignores case, spaces, punctuation and width, and unifies the level mark.
    'Victory Cheer!' -> 'victorycheer'; 'Corner Recovery O' and 'Corner Recovery ◯' -> 'cornerrecovery○'.
    The mark stays in the key, so 'X ◎' and 'X ○' remain different skills."""
    s = unicodedata.normalize("NFKC", str(text)).strip()
    s = "".join(_MARK_MAP.get(ch, ch) for ch in s)
    s = re.sub(r"\s+[Oo0]$", " ○", s)
    s = re.sub(r"\s+[xX]$", " ×", s)
    return "".join(ch for ch in s.lower() if ch.isalnum() or ch in _MARKS)


class UnmodelledSkill(ValueError):
    """A real skill whose effects the simulator does not model (for example a debuff on other runners)."""


class Data:
    """skills.json + courses.json, plus skill_aliases.json when present.

    skills.json carries the upstream (datamined) English names, which are often fan translations and differ from the
    names the game shows. skill_aliases.json maps the in-game (Global) names to the same skill ids, so a veteran read
    from a screenshot resolves. See tools/build_skill_aliases.py for how it is built and what its fields mean."""

    def __init__(self, skills: dict, courses: dict, aliases: dict | None = None):
        self.skills = skills
        self.courses = courses
        aliases = aliases if isinstance(aliases, dict) else {}
        self._alias_ids: dict[str, list] = {}      # skill_key(Global name) -> ids, preferred first
        self._display: dict[str, str] = {}         # id -> Global name
        for name, ids in (aliases.get("names") or {}).items():
            ids = [str(i) for i in ([ids] if isinstance(ids, (str, int)) else ids or [])]
            key = skill_key(name)
            if not key or not ids:
                continue
            merged = self._alias_ids.setdefault(key, [])
            merged += [i for i in ids if i not in merged]
            for i in ids:
                self._display.setdefault(i, str(name))
        self._unmodelled = {skill_key(n): str(i) for n, i in (aliases.get("unmodelled") or {}).items() if skill_key(n)}
        self._unique_owner = {str(i): skill_key(o) for i, o in (aliases.get("unique_owner") or {}).items() if skill_key(o)}
        self._upstream_keys: dict[str, list] | None = None
        self._suggest_pool: list | None = None

    @classmethod
    def load(cls, data_dir: str | None = None) -> "Data":
        d = find_data_dir(data_dir)
        with open(d / "skills.json", encoding="utf-8") as f:
            skills = json.load(f)
        with open(d / "courses.json", encoding="utf-8") as f:
            courses = json.load(f)
        aliases = None
        if (d / "skill_aliases.json").is_file():
            try:
                with open(d / "skill_aliases.json", encoding="utf-8") as f:
                    aliases = json.load(f)
            except (OSError, ValueError):
                aliases = None   # a damaged alias file costs the Global names, not the simulator
        return cls(skills, courses, aliases)

    # ----- skills ---------------------------------------------------------------
    def _upstream_index(self) -> dict:
        if self._upstream_keys is None:
            idx: dict[str, list] = {}
            for sid, s in self.skills.items():
                for text in (s["name"], s.get("name_jp", "")):
                    k = skill_key(text)
                    if k and sid not in idx.setdefault(k, []):
                        idx[k].append(sid)
            self._upstream_keys = idx
        return self._upstream_keys

    def _pick_by_owner(self, ids: list, owner) -> str:
        """Several ids share one Global name: the character's own unique skill and the weaker inherited copy.
        The owner gets the unique one; everyone else the inherited one."""
        okey = skill_key(owner) if owner else ""
        if okey:
            for i in ids:
                o = self._unique_owner.get(i)
                if o and o in okey:
                    return i
        for i in ids:
            if i not in self._unique_owner:
                return i
        return ids[0]

    def resolve_skill(self, ref, owner=None) -> str:
        """Skill id for an id, an in-game (Global) name, an upstream English name or a Japanese name.
        `owner` is the veteran's name; it decides between a unique skill and its inherited copy."""
        ref = str(ref).strip()
        if ref in self.skills:
            return ref
        key = skill_key(ref)
        usable = [i for i in self._alias_ids.get(key, []) if i in self.skills]
        if usable:
            return self._pick_by_owner(usable, owner)
        low = ref.lower()
        hits = [sid for sid, s in self.skills.items() if s["name"].lower() == low or s.get("name_jp") == ref]
        if not hits and key:
            hits = self._upstream_index().get(key, [])
        if len(hits) == 1:
            return hits[0]
        if len(hits) > 1:
            raise ValueError(f"Skill name '{ref}' is ambiguous; use an id: {', '.join(sorted(hits))}")
        if key in self._unmodelled or key in self._alias_ids:
            raise UnmodelledSkill(f"'{ref}' is a real skill but the simulator does not model its effect")
        raise ValueError(f"Unknown skill '{ref}'. Try --find-skill \"{ref}\"")

    def find_skills(self, text: str, limit: int = 25) -> list:
        low, qkey = text.lower(), skill_key(text)
        out = []
        for sid, s in self.skills.items():
            g = self._display.get(sid, "")
            if (low in s["name"].lower() or text in s.get("name_jp", "")
                    or (g and (low in g.lower() or (qkey and qkey in skill_key(g))))):
                out.append({"id": sid, "name": s["name"], "name_jp": s.get("name_jp", ""), "rarity": s["rarity"],
                            "partial": bool(s.get("partial")), "global": g})
        return sorted(out, key=lambda x: x["id"])[:limit]

    def display_name(self, sid: str) -> str:
        """The name the game shows when known, otherwise the upstream name."""
        return self._display.get(sid) or self.skills[sid]["name"]

    def suggest_skills(self, ref, limit: int = 3) -> list:
        """Closest skills to a name that did not resolve, as 'id name' strings (any of the three name kinds)."""
        key = skill_key(ref)
        if not key:
            return []
        if self._suggest_pool is None:
            pool: dict[str, list] = {}
            for sid, s in self.skills.items():
                label = f"{sid} {self._display.get(sid) or s['name']}"
                for text in (s["name"], s.get("name_jp", ""), self._display.get(sid, "")):
                    k = skill_key(text)
                    if k:
                        pool.setdefault(k, []).append((sid, label))
            self._suggest_pool = pool
        out, seen = [], set()
        for k in difflib.get_close_matches(key, list(self._suggest_pool), n=limit * 3, cutoff=0.6):
            for sid, label in self._suggest_pool[k]:
                if sid not in seen:
                    seen.add(sid)
                    out.append(label)
        return out[:limit]

    def list_courses(self, text: str = "") -> list:
        low = text.lower()
        rows = []
        for cid, c in self.courses.items():
            label = f"{c['track']} {c['distance']}m {'turf' if c['surface'] == 1 else 'dirt'}"
            if not low or low in label.lower() or low == cid:
                rows.append({"id": cid, "course": label})
        return sorted(rows, key=lambda r: (r["course"], r["id"]))


# --------------------------------------------------------------------------
# Parsing helpers
# --------------------------------------------------------------------------
def parse_style(v) -> int:
    if isinstance(v, int) and 1 <= v <= 5:
        return v
    key = str(v).strip().lower()
    if key.isdigit() and 1 <= int(key) <= 5:
        return int(key)
    if key in STYLE_NAMES:
        return STYLE_NAMES[key]
    raise ValueError(f"Unknown running style '{v}'")


def parse_apt(v) -> int:
    if isinstance(v, int) and 0 <= v <= 7:
        return v
    key = str(v).strip().upper()
    if len(key) == 1 and key in "SABCDEFG":
        return "SABCDEFG".index(key)
    raise ValueError(f"Unknown aptitude '{v}' (use S, A, B ... G)")


def parse_ground(v) -> int:
    if isinstance(v, int) and 1 <= v <= 4:
        return v
    key = str(v).strip().lower()
    if key in GROUND_NAMES:
        return GROUND_NAMES[key]
    if key.isdigit() and 1 <= int(key) <= 4:
        return int(key)
    raise ValueError(f"Unknown ground condition '{v}'")


def overcap(stat: float) -> float:
    return stat if stat <= 1200 else 1200 + math.floor((stat - 1200) / 2)


@dataclass
class Horse:
    speed: float
    stamina: float
    power: float
    guts: float
    wisdom: float
    strategy: int
    dist_apt: int
    surf_apt: int
    strat_apt: int


def base_horse(spec: dict, mood: int) -> Horse:
    st = spec["stats"]
    coef = 1 + 0.02 * mood
    apt = spec.get("aptitudes", {})
    wis = st.get("wisdom", st.get("wit"))
    if wis is None:
        raise ValueError("stats needs 'wisdom' (or 'wit')")
    return Horse(
        speed=overcap(st["speed"]) * coef, stamina=overcap(st["stamina"]) * coef,
        power=overcap(st["power"]) * coef, guts=overcap(st["guts"]) * coef,
        wisdom=overcap(wis) * coef,
        strategy=parse_style(spec.get("style", "pace")),
        dist_apt=parse_apt(apt.get("distance", "A")), surf_apt=parse_apt(apt.get("surface", "A")),
        strat_apt=parse_apt(apt.get("strategy", "A")))


def adjusted_horse(b: Horse, course: dict, ground: int) -> Horse:
    vals = [0, b.speed, b.stamina, b.power, b.guts, b.wisdom]
    vals = [min(x, 901) for x in vals]
    cs = course.get("course_set_status", [])
    mod = 1 + (sum((1 + math.floor(vals[s] / 300.01)) * 0.05 for s in cs) / max(len(cs), 1) if cs else 0)
    surf = course["surface"]
    return Horse(
        speed=max(b.speed * mod + GROUND_SPEED_MOD[surf][ground], 1), stamina=b.stamina,
        power=max(b.power + GROUND_POWER_MOD[surf][ground], 1), guts=b.guts,
        wisdom=b.wisdom * STRAT_APT_WISDOM[b.strat_apt],
        strategy=b.strategy, dist_apt=b.dist_apt, surf_apt=b.surf_apt, strat_apt=b.strat_apt)


# --------------------------------------------------------------------------
# Skill condition engine
#
# A condition is  term @ term @ ...  where each term is  atom & atom & ...
# (no parentheses; & binds tighter than @). Each atom compiles to one of:
#   static    -> True/False, decided before the race
#   region    -> list of (start, end) metre intervals, optionally "random"
#   dyn       -> predicate evaluated on the live race state every tick
#   opponent  -> depends on other runners: assumed true, skill flagged approx
# --------------------------------------------------------------------------
OPS = {"==": lambda a, b: a == b, "!=": lambda a, b: a != b, "<": lambda a, b: a < b,
       "<=": lambda a, b: a <= b, ">": lambda a, b: a > b, ">=": lambda a, b: a >= b}

OPPONENT_PREFIXES = (
    "order", "change_order", "bashin_diff", "overtake", "is_overtake", "blocked", "near_count",
    "distance_diff", "infront_near", "behind_near", "is_behind", "is_move_lane", "lane_type",
    "compete", "is_surrounded", "visiblehorse", "same_skill_horse", "running_style_count",
    "running_style_temptation", "is_hp_empty_onetime_other", "personal_space", "mate_",
)


def norm_iv(iv):
    iv = sorted((a, b) for a, b in iv if b - a > 1e-9)
    out = []
    for a, b in iv:
        if out and a <= out[-1][1] + 1e-9:
            out[-1] = (out[-1][0], max(out[-1][1], b))
        else:
            out.append((a, b))
    return out


def inter_iv(A, B):
    out, i, j = [], 0, 0
    while i < len(A) and j < len(B):
        lo, hi = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
        if hi - lo > 1e-9:
            out.append((lo, hi))
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return out


def comp_iv(A, d):
    out, cur = [], 0.0
    for a, b in A:
        if a > cur:
            out.append((cur, a))
        cur = max(cur, b)
    if cur < d:
        out.append((cur, d))
    return out


class Env:
    """Everything a condition can ask about, fixed for one (course, build)."""

    def __init__(self, course: dict, base: Horse, adj: Horse, ground: int, mood: int, params: dict):
        self.course, self.base, self.adj = course, base, adj
        self.d = float(course["distance"])
        self.ground, self.mood, self.params = ground, mood, params
        d = self.d
        self.ph_start = (0.0, d / 6, d * 2 / 3, d * 5 / 6)
        self.ph_end = (d / 6, d * 2 / 3, d * 5 / 6, d)
        self.corners = norm_iv([(c["start"], c["start"] + c["length"]) for c in course["corners"]])
        self.straights = norm_iv([(s["start"], s["end"]) for s in course["straights"]])
        self.slopes = sorted((s["start"], s["start"] + s["length"], s["slope"]) for s in course["slopes"])

    # ----- region category maps ------------------------------------------------
    def phase_cats(self, frac_lo=0.0, frac_hi=1.0):
        return {p: [(self.ph_start[p] + (self.ph_end[p] - self.ph_start[p]) * frac_lo,
                     self.ph_start[p] + (self.ph_end[p] - self.ph_start[p]) * frac_hi)] for p in range(4)}

    def corner_cats(self):
        raw = [(c["start"], c["start"] + c["length"]) for c in self.course["corners"]]
        raw.sort()
        n = len(raw)
        cats = {0: comp_iv(self.corners, self.d)}
        for num in range(1, 5):
            idx, regs = n + num - 5, []
            while idx >= 0:
                regs.append(raw[idx])
                idx -= 4
            cats[num] = norm_iv(regs)
        return cats

    def slope_cats(self):
        up = norm_iv([(a, b) for a, b, s in self.slopes if s > 0])
        down = norm_iv([(a, b) for a, b, s in self.slopes if s < 0])
        return {0: comp_iv(norm_iv(up + down), self.d), 1: up, 2: down}


def cat_region(cats: dict, op: str, val: int):
    fn = OPS[op]
    out = []
    for c, iv in cats.items():
        if fn(c, val):
            out += iv
    return norm_iv(out)


def compile_atom(key: str, op: str, val: int, env: Env):
    """Returns ('static', bool) | ('region', intervals, random) | ('dyn', fn) |
    ('opponent', random) | ('unsupported',)"""
    cmp_ = OPS[op]
    d, course, p = env.d, env.course, env.params
    cs = course

    def reg(iv, rnd=False):
        return ("region", norm_iv(iv), rnd)

    # ---- static facts ---------------------------------------------------------
    static_vals = {
        "distance_type": cs["distance_type"], "ground_type": cs["surface"], "ground_condition": env.ground,
        "track_id": cs["track_id"], "course_distance": cs["distance"], "rotation": cs["turn"],
        "is_basis_distance": 1 if cs["distance"] % 400 else 0, "motivation": env.mood + 3,
        "season": p["season"], "weather": p["weather"], "time": p["time"], "grade": p["grade"],
        "popularity": p["popularity"], "is_dirtgrade": 0, "always": 1,
        "base_speed": env.base.speed, "base_stamina": env.base.stamina, "base_power": env.base.power,
        "base_guts": env.base.guts, "base_wiz": env.base.wisdom,
        "temptation_count": 0, "is_badstart": 0,
    }
    if key in static_vals:
        return ("static", cmp_(static_vals[key], val))
    if key == "running_style":
        s = env.base.strategy
        return ("static", cmp_(1 if s == 5 else s, 1 if val == 5 else val))   # runaway counts as front

    # ---- geometry -----------------------------------------------------------
    if key == "phase":
        return reg(cat_region(env.phase_cats(), op, val))
    if key == "phase_firsthalf":
        return reg(cat_region(env.phase_cats(0, 0.5), op, val))
    if key == "phase_laterhalf":
        return reg(cat_region(env.phase_cats(0.5, 1), op, val))
    if key == "phase_firstquarter":
        return reg(cat_region(env.phase_cats(0, 0.25), op, val))
    if key == "phase_random":
        return reg(cat_region(env.phase_cats(), op, val), True)
    if key == "phase_firsthalf_random":
        return reg(cat_region(env.phase_cats(0, 0.5), op, val), True)
    if key == "phase_laterhalf_random":
        return reg(cat_region(env.phase_cats(0.5, 1), op, val), True)
    if key == "phase_firstquarter_random":
        return reg(cat_region(env.phase_cats(0, 0.25), op, val), True)
    if key == "distance_rate":
        x = d * val / 100.0
        if op in ("<=", "<"):
            return reg([(0, x)])
        if op in (">=", ">"):
            return reg([(x, d)])
        return reg([(x, x + 1)]) if op == "==" else ("unsupported",)
    if key == "distance_rate_after_random":
        return reg([(d * val / 100.0, d)], True) if op == "==" else ("unsupported",)
    if key == "remain_distance":
        x = d - val
        if op == "==":
            return reg([(x, x + 1)])
        if op in ("<=", "<"):
            return reg([(x, d)])
        if op in (">=", ">"):
            return reg([(0, x)])
        return ("unsupported",)
    if key == "corner":
        return reg(cat_region(env.corner_cats(), op, val))
    if key == "corner_random":
        cats = env.corner_cats()
        cats.pop(0, None)
        return reg(cat_region(cats, op, val), True)
    if key == "all_corner_random":
        return reg(env.corners, True) if (op == "==" and val == 1) else ("unsupported",)
    if key in ("is_finalcorner", "is_finalcorner_random", "is_finalcorner_laterhalf"):
        if not env.corners:
            return reg([])
        raw = sorted((c["start"], c["start"] + c["length"]) for c in course["corners"])
        fa, fb = raw[-1]
        if key == "is_finalcorner":
            return reg(cat_region({1: [(fa, d)], 0: [(0, fa)]}, op, val))
        if op != "==" or val != 1:
            return ("unsupported",)
        if key == "is_finalcorner_random":
            return reg([(fa, fb)], True)
        return reg([((fa + fb) / 2, fb)])
    if key in ("is_last_straight", "is_last_straight_onetime"):
        if not env.straights or op != "==" or val != 1:
            return reg([]) if op == "==" and val == 1 else ("unsupported",)
        a, b = sorted((s["start"], s["end"]) for s in course["straights"])[-1]
        return reg([(a, b)] if key == "is_last_straight" else [(a, a + 10)])
    if key == "straight_random":
        return reg(env.straights, True) if (op == "==" and val == 1) else ("unsupported",)
    if key in ("phase_corner_random", "phase_straight_random"):
        base_iv = env.corners if key == "phase_corner_random" else env.straights
        return reg(inter_iv(base_iv, cat_region(env.phase_cats(), op, val)), True)
    if key == "slope":
        return reg(cat_region(env.slope_cats(), op, val))
    if key in ("up_slope_random", "down_slope_random"):
        cats = env.slope_cats()
        return reg(cats[1 if key == "up_slope_random" else 2], True) if (op == "==" and val == 1) else ("unsupported",)

    # ---- dynamic ------------------------------------------------------------
    if key == "is_lastspurt":
        return ("region_dyn", [(env.ph_start[2], d)], (lambda s, v=val: int(s.is_last_spurt) == v) if op == "==" else None)
    if key == "lastspurt":
        fns = {1: lambda s: s.is_last_spurt and s.lst != -1, 2: lambda s: s.is_last_spurt and s.lst == -1,
               3: lambda s: not s.is_last_spurt}
        if op != "==" or val not in fns:
            return ("unsupported",)
        return ("region_dyn", [(env.ph_start[2], d)], fns[val])
    if key == "accumulatetime":
        return ("dyn", lambda s, o=cmp_, v=val: o(s.t, v))
    if key == "hp_per":
        return ("dyn", lambda s, o=cmp_, v=val: o(100.0 * max(0.0, s.hp) / s.max_hp, v))
    if key == "activate_count_all":
        return ("dyn", lambda s, o=cmp_, v=val: o(sum(s.counts), v))
    if key == "activate_count_start":
        return ("dyn", lambda s, o=cmp_, v=val: o(s.counts[0], v))
    if key == "activate_count_middle":
        return ("dyn", lambda s, o=cmp_, v=val: o(s.counts[1], v))
    if key == "activate_count_end_after":
        return ("dyn", lambda s, o=cmp_, v=val: o(s.counts[2], v))
    if key == "activate_count_heal":
        return ("dyn", lambda s, o=cmp_, v=val: o(s.heal_count, v))
    if key == "is_used_skill_id":
        return ("dyn", lambda s, o=cmp_, v=str(val): o(int(v in s.used), 1))

    if key.startswith(OPPONENT_PREFIXES):
        # Conditions about other runners (order, overtakes, blocking, gaps...) are assumed satisfied
        # as soon as the rest of the condition is. The flag is a hook for sampling them randomly
        # instead; upstream uses per-condition distributions, which this port does not copy yet.
        return ("opponent", False)
    return ("unsupported",)


@dataclass
class Term:
    intervals: list
    random: bool
    dyn: list
    approx: bool


def compile_expr(expr: str, env: Env):
    """Returns (terms, approx, unsupported_key). terms may be empty (can't fire here)."""
    expr = (expr or "").strip()
    if not expr:
        return [Term([(0.0, env.d)], False, [], False)], False, None
    terms, approx_any = [], False
    for or_part in expr.split("@"):
        iv, rnd, dyn, approx, dead = [(0.0, env.d)], False, [], False, False
        for tok in or_part.split("&"):
            tok = tok.strip()
            m = _ATOM_RE.match(tok)
            if not m:
                return [], False, tok
            key, op, val = m.group(1), m.group(2), int(m.group(3))
            r = compile_atom(key, op, val, env)
            kind = r[0]
            if kind == "unsupported":
                return [], False, key
            if kind == "static":
                dead = dead or not r[1]
            elif kind == "region":
                iv = inter_iv(iv, r[1])
                rnd = rnd or r[2]
            elif kind == "region_dyn":
                iv = inter_iv(iv, r[1])
                if r[2] is None:
                    return [], False, key
                dyn.append(r[2])
            elif kind == "dyn":
                dyn.append(r[1])
            elif kind == "opponent":
                approx = True
                rnd = rnd or r[1]
        if approx:
            approx_any = True
        if not dead and iv:
            terms.append(Term(iv, rnd, dyn, approx))
    return terms, approx_any, None


_ATOM_RE = re.compile(r"^([a-z_0-9]+)(==|!=|<=|>=|<|>)(-?\d+)$")


@dataclass
class CompiledAlt:
    effects: list          # [(type, modifier)]
    duration: float        # seconds, already scaled by course distance
    terms: list
    pre_terms: list


@dataclass
class CompiledSkill:
    sid: str
    name: str
    wisdom_check: bool
    alts: list = field(default_factory=list)
    status: str = "ok"      # ok | approx | unsupported | inactive
    reason: str = ""
    partial: bool = False


def compile_skill(sid: str, skill: dict, env: Env) -> CompiledSkill:
    cs = CompiledSkill(sid, skill["name"], bool(skill.get("wisdom_check")), partial=bool(skill.get("partial")))
    approx = False
    for alt in skill["alternatives"]:
        terms, ap1, bad = compile_expr(alt["condition"], env)
        if bad:
            cs.status, cs.reason = "unsupported", bad
            return cs
        pre, ap2, bad = compile_expr(alt.get("precondition", ""), env)
        if bad:
            cs.status, cs.reason = "unsupported", bad
            return cs
        approx = approx or ap1 or ap2
        if not terms or (alt.get("precondition") and not pre):
            continue
        cs.alts.append(CompiledAlt(
            effects=[(e["type"], e["modifier"]) for e in alt["effects"]],
            duration=alt["duration"] * env.d / 1000.0, terms=terms, pre_terms=pre))
    if not cs.alts:
        cs.status = "inactive"
    elif approx:
        cs.status = "approx"
    return cs


# --------------------------------------------------------------------------
# Race simulation
# --------------------------------------------------------------------------
class State:
    __slots__ = ("pos", "t", "hp", "max_hp", "is_last_spurt", "lst", "counts", "heal_count", "used")

    def __init__(self):
        self.pos = 0.0
        self.t = 0.0
        self.hp = 1.0
        self.max_hp = 1.0
        self.is_last_spurt = False
        self.lst = -1.0
        self.counts = [0, 0, 0]
        self.heal_count = 0
        self.used = set()


class AltRun:
    __slots__ = ("alt", "skill", "latched", "pre")

    def __init__(self, alt, skill):
        self.alt, self.skill, self.latched, self.pre = alt, skill, not alt.pre_terms, []


class SkillRun:
    __slots__ = ("cs", "done")

    def __init__(self, cs):
        self.cs, self.done = cs, False


@dataclass
class RaceResult:
    finish_time: float
    hp_left: float
    ran_out_of_hp: bool
    activations: dict   # skill id -> position (m) of first activation
    final_speed: float = 0.0
    final_pos: float = 0.0


def _sample_entries(terms, rng, owner):
    """Turn compiled terms into concrete trigger windows [a, b) for one race."""
    out = []
    for t in terms:
        if t.random:
            total = sum(b - a for a, b in t.intervals)
            if total <= 0:
                continue
            x = rng.random() * total
            for a, b in t.intervals:
                if x < b - a:
                    out.append((a + x, b, t.dyn, owner))
                    break
                x -= b - a
        else:
            for a, b in t.intervals:
                out.append((a, b, t.dyn, owner))
    return out


class Race:
    def __init__(self, env: Env, compiled: list, rng: random.Random):
        self.env, self.rng = env, rng
        self.course = env.course
        self.d = env.d
        self.S = State()
        self.compiled = compiled
        self.h = Horse(**vars(env.adj))   # mutable copy: green skills edit it
        self.base = 20.0 - (self.d - 2000.0) / 1000.0
        self.trace = None   # set to a list to record position every tick

    # ----- HP -----------------------------------------------------------------
    def hp_rate(self, phase, v):
        g = self.guts_mod if phase >= 2 else 1.0
        return 20.0 * (v - self.base + 12.0) ** 2 / 144.0 * self.ground_hp * g

    def last_spurt_pair(self, max_speed, base_target2):
        d, S = self.d, self.S
        s = (d - d * 2 / 3 - 60.0) / max_speed
        if S.hp >= self.hp_rate(2, max_speed) * s:
            return -1.0, max_speed
        remain = d - 60.0 - S.pos
        cands = []
        speed = max_speed - 0.1
        hp_base = self.hp_rate(2, base_target2)
        while speed >= base_target2:
            denom = base_target2 * self.hp_rate(2, speed) - hp_base * speed
            num = base_target2 * S.hp - hp_base * remain
            if denom == 0:
                dur_hp = remain / speed if num > 0 else 0.0
            else:
                dur_hp = max(0.0, num / denom)
            dur = min(remain / speed, dur_hp)
            cands.append((d - (dur * speed + 60.0), speed))
            speed -= 0.1
        if not cands:
            return d, max_speed
        cands.sort(key=lambda c: (c[0] - S.pos) / base_target2 + (d - c[0]) / c[1])
        for c in cands:
            if self.rng.randrange(100000) <= self.subpar:
                return c
        return cands[-1]

    # ----- skills -------------------------------------------------------------
    def _setup_skills(self):
        rng, h = self.rng, self.h
        wis_chance = max(1 - 90.0 / h.wisdom, 0.2)
        self.live = []
        for cs in self.compiled:
            if cs.status not in ("ok", "approx"):
                continue
            if cs.wisdom_check and self.env.wisdom_checks and rng.random() >= wis_chance:
                continue
            sr = SkillRun(cs)
            for alt in cs.alts:
                ar = AltRun(alt, sr)
                ar.pre = _sample_entries(alt.pre_terms, rng, ar)
                self.live += _sample_entries(alt.terms, rng, ar)

    def _expire(self, t):
        if not self.active:
            return
        keep = []
        for end, typ, mod in self.active:
            if t >= end - 1e-9:
                if typ == 22:
                    self.one_frame_accel += mod
            else:
                keep.append((end, typ, mod))
        if len(keep) != len(self.active):
            self.active = keep
            self.target_mod = sum(m for _, ty, m in keep if ty == 27)
            self.accel_mod = sum(m for _, ty, m in keep if ty == 31)
            self.cur_mod = sum(m for _, ty, m in keep if ty in (21, 22))

    def _activations(self):
        S, live = self.S, self.live
        if not live:
            return
        pos = S.pos
        for e in live[:]:
            a, b, dyn, ar = e
            if ar.skill.done or pos >= b:
                live.remove(e)
                continue
            if pos < a:
                continue
            if not ar.latched:
                for pa, pb, pdyn, _ in ar.pre:
                    if pa <= pos < pb and all(f(S) for f in pdyn):
                        ar.latched = True
                        break
                if not ar.latched:
                    continue
            if all(f(S) for f in dyn):
                live.remove(e)
                self._fire(ar)

    def _fire(self, ar):
        S, h = self.S, self.h
        ar.skill.done = True
        t = S.t
        for typ, mod in ar.alt.effects:
            if typ in SKILL_EFFECT_STAT:
                name = SKILL_EFFECT_STAT[typ]
                setattr(h, name, max(getattr(h, name) + mod, 1))
            elif typ == 9:
                S.heal_count += 1
                S.hp = min(S.max_hp, S.hp + S.max_hp * mod)
                if self.phase >= 2 and not S.is_last_spurt and self.started:
                    S.lst, self.lst_ready = -1.0, False
                    self._update_last_spurt()
            elif typ in (27, 31, 21, 22):
                self.active.append((t + ar.alt.duration, typ, mod))
                if typ == 27:
                    self.target_mod += mod
                elif typ == 31:
                    self.accel_mod += mod
                else:
                    self.cur_mod += mod
        S.counts[min(self.phase, 2)] += 1
        S.used.add(ar.skill.cs.sid)
        self.activated.setdefault(ar.skill.cs.sid, S.pos)

    # ----- per-tick pieces ----------------------------------------------------
    def _update_last_spurt(self):
        S = self.S
        if S.is_last_spurt or self.phase < 2:
            return
        if not self.lst_ready:
            S.lst, self.last_spurt_speed = self.last_spurt_pair(self.last_spurt_speed, self.base_target[2])
            self.lst_ready = True
        if S.pos >= S.lst:
            S.is_last_spurt = True

    def _target_speed(self):
        S, h = self.S, self.h
        if S.hp <= 0:
            target = self.min_speed
        elif S.is_last_spurt:
            target = self.last_spurt_speed
        else:
            target = self.base_target[self.phase]
            target += self.section_mod[min(int(S.pos / self.section_len), 24)]
        target += self.target_mod
        if self.slope > 0:
            target -= self.slope / 10000.0 * 200.0 / h.power
            target = max(target, self.min_speed)
        return target

    def run(self) -> RaceResult:
        env, S, h, rng = self.env, self.S, self.h, self.rng
        d, base = self.d, self.base
        self.phase, self.started = 0, False
        self.active, self.target_mod, self.accel_mod, self.cur_mod = [], 0.0, 0.0, 0.0
        self.one_frame_accel = 0.0
        self.activated = {}
        self.slope = 0.0
        self.section_len = d / 24.0
        tr = self.trace
        if tr is not None:
            tr.append(0.0)
        start_delay = 0.1 * rng.random()
        self._setup_skills()

        # gate: first round of activations happens before HP/derived values exist
        v = 3.0
        self._expire(0.0)
        self._activations()
        self.min_speed = 0.85 * base + math.sqrt(200.0 * h.guts) * 0.001
        # derived values (after greens)
        surf = self.course["surface"]
        self.ground_hp = HP_GROUND[surf][env.ground]
        S.max_hp = 0.8 * HP_STRATEGY[h.strategy] * h.stamina + d
        S.hp = S.max_hp
        self.guts_mod = 1.0 + 200.0 / math.sqrt(600.0 * h.guts)
        self.subpar = round((15.0 + 0.05 * h.wisdom) * 1000)
        dprof = DIST_APT_SPEED[h.dist_apt]
        self.base_target = [base * SPEED_STRAT_PHASE[h.strategy][p] + (p == 2) * math.sqrt(500.0 * h.speed) * dprof * 0.002
                            for p in range(3)]
        self.last_spurt_speed = ((self.base_target[2] + 0.01 * base) * 1.05
                                 + math.sqrt(500.0 * h.speed) * dprof * 0.002
                                 + (450.0 * h.guts) ** 0.597 * 0.0001)
        self.lst_ready = False
        mx = h.wisdom / 5500.0 * math.log10(h.wisdom * 0.1)
        self.section_mod = [base * ((mx - 0.65 + rng.random() * 0.65) / 100.0) for _ in range(24)] + [0.0]
        aprof = SURF_APT_ACCEL[h.surf_apt] * DIST_APT_ACCEL[h.dist_apt]
        base_accel = [(UPHILL_BASE_ACCEL if up else BASE_ACCEL) * math.sqrt(500.0 * h.power)
                      * ACCEL_STRAT_PHASE[h.strategy][p] * aprof for up in (0, 1) for p in range(3)]
        self.started = True

        slopes, next_slope, cur_slope = env.slopes, 0, None
        next_phase_pos = d / 6.0
        pos = S.pos = 0.0
        target = 0.85 * base
        start_dash = True
        accel_mod_dash = START_DASH_ACCEL
        accel = 0.0
        t = 0.0
        ran_out = False
        phase_end_pos = (d / 6.0, d * 2.0 / 3.0)

        while pos < d and t < MAX_SIM_SECONDS:
            # max speed rule
            if start_dash:
                max_v = min(target, 0.85 * base)
            elif v + self.one_frame_accel > target:
                max_v = 9999.0
            else:
                max_v = target
            halfv = min(v + 0.5 * DT * accel, max_v)
            pos += (halfv + self.cur_mod) * DT
            S.hp -= self.hp_rate(self.phase, v) * DT
            t += DT
            S.pos, S.t = pos, t
            if tr is not None:
                tr.append(pos)
            if S.hp <= 0:
                ran_out = True
            # hills
            if cur_slope is None:
                if next_slope < len(slopes) and pos >= slopes[next_slope][0]:
                    cur_slope = slopes[next_slope]
                    self.slope = cur_slope[2]
                    next_slope += 1
            elif pos > cur_slope[1]:
                cur_slope, self.slope = None, 0.0
            # phase
            if self.phase < 2 and pos >= next_phase_pos:
                self.phase += 1
                next_phase_pos = phase_end_pos[1] if self.phase == 1 else d
            self._expire(t)
            self._activations()
            self._update_last_spurt()
            target = self._target_speed()
            # forces
            if S.hp <= 0:
                accel = -1.2
            elif v > target:
                accel = PHASE_DECEL[self.phase]
            else:
                accel = base_accel[(3 if self.slope > 0 else 0) + self.phase] + self.accel_mod + accel_mod_dash
            if start_dash:
                max_v2 = min(target, 0.85 * base)
            elif v + self.one_frame_accel > target:
                max_v2 = 9999.0
            else:
                max_v2 = target
            v = min(halfv + 0.5 * DT * accel + self.one_frame_accel, max_v2)
            self.one_frame_accel = 0.0
            if not start_dash and v < self.min_speed:
                v = self.min_speed
            elif start_dash and v >= 0.85 * base:
                start_dash, accel_mod_dash = False, 0.0

        final_pos = pos
        if pos > d and v > 0:
            t -= (pos - d) / max(v, 0.1)
        return RaceResult(t + start_delay, max(S.hp, 0.0), ran_out, self.activated, v, final_pos)


# --------------------------------------------------------------------------
# Build setup, Monte Carlo, summaries
# --------------------------------------------------------------------------
DEFAULT_PARAMS = {"season": 1, "weather": 1, "time": 2, "grade": 100, "popularity": 1}


def make_env_and_skills(data: Data, cfg: dict, spec: dict):
    cid = str(cfg["course"])
    if cid not in data.courses:
        raise ValueError(f"Unknown course '{cid}'. Try --list-courses")
    course = data.courses[cid]
    mood = int(cfg.get("mood", 2))
    ground = parse_ground(cfg.get("ground", 1))
    params = dict(DEFAULT_PARAMS, **cfg.get("params", {}))
    base = base_horse(spec, mood)
    adj = adjusted_horse(base, course, ground)
    env = Env(course, base, adj, ground, mood, params)
    env.wisdom_checks = bool(cfg.get("wisdom_checks", True))
    compiled = []
    for ref in spec.get("skills", []):
        sid = data.resolve_skill(ref)
        cs = compile_skill(sid, data.skills[sid], env)
        cs.name = data.display_name(sid)
        compiled.append(cs)
    return env, compiled


def run_chunk(args):
    """Worker entry point (top-level so multiprocessing can pickle it)."""
    data_dir, cfg, spec, start, stop, seed = args
    data = Data.load(data_dir)
    env, compiled = make_env_and_skills(data, cfg, spec)
    out = []
    for i in range(start, stop):
        r = Race(env, compiled, random.Random(seed * 100003 + i)).run()
        out.append((r.finish_time, r.ran_out_of_hp, r.activations))
    return out


def percentile(sorted_vals, p):
    return sorted_vals[min(len(sorted_vals) - 1, max(0, round(p * (len(sorted_vals) - 1))))]


def summarize(results: list, compiled: list) -> dict:
    n = len(results)
    times = sorted(r[0] for r in results)
    skills_out = {}
    for cs in compiled:
        hits = [r[2][cs.sid] for r in results if cs.sid in r[2]]
        entry = {"name": cs.name, "status": cs.status,
                 "activation_rate": round(len(hits) / n, 4) if cs.status in ("ok", "approx") else None}
        if hits:
            entry["mean_activation_m"] = round(statistics.fmean(hits), 1)
        if cs.reason:
            entry["unsupported_condition"] = cs.reason
        skills_out[cs.sid] = entry
    return {
        "mean_s": round(statistics.fmean(times), 4), "median_s": round(statistics.median(times), 4),
        "stdev_s": round(statistics.stdev(times), 4) if n > 1 else 0.0,
        "p05_s": round(percentile(times, 0.05), 4), "p95_s": round(percentile(times, 0.95), 4),
        "out_of_hp_rate": round(sum(1 for r in results if r[1]) / n, 4),
        "skills": skills_out,
    }


def simulate(data_dir, cfg, spec, runs, seed, workers):
    if workers > 1 and runs >= workers * 2:
        from multiprocessing import Pool
        step = math.ceil(runs / workers)
        jobs = [(data_dir, cfg, spec, a, min(a + step, runs), seed) for a in range(0, runs, step)]
        with Pool(workers) as pool:
            parts = pool.map(run_chunk, jobs)
        return [r for part in parts for r in part]
    return run_chunk((data_dir, cfg, spec, 0, runs, seed))


def run_config(cfg: dict, data_dir=None, workers=1) -> dict:
    data = Data.load(data_dir)
    runs, seed = int(cfg.get("runs", 500)), int(cfg.get("seed", 1))
    cid = str(cfg["course"])
    if cid not in data.courses:
        raise ValueError(f"Unknown course '{cid}'. Try --list-courses")
    c = data.courses[cid]
    out = {"course": f"{c['track']} {c['distance']}m {'turf' if c['surface'] == 1 else 'dirt'}",
           "runs": runs, "seed": seed,
           "note": "single-runner model; conditions about other runners are assumed true (see docstring)"}
    raw, warnings = {}, []
    for label, spec in cfg["builds"].items():
        _, compiled = make_env_and_skills(data, cfg, spec)
        raw[label] = simulate(str(find_data_dir(data_dir)), cfg, spec, runs, seed, workers)
        out[label] = summarize(raw[label], compiled)
        for cs in compiled:
            if cs.status == "unsupported":
                warnings.append(f"{label}: '{cs.name}' skipped - condition '{cs.reason}' not supported")
            elif cs.status == "inactive":
                warnings.append(f"{label}: '{cs.name}' cannot activate on this course/build")
            elif cs.status == "approx":
                warnings.append(f"{label}: '{cs.name}' is approximate - depends on other runners")
            if cs.partial:
                warnings.append(f"{label}: '{cs.name}' has effects on other runners that are ignored")
    if "A" in raw and "B" in raw:
        a = [r[0] for r in raw["A"]]
        b = [r[0] for r in raw["B"]]
        wins = sum(1.0 if x < y else 0.5 if x == y else 0.0 for x, y in zip(a, b))
        out["comparison"] = {"mean_diff_s_B_minus_A": round(statistics.fmean(b) - statistics.fmean(a), 4),
                             "A_faster_rate": round(wins / runs, 4)}
    if warnings:
        out["warnings"] = warnings
    return out


DEMO_CONFIG = {
    "course": "10606", "ground": 1, "mood": 2, "runs": 300, "seed": 1,
    "builds": {
        "A": {"stats": {"speed": 1100, "stamina": 1000, "power": 900, "guts": 500, "wisdom": 600},
              "style": "pace", "aptitudes": {"distance": "A", "surface": "A", "strategy": "A"},
              "skills": ["Corner Recovery ○"]},
        "B": {"stats": {"speed": 1100, "stamina": 1000, "power": 900, "guts": 500, "wisdom": 600},
              "style": "pace", "aptitudes": {"distance": "A", "surface": "A", "strategy": "A"},
              "skills": ["Corner Recovery ○", "Corner Accel ○", "Straight Accel"]},
    },
}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Uma Musume race simulator (v2)")
    ap.add_argument("--config", help="JSON config path, or '-' for stdin (default: demo)")
    ap.add_argument("--runs", type=int)
    ap.add_argument("--seed", type=int)
    ap.add_argument("--workers", type=int, default=1, help="parallel processes")
    ap.add_argument("--data-dir")
    ap.add_argument("--find-skill", metavar="TEXT", help="search skills by name and exit")
    ap.add_argument("--list-courses", nargs="?", const="", metavar="TEXT", help="list/search courses and exit")
    args = ap.parse_args(argv)
    try:
        if args.find_skill is not None:
            print(json.dumps(Data.load(args.data_dir).find_skills(args.find_skill), ensure_ascii=False, indent=2))
            return 0
        if args.list_courses is not None:
            print(json.dumps(Data.load(args.data_dir).list_courses(args.list_courses), ensure_ascii=False, indent=2))
            return 0
        if args.config == "-":
            cfg = json.load(sys.stdin)
        elif args.config:
            with open(args.config, encoding="utf-8") as fh:
                cfg = json.load(fh)
        else:
            cfg = json.loads(json.dumps(DEMO_CONFIG))
        if args.runs is not None:
            cfg["runs"] = args.runs
        if args.seed is not None:
            cfg["seed"] = args.seed
        result = run_config(cfg, args.data_dir, max(1, args.workers))
    except (KeyError, ValueError, TypeError, FileNotFoundError) as exc:
        print(json.dumps({"error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
