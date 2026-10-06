"""The one door from LilyAi into the Simulation folder.

Simulator.py, VeteranReader.py, VeteranIntake.py and VeteranStore.py were written as stand-alone scripts that import each
other by bare name (``from VeteranReader import ...``). Rather than rewrite them, this module puts the folder on sys.path
once and re-exports what the bot needs, so the rest of LilyAi imports only from here. It adds no behaviour of its own
beyond: a cached data load, input limits, a compact text summary for the chat model, and a worker-thread wrapper so a
simulation never blocks the bot's event loop.

Nothing here writes files. Veterans and results are stored per user in the database (LilyAiMemory/Veteran).
"""
from __future__ import annotations

import asyncio
import sys
import threading
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.append(str(HERE))

import Simulator as _sim  # noqa: E402
import VeteranIntake as _intake  # noqa: E402
import VeteranReader as _reader  # noqa: E402

INTAKE_PROMPT = _intake.INTAKE_PROMPT
intake_images = _intake.intake_images
format_intake_reply = _intake.format_reply
normalize_veteran = _reader.normalize_veteran
best_style = _reader.best_style

DEFAULT_RUNS, MIN_RUNS, MAX_RUNS = 300, 50, 1000
MAX_SKILLS_SHOWN = 40
MAX_WARNINGS_SHOWN = 8
_slots = threading.BoundedSemaphore(2)   # at most two simulations at once: they are CPU-bound
_data = None
_data_lock = threading.Lock()


class SimulationError(Exception):
    """A user-presentable failure (bad course, unknown skill, busy...). Never includes a stack trace."""


def is_available() -> bool:
    """True when skills.json / courses.json can be found (built by tools/build_sim_data.py)."""
    try:
        _sim.find_data_dir()
        return True
    except FileNotFoundError:
        return False


def data():
    global _data
    with _data_lock:
        if _data is None:
            try:
                _data = _sim.Data.load()
            except FileNotFoundError as e:
                raise SimulationError(str(e)) from None
        return _data


def list_courses(text: str = "", limit: int = 30) -> tuple[list[dict], int]:
    """(first `limit` matching courses as {id, course}, total matches)."""
    rows = data().list_courses(text)
    return rows[:limit], len(rows)


def find_skills(text: str, limit: int = 15) -> list[dict]:
    return data().find_skills(text, limit)


def _fmt_time(seconds: float) -> str:
    m, s = divmod(seconds, 60)
    return f"{int(m)}:{s:06.3f}" if m else f"{s:.3f}s"


def summarize(result: dict, header: str, labels: dict[str, str]) -> str:
    """Compact text of a Simulator result: times, HP, skill activation, A vs B, warnings."""
    lines = [f"{header} - {result['course']}, {result['runs']} runs (seeded, so repeatable)."]
    for key, label in labels.items():
        r = result[key]
        lines.append(
            f"{label}: mean {_fmt_time(r['mean_s'])}, median {_fmt_time(r['median_s'])}, "
            f"p05-p95 {_fmt_time(r['p05_s'])} to {_fmt_time(r['p95_s'])}, stdev {r['stdev_s']:.3f}s, "
            f"ran out of HP in {r['out_of_hp_rate'] * 100:.1f}% of runs")
        parts = []
        for entry in list(r["skills"].values())[:MAX_SKILLS_SHOWN]:
            if entry["status"] in ("ok", "approx"):
                parts.append(f"{entry['name']} {entry['activation_rate'] * 100:.0f}%" + (" (approx)" if entry["status"] == "approx" else ""))
            else:
                parts.append(f"{entry['name']} not simulated ({entry['status']})")
        if parts:
            lines.append("  skills (share of runs that activated): " + ", ".join(parts))
    cmp_ = result.get("comparison")
    if cmp_:
        diff = cmp_["mean_diff_s_B_minus_A"]
        who = "B is faster" if diff < 0 else "A is faster" if diff > 0 else "same average"
        lines.append(f"B vs A: {who} by {abs(diff):.3f}s on average; A was the faster run in {cmp_['A_faster_rate'] * 100:.0f}% of races.")
    # Limits first and warnings last: the tool executor cuts long output at the end, and the limits must survive.
    lines.append("Model limits: single runner; skills that depend on other runners are assumed to trigger, so treat those as optimistic.")
    warnings = list(result.get("build_warnings", [])) + list(result.get("warnings", []))
    if warnings:
        shown = [w if len(w) <= 140 else w[:137] + "..." for w in warnings[:MAX_WARNINGS_SHOWN]]
        lines.append("Warnings: " + "; ".join(shown) +
                     (f"; and {len(warnings) - MAX_WARNINGS_SHOWN} more" if len(warnings) > MAX_WARNINGS_SHOWN else ""))
    return "\n".join(lines)


def run_simulation(vet: dict, course: str, style: str | None = None, add_skills: list[str] | None = None,
                   ground: Any = 1, mood: int = 2, runs: int = DEFAULT_RUNS, seed: int = 1) -> tuple[str, dict]:
    """Blocking. Simulate a checked veteran dict. Returns (summary text, raw Simulator result).
    Build A is the veteran as saved; with add_skills, build B is the same veteran plus those skills."""
    runs = max(MIN_RUNS, min(MAX_RUNS, int(runs or DEFAULT_RUNS)))
    d = data()
    try:
        build_a, warns = _reader.to_build(vet, str(course), style, None, d)
        builds = {"A": build_a}
        if add_skills:
            build_b, warns_b = _reader.to_build(vet, str(course), style, list(add_skills), d)
            builds["B"] = build_b
            warns += warns_b
        cfg = {"course": str(course), "ground": ground, "mood": int(mood), "runs": runs, "seed": int(seed), "builds": builds}
        if not _slots.acquire(timeout=10):
            raise SimulationError("The simulator is busy right now. Try again in a moment.")
        try:
            result = _sim.run_config(cfg, None, 1)
        finally:
            _slots.release()
    except (ValueError, KeyError, TypeError) as e:
        raise SimulationError(str(e)) from None
    warns = list(dict.fromkeys(warns))
    if warns:
        result["build_warnings"] = warns
    name = vet.get("name") or "Veteran"
    header = f"{name}, style {builds['A']['style']}"
    labels = {"A": "A (as saved)"} if "B" not in builds else {"A": "A (as saved)", "B": "B (+" + ", ".join(add_skills) + ")"}
    return summarize(result, header, labels), result


async def run_simulation_async(*args: Any, **kw: Any) -> tuple[str, dict]:
    return await asyncio.to_thread(run_simulation, *args, **kw)
