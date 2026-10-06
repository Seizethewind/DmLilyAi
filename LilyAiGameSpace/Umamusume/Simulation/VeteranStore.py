#!/usr/bin/env python3
"""
VeteranStore -- save veterans and simulation results in the Veteran/ folder.

Nothing else in this folder writes files: VeteranIntake only returns veterans and Simulator
only prints JSON. This module is the missing "save" step. It adds no behaviour to the other
files; import it where you want things stored.

Layout (next to this file)
--------------------------
    Veteran/
      veteran_oguri_cap.json            one veteran (clean format from VeteranReader.normalize_veteran)
      veteran_oguri_cap_2.json          same character, different stats = a different veteran
      results/
        veteran_oguri_cap/
          10606_20261006T120000Z.json   one simulation run: metadata + the full Simulator output

Saving rules
------------
* The file name comes from the character name (letters/digits only). No name -> a short hash of the stats.
* Same name AND same five stats already saved -> it is the same veteran: skills are merged in
  (duplicates dropped, missing aptitudes filled) instead of making a copy.
* Same name but different stats -> a new file with _2, _3, ... Existing veterans are never overwritten.
* Files are written to a temp file first and then renamed, so a crash cannot leave half a file.
* The veteran is validated with VeteranReader.normalize_veteran before anything is written.

Use from the bot (after VeteranIntake.intake_images):

    from VeteranStore import save_intake, format_saved
    saved = save_intake(outcome)                     # [(path, "created"|"updated"|"unchanged", warnings)]
    await message.channel.send(format_reply(outcome) + "\\n" + format_saved(saved))

Simulate a stored veteran and store the result:

    from VeteranStore import simulate_and_store
    result, path = simulate_and_store("oguri_cap", course="10606", style="pace", runs=500)
    # with add_skills a second build B is run too, so the result contains an A-vs-B comparison
    result, path = simulate_and_store("oguri_cap", "10606", add_skills=["Corner Accel ○"])

From the command line:

    python VeteranStore.py list
    python VeteranStore.py save oguri.json
    python VeteranStore.py simulate oguri_cap --course 10606 --style pace --runs 500
    python VeteranStore.py simulate oguri_cap --course 10606 --add-skill "Corner Accel ○"
    python VeteranStore.py results oguri_cap
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
VETERAN_DIR = HERE / "Veteran"
RESULTS_DIR = VETERAN_DIR / "results"
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


# --------------------------------------------------------------------------
# Small helpers
# --------------------------------------------------------------------------
def _write_json(path: Path, obj) -> None:
    """Write JSON atomically (temp file in the same folder, then rename)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def slugify(name, stats=None) -> str:
    """'Oguri Cap' -> 'oguri_cap'. Names with no latin letters/digits fall back to a stats hash."""
    s = re.sub(r"[^a-z0-9]+", "_", str(name or "").lower()).strip("_")
    if s:
        return s
    digest = hashlib.sha1(json.dumps(stats, sort_keys=True).encode("utf-8")).hexdigest()[:8] if stats else "unknown"
    return f"unnamed_{digest}"


def _now() -> datetime:
    return datetime.now(timezone.utc)


# --------------------------------------------------------------------------
# Veterans
# --------------------------------------------------------------------------
def save_veteran(veteran, directory=None) -> tuple[Path, str, list]:
    """Validate and store one veteran (dict or path to a JSON file).

    Returns (path, status, warnings). status is "created", "updated" (new skills or aptitudes
    were merged into an existing identical veteran) or "unchanged". Raises ValueError for an
    unusable veteran (for example a stat that could not be read)."""
    from VeteranReader import normalize_veteran
    vet, warnings = normalize_veteran(veteran)
    folder = Path(directory) if directory else VETERAN_DIR
    base = slugify(vet.get("name"), vet["stats"])
    n = 1
    while True:
        path = folder / (f"veteran_{base}.json" if n == 1 else f"veteran_{base}_{n}.json")
        if not path.exists():
            _write_json(path, vet)
            return path, "created", warnings
        old, _ = normalize_veteran(path)
        if old.get("name") == vet.get("name") and old["stats"] == vet["stats"]:
            seen = {s.lower() for s in old["skills"]}
            fresh = [s for s in vet["skills"] if s.lower() not in seen]
            changed = bool(fresh)
            old["skills"] += fresh
            for cat, group in vet["aptitudes"].items():
                for key, letter in group.items():
                    if letter is not None and old["aptitudes"][cat].get(key) is None:
                        old["aptitudes"][cat][key] = letter
                        changed = True
            if changed:
                _write_json(path, old)
            return path, "updated" if changed else "unchanged", warnings
        n += 1


def save_intake(outcome: dict, directory=None) -> list:
    """Store every veteran found by VeteranIntake.intake_images. Returns a list of
    (path, status, warnings); a veteran that cannot be stored is returned as (None, "error: ...", [])."""
    saved = []
    for vet in outcome.get("veterans", []):
        try:
            saved.append(save_veteran(vet, directory))
        except ValueError as exc:
            saved.append((None, f"error: {exc}", []))
    return saved


def format_saved(saved: list) -> str:
    """One short line per stored veteran, for the Discord reply."""
    lines = []
    for path, status, warnings in saved:
        if path is None:
            lines.append(f"Could not save the veteran ({status}).")
        else:
            lines.append(f"Saved as `{path.name}` ({status}).")
    return "\n".join(lines)


def find_veteran(ref) -> Path:
    """A file path, a file name in Veteran/, or just a name ('oguri_cap' or 'Oguri Cap')."""
    ref = str(ref)
    for cand in (Path(ref), VETERAN_DIR / ref, VETERAN_DIR / f"{ref}.json",
                 VETERAN_DIR / f"veteran_{slugify(ref)}.json"):
        if cand.is_file():
            return cand
    raise FileNotFoundError(f"No saved veteran '{ref}'. Try: python VeteranStore.py list")


def list_veterans(directory=None) -> list:
    from VeteranReader import normalize_veteran
    folder = Path(directory) if directory else VETERAN_DIR
    rows = []
    for p in sorted(folder.glob("veteran_*.json")):
        try:
            vet, _ = normalize_veteran(p)
        except (ValueError, json.JSONDecodeError):
            rows.append({"file": p.name, "name": None, "error": "unreadable file"})
            continue
        s = vet["stats"]
        rows.append({"file": p.name, "name": vet.get("name"),
                     "stats": f"{s['speed']}/{s['stamina']}/{s['power']}/{s['guts']}/{s['wisdom']}",
                     "skills": len(vet["skills"]),
                     "results": len(list_results(p))})
    return rows


# --------------------------------------------------------------------------
# Simulation results
# --------------------------------------------------------------------------
def save_result(result: dict, veteran_path, course, meta: dict | None = None, directory=None) -> Path:
    """Store one Simulator output under Veteran/results/<veteran file name>/. Never overwrites."""
    stem = Path(veteran_path).stem
    folder = (Path(directory) if directory else RESULTS_DIR) / stem
    course_part = re.sub(r"[^A-Za-z0-9_-]+", "", str(course)) or "course"
    stamp = _now().strftime("%Y%m%dT%H%M%SZ")
    path, n = folder / f"{course_part}_{stamp}.json", 1
    while path.exists():
        n += 1
        path = folder / f"{course_part}_{stamp}_{n}.json"
    _write_json(path, {"saved_at": _now().isoformat(timespec="seconds"),
                       "veteran_file": Path(veteran_path).name, **(meta or {}), "result": result})
    return path


def list_results(veteran_ref, directory=None) -> list:
    stem = Path(veteran_ref).stem if str(veteran_ref).endswith(".json") else slugify_ref(veteran_ref)
    folder = (Path(directory) if directory else RESULTS_DIR) / stem
    return sorted(folder.glob("*.json")) if folder.is_dir() else []


def slugify_ref(ref) -> str:
    ref = str(ref)
    return ref if ref.startswith("veteran_") else f"veteran_{slugify(ref)}"


def simulate_and_store(veteran, course, style=None, add_skills=None, ground=1, mood=2,
                       runs=500, seed=1, data_dir=None, workers=1, store=True):
    """Run the Simulator for a stored veteran and save the result.

    Build A is the veteran as stored. If add_skills is given, build B is the same veteran with
    those skills added, and the output includes the A-vs-B comparison.
    Returns (result, saved_path); saved_path is None when store=False."""
    from VeteranReader import load_data, to_build
    from Simulator import run_config
    path = find_veteran(veteran)
    data = load_data(data_dir)
    if data is None:
        raise FileNotFoundError("skills.json / courses.json not found; pass data_dir (see Simulator.py)")
    build_a, warns = to_build(path, course, style, None, data)
    builds = {"A": build_a}
    if add_skills:
        build_b, warns_b = to_build(path, course, style, list(add_skills), data)
        builds["B"] = build_b
        warns += warns_b
    cfg = {"course": str(course), "ground": ground, "mood": mood, "runs": runs, "seed": seed, "builds": builds}
    result = run_config(cfg, data_dir, max(1, workers))
    warns = list(dict.fromkeys(warns))
    if warns:
        result["build_warnings"] = warns
    saved = save_result(result, path, course, {"config": cfg}) if store else None
    return result, saved


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Store veterans and simulation results in Veteran/")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="list stored veterans")
    p_save = sub.add_parser("save", help="validate and store a veteran JSON file")
    p_save.add_argument("file")
    p_res = sub.add_parser("results", help="list stored results of a veteran")
    p_res.add_argument("veteran")
    p_sim = sub.add_parser("simulate", help="simulate a stored veteran and store the result")
    p_sim.add_argument("veteran")
    p_sim.add_argument("--course", required=True)
    p_sim.add_argument("--style")
    p_sim.add_argument("--add-skill", action="append", default=[], metavar="SKILL")
    p_sim.add_argument("--ground", default="1")
    p_sim.add_argument("--mood", type=int, default=2)
    p_sim.add_argument("--runs", type=int, default=500)
    p_sim.add_argument("--seed", type=int, default=1)
    p_sim.add_argument("--workers", type=int, default=1)
    p_sim.add_argument("--data-dir")
    p_sim.add_argument("--no-store", action="store_true", help="print only, do not save")
    args = ap.parse_args(argv)
    try:
        if args.cmd == "list":
            print(json.dumps(list_veterans(), ensure_ascii=False, indent=2))
        elif args.cmd == "save":
            path, status, warns = save_veteran(args.file)
            for w in warns:
                print(f"warning: {w}", file=sys.stderr)
            print(json.dumps({"saved": str(path), "status": status}))
        elif args.cmd == "results":
            print(json.dumps([str(p) for p in list_results(find_veteran(args.veteran))], indent=2))
        else:
            result, saved = simulate_and_store(args.veteran, args.course, args.style, args.add_skill,
                                               args.ground, args.mood, args.runs, args.seed,
                                               args.data_dir, args.workers, not args.no_store)
            print(json.dumps(result, ensure_ascii=False, indent=2))
            if saved:
                print(f"saved: {saved}", file=sys.stderr)
    except (KeyError, ValueError, TypeError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
