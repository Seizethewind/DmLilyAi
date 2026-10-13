"""Tests for the shared number check and Analyst Mode's reply check. No network, no model.

Run:  python -m pytest tests/test_number_check.py -v
"""
import pytest

number_check = pytest.importorskip("LilyAiCore.Helpers.number_check")

EVIDENCE = ["Kitasan Black has a bonus of 30", "The card costs 1,200 points"]


def test_numbers_ignore_tags_and_list_numbering():
    assert number_check.numbers_in("1. Speed +20% costs 1,200 [S3] [C2]") == {"20", "1200"}
    assert number_check.numbers_in("- Growth 3.50 and 2nd place") == {"3.5"}


def test_policy_defaults_to_log_and_ignores_junk(monkeypatch):
    monkeypatch.delenv("LILYAI_ANALYST_NUMBER_CHECK", raising=False)
    assert number_check.policy() == "log"
    for value in ("off", "flag", "drop", "LOG"):
        monkeypatch.setenv("LILYAI_ANALYST_NUMBER_CHECK", value)
        assert number_check.policy() == value.lower()
    monkeypatch.setenv("LILYAI_ANALYST_NUMBER_CHECK", "banana")
    assert number_check.policy() == "log"


def test_an_unsupported_number_is_found_and_only_that_sentence_is_cut():
    result = number_check.check_reply("Kitasan has a bonus of 30. It also has 99 speed.", EVIDENCE)
    assert result.suspects == ["It also has 99 speed."] and result.numbers == ["99"]
    assert result.cleaned == "Kitasan has a bonus of 30."


def test_supported_numbers_pass_including_thousands_separators():
    result = number_check.check_reply("It costs 1,200 points and gives 30.", EVIDENCE)
    assert result.suspects == [] and result.cleaned == "It costs 1,200 points and gives 30."


def test_small_whole_numbers_are_ignored():
    result = number_check.check_reply("Here are my top 3 picks, 2 for speed.", EVIDENCE)
    assert result.suspects == []


def test_code_blocks_are_left_alone():
    reply = "Run this:\n```\nx = 12345\n```\nDone."
    assert number_check.check_reply(reply, EVIDENCE).suspects == []


def test_a_bullet_keeps_its_marker_when_a_sentence_is_cut():
    result = number_check.check_reply("- Bonus is 30. Made up 777.", EVIDENCE)
    assert result.cleaned == "- Bonus is 30."


def test_has_content():
    assert number_check.has_content("Kitasan has a bonus of 30.")
    assert not number_check.has_content(" [S1] ")


# ---- the chat workflow hook
@pytest.fixture()
def workflow():
    module = pytest.importorskip("LilyAiMain.MainService.Interaction.Workflows.chat_workflow")
    return module.ChatWorkflow.__new__(module.ChatWorkflow)


MESSAGES = [{"role": "system", "content": "Kitasan Black bonus 30"}, {"role": "tool", "content": "cost 1,200"},
            {"role": "assistant", "content": ""}]
REPLY = "Kitasan has 30 bonus. It also has 99 speed."


def test_analyst_log_mode_leaves_the_reply_alone(workflow, monkeypatch):
    monkeypatch.delenv("LILYAI_ANALYST_NUMBER_CHECK", raising=False)
    assert workflow._check_numbers("analyst", REPLY, MESSAGES) == REPLY


def test_analyst_drop_mode_removes_the_unsupported_sentence(workflow, monkeypatch):
    monkeypatch.setenv("LILYAI_ANALYST_NUMBER_CHECK", "drop")
    assert workflow._check_numbers("analyst", REPLY, MESSAGES) == "Kitasan has 30 bonus."


def test_analyst_flag_mode_adds_a_note(workflow, monkeypatch):
    monkeypatch.setenv("LILYAI_ANALYST_NUMBER_CHECK", "flag")
    out = workflow._check_numbers("analyst", REPLY, MESSAGES)
    assert out.startswith(REPLY) and "Heads up" in out and "99" in out


def test_other_modes_and_off_are_untouched(workflow, monkeypatch):
    monkeypatch.setenv("LILYAI_ANALYST_NUMBER_CHECK", "drop")
    for mode in ("chat", "manage", "simulator", ""):
        assert workflow._check_numbers(mode, REPLY, MESSAGES) == REPLY
    monkeypatch.setenv("LILYAI_ANALYST_NUMBER_CHECK", "off")
    assert workflow._check_numbers("analyst", REPLY, MESSAGES) == REPLY
