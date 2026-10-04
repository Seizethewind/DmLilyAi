# Optimization Plan (v2.1)

**Scope:** `LilyAiGameSpace/Umamusume/Guide/` (all paths below are relative to it unless stated). Tool and maintainer files live outside it, in the repo's `tools/` folder, and are marked where used.
**Goal:** Make small, targeted markdown changes so LilyAi can find the right document and the right section quickly.
**Branch:** `docs-optimization` (never commit to `main` directly)

---

## 1. Ground rules

1. **One phase = one commit.** Each phase touches one file or one tiny, uniform edit. Conditional sub-phases (for example 36a) get their own commit too.
2. **Move and label, don't rewrite.** Content is copied verbatim. Only headers, names, links, pointers and notes change. **Named exceptions** (each reviewed by diff before commit):
   - Phase 30: site-navigation boilerplate removed from CM20.
   - Phase 36a (conditional): newer or unique text merged into `SupportCardEncyclopedia.md`, copied verbatim.
   - Phase 37: the monolith body is replaced by an index, only after every line is accounted for.
   - Phase 43: guide-library section moved from `Readme.md` to `GuideIndex.md`.
3. **Every phase has a "Done when" check.** If it can't be checked, it's too big, so split it.
4. **Never rename or move a doc until Phase 04b is done.** The engine addresses docs by id (the path without `.md`, for example `Guide/RaceList/Racelist`), and `tests/test_game_space_engine.py` asserts some ids. The calculators only mention doc paths in comments, they do not open them. The baseline search results must exist before any rename.
5. **Renames update every reference, not only markdown links.** A rename phase is done only when a repo-wide search for the old filename (code, tests, workflows, RAG or ingestion config, docs) finds nothing left, and `tests/test_game_space_engine.py` still passes.
6. **Phases can be skipped or merged** if Phase 04 shows they aren't needed. Record skips in the log (section 5).
7. **Rollback:** each phase is one commit, so `git revert <commit>` undoes it.
8. **Batching aid (optional):** uniform phases (07-16 renames, 19-27 headers) may be applied by a script or workflow driven by one reviewed mapping table, as long as each phase is still its own commit.
9. **Generated files are not edited by hand.** `RaceList/Racelist.md` is rewritten by a workflow (see Appendix B). Any change to it goes into the generating script.

---

## 2. Known issues this plan targets

| ID | Issue | Type | Phases |
|----|-------|------|--------|
| I1 | ` Legacy.md` has a leading space in its filename | Bug | 05-06 |
| I2 | `Guide1.md` to `Guide9.md` have opaque names that say nothing about content | Search | 07-16 |
| I3 | No per-file metadata (source, date, server, status) | Search | 18-27 |
| I4 | Incomplete or stale files look current (Guide6/7/9 end mid-section, Guide4 stops at Sept 2024, CM20 expires Oct 2026) | Bug | 28-32 |
| I5 | `AdvanceGameplayGuide.md` is about 573 KB in one file | Search | 33-38 |
| I6 | Luh's support card encyclopedia exists in two places | Bug | 33-37 |
| I7 | Two compatibility files hold the same 135x135 data, and rosters (74 vs 135) are not labeled | Bug | 39-41 |
| I8 | Readme mixes club-bot docs with the guide library, and has a guessed description of the xlsx | Bug | 32, 42-43 |
| I9 | No question-to-file routing table | Search | 42-45 |
| I10 | Large files have no "what this answers / doesn't" summary | Search | 46 |
| I11 | Coverage gaps (Beyond Dreams scenario guide, rank/score thresholds in one place) | Gap | 49-50 |

### Plan risks and how this version handles them

| ID | Risk | Mitigation | Phases |
|----|------|------------|--------|
| R1 | Replacing the monolith could delete Section 3 if it is newer than the encyclopedia copy | Phase 33 confirms the exact section list. Phase 36 has three outcomes. Conditional Phase 36a merges first. Phase 37 is gated on both and verified line by line | 33, 36, 36a, 37 |
| R2 | No "before" result, so the plan's effect can't be shown | Runner built in 04a, baseline recorded in 04b, final run compared in 51 | 03, 04a, 04b, 51 |
| R3 | Renames break references outside `Guide/` (code, tests, workflows, ingestion config) | Phase 04 recorded every path reference (Appendix B). Link audits are repo-wide and also search plain path strings | 04, 17, 52 |
| R4 | Maintainer files inside the docs folder are indexed and pollute search | Phase 04 found that `_` files are indexed. Phase 04c moves them out of the docs folder | 04, 04c |
| R5 | Metadata headers do nothing for search because the engine ignores most fields | Phase 04 found only `title` and `aliases` are read. Phase 18 decides on engine change 18a | 04, 18, 18a |
| R6 | A workflow overwrites a hand-edited generated file | Phase 04 found `Racelist.md` is regenerated. Phase 27 changes the script instead (27a) | 04, 27, 27a |

---

## 3. Phases

### Track 0: Setup, audit and baseline (no content changes)

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 01 | repo | Create branch `docs-optimization` from `main`, and note the `main` commit hash in the log | Branch exists, hash noted |
| 02 | this plan, Appendix A | Record every `.md` file path and size as the baseline | Appendix A filled |
| 03 | `_SearchTests.md` (new) | Write 25 real questions LilyAi should answer, each with the expected file and section, plus an empty Baseline / Final result column | File committed |
| 04 | `UmamusumeGameSpaceEngine.py` (read-only) and a repo-wide search | Record in Appendix B: (a) how docs are chunked, (b) which files are skipped (for example names starting with `_`) and whether `INDEX.md` and nested `README.md` files are indexed, (c) whether front matter is stripped or chunked as body text, (d) how files are matched by name, (e) every place, code or config, that references a `Guide/` path or an old filename (including the calculators) | Appendix B filled, with a file list for (e) |
| 04c | `Guide/Optimization Plan.md`, `Guide/_SearchTests.md` (move) | Move both files out of the indexed docs folder into `tools/docs_optimization/` (as `Optimization Plan.md` and `SearchTests.md`). From here on, `_DocHeaderSchema.md` and `_Gaps.md` are created there too, without the leading underscore (`DocHeaderSchema.md`, `Gaps.md`). Update links and the paths named in this plan | The engine's `list_docs()` no longer shows these files, and no link to the old paths is left |
| 04a | `tools/run_search_tests.py` (new, outside `Guide/`) and a workflow `.github/workflows/search-tests.yml` | Script reads `tools/docs_optimization/SearchTests.md` and runs each question through the engine in three ways: `search(query)`, `search(query, category="Guide")` and `context_for(query)`. It reports whether the expected file appears in the top 5 hits and whether the expected section is the top section. The workflow runs the script and uploads the result table as an artifact, so it can be run without a local machine | Workflow run prints a pass/fail table for all 25 |
| 04b | `SearchTests.md`, Appendix C | Run the workflow on the untouched branch and record the **Baseline** column (for the unscoped and the `Guide` scoped search) | Baseline recorded for all 25. **Gate: no Track 1 work before this.** |

### Track 1: Filename and link bugs

Each rename phase also updates every reference found in Phase 04(e), per ground rule 5.

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 05 | `Uma Musume Legacies/ Legacy.md` | Rename to `Legacy.md`. Phase 04 found no code that opens it by path (only comments in `game_calcs.py` and a test comment, which already say `Legacy.md`) | File opens by new path, no old-name reference left, engine tests pass |
| 06 | `Readme.md` | Fix the link to `Legacy.md` | Link resolves |
| 07 | `CommunityGuide/Guide1.md` | Rename to `SupportCardEvaluation_celery6305.md`, update its Readme link | Link resolves, no old-name reference left |
| 08 | `CommunityGuide/Guide2.md` | Rename to `UmaMusumeReference_JP.md`, update link | Link resolves, no old-name reference left |
| 09 | `CommunityGuide/Guide3.md` | Rename to `RaceMechanics_KuromiAK.md`, update link | Link resolves, no old-name reference left |
| 10 | `CommunityGuide/Guide4.md` | Rename to `ChampionsMeetingGuides_pecan.md`, update link | Link resolves, no old-name reference left |
| 11 | `CommunityGuide/Guide5.md` | Rename to `Scenario_GrandMasters.md`, update link | Link resolves, no old-name reference left |
| 12 | `CommunityGuide/Guide6.md` | Rename to `Scenario_ProjectLArc.md`, update link | Link resolves, no old-name reference left |
| 13 | `CommunityGuide/Guide7.md` | Rename to `Scenario_UAFReadyGo.md`, update link | Link resolves, no old-name reference left |
| 14 | `CommunityGuide/Guide8.md` | Rename to `Scenario_RunMechaUmamusume.md`, update link | Link resolves, no old-name reference left |
| 15 | `CommunityGuide/Guide9.md` | Rename to `Scenario_GreatFoodFestival.md`, update link | Link resolves, no old-name reference left |
| 16 | `Champions Meeting/Cm20.md` | Rename to `ChampionsMeeting_CM20.md`, update link | Link resolves, no old-name reference left |
| 17 | **whole repo** | Audit: (a) every relative markdown link that no longer resolves, (b) a search for every old filename and old path string in code, tests, workflows and config, (c) the two docs that name the old files: `Guide/Readme.md` and `Umamusume/README.md` (which still says "Guide1 to Guide9") | All lists are empty, or each item is fixed in its own sub-phase (17a, 17b...) |

### Track 2: Metadata headers

Schema is defined first (Phase 18). Each later phase adds the same header block to a small group of files and changes nothing else.

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 18 | `tools/docs_optimization/DocHeaderSchema.md` (new) | Define the header fields: `title`, `source`, `author`, `server` (Global / JP / Both), `written`, `last_verified`, `status` (current / incomplete / archived), `topics`, `aliases`, and optional `expires` (date, used by CM20). **Format rules from Phase 04:** the header starts on the very first line with `---` and ends with `---`; one `key: value` per line; lists only inline like `[a, b]`; no multi-line YAML. **Engine behavior from Phase 04:** only `title` and `aliases` are read, so the other fields are for humans unless engine change **18a** is made (index `topics`, show `status`, `server` and `expires` in search hits). Decide on 18a here. Alias rule: no generic words (an alias makes every section of the doc rank higher and can trigger automatic chat context) | Schema committed, and the 18a decision is recorded (do it, or accept human-only fields) |
| 19 | Quickstart (2 files), New Player FAQ, Beginner Guide | Add header | 4 files have a valid header |
| 20 | `Career/CareerStartWorkflow.md`, `Career/Scenario/UraFinale.md` | Add header (CareerStartWorkflow already has a title, aliases and author header, so extend it) | Both valid |
| 21 | `UnityCup.md`, `UraFinaleVer2UnityCupVer2Updated.md`, `GrandLive.md`, `Trackblazer.md` | Add header | 4 valid |
| 22 | `AdvanceCareerGuide.md`, `Part1`, `Part2`, `Part3` | Add header | 4 valid |
| 23 | `Part4`, `Part5`, `Part6`, `SupportCardEncyclopedia.md` | Add header (encyclopedia keeps its 29/06/26 date unless Phase 36a changes it, in which case update the date in that phase) | 4 valid |
| 24 | The five renamed `Scenario_*.md` files | Add header, with the old filename (for example `Guide5`) kept in `aliases` so old references still resolve | 5 valid |
| 25 | The four other renamed community guides | Add header, with the old filename (for example `Guide1`) kept in `aliases` | 4 valid |
| 26 | `Legacy.md` and the three Affinity files | Add header | 4 valid |
| 27 | Race lists (except `Racelist.md`), `RaceMechanicHandBook.md`, `ChampionMeeting.md`, `ChampionsMeeting_CM20.md`, `PvpTeamTrials.md` | Add header | All valid |
| 27a | `.github/scripts/scrape_racelist.py` | Make `render()` write the `Racelist.md` header, because the racelist workflow rewrites the whole file. Do not hand-edit `Racelist.md` | Header present after a script run, and `tests/test_game_space_engine.py` still passes (it asserts the id `Guide/RaceList/Racelist`) |

### Track 3: Stale, incomplete and noisy files

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 28 | `Scenario_ProjectLArc.md`, `Scenario_UAFReadyGo.md`, `Scenario_GreatFoodFestival.md` | Set `status: incomplete` and add one line at the top: "File ends mid-section" | 3 files flagged |
| 29 | `ChampionsMeetingGuides_pecan.md` | Set `status: archived`, covering June 2023 to Sept 2024 | Flag present |
| 30 | `ChampionsMeeting_CM20.md` | Remove the site-navigation boilerplate only (named exception to rule 2), after reviewing the diff | Diff shows only boilerplate removed |
| 31 | `ChampionsMeeting_CM20.md` | Add `expires: 2026-10-16` to the header (field defined in Phase 18) | Field present |
| 32 | `Readme.md`, `Affinity/compatibility_chart.xlsx` | Verify what the xlsx actually contains and replace the "appears to be" wording with a confirmed description | No guessed wording left |

### Track 4: Split the monolith and remove the duplicate

Phases 33 to 37 (and 36a if triggered) must be done in order. The monolith is replaced only after every one of its lines is accounted for.

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 33 | `AdvanceGameplayGuide/README.md` (new) | Section map of the current file: exact section list (confirm there are exactly three), names, and start and end line numbers | Map matches the file, and the section count is stated |
| 34 | `AdvanceGameplayGuide/SkillsReference.md` (new) | Copy Section 1 verbatim, using a script that extracts the line range from the Phase 33 map | A diff of the new file body against the original line range is empty (a title line may be added), and table and row counts match |
| 35 | `AdvanceGameplayGuide/SparkProcsAndLineage.md` (new) | Copy Section 2 verbatim, same method | Diff empty, counts match |
| 36 | Section 3 vs `SupportCardEncyclopedia.md` | Diff the two copies and record the outcome (note only, no edit): **A** identical, **B** the encyclopedia is newer or a superset, **C** the monolith copy is newer or has unique content | Outcome A, B or C committed in the note, with the list of differences |
| 36a | `SupportCardEncyclopedia.md` | **Only if outcome C.** Merge the newer or unique text from the monolith verbatim, and update the header date | Re-running the Phase 36 diff shows no content that exists only in the monolith |
| 37 | `AdvanceGameplayGuide.md` | Replace the body with a short index pointing to `SkillsReference.md`, `SparkProcsAndLineage.md` and `SupportCardEncyclopedia.md`. Keep the filename, since other things may reference it. Gated on 33 to 36 (and 36a if triggered) | A line-coverage check shows every line of the old file now exists in exactly one target file, or is recorded as a duplicate in Phase 36 |
| 38 | `SkillsReference.md`, `SparkProcsAndLineage.md` | Add a table of contents to each | Every TOC link resolves |

### Track 5: Affinity data

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 39 | `compatibility_spreadsheet.md` | Add a note: same data as `compatibility_chart_boxes.md`, display copy only | Note present |
| 40 | The three Affinity files | State the roster in each header with exact counts taken from the data (Global roster vs full roster), not "about" | Exact numbers stated in all three and match the data |
| 41 | The three Affinity files | Link to `Legacy.md` and to the repo's `affinity_data/` as the machine-readable source | Links resolve |

### Track 6: Navigation aids

The routing file is named `GuideIndex.md`, not `INDEX.md`. The engine turns a filename into an alias, and a single-word alias of 5 or more letters that is not in its generic list (such as "index") would inject this file into chat whenever a message contains that word.

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 42 | `GuideIndex.md` (new) | Routing table: question type to file and section, built from `SearchTests.md`. Nested and top-level `README.md` files are indexed (Phase 04), so no engine change is needed | Every test question appears |
| 43 | `Readme.md`, `GuideIndex.md` | Move the guide library (section 5) into `GuideIndex.md` (named exception to rule 2), leave the club docs and a link in `Readme.md` | Readme covers only club docs, and nothing was lost |
| 44 | `GuideIndex.md` | Add a "Server" column (Global / JP / Both) from the headers | Column filled |
| 45 | `GuideIndex.md` | Link the Global-to-JP terminology map (in `AdvanceCareerGuide.md`) and the `Glossary` folder (found at `../Glossary/Glossary.md`, outside `Guide/`) | Both links resolve |
| 46 | The 10 largest files | Add a short block: "Answers: ... / Does not cover: ..." | 10 blocks added |
| 47 | Scenario docs | Add "See also" links from each scenario to its support card section and deck advice | Links resolve |
| 48 | `Career/Scenario/README.md` (new) | Comparison table: scenario, stat caps, release, doc link | One row per scenario doc |
| 49 | `Career/ResultEvaluationRefs.md` (new) | Pointer file: where rank and score thresholds live (Part1 tables and the scenario files), for the career evaluator. `CareerEvaluator.py` already cites `AdvanceCareerGuide/Part2_StatsAndRaceMechanics.md`, so keep those names | Every pointer resolves |
| 50 | `tools/docs_optimization/Gaps.md` (new) | List missing coverage, starting with a Beyond Dreams scenario guide | File committed |

### Track 7: Verify and finish

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 51 | `SearchTests.md`, Appendix C | Re-run the workflow from 04a and record the **Final** column next to the Baseline | Both columns filled, and no question that passed at baseline fails now |
| 52 | whole repo | Second audit, same scope as Phase 17 (links, old filenames, path strings, and the two docs that name files) | Zero broken links and zero old-name references |
| 53 | failures from 51 | One tiny phase per failure (53a, 53b...), fixing only what that question needs | Re-test passes |
| 54 | PR | Open a PR from `docs-optimization` and review the diff for accidental content changes | Diff shows only headers, names, links, pointers, notes and the named exceptions in rule 2 |

---

## 4. Order and dependencies

- **04, 04c and 04b gate everything.** Findings can change or remove phases in Tracks 1, 2 and 4, the maintainer files must be out of the docs folder before the baseline, and the baseline must exist before any rename.
- After 04c, the plan, the test set, the header schema and the gap list live in `tools/docs_optimization/`. Earlier text that says `_SearchTests.md`, `_DocHeaderSchema.md` or `_Gaps.md` means those files.
- Track 1 comes before Track 2, so headers are added to final filenames.
- Phase 18 depends on Phase 04 findings (only `title` and `aliases` are read).
- Phases 33 to 37 must be done in order, with 36a inserted only if Phase 36 gives outcome C.
- Track 6 comes last because `GuideIndex.md` depends on final names and headers.
- Phase 51 depends on 04b, so the comparison is like for like.

---

## 5. Phase log

| Phase | Status | Commit | Notes |
|-------|--------|--------|-------|
| 01 | done | `05406d2` | Branch `docs-optimization` already existed (head `057c186`, "docs: add Optimization Plan (54 phases)"), so it was reused. `main` was at `f7fb4ec04c6af37d82fc9cf2b5869b121c3b71ef` when checked, and code search of `main` already shows a copy of the v1 plan under `Guide/`. That commit replaced the v1 plan with v2 |
| 02 | done | `151850c` | Appendix A filled: 40 `.md` files plus 1 `.xlsx`. Sizes are bytes as reported by GitHub on the branch head |
| 03 | done (draft) | `1c94183` | `_SearchTests.md` has 25 questions built around training Kitasan Black, each with a form for any trainee. Questions 1 to 4 come from the project owner, 5 to 25 are drafted from guide headings and need owner review |
| 04 | done | this commit | Appendix B filled from the engine source and repo-wide searches. Six findings changed the plan (v2.1): new Phase 04c, 04a now uses a workflow and three search modes, Phase 18 format rules and 18a decision, Phase 27a for the generated `Racelist.md`, `INDEX.md` renamed `GuideIndex.md`, and rule 4 corrected |
| 04c, 04a, 04b | not started | | 04c comes first |
| 05-54 (plus conditional 18a, 36a) | not started | | |

---

## Appendix A: Baseline file list

Recorded in Phase 02 from branch `docs-optimization` (head `05406d2`). Sizes are in bytes. Paths are relative to `LilyAiGameSpace/Umamusume/Guide/`.

| # | Path | Size |
|---|------|------|
| 1 | `Readme.md` | 26,554 |
| 2 | `Optimization Plan.md` | this file (size changes with every phase) |
| 3 | `AdvanceCareerGuide/AdvanceCareerGuide.md` | 13,586 |
| 4 | `AdvanceCareerGuide/Part1_CareerTraining.md` | 29,132 |
| 5 | `AdvanceCareerGuide/Part2_StatsAndRaceMechanics.md` | 44,338 |
| 6 | `AdvanceCareerGuide/Part3_SupportCards.md` | 33,250 |
| 7 | `AdvanceCareerGuide/Part4_InheritanceAndParenting.md` | 33,602 |
| 8 | `AdvanceCareerGuide/Part5_SkillsAndPvP.md` | 29,291 |
| 9 | `AdvanceCareerGuide/Part6_AccountGachaEvents.md` | 18,965 |
| 10 | `AdvanceCareerGuide/SupportCardEncyclopedia.md` | 238,564 |
| 11 | `AdvanceGameplayGuide/AdvanceGameplayGuide.md` | 573,442 |
| 12 | `Affinity/compatibility_chart_boxes.md` | 99,796 |
| 13 | `Affinity/compatibility_spreadsheet.md` | 463,588 |
| 14 | `Affinity/umamusume_affinity_tables.md` | 63,603 |
| 15 | `Career/CareerStartWorkflow.md` | 9,940 |
| 16 | `Career/Scenario/GrandLive.md` | 19,986 |
| 17 | `Career/Scenario/Trackblazer.md` | 42,120 |
| 18 | `Career/Scenario/UnityCup.md` | 18,692 |
| 19 | `Career/Scenario/UraFinale.md` | 17,543 |
| 20 | `Career/Scenario/UraFinaleVer2UnityCupVer2Updated.md` | 9,445 |
| 21 | `Champions Meeting/ChampionMeeting.md` | 4,431 |
| 22 | `Champions Meeting/Cm20.md` | 51,954 |
| 23 | `CommunityGuide/Guide1.md` | 81,368 |
| 24 | `CommunityGuide/Guide2.md` | 488,420 |
| 25 | `CommunityGuide/Guide3.md` | 529,524 |
| 26 | `CommunityGuide/Guide4.md` | 184,134 |
| 27 | `CommunityGuide/Guide5.md` | 49,621 |
| 28 | `CommunityGuide/Guide6.md` | 20,273 |
| 29 | `CommunityGuide/Guide7.md` | 20,252 |
| 30 | `CommunityGuide/Guide8.md` | 39,614 |
| 31 | `CommunityGuide/Guide9.md` | 20,257 |
| 32 | `Race Mechanics Handbook/RaceMechanicHandBook.md` | 37,993 |
| 33 | `RaceList/Race.md` | 47,044 |
| 34 | `RaceList/Racelist.md` | 22,956 |
| 35 | `Team Trials PvP Scoring System/PvpTeamTrials.md` | 15,631 |
| 36 | `Uma Musume Guide For Absolute Beginners/BeginnerGuide.md` | 24,692 |
| 37 | `Uma Musume Legacies/ Legacy.md` (leading space in the filename) | 19,568 |
| 38 | `Umamusume Global Quickstart Guide/Readme.md` | 2,872 |
| 39 | `Umamusume Global Quickstart Guide/UmamusumeGlobalQuickstartGuide.md` | 4,899 |
| 40 | `Umamusume New Player FAQ/UmamusumeNewPlayerFAQ.md` | 9,039 |
| (non-md) | `Affinity/compatibility_chart.xlsx` | 81,581 |

**Ten largest files at baseline** (for Phase 46, before Track 4 shrinks the monolith): `AdvanceGameplayGuide.md` (573,442), `Guide3.md` (529,524), `Guide2.md` (488,420), `compatibility_spreadsheet.md` (463,588), `SupportCardEncyclopedia.md` (238,564), `Guide4.md` (184,134), `compatibility_chart_boxes.md` (99,796), `Guide1.md` (81,368), `umamusume_affinity_tables.md` (63,603), `Cm20.md` (51,954).

**Notes found while listing:**

- `Guide6.md`, `Guide7.md` and `Guide9.md` are almost the same size (20,273, 20,252 and 20,257 bytes). This fits the "ends mid-section" issue (I4) and suggests they were cut at a size limit. Worth checking in Phase 28.
- The `Glossary` folder that Phase 45 links to is not under `Guide/`. It exists one level up, at `LilyAiGameSpace/Umamusume/Glossary/Glossary.md`. Phase 45 should link to `../Glossary/Glossary.md`.
- Other docs the test questions use also live outside `Guide/`: `../Character/` (for example `Kitasan_Black.md`) and `../Support Cards/`. Phase 04 confirmed the engine indexes the whole `Umamusume/` folder.
- Two files are both named `Readme.md` (`Guide/Readme.md` and `Umamusume Global Quickstart Guide/Readme.md`), and there is a third `README.md` at `Umamusume/README.md`. Their ids differ, so nothing collides in the engine.
- `GuideIndex.md`, `DocHeaderSchema.md` and `Gaps.md` do not exist yet, as expected. `_SearchTests.md` was added in Phase 03.

## Appendix B: Engine audit findings

Recorded in Phase 04 from `LilyAiGameSpace/UmamusumeGameSpaceEngine.py` (blob `75152c0`) and repo-wide code searches. GitHub code search covers `main` only and skips very large files, so each result was cross-checked against the engine source and the tests.

### (a) What is indexed, chunking and ranking

- **Indexed set:** every `*.md` under `LilyAiGameSpace/Umamusume/` (Character, Guide, Support Cards, Glossary, Skill, and the root `README.md`). Not only `Guide/`.
- **Doc id** is the path inside that folder without `.md` (for example `Guide/Career/CareerStartWorkflow`). **Category** is the top folder.
- **Index timing:** built at startup, and re-scanned at most every 30 seconds, so doc edits need no restart.
- **Chunking:** split at headings `#` to `####` (headings inside code fences are ignored). Text before the first heading becomes a section named `Overview`. A section path is its headings below the H1 joined with ` > `. There is no size cap on a section.
- **Reading:** `read()` returns 6,000 characters by default and 12,000 at most, so anything past that in one section is cut off. Giant sections are not fully readable.
- **Ranking:** TF-IDF over heading plus text. Words in the heading path add 2 x idf. Words in the doc's name or aliases add 3 x idf to every matching section of that doc. Tokens are lowercased, a trailing "s" is stemmed, and stopwords are dropped. Section length is not normalized.
- **Search:** returns 5 hits by default (10 at most). `category` limits it to a top folder (for example `Guide`).
- **Hidden or unsearched:** the `Images` section is hidden everywhere. The `Sources` section is readable but not searched.

### (b) Skipped files

- Skipped: any file or folder whose path part starts with `.`, and any file over 2,000,000 bytes (the largest guide is 573,442).
- **Not skipped:** names starting with `_`. So `_SearchTests.md`, `_Gaps.md` and `_DocHeaderSchema.md` would all be indexed, and `Optimization Plan.md` already is. `_SearchTests.md` holds the exact question text, so it would be the top hit for those questions and make the baseline meaningless.
- **Indexed:** `INDEX.md`, top-level `README.md` and nested `README.md` files. Non-markdown files (the `.xlsx`) are not indexed.

### (c) Front matter

- A file that starts with `---` and has a closing `---` has that block removed from the body, so it is **not** chunked as text.
- It is read as one `key: value` per line. Lists must be inline (`[a, b]`). Multi-line YAML does not parse.
- **Only `title` and `aliases` are used.** `source`, `author`, `server`, `written`, `last_verified`, `status`, `topics` and `expires` are parsed and then ignored: they do not affect ranking and do not appear in results.
- The header must begin on the first line of the file.

### (d) Name matching

- **Aliases** come from: the title (front matter `title`, else the first H1, else the filename), the filename (underscores and hyphens as spaces, plus a camelCase split), the parent folder name for `README` files, front matter `aliases`, and Japanese names.
- **`resolve()`** tries: exact alias, then the longest alias contained in the query (4 letters or more), then a unique substring match, then fuzzy matching at 0.8.
- **Automatic chat context (`context_for`)** fires when a message contains a multi-word alias, or a single-word alias of 5 letters or more that is not in the engine's generic list (readme, overview, guide, guides, skill, skills, character, characters, support, card, cards, race, races, training, glossary, list). "index" is not in that list.
- **Renames** change the doc id and drop the old filename alias (for example `Guide1`), unless the old name is kept in front matter `aliases`. Titles come from the H1 and do not change.
- **`doc_boost` effect:** a query that names a character (for example "Kitasan Black") boosts every matching section of `Character/Kitasan_Black`, so that doc is likely to outrank the guides. Unscoped searches for the Kitasan questions are expected to fail more often. `search(..., category="Guide")` avoids this, and `context_for` for a message naming a character injects that character's sections, not guide sections.

### (e) References to doc paths outside the docs

| Where | What it contains | Effect on the plan |
|-------|------------------|--------------------|
| `LilyAiGameSpace/sandbox_scripts/game_calcs.py` | Module docstring and a comment name `Guide/Uma Musume Legacies/Legacy.md`, `Guide/Team Trials PvP Scoring System/PvpTeamTrials.md`, `Guide/Race Mechanics Handbook/RaceMechanicHandBook.md` | Comments only, nothing opens these files. Update the comment if one of them is renamed |
| `tests/test_sandbox_table_ops.py` | A comment citing `Legacy.md` | Comment only |
| `LilyAiGameSpace/CareerEvaluator.py` | Docstring cites `AdvanceCareerGuide/Part2_StatsAndRaceMechanics.md` and `Skill/skill.md` | Keep those names (Phase 49) |
| `tests/test_game_space_engine.py` | Asserts `resolve("race list")` gives `Guide/RaceList/Racelist`, and `search("arima kinen")[0]` is `Guide/RaceList/Racelist` | `Racelist.md` must keep that id and stay the top hit |
| `.github/scripts/scrape_racelist.py` and `.github/workflows/racelist.yml` | The script writes the whole `Guide/RaceList/Racelist.md`, and the workflow commits it | A hand-added header would be overwritten. Handled by Phase 27a |
| `LilyAiGameSpace/Umamusume/README.md` | Describes `Guide/` and names "CommunityGuide (Guide1 to Guide9...)" | Update in Phase 17 |
| `Guide/Readme.md` | Links such as `CommunityGuide/Guide2.md` | Updated by the rename phases and Phase 17 |
| `.github/workflows/*` for characters and support cards | Write to `Umamusume/Character` and `Umamusume/Support Cards` only | No effect on `Guide/` |
| Affinity files | No code references `compatibility_chart`, `umamusume_affinity_tables` or `compatibility_spreadsheet` | Safe to edit |
| `Cm20`, `Guide1` to `Guide9` | No code or workflow references | Safe to rename |

## Appendix C: Search test results

Per-question results live in the table inside the search test file. This appendix holds only the summary. Each run is recorded for the unscoped search and the `Guide` scoped search.

| Run | Phase | Unscoped passed | Guide-scoped passed | Date |
|-----|-------|-----------------|---------------------|------|
| Baseline | 04b | _/25 | _/25 | |
| Final | 51 | _/25 | _/25 | |

---

## Revision notes

**v1 to v2**

- Added Phases 04a and 04b (test runner and baseline), and moved the rename gate to 04b.
- Expanded Phase 04 (indexing rules, front matter, path references) and added ground rule 5.
- Made Phases 17 and 52 repo-wide and extended them to old filenames and path strings.
- Added Phase 33 section confirmation, a three-outcome Phase 36, conditional Phase 36a, and a line-coverage gate on Phase 37.
- Made Phases 34 and 35 script-based with an empty-diff check.
- Defined the `expires` field in Phase 18, with Phase 18 decisions based on Phase 04 findings.
- Listed named exceptions to the "verbatim" rule (Phases 30, 36a, 37, 43).
- Required exact roster counts in Phase 40.
- Added a risks table and an optional batching aid (rule 8).

**v2 to v2.1 (from the Phase 04 audit)**

- Added Phase 04c: move the plan and maintainer files out of the indexed docs folder.
- Phase 04a now runs through a workflow and tests three search modes (unscoped, `Guide` scoped, `context_for`).
- Phase 18 now has header format rules and a decision on engine change 18a, because only `title` and `aliases` are read.
- Added Phase 27a: the `Racelist.md` header is written by the generating script. Added ground rule 9.
- Renamed `INDEX.md` to `GuideIndex.md` (a single-word "index" alias would trigger automatic chat context).
- Phases 24 and 25 keep the old filenames as `aliases`.
- Corrected rule 4: calculators only mention paths in comments, while the engine and its tests rely on doc ids.
- Phase 17 and 52 also cover `Umamusume/README.md`.
- Added risks R4 to R6 and updated R3.
