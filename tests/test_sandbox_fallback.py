"""Tests for the sandbox runner's local fallback. No network: the sandbox is faked, and the local path runs the real scripts.

Run:  python -m pytest tests/test_sandbox_fallback.py -v
"""
import asyncio
import importlib
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "LilyAiGameSpace" / "sandbox_scripts"


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ops, calcs, aff = _load("docs_table_ops"), _load("game_calcs"), _load("affinity_calc")

DOC = """## Cards
| Card | Rarity | Friendship |
| --- | --- | --- |
| Kitasan Black | SSR | 1,200 |
| Super Creek | SSR | 900 |
| Ines Fujin | R | 100 |
"""
TOP = {"op": "top", "column": "Friendship", "n": 1}

# three characters (ids 1, 2, 3): pair(1,2) = 5, so a main of 1 with legacy 2 totals 5
AFFINITY = {"chars": [1, 2, 3], "aff2": [0, 5, 6, 5, 0, 7, 6, 7, 0], "aff3": [0] * 27}
AFFINITY_PARAMS = {"op": "total", "main": 1, "legacy1": 2, "names": {"1": "A", "2": "B", "3": "C"}}


class _FS:
    def __init__(self, files):
        self.files = files

    def write(self, path, content):
        self.files[path] = content


class _Res:
    def __init__(self, stdout):
        self.stdout, self.exit_code, self.stderr = stdout, 0, ""


class _FakeSandbox:
    """Runs the real script against the uploaded files, like the microVM would."""

    def __init__(self):
        self.files = {}
        self.filesystem = _FS(self.files)

    def exec(self, cmd, timeout_seconds=30):
        params = json.loads(self.files["/workspace/params.json"])
        if "game_calcs.py" in cmd:
            return _Res(json.dumps(calcs.run(params)))
        if "affinity_calc.py" in cmd:
            return _Res(json.dumps(aff.run(params, json.loads(self.files["/workspace/affinity.json"]))))
        return _Res(json.dumps(ops.run(self.files["/workspace/input.md"], params)))

    def kill(self):
        pass


class _RateLimited(Exception):
    status_code = 429


@pytest.fixture()
def sr(monkeypatch):
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import sandbox_runner

    monkeypatch.setenv("PANDASTACK_API_KEY", "")
    monkeypatch.delenv("LILYAI_SANDBOX_LOCAL_FALLBACK", raising=False)
    monkeypatch.delenv("LILYAI_SANDBOX_LOCAL_MAX_CHARS", raising=False)
    sandbox_runner._cache.clear()
    sandbox_runner._pool = sandbox_runner._KeyPool()
    return sandbox_runner


def test_no_key_runs_the_same_script_locally(sr):
    text, in_box = sr.run_table_op_ex(DOC, TOP)
    assert "Kitasan Black" in text and in_box is False


def test_sandbox_is_used_when_it_works(sr):
    text, in_box = sr.run_table_op_ex(DOC, TOP, sandbox_factory=lambda template, ttl, key: _FakeSandbox())
    assert "Kitasan Black" in text and in_box is True


def test_every_key_rate_limited_falls_back_locally(sr, monkeypatch):
    monkeypatch.setenv("PANDASTACK_API_KEY", "k1,k2")

    def factory(template, ttl, key):
        raise _RateLimited("too many requests")

    text, in_box = sr.run_table_op_ex(DOC, TOP, sandbox_factory=factory)
    assert "Kitasan Black" in text and in_box is False


def test_a_bad_parameter_is_still_an_error_not_a_silent_fallback(sr):
    with pytest.raises(sr.SandboxError, match="Nope"):
        sr.run_table_op(DOC, {"op": "stat", "agg": "sum", "column": "Nope"})
    with pytest.raises(sr.SandboxError):
        sr.run_calc("compatibility", {})


def test_fallback_can_be_switched_off(sr, monkeypatch):
    monkeypatch.setenv("LILYAI_SANDBOX_LOCAL_FALLBACK", "0")
    assert sr.local_fallback_enabled() is False
    with pytest.raises(sr.SandboxError, match="isn't set up"):
        sr.run_table_op(DOC, TOP)


def test_oversized_input_reports_the_sandbox_problem(sr, monkeypatch):
    monkeypatch.setenv("LILYAI_SANDBOX_LOCAL_MAX_CHARS", "10000")
    with pytest.raises(sr.SandboxError, match="isn't set up"):
        sr.run_table_op(DOC * 400, TOP)


def test_calculators_fall_back_locally(sr):
    text, in_box = sr.run_calc_ex("blue_spark_odds", {"final_stat": 700})
    assert "50%" in text and in_box is False


def test_affinity_falls_back_locally(sr):
    text, in_box = sr.run_affinity_ex(AFFINITY_PARAMS, json.dumps(AFFINITY))
    assert "Base total: 5" in text and in_box is False


def test_can_run_follows_the_fallback_switch(sr, monkeypatch):
    assert sr.can_run() is True          # no key, fallback on
    monkeypatch.setenv("LILYAI_SANDBOX_LOCAL_FALLBACK", "off")
    assert sr.can_run() is False         # no key, fallback off


# ---- the tools the chat model sees ----
def _tools_module():
    return importlib.import_module("LilyAiTool.GameSpaceTools.sandbox_tools")


def test_tools_are_offered_with_the_fallback_and_hidden_without(sr, monkeypatch):
    st = _tools_module()
    offered = st.sandbox_tools()
    assert len(offered) == 3 and {t.category for t in offered} == {"gamespace"}
    monkeypatch.setenv("LILYAI_SANDBOX_LOCAL_FALLBACK", "0")
    assert st.sandbox_tools() == []


def test_tool_reply_says_it_ran_locally(sr):
    st = _tools_module()
    out = asyncio.run(st._calculate(None, {"calculator": "blue_spark_odds", "inputs": {"final_stat": 700}}))
    assert "locally" in out and "50%" in out
