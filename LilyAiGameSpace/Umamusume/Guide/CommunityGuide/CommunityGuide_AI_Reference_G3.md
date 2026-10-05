# UMAMUSUME AI REFERENCE — G3

«Source module: Guide 3 — Uma Musume Race Mechanics
Source author: KuromiAK

Purpose: Race simulation mechanics, stat processing, movement, acceleration, stamina/HP, skills, lane behavior, positioning, and race-state mechanics.

This module is an extension of "CommunityGuide_AI_updated.md".

IMPORTANT SOURCE STATUS

The source states that much of the race logic comes from reverse engineering, race simulators, parameter files, packet captures, and manual testing. It also states that not all information is guaranteed correct.

Mechanics after the 1st anniversary may include inferred information because the developers stopped including new race mechanics directly in the client.

Therefore each section should retain its confidence classification:

- "CONFIRMED" = directly established or repeatedly verified.
- "REVERSE_ENGINEERED" = derived from game behavior/code/data.
- "INFERRED" = based primarily on parameter data or incomplete testing.
- "SERVER_DEPENDENT" = may differ by server/version.

SOURCE ID: "G3"»

---

## 01. RACE_SIMULATION_STRUCTURE

### 01.01 FRAME_RATE

CONFIRMED

- Race simulation runs at approximately "0.0666 seconds per tick".
- This corresponds to approximately "15 frames per second".

SOURCE: "G3"

### 01.02 RACE_REPLAY_RECORDING

The game records Uma position:

- Every frame within 1 second of race start.
- Every frame when an Uma is within 25m of the goal.
- Otherwise at approximately 1-second intervals.

The source explains that the high-frequency recording near the goal was introduced to fix a replay-display issue where the apparent winner could differ from the actual result.

SOURCE: "G3"

---

## 02. RACE_SECTIONS

CONFIRMED

A race course is divided into "24 equal-distance sections".

Sections:

1–24

These sections are used by multiple race mechanics, including:

- Target-speed randomness.
- Skill conditions.
- Phase progression.

SOURCE: "G3"

---

## 03. RACE_PHASES

A race has four phases.

Phase| Name| Sections
0| Early-race| 1–4
1| Mid-race| 5–16
2| Late-race| 17–20
3| Last Spurt phase| 21–24

IMPORTANT

"Last Spurt phase" and the actual "Last Spurt" mechanic are not necessarily identical concepts.

The source explicitly warns not to confuse them.

SOURCE: "G3"

---

## 04. DISTANCE_UNIT

### 04.01 BASHIN

"Bashin" is a unit of race distance based on horse length.

It is used by movement and positioning mechanics.

### 04.02 HORSE_LANE

The source uses:

1 horse lane = 1/18 course width

SOURCE: "G3"

---

## 05. COURSE_WIDTH

### 05.01 COURSE_WIDTH

The source defines:

1 course width = 11.25m

Lane distance is measured from the inner fence using course-width units.

### 05.02 COURSE_WIDTH_RANGE

The maximum lane distance differs by race course.

The source identifies:

- Tokyo Turf as the widest example at approximately "1.5 course width".
- Several Sapporo/Hakodate/Niigata Dirt courses as narrow examples at approximately "1.1 course width".

Some courses can change maximum width during the race.

SOURCE: "G3"

---

## 06. STAT_PROCESSING

### 06.01 RAW_STATS

Raw Stats are the values displayed in the stat panel.

### 06.02 RAW_STAT_OVER_1200

The source states that:

Raw Stat above 1200
→ excess portion is halved
→ converted to Base Stat

Example structure:

Raw Stat = 1600

Base-stat contribution:
1200 + (400 × 0.5)

IMPORTANT

The source separately states that stat caps were raised to "2500" at the 5th Anniversary. The older 1200 conversion behavior remains part of the source's stat-processing description.

SOURCE: "G3"

### 06.03 BASE_STATS

Base Stats are Raw Stats after Motivation modification.

Base Stats are used by some race calculations, including Skill Activation Chance.

Base Stats are also subject to clamping.

SOURCE: "G3"

---

## 07. MOTIVATION_COEFFICIENT

The source provides the following Motivation coefficients:

Motivation| Coefficient
Very Good| 1.04
Good| 1.02
Normal| 1.00
Bad| 0.98
Very Bad| 0.96

SOURCE: "G3"

---

## 08. ADJUSTED_STATS

Adjusted Stats are generated after applying race-specific modifiers.

The source identifies the following categories:

- Ground modifier.
- Strategy proficiency modifier.
- Race-course modifier.
- Single-mode modifier.

Adjusted Stats are also subject to clamping.

AI RULE

When evaluating a race result:

Displayed Stat
≠
Race-effective Stat

Race-effective values can depend on:

- Motivation.
- Aptitude/proficiency.
- Course.
- Strategy.
- Other race modifiers.

SOURCE: "G3"

---

## 09. SPEED_SYSTEM

Speed is not a single number during a race.

The source distinguishes:

- Base Speed.
- Target Speed.
- Current Speed.
- Actual Speed.
- Minimum Speed.
- Starting Speed.

These values interact with:

- Phase.
- Distance.
- Strategy.
- Terrain.
- Slope.
- Randomness.
- Skills.
- Stamina state.
- Lane movement.

---

## 10. BASE_SPEED

CONFIRMED

A race's Base Speed is determined by the race-course distance.

The source treats Base Speed as a foundational value for subsequent target-speed calculations.

SOURCE: "G3"

---

## 11. TARGET_SPEED

Target Speed is the speed the Uma attempts to reach under the current race state.

Target Speed can be affected by:

- Base Speed.
- Strategy.
- Race phase.
- Distance aptitude.
- Course conditions.
- Slope.
- Random section modifiers.
- Skills.
- Special race states.

AI RULE

Do not evaluate a race from the Uma's displayed Speed stat alone.

The relevant question is:

What target speed was the Uma attempting to maintain
during the relevant race phase?

---

## 12. CURRENT_SPEED

Current Speed is the Uma's current movement speed.

The source distinguishes it from Target Speed.

Current Speed moves toward Target Speed over time through acceleration/deceleration.

---

## 13. ACTUAL_SPEED

Actual Speed includes effects from skills and movement.

The source notes that actual speed differs from the simplified lane-change representation and can be affected by whether the Uma is moving inward/outward.

---

## 14. SPEED_RANDOMNESS

The race is divided into 24 sections.

The source describes a random modifier applied to Target Speed on a per-section basis.

AI RULE

Two runs with identical visible Stats and skills can therefore produce different race outcomes because race-state randomness exists.

SOURCE: "G3"

---

## 15. LAST_SPURT

Last Spurt is a race-state mechanic that increases the target speed during the final portion of a race.

It depends on:

- Current race position.
- Remaining HP.
- Stamina state.
- Race distance.
- Speed.
- Relevant modifiers.

IMPORTANT

The source's race-phase "Last Spurt" label refers to Sections 21–24. This should not automatically be interpreted as saying every Uma is already in its full spurt state throughout those sections.

---

## 16. STARTING_SPEED

Starting Speed is handled separately from ordinary race speed.

The source describes:

- Starting position.
- Start delay.
- Starting speed.
- Start Dash.

as separate initialization/race mechanics.

SOURCE: "G3"

---

## 17. MINIMUM_SPEED

Minimum Speed is especially important when an Uma is out of HP.

CONFIRMED

When an Uma is out of HP:

Target Speed = Minimum Speed

After Start Dash, if current speed falls below Minimum Speed, the speed is raised to Minimum Speed after the frame's acceleration calculation.

Minimum Speed is affected by Guts.

SOURCE: "G3"

---

## 18. ACCELERATION

Acceleration changes Current Speed toward Target Speed.

The source separates:

- Base Acceleration.
- Strategy-phase coefficient.
- Ground-type proficiency modifier.
- Distance-proficiency modifier.
- Start Dash.

Acceleration is therefore not determined by Power alone.

---

## 19. START_DASH

Start Dash is a special acceleration phase occurring at race start.

It is handled separately from normal acceleration.

The source places Start Dash within the race initialization/movement system.

---

## 20. SLOPE

### 20.01 UPHILL

When running uphill:

- Target Speed is reduced by a slope modifier.

### 20.02 DOWNHILL

When running downhill:

- The Uma has a chance each second to enter Downhill Acceleration Mode.
- Downhill Acceleration Mode increases Target Speed.
- It also reduces HP consumption by "60%".
- Each second in Downhill Acceleration Mode has a "20%" chance to end.

SOURCE: "G3"

---

## 21. STAMINA_TO_HP

CONFIRMED

Stamina is converted to HP at the beginning of a race.

The resulting HP pool is then consumed throughout the race.

AI RULE

Do not directly equate Stamina to race speed.

Instead:

Stamina
→ HP
→ HP consumption
→ ability to maintain target speed
→ spurt/race-state behavior

SOURCE: "G3"

---

## 22. HP_RECOVERY

HP recovery skills restore a percentage of maximum HP.

FACT

- Recovery above maximum HP is wasted.
- Recovery skills operate through the same general HP-restoration mechanism regardless of trigger condition; the trigger determines when the recovery occurs.

SOURCE: "G3"

---

## 23. OUT_OF_HP

When an Uma runs out of HP:

Target Speed → Minimum Speed

This can cause a substantial loss of race performance.

AI RUN-EVALUATION RULE

If an Uma performed poorly despite having sufficient Speed:

1. Check Stamina.
2. Check recovery skills.
3. Check HP state.
4. Check whether the Uma reached Minimum Speed.
5. Then inspect positioning/blocking/skill activation.

Do not automatically blame Speed.

SOURCE: "G3"

---

## 24. SKILL_ACTIVATION

### 24.01 PRE_RACE_CHECK

Many skills require a Wisdom check before the race.

The source describes Skill Activation Chance as being calculated before the race.

At initialization:

1. Base Stats are calculated.
2. Skill activation chance is calculated.
3. The game determines which skills are capable of activating.
4. Skills that activate out of the gate are activated.
5. Start-related calculations continue.

SOURCE: "G3"

### 24.02 AI_RULE

A skill can therefore fail to activate because of its activation check before race-state conditions are even considered.

For a failed skill, distinguish:

Activation failure
vs.
Condition not reached
vs.
Condition reached but skill unavailable

---

## 25. SKILL_DURATION

Many skills have a base duration.

The actual duration scales with race-course distance.

AI RULE

Skill duration cannot always be compared using the displayed base duration alone.

A longer race can produce a longer effective skill duration.

SOURCE: "G3"

---

## 26. SKILL_COOLDOWN

Skills can have cooldown behavior that prevents immediate repeated activation.

Cooldown must be considered separately from:

- Activation Chance.
- Skill condition.
- Skill duration.

---

## 27. SKILL_CONDITIONS

Skill conditions can depend on race state.

The source identifies condition types including:

- Random section.
- Straight section.
- Corner section.
- Any corner.
- Phase.
- Remaining distance.
- Position/order.
- Nearby Uma count.
- Being surrounded.
- Nearby Uma position.
- Time spent behind/forward of nearby Umas.
- Number of previous activations.

AI RULE

A skill's practical reliability depends on the probability that its condition occurs in the intended race.

---

## 28. SKILL_TARGET

Skill targets determine which Uma receives the effect.

Target behavior can depend on:

- Self.
- Nearby Umas.
- Position.
- Strategy.
- Race state.

When evaluating a skill, distinguish:

Activation condition
+
Target selection
+
Effect
+
Duration

---

## 29. SKILL_LEVEL

Skill level affects skill strength.

The source specifically notes:

UNIQUE_RECOVERY

- Recovery Unique skill strength increases by approximately "2% per level".

OTHER_UNIQUE_SKILLS

- First level increase: approximately "1%".
- Subsequent level increases: approximately "3%".

SOURCE

The exact effect is source-specific and should remain version-scoped.

---

## 30. SKILL_VALUE_SCALING

The source documents several internal value-scaling types.

These include:

- Direct value.
- Multiply Skill Number.
- Aoharu-related scaling.
- Random multiplication.
- Climax scaling.
- Maximum Raw Stat scaling.
- Activated skill-count scaling.
- Distance-difference scaling.
- Blocked-side/time scaling.
- Speed multiplication.
- Global potential scaling.
- Lead amount scaling.

AI RULE

A skill's displayed effect may not represent its final race effect if the skill uses one of these scaling systems.

---

## 31. SKILL_DURATION_SCALING

Duration can scale using:

- Direct duration.
- Distance difference.
- Remaining HP.
- Order changes.
- Blocking/time conditions.

The source describes certain skills whose duration increases when the Uma successfully overtakes.

Example:

- Duration can increase by "1 second" per successful overtake.
- Up to "3" times.
- Additional duration uses the same distance scaling as base duration.

SOURCE: "G3"

---

## 32. ADDITIONAL_ACTIVATION

Some skills contain an additional activation/effect.

The source describes this as:

- The additional effect does not necessarily occur immediately at initial skill activation.
- Instead it becomes active when its specified condition is achieved.
- It can apply for the remaining skill duration.
- Some additional effects can trigger multiple times.

---

## 33. LANE_SYSTEM

### 33.01 LANE_DISTANCE

Lane position is measured from the inner fence.

Units:

1 course width = 11.25m
1 horse lane = 1/18 course width

### 33.02 LANE_LIMIT

Minimum lane distance:

0

Maximum lane distance depends on the race course.

### 33.03 INITIAL_LANE

Initial lane is determined by:

- Race course.
- Gate number.
- Course-specific adjustment.

The source lists special initial-lane adjustments for:

- Ooi.
- Kawasaki.
- Funabashi.
- Longchamp.
- Other JRA courses.

SOURCE: "G3"

---

## 34. LANE_CHANGE_SPEED

Lane-change movement contains multiple components:

- Actual Speed.
- Current Speed.
- Target Speed.

Current Speed changes toward Target Speed during lane movement.

When the target lane is reached:

Current lane-change speed resets to 0

Actual speed accounts for skill effects and differs depending on movement direction.

---

## 35. TARGET_LANE

Target Lane is the lane an Uma is attempting to reach.

Target Lane is updated when:

- The Uma is within "0.5 horse lane" of the current target.
- The Uma is blocked on the side toward which she is moving.

The source identifies three movement strategies:

1. Normal Mode.
2. Fixed Mode.
3. Overtake Mode.

---

## 36. OVERTAKE_TARGET

To become an overtake target, an Uma generally must:

- Be visible.
- Be approximately "1–20m" ahead.
- Be catchable within "15 seconds" using the current speed difference.
- Have a lower target speed than the Uma, or be blocked and have a lower current speed than the Uma's target speed.

The closest Uma directly blocking the front is also automatically an overtake target.

SOURCE: "G3"

---

## 37. NORMAL_LANE_MODE

Normal mode is used when:

- No overtake target exists.
- Or during specified early/mid-race movement conditions near a Move Lane Point.

The source's normal-mode behavior includes:

1. If out of HP, keep the current lane.
2. If Pace Down is active, use the specified target lane.
3. During/after final corner, use the Extra Move Lane when applicable and unblocked.
4. Early/mid race may move slightly inward when unblocked.
5. Mid-race positioning can force additional separation from an inside Uma.
6. Otherwise remain straight.

SOURCE: "G3"

---

## 38. OVERTAKE_MODE

When overtake targets exist:

- The Uma enters Overtake Mode.
- When all overtake targets are lost, Overtake Mode continues for approximately "1.5 seconds".

Overtake candidates are derived from the crowd surrounding the overtake target.

---

## 39. BLOCKING

Blocking can prevent an Uma from moving toward her desired lane.

If blocked in the direction of movement:

- The lane does not change.
- The Uma can continue accelerating and accumulate lane-change speed.

AI RUN-EVALUATION RULE

A failed overtake or poor race result can be caused by:

Position
+
Lane
+
Blocking

rather than insufficient Stats.

---

## 40. POSITIONING_MODES

The race uses multiple position-management states.

The source identifies:

- Normal Mode.
- Pacemaker.
- Speed Up Mode.
- Overtake Mode.
- Pace Up Mode.
- Pace Down Mode.
- Pace Up Ex Mode.

These modes modify how the Uma chooses target speed and/or lane.

---

## 41. PACEMAKER

Pacemaker behavior is associated with front-running/position maintenance.

It interacts with:

- Strategy.
- Nearby Umas.
- Target speed.
- Position keeping.

---

## 42. PACE_UP

Pace Up behavior changes target speed when the Uma needs to improve position.

---

## 43. PACE_DOWN

Pace Down behavior reduces movement requirements in certain positioning states.

The source explicitly connects Pace Down to lane selection in Normal Mode.

---

## 44. RUSHED / KAKARI

"Kakari" is a race-state condition affecting behavior and HP consumption.

The source treats it as a distinct race state alongside:

- Rushed.
- Temptation.

AI RULE

If an Uma unexpectedly loses HP early:

- Check Kakari/rushed behavior.
- Do not assume the Stamina stat itself was incorrect.

---

## 45. SPOT_STRUGGLE

Spot Struggle / Lead Competition is a race-state mechanic related to competing for position.

It can influence:

- Position.
- Speed.
- Stamina/HP usage.
- Relative race performance.

---

## 46. DUELING

Dueling / Compete Fight is a race-state mechanic involving Umas competing directly.

It should be treated separately from ordinary target-speed movement.

---

## 47. CHARGE_UP

Charge Up / Fully Charged and Conserve Power / Release are race-state mechanics related to conserving or releasing race performance.

These mechanics can affect late-race performance and should be evaluated separately from ordinary Speed.

---

## 48. COMPETE_BEFORE_SPURT

"Compete Before Spurt" is a pre-spurt positioning mechanic.

It affects race-state behavior before the main spurt phase.

---

## 49. STAMINA_KEEP

"Stamina Keep" is a race-state behavior related to conserving stamina.

It can change the tradeoff between:

Current position/speed
vs.
remaining HP

---

## 50. SECURE_LEAD

"Secure Lead" is a race-state mechanic associated with maintaining a lead.

It should be treated separately from ordinary target-speed calculations.

---

## 51. STAMINA_LIMIT_BREAK

INFERRED

The source explicitly warns that this section is based on game parameter data and is less concretely confirmed.

The described behavior is:

- If Base Stamina plus skill-based Stamina bonuses exceeds "1200",
- the Uma gains an additional Target Speed buff after reaching maximum spurt speed.
- The buff lasts until the end of the race.

AI RULE

Never present this as universally confirmed without retaining the "INFERRED" status.

SOURCE: "G3"

---

## 52. ZENKAI_SPURT

"Zenkai Spurt" is a race-state mechanic associated with full spurt behavior.

It should be evaluated separately from:

- Last Spurt phase.
- Normal acceleration.
- Target Speed.
- Stamina Limit Break.

---

## 53. WIZ_LIMIT_BREAK_BUFF

Guide 3 identifies a Wisdom-related Limit Break Buff as a separate race mechanic.

Its exact behavior is version/mechanic dependent.

AI RULE

Do not collapse this mechanic into ordinary Skill Activation Chance.

---

## 54. RACE_FINISH_TIME

Finish time is determined by the accumulated result of:

- Course distance.
- Current Speed.
- Acceleration.
- Deceleration.
- Lane movement.
- Blocking.
- Skills.
- Race-state behavior.
- HP/stamina state.

AI RULE

A lower visible stat total can still produce a faster race if race-state interactions favor that build.

---

## 55. RACE_COURSE

Race courses define:

- Distance.
- Width.
- Lane boundaries.
- Slopes.
- Course events.
- Move Lane Points.
- Extra Move Lane.
- Surface.
- Course-specific mechanics.

Therefore a skill or stat cannot always be evaluated independently of the race course.

---

## 56. COURSE_EVENTS

Course events can include:

- Uphill.
- Downhill.
- Corners.
- Straights.
- Move Lane Points.
- Other course-specific positional triggers.

Course events influence:

- Speed.
- Acceleration.
- Lane changes.
- Skill conditions.
- HP consumption.

---

## 57. INITIALIZATION_ORDER

At race initialization, the source gives the following order:

1. Calculate Base Stats.
2. Calculate Skill Activation Chance and determine which skills can activate.
3. Activate skills that trigger out of the gate.
4. Use relevant item effects.
5. Set starting location from gate number.
6. Calculate start delay.
7. Calculate adjusted Stats.

SOURCE: "G3"

---

## 58. RACE_EVALUATION_MODEL

For AI evaluation of a completed run, use the following causal chain:

CHARACTER_BUILD
    ↓
RAW_STATS
    ↓
BASE_STATS
    ↓
MOTIVATION
    ↓
RACE_ADJUSTED_STATS
    ↓
RACE_INITIALIZATION
    ↓
SKILL_ACTIVATION_CHECK
    ↓
START_STATE
    ↓
PHASE / SECTION
    ↓
TARGET_SPEED
    ↓
CURRENT_SPEED
    ↓
ACCELERATION / DECELERATION
    ↓
POSITION / LANE / BLOCKING
    ↓
HP / STAMINA STATE
    ↓
SKILLS + RACE STATES
    ↓
FINISH TIME / PLACEMENT

This structure should be preferred over evaluating the result from final Stats alone.

---

## 59. AI_DIAGNOSTIC_ORDER

When a player asks:

«"Why did my Uma lose?"»

Evaluate in this order.

STEP_01

Check:

- Distance aptitude.
- Surface aptitude.
- Running-style suitability.

STEP_02

Check:

- Stamina.
- HP.
- Recovery skills.
- Whether the Uma reached 0 HP.

STEP_03

Check:

- Speed.
- Target Speed.
- Last Spurt behavior.

STEP_04

Check:

- Power.
- Acceleration.
- Uphill/downhill interactions.

STEP_05

Check:

- Wisdom.
- Skill activation.
- Positioning behavior.

STEP_06

Check:

- Skill conditions.
- Skill timing.
- Skill duration.
- Skill target.

STEP_07

Check:

- Blocking.
- Lane.
- Overtake behavior.
- Positioning states.

STEP_08

Check:

- Race randomness.
- Section-specific conditions.
- Course-specific events.

AI RULE

Do not label a run "badly trained" merely because it lost.

A loss can result from:

Stamina failure
Skill failure
Positioning
Blocking
Course interaction
Race-state behavior
Randomness

---

## 60. BUILD_EVALUATION

When evaluating a build for a target race, compare:

SPEED

Can the build achieve the required target speed?

STAMINA

Can it maintain the required speed without reaching 0 HP?

POWER

Can it accelerate sufficiently during:

- Start.
- Position fights.
- Corners.
- Spurt.
- Uphill sections?

GUTS

Does it benefit from:

- Minimum-speed behavior.
- HP-consumption effects.
- Late-race mechanics?

WISDOM

Does it improve:

- Skill activation reliability.
- Position/race-state consistency.
- Other Wisdom-dependent mechanics?

SKILLS

Are the skills:

- Activating?
- Activating at useful times?
- Affecting the correct race state?
- Lasting long enough?
- Triggering on the intended course?

---

## 61. SKILL_EVALUATION_FRAMEWORK

Never evaluate a skill only by its displayed numerical effect.

Use:

Skill Value =
Effect Magnitude
× Effective Duration
× Activation Probability
× Condition Probability
× Target Relevance
× Race-State Relevance

This is an AI evaluation framework derived from the mechanics described by Guide 3; it is not presented as an official game formula.

### 61.01 EFFECT_MAGNITUDE

How large is the speed/acceleration/recovery/etc. effect?

### 61.02 EFFECTIVE_DURATION

How long does the effect actually last on the target race distance?

### 61.03 ACTIVATION_PROBABILITY

Can the Uma pass the pre-race Skill Activation check?

### 61.04 CONDITION_PROBABILITY

How often will the race state satisfy the skill's condition?

### 61.05 TARGET_RELEVANCE

Does the skill affect:

- Self?
- Nearby opponents?
- A specific strategy?
- A specific distance?

### 61.06 RACE_STATE_RELEVANCE

Does it activate during a strategically valuable period?

---

## 62. SOURCE_CONFIDENCE_RULES

CONFIRMED

Use directly as factual mechanics where the source establishes them.

Examples:

- 24 race sections.
- Four race phases.
- 15 FPS simulation.
- HP recovery exceeding max is wasted.
- Out-of-HP target speed becomes Minimum Speed.

REVERSE_ENGINEERED

Use as mechanical reference, but retain source attribution.

INFERRED

Do not silently convert into certainty.

Example:

- Stamina Limit Break.

SERVER_DEPENDENT

Always retain the server/version condition.

The source explicitly warns that mechanics and bugs can differ between servers.

---

## 63. VERSION_SCOPE

Guide 3 contains mechanics spanning different game versions.

The source specifically notes:

- New mechanics after the 1st anniversary are harder to verify directly.
- Some mechanics are inferred from parameter files and replay data.
- Some sections can therefore be incomplete or under investigation.

AI RULE

When a mechanic appears to conflict with another source:

1. Check game version.
2. Check server.
3. Check whether the mechanic is marked inferred.
4. Check whether the mechanic was changed after the source was written.
5. Do not automatically merge conflicting values.

---

## 64. MASTER_REFERENCE_USAGE

This module should be used primarily when the AI needs to answer:

- Why did this Uma lose?
- Why did Stamina matter?
- Why did the Uma fail to reach/maintain speed?
- Why did a skill not activate?
- Why did a skill activate too early/late?
- Why did blocking occur?
- Why did an Uma fail to overtake?
- Why did two apparently similar builds perform differently?
- How do Speed, Power, Guts, Wisdom, and Stamina interact during racing?
- How does race distance affect skill duration?
- How does race phase affect target speed?
- How does HP state affect race performance?

---

## 65. SOURCE_TRACEABILITY

SOURCE_ID

"G3"

SOURCE_TITLE

"Uma Musume Race Mechanics"

SOURCE_AUTHOR

"KuromiAK"

SOURCE_SCOPE

Race simulation and race-mechanics reference.

SOURCE_METHODS

The source states that its information is based on combinations of:

- Reverse engineering.
- Race simulators.
- Parameter files.
- Packet captures.
- Manual testing.

SOURCE_LIMITATION

Not all information is guaranteed correct.

Mechanics after the 1st anniversary may contain inferred behavior.

Server differences may exist.

MASTER_REFERENCE

This file is an extension of:

"CommunityGuide_AI_updated.md"
