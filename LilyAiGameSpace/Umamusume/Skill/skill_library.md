# Skill Library
Source: `data/skill_data.json` + `data/skillnames.json` from `uma-skill-tools-master`.
**Preservation rule:** the original skill data object is reproduced unchanged. Added English naming is metadata only; IDs, conditions, preconditions, effects, modifiers, targets, types, durations, rarity, and wisdom checks are not rewritten or interpreted.
**English-name rule:** use the English name supplied by `skillnames.json` when present; otherwise reuse an English name for the same Japanese name when available; otherwise provide a close Japanese→English translation.
**Entries:** 1963
---
## 100011 — Shooting Star
- Japanese: `シューティングスター`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&order>=1&order_rate<=50&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100021 — I'm Not Giving up the Lead!
- Japanese: `先頭の景色は譲らない…！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order==1&bashin_diff_behind>=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100031 — Ultimate Teio Step
- Japanese: `究極テイオーステップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase>=2&order<=3&bashin_diff_infront<=1&is_overtake==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 100041 — Red Flame Gear/LP1211-M
- Japanese: `紅焔ギア/LP1211-M`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"is_finalcorner==1&order<=5&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100051 — Glittering Star Vaudeville
- Japanese: `煌星のヴォードヴィル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=300","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase>=2&order_rate<=40&behind_near_lane_time_set1>=1"}],"rarity":5,"wisdomCheck":0}
```
---
## 100061 — The Beat of Victory
- Japanese: `勝利の鼓動`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"order>=2&order<=5&order_rate<=50&remain_distance<=201&remain_distance>=199","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100071 — Unsinkable Ship, Anchored!
- Japanese: `不沈艦、抜錨ォッ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=50&distance_rate<=60&order_rate>50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100081 — Cutting × DRIVE!
- Japanese: `カッティング×DRIVE！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"order>=3&order_rate<=50&remain_distance<=200&bashin_diff_infront<=1@order>=3&order_rate<=50&remain_distance<=200&bashin_diff_behind<=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100091 — Brilliant Red Ace
- Japanese: `ブリリアント・レッドエース`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order==1&bashin_diff_behind<=1@distance_rate>=50&order==2&is_overtake==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100101 — Victory Shot!
- Japanese: `ヴィクトリーショット！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner_laterhalf==1&corner!=0&order>=3&order_rate<=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100101111 — Hungry Commander
- Japanese: `はらぺこ大将`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100101211 — Dream-fulfilling Sprint
- Japanese: `夢叶える末脚`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100102111 — Midsummer Resolution
- Japanese: `真夏の思い切り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100102211 — Midsummer Commander
- Japanese: `真夏の総大将`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100103111 — Tempestuous Attack
- Japanese: `怒涛の出陣`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase==2&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100103211 — Guts of the Rising Sun
- Japanese: `日之本一のド根性`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&is_finalcorner_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100111 — Where There's a Will, There's a Way
- Japanese: `精神一到何事か成らざらん`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&change_order_onetime<0&order>=3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100121 — One-On-One! Dead Heat!
- Japanese: `タイマン！デッドヒート！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"is_finalcorner==1&is_behind_in==1&change_order_onetime<0&order_rate>=40"}],"rarity":5,"wisdomCheck":0}
```
---
## 100131 — Fulfilling Your Noble Duty
- Japanese: `貴顕の使命を果たすべく`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&corner!=0&distance_diff_rate<=30&distance_type==4&lastspurt==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"is_finalcorner==1&corner!=0&distance_diff_rate<=30","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100141 — Plancha ☆ Ganador
- Japanese: `プランチャ☆ガナドール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&hp_per>=30&order<=2","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100151 — Dance for Vittoria
- Japanese: `ヴィットーリアに捧ぐ舞踏`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&bashin_diff_behind<=1&order<=4@is_finalcorner==1&bashin_diff_infront<=1&order<=4","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100161 — Shadow Break
- Japanese: `Shadow Break`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&order>=2&order_rate<=75&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase==1&blocked_side_continuetime>=2"},{"baseDuration":50000,"condition":"is_finalcorner==1&order>=2&order_rate<=75&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100171 — Thou, Witness the Heavenly Might of the Emperor
- Japanese: `汝、皇帝の神威を見よ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&change_order_up_end_after>=3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100181 — Blaze of Pride
- Japanese: `ブレイズ・オブ・プライド`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&corner!=0&order>=3&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100191 — Kyuute☆Last SpuU(ﾟ∀ﾟ)Uurt!
- Japanese: `尊み☆ﾗｽﾄｽﾊﾟ—(ﾟ∀ﾟ)—ﾄ!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"change_order_up_end_after>=2","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":28}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100201 — Angling×Scheming
- Japanese: `アングリング×スキーミング`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&corner!=0&order==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100201111 — Perfect Concentration
- Japanese: `最大集中`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"always==1","effects":[{"modifier":4000,"target":1,"type":10},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100201211 — Dimensional Runaway
- Japanese: `異次元の逃亡者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&is_finalcorner_random==1&order==1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100202111 — Lapis Lazuli Escape
- Japanese: `瑠璃色エスケイプ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100202121 — Crossing the Ocean
- Japanese: `滄海を越えしフーガ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==1&phase_laterhalf_random==1&order==1&course_distance==2200","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100202211 — Sky-Striding Ráfaga
- Japanese: `蒼天を駆けるラーファガ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==3&always==1","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100211 — Imma Show You White Lightning!
- Japanese: `白い稲妻、見せたるで！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&corner==0&order_rate>=70&order_rate<=75&is_overtake==1@distance_rate>=50&corner==0&order_rate<=30&order_rate>=20","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100221 — Fairy Tale
- Japanese: `Fairy tale`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order>=2&order_rate<=40&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100231 — ∴win Q.E.D.
- Japanese: `∴win Q.E.D.`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&is_finalcorner==1&order<=4&temptation_count==0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"phase>=2&is_finalcorner==1&order<=4","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100241 — Inspiration ☆ Landing
- Japanese: `ひらめき☆ランディング`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&blocked_side_continuetime>=2&order<=3","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100251 — Chasing After You
- Japanese: `アナタヲ・オイカケテ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=50&order_rate>=40&order_rate<=70","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-500,"target":9,"type":21}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100261 — G00 1st.F∞;
- Japanese: `G00 1st.F∞;`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_badstart==0&order<=3&is_last_straight==1&order_rate_in20_continue==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"is_badstart==0&order<=3&is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100271 — Let's Anabolic!
- Japanese: `レッツ・アナボリック！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&corner!=0&order_rate>=65&order_rate<=70","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100281 — I'M☆FULL☆SPEED!!
- Japanese: `I'M☆FULL☆SPEED!!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=45&distance_rate<=60&order>=2&order_rate<=50&is_overtake==1&distance_type==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=45&distance_rate<=60&order>=2&order_rate<=50&is_overtake==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100291 — Chasing the Snowlight
- Japanese: `ゆきあかり、おいかけて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_diff_top<=5&remain_distance<=300&order_rate<=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100301 — Blue Rose Chaser
- Japanese: `ブルーローズチェイサー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase>=2&order<=4&change_order_onetime<0"}],"rarity":5,"wisdomCheck":0}
```
---
## 100301111 — Genius Technique
- Japanese: `天才的技巧`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&is_move_lane==1@running_style==2&is_move_lane==2","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100301211 — Teio Step
- Japanese: `帝王ステップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":350,"target":1,"type":28},{"modifier":3000,"target":1,"type":31},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100302111 — Racing Genius
- Japanese: `レースの天才`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100302211 — Beyond the Horizon
- Japanese: `地平の彼方まで`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_move_lane==1&accumulatetime>=10@distance_type==3&is_move_lane==2&accumulatetime>=10","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100303111 — Gifted Grace
- Japanese: `天賦の身ごなし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&course_distance>=2400&course_distance<=2500&phase_firstquarter_random==2&order_rate<=50&base_stamina>=1000","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""},{"baseDuration":18000,"condition":"running_style==2&course_distance<2400&phase_firsthalf_random==2&order_rate<=50@running_style==2&course_distance>2500&phase_firsthalf_random==2&order_rate<=50@running_style==2&course_distance>=2400&course_distance<=2500&phase_firsthalf_random==2&order_rate<=50&base_stamina<1000","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100303211 — Playful Revelry
- Japanese: `盤楽遊嬉`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&order_rate<=50&phase_laterhalf_random==1","effects":[{"modifier":350,"target":1,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100303221 — Easy, Peasy, Lemon Squeezy
- Japanese: `朝腹、朝腹、かやすしや♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_firsthalf_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-100,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100311 — Charge Complete! Full Speed Ahead!
- Japanese: `チャージ完了！全速前進！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=299&remain_distance>=295&order<=2&slope==0@remain_distance<=299&remain_distance>=295&order<=2&slope==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"remain_distance<=305&remain_distance>=300&slope==1"},{"baseDuration":50000,"condition":"remain_distance<=299&remain_distance>=295&order<=2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100321 — U=ma2
- Japanese: `U=ma2`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_rate>=50&corner!=0&order>=3&order_rate<=40","effects":[{"modifier":550,"target":1,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100331 — Meteor of Dioscuri
- Japanese: `ディオスクロイの流星`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&distance_diff_top>=5&order_rate<80","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"is_last_straight==1&distance_diff_top>=5&order_rate>=80","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100341 — Fast Running, Fast Running!
- Japanese: `快走かな、快走かな！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"compete_fight_count>0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate_out40_continue==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 100351 — The Ticket to Victory, for You!
- Japanese: `勝利のチケットを、君にッ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&order<=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"is_finalcorner==1&blocked_side_continuetime>=2"}],"rarity":4,"wisdomCheck":0}
```
---
## 100361 — trigger:BEAT
- Japanese: `trigger:BEAT`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":28}],"precondition":"is_finalcorner==1&order_rate>=40&order_rate<=75&lane_type==0"}],"rarity":5,"wisdomCheck":0}
```
---
## 100371 — Schwarzes Schwert
- Japanese: `Schwarzes Schwert`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"temptation_count==0&order>=3&is_last_straight==1&order_rate_in80_continue==1&order_rate_out40_continue==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"temptation_count==0&order>=3&is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100381 — #LookatCurren
- Japanese: `#LookatCurren`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=65&order>=2&order_rate<=50&change_order_onetime<0","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100391 — Victory Befitting a Princess
- Japanese: `姫たるもの、勝利をこの手に`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100401 — KEEP IT REAL.
- Japanese: `KEEP IT REAL.`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=50&order_rate>=40&order_rate<=80&is_overtake==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100401111 — Blasting Off!
- Japanese: `かっ飛ばすわよ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100401211 — Crimson Over-revving
- Japanese: `紅蓮のオーバーレブ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&distance_rate>=50&order==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100401221 — Break Through the Red Zone
- Japanese: `レッドゾーンを突き抜けて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&overtake_target_time>=1&distance_type==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100402111 — Dazzling☆Wild Girl
- Japanese: `ドキッ☆じゃじゃウマ娘！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==1&slope==1&accumulatetime>=10","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100402121 — Beach Cutey Umamusume
- Japanese: `渚の激マブウマ娘`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&running_style==1&slope==1&accumulatetime>=10","effects":[{"modifier":150,"target":1,"type":9},{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100402211 — Ruler of the Stage
- Japanese: `お立ち台の支配者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100403111 — Angelic Garment
- Japanese: `天女の羽衣`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&distance_type==2&is_overtake==1&accumulatetime>=5@running_style==1&distance_type==2&overtake_target_time>=1&accumulatetime>=5","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100403211 — Shrine Maiden's Dance
- Japanese: `神薙ダンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&distance_type==2&distance_rate>=50&overtake_target_time>=1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100411 — Honor Student x Bakushin = Big Victory
- Japanese: `優等生×バクシン＝大勝利ッ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order<=3&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100421 — 『I'm Possible』
- Japanese: `『I'm possible』`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=201&remain_distance>=199&distance_diff_top<=5&order>=2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"remain_distance<=201&remain_distance>=199&distance_diff_top<=10&order>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100431 — Ding Dong Boo
- Japanese: `Ding Dong Boo`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"compete_fight_count>0&ground_type==2","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":50000,"condition":"compete_fight_count>0","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100441 — You're Mine ☆ Strelitzia
- Japanese: `いただき☆ストレリチア！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"remain_distance<=300","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"order_rate_out50_continue==1&temptation_count==0&is_finalcorner==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 100451 — Purity of Heart
- Japanese: `ピュリティオブハート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase_random==1&order>=2&order_rate<=40","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100461 — Sparkling☆STARDOM
- Japanese: `キラキラ☆STARDOM`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase==1&corner==0&order<=2&bashin_diff_behind<=1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100471 — Raise Thy Soul's Sword!
- Japanese: `掲げよ、己が魂の剣を！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&remain_distance<=401&remain_distance>=399&order_rate<=40&grade==100&popularity<=3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"phase>=2&remain_distance<=401&remain_distance>=399&order_rate<=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100481 — YEAH☆VIVID TIME!
- Japanese: `YEAH☆VIVID TIME!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&order_rate<=40&overtake_target_time>=1@is_last_straight==1&order_rate<=40&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100491 — Laugh in the Face of Danger
- Japanese: `剣ヶ峰より、狂気に嗤え`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=400&order_rate>=30&order_rate<=50&popularity>=4","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"is_finalcorner==1&is_overtake==1"},{"baseDuration":50000,"condition":"remain_distance<=400&order_rate>=30&order_rate<=50&popularity<4","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"is_finalcorner==1&is_overtake==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 100501 — Nemesis
- Japanese: `Nemesis`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&order_rate>=40&order_rate<=75&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100501111 — Sparkling Top Star
- Japanese: `輝くトップスタァ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&is_overtake==1&accumulatetime>=5","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100501211 — Entertainer
- Japanese: `エンターテイナー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100501221 — For a Sparkling Miracle
- Japanese: `煌めく“キセキ”を`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":150,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100502111 — Stunning Trick
- Japanese: `圧巻のトリック`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&order_rate<=50&temptation_opponent_count_behind>=1","effects":[{"modifier":-300,"target":20,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100502121 — Captivating Cornering
- Japanese: `見惚れるコーナリング`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_finalcorner_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100502211 — Glittering Top Star
- Japanese: `煌めきのトップスタァ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100511 — When the Flower Bud Opens
- Japanese: `つぼみ、ほころぶ時`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&is_finalcorner_laterhalf==1&order>=3&order_rate<=40@phase>=2&is_finalcorner==1&corner==0&order>=3&order_rate<=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"phase==1&blocked_side_continuetime>=2&corner!=0"}],"rarity":5,"wisdomCheck":0}
```
---
## 100521 — Exciting Climax
- Japanese: `ワクワククライマックス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"is_finalcorner==1&corner!=0&order_rate>50&near_count>=1","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100531 — Hot-Blooded Disciplinary Attack!
- Japanese: `熱血！！風紀アタック`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"phase>=2&order_rate>=50&is_finalcorner==1&bashin_diff_infront<=1","effects":[{"modifier":1000,"target":1,"type":31},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100541 — Blasting Gale Pegasus Dash!
- Japanese: `疾風爆走ペガサスダッシュ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"remain_distance<=150&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"order_rate>=45&distance_rate>=50&change_order_onetime<0"}],"rarity":4,"wisdomCheck":0}
```
---
## 100551 — Colorful☆Marvelous★World
- Japanese: `万彩☆マーベラス★世界`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate<=50&distance_rate>=40&order_rate<=80&order_rate>=50&near_count>=1&visiblehorse>=4","effects":[{"modifier":4000,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate<=50&distance_rate>=40&order_rate<=80&order_rate>=50&near_count>=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100561 — Luck Is Coming
- Japanese: `来ます来てます来させます！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&order>=3&blocked_front==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100571 — Lyricism at Journey's End
- Japanese: `叙情、旅路の果てに`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate>50@distance_type==4&phase_laterhalf_random==1&order_rate>50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":60000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate>50@distance_type==2&phase_laterhalf_random==1&order_rate>50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100581 — I Never Goof Up!
- Japanese: `I Never Goof Up!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&change_order_onetime<0","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100591 — Beyond the Other Side
- Japanese: `彼方、その先へ…`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&corner!=0&is_finalcorner==0&temptation_count==0&order_rate>=50&order_rate<=70@phase==1&corner!=0&is_finalcorner==1&temptation_count==0&order_rate>=50&order_rate<=70","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100601 — Surely, Beyond...!
- Japanese: `きっとその先へ…！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&order==3&bashin_diff_behind<=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100601111 — Glutton of Kasamatsu
- Japanese: `笠松の食いしん坊`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_random==1","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100601121 — Starved Monster
- Japanese: `飢えた怪物`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1","effects":[{"modifier":150,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100601211 — Monstrous Cornering
- Japanese: `怪物的コーナリング`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"all_corner_random==1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100602111 — Gluttonous Regimen
- Japanese: `ドカ食い養生`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_random==1","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100602211 — First-hand Christmas Miracle
- Japanese: `クリスマスの奇跡体験`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&is_finalcorner==1&corner!=0&lane_type==0","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100603111 — Undying Flame
- Japanese: `尽きぬ炎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"distance_type==2@distance_type==4"},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&compete_fight_count>0&remain_distance<=201&remain_distance>=199","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100603211 — Let Your Name Shake Heaven and Earth
- Japanese: `天地を揺らせ君の名で`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&running_style==2&phase==2&course_distance==2500&track_id==10005","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":"distance_diff_top<=10&distance_rate>=60&phase==1"},{"baseDuration":12000,"condition":"distance_type==4&running_style==2&phase==2&course_distance==2500&track_id==10005","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100603221 — The Ashen Monster
- Japanese: `灰の怪物`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==2&running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":6000,"target":1,"type":31}],"precondition":"distance_diff_top<=10&distance_rate>=60&phase==1"},{"baseDuration":12000,"condition":"distance_type==2&running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100611 — Pride of KING
- Japanese: `Pride of KING`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"temptation_count==0&remain_distance<=201&remain_distance>=199&order>=4&order_rate<=70","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100621 — Bang, Bam, Mun
- Japanese: `どんっ、パッ、むんっ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&phase==1&order>=3&order_rate<=70","effects":[{"modifier":550,"target":1,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100631 — Forged From a Hundred Trials
- Japanese: `百錬成鋼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"is_lastspurt==1&phase==3&temptation_count==0","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100641 — The Breakaway Road
- Japanese: `ぶっちぎりロード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=50&order_rate_in20_continue==1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100651 — Everybody Put Your Hands Up!
- Japanese: `アゲてアゲてぷちょへんざ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate<=50@distance_type==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate<=50@distance_type==4&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100661 — Engine, Full Throttle! Turbo Time!
- Japanese: `エンジン全開！大噴射！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":130000,"condition":"distance_rate>=34&distance_rate<=36&order==1&bashin_diff_behind>=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":5000000,"condition":"phase==3&is_activate_other_skill_detail==1","effects":[{"modifier":-500,"target":1,"type":21}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100671 — Brilliance Illuminating the Darkness
- Japanese: `晦冥を照らせ永遠の耀き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight_onetime==1&order>=2&order<=5&distance_diff_top<=5","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"is_last_straight_onetime==1&order>=2&order<=5&distance_diff_top>5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100681 — Shout of Victory
- Japanese: `勝ち鬨ワッショイ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase==2&straight_front_type==2&order<=2","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=50&corner==3&order<=2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100691 — Longing Beyond the Sakura
- Japanese: `憧れは桜を越える！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=300&order_rate<=40&bashin_diff_infront<=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100701 — Seirios
- Japanese: `セイリオス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"remain_distance>=799&remain_distance<=801&order_rate>=30&order_rate<=60&course_distance==2400&popularity<=3","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"remain_distance>=799&remain_distance<=801&order_rate>=30&order_rate<=60","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100701111 — Clear View with 564 Eyes!
- Japanese: `564アイズで視界クッキリ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&is_move_lane==1@running_style==4&is_move_lane==2","effects":[{"modifier":100000,"target":1,"type":8},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100701211 — Extreme After-School Technique
- Japanese: `エクストリーム下校術`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&slope==2&accumulatetime>=10","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100702111 — Mysterious Gold Ship Warp!
- Japanese: `神秘体験！ゴルシワープ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&is_finalcorner==1&corner!=0&lane_type==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100702211 — Squid for a Quid!
- Japanese: `イカ揚げ、いかがですか！？`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100702221 — It's Getting Exciting!!
- Japanese: `高まってきたぜぇ！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_random==1&order_rate>=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100703111 — Flood of "Je t'aime"
- Japanese: `押し寄せるジュテーム`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==4&is_lastspurt==1&corner==0","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100703211 — Golden Ship of the Rough Seas
- Japanese: `荒磯好みの黄金船`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==2@ground_condition==3@ground_condition==4","effects":[{"modifier":1000,"target":1,"type":14},{"modifier":800000,"target":1,"type":3},{"modifier":800000,"target":1,"type":1}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 10071 — Warning Shot!
- Japanese: `波乱注意砲！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=50&distance_rate<=60&order_rate>50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 100711 — A Lifetime's Dream, A Moment's Flight
- Japanese: `一期の夢、刹那の飛翔`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"is_last_straight==1&bashin_diff_behind<=1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-100,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100721 — Dazzling Fire, Invincible Dance
- Japanese: `烈火繚乱、無敵之舞`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=300&order_rate<=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"is_finalcorner==1&change_order_onetime<0"}],"rarity":5,"wisdomCheck":0}
```
---
## 100731 — Flames of Unyielding Resolve
- Japanese: `燃え盛るは絶対の意志`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&change_order_up_end_after>=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 100741 — Lovely Spring Wind
- Japanese: `麗しき花信風`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order_rate>=40&order_rate<=80","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100761 — Blossoming World
- Japanese: `花開き、世界`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_type==4&distance_rate>=50&distance_rate<=51&order_rate>=30&order_rate<=80","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":750,"target":1,"type":9}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51&order_rate>=30&order_rate<=80","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100771 — Road to Glory
- Japanese: `Road to Glory`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=401&remain_distance>=399&distance_diff_top_float<=25&distance_type==4","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":"distance_rate>=60&phase==1&order>=2&order_rate<=40"},{"baseDuration":50000,"condition":"remain_distance<=401&remain_distance>=399","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"distance_rate>=60&phase==1&order>=2&order_rate<=40"}],"rarity":5,"wisdomCheck":0}
```
---
## 100781 — A Spring in My Step
- Japanese: `風光る`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":80000,"condition":"is_finalcorner_laterhalf==1&distance_diff_rate<=50&order==2","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":"distance_rate>=50&order_rate_out20_continue==1"},{"baseDuration":80000,"condition":"is_finalcorner_laterhalf==1&distance_diff_rate<=50","effects":[{"modifier":1000,"target":1,"type":31}],"precondition":"distance_rate>=50&order_rate_out20_continue==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 100791 — Funabashi Above All!
- Japanese: `『船橋最強！』`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=50&track_id==10101@distance_rate>=50&track_id==10103@distance_rate>=50&track_id==10104","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase==1&order_rate<=50&blocked_side_continuetime>=2"},{"baseDuration":40000,"condition":"distance_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase==1&order_rate<=50&blocked_side_continuetime>=2"}],"rarity":5,"wisdomCheck":0}
```
---
## 100801 — Info: Acquired
- Japanese: `Info: Acquired`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_other_character_activate_advantage_skill==31","effects":[{"modifier":2500,"target":1,"type":22},{"modifier":1500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate_in20_continue==1&track_id>=10001&track_id<=10010&ground_type==2"},{"baseDuration":50000,"condition":"is_other_character_activate_advantage_skill==31","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":"distance_rate>=50&order_rate_in20_continue==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 100801111 — Flasks Up
- Japanese: `スキットルブレイク`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&corner==0","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100801211 — Unrivaled Strides
- Japanese: `抜群の豪脚`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_random==2&order_rate>50","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100802111 — I'll Leave You in the Dust!
- Japanese: `ぶっ差してやるぜ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=1&is_lastspurt==1&hp_per>=1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":250,"target":1,"type":28},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100802211 — Fastest Top Gear
- Japanese: `最速のトップギア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&is_last_straight==1&order>=2&distance_diff_top<=10","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10081 — Accelerator X
- Japanese: `アクセルX`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"order>=3&order_rate<=50&remain_distance<=200&bashin_diff_infront<=1@order>=3&order_rate<=50&remain_distance<=200&bashin_diff_behind<=1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 100811 — Punkish Bite
- Japanese: `Punkish Bite`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==1&phase>=2&corner!=0&ground_type==2@running_style==2&phase>=2&corner!=0&ground_type==2","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"running_style==1&phase>=2&corner!=0@running_style==2&phase>=2&corner!=0","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100821 — Shining Runway
- Japanese: `Shining Runway`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==2&is_finalcorner==1&corner!=0&order_rate<=50&order_rate>=20","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"is_finalcorner==1&corner!=0&order_rate<=50&order_rate>=20","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100831 — Mission: Triumph
- Japanese: `Mission: Triumph`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=40&corner==0&slope==2&order_rate>=40&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=40&corner==0&order_rate>=40&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100841 — Thunderstorm Sublation
- Japanese: `霹靂のアウフヘーベン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&track_id==10006&distance_type==3","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":"phase>=2&order_rate>=50"},{"baseDuration":50000,"condition":"is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":"phase>=2&order_rate>=50"}],"rarity":5,"wisdomCheck":0}
```
---
## 100851 — Reign Supreme
- Japanese: `至上であれ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=66&distance_rate<=68&order_rate>=60&order_rate<=90&temptation_count==0","effects":[{"modifier":2500,"target":1,"type":22},{"modifier":-500,"target":7,"type":21}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100861 — Melt in Love's Embrace
- Japanese: `愛と熔けよただ熔けよ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance>=999&remain_distance<=1001&order_rate>=20&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100871 — Silent Letter
- Japanese: `Silent letter`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=400&order<=2&overtake_target_time>=1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100881 — Reversal Illusion
- Japanese: `Reversal Illusion`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==3&remain_distance<=400","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"change_order_up_middle>=1&is_finalcorner==1&corner!=0&order_rate<=70&order_rate>=40"},{"baseDuration":50000,"condition":"remain_distance<=400","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"is_finalcorner==1&corner!=0&order_rate<=70&order_rate>=40"}],"rarity":5,"wisdomCheck":0}
```
---
## 100891 — Celeste Oath
- Japanese: `Celeste Oath`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=50&course_distance>=2400","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100901 — Queen's Rebirth
- Japanese: `Queen's Rebirth`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate<=50&corner!=0&order_rate<=50&ground_type==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_last_straight==1&overtake_target_time>=1&distance_type==2@is_activate_other_skill_detail==1&phase>=2&is_last_straight==1&overtake_target_time>=1&distance_type==3","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100901111 — Perfect Tune
- Japanese: `パーフェクトチューン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100901211 — This is my win!
- Japanese: `アタシが勝つんだから！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100902111 — Tomboy Queen
- Japanese: `おてんば女王`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==1&slope==1&accumulatetime>=10","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100902121 — Scarlet Radiance
- Japanese: `緋色の光となって`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&distance_type==4&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":9000,"condition":"is_activate_other_skill_detail==1&is_lastspurt==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 100902211 — Door of Dreams
- Japanese: `開かれる夢の扉`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&is_last_straight==1&order==1&bashin_diff_behind<=1","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10091 — Red Ace
- Japanese: `レッドエース`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order==1&bashin_diff_behind<=1@distance_rate>=50&order==2&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 100911 — Deluxe☆Fountain
- Japanese: `デラックス☆ファウンテン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=300","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase>=2&is_last_straight_onetime==1&order_rate>=30&order_rate<=70&temptation_count==0"},{"baseDuration":50000,"condition":"remain_distance<=300","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"phase>=2&is_last_straight_onetime==1&order_rate>=30&order_rate<=70"}],"rarity":5,"wisdomCheck":0}
```
---
## 100921 — My Flame Lights the Way
- Japanese: `照らすのはわたしの焔`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=55&order_rate<=50&order_rate>=20&distance_type==3","effects":[{"modifier":4000,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=55&order_rate<=50&order_rate>=20","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100931 — Blue Ray of Happiness
- Japanese: `幸せの青い光`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==1&phase_firsthalf_random==2&order_rate<=50&order_rate>=20@distance_type==2&phase_firsthalf_random==2&order_rate<=50&order_rate>=20","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate<=50&order_rate>=20@distance_type==4&phase_firsthalf_random==2&order_rate<=50&order_rate>=20","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100941 — Faith in the Feral
- Japanese: `Faith in the Feral`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51&order_rate<=80&order_rate>=40&distance_type==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51&order_rate<=80&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100951 — Because I Believe
- Japanese: `念い、信ずればこそ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==2&distance_rate>=66&distance_rate<=68&order_rate<=50&distance_type==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"running_style==2&distance_rate>=66&distance_rate<=68&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100961 — Deceive Thy Foe and Be Certain of Victory
- Japanese: `知宵欺敵、百戦不殆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"corner==3&order_rate>=40&order_rate<=70&distance_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_last_straight==1&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100971 — Scarlet Lily's Elation
- Japanese: `スカーレットリリィの高揚`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&is_used_skill_id==203781&phase>=2&corner!=0","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":50000,"condition":"order_rate>=20&order_rate<=70&remain_distance>=299&remain_distance<=301","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100981 — Luck Comes to the Prepared
- Japanese: `理運開かりて翔る`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase_laterhalf_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 100991 — Shine ☆ Tomakomai
- Japanese: `かがやけ☆とまこまい`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"is_lastspurt==1&order_rate<=40&order_rate>=30&ground_type==2&lastspurt==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"phase==1&blocked_side_continuetime>=2&corner!=0"},{"baseDuration":40000,"condition":"is_lastspurt==1&order_rate<=40&order_rate>=30&ground_type==2","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":"phase==1&blocked_side_continuetime>=2&corner!=0"}],"rarity":5,"wisdomCheck":0}
```
---
## 101001 — Never Say Never
- Japanese: `Never Say Never`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance>=299&remain_distance<=301&order_rate>=20&order_rate<=40&distance_diff_top<=5&ground_type==2","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"remain_distance>=299&remain_distance<=301&order_rate>=20&order_rate<=40","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101001111 — Sharpshooting!
- Japanese: `狙い撃ちデス！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101001211 — Frontier Spirit
- Japanese: `Frontier Spirit`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_laterhalf_random==0&accumulatetime>=5&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101002111 — Adventure Leader
- Japanese: `アドベンチャーの先導者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_laterhalf_random==0&accumulatetime>=5&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101002211 — No Holds Barred!
- Japanese: `真剣勝負デス！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101003111 — Sheepy, Go!
- Japanese: `飛び出せSheepy!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_corner_random==1&order_rate<=50&distance_type==2","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""},{"baseDuration":40000,"condition":"running_style==2&phase_corner_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101003211 — Sheep Stampede!
- Japanese: `Sheep Stampede!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"phase_firstquarter==2&order==1@phase_firstquarter==2&is_overtake==1@phase_firstquarter_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"running_style==2&distance_type==2"}],"rarity":6,"wisdomCheck":1}
```
---
## 101021 — Vivace Volare
- Japanese: `ヴィヴァーチェ・ヴォラーレ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_rate<=50&order_rate>=40&order_rate<=80&infront_near_lane_time>=3&accumulatetime>=10@distance_rate<=50&order_rate>=40&order_rate<=80&behind_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""},{"baseDuration":40000,"condition":"distance_rate<=60&distance_rate>=45&corner==0&is_activate_other_skill_detail==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101031 — Absolutely Strong ☆ Appeal Declaration!
- Japanese: `絶対最強☆アピール宣言！`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase==1&order_rate<=50&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"is_activate_other_skill_detail==1&compete_fight_count>0","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":4,"wisdomCheck":0}
```
---
## 101041 — Flag of Dawn: Katsuragi Ace
- Japanese: `暁の御旗『葛城栄主』！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"corner==3&order==1&track_id==10006&distance_type==3","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""},{"baseDuration":50000,"condition":"corner==3&order==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101051 — Ad Astra
- Japanese: `アド・アストラ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=55&order_rate>=40&order_rate<=80&distance_type==3&activate_count_all>=7","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=55&order_rate>=40&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101061 — Bang☆Miracle Maker!
- Japanese: `Bang☆ミラクるわせ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_type==4&order_rate>=40&order_rate<=70&is_finalcorner_laterhalf==1&popularity>=4","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":60000,"condition":"order_rate>=40&order_rate<=70&is_finalcorner_laterhalf==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101071 — Billions of Stars
- Japanese: `Billions of stars`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&is_last_straight==1&order==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101081 — Scarlet Ascension of the Rakshasa
- Japanese: `羅刹、赤翼にて天上へ至らん`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"phase>=2&is_activate_other_skill_detail==1&is_finalcorner==1&corner!=0&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101091 — Connecting Dreams With the Future
- Japanese: `繋ぐ・繋がる×夢・未来`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_type==1&distance_rate<=50&corner!=0&order>=3&order_rate<=70@distance_type==2&distance_rate<=50&corner!=0&order>=3&order_rate<=70","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate<=50&corner!=0&order>=3&order_rate<=70","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101101 — Guiding Sea
- Japanese: `Guiding Sea`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"remain_distance>=799&remain_distance<=801&is_basis_distance==1&order_rate>=70&order_rate<=80","effects":[{"modifier":2500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31},{"modifier":2000,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"remain_distance>=799&remain_distance<=801&order_rate>=50&order_rate<=80","effects":[{"modifier":2500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101101111 — Yamato Nadeshiko
- Japanese: `大和撫子`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_random==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101101211 — Conviction
- Japanese: `不退転の意思`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101102111 — Curely Heal
- Japanese: `キュアリーヒール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101102211 — Conjuring Courage
- Japanese: `勇気の魔法`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101103111 — Piercing Azure
- Japanese: `射貫く蒼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_straight_random==1&distance_type==4&track_id==10005","effects":[{"modifier":6000,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"running_style==3&phase_straight_random==1","effects":[{"modifier":5500,"target":1,"type":27},{"modifier":-300,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101103211 — Seizing Victory
- Japanese: `勝機到来`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==27@distance_type==4&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==27@distance_type==3&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==22@distance_type==4&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==22","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10111 — Desire to Win
- Japanese: `精神一到`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&change_order_onetime<0&order>=3","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 101111 — Traced Bloodline, Budding Future
- Japanese: `辿る血脈、芽吹く未来`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=49&distance_rate<=50&order_rate>=40&order_rate<=90&slope==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":60000,"condition":"distance_rate>=49&distance_rate<=50&order_rate>=40&order_rate<=90","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101131 — Hop Step Gotcha ♡
- Japanese: `ホップステップ・ゲッチュ♡`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"order_rate>=20&order_rate<=50&distance_rate<=50&corner!=0&course_distance==2200","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"order_rate>=20&order_rate<=50&distance_rate<=50&corner!=0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101141 — To Our Vista
- Japanese: `To Our Vista`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51&order_rate>=40&distance_type==2@distance_rate>=50&distance_rate<=51&order_rate>=40&distance_type==3","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51&order_rate>=40","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101151 — None Shall Object My Rule
- Japanese: `我が覇道、阻むものなし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"running_style==4&remain_distance>=999&remain_distance<=1001&base_speed>=1000&base_stamina>=1000&base_power>=1000&base_guts>=1000&base_wiz>=1000","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":"distance_type==3@distance_type==4"},{"baseDuration":60000,"condition":"running_style==4&remain_distance>=999&remain_distance<=1001","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101161 — Rose Conquest
- Japanese: `烈華の洗礼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate<=50&corner!=0&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&order_rate<=40&phase>=2&is_last_straight==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101171 — Allegro of Valor
- Japanese: `鋭気のアレグロ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"is_last_straight_onetime==1&change_order_up_end_after>=3@is_last_straight_onetime==1&change_order_up_end_after>=2&change_order_up_middle>=1@is_last_straight_onetime==1&change_order_up_end_after>=1&change_order_up_middle>=2@is_last_straight_onetime==1&change_order_up_middle>=3","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":"running_style==4&phase>=2"},{"baseDuration":40000,"condition":"is_last_straight_onetime==1&change_order_up_end_after>=1@is_last_straight_onetime==1&change_order_up_middle>=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase>=2"}],"rarity":5,"wisdomCheck":0}
```
---
## 101191 — «Bon Voyage»
- Japanese: `『それでは、よき旅を』`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=66&distance_rate<=68&order_rate>=50&remain_distance>=500","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&corner==0&track_id==10005&distance_type==3@is_activate_other_skill_detail==1&corner==0&track_id==10005&distance_type==4@is_activate_other_skill_detail==1&corner==0&track_id==10009&distance_type==3@is_activate_other_skill_detail==1&corner==0&track_id==10009&distance_type==4","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101201 — Path of Singular Focus
- Japanese: `無二無三なる一条の路`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"furlong==3&order_rate<=50&is_used_skill_id==203061&is_used_skill_id==203071","effects":[{"modifier":6500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"furlong==3&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101201111 — Victory Roar
- Japanese: `勝利への咆哮`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_finalcorner==1&corner!=0&is_overtake==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101201121 — One-On-One Obsession
- Japanese: `タイマンにかける執念`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=201&remain_distance>=199&distance_type==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"is_finalcorner==1&change_order_onetime<0"}],"rarity":6,"wisdomCheck":1}
```
---
## 101201211 — Tempestuous Pororoca
- Japanese: `怒濤のポロロッカ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_firsthalf_random==3&is_lastspurt==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase>=2&distance_diff_rate>=50"}],"rarity":6,"wisdomCheck":1}
```
---
## 101202111 — Passionate Engagement!
- Japanese: `熱烈エンゲージ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&phase_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101202211 — Fiery Cake-Cutting!
- Japanese: `闘魂入刀！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&distance_type==3&phase_firsthalf_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"distance_rate>=66&temptation_count==0"}],"rarity":6,"wisdomCheck":1}
```
---
## 101202221 — Strike of an Oath
- Japanese: `誓いの一振り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==3&running_style==4&phase_firsthalf_random==2","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101211 — Lame de Vent
- Japanese: `Lame de vent`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_lastspurt==1&phase==3&order_rate>=40&order_rate<=80&distance_type==1@is_lastspurt==1&phase==3&order_rate>=40&order_rate<=80&distance_type==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"is_finalcorner==1&corner!=0&change_order_onetime<0"},{"baseDuration":50000,"condition":"is_lastspurt==1&phase==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"is_finalcorner==1&corner!=0&change_order_onetime<0"}],"rarity":5,"wisdomCheck":0}
```
---
## 101241 — Growing Dreams, Pioneer's Path
- Japanese: `ふくらむ夢、先駆の途`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase_laterhalf_random==1&order_rate<=50&course_distance>=1600&course_distance<=2000&distance_diff_top<=10","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101271 — Target Acquired! Serving Justice!
- Japanese: `対象捕捉！正義遂行！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&corner==0&order_rate<=70&order_rate>=30&distance_type==4","effects":[{"modifier":4000,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=50&corner==0&order_rate<=70&order_rate>=30","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101291 — Peerless Heroine
- Japanese: `Peerless Heroine`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&corner!=0&order_rate<=50&ground_type==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":20000,"condition":"is_activate_other_skill_detail==1&run_at_full_speed_random==1&order<=3&distance_type==3","effects":[{"modifier":4000,"target":1,"type":48}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101301111 — Mejiro's Wisdom
- Japanese: `メジロの心得`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101301211 — Star's Composure
- Japanese: `名優の余裕`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101302111 — Active Rest
- Japanese: `アクティブレスト`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101302211 — End of Sky
- Japanese: `空の果てまで`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101303111 — Summer Star
- Japanese: `夏の名優`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101303211 — Wholehearted Refresher
- Japanese: `一意専心にリフレッシュ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"is_badstart==0&running_style==2&distance_type==4&phase_firsthalf_random==1","effects":[{"modifier":950,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101311 — ¡Qué alegría!
- Japanese: `¡Qué alegría!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=51&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==1&is_activate_other_skill_detail==1&phase==3&is_lastspurt==1@distance_type==2&is_activate_other_skill_detail==1&phase==3&is_lastspurt==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101321 — Circulating Love♡
- Japanese: `Circulating Love♡`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase_laterhalf_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"distance_type==3&running_style==3&ground_type==1"},{"baseDuration":50000,"condition":"running_style==3&ground_type==1&phase_laterhalf_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101331 — Weaving History
- Japanese: `Weaving History`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":80000,"condition":"distance_type==3&ground_type==1&running_style==2&distance_rate>=40&distance_rate<=41@distance_type==4&ground_type==1&running_style==2&distance_rate>=40&distance_rate<=41","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":20000,"target":1,"type":42}],"precondition":""},{"baseDuration":40000,"condition":"ground_type==1&running_style==2&distance_rate>=40&distance_rate<=41","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101351 — In Search of Gold
- Japanese: `黄金を訪ねて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"running_style==3@running_style==4"},{"baseDuration":20000,"condition":"is_activate_other_skill_detail==1&course_distance>=2000&is_lastspurt==1","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 101371 — Imagination × Creation = ∞
- Japanese: `想像×創造＝∞`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"order_rate<=70&phase_firsthalf==1&is_used_skill_id==202051","effects":[{"modifier":350,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":"distance_type==3@distance_type==4"},{"baseDuration":80000,"condition":"order_rate<=70&phase_firsthalf==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":"distance_type==3@distance_type==4"}],"rarity":5,"wisdomCheck":0}
```
---
## 101401111 — Falcon Eyes
- Japanese: `鷹ノ目`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_random==0","effects":[{"modifier":150000,"target":1,"type":8},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101401211 — Flawless Performance
- Japanese: `余裕のパフォーマンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101402111 — Unparalleled Bravery
- Japanese: `豪勇無双`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_random==2&order_rate>50","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101402121 — Condor Leap
- Japanese: `コンドル跳躍術`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&phase_random==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101402211 — Rising Condor
- Japanese: `昇りコンドル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&is_finalcorner==1&corner!=0&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10141 — Hot Blooded ☆ Amigo
- Japanese: `熱血☆アミーゴ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&hp_per>=30&order<=2","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 101501111 — Centurial Overlord Descends!
- Japanese: `降臨！世紀末覇王！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101501211 — March of the Opera King
- Japanese: `歌劇王の行進`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101502111 — Waltz Maestro
- Japanese: `円舞曲のマエストロ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&corner!=0","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101502121 — Opera King's Corner Theatrics
- Japanese: `コーナーに舞い降りし歌劇王`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase==1&corner!=0","effects":[{"modifier":150,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101502211 — I Won't Fall Behind!
- Japanese: `ボクは遅れずにやってくる！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101601111 — Decisive Cleave
- Japanese: `一刀両断`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101601211 — Hungry Wolf's Fang
- Japanese: `餓狼牙`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101602111 — BLAZING WOLF
- Japanese: `BLAZING WOLF`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&distance_rate>=50&is_overtake==1@running_style==3&distance_rate>=50&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101602211 — Craving Monster
- Japanese: `渇望する怪物`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&running_style==2&phase==2","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":"distance_diff_top<=10&distance_rate>=60&phase==1"}],"rarity":6,"wisdomCheck":1}
```
---
## 101701111 — Emperor's Gaze
- Japanese: `皇帝の眼差し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_random==2","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101701121 — Unclouded Noble Path
- Japanese: `陰りなき王道`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase==2&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101701211 — Hands-Down Victory
- Japanese: `鎧袖一触`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101702111 — Perfect Composure
- Japanese: `神色自若`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101702211 — Noble Hardships
- Japanese: `風霜高潔`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==3","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 101801111 — The Empress' Ploy
- Japanese: `女帝の権謀`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_random==2&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101801211 — Moonlit Water, Mirror Flower
- Japanese: `水月鏡花`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==2","effects":[{"modifier":350,"target":1,"type":28},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101802111 — The Empress' Pride
- Japanese: `女帝の矜持`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&is_overtake==1&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101802211 — Crescent Moon Sommelier
- Japanese: `上弦のソムリエール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"all_corner_random==1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101802221 — Trajectory to the Future
- Japanese: `未来へ続く放物線`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==1&distance_type==2&is_finalcorner_random==1","effects":[{"modifier":3000,"target":1,"type":31},{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==2&is_finalcorner_random==1","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10181 — Empress・Pride
- Japanese: `エンプレス・プライド`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&corner!=0&order>=3&change_order_onetime<0","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 101901111 — Uma Mania Max
- Japanese: `限界ウママニア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"near_count>=3&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101901211 — The Front Row Is Non-Negotiable!
- Japanese: `最前列は譲れない！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==2&phase_random==2","effects":[{"modifier":350,"target":1,"type":28},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101901221 — Aim for the Front and Center!
- Japanese: `狙うは最前ドセンへの道！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==1&phase_random==2&distance_type==3","effects":[{"modifier":3000,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"ground_type==2&phase_random==2&distance_type==3","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101902111 — Super Express Submission!
- Japanese: `超特急入稿！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101902121 — Now I'm Hyped!!
- Japanese: `たぎってきたぁ～～っ！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==2&phase==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 101902211 — Revived For Moe!
- Japanese: `尊みを求めてふっかーーつ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102001111 — Fast Retrieve
- Japanese: `ファストリトリーブ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&phase_random==1&bashin_diff_behind>=1&order==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102001121 — Angler's Wisdom
- Japanese: `大物狙いの心得`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102001211 — Operation Escape
- Japanese: `脱出大作戦`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102002111 — Run~Away~♪
- Japanese: `逃げろ～♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102002121 — Surprise~Successful~☆
- Japanese: `サプライズ大成功～☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102002211 — Record Runner
- Japanese: `レコードランナー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase<=1&change_order_onetime>0&accumulatetime>=5@running_style==1&phase<=1&blocked_side_continuetime>=2&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102101111 — Stormstrider
- Japanese: `雷騰雲奔`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102101121 — Let's Get Cracking!
- Japanese: `ちゃちゃっと始めんで！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102101211 — Tail of Ecstasy
- Japanese: `尻尾の有頂天`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"activate_count_middle>=3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102102111 — Ode to Our Predecessors
- Japanese: `先達に献ぐ祈りの頌`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102102211 — 'ight, let's get em!
- Japanese: `さあ、ウチとやろうや！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase==1&change_order_onetime<0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102102221 — 'kay then, let's get movin'!
- Japanese: `ほな、行くで！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102201111 — Royal Star
- Japanese: `ロイヤルスター`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102201121 — Delightful Memory
- Japanese: `ディライトフルメモリー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102201211 — Sky Drop
- Japanese: `天空落とし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&down_slope_random==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102202111 — Memories Become Power
- Japanese: `思い出を力に変えて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102202211 — Morrígan's Spear
- Japanese: `モリガンの矛戟`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102202221 — Ideal-Seeking Determination
- Japanese: `理想へ向かう覚悟`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=300","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102301111 — Exactly As Planned
- Japanese: `想定通り、余裕十分`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102301211 — Scheduled Cooldown
- Japanese: `計画的クールダウン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102302111 — VIP Back View
- Japanese: `VIPな後ろ姿`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&is_overtake==1&accumulatetime>=5","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102302211 — Full Power Santa Claus
- Japanese: `全力サンタクロース`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102303111 — Simulation Glasses: ON
- Japanese: `シミュレートグラス・オン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==2&distance_type==4&phase_firstquarter_random==2","effects":[{"modifier":6000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102303211 — Drawing a Neon Trail
- Japanese: `ネオンの尾を引いて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&running_style==2&phase_firsthalf_random==1","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""},{"baseDuration":40000,"condition":"is_activate_other_skill_detail==1&phase_laterhalf_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102401111 — You Copy?
- Japanese: `You copy?`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&corner==0","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102401211 — I Copy!
- Japanese: `I copy!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=1&is_lastspurt==1&hp_per>=1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":250,"target":1,"type":28},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102402111 — Snow White Whisper
- Japanese: `純白のささやき`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase==1&blocked_front_continuetime>=1","effects":[{"modifier":-300,"target":9,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102402211 — Barrel Roll
- Japanese: `バレルロール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&corner!=0","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102403111 — Going Ahead☆Tailwind
- Japanese: `お先に☆テールウィンド`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==4&running_style==1&is_lastspurt==1&corner==0&order==1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""},{"baseDuration":9000,"condition":"distance_type==4&running_style==1&is_lastspurt==1&corner==0&order<=3","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102403211 — Cockpit Magician
- Japanese: `コックピット・マジシャン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10241 — Victory Kiss ☆
- Japanese: `勝利のキッス☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&blocked_side_continuetime>=2&order<=3","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 102501111 — Coffee Break
- Japanese: `コーヒーブレイク`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102501211 — Don't Leave Me
- Japanese: `オイテイカナイデ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==1&order>=5","effects":[{"modifier":-100,"target":9,"type":9},{"modifier":350,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102502111 — Imminent Twilight
- Japanese: `迫りくる宵闇`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==4&is_lastspurt==1&corner==0","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102502211 — World of Marvels
- Japanese: `玄界領域`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==4&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102601111 — Overclocking
- Japanese: `クロックアップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102601211 — Overcomer of Difficulties
- Japanese: `困難を乗り越える者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_random==1&order<=3","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102602111 — Perfect Bugfixing Technique
- Japanese: `完璧なエラー対処術`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102602121 — Slightly Sweet Escape
- Japanese: `甘さ控えめエスケープ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==1&phase_laterhalf_random==1&order_rate<=50&base_wiz>=1200","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102602211 — Perfect Boot
- Japanese: `パーフェクトブート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"always==1","effects":[{"modifier":4000,"target":1,"type":10},{"modifier":100000,"target":1,"type":32}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102701111 — Muscle Anthem
- Japanese: `マッスルアンセム`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102701211 — Rising Bulk Up
- Japanese: `ライジングバルクアップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&is_finalcorner==1&corner!=0&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102702111 — Granting Dream-fulfilling Determination
- Japanese: `夢叶える決意を授けましょう`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&down_slope_random==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102702211 — Serving Victory Supreme
- Japanese: `至高の勝利を召し上がれ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"down_slope_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102702221 — Behold My Courageous Advance
- Japanese: `踏み出す勇気をご覧あれ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"down_slope_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10271 — Burning Muscles!
- Japanese: `燃えろ筋肉！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&corner!=0&order_rate>=65&order_rate<=70","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 102801111 — Flawless Mise en Place!
- Japanese: `下ごしらえ万全！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&phase_random==1","effects":[{"modifier":350,"target":1,"type":28},{"modifier":3000,"target":1,"type":31},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102801211 — Bono-style Gluttony
- Japanese: `ボーノな健啖家`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_laterhalf_random==1","effects":[{"modifier":350,"target":1,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102801221 — Hakkeyoi!
- Japanese: `はっけよい！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_random==1&distance_type==1","effects":[{"modifier":5500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102802111 — Beckoning Sugar Lantern
- Japanese: `手招きシュガーランタン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_random==1@distance_type==2&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102802211 — Fuel Up ☆ Pumpkin Power!
- Japanese: `満たせ☆ぱんぷきんパワー！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&distance_type==1&phase_firsthalf_random==2&order_rate<=50@running_style==2&distance_type==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""},{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102901111 — Admired City Girl
- Japanese: `憧れのシチーガール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"infront_near_lane_time>=1&is_lastspurt==1&hp_per>=1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":250,"target":1,"type":28}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102901211 — Seasoned Sledder's Swoop
- Japanese: `雪国仕込みの直滑降`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&down_slope_random==1","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102901221 — Steadfast Determination
- Japanese: `決意の根性娘`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&down_slope_random==1","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=300","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102902111 — One More Push!
- Japanese: `もうひとけっぱり！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&running_style==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102902211 — Snow Fluttering Through the Corner
- Japanese: `曲線に舞う深雪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"all_corner_random==1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 102902221 — Winter's Beauty Under the Waning Moon
- Japanese: `下弦の雪月花`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==1&distance_type==2&is_finalcorner_random==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==2&is_finalcorner_random==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103001111 — Determined Hero
- Japanese: `決意のヒーロー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&down_slope_random==1","effects":[{"modifier":3000,"target":1,"type":31},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103001211 — Black Assassin
- Japanese: `黒の刺客`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103002111 — I'll Do My Beeest!
- Japanese: `がんばるぞー…おー！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103002211 — Trick & Treat
- Japanese: `トリック&トリート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&order_rate<=50&temptation_opponent_count_behind>=1","effects":[{"modifier":-300,"target":20,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103003111 — Summit Meal
- Japanese: `山頂でイタダキマス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"up_slope_random_later_half==1&running_style==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103003211 — Blessing of Yodo
- Japanese: `淀の祝福`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10008","effects":[{"modifier":800000,"target":1,"type":2},{"modifier":800000,"target":1,"type":5},{"modifier":800000,"target":1,"type":1}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 103101111 — Wild Onee-chan
- Japanese: `じゃじゃウマお姉ちゃん`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&slope==1&accumulatetime>=10","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103101211 — Raging Wind God
- Japanese: `荒ぶる風神`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1&order<=3","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":-1500,"target":10,"type":21}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103102111 — Perfect Order!
- Japanese: `オーダーはバッチリ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"always==1","effects":[{"modifier":4000,"target":1,"type":10},{"modifier":100000,"target":1,"type":32}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103102211 — Brilliant Serving
- Japanese: `華麗なサーブ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103103111 — To the Best View!
- Japanese: `一番眺めのいい場所へ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==3&always==1","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103103211 — Let's Meet Under the Blue Sky!
- Japanese: `青空の下で待ってるよ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"behind_near_lane_time>=3&accumulatetime>=10&distance_type==3","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"behind_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103201111 — Pupil of Possibility
- Japanese: `可能性の徒`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_random==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103201211 — Efficient Recreation
- Japanese: `効率的休息法`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103202111 — Laplace's Demon
- Japanese: `ラプラスの悪魔`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==2&distance_type==3&base_speed>=1200&base_wiz>=1200","effects":[{"modifier":1000000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"running_style==2&distance_type==3&base_speed>=1200&base_wiz<1200","effects":[{"modifier":800000,"target":1,"type":1}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 103202211 — Dazzling Luxon
- Japanese: `眩耀のルクシオン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&running_style==2","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103203111 — FTL Particle
- Japanese: `光速を超える粒子`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50&distance_type==3","effects":[{"modifier":5000,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103203211 — Subject Observation
- Japanese: `被験体観察`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"near_count>=3&accumulatetime>=5&course_distance==2000","effects":[{"modifier":1500,"target":11,"type":27},{"modifier":3000,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"near_count>=3&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10321 — introduction：My body
- Japanese: `introduction：My body`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_rate>=50&corner!=0&order>=3&order_rate<=40","effects":[{"modifier":350,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 103301111 — Silent Oath
- Japanese: `静かな誓い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&infront_near_lane_time>=1&accumulatetime>=10","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103301211 — Immolated Comet
- Japanese: `己身焦がすほうき星`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_firsthalf_random==3&is_lastspurt==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase>=2&distance_diff_rate>=50"}],"rarity":6,"wisdomCheck":1}
```
---
## 103302111 — On Vultur Cadens' Trail
- Japanese: `アル・ワーキを追いかけて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&distance_type==3&phase_random==1&order_rate>=40&course_distance==2400","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"running_style==4&distance_type==3&phase_random==1&order_rate>=40","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103302211 — Melting of the Icy Star
- Japanese: `氷星融解`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_firsthalf_random==2&course_distance==2400","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==3&phase_firsthalf_random==2","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103401111 — Firefighter's Hashigo-nori
- Japanese: `火消の梯子登り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"activate_count_middle>=3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103401211 — Sandstorm Wielder
- Japanese: `熟練の砂塵使い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"ground_type==2&phase_random==1&order_rate>=50","effects":[{"modifier":750,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103401221 — Stylish and Masterful
- Japanese: `粋でいなせな達人技`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_random==1&order_rate>=50","effects":[{"modifier":350,"target":1,"type":9},{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103402111 — Fan Dance
- Japanese: `扇ノ舞`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&is_finalcorner==1&corner!=0&lane_type==0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103402211 — Dramatic Finale
- Japanese: `大見得切り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==4&is_lastspurt==1&corner==0","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103402221 — Fleet Foot of Idaten
- Japanese: `韋駄天ノ襲脚`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==4&is_lastspurt==1&corner==0&distance_type==4","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_finalcorner==1&corner!=0","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103501111 — Tireless Effort
- Japanese: `たゆまぬ努力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&is_overtake==1&accumulatetime>=5","effects":[{"modifier":3000,"target":1,"type":31},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103501211 — Winning Road
- Japanese: `ウイニングロード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103502111 — Ten Million Horsepower!!!
- Japanese: `千万バリキ！！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&up_slope_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103502211 — You'll fly for sure!
- Japanese: `きっと飛べる！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&is_last_straight==1&phase>=2&order_rate>=20&order_rate<=60","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103503111 — All-Out Excitement!!
- Japanese: `全・力・ワク・ワク！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_laterhalf_random==1&order>=4&track_id==10006&course_distance==2400","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==3&phase_laterhalf_random==1&order>=4","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103503211 — Dreamer's Path
- Japanese: `Dreamer's Path`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==1&order_rate>=40&order_rate<=90","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10351 — Full Power V Sign!
- Japanese: `全力Vサインッ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&order<=5","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"is_finalcorner==1&blocked_side_continuetime>=2"}],"rarity":3,"wisdomCheck":0}
```
---
## 103601111 — Uplifting
- Japanese: `アップリフティング`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103601211 — Lose Myself
- Japanese: `Lose Myself`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103602111 — Gluttony's Grip
- Japanese: `Gluttony's Grip`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":-100,"target":9,"type":9},{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103602121 — Noise Cancellation
- Japanese: `ノイズキャンセリング`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase==1&change_order_onetime>0&order_rate>=50&order_rate<=80","effects":[{"modifier":-100,"target":9,"type":9},{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103602211 — Torment
- Japanese: `刑苦`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&is_finalcorner==1&corner!=0&lane_type==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103701111 — Flash Magier
- Japanese: `閃光のマギア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==2","effects":[{"modifier":350,"target":1,"type":28},{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103701211 — Betting My Pride
- Japanese: `誇りを懸けて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103702111 — Recipe of Victory
- Japanese: `勝利のレシピ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103702121 — Perfect Preparation
- Japanese: `仕込みは完璧`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103702211 — Black Flash
- Japanese: `黒い閃光`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&straight_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103703111 — Ritter von Fuchu
- Japanese: `Ritter von Fuchu`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10006","effects":[{"modifier":800000,"target":1,"type":2},{"modifier":800000,"target":1,"type":5},{"modifier":800000,"target":1,"type":1}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 103703211 — Flash Torrent
- Japanese: `閃光の奔流`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==1&track_id==10006","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""},{"baseDuration":40000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-300,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103801111 — #Cute Perturbation♪
- Japanese: `#カワイイかく乱♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==2&order_rate<=50","effects":[{"modifier":-50000,"target":10,"type":8},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103801211 — #Go Crazy♪
- Japanese: `#夢中になっちゃえ♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==0&order_rate<=50&accumulatetime>=5","effects":[{"modifier":-2500,"target":10,"type":21},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103802111 — #WannaGetCurren'd?
- Japanese: `#カレンに染まってみる？`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==0&order_rate<=50&accumulatetime>=5","effects":[{"modifier":-2500,"target":10,"type":21},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103802121 — Enthralling Glitter
- Japanese: `心奪われる閃光`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&phase_laterhalf_random==0&order_rate<=50&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103802211 — #Beauty Sprint
- Japanese: `#ビューティースプリント`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103901111 — Non-stop Princess
- Japanese: `ノンストッププリンセス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=1&is_lastspurt==1&hp_per>=1","effects":[{"modifier":5000,"target":1,"type":31},{"modifier":250,"target":1,"type":28}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103901211 — Raging Dragon
- Japanese: `暴れ龍`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&is_finalcorner==1&corner!=0&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103902111 — Top Princess!
- Japanese: `トップ・オブ・ザ・姫！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&is_last_straight==1&order>=2&distance_diff_top<=10","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103902121 — The Bestest Princess
- Japanese: `最っっっ高のプリンセス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&running_style==3&is_last_straight==1&track_id==10008","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==3&running_style==3&is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 103902211 — Fiery Princess☆Sudden Descent!!
- Japanese: `爆走猛姫☆急転直下！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&down_slope_random==1@distance_type==3&down_slope_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104001111 — Prescience
- Japanese: `先見の明`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_laterhalf_random==0&order_rate>50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":-2000,"target":9,"type":21},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104001211 — Star of the Runway
- Japanese: `ランウェイの主役`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104001221 — To the Finale's Forefront
- Japanese: `フィナーレの先頭へ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=201&remain_distance>=199","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104002111 — Vivid Battle Formation
- Japanese: `鮮やかな布陣`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_random==0&order_rate>50&accumulatetime>=3","effects":[{"modifier":-3000,"target":9,"type":31},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104002211 — Eagle-eyed
- Japanese: `虎視眈々`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_laterhalf_random==0&order_rate>=40","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104003111 — Wild Runway
- Japanese: `Wild Runway`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=30&order_rate<=80","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":5500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104003211 — Golden Flare
- Japanese: `黄金の炎陽`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&base_power>=1200&order_rate>=40","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==3&phase_random==1&base_power>=1200","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104101111 — Bakushin Sprint!
- Japanese: `バクシン的スプリント！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104101211 — Bakushin Lead!
- Japanese: `バクシン的リード！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase==1&bashin_diff_behind>=3&order==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104102111 — Red-hot Rush! Bakushin Road!
- Japanese: `猪突猛進！バクシンロード！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104102211 — Bakushin! Bakushin! Bakushiiin!
- Japanese: `驀進！爆進！バクシーン！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&straight_random==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10411 — Class President + Speed = Bakushin
- Japanese: `学級委員長+速さ＝バクシン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order<=3&blocked_side_continuetime>=2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 104201111 — World-wide Supreme Brilliance
- Japanese: `世界を貫く至高の輝き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&straight_random==1@distance_type==2&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104201211 — Pearl-style Dance Battle
- Japanese: `パール流ダンスバトル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&is_overtake==1&accumulatetime>=5@distance_type==1&is_overtake==1&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104202111 — Riding the Mistral
- Japanese: `ミストラルに乗って`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_first_half_straight_random==2&track_id==10006&distance_type==1@phase_first_half_straight_random==2&track_id==10006&distance_type==2","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"phase_straight_random==2&track_id!=10006&distance_type==1@phase_straight_random==2&track_id!=10006&distance_type==2","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104202211 — Shining From The Ocean Floor...☆
- Japanese: `海の底からキラめいて…☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_corner_random==1&is_finalcorner==1&corner!=0&distance_type==1@phase_corner_random==1&is_finalcorner==1&corner!=0&distance_type==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"phase_corner_random==1&distance_type==1@phase_corner_random==1&distance_type==2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104301111 — Full Speed Ahead, Nanoda!
- Japanese: `全速前進なのだ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==3&order_rate<=50&is_lastspurt==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104301211 — Masterful Prankster
- Japanese: `いたずらマイスター`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==2&ground_condition==3@ground_type==2&ground_condition==4","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 104301221 — Mud Demon Lord
- Japanese: `泥んこ魔王様`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==2&ground_condition>=3","effects":[{"modifier":400000,"target":1,"type":1},{"modifier":400000,"target":1,"type":3},{"modifier":200000,"target":1,"type":32}],"precondition":""},{"baseDuration":-1,"condition":"ground_type==2&ground_condition<=2","effects":[{"modifier":400000,"target":1,"type":1},{"modifier":400000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 104401111 — After-School Magical Girl
- Japanese: `放課後魔法少女`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&slope==2&accumulatetime>=10","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104401211 — Charm Magic
- Japanese: `チャームマジック`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_random==2&order>=2","effects":[{"modifier":-2500,"target":4,"type":21},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104401221 — Salvia☆Splendens
- Japanese: `サルビア☆スプレンデンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&phase_random==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104402111 — Sylphid Magia
- Japanese: `シルフィード・マギア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"course_distance==2200&running_style==4&phase_firstquarter_random==2","effects":[{"modifier":5000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""},{"baseDuration":12000,"condition":"course_distance!=2200&running_style==4&phase_firsthalf_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104402121 — Nox Lumina
- Japanese: `ノクス・ルミナ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==3&running_style==4&phase_firstquarter_random==2&course_distance==2000","effects":[{"modifier":3000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9},{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":12000,"condition":"distance_type==3&running_style==4&phase_firstquarter_random==2","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104402211 — Emergency Magic Boost
- Japanese: `緊急魔力ブースト`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104501111 — Sweet Bewitching
- Japanese: `あま～い幻惑`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_random==2&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104501211 — Healing Maestro
- Japanese: `癒しのマエストロ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&corner!=0","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104502111 — Professional Pamperer
- Japanese: `お世話のプロフェッショナル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104502211 — Charming Mummy Whisper
- Japanese: `魅惑のマミーウィスパー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&phase==1&blocked_front_continuetime>=1","effects":[{"modifier":-300,"target":9,"type":9},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104503111 — Run as the River Flows
- Japanese: `流水流走`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&running_style==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104503211 — Butterfly Transformation Jutsu
- Japanese: `神仙蝶変の術`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&running_style==2&phase==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"distance_diff_top<=15&distance_rate>=60&phase==1"}],"rarity":6,"wisdomCheck":1}
```
---
## 10451 — Clear Heart
- Japanese: `クリアハート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase_random==1&order>=2&order_rate<=40","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 104601111 — The Dazzling Umadol's Here★
- Japanese: `大注目のウマドル参上★`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_random==0","effects":[{"modifier":450,"target":1,"type":28}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104601121 — No Looking Away☆
- Japanese: `目を逸らしちゃダメだよ☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_random==2","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104601211 — Umadol Power Trend ↑↑
- Japanese: `ウマドルパワー急上昇↑↑`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase==1&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104602111 — Trending Towards Your Dreams!
- Japanese: `夢に向かって急上昇！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase==1&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104602121 — To the Ultimate Stage!
- Japanese: `最高峰のステージに！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase==1&blocked_side_continuetime>=2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104602211 — Absolute Center!
- Japanese: `絶対的センター！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==2&order_rate<=50","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104603111 — Taking Center Stage!
- Japanese: `立ち位置ゼロ番！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"always==1","effects":[{"modifier":4000,"target":1,"type":10},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104603211 — Fanservice For You☆
- Japanese: `爆レスあげちゃう☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&running_style==1&phase==1&is_activate_any_skill==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_activate_any_skill==1","effects":[{"modifier":2500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104701111 — Hero Handbook
- Japanese: `英雄への道標`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104701121 — Story Weaver
- Japanese: `物語を紡ぐ者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":150,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104701211 — Shining Sword
- Japanese: `光輝く剣`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&all_corner_random==1@distance_type==4&all_corner_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104702111 — Heroic Radiance
- Japanese: `勇躍閃々`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_latter_half_straight_random==1&running_style==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104702211 — The Stormforged Hero Advances
- Japanese: `嵐纏いし英雄は往く`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==3@season==4","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 104801111 — Get Those Vibes Up!
- Japanese: `ノってこ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&phase_firsthalf_random==2@running_style==2&phase_firsthalf_random==2","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104801211 — Trend Planner
- Japanese: `トレンドプランナー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1@running_style==3&phase_random==1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104802111 — Taking Every Chance!
- Japanese: `ワンチャンまくったる！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&is_finalcorner_random==1&order_rate>=40&track_id==10006","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":18000,"condition":"distance_type==3&is_finalcorner_random==1&order_rate>=40&track_id!=10006","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104802211 — Can't Top Me!
- Japanese: `あたししか勝たん！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&distance_type==3&is_finalcorner_random==1&order_rate>=30&order_rate<=80&track_id==10006","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""},{"baseDuration":24000,"condition":"running_style==3&is_finalcorner_random==1&order_rate>=30&order_rate<=80&track_id!=10006&distance_type!=3@running_style==3&is_finalcorner_random==1&order_rate>=30&order_rate<=80&track_id==10006&distance_type!=3@running_style==3&is_finalcorner_random==1&order_rate>=30&order_rate<=80&track_id!=10006&distance_type==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104802221 — Simply the Best!
- Japanese: `あたしサイコーじゃん！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&distance_type==3&phase_firsthalf_random==2&order_rate>=30&order_rate<=80&track_id==10006","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==3&distance_type==3&phase_firsthalf_random==2&order_rate>=30&order_rate<=80","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104803111 — Hop On ☆ Hype Train
- Japanese: `乗っとけ☆ぶち上げペース`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_straight_random==1&distance_diff_top>=10@distance_type==4&phase_straight_random==1&distance_diff_top>=10","effects":[{"modifier":4000,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"distance_type==3&phase_straight_random==1@distance_type==4&phase_straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104803211 — Now's the Time to Go Wild!
- Japanese: `ここ、カマしどきっしょ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==2&phase>=2&is_finalcorner==1&corner!=0&course_distance>=2000&distance_type!=4@running_style==3&phase>=2&is_finalcorner==1&corner!=0&course_distance>=2000&distance_type!=4","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"running_style==2&phase>=2&is_finalcorner==1&corner!=0&course_distance>=2000&distance_type==4@running_style==3&phase>=2&is_finalcorner==1&corner!=0&course_distance>=2000&distance_type==4","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104901111 — All or Nothing
- Japanese: `乾坤一擲の大博打`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_rate_after_random==50","effects":[{"modifier":220,"target":1,"type":27},{"modifier":-400,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104901211 — Hot-blooded Gambler
- Japanese: `鉄火のギャンブラー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"popularity<=3&random_lot==30","effects":[{"modifier":1000000,"target":1,"type":1},{"modifier":1000000,"target":1,"type":3},{"modifier":1000000,"target":1,"type":4}],"precondition":""},{"baseDuration":-1,"condition":"popularity>=4&random_lot==60","effects":[{"modifier":1000000,"target":1,"type":1},{"modifier":1000000,"target":1,"type":3},{"modifier":1000000,"target":1,"type":4}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 104902111 — All in on One Bet
- Japanese: `一点張りでいこう`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&is_last_straight==1&distance_diff_top<=10&distance_type==3&change_order_up_end_after>=1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==3&is_last_straight==1&distance_diff_top<=10","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 104902211 — Gambler's Stratagem
- Japanese: `勝負師の才略`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"phase_laterhalf_random==0&distance_type==3@phase_laterhalf_random==0&distance_type==4","effects":[{"modifier":-1500,"target":1,"type":21}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase_firsthalf_random==2","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105001111 — Menacing Presence
- Japanese: `鬼気森然`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_random==1&distance_diff_rate>=75","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105001211 — Spurring Emotions
- Japanese: `駆り立てる想い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==4&is_lastspurt==1&corner==0","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105002111 — I'll Show You!
- Japanese: `見せつけてやる！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_random==1&running_style==4&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":28}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105002211 — Recovery Output
- Japanese: `起死回生の出力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105003111 — Zero Latency
- Japanese: `ゼロレイテンシ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105003211 — Indomitable Limit Breaker
- Japanese: `不撓のLimit Breaker`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&is_last_straight==1&order>=2&distance_diff_top<=10","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105101111 — Flurry Dash
- Japanese: `風花疾走`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105101121 — A Petal's Bravery
- Japanese: `一輪の勇気`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105101211 — Large-Petaled Resolution
- Japanese: `大輪の決意`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&down_slope_random==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105102111 — Flower Girl's Blessing
- Japanese: `祝福のフラワーガール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&all_corner_random==1","effects":[{"modifier":1500,"target":11,"type":27},{"modifier":3000,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105102211 — Veil-Swaying Spring Storm
- Japanese: `ヴェール揺らす春疾風`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&down_slope_random==1@distance_type==2&down_slope_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105102221 — Blooming in Sickness and in Health
- Japanese: `末永く、寄り添う花`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&down_slope_random==1","effects":[{"modifier":1500,"target":11,"type":27},{"modifier":3000,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105201111 — Not Done Yet!
- Japanese: `まだまだだよ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"phase<=1&accumulatetime>=5&blocked_front_continuetime>=1","effects":[{"modifier":750,"target":1,"type":9},{"modifier":350,"target":1,"type":28}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105201211 — I Won't Lose!
- Japanese: `まけないからね！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&change_order_onetime>0","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105202111 — Look At Me, Look!
- Japanese: `見てて見てて！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==0","effects":[{"modifier":450,"target":1,"type":28},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105202121 — I Really Wanna Win!
- Japanese: `勝ちたいんだもん！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==2","effects":[{"modifier":450,"target":1,"type":28},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105202211 — Trying My Best!
- Japanese: `がんばるもん！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&is_overtake==1&accumulatetime>=5","effects":[{"modifier":3000,"target":1,"type":31},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10521 — Ready, Steady, Go!
- Japanese: `ワクワクよーいドン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"is_finalcorner==1&corner!=0&order_rate>50&near_count>=1","effects":[{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 105301111 — Gateway To Discipline
- Japanese: `風紀の登龍門`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&is_finalcorner==1&corner!=0&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105301121 — Dragon and Tiger's Battle
- Japanese: `龍虎相搏`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&running_style==3&is_finalcorner==1&corner!=0&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105301211 — Osu! I'm Fired Up!
- Japanese: `押忍ッ！気合十分っス！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&is_finalcorner_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105302111 — Hot-blooded Riding!
- Japanese: `熱血進化ライディング！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=201&remain_distance>=199","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105302211 — Special Move! Explosive Sprint!
- Japanese: `必殺！爆速スプリント！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=201&remain_distance>=199","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105401111 — Emergency! Hero on the Scene!
- Japanese: `急行！ヒーロー参上！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105401211 — Special Move: Lightning Kiiick!
- Japanese: `必殺・雷電キーック！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2&order_rate>50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10541 — Pegasus Full Power!
- Japanese: `ペガサスフルパワー！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"remain_distance<=150&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"order_rate>=45&distance_rate>=50&change_order_onetime<0"}],"rarity":3,"wisdomCheck":0}
```
---
## 105501111 — Exciting☆Marvelous Zone
- Japanese: `ワクワク☆マーベラスゾーン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate>=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105501121 — Marvelous Momentum☆
- Japanese: `ギュンギュンのマーベラス☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105501211 — Marvelous World Plan☆
- Japanese: `進め！世界マーベラス計画☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=1&is_lastspurt==1&hp_per>=1&remain_distance>=600","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":250,"target":1,"type":28},{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"infront_near_lane_time>=1&is_lastspurt==1&hp_per>=1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":250,"target":1,"type":28}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105502111 — Sparkle ☆ Dolly Stage
- Japanese: `煌めき☆ドーリィステージ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"activate_count_all>=13&course_distance>=2000&running_style==3&weather==1","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"activate_count_all>=13&course_distance>=2000&running_style==3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105502211 — Marvelous Showtime ♪
- Japanese: `いざ、ショーベラスタイム♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_wiz>=1200&distance_type==3&ground_condition==1@base_wiz>=1200&distance_type==4&ground_condition==1","effects":[{"modifier":1000000,"target":1,"type":5},{"modifier":1000000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"base_wiz>=1200&distance_type==3&ground_condition!=1@base_wiz>=1200&distance_type==4&ground_condition!=1","effects":[{"modifier":600000,"target":1,"type":5},{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 105601111 — Lucky Omen!
- Japanese: `吉兆です！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&phase_random==2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105601211 — Seven Heavenly Fortunes
- Japanese: `七福即生`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"post_number==7","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":2},{"modifier":800000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105602111 — Tempestuous Ultra Luck Power!
- Japanese: `怒涛の超幸運パワー！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&phase==2&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105602121 — Lucky Mad Rush!
- Japanese: `怒涛のラッキー大猛進！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==4&phase==2&is_overtake==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"is_activate_other_skill_detail==1&phase_firsthalf==3&is_overtake==1&is_lastspurt==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105602211 — First-hand Rising Fortune!
- Japanese: `ばっちり開運体験！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&is_finalcorner==1&corner!=0&lane_type==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10561 — Come, Come!
- Japanese: `来てください来てください！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&order>=3&blocked_front==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 105701111 — Soaring Step
- Japanese: `天翔る足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&corner_random==3&order_rate>=50@distance_type==4&corner_random==3&order_rate>=50","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105701211 — Supple Land
- Japanese: `弾む大地`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==4&is_lastspurt==1&corner==0","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105701221 — Dancing Flourish
- Japanese: `踊る脚色`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==3&running_style==4&phase_firstquarter==2&corner==0@distance_type==3&running_style==4&phase_firstquarter_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105702111 — Mesmerizing Somersault
- Japanese: `奪目の宙乗り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&corner_random==3@distance_type==4&corner_random==3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":"distance_rate>=50&change_order_onetime<0"},{"baseDuration":30000,"condition":"distance_type==3&corner_random==3@distance_type==4&corner_random==3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105702211 — Step Up and Behold!
- Japanese: `さァさ、お立ち合い！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==4&distance_type==4&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""},{"baseDuration":12000,"condition":"running_style==4&distance_type==4&phase_firstquarter_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105801111 — Tempestuous Speed
- Japanese: `怒涛のスピード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105801211 — I'm Not Giving Up!
- Japanese: `諦めない、ですぅ～！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&change_order_onetime>0","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105802111 — I've Got a Rival After All!
- Japanese: `ライバルがいるから！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105802121 — Fervent Determination
- Japanese: `心に灯す闘志`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105802211 — Soul Guide
- Japanese: `魂の導き手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&corner!=0","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105901111 — Cool Gaze
- Japanese: `クールな視線`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_random==2&order_rate>50","effects":[{"modifier":-300,"target":4,"type":9},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105901121 — Fluttering Towards Glory
- Japanese: `栄光への羽ばたき`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105901211 — Queen of Yodo
- Japanese: `淀の女王`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10008","effects":[{"modifier":800000,"target":1,"type":2},{"modifier":800000,"target":1,"type":5},{"modifier":800000,"target":1,"type":1}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 105902111 — I Want To Be More Adventurous!
- Japanese: `もっと冒険してみたい！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&distance_rate_after_random==50&order_rate>=30&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105902121 — Step with Confidence
- Japanese: `自信持って踏み出して`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&distance_rate_after_random==50","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 105902211 — First Step To Recovery
- Japanese: `起死回生の一歩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106001111 — Charming Cynical Girl
- Japanese: `魅惑のシニカルガール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase>=2&blocked_front_continuetime>=1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106001211 — Aim for the Leading Role!
- Japanese: `目指せ！主人公！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106002111 — Guess I've Gotta Try
- Japanese: `頑張るしかないよね`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106002211 — Non-stop Cheer
- Japanese: `ノンストップエール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=1&is_lastspurt==1&hp_per>=1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":250,"target":1,"type":28},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106003111 — Tasty, Isn't It?
- Japanese: `いい味、出てるでしょ？`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106003211 — Year-End Cleaning Pro
- Japanese: `大掃除上手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106003221 — Pump-Up Pro
- Japanese: `盛り上げ上手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&running_style==3&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31},{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10601 — You Know, Sometimes Even I Can...
- Japanese: `アタシもたまには、ね？`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&order==3&bashin_diff_behind<=1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 106101111 — Electrifying Sweep
- Japanese: `電撃の撫で切り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&phase_random==2&order_rate>50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106101211 — King's Perspective
- Japanese: `王の大局観`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":150000,"target":1,"type":8},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106102111 — Like Riding a Dragon's Cloud
- Japanese: `竜の雲を得る如し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&is_finalcorner==1&corner!=0&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106102211 — As Spring Blooms, the Sakura Dance
- Japanese: `春風吹きて、桜舞う`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==1@season==5","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 106103111 — Unobstructable
- Japanese: `遮るものはない`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2@distance_type==2&phase_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106103211 — Proof of Indomitability
- Japanese: `不屈の証明`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate>=40@distance_type==2&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106103221 — First-Class Presence
- Japanese: `一流の在り方`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10611 — Call me KING
- Japanese: `Call me KING`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"temptation_count==0&remain_distance<=201&remain_distance>=199&order>=4&order_rate<=70","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 106201111 — Going My Way
- Japanese: `ゴーイングマイウェイ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&is_surrounded==1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106201211 — Ei! Ei! Mun!
- Japanese: `えい！えい！むん！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase==2&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106202111 — Positive Smile
- Japanese: `ポジティブスマイル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==3&phase_firsthalf_random==1","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106202211 — Big Comeback
- Japanese: `大どんでんがえし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106202221 — Oopsy-Doopsy
- Japanese: `やばしやばし！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=300","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10621 — Ready, Bang!
- Japanese: `レディー、どんっ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&phase==1&order>=3&order_rate<=70","effects":[{"modifier":350,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 106301111 — Thorough Planning
- Japanese: `徹底管理プラン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&distance_rate>=50&distance_rate<=51@running_style==3&distance_rate>=50&distance_rate<=51","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106301211 — Red-Hot Spark
- Japanese: `鉄火花`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&distance_rate>=50&distance_rate<=51@running_style==3&distance_rate>=50&distance_rate<=51","effects":[{"modifier":5500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106302111 — Rowing Beneath Plum Blossoms
- Japanese: `梅仰ぎ、漕ぐ計路`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_speed>=1000&base_power>=1000&distance_type==2@base_speed>=1000&base_power>=1000&distance_type==3","effects":[{"modifier":600000,"target":1,"type":32}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 106302211 — Treading the Spring Path
- Japanese: `春道踏破`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50&distance_type==3","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10631 — Strike and Strengthen
- Japanese: `打ち、鍛えて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"is_lastspurt==1&phase==3&temptation_count==0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 106401111 — Dope Stuff!
- Japanese: `パないっしょ？`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"behind_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106401211 — Godly Runner's Wisdom
- Japanese: `神逃げの心得`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&phase_random==1&bashin_diff_behind>=1&order==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106401221 — Pump It Up
- Japanese: `テンアゲスタイル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase==1&blocked_side_continuetime>=2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106402111 — North Wind Kick
- Japanese: `北風一蹴`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106402211 — Merry☆Christmas↑Party
- Japanese: `メリ☆クリ↑パーリー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_random==1&track_id==10005&motivation==5&is_used_skill_id==202051","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":550,"target":1,"type":9}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==4&phase_random==1&track_id==10005&motivation<=4&is_used_skill_id==202051@distance_type==4&phase_random==1&track_id!=10005&is_used_skill_id==202051","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106501111 — Hella Vibes Up!
- Japanese: `マジ爆上げっしょ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106501211 — Just Do It!
- Japanese: `とりまやったれ～！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106502111 — Ahead of the Trend☆
- Japanese: `トレンド先取り☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106502211 — Emergence of the Mile☆God
- Japanese: `マイル神、爆☆誕`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106601111 — Ten Million Percent Output!!
- Japanese: `出力1000万%！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":27000,"condition":"phase_firsthalf_random==1&running_style==1","effects":[{"modifier":5500,"target":1,"type":27},{"modifier":-400,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106601211 — Keep Up with Turbo!
- Japanese: `ターボについてこーい！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10661 — Engine Ignition!
- Japanese: `エンジン点火！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":130000,"condition":"distance_rate>=34&distance_rate<=36&order==1&bashin_diff_behind>=1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":5000000,"condition":"phase==3&is_activate_other_skill_detail==1","effects":[{"modifier":-500,"target":1,"type":21}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 106701111 — Adamantine
- Japanese: `金剛不壊`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_laterhalf_random==0&order_rate>=40","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106701121 — Unconcealed Brilliance
- Japanese: `隠せぬ輝き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_laterhalf_random==0&order_rate>=40","effects":[{"modifier":150,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106701211 — Clockwise Rondo
- Japanese: `右回りの輪舞曲`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==1","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 106702111 — Realm of No-Self
- Japanese: `無我の境地`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==4&running_style==3&is_lastspurt==1&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":-50,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106702211 — Dawn Always Comes!
- Japanese: `明けぬ夜はない！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==1&order>=5","effects":[{"modifier":-100,"target":9,"type":9},{"modifier":350,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106703111 — Azure Revolution
- Japanese: `蒼色革命`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106703211 — Danse de L'Epée
- Japanese: `ダンス・デ・レぺ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"track_id==10201&distance_type==3&all_corner_random==1&motivation==5","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"track_id!=10201&distance_type==3&all_corner_random==1@track_id==10201&all_corner_random==1&motivation<=4&distance_type==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106801111 — Festival Shout!
- Japanese: `祭りだワッショイ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106801211 — Blast Flash
- Japanese: `爆風一閃！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&straight_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106801221 — Passionate Dance Parade
- Japanese: `熱踊の花道`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&straight_random==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106802111 — Leap Towards The Future!
- Japanese: `未来へ飛び立ちましょう！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106802211 — Preamble of Victory!
- Japanese: `必勝の前口上！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106803111 — Unleash the Dragon
- Japanese: `あっぱれ！臥竜勇往`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==1&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106803211 — Thousand Mile Cheer!
- Japanese: `万里飛び越えソイヤッ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==4&running_style==1&is_lastspurt==1&corner==0&order<=3","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106901111 — Pretty Blossoms, Pretty Year!
- Japanese: `お花見当たり年！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106901121 — Rather Run than Worry!
- Japanese: `案ずるより走るが速し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&running_style==2&phase_corner_random==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106901211 — In Ninefold Bloom
- Japanese: `けふ九重に満開です`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==1@season==5","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 106902111 — Trail of Blooming Sakura
- Japanese: `桜花爛漫一直線`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 106902211 — I Don't Want to Lose!
- Japanese: `負けたくない！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase==1&order_rate<=80&order_rate>=30&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107001111 — Unwavering Aster
- Japanese: `揺るがぬアスター`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase>=2&is_last_straight==1&order_rate>=20&order_rate<=60","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107001211 — Brightest Star's Arabesque
- Japanese: `一等星のアラベスク`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107001221 — Reminiscent Träumerei
- Japanese: `追想のトロイメライ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_firsthalf_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107002111 — I Like a Rough Road
- Japanese: `悪路のほうが好みでね`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==2&ground_type==1@ground_condition==3&ground_type==1@ground_condition==4&ground_type==1","effects":[{"modifier":800000,"target":1,"type":3},{"modifier":800000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"ground_condition==1&ground_type==1","effects":[{"modifier":600000,"target":1,"type":3},{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 107002211 — Beat the Stars
- Japanese: `Beat the Stars`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firstquarter_random==2&order_rate>=30&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":"ground_condition==2@ground_condition==3@ground_condition==4"},{"baseDuration":30000,"condition":"distance_type==3&phase_firstquarter_random==2&order_rate>=30&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":"ground_condition==1"}],"rarity":6,"wisdomCheck":1}
```
---
## 107101111 — Eternal Brilliance
- Japanese: `永遠の輝き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107101211 — Moment's Readiness
- Japanese: `刹那への覚悟`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_last_straight==1&phase>=2&order_rate>=20&order_rate<=60","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107102111 — Beautiful Phosphorescence
- Japanese: `美しき燐光`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_laterhalf_random==1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107102121 — Mystic Flame
- Japanese: `幽玄の灯火`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_firsthalf_random==1","effects":[{"modifier":350,"target":1,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107102211 — Ephemeral Afterglow
- Japanese: `淡く儚い残照`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&distance_type==3&is_last_straight==1&phase>=2","effects":[{"modifier":5500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107201111 — Stirring Flame
- Japanese: `昂る焔`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107201211 — Layered Determination
- Japanese: `八重の向こう意気`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_finalcorner==1&overtake_target_time>=2","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107201221 — Ardent Desire for Victory
- Japanese: `勝利に焦がれる激情`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&is_finalcorner==1&is_overtake==1&distance_type==3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107202111 — General's Swift Strike
- Japanese: `将の疾刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==2&phase>=2&is_finalcorner==1&corner!=0&remain_distance>=600&order_rate<=70@running_style==3&phase>=2&is_finalcorner==1&corner!=0&remain_distance>=600&order_rate<=70","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107202211 — Peerless Pursuit
- Japanese: `無双の追撃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&distance_rate>=50&is_overtake==1&lane_type==0@running_style==3&distance_rate>=50&is_overtake==1&lane_type==0","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==2&distance_rate>=50&is_overtake==1@running_style==3&distance_rate>=50&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107301111 — Slash of a Thousand Trials
- Japanese: `千辛万苦切り裂く刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&all_corner_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107301211 — Surging Crescent Moon
- Japanese: `迸る月流星`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 10731 — Steel Your Heart, Tsuyoshi!
- Japanese: `心、強し！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&change_order_up_end_after>=1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 107401111 — Indomitable Dame
- Japanese: `不屈のお嬢様`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&change_order_onetime>0","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107401211 — Immovable as Mt. Youtei
- Japanese: `動かざること羊蹄山の若し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&phase_firsthalf_random==1&order_rate>=40&order_rate<=80","effects":[{"modifier":950,"target":1,"type":9},{"modifier":-1500,"target":1,"type":21}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107402111 — Heavenly Road of the Holy Night
- Japanese: `聖夜の天路`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"running_style==3&phase_random==1&base_stamina>=1200","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"running_style==3&phase_random==1&base_stamina<1200","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107402211 — Snowflake Pursuit
- Japanese: `雪華の追い上げ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==4&phase==2&change_order_onetime<0&base_stamina>=1200","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"distance_type==4&phase==2&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107601111 — Advancing Sakura Front!
- Japanese: `桜前線進行中！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107601211 — Let's Bloom in the Moment!
- Japanese: `一花咲かせましょう！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==3&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107602111 — First Sky, Flower Feast
- Japanese: `初空高く、花宴`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_stamina>=1200","effects":[{"modifier":800000,"target":1,"type":2},{"modifier":800000,"target":1,"type":1}],"precondition":"distance_type==3@distance_type==4"}],"rarity":6,"wisdomCheck":0}
```
---
## 107602211 — Spring Awakened: Lumière
- Japanese: `春めき、Lumière`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&running_style==3&distance_rate>=50&is_overtake==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107701111 — Turf Protagonist
- Japanese: `ターフの主人公`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==1&ground_type==1","effects":[{"modifier":800000,"target":1,"type":3},{"modifier":800000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"ground_condition!=1&ground_type==1","effects":[{"modifier":400000,"target":1,"type":3},{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 107701211 — The Right Path
- Japanese: `正道`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":9000,"condition":"is_activate_other_skill_detail==1&is_lastspurt==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107702111 — Single-Minded Santa Claus
- Japanese: `ひたむきサンタクロース`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_firsthalf_random==1","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107702211 — Leave the Dark Nights to Me!
- Japanese: `暗い夜道もお任せを！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_laterhalf_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-400,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107801111 — Wind Shear
- Japanese: `ウインドシアー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107801211 — Divine Crossing
- Japanese: `神渡し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&order>=2&distance_diff_top<=5&distance_rate>=60&phase==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107801221 — Heavenly Wind
- Japanese: `天つ風`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&order>=3&distance_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107802111 — Dust Devil Manifest
- Japanese: `塵旋風となりて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107802211 — Sylph Spirit
- Japanese: `シルフ・スピリット`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&distance_type==2&distance_diff_top<=10&distance_rate>=60","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107901111 — Guidance of the Sea Breeze
- Japanese: `潮風の導き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&phase_straight_random==1&ground_type==2@distance_type==3&phase_straight_random==1&ground_type==2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==2&phase_straight_random==1@distance_type==3&phase_straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 107901211 — Brave Advance
- Japanese: `勇船直往`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&remain_distance<=200@running_style==2&remain_distance<=200","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":"compete_fight_count>0"}],"rarity":6,"wisdomCheck":1}
```
---
## 108001111 — Information Broker
- Japanese: `情報強者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&activate_count_start>=3@distance_type==3&activate_count_start>=3","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==1&activate_count_start>=3@distance_type==4&activate_count_start>=3","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108001211 — Seeking the Unknown
- Japanese: `『未知』を求めて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108002111 — Victory Path Domination
- Japanese: `勝ち筋ドミネーション`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"activate_count_start>=3&distance_type==2@activate_count_start>=3&distance_type==3","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_badstart==0&is_lastspurt==1","effects":[{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108002211 — Not Gonna Miss This Chance☆
- Japanese: `ここ、逃す手はないってね☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&corner_random==3&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_other_character_activate_advantage_skill==27@is_activate_other_skill_detail==1&is_other_character_activate_advantage_skill==22","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108101111 — Whack Them Silly!
- Japanese: `ベッコベコに凹ます！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"order_rate<=50&ground_type==2&phase_firstquarter_random==2&course_distance<=1800","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":18000,"condition":"order_rate<=50&ground_type==2&phase_firsthalf_random==2&course_distance>1800","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108101211 — I'll Take Anyone On!
- Japanese: `相手が誰でも関係ねーし！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==2&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108201111 — With A Sparkling Heart!
- Japanese: `ココロ、キラめくままに！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase==1&change_order_onetime<0&base_wiz>=1200","effects":[{"modifier":4000,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"phase==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108201211 — Enjoy the Flight
- Japanese: `Enjoy the Flight`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=201&remain_distance>=199","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108301111 — Ironclad
- Japanese: `質実剛健`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==4&running_style==3&is_lastspurt==1&order_rate>=40&track_id==10005","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":150,"target":1,"type":9}],"precondition":""},{"baseDuration":15000,"condition":"distance_type==4&running_style==3&is_lastspurt==1&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108301211 — Revolutionary Presence
- Japanese: `革命をもたらす威容`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate>=50@distance_type==4&phase_laterhalf_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108302111 — Burn Down
- Japanese: `Burn Down`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase==1&order_rate<=80&order_rate>=30&blocked_side_continuetime>=2","effects":[{"modifier":1500,"target":11,"type":27},{"modifier":3000,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108302211 — Service: Transit
- Japanese: `Service: Transit`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108401111 — Storm-Calling God of Destruction
- Japanese: `嵐を呼ぶ破壊神`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_firsthalf_random==3&is_lastspurt==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase>=2&distance_diff_rate>=50"}],"rarity":6,"wisdomCheck":1}
```
---
## 108401211 — Imbibe in Ecstasy, World!
- Japanese: `酔い痴れよ、世界`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_speed>=1000&base_power>=1000&distance_type==2@base_speed>=1000&base_power>=1000&distance_type==3","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 108402111 — Attack of Ares
- Japanese: `アレスの進撃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==2&phase_laterhalf_random==0","effects":[{"modifier":-1500,"target":1,"type":21}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&phase_firsthalf_random==2&order_rate>50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108402211 — Arrow of Artemis
- Japanese: `アルテミスの矢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&is_last_straight==1&phase>=2&distance_type==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"running_style==4&is_last_straight==1&phase>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108501111 — Be Majestic
- Japanese: `華麗であれ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&order_rate>=40&is_finalcorner_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-1500,"target":9,"type":21},{"modifier":-1500,"target":10,"type":21}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108501121 — My Clan's Code of Honor
- Japanese: `我が一族の玉条を胸に`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"order_rate>=40&is_finalcorner_random==1&distance_type==1&temptation_count==0","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""},{"baseDuration":18000,"condition":"order_rate>=40&is_finalcorner_random==1&distance_type==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108501211 — Pursuing Greater Brilliance
- Japanese: `常に最たる輝きを`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"distance_type==1&phase>=2&order_rate>=50&is_overtake==1@distance_type==2&phase>=2&order_rate>=50&is_overtake==1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":-1500,"target":9,"type":21}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108502111 — Thunderclap
- Japanese: `霹靂閃電`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"running_style==3&distance_type==2&phase>=2&is_overtake==1&distance_rate<=75@running_style==3&distance_type==2&phase_firsthalf_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108502211 — Until Only Ashes Remain
- Japanese: `灰と化すまで`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108601111 — Pure Love
- Japanese: `純愛`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&corner_random==3&order_rate<=50@distance_type==3&corner_random==3&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108601211 — Enchanting Smile Beyond Reach
- Japanese: `高嶺の艶笑`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&phase_random==1@distance_type==3&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108602111 — Limitless Love
- Japanese: `Limitless Love`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&running_style==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108602211 — Conqueror of Banquets
- Japanese: `祝宴の征服者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&phase_laterhalf_random==0&order_rate<=50@distance_type==3&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108701111 — Victory Pitch-Up
- Japanese: `必勝のピッチアップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==1&always==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108701211 — Unforgettable Step
- Japanese: `記憶に刻む足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108702111 — The Art of Photobombing
- Japanese: `辻映りの妙技`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&distance_type==1&always==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"is_activate_other_skill_detail==1&phase_random==1&order_rate<=50&is_badstart==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108702211 — Please Remember Me, Okay?
- Japanese: `覚えていてくださいね？`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==1&distance_type==1&phase_firstquarter_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108801111 — Ambitious Card
- Japanese: `アンビシャスカード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108801211 — Million Card
- Japanese: `ミリオンカード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&course_distance>=2200&course_distance<=2400&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":5000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""},{"baseDuration":18000,"condition":"distance_type==3&course_distance<2200&phase_firsthalf_random==2&order_rate>=40@distance_type==3&course_distance>2400&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108802111 — Dazzling Illusion
- Japanese: `煌めきのイリュージョン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==3&distance_rate>=50&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108802211 — Waveriding Finale
- Japanese: `波上のラストトリック`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&running_style==3&distance_rate>=50&corner!=0&change_order_onetime<0&base_wiz>=1200","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==3&running_style==3&distance_rate>=50&corner!=0&change_order_onetime<0","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108901111 — Grand Expedition
- Japanese: `偉大なる踏破`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&running_style==2&phase_laterhalf_random==1&order_rate<=50&course_distance==2400","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==3&running_style==2&phase_laterhalf_random==1&order_rate<=50&course_distance!=2400","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108901211 — Full-Power Pitch
- Japanese: `全力投球`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108902111 — Marine Blue Liner
- Japanese: `マリンブルー・ライナー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_random==1&running_style==2&distance_type==4","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 108902211 — Not My Usual Self!
- Japanese: `いつもの僕じゃないから！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==4&running_style==2&is_lastspurt==1&corner==0","effects":[{"modifier":5000,"target":1,"type":31},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109001111 — Indomitable Queen
- Japanese: `不撓不屈の女王`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1&distance_type==2","effects":[{"modifier":2500,"target":1,"type":22},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109001211 — I'm a Big Sis After All
- Japanese: `『お姉ちゃん、だもの』`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&activate_count_start>=1","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"distance_type!=2&activate_count_start>=1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109101111 — Heavenly Little Sister
- Japanese: `天来のリトルシスター`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&down_slope_random==1@distance_type==3&down_slope_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109101211 — High Society Mentality!
- Japanese: `ハイソ・メンタリティ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&distance_rate_after_random==50&order_rate>=30&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109102111 — Desert Jewel's Allure
- Japanese: `デザートジュエルに魅せられ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109102211 — Onward! To the Sea!
- Japanese: `いざ征かん！マリンロード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==1&order_rate>=40&order_rate<=90&track_id==10008&base_wiz>=1200","effects":[{"modifier":4000,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"running_style==3&phase_random==1&order_rate>=40&order_rate<=90","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109201111 — I Wanna Win Too!!
- Japanese: `わたしだって、勝ちたい！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==3&is_activate_other_skill_detail==1&compete_fight_count>0","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109201211 — Ignite This Stage
- Japanese: `Ignite this Stage`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_firsthalf_random==2","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":2000,"target":1,"type":31}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==2&phase_firsthalf_random==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109301111 — K.Speed
- Japanese: `K.Speed`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==1&running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":18000,"condition":"distance_type!=1&running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109301121 — Shooting Star's Trail
- Japanese: `流れ星の軌跡`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109301211 — Spark of Life
- Japanese: `命の火花`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=201&remain_distance>=199","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109302111 — Keep Your Eyes on Me
- Japanese: `『見ていて、くださいね』`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_random==1&distance_type==1","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"running_style==2&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109302211 — Comet-Colored Flutter
- Japanese: `彗星色の羽搏き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&is_overtake==1&accumulatetime>=5","effects":[{"modifier":1500,"target":11,"type":22},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109401111 — Fangs of Ferocity
- Japanese: `猛襲の牙`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==3&phase_laterhalf_random==1&order_rate>=40&base_power>=1200","effects":[{"modifier":4000,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"distance_type==3&running_style==3&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109401211 — Demon of Tokyo
- Japanese: `闘叫の鬼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_firsthalf_random==2&track_id==10006","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109401221 — Unparalleled Bomber Runner
- Japanese: `天上天下唯我爆走`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==2","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109501111 — Limitless
- Japanese: `無極`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109501211 — Bred in the Bone
- Japanese: `徹骨徹髄`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&running_style==2&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109601111 — Fierce as Fire
- Japanese: `侵掠如火`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase==1&order_rate<=80&order_rate>=30&blocked_side_continuetime>=2","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109601211 — Decisive Battle
- Japanese: `天下分け目`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&distance_rate_after_random==50","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109701111 — Crimson Stirring
- Japanese: `赫き胎動`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&corner_random==3&is_used_skill_id==203781@distance_type==3&corner_random==3&is_used_skill_id==203781","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109701211 — Untold Vow
- Japanese: `誰にも告げぬ誓い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase==1&slope==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase==1&slope==2&distance_rate>=60&is_used_skill_id==203781","effects":[{"modifier":2500,"target":1,"type":22},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109701221 — Awakened Desire
- Japanese: `呼び覚まされし願い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1@distance_type==3&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase_firstquarter_random==2&is_used_skill_id==203781","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109801111 — Copano-style Rising Fortunes!
- Japanese: `コパッと開運！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109801211 — Surging Ley Lines
- Japanese: `龍脈の波濤`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==2&base_power>=1200","effects":[{"modifier":1000000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"ground_type==2&base_power>=1000&base_power<1200","effects":[{"modifier":800000,"target":1,"type":1}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 109802111 — The Yellow Dragon Ascends
- Japanese: `黄龍、天へと昇る`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109802211 — Lucky Race Charm
- Japanese: `走る縁起物`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_dirtgrade==1","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3}],"precondition":""},{"baseDuration":-1,"condition":"ground_type==2&is_dirtgrade!=1","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 109901111 — Feast of Tomakomai
- Japanese: `苫小牧グルメで舌鼓！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109901211 — Tourism Ambassador's Prestige
- Japanese: `観光大使の面目躍如！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase==1&blocked_side_continuetime>=2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109901221 — Give Your All, Star of Tomakomai!
- Japanese: `ひた走れ！苫小牧の星`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase==1&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":9000,"condition":"is_activate_other_skill_detail==1&is_lastspurt==1&lastspurt==2","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109902111 — Hometown Medley
- Japanese: `感謝のふるさとメドレー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&running_style==2&phase==1&is_activate_any_skill==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_activate_any_skill==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 109902211 — Plunge into the Northern Sea
- Japanese: `突き進め北の海`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"ground_type==2&running_style==2&phase_firstquarter_random==2&course_distance>=1800","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":18000,"condition":"ground_type==2&running_style==2&phase_firsthalf_random==2&course_distance<1800","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110001111 — Refueled Fighting Spirit
- Japanese: `闘魂注入`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&is_overtake==1&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110001121 — Veiled Grit
- Japanese: `いぶし銀の闘志`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&is_overtake==1&accumulatetime>=5","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110001211 — Goddess' Dust Bath
- Japanese: `女神の砂浴び`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==2&accumulatetime>=5&infront_near_lane_time>=3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110002111 — Ground-Shaking Geyser
- Japanese: `大地轟く大噴湯`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&is_lastspurt==1&change_order_onetime<0@ground_type==2&is_lastspurt==1&blocked_side_continuetime>=2","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110002211 — Follow the Wind, Follow the Water
- Japanese: `風まかせ、お湯まかせ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&running_style==2&phase_random==1&base_guts>=1200@ground_type==2&running_style==3&phase_random==1&base_guts>=1200","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"running_style==2&phase_random==1@running_style==3&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110011 — Wayakawa ♪ Marine Dive
- Japanese: `わやかわ♪マリンダイヴ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase==1&order>=2&order_rate<=80&activate_count_middle>=2","effects":[{"modifier":550,"target":1,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110021 — Beyond the Ocean's Infinity
- Japanese: `水平線のその先へ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=66&distance_rate<=68&corner==3&order==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":"phase==1&bashin_diff_behind>=3&order==1"},{"baseDuration":50000,"condition":"distance_rate>=66&distance_rate<=68&order==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110031 — It's Going to Be Me
- Japanese: `絶対は、ボクだ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"is_finalcorner==1&is_overtake==1&order<=5&order_rate<=50&overtake_target_no_order_up_time>=2"}],"rarity":5,"wisdomCheck":0}
```
---
## 110041 — Heartfelt ♪ Smooch
- Japanese: `グッときて♪Chu`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&activate_count_heal>=1&order<=3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110051 — Ravissante
- Japanese: `Ravissant`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"is_finalcorner==1&change_order_onetime<0&order_rate<=40","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110061 — Christmas Eve Miracle Run!
- Japanese: `聖夜のミラクルラン！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"activate_count_heal>=3&distance_rate>=50","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110071 — Adventure of 564
- Japanese: `Adventure of 564`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate_after_random==50","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":20000,"target":1,"type":37}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110081 — Into High Gear!
- Japanese: `Into High Gear!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"slope==0@slope==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":"phase>=1&slope==2&order_rate>=50&order_rate<=80&track_id==10006"},{"baseDuration":40000,"condition":"slope==0@slope==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase>=1&slope==2&order_rate>=50&order_rate<=80"}],"rarity":5,"wisdomCheck":0}
```
---
## 110091 — Queen's Lumination
- Japanese: `Queen's Lumination`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=50&corner==0&order==1&bashin_diff_behind<=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":60000,"condition":"distance_rate>=50&corner==0&order<=2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110101 — Joyful Voyage!
- Japanese: `Joyful Voyage!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_diff_top<=5&order>=2&order_rate<=40&remain_distance<=201&remain_distance>=199","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"order>=2&order_rate<=40&remain_distance<=201&remain_distance>=199","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110111 — Gain Superior Heal
- Japanese: `ゲインヒール・スペリアー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&change_order_onetime>0&order_rate>=40","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110121 — Extra Large First Bite!
- Japanese: `大盛り！ファーストバイト！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_rate>=60&phase==1&slope==2&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":"change_order_up_middle>=3"}],"rarity":5,"wisdomCheck":0}
```
---
## 110131 — For the Strongest Name
- Japanese: `最強の名を懸けて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"phase>=2&is_finalcorner==1&order<=4&overtake_target_time>=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110141 — Condor Onslaught
- Japanese: `コンドル猛撃波`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"is_finalcorner==1&corner!=0&is_overtake==1&order>=4&order_rate<=75","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110151 — Blessed Barcarolle
- Japanese: `恵福バルカローレ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=401&remain_distance>=399&order_rate<=40&activate_count_all>=7","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"remain_distance<=401&remain_distance>=399&order_rate<=40&activate_count_all<=6","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110161 — Critical Point: Gray
- Japanese: `灰色の臨界点`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==4&phase>=2&is_finalcorner_laterhalf==1&order_rate<=40","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":"phase==1&blocked_side_continuetime>=2"},{"baseDuration":50000,"condition":"phase>=2&is_finalcorner_laterhalf==1&order_rate<=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110171 — Howling Arrow Piercing the Darkness
- Japanese: `翳り退く、さざめきの矢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"is_finalcorner==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase>=2&order_rate<=50&overtake_target_time>=2"}],"rarity":5,"wisdomCheck":0}
```
---
## 110181 — Summer Breeze, the Eternal Moment
- Japanese: `薫風、永遠なる瞬間を`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase==1&order>=3&order_rate<=50&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110191 — Revived by Moe!
- Japanese: `萌到讓我活過來了！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"near_count>=3&phase==1&corner!=0&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110201 — Do Ya Breakin!
- Japanese: `Do Ya Breakin!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&corner==0&order<=2&straight_front_type==2","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""},{"baseDuration":50000,"condition":"phase>=2&corner==0&order<=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110201111 — Caesura
- Japanese: `カエスーラ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&corner==0","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110201211 — Trionfo
- Japanese: `トライアンフ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-1500,"target":9,"type":21},{"modifier":-1500,"target":10,"type":21}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110201221 — Esplosione
- Japanese: `エスプロズィオーネ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&distance_type==4&phase_laterhalf_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":-300,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110202111 — Musica Scintillante
- Japanese: `ムジカ・シンティッランテ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&activate_count_all>=13","effects":[{"modifier":1500,"target":11,"type":22},{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110202211 — Dono di Flora!
- Japanese: `ドーノ・ディ・フローラ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&distance_rate_after_random==50&distance_type==3&order_rate<=50","effects":[{"modifier":1500,"target":11,"type":22},{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==2&distance_rate_after_random==50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110211 — Thunderous Firestarter
- Japanese: `火神鳴`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"activate_count_middle>=2","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":250,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110221 — Best Day Ever
- Japanese: `Best day ever`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance>=401&phase>=2&is_finalcorner==1&order_rate>=20&order_rate<=40","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":50000,"condition":"phase>=2&is_finalcorner==1&order_rate>=20&order_rate<=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110231 — Presents from X
- Japanese: `Presents from X`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"order_rate_in50_continue==1&phase==1&distance_rate>=50&order>=2&order_rate<=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110241 — Flowery ☆ Maneuver
- Japanese: `フラワリー☆マニューバ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&order_rate<=40&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"is_finalcorner==1&order_rate>=50&order_rate<=80&change_order_onetime<0","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110251 — Purrfect Hospitality
- Japanese: `心からのおもてにゃし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==4&phase>=2&is_finalcorner==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":"distance_rate>=50&order_rate_out40_continue==1"},{"baseDuration":50000,"condition":"phase>=2&is_finalcorner==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":"distance_rate>=50&order_rate_out40_continue==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 110261 — Operation Cacao
- Japanese: `オペレーション・Cacao`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"order<=4&phase==1&corner!=0&bashin_diff_behind<=3","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110271 — Latte Art For You
- Japanese: `あなたに捧げるフリーポア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_rate>=60&slope==2&phase==1&order>=2&distance_diff_top<=10&distance_type==3","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"distance_rate>=60&slope==2&phase==1&order>=2&distance_diff_top<=10&distance_type!=3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110281 — Sugar Parade: Start!
- Japanese: `シュガーパレード・始動！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&phase_laterhalf_random==0&order_rate>=20&order_rate<=50@distance_type==2&phase_laterhalf_random==0&order_rate>=20&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"phase_laterhalf_random==0&order_rate>=20&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110291 — Have Your Fill!
- Japanese: `いっぱいおあげんしぇ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=50&is_overtake==1&distance_type==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=50&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110301 — Drain for Rose
- Japanese: `Drain for rose`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase==1&order>=2&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":-50,"target":9,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110301111 — Skillful Phantom
- Japanese: `巧みなるファントム`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&corner!=0&is_move_lane==1@distance_rate>=50&corner!=0&is_move_lane==2","effects":[{"modifier":3000,"target":1,"type":31},{"modifier":1500,"target":1,"type":22}],"precondition":"distance_type==3&running_style==2"}],"rarity":6,"wisdomCheck":1}
```
---
## 110301211 — Rapidly Rising Recognition!
- Japanese: `認知度、急上昇！`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&up_slope_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 11031 — Appeal Declaration!
- Japanese: `アピール宣言！`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase==1&order_rate<=50&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":3,"wisdomCheck":0}
```
---
## 110311 — Fresh ☆ Parlor
- Japanese: `フレッシュ☆パーラー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"phase_firsthalf_random==1&order_rate<=30","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110321 — Summer Halation
- Japanese: `夏空ハレーション`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_rate>=50&corner!=0&order_rate>=20&order_rate<=50&track_id==10005","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"distance_rate>=50&corner!=0&order_rate>=20&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110331 — Crystal Mist
- Japanese: `Crystal Mist`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&is_finalcorner==1&order_rate>=40&course_distance==2400","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"running_style==4&is_finalcorner==1&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110341 — Bristling Lights
- Japanese: `灯穂`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight_onetime==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase>=2&corner!=0&order_rate>=60&is_overtake==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 110351 — Delivering Beyond the Dreams!
- Japanese: `夢の先へ、届け！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"is_lastspurt==1&is_last_straight==1&order_rate>=40","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110361 — ...found you.
- Japanese: `...found you.`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&is_finalcorner_laterhalf==1&is_overtake==1@phase>=2&is_finalcorner==1&corner==0&is_overtake==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase==1&change_order_onetime>0&order_rate>=50&order_rate<=80"},{"baseDuration":50000,"condition":"phase>=2&is_finalcorner_laterhalf==1&is_overtake==1@phase>=2&is_finalcorner==1&corner==0&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110371 — Guten Appetit♪
- Japanese: `Guten Appetit♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"change_order_up_finalcorner_after>=2&is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110381 — One True Color
- Japanese: `One True Color`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=350&order_rate<=40&order_rate>=20&bashin_diff_behind<=1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110391 — Invigorating Strength
- Japanese: `快なる剛力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"slope==0@slope==2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase>=1&slope==1&order_rate>=40&order_rate<=80"}],"rarity":5,"wisdomCheck":0}
```
---
## 110401 — GET DOWN
- Japanese: `GET DOWN`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&corner!=0&order_rate>=30&order_rate<=70&blocked_side_continuetime>=2","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110401111 — Beat You to It!
- Japanese: `してやったり！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110401211 — Solitary Getaway
- Japanese: `逃げっ切りの1人旅`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&is_last_straight==1&order==1&track_id==10006&distance_type==3","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":"phase==1&bashin_diff_behind>=3&order==1"},{"baseDuration":24000,"condition":"running_style==1&is_last_straight==1&order==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase==1&bashin_diff_behind>=3&order==1"}],"rarity":6,"wisdomCheck":1}
```
---
## 110402111 — Dormant Dragon's Rise
- Japanese: `伏竜は目覚めて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==3&running_style==1&phase>=2&is_finalcorner==1&corner!=0&order<=3","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110402211 — Dawnborne
- Japanese: `暁光背負いて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&running_style==1&corner_random==3&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110411 — Cherry☆Scramble
- Japanese: `CHERRY☆スクランブル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":10000,"condition":"order<=3&remain_distance<=401&remain_distance>=399","effects":[{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110421 — Oh!bento-magic☆
- Japanese: `Oh!bento-magic☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order_rate<=50&is_overtake==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"is_activate_other_skill_detail==1&is_finalcorner==1&corner!=0&change_order_onetime<0&distance_type==1@is_activate_other_skill_detail==1&is_finalcorner==1&corner!=0&change_order_onetime<0&distance_type==2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110441 — Special Materialization
- Japanese: `とっておきmaterialize`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=1&slope==2&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":-200,"target":1,"type":9}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_last_straight==1&motivation>=4","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110451 — Round and Round, Mummy Trick♡
- Japanese: `ぐるぐるマミートリック♡`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&order<=4&bashin_diff_infront<=1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110461 — α-star*
- Japanese: `α-star*`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=40&distance_rate<=50&distance_diff_rate<=10&ground_type==2","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""},{"baseDuration":60000,"condition":"distance_rate>=40&distance_rate<=50&distance_diff_rate<=10","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110471 — Close Encounters of the Literary Kind
- Japanese: `未知との遭遇、即ち物語`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&is_last_straight==1&order_rate<=40&track_id==10005&course_distance==2500@phase>=2&is_last_straight==1&order_rate<=40&track_id==10006&distance_type==3","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"phase>=2&is_last_straight==1&order_rate<=40","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110481 — GALmem. forever♪
- Japanese: `GALmem.ふぉーえば♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=40&order_rate<=80&motivation==5","effects":[{"modifier":3000,"target":1,"type":27}],"precondition":""},{"baseDuration":60000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=40&order_rate<=80","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110491 — Wager on the Holy Night Stars
- Japanese: `運否、聖夜の星に賭ける`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"phase_firsthalf_random==1&distance_type==3@phase_firsthalf_random==1&distance_type==4","effects":[{"modifier":-2500,"target":1,"type":21}],"precondition":""},{"baseDuration":60000,"condition":"is_activate_other_skill_detail==1&phase_laterhalf_random==1&order_rate>=40&order_rate<=80","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110501 — Hephaistos
- Japanese: `Hephaistos`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&is_finalcorner_laterhalf==1&order_rate<=75&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110501111 — Beyond the Milky Way With You
- Japanese: `銀河のその先へ、あなたと`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase>=2&is_last_straight==1&order_rate>=20&order_rate<=60","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110501211 — Crossing the Sea of Stars
- Japanese: `星の海を駆けて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&activate_count_all>=13","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110502111 — Luminous Spectrum
- Japanese: `ルミナス・スペクトラム`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&activate_count_all>=13","effects":[{"modifier":1500,"target":11,"type":22},{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110502211 — METI Resonance
- Japanese: `“METI”レゾナンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==1&distance_type==3&is_exist_skill_id==201631","effects":[{"modifier":1000000,"target":1,"type":1},{"modifier":0,"target":2,"type":41}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 110511 — Flowering Dreams
- Japanese: `Flowering Dreams`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"order>=2&order_rate<=70&remain_distance<=201&remain_distance>=199&near_count>=3","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"order>=2&order_rate<=70&remain_distance<=201&remain_distance>=199","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110521 — Fall Down 113 Times, Get Up 114
- Japanese: `113転び114起き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&corner!=0&distance_diff_top>=7","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110531 — Secret Technique: Everlasting Summer!!
- Japanese: `奥義・常夏バーニング！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==1&remain_distance<=201&remain_distance>=199&order_rate>=20&order_rate<=50&change_order_up_end_after>=1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"remain_distance<=201&remain_distance>=199&order_rate>=20&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110551 — Bravo ☆ Wonder Doll!
- Japanese: `喝采☆ワンダードール！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&motivation==5","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":"phase>=2&is_finalcorner==1&corner!=0&near_count>=1&order_rate>=30&order_rate<=70"},{"baseDuration":50000,"condition":"is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase>=2&is_finalcorner==1&corner!=0&near_count>=1&order_rate>=30&order_rate<=70"}],"rarity":5,"wisdomCheck":0}
```
---
## 110561 — Grains Become Ripe
- Japanese: `禾スナハチ登ル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order_rate>=40&overtake_target_time>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110571 — Radiant Stride
- Japanese: `爛然闊歩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110581 — Spooky-Scary-Happy
- Japanese: `Spooky-Scary-Happy`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight_onetime==1&order_rate<=40","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":-500,"target":9,"type":21},{"modifier":-500,"target":10,"type":21}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110591 — To Where the Heart Beckons
- Japanese: `ときめきが呼ぶほうへ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=60&slope==2&phase==1&order_rate>=40&order_rate<=80&remain_distance>=500","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110601 — Go☆Go☆For It!
- Japanese: `Go☆Go☆for it!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"is_last_straight==1&order_rate>=40&order_rate<=70&popularity>=4","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"is_finalcorner==1&change_order_onetime<0"},{"baseDuration":50000,"condition":"is_last_straight==1&order_rate>=40&order_rate<=70&popularity<4","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"is_finalcorner==1&change_order_onetime<0"}],"rarity":5,"wisdomCheck":0}
```
---
## 110601111 — Keep Calm, Don't Overthink
- Japanese: `焦らず、気負わず`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110601121 — I'll Do What I Can~!
- Japanese: `できる範囲でがんばろ～！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":150,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110601211 — Collecting Little Joys
- Japanese: `ちょっといいこと、集めて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==1&order_rate>=40&order_rate<=90","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110602111 — Coming Through♪
- Japanese: `お邪魔しま～す♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110602211 — Big Comeback Time!?
- Japanese: `まさかここから大逆転！？`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"lastspurt==2&running_style==3&distance_type==3&phase_firstquarter_random==2&order_rate>=40&slope==2","effects":[{"modifier":3000,"target":1,"type":31},{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":18000,"condition":"running_style==3&distance_type==3&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110611 — Roaring Tracen Cheerleading Squad
- Japanese: `轟！トレセン応援団！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"is_last_straight==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"distance_rate>=50&order_rate_out70_continue==1&temptation_count==0"}],"rarity":5,"wisdomCheck":0}
```
---
## 110621 — Rolling Power Drive!
- Japanese: `ごろりん！？パワードライブ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"distance_rate>=50&corner!=0&order_rate>=40&order_rate<=80&distance_type==3","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":20000,"condition":"distance_rate>=50&corner!=0&order_rate>=40&order_rate<=80","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110631 — Chitose, Circling On
- Japanese: `千歳、廻りて`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_firsthalf==1&is_overtake==1@phase_firsthalf==1&overtake_target_time>=1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&phase_laterhalf_random==1&order_rate<=40&distance_type==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110641 — Jingle All the Way
- Japanese: `jingle all the way`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":70000,"condition":"distance_rate>=40&corner==0&order==1&track_id==10005&is_used_skill_id==202051","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":70000,"condition":"distance_rate>=40&corner==0&order==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110651 — It's Mashup Time!
- Japanese: `ノッてけ、マッシュアップ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==2&blocked_side_continuetime>=2&order_rate<=50&phase==0&accumulatetime>=5","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-300,"target":1,"type":9}],"precondition":""},{"baseDuration":50000,"condition":"blocked_side_continuetime>=2&order_rate<=50&phase==0&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110671 — Arrow of Gold, Break up the Dark Clouds
- Japanese: `玄雲散らす、黄金甲矢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=40&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110681 — Lavish Feast
- Japanese: `あっぱれ大盤振る舞い！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&corner!=0&remain_distance>=600&order<=3","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110691 — Bloom! Blossom! Sakura!
- Japanese: `咲け咲け！私！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=651&remain_distance>=649&order_rate<=40&order_rate>=30","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"phase==1&blocked_side_continuetime>=2"}],"rarity":5,"wisdomCheck":0}
```
---
## 110701 — Driven by Light, the Heavenly Wolf Hunts
- Japanese: `駆るは光、狩るは星々`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":70000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=30&order_rate<=80&distance_type==3&base_power>=1200","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":60000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=30&order_rate<=80","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110701111 — Breakaway Star
- Japanese: `Breakaway Star`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==1&order==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110701211 — Smooth Sailing!
- Japanese: `Smooth Sailing!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"activate_count_middle>=3&order==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110702111 — True Wire-to-Wire!
- Japanese: `True Wire-to-Wire!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&is_last_straight==1&order==1&bashin_diff_behind<=1","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110702211 — Easygoing Grand Voyage
- Japanese: `大航海、飄々と`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":27000,"condition":"distance_type==3&phase_firsthalf_random==1&running_style==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-400,"target":1,"type":9},{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":27000,"condition":"phase_firsthalf_random==1&running_style==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-400,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110711 — Danser le Présent
- Japanese: `Danser le présent`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&is_last_straight==1&order_rate>=20&order_rate<=40&bashin_diff_behind<=1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22},{"modifier":-300,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110721 — Decisive Blade of Blazing Fire
- Japanese: `剛勇果断、烈火之刀`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate_after_random==50&lane_type==0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"distance_rate>=40&distance_rate<=50&blocked_side_continuetime>=2"},{"baseDuration":50000,"condition":"distance_rate_after_random==50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"distance_rate>=40&distance_rate<=50&blocked_side_continuetime>=2"}],"rarity":5,"wisdomCheck":0}
```
---
## 110741 — Illuminate You
- Japanese: `Illuminate you`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"phase==1&order_rate>=40&order_rate<=80","effects":[{"modifier":750,"target":1,"type":9},{"modifier":-1500,"target":1,"type":21}],"precondition":""},{"baseDuration":80000,"condition":"is_activate_other_skill_detail==1&base_stamina>=1200&phase>=2","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110761 — Spring Light: Bon Appétit
- Japanese: `春光・Bon appétit`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==4&phase>=2&is_finalcorner_laterhalf==1&order_rate>=40&order_rate<=80","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":"phase==1&blocked_side_continuetime>=2"},{"baseDuration":50000,"condition":"phase>=2&is_finalcorner_laterhalf==1&order_rate>=40&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110771 — Joy to the World
- Japanese: `Joy to the World`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=45&order_rate>=20&order_rate<=50&remain_distance>=1000","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase_firsthalf==1&is_activate_heal_skill==1"},{"baseDuration":50000,"condition":"distance_rate>=45&order_rate>=20&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"phase_firsthalf==1&is_activate_heal_skill==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 110781 — Breezy Treat
- Japanese: `Breezy Treat`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&remain_distance<=351&remain_distance>=349&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"remain_distance<=351&remain_distance>=349&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110801 — Geothermal Overdrive
- Japanese: `地熱解放オーヴァードライブ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_laterhalf==0&order_rate<=30","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"is_activate_other_skill_detail==1&distance_rate>=40&distance_rate<=50&overtake_target_time>=2","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110801111 — Constant Refinement
- Japanese: `磨穿鉄硯`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110801211 — Blazing Brilliance
- Japanese: `赫焉`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==3&track_id!=10005&running_style==4&phase>=2&is_finalcorner==1&corner!=0&order_rate>=40@distance_type==3&track_id==10005&running_style==4&phase>=2&corner!=0&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110831 — Immortal Work
- Japanese: `Immortal Work`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&track_id==10005&distance_type==3","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":"distance_rate>=50&distance_rate<=51&order_rate>=40&order_rate<=80"},{"baseDuration":50000,"condition":"is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"distance_rate>=50&distance_rate<=51&order_rate>=40&order_rate<=80"}],"rarity":5,"wisdomCheck":0}
```
---
## 110841 — Terpsichore of the Abyss
- Japanese: `深淵のテルプシコラー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&order_rate>=50&distance_type==2&order_rate_out70_continue==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"phase>=2&order_rate>=50","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110851 — Sapphire Flame
- Japanese: `蒼炎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate<=50&distance_rate>=45&order_rate<=90&order_rate>=40&distance_type==2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate<=50&distance_rate>=45&order_rate<=90&order_rate>=40","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110861 — Everlasting Knot
- Japanese: `解けぬ結い目`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"running_style==2&order_rate<=40&remain_distance>=299&remain_distance<=301&distance_diff_top<=5","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"running_style==2&order_rate<=40&remain_distance>=299&remain_distance<=301","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110871 — Fluffy Fuzzy Hour
- Japanese: `ふわもこアワー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==1&distance_rate<=50&distance_rate>=45&order_rate<=30&base_wiz>=1200","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_type==1&distance_rate<=50&distance_rate>=45&order_rate<=30","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110881 — Summer Thunder Cascade!
- Japanese: `夏雷カスケード！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_firsthalf==1&change_order_onetime<0&distance_type==3","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"running_style==3&phase_firsthalf==1&change_order_onetime<0","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110891 — Tidebreaker
- Japanese: `Tidebreaker`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":70000,"condition":"distance_type==4&distance_rate>=40&distance_rate<=50&order_rate>=20&order_rate<=70&course_distance<3000","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":70000,"condition":"distance_type==4&distance_rate>=40&distance_rate<=50&order_rate>=20&order_rate<=70","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110901111 — Pioneering the Future!
- Japanese: `未来を拓け！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110901121 — Watch Me Do It!
- Japanese: `やってみせるんだ！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&running_style==2&is_finalcorner_random==1&order_rate<=50&track_id==10006","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==2&running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110901211 — There's No Way I'll Lose!
- Japanese: `ぜーったい負けられない！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=201&remain_distance>=199","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110902111 — Hope Comes Around
- Japanese: `希望は巡る、何度でも`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&distance_rate_after_random==50@distance_type==3&distance_rate_after_random==50","effects":[{"modifier":4500,"target":1,"type":22},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110902211 — Tiara Dive!
- Japanese: `ティアラ・ダイブ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&down_slope_random==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 110911 — Je t'aime ☆ Vacances
- Japanese: `ジュ・テーム☆バカンス！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_rate>=50&corner==3&order_rate>=40&order_rate<=90&slope==1&course_distance==2000","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=50&corner==3&order_rate>=40&order_rate<=90","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110931 — Miracle, Hopes, Melody
- Japanese: `きせき・おもい・かなで`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase==3&is_lastspurt==1&distance_type==1&order<=3","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":"phase==1&order_rate<=70&order_rate>=20&blocked_side_continuetime>=2"},{"baseDuration":50000,"condition":"phase==3&is_lastspurt==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase==1&order_rate<=70&order_rate>=20&blocked_side_continuetime>=2"}],"rarity":5,"wisdomCheck":0}
```
---
## 110981 — Parade of the Five Heavenly Beasts
- Japanese: `五獣挙りて彩光奏づ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&order_rate<=50&ground_type==2&remain_distance>=500","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 110991 — Popping☆Clams
- Japanese: `とびだせ☆ポッピングシェル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51&ground_type==2&corner!=3","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 111001 — Bathkeeper's Heart of Zen
- Japanese: `湯守の和心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"ground_type==2&phase_firsthalf==1&order>=3&infront_near_lane_time>=3@ground_type==2&phase_firsthalf==1&order>=3&behind_near_lane_time>=3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"phase_firsthalf==1&order>=3&infront_near_lane_time>=3@phase_firsthalf==1&order>=3&behind_near_lane_time>=3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 111001111 — Become the Foundation
- Japanese: `礎たれ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&is_last_straight==1&order_rate>=20&order_rate<=60&phase>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111001211 — Beautiful Transformation
- Japanese: `麗しき転身`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==3&phase_laterhalf_random==0","effects":[{"modifier":-1500,"target":1,"type":21}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase_firsthalf_random==2","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111002111 — None Can Block Glory's Advance
- Japanese: `栄華の歩み、誰ぞ遮る`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&running_style==2&phase_laterhalf_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111002211 — Vow of White Cloth
- Japanese: `白妙の約定`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_laterhalf_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111021 — Che Piacevole!
- Japanese: `ケ・ピアチェーヴォレ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&is_last_straight==1&distance_type==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate_in50_continue==1"},{"baseDuration":50000,"condition":"phase>=2&is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate_in50_continue==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 111041 — Determined Stroke
- Japanese: `決意一筆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&distance_rate>=50&order_rate_in40_continue==1&is_used_skill_id==202051","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""},{"baseDuration":80000,"condition":"distance_type==3&distance_rate>=50&order_rate_in40_continue==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 111051 — Encounter With U
- Japanese: `Encounter with U`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_last_straight==1&phase>=2&order>=2&activate_count_middle==7@is_last_straight==1&phase>=2&order>=2&activate_count_middle==13","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"is_last_straight==1&phase>=2&order>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 111061 — A Small Miracle for You♪
- Japanese: `小さな奇跡、フォーユー♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&is_overtake==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_finalcorner_laterhalf==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 111071 — Romantic Horizon
- Japanese: `Romantic Horizon`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"distance_type==3&phase_laterhalf_random==1&order<=3","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":60000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 111091 — Shine on Forever
- Japanese: `ずっとずっと輝いて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==1&phase>=2&corner!=0&slope==2","effects":[{"modifier":2500,"target":1,"type":22},{"modifier":2000,"target":1,"type":31}],"precondition":"track_id==10009&course_distance==1600@track_id==10008&course_distance==2000@track_id==10006&course_distance==2400"},{"baseDuration":40000,"condition":"ground_type==1&phase>=2&corner!=0","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":"track_id==10009&course_distance==1600@track_id==10008&course_distance==2000@track_id==10006&course_distance==2400"}],"rarity":5,"wisdomCheck":0}
```
---
## 111101 — Perennial Babbles
- Japanese: `時かけるせせらぎ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&is_lastspurt==1&phase==3&running_style==2","effects":[{"modifier":5000,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"is_lastspurt==1&phase==3&running_style==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 111101111 — Chasing Mother's Likeness
- Japanese: `母の面影を追って`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&base_wiz>=1200","effects":[{"modifier":5000,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111101211 — Steady Stratagem
- Japanese: `堅実なる秘策`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_firsthalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&slope==2&distance_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111191 — Dreaming of the Silver World
- Japanese: `夢寐に見る銀世界`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"order_rate>=50&remain_distance>=999&remain_distance<=1001","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"distance_type==4&phase>=2&corner!=0&change_order_onetime<0&is_activate_other_skill_detail==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 111241 — Break Through the Dawn Haze, Seize the Morning
- Japanese: `暁霞を拓き、朝を掴む`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase>=2&is_finalcorner_laterhalf==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&distance_type==2&is_last_straight==1@is_activate_other_skill_detail==1&distance_type==3&is_last_straight==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 111301111 — Love Me ☆ Parade
- Japanese: `ラブミー☆パレード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=50&course_distance==2200","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111301211 — Let Me Win Pleeease ♥
- Japanese: `ぜーったい譲って♡`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&distance_type==3&order_rate<=50&phase_firstquarter_random==2&course_distance==2200","effects":[{"modifier":5000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""},{"baseDuration":18000,"condition":"running_style==2&distance_type==3&order_rate<=50&phase_firsthalf_random==2&course_distance!=2200","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111321 — Watch Us Flourish
- Japanese: `Watch Us Flourish`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"phase==1&corner==0&order_rate<=50&is_abroad==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":60000,"condition":"phase==1&corner==0&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 111401111 — When Our Promise Comes True
- Japanese: `ふたりの約束、とどく時`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&course_distance>=1600&course_distance<=2500&corner_random==3&is_basis_distance==1","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"running_style==4&course_distance>=1600&course_distance<=2500&corner_random==3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111401211 — Sincere-Hearted Radiance
- Japanese: `誠心たる光燿`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==2&running_style==4&ground_type==1&phase_firsthalf_random==2@distance_type==3&running_style==4&ground_type==1&phase>=2&is_finalcorner==1&corner!=0","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111501111 — My Will is Divine
- Japanese: `我が意、即ち天の理なり`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==4&course_distance>=2000&is_lastspurt==1&ground_type==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111501211 — Sovereign's Dominion
- Japanese: `王威絢爛`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&phase_laterhalf_random==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111501221 — You Shall Kneel in Reverence
- Japanese: `――畏れよ、然して拝跪せよ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==1&order_rate>=40@distance_type==4&phase_firsthalf_random==1&order_rate>=40","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111601111 — Step Aside
- Japanese: `――お退きなさい`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&course_distance>=2000&infront_near_lane_time>=1&phase_firstquarter==2@running_style==2&course_distance>=2000&phase_firstquarter_random==2","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":250,"target":1,"type":28}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111601211 — Power Am I
- Japanese: `Power Am I`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==2&distance_type==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111601221 — A Lady's Domain
- Japanese: `淑女の独擅場`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_laterhalf_random==1&running_style==2&course_distance>=2400&course_distance<=2500&base_power>=1200","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"phase_laterhalf_random==1&running_style==2&course_distance>=2400&course_distance<=2500","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111701111 — Grand Jeté
- Japanese: `グラン・ジュッテ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&distance_rate>=50&is_overtake==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111701211 — En l'Air
- Japanese: `邁進アン・レール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_corner_random==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111901111 — Starboard Till the End
- Japanese: `果てへの面舵`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==1","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3}],"precondition":""}],"rarity":6,"wisdomCheck":0}
```
---
## 111901211 — Trance
- Japanese: `夢見心地`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&phase>=2&corner!=0&is_overtake==1&track_id==10005&base_wiz>=1200","effects":[{"modifier":4000,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"running_style==4&phase>=2&corner!=0&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111902111 — Smiling Behind Snowy Dusk
- Japanese: `雪暗れに微笑む`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==4&running_style==4&phase_firsthalf_random==2&lastspurt==2&base_wiz>=1200","effects":[{"modifier":4000,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"distance_type==4&running_style==4&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 111902211 — Now Then, Let's Conclude This
- Japanese: `さて、収めに参りましょう`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&running_style==4&distance_rate>=50&is_overtake==1","effects":[{"modifier":1500,"target":11,"type":27},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112001111 — Flash Dash!
- Japanese: `閃光一走！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==1&running_style==1&always==1","effects":[{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&straight_random==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112001211 — Gale Rush!
- Japanese: `突風一駆！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==1&running_style==1&always==1","effects":[{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&straight_random==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112101111 — Faithful Veillantif
- Japanese: `忠心のヴェイヤンティフ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_laterhalf_random==1&running_style==4","effects":[{"modifier":5500,"target":1,"type":27},{"modifier":-300,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112101211 — Olifant's Roar
- Japanese: `オリファントの轟雷`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"distance_type==1&phase>=2&is_overtake==1&is_finalcorner==1&corner!=0@distance_type==2&phase>=2&is_overtake==1&is_finalcorner==1&corner!=0","effects":[{"modifier":5000,"target":1,"type":31}],"precondition":""},{"baseDuration":20000,"condition":"distance_type==1&phase>=2&is_overtake==1@distance_type==2&phase>=2&is_overtake==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112401111 — Champion's Composure
- Japanese: `俊傑の悠`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&distance_rate>=60&phase==1&distance_diff_top<=5&distance_type==2@running_style==2&distance_rate>=60&phase==1&distance_diff_top<=5&distance_type==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"running_style==2&distance_rate>=60&phase==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112401211 — Vanguard's Limelight
- Japanese: `嚆矢の花道`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&is_last_straight==1&distance_diff_top_float<=25&distance_type==2@running_style==2&is_last_straight==1&distance_diff_top_float<=25&distance_type==3","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==2&remain_distance<=201&remain_distance>=199","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112402111 — Take the High Ground
- Japanese: `風上に立て`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_overtake==1&accumulatetime>=5@order==1&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"distance_type==2@distance_type==3"},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&track_id==10006&phase>=2&is_last_straight==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112402211 — Bursting Wind-Up Prodigy
- Japanese: `ハジける風雲児`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&distance_type==2&phase>=2&is_last_straight==1@is_activate_other_skill_detail==1&distance_type==3&phase>=2&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112701111 — Anpan and Milk
- Japanese: `あんぱんと牛乳`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_firsthalf_random==1&course_distance>=3200","effects":[{"modifier":750,"target":1,"type":9},{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":0,"condition":"distance_type==4&phase_firsthalf_random==1","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112701211 — The Fierce Beast Howls at the Sun
- Japanese: `猛き獣は太陽に吼える`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&running_style==2&phase==2&course_distance>=3200","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112901111 — The Next Phase
- Japanese: `The Next Phase`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50&base_speed>=1200","effects":[{"modifier":4000,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112901211 — Certain Victory
- Japanese: `確信された勝利`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&distance_type==3&phase_laterhalf_random==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":9000,"condition":"is_activate_other_skill_detail==1&is_lastspurt==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 112901221 — Innovated Future
- Japanese: `革新された未来`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&distance_type==2&distance_rate_after_random==50&base_guts>=1200","effects":[{"modifier":5500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"running_style==2&distance_type==2&distance_rate_after_random==50","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113101111 — I'll Go the Extra Mile!!
- Japanese: `推してまいる！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==2&phase_firsthalf_random==2","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"distance_type==1&phase_firsthalf_random==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113101211 — Thousand Mile Shout
- Japanese: `万哩へ響け大歓声`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_firstquarter_random==2&order_rate>=40&ground_type==1","effects":[{"modifier":5000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""},{"baseDuration":18000,"condition":"distance_type!=2&phase_firsthalf_random==2&order_rate>=40&ground_type==1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113201111 — Streaming ♡ Rush
- Japanese: `ストリーミング♡ラッシュ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==3&phase_straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113201211 — Like and Comment!
- Japanese: `応援コメントよろしく！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&distance_rate_after_random==50&running_style==3&base_wiz>=1200","effects":[{"modifier":4000,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"distance_type==3&distance_rate_after_random==50&running_style==3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113202111 — Lots of Love ♡
- Japanese: `ロッツオブラヴ♡`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"order_rate<=50&distance_type==3&ground_type==1&is_lastspurt==1&corner==0&is_abroad==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":18000,"condition":"order_rate<=50&distance_type==3&phase_firsthalf_random==2&is_abroad==0@order_rate<=50&distance_type==3&ground_type==2&phase_firsthalf_random==2&is_abroad==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113202211 — The Legendary Episode Beyond the Sea!
- Japanese: `海を越える神回！`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_latter_half_straight_random==1&running_style==2&distance_type==3&order_rate<=50&is_abroad==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"phase_latter_half_straight_random==1&running_style==2&distance_type==3","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113301111 — Forever and Ever
- Japanese: `永永無窮`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113301211 — A Page of Creation
- Japanese: `創世の一頁`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==2&course_distance>=2000&course_distance<=2500&is_overtake==1&phase_firstquarter==2@running_style==2&course_distance>=2000&course_distance<=2500&phase_firstquarter_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113501111 — Unfinished Journey
- Japanese: `見果てぬ旅路`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&is_lastspurt==1&is_last_straight==1&motivation==5","effects":[{"modifier":6500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""},{"baseDuration":24000,"condition":"running_style==3&is_lastspurt==1&is_last_straight==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113501211 — When the Clock Hands Cross
- Japanese: `針が交わる時`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&running_style==3&distance_rate>=66&distance_rate<=68","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"remain_distance<=400&order_rate>=30&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"is_activate_other_skill_detail==1&is_finalcorner==1&is_overtake==1"}],"rarity":6,"wisdomCheck":1}
```
---
## 113501221 — Traveler's Knowledge
- Japanese: `旅の心得`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&running_style==3&distance_rate>=50&corner==0&order_rate<=70&order_rate>=30","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"is_activate_other_skill_detail==1&remain_distance>=999&remain_distance<=1001","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113701111 — Brush Up!
- Japanese: `ブラッシュアップ！`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&phase_laterhalf_random==0&is_used_skill_id==202051","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""},{"baseDuration":40000,"condition":"running_style==1&phase_laterhalf_random==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 113701211 — Emergency Reprint
- Japanese: `緊急重版`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&phase_firstquarter_random==2&order<=2&course_distance>=2000","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":12000,"condition":"running_style==1&phase_firstquarter_random==2&order_rate<=50&course_distance>=2000","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 120011 — Dignified Dreamlike Brocade
- Japanese: `威風堂々、夢錦！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&is_finalcorner==1&corner!=0&is_activate_any_skill==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"track_id==10005"},{"baseDuration":50000,"condition":"phase>=2&is_finalcorner==1&corner!=0&is_activate_any_skill==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120031 — Merrymaking Song and Dance
- Japanese: `歌舞歓楽や、ああをかし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase>=2&is_finalcorner_laterhalf==1&course_distance>=2400&course_distance<=2500@phase>=2&is_finalcorner==1&corner==0&course_distance>=2400&course_distance<=2500","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1500,"target":1,"type":22}],"precondition":"distance_rate>=50&order_rate<=50&overtake_target_time>=2"},{"baseDuration":50000,"condition":"phase>=2&is_finalcorner_laterhalf==1@phase>=2&is_finalcorner==1&corner==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate<=50&overtake_target_time>=2"}],"rarity":5,"wisdomCheck":0}
```
---
## 120041 — Miraculously Tubular Oracle
- Japanese: `霊験灼然チョベリグ神託`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_firsthalf==1&is_overtake==1&order_rate<=30&distance_type==2@phase_firsthalf==1&overtake_target_time>=1&order_rate<=30&distance_type==2","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"phase_firsthalf==1&is_overtake==1&order_rate<=30@phase_firsthalf==1&overtake_target_time>=1&order_rate<=30","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120061 — Ashen Trail: Cinderella Gray
- Japanese: `灰の光跡：シンデレラグレイ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=70","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"course_distance==2500&track_id==10005&fan_count>=146738@distance_type==2"},{"baseDuration":50000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=70","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120071 — Vive la GOLD
- Japanese: `Vive la GOLD`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_type==3&is_finalcorner==1&is_overtake==1&order_rate>=50&is_badstart==1@distance_type==4&is_finalcorner==1&is_overtake==1&order_rate>=50&is_badstart==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"distance_type==3&is_finalcorner==1&is_overtake==1&order_rate>=50@distance_type==4&is_finalcorner==1&is_overtake==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120101 — Have S'more Love!
- Japanese: `Have S'more Love!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_laterhalf_random==0&order_rate>=20&order_rate<=70&distance_type==2&ground_type==1","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""},{"baseDuration":40000,"condition":"running_style==2&phase_laterhalf_random==0&order_rate>=20&order_rate<=70","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120111 — Naginata Maiden's Dance
- Japanese: `演舞・撫子大薙刀`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"remain_distance<=401&remain_distance>=399&is_basis_distance==0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate<=70&order_rate>=30&overtake_target_time>=1@distance_rate>=50&order_rate<=70&order_rate>=30&is_overtake==1"},{"baseDuration":50000,"condition":"remain_distance<=401&remain_distance>=399","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate<=70&order_rate>=30&overtake_target_time>=1@distance_rate>=50&order_rate<=70&order_rate>=30&is_overtake==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 120131 — The Sea Glitters, but You're Dazzling
- Japanese: `きらめくは海、まばゆきは君`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&order_rate<=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120231 — Accumulative Victory
- Japanese: `勝利ヘ至ル累積`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51&distance_type==4&order_rate<=50","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":"blocked_side_continuetime>=2&corner!=0"},{"baseDuration":50000,"condition":"distance_rate>=50&distance_rate<=51&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120241 — HOP STEP♪LOCK ON!
- Japanese: `HOP STEP♪LOCK ON!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"phase>=1&order==1@phase>=1&order<=3&is_overtake==1","effects":[{"modifier":750,"target":1,"type":9},{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120301 — Clear Sky Cooking♪
- Japanese: `あおぞらクッキング♪`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"order_rate<=40&phase>=2&corner!=0&is_finalcorner==1&track_id==10008&distance_type==4","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"order_rate<=40&phase>=2&corner!=0&is_finalcorner==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120311 — Full-Throttle Cyclone!
- Japanese: `全力全開！サイクロン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase_laterhalf==0&order_rate<=30","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"is_activate_other_skill_detail==1&distance_type==3&phase==1&corner==0","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120321 — Tachyon Potential
- Japanese: `超光速微粒子の可能性`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&is_finalcorner==1&order_rate<=50&distance_type==3","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"phase>=2&is_finalcorner==1&order_rate<=50","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120351 — GO! Full-send
- Japanese: `GO! Full-send`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"corner==3&course_distance==2400&popularity<=3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase==1&change_order_onetime<0&order_rate>=40&order_rate<=80"},{"baseDuration":40000,"condition":"corner==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase==1&change_order_onetime<0&order_rate>=40&order_rate<=80"}],"rarity":5,"wisdomCheck":0}
```
---
## 120371 — Geschenk of the Salty Sea Breeze
- Japanese: `潮風のGeschenk`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_finalcorner==1&corner!=0&order_rate<=80&order_rate>=40&distance_type==3&track_id==10006","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":50000,"condition":"is_finalcorner==1&corner!=0&order_rate<=80&order_rate>=40&distance_type==3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120401 — Silent Sunset Gold
- Japanese: `Silent Sunset Gold`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=40&distance_rate<=45&order_rate>=30&order_rate<=80","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"remain_distance<=351&remain_distance>=349","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":"phase>=2&blocked_side_continuetime>=2&corner!=0&is_activate_other_skill_detail==1"}],"rarity":5,"wisdomCheck":0}
```
---
## 120451 — Ninja Art: Seal of the Smiling Heart
- Japanese: `忍法・ほほえみ心結の印`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"phase==1&distance_type==3&corner!=0&order_rate>=20&order_rate<=50@phase==1&distance_type==4&corner!=0&order_rate>=20&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":0,"condition":"phase==1&corner!=0&order_rate>=20&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120461 — Forward March!
- Japanese: `Forward March!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"ground_type==2&distance_rate>=50&order_rate_in40_continue==1&is_badstart==0","effects":[{"modifier":5500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"ground_type==2&distance_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120481 — Sick Moves ☆ Juggle Beat
- Japanese: `ヤバ技☆ジャグルビート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":70000,"condition":"slope==0&distance_type==3@slope==1&distance_type==3@slope==0&distance_type==4@slope==1&distance_type==4","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31},{"modifier":500,"target":1,"type":31}],"precondition":"phase>=1&slope==2&order_rate>=30&order_rate<=70"}],"rarity":5,"wisdomCheck":0}
```
---
## 120501 — Overdrive Speed
- Japanese: `Overdrive Speed`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&corner!=0&remain_distance>=600&order_rate>=50&distance_type==3&track_id==10005","effects":[{"modifier":4500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":40000,"condition":"phase>=2&corner!=0&remain_distance>=600&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120601 — Springy Festivities
- Japanese: `もちっと・ハレハレ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase>=2&is_finalcorner==1&order_rate>=40&distance_type==3","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""},{"baseDuration":40000,"condition":"phase>=2&is_finalcorner==1&order_rate>=40","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120611 — The Winding Road to Ideals
- Japanese: `理想へのwinding road`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":60000,"condition":"is_lastspurt==1&phase==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"remain_distance<=600&order_rate>=40&order_rate<=80&is_behind_in==1&change_order_onetime<0"}],"rarity":5,"wisdomCheck":0}
```
---
## 120671 — Ponte de Diamant
- Japanese: `ポンテ・デ・ディアマン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"phase_laterhalf_random==1&order_rate>=40&order_rate<=80&distance_type==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":50000,"condition":"phase_laterhalf_random==1&order_rate>=40&order_rate<=80&distance_type!=3","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 120681 — Becoming Everyone's Joy!
- Japanese: `ミンナノアタシへ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase<=1&change_order_onetime>0&accumulatetime>=5&order_rate<=50@phase<=1&blocked_side_continuetime>=2&accumulatetime>=5&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":60000,"condition":"is_activate_other_skill_detail==1&order<=2&distance_rate>=50&distance_type==4","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 1400011 — Master's Drive
- Japanese: `マスターズドライブ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":50000,"condition":"is_lastspurt==1&phase==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 1400021 — Legendary Accel
- Japanese: `レジェンダリーアクセル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"is_lastspurt==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 200011 — Right Turns ◎
- Japanese: `右回り◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==1","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200012 — Right Turns ○
- Japanese: `右回り○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==1","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200013 — Right Turns ×
- Japanese: `右回り×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==1","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200014 — Clockwise Demon
- Japanese: `右回りの鬼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==1","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200021 — Left Turns ◎
- Japanese: `左回り◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==2","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200022 — Left Turns ○
- Japanese: `左回り○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==2","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200023 — Left Turns ×
- Japanese: `左回り×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==2","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200024 — Counterclockwise Demon
- Japanese: `左回りの鬼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"rotation==2","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200031 — Tokyo Racetrack ◎
- Japanese: `東京レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10006","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200032 — Tokyo Racetrack ○
- Japanese: `東京レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10006","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200033 — Tokyo Racetrack ×
- Japanese: `東京レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10006","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200034 — Child of Fuchu
- Japanese: `府中の申し子`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10006","effects":[{"modifier":600000,"target":1,"type":2},{"modifier":600000,"target":1,"type":5},{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200041 — Nakayama Racetrack ◎
- Japanese: `中山レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10005","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200042 — Nakayama Racetrack ○
- Japanese: `中山レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10005","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200043 — Nakayama Racetrack ×
- Japanese: `中山レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10005","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200051 — Hanshin Racetrack ◎
- Japanese: `阪神レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10009","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200052 — Hanshin Racetrack ○
- Japanese: `阪神レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10009","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200053 — Hanshin Racetrack ×
- Japanese: `阪神レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10009","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200061 — Kyoto Racetrack ◎
- Japanese: `京都レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10008","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200062 — Kyoto Racetrack ○
- Japanese: `京都レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10008","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200063 — Kyoto Racetrack ×
- Japanese: `京都レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10008","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200064 — Child of Yodo
- Japanese: `淀の申し子`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10008","effects":[{"modifier":600000,"target":1,"type":2},{"modifier":600000,"target":1,"type":5},{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200071 — Chukyo Racetrack ◎
- Japanese: `中京レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10007","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200072 — Chukyo Racetrack ○
- Japanese: `中京レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10007","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200073 — Chukyo Racetrack ×
- Japanese: `中京レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10007","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200081 — Sapporo Racetrack ◎
- Japanese: `札幌レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10001","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200082 — Sapporo Racetrack ○
- Japanese: `札幌レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10001","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200083 — Sapporo Racetrack ×
- Japanese: `札幌レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10001","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200091 — Hakodate Racetrack ◎
- Japanese: `函館レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10002","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200092 — Hakodate Racetrack ○
- Japanese: `函館レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10002","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200093 — Hakodate Racetrack ×
- Japanese: `函館レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10002","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200101 — Fukushima Racetrack ◎
- Japanese: `福島レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10004","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200102 — Fukushima Racetrack ○
- Japanese: `福島レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10004","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200103 — Fukushima Racetrack ×
- Japanese: `福島レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10004","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200111 — Niigata Racetrack ◎
- Japanese: `新潟レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10003","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200112 — Niigata Racetrack ○
- Japanese: `新潟レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10003","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200113 — Niigata Racetrack ×
- Japanese: `新潟レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10003","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200121 — Kokura Racetrack ◎
- Japanese: `小倉レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10010","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200122 — Kokura Racetrack ○
- Japanese: `小倉レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10010","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200123 — Kokura Racetrack ×
- Japanese: `小倉レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10010","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200131 — Core Distances ◎
- Japanese: `根幹距離◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_basis_distance==1","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200132 — Core Distances ○
- Japanese: `根幹距離○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_basis_distance==1","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200133 — Core Distances ×
- Japanese: `根幹距離×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_basis_distance==1","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200141 — Non-Core Distances ◎
- Japanese: `非根幹距離◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_basis_distance==0","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200142 — Non-Core Distances ○
- Japanese: `非根幹距離○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_basis_distance==0","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200143 — Non-Core Distances ×
- Japanese: `非根幹距離×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_basis_distance==0","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200151 — Good Track Condition ◎
- Japanese: `良バ場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==1","effects":[{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200152 — Good Track Condition ○
- Japanese: `良バ場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==1","effects":[{"modifier":400000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200153 — Good Track Condition ×
- Japanese: `良バ場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==1","effects":[{"modifier":-400000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200154 — Good Track Demon
- Japanese: `良バ場の鬼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==1","effects":[{"modifier":600000,"target":1,"type":3},{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200161 — Bad Track Condition ◎
- Japanese: `道悪◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==2@ground_condition==3@ground_condition==4","effects":[{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200162 — Bad Track Condition ○
- Japanese: `道悪○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==2@ground_condition==3@ground_condition==4","effects":[{"modifier":400000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200163 — Bad Track Condition ×
- Japanese: `道悪×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==2@ground_condition==3@ground_condition==4","effects":[{"modifier":-400000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200164 — Bad Track Demon
- Japanese: `道悪の鬼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==2@ground_condition==3@ground_condition==4","effects":[{"modifier":600000,"target":1,"type":3},{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200171 — Spring Girl ◎
- Japanese: `春ウマ娘◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==1@season==5","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200172 — Spring Girl ○
- Japanese: `春ウマ娘○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==1@season==5","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200173 — Spring Girl ×
- Japanese: `春ウマ娘×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==1@season==5","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200174 — First Breeze of Spring
- Japanese: `春一番`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==1@season==5","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200181 — Summer Girl ◎
- Japanese: `夏ウマ娘◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==2","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200182 — Summer Girl ○
- Japanese: `夏ウマ娘○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==2","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200183 — Summer Girl ×
- Japanese: `夏ウマ娘×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==2","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200184 — Summer Gale
- Japanese: `青嵐`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==2","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200191 — Autumn Girl ◎
- Japanese: `秋ウマ娘◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==3","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200192 — Autumn Girl ○
- Japanese: `秋ウマ娘○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==3","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200193 — Autumn Girl ×
- Japanese: `秋ウマ娘×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==3","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200194 — The First Storm
- Japanese: `初嵐`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==3","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200201 — Winter Girl ◎
- Japanese: `冬ウマ娘◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==4","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200202 — Winter Girl ○
- Japanese: `冬ウマ娘○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==4","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200203 — Winter Girl ×
- Japanese: `冬ウマ娘×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==4","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200204 — Chilling Wind
- Japanese: `凍て風`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"season==4","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 200211 — Sunny Days ◎
- Japanese: `晴れの日◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"weather==1","effects":[{"modifier":600000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200212 — Sunny Days ○
- Japanese: `晴れの日○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"weather==1","effects":[{"modifier":400000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200221 — Cloudy Days ◎
- Japanese: `曇りの日◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"weather==2","effects":[{"modifier":600000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200222 — Cloudy Days ○
- Japanese: `曇りの日○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"weather==2","effects":[{"modifier":400000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200231 — Rainy Days ◎
- Japanese: `雨の日◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"weather==3","effects":[{"modifier":600000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200232 — Rainy Days ○
- Japanese: `雨の日○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"weather==3","effects":[{"modifier":400000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200233 — Rainy Days ×
- Japanese: `雨の日×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"weather==3","effects":[{"modifier":-400000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200241 — Snowy Days ◎
- Japanese: `雪の日◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"weather==4","effects":[{"modifier":600000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200242 — Snowy Days ○
- Japanese: `雪の日○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"weather==4","effects":[{"modifier":400000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200251 — Inner Gate Affinity ◎
- Japanese: `内枠得意◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"post_number<=3","effects":[{"modifier":600000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200252 — Inner Gate Affinity ○
- Japanese: `内枠得意○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"post_number<=3","effects":[{"modifier":400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200253 — Inner Gate Affinity ×
- Japanese: `内枠苦手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"post_number<=3","effects":[{"modifier":-400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200261 — Outer Gate Affinity ◎
- Japanese: `外枠得意◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"post_number>=6","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200262 — Outer Gate Affinity ○
- Japanese: `外枠得意○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"post_number>=6","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200263 — Outer Gate Affinity ×
- Japanese: `外枠苦手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"post_number>=6","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200271 — Loner ◎
- Japanese: `おひとり様◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style_count_same<=1","effects":[{"modifier":800000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200272 — Loner ○
- Japanese: `おひとり様○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style_count_same<=1","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200281 — Competitive Spirit ◎
- Japanese: `対抗意識◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style_count_same_rate>=40","effects":[{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200282 — Competitive Spirit ○
- Japanese: `対抗意識○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style_count_same_rate>=40","effects":[{"modifier":400000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200283 — Introverted
- Japanese: `引っ込み思案`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style_count_same_rate>=40","effects":[{"modifier":-400000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200291 — Eyes On You ◎
- Japanese: `徹底マーク◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style_equal_popularity_one==1","effects":[{"modifier":600000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200292 — Eyes On You ○
- Japanese: `徹底マーク○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style_equal_popularity_one==1","effects":[{"modifier":400000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200301 — Underdog ◎
- Japanese: `伏兵◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"popularity>=4","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200302 — Underdog ○
- Japanese: `伏兵○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"popularity>=4","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200311 — G1 Dislike
- Japanese: `GⅠ苦手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"grade==100","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200321 — Timid
- Japanese: `小心者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"popularity==1","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200331 — Archline Professor
- Japanese: `弧線のプロフェッサー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200332 — Clever Cornerer ○
- Japanese: `コーナー巧者○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200333 — Clever Cornerer ×
- Japanese: `コーナー巧者×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"all_corner_random==1","effects":[{"modifier":-2000,"target":1,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200341 — Curve Sommelier
- Japanese: `曲線のソムリエ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"all_corner_random==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200342 — Corner Accel ○
- Japanese: `コーナー加速○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"all_corner_random==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200343 — Corner Accel ×
- Japanese: `コーナー加速×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"all_corner_random==1","effects":[{"modifier":-2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200351 — Arc Maestro
- Japanese: `円弧のマエストロ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&corner!=0","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200352 — Corner Recovery ○
- Japanese: `コーナー回復○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&corner!=0","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200353 — Corner Recovery ×
- Japanese: `コーナー回復×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&corner!=0","effects":[{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200361 — Like The Wind
- Japanese: `ハヤテ一文字`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200362 — Straight Skill
- Japanese: `直線巧者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200371 — Gust of Wind
- Japanese: `一陣の風`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200372 — Straight Accel
- Japanese: `直線加速`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200381 — Breath of Fresh Air
- Japanese: `好転一息`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&corner==0","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200382 — Straight Recovery
- Japanese: `直線回復`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&corner==0","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200391 — Hill Dislike
- Japanese: `坂苦手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"up_slope_random==1","effects":[{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200401 — Crowd Hater
- Japanese: `バ群嫌い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"accumulatetime>=2&is_surrounded==1","effects":[{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200411 — Resignation
- Japanese: `あきらめ癖`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"last_straight_random==1&distance_diff_rate>=75","effects":[{"modifier":-2000,"target":1,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200421 — Negligence
- Japanese: `手抜き癖`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance==200&order==1&bashin_diff_behind>=1","effects":[{"modifier":-2000,"target":1,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200431 — Concentration
- Japanese: `コンセントレーション`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"always==1","effects":[{"modifier":4000,"target":1,"type":10}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200432 — Focus
- Japanese: `集中力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"always==1","effects":[{"modifier":9000,"target":1,"type":10}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200433 — Gate Trouble
- Japanese: `ゲート難`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"always==1","effects":[{"modifier":15000,"target":1,"type":10}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200441 — Will of Steel
- Japanese: `鋼の意志`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"phase<=1&accumulatetime>=5&blocked_front_continuetime>=1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":350,"target":1,"type":28}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200442 — Undercover
- Japanese: `隠れ蓑`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"phase<=1&accumulatetime>=5&blocked_front_continuetime>=1","effects":[{"modifier":150,"target":1,"type":9},{"modifier":150,"target":1,"type":28}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200451 — Star of the Show
- Japanese: `注目の踊り子`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==0","effects":[{"modifier":450,"target":1,"type":28}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200452 — Position Sense
- Japanese: `ポジションセンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==0","effects":[{"modifier":350,"target":1,"type":28}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200461 — Now I'm Pumped!
- Japanese: `アガッてきた！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200462 — Up The Pace
- Japanese: `ペースアップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase==1&change_order_onetime<0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200471 — Indomitable Heart
- Japanese: `不屈の心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&change_order_onetime>0","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200472 — Keep the Pace
- Japanese: `ペースキープ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&change_order_onetime>0","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200481 — Where the Wind Blows
- Japanese: `どこ吹く風`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&is_surrounded==1","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200482 — Crowded Calm
- Japanese: `ウマ込み冷静`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&is_surrounded==1","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200491 — Non-stop Girl
- Japanese: `ノンストップガール`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=1&is_lastspurt==1&hp_per>=1","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":250,"target":1,"type":28}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200492 — Slight Detour
- Japanese: `垂れウマ回避`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=1&is_lastspurt==1&hp_per>=1","effects":[{"modifier":2000,"target":1,"type":31},{"modifier":50,"target":1,"type":28}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200501 — Magician of the Lane
- Japanese: `レーンの魔術師`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==2","effects":[{"modifier":350,"target":1,"type":28}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200502 — Improvise
- Japanese: `臨機応変`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==2","effects":[{"modifier":250,"target":1,"type":28}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200511 — Heart and Soul
- Japanese: `全身全霊`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200512 — Last Leg
- Japanese: `末脚`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200521 — Running Idle
- Japanese: `空回り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"accumulatetime>=2&order==1&bashin_diff_behind>=1","effects":[{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200531 — Fortune Favors the Fast
- Japanese: `先手必勝`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200532 — Frontrunner
- Japanese: `先駆け`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200541 — Escape Artist
- Japanese: `脱出術`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200542 — Fast Paced
- Japanese: `急ぎ足`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200551 — Runaway
- Japanese: `逃亡者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&is_finalcorner_random==1&order==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200552 — Press Forward, Ready!
- Japanese: `押し切り準備`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&is_finalcorner_random==1&order==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200561 — Calm and Composed
- Japanese: `余裕綽々`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200562 — Stamina Keep
- Japanese: `スタミナキープ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200571 — Race Planner
- Japanese: `レースプランナー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200572 — Favorite Place
- Japanese: `好位追走`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200581 — Speed Star
- Japanese: `スピードスター`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200582 — Passing Preparations
- Japanese: `抜け出し準備`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&is_finalcorner_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200591 — Quick and Decisive
- Japanese: `迅速果断`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200592 — Position Swiper
- Japanese: `位置取り押し上げ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200601 — Switch-up Pro
- Japanese: `乗り換え上手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200602 — Between the Lines
- Japanese: `差し切り体勢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200611 — Rising Dragon
- Japanese: `昇り龍`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&is_finalcorner==1&corner!=0&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200612 — Outside Pass, Ready!
- Japanese: `外差し準備`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&is_finalcorner==1&corner!=0&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200621 — Sleeping Lion
- Japanese: `眠れる獅子`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==4&phase_random==1&distance_diff_rate>=75","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200622 — On Standby
- Japanese: `後方待機`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==4&phase_random==1&distance_diff_rate>=75","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200631 — Storm and Stress
- Japanese: `疾風怒濤`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_firsthalf_random==3&is_lastspurt==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"phase==2&distance_diff_rate>=50"}],"rarity":2,"wisdomCheck":1}
```
---
## 200632 — Outstanding Stratagem
- Japanese: `仕掛け抜群`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_firsthalf_random==3&is_lastspurt==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase==2&distance_diff_rate>=50"}],"rarity":1,"wisdomCheck":1}
```
---
## 200641 — Imminent Shadow
- Japanese: `迫る影`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==4&is_lastspurt==1&corner==0","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200642 — Straight Shot
- Japanese: `直線一気`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==4&is_lastspurt==1&corner==0","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200651 — Sprint Turbo
- Japanese: `スプリントターボ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200652 — Sprinting Gear
- Japanese: `スプリントギア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200662 — Wait and See
- Japanese: `様子見`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==1&order_rate>50","effects":[{"modifier":150,"target":1,"type":9},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200671 — Jolt of Energy
- Japanese: `電撃の煌めき`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2&order_rate>50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200672 — Draw Forward
- Japanese: `詰め寄り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2&order_rate>50","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200681 — Ruler of Mile
- Japanese: `マイルの支配者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200682 — Positive Planning
- Japanese: `積極策`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200691 — Keen Insight
- Japanese: `慧眼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_laterhalf_random==0&order_rate>50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":-2000,"target":9,"type":21}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200692 — Progress Peek
- Japanese: `展開窺い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_laterhalf_random==0&order_rate>50","effects":[{"modifier":150,"target":1,"type":9},{"modifier":-500,"target":9,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200701 — Big Strides
- Japanese: `豪脚`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_random==2&order_rate>50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200702 — Updraft
- Japanese: `上昇気流`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_random==2&order_rate>50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200711 — Trailblazer
- Japanese: `切り開く者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&phase_random==1&order<=3","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200712 — Bright Future
- Japanese: `前途洋々`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&phase_random==1&order<=3","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200721 — Killer Tune
- Japanese: `キラーチューン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200722 — Uptempo
- Japanese: `テンポアップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200731 — To Victory!
- Japanese: `勝利への執念`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_finalcorner==1&overtake_target_time>=2","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200732 — Stand Your Ground
- Japanese: `食い下がり`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_finalcorner==1&overtake_target_time>=2","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200741 — Cooldown
- Japanese: `クールダウン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200742 — Deep Breaths
- Japanese: `深呼吸`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200751 — Intrinsic Experience
- Japanese: `内的体験`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&is_finalcorner==1&corner!=0&lane_type==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200752 — King of the Castle
- Japanese: `内弁慶`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&is_finalcorner==1&corner!=0&lane_type==0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200761 — Fight or Flight
- Japanese: `火事場のバ鹿力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==4&hp_per<=30","effects":[{"modifier":550,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200762 — Backup Belly
- Japanese: `別腹タンク`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&hp_per<=30","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200771 — Trick (Front)
- Japanese: `トリック（前）`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&order_rate<=50&temptation_opponent_count_behind>=1","effects":[{"modifier":-100,"target":20,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200772 — Captivating Trick
- Japanese: `見惚れるトリック`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&order_rate<=50&temptation_opponent_count_behind>=1","effects":[{"modifier":-300,"target":20,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200781 — Trick (Back)
- Japanese: `トリック（後）`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&order_rate>50&temptation_opponent_count_infront>=1","effects":[{"modifier":-100,"target":19,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200791 — Frantic Runners
- Japanese: `逃げ駆け引き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_temptation_opponent_count_nige>=1&is_temptation==0","effects":[{"modifier":50000,"target":21,"type":13}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200801 — Frantic Leaders
- Japanese: `先行駆け引き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_temptation_opponent_count_senko>=1&is_temptation==0","effects":[{"modifier":50000,"target":21,"type":13}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200811 — Frantic Betweeners
- Japanese: `差し駆け引き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_temptation_opponent_count_sashi>=1&is_temptation==0","effects":[{"modifier":50000,"target":21,"type":13}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200821 — Frantic Chasers
- Japanese: `追込駆け引き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_temptation_opponent_count_oikomi>=1&is_temptation==0","effects":[{"modifier":50000,"target":21,"type":13}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200831 — Restrained Runners
- Japanese: `逃げけん制`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_count_nige_otherself>=1&phase_random==0&accumulatetime>=5","effects":[{"modifier":-100,"target":18,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200841 — Panicked Runners
- Japanese: `逃げ焦り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_count_nige_otherself>=1&phase_random==1","effects":[{"modifier":-100,"target":18,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200851 — Faltering Runners
- Japanese: `逃げためらい`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style_count_nige_otherself>=1&phase_random==2","effects":[{"modifier":-1500,"target":18,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200861 — Restrained Leaders
- Japanese: `先行けん制`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_count_senko_otherself>=1&phase_random==0&accumulatetime>=5","effects":[{"modifier":-100,"target":18,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200871 — Panicked Leaders
- Japanese: `先行焦り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_count_senko_otherself>=1&phase_random==1","effects":[{"modifier":-100,"target":18,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200881 — Faltering Leaders
- Japanese: `先行ためらい`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style_count_senko_otherself>=1&phase_random==2","effects":[{"modifier":-1500,"target":18,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200891 — Restrained Betweeners
- Japanese: `差しけん制`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_count_sashi_otherself>=1&phase_random==0&accumulatetime>=5","effects":[{"modifier":-100,"target":18,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200901 — Panicked Betweeners
- Japanese: `差し焦り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_count_sashi_otherself>=1&phase_random==1","effects":[{"modifier":-100,"target":18,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200911 — Faltering Betweeners
- Japanese: `差しためらい`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style_count_sashi_otherself>=1&phase_random==2","effects":[{"modifier":-1500,"target":18,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200921 — Restrained Chasers
- Japanese: `追込けん制`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_count_oikomi_otherself>=1&phase_random==0&accumulatetime>=5","effects":[{"modifier":-100,"target":18,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200931 — Panicked Chasers
- Japanese: `追込焦り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style_count_oikomi_otherself>=1&phase_random==1","effects":[{"modifier":-100,"target":18,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200941 — Faltering Chasers
- Japanese: `追込ためらい`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style_count_oikomi_otherself>=1&phase_random==2","effects":[{"modifier":-1500,"target":18,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200951 — Ooi Racetrack ◎
- Japanese: `大井レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10101","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200952 — Ooi Racetrack ○
- Japanese: `大井レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10101","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200953 — Ooi Racetrack ×
- Japanese: `大井レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10101","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 200961 — Short Distance Straights ◎
- Japanese: `短距離直線◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&straight_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200962 — Short Distance Straights ○
- Japanese: `短距離直線○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200963 — Lightning Flash
- Japanese: `紫電一閃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200971 — Short Distance Corners ◎
- Japanese: `短距離コーナー◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&all_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200972 — Short Distance Corners ○
- Japanese: `短距離コーナー○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200973 — Lightning Slash
- Japanese: `紫電円刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200981 — Overwhelming Lead
- Japanese: `圧倒的リード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase==1&bashin_diff_behind>=3&order==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200982 — Big Lead
- Japanese: `大きなリード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase==1&bashin_diff_behind>=3&order==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 200991 — Plan X
- Japanese: `プランX`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_laterhalf_random==1&order>=2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 200992 — Countermeasures
- Japanese: `善後策`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_laterhalf_random==1&order>=2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201001 — Flawless Preparation!
- Japanese: `準備万全！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&phase_random==1","effects":[{"modifier":350,"target":1,"type":28},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201002 — Calculated Preparations
- Japanese: `仕掛け準備`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&phase_random==1","effects":[{"modifier":250,"target":1,"type":28},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201011 — Bewitching
- Japanese: `悩殺術`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==0&order_rate<=50&accumulatetime>=5","effects":[{"modifier":-2500,"target":10,"type":21}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201012 — Final Nail
- Japanese: `後方釘付`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==0&order_rate<=50&accumulatetime>=5","effects":[{"modifier":-2000,"target":10,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201021 — Escape Prohibition
- Japanese: `逃亡禁止令`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==1&phase_random==0&order_rate>50&accumulatetime>=5","effects":[{"modifier":-300,"target":9,"type":9},{"modifier":-2000,"target":9,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201022 — No Running Allowed
- Japanese: `抜け駆け禁止`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==1&phase_random==0&order_rate>50&accumulatetime>=5","effects":[{"modifier":-100,"target":9,"type":9},{"modifier":-500,"target":9,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201031 — Mile Straights ◎
- Japanese: `マイル直線◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&straight_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201032 — Mile Straights ○
- Japanese: `マイル直線○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201033 — Cyclone Flash
- Japanese: `豪風一閃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201041 — Mile Corners ◎
- Japanese: `マイルコーナー◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&all_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201042 — Mile Corners ○
- Japanese: `マイルコーナー○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201043 — Cyclone Slash
- Japanese: `豪風円刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201051 — Gear Change
- Japanese: `ギアチェンジ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201052 — Shift Gears
- Japanese: `ギアシフト`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201061 — Accel Full Throttle!
- Japanese: `アクセル全開！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&distance_rate>=50&change_order_onetime<0","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201062 — Acceleration
- Japanese: `アクセラレーション`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&distance_rate>=50&change_order_onetime<0","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201071 — Big Sister Disposition
- Japanese: `姉御肌`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&is_overtake==1&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201072 — Rival Spirit
- Japanese: `負けん気`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&is_overtake==1&accumulatetime>=5","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201081 — Speed Greed
- Japanese: `スピードグリード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_random==1&order<=3","effects":[{"modifier":-2000,"target":10,"type":21},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201082 — Speed Eater
- Japanese: `スピードイーター`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_random==1&order<=3","effects":[{"modifier":-1500,"target":10,"type":21},{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201091 — Battle Formation
- Japanese: `布陣`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_random==0&order_rate>50&accumulatetime>=3","effects":[{"modifier":-3000,"target":9,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201092 — Opener
- Japanese: `布石`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&phase_random==0&order_rate>50&accumulatetime>=3","effects":[{"modifier":-1000,"target":9,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201101 — Medium Distance Straights ◎
- Japanese: `中距離直線◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&straight_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201102 — Medium Distance Straights ○
- Japanese: `中距離直線○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201103 — Photon Flash
- Japanese: `光芒一閃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201111 — Medium Distance Corners ◎
- Japanese: `中距離コーナー◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&all_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201112 — Medium Distance Corners ○
- Japanese: `中距離コーナー○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201113 — Photon Slash
- Japanese: `光芒円刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201121 — Clairvoyance
- Japanese: `千里眼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_random==0","effects":[{"modifier":150000,"target":1,"type":8}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201122 — Hawkeye
- Japanese: `ホークアイ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_random==0","effects":[{"modifier":100000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201131 — Lightning Step
- Japanese: `ライトニングステップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":350,"target":1,"type":28},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201132 — Inazuma Step
- Japanese: `イナズマステップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":250,"target":1,"type":28},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201141 — Miracle Step
- Japanese: `神業ステップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&is_move_lane==1&accumulatetime>=10@distance_type==3&is_move_lane==2&accumulatetime>=10","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201142 — Light Step
- Japanese: `軽やかステップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&is_move_lane==1&accumulatetime>=10@distance_type==3&is_move_lane==2&accumulatetime>=10","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201151 — Monopolizer
- Japanese: `独占力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_random==2&order_rate>50","effects":[{"modifier":-2500,"target":9,"type":21}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201152 — Binding Chains
- Japanese: `束縛`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_random==2&order_rate>50","effects":[{"modifier":-1500,"target":9,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201161 — Charming Whisper
- Japanese: `魅惑のささやき`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&phase==1&blocked_front_continuetime>=1","effects":[{"modifier":-300,"target":9,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201162 — Gentle Whisper
- Japanese: `ささやき`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==3&phase==1&blocked_front_continuetime>=1","effects":[{"modifier":-100,"target":9,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201171 — Long Distance Straights ◎
- Japanese: `長距離直線◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&straight_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201172 — Long Distance Straights ○
- Japanese: `長距離直線○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201173 — Flash of Wind
- Japanese: `烈風一閃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201181 — Long Distance Corners ◎
- Japanese: `長距離コーナー◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&all_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201182 — Long Distance Corners ○
- Japanese: `長距離コーナー○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201183 — Wind Slash
- Japanese: `烈風円刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201191 — Vanguard's Wisdom
- Japanese: `先陣の心得`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==1&bashin_diff_behind>=1&order==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201192 — Keep the Lead
- Japanese: `リードキープ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==1&bashin_diff_behind>=1&order==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201201 — VIP Pass
- Japanese: `VIP顔パス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&is_overtake==1&accumulatetime>=5","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201202 — Pass Expert
- Japanese: `パス上手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&is_overtake==1&accumulatetime>=5","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201211 — Tempestuous Pressure
- Japanese: `怒涛の追い上げ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase==2&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201212 — Press the Attack
- Japanese: `追い上げ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase==2&change_order_onetime<0","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201221 — Stamina Greed
- Japanese: `スタミナグリード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&phase_random==1&order>=5","effects":[{"modifier":-100,"target":9,"type":9},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201222 — Stamina Eater
- Japanese: `スタミナイーター`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_type==4&phase_random==1&order>=5","effects":[{"modifier":-50,"target":9,"type":9},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201231 — Conjurer
- Japanese: `奇術師`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==2","effects":[{"modifier":-100000,"target":9,"type":8}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201232 — Smoke Screen
- Japanese: `目くらまし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_random==2","effects":[{"modifier":-50000,"target":9,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201241 — Runner's Straights ◎
- Japanese: `逃げ直線◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&straight_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201242 — Runner's Straights ○
- Japanese: `逃げ直線○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201243 — Gale Flash
- Japanese: `陣風一閃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201251 — Runner's Corners ◎
- Japanese: `逃げコーナー◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&all_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201252 — Runner's Corners ○
- Japanese: `逃げコーナー○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201253 — Gale Slash
- Japanese: `陣風円刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201261 — Sixth Sense
- Japanese: `シックスセンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase==0&blocked_front_continuetime>=1@running_style==1&phase==0&blocked_side_continuetime>=1","effects":[{"modifier":350,"target":1,"type":28},{"modifier":5000,"target":1,"type":35}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201262 — Danger Avoidance
- Japanese: `危険回避`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase==0&blocked_front_continuetime>=1@running_style==1&phase==0&blocked_side_continuetime>=1","effects":[{"modifier":250,"target":1,"type":28},{"modifier":5000,"target":1,"type":35}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201271 — Top Runner
- Japanese: `トップランナー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase<=1&change_order_onetime>0&accumulatetime>=5@running_style==1&phase<=1&blocked_side_continuetime>=2&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201272 — Lead Pride
- Japanese: `先頭プライド`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase<=1&change_order_onetime>0&accumulatetime>=5@running_style==1&phase<=1&blocked_side_continuetime>=2&accumulatetime>=5","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201281 — Wild Girl
- Japanese: `じゃじゃウマ娘`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==1&slope==1&accumulatetime>=10","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201282 — Leave It to Vigor!
- Japanese: `勢い任せ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==1&slope==1&accumulatetime>=10","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201291 — Recombustion
- Japanese: `再燃焼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==2","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201292 — Next Steps
- Japanese: `二の矢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==2","effects":[{"modifier":2000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201302 — Restart
- Japanese: `リスタート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==1&phase_random==0&order>=2&accumulatetime>=5","effects":[{"modifier":-1000,"target":9,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201311 — Leader's Straights ◎
- Japanese: `先行直線◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&straight_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201312 — Leader's Straights ○
- Japanese: `先行直線○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201313 — Valiant Flash
- Japanese: `勇迅一閃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201321 — Leader's Corners ◎
- Japanese: `先行コーナー◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&all_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201322 — Leader's Corners ○
- Japanese: `先行コーナー○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201323 — Bravery Slash
- Japanese: `勇迅円刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201331 — Technician
- Japanese: `技巧派`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&is_move_lane==1@running_style==2&is_move_lane==2","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201332 — Clever Step
- Japanese: `巧みなステップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&is_move_lane==1@running_style==2&is_move_lane==2","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201341 — Straight Down Resolution
- Japanese: `決意の直滑降`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&down_slope_random==1","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201342 — Straight Down
- Japanese: `直滑降`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&down_slope_random==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201351 — Big Eater
- Japanese: `食いしん坊`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_random==1","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201352 — Nutritional Supplements
- Japanese: `栄養補給`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==2&phase_random==1","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201361 — Unbreakable Spirit
- Japanese: `くじけぬ精神`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&order_rate>40","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201362 — Redo
- Japanese: `まき直し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&order_rate>40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201371 — Glamorous Perturbation
- Japanese: `幻惑のかく乱`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==2&order_rate<=50","effects":[{"modifier":-50000,"target":10,"type":8}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201372 — Perturbation
- Japanese: `かく乱`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==2&order_rate<=50","effects":[{"modifier":-30000,"target":10,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201381 — Betweener's Straights ◎
- Japanese: `差し直線◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&straight_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201382 — Betweener's Straights ○
- Japanese: `差し直線○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201383 — Incisive Flash
- Japanese: `鋭脚一閃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201391 — Betweener's Corners ◎
- Japanese: `差しコーナー◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&all_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201392 — Betweener's Corners ○
- Japanese: `差しコーナー○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201393 — Incisive Slash
- Japanese: `鋭脚円刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201401 — Laborious
- Japanese: `努力家`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&is_overtake==1&accumulatetime>=5","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201402 — Hard Worker
- Japanese: `がんばり屋`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&is_overtake==1&accumulatetime>=5","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201411 — 1M Horsepower
- Japanese: `百万バリキ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&up_slope_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201412 — 100K Horsepower
- Japanese: `十万バリキ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&up_slope_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201421 — Relax
- Japanese: `リラックス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201422 — A Little Break
- Japanese: `小休憩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201431 — Seeing the Big Picture
- Japanese: `大局観`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":150000,"target":1,"type":8}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201432 — Reading Comprehension
- Japanese: `読解力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201441 — Watching All Directions
- Japanese: `八方にらみ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==3&phase_random==2&order_rate>50","effects":[{"modifier":-300,"target":4,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201442 — Sharp Gaze
- Japanese: `鋭い眼光`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==3&phase_random==2&order_rate>50","effects":[{"modifier":-100,"target":4,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201451 — Chaser's Straights ◎
- Japanese: `追込直線◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&straight_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201452 — Chaser's Straights ○
- Japanese: `追込直線○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201453 — Moonlight Flash
- Japanese: `月影一閃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201461 — Chaser's Corners ◎
- Japanese: `追込コーナー◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&all_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201462 — Chaser's Corners ○
- Japanese: `追込コーナー○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201463 — Moonlight Slash
- Japanese: `月影円刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201471 — Good Visibility! All Clear!
- Japanese: `視界良好！異常なし！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&is_move_lane==1@running_style==4&is_move_lane==2","effects":[{"modifier":100000,"target":1,"type":8}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201472 — See Right Through
- Japanese: `お見通し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&is_move_lane==1@running_style==4&is_move_lane==2","effects":[{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201481 — After School Specialist
- Japanese: `下校後のスペシャリスト`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==4&slope==2&accumulatetime>=10","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201482 — Winding Down
- Japanese: `下校の楽しみ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==4&slope==2&accumulatetime>=10","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201491 — Calm and Collected
- Japanese: `冷静沈着`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==4&infront_near_lane_time>=1&accumulatetime>=10","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201492 — Serene
- Japanese: `冷静`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==4&infront_near_lane_time>=1&accumulatetime>=10","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201501 — Heavenly Warrior
- Japanese: `天命士`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_random==2&order_rate>50","effects":[{"modifier":150000,"target":1,"type":8}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201502 — Tactician
- Japanese: `策士`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_random==2&order_rate>50","effects":[{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201511 — Passionate Gaze
- Japanese: `熱いまなざし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_random==2&order>=2","effects":[{"modifier":-2500,"target":4,"type":21}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201512 — Sightlines
- Japanese: `まなざし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_random==2&order>=2","effects":[{"modifier":-1500,"target":4,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201521 — Runner's Tricks ◎
- Japanese: `逃げのコツ◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==1","effects":[{"modifier":600000,"target":1,"type":5},{"modifier":100000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201522 — Runner's Tricks ○
- Japanese: `逃げのコツ○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==1","effects":[{"modifier":400000,"target":1,"type":5},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201531 — Leader's Tricks ◎
- Japanese: `先行のコツ◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==2","effects":[{"modifier":600000,"target":1,"type":5},{"modifier":100000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201532 — Leader's Tricks ○
- Japanese: `先行のコツ○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==2","effects":[{"modifier":400000,"target":1,"type":5},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201541 — Betweener's Tricks ◎
- Japanese: `差しのコツ◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==3","effects":[{"modifier":600000,"target":1,"type":5},{"modifier":100000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201542 — Betweener's Tricks ○
- Japanese: `差しのコツ○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==3","effects":[{"modifier":400000,"target":1,"type":5},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201551 — Chaser's Tricks ◎
- Japanese: `追込のコツ◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==4","effects":[{"modifier":600000,"target":1,"type":5},{"modifier":100000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201552 — Chaser's Tricks ○
- Japanese: `追込のコツ○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==4","effects":[{"modifier":400000,"target":1,"type":5},{"modifier":50000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201561 — Super Lucky Seven
- Japanese: `スーパーラッキーセブン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"random_lot==50&post_number==7","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":2},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201562 — Lucky Seven
- Japanese: `ラッキーセブン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"random_lot==50&post_number==7","effects":[{"modifier":400000,"target":1,"type":1},{"modifier":400000,"target":1,"type":2},{"modifier":400000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201571 — Triple 7s
- Japanese: `スリーセブン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"remain_distance<=778&remain_distance>=776","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201581 — Mountain Climber
- Japanese: `登山家`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"up_slope_random==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201582 — Ultimate Hill Climber
- Japanese: `究極のヒルクライマー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"up_slope_random==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201591 — Big Fan
- Japanese: `ウマ好み`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"near_count>=3&accumulatetime>=5","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201592 — Uma Mania
- Japanese: `ウママニア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"near_count>=3&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201601 — Groundwork
- Japanese: `地固め`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"activate_count_start>=3","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201602 — Unshakable Stance
- Japanese: `盤石の構え`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"activate_count_start>=3","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201611 — Hold Your Tail High
- Japanese: `尻尾上がり`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"activate_count_middle>=3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201612 — Tail of Victory
- Japanese: `尻尾の滝登り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"activate_count_middle>=3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201621 — Shake It Out
- Japanese: `ふり絞り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"activate_count_end_after>=3","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201631 — Sympathy
- Japanese: `シンパシー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"same_skill_horse_count>=5","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201632 — Connection
- Japanese: `コネクト`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==1&is_exist_skill_id==201631","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":0,"target":2,"type":41}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 201641 — Lone Wolf
- Japanese: `一匹狼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"same_skill_horse_count==1","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201651 — Slipstream
- Japanese: `スリップストリーム`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201652 — In the Right Place!
- Japanese: `いいとこ入った！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201661 — Playtime's Over!
- Japanese: `遊びはおしまいっ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"behind_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201662 — Sorry, Gotta Go!
- Japanese: `お先に失礼っ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"behind_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201671 — Trending Charts!
- Japanese: `チャート急上昇！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase==1&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201672 — Recommendation
- Japanese: `レコメンド`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase==1&blocked_side_continuetime>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201681 — Aim for the Front Row!
- Japanese: `狙うは最前列！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==2","effects":[{"modifier":350,"target":1,"type":28},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201682 — Front Row Aim
- Japanese: `前列狙い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==2","effects":[{"modifier":250,"target":1,"type":28},{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201691 — Concealed Readiness
- Japanese: `潜伏態勢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==3&phase_laterhalf_random==0&order_rate>=40","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201692 — Quiet Breathing
- Japanese: `静かな呼吸`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==3&phase_laterhalf_random==0&order_rate>=40","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201701 — Prepared to Die
- Japanese: `決死の覚悟`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_last_straight==1&order_rate>=20&order_rate<=60&phase>=2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201702 — All That There Is
- Japanese: `ありったけ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_last_straight==1&order_rate>=20&order_rate<=60&phase>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 201801 — Uneven Nail
- Japanese: `凸凹ネイル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_condition==1","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 201901 — Fierce Competition
- Japanese: `鍔迫り合い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 201902 — Head-To-Head
- Japanese: `真っ向勝負`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202001 — Sand Expert
- Japanese: `砂の玄人`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"ground_type==2&phase_random==1&order_rate>=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202002 — Sandstorm Practice
- Japanese: `砂塵慣れ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"ground_type==2&phase_random==1&order_rate>=50","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202011 — Shinuchi
- Japanese: `真打`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202012 — Kageuchi
- Japanese: `影打`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202021 — Daring Attack
- Japanese: `強攻策`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&phase_random==1&order_rate>=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202022 — Early Gambit
- Japanese: `早仕掛け`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&phase_random==1&order_rate>=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202031 — Gamester
- Japanese: `博打うち`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_rate_after_random==50","effects":[{"modifier":180,"target":1,"type":27},{"modifier":-400,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202032 — Questionable Strategy
- Japanese: `あやしげな作戦`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_rate_after_random==50","effects":[{"modifier":100,"target":1,"type":27},{"modifier":-400,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202041 — In High Spirits
- Japanese: `意気衝天`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202042 — Nimble Step
- Japanese: `軽い足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202051 — Great Escape
- Japanese: `大逃げ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==1","effects":[{"modifier":0,"target":1,"type":6}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 202061 — #1 Horsegirl in Japan
- Japanese: `日本一のウマ娘`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&is_finalcorner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202071 — Self-Possessed
- Japanese: `泰然自若`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&phase_firsthalf_random==1&order_rate>=40&order_rate<=80","effects":[{"modifier":750,"target":1,"type":9},{"modifier":-1500,"target":1,"type":21}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202072 — My Own Pace
- Japanese: `マイペース`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&phase_firsthalf_random==1&order_rate>=40&order_rate<=80","effects":[{"modifier":350,"target":1,"type":9},{"modifier":-1500,"target":1,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202081 — Rise From the Ashes
- Japanese: `起死回生`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202082 — One Chance
- Japanese: `ワンチャンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202091 — Burning Spirit
- Japanese: `気炎万丈`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase==1&order_rate<=80&order_rate>=30&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202092 — Fighting Spirit
- Japanese: `闘争心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase==1&order_rate<=80&order_rate>=30&blocked_side_continuetime>=2","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202101 — Elation
- Japanese: `高揚感`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202102 — Tumbling Forward
- Japanese: `前のめり`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202111 — Unstoppable Force
- Japanese: `破竹の勢い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&is_finalcorner_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202112 — Sufficient Spirit
- Japanese: `気合十分`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&is_finalcorner_random==1&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202121 — Daredevil
- Japanese: `大胆不敵`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&distance_rate_after_random==50&order_rate>=30&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202122 — Fearless Heart
- Japanese: `恐れぬ心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&distance_rate_after_random==50&order_rate>=30&order_rate<=80","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202131 — Wild Whirlwind
- Japanese: `荒ぶる旋風`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_random==1&order<=3","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":-1500,"target":10,"type":21}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202132 — With Verve
- Japanese: `気迫を込めて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_random==1&order<=3","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":-350,"target":10,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202141 — Don't Tell Me What to Do!
- Japanese: `アタシに指図しないで！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"always==1","effects":[{"modifier":850,"target":1,"type":14},{"modifier":-400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202151 — Pushing Forward
- Japanese: `勇往邁進`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202152 — Full Throttle
- Japanese: `フルスロットル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202161 — Self-Control
- Japanese: `自制心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"always==1","effects":[{"modifier":600000,"target":1,"type":5},{"modifier":-30000,"target":1,"type":29}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202171 — Supreme Downhiller
- Japanese: `至高のダウンヒラー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"down_slope_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202172 — Downhill Adept
- Japanese: `下り坂巧者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"down_slope_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202181 — 99 Problems
- Japanese: `99 Problems`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"always==1","effects":[{"modifier":-400000,"target":1,"type":4},{"modifier":-400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202191 — Single-Minded
- Japanese: `一意専心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"is_badstart==0&running_style==2&distance_type==4&phase_firsthalf_random==1","effects":[{"modifier":750,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202192 — Faultless
- Japanese: `抜かりなし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"is_badstart==0&running_style==2&distance_type==4&phase_firsthalf_random==1","effects":[{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202201 — Kawasaki Racetrack ◎
- Japanese: `川崎レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10103","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202202 — Kawasaki Racetrack ○
- Japanese: `川崎レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10103","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202203 — Kawasaki Racetrack ×
- Japanese: `川崎レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10103","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202211 — Funabashi Racetrack ◎
- Japanese: `船橋レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10104","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202212 — Funabashi Racetrack ○
- Japanese: `船橋レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10104","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202213 — Funabashi Racetrack ×
- Japanese: `船橋レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10104","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202221 — Morioka Racetrack ◎
- Japanese: `盛岡レース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10105","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202222 — Morioka Racetrack ○
- Japanese: `盛岡レース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10105","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202223 — Morioka Racetrack ×
- Japanese: `盛岡レース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10105","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202231 — Nocturnal ◎
- Japanese: `ナイター◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"time==4","effects":[{"modifier":600000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202232 — Nocturnal ○
- Japanese: `ナイター○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"time==4","effects":[{"modifier":400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202233 — Nocturnal ×
- Japanese: `ナイター×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"time==4","effects":[{"modifier":-400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202241 — Tight Turns ◎
- Japanese: `小回り◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_tight_track==1","effects":[{"modifier":600000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202242 — Tight Turns ○
- Japanese: `小回り○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_tight_track==1","effects":[{"modifier":400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202243 — Tight Turns ×
- Japanese: `小回り×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_tight_track==1","effects":[{"modifier":-400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202251 — Exchange Races ◎
- Japanese: `交流重賞◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_dirtgrade==1","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202252 — Exchange Races ○
- Japanese: `交流重賞○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_dirtgrade==1","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202253 — Exchange Races ×
- Japanese: `交流重賞×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_dirtgrade==1","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202254 — Exchange Races Demon
- Japanese: `交流重賞の鬼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"is_dirtgrade==1","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 202261 — Victory Opportunity
- Japanese: `勝利の機運`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202262 — Promising Omen
- Japanese: `明るい兆し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202271 — Redoubled Efforts
- Japanese: `捲土重来`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202272 — Turnaround
- Japanese: `盛り返し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase_random==1&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202281 — Full Speed Ahead!
- Japanese: `全速前進！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==3&order_rate<=50&is_lastspurt==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202282 — At Full Speed
- Japanese: `まっしぐら`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==3&order_rate<=50&is_lastspurt==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202291 — Clear and Serene
- Japanese: `明鏡止水`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"ground_type==2&order_rate>=50&activate_count_heal>=1&distance_rate<=42&phase==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202292 — Clear Head
- Japanese: `冴える思考`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"ground_type==2&order_rate>=50&activate_count_heal>=1&distance_rate<=42&phase==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202301 — Leisurely Dust Bath
- Japanese: `優雅な砂浴び`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&accumulatetime>=5&infront_near_lane_time>=3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202302 — Dust Bath ○
- Japanese: `砂浴び○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&accumulatetime>=5&infront_near_lane_time>=3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202303 — Dust Bath ×
- Japanese: `砂浴び×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&accumulatetime>=5&infront_near_lane_time>=3","effects":[{"modifier":-2000,"target":1,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202311 — Aim for the Center!
- Japanese: `目指せセンター！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202312 — Full of Zeal
- Japanese: `意気込み十分`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202321 — Blast Mode!
- Japanese: `爆走モード！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==2&order_rate>=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202322 — Rapid Ascent
- Japanese: `急浮上`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_random==2&order_rate>=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202331 — Outstanding Step
- Japanese: `抜群の踏み込み`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==2&base_power>=1200","effects":[{"modifier":800000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"ground_type==2&base_power>=1000&base_power<1200","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 202332 — Skillful Step
- Japanese: `踏み込み上手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==2&base_power>=1200","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"ground_type==2&base_power>=1000&base_power<1200","effects":[{"modifier":200000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202341 — Mud Master
- Japanese: `泥んこマイスター`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==2&ground_condition==3@ground_type==2&ground_condition==4","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 202342 — Mud Play ◎
- Japanese: `泥遊び◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==2&ground_condition==3@ground_type==2&ground_condition==4","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202343 — Mud Play ○
- Japanese: `泥遊び○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==2&ground_condition==3@ground_type==2&ground_condition==4","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202344 — Mud Play ×
- Japanese: `泥遊び×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"ground_type==2&ground_condition==3@ground_type==2&ground_condition==4","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202351 — Dancer of the Sands
- Japanese: `砂上の舞姫`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&accumulatetime>=10&phase==0&order<=1&bashin_diff_behind<=1","effects":[{"modifier":-2500,"target":10,"type":21}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202352 — Cloud of Dust
- Japanese: `土煙`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&accumulatetime>=10&phase==0&order<=1&bashin_diff_behind<=1","effects":[{"modifier":-1500,"target":10,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202361 — Don't Let Your Guard Down
- Japanese: `油断大敵`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&distance_rate>=50&is_other_character_activate_advantage_skill==9","effects":[{"modifier":-2500,"target":23,"type":21}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202362 — Pressing Feeling
- Japanese: `圧迫感`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&distance_rate>=50&is_other_character_activate_advantage_skill==9","effects":[{"modifier":-1500,"target":23,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202371 — Unstoppable
- Japanese: `アンストッパブル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&running_style==2","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202372 — Attack Stance
- Japanese: `攻めの姿勢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&running_style==2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202381 — Breakthrough
- Japanese: `ブレイクスルー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&running_style==4&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":28}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202382 — Breakthrough Plan
- Japanese: `打開策`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&running_style==4&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":150,"target":1,"type":28}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202391 — 1000% Output!
- Japanese: `出力1000％！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":27000,"condition":"phase_firsthalf_random==1&running_style==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-400,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202392 — Frantic State
- Japanese: `しゃかりき`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":27000,"condition":"phase_firsthalf_random==1&running_style==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-400,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202401 — Lightning Speed
- Japanese: `電光石火`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"distance_type==1&phase>=2&order_rate>=50&is_overtake==1@distance_type==2&phase>=2&order_rate>=50&is_overtake==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202402 — Mighty Leap
- Japanese: `一足飛び`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"distance_type==1&phase>=2&order_rate>=50&is_overtake==1@distance_type==2&phase>=2&order_rate>=50&is_overtake==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202411 — Winds of Change
- Japanese: `風雲の志`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&order>=2&distance_diff_top<=5&distance_rate>=60&phase==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202412 — Ambitions
- Japanese: `向上心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&order>=2&distance_diff_top<=5&distance_rate>=60&phase==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202421 — Lose Yourself
- Japanese: `無我夢中`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==4&running_style==3&is_lastspurt==1&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202422 — Devil-May-Care
- Japanese: `がむしゃら`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==4&running_style==3&is_lastspurt==1&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202431 — Steady Advance
- Japanese: `快進撃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&running_style==2&phase_laterhalf_random==1&distance_diff_top<=10","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":3000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202432 — Firm Step
- Japanese: `確かな足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&running_style==2&phase_laterhalf_random==1&distance_diff_top<=10","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202441 — Gambler
- Japanese: `勝負師`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"popularity<=3&random_lot==30","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3},{"modifier":800000,"target":1,"type":4}],"precondition":""},{"baseDuration":-1,"condition":"popularity>=4&random_lot==60","effects":[{"modifier":800000,"target":1,"type":1},{"modifier":800000,"target":1,"type":3},{"modifier":800000,"target":1,"type":4}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 202442 — Gambling Spirit
- Japanese: `やまっけ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"popularity<=3&random_lot==15","effects":[{"modifier":400000,"target":1,"type":1},{"modifier":400000,"target":1,"type":3},{"modifier":400000,"target":1,"type":4}],"precondition":""},{"baseDuration":-1,"condition":"popularity>=4&random_lot==30","effects":[{"modifier":400000,"target":1,"type":1},{"modifier":400000,"target":1,"type":3},{"modifier":400000,"target":1,"type":4}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202451 — Top Gear
- Japanese: `トップギア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&is_last_straight==1&order>=2&distance_diff_top<=10","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202452 — Razor-Sharp Stride
- Japanese: `キレる脚`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&is_last_straight==1&order>=2&distance_diff_top<=10","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202461 — Untouchable Shadow
- Japanese: `踏ませぬ影`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&is_last_straight==1&order==1&bashin_diff_behind<=1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202462 — Steadfast
- Japanese: `粘り腰`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&is_last_straight==1&order==1&bashin_diff_behind<=1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202471 — Hot Pursuit
- Japanese: `猛追`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&distance_rate>=50&is_overtake==1@running_style==3&distance_rate>=50&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202472 — Tooth and Tail
- Japanese: `食らいつき`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&distance_rate>=50&is_overtake==1@running_style==3&distance_rate>=50&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202481 — Monster
- Japanese: `怪物`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&running_style==2&phase==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"distance_diff_top<=10&distance_rate>=60&phase==1"}],"rarity":2,"wisdomCheck":1}
```
---
## 202482 — True Worth
- Japanese: `本領発揮`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&running_style==2&phase==2","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":"distance_diff_top<=10&distance_rate>=60&phase==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 202491 — Unrivaled Wits
- Japanese: `抜群の切れ味`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==4&phase_firsthalf_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"distance_rate>=66&order_rate_out50_continue==1&temptation_count==0"}],"rarity":2,"wisdomCheck":1}
```
---
## 202492 — Witful
- Japanese: `切れ味`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==4&phase_firsthalf_random==2","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":"distance_rate>=66&order_rate_out50_continue==1&temptation_count==0"}],"rarity":1,"wisdomCheck":1}
```
---
## 202501 — Reckless
- Japanese: `遮二無二`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202502 — Rushing in Blind
- Japanese: `向こう見ず`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202511 — Favorite, For Reals?!
- Japanese: `1番人気でヤバたん`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"always==1","effects":[{"modifier":100000,"target":1,"type":29}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202521 — Seamless
- Japanese: `天衣無縫`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&corner_random==3&order_rate>=50@distance_type==4&corner_random==3&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202522 — Mold Breaker
- Japanese: `型破り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&corner_random==3&order_rate>=50@distance_type==4&corner_random==3&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202531 — Ascendance
- Japanese: `優位形成`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1@distance_type==3&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202532 — Graceful Step
- Japanese: `しとやかな足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1@distance_type==3&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202541 — Dignified
- Japanese: `威風堂々`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&order_rate>=40&is_finalcorner_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":-1500,"target":9,"type":21},{"modifier":-1500,"target":10,"type":21}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202542 — Pressure
- Japanese: `プレッシャー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&order_rate>=40&is_finalcorner_random==1","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":-350,"target":9,"type":21},{"modifier":-350,"target":10,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202551 — Divine Speed
- Japanese: `神速`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate_after_random==50","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202552 — Rapid
- Japanese: `快速`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate_after_random==50","effects":[{"modifier":1500,"target":1,"type":22},{"modifier":35,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202561 — One-shot
- Japanese: `一発必中`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_laterhalf_random==1&order_rate>=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202562 — Lock On
- Japanese: `ロックオン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_laterhalf_random==1&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202571 — Miracle Pathmaker
- Japanese: `未来を拓く奇跡`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==1&phase_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202581 — Ahead of the Game
- Japanese: `脱兎の先へ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":550,"target":1,"type":9},{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202582 — Stay the Course
- Japanese: `脇目も振らず`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":150,"target":1,"type":9},{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202591 — In One Fell Swoop
- Japanese: `一気呵成`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==3&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202592 — Great Haste
- Japanese: `大急ぎ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==3&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202601 — Luminescence
- Japanese: `ルミネセンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&activate_count_all>=13","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202602 — Ignition
- Japanese: `イグニッション`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&activate_count_all>=13","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202611 — Inspiration
- Japanese: `インスピレーション`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_laterhalf_random==0&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202612 — Overflowing Passion
- Japanese: `溢れる情熱`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_laterhalf_random==0&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202621 — Blitzing Spirit
- Japanese: `突撃魂`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202622 — On the Move
- Japanese: `進出開始`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202641 — Thousand-Mile Journey
- Japanese: `千里の道`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==1&order_rate>=40&order_rate<=90","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202642 — From the First Step
- Japanese: `一歩から`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==1&order_rate>=40&order_rate<=90","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202651 — Cloud Dragon's Metamorphosis
- Japanese: `雲蒸竜変`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_speed>=1000&base_power>=1000&distance_type==2@base_speed>=1000&base_power>=1000&distance_type==3","effects":[{"modifier":600000,"target":1,"type":1},{"modifier":600000,"target":1,"type":3}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 202652 — Self-Assured
- Japanese: `自信家`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_speed>=1000&base_power>=1000&distance_type==2@base_speed>=1000&base_power>=1000&distance_type==3","effects":[{"modifier":200000,"target":1,"type":1},{"modifier":200000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202661 — Surging Beat
- Japanese: `昂る鼓動`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=30&order_rate<=80@distance_type==4&phase_firsthalf_random==2&order_rate>=30&order_rate<=80","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202662 — Rising Passion
- Japanese: `込み上げる熱`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=30&order_rate<=80@distance_type==4&phase_firsthalf_random==2&order_rate>=30&order_rate<=80","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202671 — High Voltage
- Japanese: `ハイボルテージ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202672 — High Hopes
- Japanese: `心弾んで`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202681 — Seriously☆Good↑Vibes
- Japanese: `ブチ☆アゲ↑バイブス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202682 — Up the Vibes
- Japanese: `バイブス上昇`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202691 — Further Than Anyone
- Japanese: `誰より前へ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==3&always==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202692 — Early Bird
- Japanese: `一番乗り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==3&always==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202701 — Singularity
- Japanese: `シンギュラリティ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==2&distance_type==3&base_speed>=1200&base_wiz>=1200","effects":[{"modifier":800000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"running_style==2&distance_type==3&base_speed>=1200&base_wiz<1200","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 202702 — Inquisitive Mind
- Japanese: `探求心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==2&distance_type==3&base_speed>=1200&base_wiz>=1200","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"running_style==2&distance_type==3&base_speed>=1200&base_wiz<1200","effects":[{"modifier":200000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202711 — Check
- Japanese: `王手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==2&phase>=2&is_finalcorner==1&corner!=0&remain_distance>=600&order_rate<=70@running_style==3&phase>=2&is_finalcorner==1&corner!=0&remain_distance>=600&order_rate<=70","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202712 — Satisfying Pace
- Japanese: `会心の一歩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==2&phase>=2&is_finalcorner==1&corner!=0&remain_distance>=600&order_rate<=70@running_style==3&phase>=2&is_finalcorner==1&corner!=0&remain_distance>=600&order_rate<=70","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202721 — Never Give Up
- Japanese: `ネバーギブアップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202722 — Unbreakable Mind
- Japanese: `折れない心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_corner_random==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202731 — Longchamp Racetrack ◎
- Japanese: `ロンシャンレース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10201","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202732 — Longchamp Racetrack ○
- Japanese: `ロンシャンレース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10201","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202733 — Longchamp Racetrack ×
- Japanese: `ロンシャンレース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10201","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202734 — Child of Longchamp
- Japanese: `ロンシャンの申し子`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10201","effects":[{"modifier":600000,"target":1,"type":2},{"modifier":600000,"target":1,"type":5},{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 202741 — Pure Perfection
- Japanese: `十全十美`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&corner_random==3&order_rate<=50@distance_type==3&corner_random==3&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202742 — Refined Conduct
- Japanese: `品行方正`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&corner_random==3&order_rate<=50@distance_type==3&corner_random==3&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202751 — Unyielding Tenacity
- Japanese: `気骨稜稜`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202752 — Single-Minded Advance
- Japanese: `ひたむき前進`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202761 — Send It Flying!
- Japanese: `かっとばせ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202762 — Toward Victory
- Japanese: `勝利に向かって`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202771 — Laser-Focused
- Japanese: `一点集中`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==2&distance_type==4&phase_firstquarter_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202772 — Honing In
- Japanese: `狙いを定めて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==2&distance_type==4&phase_firstquarter_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202791 — Exquisite Timing
- Japanese: `時中の妙`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202792 — Middle Leg Adept
- Japanese: `中盤巧者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202801 — Battle for Initiative
- Japanese: `機先の勝負`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_laterhalf_random==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202802 — Opening Leg Adept
- Japanese: `序盤巧者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_laterhalf_random==0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202811 — Finishing Touch
- Japanese: `画竜点睛`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==1&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202812 — Finale
- Japanese: `大詰め`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==1&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202821 — One Sky, One Goal
- Japanese: `万里一空`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==4&running_style==1&is_lastspurt==1&corner==0&order<=3","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202822 — No Hesitation
- Japanese: `迷いなし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==4&running_style==1&is_lastspurt==1&corner==0&order<=3","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202831 — Call & Response
- Japanese: `コール&レスポンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase==1&is_activate_any_skill==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_activate_any_skill==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202832 — Backup Planning
- Japanese: `二段構え`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase==1&is_activate_any_skill==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_activate_any_skill==1","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202841 — Sand Virtuoso
- Japanese: `砂の妙手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"ground_type==2&phase_random==1&order_rate<=50","effects":[{"modifier":550,"target":1,"type":9},{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202842 — Dust Off
- Japanese: `砂払い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"ground_type==2&phase_random==1&order_rate<=50","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202851 — Clean Sweep
- Japanese: `一網打尽`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==4&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202852 — Rapid Overtakes
- Japanese: `ごぼう抜き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==4&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202861 — Rocket Start
- Japanese: `ロケットスタート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==1&always==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202862 — Swift Takeoff
- Japanese: `急発進`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"distance_type==1&always==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202871 — Reign
- Japanese: `君臨`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==3&running_style==4&phase>=2&is_finalcorner==1&corner!=0&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202872 — Mighty Step
- Japanese: `渾身の足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==3&running_style==4&phase>=2&is_finalcorner==1&corner!=0&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202881 — Complete Combustion
- Japanese: `完全燃焼`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&is_last_straight==1&order>=2&distance_diff_top<=10","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202882 — Boiling Blood
- Japanese: `たぎる血潮`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&is_last_straight==1&order>=2&distance_diff_top<=10","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202891 — Clear Mind
- Japanese: `心頭滅却`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==4&phase_laterhalf_random==0&order_rate>=50","effects":[{"modifier":550,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202892 — Immovable Spirit
- Japanese: `不動の心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"running_style==4&phase_laterhalf_random==0&order_rate>=50","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202901 — Soaring Stride
- Japanese: `飛翔脚`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202902 — Sufficient Thrust
- Japanese: `推力十分`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202912 — Cleave
- Japanese: `切り崩し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==4&order_rate>=50&is_finalcorner_random==1","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":-350,"target":9,"type":21},{"modifier":-350,"target":10,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202921 — Undivided Focus
- Japanese: `一心不乱`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202922 — No Reluctance
- Japanese: `惜しみなし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202931 — Relentless Approach
- Japanese: `肉薄`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&distance_rate>=50&is_overtake==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202932 — Shadowstepper
- Japanese: `影踏み`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&distance_rate>=50&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202942 — Ghastly
- Japanese: `鬼気迫って`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&running_style==4&phase_random==1&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":-350,"target":9,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202951 — Pioneer of the Sands
- Japanese: `砂の開拓者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202952 — Pioneer
- Japanese: `パイオニア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&phase_laterhalf_random==0&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202961 — Ardour
- Japanese: `熱情`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202962 — Boiling Emotions
- Japanese: `滾る想い`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202971 — Golden Opportunity
- Japanese: `千載一遇`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==4&distance_type==4&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202972 — Seize the Chance
- Japanese: `好機を捉えて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==4&distance_type==4&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202981 — Gamma Ray Burst
- Japanese: `流星光底`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 202982 — Leap Premonition
- Japanese: `飛躍の予感`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 202991 — Straight Course ◎
- Japanese: `直線コース◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"corner_count==0","effects":[{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202992 — Straight Course ○
- Japanese: `直線コース○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"corner_count==0","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 202993 — Straight Course ×
- Japanese: `直線コース×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"corner_count==0","effects":[{"modifier":-400000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 203001 — Manipulation
- Japanese: `掌握`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&phase>=2&corner!=0&is_overtake==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203002 — Art of Coaxing
- Japanese: `手練手管`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==4&phase>=2&corner!=0&is_overtake==1","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203011 — Lightning Blitz
- Japanese: `電迅速攻`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==1&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203012 — Explosive Force
- Japanese: `瞬発力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==1&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203021 — Wind Rider
- Japanese: `風翔`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203022 — Wind Vane
- Japanese: `風切り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203031 — Frontal Attack
- Japanese: `正攻法`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203032 — An Honest Step
- Japanese: `素直な一歩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203041 — Fluttering Heart
- Japanese: `トキメキハート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_firsthalf_random==2@distance_type==2&phase_firsthalf_random==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203042 — Pounding Chest
- Japanese: `胸の高鳴り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_firsthalf_random==2@distance_type==2&phase_firsthalf_random==2","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203051 — Unwavering Ambition
- Japanese: `初志貫徹`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203052 — Unshakeable Faith
- Japanese: `揺るがぬ信念`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203061 — No Second Thoughts
- Japanese: `無二`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&furlong==1&near_infront_count==0&corner==0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==1&furlong==1&near_infront_count==0","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203071 — No Third Chances
- Japanese: `無三`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&furlong==2&near_infront_count==0&corner==0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==1&furlong==2&near_infront_count==0","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203081 — Stamp on the Ground
- Japanese: `踏みしめる大地`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"ground_type==2&running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203082 — With All My Might
- Japanese: `力の限り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"ground_type==2&running_style==2&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203091 — Sandstorm Flash
- Japanese: `砂塵一閃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&straight_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203092 — Dirt Straights ◎
- Japanese: `ダート直線◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&straight_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203093 — Dirt Straights ○
- Japanese: `ダート直線○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&straight_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203101 — Sandstorm Slash
- Japanese: `砂塵円刃`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&all_corner_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203102 — Dirt Corners ◎
- Japanese: `ダートコーナー◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&all_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203103 — Dirt Corners ○
- Japanese: `ダートコーナー○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&all_corner_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203111 — Just Rule
- Japanese: `王道一途`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203112 — Frontal Breakthrough
- Japanese: `正面突破`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203121 — Proof of Strength
- Japanese: `強者の証`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==2&distance_type==3&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203122 — To Greater Heights
- Japanese: `さらなる高みへ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==2&distance_type==3&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203131 — Curtain Closer
- Japanese: `幕引き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&is_last_straight==1&distance_diff_top_float<=25","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203132 — Decisive Blow
- Japanese: `決定打`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&is_last_straight==1&distance_diff_top_float<=25","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203141 — Sharp-Witted Composure
- Japanese: `怜悧清澄`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203142 — Self-Restraint
- Japanese: `克己心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203151 — Pure Instincts
- Japanese: `本能の解放`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&remain_distance<=200@running_style==4&remain_distance<=200","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":"compete_fight_count>0"}],"rarity":2,"wisdomCheck":1}
```
---
## 203152 — Bare Passion
- Japanese: `むきだしの情熱`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&remain_distance<=200@running_style==4&remain_distance<=200","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":"compete_fight_count>0"}],"rarity":1,"wisdomCheck":1}
```
---
## 203161 — Peerless Boldness
- Japanese: `豪胆無比`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&order_rate<=50&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203162 — Fearless Advance
- Japanese: `後先恐れず`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&order_rate<=50&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203171 — Tension and Release
- Japanese: `一張一弛`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==3&phase_laterhalf_random==0","effects":[{"modifier":-1500,"target":1,"type":21}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase_firsthalf_random==2","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203172 — Switch Over Pro
- Japanese: `切り替え上手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==3&phase_laterhalf_random==0","effects":[{"modifier":-1500,"target":1,"type":21}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase_firsthalf_random==2","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203181 — Embracing Virtue and Vice
- Japanese: `清濁併呑`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203182 — Contradicting Emotions
- Japanese: `裏腹なキモチ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203201 — Quick Work
- Japanese: `早業`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203202 — Not Even a Glimpse
- Japanese: `目にも留まらず`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==1&phase_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203212 — Free-Spirited
- Japanese: `気の向くままに`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==4&running_style==1&is_last_straight==1&order<=3&motivation>=4","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"distance_type==4&running_style==1&is_last_straight==1&order<=3","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203221 — Breaking Free
- Japanese: `影従打破`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203222 — Aggressive
- Japanese: `アグレッシブ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203231 — Surging Fighting Spirit
- Japanese: `ハジける闘志`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==0","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203232 — Restless Step
- Japanese: `逸る足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203241 — Chain Reaction
- Japanese: `連鎖反応`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase==1&corner==0","effects":[{"modifier":550,"target":1,"type":9},{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203242 — Fuse
- Japanese: `端緒`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase==1&corner==0","effects":[{"modifier":150,"target":1,"type":9},{"modifier":350,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203251 — Like a Blaze
- Japanese: `烈火の如く`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=40@distance_type==4&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203252 — Surprise Attack
- Japanese: `急襲`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate>=40@distance_type==4&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203262 — Firm Resolve
- Japanese: `覚悟を決めて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&distance_type==4&phase_firstquarter_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203272 — Spearhead
- Japanese: `切り込み隊長`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&phase_laterhalf_random==0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203281 — Unconscious Shackles
- Japanese: `無意識の枷`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"always==1","effects":[{"modifier":-1000000,"target":1,"type":1},{"modifier":-1000000,"target":1,"type":2},{"modifier":-1000000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 203301 — Peak Ferocity
- Japanese: `熾烈の極み`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203302 — Fervor
- Japanese: `熱狂的`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==4&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203311 — Flash
- Japanese: `閃光`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203312 — Towards the Light
- Japanese: `光差す方へ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203322 — Descent
- Japanese: `駆け降り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&down_slope_random==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203331 — Thorough Preparation
- Japanese: `用意周到`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_firsthalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203332 — Preliminary Preparation
- Japanese: `下準備`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_firsthalf_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203341 — Pursuer
- Japanese: `追跡者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&distance_type==3&phase_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203342 — Creeping Footsteps
- Japanese: `這い寄る足音`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&distance_type==3&phase_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203351 — Brave and Bold
- Japanese: `勇猛果敢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&order_rate>=40&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203352 — High Pitch
- Japanese: `ハイピッチ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&order_rate>=40&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203361 — Proven Mettle
- Japanese: `真骨頂`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203362 — Forward Step by Step
- Japanese: `一歩ずつ前へ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203371 — Seize the Initiative
- Japanese: `後の先`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==27@distance_type==4&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==27@distance_type==3&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==22@distance_type==4&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==22","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203372 — Striking Back
- Japanese: `切り返し`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==27@distance_type==4&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==27@distance_type==3&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==22@distance_type==4&phase>=2&is_finalcorner==1&is_other_character_activate_advantage_skill==22","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203381 — The Fight's Not Over Yet!
- Japanese: `勝負はここから！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==3&running_style==1&phase>=2&is_finalcorner==1&corner!=0&order<=3","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203382 — Pulling Away
- Japanese: `逃げ切り体勢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"distance_type==3&running_style==1&phase>=2&is_finalcorner==1&corner!=0&order<=3","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203391 — Gallant Figure
- Japanese: `英姿颯爽`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&running_style==1&corner_random==3&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203392 — Unprecedented
- Japanese: `破天荒`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&running_style==1&corner_random==3&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203402 — Riding the Tailwind
- Japanese: `追い風に乗って`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&distance_type==3&phase_firstquarter_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203411 — Fruits of Labor
- Japanese: `努力の結実`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==2&distance_type==4&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203412 — Steady Effort
- Japanese: `地道に重ねて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==2&distance_type==4&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203421 — Forthright
- Japanese: `正々堂々`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203422 — Believe in Yourself
- Japanese: `己を信じて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203431 — Brilliant Mind
- Japanese: `才気煥発`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203432 — Dynamic Motion
- Japanese: `躍動`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203441 — To the Stage of Dreams
- Japanese: `夢の舞台へ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==2&distance_type==3&phase_firstquarter_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203442 — Surpassing Ambitions
- Japanese: `憧れを越えて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==2&distance_type==3&phase_firstquarter_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203452 — Turning Point
- Japanese: `ターニングポイント`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==3&distance_type==1&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203461 — Preeminent
- Japanese: `傑出`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&distance_rate>=50&overtake_target_time>=1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203462 — Outstanding Step
- Japanese: `抜きん出る一歩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&distance_rate>=50&overtake_target_time>=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203471 — Furious Sprint
- Japanese: `猛烈激走`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&remain_distance<=200@running_style==2&remain_distance<=200","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":"compete_fight_count>0"}],"rarity":2,"wisdomCheck":1}
```
---
## 203472 — Overflowing Fighting Spirit
- Japanese: `みなぎる闘志`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&remain_distance<=200@running_style==2&remain_distance<=200","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":"compete_fight_count>0"}],"rarity":1,"wisdomCheck":1}
```
---
## 203481 — Initiative
- Japanese: `イニシアチブ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==1&distance_type==1&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203482 — Unyielding Step
- Japanese: `譲れぬ一歩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==1&distance_type==1&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203491 — Fierce Clash
- Japanese: `丁々発止`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&distance_type==1&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203492 — Flying Sparks
- Japanese: `火花散らして`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&distance_type==1&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203501 — Unpredecented Prodigy
- Japanese: `英俊豪傑`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203502 — Peerless
- Japanese: `比類なき`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203511 — Domineering Glare
- Japanese: `睥睨`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==1&order_rate>=40@distance_type==4&phase_firsthalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203512 — High Ambitions
- Japanese: `覇気十分`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==1&order_rate>=40@distance_type==4&phase_firsthalf_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":35,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203522 — Glimpse of Light
- Japanese: `垣間見た光`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==4&distance_type==3&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203532 — Gateway to Success
- Japanese: `登竜門`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&up_slope_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203541 — Carefree Stride
- Japanese: `天真爛漫`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203542 — Footloose
- Japanese: `足任せ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203552 — Step Up
- Japanese: `ステップアップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203562 — Fierce Struggle
- Japanese: `奮闘`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203571 — Breach
- Japanese: `突破口`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203572 — Foothold
- Japanese: `足がかり`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203582 — Capture
- Japanese: `捕捉`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&phase_random==1&distance_diff_top>=20","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"running_style==4&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203591 — Independence
- Japanese: `独立独歩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203592 — Pushing Through!
- Japanese: `押し通る！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203601 — Magnificent Sand Stride
- Japanese: `見事な砂蹴り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&accumulatetime>=5&behind_near_lane_time>=3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203602 — Sand Stride
- Japanese: `砂蹴り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&accumulatetime>=5&behind_near_lane_time>=3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203611 — Sum of Small Efforts
- Japanese: `点滴穿石`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203612 — Diligence
- Japanese: `精進`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203621 — Straight Heart
- Japanese: `ストレートハート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==3&phase_straight_random==1&order_rate>=40","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203622 — Straight Steps
- Japanese: `真っ直ぐな走り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==3&phase_straight_random==1&order_rate>=40","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203631 — One and Only
- Japanese: `唯一無二`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&distance_rate_after_random==50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203632 — Dream-Fulfilling Challenge
- Japanese: `夢への挑戦`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&distance_rate_after_random==50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203642 — Luminance
- Japanese: `光明`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate<=50@distance_type==4&phase_firsthalf_random==2&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203651 — Pathfinder
- Japanese: `パスファインダー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1@distance_type==4&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203652 — Find a Way!
- Japanese: `活路を拓く！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1@distance_type==4&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203661 — Long Haul
- Japanese: `悠久走破`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1@distance_type==4&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203662 — Trekker
- Japanese: `健脚`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1@distance_type==4&phase_random==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203671 — Heat Haze
- Japanese: `陽炎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203672 — Simmering Heat
- Japanese: `静かな熱`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203681 — Latent Fighting Spirit
- Japanese: `秘めた闘魂`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==3&distance_type==3&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203682 — Ceaseless Training
- Japanese: `不断の鍛錬`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==3&distance_type==3&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203691 — Hyper Excitement
- Japanese: `ハイパーハイテンション☆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"always==1","effects":[{"modifier":400000,"target":1,"type":29},{"modifier":-200000,"target":1,"type":32}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 203701 — Gordian Cut
- Japanese: `快刀乱麻`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==2&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203702 — Take the Plunge
- Japanese: `思い切り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&running_style==2&phase_firsthalf_random==2&lastspurt==2","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203711 — Showdown
- Japanese: `ショーダウン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==2&is_lastspurt==1&corner==0","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203712 — One Brave Step
- Japanese: `勇気の一歩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==2&is_lastspurt==1&corner==0","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203721 — The Future in My Hands
- Japanese: `この手に掴んだ未来`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&distance_rate_after_random==50@distance_type==3&distance_rate_after_random==50","effects":[{"modifier":3500,"target":1,"type":22},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203731 — Energetic
- Japanese: `エネルギッシュ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_firsthalf_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203732 — Enthusiastic
- Japanese: `張り切り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase_firsthalf_random==1","effects":[{"modifier":500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203741 — Moment of Opportunity
- Japanese: `刹那の勝機`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&running_style==3&distance_rate>=50&corner!=0&change_order_onetime<0","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203742 — Exploit the Gap
- Japanese: `間隙を突いて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&running_style==3&distance_rate>=50&corner!=0&change_order_onetime<0","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203751 — Afterimage
- Japanese: `残影`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==4&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203752 — Chasing the Shadow
- Japanese: `影を追って`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==4&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203761 — Swift Decision
- Japanese: `即断即決`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203762 — Give Chase
- Japanese: `追駆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203772 — Unwavering Heart
- Japanese: `臆せぬ心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1&distance_type==4","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203781 — Impulse
- Japanese: `衝動`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==3&ground_type==1","effects":[{"modifier":200000,"target":1,"type":32}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 203791 — Killer Instict
- Japanese: `闘争本能`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&corner_random==3&order_rate>=40@distance_type==3&corner_random==3&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203792 — Belligerent
- Japanese: `好戦的`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&corner_random==3&order_rate>=40@distance_type==3&corner_random==3&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203801 — Unshackled Passion
- Japanese: `解き放つ情念`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1@distance_type==3&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase_random==2","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203802 — Unquenched Longing
- Japanese: `想い焦がれて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_random==1@distance_type==3&phase_random==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase_random==2","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203812 — Mental Strength
- Japanese: `精神力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==3&distance_type==3&base_speed>=1200&base_power>=1200","effects":[{"modifier":400000,"target":1,"type":1}],"precondition":""},{"baseDuration":-1,"condition":"running_style==3&distance_type==3&base_speed>=1200&base_power<1200","effects":[{"modifier":200000,"target":1,"type":1}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 203822 — Beast Within
- Japanese: `内なる獣`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&distance_type==3&phase>=2&is_last_straight==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":"distance_rate>=66&order_rate_out40_continue==1"},{"baseDuration":24000,"condition":"running_style==3&distance_type==3&phase>=2&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203831 — Natural Talent
- Japanese: `天賦の才`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==3&distance_type==3&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203832 — Aim for the Summit
- Japanese: `頂を目指して`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==3&distance_type==3&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203841 — Brains and Beauty
- Japanese: `才色兼備`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1&order_rate>=40","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203842 — Model Student
- Japanese: `優等生`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1&order_rate>=40","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203851 — Curiosity
- Japanese: `好奇心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203852 — Intrigued
- Japanese: `心惹かれて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203861 — Freewheeling
- Japanese: `自由奔放`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase<=1&change_order_onetime>0&accumulatetime>=5@distance_type==3&phase<=1&blocked_side_continuetime>=2&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203862 — Carefree Step
- Japanese: `気ままな足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&phase<=1&change_order_onetime>0&accumulatetime>=5@distance_type==3&phase<=1&blocked_side_continuetime>=2&accumulatetime>=5","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203871 — Thunderflash
- Japanese: `閃く雷光`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&is_overtake==1&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203872 — Bouncy Step
- Japanese: `弾ける足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&is_overtake==1&accumulatetime>=5","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203881 — Foregone Conclusion
- Japanese: `問答無用`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203882 — In No Time
- Japanese: `待ったなし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203892 — Heat Up
- Japanese: `ヒートアップ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==4&distance_type==1&phase_firsthalf_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203902 — Nosedive
- Japanese: `急降下`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&down_slope_random==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203911 — Radiant Treasure
- Japanese: `至宝の輝き`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==3&distance_type==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203912 — With Pride
- Japanese: `誇りを抱いて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==3&distance_type==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203922 — Prelude
- Japanese: `プレリュード`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_random==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203931 — Battle-Hardened
- Japanese: `百戦錬磨`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&phase_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203932 — Step Toward Mastery
- Japanese: `練達の一歩`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==1&phase_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203941 — Don't Blink!
- Japanese: `まばたき厳禁！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_random==1@distance_type==2&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203942 — Electrifying Run
- Japanese: `シビれる走り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&phase_random==1@distance_type==2&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203951 — Wonderkid
- Japanese: `麒麟児`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_wiz>=1200&distance_type==3@base_wiz>=1200&distance_type==4","effects":[{"modifier":600000,"target":1,"type":5},{"modifier":600000,"target":1,"type":1}],"precondition":""}],"rarity":2,"wisdomCheck":0}
```
---
## 203952 — Natural Genius
- Japanese: `天才肌`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_wiz>=1200&distance_type==3@base_wiz>=1200&distance_type==4","effects":[{"modifier":400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 203961 — Steadfast Spirit
- Japanese: `不抜の気概`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==2&distance_type==2&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203962 — Resolute Stance
- Japanese: `気丈な姿勢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==1&running_style==2&distance_type==2&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203972 — No Concern for Appearances
- Japanese: `なりふり構わず`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==2&order_rate<=50&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203981 — Heroic Energy
- Japanese: `勇壮活発`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&corner_random==3&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203982 — Vitality
- Japanese: `バイタリティ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&corner_random==3&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 203991 — Blooming
- Japanese: `開花`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==2&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 203992 — Time to Awaken
- Japanese: `目覚めの時`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"running_style==2&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204001 — Surging Spirit
- Japanese: `迸る気迫`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase<=1&change_order_onetime>0&accumulatetime>=5@running_style==2&phase<=1&blocked_side_continuetime>=2&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204002 — Stubborn
- Japanese: `意地っ張り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase<=1&change_order_onetime>0&accumulatetime>=5@running_style==2&phase<=1&blocked_side_continuetime>=2&accumulatetime>=5","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204012 — Brute Force
- Japanese: `力業`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase_random==1&distance_diff_top>=10","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"running_style==2&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204021 — Once-in-a-Lifetime
- Japanese: `一世一代`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==3&distance_type==4&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204022 — Crucial Stage
- Japanese: `ここ一番`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==3&distance_type==4&phase_firstquarter_random==2&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204031 — A Thousand Trials, Ten Thousand Refinements
- Japanese: `千鍛万錬`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_corner_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204032 — Spare No Effort
- Japanese: `労を惜しまず`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_corner_random==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204041 — Crowning Beauty
- Japanese: `錦上添花`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&change_order_onetime<0&accumulatetime>=5","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204042 — Gorgeous Step
- Japanese: `華麗な足取り`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&change_order_onetime<0&accumulatetime>=5","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204051 — Soul Ablaze
- Japanese: `燃ゆる魂`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_firsthalf_random==2@distance_type==3&phase_firsthalf_random==2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204052 — With a Light in My Heart
- Japanese: `灯を胸に`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_firsthalf_random==2@distance_type==3&phase_firsthalf_random==2","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204061 — Mettlesome
- Japanese: `勇気凛々`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&distance_type==3&corner_random==3&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204062 — With Dignity
- Japanese: `凛然と`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==4&distance_type==3&corner_random==3&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204071 — Smooth Sailing
- Japanese: `順風満帆`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204072 — With Feelings Aboard
- Japanese: `気持ちを乗せて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204081 — Great Wheel
- Japanese: `大車輪`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&up_slope_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204082 — Ride the Momentum
- Japanese: `余勢を駆って`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&up_slope_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204092 — Running is Winning!
- Japanese: `逃げるが勝ち！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204101 — Earthshaker
- Japanese: `震天動地`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&is_lastspurt==1&change_order_onetime<0@ground_type==2&is_lastspurt==1&blocked_side_continuetime>=2","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204102 — Thunderous Footfall
- Japanese: `轟く足音`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&is_lastspurt==1&change_order_onetime<0@ground_type==2&is_lastspurt==1&blocked_side_continuetime>=2","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204111 — Floating with the Tide
- Japanese: `行雲流水`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_random==1@running_style==3&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204112 — No Stagnation
- Japanese: `淀みなし`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_random==1@running_style==3&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204121 — To the Far Beyond
- Japanese: `遥か先へ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&is_last_straight==1&lastspurt==2","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_lastspurt==1&is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204122 — Putting All on the Line
- Japanese: `勝負を懸けて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&is_last_straight==1&lastspurt==2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_lastspurt==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204131 — Where There Is Will, There Is Achievement
- Japanese: `有志竟成`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204132 — Embrace Great Ambition
- Japanese: `大志を抱いて`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204141 — Stout-Hearted
- Japanese: `気丈夫`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_stamina>=1200","effects":[{"modifier":600000,"target":1,"type":2},{"modifier":600000,"target":1,"type":1}],"precondition":"distance_type==3@distance_type==4"}],"rarity":2,"wisdomCheck":0}
```
---
## 204142 — Overflowing Vitality
- Japanese: `あふれる活力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_stamina>=1200","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":"distance_type==3@distance_type==4"}],"rarity":1,"wisdomCheck":0}
```
---
## 204151 — Breakaway!
- Japanese: `ぶっちぎり！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_corner_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204152 — The Only Way is Forward
- Japanese: `前進あるのみ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_corner_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204161 — Headlong Charge
- Japanese: `猪突猛進`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"phase>=2&remain_distance<=600&order==1@phase>=2&remain_distance<=600&is_overtake==1&order_rate<=50","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"running_style==1@running_style==2"}],"rarity":2,"wisdomCheck":1}
```
---
## 204162 — Committed Push
- Japanese: `押しの一手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"phase>=2&remain_distance<=600&order==1@phase>=2&remain_distance<=600&is_overtake==1&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":"running_style==1@running_style==2"}],"rarity":1,"wisdomCheck":1}
```
---
## 204172 — Lively
- Japanese: `溌剌`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204181 — Unprecedented
- Japanese: `前人未到`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase==1&change_order_onetime<0@phase==1&order==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204182 — Giant Stride
- Japanese: `巨歩`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase==1&change_order_onetime<0@phase==1&order==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204191 — Innovation
- Japanese: `イノベーション`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==2&phase_random==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204192 — Approach
- Japanese: `アプローチ`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==2&phase_random==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204202 — Strategist
- Japanese: `戦略家`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"base_speed>=1000&base_power>=1000&distance_type==3@base_speed>=1000&base_power>=1000&distance_type==4","effects":[{"modifier":200000,"target":1,"type":1},{"modifier":200000,"target":1,"type":3}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 204211 — Paradigm Shift
- Japanese: `パラダイムシフト`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204212 — Exceptional Running
- Japanese: `卓越する走り`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204222 — One More Push
- Japanese: `もう一踏ん張り`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"run_at_full_speed_random==1&distance_type==3","effects":[{"modifier":2000,"target":1,"type":48}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 204232 — Santa Anita Racetrack ◎
- Japanese: `サンタアニタパークレース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10202","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 204233 — Santa Anita Racetrack ○
- Japanese: `サンタアニタパークレース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10202","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 204234 — Santa Anita Racetrack ×
- Japanese: `サンタアニタパークレース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10202","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 204242 — Del Mar Racetrack ◎
- Japanese: `デルマーレース場◎`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10203","effects":[{"modifier":600000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 204243 — Del Mar Racetrack ○
- Japanese: `デルマーレース場○`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10203","effects":[{"modifier":400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 204244 — Del Mar Racetrack ×
- Japanese: `デルマーレース場×`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"track_id==10203","effects":[{"modifier":-400000,"target":1,"type":2}],"precondition":""}],"rarity":1,"wisdomCheck":0}
```
---
## 204301 — Hundred Flowers in Full Bloom
- Japanese: `百花繚乱`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==2&phase_straight_random==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 204302 — Individualistic
- Japanese: `個性的`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&running_style==2&phase_straight_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210011 — Aoharu Burning・Speed
- Japanese: `アオハル燃焼・速`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_random==1","effects":[{"modifier":4200,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210012 — Aoharu Ignition・Speed
- Japanese: `アオハル点火・速`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_random==1","effects":[{"modifier":1800,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210021 — Aoharu Burning・Stamina
- Japanese: `アオハル燃焼・体`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase_random==1","effects":[{"modifier":660,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210022 — Aoharu Ignition・Stamina
- Japanese: `アオハル点火・体`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase_random==1","effects":[{"modifier":180,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210031 — Aoharu Burning・Power
- Japanese: `アオハル燃焼・力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"phase_random==2","effects":[{"modifier":4800,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210032 — Aoharu Ignition・Power
- Japanese: `アオハル点火・力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"phase_random==2","effects":[{"modifier":2400,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210041 — Aoharu Burning・Guts
- Japanese: `アオハル燃焼・根`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_random==2","effects":[{"modifier":3000,"target":1,"type":27},{"modifier":3600,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210042 — Aoharu Ignition・Guts
- Japanese: `アオハル点火・根`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_random==2","effects":[{"modifier":600,"target":1,"type":27},{"modifier":1200,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210051 — Aoharu Burning・Wisdom
- Japanese: `アオハル燃焼・賢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_random==0","effects":[{"modifier":420,"target":1,"type":28},{"modifier":180000,"target":1,"type":8}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210052 — Aoharu Ignition・Wisdom
- Japanese: `アオハル点火・賢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_random==0","effects":[{"modifier":180,"target":1,"type":28},{"modifier":60000,"target":1,"type":8}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210061 — The First Star
- Japanese: `一番星`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_rate_after_random==50","effects":[{"modifier":3000,"target":1,"type":27},{"modifier":3600,"target":1,"type":31},{"modifier":420,"target":1,"type":9}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210062 — Glittering Stars
- Japanese: `綺羅星`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_rate_after_random==50","effects":[{"modifier":600,"target":1,"type":27},{"modifier":1200,"target":1,"type":31},{"modifier":60,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210071 — I Want to Win With You
- Japanese: `キミと勝ちたい`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_rate_after_random==50&order_rate<=65","effects":[{"modifier":4200,"target":1,"type":27},{"modifier":2400,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210072 — Halfway to a Dream
- Japanese: `夢の途中`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_rate_after_random==50&order_rate<=65","effects":[{"modifier":1800,"target":1,"type":27},{"modifier":840,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210081 — Beyond the Limits
- Japanese: `限界の先へ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_random==3","effects":[{"modifier":4200,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210082 — Eyes on the Horizon
- Japanese: `前だけ見据えて`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_random==3","effects":[{"modifier":1800,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210091 — Essence of Racing・Speed
- Japanese: `レースの真髄・速`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"phase_laterhalf_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210101 — Essence of Racing・Stamina
- Japanese: `レースの真髄・体`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_random==3&hp_per>=2&is_lastspurt==1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210111 — Essence of Racing・Power
- Japanese: `レースの真髄・力`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase==3&is_overtake==1&is_lastspurt==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210121 — Essence of Racing・Guts
- Japanese: `レースの真髄・根`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"compete_fight_count>0","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210131 — Essence of Racing・Wisdom
- Japanese: `レースの真髄・賢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"activate_count_later_half>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210141 — Essence of Racing・Energy
- Japanese: `レースの真髄・心`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"motivation>=4","effects":[{"modifier":400000,"target":1,"type":2},{"modifier":400000,"target":1,"type":4},{"modifier":400000,"target":1,"type":5}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210261 — Wisdom of the Sun
- Japanese: `太陽の叡智`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase==1&blocked_side_continuetime>=2","effects":[{"modifier":4200,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210262 — Blessing of the Sun
- Japanese: `陽の加護`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase==1&blocked_side_continuetime>=2","effects":[{"modifier":1800,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210271 — Wisdom of the Ocean
- Japanese: `大海の叡智`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"phase_firsthalf_random==0","effects":[{"modifier":4800,"target":1,"type":31}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210272 — Blessing of the Ocean
- Japanese: `海の加護`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":15000,"condition":"phase_firsthalf_random==0","effects":[{"modifier":2400,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210281 — Wisdom of the Land
- Japanese: `大地の叡智`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_laterhalf_random==2","effects":[{"modifier":4200,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210282 — Blessing of the Land
- Japanese: `地の加護`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_laterhalf_random==2","effects":[{"modifier":1800,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210291 — Dreaming of the Peak
- Japanese: `最高峰の夢`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_last_straight==1","effects":[{"modifier":4200,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210292 — Bearer of Hope
- Japanese: `想いを背負って`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210301 — Blazing Radiance!
- Japanese: `爆熱のキラメキ！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_random==1@distance_type==3&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210302 — Burning Soul
- Japanese: `バーニングソウル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_random==1@distance_type==3&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210311 — Athlete's Spirit
- Japanese: `アスリート魂`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==2&distance_rate_after_random==50&base_guts>=1200@distance_type==3&distance_rate_after_random==50&base_guts>=1200","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":12000,"condition":"distance_type==2&distance_rate_after_random==50&base_guts<1200@distance_type==3&distance_rate_after_random==50&base_guts<1200","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210321 — The Races We Run
- Japanese: `私たちの走る道程`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&is_lastspurt==1&phase_random==3@distance_type==2&is_lastspurt==1&phase_random==3","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210322 — Forever Healthy
- Japanese: `いつまでも健やかに`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==1&is_lastspurt==1&phase_random==3@distance_type==2&is_lastspurt==1&phase_random==3","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210331 — Essence of Food
- Japanese: `食の極意`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==1&phase_random==1&base_power>=1200@distance_type==2&phase_random==1&base_power>=1200","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":12000,"condition":"distance_type==1&phase_random==1@distance_type==2&phase_random==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210341 — For a Fleeting View
- Japanese: `もう少しだけ、いい景色`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&is_last_straight==1@distance_type==4&is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210342 — Reproducing a Dream
- Japanese: `夢の再生方法`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&is_last_straight==1@distance_type==4&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210351 — Forger of Legends
- Japanese: `新たな伝説を築く者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210352 — Herald of a New Age
- Japanese: `時代を変える者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210361 — Guided by Instinct
- Japanese: `本能の懸け橋`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&is_last_straight==1@distance_type==4&is_last_straight==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210362 — Be Myself
- Japanese: `あるがままに`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&is_last_straight==1@distance_type==4&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210371 — Miracle of Recreation
- Japanese: `保養が導く奇跡`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210372 — Rest and Rise
- Japanese: `本気で休んで、もう一度`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 210381 — Glory Beyond Passion and Challenge
- Japanese: `情熱と挑戦の先の栄光`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":2,"wisdomCheck":1}
```
---
## 210382 — American Dream
- Japanese: `アメリカンドリーム`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 300131 — Supreme Commander of Japan
- Japanese: `日本総大将`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance>=350&remain_distance<=400","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 300141 — Dauntlessness
- Japanese: `不撓不屈`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance>=350&remain_distance<=400","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":5,"wisdomCheck":0}
```
---
## 407011 — Sparkling Contest
- Japanese: `キラメキの勝負`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase_laterhalf_random==0@distance_type==3&phase_laterhalf_random==0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 407021 — Now I'm Fired Up!!
- Japanese: `燃えてきたッ！！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&phase==1&change_order_onetime<0@distance_type==3&phase==1&change_order_onetime<0","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 407031 — Doing My Best!
- Japanese: `ベストを尽くして！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&is_lastspurt==1&phase_firsthalf_random==3@distance_type==3&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 407041 — Reckless Passion
- Japanese: `無二の情熱`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&phase_laterhalf_random==1&order_rate<=70","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 407051 — Unstoppable Muscles
- Japanese: `破竹の筋肉`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==2&is_finalcorner_random==1&order_rate>=25","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 407061 — Stay Tuned
- Japanese: `ステイチューン！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=70","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 407071 — Connecting Elation
- Japanese: `繋がる高揚感`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate>=25","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 408011 — Respect! Uma Mania!
- Japanese: `敬愛ッ！ウママニア`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&near_count>=3&accumulatetime>=5@distance_type==2&near_count>=3&accumulatetime>=5","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 408021 — Here You Go!
- Japanese: `お待ちどおさま！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":20000,"condition":"distance_type==1&phase>=2&order_rate>=50&is_overtake==1@distance_type==2&phase>=2&order_rate>=50&is_overtake==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=200","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 408031 — Mid-Meal Seasoning!
- Japanese: `ここらで味変！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_type==1&phase_random==1@distance_type==2&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 408041 — Three-Star Cornering
- Japanese: `即席三ツ星コーナリング`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&all_corner_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 408051 — Cultivation Sprint!
- Japanese: `耕せ！開墾スプリント`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_random==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=200","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 408061 — Curve Grand Chef
- Japanese: `曲線のグランシェフ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&all_corner_random==1@distance_type==2&all_corner_random==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&remain_distance<=200","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 409011 — Monster Machine
- Japanese: `モンスターマシン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_type==4&running_style==2&phase==2","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":"distance_diff_top<=10&distance_rate>=60&phase==1"},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 409021 — Recovery Sequence
- Japanese: `リカバリーシーケンス`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase==1&corner==0@distance_type==4&phase==1&corner==0","effects":[{"modifier":550,"target":1,"type":9},{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 409031 — All Systems Green
- Japanese: `システムオールグリーン`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 409041 — Limiter Release
- Japanese: `リミッター解除`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&is_lastspurt==1&phase_firsthalf_random==3@distance_type==4&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 409051 — Lead-Preserving Algorithm
- Japanese: `先頭維持アルゴリズム`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"course_distance>=2000&running_style==1&phase<=1&change_order_onetime>0&accumulatetime>=5@course_distance>=2000&running_style==1&phase<=1&blocked_side_continuetime>=2&accumulatetime>=5","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 409061 — Archline Top Scholar
- Japanese: `弧線のトップスカラー`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&all_corner_random==1@distance_type==4&all_corner_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 410011 — Advent of the Legends
- Japanese: `伝説降臨`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_random==1","effects":[{"modifier":3500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 410021 — Ahead of the Gale
- Japanese: `疾風より先へ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"straight_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 410031 — Crossroads of Revolution
- Japanese: `革命の岐路`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 410041 — Pioneer of Dreams
- Japanese: `夢の先駆者`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 410051 — Guidance of Many Moons
- Japanese: `幾星霜が導く一手`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":9000,"condition":"running_style==2&phase>=2&is_finalcorner==1&corner!=0&remain_distance>=600&order_rate<=70@running_style==3&phase>=2&is_finalcorner==1&corner!=0&remain_distance>=600&order_rate<=70","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 410061 — Soar Above The Clouds
- Japanese: `雲上飛翔`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&phase_laterhalf_random==1&order_rate>=40","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 411011 — Trails of Pioneers
- Japanese: `開拓者の軌跡`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1@distance_type==4&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 411021 — Trials into the Unknown
- Japanese: `未知へのトライアル`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"distance_type==3&phase_random==1@distance_type==4&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 411031 — Unyielding Survivalist Spirit
- Japanese: `不屈のサバイバル魂`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"phase_corner_random==1&distance_type==3@phase_corner_random==1&distance_type==4","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 411041 — Earth-Shaking Dash
- Japanese: `大地を揺るがす疾走`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&is_lastspurt==1&phase_firsthalf_random==3@distance_type==4&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 411051 — Wild at Heart
- Japanese: `ワイルドアットハート`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate>=25","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 411061 — Nature's Rhythm
- Japanese: `大自然の鼓動`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1&order_rate<=70","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 412011 — Hot Spring Dash
- Japanese: `走り湯ダッシュ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"behind_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 412021 — First in the Bath!
- Japanese: `一番風呂いただきます！`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"running_style==1&always==1","effects":[{"modifier":4000,"target":1,"type":31}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase_random==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 412031 — Geyser Spirit
- Japanese: `噴泉スピリット`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&phase<=1&change_order_onetime>0&accumulatetime>=5@running_style==2&phase<=1&blocked_side_continuetime>=2&accumulatetime>=5","effects":[{"modifier":4500,"target":1,"type":22}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 412041 — Bathe in Moderation
- Japanese: `湯に入りて湯に入らざれ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 412051 — Secret Onsen Power
- Japanese: `秘湯より湧くチカラ`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"running_style==3&phase_random==1@running_style==4&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 413011 — Aim for Stardom!
- Japanese: `スターダムを目指して！`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"infront_near_lane_time>=3&accumulatetime>=10@order==1&behind_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 413021 — Journey to a New Dream
- Japanese: `新しい夢への旅路`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase==1&change_order_onetime<0@phase==1&order==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 413031 — Turn the Tables!
- Japanese: `Turn the tables!`
- English name source: skillnames.json
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":40000,"condition":"ground_type==2&phase_random==1","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 413041 — Brilliance That Captivates the World
- Japanese: `世界を魅せる輝き`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase_firsthalf_random==3","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 413051 — Blazing ☆ Roadmap
- Japanese: `激アツ☆ロードマップ`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==3&phase_random==1@distance_type==4&phase_random==1","effects":[{"modifier":4500,"target":1,"type":27}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 900011 — Shooting Star
- Japanese: `シューティングスター`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&order>=1&order_rate<=50&change_order_onetime<0","effects":[{"modifier":1500,"target":1,"type":22},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900021 — I'm Not Giving up the Lead!
- Japanese: `先頭の景色は譲らない…！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&order==1&bashin_diff_behind>=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900031 — Ultimate Teio Step
- Japanese: `究極テイオーステップ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"phase>=2&order<=3&bashin_diff_infront<=1&is_overtake==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 900041 — Red Flame Gear/LP1211-M
- Japanese: `紅焔ギア/LP1211-M`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_finalcorner==1&order<=5&order_rate<=50","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900051 — Glittering Star Vaudeville
- Japanese: `煌星のヴォードヴィル`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=300","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"phase>=2&order_rate<=40&behind_near_lane_time_set1>=1"}],"rarity":1,"wisdomCheck":1}
```
---
## 900061 — The Beat of Victory
- Japanese: `勝利の鼓動`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"order>=2&order<=5&order_rate<=50&remain_distance<=201&remain_distance>=199","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900071 — Unsinkable Ship, Anchored!
- Japanese: `不沈艦、抜錨ォッ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=50&distance_rate<=60&order_rate>50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900081 — Cutting × DRIVE!
- Japanese: `カッティング×DRIVE！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"order>=3&order_rate<=50&remain_distance<=200&bashin_diff_infront<=1@order>=3&order_rate<=50&remain_distance<=200&bashin_diff_behind<=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900091 — Brilliant Red Ace
- Japanese: `ブリリアント・レッドエース`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&order==1&bashin_diff_behind<=1@distance_rate>=50&order==2&is_overtake==1","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900101 — Victory Shot!
- Japanese: `ヴィクトリーショット！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner_laterhalf==1&corner!=0&order>=3&order_rate<=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900111 — Where There's a Will, There's a Way
- Japanese: `精神一到何事か成らざらん`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&change_order_onetime<0&order>=3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900121 — One-On-One! Dead Heat!
- Japanese: `タイマン！デッドヒート！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"is_finalcorner==1&is_behind_in==1&change_order_onetime<0&order_rate>=40"}],"rarity":1,"wisdomCheck":1}
```
---
## 900131 — Fulfilling Your Noble Duty
- Japanese: `貴顕の使命を果たすべく`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&corner!=0&distance_diff_rate<=30&distance_type==4&lastspurt==2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_finalcorner==1&corner!=0&distance_diff_rate<=30","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900141 — Plancha ☆ Ganador
- Japanese: `プランチャ☆ガナドール`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&hp_per>=30&order<=2","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900151 — Dance for Vittoria
- Japanese: `ヴィットーリアに捧ぐ舞踏`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&bashin_diff_behind<=1&order<=4@is_finalcorner==1&bashin_diff_infront<=1&order<=4","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900161 — Shadow Break
- Japanese: `Shadow Break`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&order>=2&order_rate<=75&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"phase==1&blocked_side_continuetime>=2"},{"baseDuration":30000,"condition":"is_finalcorner==1&order>=2&order_rate<=75&is_behind_in==1&change_order_onetime<0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900171 — Thou, Witness the Heavenly Might of the Emperor
- Japanese: `汝、皇帝の神威を見よ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&change_order_up_end_after>=3","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900181 — Blaze of Pride
- Japanese: `ブレイズ・オブ・プライド`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&corner!=0&order>=3&change_order_onetime<0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900191 — Kyuute☆Last SpuU(ﾟ∀ﾟ)Uurt!
- Japanese: `尊み☆ﾗｽﾄｽﾊﾟ—(ﾟ∀ﾟ)—ﾄ!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"change_order_up_end_after>=2","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":150,"target":1,"type":28}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900201 — Angling×Scheming
- Japanese: `アングリング×スキーミング`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase>=2&corner!=0&order==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900211 — Imma Show You White Lightning!
- Japanese: `白い稲妻、見せたるで！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&corner==0&order_rate>=70&order_rate<=75&is_overtake==1@distance_rate>=50&corner==0&order_rate<=30&order_rate>=20","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900221 — Fairy Tale
- Japanese: `Fairy tale`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&order>=2&order_rate<=40&blocked_side_continuetime>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900231 — ∴win Q.E.D.
- Japanese: `∴win Q.E.D.`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_finalcorner==1&order<=4&temptation_count==0","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"phase>=2&is_finalcorner==1&order<=4","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900241 — Inspiration ☆ Landing
- Japanese: `ひらめき☆ランディング`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&blocked_side_continuetime>=2&order<=3","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900251 — Chasing After You
- Japanese: `アナタヲ・オイカケテ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=50&order_rate>=40&order_rate<=70","effects":[{"modifier":500,"target":1,"type":27},{"modifier":-250,"target":9,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900261 — G00 1st.F∞;
- Japanese: `G00 1st.F∞;`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_badstart==0&order<=3&is_last_straight==1&order_rate_in20_continue==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_badstart==0&order<=3&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900271 — Let's Anabolic!
- Japanese: `レッツ・アナボリック！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase>=2&corner!=0&order_rate>=65&order_rate<=70","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900281 — I'M☆FULL☆SPEED!!
- Japanese: `I'M☆FULL☆SPEED!!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=45&distance_rate<=60&order>=2&order_rate<=50&is_overtake==1&distance_type==1","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=45&distance_rate<=60&order>=2&order_rate<=50&is_overtake==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900291 — Chasing the Snowlight
- Japanese: `ゆきあかり、おいかけて`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_diff_top<=5&remain_distance<=300&order_rate<=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900301 — Blue Rose Chaser
- Japanese: `ブルーローズチェイサー`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase>=2&order<=4&change_order_onetime<0"}],"rarity":1,"wisdomCheck":1}
```
---
## 900311 — Charge Complete! Full Speed Ahead!
- Japanese: `チャージ完了！全速前進！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=299&remain_distance>=295&order<=2&slope==0@remain_distance<=299&remain_distance>=295&order<=2&slope==2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"remain_distance<=305&remain_distance>=300&slope==1"},{"baseDuration":30000,"condition":"remain_distance<=299&remain_distance>=295&order<=2","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900321 — U=ma2
- Japanese: `U=ma2`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_rate>=50&corner!=0&order>=3&order_rate<=40","effects":[{"modifier":150,"target":1,"type":9},{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900331 — Meteor of Dioscuri
- Japanese: `ディオスクロイの流星`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&distance_diff_top>=5&order_rate<80","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_last_straight==1&distance_diff_top>=5&order_rate>=80","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900341 — Fast Running, Fast Running!
- Japanese: `快走かな、快走かな！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"compete_fight_count>0","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate_out40_continue==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 900351 — The Ticket to Victory, for You!
- Japanese: `勝利のチケットを、君にッ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&order<=5","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"is_finalcorner==1&blocked_side_continuetime>=2"}],"rarity":1,"wisdomCheck":1}
```
---
## 900361 — trigger:BEAT
- Japanese: `trigger:BEAT`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":150,"target":1,"type":28}],"precondition":"is_finalcorner==1&order_rate>=40&order_rate<=75&lane_type==0"}],"rarity":1,"wisdomCheck":1}
```
---
## 900371 — Schwarzes Schwert
- Japanese: `Schwarzes Schwert`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"temptation_count==0&order>=3&is_last_straight==1&order_rate_in80_continue==1&order_rate_out40_continue==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"temptation_count==0&order>=3&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900381 — #LookatCurren
- Japanese: `#LookatCurren`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=65&order>=2&order_rate<=50&change_order_onetime<0","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900391 — Victory Befitting a Princess
- Japanese: `姫たるもの、勝利をこの手に`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&blocked_side_continuetime>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900401 — KEEP IT REAL.
- Japanese: `KEEP IT REAL.`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=50&order_rate>=40&order_rate<=80&is_overtake==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900411 — Honor Student x Bakushin = Big Victory
- Japanese: `優等生×バクシン＝大勝利ッ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&order<=3&blocked_side_continuetime>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900421 — 『I'm Possible』
- Japanese: `『I'm possible』`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=201&remain_distance>=199&distance_diff_top<=5&order>=2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"remain_distance<=201&remain_distance>=199&distance_diff_top<=10&order>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900431 — Ding Dong Boo
- Japanese: `Ding Dong Boo`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"compete_fight_count>0&ground_type==2","effects":[{"modifier":500,"target":1,"type":27},{"modifier":2000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"compete_fight_count>0","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900441 — You're Mine ☆ Strelitzia
- Japanese: `いただき☆ストレリチア！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"remain_distance<=300","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"order_rate_out50_continue==1&temptation_count==0&is_finalcorner==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 900451 — Purity of Heart
- Japanese: `ピュリティオブハート`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase_random==1&order>=2&order_rate<=40","effects":[{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900461 — Sparkling☆STARDOM
- Japanese: `キラキラ☆STARDOM`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&corner==0&order<=2&bashin_diff_behind<=1","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900471 — Raise Thy Soul's Sword!
- Japanese: `掲げよ、己が魂の剣を！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&remain_distance<=401&remain_distance>=399&order_rate<=40&grade==100&popularity<=3","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"phase>=2&remain_distance<=401&remain_distance>=399&order_rate<=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900481 — YEAH☆VIVID TIME!
- Japanese: `YEAH☆VIVID TIME!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&order_rate<=40&overtake_target_time>=1@is_last_straight==1&order_rate<=40&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900491 — Laugh in the Face of Danger
- Japanese: `剣ヶ峰より、狂気に嗤え`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=400&order_rate>=30&order_rate<=50&popularity>=4","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"is_finalcorner==1&is_overtake==1"},{"baseDuration":30000,"condition":"remain_distance<=400&order_rate>=30&order_rate<=50&popularity<4","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"is_finalcorner==1&is_overtake==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 900501 — Nemesis
- Japanese: `Nemesis`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&order_rate>=40&order_rate<=75&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900511 — When the Flower Bud Opens
- Japanese: `つぼみ、ほころぶ時`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase>=2&is_finalcorner_laterhalf==1&order>=3&order_rate<=40@phase>=2&is_finalcorner==1&corner==0&order>=3&order_rate<=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":"phase==1&blocked_side_continuetime>=2&corner!=0"}],"rarity":1,"wisdomCheck":1}
```
---
## 900521 — Exciting Climax
- Japanese: `ワクワククライマックス`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"is_finalcorner==1&corner!=0&order_rate>50&near_count>=1","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900531 — Hot-Blooded Disciplinary Attack!
- Japanese: `熱血！！風紀アタック`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"phase>=2&order_rate>=50&is_finalcorner==1&bashin_diff_infront<=1","effects":[{"modifier":500,"target":1,"type":31},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900541 — Blasting Gale Pegasus Dash!
- Japanese: `疾風爆走ペガサスダッシュ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"remain_distance<=150&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"order_rate>=45&distance_rate>=50&change_order_onetime<0"}],"rarity":1,"wisdomCheck":1}
```
---
## 900551 — Colorful☆Marvelous★World
- Japanese: `万彩☆マーベラス★世界`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate<=50&distance_rate>=40&order_rate<=80&order_rate>=50&near_count>=1&visiblehorse>=4","effects":[{"modifier":2000,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate<=50&distance_rate>=40&order_rate<=80&order_rate>=50&near_count>=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900561 — Luck Is Coming
- Japanese: `来ます来てます来させます！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&order>=3&blocked_front==1","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900571 — Lyricism at Journey's End
- Japanese: `叙情、旅路の果てに`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate>50@distance_type==4&phase_laterhalf_random==1&order_rate>50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":36000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate>50@distance_type==2&phase_laterhalf_random==1&order_rate>50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900581 — I Never Goof Up!
- Japanese: `I Never Goof Up!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&change_order_onetime<0","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900591 — Beyond the Other Side
- Japanese: `彼方、その先へ…`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase>=2&corner!=0&is_finalcorner==0&temptation_count==0&order_rate>=50&order_rate<=70@phase==1&corner!=0&is_finalcorner==1&temptation_count==0&order_rate>=50&order_rate<=70","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900601 — Surely, Beyond...!
- Japanese: `きっとその先へ…！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&order==3&bashin_diff_behind<=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900611 — Pride of KING
- Japanese: `Pride of KING`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"temptation_count==0&remain_distance<=201&remain_distance>=199&order>=4&order_rate<=70","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900621 — Bang, Bam, Mun
- Japanese: `どんっ、パッ、むんっ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&phase==1&order>=3&order_rate<=70","effects":[{"modifier":150,"target":1,"type":9},{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900631 — Forged From a Hundred Trials
- Japanese: `百錬成鋼`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"is_lastspurt==1&phase==3&temptation_count==0","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900641 — The Breakaway Road
- Japanese: `ぶっちぎりロード`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=50&order_rate_in20_continue==1","effects":[{"modifier":150,"target":1,"type":9},{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900651 — Everybody Put Your Hands Up!
- Japanese: `アゲてアゲてぷちょへんざ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_type==1&phase_laterhalf_random==1&order_rate<=50@distance_type==2&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate<=50@distance_type==4&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900661 — Engine, Full Throttle! Turbo Time!
- Japanese: `エンジン全開！大噴射！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":104000,"condition":"distance_rate>=34&distance_rate<=36&order==1&bashin_diff_behind>=1","effects":[{"modifier":350,"target":1,"type":27}],"precondition":""},{"baseDuration":5000000,"condition":"phase==3&is_activate_other_skill_detail==1","effects":[{"modifier":-500,"target":1,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900671 — Brilliance Illuminating the Darkness
- Japanese: `晦冥を照らせ永遠の耀き`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight_onetime==1&order>=2&order<=5&distance_diff_top<=5","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_last_straight_onetime==1&order>=2&order<=5&distance_diff_top>5","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900681 — Shout of Victory
- Japanese: `勝ち鬨ワッショイ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==2&straight_front_type==2&order<=2","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=50&corner==3&order<=2","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900691 — Longing Beyond the Sakura
- Japanese: `憧れは桜を越える！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=300&order_rate<=40&bashin_diff_infront<=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900701 — Seirios
- Japanese: `セイリオス`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"remain_distance>=799&remain_distance<=801&order_rate>=30&order_rate<=60&course_distance==2400&popularity<=3","effects":[{"modifier":3000,"target":1,"type":31}],"precondition":""},{"baseDuration":24000,"condition":"remain_distance>=799&remain_distance<=801&order_rate>=30&order_rate<=60","effects":[{"modifier":700,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900711 — A Lifetime's Dream, A Moment's Flight
- Japanese: `一期の夢、刹那の飛翔`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_last_straight==1&bashin_diff_behind<=1","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-100,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900721 — Dazzling Fire, Invincible Dance
- Japanese: `烈火繚乱、無敵之舞`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=300&order_rate<=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"is_finalcorner==1&change_order_onetime<0"}],"rarity":1,"wisdomCheck":1}
```
---
## 900731 — Flames of Unyielding Resolve
- Japanese: `燃え盛るは絶対の意志`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&change_order_up_end_after>=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900741 — Lovely Spring Wind
- Japanese: `麗しき花信風`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&order_rate>=40&order_rate<=80","effects":[{"modifier":350,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900761 — Blossoming World
- Japanese: `花開き、世界`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_type==4&distance_rate>=50&distance_rate<=51&order_rate>=30&order_rate<=80","effects":[{"modifier":500,"target":1,"type":27},{"modifier":350,"target":1,"type":9}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=51&order_rate>=30&order_rate<=80","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900771 — Road to Glory
- Japanese: `Road to Glory`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=401&remain_distance>=399","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"distance_rate>=60&phase==1&order>=2&order_rate<=40"}],"rarity":1,"wisdomCheck":1}
```
---
## 900781 — A Spring in My Step
- Japanese: `風光る`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":48000,"condition":"is_finalcorner_laterhalf==1&distance_diff_rate<=50&order==2","effects":[{"modifier":700,"target":1,"type":31}],"precondition":"distance_rate>=50&order_rate_out20_continue==1"},{"baseDuration":48000,"condition":"is_finalcorner_laterhalf==1&distance_diff_rate<=50","effects":[{"modifier":500,"target":1,"type":31}],"precondition":"distance_rate>=50&order_rate_out20_continue==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 900791 — Funabashi Above All!
- Japanese: `『船橋最強！』`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=50&track_id==10101@distance_rate>=50&track_id==10103@distance_rate>=50&track_id==10104","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase==1&order_rate<=50&blocked_side_continuetime>=2"},{"baseDuration":24000,"condition":"distance_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase==1&order_rate<=50&blocked_side_continuetime>=2"}],"rarity":1,"wisdomCheck":1}
```
---
## 900801 — Info: Acquired
- Japanese: `Info: Acquired`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_other_character_activate_advantage_skill==31","effects":[{"modifier":500,"target":1,"type":22}],"precondition":"distance_rate>=50&order_rate_in20_continue==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 900811 — Punkish Bite
- Japanese: `Punkish Bite`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==1&phase>=2&corner!=0@running_style==2&phase>=2&corner!=0","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900821 — Shining Runway
- Japanese: `Shining Runway`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&is_finalcorner==1&corner!=0&order_rate<=50&order_rate>=20","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_finalcorner==1&corner!=0&order_rate<=50&order_rate>=20","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900831 — Mission: Triumph
- Japanese: `Mission: Triumph`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=40&corner==0&slope==2&order_rate>=40&order_rate<=80","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=40&corner==0&order_rate>=40&order_rate<=80","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900841 — Thunderstorm Sublation
- Japanese: `霹靂のアウフヘーベン`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":"phase>=2&order_rate>=50"}],"rarity":1,"wisdomCheck":1}
```
---
## 900851 — Reign Supreme
- Japanese: `至上であれ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=66&distance_rate<=68&order_rate>=60&order_rate<=90&temptation_count==0","effects":[{"modifier":500,"target":1,"type":22},{"modifier":-250,"target":7,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900861 — Melt in Love's Embrace
- Japanese: `愛と熔けよただ熔けよ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance>=999&remain_distance<=1001&order_rate>=20&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900871 — Silent Letter
- Japanese: `Silent letter`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=400&order<=2&overtake_target_time>=1","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900881 — Reversal Illusion
- Japanese: `Reversal Illusion`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&remain_distance<=400","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"change_order_up_middle>=1&is_finalcorner==1&corner!=0&order_rate<=70&order_rate>=40"},{"baseDuration":30000,"condition":"remain_distance<=400","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"is_finalcorner==1&corner!=0&order_rate<=70&order_rate>=40"}],"rarity":1,"wisdomCheck":1}
```
---
## 900891 — Celeste Oath
- Japanese: `Celeste Oath`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=50&course_distance>=2400","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":35,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900901 — Queen's Rebirth
- Japanese: `Queen's Rebirth`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_rate<=50&corner!=0&order_rate<=50&ground_type==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_last_straight==1&overtake_target_time>=1&distance_type==2@is_activate_other_skill_detail==1&phase>=2&is_last_straight==1&overtake_target_time>=1&distance_type==3","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900911 — Deluxe☆Fountain
- Japanese: `デラックス☆ファウンテン`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=300","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"phase>=2&is_last_straight_onetime==1&order_rate>=30&order_rate<=70&temptation_count==0"},{"baseDuration":30000,"condition":"remain_distance<=300","effects":[{"modifier":500,"target":1,"type":27}],"precondition":"phase>=2&is_last_straight_onetime==1&order_rate>=30&order_rate<=70"}],"rarity":1,"wisdomCheck":1}
```
---
## 900921 — My Flame Lights the Way
- Japanese: `照らすのはわたしの焔`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=55&order_rate<=50&order_rate>=20","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900931 — Blue Ray of Happiness
- Japanese: `幸せの青い光`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&phase_firsthalf_random==2&order_rate<=50&order_rate>=20@distance_type==2&phase_firsthalf_random==2&order_rate<=50&order_rate>=20","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==3&phase_firsthalf_random==2&order_rate<=50&order_rate>=20@distance_type==4&phase_firsthalf_random==2&order_rate<=50&order_rate>=20","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900941 — Faith in the Feral
- Japanese: `Faith in the Feral`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=51&order_rate<=80&order_rate>=40&distance_type==3","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=51&order_rate<=80&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900951 — Because I Believe
- Japanese: `念い、信ずればこそ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":-1,"condition":"running_style==2&distance_rate>=66&distance_rate<=68&order_rate<=50&distance_type==1","effects":[{"modifier":350,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"running_style==2&distance_rate>=66&distance_rate<=68&order_rate<=50","effects":[{"modifier":350,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900961 — Deceive Thy Foe and Be Certain of Victory
- Japanese: `知宵欺敵、百戦不殆`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"corner==3&order_rate>=40&order_rate<=70&distance_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_last_straight==1&is_overtake==1","effects":[{"modifier":350,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900971 — Scarlet Lily's Elation
- Japanese: `スカーレットリリィの高揚`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"order_rate>=20&order_rate<=70&remain_distance>=299&remain_distance<=301","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900981 — Luck Comes to the Prepared
- Japanese: `理運開かりて翔る`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_laterhalf_random==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 900991 — Shine ☆ Tomakomai
- Japanese: `かがやけ☆とまこまい`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&order_rate<=40&order_rate>=30&ground_type==2","effects":[{"modifier":700,"target":1,"type":31}],"precondition":"phase==1&blocked_side_continuetime>=2&corner!=0"}],"rarity":1,"wisdomCheck":1}
```
---
## 901001 — Never Say Never
- Japanese: `Never Say Never`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance>=299&remain_distance<=301&order_rate>=20&order_rate<=40&distance_diff_top<=5&ground_type==2","effects":[{"modifier":500,"target":1,"type":27},{"modifier":500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"remain_distance>=299&remain_distance<=301&order_rate>=20&order_rate<=40","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901021 — Vivace Volare
- Japanese: `ヴィヴァーチェ・ヴォラーレ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"distance_rate<=50&order_rate>=40&order_rate<=80&infront_near_lane_time>=3&accumulatetime>=10@distance_rate<=50&order_rate>=40&order_rate<=80&behind_near_lane_time>=3&accumulatetime>=10","effects":[{"modifier":35,"target":1,"type":9}],"precondition":""},{"baseDuration":24000,"condition":"distance_rate<=60&distance_rate>=45&corner==0&is_activate_other_skill_detail==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901031 — Absolutely Strong ☆ Appeal Declaration!
- Japanese: `絶対最強☆アピール宣言！`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase==1&order_rate<=50&blocked_side_continuetime>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&compete_fight_count>0","effects":[{"modifier":350,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901041 — Flag of Dawn: Katsuragi Ace
- Japanese: `暁の御旗『葛城栄主』！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"corner==3&order==1&track_id==10006&distance_type==3","effects":[{"modifier":500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""},{"baseDuration":30000,"condition":"corner==3&order==1","effects":[{"modifier":500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901051 — Ad Astra
- Japanese: `アド・アストラ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=55&order_rate>=40&order_rate<=80&distance_type==3&activate_count_all>=7","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=55&order_rate>=40&order_rate<=80","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901061 — Bang☆Miracle Maker!
- Japanese: `Bang☆ミラクるわせ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_type==4&order_rate>=40&order_rate<=70&is_finalcorner_laterhalf==1&popularity>=4","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":36000,"condition":"order_rate>=40&order_rate<=70&is_finalcorner_laterhalf==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901071 — Billions of Stars
- Japanese: `Billions of stars`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_last_straight==1&order==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901081 — Scarlet Ascension of the Rakshasa
- Japanese: `羅刹、赤翼にて天上へ至らん`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=51&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":18000,"condition":"phase>=2&is_activate_other_skill_detail==1&is_finalcorner==1&corner!=0&is_overtake==1","effects":[{"modifier":350,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901091 — Connecting Dreams With the Future
- Japanese: `繋ぐ・繋がる×夢・未来`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_type==1&distance_rate<=50&corner!=0&order>=3&order_rate<=70@distance_type==2&distance_rate<=50&corner!=0&order>=3&order_rate<=70","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate<=50&corner!=0&order>=3&order_rate<=70","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901101 — Guiding Sea
- Japanese: `Guiding Sea`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"remain_distance>=799&remain_distance<=801&is_basis_distance==1&order_rate>=70&order_rate<=80","effects":[{"modifier":500,"target":1,"type":22},{"modifier":500,"target":1,"type":31},{"modifier":700,"target":1,"type":31}],"precondition":""},{"baseDuration":24000,"condition":"remain_distance>=799&remain_distance<=801&order_rate>=50&order_rate<=80","effects":[{"modifier":500,"target":1,"type":22},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901111 — Traced Bloodline, Budding Future
- Japanese: `辿る血脈、芽吹く未来`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=49&distance_rate<=50&order_rate>=40&order_rate<=90&slope==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":36000,"condition":"distance_rate>=49&distance_rate<=50&order_rate>=40&order_rate<=90","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901131 — Hop Step Gotcha ♡
- Japanese: `ホップステップ・ゲッチュ♡`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"order_rate>=20&order_rate<=50&distance_rate<=50&corner!=0&course_distance==2200","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"order_rate>=20&order_rate<=50&distance_rate<=50&corner!=0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901141 — To Our Vista
- Japanese: `To Our Vista`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=51&order_rate>=40","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901151 — None Shall Object My Rule
- Japanese: `我が覇道、阻むものなし`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"running_style==4&remain_distance>=999&remain_distance<=1001","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901161 — Rose Conquest
- Japanese: `烈華の洗礼`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate<=50&corner!=0&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":18000,"condition":"is_activate_other_skill_detail==1&order_rate<=40&phase>=2&is_last_straight==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901171 — Allegro of Valor
- Japanese: `鋭気のアレグロ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_last_straight_onetime==1&change_order_up_end_after>=3@is_last_straight_onetime==1&change_order_up_end_after>=2&change_order_up_middle>=1@is_last_straight_onetime==1&change_order_up_end_after>=1&change_order_up_middle>=2@is_last_straight_onetime==1&change_order_up_middle>=3","effects":[{"modifier":3500,"target":1,"type":27}],"precondition":"running_style==4&phase>=2"},{"baseDuration":24000,"condition":"is_last_straight_onetime==1&change_order_up_end_after>=1@is_last_straight_onetime==1&change_order_up_middle>=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase>=2"}],"rarity":1,"wisdomCheck":1}
```
---
## 901191 — «Bon Voyage»
- Japanese: `『それでは、よき旅を』`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_rate>=66&distance_rate<=68&order_rate>=50&remain_distance>=500","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""},{"baseDuration":18000,"condition":"is_activate_other_skill_detail==1&corner==0&track_id==10005&distance_type==3@is_activate_other_skill_detail==1&corner==0&track_id==10005&distance_type==4@is_activate_other_skill_detail==1&corner==0&track_id==10009&distance_type==3@is_activate_other_skill_detail==1&corner==0&track_id==10009&distance_type==4","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901201 — Path of Singular Focus
- Japanese: `無二無三なる一条の路`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"furlong==3&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901211 — Lame de Vent
- Japanese: `Lame de vent`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_lastspurt==1&phase==3&order_rate>=40&order_rate<=80&distance_type==1@is_lastspurt==1&phase==3&order_rate>=40&order_rate<=80&distance_type==2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"is_finalcorner==1&corner!=0&change_order_onetime<0"},{"baseDuration":30000,"condition":"is_lastspurt==1&phase==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"is_finalcorner==1&corner!=0&change_order_onetime<0"}],"rarity":1,"wisdomCheck":1}
```
---
## 901241 — Growing Dreams, Pioneer's Path
- Japanese: `ふくらむ夢、先駆の途`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901271 — Target Acquired! Serving Justice!
- Japanese: `対象捕捉！正義遂行！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&corner==0&order_rate<=70&order_rate>=30&distance_type==4","effects":[{"modifier":2000,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=50&corner==0&order_rate<=70&order_rate>=30","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901291 — Peerless Heroine
- Japanese: `Peerless Heroine`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase==1&corner!=0&order_rate<=50&ground_type==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901311 — ¡Qué alegría!
- Japanese: `¡Qué alegría!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_rate>=50&distance_rate<=51&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""},{"baseDuration":18000,"condition":"distance_type==1&is_activate_other_skill_detail==1&phase==3&is_lastspurt==1@distance_type==2&is_activate_other_skill_detail==1&phase==3&is_lastspurt==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901321 — Circulating Love♡
- Japanese: `Circulating Love♡`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==3&ground_type==1&phase_laterhalf_random==1","effects":[{"modifier":350,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901331 — Weaving History
- Japanese: `Weaving History`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==1&running_style==2&distance_rate>=40&distance_rate<=41","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901351 — In Search of Gold
- Japanese: `黄金を訪ねて`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":"running_style==3@running_style==4"},{"baseDuration":12000,"condition":"is_activate_other_skill_detail==1&course_distance>=2000&is_lastspurt==1","effects":[{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 901371 — Imagination × Creation = ∞
- Japanese: `想像×創造＝∞`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":48000,"condition":"order_rate<=70&phase_firsthalf==1","effects":[{"modifier":500,"target":1,"type":22}],"precondition":"distance_type==3@distance_type==4"}],"rarity":1,"wisdomCheck":1}
```
---
## 910011 — Wayakawa ♪ Marine Dive
- Japanese: `わやかわ♪マリンダイヴ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&order>=2&order_rate<=80&activate_count_middle>=2","effects":[{"modifier":150,"target":1,"type":9},{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910021 — Beyond the Ocean's Infinity
- Japanese: `水平線のその先へ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=66&distance_rate<=68&corner==3&order==1","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":"phase==1&bashin_diff_behind>=3&order==1"},{"baseDuration":30000,"condition":"distance_rate>=66&distance_rate<=68&order==1","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910031 — It's Going to Be Me
- Japanese: `絶対は、ボクだ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"is_finalcorner==1&is_overtake==1&order<=5&order_rate<=50&overtake_target_no_order_up_time>=2"}],"rarity":1,"wisdomCheck":1}
```
---
## 910041 — Heartfelt ♪ Smooch
- Japanese: `グッときて♪Chu`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&activate_count_heal>=1&order<=3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910051 — Ravissante
- Japanese: `Ravissant`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_finalcorner==1&change_order_onetime<0&order_rate<=40","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910061 — Christmas Eve Miracle Run!
- Japanese: `聖夜のミラクルラン！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"activate_count_heal>=3&distance_rate>=50","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31},{"modifier":50,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910071 — Adventure of 564
- Japanese: `Adventure of 564`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate_after_random==50","effects":[{"modifier":350,"target":1,"type":27},{"modifier":10000,"target":1,"type":37}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910081 — Into High Gear!
- Japanese: `Into High Gear!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"slope==0@slope==1","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":"phase>=1&slope==2&order_rate>=50&order_rate<=80&track_id==10006"},{"baseDuration":24000,"condition":"slope==0@slope==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase>=1&slope==2&order_rate>=50&order_rate<=80"}],"rarity":1,"wisdomCheck":1}
```
---
## 910091 — Queen's Lumination
- Japanese: `Queen's Lumination`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=50&corner==0&order==1&bashin_diff_behind<=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":36000,"condition":"distance_rate>=50&corner==0&order<=2","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910101 — Joyful Voyage!
- Japanese: `Joyful Voyage!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_diff_top<=5&order>=2&order_rate<=40&remain_distance<=201&remain_distance>=199","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":350,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"order>=2&order_rate<=40&remain_distance<=201&remain_distance>=199","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910111 — Gain Superior Heal
- Japanese: `ゲインヒール・スペリアー`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":0,"condition":"phase==1&change_order_onetime>0&order_rate>=40","effects":[{"modifier":350,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910121 — Extra Large First Bite!
- Japanese: `大盛り！ファーストバイト！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_rate>=60&phase==1&slope==2&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":"change_order_up_middle>=3"}],"rarity":1,"wisdomCheck":1}
```
---
## 910131 — For the Strongest Name
- Japanese: `最強の名を懸けて`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"phase>=2&is_finalcorner==1&order<=4&overtake_target_time>=1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910141 — Condor Onslaught
- Japanese: `コンドル猛撃波`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_finalcorner==1&corner!=0&is_overtake==1&order>=4&order_rate<=75","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910151 — Blessed Barcarolle
- Japanese: `恵福バルカローレ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=401&remain_distance>=399&order_rate<=40&activate_count_all>=7","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"remain_distance<=401&remain_distance>=399&order_rate<=40&activate_count_all<=6","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910161 — Critical Point: Gray
- Japanese: `灰色の臨界点`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_finalcorner_laterhalf==1&order_rate<=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910171 — Howling Arrow Piercing the Darkness
- Japanese: `翳り退く、さざめきの矢`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"is_finalcorner==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase>=2&order_rate<=50&overtake_target_time>=2"}],"rarity":1,"wisdomCheck":1}
```
---
## 910181 — Summer Breeze, the Eternal Moment
- Japanese: `薫風、永遠なる瞬間を`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&order>=3&order_rate<=50&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910191 — Revived by Moe!
- Japanese: `萌到讓我活過來了！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"near_count>=3&phase==1&corner!=0&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910201 — Do Ya Breakin!
- Japanese: `Do Ya Breakin!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&corner==0&order<=2&straight_front_type==2","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":700,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"phase>=2&corner==0&order<=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910211 — Thunderous Firestarter
- Japanese: `火神鳴`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"activate_count_middle>=2","effects":[{"modifier":500,"target":1,"type":27},{"modifier":250,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910221 — Best Day Ever
- Japanese: `Best day ever`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance>=401&phase>=2&is_finalcorner==1&order_rate>=20&order_rate<=40","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""},{"baseDuration":30000,"condition":"phase>=2&is_finalcorner==1&order_rate>=20&order_rate<=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910231 — Presents from X
- Japanese: `Presents from X`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"order_rate_in50_continue==1&phase==1&distance_rate>=50&order>=2&order_rate<=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910241 — Flowery ☆ Maneuver
- Japanese: `フラワリー☆マニューバ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&order_rate<=40&change_order_onetime<0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"is_finalcorner==1&order_rate>=50&order_rate<=80&change_order_onetime<0","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910251 — Purrfect Hospitality
- Japanese: `心からのおもてにゃし`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==4&phase>=2&is_finalcorner==1","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":"distance_rate>=50&order_rate_out40_continue==1"},{"baseDuration":30000,"condition":"phase>=2&is_finalcorner==1","effects":[{"modifier":500,"target":1,"type":22}],"precondition":"distance_rate>=50&order_rate_out40_continue==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 910261 — Operation Cacao
- Japanese: `オペレーション・Cacao`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"order<=4&phase==1&corner!=0&bashin_diff_behind<=3","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":35,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910271 — Latte Art For You
- Japanese: `あなたに捧げるフリーポア`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_rate>=60&slope==2&phase==1&order>=2&distance_diff_top<=10&distance_type==3","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""},{"baseDuration":24000,"condition":"distance_rate>=60&slope==2&phase==1&order>=2&distance_diff_top<=10&distance_type!=3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910281 — Sugar Parade: Start!
- Japanese: `シュガーパレード・始動！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_laterhalf_random==0&order_rate>=20&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910291 — Have Your Fill!
- Japanese: `いっぱいおあげんしぇ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=50&is_overtake==1&distance_type==2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=50&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910301 — Drain for Rose
- Japanese: `Drain for rose`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==1&order>=2&order_rate<=50","effects":[{"modifier":150,"target":1,"type":9},{"modifier":-25,"target":9,"type":9},{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910311 — Fresh ☆ Parlor
- Japanese: `フレッシュ☆パーラー`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"phase_firsthalf_random==1&order_rate<=30","effects":[{"modifier":500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910321 — Summer Halation
- Japanese: `夏空ハレーション`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_rate>=50&corner!=0&order_rate>=20&order_rate<=50&track_id==10005","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":250,"target":1,"type":31}],"precondition":""},{"baseDuration":24000,"condition":"distance_rate>=50&corner!=0&order_rate>=20&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910331 — Crystal Mist
- Japanese: `Crystal Mist`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==4&is_finalcorner==1&order_rate>=40","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910341 — Bristling Lights
- Japanese: `灯穂`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight_onetime==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase>=2&corner!=0&order_rate>=60&is_overtake==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 910351 — Delivering Beyond the Dreams!
- Japanese: `夢の先へ、届け！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"is_lastspurt==1&is_last_straight==1&order_rate>=40","effects":[{"modifier":500,"target":1,"type":27},{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910361 — ...found you.
- Japanese: `...found you.`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_finalcorner_laterhalf==1&is_overtake==1@phase>=2&is_finalcorner==1&corner==0&is_overtake==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"phase==1&change_order_onetime>0&order_rate>=50&order_rate<=80"},{"baseDuration":30000,"condition":"phase>=2&is_finalcorner_laterhalf==1&is_overtake==1@phase>=2&is_finalcorner==1&corner==0&is_overtake==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910371 — Guten Appetit♪
- Japanese: `Guten Appetit♪`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"change_order_up_finalcorner_after>=2&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910381 — One True Color
- Japanese: `One True Color`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=350&order_rate<=40&order_rate>=20&bashin_diff_behind<=1","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910391 — Invigorating Strength
- Japanese: `快なる剛力`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"slope==0@slope==2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase>=1&slope==1&order_rate>=40&order_rate<=80"}],"rarity":1,"wisdomCheck":1}
```
---
## 910401 — GET DOWN
- Japanese: `GET DOWN`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&corner!=0&order_rate>=30&order_rate<=70&blocked_side_continuetime>=2","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910411 — Cherry☆Scramble
- Japanese: `CHERRY☆スクランブル`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":6000,"condition":"order<=3&remain_distance<=401&remain_distance>=399","effects":[{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910421 — Oh!bento-magic☆
- Japanese: `Oh!bento-magic☆`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&order_rate<=50&is_overtake==1","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&is_finalcorner==1&corner!=0&change_order_onetime<0&distance_type==1@is_activate_other_skill_detail==1&is_finalcorner==1&corner!=0&change_order_onetime<0&distance_type==2","effects":[{"modifier":350,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910441 — Special Materialization
- Japanese: `とっておきmaterialize`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase>=1&slope==2&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":22},{"modifier":-200,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910451 — Round and Round, Mummy Trick♡
- Japanese: `ぐるぐるマミートリック♡`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&order<=4&bashin_diff_infront<=1","effects":[{"modifier":500,"target":1,"type":27},{"modifier":1000,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910461 — α-star*
- Japanese: `α-star*`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=40&distance_rate<=50&distance_diff_rate<=10&ground_type==2","effects":[{"modifier":500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""},{"baseDuration":36000,"condition":"distance_rate>=40&distance_rate<=50&distance_diff_rate<=10","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910471 — Close Encounters of the Literary Kind
- Japanese: `未知との遭遇、即ち物語`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_last_straight==1&order_rate<=40&track_id==10005&course_distance==2500@phase>=2&is_last_straight==1&order_rate<=40&track_id==10006&distance_type==3","effects":[{"modifier":500,"target":1,"type":27},{"modifier":500,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"phase>=2&is_last_straight==1&order_rate<=40","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910481 — GALmem. forever♪
- Japanese: `GALmem.ふぉーえば♪`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=40&order_rate<=80&motivation==5","effects":[{"modifier":1000,"target":1,"type":27}],"precondition":""},{"baseDuration":36000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=40&order_rate<=80","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910491 — Wager on the Holy Night Stars
- Japanese: `運否、聖夜の星に賭ける`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"phase_firsthalf_random==1&distance_type==3@phase_firsthalf_random==1&distance_type==4","effects":[{"modifier":-2500,"target":1,"type":21}],"precondition":""},{"baseDuration":36000,"condition":"is_activate_other_skill_detail==1&phase_laterhalf_random==1&order_rate>=40&order_rate<=80","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910501 — Hephaistos
- Japanese: `Hephaistos`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_finalcorner_laterhalf==1&order_rate<=75&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910511 — Flowering Dreams
- Japanese: `Flowering Dreams`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"order>=2&order_rate<=70&remain_distance<=201&remain_distance>=199&near_count>=3","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":350,"target":1,"type":22}],"precondition":""},{"baseDuration":30000,"condition":"order>=2&order_rate<=70&remain_distance<=201&remain_distance>=199","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910521 — Fall Down 113 Times, Get Up 114
- Japanese: `113転び114起き`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&corner!=0&distance_diff_top>=7","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910531 — Secret Technique: Everlasting Summer!!
- Japanese: `奥義・常夏バーニング！！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&remain_distance<=201&remain_distance>=199&order_rate>=20&order_rate<=50&change_order_up_end_after>=1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"remain_distance<=201&remain_distance>=199&order_rate>=20&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910551 — Bravo ☆ Wonder Doll!
- Japanese: `喝采☆ワンダードール！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&motivation==5","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":350,"target":1,"type":22}],"precondition":"phase>=2&is_finalcorner==1&corner!=0&near_count>=1&order_rate>=30&order_rate<=70"},{"baseDuration":30000,"condition":"is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase>=2&is_finalcorner==1&corner!=0&near_count>=1&order_rate>=30&order_rate<=70"}],"rarity":1,"wisdomCheck":1}
```
---
## 910561 — Grains Become Ripe
- Japanese: `禾スナハチ登ル`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&order_rate>=40&overtake_target_time>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910571 — Radiant Stride
- Japanese: `爛然闊歩`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&order_rate>=50","effects":[{"modifier":350,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910581 — Spooky-Scary-Happy
- Japanese: `Spooky-Scary-Happy`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight_onetime==1&order_rate<=40","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":-250,"target":9,"type":21},{"modifier":-250,"target":10,"type":21}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910591 — To Where the Heart Beckons
- Japanese: `ときめきが呼ぶほうへ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=60&slope==2&phase==1&order_rate>=40&order_rate<=80&remain_distance>=500","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910601 — Go☆Go☆For It!
- Japanese: `Go☆Go☆for it!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"is_last_straight==1&order_rate>=40&order_rate<=70&popularity>=4","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"is_finalcorner==1&change_order_onetime<0"},{"baseDuration":30000,"condition":"is_last_straight==1&order_rate>=40&order_rate<=70&popularity<4","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"is_finalcorner==1&change_order_onetime<0"}],"rarity":1,"wisdomCheck":1}
```
---
## 910611 — Roaring Tracen Cheerleading Squad
- Japanese: `轟！トレセン応援団！！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_last_straight==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":"distance_rate>=50&order_rate_out70_continue==1&temptation_count==0"}],"rarity":1,"wisdomCheck":1}
```
---
## 910621 — Rolling Power Drive!
- Japanese: `ごろりん！？パワードライブ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"distance_rate>=50&corner!=0&order_rate>=40&order_rate<=80&distance_type==3","effects":[{"modifier":500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""},{"baseDuration":12000,"condition":"distance_rate>=50&corner!=0&order_rate>=40&order_rate<=80","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910631 — Chitose, Circling On
- Japanese: `千歳、廻りて`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_firsthalf==1&is_overtake==1@phase_firsthalf==1&overtake_target_time>=1","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910641 — Jingle All the Way
- Japanese: `jingle all the way`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":42000,"condition":"distance_rate>=40&corner==0&order==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910651 — It's Mashup Time!
- Japanese: `ノッてけ、マッシュアップ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==2&blocked_side_continuetime>=2&order_rate<=50&phase==0&accumulatetime>=5","effects":[{"modifier":2500,"target":1,"type":27},{"modifier":-300,"target":1,"type":9}],"precondition":""},{"baseDuration":30000,"condition":"blocked_side_continuetime>=2&order_rate<=50&phase==0&accumulatetime>=5","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910671 — Arrow of Gold, Break up the Dark Clouds
- Japanese: `玄雲散らす、黄金甲矢`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=40&order_rate<=80","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":50,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910681 — Lavish Feast
- Japanese: `あっぱれ大盤振る舞い！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase>=2&corner!=0&remain_distance>=600&order<=3","effects":[{"modifier":1500,"target":1,"type":22},{"modifier":500,"target":1,"type":31}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910691 — Bloom! Blossom! Sakura!
- Japanese: `咲け咲け！私！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=651&remain_distance>=649&order_rate<=40&order_rate>=30","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":"phase==1&blocked_side_continuetime>=2"}],"rarity":1,"wisdomCheck":1}
```
---
## 910701 — Driven by Light, the Heavenly Wolf Hunts
- Japanese: `駆るは光、狩るは星々`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":42000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=30&order_rate<=80&distance_type==3&base_power>=1200","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":36000,"condition":"distance_rate>=40&distance_rate<=50&order_rate>=30&order_rate<=80","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910711 — Danser le Présent
- Japanese: `Danser le présent`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_last_straight==1&order_rate>=20&order_rate<=40&bashin_diff_behind<=1","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":350,"target":1,"type":22},{"modifier":-300,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910721 — Decisive Blade of Blazing Fire
- Japanese: `剛勇果断、烈火之刀`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate_after_random==50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"distance_rate>=40&distance_rate<=50&blocked_side_continuetime>=2"}],"rarity":1,"wisdomCheck":1}
```
---
## 910741 — Illuminate You
- Japanese: `Illuminate you`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":12000,"condition":"phase==1&order_rate>=40&order_rate<=80","effects":[{"modifier":350,"target":1,"type":9},{"modifier":-1500,"target":1,"type":21}],"precondition":""},{"baseDuration":48000,"condition":"is_activate_other_skill_detail==1&base_stamina>=1200&phase>=2","effects":[{"modifier":350,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910761 — Spring Light: Bon Appétit
- Japanese: `春光・Bon appétit`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_finalcorner_laterhalf==1&order_rate>=40&order_rate<=80","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910771 — Joy to the World
- Japanese: `Joy to the World`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=45&order_rate>=20&order_rate<=50&remain_distance>=1000","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"phase_firsthalf==1&is_activate_heal_skill==1"},{"baseDuration":30000,"condition":"distance_rate>=45&order_rate>=20&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":"phase_firsthalf==1&is_activate_heal_skill==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 910781 — Breezy Treat
- Japanese: `Breezy Treat`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"distance_type==2&remain_distance<=351&remain_distance>=349&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":22},{"modifier":350,"target":1,"type":27}],"precondition":""},{"baseDuration":24000,"condition":"remain_distance<=351&remain_distance>=349&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910801 — Geothermal Overdrive
- Japanese: `地熱解放オーヴァードライブ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"ground_type==2&phase_laterhalf==0&order_rate<=30","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&distance_rate>=40&distance_rate<=50&overtake_target_time>=2","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910831 — Immortal Work
- Japanese: `Immortal Work`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"distance_rate>=50&distance_rate<=51&order_rate>=40&order_rate<=80"}],"rarity":1,"wisdomCheck":1}
```
---
## 910841 — Terpsichore of the Abyss
- Japanese: `深淵のテルプシコラー`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&order_rate>=50","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910851 — Sapphire Flame
- Japanese: `蒼炎`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate<=50&distance_rate>=45&order_rate<=90&order_rate>=40&distance_type==2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate<=50&distance_rate>=45&order_rate<=90&order_rate>=40","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910861 — Everlasting Knot
- Japanese: `解けぬ結い目`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"running_style==2&order_rate<=40&remain_distance>=299&remain_distance<=301&distance_diff_top<=5","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"running_style==2&order_rate<=40&remain_distance>=299&remain_distance<=301","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910871 — Fluffy Fuzzy Hour
- Japanese: `ふわもこアワー`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==1&distance_rate<=50&distance_rate>=45&order_rate<=30&base_wiz>=1200","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==1&distance_rate<=50&distance_rate>=45&order_rate<=30","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910881 — Summer Thunder Cascade!
- Japanese: `夏雷カスケード！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==3&phase_firsthalf==1&change_order_onetime<0","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910891 — Tidebreaker
- Japanese: `Tidebreaker`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":42000,"condition":"distance_type==4&distance_rate>=40&distance_rate<=50&order_rate>=20&order_rate<=70","effects":[{"modifier":500,"target":1,"type":27},{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910911 — Je t'aime ☆ Vacances
- Japanese: `ジュ・テーム☆バカンス！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=50&corner==3&order_rate>=40&order_rate<=90&slope==1&course_distance==2000","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=50&corner==3&order_rate>=40&order_rate<=90","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910931 — Miracle, Hopes, Melody
- Japanese: `きせき・おもい・かなで`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase==3&is_lastspurt==1&distance_type==1&order<=3","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":350,"target":1,"type":22}],"precondition":"phase==1&order_rate<=70&order_rate>=20&blocked_side_continuetime>=2"},{"baseDuration":30000,"condition":"phase==3&is_lastspurt==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase==1&order_rate<=70&order_rate>=20&blocked_side_continuetime>=2"}],"rarity":1,"wisdomCheck":1}
```
---
## 910981 — Parade of the Five Heavenly Beasts
- Japanese: `五獣挙りて彩光奏づ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&order_rate<=50&ground_type==2&remain_distance>=500","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 910991 — Popping☆Clams
- Japanese: `とびだせ☆ポッピングシェル`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=51&ground_type==2&corner!=3","effects":[{"modifier":500,"target":1,"type":27},{"modifier":350,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=51","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 911001 — Bathkeeper's Heart of Zen
- Japanese: `湯守の和心`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_firsthalf==1&order>=3&infront_near_lane_time>=3@phase_firsthalf==1&order>=3&behind_near_lane_time>=3","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 91101351 — In Search of Gold
- Japanese: `黄金を訪ねて`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"running_style==3@running_style==4"},{"baseDuration":12000,"condition":"is_activate_other_skill_detail==1&course_distance>=2000&is_lastspurt==1","effects":[{"modifier":2000,"target":1,"type":31}],"precondition":""}],"rarity":6,"wisdomCheck":1}
```
---
## 911021 — Che Piacevole!
- Japanese: `ケ・ピアチェーヴォレ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate_in50_continue==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 911041 — Determined Stroke
- Japanese: `決意一筆`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":48000,"condition":"distance_type==3&distance_rate>=50&order_rate_in40_continue==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 911051 — Encounter With U
- Japanese: `Encounter with U`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_last_straight==1&phase>=2&order>=2","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 911061 — A Small Miracle for You♪
- Japanese: `小さな奇跡、フォーユー♪`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase==1&is_overtake==1","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"is_activate_other_skill_detail==1&phase>=2&is_finalcorner_laterhalf==1&order_rate>=40","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 911071 — Romantic Horizon
- Japanese: `Romantic Horizon`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"distance_type==3&phase_laterhalf_random==1&order<=3","effects":[{"modifier":500,"target":1,"type":27},{"modifier":500,"target":1,"type":31}],"precondition":""},{"baseDuration":36000,"condition":"distance_type==3&phase_laterhalf_random==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 911091 — Shine on Forever
- Japanese: `ずっとずっと輝いて`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==1&phase>=2&corner!=0","effects":[{"modifier":500,"target":1,"type":22}],"precondition":"track_id==10009&course_distance==1600@track_id==10008&course_distance==2000@track_id==10006&course_distance==2400"}],"rarity":1,"wisdomCheck":1}
```
---
## 911101 — Perennial Babbles
- Japanese: `時かけるせせらぎ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"is_lastspurt==1&phase==3&running_style==2","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 911191 — Dreaming of the Silver World
- Japanese: `夢寐に見る銀世界`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"order_rate>=50&remain_distance>=999&remain_distance<=1001","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""},{"baseDuration":18000,"condition":"is_last_straight==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"distance_type==4&phase>=2&corner!=0&change_order_onetime<0&is_activate_other_skill_detail==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 911241 — Break Through the Dawn Haze, Seize the Morning
- Japanese: `暁霞を拓き、朝を掴む`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"running_style==2&phase>=2&is_finalcorner_laterhalf==1&order_rate<=50","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 911321 — Watch Us Flourish
- Japanese: `Watch Us Flourish`
- English name source: close Japanese→English translation
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"phase==1&corner==0&order_rate<=50","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920011 — Dignified Dreamlike Brocade
- Japanese: `威風堂々、夢錦！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_finalcorner==1&corner!=0&is_activate_any_skill==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"track_id==10005"},{"baseDuration":30000,"condition":"phase>=2&is_finalcorner==1&corner!=0&is_activate_any_skill==1","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920031 — Merrymaking Song and Dance
- Japanese: `歌舞歓楽や、ああをかし`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase>=2&is_finalcorner_laterhalf==1&course_distance>=2400&course_distance<=2500@phase>=2&is_finalcorner==1&corner==0&course_distance>=2400&course_distance<=2500","effects":[{"modifier":1500,"target":1,"type":27},{"modifier":350,"target":1,"type":22}],"precondition":"distance_rate>=50&order_rate<=50&overtake_target_time>=2"},{"baseDuration":30000,"condition":"phase>=2&is_finalcorner_laterhalf==1@phase>=2&is_finalcorner==1&corner==0","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate<=50&overtake_target_time>=2"}],"rarity":1,"wisdomCheck":1}
```
---
## 920041 — Miraculously Tubular Oracle
- Japanese: `霊験灼然チョベリグ神託`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase_firsthalf==1&is_overtake==1&order_rate<=30&distance_type==2@phase_firsthalf==1&overtake_target_time>=1&order_rate<=30&distance_type==2","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"phase_firsthalf==1&is_overtake==1&order_rate<=30@phase_firsthalf==1&overtake_target_time>=1&order_rate<=30","effects":[{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920061 — Ashen Trail: Cinderella Gray
- Japanese: `灰の光跡：シンデレラグレイ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=45&distance_rate<=55&order_rate>=20&order_rate<=70","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920071 — Vive la GOLD
- Japanese: `Vive la GOLD`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_type==3&is_finalcorner==1&is_overtake==1&order_rate>=50&is_badstart==1@distance_type==4&is_finalcorner==1&is_overtake==1&order_rate>=50&is_badstart==1","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"distance_type==3&is_finalcorner==1&is_overtake==1&order_rate>=50@distance_type==4&is_finalcorner==1&is_overtake==1&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920101 — Have S'more Love!
- Japanese: `Have S'more Love!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"running_style==2&phase_laterhalf_random==0&order_rate>=20&order_rate<=70","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920111 — Naginata Maiden's Dance
- Japanese: `演舞・撫子大薙刀`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"remain_distance<=401&remain_distance>=399&is_basis_distance==0","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate<=70&order_rate>=30&overtake_target_time>=1@distance_rate>=50&order_rate<=70&order_rate>=30&is_overtake==1"},{"baseDuration":30000,"condition":"remain_distance<=401&remain_distance>=399","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"distance_rate>=50&order_rate<=70&order_rate>=30&overtake_target_time>=1@distance_rate>=50&order_rate<=70&order_rate>=30&is_overtake==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 920131 — The Sea Glitters, but You're Dazzling
- Japanese: `きらめくは海、まばゆきは君`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&order_rate<=40","effects":[{"modifier":350,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920231 — Accumulative Victory
- Japanese: `勝利ヘ至ル累積`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"distance_rate>=50&distance_rate<=51&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920241 — HOP STEP♪LOCK ON!
- Japanese: `HOP STEP♪LOCK ON!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"phase>=1&order==1@phase>=1&order<=3&is_overtake==1","effects":[{"modifier":350,"target":1,"type":9},{"modifier":500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920301 — Clear Sky Cooking♪
- Japanese: `あおぞらクッキング♪`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"order_rate<=40&phase>=2&corner!=0&is_finalcorner==1","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920311 — Full-Throttle Cyclone!
- Japanese: `全力全開！サイクロン`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_laterhalf==0&order_rate<=30","effects":[{"modifier":350,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"is_activate_other_skill_detail==1&distance_type==3&phase==1&corner==0","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920321 — Tachyon Potential
- Japanese: `超光速微粒子の可能性`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase>=2&is_finalcorner==1&order_rate<=50&distance_type==3","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"phase>=2&is_finalcorner==1&order_rate<=50","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920351 — GO! Full-send
- Japanese: `GO! Full-send`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"corner==3&course_distance==2400&popularity<=3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase==1&change_order_onetime<0&order_rate>=40&order_rate<=80"},{"baseDuration":24000,"condition":"corner==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"phase==1&change_order_onetime<0&order_rate>=40&order_rate<=80"}],"rarity":1,"wisdomCheck":1}
```
---
## 920371 — Geschenk of the Salty Sea Breeze
- Japanese: `潮風のGeschenk`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"is_finalcorner==1&corner!=0&order_rate<=80&order_rate>=40&distance_type==3","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920401 — Silent Sunset Gold
- Japanese: `Silent Sunset Gold`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"distance_rate>=40&distance_rate<=45&order_rate>=30&order_rate<=80","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":18000,"condition":"remain_distance<=351&remain_distance>=349","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":"phase>=2&blocked_side_continuetime>=2&corner!=0&is_activate_other_skill_detail==1"}],"rarity":1,"wisdomCheck":1}
```
---
## 920451 — Ninja Art: Seal of the Smiling Heart
- Japanese: `忍法・ほほえみ心結の印`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"phase==1&distance_type==3&corner!=0&order_rate>=20&order_rate<=50@phase==1&distance_type==4&corner!=0&order_rate>=20&order_rate<=50","effects":[{"modifier":150,"target":1,"type":9},{"modifier":500,"target":1,"type":27}],"precondition":""},{"baseDuration":0,"condition":"phase==1&corner!=0&order_rate>=20&order_rate<=50","effects":[{"modifier":150,"target":1,"type":9}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920461 — Forward March!
- Japanese: `Forward March!`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"ground_type==2&distance_rate>=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920481 — Sick Moves ☆ Juggle Beat
- Japanese: `ヤバ技☆ジャグルビート`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":42000,"condition":"slope==0&distance_type==3@slope==1&distance_type==3@slope==0&distance_type==4@slope==1&distance_type==4","effects":[{"modifier":350,"target":1,"type":27}],"precondition":"phase>=1&slope==2&order_rate>=30&order_rate<=70"}],"rarity":1,"wisdomCheck":1}
```
---
## 920501 — Overdrive Speed
- Japanese: `Overdrive Speed`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase>=2&corner!=0&remain_distance>=600&order_rate>=50","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920601 — Springy Festivities
- Japanese: `もちっと・ハレハレ`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"phase>=2&is_finalcorner==1&order_rate>=40&distance_type==3","effects":[{"modifier":2500,"target":1,"type":22}],"precondition":""},{"baseDuration":24000,"condition":"phase>=2&is_finalcorner==1&order_rate>=40","effects":[{"modifier":2500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920611 — The Winding Road to Ideals
- Japanese: `理想へのwinding road`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":36000,"condition":"is_lastspurt==1&phase==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":"remain_distance<=600&order_rate>=40&order_rate<=80&is_behind_in==1&change_order_onetime<0"}],"rarity":1,"wisdomCheck":1}
```
---
## 920671 — Ponte de Diamant
- Japanese: `ポンテ・デ・ディアマン`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":30000,"condition":"phase_laterhalf_random==1&order_rate>=40&order_rate<=80&distance_type==3","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":30000,"condition":"phase_laterhalf_random==1&order_rate>=40&order_rate<=80&distance_type!=3","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 920681 — Becoming Everyone's Joy!
- Japanese: `ミンナノアタシへ！`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":18000,"condition":"phase<=1&change_order_onetime>0&accumulatetime>=5&order_rate<=50@phase<=1&blocked_side_continuetime>=2&accumulatetime>=5&order_rate<=50","effects":[{"modifier":1500,"target":1,"type":27}],"precondition":""},{"baseDuration":36000,"condition":"is_activate_other_skill_detail==1&order<=2&distance_rate>=50&distance_type==4","effects":[{"modifier":500,"target":1,"type":27}],"precondition":""}],"rarity":1,"wisdomCheck":1}
```
---
## 92111091 — Shine on Forever
- Japanese: `ずっとずっと輝いて`
- English name source: skillnames.json (same Japanese name)
- Original `skill_data.json` record (unchanged):
```json
{"alternatives":[{"baseDuration":24000,"condition":"ground_type==1&phase>=2&corner!=0&slope==2","effects":[{"modifier":1500,"target":1,"type":22},{"modifier":1000,"target":1,"type":31}],"precondition":"track_id==10009&course_distance==1600@track_id==10008&course_distance==2000@track_id==10006&course_distance==2400"},{"baseDuration":24000,"condition":"ground_type==1&phase>=2&corner!=0","effects":[{"modifier":1500,"target":1,"type":22}],"precondition":"track_id==10009&course_distance==1600@track_id==10008&course_distance==2000@track_id==10006&course_distance==2400"}],"rarity":6,"wisdomCheck":1}
```
