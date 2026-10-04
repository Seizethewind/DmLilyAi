# Phase Log

Status of every phase in `Optimization Plan.md` (same folder). One row per phase or group of phases. Updated in the same commit as the phase it records, or in the next phase's commit when a result is only known later.

| Phase | Status | Commit | Notes |
|-------|--------|--------|-------|
| 01 | done | `05406d2` | Branch `docs-optimization` already existed (head `057c186`, "docs: add Optimization Plan (54 phases)"), so it was reused. `main` was at `f7fb4ec04c6af37d82fc9cf2b5869b121c3b71ef` when checked, and code search of `main` already shows a copy of the v1 plan under `Guide/`. That commit replaced the v1 plan with v2 |
| 02 | done | `151850c` | Appendix A filled: 40 `.md` files plus 1 `.xlsx`. Sizes are bytes as reported by GitHub on the branch head |
| 03 | done (draft) | `1c94183` | The test set has 25 questions built around training Kitasan Black, each with a form for any trainee. Questions 1 to 4 come from the project owner, 5 to 25 are drafted from guide headings and need owner review |
| 04 | done | `e805496` | Appendix B filled from the engine source and repo-wide searches. Six findings changed the plan (v2.1) |
| 04c | done | `f08f781` plus two delete commits | Added the plan and `SearchTests.md` under `tools/docs_optimization/`, then deleted `Guide/Optimization Plan.md` and `Guide/_SearchTests.md`. A move is an add plus deletes through the GitHub API. Owner also approved engine change 18a (built in Phase 18) |
| 04a | built, first run not yet read | `6c077b9` | Added `tools/run_search_tests.py` and `.github/workflows/search-tests.yml`. The workflow runs on every push to `docs-optimization` that touches the docs, the engine, the runner, the test table or the workflow, so this commit started the first run. It could not be checked from the chat (no access to the Actions page). **To read it:** repo Actions tab, workflow "Search tests", open the latest run, then the job summary (tables) or the `search-test-results` artifact (JSON). The run also reports whether `tests/test_game_space_engine.py` passes |
| 04b | not started | | Record the first run on an untouched docs folder as the **Baseline**. Needs the run result from 04a |
| 05-54 (plus conditional 18a, 36a) | not started | | |

## Search test summary (Appendix C of the plan)

Per-question results are in the run's job summary. Fill this table in Phases 04b and 51. Passed = a top-5 hit is the expected doc and section.

| Run | Phase | Commit | search passed | scoped passed | context passed | Engine tests |
|-----|-------|--------|---------------|---------------|----------------|--------------|
| Baseline | 04b | | _/25 | _/25 | _/25 | |
| Final | 51 | | _/25 | _/25 | _/25 | |
