---
title: Umamusume Taxonomy
aliases: [Taxonomy, Umamusume data taxonomy, data categories, naming rules]
---

# Umamusume Taxonomy

How Umamusume data is categorised and named in this project. The code side is `LilyAiGameSpace/Umamusume/Taxonomy.py` (standard library only, no data, no file access). This page explains the same categories in plain words. Canonical names are the **Global server's official English names** (for example Wit, not Wisdom). Older, fan or upstream names still work as aliases.

## Quick lookup

| Question is about... | Section |
|----------------------|---------|
| What the categories of skills are (tier, effect, scope) | Skills |
| What a stat, running style, distance type, ground or aptitude is called, and its number | Race basics |
| Support card types and rarities | Support cards |
| What kinds of things have ids (trainee, skill, course...) and where they live | Entities |
| Which mechanics topics exist | Mechanics |
| Why a name differs between files | Naming rules and known differences |

## Race basics

Each row is an enum in `Taxonomy.py`. The number is the value the upstream data and `Simulator.py` already use.

| Enum | Members (value) | Notes |
|------|-----------------|-------|
| `Stat` | speed, stamina, power, guts, wit | Upstream ids 1-5. The simulator and veteran JSON write `wisdom` for wit. |
| `RunningStyle` | Front Runner 1, Pace Chaser 2, Late Surger 3, End Closer 4, Runaway 5 | Skill conditions treat Runaway as a Front Runner. Aliases: nige, senkou, sashi, oikomi, oonige. |
| `Surface` | Turf 1, Dirt 2 | |
| `DistanceType` | Sprint 1, Mile 2, Medium 3, Long 4 | Standard bands: sprint up to 1400 m, mile up to 1800 m, medium up to 2400 m, long above. A course's own distance type is authoritative. |
| `Ground` | Firm 1, Good 2, Soft 3, Heavy 4 | Global names. See the known difference below. |
| `Aptitude` | S 0, A 1, B 2, C 3, D 4, E 5, F 6, G 7 | The number is a table index in the simulator, so S (best) is 0. |
| `Mood` | Awful -2, Bad -1, Normal 0, Good 1, Great 2 | The simulator's mood. The `motivation` skill condition is mood + 3. |
| `Phase` | Early 0, Middle 1, Late 2, Last Spurt 3 | Early is the first sixth of the course, Middle runs to two thirds, Late to five sixths, Last Spurt is the rest. |
| `Server` | Global, JP | Availability marker for entities. |

## Support cards

- `SupportType`: Speed, Stamina, Power, Guts, Wit, Friend, Group. The wiki calls Friend "Pal". Speed to Wit map to a `Stat`; Friend and Group do not.
- `SupportRarity`: SSR, SR, R.

These match the section and file names in `Support Cards/`.

## Skills

A skill is classified on independent axes, because it is several things at once.

**1. Tier** (`SkillTier`): how it is obtained.

| Tier | Meaning |
|------|---------|
| normal | White skill, bought with Skill Points |
| rare | Gold skill, bought with Skill Points |
| unique | A character's own unique skill |
| inherited_unique | The weaker copy passed down with a Green Spark. Game8 treats it as a normal skill. In the data its id has six digits and starts with 9. |
| negative | Purple skill gained by losing races |

**2. Effect** (`SkillEffect`): what it does.

| Effect | Meaning | Game8 label |
|--------|---------|-------------|
| velocity | Raises speed | Velocity |
| acceleration | Raises acceleration | Acceleration |
| recovery | Restores or saves stamina | Recovery |
| positioning | Position, navigation, passing, field of view, slow start, slopes | Speed - Other |
| passive | Stat and performance boosts (season, weather, track, distance...) | Green Skill |
| debuff | Aimed at other runners | Debuff |

A skill can have more than one effect, so effect is a set. Game8's "Unique Skill" and "Negative" labels name a tier and say nothing about the effect.

**3. Scope**: where it works at all. The words in skill.md such as "(Long)" or "(Front Runner)" map to a running style, a distance type or a surface.

**4. Level mark** (`LevelMark`): none, single circle (1), double circle (2), or the cross on negative skills.

**5. Trigger context** (`ConditionKind`): how the simulator treats a condition key.

| Kind | Meaning | Examples |
|------|---------|----------|
| static | Fixed before the race | ground condition, season, base stats |
| region | A stretch of the course | phase, corner, final straight, slope |
| dynamic | Depends on the live race | HP percent, last spurt, skills used so far |
| opponent | Depends on other runners | order, overtakes, blocking |

**6. Simulator status** (`SimStatus`): ok, approx, unsupported, inactive. This is an implementation fact about `Simulator.py`, not a game category, and is kept apart from the rest.

## Entities

`EntityKind` lists the things that have ids. It mirrors the Database sections of GameTora.

| Kind | Where it lives in the repo today |
|------|----------------------------------|
| trainee | `Umamusume/Character/` (one file per character) |
| support_card | `Umamusume/Support Cards/` |
| skill | `Umamusume/Skill/skill.md`, `skill_library.md`, `tools/sim_data/skills.json`, `skill_aliases.json` |
| course | `tools/sim_data/courses.json` |
| racetrack, race, scenario, event, factor, item, epithet | Not stored as structured data yet (some are covered in `Guide/`) |

## Mechanics

`MechanicDomain` groups the rules of the game. Each domain has topics.

| Domain | Topics |
|--------|--------|
| career | training, stat growth, energy and mood, inheritance, affinity, objectives, scenarios, events, support deck |
| race | phases, running styles, stamina and HP, last spurt, position keep, rushed, course geometry, ground and weather, skill activation |
| mode | Champions Meeting, Team Trials, League of Heroes, Monthly Match |
| economy | carats, gacha, items, missions |

Definitions of the terms themselves are in `Glossary/Glossary.md`; strategy is in `Guide/`.

## Naming rules and known differences

- **Wit, not Wisdom.** Wit is the Global name. Upstream data, `Simulator.py` configs and veteran JSON keep the key `wisdom`; both spellings are accepted when reading.
- **Friend, not Pal.** Same reason.
- **Ground names differ between sources.** Global says Firm, Good, Soft, Heavy for 1 to 4. Upstream data and `Simulator.py` say good, yielding, soft, heavy, so their word "good" means Firm (1), while Global "Good" is 2. `Taxonomy.py` follows Global. When you read an upstream name, translate it first. `Simulator.py` is unchanged and still reads "good" as 1.
- **Skills have three names**: the in-game Global name, the upstream English name (often a fan translation) and the Japanese name. `tools/sim_data/skill_aliases.json` links the Global names to ids.
- **Running style, strategy and style** all mean the same thing. The canonical term is running style.

## Sources

- https://uma.guide/
- https://gametora.com/umamusume
- https://github.com/alpha123/uma-skill-tools (datamined skill and course data behind the simulator)
