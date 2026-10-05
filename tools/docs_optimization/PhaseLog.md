# Phase Log

Status of every phase in `Optimization Plan.md` (same folder). One row per phase or group of phases. Updated in the same commit as the phase it records, or in the next phase's commit when a result is only known later.

| Phase | Status | Commit | Notes |
|-------|--------|--------|-------|
| 01 | done | `05406d2` | Branch `docs-optimization` already existed (head `057c186`, "docs: add Optimization Plan (54 phases)"), so it was reused. `main` was at `f7fb4ec04c6af37d82fc9cf2b5869b121c3b71ef` when checked, and code search of `main` already shows a copy of the v1 plan under `Guide/`. That commit replaced the v1 plan with v2 |
| 02 | done | `151850c` | Appendix A filled: 40 `.md` files plus 1 `.xlsx`. Sizes are bytes as reported by GitHub on the branch head |
| 03 | done (draft) | `1c94183` | The test set has 25 questions built around training Kitasan Black, each with a form for any trainee. Questions 1 to 4 come from the project owner, 5 to 25 are drafted from guide headings and need owner review |
| 04 | done (two passes, merged) | `a17b343`, `3352d0f`, `f3c2fb1` (first pass), `e805496` (second pass), `0ead676` (merge) | First pass: engine skips files and folders starting with `_` (plus a test), and a line-numbered audit. Second pass: ranking, front matter and name-matching findings. The second pass replaced the plan file without re-reading it, so the first pass's audit text and log rows were lost from the plan, and it wrongly stated that `_` files were still indexed. `EngineAudit.md` now holds the merged audit with that corrected. Original first-pass text: `git show f3c2fb1` |
| 04c | done | `f08f781` plus two delete commits | Added the plan and `SearchTests.md` under `tools/docs_optimization/`, then deleted `Guide/Optimization Plan.md` and `Guide/_SearchTests.md`. The move was still needed for the plan file (not `_`-prefixed, so it was indexed). `_SearchTests.md` would have been skipped by the engine anyway. Owner also approved engine change 18a (built in Phase 18) |
| 04a | done | `6c077b9` | Added `tools/run_search_tests.py` and `.github/workflows/search-tests.yml`. The first run worked and produced the baseline below. The run's engine-test result was not reported, so it is still unknown whether `tests/test_game_space_engine.py` passes |
| 04b | done | `f270e6d` | Baseline recorded: per-question results in `SearchTests.md`, totals below, and `baseline.json` saved for `--compare`. The baseline was typed in from the run's job summary, with Q1 context counted as `fail` (see `SearchTests.md`) |
| 04d | step 1 done, rest waiting for owner | `8d936ef` (measurement) | Step 1: the runner now reports section sizes. The measurement confirmed the cause (see below). Steps 2 and 3 are engine changes and need owner approval |
| 05-54 (plus conditional 18a, 36a) | not started | | |

## Search test summary (Appendix C of the plan)

Passed = a top-5 hit is the expected doc and section.

| Run | Phase | Commit | search passed | scoped passed | context passed | Engine tests |
|-----|-------|--------|---------------|---------------|----------------|--------------|
| Baseline | 04b | `6c077b9` | 1/25 | 1/25 | 1/25 | not reported |
| Size measurement run | 04d step 1 | `8d936ef` | 1/25 | 1/25 | 1/25 | not reported |
| Final | 51 | | _/25 | _/25 | _/25 | |

Baseline detail: search has 1 pass, 4 file, 1 alt, 19 fail. Scoped is the same. Context has 1 pass, 3 file, 19 fail, 2 none. The measurement run gave the same numbers, as expected (no docs changed).

## Finding (measured): very large sections outrank small, focused ones

The size measurement (run for `8d936ef`) confirms the cause that the baseline suggested:

- **The index:** 3,164 sections, 4,145,232 characters of text. 80 sections are longer than a default read (6,000 characters), and 47 are longer than the maximum read (12,000), so a read cuts them off. The 15 largest sections hold 22% of all text.
- **Expected sections are small:** for the 25 questions the expected sections are 141 to 4,647 characters (Q5 is the affinity chart table, 99,755).
- **The top hits are huge:** for 19 questions the first search hit is a section of 93,716 or 150,828 characters (`Guide2 > Uma Musume Reference` and `Guide2 > Technical Information > Racing vs Training`), or another very large section. That is 20 to 1,000 times larger than the section that holds the answer.
- **Largest sections:** `compatibility_spreadsheet` (217,128, a duplicate of the boxes chart, issue I7), `Guide2 > Racing vs Training` (150,828), `compatibility_chart_boxes` (99,755), `Guide2 > Uma Musume Reference` (93,716), the monolith's Master Tier List (46,251), `Guide2 > Technical Information` (42,495), `Guide1 > How does the tool work` (40,866), `umamusume_affinity_tables > Pair Affinity Matrix` (28,857), `Cm20` (28,190), `Skill/skill > Normal Skills` (27,912), `Guide2 > Daily Legend Race` (27,773), and four monolith tier lists of about 26,800 each. Guide2's four large sections alone hold about 315,000 of its 488,000 characters.
- **Other results:** scoping to the Guide folder changes nothing. In chat, a message that names Kitasan Black injects only her character page. Questions 12, 13 and 15 find the right character page but return its parent section instead of the aptitudes or objectives section.
- **What this means for the plan:** renames (Track 1) and headers (Track 2) will not change these results. Changing them needs engine changes (04d) or splitting the giant sections in the docs.

## Phase 04d: options (owner decision needed)

Step 1 (measurement) is done. Options for the engine change, with the main trade-offs:

- **A. Split large sections into chunks at index time** (for example up to about 3,000 characters, at paragraph or table-row boundaries, kept as sub-sections named `part n of N`). Ranking then compares small pieces with small pieces, and a read of a section can return its parts. It fixes both the ranking and the read cut-off. It is the larger change: roughly 40 lines in the engine, search results should show at most one part per section so siblings do not fill the top 5, the outline must hide the parts, and the engine tests need new cases. Saved guides store doc ids and fingerprints, so check they still resolve.
- **B. Length-normalized scoring** (BM25 style) in the ranking. About 10 lines and low risk. It pushes huge sections down, but it does not make them readable, and an answer that really lives inside a huge section is still hard to retrieve.
- **C. A then B**, if A alone leaves some questions failing.

Recommendation: A. Either way the change is made on this branch, checked by the test run (pass counts must not drop), and reaches production only when the branch is merged.
