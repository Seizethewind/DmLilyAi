# Umamusume Guide

This folder holds two things: the documentation for how **LilyAi** supports the Umamusume clubs **Umakraft** and **Umakraft 2** (linking your account, the fan quota, the daily DM report, and the Leaderboard), and a library of Umamusume game guides that LilyAi can draw on. Club data comes from the [uma.moe](https://uma.moe) API.

**Contents**

1. [Link your account](#1-link-your-account)
2. [Fan quota](#2-fan-quota)
3. [Daily DM report](#3-daily-dm-report)
4. [Leaderboard](#4-leaderboard)
5. [Guide library](#5-guide-library)
6. [Where this lives in the codebase](#6-where-this-lives-in-the-codebase)
7. [Troubleshooting](#troubleshooting)

---

## 1. Link your account

LilyAi needs to know which Discord user is which uma.moe trainer. Linking is done entirely in DMs, with no slash commands and no Discord modals.

| DM phrase | What it does |
|-----------|--------------|
| `link me` | Starts the link flow. LilyAi asks for your uma.moe **Trainer ID**. |
| `unlink me` | Removes your link. |

Only members linked by **both** Discord ID and uma.moe Trainer ID receive the daily quota DM.

---

## 2. Fan quota

| Quota | Amount |
|-------|--------|
| Monthly | 150,000,000 fans (fixed, regardless of days in the month) |
| Daily | 5,000,000 fans (5m x 30 = 150m) |

The quota carries over from day to day, so the month always totals 150m:

- **Deficit:** a day's shortfall is added to the next day's required amount and keeps stacking until it is paid off.
- **Surplus:** a day's surplus reduces the next day's requirement.

---

## 3. Daily DM report

Once per day, LilyAi sends each linked member one DM stating whether that day was:

- **Met**
- **Deficit**
- **Surplus**

---

## 4. Leaderboard

The Leaderboard shows daily gain and monthly gain per trainee in a table.

- **Club tabs:** one tab for Umakraft and one for Umakraft 2.
- **Paging:** 10 trainees per page, up to 3 pages (30-player roster cap per club). The page fits the screen without scrolling down.
- **Former Member tab:** 10 per page with no page cap. Shows each former member's total fan contribution and when they were last detected on uma.moe.

---

## 5. Guide library

Every document below lives in a subfolder of this directory. Each entry gives the file, then what it contains and who it is useful for. Many files are large community or wiki references, so a few are best searched rather than read top to bottom.

### 5.1 Getting started

#### [Umamusume Global Quickstart Guide/Readme.md](Umamusume%20Global%20Quickstart%20Guide/Readme.md)

A summary and link index written for this repository rather than a copy of the original. It records the source URL, the author (Gertas) and creation date (2025-06-26), with a copyright note. It lists key facts an agent needs: supported platforms, the two gacha pools, six supports per run, saved builds, rerolling advice, clubs, and the Global server's lag behind Japan. A table indexes useful URLs for stores, guides, lists and tools, which makes it the quickest orientation page.

#### [Umamusume Global Quickstart Guide/UmamusumeGlobalQuickstartGuide.md](Umamusume%20Global%20Quickstart%20Guide/UmamusumeGlobalQuickstartGuide.md)

A short eleven-step onboarding path for brand-new Global-server players, written by Gertas. It covers whether the game suits you, downloading it, and how characters and support cards work, including the roguelite idea of saving builds. Later steps cover rerolling, the tutorial, the FAQ, joining a club, character and support lists, upcoming Japan-server banners, and tools such as the Training Event Helper and Compatibility Calculator. It has links but no data tables.

#### [Umamusume New Player FAQ/UmamusumeNewPlayerFAQ.md](Umamusume%20New%20Player%20FAQ/UmamusumeNewPlayerFAQ.md)

A question-and-answer guide for new Global players from GameTora, last updated 2025-06-28. It explains rerolling for support cards, lists strong early supports (Kitasan Black, Fine Motion, Super Creek, Biko Pegasus, Tazuna) and good character picks (Oguri Cap, Maruzensky, Taiki Shuttle), and gives Career priorities such as friendship gauges and rainbow training. Two tables list recommended Stamina by distance for Career and PvP, adjusted for recovery skills and running strategy.

#### [Uma Musume Guide For Absolute Beginners/BeginnerGuide.md](Uma%20Musume%20Guide%20For%20Absolute%20Beginners/BeginnerGuide.md)

A GameTora introduction for complete newcomers, written when only the Japanese server existed. It explains the gacha and the forgiving stamina system, then walks through Career mode step by step: starting a run, turns, stat training, support cards, skills, outings, races, goals and events. It closes with Daily Races, Legend Races and Team Trials PvP. There are no data tables, which makes it a gentle read for players who just want to understand the core gameplay loop.

### 5.2 Career mode and scenarios

#### [Career/CareerStartWorkflow.md](Career/CareerStartWorkflow.md)

An interview-style playbook that LilyAi follows to plan a new career, using Ura Finale as the worked example. It asks one question at a time and keeps a single-line state covering scenario, trainee, target, inheritance and deck. The steps run through scenario, trainee, target, inheritance, support cards and result review. It explains spark priority (white, pink, blue, unique), the Unique Skill Gate, position competition, and how an Ideal Deck differs from a Budget Deck. It is both a build-planning aid and the conversation logic for LilyAi.

#### [Career/Scenario/UraFinale.md](Career/Scenario/UraFinale.md)

A wiki-style reference page for the first scenario, "The Beginning: URA Finale". It covers release dates, the story with Director Akikawa and Aoi Kiryuin, and the 1400 stat ceiling. It describes the Happy Meek duels with probability indicators and defeat rewards, plus the three-race URA Finale (Qualifier, Semifinal, Finals). It lists the fan requirements to level up the unique skill, fixed and multiple-choice scenario events, and the exclusive Racing Spirit skills and sparks, ending with scenario record awards.

#### [Career/Scenario/UnityCup.md](Career/Scenario/UnityCup.md)

A turn-by-turn uma.guide walkthrough of the Unity Cup scenario, split into Junior, Classic and Senior Year. It teaches a point-based turn scoring method for choosing trainings, with separate tables for early, mid and late game. It covers Recreation and mood timing, Energy management, secret events, the Race Agenda, Spirit Burst timing, 15 to 22 optional races for Skill Points, Summer Training prep, New Year energy events and Senior stat targets. It assumes a deck of two Speed and three Wit cards with Riko, and suits intermediate players.

#### [Career/Scenario/UraFinaleVer2UnityCupVer2Updated.md](Career/Scenario/UraFinaleVer2UnityCupVer2Updated.md)

An uma.guide summary of the July 1 patch changes to URA Finale and Unity Cup. For URA Finale it covers the new 1400 stat caps, higher training gains, interactive Happy Meek contests with five levels and reward tables, cheap Racing Spirit skills, and Director Akikawa's summer Energy event. For Unity Cup it covers new caps (1300, Wit 1800), new gains, Spirit Burst hint changes, Extreme Spirit Bursts, Alarm Clocks, Team Rank S+ and the Elite Team. It helps players update older strategies.

#### [Career/Scenario/GrandLive.md](Career/Scenario/GrandLive.md)

An uma.guide article on the fourth scenario, Grand Concert (Grand Live). It gives the stat caps (Speed 1600, Stamina 1300, Power 1300, Guts 1500, Wit 1300) with halving above 1200, facility training gains and inheritance uncaps. It covers deck advice built around Light Hello and the five Performance Point types, with the point formula. It lists Techniques and Songs with costs and priorities, the five Concerts and their timing, Song Saving, and junior-year strategy. It suits players optimizing lessons and concerts.

#### [Career/Scenario/Trackblazer.md](Career/Scenario/Trackblazer.md)

An uma.guide guide to the Trackblazer (Make A New Track) scenario. It covers Speed and Wit and Wit and Guts deck frameworks, race-heavy careers of 30 to 40 races, and Grade Point objectives with Shop Coin rewards. It includes large Race Bonus and Hammer stat tables, epithet routes (Tiara, Classic, Dirt and others), Rival Races, Coin Shop item values and the Race Fatigue odds table. It also covers Summer planning, Twinkle Star Climax scoring and Unique level requirements, which helps with schedules and shop purchases.

#### [Career/Scenario/Grandmaster_Scenario.md](Career/Scenario/Grandmaster_Scenario.md)

A master guide to the Grand Masters scenario by celery#6305, written for training strong Champions Meeting umas, with stat caps given. It explains knowledge fragments, crystals and the three goddess wisdoms, with tables of level bonuses and special-race effects. It then lays out an ideal run for junior, classic and senior years, wisdom timing and turn-planning leeway, fragment stat considerations and scenario skills. A deck section recommends three goddess cards plus two speed, two int and one flexible card, with inheritance by distance.

#### [Career/Scenario/Project_Larc.md](Career/Scenario/Project_Larc.md)

A master guide to the Project L'Arc scenario by celery#6305, with dated update notes from August to September 2023 and stat caps listed. It explains star gauges, SS and SSS matches, supporter points, the two L'Arc races and four preliminary VR races, and overseas aptitude with its tasks and unlock-node tables. It lists scenario-linked characters and their gold skills, then begins gameplay strategy, though the guide ends mid-section.

#### [Career/Scenario/U.A.F.md](Career/Scenario/U.A.F.md)

A master guide to the U.A.F. Ready Go! scenario by celery#6305, aimed at monthly PvP training, with stat caps and 2024 update notes. It explains competition training, genre links, heat-up effects, consultation and tournaments, with tables of level thresholds, bonuses per win and tournament timing. It lists scenario-linked characters, a competition-level gain formula, scenario gold skills and pink evolutions, then gameplay strategy and consultation usage by colour pattern, ending mid-section.

#### [Career/Scenario/Run!Mecha.md](Career/Scenario/Run!Mecha.md)

A master guide to the Run! Mecha Umamusume scenario by celery6305 for mid and long PvP builds, with stat caps and October 2024 update notes. It covers research levels, the overdrive gauge, upgrade events, and the Sati core and chip tuning tables, plus URA finals Super Overdrive. It also lists scenario-linked characters, scenario gold skills and evolutions, recommended tuning for each upgrade event, deckbuilding, a friend ID for borrowing Air Shakur, and an example Mayano run.

#### [Career/Scenario/GreatFoodFestival.md](Career/Scenario/GreatFoodFestival.md)

A master guide to the Harvesting! Feasting! Great Food Festival scenario by celery6305, aimed at short and mile PvP builds, with stat caps and 2024 update notes. It explains vegetable harvesting, field points, vegetable level tables and the Akikawa Yayoi link bonus. It covers cooking, cooking-point bonus breakpoints, tasting party requirements and dish lists with costs and effects, then scenario-linked characters and gold skills, ending mid-section.

### 5.3 Advanced career, gameplay and community guides

#### [AdvanceCareerGuide/AdvanceCareerGuide.md](AdvanceCareerGuide/AdvanceCareerGuide.md)

The master index of a six-part unified reference, merged from seven community sources covering both Japanese and Global servers. It lists the part files, the source tags S1 to S7 and a Global-to-JP terminology map. It gives a nine-point consensus summary, suggested reading orders for new, competitive, parent-farming and fan-farming players, and a 28-row conflict register of disagreements between sources. It also notes coverage gaps and how quickly the meta drifts, so start here before the individual parts.

#### [AdvanceCareerGuide/Part1_CareerTraining.md](AdvanceCareerGuide/Part1_CareerTraining.md)

Part 1 of the unified reference, covering how to play a training run. It explains bond and rainbow training, the training-gain formula and specialty rate, mood and status effects, failure outcomes, summer camp, New Year and other seasonal events with odds, fan checkpoints and race rewards. It also covers auto-kun and background auto, run scoring with stat-to-points and rank threshold tables, a detailed URA fan-farming guide with decks and race routes, rerolling, and a first-month checklist.

#### [AdvanceCareerGuide/Part2_StatsAndRaceMechanics.md](AdvanceCareerGuide/Part2_StatsAndRaceMechanics.md)

Part 2 is a technical reference on the race engine. It covers stat caps and adjusted stats, aptitude modifier tables, what each stat does, and the Stamina, Guts and Wit formulas. It includes required-Stamina and recovery-consistency tables and Stamina-versus-Speed tests, then the speed model, phases and strategy coefficients. It also explains skill activation and scaling, lanes and blocking, Rushed, Spot Struggle, Dueling, Conserve Power, Stamina Limit Break, Zenkai Spurt and the Wiz Limit Break multiplier table. It suits competitive theorycrafters.

#### [AdvanceCareerGuide/Part3_SupportCards.md](AdvanceCareerGuide/Part3_SupportCards.md)

Part 3 explains support card passives (friendship, training, motivation, race and fan bonuses, specialty, hints) and Race Bonus breakpoints such as 34 percent. It describes how the celery6305 evaluation scores cards and gives investment order and limit-break advice. It has write-ups for Speed, Stamina, Power, Guts and Wisdom cards, welfare selector choices, pick tickets, the training-pass shop and Club medal priorities. A table lists mandatory scenario friend and group cards and fan-bonus cards for URA, useful for rerolls, pulls and deck building.

#### [AdvanceCareerGuide/Part4_InheritanceAndParenting.md](AdvanceCareerGuide/Part4_InheritanceAndParenting.md)

Part 4 covers inheritance sparks (blue, red, green, white, race and scenario genes) and what each does at the start of a run and in mid-run inheritance. It explains compatibility under both the current G1-based system and the legacy system, with proc-rate tables and formulas. It describes how each spark type is generated, with star-odds tables by uma grade and by stat, plus parent-building and rental advice, Uma Plan and bulk inheritance, and a table rating parent-farming scenarios. It is aimed at parent farmers.

#### [AdvanceCareerGuide/Part5_SkillsAndPvP.md](AdvanceCareerGuide/Part5_SkillsAndPvP.md)

Part 5 explains skill colours and types, activation conditions, inherited unique penalties, and worked acceleration and speed skill distance math. It covers track analysis with spurt-start tables for G1 courses and Umalator workflows. It gives strategy builds for Front Runner, Pace Chaser, Late Surger, End Closer and debuffers, plus team composition. It also covers the Team Trials (Stadium) format and race-frequency statistics, Champions Meeting, League of Heroes ticket optimization and popularity, making it a core reference for competitive PvP players.

#### [AdvanceCareerGuide/Part6_AccountGachaEvents.md](AdvanceCareerGuide/Part6_AccountGachaEvents.md)

Part 6 covers account management and resources. It lists gacha rates, the 200-pull spark and an expected-result table by pull count. It details every currency and its income sources (jewels, pink tickets, Friend Points, Trainer Medals, clovers, horseshoes, statues, hint books), yearly pull planning and the monthly training pass. It also covers Circles, Legend Races, Trainer Exchange, story-event roulette and other JP events, ending with collection, new-player and Global-versus-JP notes. It is the go-to document for resource planning.

#### [AdvanceCareerGuide/SupportCardEncyclopedia.md](AdvanceCareerGuide/SupportCardEncyclopedia.md)

A Markdown conversion of Luh's support card spreadsheet, updated 29/06/26, with card art omitted. It opens with reading notes and a guide to what makes a card good, including a worked Kitasan Black limit-break breakdown. Per-scenario tables from URA through Beyond Dreams list rarity, release date, type, style, limit-break breakpoints, bonuses, hints, a pull verdict and notes. It closes with links to tools and guides and a changelog. It is very large, so search it by card name for Global pull decisions and deck building.

#### [AdvanceGameplayGuide/AdvanceGameplayGuide.md](AdvanceGameplayGuide/AdvanceGameplayGuide.md)

A very large text-only merge of three community spreadsheets, kept as Markdown tables. Section 1 is the Skills Reference, with a rank legend, glossary, category tables (speed, acceleration, stamina recovery, orange, debuff, green) and tier lists by running style and distance. Section 2 covers spark procs and lineage planning with affinity and a calculator guide. Section 3 is Luh's Support Card Encyclopedia with 13 scenario card tables. It ends with a workflow, credits and omissions, and helps players optimizing skills, inheritance and card choices.

#### [CommunityGuide/CommunityGuide_AI_updated.md](CommunityGuide/CommunityGuide_AI_updated.md)

The working AI knowledge base, distilled from four community guides (tagged G1 to G4: support-card evaluation, a broad gameplay reference, race mechanics, and Champions Meeting strategy). It is organised into numbered sections 00 to 22 covering terminology, training, stats, energy, motivation, inheritance, aptitudes, support cards, skills, racing, speed, lanes, overtaking, tracks, scenarios, strategy, run evaluation, decision rules, exceptions, verification and maintenance. Every entry carries a status tag (FACT, VALUE, FORMULA, CONDITION, RELATION, EVALUATION, STRATEGY, META or UNVERIFIED) so rankings and meta advice are not mistaken for mechanics, and reverse-engineered items keep that label. It includes aptitude, strategy and ground modifier tables. It is only partly populated, and sections still awaiting extraction (compatibility, lane rules, overtake targets) say so. The original Guides 1 to 4 are no longer in this folder; `CommunityGuide/_sources/README.md` records where to find them in git history.

#### [CommunityGuide/CommunityGuide_AI_Guide1_Details.md](CommunityGuide/CommunityGuide_AI_Guide1_Details.md)

An extension module for the AI knowledge base covering Guide 1, celery6305's support-card evaluation doc for the JP meta. It explains the value model (main training, cross-training, race and event contribution), the six-phase training simulation, the bonus priority order, the fixed five-card comparison deck, why Group and Friend cards are left out, and rules for extracting card data without treating rankings as facts. It then lists card-by-card properties for Speed cards and part of the Stamina cards. The file is incomplete: it stops partway through the Stamina cards, so the Power, Guts, Wisdom, non-MLB and Group/Friend entries are missing. Rankings here are evaluations tied to the JP meta, not universal facts.

#### [CommunityGuide/CommunityGuide_AI_Reference_G2.md](CommunityGuide/CommunityGuide_AI_Reference_G2.md)

The reference module for Guide 2, the broad Uma Musume Reference. It covers terminology, early training and bond, motivation, racing versus training, failure risk, the stat formulas (Speed, Stamina, Power, Guts, Wisdom), HP calculation, support card and friend card passives, Race Bonus breakpoints, the training gain formula and skill conditions. Its recommendations stay tied to the scenario they came from. The file is incomplete: it is cut off partway through its section 24.

#### [CommunityGuide/CommunityGuide_AI_Reference_G3.md](CommunityGuide/CommunityGuide_AI_Reference_G3.md)

The reference module for Guide 3, the race mechanics document by KuromiAK. It covers the race structure (sections and phases), stat processing, the speed system, acceleration, stamina and HP, skill activation and scaling, lanes, overtaking, blocking, positioning modes and the special race states. It ends with diagnostic steps for working out why an uma lost. Much of the source is reverse-engineered, so entries keep their confidence labels (CONFIRMED, REVERSE_ENGINEERED, INFERRED, SERVER_DEPENDENT). It suits advanced players and simulator work.

#### [CommunityGuide/CommunityGuide_AI_Reference_G4.md](CommunityGuide/CommunityGuide_AI_Reference_G4.md)

The reference module for Guide 4, pecan's Champions Meeting and League of Heroes guides. It covers how spurt position, final corners, final straights and hills change skill value, stat thresholds, positioning, inherited acceleration choices, skill budgets, Oonige competition, League of Heroes versus Champions Meeting formats and debuffers. It ends with profiles of historical tracks (Kyoto 1600 and 3200, Chukyo 1800 dirt, Niigata 1000, Tokyo 2400, Nakayama 2500, Longchamp 2400). Each recommendation applies only to the event and course conditions it was written for. The file is incomplete: it is cut off in the Longchamp 2400 profile.

### 5.4 Inheritance and affinity

#### [Uma Musume Legacies/ Legacy.md](Uma%20Musume%20Legacies/%20Legacy.md)

A detailed guide to the Legacy (inheritance) system. The basics cover legacies, sub-legacies, initial bonuses, inspiration events and compatibility symbols. The Sparks section covers blue, pink, green and white sparks, with tables of Japanese and English names, star-roll odds by stat, and stat bonuses (+5, +12, +21). Advanced topics include "9-star" goals, guest legacies, spark farming, double-circle compatibility and the outdated legacy loop. It suits players optimizing builds beyond the early game. Note the filename starts with a space.

#### [Affinity/umamusume_affinity_tables.md](Affinity/umamusume_affinity_tables.md)

Base pair and trio affinity data for 74 Global-roster characters, taken from uma.moe's affinity.json (game version 1.35.2). It provides a formula for a build's total affinity and community tier thresholds. Sections include a character ID list, a full 74-by-74 pair matrix, each character's top ten partners in per-character tables, and the 100 highest-affinity trios. G1 race-win bonuses are excluded. It is useful for planning legacy parents and sub-legacies.

#### [Affinity/compatibility_chart_boxes.md](Affinity/compatibility_chart_boxes.md)

A single very wide Markdown table of the mee1080.github.io "2nd Generation Compatibility Chart". It has 135 character rows and 135 columns with the same names across the top and down the left. Each cell holds the pairwise affinity value, the diagonal is 0, and extra columns give each row's total and a short note such as aptitude tags. It is useful for finding the best second-generation pairings, though it needs horizontal scrolling.

#### [Affinity/compatibility_spreadsheet.md](Affinity/compatibility_spreadsheet.md)

The same mee1080.github.io compatibility data as the boxes file, drawn as one monospace box-drawing grid inside a code fence so it looks like a spreadsheet. Names run down the left, column headers sit in vertical letters across the top, each cell is a padded two-digit value, the diagonal is 0, and trailing columns give the row total and a short note. It covers roughly 135 characters and is useful for scanning affinity, but needs wide scrolling.

#### [Affinity/compatibility_chart.xlsx](Affinity/compatibility_chart.xlsx)

A binary Excel workbook with a single worksheet. Judging from the sibling files, it appears to be the original spreadsheet form of the 2nd Generation Compatibility Chart: a roughly 135-by-135 character matrix of pairwise affinity values with a zero diagonal, a row-total column and a notes column. Open it in Excel or Google Sheets to sort, filter or look up pairings, since it cannot be read as plain text in the repository.

### 5.5 Races, Champions Meeting and PvP

#### [RaceList/Race.md](RaceList/Race.md)

A career-mode race calendar in calendar order, grouped into Junior, Classic and Senior Year tables. Within each period, races run from higher to lower grade (G1 to Pre-OP). Each row lists the period, race name, grade, required fans, first-place fan reward and race conditions (course, distance category, ground, weather, turn direction). Notes say the fan data comes from Korean-server NamuWiki data, so Global values may differ, and that JBC races vary by venue. It is useful for planning optional races, fan goals and secret-event routes.

#### [RaceList/Racelist.md](RaceList/Racelist.md)

A GameTora-sourced race calendar with Junior, Classic and Senior Year tables, one row per half-month period (Early and Late, January to December). Each cell lists the races available with surface, distance, category (Short, Mile, Medium, Long) and venue. Junior Year has no races before Late June, then runs from Make Debut through the G1s. Unlike Race.md it carries no fan requirements or rewards, so it works as a compact schedule and name reference for planning by period, surface and distance.

#### [Race Mechanics Handbook/RaceMechanicHandBook.md](Race%20Mechanics%20Handbook/RaceMechanicHandBook.md)

A GameTora handbook for beginner-to-intermediate readers explaining core race mechanics. It covers the five stats (including halving above 1200 and mood effects), the four race phases with worked distance tables, terrain and condition penalties, and horse lengths. It explains Target versus Current Speed, acceleration, start delay and late starts, and the last spurt. It also covers Position Keep modes, Rushing, Spot Struggle, Dueling, Stamina Contest, Repositioning, Securing the Lead, corner numbering and gate brackets. It is useful for understanding skills and builds.

#### [Champions Meeting/ChampionMeeting.md](Champions%20Meeting/ChampionMeeting.md)

A GameTora overview of the Champions Meeting (CM) tournament system. It explains choosing between Open League and Graded League (Open is limited to rank B or lower and gives fewer rewards) and the three-round structure. It covers Round 1 and Round 2 groups and win thresholds, four attempts per day of five races each and the entry ticket system. It also covers the single-race Finals, three-girl teams in nine-runner races and the Group A and B advancement rules. It suits newcomers learning the format.

#### [Champions Meeting/Cm20.md](Champions%20Meeting/Cm20.md)

A Game8 Champions Meeting guide, saved with heavy site-navigation boilerplate. It covers the Sagittarius Cup CM20 (Oct 7 to 16, 2026, Long, Nakayama 2500m, based on the Arima Kinen) and the upcoming CM21 (Sprint) and CM22 (Dirt Mile). It lists previous cups with dates and conditions, a CM20 character tier list with debuffer roles, stat baselines (Stamina first), spark and legacy advice, Room Match and Practice Mode tips, and participation requirements. It is useful for CM20 preparation.

#### [Team Trials PvP Scoring System/PvpTeamTrials.md](Team%20Trials%20PvP%20Scoring%20System/PvpTeamTrials.md)

A GameTora article explaining how Team Trials PvP scores are calculated. Additive modifiers are the Ace, Opponent Rating, Support and Consecutive Win bonuses. Team points cover Victory (10,000), Trio/Quinella and All Members Placed. Individual points come from finishing position and the first-to-second margin, skill and unique-skill activations by level and star rarity, Good Positioning, Beat Target Time, Strong Start, Dark Horse and the Rushed penalty. It ends with a worked example of why a losing team out-scored a winning one, with several scoring tables.

---

## 6. Where this lives in the codebase

| Area | Location |
|------|----------|
| Quota logic | `LilyAiTask/MonthlyTask/quota.py` |
| Daily deficit report | `LilyAiTask/DailyTask/DeficitTask/Deficit.py` |
| Trainer link storage | `LilyAiMemory/TrainerLink/TrainerLinkStore` |
| Leaderboard UI | `LilyAiFrontend` |

---

## Troubleshooting

- **Not receiving the daily DM?** Make sure you are linked: DM `link me` and enter your Trainer ID.
- **Wrong or outdated stats?** Data is pulled from uma.moe, so it reflects whatever uma.moe has most recently detected.
