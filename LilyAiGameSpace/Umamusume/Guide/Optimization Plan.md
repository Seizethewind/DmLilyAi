# Optimization Plan

**Scope:** `LilyAiGameSpace/Umamusume/Guide/` (all paths below are relative to it unless stated)
**Goal:** Make small, targeted markdown changes so LilyAi can find the right document and the right section quickly.
**Branch:** `docs-optimization` (never commit to `main` directly)

---

## 1. Ground rules

1. **One phase = one commit.** Each phase touches one file or one tiny, uniform edit.
2. **Move and label, don't rewrite.** Content is copied verbatim. Only headers, names, links, pointers and notes change.
3. **Every phase has a "Done when" check.** If it can't be checked, it's too big, so split it.
4. **Never rename or move a file until Phase 04 is done.** The calculators and the docs engine read some files by path (at least `Legacy.md`, `PvpTeamTrials.md`, `RaceMechanicHandBook.md`).
5. **Phases can be skipped or merged** if Phase 04 shows they aren't needed. Record skips in the log (section 5).
6. **Rollback:** each phase is one commit, so `git revert <commit>` undoes it.

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

---

## 3. Phases

### Track 0: Setup and audit (no content changes)

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 01 | repo | Create branch `docs-optimization` from `main` | Branch exists |
| 02 | this plan, Appendix A | Record every `.md` file path and size as the baseline | Appendix A filled |
| 03 | `_SearchTests.md` (new) | Write 25 real questions LilyAi should answer, each with the expected file and section | File committed |
| 04 | `UmamusumeGameSpaceEngine.py` (read-only) | Record in Appendix B: how docs are chunked, which files are skipped (for example names starting with `_`), whether front matter is stripped, how files are matched by name, and which docs the calculators open by path | Appendix B filled. **Gate: no Track 1 work before this.** |

### Track 1: Filename and link bugs

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 05 | `Uma Musume Legacies/ Legacy.md` | Rename to `Legacy.md`, and update any path found in Phase 04 | File opens by new path, calculator still runs |
| 06 | `Readme.md` | Fix the link to `Legacy.md` | Link resolves |
| 07 | `CommunityGuide/Guide1.md` | Rename to `SupportCardEvaluation_celery6305.md`, update its Readme link | Link resolves |
| 08 | `CommunityGuide/Guide2.md` | Rename to `UmaMusumeReference_JP.md`, update link | Link resolves |
| 09 | `CommunityGuide/Guide3.md` | Rename to `RaceMechanics_KuromiAK.md`, update link | Link resolves |
| 10 | `CommunityGuide/Guide4.md` | Rename to `ChampionsMeetingGuides_pecan.md`, update link | Link resolves |
| 11 | `CommunityGuide/Guide5.md` | Rename to `Scenario_GrandMasters.md`, update link | Link resolves |
| 12 | `CommunityGuide/Guide6.md` | Rename to `Scenario_ProjectLArc.md`, update link | Link resolves |
| 13 | `CommunityGuide/Guide7.md` | Rename to `Scenario_UAFReadyGo.md`, update link | Link resolves |
| 14 | `CommunityGuide/Guide8.md` | Rename to `Scenario_RunMechaUmamusume.md`, update link | Link resolves |
| 15 | `CommunityGuide/Guide9.md` | Rename to `Scenario_GreatFoodFestival.md`, update link | Link resolves |
| 16 | `Champions Meeting/Cm20.md` | Rename to `ChampionsMeeting_CM20.md`, update link | Link resolves |
| 17 | whole `Guide/` tree | Link audit: list every relative link that no longer resolves | Broken-link list is empty, or each item is fixed in its own sub-phase (17a, 17b...) |

### Track 2: Metadata headers

Schema is defined first (Phase 18). Each later phase adds the same header block to a small group of files and changes nothing else.

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 18 | `_DocHeaderSchema.md` (new) | Define the header fields: `title`, `source`, `author`, `server` (Global / JP / Both), `written`, `last_verified`, `status` (current / incomplete / archived), `topics`, `aliases` | Schema committed, and Phase 04 confirms the engine tolerates it |
| 19 | Quickstart (2 files), New Player FAQ, Beginner Guide | Add header | 4 files have a valid header |
| 20 | `Career/CareerStartWorkflow.md`, `Career/Scenario/UraFinale.md` | Add header | Both valid |
| 21 | `UnityCup.md`, `UraFinaleVer2UnityCupVer2Updated.md`, `GrandLive.md`, `Trackblazer.md` | Add header | 4 valid |
| 22 | `AdvanceCareerGuide.md`, `Part1`, `Part2`, `Part3` | Add header | 4 valid |
| 23 | `Part4`, `Part5`, `Part6`, `SupportCardEncyclopedia.md` | Add header (encyclopedia keeps its 29/06/26 date) | 4 valid |
| 24 | The five renamed `Scenario_*.md` files | Add header | 5 valid |
| 25 | The four other renamed community guides | Add header | 4 valid |
| 26 | `Legacy.md` and the three Affinity files | Add header | 4 valid |
| 27 | Race lists, `RaceMechanicHandBook.md`, `ChampionMeeting.md`, `ChampionsMeeting_CM20.md`, `PvpTeamTrials.md` | Add header | All valid |

### Track 3: Stale, incomplete and noisy files

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 28 | `Scenario_ProjectLArc.md`, `Scenario_UAFReadyGo.md`, `Scenario_GreatFoodFestival.md` | Set `status: incomplete` and add one line at the top: "File ends mid-section" | 3 files flagged |
| 29 | `ChampionsMeetingGuides_pecan.md` | Set `status: archived`, covering June 2023 to Sept 2024 | Flag present |
| 30 | `ChampionsMeeting_CM20.md` | Remove the site-navigation boilerplate only, after reviewing the diff | Diff shows only boilerplate removed |
| 31 | `ChampionsMeeting_CM20.md` | Add `expires: 2026-10-16` to the header | Field present |
| 32 | `Readme.md`, `Affinity/compatibility_chart.xlsx` | Verify what the xlsx actually contains and replace the "appears to be" wording with a confirmed description | No guessed wording left |

### Track 4: Split the monolith and remove the duplicate

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 33 | `AdvanceGameplayGuide/README.md` (new) | Section map of the current file (section names, approximate line ranges) | Map matches the file |
| 34 | `AdvanceGameplayGuide/SkillsReference.md` (new) | Copy Section 1 verbatim | Table count and row count match the original |
| 35 | `AdvanceGameplayGuide/SparkProcsAndLineage.md` (new) | Copy Section 2 verbatim | Counts match |
| 36 | Section 3 vs `SupportCardEncyclopedia.md` | Diff the two copies and record which is newer (note only, no edit) | Note committed |
| 37 | `AdvanceGameplayGuide.md` | Replace the body with a short index pointing to the three files. Keep the filename, since other things may reference it | Old content exists only in the new files |
| 38 | `SkillsReference.md`, `SparkProcsAndLineage.md` | Add a table of contents to each | Every TOC link resolves |

### Track 5: Affinity data

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 39 | `compatibility_spreadsheet.md` | Add a note: same data as `compatibility_chart_boxes.md`, display copy only | Note present |
| 40 | The three Affinity files | State the roster in each header: 74 Global characters vs about 135 characters | Roster stated in all three |
| 41 | The three Affinity files | Link to `Legacy.md` and to the repo's `affinity_data/` as the machine-readable source | Links resolve |

### Track 6: Navigation aids

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 42 | `INDEX.md` (new) | Routing table: question type to file and section, built from `_SearchTests.md` | Every test question appears |
| 43 | `Readme.md`, `INDEX.md` | Move the guide library (section 5) into `INDEX.md`, leave the club docs and a link in `Readme.md` | Readme covers only club docs |
| 44 | `INDEX.md` | Add a "Server" column (Global / JP / Both) from the headers | Column filled |
| 45 | `INDEX.md` | Link the Global-to-JP terminology map (in `AdvanceCareerGuide.md`) and the `Glossary` folder | Both links resolve |
| 46 | The 10 largest files | Add a short block: "Answers: ... / Does not cover: ..." | 10 blocks added |
| 47 | Scenario docs | Add "See also" links from each scenario to its support card section and deck advice | Links resolve |
| 48 | `Career/Scenario/README.md` (new) | Comparison table: scenario, stat caps, release, doc link | One row per scenario doc |
| 49 | `Career/ResultEvaluationRefs.md` (new) | Pointer file: where rank and score thresholds live (Part1 tables and the scenario files), for the career evaluator | Every pointer resolves |
| 50 | `_Gaps.md` (new) | List missing coverage, starting with a Beyond Dreams scenario guide | File committed |

### Track 7: Verify and finish

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 51 | `_SearchTests.md` | Re-run all 25 questions and record pass or fail | Results recorded |
| 52 | whole `Guide/` tree | Second link audit | Zero broken links |
| 53 | failures from 51 | One tiny phase per failure (53a, 53b...), fixing only what that question needs | Re-test passes |
| 54 | PR | Open a PR from `docs-optimization` and review the diff for accidental content changes | Diff shows only headers, names, links, pointers and notes |

---

## 4. Order and dependencies

- **04 gates everything.** Its findings can change or remove phases in Tracks 1, 2 and 4.
- Track 1 comes before Track 2, so headers are added to final filenames.
- Phases 34-37 must be done in order. The monolith is replaced only after the copies are verified.
- Track 6 comes last because `INDEX.md` depends on final names and headers.

---

## 5. Phase log

| Phase | Status | Commit | Notes |
|-------|--------|--------|-------|
| 01 | done | branch `docs-optimization` created from `main` (b3a4c94) | |
| 02-54 | not started | | |

---

## Appendix A: Baseline file list

_To be filled in Phase 02._

## Appendix B: Engine audit findings

_To be filled in Phase 04._
