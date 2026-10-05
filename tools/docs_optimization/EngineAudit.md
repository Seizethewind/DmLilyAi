# Engine Audit (Appendix B of the plan)

Findings from Phase 04, read from `LilyAiGameSpace/UmamusumeGameSpaceEngine.py` on branch `docs-optimization` (blob `a42e35a`).

**History of this file.** Phase 04 was done twice on this branch. A first pass (commits `a17b343` and `3352d0f` for the engine change and its test, `f3c2fb1` for the notes) added the `_` skip rule and the first version of this audit, with line numbers for the path references. A second pass (`e805496`) added the ranking, front matter and name-matching findings, but it replaced the plan file without re-reading it, so the first pass's audit text and log rows were lost from the plan, and the second pass wrongly said `_` files were still indexed. This file merges both passes and corrects that mistake. The original first-pass text is still in git history at `f3c2fb1`.

## (a) What is indexed, chunking and ranking

- **Indexed set:** every `*.md` under `LilyAiGameSpace/Umamusume/` (Character, Glossary, Guide, Skill, Support Cards, and the top-level `README.md`). Not only `Guide/`.
- **Doc id** is the path inside that folder without `.md` (for example `Guide/Career/CareerStartWorkflow`). **Category** is the top folder.
- **Index timing:** built at startup, and re-scanned at most every 30 seconds, so doc edits need no restart.
- **Chunking:** docs are split at headings `#` to `####`. Headings inside fenced code blocks are ignored. Text before the first heading becomes a section named `Overview`. A section path is its headings below the H1 joined with ` > `. **Nothing splits by size**: a section with no sub-headings is one chunk, however long.
- **Reading:** `read()` returns 6,000 characters by default and 12,000 at most. A whole doc longer than the limit returns only its first section plus an outline of up to 40 sections. A section longer than the limit is cut off.
- **Ranking:** TF-IDF over heading plus text. Words in the heading path add 2 x idf. Words in the doc's name or aliases add 3 x idf to every matching section of that doc. Tokens are lowercased, a trailing "s" is stemmed, and stopwords are dropped. **Section length is not normalized.**
- **Search:** returns 5 hits by default (10 at most). `category` limits it to a top folder.
- **Hidden or unsearched:** the `Images` section is hidden everywhere. The `Sources` section is readable but not searched.
- **Size limits:** files over 2,000,000 bytes are skipped. No current file is that large (the largest, `Support Cards/SSR-Details.md`, is about 601 KB). The sandbox table tool refuses more than 400,000 characters of text, so the monolith, Guide2, Guide3 and `compatibility_spreadsheet.md` only work there when a section is named.

## (b) Skipped and indexed files

- **Current rule:** a file is skipped if any part of its path starts with `.` or `_`, or if it is over 2 MB. The `_` part was added in commits `a17b343` and `3352d0f` (with a test). Before that, only `.` was skipped.
- No existing doc under `Umamusume/` starts with `_` or `.`, so the rule hides no current doc.
- Consequence for this plan: `_SearchTests.md`, `_Gaps.md` and `_DocHeaderSchema.md` would stay out of the index even inside `Guide/`. The plan file, `Optimization Plan.md`, does not start with `_`, so the engine indexed it. Phase 04c moved the plan and the test set to `tools/docs_optimization/`, outside the indexed folder.
- `INDEX.md` and nested `README.md` files are indexed like any other `.md` file. Every `README.md` also gets its parent folder name as an alias, and all of them share the alias `readme`. A lookup of `readme` returns the first by id order, which is `Guide/Readme`.
- Non-markdown files (the `.xlsx`) are not indexed.

## (c) Front matter

- A header is read only if the file starts with `---` at the very first character and has a closing `---`. A leading blank line or a byte-order mark turns the header into body text.
- The header is removed from the body, so it is **not** chunked as text.
- Lines are plain `key: value`, one per line. Multi-line YAML does not parse. Lists work only inline (`[a, b]` or a comma-separated line).
- **Only `title` (overrides the first H1) and `aliases` are used.** `source`, `author`, `server`, `written`, `last_verified`, `status`, `topics` and `expires` are read and discarded, so they are invisible to search and reads.
- Aliases boost the doc's rank for any matching word, so generic words in `aliases` would skew results.
- Input for Phase 18: the full schema is tolerated, but `server`, `status`, `expires` and `topics` are for human readers only unless the engine is changed (the approved change 18a).

## (d) Name matching

- **Aliases:** the title (front matter `title`, else the first H1), the file name with `_` and `-` turned into spaces, the same name split at CamelCase, the parent folder name for README files, front matter `aliases`, and the Japanese name for characters.
- **Lookup** ignores case, spaces, underscores and punctuation. `resolve()` tries: exact alias, then the longest alias contained in the query (4 letters or more), then a unique substring match, then fuzzy matching at 0.8.
- **Automatic chat context (`context_for`)** fires when a message contains a multi-word alias, or a single-word alias of 5 letters or more that is not in the engine's generic list (readme, overview, guide, guides, skill, skills, character, characters, support, card, cards, race, races, training, glossary, list). "index" is not in that list, so a file named `INDEX.md` would be injected whenever a message contains the word "index". Hence `GuideIndex.md`.
- **Renames** change the doc id and drop the old file-name alias (for example `Guide1`), unless the old name is kept in front matter `aliases`. Titles come from the H1 and do not change. The leading space in ` Legacy.md` does not break lookup but is part of the id.
- **Saved guides** (table `guide_cache`) store doc ids and a content fingerprint. After a rename or split they are still served but flagged as stale.
- **Character boost:** a query that names a character (for example "Kitasan Black") boosts every matching section of that character's page, and in chat only that page is injected automatically.

## (e) References to `Guide/` paths and old filenames

Checked so far (line numbers from the branch head at the first pass):

| File | Line | What it says | Kind |
|------|------|--------------|------|
| `.github/workflows/racelist.yml` | 41 | `git add LilyAiGameSpace/Umamusume/Guide/RaceList/Racelist.md` | Runtime path (`Racelist.md` is not renamed in this plan) |
| `.github/scripts/scrape_racelist.py` | 4, 29 | Output path `LilyAiGameSpace/Umamusume/Guide/RaceList/Racelist.md` (line 29 is the runtime `OUT` path). The script rewrites the whole file | Runtime path (not renamed). A hand-added header would be overwritten, so Phase 27a changes the script instead |
| `.github/scripts/scrape_racelist.py` | 8, 15 | File name `Racelist.md` in the docstring | Comment |
| `LilyAiGameSpace/sandbox_scripts/game_calcs.py` | 7, 11 to 13 | Docstring names `Guide/Uma Musume Legacies/Legacy.md`, `PvpTeamTrials.md`, `RaceMechanicHandBook.md`; two section comments repeat `Legacy.md` and `PvpTeamTrials.md` | Comment only. The calculators hold their rules in code and read no doc files at run time. The docstring already uses the post-Phase-05 name `Legacy.md` |
| `LilyAiGameSpace/CareerEvaluator.py` | 2 to 3 | Cites `AdvanceCareerGuide/Part2_StatsAndRaceMechanics.md` and `Skill/skill.md` | Comment only (Part 2 is not renamed in this plan) |
| `tests/test_game_space_engine.py` | `setUp` and the search tests | Fixture `Guide/RaceList/Racelist` in a temp folder | Synthetic fixture, does not read the real files |
| `tests/test_sandbox_table_ops.py` | comment | Cites `Legacy.md` | Comment only |
| `LilyAiGameSpace/Umamusume/README.md` | | Describes `Guide/` and names "CommunityGuide (Guide1 to Guide9...)" | Doc that names old files. Update in Phase 17 |
| `Guide/Readme.md` | | Links such as `CommunityGuide/Guide2.md` | Doc that names old files. Updated by the rename phases and Phase 17 |

Repo-wide code searches for `Legacy.md`, `PvpTeamTrials`, `RaceMechanicHandBook`, `CommunityGuide`, `Cm20`, `Guide1` to `Guide9`, `compatibility_chart`, `umamusume_affinity_tables` and `compatibility_spreadsheet` found nothing else in code, tests or workflows. (GitHub code search covers `main` only and skips files over about 384 KB, so each rename phase repeats the search on the branch.)

Checked with no `Guide/` references: `UmamusumeCatalog.py`, `UmamusumeSkills.py`, `affinity_data.py`, `sandbox_runner.py`, `docs_table_ops.py`, `guide_builder.py`, `LilyAiTool/GameSpaceTools/game_space_tools.py` and `sandbox_tools.py`, `LilyAiRag/service.py`, `LilyAiMain/MainService/bootstrap.py`, `tests/test_guide_builder.py`, `render.yaml`, `.dockerignore`, root `README.md`, `.github/workflows/fetch-wiki-sources.yml`, and the workflows for characters and support cards (they write only to `Umamusume/Character` and `Umamusume/Support Cards`).

Not yet checked file by file (covered by each rename phase's repo-wide search, and by Phase 17 and 52): `tools/*.py`, `.github/scripts/populate_character_stubs.py`, the other workflows, `LilyAiContext`, `LilyAiMain` Discord, Interaction and Api folders, `LilyAiFrontend`, `LilyAiWeb`, `LilyAiLearning`, `LilyAiMemory`, `LilyAiCore`, `LilyAiDocs`, `debug/`, `sources/`, `Dockerfile`, `.env.example`, and the remaining tests.

Other findings for later phases:

- `affinity_data/` is at `LilyAiGameSpace/affinity_data/`. From the Affinity files the relative link for Phase 41 is `../../../affinity_data/`.
- `affinity_data.py` states that its data covers 74 characters on Global (v1.35.2), which fits issue I7.
- `game_docs_list` shows up to 200 docs per category, and all guide docs share the category `Guide`, so adding files under `Guide/` needs no code change.

## (f) What the baseline showed

The first search-test run (Phase 04b) is summarized in `PhaseLog.md`. In short: most failures come from very large sections outranking small, focused ones, which follows from the two points in (a) in bold (no size split, no length normalization).
