"""Career evaluator: skill catalog, screenshot validation and the guide-based checks.

Uses a small inline skill table (rows copied from Skill/skill.md) so it does not depend on the docs folder."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from LilyAiGameSpace.CareerEvaluator import (
    Goal, base_stat, evaluate, guts_adjustment, parse_goal, render_report, required_stamina, rushed_pct,
    skill_activation_pct, COURSES,
)
from LilyAiGameSpace.TraineeSheet import (
    Sheet, extract_json, merge_sheets, sheet_from_extraction,
)
from LilyAiGameSpace.UmamusumeSkills import SkillCatalog, skill_key, split_mark

MINI_SKILLS = """
## Unique Skills

| Skill Name | Skill Type | Skill Activation Requirements | Acquisitions |
| --- | --- | --- | --- |
| Angling and Scheming | Unique Skill | Increase acceleration at an opportune moment when in the lead on a corner late-race. | Innate: Seiun Sky (Reeling in the Big One) |
| Victoria por Plancha ☆ | Unique Skill | Hang on to the advantage when positioned toward the front with energy to spare on the final straight. | Innate: El Condor Pasa (El Numero 1) |
| SPARKLY☆STARDOM | Unique Skill | Become empowered to keep the spotlight when positioned toward the front and close to the runner behind on a straight mid-race. | Innate: Smart Falcon (LOVE☆4EVER) |
| Pure Heart | Unique Skill | Greatly recover endurance when well-positioned mid-race. | Innate: Super Creek (Murmuring Stream) |

## Rare Skills

| Skill Name | Skill Type | Skill Activation Requirements | Acquisitions |
| --- | --- | --- | --- |
| Center Stage | Speed - Other | Greatly increase navigation early-race. | Skill Points |
| Cooldown | Recovery | Decrease fatigue by taking a breather upon entering a straight. (Long) | Skill Points |

## Normal Skills

| Skill Name | Skill Type | Skill Activation Requirements | Acquisitions |
| --- | --- | --- | --- |
| Long Corners ◯ | Velocity | Slightly increase velocity on a corner. (Long) | Skill Points |
| Long Corners ◎ | Velocity | Moderately increase velocity on a corner. (Long) | Skill Points |
| Straightaway Adept | Velocity | Slightly increase velocity on a straight. | Skill Points |
| Front Runner Straightaways ◎ | Velocity | Moderately increase velocity on a straight. (Front Runner) | Skill Points |
| Groundwork | Acceleration | Slightly increase acceleration after activating many skills early-race. | Skill Points |
| Fast-Paced | Speed - Other | Slightly increase ability to go to the front mid-race. (Front Runner) | Skill Points |
| Deep Breaths | Recovery | Slightly decrease fatigue by taking a breather upon entering a straight. (Long) | Skill Points |
| Corner Recovery ◯ | Recovery | Slightly recover endurance on a corner with efficient turning. | Skill Points |
| Extra Tank | Recovery | Slightly regain the energy to run when close to exhausting strength. (Long) | Skill Points |
| Right-Handed ◯ | Green Skill | Moderately increase performance on right-handed tracks. | Skill Points |
| Wet Conditions ◯ | Green Skill | Moderately increase performance on good, soft, and heavy ground. | Skill Points |
| Front Runner Savvy ◯ | Green Skill | Moderately increase ability to get into a good position. (Front Runner) | Skill Points |
| Mile Straightaway ◎ | Velocity | Moderately increase velocity on a straight. (Mile) | Skill Points |
"""
CATALOG = SkillCatalog.from_markdown(MINI_SKILLS)

# Smart Falcon [LOVE☆4EVER], the post-career screenshots (Skills tab, scrolled to the end).
SKILL_ROWS = [
    ("SPARKLY☆STARDOM Lvl 5", "unique", "speed"), ("Victoria por plancha ☆", "unique", "speed"),
    ("Angling and Scheming", "unique", "acceleration"), ("Victory Cheer!", "unique", "speed"),
    ("Right-Handed O", "white", "green"), ("Nakayama Racecourse O", "white", "green"),
    ("Wet Conditions O", "white", "green"), ("Corner Recovery O", "white", "recovery"),
    ("Straightaway Adept", "white", "speed"), ("Center Stage", "gold", "other"), ("Fast-Paced", "white", "other"),
    ("Deep Breaths", "white", "recovery"), ("Extra Tank", "white", "recovery"), ("Long Corners ◎", "white", "speed"),
    ("Front Runner Straightaways ◎", "white", "speed"), ("Top Runner", "gold", "speed"),
    ("Front Runner Savvy O", "white", "green"), ("Groundwork", "white", "acceleration"),
    ("See Ya Later!", "gold", "speed"), ("On the Way to Our Dream", "white", "speed"),
]


def falcon_extraction(tab="skills"):
    return {
        "is_trainee_details_screen": True,
        "active_tab": tab,
        "trainee": {"name": "Smart Falcon", "outfit": "LOVE☆4EVER", "rating": "20,704"},
        "stats": {"speed": 1538, "stamina": "739", "power": 1127, "guts": 619, "wit": 784},
        "aptitudes": {"turf": "S", "dirt": "A", "sprint": "B", "mile": "A", "medium": "A", "long": "A",
                      "front": "A", "pace": "D", "late": "G", "end": "G"},
        "skills": [{"name": n, "rarity": r, "icon": i} for n, r, i in SKILL_ROWS],
        "uncertain": [],
    }


def falcon_sheet():
    return sheet_from_extraction(falcon_extraction())


class CareerEvaluatorTests(unittest.TestCase):
    # --------------------------------------------------------------------------- skill names

    def test_level_marks_are_found_even_when_read_as_a_letter(self):
        assert split_mark("Corner Recovery O") == ("Corner Recovery", 1)
        assert split_mark("Long Corners ◎") == ("Long Corners", 2)
        assert split_mark("Wet Conditions") == ("Wet Conditions", 0)
        assert skill_key("Corner Recovery O") == skill_key("Corner Recovery ◯")
        assert CATALOG.find("Corner Recovery O").name == "Corner Recovery ◯"
        assert CATALOG.find("Long Corners ◎").level == 2
        assert CATALOG.find("victoria por plancha").tier == "unique"
        assert CATALOG.find("Top Runner") is None

    # --------------------------------------------------------------------------- formulas

    def test_formulas_match_the_guide(self):
        assert base_stat(1600) == 1400 and base_stat(1538) == 1369 and base_stat(1127) == 1127
        assert round(skill_activation_pct(300), 1) == 70.0 and round(skill_activation_pct(900), 1) == 90.0
        assert rushed_pct(300) == 19 and rushed_pct(600) == 14 and rushed_pct(900) == 12 and rushed_pct(1200) == 10
        assert rushed_pct(784) == 12 and round(skill_activation_pct(784), 1) == 88.5

    def test_guts_conversion_uses_the_guide_tiers(self):
        # exactly at the baseline: no adjustment
        assert guts_adjustment(400, 400, 380) == (0.0, 0.0)
        lo, hi = guts_adjustment(619, 400, 380)  # Long
        assert 88 < lo < 90 and 150 < hi < 152
        lo, hi = guts_adjustment(200, 300, 260)  # below target Guts costs Stamina
        assert hi < 0

    def test_required_stamina_interpolates_and_flags_extrapolation(self):
        long3200 = next(c for c in COURSES if c.key == "long3200")
        assert required_stamina(long3200, "front", 2) == (1080.0, False)
        assert required_stamina(long3200, "front", 3) == (830.0, False)
        need, extrap = required_stamina(long3200, "front", 0.82)
        assert extrap and 1370 < need < 1380
        mile = next(c for c in COURSES if c.key == "mile")
        assert required_stamina(mile, "front", 0) == (800.0, False)
        assert round(required_stamina(mile, "front", 0.5)[0]) == 720

    # --------------------------------------------------------------------------- screenshot validation

    def test_extraction_is_validated_not_trusted(self):
        sheet = falcon_sheet()
        assert sheet.trainee == "Smart Falcon" and sheet.outfit == "LOVE☆4EVER" and sheet.rating == 20704
        assert sheet.stats == {"speed": 1538, "stamina": 739, "power": 1127, "guts": 619, "wit": 784}
        assert len(sheet.skills) == 20 and sheet.unique_level == 5 and sheet.skills_seen
        bad = falcon_extraction()
        bad["stats"]["speed"] = 31538  # a misread, out of range
        bad["stats"]["guts"] = None
        bad["aptitudes"]["turf"] = "Z"
        s = sheet_from_extraction(bad)
        assert "speed" not in s.stats and "guts" not in s.stats and "turf" not in s.aptitudes
        assert any("Speed" in n for n in s.notes)

    def test_skills_from_other_tabs_are_ignored(self):
        # the Inspiration tab lists sparks that look like skill names; they must never be read as skills
        s = sheet_from_extraction(falcon_extraction(tab="inspiration"))
        assert s.skills == [] and not s.skills_seen
        assert sheet_from_extraction({"is_trainee_details_screen": False}) is None

    def test_json_is_found_inside_reasoning_text_and_fences(self):
        reply = '<think>let me look</think>```json\n{"is_trainee_details_screen": true, "stats": {"speed": 900}}\n```'
        assert extract_json(reply)["stats"]["speed"] == 900
        assert extract_json("no json here") is None

    def test_merge_keeps_first_reading_and_notes_disagreements(self):
        a = sheet_from_extraction(falcon_extraction())
        other = falcon_extraction(tab="career_info")
        other["stats"]["speed"] = 1583
        b = sheet_from_extraction(other)
        merged = merge_sheets([a, b])
        assert merged.stats["speed"] == 1538
        assert any("1538" in n and "1583" in n for n in merged.notes)
        assert len(merged.skills) == 20

    # --------------------------------------------------------------------------- the evaluation

    def test_goal_parsing(self):
        goal, cap = parse_goal("is she good for long front runner on turf? cap 1200")
        assert goal == Goal(("long",), ("front",), "turf") and cap == 1200
        goal, cap = parse_goal("what do you think")
        assert goal == Goal() and cap is None
        assert parse_goal("1600 cap mile or medium")[0].distances == ("mile", "medium")

    def test_smart_falcon_is_a_mile_runner_not_a_long_runner(self):
        report = evaluate(falcon_sheet(), cap=1600, catalog=CATALOG)
        labels = {t.target.label: t for t in report.targets}
        assert set(labels) == {"Mile Front Runner on Turf", "Medium Front Runner on Turf", "Long Front Runner on Turf"}
        assert labels["Mile Front Runner on Turf"].verdict == "Good"
        assert labels["Medium Front Runner on Turf"].verdict == "Not good"
        assert labels["Long Front Runner on Turf"].verdict == "Not good"
        assert report.targets[0].target.distance == "mile"
        assert report.headline.startswith("Best fit: Mile Front Runner on Turf")
        assert "Not good for" in report.headline

    def test_recoveries_only_count_where_they_work(self):
        report = evaluate(falcon_sheet(), cap=1600, catalog=CATALOG, goal=Goal(("long", "mile"), ("front",), "turf"))
        by = {t.target.distance: t for t in report.targets}
        long_rec = next(f for f in by["long"].findings if f.area == "Recoveries")
        mile_rec = next(f for f in by["mile"].findings if f.area == "Recoveries")
        assert "Deep Breaths" in long_rec.text and "Extra Tank" in long_rec.text and "0.82" in long_rec.text
        assert "Deep Breaths" not in mile_rec.text and "0.27" in mile_rec.text  # Long-only skills do nothing in a Mile
        off = next(f for f in by["mile"].findings if f.area == "Off-target skills")
        assert "Deep Breaths" in off.text and "Long Corners ◎" in off.text

    def test_unknown_skills_are_reported_not_judged(self):
        report = evaluate(falcon_sheet(), cap=1600, catalog=CATALOG)
        unknown = next(f for f in report.general if "not in my skill docs" in f.text)
        for name in ("Top Runner", "See Ya Later!", "On the Way to Our Dream", "Victory Cheer!", "Nakayama Racecourse O"):
            assert name in unknown.text
        # her own unique is recognised but not scored; an inherited unique is treated as a normal skill
        assert any(f.area == "Unique" for f in report.general)
        inherited = next(r for r in report.skills if r.name.startswith("Victoria"))
        assert inherited.inherited_unique and not inherited.own_unique

    def test_a_gold_recovery_changes_the_answer(self):
        base = falcon_extraction()
        base["skills"].append({"name": "Cooldown", "rarity": "gold", "icon": "recovery"})
        with_gold = evaluate(sheet_from_extraction(base), cap=1600, catalog=CATALOG, goal=Goal(("long",), ("front",), "turf"))
        without = evaluate(falcon_sheet(), cap=1600, catalog=CATALOG, goal=Goal(("long",), ("front",), "turf"))
        assert with_gold.targets[0].shortfall < without.targets[0].shortfall - 100

    def test_unknown_recovery_icon_is_counted_only_as_white_unless_gold(self):
        ex = falcon_extraction()
        ex["skills"].append({"name": "Mystery Heal", "rarity": "gold", "icon": "recovery"})
        ex["skills"].append({"name": "Other Heal", "rarity": "white", "icon": "recovery"})
        report = evaluate(sheet_from_extraction(ex), cap=1600, catalog=CATALOG, goal=Goal(("medium",), ("front",), "turf"))
        rec = next(f for f in report.targets[0].findings if f.area == "Recoveries")
        assert "Mystery Heal 5.5%" in rec.text and "Other Heal 1.5%" in rec.text

    def test_missing_skills_tab_is_said_plainly(self):
        ex = falcon_extraction(tab="inspiration")
        report = evaluate(sheet_from_extraction(ex), cap=1600, catalog=CATALOG)
        assert any("No Skills tab" in f.text for f in report.general)
        assert not any(f.area == "Recoveries" for t in report.targets for f in t.findings)

    def test_render_is_readable_and_honest(self):
        text = render_report(evaluate(falcon_sheet(), cap=1600, catalog=CATALOG))
        assert "Smart Falcon [LOVE☆4EVER]" in text and "rating 20,704" in text
        assert "Speed 1538" in text and "Nothing from this screenshot is saved" in text
        assert "Verdict: Best fit: Mile Front Runner on Turf" in text
        assert "estimate" in text
        assert len(text) < 6000

    def test_empty_catalog_still_works(self):
        report = evaluate(falcon_sheet(), cap=1600, catalog=SkillCatalog([]))
        assert report.targets and any("not in my skill docs" in f.text for f in report.general)


if __name__ == "__main__":
    unittest.main()
