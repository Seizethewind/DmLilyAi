"""Umamusume taxonomy (LilyAiGameSpace/Umamusume/Taxonomy.py) and its agreement with the code that already
holds the same constants: Simulator.py, UmamusumeCatalog.py, UmamusumeSkills.py and the docs engine.

No network, no API keys. Tests that need real repo data skip themselves when it is missing.

Run:  python -m unittest tests.test_umamusume_taxonomy -v
"""
import ast
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from LilyAiGameSpace.Umamusume import Taxonomy as T  # noqa: E402
from LilyAiGameSpace.Umamusume.Simulation import Simulator as S  # noqa: E402
from LilyAiGameSpace.Umamusume import UmamusumeCatalog as C  # noqa: E402
from LilyAiGameSpace.Umamusume import UmamusumeSkills as K  # noqa: E402

TAXONOMY_PY = ROOT / "LilyAiGameSpace" / "Umamusume" / "Taxonomy.py"
TAXONOMY_MD = ROOT / "LilyAiGameSpace" / "Umamusume" / "Taxonomy" / "Taxonomy.md"
PUBLIC_ENUMS = [
    T.Stat, T.RunningStyle, T.Surface, T.DistanceType, T.Ground, T.Aptitude, T.Mood, T.Phase, T.Server,
    T.SupportType, T.SupportRarity, T.SkillTier, T.SkillEffect, T.LevelMark, T.SimStatus, T.ConditionKind,
    T.EntityKind, T.MechanicDomain,
]


class ParsingTests(unittest.TestCase):
    def test_every_member_parses_by_name_value_and_case(self):
        for enum in PUBLIC_ENUMS:
            for m in enum:
                self.assertIs(enum.parse(m), m)
                self.assertIs(enum.parse(m.name), m, f"{enum.__name__}.{m.name}")
                self.assertIs(enum.parse(m.name.lower()), m)
                self.assertIs(enum.parse(m.value), m)

    def test_unknown_values_raise_with_a_suggestion(self):
        with self.assertRaises(ValueError) as cm:
            T.RunningStyle.parse("pace chasr")
        self.assertIn("PACE", str(cm.exception))
        for bad in ("", "zzz", None, True, 99):
            with self.assertRaises(ValueError, msg=repr(bad)):
                T.RunningStyle.parse(bad)

    def test_punctuation_and_spacing_are_ignored(self):
        self.assertIs(T.RunningStyle.parse("Front-Runner"), T.RunningStyle.FRONT)
        self.assertIs(T.RunningStyle.parse(" Late  Surger "), T.RunningStyle.LATE)
        self.assertIs(T.Phase.parse("last spurt"), T.Phase.LAST_SPURT)

    def test_numeric_strings_and_negative_numbers(self):
        self.assertIs(T.Ground.parse("3"), T.Ground.SOFT)
        self.assertIs(T.Mood.parse(-2), T.Mood.AWFUL)
        self.assertIs(T.Mood.parse("-1"), T.Mood.BAD)
        self.assertIs(T.Mood.parse("2"), T.Mood.GREAT)


class AgreementWithSimulatorTests(unittest.TestCase):
    def test_running_style_names_resolve_to_the_same_numbers(self):
        for name, num in S.STYLE_NAMES.items():
            self.assertEqual(int(T.RunningStyle.parse(name)), num, name)
        for n in range(1, 6):
            self.assertEqual(int(T.RunningStyle.parse(n)), S.parse_style(n))

    def test_stats_match_the_simulator_effect_ids(self):
        for sid, sim_name in S.SKILL_EFFECT_STAT.items():
            stat = T.Stat.from_upstream_id(sid)
            self.assertEqual(stat.sim_key, sim_name)
            self.assertEqual(stat.upstream_id, sid)
            self.assertIs(T.Stat.parse(sim_name), stat)

    def test_aptitude_letters(self):
        for i, letter in enumerate("SABCDEFG"):
            self.assertEqual(int(T.Aptitude.parse(letter)), S.parse_apt(letter))
            self.assertEqual(int(T.Aptitude.parse(letter.lower())), i)

    def test_ground_numbers_match_and_good_is_a_documented_divergence(self):
        for n in range(1, 5):
            self.assertEqual(int(T.Ground.parse(n)), S.parse_ground(n))
        for name in ("yielding", "soft", "heavy"):
            self.assertEqual(int(T.Ground.parse(name)), S.GROUND_NAMES[name], name)
        # Simulator calls ground 1 "good"; Global calls it "Firm" and calls 2 "Good". Taxonomy follows Global.
        self.assertEqual(S.GROUND_NAMES["good"], 1)
        self.assertIs(T.Ground.parse("good"), T.Ground.GOOD)
        self.assertIs(T.Ground.parse("firm"), T.Ground.FIRM)
        # ...and the upstream names are still readable through the explicit path.
        for name, num in S.GROUND_NAMES.items():
            self.assertEqual(int(T.Ground.from_upstream_name(name)), num, name)

    def test_phase_spans_match_the_simulator_env(self):
        course = {"distance": 2400, "corners": [], "straights": [], "slopes": []}
        env = S.Env(course, None, None, 1, 2, dict(S.DEFAULT_PARAMS))
        for p in T.Phase:
            start, end = p.span(2400)
            self.assertAlmostEqual(start, env.ph_start[p.value])
            self.assertAlmostEqual(end, env.ph_end[p.value])

    def test_opponent_prefixes_are_the_same(self):
        self.assertEqual(T.OPPONENT_PREFIXES, S.OPPONENT_PREFIXES)

    def test_every_listed_condition_key_is_handled_with_the_same_kind(self):
        base = S.Horse(1000, 1000, 1000, 1000, 1000, 2, 1, 1, 1)
        course = {"distance": 2000, "distance_type": 3, "surface": 1, "turn": 1, "track_id": 10006,
                  "course_set_status": [], "corners": [{"start": 400, "length": 200}, {"start": 1400, "length": 200}],
                  "straights": [{"start": 0, "end": 400}, {"start": 600, "end": 1400}],
                  "slopes": [{"start": 700, "length": 100, "slope": 15}]}
        env = S.Env(course, base, base, 1, 2, dict(S.DEFAULT_PARAMS))
        expect = {"static": T.ConditionKind.STATIC, "region": T.ConditionKind.REGION,
                  "region_dyn": T.ConditionKind.DYNAMIC, "dyn": T.ConditionKind.DYNAMIC}
        for kind, keys in T._CONDITION_KEYS.items():
            for key in sorted(keys):
                got = S.compile_atom(key, "==", 1, env)[0]
                self.assertNotEqual(got, "unsupported", f"Simulator cannot handle '{key}'")
                self.assertEqual(expect[got], kind, key)
        for prefix in T.OPPONENT_PREFIXES:
            self.assertEqual(S.compile_atom(prefix + "x", "==", 1, env)[0], "opponent", prefix)
            self.assertIs(T.classify_condition_key(prefix + "x"), T.ConditionKind.OPPONENT)
        self.assertIsNone(T.classify_condition_key("no_such_key"))

    def test_sim_status_values_are_the_strings_the_simulator_uses(self):
        self.assertEqual({m.value for m in T.SimStatus}, {"ok", "approx", "unsupported", "inactive"})


class AgreementWithCatalogTests(unittest.TestCase):
    def test_stats_and_support_types(self):
        self.assertEqual(tuple(m.value for m in T.Stat), C.STATS)
        self.assertEqual(tuple(m.value for m in T.SupportType), C.TYPE_ORDER)
        self.assertEqual(tuple(m.value for m in T.SupportRarity), C.RARITIES)

    def test_catalog_type_words_resolve_to_the_same_support_type(self):
        for word, canonical in C._TYPE_WORDS.items():
            self.assertEqual(T.SupportType.parse(word).value, canonical, word)

    def test_stat_for_support_type(self):
        self.assertIs(T.SupportType.WIT.stat, T.Stat.WIT)
        self.assertIsNone(T.SupportType.FRIEND.stat)
        self.assertIsNone(T.SupportType.GROUP.stat)

    def test_wit_wisdom_and_friend_pal_aliases(self):
        self.assertIs(T.Stat.parse("Wisdom"), T.Stat.WIT)
        self.assertIs(T.SupportType.parse("Pal"), T.SupportType.FRIEND)

    def test_catalog_aptitude_words_resolve(self):
        for value in set(C._DIST.values()):
            self.assertIsInstance(T.DistanceType.parse(value), T.DistanceType, value)
        for value in set(C._TRACK.values()):
            self.assertIsInstance(T.Surface.parse(value), T.Surface, value)
        for value in set(C._STYLE.values()):
            self.assertIsInstance(T.RunningStyle.parse(value), T.RunningStyle, value)


class SkillTaxonomyTests(unittest.TestCase):
    def test_scope_words_match_the_skill_catalog(self):
        self.assertEqual(set(T.SKILL_SCOPE_WORDS), set(K._SCOPE_WORDS.values()))
        self.assertIs(T.scope_member("front"), T.RunningStyle.FRONT)
        self.assertIs(T.scope_member("dirt"), T.Surface.DIRT)
        self.assertIs(T.scope_member("Long"), T.DistanceType.LONG)
        for style in T.RunningStyle:
            self.assertIs(T.scope_member(style.scope_word), style.condition_group)
        with self.assertRaises(ValueError):
            T.scope_member("nowhere")

    def test_tier_strings_match_the_skill_catalog(self):
        self.assertEqual({"normal", "rare", "unique"}, {T.SkillTier.NORMAL.value, T.SkillTier.RARE.value, T.SkillTier.UNIQUE.value})
        cat = K.default_catalog()
        for s in cat.skills:
            self.assertIsInstance(T.SkillTier.parse(s.tier), T.SkillTier, s.name)

    def test_every_game8_label_in_skill_md_is_classified(self):
        cat = K.default_catalog()
        if not len(cat):
            self.skipTest("skill.md not found")
        for kind in {s.kind for s in cat.skills}:
            tier, effect = T.classify_game8_kind(kind)
            self.assertTrue(tier or effect, kind)

    def test_game8_labels(self):
        self.assertEqual(T.classify_game8_kind("Speed - Other"), (None, T.SkillEffect.POSITIONING))
        self.assertEqual(T.classify_game8_kind("green skill"), (None, T.SkillEffect.PASSIVE))
        self.assertEqual(T.classify_game8_kind("Negative"), (T.SkillTier.NEGATIVE, None))
        self.assertEqual(T.classify_game8_kind("Unique Skill"), (T.SkillTier.UNIQUE, None))
        with self.assertRaises(ValueError):
            T.classify_game8_kind("Mystery")

    def test_effect_types(self):
        self.assertEqual(T.classify_effect_types([27, 31, 9]),
                         {T.SkillEffect.VELOCITY, T.SkillEffect.ACCELERATION, T.SkillEffect.RECOVERY})
        self.assertEqual(T.classify_effect_types([1, 2, 3, 4, 5]), {T.SkillEffect.PASSIVE})
        self.assertEqual(T.unmapped_effect_types([27, 99, 100]), {99, 100})
        self.assertEqual(set(T.UPSTREAM_EFFECT_CATEGORY), set(S.SKILL_EFFECT_STAT) | {9, 21, 22, 27, 31})

    def test_classify_skill(self):
        entry = {"rarity": 2, "alternatives": [{"effects": [{"type": 27, "modifier": 0.25}, {"type": 9, "modifier": 0.03}]}],
                 "partial": True}
        c = T.classify_skill("200352", entry)
        self.assertIs(c.tier, T.SkillTier.RARE)
        self.assertEqual(c.effects, {T.SkillEffect.VELOCITY, T.SkillEffect.RECOVERY})
        self.assertTrue(c.partial)
        self.assertEqual(T.classify_skill("200001", {"rarity": 1, "alternatives": []}).tier, T.SkillTier.NORMAL)
        self.assertIs(T.classify_skill("900123", {"rarity": 1}).tier, T.SkillTier.INHERITED_UNIQUE)
        self.assertIsNone(T.classify_skill("100123", {"rarity": 4}).tier, "rarity 3+ is not mapped from data")
        self.assertIs(T.classify_skill("100123", {"rarity": 4}, "Unique Skill").tier, T.SkillTier.UNIQUE)
        merged = T.classify_skill("210001", {"rarity": 1, "alternatives": [{"effects": [{"type": 31}]}]}, "Speed - Other")
        self.assertEqual(merged.effects, {T.SkillEffect.POSITIONING, T.SkillEffect.ACCELERATION})
        self.assertEqual(T.classify_skill("1", {"alternatives": [{"effects": [{"type": 77}]}]}).unmapped_types, {77})
        self.assertEqual(T.classify_skill("1").effects, frozenset())

    def test_level_marks_agree_with_the_skill_catalog(self):
        for name, level in [("Corner Recovery ○", 1), ("Corner Recovery ◯", 1), ("Long Corners ◎", 2), ("Plain", 0)]:
            base, lvl = K.split_mark(name)
            self.assertEqual(lvl, level)
            glyph = name[len(base):].strip()
            self.assertEqual(int(T.LevelMark.from_glyph(glyph)), level, name)
        self.assertIs(T.LevelMark.from_glyph("×"), T.LevelMark.NEGATIVE)
        with self.assertRaises(ValueError):
            T.LevelMark.from_glyph("?")

    def test_skill_key_still_separates_levels(self):
        # The taxonomy does not change how names are matched; both resolvers keep the mark in the key.
        self.assertNotEqual(S.skill_key("X ◎"), S.skill_key("X ○"))
        self.assertNotEqual(K.skill_key("X ◎"), K.skill_key("X ○"))


class RaceBasicsTests(unittest.TestCase):
    def test_distance_bands(self):
        for meters, expect in [(1200, "SPRINT"), (1400, "SPRINT"), (1600, "MILE"), (1800, "MILE"),
                               (2000, "MEDIUM"), (2400, "MEDIUM"), (2500, "LONG"), (3600, "LONG")]:
            self.assertEqual(T.DistanceType.from_meters(meters).name, expect, meters)

    def test_running_style_extras(self):
        self.assertIs(T.RunningStyle.RUNAWAY.condition_group, T.RunningStyle.FRONT)
        self.assertEqual(T.RunningStyle.END.label, "End Closer")
        self.assertEqual(T.Mood.GREAT.motivation, 5)

    def test_stat_ids(self):
        self.assertIs(T.Stat.from_upstream_id(5), T.Stat.WIT)
        for bad in (0, 6):
            with self.assertRaises(ValueError):
                T.Stat.from_upstream_id(bad)


class DefinitionTests(unittest.TestCase):
    def test_entity_homes_cover_every_kind_and_point_at_real_paths(self):
        self.assertEqual(set(T.ENTITY_HOMES), set(T.EntityKind))
        for kind, paths in T.ENTITY_HOMES.items():
            for p in paths or ():
                self.assertTrue((ROOT / p).exists(), f"{kind.name}: {p} is missing")

    def test_mechanics_cover_every_domain(self):
        self.assertEqual(set(T.MECHANICS), set(T.MechanicDomain))
        for domain, topics in T.MECHANICS.items():
            self.assertTrue(topics)
            self.assertEqual(len(topics), len(set(topics)), domain)

    def test_module_uses_only_the_standard_library(self):
        tree = ast.parse(TAXONOMY_PY.read_text(encoding="utf-8"))
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names |= {a.name.split(".")[0] for a in node.names}
            elif isinstance(node, ast.ImportFrom) and node.module:
                names.add(node.module.split(".")[0])
        self.assertLessEqual(names, set(sys.stdlib_module_names) | {"__future__"}, names)

    def test_no_enum_has_duplicate_aliases_pointing_at_two_members(self):
        for enum in PUBLIC_ENUMS:
            keys = {}
            for m in enum:
                keys.setdefault(T._key(m.name), m)
            for alias, name in T._ALIASES.get(enum, {}).items():
                self.assertIn(name, enum.__members__, f"{enum.__name__}: alias {alias!r} -> {name}")


class DocTests(unittest.TestCase):
    def test_doc_exists_and_names_every_enum_and_its_members_by_class(self):
        text = TAXONOMY_MD.read_text(encoding="utf-8")
        for enum in PUBLIC_ENUMS:
            self.assertIn(f"`{enum.__name__}`", text, f"{enum.__name__} is not described in Taxonomy.md")

    def test_doc_is_found_by_the_docs_engine(self):
        try:
            from LilyAiGameSpace.Umamusume.UmamusumeGameSpaceEngine import UmamusumeGameSpaceEngine
        except ImportError:
            self.skipTest("docs engine not importable here")
        engine = UmamusumeGameSpaceEngine(refresh_interval=0)
        doc = engine.resolve("Umamusume Taxonomy")
        self.assertIsNotNone(doc)
        self.assertEqual(doc.id, "Taxonomy/Taxonomy")
        self.assertEqual(doc.category, "Taxonomy")
        hits = engine.search("skill tier inherited unique", category="Taxonomy")
        self.assertTrue(hits)


if __name__ == "__main__":
    unittest.main()
