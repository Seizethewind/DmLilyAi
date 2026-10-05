# Phase Log

Status of every phase in `Optimization Plan.md` (same folder). One row per phase or group of phases. Updated in the same commit as the phase it records, or in the next phase's commit when a result is only known later.

| Phase | Status | Commit | Notes |
|-------|--------|--------|-------|
| 01 | done | `05406d2` | Branch `docs-optimization` already existed (head `057c186`, "docs: add Optimization Plan (54 phases)"), so it was reused. `main` was at `f7fb4ec04c6af37d82fc9cf2b5869b121c3b71ef` when checked, and code search of `main` already shows a copy of the v1 plan under `Guide/`. That commit replaced the v1 plan with v2 |
| 02 | done | `151850c` | Appendix A filled: 40 `.md` files plus 1 `.xlsx`. Sizes are bytes as reported by GitHub on the branch head |
| 03 | done (draft) | `1c94183` | The test set has 25 questions built around training Kitasan Black, each with a form for any trainee. Questions 1 to 4 come from the project owner, 5 to 25 are drafted from guide headings and need owner review |
| 04 | done (two passes, merged) | `a17b343`, `3352d0f`, `f3c2fb1` (first pass), `e805496` (second pass), merge in this commit | First pass: engine skips files and folders starting with `_` (plus a test), and a line-numbered audit. Second pass: ranking, front matter and name-matching findings. The second pass replaced the plan file without re-reading it, so the first pass's audit text and log rows were lost from the plan, and it wrongly stated that `_` files were still indexed. `EngineAudit.md` now holds the merged audit with that corrected. Original first-pass text: `git show f3c2fb1` |
| 04c | done | `f08f781` plus two delete commits | Added the plan and `SearchTests.md` under `tools/docs_optimization/`, then deleted `Guide/Optimization Plan.md` and `Guide/_SearchTests.md`. The move was still needed for the plan file (not `_`-prefixed, so it was indexed). `_SearchTests.md` would have been skipped by the engine anyway. Owner also approved engine change 18a (built in Phase 18) |
| 04a | done | `6c077b9` | Added `tools/run_search_tests.py` and `.github/workflows/search-tests.yml`. The first run worked and produced the baseline below. The run's engine-test result was not reported, so it is still unknown whether `tests/test_game_space_engine.py` passes |
| 04b | done | `f270e6d` | Baseline recorded: per-question results in `SearchTests.md`, totals below, and `baseline.json` saved for `--compare`. The baseline was typed in from the run's job summary, with Q1 context counted as `fail` (see `SearchTests.md`) |
| 04d | proposed, waiting for owner | | Engine ranking fix. See the finding below. Step 1 (measure section sizes in the runner output, no engine change) is allowed without a decision |
| 05-54 (plus conditional 18a, 36a) | not started | | |

## Search test summary (Appendix C of the plan)

Passed = a top-5 hit is the expected doc and section.

| Run | Phase | Commit | search passed | scoped passed | context passed | Engine tests |
|-----|-------|--------|---------------|---------------|----------------|--------------|
| Baseline | 04b | `6c077b9` | 1/25 | 1/25 | 1/25 | not reported |
| Final | 51 | | _/25 | _/25 | _/25 | |

Baseline detail: search has 1 pass, 4 file, 1 alt, 19 fail. Scoped is the same. Context has 1 pass, 3 file, 19 fail, 2 none (after the Q1 correction).

## Baseline finding: ranking, not the documents, causes most failures

- In 19 of 25 questions the top hits are the same few sections of the community guides, mostly `Guide/CommunityGuide/Guide2 > Technical Information > Racing vs Training` and `Guide2 > Uma Musume Reference`, plus `Guide1 > How does the tool work`. They come back for unrelated questions (summer camp, deck slots, fans) and push the right sections out of the top 5.
- The most likely cause is the engine's ranking (`EngineAudit.md` (a): nothing splits sections by size, and section length is not normalized). Very large sections contain every query word many times, so they score higher than small, focused sections such as `CareerStartWorkflow > Step 4`. This is a cause inferred from the engine code and these results, not yet measured. Step 1 of Phase 04d adds section sizes to the runner output to confirm it.
- Scoping the search to the Guide folder changes nothing, so the character page boost is not the main problem for these questions.
- In chat, a message that names Kitasan Black injects only her character page (`context` mode), so guide answers reach the model only if it calls the search tool.
- Questions 12, 13 and 15 find the right character page but return its parent section (`Game data: versions`) instead of `Shared aptitudes` or `Shared career objectives`.
- Renames (Track 1) and headers (Track 2) will not change these results, because they do not change section sizes or ranking. Only splitting large files and engine changes can.

**Proposed Phase 04d (owner decision needed):** change the engine so that section length does not dominate. Two options, which can be combined: (1) length-normalized scoring (BM25 style) in `_rank`, and (2) splitting very large sections into smaller chunks at index time, which also fixes `read()` cutting off long sections at 12,000 characters. Either needs engine tests. Track 4 would then target the largest sections (Guide2, Guide3, Guide1, the encyclopedia, the monolith), not only `AdvanceGameplayGuide.md`.
