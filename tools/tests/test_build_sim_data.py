import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_sim_data as b  # noqa: E402


class SlimSkills(unittest.TestCase):
    def test_units_and_filtering(self):
        raw = {"1": {"rarity": 2, "wisdomCheck": 1, "alternatives": [{
            "baseDuration": 50000, "condition": "phase>=2", "precondition": "",
            "effects": [{"type": 27, "modifier": 3500, "target": 1},
                        {"type": 27, "modifier": 1000, "target": 2}]}]}}
        out = b.slim_skills(raw, {"1": ["jp", "en"]})
        alt = out["1"]["alternatives"][0]
        self.assertEqual(alt["duration"], 5.0)
        self.assertEqual(alt["effects"], [{"type": 27, "modifier": 0.35}])
        self.assertTrue(out["1"]["partial"])
        self.assertEqual(out["1"]["name"], "en")
        self.assertTrue(out["1"]["wisdom_check"])

    def test_skill_with_no_supported_effect_is_dropped(self):
        raw = {"1": {"rarity": 1, "alternatives": [{"baseDuration": 1, "condition": "", "precondition": "",
                                                    "effects": [{"type": 99, "modifier": 1, "target": 1}]}]}}
        self.assertEqual(b.slim_skills(raw, {}), {})

    def test_course_slopes_sorted(self):
        raw = {"1": {"raceTrackId": 10001, "distance": 1200, "distanceType": 1, "surface": 1, "turn": 1,
                     "corners": [], "straights": [],
                     "slopes": [{"start": 900, "length": 10, "slope": -5000}, {"start": 100, "length": 10, "slope": 5000}]}}
        out = b.slim_courses(raw, {"10001": ["jp", "Sapporo"]})
        self.assertEqual([s["start"] for s in out["1"]["slopes"]], [100, 900])
        self.assertEqual(out["1"]["track"], "Sapporo")


if __name__ == "__main__":
    unittest.main()
