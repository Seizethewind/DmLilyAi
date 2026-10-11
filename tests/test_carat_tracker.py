import unittest

from LilyAiCore.ExternalServices.Database.sqlite import Database
from LilyAiMemory.Carat.carat_store import CaratError, CaratStore, classify
from LilyAiMemory.Storage.store import MemoryStore
from LilyAiTool.CaratTools import carat_tools
from LilyAiTool.Models.tool_models import ToolContextData


class ClassifyTests(unittest.TestCase):
    def test_first_entry_is_baseline(self):
        self.assertEqual(classify(None, 20000)["kind"], "baseline")

    def test_gain_is_difference(self):
        self.assertEqual(classify(20000, 20600)["income"], 600)

    def test_drop_must_be_explained(self):
        with self.assertRaises(CaratError) as cm:
            classify(20000, 18500)
        self.assertIn("10 pulls", str(cm.exception))

    def test_pulls_add_back_income(self):
        e = classify(20000, 18900, spent=1500)   # 10 pulls and earned 400
        self.assertEqual((e["income"], e["spent"]), (400, 1500))

    def test_spent_too_small(self):
        with self.assertRaises(CaratError):
            classify(20000, 18000, spent=1500)

    def test_correction(self):
        e = classify(20000, 2000, correction=True)
        self.assertEqual((e["kind"], e["income"], e["spent"]), ("baseline", 0, 0))


class ToolTests(unittest.TestCase):
    def setUp(self):
        self.store = CaratStore(MemoryStore(Database()))
        self.t = {s.name: s.handler for s in carat_tools(self.store)}
        self.ctx = ToolContextData(user_id="u1")

    def test_flow(self):
        self.assertIn("starting balance", self.t["carat_update"](self.ctx, {"balance": "20k"}))
        out = self.t["carat_update"](self.ctx, {"balance": 18500})
        self.assertTrue(out.startswith("NOT RECORDED"))
        self.assertEqual(self.store.last("u1")["balance"], 20000)
        out = self.t["carat_update"](self.ctx, {"balance": 18500, "pulls": 10, "reason": "banner pulls"})
        self.assertIn("Spent 1,500", out)
        self.assertEqual(self.store.last("u1")["balance"], 18500)
        self.assertIn("+600", self.t["carat_update"](self.ctx, {"balance": 19100}))
        self.assertIn("19,100", self.t["carat_status"](self.ctx, {}))
        self.assertIn("now 18,500", self.t["carat_undo"](self.ctx, {}))

    def test_users_are_separate(self):
        self.t["carat_update"](self.ctx, {"balance": 100})
        self.assertIn("No carat", self.t["carat_status"](ToolContextData(user_id="u2"), {}))


if __name__ == "__main__":
    unittest.main()
