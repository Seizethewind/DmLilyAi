"""Global (in-game) skill names -> simulator ids: the key normaliser, the resolver, the builder and the shipped data."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "LilyAiGameSpace" / "Umamusume" / "Simulation"))
sys.path.insert(0, str(ROOT / "tools"))
import Simulator as S  # noqa: E402
import VeteranReader as R  # noqa: E402
import build_skill_aliases as B  # noqa: E402

DATA_DIR = ROOT / "tools" / "sim_data"


def sk(name, jp="", rarity=1):
    return {"name": name, "name_jp": jp, "rarity": rarity, "wisdom_check": False, "alternatives": []}


SKILLS = {"200382": sk("Straight Recovery", "直線回復"), "200351": sk("Corner Recovery ◎", "コーナー回復◎", 2),
          "200352": sk("Corner Recovery ○", "コーナー回復○"), "110061": sk("Christmas Eve Miracle Run!", "聖夜のミラクルラン！", 5),
          "910061": sk("聖夜のミラクルラン！", "聖夜のミラクルラン！"), "202462": sk("Steadfast", "別の技")}
ALIASES = {"names": {"Straightaway Recovery": ["200382"], "Festive Miracle": ["910061", "110061"],
                     "Steadfast": ["200732"], "Hawkeye": ["201122"]},
           "unmodelled": {"Hawkeye": "201122"}, "unique_owner": {"110061": "Oguri Cap"}}
D = S.Data(SKILLS, {}, ALIASES)


class Keys(unittest.TestCase):
    def test_circle_spellings_and_punctuation(self):
        k = S.skill_key("Corner Recovery ○")
        for t in ("Corner Recovery O", "corner recovery ◯", "Corner  Recovery 〇", "CORNER RECOVERY ○"):
            self.assertEqual(S.skill_key(t), k, t)
        self.assertNotEqual(S.skill_key("Corner Recovery ◎"), k)
        self.assertEqual(S.skill_key("Victory Cheer!"), S.skill_key("victory cheer"))


class Resolve(unittest.TestCase):
    def test_global_name_and_id_and_upstream_name(self):
        self.assertEqual(D.resolve_skill("Straightaway Recovery"), "200382")
        self.assertEqual(D.resolve_skill("straightaway  recovery!"), "200382")
        self.assertEqual(D.resolve_skill("200382"), "200382")
        self.assertEqual(D.resolve_skill("Straight Recovery"), "200382")
        self.assertEqual(D.resolve_skill("Corner Recovery O"), "200352")

    def test_owner_gets_unique_others_get_inherited(self):
        self.assertEqual(D.resolve_skill("Festive Miracle", owner="Oguri Cap"), "110061")
        self.assertEqual(D.resolve_skill("Festive Miracle", owner="Oguri Cap [Ashen Miracle]"), "110061")
        self.assertEqual(D.resolve_skill("Festive Miracle", owner="Special Week"), "910061")
        self.assertEqual(D.resolve_skill("Festive Miracle"), "910061")

    def test_in_game_name_wins_over_a_clashing_upstream_name_only_when_simulatable(self):
        # alias points at an id that is not in skills.json, so the upstream 'Steadfast' is still found
        self.assertEqual(D.resolve_skill("Steadfast"), "202462")

    def test_unmodelled_and_unknown_are_told_apart(self):
        with self.assertRaises(S.UnmodelledSkill):
            D.resolve_skill("Hawkeye")
        with self.assertRaises(ValueError) as cm:
            D.resolve_skill("Totally Made Up")
        self.assertNotIsInstance(cm.exception, S.UnmodelledSkill)

    def test_find_and_suggest(self):
        hit = D.find_skills("straightaway")
        self.assertEqual([h["id"] for h in hit], ["200382"])
        self.assertEqual(hit[0]["global"], "Straightaway Recovery")
        self.assertTrue(D.suggest_skills("Straightaway Recovry")[0].startswith("200382"))

    def test_reader_messages(self):
        ids, problems = R.resolve_skills(["Straightaway Recovery", "Hawkeye", "Nope Nope"], D, owner="X")
        self.assertEqual(ids, ["200382"])
        self.assertIn("not simulated", problems[0])
        self.assertIn("not recognised", problems[1])
        self.assertIn("sim_find_skill", problems[1])


class Builder(unittest.TestCase):
    HTML = ('<table><tr><td><a href="/File:Icon.png"><img></a></td>'
            '<td><b><a href="/Game:Skills/200382" title="Game:Skills/200382">Straightaway Recovery</a></b> <i>直線回復</i></td></tr>'
            '<tr><td><a href="/Game:Skills/110061" title="Game:Skills/110061">Festive Miracle</a></td></tr>'
            '<tr><td><a href="/Game:Skills/910061">Festive Miracle</a></td></tr>'
            '<tr><td><a href="/Game:Skills/201122">Hawkeye</a></td></tr></table>')

    def test_parse_links_ignores_icons_and_other_pages(self):
        self.assertEqual(B.parse_links(self.HTML), [("200382", "Straightaway Recovery"), ("110061", "Festive Miracle"),
                                                    ("910061", "Festive Miracle"), ("201122", "Hawkeye")])

    def test_build_orders_inherited_first_and_sets_owner(self):
        doc = B.build(B.parse_links(self.HTML), SKILLS, {"Festive Miracle": "Oguri Cap"})
        self.assertEqual(doc["names"]["Festive Miracle"], ["910061", "110061"])
        self.assertEqual(doc["unique_owner"], {"110061": "Oguri Cap"})
        self.assertEqual(doc["unmodelled"], {"Hawkeye": "201122"})

    def test_rebuild_keeps_hand_added_entries(self):
        prev = {"names": {"Hand Added": ["200352"]}, "unique_owner": {"110061": "Oguri Cap"}}
        doc = B.build(B.parse_links(self.HTML), SKILLS, {}, prev)
        self.assertEqual(doc["names"]["Hand Added"], ["200352"])
        self.assertEqual(doc["unique_owner"]["110061"], "Oguri Cap")

    def test_game8_owner_table(self):
        md = ("## Unique Skills\n\n| Skill Name | Skill Type | Skill Activation Requirements | Acquisitions |\n| --- | --- | --- | --- |\n"
              "| Festive Miracle | Unique Skill | text | Innate: Oguri Cap (Ashen Miracle) |\n## Rare Skills\n| X | Y | z | Innate: Nobody (N) |\n")
        self.assertEqual(B.game8_unique_owners(md), {"Festive Miracle": "Oguri Cap"})


@unittest.skipUnless((DATA_DIR / "skills.json").is_file(), "tools/sim_data not found")
class ShippedData(unittest.TestCase):
    def test_every_alias_id_exists_and_oguri_resolves(self):
        d = S.Data.load()
        doc = json.loads((DATA_DIR / "skill_aliases.json").read_text(encoding="utf-8"))
        for name, ids in doc["names"].items():
            for i in ids:
                self.assertIn(i, d.skills, f"{name} -> {i}")
        vet = json.loads((ROOT / "LilyAiGameSpace/Umamusume/Simulation/Veteran/veteran_oguri_cap.json").read_text(encoding="utf-8"))
        ids, problems = R.resolve_skills(vet["skills"], d, owner=vet["name"])
        self.assertEqual(problems, [])
        self.assertEqual(len(ids), len(vet["skills"]))


if __name__ == "__main__":
    unittest.main()
