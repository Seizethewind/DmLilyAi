"""Tests for the guide sandbox script (guide_ops.py) and the guide builder's use of it. No network, no real model.

Run:  python -m pytest tests/test_guide_ops.py -v
"""
import asyncio
import importlib.util
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "LilyAiGameSpace" / "sandbox_scripts"


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


go = _load("guide_ops")

TABLE = """| Card | Type | Bonus | Cost |
| --- | --- | --- | --- |
| Kitasan Black | Speed | 30 | 10 |
| Super Creek | Stamina | 24 | 8 |
| Ines Fujin | Wit | 12 | 6 |
| Mejiro Ryan | Power | 18 | 9 |
| Biko Pegasus | Speed | 21 | 7 |
"""

NUMBER_SAMPLES = [
    "- Speed +20% costs 1,200 [S3], 2nd place, 3.50",
    "1. First step\n2. Second step with 45 points [C1]",
    "She wins on the 3rd of May with 1,000.50 points and 007",
    "No numbers at all here.",
]


# ---- the three copies of the number rules must agree
def test_number_rules_agree_everywhere():
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import guide_builder, number_check

    for text in NUMBER_SAMPLES:
        assert go.numbers_in(text) == number_check.numbers_in(text) == guide_builder.numbers_in(text)


def test_verify_agrees_with_the_guide_builder():
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import guide_builder as gb

    passage = gb.Passage("S1", "d1", "Special Week", "Overview", "Speed growth is 20% and it costs 1,200 points. Stamina is 15%.")
    draft = "- Growth is 20% [S1]. Costs 999 points [S1] [S9]\n- Stamina is 15% [S1]\n- Wild claim of 777 [S1]"
    expected = gb.verify_section(draft, [passage])
    got = go.verify_section(draft, {"S1"}, [f"{passage.title} {passage.section} {passage.text}"])
    assert got == expected and expected[1] >= 2


# ---- prep
def test_prep_keeps_the_part_that_matches_the_section():
    filler1 = "Unrelated filler about the weather and nothing else."
    wanted = "Speed growth rate is 20% for Special Week."
    filler2 = "Other filler about snacks and tea."
    passages = [{"tag": "S1", "text": f"{filler1}\n\n{wanted}\n\n{filler2}"}]
    chosen = go.select_passages(passages, go._terms(["speed growth rate"]), 60)
    assert len(chosen) == 1 and wanted in chosen[0]["text"] and "weather" not in chosen[0]["text"]


def test_prep_keeps_everything_when_it_fits():
    passages = [{"tag": "S1", "text": "One short paragraph.\n\nAnother short one."}]
    chosen = go.select_passages(passages, set(), 3000)
    assert "One short paragraph." in chosen[0]["text"] and "Another short one." in chosen[0]["text"]


def test_prep_clips_a_big_table_instead_of_dropping_it():
    rows = "\n".join(f"| Card {i} | {i} |" for i in range(200))
    table = f"| Name | Value |\n| --- | --- |\n{rows}"
    chosen = go.select_passages([{"tag": "S1", "text": table}], set(), 500)
    assert chosen and chosen[0]["text"].startswith("| Name | Value |") and len(chosen[0]["text"]) <= 520


def test_table_figures_are_exact():
    facts = go.table_facts(TABLE, "Support Cards > Cards", 3)
    assert len(facts) == 1
    assert "highest Kitasan Black (30)" in facts[0] and "lowest Ines Fujin (12)" in facts[0]
    assert "average 21" in facts[0] and "total 105 over 5 rows" in facts[0]


def test_small_tables_get_no_figures():
    assert go.table_facts("| A | B |\n| --- | --- |\n| x | 1 |\n| y | 2 |\n", "Doc > Sec", 3) == []


def test_prep_op_end_to_end():
    result = go.run({"op": "prep", "budget": 3000, "sections": [
        {"title": "Cards", "queries": ["cards"],
         "passages": [{"tag": "S1", "doc": "Support Cards", "section": "Cards", "text": TABLE}]}]})
    assert result["ok"]
    sec = json.loads(result["text"])["sections"][0]
    assert sec["passages"][0]["tag"] == "S1"
    assert sec["facts"][0]["tag"] == "C1" and sec["facts"][0]["from"] == "S1"


def test_verify_op_end_to_end():
    result = go.run({"op": "verify", "sections": [
        {"text": "- Real 30 [S1]\n- Made up 777 [S1]", "tags": ["S1"], "allowed": [TABLE]}]})
    sec = json.loads(result["text"])["sections"][0]
    assert "Real 30" in sec["text"] and "777" not in sec["text"] and sec["dropped"] == 1


def test_unknown_op_is_an_error():
    assert go.run({"op": "nope"})["ok"] is False


# ---- the builder: prep and verify through the sandbox runner (local fallback here), a stub engine and a stub model
@pytest.fixture()
def gb(monkeypatch):
    pytest.importorskip("LilyAiCore.Logging.logger")
    from LilyAiGameSpace import guide_builder, sandbox_runner

    monkeypatch.setenv("PANDASTACK_API_KEY", "")
    monkeypatch.delenv("LILYAI_SANDBOX_LOCAL_FALLBACK", raising=False)
    sandbox_runner._cache.clear()
    sandbox_runner._pool = sandbox_runner._KeyPool()
    return guide_builder


class _Engine:
    def search(self, query, category, limit):
        return [SimpleNamespace(doc_id="d1", section="Cards", score=1.0)]

    def read(self, doc_id, section, max_chars):
        return SimpleNamespace(doc_id="d1", title="Support Cards", section="Cards", text=TABLE,
                               sources=["https://example.test/cards"])


class _Provider:
    def __init__(self, content):
        self.content, self.calls = content, 0

    async def chat(self, messages, **kw):
        self.calls += 1
        return SimpleNamespace(content=self.content, model="stub", tool_calls=[], raw_message={})


def _plan(gb_module):
    return gb_module.GuidePlan(
        key="k", title="Cards Guide", subject="Support Cards", goal="", subject_ids=["d1"], question="q",
        outline=[gb_module.SectionSpec("Cards", "About the cards.", ("cards",))])


DRAFT = ("- Kitasan Black has the top bonus of 30 [S1].\n"
         "- The average bonus is 21 across 5 cards [C1].\n"
         "- A made-up figure of 777 appears here [S1].")


def test_the_builder_uses_prep_facts_and_verifies(gb):
    builder = gb.GuideBuilder(_Engine(), _Provider(DRAFT), "m", None, retry_delay=0, use_sandbox=True)
    result = asyncio.run(builder.build(_plan(gb)))
    assert result.ok and result.dropped >= 1
    assert "Kitasan Black has the top bonus of 30" in result.text
    assert "average bonus is 21" in result.text and "777" not in result.text
    assert "[C1] Computed from Support Cards > Cards" in result.text


def test_the_builder_still_works_with_the_sandbox_steps_off(gb):
    builder = gb.GuideBuilder(_Engine(), _Provider(DRAFT), "m", None, retry_delay=0, use_sandbox=False)
    result = asyncio.run(builder.build(_plan(gb)))
    assert result.ok and "777" not in result.text and "Kitasan Black has the top bonus of 30" in result.text
    assert "Computed from" not in result.text


def test_a_failing_sandbox_step_falls_back_to_the_old_path(gb, monkeypatch):
    async def boom(params, **kw):
        raise RuntimeError("sandbox exploded")

    monkeypatch.setattr(gb.sandbox_runner, "run_guide_ops_ex_async", boom)
    builder = gb.GuideBuilder(_Engine(), _Provider(DRAFT), "m", None, retry_delay=0, use_sandbox=True)
    result = asyncio.run(builder.build(_plan(gb)))
    assert result.ok and "777" not in result.text and "Kitasan Black has the top bonus of 30" in result.text
