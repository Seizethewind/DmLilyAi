"""Number checks shared by the guide builder and Analyst Mode's chat replies. Standard library only.

A number in an answer should come from somewhere the writer was shown: a doc passage, a calculator result, the user's
own message. `numbers_in` is the one definition of "a number in this text" (tags like [S1] and list numbering don't
count). guide_builder.verify_section and sandbox_scripts/guide_ops.py use the same rules, and tests/test_guide_ops.py
checks that all three agree.

check_reply() looks at a finished chat reply and lists the sentences whose numbers appear in none of the evidence.
Small whole numbers (0-10) are ignored: "top 3", "2 steps" and the like are usually counting, not facts.

LILYAI_ANALYST_NUMBER_CHECK: off | log (default: only write to the log) | flag (add a note to the reply) | drop (remove
the sentences). The chat workflow applies it in Analyst Mode only.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass, field

TAG = re.compile(r"\[([SC]\d+)\]")
NUM = re.compile(r"(?<![\w.])(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?!\d)(?!(?:st|nd|rd|th)\b)")
LIST_MARK = re.compile(r"(?m)^\s*(?:[-*\u2022]|\d+[.)])\s+")
BULLET = re.compile(r"^\s*(?:[-*\u2022]|\d+[.)])\s+")

POLICIES = ("off", "log", "flag", "drop")


def canon(n: str) -> str:
    n = n.replace(",", "")
    return n.rstrip("0").rstrip(".") if "." in n else n


def numbers_in(text: str) -> set[str]:
    """Every number in `text` (ignoring [S1] / [C1] tags and list numbering), normalised for comparison."""
    text = LIST_MARK.sub("", TAG.sub(" ", text))
    return {canon(m) for m in NUM.findall(text)}


def policy() -> str:
    value = os.getenv("LILYAI_ANALYST_NUMBER_CHECK", "log").strip().lower()
    return value if value in POLICIES else "log"


def _trivial(n: str) -> bool:
    return n.isdigit() and int(n) <= 10


@dataclass
class NumberCheck:
    cleaned: str
    suspects: list[str] = field(default_factory=list)     # the sentences that were not supported
    numbers: list[str] = field(default_factory=list)      # the unsupported numbers in them


def check_reply(reply: str, evidence: list[str]) -> NumberCheck:
    """Split the reply into lines and sentences; a sentence is unsupported when it has a number (above 10) that none of
    the evidence texts contain. `cleaned` is the reply without those sentences."""
    allowed: set[str] = set()
    for text in evidence:
        allowed |= numbers_in(text)

    def unsupported(part: str) -> set[str]:
        return {n for n in numbers_in(part) if n not in allowed and not _trivial(n)}

    kept: list[str] = []
    suspects: list[str] = []
    bad_numbers: list[str] = []
    in_code = False
    for line in reply.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            kept.append(line.rstrip())
            continue
        if in_code or not line.strip():
            kept.append(line.rstrip())
            continue
        bad = unsupported(line)
        if not bad:
            kept.append(line.rstrip())
            continue
        parts = re.split(r"(?<=[.!?])\s+", line.strip())
        good = []
        for part in parts:
            miss = unsupported(part)
            if miss:
                suspects.append(part.strip())
                bad_numbers.extend(sorted(miss))
            else:
                good.append(part)
        if good:
            joined = " ".join(good)
            m = BULLET.match(line)
            if m and not BULLET.match(joined):
                joined = m.group(0) + joined
            kept.append(joined)
    cleaned = re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()
    return NumberCheck(cleaned, suspects, list(dict.fromkeys(bad_numbers)))


def has_content(text: str) -> bool:
    return len(re.sub(r"[\W_]+", "", TAG.sub("", text))) >= 15
