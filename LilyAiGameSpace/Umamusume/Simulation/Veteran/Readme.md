# Veteran

> **In the bot,** veterans and results are stored per user in the database (`LilyAiMemory/Veteran`), not in this folder, and the bot reaches the simulator only through `../sim_service.py`.
> This folder and `../VeteranStore.py` are for command-line use and for committing example veterans.

This folder holds **veterans** (finished Uma Musume trainees) and the **results of simulations** run on them.
The files here are written by `../VeteranStore.py`. The Simulator itself never writes files; it only prints JSON.

## Layout

```
Veteran/
  Readme.md
  veteran_oguri_cap.json            one veteran
  veteran_oguri_cap_2.json          same character, different stats = a different veteran
  results/
    veteran_oguri_cap/
      10606_20261006T120000Z.json   one simulation run (course id + UTC time)
```

## How a veteran gets here

1. A user uploads veteran screenshots to the bot.
2. `VeteranIntake.intake_images()` sends each image to the vision AI, checks the reply, and merges
   screenshots of the same veteran (same name and same five stats) into one.
3. `VeteranStore.save_intake(outcome)` validates each veteran and writes `veteran_<name>.json`.

Saving rules:

- File name comes from the character name (letters and digits only). Names with no latin letters get a short hash of the stats.
- Same name **and** same five stats already saved: the skills are merged in (duplicates dropped, missing aptitudes filled). Status is `updated` or `unchanged`.
- Same name but different stats: a new file with `_2`, `_3`, and so on. Existing veterans are not overwritten.
- A veteran with an unreadable stat is rejected and nothing is written.

## Veteran file format

```json
{
  "name": "Oguri Cap",
  "stats": {"speed": 1608, "stamina": 747, "power": 1250, "guts": 623, "wisdom": 775},
  "aptitudes": {
    "distance": {"short": "E", "mile": "A", "medium": "A", "long": "S"},
    "surface":  {"turf": "A", "dirt": "B"},
    "strategy": {"front": "S", "pace": "A", "late": "A", "end": "D"}
  },
  "skills": ["Top Runner", "Moxie", "Groundwork"]
}
```

- Stats are whole numbers. Aptitudes are letters S to G, or `null` when they could not be read.
- Skills are stored as **names**, exactly as read. They are turned into skill ids only when a build is made
  (`VeteranReader.to_build`). Names may be the in-game (Global) name, the upstream English name, the Japanese name or a skill id; case, punctuation and the circle spelling (○ ◯ O) do not matter. The Global names come from `tools/sim_data/skill_aliases.json`. A name that matches nothing is skipped with a warning that lists the closest skills.

## Simulating a veteran

The Simulator uses a veteran through `VeteranReader.to_build(veteran, course, style)`. Only three aptitudes matter
for a race: the distance of the course, turf or dirt, and the running style chosen (default: the veteran's best style).

```
python VeteranStore.py list
python VeteranStore.py simulate oguri_cap --course 10606 --style pace --runs 500
python VeteranStore.py simulate oguri_cap --course 10606 --add-skill "Corner Accel ○"
python VeteranStore.py results oguri_cap
```

- Build **A** is the veteran as stored. With `--add-skill`, build **B** is the same veteran plus those skills,
  and the result contains the A vs B comparison.
- Find course ids with `python ../Simulator.py --list-courses tokyo`.
- Use `--no-store` to print a result without saving it.

## Result file format

```json
{
  "saved_at": "2026-10-06T12:00:00+00:00",
  "veteran_file": "veteran_oguri_cap.json",
  "config": { "course": "10606", "ground": 1, "mood": 2, "runs": 500, "seed": 1, "builds": { "A": {} } },
  "result": { "course": "...", "A": { "mean_s": 0, "median_s": 0, "p05_s": 0, "p95_s": 0, "out_of_hp_rate": 0, "skills": {} } }
}
```

`config` is exactly what was given to the Simulator, so a run can be repeated: same config and seed give the same result.
Skill problems found while making the build are listed under `result.build_warnings`.

## Notes

- The Simulator is a single-runner model. Conditions about other runners are assumed true and those skills are flagged as approximate in the warnings. See the docstring of `../Simulator.py`.
- Simulation results are only worth comparing when they use the same course, ground, mood and run count.
- On a host such as Render the disk is reset on each deploy unless a persistent disk is attached.
  Files written by the bot are lost on redeploy unless you add a disk or commit them back to the repo.
