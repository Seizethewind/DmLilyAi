"""Tests for the batch / wider table operations and their runner. No network: the sandbox is faked, the scripts are real.

Run:  python -m pytest tests/test_sandbox_batch_ops.py -v
"""
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


ops = _load("docs_table_ops")

DOC_A = """## Cards
| Card | Type | Bonus | Cost |
| --- | --- | --- | --- |
| Kitasan Black | Speed | 30 | 10 |
| Super Creek | Stamina | 24 | 8 |
| Ines Fujin | Wit | 12 | 6 |
| Mejiro Ryan | Power | 18 | 9 |
| Biko Pegasus | Speed | 21 | 7 |
"""
DOC_B = """| Name | Cost |
| --- | --- |
| X | 5 |
| Y | 9 |
"""


def _run(params, text=DOC_A, sources=None):
    return ops.run(text, params, sources)


# ---- the wider single operations
def test_the_original_single_ops_still_work():
    r = _run({"op": "top", "column": "Bonus", "n": 2})
    assert r["ok"] and "Kitasan Black" in r["text"] and "Super Creek" in r["text"]


def test_several_where_conditions_must_all_hold():
    r = _run({"op": "filter", "where": [{"column": "Type", "op": "eq", "value": "Speed"},
                                        {"column": "Bonus", "op": "gt", "value": "25"}]})
    assert r["ok"] and "Kitasan Black" in r["text"] and "Biko Pegasus" not in r["text"]


def test_multi_column_sort():
    r = _run({"op": "top", "n": 3, "sort": [{"column": "Type", "order": "asc"}, {"column": "Bonus", "order": "desc"}]})
    text = r["text"]
    assert r["ok"] and text.index("Mejiro") < text.index("Kitasan") < text.index("Biko")


def test_a_derived_ratio_column_can_be_sorted_on():
    r = _run({"op": "top", "column": "Per Cost", "n": 1,
              "derive": {"name": "Per Cost", "numerator": "Bonus", "denominator": "Cost"}})
    assert r["ok"] and "Kitasan Black" in r["text"] and "Per Cost" in r["text"]


def test_rank_of_one_row():
    r = _run({"op": "rank", "names": "Super Creek", "column": "Bonus"})
    assert r["ok"] and "ranks 2 of 5 by Bonus" in r["text"]


def test_group_by_a_column():
    r = _run({"op": "group", "group_column": "Type", "agg": "sum", "column": "Bonus"})
    assert r["ok"] and "| Speed | 51 |" in r["text"]


def test_list_items_without_a_table():
    r = ops.run("- Alpha 12\n- Beta\n1. Gamma 5\n", {"op": "lists", "contains": "ga"})
    assert r["ok"] and "Gamma 5" in r["text"] and "Alpha" not in r["text"]


def test_bad_parameters_are_reported_not_raised():
    assert not _run({"op": "stat", "agg": "sum", "column": "Nope"})["ok"]
    assert not _run({"op": "rank", "names": "A, B", "column": "Bonus"})["ok"]
    assert not _run({"op": "group", "agg": "sum", "column": "Bonus"})["ok"]


# ---- batches
def test_a_batch_runs_ops_across_several_sources():
    r = _run({"ops": [{"op": "stat", "agg": "sum", "column": "Bonus", "source": "a"},
                      {"op": "stat", "agg": "max", "column": "Cost", "source": "b"}]},
             text="", sources={"a": DOC_A, "b": DOC_B})
    assert r["ok"]
    assert "sum of Bonus = 105" in r["text"] and "max of Cost = 9" in r["text"]
    assert "[1]" in r["text"] and "[2]" in r["text"]


def test_a_batch_reports_a_failed_op_but_keeps_the_good_ones():
    r = _run({"ops": [{"op": "stat", "agg": "sum", "column": "Bonus"}, {"op": "stat", "agg": "sum", "column": "Nope"}]})
    assert r["ok"] and "sum of Bonus = 105" in r["text"] and "error:" in r["text"]


def test_a_batch_where_everything_fails_is_an_error():
    r = _run({"ops": [{"op": "stat", "agg": "sum", "column": "Nope"}]})
    assert not r["ok"] and "Nope" in r["error"]


def test_a_batch_is_capped_and_unknown_sources_are_errors():
    assert not _run({"ops": [{"op": "tables"}] * 9})["ok"]
    r = _run({"ops": [{"op": "tables", "source": "zzz"}]})
    assert not r["ok"] and "unknown source" in r["error"]


# ---- the runner (batch, local fallback, sandbox)
class _FS:
    def __init__(self, files):
        self.files = files

    def write(self, path, content):
        self.files[path] = content


class _Res:
    def __init__(self, stdout):
        self.stdout, self.exit_code, self.stderr = stdout, 0, ""


class _FakeSandbox:
    def __init__(self):
        self.files = {}
        self.filesystem = _FS(self.files)

    def exec(self, cmd, timeout_seconds=30):
        sources = {p[len("/workspace/src_"):-3]: v for p, v in self.files.items() if p.startswith("/workspace/src_")}
        params = json.loads(self.files["/workspace/params.json"])
        return _Res(json.dumps(ops.run(self.files.get("/workspace/input.md", ""), params, sources)))

    def kill(self):
        pass


@pytest.fixture()
def sr(monkeypatch):
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import sandbox_runner

    monkeypatch.setenv("PANDASTACK_API_KEY", "")
    monkeypatch.delenv("LILYAI_SANDBOX_LOCAL_FALLBACK", raising=False)
    sandbox_runner._cache.clear()
    sandbox_runner._pool = sandbox_runner._KeyPool()
    return sandbox_runner


BATCH = [{"op": "stat", "agg": "sum", "column": "Bonus", "source": "a"},
         {"op": "stat", "agg": "max", "column": "Cost", "source": "b"}]


def test_runner_batch_in_the_sandbox(sr):
    text, in_box = sr.run_table_batch_ex(BATCH, {"a": DOC_A, "b": DOC_B}, sandbox_factory=lambda t, ttl, k: _FakeSandbox())
    assert in_box is True and "sum of Bonus = 105" in text and "max of Cost = 9" in text


def test_runner_batch_falls_back_locally(sr):
    text, in_box = sr.run_table_batch_ex(BATCH, {"a": DOC_A, "b": DOC_B})
    assert in_box is False and "sum of Bonus = 105" in text and "max of Cost = 9" in text


def test_runner_batch_checks_its_inputs(sr):
    with pytest.raises(sr.SandboxError):
        sr.run_table_batch_ex([], {})
    with pytest.raises(sr.SandboxError):
        sr.run_table_batch_ex([{"op": "tables"}] * 9, {"a": DOC_A})
    with pytest.raises(sr.SandboxError):
        sr.run_table_batch_ex(BATCH, {"bad name": DOC_A})
    with pytest.raises(sr.SandboxError):
        sr.run_table_batch_ex(BATCH, {f"s{i}": DOC_A for i in range(7)})
