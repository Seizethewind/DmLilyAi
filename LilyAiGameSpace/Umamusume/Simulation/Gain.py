#!/usr/bin/env python3
"""
Per-skill gain analysis for the Umamusume race simulator.

For every skill in a build this reports how many metres it gains, measured the
way Umalator does: two races with identical randomness are run side by side and
the distance between the runners is read at the moment the faster one crosses
the finish line.

Two numbers per skill:
  solo_gain_m      the skill alone vs. a build with no skills
  marginal_gain_m  your full build vs. the same build WITHOUT this skill
                   (what you would lose by dropping it; accounts for synergies,
                   e.g. a heal that lets a later speed skill matter)
plus the gain of the whole build vs. no skills. Each comes with a 95% interval
(+/- ci95): if it is larger than the gain, run more races.

Usage (same config file as Simulator.py; every build in "builds" is analysed):
    python Gain.py                                 # demo
    python Gain.py --config build.json --runs 600 --workers 4

Notes
-----
* Metres gained is not seconds: gain_s_approx divides by the runner's final speed.
* Skills with a wit check can fail to activate; that is included (it is the
  expected gain). Set "wisdom_checks": false in the config to see the gain when
  the skill always gets its chance.
* Conditions about other runners are assumed true (see Simulator.py), so gains
  for skills flagged "approx" are rough; "unsupported"/"inactive" skills get no
  gain and are listed in "warnings".
"""
from __future__ import annotations

import argparse
import json
import math
import random
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import Simulator as S  # noqa: E402


class PairedRace(S.Race):
    """Race whose skill randomness is keyed by (race seed, skill id).

    Two builds that differ only in which skills they carry then share the same
    start delay, section speed noise and the same random trigger point / wit
    roll for every skill they have in common, so differences are due to the
    skills and not to luck.
    """

    def __init__(self, env, compiled, seed):
        super().__init__(env, compiled, random.Random(seed))
        self.seed = seed

    def _setup_skills(self):
        h = self.h
        wis_chance = max(1 - 90.0 / h.wisdom, 0.2)
        self.live = []
        for cs in self.compiled:
            if cs.status not in ("ok", "approx"):
                continue
            rng = random.Random(f"{self.seed}:{cs.sid}")
            if cs.wisdom_check and self.env.wisdom_checks and rng.random() >= wis_chance:
                continue
            sr = S.SkillRun(cs)
            for alt in cs.alts:
                ar = S.AltRun(alt, sr)
                ar.pre = S._sample_entries(alt.pre_terms, rng, ar)
                self.live += S._sample_entries(alt.terms, rng, ar)


def gain_job(args):
    """One comparison: `test` skills vs `base` skills. Returns per-race gains in metres."""
    data_dir, cfg, spec, base_ids, test_ids, runs, seed = args
    data = S.Data.load(data_dir)
    env_b, comp_b = S.make_env_and_skills(data, cfg, dict(spec, skills=base_ids))
    env_t, comp_t = S.make_env_and_skills(data, cfg, dict(spec, skills=test_ids))
    gains, speeds, acts = [], [], {}
    for i in range(runs):
        s = seed * 100003 + i
        rb = PairedRace(env_b, comp_b, s)
        rb.trace = []
        res_b = rb.run()
        rt = PairedRace(env_t, comp_t, s)
        rt.trace = []
        res_t = rt.run()
        k = len(rt.trace) - 1
        if k < len(rb.trace):
            pos_b = rb.trace[k]
        else:   # the baseline finished first: carry it on at its final speed
            pos_b = rb.trace[-1] + (k - len(rb.trace) + 1) * res_b.final_speed * S.DT
        gains.append(res_t.final_pos - pos_b)
        speeds.append(res_t.final_speed)
        for sid in res_t.activations:
            acts[sid] = acts.get(sid, 0) + 1
    return gains, speeds, acts


def stats_of(gains, speeds):
    n = len(gains)
    mean = statistics.fmean(gains)
    ci = 1.96 * statistics.stdev(gains) / math.sqrt(n) if n > 1 else 0.0
    v = statistics.fmean(speeds) if speeds else 20.0
    return {"gain_m": round(mean, 2), "ci95_m": round(ci, 2), "gain_s_approx": round(mean / v, 3)}


def analyse(cfg: dict, data_dir=None, workers: int = 1) -> dict:
    data = S.Data.load(data_dir)
    dd = str(S.find_data_dir(data_dir))
    runs, seed = int(cfg.get("runs", 300)), int(cfg.get("seed", 1))
    c = data.courses[str(cfg["course"])]
    out = {"course": f"{c['track']} {c['distance']}m {'turf' if c['surface'] == 1 else 'dirt'}",
           "runs": runs, "seed": seed, "mode": "gain",
           "note": "metres gained at the finish vs the comparison build, same randomness; see Gain.py docstring"}
    warnings, jobs, plan = [], [], []   # plan: (label, kind, sid) in job order

    for label, spec in cfg["builds"].items():
        ids = []
        for ref in spec.get("skills", []):
            sid = data.resolve_skill(ref)
            if sid not in ids:
                ids.append(sid)
        _, compiled = S.make_env_and_skills(data, cfg, dict(spec, skills=ids))
        status = {cs.sid: cs for cs in compiled}
        live = [sid for sid in ids if status[sid].status in ("ok", "approx")]
        for sid in ids:
            cs = status[sid]
            if cs.status == "unsupported":
                warnings.append(f"{label}: '{cs.name}' skipped - condition '{cs.reason}' not supported")
            elif cs.status == "inactive":
                warnings.append(f"{label}: '{cs.name}' cannot activate on this course/build")
            elif cs.status == "approx":
                warnings.append(f"{label}: '{cs.name}' is approximate - depends on other runners")
        out[label] = {"_ids": ids, "_status": status, "_live": live}
        if not live:
            continue
        jobs.append((dd, cfg, spec, [], live, runs, seed))
        plan.append((label, "full", None))
        for sid in live:
            jobs.append((dd, cfg, spec, [], [sid], runs, seed))
            plan.append((label, "solo", sid))
            if len(live) > 1:
                jobs.append((dd, cfg, spec, [x for x in live if x != sid], live, runs, seed))
                plan.append((label, "marginal", sid))

    if workers > 1 and len(jobs) > 1:
        from multiprocessing import Pool
        with Pool(workers) as pool:
            results = pool.map(gain_job, jobs)
    else:
        results = [gain_job(j) for j in jobs]

    per = {}
    for (label, kind, sid), (gains, speeds, acts) in zip(plan, results):
        per.setdefault(label, {})[(kind, sid)] = (stats_of(gains, speeds), acts)

    for label in list(cfg["builds"]):
        info = out.pop(label)
        ids, status, live = info["_ids"], info["_status"], info["_live"]
        res = per.get(label, {})
        entry = {}
        if ("full", None) in res:
            entry["full_build_vs_no_skills"] = res[("full", None)][0]
        rows = []
        full_acts = res.get(("full", None), (None, {}))[1]
        for sid in ids:
            cs = status[sid]
            row = {"id": sid, "name": cs.name, "status": cs.status}
            if sid in live:
                row["activation_rate"] = round(full_acts.get(sid, 0) / runs, 3)
                solo = res[("solo", sid)][0]
                row["solo_gain_m"], row["solo_ci95_m"] = solo["gain_m"], solo["ci95_m"]
                marg = res.get(("marginal", sid), res[("solo", sid)])[0]
                row["marginal_gain_m"], row["marginal_ci95_m"] = marg["gain_m"], marg["ci95_m"]
                row["marginal_gain_s_approx"] = marg["gain_s_approx"]
            rows.append(row)
        rows.sort(key=lambda r: -r.get("marginal_gain_m", float("-inf")))
        entry["skills"] = rows
        out[label] = entry
    if warnings:
        out["warnings"] = warnings
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Per-skill gain analysis (see docstring)")
    ap.add_argument("--config", help="JSON config path, or '-' for stdin (default: Simulator demo)")
    ap.add_argument("--runs", type=int, help="races per comparison (default 300)")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--workers", type=int, default=1, help="parallel processes")
    ap.add_argument("--data-dir")
    args = ap.parse_args(argv)
    try:
        if args.config == "-":
            cfg = json.load(sys.stdin)
        elif args.config:
            with open(args.config, encoding="utf-8") as fh:
                cfg = json.load(fh)
        else:
            cfg = json.loads(json.dumps(S.DEMO_CONFIG))
        if args.runs is not None:
            cfg["runs"] = args.runs
        if args.seed is not None:
            cfg["seed"] = args.seed
        result = analyse(cfg, args.data_dir, max(1, args.workers))
    except (KeyError, ValueError, TypeError, FileNotFoundError) as exc:
        print(json.dumps({"error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
