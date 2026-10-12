#!/usr/bin/env python3
"""
Umamusume data taxonomy: one place that names the categories the rest of the project already uses.

What this is
------------
Enums, alias tables and small classifier functions for the things Umamusume data is organised by:
running styles, surfaces, distance types, ground, aptitudes, stats, support card types, race phases, and
the skill taxonomy (tier, effect category, scope, level mark, simulator status, condition kind).
It also lists the entity kinds (trainee, support card, skill, ...) and the mechanics domains, as
definitions only.

What this is not
----------------
It holds no game data, reads no files and has no dependencies beyond the standard library. It does
not replace Simulator.py, UmamusumeCatalog.py or UmamusumeSkills.py; those keep their own constants.
tests/test_umamusume_taxonomy.py checks that the two sides agree, so a drift fails a test instead of
silently changing results.

Conventions
-----------
* Canonical names are the Global server's official English names (Wit, Friend, Firm/Good/Soft/Heavy,
  Front Runner / Pace Chaser / Late Surger / End Closer). Upstream/fan names stay accepted as aliases.
* Integer values equal the integers the upstream datamined data and Simulator.py already use, so
  existing JSON stays valid. String values equal the strings UmamusumeCatalog / UmamusumeSkills use.
* Every enum has .parse(value): accepts a member, its integer value, its name or an alias (case,
  spaces and punctuation ignored) and raises ValueError with close-match suggestions otherwise.
* Nothing is invented: where the project has no source for a mapping, the function returns None
  (or the id is reported as unmapped) instead of guessing.

KNOWN DIVERGENCE (Ground)
-------------------------
Global calls ground 1 "Firm", 2 "Good", 3 "Soft", 4 "Heavy". Upstream (and Simulator.GROUND_NAMES)
calls them good/yielding/soft/heavy, so the word "good" means 1 there but 2 here. Ground.parse("good")
follows Global (2). Use Ground.from_upstream_name() to read upstream names. Simulator.py is unchanged.
"""
from __future__ import annotations

import difflib
import re
import unicodedata
from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Iterable, Mapping

TAXONOMY_VERSION = 1


# --------------------------------------------------------------------------
# Parsing support
# --------------------------------------------------------------------------
def _key(text) -> str:
    """Comparison key: ignores case, width, spaces and punctuation ('Front-Runner' == 'front runner')."""
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFKC", str(text)).casefold())


_INT_RE = re.compile(r"\s*-?\d+\s*")
_TABLES: dict[type, dict[str, Enum]] = {}


def _table(cls) -> dict[str, Enum]:
    t = _TABLES.get(cls)
    if t is None:
        t = {}
        for m in cls:
            t[_key(m.name)] = m
            if isinstance(m.value, str):
                t.setdefault(_key(m.value), m)
        for alias, name in _ALIASES.get(cls, {}).items():
            t[_key(alias)] = cls[name]
        _TABLES[cls] = t
    return t


class _Parse:
    """Mixin giving an Enum a tolerant .parse()."""

    @classmethod
    def parse(cls, value):
        if isinstance(value, cls):
            return value
        if isinstance(value, bool):
            raise ValueError(f"Unknown {cls.__name__} {value!r}")
        if isinstance(value, int) or (isinstance(value, str) and _INT_RE.fullmatch(value)):
            try:
                return cls(int(value))
            except ValueError:
                pass
        table = _table(cls)
        hit = table.get(_key(value))
        if hit is not None:
            return hit
        near = difflib.get_close_matches(_key(value), list(table), n=3, cutoff=0.6)
        names = list(dict.fromkeys(table[k].name for k in near))
        hint = f" Did you mean: {', '.join(names)}?" if names else ""
        raise ValueError(f"Unknown {cls.__name__} {value!r}.{hint}")


# --------------------------------------------------------------------------
# Character and race basics
# --------------------------------------------------------------------------
class Stat(_Parse, str, Enum):
    """The five trainee stats. Values match UmamusumeCatalog.STATS; WIT is the Global name for 'wisdom'."""
    SPEED = "speed"
    STAMINA = "stamina"
    POWER = "power"
    GUTS = "guts"
    WIT = "wit"

    @property
    def upstream_id(self) -> int:
        """1-5, the stat ids used by upstream skill effects (types 1-5)."""
        return list(Stat).index(self) + 1

    @property
    def sim_key(self) -> str:
        """The key Simulator.py configs and veteran JSON use ('wisdom' for WIT)."""
        return "wisdom" if self is Stat.WIT else self.value

    @classmethod
    def from_upstream_id(cls, n: int) -> "Stat":
        members = list(cls)
        if not 1 <= int(n) <= len(members):
            raise ValueError(f"Unknown stat id {n!r} (expected 1-5)")
        return members[int(n) - 1]


class RunningStyle(_Parse, IntEnum):
    """Integers match upstream / Simulator.py (1 front ... 5 runaway)."""
    FRONT = 1
    PACE = 2
    LATE = 3
    END = 4
    RUNAWAY = 5

    @property
    def label(self) -> str:
        return _STYLE_LABELS[self.value]

    @property
    def condition_group(self) -> "RunningStyle":
        """Skill conditions treat Runaway (Oonige) as a Front Runner."""
        return RunningStyle.FRONT if self is RunningStyle.RUNAWAY else self

    @property
    def scope_word(self) -> str:
        """The word skill.md puts in '(Front Runner)' style suffixes, as UmamusumeSkills reports it."""
        return {1: "front", 2: "pace", 3: "late", 4: "end"}[self.condition_group.value]


_STYLE_LABELS = {1: "Front Runner", 2: "Pace Chaser", 3: "Late Surger", 4: "End Closer", 5: "Runaway"}


class Surface(_Parse, IntEnum):
    TURF = 1
    DIRT = 2


class DistanceType(_Parse, IntEnum):
    """1 sprint, 2 mile, 3 medium, 4 long (course data's distance_type)."""
    SPRINT = 1
    MILE = 2
    MEDIUM = 3
    LONG = 4

    @classmethod
    def from_meters(cls, meters: int) -> "DistanceType":
        """Convenience for the standard bands; a course's own distance_type is authoritative."""
        m = int(meters)
        if m <= 1400:
            return cls.SPRINT
        if m <= 1800:
            return cls.MILE
        if m <= 2400:
            return cls.MEDIUM
        return cls.LONG


class Ground(_Parse, IntEnum):
    """Global names. See the module docstring: upstream's 'good' is FIRM here."""
    FIRM = 1
    GOOD = 2
    SOFT = 3
    HEAVY = 4

    @classmethod
    def from_upstream_name(cls, value) -> "Ground":
        """Reads Simulator.GROUND_NAMES-style names (good/yielding/soft/heavy) or 1-4."""
        if isinstance(value, int) and not isinstance(value, bool) or (isinstance(value, str) and _INT_RE.fullmatch(value)):
            return cls(int(value))
        try:
            return {"good": cls.FIRM, "yielding": cls.GOOD, "soft": cls.SOFT, "heavy": cls.HEAVY}[_key(value)]
        except KeyError:
            raise ValueError(f"Unknown upstream ground name {value!r} (good, yielding, soft, heavy)") from None


class Aptitude(_Parse, IntEnum):
    """Aptitude letter as an index into Simulator.py's tables: S=0 (best) ... G=7."""
    S = 0
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7

    @property
    def letter(self) -> str:
        return self.name


class Mood(_Parse, IntEnum):
    """-2 .. 2, as Simulator.py's 'mood'. The simulator's 'motivation' condition value is value + 3."""
    AWFUL = -2
    BAD = -1
    NORMAL = 0
    GOOD = 1
    GREAT = 2

    @property
    def motivation(self) -> int:
        return self.value + 3


class Phase(_Parse, IntEnum):
    """Race phases as skill conditions number them: 0 early, 1 middle, 2 late, 3 last spurt."""
    EARLY = 0
    MIDDLE = 1
    LATE = 2
    LAST_SPURT = 3

    def span(self, distance: float) -> tuple[float, float]:
        """(start, end) in metres on a course of this length; same arithmetic as Simulator.Env."""
        d = float(distance)
        starts = (0.0, d / 6, d * 2 / 3, d * 5 / 6)
        ends = (d / 6, d * 2 / 3, d * 5 / 6, d)
        return starts[self.value], ends[self.value]


class Server(_Parse, str, Enum):
    GLOBAL = "global"
    JP = "jp"


# --------------------------------------------------------------------------
# Support cards
# --------------------------------------------------------------------------
class SupportType(_Parse, str, Enum):
    """Values match UmamusumeCatalog.TYPE_ORDER. The wiki calls FRIEND 'Pal'."""
    SPEED = "Speed"
    STAMINA = "Stamina"
    POWER = "Power"
    GUTS = "Guts"
    WIT = "Wit"
    FRIEND = "Friend"
    GROUP = "Group"

    @property
    def stat(self) -> Stat | None:
        """The stat a Speed/Stamina/Power/Guts/Wit card trains; None for Friend and Group."""
        try:
            return Stat(self.value.lower())
        except ValueError:
            return None


class SupportRarity(_Parse, str, Enum):
    SSR = "SSR"
    SR = "SR"
    R = "R"


# --------------------------------------------------------------------------
# Skills
# --------------------------------------------------------------------------
class SkillTier(_Parse, str, Enum):
    """How a skill is obtained / its colour. normal, rare and unique match UmamusumeSkills.Skill.tier."""
    NORMAL = "normal"                      # white
    RARE = "rare"                          # gold
    UNIQUE = "unique"                      # a character's own unique skill
    INHERITED_UNIQUE = "inherited_unique"  # the weaker copy passed down with a Green Spark; Game8 treats it as Normal
    NEGATIVE = "negative"                  # purple, gained by losing races


class SkillEffect(_Parse, str, Enum):
    """What a skill does. Game8's 'Speed - Other' is POSITIONING; its 'Green Skill' is PASSIVE."""
    VELOCITY = "velocity"
    ACCELERATION = "acceleration"
    RECOVERY = "recovery"
    POSITIONING = "positioning"   # position, navigation, passing, field of view, slow start, slopes
    PASSIVE = "passive"           # stat / performance boosts (green)
    DEBUFF = "debuff"             # effects aimed at other runners


class LevelMark(_Parse, IntEnum):
    """The mark on a skill name: none, single circle, double circle, or the cross on negative skills."""
    NEGATIVE = -1
    NONE = 0
    SINGLE = 1
    DOUBLE = 2

    @classmethod
    def from_glyph(cls, glyph: str) -> "LevelMark":
        g = unicodedata.normalize("NFKC", str(glyph)).strip()
        if g in _DOUBLE_GLYPHS:
            return cls.DOUBLE
        if g in _SINGLE_GLYPHS:
            return cls.SINGLE
        if g in _CROSS_GLYPHS:
            return cls.NEGATIVE
        if g == "":
            return cls.NONE
        raise ValueError(f"Unknown level mark {glyph!r}")


_DOUBLE_GLYPHS = frozenset("◎⊚◉⦾")          # ◎ ⊚ ◉ ⦾
_SINGLE_GLYPHS = frozenset("○◯〇⚪◦⭘")  # ○ ◯ 〇 ⚪ ◦ ⭘
_CROSS_GLYPHS = frozenset("×✕✖╳x")          # × ✕ ✖ ╳ x


class SimStatus(_Parse, str, Enum):
    """Whether Simulator.py can model a skill. An implementation fact, not a game category."""
    OK = "ok"
    APPROX = "approx"
    UNSUPPORTED = "unsupported"
    INACTIVE = "inactive"


class ConditionKind(_Parse, str, Enum):
    """How Simulator.py treats a skill-condition key (the 'trigger context' of a skill)."""
    STATIC = "static"      # decided before the race (course, ground, stats, season ...)
    REGION = "region"      # a stretch of the course (phase, corner, straight, slope, distance)
    DYNAMIC = "dynamic"    # depends on the live race (HP, last spurt, skills used so far)
    OPPONENT = "opponent"  # depends on other runners; the simulator assumes it true


# Copied from Simulator.compile_atom / OPPONENT_PREFIXES; tests keep them in step.
OPPONENT_PREFIXES = (
    "order", "change_order", "bashin_diff", "overtake", "is_overtake", "blocked", "near_count",
    "distance_diff", "infront_near", "behind_near", "is_behind", "is_move_lane", "lane_type",
    "compete", "is_surrounded", "visiblehorse", "same_skill_horse", "running_style_count",
    "running_style_temptation", "is_hp_empty_onetime_other", "personal_space", "mate_",
)
_CONDITION_KEYS: dict[ConditionKind, frozenset[str]] = {
    ConditionKind.STATIC: frozenset({
        "distance_type", "ground_type", "ground_condition", "track_id", "course_distance", "rotation",
        "is_basis_distance", "motivation", "season", "weather", "time", "grade", "popularity",
        "is_dirtgrade", "always", "base_speed", "base_stamina", "base_power", "base_guts", "base_wiz",
        "temptation_count", "is_badstart", "running_style"}),
    ConditionKind.REGION: frozenset({
        "phase", "phase_firsthalf", "phase_laterhalf", "phase_firstquarter", "phase_random",
        "phase_firsthalf_random", "phase_laterhalf_random", "phase_firstquarter_random",
        "distance_rate", "distance_rate_after_random", "remain_distance", "corner", "corner_random",
        "all_corner_random", "is_finalcorner", "is_finalcorner_random", "is_finalcorner_laterhalf",
        "is_last_straight", "is_last_straight_onetime", "straight_random", "phase_corner_random",
        "phase_straight_random", "slope", "up_slope_random", "down_slope_random"}),
    ConditionKind.DYNAMIC: frozenset({
        "is_lastspurt", "lastspurt", "accumulatetime", "hp_per", "activate_count_all",
        "activate_count_start", "activate_count_middle", "activate_count_end_after",
        "activate_count_heal", "is_used_skill_id"}),
}


def classify_condition_key(key: str) -> ConditionKind | None:
    """Kind of a condition key such as 'phase' or 'order_rate'; None if the project does not know it."""
    k = str(key).strip()
    for kind, keys in _CONDITION_KEYS.items():
        if k in keys:
            return kind
    return ConditionKind.OPPONENT if k.startswith(OPPONENT_PREFIXES) else None


# Skill.md '(Long)' / '(Front Runner)' suffixes, as UmamusumeSkills reports them.
SKILL_SCOPE_WORDS: dict[str, Enum] = {
    "front": RunningStyle.FRONT, "pace": RunningStyle.PACE, "late": RunningStyle.LATE, "end": RunningStyle.END,
    "sprint": DistanceType.SPRINT, "mile": DistanceType.MILE, "medium": DistanceType.MEDIUM,
    "long": DistanceType.LONG, "turf": Surface.TURF, "dirt": Surface.DIRT,
}


def scope_member(word: str) -> Enum:
    """The running style, distance type or surface a skill scope word stands for."""
    try:
        return SKILL_SCOPE_WORDS[str(word).strip().lower()]
    except KeyError:
        raise ValueError(f"Unknown skill scope word {word!r}") from None


# Game8 'Skill Type' labels -> (tier, effect). None means the label does not say.
GAME8_SKILL_KINDS: dict[str, tuple[SkillTier | None, SkillEffect | None]] = {
    "Unique Skill": (SkillTier.UNIQUE, None),
    "Velocity": (None, SkillEffect.VELOCITY),
    "Acceleration": (None, SkillEffect.ACCELERATION),
    "Speed - Other": (None, SkillEffect.POSITIONING),
    "Green Skill": (None, SkillEffect.PASSIVE),
    "Recovery": (None, SkillEffect.RECOVERY),
    "Debuff": (None, SkillEffect.DEBUFF),
    "Negative": (SkillTier.NEGATIVE, None),
}
_GAME8_BY_KEY = {_key(label): pair for label, pair in GAME8_SKILL_KINDS.items()}


def classify_game8_kind(label: str) -> tuple[SkillTier | None, SkillEffect | None]:
    try:
        return _GAME8_BY_KEY[_key(label)]
    except KeyError:
        raise ValueError(f"Unknown Game8 skill type {label!r}") from None


# Upstream effect type ids, only those the project already confirms (build_sim_data.SUPPORTED_EFFECTS):
# 1-5 stat up, 9 HP recovery, 21 / 22 current speed, 27 target speed, 31 acceleration.
# Other ids are reported as unmapped, not guessed.
UPSTREAM_EFFECT_CATEGORY: dict[int, SkillEffect] = {
    1: SkillEffect.PASSIVE, 2: SkillEffect.PASSIVE, 3: SkillEffect.PASSIVE, 4: SkillEffect.PASSIVE,
    5: SkillEffect.PASSIVE, 9: SkillEffect.RECOVERY, 21: SkillEffect.VELOCITY, 22: SkillEffect.VELOCITY,
    27: SkillEffect.VELOCITY, 31: SkillEffect.ACCELERATION,
}


def classify_effect_types(types: Iterable[int]) -> frozenset[SkillEffect]:
    return frozenset(UPSTREAM_EFFECT_CATEGORY[t] for t in types if t in UPSTREAM_EFFECT_CATEGORY)


def unmapped_effect_types(types: Iterable[int]) -> frozenset[int]:
    return frozenset(t for t in types if t not in UPSTREAM_EFFECT_CATEGORY)


def is_inherited_skill_id(skill_id) -> bool:
    """The repo's existing heuristic (tools/build_skill_aliases.py): six digits starting with 9."""
    s = str(skill_id)
    return len(s) == 6 and s.startswith("9")


@dataclass(frozen=True)
class SkillClass:
    tier: SkillTier | None             # None = the data does not say
    effects: frozenset                 # frozenset[SkillEffect]; may be empty
    partial: bool                      # tools/sim_data dropped some effects (other runners / unsupported)
    unmapped_types: frozenset = frozenset()   # effect type ids present but not mapped


def classify_skill(skill_id, entry: Mapping | None = None, game8_kind: str | None = None) -> SkillClass:
    """Classify one skill from whatever is known.

    skill_id   upstream id (decides INHERITED_UNIQUE).
    entry      its tools/sim_data/skills.json entry (rarity, alternatives[].effects[].type, partial).
    game8_kind its Game8 'Skill Type' label (from UmamusumeSkills.Skill.kind), if known.
    Only rarity 1 and 2 are mapped to a tier from the entry; other rarities stay None unless Game8 says.
    Debuff and positioning effects are not in the slimmed data, so they come only from game8_kind.
    """
    entry = entry or {}
    tier: SkillTier | None = None
    effects: set[SkillEffect] = set()
    if game8_kind:
        g_tier, g_effect = classify_game8_kind(game8_kind)
        tier = g_tier
        if g_effect:
            effects.add(g_effect)
    if is_inherited_skill_id(skill_id):
        tier = SkillTier.INHERITED_UNIQUE
    elif tier is None:
        tier = {1: SkillTier.NORMAL, 2: SkillTier.RARE}.get(entry.get("rarity"))
    types = [e.get("type") for alt in entry.get("alternatives", []) for e in alt.get("effects", [])]
    types = [t for t in types if isinstance(t, int)]
    effects |= classify_effect_types(types)
    return SkillClass(tier, frozenset(effects), bool(entry.get("partial")), unmapped_effect_types(types))


# --------------------------------------------------------------------------
# Entities and mechanics (definitions only)
# --------------------------------------------------------------------------
class EntityKind(_Parse, str, Enum):
    """Things that have ids. Mirrors the Database sections of the source sites."""
    TRAINEE = "trainee"
    SUPPORT_CARD = "support_card"
    SKILL = "skill"
    RACETRACK = "racetrack"
    COURSE = "course"
    RACE = "race"
    SCENARIO = "scenario"
    EVENT = "event"
    FACTOR = "factor"
    ITEM = "item"
    EPITHET = "epithet"


# Where each kind lives in this repo today; None = not stored as structured data yet.
ENTITY_HOMES: dict[EntityKind, tuple[str, ...] | None] = {
    EntityKind.TRAINEE: ("LilyAiGameSpace/Umamusume/Character",),
    EntityKind.SUPPORT_CARD: ("LilyAiGameSpace/Umamusume/Support Cards",),
    EntityKind.SKILL: ("LilyAiGameSpace/Umamusume/Skill/skill.md",
                       "LilyAiGameSpace/Umamusume/Skill/skill_library.md",
                       "tools/sim_data/skills.json", "tools/sim_data/skill_aliases.json"),
    EntityKind.COURSE: ("tools/sim_data/courses.json",),
    EntityKind.RACETRACK: None, EntityKind.RACE: None, EntityKind.SCENARIO: None, EntityKind.EVENT: None,
    EntityKind.FACTOR: None, EntityKind.ITEM: None, EntityKind.EPITHET: None,
}


class MechanicDomain(_Parse, str, Enum):
    CAREER = "career"
    RACE = "race"
    MODE = "mode"
    ECONOMY = "economy"


MECHANICS: dict[MechanicDomain, tuple[str, ...]] = {
    MechanicDomain.CAREER: ("training", "stat_growth", "energy_and_mood", "inheritance", "affinity",
                            "objectives", "scenarios", "events", "support_deck"),
    MechanicDomain.RACE: ("phases", "running_styles", "stamina_and_hp", "last_spurt", "position_keep",
                          "rushed", "course_geometry", "ground_and_weather", "skill_activation"),
    MechanicDomain.MODE: ("champions_meeting", "team_trials", "league_of_heroes", "monthly_match"),
    MechanicDomain.ECONOMY: ("carats", "gacha", "items", "missions"),
}


# --------------------------------------------------------------------------
# Aliases (alias -> member name). Names and string values are accepted automatically.
# --------------------------------------------------------------------------
_ALIASES: dict[type, dict[str, str]] = {
    Stat: {"spd": "SPEED", "stam": "STAMINA", "sta": "STAMINA", "pow": "POWER", "pwr": "POWER",
           "wisdom": "WIT", "wiz": "WIT"},
    RunningStyle: {"nige": "FRONT", "runner": "FRONT", "front runner": "FRONT",
                   "senkou": "PACE", "pace chaser": "PACE",
                   "sasi": "LATE", "sashi": "LATE", "late surger": "LATE",
                   "oikomi": "END", "end closer": "END", "closer": "END",
                   "oonige": "RUNAWAY"},
    Surface: {"grass": "TURF"},
    DistanceType: {"short": "SPRINT", "med": "MEDIUM", "mid": "MEDIUM", "middle": "MEDIUM"},
    Ground: {"yielding": "GOOD"},
    Phase: {"opening": "EARLY", "start": "EARLY", "mid": "MIDDLE", "spurt": "LAST_SPURT"},
    Server: {"en": "GLOBAL", "english": "GLOBAL", "japan": "JP", "japanese": "JP"},
    SupportType: {"spd": "SPEED", "stam": "STAMINA", "sta": "STAMINA", "pow": "POWER", "pwr": "POWER",
                  "wiz": "WIT", "wisdom": "WIT", "pal": "FRIEND"},
    SkillTier: {"white": "NORMAL", "gold": "RARE", "purple": "NEGATIVE", "inherited": "INHERITED_UNIQUE"},
    SkillEffect: {"speed other": "POSITIONING", "speed - other": "POSITIONING", "green": "PASSIVE",
                  "green skill": "PASSIVE", "speed": "VELOCITY", "accel": "ACCELERATION", "heal": "RECOVERY"},
}
