"""Skill catalog parsed from Umamusume/Skill/skill.md (the Unique / Rare / Normal tables).

Used by the career evaluator to classify the skills read off a trainee screenshot. Pure and stdlib-only.
Names are matched ignoring case, punctuation and the level mark (single or double circle): a vision model
often reads the circle as a letter "O", so "Corner Recovery O" must still find "Corner Recovery ◯".
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

SKILL_FILE = Path(__file__).resolve().parent / "Umamusume" / "Skill" / "skill.md"

# The "(Long)" / "(Front Runner)" / "(Dirt)" suffix on an effect line says where the skill works at all.
_SCOPE_WORDS = {
    "front runner": "front", "pace chaser": "pace", "late surger": "late", "end closer": "end",
    "sprint": "sprint", "mile": "mile", "medium": "medium", "long": "long", "dirt": "dirt", "turf": "turf",
}
_SCOPE_RE = re.compile(r"\(([A-Za-z ]+)\)\s*$")
# Trailing level mark: double circle = 2, single circle = 1, or a lone letter O / o / 0 after a space.
_MARK_RE = re.compile(r"\s*(?:([\u25ce\u229a\u25c9\u29be])|([\u25cb\u25ef\u26aa\u25e6\u2b58])|(?<=\s)([Oo0]))\s*$")


def split_mark(name: str) -> tuple[str, int]:
    """'Wet Conditions O' -> ('Wet Conditions', 1); 'Long Corners ◎' -> ('Long Corners', 2); no mark -> level 0."""
    s = " ".join(str(name).split())
    m = _MARK_RE.search(s)
    if not m:
        return s, 0
    return s[: m.start()].strip(), 2 if m.group(1) else 1


def skill_key(name: str) -> str:
    """Lookup key: lower-case letters and digits of the base name, plus '~1' / '~2' for the level mark."""
    base, level = split_mark(name)
    key = re.sub(r"[^a-z0-9]+", "", base.lower())
    if not key:
        return ""
    return f"{key}~{level}" if level else key


@dataclass(frozen=True)
class Skill:
    name: str
    tier: str  # unique | rare | normal
    kind: str  # Velocity, Acceleration, Speed - Other, Green Skill, Recovery, Debuff, Negative, Unique Skill
    text: str  # the effect line from the docs
    owner: str  # unique skills only: "Smart Falcon (LOVE☆4EVER)"
    level: int  # 0 none, 1 single circle, 2 double circle
    scope: tuple[str, ...]  # where it works: ("long",), ("front",), ("dirt",) ... empty = anywhere


def _scope(text: str) -> tuple[str, ...]:
    m = _SCOPE_RE.search(text.strip())
    if not m:
        return ()
    word = _SCOPE_WORDS.get(m.group(1).strip().lower())
    return (word,) if word else ()


def parse_markdown(text: str) -> list[Skill]:
    out: list[Skill] = []
    tier = ""
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            head = line[3:].strip().lower()
            tier = "unique" if head.startswith("unique") else "rare" if head.startswith("rare") else (
                "normal" if head.startswith("normal") else "")
            continue
        if not tier or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4 or cells[0].lower() == "skill name" or set(cells[0]) <= set("-: "):
            continue
        name, kind, acquisition = cells[0], cells[1], cells[-1]
        body = " | ".join(cells[2:-1])
        owner = acquisition[len("Innate:"):].strip() if acquisition.lower().startswith("innate:") else ""
        out.append(Skill(name, tier, kind, body, owner, split_mark(name)[1], _scope(body)))
    return out


class SkillCatalog:
    def __init__(self, skills: list[Skill]):
        self.skills = list(skills)
        self._exact: dict[str, Skill] = {}
        self._family: dict[str, list[Skill]] = {}
        for s in self.skills:
            key = skill_key(s.name)
            if not key:
                continue
            self._exact.setdefault(key, s)
            self._family.setdefault(key.split("~")[0], []).append(s)

    @classmethod
    def from_markdown(cls, text: str) -> "SkillCatalog":
        return cls(parse_markdown(text))

    def __len__(self) -> int:
        return len(self.skills)

    def find(self, name: str) -> Skill | None:
        key = skill_key(name)
        if not key:
            return None
        hit = self._exact.get(key)
        if hit:
            return hit
        family = self._family.get(key.split("~")[0])
        # Same skill family but a different circle mark: the mark was probably misread, take the lowest level.
        return min(family, key=lambda s: s.level) if family else None


_cache: tuple[float, SkillCatalog] | None = None


def default_catalog() -> SkillCatalog:
    """The catalog built from skill.md, reloaded when the file changes. Empty if the file is missing."""
    global _cache
    try:
        mtime = SKILL_FILE.stat().st_mtime
    except OSError:
        return SkillCatalog([])
    if _cache is None or _cache[0] != mtime:
        _cache = (mtime, SkillCatalog.from_markdown(SKILL_FILE.read_text(encoding="utf-8")))
    return _cache[1]
