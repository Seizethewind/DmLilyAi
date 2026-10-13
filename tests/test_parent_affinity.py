"""Tests for the affinity script's "parents" op (saved parents scored for a trainee) and its runner path. No network.

Run:  python -m pytest tests/test_parent_affinity.py -v
"""
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "LilyAiTool" / "Sandbox" / "sandbox_scripts"


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


aff = _load("affinity_calc")


def _data():
    """Four characters (ids 1-4). pair(1,2)=5 pair(1,3)=7 pair(2,3)=4 pair(1,4)=1 pair(2,4)=2 pair(3,4)=3; triple(1,2,3)=10."""
    n = 4
    a2 = [0] * (n * n)
    for (a, b), v in {(1, 2): 5, (1, 3): 7, (2, 3): 4, (1, 4): 1, (2, 4): 2, (3, 4): 3}.items():
        a2[(a - 1) * n + (b - 1)] = v
        a2[(b - 1) * n + (a - 1)] = v
    a3 = [0] * (n ** 3)
    a3[((1 - 1) * n + (2 - 1)) * n + (3 - 1)] = 10
    return {"chars": [1, 2, 3, 4], "aff2": a2, "aff3": a3}


NAMES = {"1": "A", "2": "B", "3": "C", "4": "D"}
PARENTS = [
    {"id": 1, "label": "#1 B", "uma": 2, "gps": [3]},     # side = pair(1,2) 5 + triple(1,2,3) 10 = 15
    {"id": 2, "label": "#2 C", "uma": 3, "gps": []},      # side = pair(1,3) = 7
    {"id": 3, "label": "#3 D", "uma": 4, "gps": []},      # side = pair(1,4) = 1
]


def _run(parents=PARENTS, **extra):
    return aff.run({"op": "parents", "main": 1, "parents": parents, "names": NAMES, **extra}, _data())


def test_each_parent_is_scored_best_first():
    r = _run()
    assert r["ok"]
    text = r["text"]
    assert "1. #1 B: 15 (pair 5 + sub-legacies 10 from C)" in text
    assert "2. #2 C: 7 (pair 7 + sub-legacies 0)" in text
    assert "3. #3 D: 1" in text


def test_the_best_pair_adds_both_sides_and_the_parents_own_pair():
    text = _run()["text"]
    assert "1. #1 B + #2 C: 26" in text          # 15 + 7 + pair(2,3)=4
    assert "2. #1 B + #3 D: 18" in text          # 15 + 1 + pair(2,4)=2
    assert "Race-win bonuses (shared G1 wins) are not included" in text


def test_a_race_bonus_is_added_to_pair_totals_only():
    text = _run(bonus=10)["text"]
    assert "#1 B + #2 C: 36" in text and "of 10 are included" in text


def test_top_limits_the_pair_list():
    text = _run(top=1)["text"]
    assert "#1 B + #2 C" in text and "#2 C + #3 D" not in text


def test_a_parent_the_same_as_the_trainee_or_missing_is_skipped_with_a_note():
    parents = PARENTS + [{"id": 9, "label": "#9 A", "uma": 1, "gps": []}, {"id": 10, "label": "#10 ?", "uma": 99, "gps": []}]
    text = _run(parents)["text"]
    assert "Not scored:" in text and "#9 A (same character as the trainee)" in text and "#10 ? (not in the affinity data)" in text


def test_no_usable_parent_is_an_error():
    r = _run([{"id": 9, "label": "#9 A", "uma": 1, "gps": []}])
    assert not r["ok"] and "none of the saved parents" in r["error"]


def test_a_missing_parents_list_is_an_error():
    assert not aff.run({"op": "parents", "main": 1, "names": NAMES}, _data())["ok"]


def test_the_old_ops_are_unchanged():
    r = aff.run({"op": "total", "main": 1, "legacy1": 2, "names": NAMES}, _data())
    assert r["ok"] and "Base total: 5" in r["text"]


# ---- through the runner (local fallback: no key here)
def test_the_runner_falls_back_locally_for_parents(monkeypatch):
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiTool.Sandbox import sandbox_runner as sr

    monkeypatch.setenv("PANDASTACK_API_KEY", "")
    monkeypatch.delenv("LILYAI_SANDBOX_LOCAL_FALLBACK", raising=False)
    sr._cache.clear()
    sr._pool = sr._KeyPool()
    params = {"op": "parents", "main": 1, "parents": PARENTS, "names": NAMES}
    text, in_box = sr.run_affinity_ex(params, json.dumps(_data()))
    assert in_box is False and "#1 B + #2 C: 26" in text
