#!/usr/bin/env python3
"""
Race templates for Simulator.py.

A template is a ready-made race setup: course id, season, ground, weather,
time of day and grade. It turns into a Simulator config, so you do not have to
look up course ids or remember the numeric codes for season / weather.

Two kinds of template
---------------------
1. Champions Meeting templates ("cm_*"), generated from the cmdefs/ folder of
   alpha123/uma-skill-tools (GPL-3.0; keep that attribution if you share this
   file). Course, season, ground and weather are real. They also carry the
   cmdef's base stats and the presupposed skills per running style, which
   become the default builds.
2. Race presets (e.g. "arima_kinen"). The upstream data has no race names, so
   these are only a course id (checked against upstream course_data.json) plus
   the season the race is normally run in. Season, and the good / sunny /
   midday defaults, are ASSUMPTIONS: override them if you want something else.
   Their default build is a generic one, so pass your own builds.

Simulator limits still apply: it runs ONE horse, so the field data in the CM
templates (number of runners, strategy positions) is kept for reference only
and does not change the result.

Usage
-----
    python race_template.py --list
    python race_template.py arima_kinen --show
    python race_template.py arima_kinen --ground yielding | python Simulator.py --config -
    python race_template.py cm_2024_12_nakayama2500 --run --runs 1000 --seed 7
    python race_template.py nakayama2500 --list        # name search (substring)

From Python:
    from race_template import make_config, run
    cfg = make_config("arima_kinen", builds={"A": {...}, "B": {...}}, ground="soft")
    result = run("arima_kinen", builds={...}, runs=1000)
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys

# --------------------------------------------------------------------------
# Numeric codes (from upstream RaceParameters.ts)
# --------------------------------------------------------------------------
SEASONS = {"spring": 1, "summer": 2, "autumn": 3, "winter": 4, "sakura": 5}
WEATHERS = {"sunny": 1, "cloudy": 2, "rainy": 3, "snowy": 4}
TIMES = {"notime": 0, "morning": 1, "midday": 2, "evening": 3, "night": 4}
GRADES = {"g1": 100, "g2": 200, "g3": 300, "op": 400, "preop": 700,
          "maiden": 800, "debut": 900, "daily": 999}
GROUNDS = ("good", "yielding", "soft", "heavy")

# Used when a template has no stats of its own (the race presets). Same numbers as
# the demo build in Simulator.py.
DEFAULT_STATS = {"speed": 1100, "stamina": 1000, "power": 900, "guts": 500, "wisdom": 600}

# --------------------------------------------------------------------------
# Template data
# --------------------------------------------------------------------------
# Generated from uma-skill-tools cmdefs/*.json. Skill ids are strings, as in Simulator's skills.json.
CM_TEMPLATES = {'cm_2023_05_tokyo2400': {'course': '10606',
                          'course_label': 'Tokyo 2400m turf',
                          'season': 'spring',
                          'ground': 'good',
                          'weather': 'sunny',
                          'time': None,
                          'stats': {'speed': 1500,
                                    'stamina': 1100,
                                    'power': 1200,
                                    'guts': 700,
                                    'wisdom': 1200},
                          'skills': {'nige': ['900041', '900201'],
                                     'senkou': ['900041', '910681'],
                                     'sasi': ['900041', '900591'],
                                     'oikomi': ['900041', '900591']},
                          'field': {'total_umas': 12,
                                    'strategy_positions': {'nige': [1],
                                                           'senkou': [1, 2, 3, 4, 5],
                                                           'sasi': [4, 5, 6, 7, 8, 9],
                                                           'oikomi': [4, 5, 6, 7, 8, 9, 10, 11, 12]}},
                          'source': 'cmdefs/2023-05.tokyo2400.cmdef.json'},
 'cm_2023_06_tokyo1600': {'course': '10602',
                          'course_label': 'Tokyo 1600m turf',
                          'season': 'spring',
                          'ground': 'heavy',
                          'weather': 'rainy',
                          'time': None,
                          'stats': {'speed': 1500,
                                    'stamina': 600,
                                    'power': 1200,
                                    'guts': 900,
                                    'wisdom': 1200},
                          'skills': {'nige': ['900201', '900141'],
                                     'senkou': ['900511'],
                                     'sasi': ['900271', '910611'],
                                     'oikomi': ['900271', '910611', '200642']},
                          'field': {'total_umas': 9,
                                    'strategy_positions': {'nige': [1],
                                                           'senkou': [1, 2, 3, 4],
                                                           'sasi': [5, 6, 7, 8, 9],
                                                           'oikomi': [5, 6, 7, 8, 9]}},
                          'source': 'cmdefs/2023-06.tokyo1600.cmdef.json'},
 'cm_2023_10_longchamp2400': {'course': '11203',
                              'course_label': 'Longchamp 2400m turf',
                              'season': 'autumn',
                              'ground': 'soft',
                              'weather': 'rainy',
                              'time': None,
                              'stats': {'speed': 1600,
                                        'stamina': 1200,
                                        'power': 1200,
                                        'guts': 800,
                                        'wisdom': 1100},
                              'skills': {'nige': ['900201', '910681'],
                                         'senkou': ['900511', '202711'],
                                         'sasi': ['900511', '202711'],
                                         'oikomi': ['900271', '200641']},
                              'field': {'total_umas': 9,
                                        'strategy_positions': {'nige': [1],
                                                               'senkou': [1, 2, 3, 4],
                                                               'sasi': [4, 5, 6, 7, 8, 9],
                                                               'oikomi': [4, 5, 6, 7, 8, 9]}},
                              'source': 'cmdefs/2023-10.longchamp2400.cmdef.json'},
 'cm_2023_11_kyoto1600': {'course': '10805',
                          'course_label': 'Kyoto 1600m turf',
                          'season': 'autumn',
                          'ground': 'good',
                          'weather': 'sunny',
                          'time': None,
                          'stats': {'speed': 1600,
                                    'stamina': 700,
                                    'power': 1250,
                                    'guts': 1300,
                                    'wisdom': 1200},
                          'skills': {'nige': ['900201'],
                                     'senkou': ['900511', '900101'],
                                     'sasi': [],
                                     'oikomi': []},
                          'field': {'total_umas': 12,
                                    'strategy_positions': {'nige': [1],
                                                           'senkou': [1, 2, 3, 4, 5],
                                                           'sasi': [4, 5, 6, 7, 8, 9],
                                                           'oikomi': [4, 5, 6, 7, 8, 9, 10, 11, 12]}},
                          'source': 'cmdefs/2023-11-kyoto1600.cmdef.json'},
 'cm_2023_12_nakayama2500': {'course': '10506',
                             'course_label': 'Nakayama 2500m turf',
                             'season': 'winter',
                             'ground': 'soft',
                             'weather': 'snowy',
                             'time': None,
                             'stats': {'speed': 1600,
                                       'stamina': 1200,
                                       'power': 1200,
                                       'guts': 800,
                                       'wisdom': 1100},
                             'skills': {'nige': ['900201', '900681'],
                                        'senkou': ['202481'],
                                        'sasi': ['900591', '202421'],
                                        'oikomi': ['900591', '200641']},
                             'field': {'total_umas': 9,
                                       'strategy_positions': {'nige': [1],
                                                              'senkou': [1, 2, 3, 4],
                                                              'sasi': [4, 5, 6, 7, 8, 9],
                                                              'oikomi': [4, 5, 6, 7, 8, 9]}},
                             'source': 'cmdefs/2023-12-nakayama2500.cmdef.json'},
 'cm_2024_01_kawasaki2100': {'course': '11303',
                             'course_label': 'Kawasaki 2100m dirt',
                             'season': 'winter',
                             'ground': 'good',
                             'weather': 'sunny',
                             'time': None,
                             'stats': {'speed': 1600,
                                       'stamina': 1000,
                                       'power': 1250,
                                       'guts': 1000,
                                       'wisdom': 1100},
                             'skills': {'nige': ['900681', '910201'],
                                        'senkou': ['900991', '910691'],
                                        'sasi': ['900991', '910691'],
                                        'oikomi': ['200641']},
                             'field': {'total_umas': 12,
                                       'strategy_positions': {'nige': [1],
                                                              'senkou': [1, 2, 3, 4, 5],
                                                              'sasi': [4, 5, 6, 7, 8, 9],
                                                              'oikomi': [4, 5, 6, 7, 8, 9, 10, 11, 12]}},
                             'source': 'cmdefs/2024-01-kawasaki2100.cmdef.json'},
 'cm_2024_02_hanshin1400': {'course': '10902',
                            'course_label': 'Hanshin 1400m turf',
                            'season': 'winter',
                            'ground': 'yielding',
                            'weather': 'cloudy',
                            'time': None,
                            'stats': {'speed': 1600,
                                      'stamina': 600,
                                      'power': 1250,
                                      'guts': 1200,
                                      'wisdom': 1200},
                            'skills': {'nige': ['900201'],
                                       'senkou': ['900101', '900511'],
                                       'sasi': ['900271'],
                                       'oikomi': ['900271']},
                            'field': {'total_umas': 9,
                                      'strategy_positions': {'nige': [1],
                                                             'senkou': [1, 2, 3, 4],
                                                             'sasi': [4, 5, 6, 7, 8, 9],
                                                             'oikomi': [4, 5, 6, 7, 8, 9]}},
                            'source': 'cmdefs/2024-02-hanshin1400.cmdef.json'},
 'cm_2024_04_hanshin1600': {'course': '10903',
                            'course_label': 'Hanshin 1600m turf',
                            'season': 'spring',
                            'ground': 'good',
                            'weather': 'sunny',
                            'time': None,
                            'stats': {'speed': 1700,
                                      'stamina': 700,
                                      'power': 1300,
                                      'guts': 1350,
                                      'wisdom': 1200},
                            'skills': {'nige': ['900201'],
                                       'senkou': ['900511'],
                                       'sasi': ['900271'],
                                       'oikomi': ['900271']},
                            'field': {'total_umas': 9,
                                      'strategy_positions': {'nige': [1],
                                                             'senkou': [1, 2, 3, 4],
                                                             'sasi': [4, 5, 6, 7, 8, 9],
                                                             'oikomi': [4, 5, 6, 7, 8, 9]}},
                            'source': 'cmdefs/2024-04-hanshin1600.cmdef.json'},
 'cm_2024_05_kyoto3200': {'course': '10811',
                          'course_label': 'Kyoto 3200m turf',
                          'season': 'spring',
                          'ground': 'good',
                          'weather': 'sunny',
                          'time': None,
                          'stats': {'speed': 1700,
                                    'stamina': 1300,
                                    'power': 1200,
                                    'guts': 1200,
                                    'wisdom': 1200},
                          'skills': {'nige': ['900681', '202822'],
                                     'senkou': ['202481'],
                                     'sasi': ['202421'],
                                     'oikomi': ['200641']},
                          'field': {'total_umas': 12,
                                    'strategy_positions': {'nige': [1],
                                                           'senkou': [1, 2, 3, 4, 5],
                                                           'sasi': [4, 5, 6, 7, 8, 9],
                                                           'oikomi': [4, 5, 6, 7, 8, 9, 10, 11, 12]}},
                          'source': 'cmdefs/2024-05-kyoto3200.cmdef.json'},
 'cm_2024_06_tokyo2400': {'course': '10606',
                          'course_label': 'Tokyo 2400m turf',
                          'season': 'spring',
                          'ground': 'soft',
                          'weather': 'cloudy',
                          'time': None,
                          'stats': {'speed': 1700,
                                    'stamina': 1250,
                                    'power': 1200,
                                    'guts': 1200,
                                    'wisdom': 1200},
                          'skills': {'nige': ['900041', '900201'],
                                     'senkou': ['900041', '202711'],
                                     'sasi': ['900041', '202711', '900591'],
                                     'oikomi': ['900041', '900591', '202872']},
                          'field': {'total_umas': 9,
                                    'strategy_positions': {'nige': [1],
                                                           'senkou': [1, 2, 3, 4],
                                                           'sasi': [4, 5, 6, 7, 8, 9],
                                                           'oikomi': [4, 5, 6, 7, 8, 9]}},
                          'source': 'cmdefs/2024-06-tokyo2400.cmdef.json'},
 'cm_2024_07_niigata1000': {'course': '10301',
                            'course_label': 'Niigata 1000m turf',
                            'season': 'summer',
                            'ground': 'good',
                            'weather': 'sunny',
                            'time': None,
                            'stats': {'speed': 1700,
                                      'stamina': 600,
                                      'power': 1500,
                                      'guts': 1500,
                                      'wisdom': 1200},
                            'skills': {'nige': [], 'senkou': [], 'sasi': [], 'oikomi': []},
                            'field': {'total_umas': 12,
                                      'strategy_positions': {'nige': [1],
                                                             'senkou': [1, 2, 3, 4, 5],
                                                             'sasi': [4, 5, 6, 7, 8, 9],
                                                             'oikomi': [4, 5, 6, 7, 8, 9, 10, 11, 12]}},
                            'source': 'cmdefs/2024-07-niigata1000.cmdef.json'},
 'cm_2024_08_chukyo1800': {'course': '10708',
                           'course_label': 'Chuukyo 1800m dirt',
                           'season': 'summer',
                           'ground': 'good',
                           'weather': 'sunny',
                           'time': None,
                           'stats': {'speed': 1750,
                                     'stamina': 867,
                                     'power': 1300,
                                     'guts': 1300,
                                     'wisdom': 1100},
                           'skills': {'nige': ['900041', '900201'],
                                      'senkou': ['900041', '910691'],
                                      'sasi': ['900591', '900271'],
                                      'oikomi': ['900591', '900271']},
                           'field': {'total_umas': 9,
                                     'strategy_positions': {'nige': [1],
                                                            'senkou': [1, 2, 3, 4],
                                                            'sasi': [4, 5, 6, 7, 8, 9],
                                                            'oikomi': [4, 5, 6, 7, 8, 9]}},
                           'source': 'cmdefs/2024-08-chukyo1800.cmdef.json'},
 'cm_2024_09_kyoto1600': {'course': '10805',
                          'course_label': 'Kyoto 1600m turf',
                          'season': 'autumn',
                          'ground': 'good',
                          'weather': 'sunny',
                          'time': None,
                          'stats': {'speed': 1750,
                                    'stamina': 800,
                                    'power': 1300,
                                    'guts': 1300,
                                    'wisdom': 1100},
                          'skills': {'nige': ['900201'],
                                     'senkou': ['900511', '900101'],
                                     'sasi': ['900271'],
                                     'oikomi': ['900271']},
                          'field': {'total_umas': 12,
                                    'strategy_positions': {'nige': [1],
                                                           'senkou': [1, 2, 3, 4, 5],
                                                           'sasi': [4, 5, 6, 7, 8, 9],
                                                           'oikomi': [4, 5, 6, 7, 8, 9, 10, 11, 12]}},
                          'source': 'cmdefs/2024-09-kyoto1600.cmdef.json'},
 'cm_2024_12_nakayama2500': {'course': '10506',
                             'course_label': 'Nakayama 2500m turf',
                             'season': 'winter',
                             'ground': 'yielding',
                             'weather': 'cloudy',
                             'time': None,
                             'stats': {'speed': 1750,
                                       'stamina': 1600,
                                       'power': 1300,
                                       'guts': 1200,
                                       'wisdom': 1200},
                             'skills': {'nige': ['202821'],
                                        'senkou': ['202481'],
                                        'sasi': ['202421'],
                                        'oikomi': ['200641']},
                             'field': {'total_umas': 9,
                                       'strategy_positions': {'nige': [1],
                                                              'senkou': [1, 2, 3, 4],
                                                              'sasi': [4, 5, 6, 7, 8, 9],
                                                              'oikomi': [4, 5, 6, 7, 8, 9]}},
                             'source': 'cmdefs/2024-12-nakayama2500.cmdef.json'},
 'cm_2025_01_hanshin2400': {'course': '10907',
                            'course_label': 'Hanshin 2400m turf',
                            'season': 'winter',
                            'ground': 'soft',
                            'weather': 'rainy',
                            'time': None,
                            'stats': {'speed': 1750,
                                      'stamina': 1600,
                                      'power': 1300,
                                      'guts': 1200,
                                      'wisdom': 1200},
                            'skills': {'nige': ['900041', '900201'],
                                       'senkou': ['900041', '202711'],
                                       'sasi': ['900041', '202711'],
                                       'oikomi': ['900041', '202872', '910331']},
                            'field': {'total_umas': 9,
                                      'strategy_positions': {'nige': [1],
                                                             'senkou': [1, 2, 3, 4],
                                                             'sasi': [4, 5, 6, 7, 8, 9],
                                                             'oikomi': [4, 5, 6, 7, 8, 9]}},
                            'source': 'cmdefs/2025-01-hanshin2400.cmdef.json'},
 'cm_2025_02_nakayama1200': {'course': '10501',
                             'course_label': 'Nakayama 1200m turf',
                             'season': 'winter',
                             'ground': 'good',
                             'weather': 'sunny',
                             'time': None,
                             'stats': {'speed': 1750,
                                       'stamina': 1500,
                                       'power': 1350,
                                       'guts': 1200,
                                       'wisdom': 1200},
                             'skills': {'nige': ['900201', '900871'],
                                        'senkou': ['900511', '900101'],
                                        'sasi': ['900511', '900101'],
                                        'oikomi': ['900511', '900101']},
                             'field': {'total_umas': 12,
                                       'strategy_positions': {'nige': [1],
                                                              'senkou': [1, 2, 3, 4, 5],
                                                              'sasi': [4, 5, 6, 7, 8, 9],
                                                              'oikomi': [4, 5, 6, 7, 8, 9, 10, 11, 12]}},
                             'source': 'cmdefs/2025-02-nakayama1200.cmdef.json'},
 'cm_2025_05_ooi2000': {'course': '11103',
                        'course_label': 'Ooi 2000m dirt',
                        'season': 'spring',
                        'ground': 'good',
                        'weather': 'sunny',
                        'time': 'night',
                        'stats': {'speed': 1850,
                                  'stamina': 1200,
                                  'power': 1350,
                                  'guts': 1350,
                                  'wisdom': 1400},
                        'skills': {'nige': ['910691'], 'senkou': ['910691'], 'sasi': [], 'oikomi': []},
                        'field': {'total_umas': 12,
                                  'strategy_positions': {'nige': [1],
                                                         'senkou': [1, 2, 3, 4, 5],
                                                         'sasi': [4, 5, 6, 7, 8, 9],
                                                         'oikomi': [4, 5, 6, 7, 8, 9, 10, 11, 12]}},
                        'source': 'cmdefs/2025-05-ooi2000.cmdef.json'},
 'cm_2025_07_hanshin2200': {'course': '10906',
                            'course_label': 'Hanshin 2200m turf',
                            'season': 'summer',
                            'ground': 'yielding',
                            'weather': 'cloudy',
                            'time': None,
                            'stats': {'speed': 1850,
                                      'stamina': 1500,
                                      'power': 1500,
                                      'guts': 1300,
                                      'wisdom': 1300},
                            'skills': {'nige': ['900201', '910681'],
                                       'senkou': ['910271', '910681'],
                                       'sasi': ['900591'],
                                       'oikomi': ['900591']},
                            'field': {'total_umas': 9,
                                      'strategy_positions': {'nige': [1],
                                                             'senkou': [1, 2, 3, 4],
                                                             'sasi': [4, 5, 6, 7, 8, 9],
                                                             'oikomi': [4, 5, 6, 7, 8, 9]}},
                            'source': 'cmdefs/2025-07-hanshin2200.cmdef.json'}}

# Hand-written. Season is the usual calendar slot of the race (assumption).
RACE_PRESETS = {'arima_kinen': {'course': '10506',
                 'course_label': 'Nakayama 2500m turf',
                 'season': 'winter',
                 'description': 'Arima Kinen (Nakayama 2500m turf, December)'},
 'japan_cup': {'course': '10606',
               'course_label': 'Tokyo 2400m turf',
               'season': 'autumn',
               'description': 'Japan Cup (Tokyo 2400m turf, late November)'},
 'tenno_sho_autumn': {'course': '10604',
                      'course_label': 'Tokyo 2000m turf',
                      'season': 'autumn',
                      'description': 'Tenno Sho Autumn (Tokyo 2000m turf, late October)'},
 'tenno_sho_spring': {'course': '10811',
                      'course_label': 'Kyoto 3200m turf',
                      'season': 'spring',
                      'description': 'Tenno Sho Spring (Kyoto 3200m turf, late April/May)'},
 'takarazuka_kinen': {'course': '10906',
                      'course_label': 'Hanshin 2200m turf',
                      'season': 'summer',
                      'description': 'Takarazuka Kinen (Hanshin 2200m turf, June)'}}


# --------------------------------------------------------------------------
# Lookup
# --------------------------------------------------------------------------
def _norm(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(name).lower()).strip("_")


def _all_templates() -> dict:
    out = {}
    for key, t in CM_TEMPLATES.items():
        out[key] = dict(t, kind="cm")
    for key, t in RACE_PRESETS.items():
        out[key] = dict(t, kind="preset")
    return out


def find_templates(text: str = "") -> list:
    """Template names matching `text` (substring of the name or course label)."""
    q = _norm(text)
    rows = []
    for key, t in _all_templates().items():
        if not q or q in key or q in _norm(t["course_label"]) or q in _norm(t.get("description", "")):
            rows.append(key)
    return rows


def get_template(name: str) -> dict:
    """Exact name first, then a unique substring match."""
    allt = _all_templates()
    key = _norm(name)
    if key in allt:
        return dict(allt[key], name=key)
    hits = find_templates(name)
    if len(hits) == 1:
        return dict(allt[hits[0]], name=hits[0])
    if not hits:
        raise ValueError(f"Unknown race template '{name}'. Try --list")
    raise ValueError(f"'{name}' matches several templates: {', '.join(hits)}")


def from_cmdef(cmdef, name: str | None = None) -> dict:
    """Build a template from a cmdef.json (path or already-loaded dict), e.g. a newer
    Champions Meeting than the ones embedded above."""
    if isinstance(cmdef, (str, bytes)) or hasattr(cmdef, "__fspath__"):
        with open(cmdef, encoding="utf-8") as fh:
            cmdef = json.load(fh)
    return {
        "name": name or f"cmdef_{cmdef['courseid']}", "kind": "cm",
        "course": str(cmdef["courseid"]), "course_label": f"course {cmdef['courseid']}",
        "season": cmdef["season"], "ground": cmdef["groundCondition"], "weather": cmdef["weather"],
        "time": cmdef.get("time"), "stats": dict(cmdef["baseStats"]),
        "skills": {k: [str(x) for x in v] for k, v in cmdef["presupposedSkills"].items()},
        "field": {"total_umas": cmdef.get("totalUmas"),
                  "strategy_positions": cmdef.get("strategyPositions")},
    }


# --------------------------------------------------------------------------
# Config building
# --------------------------------------------------------------------------
def _code(table: dict, value, what: str) -> int:
    if isinstance(value, int):
        return value
    key = str(value).strip().lower()
    if key.isdigit():
        return int(key)
    if key not in table:
        raise ValueError(f"Unknown {what} '{value}' (use {', '.join(table)} or a number)")
    return table[key]


def default_builds(t: dict) -> dict:
    """One build per running style for CM templates, one generic build for presets."""
    apt = {"distance": "A", "surface": "A", "strategy": "A"}
    if t.get("skills") and t.get("stats"):
        return {style: {"stats": dict(t["stats"]), "style": style, "aptitudes": dict(apt),
                        "skills": list(ids)}
                for style, ids in t["skills"].items()}
    return {"A": {"stats": dict(DEFAULT_STATS), "style": "pace", "aptitudes": dict(apt), "skills": []}}


def make_config(template, builds: dict | None = None, *, mood: int = 2, ground=None, weather=None,
                season=None, time=None, grade="g1", popularity: int = 1, runs: int = 500,
                seed: int = 1, wisdom_checks: bool = True) -> dict:
    """Simulator config for a template. `template` is a name or a template dict.
    Keyword arguments override the template's own values."""
    t = get_template(template) if isinstance(template, str) else template
    g = ground if ground is not None else t.get("ground", "good")
    if isinstance(g, str) and g.lower() not in GROUNDS and not g.isdigit():
        raise ValueError(f"Unknown ground '{g}' (use {', '.join(GROUNDS)})")
    w = weather if weather is not None else t.get("weather", "sunny")
    s = season if season is not None else t["season"]
    tm = time if time is not None else (t.get("time") or "midday")
    cfg = {
        "course": str(t["course"]),
        "ground": g,
        "mood": int(mood),
        "wisdom_checks": bool(wisdom_checks),
        "runs": int(runs), "seed": int(seed),
        "params": {
            "season": _code(SEASONS, s, "season"),
            "weather": _code(WEATHERS, w, "weather"),
            "time": _code(TIMES, tm, "time"),
            "grade": _code(GRADES, grade, "grade"),
            "popularity": int(popularity),
        },
        "builds": copy.deepcopy(builds) if builds else default_builds(t),
    }
    return cfg


def run(template, builds: dict | None = None, *, data_dir: str | None = None, workers: int = 1, **kw) -> dict:
    """Build the config and run it through Simulator.run_config (Simulator.py must be importable,
    i.e. in the same folder)."""
    from Simulator import run_config
    return run_config(make_config(template, builds, **kw), data_dir, max(1, workers))


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def _describe(t: dict) -> dict:
    out = {"name": t["name"], "kind": "Champions Meeting" if t["kind"] == "cm" else "race preset",
           "course": t["course"], "course_label": t["course_label"], "season": t["season"]}
    for k in ("description", "ground", "weather", "time", "source"):
        if t.get(k):
            out[k] = t[k]
    if t.get("field"):
        out["field_reference_only"] = t["field"]
    if t.get("stats"):
        out["default_stats"] = t["stats"]
        out["default_skills"] = t["skills"]
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Race templates for Simulator.py")
    ap.add_argument("name", nargs="?", help="template name (or a unique part of it)")
    ap.add_argument("--list", action="store_true", help="list templates (filtered by name, if given) and exit")
    ap.add_argument("--show", action="store_true", help="describe the template instead of printing a config")
    ap.add_argument("--run", action="store_true", help="run the simulation now (needs Simulator.py + data)")
    ap.add_argument("--cmdef", help="use a cmdef.json file as the template instead of a built-in one")
    ap.add_argument("--ground", help="good / yielding / soft / heavy")
    ap.add_argument("--weather", help="sunny / cloudy / rainy / snowy")
    ap.add_argument("--season", help="spring / summer / autumn / winter")
    ap.add_argument("--time", help="morning / midday / evening / night")
    ap.add_argument("--grade", default="g1")
    ap.add_argument("--mood", type=int, default=2)
    ap.add_argument("--runs", type=int, default=500)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--builds", help="JSON file holding the 'builds' section (replaces the template's default builds)")
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--data-dir")
    args = ap.parse_args(argv)
    try:
        if args.list:
            for key in find_templates(args.name or ""):
                t = get_template(key)
                extra = f"{t['season']}, {t.get('ground', 'good')}, {t.get('weather', 'sunny')}" if t["kind"] == "cm" \
                    else t.get("description", "")
                print(f"{key:34} {t['course']:>6}  {t['course_label']:26} {extra}")
            return 0
        if args.cmdef:
            t = from_cmdef(args.cmdef)
        elif args.name:
            t = get_template(args.name)
        else:
            ap.error("give a template name, or use --list")
        if args.show:
            print(json.dumps(_describe(t), ensure_ascii=False, indent=2))
            return 0
        builds = None
        if args.builds:
            with open(args.builds, encoding="utf-8") as fh:
                builds = json.load(fh)
        cfg = make_config(t, builds, mood=args.mood, ground=args.ground, weather=args.weather,
                          season=args.season, time=args.time, grade=args.grade,
                          runs=args.runs, seed=args.seed)
        if args.run:
            from Simulator import run_config
            cfg = run_config(cfg, args.data_dir, max(1, args.workers))
        print(json.dumps(cfg, ensure_ascii=False, indent=2))
    except (KeyError, ValueError, TypeError, FileNotFoundError, ImportError) as exc:
        print(json.dumps({"error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
