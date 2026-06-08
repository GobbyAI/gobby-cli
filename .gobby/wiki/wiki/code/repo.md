---
title: Repository Overview
type: code_repo
source_files:
- file: crates/gcode/src/commands/codewiki/build.rs
  ranges:
  - 3-73
  - 75-164
- file: crates/gcode/src/commands/codewiki/cluster.rs
  ranges:
  - 3-54
  - 56-80
  - 89-130
  - 132-156
  - 158-168
  - 170-178
  - 180-196
  - 198-206
  - 208-226
  - 228-233
- file: crates/gcode/src/commands/codewiki/graph.rs
  ranges:
  - 4-124
  - 34-49
  - 126-145
  - 147-165
- file: crates/gcode/src/commands/codewiki/io.rs
  ranges:
  - 3-9
  - 11-59
  - 61-69
  - 71-89
  - 91-111
  - 113-120
  - 122-125
  - 127-148
  - 150-183
  - 186-216
  - 219-226
  - 228-238
- file: crates/gcode/src/commands/codewiki/mod.rs
  ranges:
  - 68-73
  - 76-80
  - 82-104
  - 83-92
  - 94-103
  - 107-110
  - 113-116
  - 118-139
  - 119-124
  - 126-131
  - 133-138
  - 142-146
  - 149-156
  - 159-165
  - 168-178
  - 181-185
  - 188-192
  - 195-199
  - 202-214
  - 217-220
  - 223-225
  - '227'
  - 229-249
  - 230-236
  - 238-244
  - 246-248
  - 251-326
  - 328-333
  - 335-340
  - 342-405
- file: crates/gcode/src/commands/codewiki/paths.rs
  ranges:
  - 3-14
  - 16-28
  - 30-32
  - 34-41
  - 43-88
  - 93-101
  - 103-109
  - 111-119
  - 121-123
  - 125-127
  - 129-137
  - 139-141
  - 143-145
  - 147-149
  - 151-153
  - 155-157
- file: crates/gcode/src/commands/codewiki/prompts.rs
  ranges:
  - 10-32
  - 34-55
  - 57-90
  - 92-112
  - 115-123
  - 126-129
- file: crates/gcode/src/commands/codewiki/render.rs
  ranges:
  - 5-51
  - 53-141
  - 143-172
  - 174-224
  - 226-239
  - 241-251
  - 253-268
  - 270-318
  - 320-349
  - 351-410
  - 412-450
- file: crates/gcode/src/commands/codewiki/tests.rs
  ranges:
  - 7-41
  - 44-51
  - 54-127
  - 130-143
  - 146-148
  - 151-156
  - 159-171
  - 174-196
  - 199-226
  - 229-238
  - 241-248
  - 251-335
  - 338-406
  - 409-423
  - 426-456
  - 459-480
  - 483-521
  - 524-536
  - 539-555
  - 558-575
  - 578-592
  - 595-628
  - 631-680
  - 683-776
  - 779-802
  - 805-809
  - 813-827
  - 831-845
  - 847-855
  - 857-859
  - 861-889
  - 891-919
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 6-11
  - 14-17
  - 19-50
  - 52-68
  - 70-78
  - 80-83
  - 85-100
  - 102-111
  - 113-125
  - 127-133
  - 135-137
  - 139-148
  - 150-159
  - 161-172
  - 174-200
  - 202-219
  - 221-234
  - 236-277
---

# Repository Overview

## Overview

Repository code documentation covers 10 files across 5 modules. [crates/gcode/src/commands/codewiki/build.rs:3-73] [crates/gcode/src/commands/codewiki/build.rs:75-164] [crates/gcode/src/commands/codewiki/cluster.rs:3-54] [crates/gcode/src/commands/codewiki/cluster.rs:56-80] [crates/gcode/src/commands/codewiki/cluster.rs:89-130] [crates/gcode/src/commands/codewiki/cluster.rs:132-156] [crates/gcode/src/commands/codewiki/cluster.rs:158-168] [crates/gcode/src/commands/codewiki/cluster.rs:170-178] [crates/gcode/src/commands/codewiki/cluster.rs:180-196] [crates/gcode/src/commands/codewiki/cluster.rs:198-206] [crates/gcode/src/commands/codewiki/cluster.rs:208-226] [crates/gcode/src/commands/codewiki/cluster.rs:228-233] [crates/gcode/src/commands/codewiki/graph.rs:4-124] [crates/gcode/src/commands/codewiki/graph.rs:34-49] [crates/gcode/src/commands/codewiki/graph.rs:126-145] [crates/gcode/src/commands/codewiki/graph.rs:147-165] [crates/gcode/src/commands/codewiki/io.rs:3-9] [crates/gcode/src/commands/codewiki/io.rs:11-59] [crates/gcode/src/commands/codewiki/io.rs:61-69] [crates/gcode/src/commands/codewiki/io.rs:71-89] [crates/gcode/src/commands/codewiki/io.rs:91-111] [crates/gcode/src/commands/codewiki/io.rs:113-120] [crates/gcode/src/commands/codewiki/io.rs:122-125] [crates/gcode/src/commands/codewiki/io.rs:127-148] [crates/gcode/src/commands/codewiki/io.rs:150-183] [crates/gcode/src/commands/codewiki/io.rs:186-216] [crates/gcode/src/commands/codewiki/io.rs:219-226] [crates/gcode/src/commands/codewiki/io.rs:228-238] [crates/gcode/src/commands/codewiki/mod.rs:68-73] [crates/gcode/src/commands/codewiki/mod.rs:76-80] [crates/gcode/src/commands/codewiki/mod.rs:82-104] [crates/gcode/src/commands/codewiki/mod.rs:83-92] [crates/gcode/src/commands/codewiki/mod.rs:94-103] [crates/gcode/src/commands/codewiki/mod.rs:107-110] [crates/gcode/src/commands/codewiki/mod.rs:113-116] [crates/gcode/src/commands/codewiki/mod.rs:118-139] [crates/gcode/src/commands/codewiki/mod.rs:119-124] [crates/gcode/src/commands/codewiki/mod.rs:126-131] [crates/gcode/src/commands/codewiki/mod.rs:133-138] [crates/gcode/src/commands/codewiki/mod.rs:142-146] [crates/gcode/src/commands/codewiki/mod.rs:149-156] [crates/gcode/src/commands/codewiki/mod.rs:159-165] [crates/gcode/src/commands/codewiki/mod.rs:168-178] [crates/gcode/src/commands/codewiki/mod.rs:181-185] [crates/gcode/src/commands/codewiki/mod.rs:188-192] [crates/gcode/src/commands/codewiki/mod.rs:195-199] [crates/gcode/src/commands/codewiki/mod.rs:202-214] [crates/gcode/src/commands/codewiki/mod.rs:217-220] [crates/gcode/src/commands/codewiki/mod.rs:223-225] [crates/gcode/src/commands/codewiki/mod.rs:227] [crates/gcode/src/commands/codewiki/mod.rs:229-249] [crates/gcode/src/commands/codewiki/mod.rs:230-236] [crates/gcode/src/commands/codewiki/mod.rs:238-244] [crates/gcode/src/commands/codewiki/mod.rs:246-248] [crates/gcode/src/commands/codewiki/mod.rs:251-326] [crates/gcode/src/commands/codewiki/mod.rs:328-333] [crates/gcode/src/commands/codewiki/mod.rs:335-340] [crates/gcode/src/commands/codewiki/mod.rs:342-405] [crates/gcode/src/commands/codewiki/paths.rs:3-14] [crates/gcode/src/commands/codewiki/paths.rs:16-28] [crates/gcode/src/commands/codewiki/paths.rs:30-32] [crates/gcode/src/commands/codewiki/paths.rs:34-41] [crates/gcode/src/commands/codewiki/paths.rs:43-88] [crates/gcode/src/commands/codewiki/paths.rs:93-101] [crates/gcode/src/commands/codewiki/paths.rs:103-109] [crates/gcode/src/commands/codewiki/paths.rs:111-119] [crates/gcode/src/commands/codewiki/paths.rs:121-123] [crates/gcode/src/commands/codewiki/paths.rs:125-127] [crates/gcode/src/commands/codewiki/paths.rs:129-137] [crates/gcode/src/commands/codewiki/paths.rs:139-141] [crates/gcode/src/commands/codewiki/paths.rs:143-145] [crates/gcode/src/commands/codewiki/paths.rs:147-149] [crates/gcode/src/commands/codewiki/paths.rs:151-153] [crates/gcode/src/commands/codewiki/paths.rs:155-157] [crates/gcode/src/commands/codewiki/prompts.rs:10-32] [crates/gcode/src/commands/codewiki/prompts.rs:34-55] [crates/gcode/src/commands/codewiki/prompts.rs:57-90] [crates/gcode/src/commands/codewiki/prompts.rs:92-112] [crates/gcode/src/commands/codewiki/prompts.rs:115-123] [crates/gcode/src/commands/codewiki/prompts.rs:126-129] [crates/gcode/src/commands/codewiki/render.rs:5-51] [crates/gcode/src/commands/codewiki/render.rs:53-141] [crates/gcode/src/commands/codewiki/render.rs:143-172] [crates/gcode/src/commands/codewiki/render.rs:174-224] [crates/gcode/src/commands/codewiki/render.rs:226-239] [crates/gcode/src/commands/codewiki/render.rs:241-251] [crates/gcode/src/commands/codewiki/render.rs:253-268] [crates/gcode/src/commands/codewiki/render.rs:270-318] [crates/gcode/src/commands/codewiki/render.rs:320-349] [crates/gcode/src/commands/codewiki/render.rs:351-410] [crates/gcode/src/commands/codewiki/render.rs:412-450] [crates/gcode/src/commands/codewiki/tests.rs:7-41] [crates/gcode/src/commands/codewiki/tests.rs:44-51] [crates/gcode/src/commands/codewiki/tests.rs:54-127] [crates/gcode/src/commands/codewiki/tests.rs:130-143] [crates/gcode/src/commands/codewiki/tests.rs:146-148] [crates/gcode/src/commands/codewiki/tests.rs:151-156] [crates/gcode/src/commands/codewiki/tests.rs:159-171] [crates/gcode/src/commands/codewiki/tests.rs:174-196] [crates/gcode/src/commands/codewiki/tests.rs:199-226] [crates/gcode/src/commands/codewiki/tests.rs:229-238] [crates/gcode/src/commands/codewiki/tests.rs:241-248] [crates/gcode/src/commands/codewiki/tests.rs:251-335] [crates/gcode/src/commands/codewiki/tests.rs:338-406] [crates/gcode/src/commands/codewiki/tests.rs:409-423] [crates/gcode/src/commands/codewiki/tests.rs:426-456] [crates/gcode/src/commands/codewiki/tests.rs:459-480] [crates/gcode/src/commands/codewiki/tests.rs:483-521] [crates/gcode/src/commands/codewiki/tests.rs:524-536] [crates/gcode/src/commands/codewiki/tests.rs:539-555] [crates/gcode/src/commands/codewiki/tests.rs:558-575] [crates/gcode/src/commands/codewiki/tests.rs:578-592] [crates/gcode/src/commands/codewiki/tests.rs:595-628] [crates/gcode/src/commands/codewiki/tests.rs:631-680] [crates/gcode/src/commands/codewiki/tests.rs:683-776] [crates/gcode/src/commands/codewiki/tests.rs:779-802] [crates/gcode/src/commands/codewiki/tests.rs:805-809] [crates/gcode/src/commands/codewiki/tests.rs:813-827] [crates/gcode/src/commands/codewiki/tests.rs:831-845] [crates/gcode/src/commands/codewiki/tests.rs:847-855] [crates/gcode/src/commands/codewiki/tests.rs:857-859] [crates/gcode/src/commands/codewiki/tests.rs:861-889] [crates/gcode/src/commands/codewiki/tests.rs:891-919] [crates/gcode/src/commands/codewiki/text.rs:6-11] [crates/gcode/src/commands/codewiki/text.rs:14-17] [crates/gcode/src/commands/codewiki/text.rs:19-50] [crates/gcode/src/commands/codewiki/text.rs:52-68] [crates/gcode/src/commands/codewiki/text.rs:70-78] [crates/gcode/src/commands/codewiki/text.rs:80-83] [crates/gcode/src/commands/codewiki/text.rs:85-100] [crates/gcode/src/commands/codewiki/text.rs:102-111] [crates/gcode/src/commands/codewiki/text.rs:113-125] [crates/gcode/src/commands/codewiki/text.rs:127-133] [crates/gcode/src/commands/codewiki/text.rs:135-137] [crates/gcode/src/commands/codewiki/text.rs:139-148] [crates/gcode/src/commands/codewiki/text.rs:150-159] [crates/gcode/src/commands/codewiki/text.rs:161-172] [crates/gcode/src/commands/codewiki/text.rs:174-200] [crates/gcode/src/commands/codewiki/text.rs:202-219] [crates/gcode/src/commands/codewiki/text.rs:221-234] [crates/gcode/src/commands/codewiki/text.rs:236-277]

## Modules

- [[modules/crates|crates]] - `crates` contains 0 direct files and 1 child module. [crates/gcode/src/commands/codewiki/build.rs:3-73] [crates/gcode/src/commands/codewiki/build.rs:75-164] [crates/gcode/src/commands/codewiki/cluster.rs:3-54] [crates/gcode/src/commands/codewiki/cluster.rs:56-80] [crates/gcode/src/commands/codewiki/cluster.rs:89-130] [crates/gcode/src/commands/codewiki/cluster.rs:132-156] [crates/gcode/src/commands/codewiki/cluster.rs:158-168] [crates/gcode/src/commands/codewiki/cluster.rs:170-178] [crates/gcode/src/commands/codewiki/cluster.rs:180-196] [crates/gcode/src/commands/codewiki/cluster.rs:198-206] [crates/gcode/src/commands/codewiki/cluster.rs:208-226] [crates/gcode/src/commands/codewiki/cluster.rs:228-233] [crates/gcode/src/commands/codewiki/graph.rs:4-124] [crates/gcode/src/commands/codewiki/graph.rs:34-49] [crates/gcode/src/commands/codewiki/graph.rs:126-145] [crates/gcode/src/commands/codewiki/graph.rs:147-165] [crates/gcode/src/commands/codewiki/io.rs:3-9] [crates/gcode/src/commands/codewiki/io.rs:11-59] [crates/gcode/src/commands/codewiki/io.rs:61-69] [crates/gcode/src/commands/codewiki/io.rs:71-89] [crates/gcode/src/commands/codewiki/io.rs:91-111] [crates/gcode/src/commands/codewiki/io.rs:113-120] [crates/gcode/src/commands/codewiki/io.rs:122-125] [crates/gcode/src/commands/codewiki/io.rs:127-148] [crates/gcode/src/commands/codewiki/io.rs:150-183] [crates/gcode/src/commands/codewiki/io.rs:186-216] [crates/gcode/src/commands/codewiki/io.rs:219-226] [crates/gcode/src/commands/codewiki/io.rs:228-238] [crates/gcode/src/commands/codewiki/mod.rs:68-73] [crates/gcode/src/commands/codewiki/mod.rs:76-80] [crates/gcode/src/commands/codewiki/mod.rs:82-104] [crates/gcode/src/commands/codewiki/mod.rs:83-92] [crates/gcode/src/commands/codewiki/mod.rs:94-103] [crates/gcode/src/commands/codewiki/mod.rs:107-110] [crates/gcode/src/commands/codewiki/mod.rs:113-116] [crates/gcode/src/commands/codewiki/mod.rs:118-139] [crates/gcode/src/commands/codewiki/mod.rs:119-124] [crates/gcode/src/commands/codewiki/mod.rs:126-131] [crates/gcode/src/commands/codewiki/mod.rs:133-138] [crates/gcode/src/commands/codewiki/mod.rs:142-146] [crates/gcode/src/commands/codewiki/mod.rs:149-156] [crates/gcode/src/commands/codewiki/mod.rs:159-165] [crates/gcode/src/commands/codewiki/mod.rs:168-178] [crates/gcode/src/commands/codewiki/mod.rs:181-185] [crates/gcode/src/commands/codewiki/mod.rs:188-192] [crates/gcode/src/commands/codewiki/mod.rs:195-199] [crates/gcode/src/commands/codewiki/mod.rs:202-214] [crates/gcode/src/commands/codewiki/mod.rs:217-220] [crates/gcode/src/commands/codewiki/mod.rs:223-225] [crates/gcode/src/commands/codewiki/mod.rs:227] [crates/gcode/src/commands/codewiki/mod.rs:229-249] [crates/gcode/src/commands/codewiki/mod.rs:230-236] [crates/gcode/src/commands/codewiki/mod.rs:238-244] [crates/gcode/src/commands/codewiki/mod.rs:246-248] [crates/gcode/src/commands/codewiki/mod.rs:251-326] [crates/gcode/src/commands/codewiki/mod.rs:328-333] [crates/gcode/src/commands/codewiki/mod.rs:335-340] [crates/gcode/src/commands/codewiki/mod.rs:342-405] [crates/gcode/src/commands/codewiki/paths.rs:3-14] [crates/gcode/src/commands/codewiki/paths.rs:16-28] [crates/gcode/src/commands/codewiki/paths.rs:30-32] [crates/gcode/src/commands/codewiki/paths.rs:34-41] [crates/gcode/src/commands/codewiki/paths.rs:43-88] [crates/gcode/src/commands/codewiki/paths.rs:93-101] [crates/gcode/src/commands/codewiki/paths.rs:103-109] [crates/gcode/src/commands/codewiki/paths.rs:111-119] [crates/gcode/src/commands/codewiki/paths.rs:121-123] [crates/gcode/src/commands/codewiki/paths.rs:125-127] [crates/gcode/src/commands/codewiki/paths.rs:129-137] [crates/gcode/src/commands/codewiki/paths.rs:139-141] [crates/gcode/src/commands/codewiki/paths.rs:143-145] [crates/gcode/src/commands/codewiki/paths.rs:147-149] [crates/gcode/src/commands/codewiki/paths.rs:151-153] [crates/gcode/src/commands/codewiki/paths.rs:155-157] [crates/gcode/src/commands/codewiki/prompts.rs:10-32] [crates/gcode/src/commands/codewiki/prompts.rs:34-55] [crates/gcode/src/commands/codewiki/prompts.rs:57-90] [crates/gcode/src/commands/codewiki/prompts.rs:92-112] [crates/gcode/src/commands/codewiki/prompts.rs:115-123] [crates/gcode/src/commands/codewiki/prompts.rs:126-129] [crates/gcode/src/commands/codewiki/render.rs:5-51] [crates/gcode/src/commands/codewiki/render.rs:53-141] [crates/gcode/src/commands/codewiki/render.rs:143-172] [crates/gcode/src/commands/codewiki/render.rs:174-224] [crates/gcode/src/commands/codewiki/render.rs:226-239] [crates/gcode/src/commands/codewiki/render.rs:241-251] [crates/gcode/src/commands/codewiki/render.rs:253-268] [crates/gcode/src/commands/codewiki/render.rs:270-318] [crates/gcode/src/commands/codewiki/render.rs:320-349] [crates/gcode/src/commands/codewiki/render.rs:351-410] [crates/gcode/src/commands/codewiki/render.rs:412-450] [crates/gcode/src/commands/codewiki/tests.rs:7-41] [crates/gcode/src/commands/codewiki/tests.rs:44-51] [crates/gcode/src/commands/codewiki/tests.rs:54-127] [crates/gcode/src/commands/codewiki/tests.rs:130-143] [crates/gcode/src/commands/codewiki/tests.rs:146-148] [crates/gcode/src/commands/codewiki/tests.rs:151-156] [crates/gcode/src/commands/codewiki/tests.rs:159-171] [crates/gcode/src/commands/codewiki/tests.rs:174-196] [crates/gcode/src/commands/codewiki/tests.rs:199-226] [crates/gcode/src/commands/codewiki/tests.rs:229-238] [crates/gcode/src/commands/codewiki/tests.rs:241-248] [crates/gcode/src/commands/codewiki/tests.rs:251-335] [crates/gcode/src/commands/codewiki/tests.rs:338-406] [crates/gcode/src/commands/codewiki/tests.rs:409-423] [crates/gcode/src/commands/codewiki/tests.rs:426-456] [crates/gcode/src/commands/codewiki/tests.rs:459-480] [crates/gcode/src/commands/codewiki/tests.rs:483-521] [crates/gcode/src/commands/codewiki/tests.rs:524-536] [crates/gcode/src/commands/codewiki/tests.rs:539-555] [crates/gcode/src/commands/codewiki/tests.rs:558-575] [crates/gcode/src/commands/codewiki/tests.rs:578-592] [crates/gcode/src/commands/codewiki/tests.rs:595-628] [crates/gcode/src/commands/codewiki/tests.rs:631-680] [crates/gcode/src/commands/codewiki/tests.rs:683-776] [crates/gcode/src/commands/codewiki/tests.rs:779-802] [crates/gcode/src/commands/codewiki/tests.rs:805-809] [crates/gcode/src/commands/codewiki/tests.rs:813-827] [crates/gcode/src/commands/codewiki/tests.rs:831-845] [crates/gcode/src/commands/codewiki/tests.rs:847-855] [crates/gcode/src/commands/codewiki/tests.rs:857-859] [crates/gcode/src/commands/codewiki/tests.rs:861-889] [crates/gcode/src/commands/codewiki/tests.rs:891-919] [crates/gcode/src/commands/codewiki/text.rs:6-11] [crates/gcode/src/commands/codewiki/text.rs:14-17] [crates/gcode/src/commands/codewiki/text.rs:19-50] [crates/gcode/src/commands/codewiki/text.rs:52-68] [crates/gcode/src/commands/codewiki/text.rs:70-78] [crates/gcode/src/commands/codewiki/text.rs:80-83] [crates/gcode/src/commands/codewiki/text.rs:85-100] [crates/gcode/src/commands/codewiki/text.rs:102-111] [crates/gcode/src/commands/codewiki/text.rs:113-125] [crates/gcode/src/commands/codewiki/text.rs:127-133] [crates/gcode/src/commands/codewiki/text.rs:135-137] [crates/gcode/src/commands/codewiki/text.rs:139-148] [crates/gcode/src/commands/codewiki/text.rs:150-159] [crates/gcode/src/commands/codewiki/text.rs:161-172] [crates/gcode/src/commands/codewiki/text.rs:174-200] [crates/gcode/src/commands/codewiki/text.rs:202-219] [crates/gcode/src/commands/codewiki/text.rs:221-234] [crates/gcode/src/commands/codewiki/text.rs:236-277]

