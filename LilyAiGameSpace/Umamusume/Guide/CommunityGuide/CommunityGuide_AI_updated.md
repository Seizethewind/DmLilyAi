# UMAMUSUME AI KNOWLEDGE BASE

> Unified AI-readable reference derived from Community Guides 1–4.
>
> Purpose: provide compact, structured knowledge for AI reference, run evaluation, and decision support.
>
> Human-oriented prose, jokes, personal preference, duplicated explanations, and unsupported rankings are excluded. Claims retain scope and uncertainty where required.

---

## 00. DOCUMENT_RULES

### KNOWLEDGE_STATUS

- `FACT` — Direct game/mechanical statement supported by source material.
- `VALUE` — Numeric value, threshold, modifier, duration, cost, or probability.
- `FORMULA` — Calculation or mechanical relationship stated by the source.
- `CONDITION` — Requirement or state under which something applies.
- `RELATION` — Relationship between mechanics.
- `EVALUATION` — Simulation, measurement, testing, or comparison result.
- `STRATEGY` — Conditional decision guidance; not a universal fact.
- `META` — Scenario/event/server/time-dependent information.
- `UNVERIFIED` — Source claim not established sufficiently to treat as confirmed.

### AI_USAGE_RULES

- Treat verified `FACT`, `VALUE`, `FORMULA`, `CONDITION`, and `RELATION` as core reference knowledge.
- Do not treat `EVALUATION`, `STRATEGY`, or `META` as universal facts.
- Preserve conditions and scope attached to every evaluation or recommendation.
- Do not convert personal preference into factual knowledge.
- Do not infer missing information.
- Preserve reverse-engineered status for mechanics sourced from Guide 3.
- Use one canonical entry for a concept instead of repeating four source explanations.

---

## 01. CORE_GAME_CONCEPTS

### TERMINOLOGY

**FACT**

- Core stats: Speed, Stamina, Power, Guts, Wisdom.
- Energy is the training-run resource represented by 体力.
- Motivation is the training-run state represented by やる気.
- Turf = 芝.
- Dirt = ダート.
- Short distance = 1000–1400m.
- Mile distance = 1500–1800m.
- Medium/Mid distance = 1900–2400m.
- Long distance = 2500–3600m.
- Runner = 逃げ.
- Leader = 先行.
- Betweener = 差し.
- Chaser = 追込.
- Oonige = 大逃げ.
- Friendship/rainbow training = training with the friendship/rainbow effect active.
- Bond = support-card bond gauge.
- Hint = the `!` indicator associated with skill hints.
- CM = Champions Meeting.
- LB = Limit Break.
- MLB = Max Limit Break / 4LB.

**SOURCE**
- Guide 2 terminology/reference material.

### BASIC_ACTIONS

**FACT**

- Resting raises Energy.
- Dating raises Motivation.
- Racing raises Fans.
- Training raises Stats.

**SOURCE**
- Guide 2.

---

## 02. TRAINING

### TRAINING_MECHANICS

**FACT**

- Training is the primary action for increasing stats during a training run.
- Training results depend on the selected training, support presence/effects, and current run state.
- Friendship/rainbow training is a distinct high-value training state used by the support-card evaluation methodology.

### EVENT_SELECTION

**FACT**

- Event choices can provide Stats, Energy, Motivation, and skill hints.

**STRATEGY**

- Guide 2 recommends considering stats that are not normally trained when selecting event rewards while also considering Energy, Motivation, and useful skill hints.

**STATUS**
- Conditional strategy, not universal rule.

### TRAINING_EVALUATION_METHOD

**EVALUATION**

- Guide 1 estimates expected stat contribution across possible training configurations.
- Training situations are weighted by their probability of occurring.
- The simulation selects the best training for each simulated state using its configured stat weights.
- The model divides training into six phases from early bonding through late game.
- Energy/failure rate is not directly simulated; turns are reserved for rest, dating, and objectives, while Energy gained from training/events contributes to the score.

**SCOPE**
- Guide 1's methodology targets JP PvP evaluation and can become outdated as scenarios/meta change.
- This is an evaluation model, not a universal game formula.

---

## 03. STATS

### STAT_TYPES

**FACT**

- Core training stats are Speed, Stamina, Power, Guts, and Wisdom.

### STAT_EVALUATION

**EVALUATION**

- Guide 1 uses configured stat weights to determine which training is preferred in simulated states.
- Those weights are evaluation-model parameters, not universal game values.

### STAMINA_AND_HP

**FACT**

- Stamina is converted to HP at race start.
- HP consumption depends on race state and modifiers.
- During the late-race/last-spurt portion, HP consumption uses a Guts-related modifier.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

---

## 04. ENERGY_AND_RECOVERY

### ENERGY_MECHANICS

**FACT**

- Energy is consumed by training.
- Resting raises Energy.
- Events and other actions can change Energy.

### TRAINING_SIMULATION_ENERGY

**EVALUATION**

- Guide 1 reserves turns for resting, dating, and objectives rather than directly simulating every Energy/failure outcome.
- Energy gained from training/events contributes to its evaluation score.

### HP_RECOVERY

**FACT**

- Recovery skills restore a percentage of maximum HP.
- HP restored above maximum is wasted.
- Recovery follows the skill's trigger and recovery conditions.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

---

## 05. MOTIVATION

### MOTIVATION_STATE

**FACT**

- Motivation is a training-run state.
- Dating can raise Motivation.

### MOTIVATION_BONUS

**EVALUATION**

- Guide 1 treats Motivation Bonus as a contributor to cross-training value.
- Guide 1's normalized model treats Motivation Bonus divided by 5 as approximately comparable to Training Bonus.

**STATUS**
- Evaluation-model relationship, not universal game law.

---

## 06. INHERITANCE_AND_FACTORS

### INHERITANCE

**FACT**

- Inheritance transfers inherited effects/factors into a training run.
- Factors are commonly referred to as Sparks in English community terminology.

### FACTOR_SELECTION

**STATUS**
- Detailed probabilities, compatibility calculations, and factor-selection rules must be retained from the source material with their original conditions before being promoted to confirmed rules.

### COMPATIBILITY

**STATUS**
- Requires detailed extraction/verification from Guide 2 before being treated as a canonical formula.

---

## 07. APTITUDES

### APTITUDE_TYPES

**FACT**

- Aptitudes include surface, distance, and strategy categories.
- Aptitude grades include S through G.

### GROUND_TYPE_PROFICIENCY_MODIFIER

**VALUE**

| Grade | Modifier |
|---|---:|
| S | 1.05 |
| A | 1.00 |
| B | 0.90 |
| C | 0.80 |
| D | 0.70 |
| E | 0.50 |
| F | 0.30 |
| G | 0.10 |

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

### DISTANCE_PROFICIENCY_MODIFIER

**VALUE**

| Grade | Modifier |
|---|---:|
| S | 1.00 |
| A | 1.00 |
| B | 1.00 |
| C | 1.00 |
| D | 1.00 |
| E | 1.00 |
| F | 0.60 |
| G | 0.50 |

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

---

## 08. SUPPORT_CARDS

### SUPPORT_CARD_ATTRIBUTES

**FACT**

Guide 1 identifies major contributors to support-card evaluation:

- Friendship Bonus.
- Flat Stat Bonuses.
- Specialty Rate.
- Initial Bond.
- Training Bonus.
- Motivation Bonus.
- Race Bonus.
- Event Stats.

### CROSS_TRAINING

**RELATION**

- Support cards can contribute to trainings outside their main training category when they appear there.
- Training Bonus and Motivation Bonus are important contributors to this cross-training value in Guide 1's evaluation model.

### SUPPORT_CARD_EVALUATION_METHOD

**EVALUATION**

- Expected stat gain is evaluated across possible training configurations.
- Configuration probability is used as a weight.
- Six training phases are evaluated.
- Race and event stat gains can contribute to the total score.
- Initial Bond affects the probability of reaching friendship/rainbow training in later phases.
- Cards are compared beside five fixed companion cards selected as reasonable meta-deck choices.

### MODEL_LIMITATIONS

**CONDITION**

- Scenario mechanics are not fully simulated.
- Scenario parameters are adjusted for the relevant scenario/meta.
- Low-LB cards can be represented less accurately when evaluated beside five strong companion cards.
- Race Bonus breakpoints are not normally represented in the ranking because breakpoints can strongly affect deck choice.

### BONUS_PRIORITY_IN_GUIDE1_MODEL

**EVALUATION**

Guide 1's normalized evaluation model approximately prioritizes:

1. Flat stat bonuses.
2. Training Bonus / Motivation Bonus.
3. Friendship Bonus.
4. Specialty Rate.
5. Race Bonus.
6. Other bonuses such as initial stats.

**STATUS**
- Evaluation-model ordering, not universal game law.

### CARD_RANKINGS

**META / EVALUATION**

- Individual support-card rankings are context-dependent.
- If retained for future use, rankings require scenario, deck context, server/meta, and evaluation-method scope.

---

## 09. SKILLS

### SKILL_ACTIVATION

**FACT**

- Many skills require a Wisdom check before the race to determine activation chance.
- Guide 3 provides example activation chances using base Wisdom: 300 Wisdom = 70.0%, 600 = 85.0%, 900 = 90.0%, 1200 = 92.5%.
- The cited activation calculation uses base Wisdom and is not affected by strategy proficiency or skills.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

### CURRENT_SPEED_AND_ACTUAL_SPEED

**FACT**

- Current Speed is the direct result after acceleration calculations.
- Actual Speed is Current Speed after current-speed modifiers are applied.
- Current-speed modifiers take effect immediately without requiring additional acceleration/deceleration.
- Current Speed is used in subsequent acceleration calculations and HP-consumption calculations.
- Actual Speed is used for distance travelled and relative-speed calculations such as blocking and overtaking.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

### SKILL_DURATION

**FACT**

- Many skills have a base duration.
- Actual skill duration scales with course distance.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

### SKILL_SELECTION

**STRATEGY**

- Skill selection should account for target race, strategy, distance, activation conditions, timing, and available skill effects.
- Skill rankings in community guides are evaluations/meta unless directly supported as mechanical facts.

---

## 10. RACING_SYSTEM

### STRATEGY_COEFFICIENTS

**VALUE**

| Strategy | Coefficient |
|---|---:|
| Front Runner | 0.95 |
| Pace Chaser | 0.89 |
| Late Surger | 1.00 |
| End Closer | 0.995 |
| Oonige | 0.86 |

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

### STRATEGY_PROFICIENCY_MODIFIER

**VALUE**

| Strategy | Early | Middle | Late |
|---|---:|---:|---:|
| Front Runner | 1.000 | 1.000 | 0.996 |
| Pace Chaser | 0.985 | 1.000 | 0.996 |
| Late Surger | 0.975 | 1.000 | 1.000 |
| End Closer | 0.945 | 1.000 | 0.997 |
| Oonige | 1.170 | 0.940 | 0.956 |

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

### START_DASH

**FACT**

- Start dash applies additional acceleration.
- The start-dash state ends when the uma reaches its start-dash speed threshold.
- Guide 3 documents historical bugs involving start-dash acceleration and speed debuffs and states those issues were fixed.
- An uphill at the start of a course can prolong start dash when low Power keeps target speed below the threshold.
- After start dash ends, minimum-speed handling can apply if the uma cannot reach minimum speed within one frame.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics and documented bug/fix behavior.

### DECELERATION

**FACT**

- Deceleration is determined by race phase.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

---

## 11. RACE_PHASES

### PHASE_DEPENDENCE

**FACT**

- Race calculations can change by phase.
- Deceleration is phase-dependent.
- HP consumption has phase-dependent behavior.
- The late-race/last-spurt portion uses a Guts-related HP-consumption modifier.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

---

## 12. SPEED_AND_ACCELERATION

### CURRENT_SPEED

**FACT**

- Current Speed is the direct result after acceleration calculations.
- Current Speed feeds subsequent acceleration calculations.
- Current Speed is used in HP-consumption calculations.

### ACTUAL_SPEED

**FACT**

- Actual Speed is Current Speed after current-speed modifiers.
- Current-speed modifiers apply immediately.
- Actual Speed is used for distance travelled and relative-speed calculations.

### ACCELERATION

**FACT**

- Start dash provides additional acceleration.
- Acceleration behavior depends on race phase and race state.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

---

## 13. POSITIONING_AND_LANES

### RELATIVE_SPEED

**FACT**

- Actual Speed is used for relative-speed calculations.
- Relative speed is relevant to blocking and overtaking.

### BLOCKING

**FACT**

- Blocking/surrounded behavior is a race-state mechanic.
- Guide 2 identifies being surrounded and unable to move as a possible cause of race loss even when an uma is otherwise strong.

**SOURCE_STATUS**
- Guide 2 general reference; Guide 3 deeper mechanics.

### LANE_MOVEMENT

**STATUS**
- Detailed lane-selection and movement rules belong here once fully extracted from Guide 3.

---

## 14. OVERTAKING

### OVERTAKING_RELATION

**FACT**

- Overtaking calculations use relative speed and Actual Speed.

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

### OVERTAKE_TARGETS

**STATUS**
- Detailed target-selection rules require the corresponding Guide 3 source section before canonicalization.

---

## 15. TRACK_AND_COURSE

### TRACK_ATTRIBUTES

**FACT**

Relevant race attributes include:

- Distance.
- Surface.
- Direction.
- Season.
- Weather.
- Ground condition.
- Course layout.

### GROUND_MODIFIERS

**VALUE**

| Surface | Good | Soft | Heavy | Bad |
|---|---:|---:|---:|---:|
| Turf | 1.00 | 1.00 | 1.02 | 1.02 |
| Dirt | 1.00 | 1.00 | 1.01 | 1.02 |

**SOURCE_STATUS**
- Guide 3; reverse-engineered mechanics.

### TRACK_SPECIFIC_REQUIREMENTS

**META / STRATEGY**

- Guide 4 contains event-specific stamina, stat, inheritance, skill, strategy, and character recommendations.
- These recommendations must remain attached to the specific event/track/distance/conditions that produced them.

---

## 16. SCENARIO_MECHANICS

### SCENARIO_SCOPE

**FACT**

- Scenario mechanics can change training evaluation and support-card value.
- Guide 1 adjusts evaluation parameters toward the current JP scenario/meta.
- Guide 1 does not fully simulate every scenario mechanic.

### SCENARIO_META

**META**

- Scenario recommendations from Guide 2 must retain scenario identity.
- Historical scenario recommendations are not universal current-game rules.

---

## 17. RACE_STRATEGY

### STRATEGY_TYPES

**FACT**

- Runner, Leader, Betweener, Chaser, and Oonige are distinct strategy categories in the source terminology.

### STRATEGY_CONDITIONS

**STRATEGY**

- Race strategy depends on track, distance, field behavior, available acceleration, and the uma's skill kit.
- Guide 4 contains event-specific examples where a strategy is favored because of course configuration or available acceleration.

### GUIDE4_SCOPE

**META**

- Guide 4 recommendations are tied to specific Champions Meeting / League of Heroes events.
- Example source context includes Kyoto 1600m Turf with clockwise direction, autumn, random weather/ground, and a stated good-ground distribution. Its strategy and skill recommendations belong to that event context.

### STRATEGY_TRADEOFFS

**RULE**

- A strategy recommendation must retain the reason and condition that make it useful.
- Do not preserve bare statements such as `use X` without the associated context.

---

## 18. RUN_EVALUATION

### RUN_EVALUATION_INPUTS

**INPUTS**

- Current Speed.
- Current Stamina.
- Current Power.
- Current Guts.
- Current Wisdom.
- Energy.
- Motivation.
- Aptitudes.
- Strategy.
- Skills and activation conditions.
- Support-card configuration.
- Remaining turns.
- Target race and track attributes.
- Inheritance/factor configuration.
- Current objective.

### RUN_STATE

**RELATION**

- Run quality should be evaluated against the current objective and target-race requirements, not raw stats alone.
- Guide 2 identifies insufficient Stamina as a common race-failure condition and notes Power as a possible next limiting factor when Stamina is adequate.

### ACTION_EVALUATION

**STRATEGY**

- Compare actions by supported immediate effect, opportunity cost, risk, and relevance to future requirements.
- Do not apply a generic preference when source material supplies a condition-specific rule.

### RACE_EVALUATION

**RELATION**

- Race outcome depends on multiple systems, including stamina/HP, aptitude, strategy modifiers, speed/acceleration, positioning, blocking, overtaking, and skill activation.

### SUPPORT_EVALUATION

**EVALUATION**

- Support-card value should be interpreted using its evaluation methodology, scenario, deck context, and skill contribution rather than a permanent universal tier.

---

## 19. DECISION_RULES

### TRAINING_DECISIONS

**RULE**

- Evaluate training against current run state, objective, and future requirements.
- Friendship/rainbow states have high value within Guide 1's support-card simulation model, but the preferred stat target depends on that model's configured weights.

### RECOVERY_DECISIONS

**RULE**

- Recovery decisions must account for current Energy and future training requirements.

### SKILL_DECISIONS

**RULE**

- Evaluate skills using race distance, strategy, activation conditions, timing, and target-race requirements.
- Treat source skill rankings as evaluation/meta unless mechanically established.

### INHERITANCE_DECISIONS

**RULE**

- Evaluate inheritance against target-race requirements, aptitude, compatibility, and available inherited effects.

### BUILD_DECISIONS

**RULE**

- Separate mechanical requirements from meta preference.
- Keep scenario/event-specific build advice scoped to its scenario/event.

---

## 20. EXCEPTIONS

### SOURCE_CONFLICTS

**RULE**

- If two sources disagree, do not silently choose one.
- Preserve the disagreement and source scope until verification resolves it.

### REVERSE_ENGINEERED_MECHANICS

**STATUS**

- Guide 3 is a detailed reverse-engineering document.
- Its formulas and mechanics are valuable for AI reasoning but remain marked as reverse-engineered unless independently verified.

### META_VS_FACT

**RULE**

- Terms such as `best`, `worst`, `mandatory`, `staple`, `weak`, and similar rankings are not automatically facts.
- Convert a recommendation into a rule only when its mechanical reason and applicable conditions are supported.

---

## 21. SOURCE_AND_VERIFICATION

### SOURCE_SCOPE

- `G1` — Support-card evaluation methodology and card evaluations.
- `G2` — Broad gameplay/reference information, terminology, training, inheritance, scenarios, skills, racing, and practical guidance.
- `G3` — Detailed race mechanics, formulas, modifiers, HP/stamina behavior, skill activation/effects, and reverse-engineered systems.
- `G4` — Champions Meeting / League of Heroes track-specific strategy, inheritance, skill, stamina, stat, and character recommendations.

### VERIFICATION_POLICY

- Source claims are not automatically confirmed facts.
- Reverse-engineered mechanics retain source status.
- Simulation outputs retain methodology and scope.
- Meta recommendations retain event/scenario/server/time scope.
- Personal opinion and author personality are excluded.
- Unresolved claims remain marked rather than silently corrected.

### SOURCE_TRACEABILITY

- Use lightweight source markers such as `G1`, `G2`, `G3`, and `G4` where useful.
- Do not duplicate source explanations when one canonical entry represents the information.

---

## 22. KNOWLEDGE_MAINTENANCE

### UPDATE_RULES

- Update the canonical concept rather than adding duplicate explanations.
- Preserve conditions and scope when updating values or recommendations.
- Re-evaluate time-sensitive meta information when the game environment changes.
- Never silently promote an evaluation or recommendation to `FACT`.
- Keep Guides 1–4 available until this file is fully populated and validated.

### COMPLETENESS_STATUS

- This file is the canonical target for the unified knowledge base.
- This version contains the initial populated knowledge structure.
- Detailed source sections that have not yet been fully extracted remain explicitly marked rather than guessed.
- Guides 1–4 should not be deleted until the remaining marked sections are extracted, verified, and merged.
