# UMAMUSUME AI REFERENCE — G2

«Source module: Guide 2 — Uma Musume Reference
Purpose: General training, stat, race, support-card, skill, and run-evaluation reference.

This module is an extension of "CommunityGuide_AI_updated.md".

SOURCE STATUS: Guide 2 contains a mixture of mechanical information, practical training advice, scenario-specific strategy, current/meta recommendations, and personal evaluation. Only mechanically supported information should be treated as FACT. Strategy recommendations remain scoped to the source and its stated scenario/context.»

> **NOTE — INCOMPLETE FILE:** this module is cut off partway through section 24. Anything after that point in Guide 2 was never saved.

---

## 01. SOURCE_SCOPE

### 01.01 GENERAL

FACT

- Guide 2 is a Japanese-server-focused reference document.
- The document is intended to answer questions about game mechanics, training, racing, support cards, skills, inheritance, and related systems.
- The document contains information from multiple eras/scenarios.
- Some sections are explicitly marked outdated or superseded.

AI RULE

- Do not treat the entire document as current meta data.
- Mechanical information and scenario-specific information must retain their scope.
- Tier lists, banner recommendations, and current-event recommendations must not be promoted to permanent facts.

SOURCE: "G2"

---

## 02. COMMON_TERMS

### 02.01 STATS

Term| Meaning
Speed| Speed
Stamina| Stamina
Power| Power
Guts| Guts
Wisdom / Intelligence / Wit| Wisdom
Energy| Training HP/Energy
Motivation| Mood

### 02.02 SURFACE

- Turf
- Dirt

### 02.03 DISTANCE

- Short: 1000m–1400m
- Mile: 1500m–1800m
- Mid: 1900m–2400m
- Long: 2500m–3600m

### 02.04 RUNNING_STYLES

- Runner / Escape
- Leader
- Betweener
- Chaser

### 02.05 TRAINING_TERMS

- Rainbow = Friendship training.
- Bond = Support-card bond gauge.
- Hint = "!" appearing on training.
- Welfare = Free support card, including event/story cards.
- LB = Limit Break.
- MLB = Maximum Limit Break / 4LB.
- Spark = Selecting an SSR/3★ after 200 rolls on the same banner.

SOURCE: "G2"

---

## 03. BASIC_TRAINING_STRATEGY

### 03.01 EARLY_TRAINING

SOURCE GUIDANCE

During the early phase:

1. Raise support-card Bond.
2. Work toward Orange Bond so Friendship/Rainbow training becomes available.
3. Once cards are sufficiently bonded, prioritize Rainbow training.
4. If no useful Rainbow is available:
   - Wisdom training can be considered.
   - Racing can be considered.

SOURCE: "G2"

### 03.02 SUPPORT_BOND

FACT

- Support-card Bond is displayed during training selection.
- Rainbow/Friendship training requires the support to reach the required Bond state.

SOURCE: "G2"

### 03.03 EXPERIENCE_RULE

The source notes that experienced players can alter the basic flow depending on:

- Risk tolerance.
- Available Rainbow training.
- Motivation.
- Energy.
- Target stats.
- Upcoming scheduled events.

These are decision variables rather than fixed rules.

---

## 04. URA_TRAINING_STRATEGY

### 04.01 TRAINING_LEVELS

FACT

- A training gains a level after being performed four times.
- Higher training levels increase the stats obtained from that training.
- Training selection therefore affects the future value of that training type.

SOURCE: "G2"

### 04.02 BONDING_WITH_TRAINING_LEVELS

During the Bonding phase:

- Prioritize support Bond.
- Also consider which training types you intend to use later.
- Training a slightly worse Bond opportunity can be justified if it helps level an important training type.

SOURCE: "G2"

### 04.03 WISDOM_TRAINING

FACT

- Wisdom training does not consume Energy in the same way as the other standard trainings.
- Guide 2 therefore treats Wisdom training as an important low-energy option.

### 04.04 GUTS_TRAINING

SOURCE EVALUATION

- Guts training has the highest Energy cost among normal trainings.
- Guide 2 therefore recommends avoiding weak Guts trainings unless their output is sufficiently high.

STATUS: "STRATEGY", not universal rule.

---

## 05. HINTS_AND_BOND

### 05.01 HINT_BOND

FACT

- A support-card Hint provides +5 Bond according to Guide 2.

### 05.02 HINT_VALUE

A Hint can simultaneously:

- Increase Bond.
- Move a support toward Rainbow/Friendship activation.
- Provide access to a discounted skill.

AI RULE

When evaluating a training with a Hint, consider both:

Immediate training value
+
Bond gain
+
Potential skill discount

SOURCE: "G2"

---

## 06. MOTIVATION

### 06.01 MOTIVATION_EFFECT

FACT / SOURCE MODEL

Guide 2 treats Motivation as a multiplier on training stat gain.

The source's practical discussion uses approximately "1.16" as the multiplier associated with a one-step Motivation increase under its assumed conditions.

IMPORTANT

- Exact training results also depend on support-card bonuses and other modifiers.
- Do not use "1.16" as a universal fixed multiplier for every situation.

### 06.02 MOTIVATION_TRADEOFF

Raising Motivation may require spending a training turn on an outing/date.

The decision therefore compares:

Expected future training gain
vs.
Cost of the turn used to raise Motivation

### 06.03 UPCOMING_MOTIVATION_EVENTS

Guide 2 identifies several scheduled events that can raise Motivation.

AI RULE

If a guaranteed Motivation event is near, avoid unnecessarily spending a turn to raise Motivation immediately unless the current state requires it.

SOURCE: "G2"

---

## 07. RACING_VS_TRAINING

### 07.01 BASE_RACE_REWARD

Guide 2 states that a winning G1 provides:

- 10 base Stats.
- 45 base Skill Points.

At 35% Race Bonus, the guide describes this as approximately:

- 13 Stats.
- 60 Skill Points.

SOURCE: "G2"

### 07.02 GUIDE_2_RACE_VALUE_MODEL

Guide 2 treats Skill Points as approximately half a stat when comparing race value with training value.

Under that model:

Race| Reward at 35% Race Bonus| Points/Energy| Approx. Training Equivalent
G1| 13 Stat + 60 SP| 2.86| 66
G2/G3| 10 Stat + 47 SP| 2.23| 51
OP| 6 Stat + 47 SP| 1.97| 45

STATUS: "EVALUATION_MODEL"

These values should not be treated as raw game formulas.

### 07.03 RACE_SELECTION

Guide 2's general rule:

- If it is a G1 race day and there is no exceptional Rainbow training, racing can be preferable.
- More Race Bonus increases race value.
- Racing is more valuable when Skill Points are important, such as Stadium-oriented builds.
- Racing is relatively less valuable when optimizing primarily for Champion's Meeting stats.

SOURCE: "G2"

---

## 08. RAINBOW_SELECTION

### 08.01 DECK_CONTEXT

Rainbow frequency depends strongly on deck composition.

Example from Guide 2:

- A deck with many Speed cards produces Speed Rainbows frequently.
- A Power Rainbow can therefore have greater marginal value when it appears.

### 08.02 SINGLE_VS_MULTIPLE_RAINBOWS

When multiple Rainbows are available, compare:

- Number of supports.
- Training type.
- Expected total stats.
- Target stat requirements.
- Energy cost.
- Future training opportunities.

### 08.03 RAINBOW_NOT_ALWAYS_BEST

A Rainbow can be ignored when:

- Another training fixes an important stat deficit.
- The Rainbow causes an unacceptable Energy state.
- Another Rainbow is likely to provide substantially greater value.
- The current training is required to meet a run objective.

SOURCE: "G2"

---

## 09. TRAINING_FAILURE_RISK

### 09.01 GUIDE_2_RULE_OF_THUMB

Guide 2 gives the following heuristic:

If expected stat gain < approximately 2 × failure chance,
consider resting instead.

Example:

Failure chance = 27%
2 × 27 = 54

Training gain:
+35 Speed
+16 Power
= 51 total

51 < 54

The guide therefore recommends resting in this example.

STATUS: "HEURISTIC"

This is not a game mechanic or guaranteed optimal decision.

### 09.02 RISK_TOLERANCE

The source explicitly notes that players can choose to be more or less risk-tolerant.

AI RULE

For run evaluation, record failure risk separately from expected gain rather than automatically rejecting every high-risk training.

---

## 10. STAT_SYSTEM

### 10.01 STAT_CAP

SOURCE SCOPE

Guide 2 states that values above 1200 have reduced effective value in its formulas:

Effective value above 1200 = 50%

Example:

1600 Speed
→ 1200 + (400 × 0.5)
→ 1400 effective

IMPORTANT

The source is version-dependent. Do not apply this blindly if the game version has changed the cap or over-cap rules.

### 10.02 SPEED

Speed:

- Is important for maximum race performance.
- Primarily increases top speed during the Last Spurt according to Guide 2.
- Does not directly increase ordinary opening/middle-leg speed under the source's model.

Guide 2 gives:

BaseSpeed =
20 - ((CourseLength - 2000) / 1000)
× PhaseModifier

FinalLegSpeed =
BaseSpeed
+ sqrt(500 × Speed)
× DistanceAptitude
× 0.002

MaxSpurtSpeed =
(FinalLegSpeed + 0.01 × BaseSpeed) × 1.05
+ sqrt(500 × Speed)
× DistanceAptitude
× 0.002

SOURCE: "G2"

---

## 11. STAMINA

### 11.01 FUNCTION

Stamina determines how much HP a character can effectively use during the race.

Guide 2 states:

- Stamina is necessary up to a point.
- Its marginal value decreases depending on distance and other conditions.
- Lower speed requirements reduce Stamina requirements.
- Leaders receive an 11% Stamina penalty in the source's model.

### 11.02 INSUFFICIENT_STAMINA

If Stamina is insufficient:

- Last Spurt can begin later.
- Speed during the relevant portion can be reduced.
- HP conservation behavior can occur.
- Running out of HP causes rapid deceleration.

SOURCE: "G2"

---

## 12. POWER

### 12.01 ACCELERATION

Power affects acceleration toward top speed.

Guide 2 gives:

BaseAcceleration = 0.0006

Normally.

On uphill:

BaseAcceleration = 0.0004

The source gives:

Acceleration =
BaseAcceleration
× sqrt(500 × Power)
× PhaseModifier
× SurfaceAptitude

### 12.02 POWER_AND_UPHILLS

Power also affects uphill speed penalties.

### 12.03 LANE_CHANGE

Guide 2 gives the lane-change-speed relationship:

Lane Change Speed =
0.02 × (0.3 + 0.001 × Power) m/s

### 12.04 POWER_OVER_1200

Guide 2 states that when Power is above 1200, excess Power can be stored and released during the spurt to increase acceleration.

The source refers to the race-mechanics document for the detailed implementation.

AI RULE

Use this only when the applicable game version supports the described mechanic.

---

## 13. GUTS

### 13.01 HP_CONSUMPTION

Guts reduces HP consumption during the final leg.

Guide 2 states that Guts is less valuable point-for-point than Stamina for this purpose.

### 13.02 MINIMUM_SPEED

Guts also increases minimum speed.

The source describes this as most relevant in niche situations such as a Leader without Runners ahead.

### 13.03 LAST_SPURT_SPEED

Guide 2 gives:

Last Spurt Guts Speed =
(450 × Guts)^0.597 × 0.0001 m/s

Guts also affects speed during position competition.

---

## 14. WISDOM

### 14.01 SKILL_ACTIVATION

Guide 2 states that Wisdom affects skill activation chance.

Example values:

Wisdom| Skill Proc
200| 55%
300| 70%
400| 77.5%
500| 82%
600| 85%
700| 87%

### 14.02 KAKARI

Wisdom also affects the chance of entering Kakari.

Guide 2 gives:

Wisdom| Kakari Chance
200| 24.17%
300| 19.00%
400| 16.24%
500| 14.49%
600| 13.26%
700| 12.32%

When Kakari occurs:

- It occurs during the first half of the course.
- It lasts up to 12 seconds.
- There is a 55% chance to break free every 3 seconds.
- HP consumption increases by 60%.
- Running behavior becomes more aggressive.

SOURCE: "G2"

### 14.03 DOWNHILL

Wisdom affects the chance of receiving the downhill speed boost.

Guide 2 states:

Chance = 0.04% × Wisdom

Therefore:

100 Wisdom = 4% chance

### 14.04 TARGET_SPEED_RANDOMNESS

The race is divided into 24 sections.

Wisdom influences the random modifier applied to target speed in each section.

Guide 2 gives:

Maximum modifier =
Wisdom / 5500 × log10(Wisdom × 0.1)

The minimum modifier is:

Maximum modifier - 0.65

SOURCE: "G2"

---

## 15. STAMINA_VS_GUTS

Guide 2 identifies a distance-dependent Guts threshold.

Below the threshold:

- Guts is more valuable than Stamina point-for-point in the described comparison.

Above the threshold:

- Guts becomes less valuable than Stamina.

THRESHOLDS

Distance| Target Guts
Short| 210
Mile| 260
Dirt| 260
Mid| 320
Long 3000m| 380
Long 3600m| 440

SOURCE: "G2"

### 15.01 MARGINAL_VALUE

The source gives the following approximate relationships:

ABOVE_THRESHOLD

50 Guts above the threshold:

- approximately 43–46 Stamina equivalent.

The next 50:

- approximately 33–37 Stamina equivalent.

The next 50:

- approximately 30–31 Stamina equivalent.

BELOW_THRESHOLD

50 Guts below the threshold:

- approximately 55–62 Stamina equivalent.

100 below:

- approximately 66–83 equivalent.

150 below:

- approximately 82–106 equivalent.

STATUS

These are source-derived comparative values, not direct game-stat conversions.

---

## 16. HP_CALCULATION

Guide 2 gives:

HP =
Track Distance
+
(Stamina × 0.8 × Strategy Modifier)

Strategy modifiers given by the source:

Strategy| Modifier
Runner| 0.95
Leader| 0.89
Betweener| 1.00
Chaser| 0.995

### 16.01 GUTS_HP_EFFECT

The source gives the Guts HP-consumption multiplier as:

HP Consumption Multiplier =
1 + (200 / sqrt(600 × Guts))

Higher Guts therefore lowers HP consumption through this multiplier.

### 16.02 BASE_HP_CONSUMPTION

Guide 2 gives:

Base HP Consumption Rate =
20 × (CurrentSpeed - BaseSpeed + 12)^2 / 144

Track condition also modifies HP consumption.

SOURCE: "G2"

---

## 17. SUPPORT_CARD_PASSIVES

### 17.01 SPECIALTY_RATE

Specialty Rate increases the probability that a support card appears on its preferred training.

Guide 2 describes the underlying appearance weights as:

- Each stat training starts with a weight of 100.
- Not appearing has a weight of 50.
- Specialty Rate adds to the preferred-training weight.
- Certain unique effects can multiply the resulting specialty rate.

Example given by the source:

Base preferred weight = 100
Specialty = +80

100 + 80 = 180

If a unique effect multiplies specialty by 1.2:

180 × 1.2 = 216

The source's example then calculates the final appearance rate from the total weights.

SOURCE: "G2"

### 17.02 STAT_BONUS

A "<Stat> Bonus":

- Adds to the amount of that stat produced by the training.
- Applies before the other training modifiers.

A Power Bonus on a Speed support, for example, increases the Power obtained during Speed training.

### 17.03 INITIAL_STAT_UP

Initial "<Stat> Up" adds that amount to the corresponding stat during training.

It can be particularly useful for cards that appear in small numbers in a deck.

### 17.04 HINT_RATE

Hint Rate Up:

- Increases the chance of a support's Hint appearing.
- Hints provide Bond.
- Hints can therefore accelerate Rainbow activation.
- Hints also provide skill discounts.

### 17.05 HINT_LEVEL

Hint Level Bonus increases the skill discount obtained from a Hint.

### 17.06 WISDOM_TRAINING_RECOVERY

Wisdom Training Recovery Up:

- Is found on Wisdom cards.
- Increases Energy restored by Rainbow Wisdom training.
- Guide 2 states that an MLB value is commonly around 4–5 Energy.

### 17.07 RACE_BONUS

Race Bonus increases Stats and Skill Points obtained from races.

Guide 2 states that this includes:

- Optional races.
- Mandatory races.
- Finals.

It also affects certain mandatory/stat rewards according to scenario.

### 17.08 FAN_COUNT_BONUS

Fan Count Bonus increases Fans obtained from races.

---

## 18. FRIEND_CARD_PASSIVES

### 18.01 STACKING

Multiple Friend cards cannot appear on the same training.

Therefore their corresponding Friend-card training effects cannot stack on the same training.

### 18.02 FAILURE_RATE_DOWN

Failure Rate Down reduces the probability of a failed training.

Guide 2's example:

35% Failure Rate Down
9% fail chance → 6%

### 18.03 ENERGY_DISCOUNT

Energy Discount reduces the Energy cost of the training the Friend card is on.

Example from Guide 2:

Level 5 Speed training = 25 Energy

20% discount:
25 × 0.8 = 20 Energy

### 18.04 EVENT_RECOVERY

Event Recovery Amount Up increases Energy obtained from support-card events, particularly dates.

### 18.05 EVENT_EFFECT

Event Effect Up increases other event rewards such as Skill Points.

---

## 19. AGEMASEN

### 19.01 DEFINITION

Some support-card event chains have a chance to provide the Gold skill or its lower-rarity version.

When the Gold skill is not provided, Guide 2 calls this:

"Agemasen"

### 19.02 STAT_DEPENDENCY

Guide 2 states that the probability depends on the relevant stat associated with the support card.

Example:

- Fine Motion's check uses Wisdom.

GOLD_SKILL_CHANCE

Relevant Stat| Gold Skill Chance
<400| 30%
400+| 60%
600+| 65%
700+| 75%
800+| 80%
1000+| 90%

SOURCE: "G2"

---

## 20. RACE_BONUS

### 20.01 GENERAL

Race Bonus increases the Stats and Skill Points obtained from race completion.

It applies to:

- Optional races.
- Mandatory races.
- Finals.

### 20.02 MANT_CONTEXT

Guide 2 states:

- Maximum Race Bonus on an individual support card in the source context is 15%.
- The stated maximum deck total is 90%.

For MANT, the source identifies 50% Race Bonus as an important target because:

- Every 10% provides another +1 from G1/final rewards.
- Every 12.5% provides another +1 from G2/G3 rewards.
- 50% aligns the relevant breakpoints.

### 20.03 HAMMER_INTERACTION

Golden Hammers multiply Race Bonus for the affected races.

Guide 2 gives:

Effective Race Bonus =
Race Bonus × 1.35

Example:

50% × 1.35 = 67.5%

The source describes this as approximately 102% effective Race Bonus under its displayed percentage representation.

### 20.04 URA_AOHARU

Guide 2 states:

- Objective reward of +3 all Stats increases to +4 at 34% Race Bonus.
- It increases to +5 at 67% Race Bonus.
- The source recommends at least 34% Race Bonus for URA/Aoharu builds.

STATUS: scenario-specific source recommendation.

---

## 21. TRAINING_STAT_GAIN

Guide 2 gives the following training-output structure:

Training Result =
(BaseValue + Sum of StatBonus)
× (1 + MotivationMultiplier × Sum of MotivationBonus)
× Sum of TrainingBonus
× Product of FriendshipBonus
× (1 + 0.05 × NumberOfSupportCards)

### 21.01 CONDITIONS

Friendship Bonus:

- Applies when the support has Orange-or-higher Bond.
- Applies when the support is on a training matching its type.

Stat Bonus:

- Applies only when the training normally gives that stat.

### 21.02 MOTIVATION_MULTIPLIER

Guide 2 states:

- Neutral Motivation has a Motivation Multiplier of 0.
- Each Motivation step changes the multiplier by 0.1.

SOURCE: "G2"

---

## 22. SKILLS

### 22.01 STRATEGY_AND_DISTANCE_REQUIREMENTS

Skills can have:

- Running-style requirements.
- Distance requirements.
- Other conditions.

A skill that does not match the Uma's applicable strategy/distance may provide no benefit.

AI RULE

Before evaluating a skill:

1. Check running-style condition.
2. Check distance condition.
3. Check surface condition if present.
4. Check race-phase condition.
5. Check remaining conditions.

### 22.02 SKILL_CONDITIONS

Guide 2 describes skill conditions using logical operators:

- "&" = AND.
- "@" = OR.

Operator order:

& is evaluated before @

Example structure:

A & B @ C

means:

(A AND B) OR C

SOURCE: "G2"

---

## 23. TRAINING_DECISION_MODEL

For AI run evaluation, Guide 2 supports comparing a training against alternatives using:

Immediate Stat Gain
+ Skill/Hints
+ Bond Gain
+ Training-Level Progress
+ Energy Effect
+ Motivation Effect
+ Future Rainbow Potential
+ Race Value
+ Objective Requirements

A training should not be judged solely by its displayed stat total.

### 23.01 EARLY_GAME_PRIORITY

Early run:

Bond
→ Training Level
→ Rainbow Access
→ Core Stat Development

### 23.02 MID_GAME_PRIORITY

Middle run:

Strong Rainbow
→ Required Stat Correction
→ Race Value
→ Energy/Motivation Management

### 23.03 LATE_GAME_PRIORITY

Late run:

High-value Rainbow
→ Required Stat Thresholds
→ Race/Skill Point Value
→ Final Stat Optimization

STATUS

This section is a structured interpretation of Guide 2's training discussion, not a quoted formula.

---

## 24. RACE_VS_TRAINING_AI_RULE

When deciding between a race and training, evaluate:

Race Value =
Stat Rewards
+ Skill Point Value
+ Race Bonus
+ Fan/Objectives
+ Rival/Skill Benefits

versus:

Training Value =
Immediate Stats
+ Bond
+ Rainbow Value
+ Training Level
+ Energy/Recovery
+ Future Value

Guide 2 gives these approximate baseline thresholds:

- Around 43 base Stats to beat a G2/G3.
- Around 70 base Stats to beat a G1.

These thresholds are source

> **NOTE — FILE ENDS HERE.** The last sentence was cut off when the file was saved.
