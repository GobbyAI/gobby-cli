---
title: Architecture Overview
type: code_architecture
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
  ranges:
  - 4-99
  - 101-116
  - 118-168
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
  ranges:
  - 5-101
  - 104-113
  - 115-136
  - 138-154
  - 156-161
- file: crates/gcode/src/commands/codewiki/build_parts/file.rs
  ranges:
  - 4-74
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
  ranges:
  - 5-131
  - 133-157
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
  ranges:
  - 4-93
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
  ranges:
  - 7-53
  - 55-110
  - 112-201
  - 203-209
  - 211-213
  - 215-220
- file: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
  ranges:
  - 6-84
  - 86-99
  - 101-134
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
  - 11-17
  - 19-69
  - 71-79
  - 81-99
  - 101-121
  - 123-130
  - 132-135
  - 137-144
  - 146-149
  - 151-172
  - 174-207
  - 210-240
  - 243-250
  - 252-262
- file: crates/gcode/src/commands/codewiki/mod.rs
  ranges:
  - 79-84
  - 87-91
  - 93-115
  - 94-103
  - 105-114
  - 118-121
  - 124-127
  - 129-150
  - 130-135
  - 137-142
  - 144-149
  - 153-157
  - 160-167
  - 170-176
  - 179-189
  - 192-197
  - 200-204
  - 207-212
  - 215-219
  - 222-227
  - 230-236
  - 239-245
  - 248-255
  - 258-262
  - 265-269
  - 272-276
  - 279-291
  - 294-299
  - 302-304
  - 307-314
  - 317-320
  - 323-329
  - '331'
  - 333-353
  - 334-340
  - 342-348
  - 350-352
  - 355-449
  - 451-456
  - 458-463
  - 465-476
  - 478-485
  - 487-590
- file: crates/gcode/src/commands/codewiki/ownership.rs
  ranges:
  - 13-16
  - 18-25
  - 19-24
  - 28-31
  - 34-37
  - 40-45
  - 48-50
  - 53-56
  - 59-63
  - 66-69
  - 71-116
  - 118-128
  - 130-148
  - 150-169
  - 171-206
  - 208-253
  - 255-257
  - 259-290
  - 292-313
  - 315-347
  - 317-331
  - 349-351
  - 353-379
  - 381-393
  - 395-405
  - 407-429
  - 431-437
  - 439-461
  - 472-499
  - 502-522
  - 525-546
  - 549-572
  - 575-594
  - 596-601
  - 603-622
  - 624-633
  - 635-651
  - 653-661
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
  - 11-33
  - 35-56
  - 58-69
  - 71-91
  - 93-104
  - 106-135
  - 138-146
  - 149-152
- file: crates/gcode/src/commands/codewiki/render.rs
  ranges:
  - 5-33
  - 35-67
  - 69-83
  - 85-108
  - 110-198
  - 200-229
  - 231-281
  - 283-296
  - 298-308
  - 310-325
  - 327-375
  - 377-405
  - 407-433
  - 435-471
  - 473-501
  - 503-545
  - 547-606
  - 608-646
- file: crates/gcode/src/commands/codewiki/tests.rs
  ranges:
  - 11-45
  - 48-110
  - 113-120
  - 123-196
  - 199-212
  - 215-217
  - 220-225
  - 228-240
  - 243-265
  - 268-295
  - 298-307
  - 310-317
  - 320-404
  - 407-475
  - 478-492
  - 495-525
  - 528-549
  - 552-590
  - 593-605
  - 608-624
  - 627-644
  - 647-661
  - 664-697
  - 700-750
  - 753-854
  - 857-880
  - 883-887
  - 891-905
  - 909-923
  - 925-933
  - 935-937
  - 939-967
  - 969-997
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 6-18
  - 21-24
  - 26-57
  - 59-75
  - 77-85
  - 87-90
  - 92-107
  - 109-118
  - 120-132
  - 134-140
  - 142-144
  - 146-155
  - 157-169
  - 171-177
  - 179-185
  - 187-197
  - 199-208
  - 210-223
  - 225-251
  - 253-270
  - 272-285
  - 287-289
  - 293-344
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# Architecture Overview

## Subsystems

- [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]] - `crates/gcode/src/commands/codewiki` contains 11 direct files and 1 child module.
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:4-99] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:101-116] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:118-168] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-136] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:138-154] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:156-161]
[crates/gcode/src/commands/codewiki/build_parts/file.rs:4-74] [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-131] [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:133-157] [crates/gcode/src/commands/codewiki/build_parts/modules.rs:4-93]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-53] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:55-110] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:112-201] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:215-220] [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84] [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134] [crates/gcode/src/commands/codewiki/cluster.rs:3-54] [crates/gcode/src/commands/codewiki/cluster.rs:56-80] [crates/gcode/src/commands/codewiki/cluster.rs:89-130]
[crates/gcode/src/commands/codewiki/cluster.rs:132-156] [crates/gcode/src/commands/codewiki/cluster.rs:158-168] [crates/gcode/src/commands/codewiki/cluster.rs:170-178] [crates/gcode/src/commands/codewiki/cluster.rs:180-196]
[crates/gcode/src/commands/codewiki/cluster.rs:198-206] [crates/gcode/src/commands/codewiki/cluster.rs:208-226] [crates/gcode/src/commands/codewiki/cluster.rs:228-233] [crates/gcode/src/commands/codewiki/graph.rs:4-124]
[crates/gcode/src/commands/codewiki/graph.rs:34-49] [crates/gcode/src/commands/codewiki/graph.rs:126-145] [crates/gcode/src/commands/codewiki/graph.rs:147-165] [crates/gcode/src/commands/codewiki/io.rs:3-9]
[crates/gcode/src/commands/codewiki/io.rs:11-17] [crates/gcode/src/commands/codewiki/io.rs:19-69] [crates/gcode/src/commands/codewiki/io.rs:71-79] [crates/gcode/src/commands/codewiki/io.rs:81-99]
[crates/gcode/src/commands/codewiki/io.rs:101-121] [crates/gcode/src/commands/codewiki/io.rs:123-130] [crates/gcode/src/commands/codewiki/io.rs:132-135] [crates/gcode/src/commands/codewiki/io.rs:137-144]
[crates/gcode/src/commands/codewiki/io.rs:146-149] [crates/gcode/src/commands/codewiki/io.rs:151-172] [crates/gcode/src/commands/codewiki/io.rs:174-207] [crates/gcode/src/commands/codewiki/io.rs:210-240]
[crates/gcode/src/commands/codewiki/io.rs:243-250] [crates/gcode/src/commands/codewiki/io.rs:252-262] [crates/gcode/src/commands/codewiki/mod.rs:79-84] [crates/gcode/src/commands/codewiki/mod.rs:87-91]
[crates/gcode/src/commands/codewiki/mod.rs:93-115] [crates/gcode/src/commands/codewiki/mod.rs:94-103] [crates/gcode/src/commands/codewiki/mod.rs:105-114] [crates/gcode/src/commands/codewiki/mod.rs:118-121]
[crates/gcode/src/commands/codewiki/mod.rs:124-127] [crates/gcode/src/commands/codewiki/mod.rs:129-150] [crates/gcode/src/commands/codewiki/mod.rs:130-135] [crates/gcode/src/commands/codewiki/mod.rs:137-142]
[crates/gcode/src/commands/codewiki/mod.rs:144-149] [crates/gcode/src/commands/codewiki/mod.rs:153-157] [crates/gcode/src/commands/codewiki/mod.rs:160-167] [crates/gcode/src/commands/codewiki/mod.rs:170-176]
[crates/gcode/src/commands/codewiki/mod.rs:179-189] [crates/gcode/src/commands/codewiki/mod.rs:192-197] [crates/gcode/src/commands/codewiki/mod.rs:200-204] [crates/gcode/src/commands/codewiki/mod.rs:207-212]
[crates/gcode/src/commands/codewiki/mod.rs:215-219] [crates/gcode/src/commands/codewiki/mod.rs:222-227] [crates/gcode/src/commands/codewiki/mod.rs:230-236] [crates/gcode/src/commands/codewiki/mod.rs:239-245]
[crates/gcode/src/commands/codewiki/mod.rs:248-255] [crates/gcode/src/commands/codewiki/mod.rs:258-262] [crates/gcode/src/commands/codewiki/mod.rs:265-269] [crates/gcode/src/commands/codewiki/mod.rs:272-276]
[crates/gcode/src/commands/codewiki/mod.rs:279-291] [crates/gcode/src/commands/codewiki/mod.rs:294-299] [crates/gcode/src/commands/codewiki/mod.rs:302-304] [crates/gcode/src/commands/codewiki/mod.rs:307-314]
[crates/gcode/src/commands/codewiki/mod.rs:317-320] [crates/gcode/src/commands/codewiki/mod.rs:323-329] [crates/gcode/src/commands/codewiki/mod.rs:331] [crates/gcode/src/commands/codewiki/mod.rs:333-353]
[crates/gcode/src/commands/codewiki/mod.rs:334-340] [crates/gcode/src/commands/codewiki/mod.rs:342-348] [crates/gcode/src/commands/codewiki/mod.rs:350-352] [crates/gcode/src/commands/codewiki/mod.rs:355-449]
[crates/gcode/src/commands/codewiki/mod.rs:451-456] [crates/gcode/src/commands/codewiki/mod.rs:458-463] [crates/gcode/src/commands/codewiki/mod.rs:465-476] [crates/gcode/src/commands/codewiki/mod.rs:478-485]
[crates/gcode/src/commands/codewiki/mod.rs:487-590] [crates/gcode/src/commands/codewiki/ownership.rs:13-16] [crates/gcode/src/commands/codewiki/ownership.rs:18-25] [crates/gcode/src/commands/codewiki/ownership.rs:19-24]
[crates/gcode/src/commands/codewiki/ownership.rs:28-31] [crates/gcode/src/commands/codewiki/ownership.rs:34-37] [crates/gcode/src/commands/codewiki/ownership.rs:40-45] [crates/gcode/src/commands/codewiki/ownership.rs:48-50]
[crates/gcode/src/commands/codewiki/ownership.rs:53-56] [crates/gcode/src/commands/codewiki/ownership.rs:59-63] [crates/gcode/src/commands/codewiki/ownership.rs:66-69] [crates/gcode/src/commands/codewiki/ownership.rs:71-116]
[crates/gcode/src/commands/codewiki/ownership.rs:118-128] [crates/gcode/src/commands/codewiki/ownership.rs:130-148] [crates/gcode/src/commands/codewiki/ownership.rs:150-169] [crates/gcode/src/commands/codewiki/ownership.rs:171-206]
[crates/gcode/src/commands/codewiki/ownership.rs:208-253] [crates/gcode/src/commands/codewiki/ownership.rs:255-257] [crates/gcode/src/commands/codewiki/ownership.rs:259-290] [crates/gcode/src/commands/codewiki/ownership.rs:292-313]
[crates/gcode/src/commands/codewiki/ownership.rs:315-347] [crates/gcode/src/commands/codewiki/ownership.rs:317-331] [crates/gcode/src/commands/codewiki/ownership.rs:349-351] [crates/gcode/src/commands/codewiki/ownership.rs:353-379]
[crates/gcode/src/commands/codewiki/ownership.rs:381-393] [crates/gcode/src/commands/codewiki/ownership.rs:395-405] [crates/gcode/src/commands/codewiki/ownership.rs:407-429] [crates/gcode/src/commands/codewiki/ownership.rs:431-437]
[crates/gcode/src/commands/codewiki/ownership.rs:439-461] [crates/gcode/src/commands/codewiki/ownership.rs:472-499] [crates/gcode/src/commands/codewiki/ownership.rs:502-522] [crates/gcode/src/commands/codewiki/ownership.rs:525-546]
[crates/gcode/src/commands/codewiki/ownership.rs:549-572] [crates/gcode/src/commands/codewiki/ownership.rs:575-594] [crates/gcode/src/commands/codewiki/ownership.rs:596-601] [crates/gcode/src/commands/codewiki/ownership.rs:603-622]
[crates/gcode/src/commands/codewiki/ownership.rs:624-633] [crates/gcode/src/commands/codewiki/ownership.rs:635-651] [crates/gcode/src/commands/codewiki/ownership.rs:653-661] [crates/gcode/src/commands/codewiki/paths.rs:3-14]
[crates/gcode/src/commands/codewiki/paths.rs:16-28] [crates/gcode/src/commands/codewiki/paths.rs:30-32] [crates/gcode/src/commands/codewiki/paths.rs:34-41] [crates/gcode/src/commands/codewiki/paths.rs:43-88]
[crates/gcode/src/commands/codewiki/paths.rs:93-101] [crates/gcode/src/commands/codewiki/paths.rs:103-109] [crates/gcode/src/commands/codewiki/paths.rs:111-119] [crates/gcode/src/commands/codewiki/paths.rs:121-123]
[crates/gcode/src/commands/codewiki/paths.rs:125-127] [crates/gcode/src/commands/codewiki/paths.rs:129-137] [crates/gcode/src/commands/codewiki/paths.rs:139-141] [crates/gcode/src/commands/codewiki/paths.rs:143-145]
[crates/gcode/src/commands/codewiki/paths.rs:147-149] [crates/gcode/src/commands/codewiki/paths.rs:151-153] [crates/gcode/src/commands/codewiki/paths.rs:155-157] [crates/gcode/src/commands/codewiki/prompts.rs:11-33]
[crates/gcode/src/commands/codewiki/prompts.rs:35-56] [crates/gcode/src/commands/codewiki/prompts.rs:58-69] [crates/gcode/src/commands/codewiki/prompts.rs:71-91] [crates/gcode/src/commands/codewiki/prompts.rs:93-104]
[crates/gcode/src/commands/codewiki/prompts.rs:106-135] [crates/gcode/src/commands/codewiki/prompts.rs:138-146] [crates/gcode/src/commands/codewiki/prompts.rs:149-152] [crates/gcode/src/commands/codewiki/render.rs:5-33]
[crates/gcode/src/commands/codewiki/render.rs:35-67] [crates/gcode/src/commands/codewiki/render.rs:69-83] [crates/gcode/src/commands/codewiki/render.rs:85-108] [crates/gcode/src/commands/codewiki/render.rs:110-198]
[crates/gcode/src/commands/codewiki/render.rs:200-229] [crates/gcode/src/commands/codewiki/render.rs:231-281] [crates/gcode/src/commands/codewiki/render.rs:283-296] [crates/gcode/src/commands/codewiki/render.rs:298-308]
[crates/gcode/src/commands/codewiki/render.rs:310-325] [crates/gcode/src/commands/codewiki/render.rs:327-375] [crates/gcode/src/commands/codewiki/render.rs:377-405] [crates/gcode/src/commands/codewiki/render.rs:407-433]
[crates/gcode/src/commands/codewiki/render.rs:435-471] [crates/gcode/src/commands/codewiki/render.rs:473-501] [crates/gcode/src/commands/codewiki/render.rs:503-545] [crates/gcode/src/commands/codewiki/render.rs:547-606]
[crates/gcode/src/commands/codewiki/render.rs:608-646] [crates/gcode/src/commands/codewiki/tests.rs:11-45] [crates/gcode/src/commands/codewiki/tests.rs:48-110] [crates/gcode/src/commands/codewiki/tests.rs:113-120]
[crates/gcode/src/commands/codewiki/tests.rs:123-196] [crates/gcode/src/commands/codewiki/tests.rs:199-212] [crates/gcode/src/commands/codewiki/tests.rs:215-217] [crates/gcode/src/commands/codewiki/tests.rs:220-225]
[crates/gcode/src/commands/codewiki/tests.rs:228-240] [crates/gcode/src/commands/codewiki/tests.rs:243-265] [crates/gcode/src/commands/codewiki/tests.rs:268-295] [crates/gcode/src/commands/codewiki/tests.rs:298-307]
[crates/gcode/src/commands/codewiki/tests.rs:310-317] [crates/gcode/src/commands/codewiki/tests.rs:320-404] [crates/gcode/src/commands/codewiki/tests.rs:407-475] [crates/gcode/src/commands/codewiki/tests.rs:478-492]
[crates/gcode/src/commands/codewiki/tests.rs:495-525] [crates/gcode/src/commands/codewiki/tests.rs:528-549] [crates/gcode/src/commands/codewiki/tests.rs:552-590] [crates/gcode/src/commands/codewiki/tests.rs:593-605]
[crates/gcode/src/commands/codewiki/tests.rs:608-624] [crates/gcode/src/commands/codewiki/tests.rs:627-644] [crates/gcode/src/commands/codewiki/tests.rs:647-661] [crates/gcode/src/commands/codewiki/tests.rs:664-697]
[crates/gcode/src/commands/codewiki/tests.rs:700-750] [crates/gcode/src/commands/codewiki/tests.rs:753-854] [crates/gcode/src/commands/codewiki/tests.rs:857-880] [crates/gcode/src/commands/codewiki/tests.rs:883-887]
[crates/gcode/src/commands/codewiki/tests.rs:891-905] [crates/gcode/src/commands/codewiki/tests.rs:909-923] [crates/gcode/src/commands/codewiki/tests.rs:925-933] [crates/gcode/src/commands/codewiki/tests.rs:935-937]
[crates/gcode/src/commands/codewiki/tests.rs:939-967] [crates/gcode/src/commands/codewiki/tests.rs:969-997] [crates/gcode/src/commands/codewiki/text.rs:6-18] [crates/gcode/src/commands/codewiki/text.rs:21-24]
[crates/gcode/src/commands/codewiki/text.rs:26-57] [crates/gcode/src/commands/codewiki/text.rs:59-75] [crates/gcode/src/commands/codewiki/text.rs:77-85] [crates/gcode/src/commands/codewiki/text.rs:87-90]
[crates/gcode/src/commands/codewiki/text.rs:92-107] [crates/gcode/src/commands/codewiki/text.rs:109-118] [crates/gcode/src/commands/codewiki/text.rs:120-132] [crates/gcode/src/commands/codewiki/text.rs:134-140]
[crates/gcode/src/commands/codewiki/text.rs:142-144] [crates/gcode/src/commands/codewiki/text.rs:146-155] [crates/gcode/src/commands/codewiki/text.rs:157-169] [crates/gcode/src/commands/codewiki/text.rs:171-177]
[crates/gcode/src/commands/codewiki/text.rs:179-185] [crates/gcode/src/commands/codewiki/text.rs:187-197] [crates/gcode/src/commands/codewiki/text.rs:199-208] [crates/gcode/src/commands/codewiki/text.rs:210-223]
[crates/gcode/src/commands/codewiki/text.rs:225-251] [crates/gcode/src/commands/codewiki/text.rs:253-270] [crates/gcode/src/commands/codewiki/text.rs:272-285] [crates/gcode/src/commands/codewiki/text.rs:287-289]
[crates/gcode/src/commands/codewiki/text.rs:293-344]
- [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]] - `crates/gcode/src/commands/codewiki/build_parts` contains 7 direct files and 0 child modules.
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:4-99] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:101-116] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:118-168] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-136] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:138-154] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:156-161]
[crates/gcode/src/commands/codewiki/build_parts/file.rs:4-74] [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-131] [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:133-157] [crates/gcode/src/commands/codewiki/build_parts/modules.rs:4-93]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-53] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:55-110] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:112-201] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:203-209]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:211-213] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:215-220] [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84] [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

