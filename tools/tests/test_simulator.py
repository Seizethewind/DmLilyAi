"""Tests for Simulator.py using tiny synthetic data (no data files needed)."""
import random
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "LilyAiGameSpace" / "Umamusume" / "Simulation"))
import Simulator as S  # noqa: E402

COURSE = {"track_id": 10001, "track": "Test", "distance": 2000, "distance_type": 3, "surface": 1, "turn": 1,
          "course_set_status": [],
          "corners": [{"start": 400, "length": 200}, {"start": 800, "length": 200},
                      {"start": 1200, "length": 200}, {"start": 1600, "length": 200}],
          "straights": [{"start": 0, "end": 400}, {"start": 600, "end": 800}, {"start": 1000, "end": 1200},
                        {"start": 1400, "end": 1600}, {"start": 1800, "end": 2000}],
          "slopes": []}


def skill(cond, effects, duration=3.0, name="T", pre=""):
    return {"name": name, "rarity": 1, "wisdom_check": False,
            "alternatives": [{"duration": duration, "condition": cond, "precondition": pre,
                              "effects": [{"type": t, "modifier": m} for t, m in effects]}]}


DATA = S.Data(
    {"1": skill("phase>=2&is_lastspurt==1", [(31, 0.4), (27, 0.5)], name="Burst"),
     "2": skill("phase==1&order_rate<=50", [(9, 0.05)], name="Heal"),
     "3": skill("some_future_condition==1", [(27, 0.5)], name="Mystery"),
     "4": skill("phase==3&distance_type==1", [(27, 0.5)], name="WrongDistance")},
    {"1": COURSE})
SPEC = {"stats": {"speed": 900, "stamina": 1300, "power": 800, "guts": 400, "wisdom": 500}, "style": "pace"}


def cfg(skills=(), **kw):
    return dict({"course": "1", "runs": 30, "seed": 5, "builds": {"A": dict(SPEC, skills=list(skills))}}, **kw)


class Intervals(unittest.TestCase):
    def test_ops(self):
        self.assertEqual(S.norm_iv([(5, 10), (0, 6), (20, 20)]), [(0, 10)])
        self.assertEqual(S.inter_iv([(0, 10), (20, 30)], [(5, 25)]), [(5, 10), (20, 25)])
        self.assertEqual(S.comp_iv([(10, 20)], 30), [(0, 10), (20, 30)])


class Conditions(unittest.TestCase):
    def setUp(self):
        base = S.base_horse(SPEC, 2)
        self.env = S.Env(COURSE, base, S.adjusted_horse(base, COURSE, 1), 1, 2, dict(S.DEFAULT_PARAMS))

    def test_phase_and_static(self):
        terms, approx, bad = S.compile_expr("phase==2&distance_type==3", self.env)
        self.assertIsNone(bad)
        self.assertEqual(terms[0].intervals, [(2000 * 2 / 3, 2000 * 5 / 6)])
        terms, _, _ = S.compile_expr("distance_type==1", self.env)
        self.assertEqual(terms, [])          # static false -> can't fire

    def test_or_terms_and_opponent(self):
        terms, approx, bad = S.compile_expr("phase==0@phase==3&order<=3", self.env)
        self.assertEqual(len(terms), 2)
        self.assertTrue(approx)

    def test_corner_numbering(self):
        # 4 corners: corner==4 is the last one, corner==1 the first
        self.assertEqual(self.env.corner_cats()[4], [(1600, 1800)])
        self.assertEqual(self.env.corner_cats()[1], [(400, 600)])

    def test_unsupported_key(self):
        _, _, bad = S.compile_expr("some_future_condition==1", self.env)
        self.assertEqual(bad, "some_future_condition")


class Races(unittest.TestCase):
    def _run(self, c):
        env, comp = S.make_env_and_skills(DATA, c, c["builds"]["A"])
        times = [S.Race(env, comp, random.Random(i)).run().finish_time for i in range(c["runs"])]
        return sum(times) / len(times), comp

    def test_deterministic(self):
        self.assertEqual(self._run(cfg())[0], self._run(cfg())[0])

    def test_plausible_time(self):
        mean, _ = self._run(cfg())
        self.assertTrue(85 < mean < 115, mean)

    def test_speed_skill_helps(self):
        base, _ = self._run(cfg())
        fast, comp = self._run(cfg(["1"]))
        self.assertEqual(comp[0].status, "ok")
        self.assertLess(fast, base)

    def test_statuses(self):
        _, comp = self._run(cfg(["2", "3", "4"]))
        self.assertEqual([c.status for c in comp], ["approx", "unsupported", "inactive"])

    def test_exhausted_runner_ignores_target_speed_skill(self):
        weak = dict(SPEC, stats=dict(SPEC["stats"], stamina=300))
        env, comp = S.make_env_and_skills(DATA, cfg(["1"]), dict(weak, skills=["1"]))
        res = S.Race(env, comp, random.Random(1)).run()
        self.assertTrue(res.ran_out_of_hp)

    def test_more_speed_is_faster(self):
        slow = dict(SPEC, stats=dict(SPEC["stats"], speed=500))
        env1, c1 = S.make_env_and_skills(DATA, cfg(), slow)
        env2, c2 = S.make_env_and_skills(DATA, cfg(), SPEC)
        t1 = S.Race(env1, c1, random.Random(1)).run().finish_time
        t2 = S.Race(env2, c2, random.Random(1)).run().finish_time
        self.assertGreater(t1, t2)


if __name__ == "__main__":
    unittest.main()
