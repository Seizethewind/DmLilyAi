"""Tests for Gain.py using tiny synthetic data written to a temp folder."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "LilyAiGameSpace" / "Umamusume" / "Simulation"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import Gain as G  # noqa: E402
import test_simulator as T  # noqa: E402  (reuses its synthetic course and skills)


class GainMode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        d = Path(cls.tmp.name)
        (d / "skills.json").write_text(json.dumps(T.DATA.skills))
        (d / "courses.json").write_text(json.dumps(T.DATA.courses))
        cls.dir = str(d)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def run_gain(self, skills, runs=40):
        cfg = {"course": "1", "runs": runs, "seed": 3, "wisdom_checks": False,
               "builds": {"A": dict(T.SPEC, skills=skills)}}
        return G.analyse(cfg, data_dir=self.dir)["A"]

    def test_useful_skill_has_positive_gain(self):
        out = self.run_gain(["1"])
        row = out["skills"][0]
        self.assertGreater(row["solo_gain_m"], 0)
        self.assertEqual(row["solo_gain_m"], row["marginal_gain_m"])   # only skill in the build

    def test_useless_skill_gains_exactly_zero(self):
        # a heal with HP already full changes nothing: paired randomness => exactly 0, not noise
        out = self.run_gain(["2"])
        self.assertEqual(out["skills"][0]["solo_gain_m"], 0.0)

    def test_unsupported_and_inactive_are_listed_without_gain(self):
        out = self.run_gain(["1", "3", "4"])
        by_id = {r["id"]: r for r in out["skills"]}
        self.assertNotIn("solo_gain_m", by_id["3"])
        self.assertNotIn("solo_gain_m", by_id["4"])
        self.assertEqual(out["skills"][0]["id"], "1")     # sorted best first

    def test_deterministic(self):
        self.assertEqual(self.run_gain(["1"]), self.run_gain(["1"]))


if __name__ == "__main__":
    unittest.main()
