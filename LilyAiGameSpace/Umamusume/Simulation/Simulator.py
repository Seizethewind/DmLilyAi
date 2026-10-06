#!/usr/bin/env python3
"""
Uma Musume race simulator -- SKELETON.

A small, dependency-free Monte Carlo time-trial simulator. It compares two
builds (A vs B) on one course by running many seeded races and reporting
finish-time statistics as JSON on stdout.

IMPORTANT: every number in the "MODEL" section is a PLACEHOLDER chosen to
give plausible-looking behaviour. They are NOT the game's real formulas.
Replace them (and validate against known results) before trusting output.

Usage
-----
    python Simulator.py                      # demo config
    python Simulator.py --config build.json  # your own config ('-' = stdin)
    python Simulator.py --runs 5000 --seed 7

Config shape (JSON)
-------------------
    {
      "course": "demo_2000",
      "runs": 2000,
      "seed": 1,
      "builds": {
        "A": {"stats": {"speed": 1000, "stamina": 600, "power": 700,
                        "guts": 400, "wit": 500},
              "style": "pace", "skills": ["Demo Late Burst"]},
        "B": {"stats": {...}, "style": "pace", "skills": [...]}
      }
    }

Roadmap / TODO
--------------
 1. Replace placeholder formulas with verified ones.
 2. Load courses and skills from data files (see ../Skill/) instead of the
    built-in demo dicts below.
 3. Richer skill conditions (rank, corner/straight, slope, terrain).
 4. Multi-runner races (positions, blocking, rank-based conditions).
 5. Tests that compare against known community results.
"""
from __future__ import annotations

import argparse
import json
import random
import statistics
import sys
from dataclasses import dataclass

TICK = 1.0 / 15.0          # seconds per simulation step
MAX_SIM_SECONDS = 600.0    # safety cap so a bad config can't loop forever
START_SPEED = 3.0          # m/s at the gate (placeholder)
DECEL = 1.0                # m/s^2 when above target speed (placeholder)


# --------------------------------------------------------------------------
# DATA (demo only -- move to data files later)
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Course:
    name: str
    length: int  # metres


COURSES = {
    "demo_1600": Course("Demo 1600m", 1600),
    "demo_2000": Course("Demo 2000m", 2000),
    "demo_2400": Course("Demo 2400m", 2400),
}


@dataclass(frozen=True)
class Skill:
    name: str
    effect: str        # "target_speed" | "acceleration" | "recovery"
    magnitude: float   # m/s, m/s^2, or fraction of max HP (recovery)
    duration: float    # seconds (ignored for "recovery", which is instant)
    condition: dict    # see condition_met()
    chance: float = 1.0  # activation probability once condition is met


SKILLS = {
    s.name: s
    for s in [
        Skill("Demo Early Pace Up", "target_speed", 0.15, 2.5, {"phase": "early"}),
        Skill("Demo Late Burst", "target_speed", 0.25, 3.0, {"phase": "late"}, 0.8),
        Skill("Demo Late Accel", "acceleration", 0.20, 3.0, {"phase": "late"}),
        Skill("Demo Mid Recovery", "recovery", 0.03, 0.0, {"phase": "middle"}),
    ]
}


@dataclass(frozen=True)
class Runner:
    speed: int
    stamina: int
    power: int
    guts: int
    wit: int
    style: str = "pace"   # front | pace | late | end


# --------------------------------------------------------------------------
# MODEL -- PLACEHOLDER FORMULAS (replace with verified ones)
# --------------------------------------------------------------------------
STYLE_PHASE_SPEED = {
    "front": {"early": 1.000, "middle": 0.980, "late": 0.962},
    "pace":  {"early": 0.978, "middle": 0.991, "late": 0.975},
    "late":  {"early": 0.938, "middle": 0.998, "late": 0.994},
    "end":   {"early": 0.931, "middle": 1.000, "late": 1.000},
}
STYLE_HP_COEF = {"front": 0.95, "pace": 0.89, "late": 1.0, "end": 0.995}


def phase_of(course: Course, pos: float) -> str:
    f = pos / course.length
    if f < 1 / 6:
        return "early"
    if f < 2 / 3:
        return "middle"
    return "late"


def base_speed(course: Course) -> float:
    return 20.0 - (course.length - 2000) / 1000.0


def target_speed(course: Course, r: Runner, phase: str) -> float:
    return base_speed(course) * STYLE_PHASE_SPEED[r.style][phase] + r.speed * 0.0010


def base_accel(r: Runner) -> float:
    return 0.5 + r.power / 1000.0


def max_hp(course: Course, r: Runner) -> float:
    return course.length + 0.8 * r.stamina * STYLE_HP_COEF[r.style]


def hp_drain(v: float, course: Course) -> float:
    """HP lost per second at speed v."""
    return 20.0 * (v - base_speed(course) + 12.0) ** 2 / 144.0


def condition_met(cond: dict, course: Course, pos: float) -> bool:
    """Data-driven skill conditions. Add new keys here as you need them."""
    f = pos / course.length
    if "phase" in cond and phase_of(course, pos) != cond["phase"]:
        return False
    if "pos_min" in cond and f < cond["pos_min"]:
        return False
    if "pos_max" in cond and f > cond["pos_max"]:
        return False
    return True


# --------------------------------------------------------------------------
# SIMULATION
# --------------------------------------------------------------------------
@dataclass
class RaceResult:
    finish_time: float
    hp_left: float
    activated: list


def run_race(course: Course, runner: Runner, skills: list, rng: random.Random) -> RaceResult:
    hp_max = max_hp(course, runner)
    hp = hp_max
    pos, v, t = 0.0, START_SPEED, 0.0
    pending = list(skills)   # each skill gets ONE activation attempt
    active = []              # (skill, ends_at)
    fired = []

    while pos < course.length and t < MAX_SIM_SECONDS:
        # 1. skill activation
        for s in pending[:]:
            if condition_met(s.condition, course, pos):
                pending.remove(s)
                if rng.random() < s.chance:
                    fired.append(s.name)
                    if s.effect == "recovery":
                        hp = min(hp_max, hp + s.magnitude * hp_max)
                    else:
                        active.append((s, t + s.duration))
        active = [(s, end) for s, end in active if end > t]

        # 2. current targets
        target = target_speed(course, runner, phase_of(course, pos))
        accel = base_accel(runner)
        for s, _ in active:
            if s.effect == "target_speed":
                target += s.magnitude
            elif s.effect == "acceleration":
                accel += s.magnitude
        if hp <= 0:
            target = min(target, 0.85 * base_speed(course))

        # 3. integrate
        if v < target:
            v = min(target, v + accel * TICK)
        else:
            v = max(target, v - DECEL * TICK)
        pos += v * TICK
        hp -= hp_drain(v, course) * TICK
        t += TICK

    if pos > course.length and v > 0:   # trim the final partial tick
        t -= (pos - course.length) / v
    return RaceResult(finish_time=t, hp_left=hp, activated=fired)


def simulate_build(course, runner, skills, runs, seed):
    """Seeded Monte Carlo. Run i uses seed*100003+i so builds share RNG streams."""
    return [
        run_race(course, runner, skills, random.Random(seed * 100003 + i))
        for i in range(runs)
    ]


def percentile(sorted_vals, p):
    if not sorted_vals:
        return None
    idx = min(len(sorted_vals) - 1, max(0, round(p * (len(sorted_vals) - 1))))
    return sorted_vals[idx]


def summarize(results: list, skills: list) -> dict:
    times = sorted(r.finish_time for r in results)
    n = len(results)
    return {
        "mean_s": round(statistics.fmean(times), 4),
        "median_s": round(statistics.median(times), 4),
        "stdev_s": round(statistics.stdev(times), 4) if n > 1 else 0.0,
        "p05_s": round(percentile(times, 0.05), 4),
        "p95_s": round(percentile(times, 0.95), 4),
        "out_of_hp_rate": round(sum(1 for r in results if r.hp_left <= 0) / n, 4),
        "skill_activation_rate": {
            s.name: round(sum(1 for r in results if s.name in r.activated) / n, 4)
            for s in skills
        },
    }


# --------------------------------------------------------------------------
# CONFIG / CLI
# --------------------------------------------------------------------------
DEMO_CONFIG = {
    "course": "demo_2000",
    "runs": 2000,
    "seed": 1,
    "builds": {
        "A": {
            "stats": {"speed": 1000, "stamina": 600, "power": 700, "guts": 400, "wit": 500},
            "style": "pace",
            "skills": ["Demo Late Burst"],
        },
        "B": {
            "stats": {"speed": 1000, "stamina": 600, "power": 700, "guts": 400, "wit": 500},
            "style": "pace",
            "skills": ["Demo Late Burst", "Demo Mid Recovery"],
        },
    },
}


def build_from_spec(spec: dict):
    runner = Runner(**spec["stats"], style=spec.get("style", "pace"))
    if runner.style not in STYLE_PHASE_SPEED:
        raise ValueError(f"Unknown style '{runner.style}'")
    skills = []
    for name in spec.get("skills", []):
        if name not in SKILLS:
            raise ValueError(f"Unknown skill '{name}'. Known: {sorted(SKILLS)}")
        skills.append(SKILLS[name])
    return runner, skills


def run_config(cfg: dict) -> dict:
    cname = cfg["course"]
    if cname not in COURSES:
        raise ValueError(f"Unknown course '{cname}'. Known: {sorted(COURSES)}")
    course = COURSES[cname]
    runs, seed = int(cfg.get("runs", 1000)), int(cfg.get("seed", 1))

    out = {"course": course.name, "runs": runs, "seed": seed,
           "note": "placeholder model - not game-accurate"}
    raw = {}
    for label, spec in cfg["builds"].items():
        runner, skills = build_from_spec(spec)
        raw[label] = simulate_build(course, runner, skills, runs, seed)
        out[label] = summarize(raw[label], skills)

    if "A" in raw and "B" in raw:
        a = [r.finish_time for r in raw["A"]]
        b = [r.finish_time for r in raw["B"]]
        wins = sum(1.0 if x < y else 0.5 if x == y else 0.0 for x, y in zip(a, b))
        out["comparison"] = {
            "mean_diff_s_B_minus_A": round(statistics.fmean(b) - statistics.fmean(a), 4),
            "A_faster_rate": round(wins / runs, 4),
        }
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Uma Musume race simulator (skeleton)")
    ap.add_argument("--config", help="JSON config path, or '-' for stdin (default: demo)")
    ap.add_argument("--runs", type=int, help="override number of runs")
    ap.add_argument("--seed", type=int, help="override RNG seed")
    args = ap.parse_args(argv)

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

    try:
        result = run_config(cfg)
    except (KeyError, ValueError, TypeError) as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
