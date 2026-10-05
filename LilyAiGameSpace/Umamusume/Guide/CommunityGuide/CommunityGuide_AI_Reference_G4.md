# UMAMUSUME AI REFERENCE — G4

«Source module: pecan's Champions Meeting Guides

Authors listed in source: pecan, Steven, hanue

Purpose: Track-specific race knowledge, Champions Meeting / League of Heroes observations, skill timing, stat thresholds, strategy constraints, and build tradeoffs.

This module is an extension of "CommunityGuide_AI_updated.md".

IMPORTANT

Guide 4 is primarily a collection of historical event guides.

Therefore:

- Track information can be reusable.
- Course geometry can be reusable.
- Skill interaction observations are useful when tied to the listed track.
- Stat-threshold observations are scenario/version dependent.
- Uma tier rankings are historical.
- Card/meta recommendations are historical.
- "Best Uma" claims are historical opinions.
- Current meta must NOT be inferred from this file without checking the event/version.

SOURCE ID: "G4"»

> **NOTE — INCOMPLETE FILE:** this module is cut off in the middle of the Longchamp 2400m profile (section 32.07). Any track profiles after it were never saved.

---

## 01. DATA_CLASSIFICATION

### 01.01 REUSABLE_TRACK_DATA

The following information is useful as structured race data:

- Race distance.
- Surface.
- Direction.
- Season.
- Weather.
- Ground condition.
- Course width/layout.
- Number and placement of corners.
- Straight length.
- Uphill sections.
- Downhill sections.
- Spurt starting location.
- Final corner relationship to spurt.
- Final straight length.
- Skill activation timing.
- Historical stat thresholds.

### 01.02 HISTORICAL_META

Do not treat the following as permanent facts:

- Best Uma.
- Best strategy.
- Tier list.
- Best support card.
- Current banner recommendations.
- "Must use" recommendations.
- Current parent recommendations.
- Current deck recommendations.

These are event/version dependent.

---

## 02. TRACK_ANALYSIS_MODEL

For AI race evaluation, represent a track using:

TRACK
├── distance
├── surface
├── direction
├── season
├── weather
├── ground_condition
├── corners
├── straights
├── final_corner
├── final_straight
├── hills
├── downhill_sections
├── spurt_start
├── stat_thresholds
├── strategy_environment
└── skill_interactions

---

## 03. SKILL_EFFECTIVENESS_MODEL

Guide 4 repeatedly evaluates skills by where and when they activate.

For AI evaluation:

Skill effectiveness =
Activation condition
+ Activation position
+ Activation timing
+ Duration
+ Race phase
+ Track geometry
+ Strategy compatibility

A skill with a high numerical modifier can still have poor practical value if:

- It activates too late.
- Its position condition is difficult.
- It activates after acceleration is no longer useful.
- The track lacks the required corner/straight.
- The strategy cannot reliably reach its required position.

---

## 04. ACCELERATION_SKILLS

Acceleration skills are strongly dependent on:

- Spurt location.
- Corner position.
- Final straight position.
- Strategy.
- Current race position.
- Track length.

### 04.01 IMMEDIATE_ACCEL

Immediate acceleration is generally most valuable when it overlaps the beginning of the spurt.

### 04.02 LATE_ACCEL

An acceleration skill that activates after a large portion of the spurt has already occurred loses practical value.

### 04.03 RANDOM_ACCEL

Guide 4 repeatedly distinguishes reliable acceleration from random acceleration.

Random acceleration can be useful when:

- Reliable acceleration options are limited.
- The activation window is sufficiently large.
- The race is short enough that the random activation has meaningful probability.

Random acceleration becomes less attractive when:

- Reliable track-specific acceleration exists.
- Its activation condition is narrow.
- Its activation occurs outside the important spurt window.

---

## 05. FINAL_CORNER_SKILLS

Final-corner skills depend heavily on the location of:

Spurt start
vs.
Final corner

### 05.01 SPURT_DURING_FINAL_CORNER

Final-corner acceleration can be highly valuable when the spurt begins during the final corner.

### 05.02 SPURT_AFTER_FINAL_CORNER

If the spurt begins after the final corner:

- Final-corner acceleration may lose value.
- Final-corner speed skills can still retain value depending on timing.

### 05.03 FINAL_CORNER_TOO_EARLY

If the final corner occurs substantially before spurt:

- Acceleration can finish before the important phase.
- Some final-corner skills may therefore have reduced practical value.

AI RULE

Never label a final-corner skill universally good or bad.

Evaluate its activation point against the track's spurt start.

---

## 06. FINAL_STRAIGHT

Final-straight length changes strategy balance.

LONG_FINAL_STRAIGHT

Can favor:

- Backline strategies.
- Long-duration speed skills.
- Late acceleration.
- Guts competition mechanics.

SHORT_FINAL_STRAIGHT

Can favor:

- Frontline strategies.
- Earlier acceleration.
- Early positioning.
- Strong mid-leg positioning.

Guide 4 repeatedly uses final-straight length as an explanation for strategy differences.

---

## 07. HILLS

Hills affect:

- Power.
- Acceleration.
- Speed.
- Stamina consumption.
- Skill timing.

### 07.01 UPHILL

A long uphill section increases the practical value of Power.

### 07.02 DOWNHILL

Downhill sections can:

- Trigger downhill-related mechanics.
- Modify speed.
- Affect stamina consumption.
- Change the value of downhill-specific skills.

### 07.03 SPURT_ON_HILL

When spurt begins on or near a hill:

- Hill-related acceleration/speed interactions become particularly relevant.
- A skill that appears strong in generic analysis may behave differently depending on the hill location.

---

## 08. STAT_THRESHOLDS

Guide 4 uses "stat thresholds" to identify tracks where reaching a specific stat breakpoint produces additional race value.

Common threshold categories:

- Speed.
- Stamina.
- Guts.
- Power.

### 08.01 THRESHOLD_EVALUATION

For a target race:

Required Stat
→ Threshold 1
→ Threshold 2
→ Threshold 3
→ Excess stat value

Do not automatically maximize a stat if:

- The threshold has already been reached.
- Another stat has greater marginal value.
- The excess stat is difficult to obtain efficiently.

---

## 09. STAMINA_THRESHOLD

Stamina thresholds can affect:

- Survival.
- Race-state mechanics.
- Speed effects.
- Stamina Battle mechanics where applicable.

Guide 4 gives historical examples such as:

CHUUKYO 1800M DIRT

The source lists:

Stamina thresholds:
300 / 600 / 900

The source describes 750 Stamina as sufficient for survival in its examined scenario and approximately 867 as the target for maximizing the described threshold effect before Finals motivation.

STATUS: historical event-specific data.

---

## 10. GUTS_THRESHOLD

Guts thresholds are relevant to:

- Final-race competition mechanics.
- Minimum-speed behavior.
- Certain track-specific stat threshold systems.

Guide 4 gives historical examples where:

- 900 Guts was used as a threshold target.
- Guts was compared against Power for marginal value.
- Long final straights were considered favorable to Guts-related competition.

STATUS: track/version dependent.

---

## 11. POWER_VALUE

Guide 4 repeatedly identifies Power as valuable when a track contains:

- Uphill sections.
- Early acceleration requirements.
- Short races where acceleration has a large effect.
- Race-state competition requiring acceleration.

Example:

For Niigata 1000m, Guide 4 identifies the opening hill and short race distance as reasons high Power is valuable.

---

## 12. START_DELAY

Short tracks make start delay more important because:

Lost opening distance
/
Short total race distance
=
larger relative impact

Guide 4 specifically identifies Concentration as valuable on Niigata 1000m because of the effect of start delay on such a short course.

AI RULE

When evaluating a very short race:

- Include start delay in the analysis.
- Do not evaluate Speed alone.
- Consider start-related skills.

---

## 13. NO_CORNER_TRACKS

Niigata 1000m is identified as a track with no corners.

Consequences described by Guide 4:

- Corner-condition skills cannot activate.
- Lane changes are greatly reduced.
- Blocking behavior is reduced.
- Some skills using last-straight conditions can activate unusually early.
- Final-straight competition mechanics can also behave differently.
- Backline strategies are less disadvantaged by blocking.

AI RULE

Before evaluating a corner-based skill:

Does the track actually contain the required corner?

---

## 14. CORNER_COUNT

Corner numbering matters.

Guide 4 notes that some skills use corner-number conditions.

The source gives an example where a skill activating on "corner 3" can actually activate early because corners are numbered from the end in the relevant mechanic.

AI RULE

Do not interpret "corner 3" as simply the third physical corner without checking the game's corner numbering convention.

---

## 15. POSITION_CONDITIONS

Many acceleration skills require a specific race position.

Examples found throughout Guide 4 include conditions such as:

1st
1st–5th
3rd–4th
3rd–5th
5th–6th
5th–8th
6th

AI RULE

Skill value depends on whether the intended strategy can realistically occupy the required position at activation time.

---

## 16. BACKLINE_BLOCKING

Backline strategies can be affected by blocking.

Guide 4 repeatedly identifies blocking as an important disadvantage for:

- Betweeners.
- Chasers.

However, track geometry can reduce or eliminate the problem.

Example:

Niigata 1000m has no corners and minimal lane changes, so Guide 4 notes that blocking is much less significant than normal.

AI RULE

Blocking risk is:

Track geometry
+
Crowd density
+
Strategy
+
Lane movement
+
Positioning

not a fixed property of the strategy.

---

## 17. FRONTLINE_POSITIONING

For Runners and Leaders, early position can determine whether position-dependent skills activate.

Guide 4 repeatedly recommends considering:

- Early-leg speed.
- Positioning skills.
- Opening acceleration.
- Mid-leg speed.

especially when the build requires a specific position for an inherited unique.

---

## 18. NON_RUNNER_POSITIONING

Guide 4 repeatedly identifies "Uma Like" ("ウマ好み") as valuable for non-Runners because it can help them establish a useful early position.

Its value is especially relevant when:

- A Leader needs to reach a specific position.
- A Betweener needs to avoid falling too far back.
- The track is dominated by backline/frontline competition.

This is a historical strategy observation, not a universal requirement.

---

## 19. INHERITED_ACCELERATION

Inherited acceleration should be selected according to:

Strategy
+
Expected position
+
Track spurt location
+
Activation condition
+
Reliability

Common inherited acceleration skills appearing repeatedly in the source include:

- Angling × Skimming.
- Red Maruzensky unique.
- Nishino Flower unique.
- Taiki Shuttle unique.
- Sirius Symboli unique.
- Mejiro Dober unique.
- Mejiro Ryan unique.
- Cheerleader King Halo unique.

IMPORTANT

The fact that a skill appears repeatedly does not mean it is universally best.

The source evaluates these skills differently on different tracks.

---

## 20. INHERIT_SELECTION

Guide 4 demonstrates that inherited skill choice can be modeled as a conditional decision:

If expected_position satisfies Skill_A
    → Skill_A gains value

If expected_position satisfies Skill_B
    → Skill_B gains value

If expected_position is uncertain
    → prefer the skill with greater condition coverage

Popularity requirements, blocking requirements, and strategy requirements can significantly change the expected value.

---

## 21. POPULARITY_CONDITIONS

Some skills depend on popularity.

Guide 4 gives Sirius Symboli's inherited skill as an example:

- A weaker modifier applies outside the required popularity range.
- A stronger modifier applies when the popularity condition is satisfied.

The source notes that popularity can be difficult to predict.

AI RULE

For popularity-dependent skills:

Expected Value =
Probability(popularity condition met)
×
Skill value if met
+
Probability(condition failed)
×
Skill value if failed

---

## 22. SKILL_BUDGET

Guide 4 explicitly warns against buying every available acceleration skill.

Reason:

- Some acceleration skills require different positions.
- Some may conflict with the build's positioning needs.
- Speed skills are still required to reach the required positions.
- Skill Points are limited.

One Guide 4 example recommends approximately:

~800 SP
or
~5 acceleration skills maximum

including inherited uniques and gold skills.

STATUS: historical strategy heuristic, not universal rule.

---

## 23. SPEED_VS_ACCELERATION

Guide 4 demonstrates an important build principle:

Acceleration
does not replace
Positioning Speed.

A build can own many acceleration skills but fail to activate them because it cannot reach the required position.

Therefore:

Speed skills
→ position
→ acceleration condition
→ acceleration

must be evaluated together.

---

## 24. RECOVERY_SKILLS

Recovery requirements depend on:

- Distance.
- Stamina.
- Guts.
- Race-state mechanics.
- Strategy.
- Competition.
- Track geometry.

Guide 4 provides historical examples where:

- 2400m builds were evaluated with approximately 800 Stamina.
- 2500m builds were evaluated around 1250 Stamina.
- 3200m builds were evaluated around 1300+ Stamina.
- Oonige competition can require substantially more Stamina than ordinary racing.

These are historical event-specific values.

---

## 25. OONIGE_COMPETITION

Guide 4 identifies Oonige/Runner competition as a special stamina-intensive race state.

The source states that:

- Multiple Oonige can consume very large amounts of HP.
- Insufficient preparation can cause both competing Runners to run out of HP.
- Guts affects the competition modifier and duration.
- Higher Guts can increase consumption requirements.

One historical example gives approximately:

1200 Stamina
+
2 Gold Recoveries

as generally sufficient for the examined 1600m Oonige competition situation.

STATUS: historical scenario-specific observation.

---

## 26. STAMINA_VS_POWER

Guide 4 contains explicit comparisons between overcapping Stamina and increasing Power.

One examined track concluded:

- Power can have greater value per stat for the relevant mechanic.
- Stamina builds are easier to execute.
- Overcapped Stamina can provide race benefits.
- Deck constraints can make the theoretically stronger Power build impractical.

The source describes several possible deck structures:

3 Speed + 1 Stamina
2 Speed + 2 Power
3 Speed + 1 Guts
1 Speed + 3 Guts

with remaining slots occupied by scenario/Intelligence support as appropriate.

AI RULE

Do not convert this into a universal "Power > Stamina" rule.

Evaluate:

Stat value
+
Deck accessibility
+
Skill availability
+
Inheritance cost
+
Threshold requirements

---

## 27. OVERCAP_STAMINA

Guide 4 describes a track-specific Stamina Battle mechanic.

The source states:

- The mechanic has no effect below 1200 Stamina in the examined context.
- Additional Stamina above the threshold can produce additional speed.
- A specific historical comparison equates approximately 1300 Stamina to the effect of an additional speed green under the examined conditions.

STATUS: historical/version-specific.

---

## 28. POWER_VS_GUTS

Guide 4 provides a historical comparison where:

- Power is slightly stronger per stat.
- Overcapping Power is more difficult.
- Raising Guts into the 900–1200 range may be easier.
- If a Power card is required for a key skill, inheritance can be used to compensate for Guts.
- If using a Guts-heavy build, Power inheritance may be appropriate.

STATUS: track-specific analysis.

---

## 29. LEAGUE_OF_HEROES_FORMAT

Guide 4 repeatedly distinguishes League of Heroes from Champions Meeting.

Important implications in the source:

- Consistency can be more important than maximum single-race winning power.
- Top-three consistency can matter more than maximizing first-place probability.
- Backline strategies can be penalized depending on field composition.
- Debuff strategies may have different value depending on the format.

AI RULE

Never transfer a League of Heroes recommendation directly to Champions Meeting without considering the scoring format.

---

## 30. CHAMPIONS_MEETING_FORMAT

Champions Meeting analysis can emphasize:

- Win probability.
- Room composition.
- Strategy distribution.
- Skill reliability.
- Counter-building.
- Opponent strategy.

Therefore:

Best for LOH
≠
Best for CM

---

## 31. DEBUFFERS

Guide 4 contains both positive and negative historical opinions about debuffers depending on the event.

The reusable data is:

Debuff effectiveness depends on:

- Target's Stamina.
- Target's strategy.
- Debuff range.
- Activation condition.
- Field composition.
- Format.

Example:

The August 2023 Funabashi 1600m dirt section explicitly analyzes stamina debuffs and speed debuffs as part of that event's environment.

AI RULE

Do not treat debuffers as universally good or bad.

---

## 32. TRACK_PROFILE_EXAMPLES

The following historical profiles are useful as examples of how track geometry changes build evaluation.

### 32.01 KYOTO_1600_TURF

Historical Guide 4 entries include:

Distance: 1600m
Surface: Turf
Direction: Clockwise
Season: Autumn
Weather/Ground: Variable in listed LOH events

The source repeatedly analyzes:

- Runner/frontline strength.
- Mile acceleration.
- High-value position-dependent skills.
- Race Bonus/skill considerations depending on event format.

STATUS: historical track profile.

### 32.02 CHUUKYO_1800_DIRT

Distance: 1800m
Surface: Dirt
Direction: Counter-clockwise
Season: Summer
Weather: Sunny
Ground: Good

Source observations:

- Stamina thresholds: "300 / 600 / 900".
- A downhill section of approximately "600m".
- High Wisdom is described as beneficial in the examined event.
- Final-corner spurt timing strongly affects acceleration skill selection.

### 32.03 NIIGATA_1000_TURF

Distance: 1000m
Surface: Turf
Direction: Straight
Season: Summer

Source observations:

- No corners.
- Corner-condition skills cannot activate.
- Some last-straight conditions can activate unusually early.
- Blocking is greatly reduced.
- Start delay has large relative impact.
- Power is valuable because of the opening hill.
- Guts is valuable because of final-straight competition.
- Speed can be sacrificed somewhat for Power/Guts compared with normal builds.

### 32.04 TOKYO_2400_TURF

Distance: 2400m
Surface: Turf
Direction: Counter-clockwise
Season: Spring
Ground: Heavy
Weather: Cloudy

Source observations:

- Final straight approximately "525m".
- Backline strategies can benefit from the long final straight.
- Spurt begins around the third corner in the examined event.
- Final-corner acceleration can therefore be relevant.
- Long final straight makes late acceleration and speed important.
- Stamina requirements can be high.
- Positioning skills are important for non-Runners.

### 32.05 KYOTO_3200_TURF

Distance: 3200m
Surface: Turf
Direction: Clockwise
Season: Spring

Source observations:

- Long-distance acceleration is important.
- High Stamina requirement.
- Recovery reliability becomes important.
- Long-race strategy can favor frontlines depending on format.
- The source gives approximately 1300+ Stamina as a historical target for the examined LOH event.

### 32.06 NAKAYAMA_2500_TURF

Distance: 2500m
Surface: Turf
Direction: Clockwise
Season: Winter
Ground: Heavy
Weather: Snowy

Source observations:

- Stamina and Guts thresholds are relevant.
- Spurt begins on a straight.
- Final corner follows shortly after spurt start.
- Both straight and final-corner acceleration can therefore have value.
- Historical safe-build discussion used approximately "1250 Stamina + 1000 Guts".
- Recovery can substitute for some raw Stamina.

### 32.07 LONGCHAMP_2400_TURF

Distance: 2400m
Surface: Turf
Direction: Clockwise
Season: Autumn
Weather: Rainy
Ground: Soft

Source observations:

- Spurt starts late on the final corner.
- Final straight follows shortly afterward.
- Final-straight acceleration is less useful because of timing.
- Final-straight speed skills can have high value.
- Long uphill makes Power valuable.
- Stamina and Power thresholds are relevant.
- Non-Runner early-position skills can be important.
- Th

> **NOTE — FILE ENDS HERE.** The last line was cut off when the file was saved.
