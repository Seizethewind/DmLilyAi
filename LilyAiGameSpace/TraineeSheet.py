"""A trainee's details sheet (the in-game "Umamusume Details" screen) and the checks on what the vision model read.

The model only transcribes. Everything it returns is validated here before anything is judged: stats must be
whole numbers in range, aptitudes must be a letter S-G, skill names are cleaned and de-duplicated. Anything that
fails validation is dropped and noted, never guessed. Pure and stdlib-only.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from typing import Any

from .UmamusumeSkills import skill_key

STATS = ("speed", "stamina", "power", "guts", "wit")
SURFACES = ("turf", "dirt")
DISTANCES = ("sprint", "mile", "medium", "long")
STYLES = ("front", "pace", "late", "end")
APTITUDE_KEYS = SURFACES + DISTANCES + STYLES
GRADES = "SABCDEFG"
MAX_STAT = 2500  # highest cap any server uses; anything above is a misread
MAX_SKILLS = 80

_APTITUDE_ALIASES = {
    "turf": "turf", "dirt": "dirt",
    "sprint": "sprint", "short": "sprint", "mile": "mile", "medium": "medium", "mid": "medium", "middle": "medium",
    "long": "long",
    "front": "front", "frontrunner": "front", "runner": "front", "nige": "front",
    "pace": "pace", "pacechaser": "pace", "leader": "pace", "senkou": "pace",
    "late": "late", "latesurger": "late", "betweener": "late", "sashi": "late",
    "end": "end", "endcloser": "end", "closer": "end", "oikomi": "end",
}
_RARITY = {
    "gold": "gold", "yellow": "gold", "rare": "gold",
    "white": "white", "normal": "white", "common": "white", "grey": "white", "gray": "white",
    "unique": "unique", "rainbow": "unique",
    "negative": "negative", "purple": "negative",
}


@dataclass
class SkillRead:
    name: str
    rarity: str | None = None  # white | gold | unique | negative - from the row colour, only a fallback
    icon: str | None = None  # recovery | speed | acceleration | green | debuff | other - from the icon colour


@dataclass
class Sheet:
    trainee: str = ""
    outfit: str = ""
    rating: int | None = None
    stats: dict[str, int] = field(default_factory=dict)  # raw stat panel values
    aptitudes: dict[str, str] = field(default_factory=dict)  # key from APTITUDE_KEYS -> letter
    skills: list[SkillRead] = field(default_factory=list)
    unique_level: int | None = None
    skills_seen: bool = False  # a Skills tab screenshot was part of the input
    notes: list[str] = field(default_factory=list)

    @property
    def has_stats(self) -> bool:
        return all(k in self.stats for k in STATS)

    @property
    def is_empty(self) -> bool:
        return not (self.stats or self.aptitudes or self.skills or self.trainee)


# --------------------------------------------------------------------------- normalizers


def norm_aptitude_key(raw: Any) -> str | None:
    return _APTITUDE_ALIASES.get(re.sub(r"[^a-z]", "", str(raw).lower()))


def norm_grade(raw: Any) -> str | None:
    if raw is None:
        return None
    s = str(raw).strip().upper()[:1]
    return s if s and s in GRADES else None


def norm_int(raw: Any, lo: int, hi: int) -> int | None:
    if raw is None or isinstance(raw, bool):
        return None
    if isinstance(raw, (int, float)):
        n = int(raw)
    else:
        digits = re.sub(r"[^\d]", "", str(raw))
        if not digits:
            return None
        n = int(digits)
    return n if lo <= n <= hi else None


def _text(raw: Any, limit: int = 60) -> str:
    return " ".join(str(raw or "").split())[:limit]


_LVL_RE = re.compile(r"\s*lvl\.?\s*(\d+)\s*$", re.I)


def clean_skill_name(raw: Any) -> tuple[str, int | None]:
    """Strip bullets and a trailing 'Lvl 5' (a unique skill's level). Returns (name, level or None)."""
    s = " ".join(str(raw or "").split())
    s = re.sub(r"^[\-*\u2022\d.)\s]+(?=[A-Za-z#\"'(])", "", s)
    m = _LVL_RE.search(s)
    level = int(m.group(1)) if m else None
    if m:
        s = s[: m.start()]
    return s.strip()[:80], level


def _icon(raw: Any) -> str | None:
    s = str(raw or "").lower()
    if not s:
        return None
    if any(w in s for w in ("recover", "heal", "stamina", "sparkle")):
        return "recovery"
    if any(w in s for w in ("accel",)):
        return "acceleration"
    if any(w in s for w in ("speed", "velocity")):
        return "speed"
    if "green" in s or "passive" in s:
        return "green"
    if "debuff" in s:
        return "debuff"
    return "other"


# --------------------------------------------------------------------------- extraction -> Sheet


def extract_json(text: str) -> dict | None:
    """The first JSON object in a model reply, tolerating <think> blocks and code fences."""
    s = re.sub(r"<think>.*?</think>", "", text or "", flags=re.S)
    s = re.sub(r"```(?:json)?", "", s)
    start, end = s.find("{"), s.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        data = json.loads(s[start:end + 1])
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def sheet_from_extraction(data: dict[str, Any]) -> Sheet | None:
    """Validate one screenshot's extraction. None if the model says it is not the trainee details screen."""
    if data.get("is_trainee_details_screen") is False:
        return None
    sheet = Sheet()

    trainee = data.get("trainee") if isinstance(data.get("trainee"), dict) else {}
    sheet.trainee = _text(trainee.get("name"))
    sheet.outfit = _text(trainee.get("outfit"))
    sheet.rating = norm_int(trainee.get("rating"), 1, 200_000)

    raw_stats = data.get("stats") if isinstance(data.get("stats"), dict) else {}
    for key in STATS:
        value = norm_int(raw_stats.get(key), 1, MAX_STAT)
        if value is not None:
            sheet.stats[key] = value
        elif raw_stats.get(key) is not None:
            sheet.notes.append(f"I couldn't read {key.title()} cleanly, so it was left out.")

    raw_apt = data.get("aptitudes") if isinstance(data.get("aptitudes"), dict) else {}
    for raw_key, raw_grade in raw_apt.items():
        key = norm_aptitude_key(raw_key)
        grade = norm_grade(raw_grade)
        if key and grade:
            sheet.aptitudes[key] = grade

    if "skill" in str(data.get("active_tab") or "").lower():
        sheet.skills_seen = True
        raw_skills = data.get("skills") if isinstance(data.get("skills"), list) else []
        seen: set[str] = set()
        for item in raw_skills[:MAX_SKILLS]:
            if isinstance(item, dict):
                raw_name, rarity, icon = item.get("name"), item.get("rarity"), item.get("icon")
            else:
                raw_name, rarity, icon = item, None, None
            name, level = clean_skill_name(raw_name)
            key = skill_key(name)
            if not key or key in seen:
                continue
            seen.add(key)
            if level is not None:
                sheet.unique_level = level
            sheet.skills.append(SkillRead(name, _RARITY.get(str(rarity or "").strip().lower()), _icon(icon)))

    uncertain = data.get("uncertain") if isinstance(data.get("uncertain"), list) else []
    sheet.notes += [f"Reader note: {_text(u, 120)}" for u in uncertain[:6] if _text(u)]
    return sheet


def merge_sheets(sheets: list[Sheet]) -> Sheet:
    """Combine the screenshots of one trainee. First reading wins; disagreements are noted, never averaged."""
    out = Sheet()
    seen: set[str] = set()
    for s in sheets:
        if s.trainee:
            if not out.trainee:
                out.trainee, out.outfit = s.trainee, s.outfit
            elif s.trainee.lower() != out.trainee.lower():
                out.notes.append(f"Screenshots show different trainees ({out.trainee} / {s.trainee}); using {out.trainee}.")
        if out.rating is None:
            out.rating = s.rating
        for k, v in s.stats.items():
            if k not in out.stats:
                out.stats[k] = v
            elif out.stats[k] != v:
                out.notes.append(f"{k.title()} was read as {out.stats[k]} and {v} - please double-check it.")
        for k, g in s.aptitudes.items():
            if k not in out.aptitudes:
                out.aptitudes[k] = g
            elif out.aptitudes[k] != g:
                out.notes.append(f"{k.title()} aptitude was read as {out.aptitudes[k]} and {g} - please double-check it.")
        if s.skills_seen:
            out.skills_seen = True
        if s.unique_level is not None:
            out.unique_level = s.unique_level
        for sk in s.skills:
            key = skill_key(sk.name)
            if key and key not in seen:
                seen.add(key)
                out.skills.append(sk)
        out.notes += [n for n in s.notes if n not in out.notes]
    return out
