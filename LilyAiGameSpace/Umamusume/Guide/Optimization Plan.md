# Optimization Plan (v2)

**Scope:** `LilyAiGameSpace/Umamusume/Guide/` (all paths below are relative to it unless stated). Two tool files live outside it, in the repo's `tools/` folder, and are marked where used.
**Goal:** Make small, targeted markdown changes so LilyAi can find the right document and the right section quickly.
**Branch:** `docs-optimization` (never commit to `main` directly)

---

## 1. Ground rules

1. **One phase = one commit.** Each phase touches one file or one tiny, uniform edit. Conditional sub-phases (for example 36a) get their own commit too.
2. **Move and label, don't rewrite.** Content is copied verbatim. Only headers, names, links, pointers and notes change. **Named exceptions** (each reviewed by diff before commit):
   - Phase 30: site-navigation boilerplate removed from CM20.
   - Phase 36a (conditional): newer or unique text merged into `SupportCardEncyclopedia.md`, copied verbatim.
   - Phase 37: the monolith body is replaced by an index, only after every line is accounted for.
   - Phase 43: guide-library section moved from `Readme.md` to `INDEX.md`.
3. **Every phase has a "Done when" check.** If it can't be checked, it's too big, so split it.
4. **Never rename or move a file until Phase 04b is done.** The calculators and the docs engine read some files by path (at least `Legacy.md`, `PvpTeamTrials.md`, `RaceMechanicHandBook.md`), and the baseline search results must exist first.
5. **Renames update every reference, not only markdown links.** A rename phase is done only when a repo-wide search for the old filename (code, tests, workflows, RAG or ingestion config, docs) finds nothing left.
6. **Phases can be skipped or merged** if Phase 04 shows they aren't needed. Record skips in the log (section 5).
7. **Rollback:** each phase is one commit, so `git revert <commit>` undoes it.
8. **Batching aid (optional):** uniform phases (07-16 renames, 19-27 headers) may be applied by a script or workflow driven by one reviewed mapping table, as long as each phase is still its own commit.

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
| R3 | Renames break references outside `Guide/` (code, tests, workflows, ingestion config) | Phase 04 records every path reference. Link audits are repo-wide and also search plain path strings | 04, 17, 52 |
| R4 | Underscore files or front matter behave badly in the engine (skipped, or chunked as body text) | Phase 04 records the exact rules. Phase 18 and Phase 42 have explicit decisions based on them | 04, 18, 42 |

---

## 3. Phases

### Track 0: Setup, audit and baseline (no content changes)

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 01 | repo | Create branch `docs-optimization` from `main`, and note the `main` commit hash in the log | Branch exists, hash noted |
| 02 | this plan, Appendix A | Record every `.md` file path and size as the baseline | Appendix A filled |
| 03 | `_SearchTests.md` (new) | Write 25 real questions LilyAi should answer, each with the expected file and section, plus an empty Baseline / Final result column | File committed |
| 04 | `UmamusumeGameSpaceEngine.py` (read-only) and a repo-wide search | Record in Appendix B: (a) how docs are chunked, (b) which files are skipped (for example names starting with `_`) and whether `INDEX.md` and nested `README.md` files are indexed, (c) whether front matter is stripped or chunked as body text, (d) how files are matched by name, (e) every place, code or config, that references a `Guide/` path or an old filename (including the calculators) | Appendix B filled, with a file-and-line list for (e) |
| 04a | `tools/run_search_tests.py` (new, outside `Guide/`) | Script that reads `_SearchTests.md`, runs each question through the engine's retrieval, and reports whether the expected file appears in the top results (and whether the expected section is in the top chunk) | Script runs and prints a pass/fail table |
| 04b | `_SearchTests.md`, Appendix C | Run the script on the untouched branch and record the **Baseline** column | Baseline recorded for all 25. **Gate: no Track 1 work before this.** |

### Track 1: Filename and link bugs

Each rename phase also updates every reference found in Phase 04(e), per ground rule 5.

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 05 | `Uma Musume Legacies/ Legacy.md` | Rename to `Legacy.md`, and update any path found in Phase 04 | File opens by new path, calculator still runs, no old-name reference left |
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
| 17 | **whole repo** | Audit: (a) every relative markdown link that no longer resolves, (b) a search for every old filename and old path string in code, tests, workflows and config | Both lists are empty, or each item is fixed in its own sub-phase (17a, 17b...) |

### Track 2: Metadata headers

Schema is defined first (Phase 18). Each later phase adds the same header block to a small group of files and changes nothing else.

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 18 | `_DocHeaderSchema.md` (new) | Define the header fields: `title`, `source`, `author`, `server` (Global / JP / Both), `written`, `last_verified`, `status` (current / incomplete / archived), `topics`, `aliases`, and optional `expires` (date, used by CM20). Use the Phase 04 findings to decide: if front matter is stripped, keep the full schema. If it is chunked as body text, keep headers compact and decide whether the engine should strip them (a separate code-change phase, 18a). If `_` files are skipped, confirm that is the intent for `_SearchTests.md`, `_Gaps.md` and this file | Schema committed, and Appendix B confirms the engine tolerates it, with any 18a decision recorded |
| 19 | Quickstart (2 files), New Player FAQ, Beginner Guide | Add header | 4 files have a valid header |
| 20 | `Career/CareerStartWorkflow.md`, `Career/Scenario/UraFinale.md` | Add header | Both valid |
| 21 | `UnityCup.md`, `UraFinaleVer2UnityCupVer2Updated.md`, `GrandLive.md`, `Trackblazer.md` | Add header | 4 valid |
| 22 | `AdvanceCareerGuide.md`, `Part1`, `Part2`, `Part3` | Add header | 4 valid |
| 23 | `Part4`, `Part5`, `Part6`, `SupportCardEncyclopedia.md` | Add header (encyclopedia keeps its 29/06/26 date unless Phase 36a changes it, in which case update the date in that phase) | 4 valid |
| 24 | The five renamed `Scenario_*.md` files | Add header | 5 valid |
| 25 | The four other renamed community guides | Add header | 4 valid |
| 26 | `Legacy.md` and the three Affinity files | Add header | 4 valid |
| 27 | Race lists, `RaceMechanicHandBook.md`, `ChampionMeeting.md`, `ChampionsMeeting_CM20.md`, `PvpTeamTrials.md` | Add header | All valid |

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

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 42 | `INDEX.md` (new) | Routing table: question type to file and section, built from `_SearchTests.md`. Confirm from Appendix B that `INDEX.md` is indexed by the engine | Every test question appears, and indexing is confirmed |
| 43 | `Readme.md`, `INDEX.md` | Move the guide library (section 5) into `INDEX.md` (named exception to rule 2), leave the club docs and a link in `Readme.md` | Readme covers only club docs, and nothing was lost |
| 44 | `INDEX.md` | Add a "Server" column (Global / JP / Both) from the headers | Column filled |
| 45 | `INDEX.md` | Link the Global-to-JP terminology map (in `AdvanceCareerGuide.md`) and the `Glossary` folder | Both links resolve |
| 46 | The 10 largest files | Add a short block: "Answers: ... / Does not cover: ..." | 10 blocks added |
| 47 | Scenario docs | Add "See also" links from each scenario to its support card section and deck advice | Links resolve |
| 48 | `Career/Scenario/README.md` (new) | Comparison table: scenario, stat caps, release, doc link. Confirm from Appendix B that nested `README.md` files are indexed | One row per scenario doc |
| 49 | `Career/ResultEvaluationRefs.md` (new) | Pointer file: where rank and score thresholds live (Part1 tables and the scenario files), for the career evaluator | Every pointer resolves |
| 50 | `_Gaps.md` (new) | List missing coverage, starting with a Beyond Dreams scenario guide | File committed |

### Track 7: Verify and finish

| Phase | Target | Change | Done when |
|-------|--------|--------|-----------|
| 51 | `_SearchTests.md`, Appendix C | Re-run the script from 04a and record the **Final** column next to the Baseline | Both columns filled, and no question that passed at baseline fails now |
| 52 | whole repo | Second audit, same scope as Phase 17 (links plus old filenames and path strings) | Zero broken links and zero old-name references |
| 53 | failures from 51 | One tiny phase per failure (53a, 53b...), fixing only what that question needs | Re-test passes |
| 54 | PR | Open a PR from `docs-optimization` and review the diff for accidental content changes | Diff shows only headers, names, links, pointers, notes and the named exceptions in rule 2 |

---

## 4. Order and dependencies

- **04 and 04b gate everything.** Findings can change or remove phases in Tracks 1, 2 and 4, and the baseline must exist before any rename.
- Track 1 comes before Track 2, so headers are added to final filenames.
- Phase 18 depends on Phase 04 findings (front matter handling, underscore files).
- Phases 33 to 37 must be done in order, with 36a inserted only if Phase 36 gives outcome C.
- Track 6 comes last because `INDEX.md` depends on final names and headers.
- Phase 51 depends on 04b, so the comparison is like for like.

---

## 5. Phase log

| Phase | Status | Commit | Notes |
|-------|--------|--------|-------|
| 01 | done | this commit | Branch `docs-optimization` already existed (head `057c186`, "docs: add Optimization Plan (54 phases)"), so it was reused. `main` was at `f7fb4ec04c6af37d82fc9cf2b5869b121c3b71ef` when checked. This commit replaces the v1 plan with v2 |
| 02 | not started | | |
| 03-54 (plus 04a, 04b, and conditional 18a, 36a) | not started | | Note for Phase 04: this plan file lives inside `Guide/`, so check whether the engine indexes it |

---

## Appendix A: Baseline file list

_To be filled in Phase 02._

## Appendix B: Engine audit findings

_To be filled in Phase 04. Required items: (a) chunking, (b) skipped files and indexed `INDEX.md` / `README.md`, (c) front matter handling, (d) name matching, (e) file-and-line list of path references._

## Appendix C: Search test results

_Baseline filled in Phase 04b, Final filled in Phase 51._

| # | Question | Expected file and section | Baseline | Final |
|---|----------|---------------------------|----------|-------|
| 1-25 | | | | |

---

## Revision notes (v1 to v2)

- Added Phases 04a and 04b (test runner and baseline), and moved the rename gate to 04b.
- Expanded Phase 04 (indexing rules, front matter, path references) and added ground rule 5.
- Made Phases 17 and 52 repo-wide and extended them to old filenames and path strings.
- Added Phase 33 section confirmation, a three-outcome Phase 36, conditional Phase 36a, and a line-coverage gate on Phase 37.
- Made Phases 34 and 35 script-based with an empty-diff check.
- Defined the `expires` field in Phase 18, with Phase 18 decisions based on Phase 04 findings.
- Listed named exceptions to the "verbatim" rule (Phases 30, 36a, 37, 43).
- Required exact roster counts in Phase 40.
- Added a risks table and an optional batching aid (rule 8).
