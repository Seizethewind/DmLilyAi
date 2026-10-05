# UMAMUSUME AI REFERENCE — G1

«Source module: Guide 1 — UmaMusu Support Card Evaluation Doc
Source author: celery6305
Primary purpose: support-card evaluation methodology and card-property reference.

This module is an extension of "CommunityGuide_AI_updated.md".

Source scope: Guide 1 evaluates support cards primarily for stat gain and PvP usefulness using a simulation model based on JP scenario/meta parameters. Its rankings are evaluations, not universal game facts.»

> **NOTE — INCOMPLETE FILE:** this module stops partway through the Stamina cards (section 13.03). The remaining Stamina, Power, Guts, Wisdom, non-MLB and Group/Friend card entries were never saved. Do not assume a card is missing from the game because it is missing here.

---

## 01. SOURCE_SCOPE

### DOCUMENT_PURPOSE

FACT

- Guide 1 contains support-card evaluation results produced using a support-card rating tool.
- The stated purpose is to estimate how support cards rank in terms of stats gained.
- The evaluation uses simulations.
- Evaluation parameters are adjusted toward the current JP meta scenario.

SOURCE: "G1"

### CURRENT_SCENARIO_CONTEXT

META

- Guide 1 identifies its current scenario parameters as "General (YHS)".
- The evaluation is intended for the current JP environment represented by the guide.

SOURCE: "G1"

### MLB_SCOPE

FACT

- Cards in the main evaluation sections are evaluated at MLB.
- Non-MLB evaluations are handled separately in the referenced spreadsheet.

SOURCE: "G1"

### GLOBAL_TIME_SCOPE

LIMITATION

- The source states that its current JP scenario parameters can make historical Global evaluations inaccurate.
- A release-date filter exists in the spreadsheet, but the source warns that it does not accurately reproduce historical Global conditions because current JP scenario parameters are still used.

SOURCE: "G1"

---

## 02. SUPPORT_CARD_VALUE_MODEL

### 02.01 MAIN_TRAINING_VALUE

RELATION

Guide 1 identifies the main contributors to a support card's ability to raise its primary training stat as:

- Friendship Bonus.
- Flat Stat Bonuses.
- Specialty Rate.
- Initial Bond.

SOURCE: "G1"

### 02.02 CROSS_TRAINING_VALUE

RELATION

Cross-training value describes the benefit a support card provides when it appears in trainings outside its primary training type.

The main contributors identified by Guide 1 are:

- Training Bonus.
- Motivation Bonus.

SOURCE: "G1"

### 02.03 OTHER_STAT_VALUE

RELATION

Guide 1 also identifies the following as important contributors to total stat value:

- Race Bonus.
- Event Stats.

SOURCE: "G1"

### 02.04 SUPPORT_CARD_VALUE_SUMMARY

MODEL

A support card's evaluated value can be represented conceptually as:

Support Card Value =
    Main Training Contribution
  + Cross Training Contribution
  + Race Contribution
  + Event Contribution
  + Skill-related practical value

IMPORTANT

- This is a structural summary of the source methodology.
- It is not presented by Guide 1 as a single in-game formula.

---

## 03. SUPPORT_CARD_SIMULATION

### 03.01 GENERAL_METHOD

EVALUATION

Guide 1 evaluates cards by simulating possible combinations of training situations.

For each possible situation:

1. Determine which support cards are present on each training.
2. Determine the probability of that configuration.
3. Use configured stat weights to determine the preferred training.
4. Calculate the result of the selected training.
5. Multiply the result by the probability of the configuration.
6. Repeat across possible configurations.
7. Aggregate the results.

SOURCE: "G1"

### 03.02 TRAINING_PHASES

FACT

- The simulation uses 6 training phases.
- The phases range from an early bonding phase to the late game.
- Each phase uses its own number of simulated turns.

SOURCE: "G1"

### 03.03 TRAINING_SELECTION

EVALUATION

The simulation does not simply total every possible training.

It:

- evaluates the available training situations,
- selects the training considered best according to the configured stat weights,
- keeps the result of that selected training,
- discards the results of the other available trainings.

SOURCE: "G1"

### 03.04 EXAMPLE_CONFIGURATION

SOURCE_EXAMPLE

A simulated situation can include:

- A Speed support card rainbowing on Speed.
- One support card absent.
- Four other support cards on Wisdom.

The model may determine Wisdom to be the best training for that configuration based on its stat weights.

The resulting Wisdom training is then weighted by the probability of that configuration.

SOURCE: "G1"

---

## 04. ENERGY_AND_TURNS_IN_G1_MODEL

### 04.01 ENERGY

EVALUATION

- Energy/failure rate is not directly simulated.
- A certain number of turns are reserved for:
  - Resting.
  - Dating.
  - Objectives.

SOURCE: "G1"

### 04.02 ENERGY_GAIN

RELATION

- Total Energy gained from training and events is added to the simulation result.
- Energy therefore affects the evaluation score indirectly.

SOURCE: "G1"

### 04.03 INITIAL_BOND

RELATION

- Initial Bond affects the probability of reaching rainbow/friendship training.
- Guide 1 specifically states that this effect applies somewhat during phases 2–3.

SOURCE: "G1"

---

## 05. RACE_AND_EVENT_CONTRIBUTION

### 05.01 RACE_STATS

FACT

- Stats obtained from races contribute to the total simulation score.

SOURCE: "G1"

### 05.02 EVENT_STATS

FACT

- Stats obtained from events contribute to the total simulation score.

SOURCE: "G1"

### 05.03 RACE_BONUS

RELATION

- Race Bonus affects race-derived stat contribution.
- Guide 1 includes Race Bonus as a contributor to support-card value.

SOURCE: "G1"

### 05.04 RACE_BONUS_BREAKPOINT

VALUE / EVALUATION

- Guide 1 identifies "34% Race Bonus" as an important breakpoint in its evaluation context.
- The source states that reaching the breakpoint can produce a sufficiently large effect to materially change practical card choice.
- The ranking system deliberately avoids directly evaluating Race Bonus breakpoints because doing so would skew card rankings.

SOURCE: "G1"

AI_RULE

- Do not treat "34%" as a universal support-card score.
- Treat it as a breakpoint identified by Guide 1's evaluation context.

---

## 06. SUPPORT_CARD_BONUSES

### 06.01 BONUS_PRIORITY_IN_G1_MODEL

EVALUATION

Guide 1 gives the following approximate order for bonuses that increase stat output, normalized according to quantities the game considers equivalent:

1. Flat Stat Bonuses.
2. Training Bonus / Motivation Bonus.
3. Friendship Bonus.
4. Specialty Rate.
5. Race Bonus.
6. Other bonuses such as Initial Stats.

SOURCE: "G1"

IMPORTANT

This is an evaluation-model ordering, not a universal mechanical priority.

---

### 06.02 FLAT_STAT_BONUS

EVALUATION

Guide 1 identifies Flat Stat Bonuses as the highest-value bonus category in its normalized evaluation.

Specific observations:

- Speed bonuses are especially valuable on Speed cards.
- Speed bonuses can contribute across 3 training categories.
- Skill Point bonuses are highly valuable.
- Offset-stat bonuses also contribute useful value.

SOURCE: "G1"

---

### 06.03 TRAINING_BONUS

RELATION

- Training Bonus contributes to training output.
- Guide 1 places Training Bonus among the highest-value cross-training contributors.

SOURCE: "G1"

---

### 06.04 MOTIVATION_BONUS

EVALUATION

Guide 1 states that:

Motivation Bonus / 5
≈ Training Bonus equivalent

within its normalized evaluation model.

IMPORTANT

- This relationship belongs to Guide 1's evaluation methodology.
- It should not be treated as an independent universal game formula.

SOURCE: "G1"

---

### 06.05 FRIENDSHIP_BONUS

RELATION

- Friendship Bonus increases the value of friendship/rainbow training.
- Its practical value depends on how often the card reaches friendship/rainbow training.

SOURCE: "G1"

---

### 06.06 SPECIALTY_RATE

RELATION

- Specialty Rate affects the probability of the support card appearing in its specialty training.

EVALUATION

Guide 1 states:

- Initial Specialty Rate around "35" has meaningful value.
- Additional Specialty Rate above approximately "50" has diminishing importance in its evaluation.

SOURCE: "G1"

IMPORTANT

The diminishing-value observation is an evaluation result, not a universal mathematical cutoff.

---

### 06.07 INITIAL_BOND

RELATION

- Initial Bond affects the speed at which a card can reach friendship/rainbow training.
- Its effect is particularly relevant to early-run bonding and later rainbow probability.

SOURCE: "G1"

---

### 06.08 RACE_BONUS

RELATION

- Race Bonus increases the value obtained from race rewards.
- Race Bonus can create threshold effects that are not represented normally in the Guide 1 card rankings.

SOURCE: "G1"

---

### 06.09 EVENT_STATS

RELATION

- Event-provided Stats contribute to total card value in the simulation.

SOURCE: "G1"

---

## 07. SKILL_POINT_VALUE

### 07.01 SKILL_POINTS

EVALUATION

Guide 1 treats Skill Point gains as particularly valuable for PvP build construction.

The source identifies Skill Point bonuses as an important contributor to practical card value.

SOURCE: "G1"

### 07.02 HINT_DISCOUNTS

RELATION

- Skill hints can reduce the Skill Point cost of skills.
- If a discounted skill would otherwise be purchased, the discount can function as an effective Skill Point saving.

SOURCE: "G1"

### 07.03 CARD_SCORE_VS_SKILLS

EVALUATION

Guide 1 states that cards within approximately "20–40" score should often be considered practically similar within its evaluation framework.

When scores are close:

- Skill availability can become the deciding factor.
- Useful skill hints can increase practical value beyond the raw score.

IMPORTANT

- "20–40" is a Guide 1 evaluation guideline.
- It is not an in-game threshold.

SOURCE: "G1"

---

## 08. SCENARIO_SIMULATION_LIMITATIONS

### 08.01 GENERAL_SCENARIO_MODEL

LIMITATION

Guide 1 states that it moved away from attempting to accurately simulate every detail of each scenario.

The model instead aims to provide a more general evaluation.

SOURCE: "G1"

### 08.02 SCENARIO_PARAMETERS

FACT

The evaluation can still adjust parameters for:

- Race stats.
- Scenario stat bonuses.
- Current meta decks.
- Other scenario-related conditions.

SOURCE: "G1"

### 08.03 REASON_FOR_GENERALIZED_MODEL

SOURCE_CONTEXT

- Scenarios change regularly.
- Guide 1 prioritizes a more reusable evaluation model instead of rebuilding a highly detailed scenario simulation every time.

STATUS

- Methodology explanation; not gameplay mechanic.

### 08.04 EFFECT_ON_CARD_EVALUATION

LIMITATION

Because scenario mechanics are not fully simulated:

- Cards with unusually strong scenario-specific effects may not receive their complete practical value.
- Future scenarios with stronger scenario-linked effects may produce evaluation differences not captured by the model.

SOURCE: "G1"

---

## 09. COMPARISON_DECK_ASSUMPTION

### 09.01 FIXED_COMPANION_CARDS

CONDITION

When comparing one support card against another:

- The target card is simulated together with 5 other support cards.
- Those 5 cards remain constant during the comparison.
- The companion cards are selected as reasonable choices based on meta decks.

SOURCE: "G1"

### 09.02 EFFECT_ON_WEAKER_CARDS

LIMITATION

- Weaker or low-LB cards can be evaluated less accurately.
- Their score assumes they are being used alongside 5 strong cards.

AI_RULE

- Do not interpret a low score from this model as an absolute measurement of the card's isolated strength.

SOURCE: "G1"

---

## 10. GROUP_AND_FRIEND_CARDS

### 10.01 EVALUATION_EXCLUSION

FACT

- Group/Friend cards are generally not included in the normal evaluation.

REASON

Guide 1 states that:

- Their mechanics can be complicated.
- Their mechanics can be strongly tied to individual scenarios.
- Scenario-linked Group/Friend cards are commonly intended for use in their respective scenarios.

SOURCE: "G1"

### 10.02 FRIEND_LIKE_CARDS

FACT

- Friend-like cards can also be difficult to compare directly with ordinary support cards.
- Some are therefore absent from the main evaluation images.

AI_RULE

- Absence from the ranking does not mean the card has no value.

---

## 11. CARD_DATA_EXTRACTION_RULE

When extracting an individual support card into the AI knowledge base, preserve objective properties where available:

CORE_PROPERTIES

- Card name.
- Support type.
- Limit Break state used by the source.
- Flat Stat Bonuses.
- Training Bonus.
- Motivation Bonus.
- Friendship Bonus.
- Specialty Rate.
- Initial Bond.
- Race Bonus.
- Skill Point Bonus.
- Event effects.
- Unique-effect conditions.
- Skill hints.
- Gold skills.
- Strategy restrictions.
- Distance restrictions.
- Surface restrictions.
- Scenario restrictions.
- Evaluation assumptions.

DO_NOT_PROMOTE_TO_FACT

Do not automatically treat these source statements as universal facts:

- Best.
- Worst.
- Staple.
- Mandatory.
- Weak.
- Amazing.
- Overrated.
- Underrated.
- Meta.
- Better in practice.
- Worse in practice.

These are evaluation/meta statements unless the mechanical condition behind them is separately recorded.

---

## 12. SPEED_SUPPORT_CARDS

### 12.01 CATEGORY_CONTEXT

EVALUATION

Guide 1 provides a Speed-card ranking based on its simulation model.

Individual ranking positions are not permanent facts because they depend on:

- Scenario.
- Stat weights.
- Deck assumptions.
- Skill value.
- Current meta.

SOURCE: "G1"

### 12.02 CARD_PROPERTIES_FROM_GUIDE1

#### TOKAI_TEIO

SOURCE_DATA

- Speed support card.
- Leader-specific.
- Provides a leader early-speed skill.
- Provides a choice involving a final-leg skill or mid-distance acceleration skill for leaders.

SOURCE: "G1"

#### ALMOND_EYE

SOURCE_DATA

- Speed support card.
- Broad-use Speed card according to Guide 1.
- Provides a choice of two Gold skills from four.
- Skill choices include mid-distance leader skills and universal Speed skills.

SOURCE: "G1"

#### ADMIRE_GROOVE

SOURCE_DATA

- Speed support card.
- Mid-distance Betweener specialization.
- Provides a Betweener acceleration Gold skill.
- Provides another general-use Betweener Gold skill.

SOURCE: "G1"

#### STILL_IN_LOVE

SOURCE_DATA

- Speed support card.
- Provides a strong mid-distance Gold skill.
- Provides another Gold skill oriented toward Betweener/Chaser use.
- Skill Point gain is a significant part of its value in Guide 1's evaluation.

EVALUATION

- Guide 1 considers its practical value somewhat higher than similarly scored cards because of Skill Point gain.

SOURCE: "G1"

#### RHEIN_KRAFT

SOURCE_DATA

- Speed support card.
- Mile specialization.
- Frontliner-oriented.
- Provides two frontline-specific Mile Gold skills.
- One is the acceleration skill "High Voltage".

SOURCE: "G1"

#### DREAM_JOURNEY

SOURCE_DATA

- Speed support card.
- Chaser specialization.
- Provides two Chaser Gold skills.
- Intended for Chaser training.

SOURCE: "G1"

#### NARITA_BRIAN

SOURCE_DATA

- Speed support card.
- Leader-specific skill set.
- Provides the long-distance Leader Gold acceleration skill "Monster".
- Provides a Leader mid-leg skill that consumes Stamina.

SOURCE: "G1"

#### SMART_FALCON

SOURCE_DATA

- Speed support card.
- Runner specialization.
- Provides an opening-leg acceleration Gold skill for Runners.
- Provides multiple Runner skill hints.

SOURCE: "G1"

#### VIVLOS

SOURCE_DATA

- Speed support card.
- Provides a Gold version of "Hold Your Tail High".
- Guide 1 identifies high stat bonuses as a major part of its value.

SOURCE: "G1"

#### SEEKING_THE_PEARL

SOURCE_DATA

- Speed support card.
- Short-distance backline specialization.

SOURCE: "G1"

#### EL_CONDOR_PASA_SPEED

SOURCE_DATA

- Speed support card.
- Provides a unique effect involving an all-stat bonus at maximum Bond.
- Provides Skill Point bonuses.
- Provides the universal Gold skill "Arcline Professor".
- Also provides a Leader/Betweener acceleration Gold skill for some tracks.

SOURCE: "G1"

#### JUNGLE_POCKET

SOURCE_DATA

- Speed support card.
- Provides high stat bonuses.
- Provides Race Bonus and Skill Point Bonus.
- Unique effect provides an additional Speed bonus at maximum Bond.
- Provides mid/long/backline skills.

SOURCE: "G1"

#### DURAMENTE_SPEED

SOURCE_DATA

- Speed support card.
- Very high Specialty Rate according to Guide 1.
- Provides strong cross-training bonuses.
- Provides the Gold skill "Never Give Up".
- "Never Give Up" is described by the source as general-use across strategies and distances.

SOURCE: "G1"

#### SAKURA_BAKUSHIN_O_SPEED

SOURCE_DATA

- Speed support card.
- Short-distance specialization.
- Provides up to +3 Speed Bonus according to Guide 1.
- Has lower cross-training bonuses than Maruzensky according to the source comparison.

SOURCE: "G1"

#### MARUZENSKY_SPEED

SOURCE_DATA

- Speed support card.
- Provides a unique Training Bonus effect based on training level.
- The source describes the effect as 5% Training Bonus per training level.
- Provides Runner skill hints.
- Provides the Gold skill "Top Runner".

SOURCE: "G1"

#### MEJIRO_DOBER_SPEED

SOURCE_DATA

- Speed support card.
- Mile backline specialization.
- Guide 1 describes its value as frontloaded.

SOURCE: "G1"

#### MEJIRO_PALMER_SPEED

CONDITION

- Its unique effect depends on purchasing 3 recovery skills.

SOURCE_DATA

- Speed support card.
- High Specialty Rate.
- Provides long-distance/Runner skills.
- Provides Race Bonus and Skill Point Bonus.

LIMITATION

- Guide 1 explicitly states that purchasing 3 recoveries early is not always realistic.
- Therefore the evaluation of the unique effect depends on an assumption that may not hold in every build.

SOURCE: "G1"

#### MARVELOUS_SUNDAY_SPEED

SOURCE_DATA

- Speed support card.
- Provides Training Bonus at maximum Bond.
- Provides Speed, Power, and Skill Point bonuses.
- Provides a Gold recovery skill.

SOURCE: "G1"

#### EISHIN_FLASH_SPEED

SOURCE_DATA

- Speed support card.
- Provides Speed and Power bonuses.
- Provides Skill Point Bonus.
- Has no Race Bonus according to Guide 1.
- Provides Betweener skills.

SOURCE: "G1"

#### KITASAN_BLACK_SPEED

SOURCE_DATA

- Speed support card.
- Provides consistent friendship/rainbow value according to Guide 1.
- Provides universal skills including "Arcline Professor".

EVALUATION

- Guide 1 describes the card as historically common/staple and still useful for newer players.

SOURCE: "G1"

#### TAIKI_SHUTTLE_SPEED

SOURCE_DATA

- Speed support card.
- Provides Speed and Power bonuses.
- Provides Skill Point Bonus.
- Provides Training Bonus.
- Provides Race Bonus.
- Provides Mile-related skills including "Ruler of Mile".

SOURCE: "G1"

---

## 13. STAMINA_SUPPORT_CARDS

### 13.01 CATEGORY_CONTEXT

EVALUATION

Guide 1 states that Stamina-card ranking depends strongly on target distance.

General source relationship:

- Long-distance builds place greater value on direct Stamina gain.
- Shorter-distance builds can place relatively greater value on cross-training bonuses from Stamina cards.

SOURCE: "G1"

### 13.02 SPECIAL_ASSUMPTIONS

Some Stamina-card evaluations include explicit assumptions.

Examples:

- Mayano: 0 starting Bond.
- Palmer: assumed 15% Training Bonus.
- Laurel: assumed early purchase of 3 recoveries.
- Ikuno: 0 Specialty Rate.

AI_RULE

These assumptions must not be converted into general card properties.

SOURCE: "G1"

### 13.03 CARD_PROPERTIES

#### FENOMENO

- Stamina support card.
- Long-distance Leader orientation.
- Provides a long-distance random acceleration Gold skill for Leaders.
- Provides a late/mid-leg Gold skill.

#### INARI_ONE

- Stamina support card.
- Long-distance Betweener orientation.
- Provides long-distance Betweener acceleration Gold skill.
- Provides a mid-leg Gold skill.

#### GOLD_SHIP_STAMINA

- Stamina support card.
- Long-distance Chaser orientation.
- Provides "Imminent Shadow".
- Provides a Gold recovery for Chasers.

#### AIR_SHakur

- Stamina support card.
- Provides a strong overall stat line according to Guide 1.
- Provides a universal recovery + Speed skill or a final-leg current-Speed skill.
- The final-leg skill has a condition related to not being at the front of the pack.

#### MEJIRO_RYAN_STAMINA

- Stamina support card.
- Mid-distance Betweener specialization.
- Provides a mid-distance Betweener mid-leg Gold skill from the first chain event.
- Guide 1 notes strong low-LB performance.

#### SOUNDS_OF_EARTH

- Stamina support card.
- Provides strong cross-training.
- Provides Stamina gain.
- Provides high Skill Point gain.
- Provides a choice involving a Gold recovery skill or Gold Speed skill.

#### CURREN_BOUQUETDOR

- Stamina support card.
- Leader specialization.
- Provides a Gold recovery skill.

#### DURAMENTE_STAMINA

> **NOTE — FILE ENDS HERE.** The entry above was cut off when the file was saved.
