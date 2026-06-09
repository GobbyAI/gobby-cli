---
title: Architecture Overview
type: code_architecture
source:
- file: crates/gcode/src/commands/codewiki/build.rs
  ranges:
  - 5-83
  - 85-181
  - 183-253
  - 255-268
  - 270-303
  - 306-315
  - 317-338
  - 340-356
  - 358-363
  - 365-454
  - 456-551
  - 553-599
  - 601-727
  - 729-753
  - 755-810
  - 812-901
  - 903-918
  - 920-970
  - 972-978
  - 980-982
  - 984-989
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
  - 78-83
  - 86-90
  - 92-114
  - 93-102
  - 104-113
  - 117-120
  - 123-126
  - 128-149
  - 129-134
  - 136-141
  - 143-148
  - 152-156
  - 159-166
  - 169-175
  - 178-188
  - 191-196
  - 199-203
  - 205-210
  - 212-216
  - 218-223
  - 226-232
  - 235-241
  - 244-251
  - 254-258
  - 261-265
  - 268-272
  - 275-287
  - 290-295
  - 298-300
  - 303-310
  - 313-316
  - 319-325
  - '327'
  - 329-349
  - 330-336
  - 338-344
  - 346-348
  - 351-445
  - 447-452
  - 454-459
  - 461-472
  - 474-481
  - 483-586
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
  - 171-196
  - 198-243
  - 245-247
  - 249-280
  - 282-303
  - 305-339
  - 307-322
  - 341-343
  - 345-371
  - 373-385
  - 387-397
  - 399-421
  - 423-429
  - 431-453
  - 464-491
  - 494-514
  - 517-538
  - 541-564
  - 567-586
  - 588-593
  - 595-614
  - 616-625
  - 627-643
  - 645-653
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
  - 58-91
  - 93-113
  - 115-148
  - 151-159
  - 162-165
- file: crates/gcode/src/commands/codewiki/render.rs
  ranges:
  - 5-33
  - 35-57
  - 59-82
  - 84-172
  - 174-203
  - 205-255
  - 257-270
  - 272-282
  - 284-299
  - 301-349
  - 351-380
  - 382-408
  - 410-452
  - 454-482
  - 484-526
  - 528-587
  - 589-627
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
  - 6-19
  - 22-25
  - 27-58
  - 60-76
  - 78-86
  - 88-91
  - 93-108
  - 110-119
  - 121-133
  - 135-141
  - 143-145
  - 147-156
  - 158-170
  - 172-185
  - 187-213
  - 215-232
  - 234-247
  - 249-251
  - 253-305
provenance:
- file: crates/gcode/src/commands/codewiki/build.rs
  ranges:
  - 5-83
  - 85-181
  - 183-253
  - 255-268
  - 270-303
  - 306-315
  - 317-338
  - 340-356
  - 358-363
  - 365-454
  - 456-551
  - 553-599
  - 601-727
  - 729-753
  - 755-810
  - 812-901
  - 903-918
  - 920-970
  - 972-978
  - 980-982
  - 984-989
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
  - 78-83
  - 86-90
  - 92-114
  - 93-102
  - 104-113
  - 117-120
  - 123-126
  - 128-149
  - 129-134
  - 136-141
  - 143-148
  - 152-156
  - 159-166
  - 169-175
  - 178-188
  - 191-196
  - 199-203
  - 205-210
  - 212-216
  - 218-223
  - 226-232
  - 235-241
  - 244-251
  - 254-258
  - 261-265
  - 268-272
  - 275-287
  - 290-295
  - 298-300
  - 303-310
  - 313-316
  - 319-325
  - '327'
  - 329-349
  - 330-336
  - 338-344
  - 346-348
  - 351-445
  - 447-452
  - 454-459
  - 461-472
  - 474-481
  - 483-586
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
  - 171-196
  - 198-243
  - 245-247
  - 249-280
  - 282-303
  - 305-339
  - 307-322
  - 341-343
  - 345-371
  - 373-385
  - 387-397
  - 399-421
  - 423-429
  - 431-453
  - 464-491
  - 494-514
  - 517-538
  - 541-564
  - 567-586
  - 588-593
  - 595-614
  - 616-625
  - 627-643
  - 645-653
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
  - 58-91
  - 93-113
  - 115-148
  - 151-159
  - 162-165
- file: crates/gcode/src/commands/codewiki/render.rs
  ranges:
  - 5-33
  - 35-57
  - 59-82
  - 84-172
  - 174-203
  - 205-255
  - 257-270
  - 272-282
  - 284-299
  - 301-349
  - 351-380
  - 382-408
  - 410-452
  - 454-482
  - 484-526
  - 528-587
  - 589-627
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
  - 6-19
  - 22-25
  - 27-58
  - 60-76
  - 78-86
  - 88-91
  - 93-108
  - 110-119
  - 121-133
  - 135-141
  - 143-145
  - 147-156
  - 158-170
  - 172-185
  - 187-213
  - 215-232
  - 234-247
  - 249-251
  - 253-305
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# Architecture Overview

## Subsystems

- [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]] - `crates/gcode/src/commands/codewiki` contains 11 direct files and 0 child modules.
[crates/gcode/src/commands/codewiki/build.rs:5-83] [crates/gcode/src/commands/codewiki/build.rs:85-181] [crates/gcode/src/commands/codewiki/build.rs:183-253] [crates/gcode/src/commands/codewiki/build.rs:255-268]
[crates/gcode/src/commands/codewiki/build.rs:270-303] [crates/gcode/src/commands/codewiki/build.rs:306-315] [crates/gcode/src/commands/codewiki/build.rs:317-338] [crates/gcode/src/commands/codewiki/build.rs:340-356]
[crates/gcode/src/commands/codewiki/build.rs:358-363] [crates/gcode/src/commands/codewiki/build.rs:365-454] [crates/gcode/src/commands/codewiki/build.rs:456-551] [crates/gcode/src/commands/codewiki/build.rs:553-599]
[crates/gcode/src/commands/codewiki/build.rs:601-727] [crates/gcode/src/commands/codewiki/build.rs:729-753] [crates/gcode/src/commands/codewiki/build.rs:755-810] [crates/gcode/src/commands/codewiki/build.rs:812-901]
[crates/gcode/src/commands/codewiki/build.rs:903-918] [crates/gcode/src/commands/codewiki/build.rs:920-970] [crates/gcode/src/commands/codewiki/build.rs:972-978] [crates/gcode/src/commands/codewiki/build.rs:980-982]
[crates/gcode/src/commands/codewiki/build.rs:984-989] [crates/gcode/src/commands/codewiki/cluster.rs:3-54] [crates/gcode/src/commands/codewiki/cluster.rs:56-80] [crates/gcode/src/commands/codewiki/cluster.rs:89-130]
[crates/gcode/src/commands/codewiki/cluster.rs:132-156] [crates/gcode/src/commands/codewiki/cluster.rs:158-168] [crates/gcode/src/commands/codewiki/cluster.rs:170-178] [crates/gcode/src/commands/codewiki/cluster.rs:180-196]
[crates/gcode/src/commands/codewiki/cluster.rs:198-206] [crates/gcode/src/commands/codewiki/cluster.rs:208-226] [crates/gcode/src/commands/codewiki/cluster.rs:228-233] [crates/gcode/src/commands/codewiki/graph.rs:4-124]
[crates/gcode/src/commands/codewiki/graph.rs:34-49] [crates/gcode/src/commands/codewiki/graph.rs:126-145] [crates/gcode/src/commands/codewiki/graph.rs:147-165] [crates/gcode/src/commands/codewiki/io.rs:3-9]
[crates/gcode/src/commands/codewiki/io.rs:11-17] [crates/gcode/src/commands/codewiki/io.rs:19-69] [crates/gcode/src/commands/codewiki/io.rs:71-79] [crates/gcode/src/commands/codewiki/io.rs:81-99]
[crates/gcode/src/commands/codewiki/io.rs:101-121] [crates/gcode/src/commands/codewiki/io.rs:123-130] [crates/gcode/src/commands/codewiki/io.rs:132-135] [crates/gcode/src/commands/codewiki/io.rs:137-144]
[crates/gcode/src/commands/codewiki/io.rs:146-149] [crates/gcode/src/commands/codewiki/io.rs:151-172] [crates/gcode/src/commands/codewiki/io.rs:174-207] [crates/gcode/src/commands/codewiki/io.rs:210-240]
[crates/gcode/src/commands/codewiki/io.rs:243-250] [crates/gcode/src/commands/codewiki/io.rs:252-262] [crates/gcode/src/commands/codewiki/mod.rs:78-83] [crates/gcode/src/commands/codewiki/mod.rs:86-90]
[crates/gcode/src/commands/codewiki/mod.rs:92-114] [crates/gcode/src/commands/codewiki/mod.rs:93-102] [crates/gcode/src/commands/codewiki/mod.rs:104-113] [crates/gcode/src/commands/codewiki/mod.rs:117-120]
[crates/gcode/src/commands/codewiki/mod.rs:123-126] [crates/gcode/src/commands/codewiki/mod.rs:128-149] [crates/gcode/src/commands/codewiki/mod.rs:129-134] [crates/gcode/src/commands/codewiki/mod.rs:136-141]
[crates/gcode/src/commands/codewiki/mod.rs:143-148] [crates/gcode/src/commands/codewiki/mod.rs:152-156] [crates/gcode/src/commands/codewiki/mod.rs:159-166] [crates/gcode/src/commands/codewiki/mod.rs:169-175]
[crates/gcode/src/commands/codewiki/mod.rs:178-188] [crates/gcode/src/commands/codewiki/mod.rs:191-196] [crates/gcode/src/commands/codewiki/mod.rs:199-203] [crates/gcode/src/commands/codewiki/mod.rs:205-210]
[crates/gcode/src/commands/codewiki/mod.rs:212-216] [crates/gcode/src/commands/codewiki/mod.rs:218-223] [crates/gcode/src/commands/codewiki/mod.rs:226-232] [crates/gcode/src/commands/codewiki/mod.rs:235-241]
[crates/gcode/src/commands/codewiki/mod.rs:244-251] [crates/gcode/src/commands/codewiki/mod.rs:254-258] [crates/gcode/src/commands/codewiki/mod.rs:261-265] [crates/gcode/src/commands/codewiki/mod.rs:268-272]
[crates/gcode/src/commands/codewiki/mod.rs:275-287] [crates/gcode/src/commands/codewiki/mod.rs:290-295] [crates/gcode/src/commands/codewiki/mod.rs:298-300] [crates/gcode/src/commands/codewiki/mod.rs:303-310]
[crates/gcode/src/commands/codewiki/mod.rs:313-316] [crates/gcode/src/commands/codewiki/mod.rs:319-325] [crates/gcode/src/commands/codewiki/mod.rs:327] [crates/gcode/src/commands/codewiki/mod.rs:329-349]
[crates/gcode/src/commands/codewiki/mod.rs:330-336] [crates/gcode/src/commands/codewiki/mod.rs:338-344] [crates/gcode/src/commands/codewiki/mod.rs:346-348] [crates/gcode/src/commands/codewiki/mod.rs:351-445]
[crates/gcode/src/commands/codewiki/mod.rs:447-452] [crates/gcode/src/commands/codewiki/mod.rs:454-459] [crates/gcode/src/commands/codewiki/mod.rs:461-472] [crates/gcode/src/commands/codewiki/mod.rs:474-481]
[crates/gcode/src/commands/codewiki/mod.rs:483-586] [crates/gcode/src/commands/codewiki/ownership.rs:13-16] [crates/gcode/src/commands/codewiki/ownership.rs:18-25] [crates/gcode/src/commands/codewiki/ownership.rs:19-24]
[crates/gcode/src/commands/codewiki/ownership.rs:28-31] [crates/gcode/src/commands/codewiki/ownership.rs:34-37] [crates/gcode/src/commands/codewiki/ownership.rs:40-45] [crates/gcode/src/commands/codewiki/ownership.rs:48-50]
[crates/gcode/src/commands/codewiki/ownership.rs:53-56] [crates/gcode/src/commands/codewiki/ownership.rs:59-63] [crates/gcode/src/commands/codewiki/ownership.rs:66-69] [crates/gcode/src/commands/codewiki/ownership.rs:71-116]
[crates/gcode/src/commands/codewiki/ownership.rs:118-128] [crates/gcode/src/commands/codewiki/ownership.rs:130-148] [crates/gcode/src/commands/codewiki/ownership.rs:150-169] [crates/gcode/src/commands/codewiki/ownership.rs:171-196]
[crates/gcode/src/commands/codewiki/ownership.rs:198-243] [crates/gcode/src/commands/codewiki/ownership.rs:245-247] [crates/gcode/src/commands/codewiki/ownership.rs:249-280] [crates/gcode/src/commands/codewiki/ownership.rs:282-303]
[crates/gcode/src/commands/codewiki/ownership.rs:305-339] [crates/gcode/src/commands/codewiki/ownership.rs:307-322] [crates/gcode/src/commands/codewiki/ownership.rs:341-343] [crates/gcode/src/commands/codewiki/ownership.rs:345-371]
[crates/gcode/src/commands/codewiki/ownership.rs:373-385] [crates/gcode/src/commands/codewiki/ownership.rs:387-397] [crates/gcode/src/commands/codewiki/ownership.rs:399-421] [crates/gcode/src/commands/codewiki/ownership.rs:423-429]
[crates/gcode/src/commands/codewiki/ownership.rs:431-453] [crates/gcode/src/commands/codewiki/ownership.rs:464-491] [crates/gcode/src/commands/codewiki/ownership.rs:494-514] [crates/gcode/src/commands/codewiki/ownership.rs:517-538]
[crates/gcode/src/commands/codewiki/ownership.rs:541-564] [crates/gcode/src/commands/codewiki/ownership.rs:567-586] [crates/gcode/src/commands/codewiki/ownership.rs:588-593] [crates/gcode/src/commands/codewiki/ownership.rs:595-614]
[crates/gcode/src/commands/codewiki/ownership.rs:616-625] [crates/gcode/src/commands/codewiki/ownership.rs:627-643] [crates/gcode/src/commands/codewiki/ownership.rs:645-653] [crates/gcode/src/commands/codewiki/paths.rs:3-14]
[crates/gcode/src/commands/codewiki/paths.rs:16-28] [crates/gcode/src/commands/codewiki/paths.rs:30-32] [crates/gcode/src/commands/codewiki/paths.rs:34-41] [crates/gcode/src/commands/codewiki/paths.rs:43-88]
[crates/gcode/src/commands/codewiki/paths.rs:93-101] [crates/gcode/src/commands/codewiki/paths.rs:103-109] [crates/gcode/src/commands/codewiki/paths.rs:111-119] [crates/gcode/src/commands/codewiki/paths.rs:121-123]
[crates/gcode/src/commands/codewiki/paths.rs:125-127] [crates/gcode/src/commands/codewiki/paths.rs:129-137] [crates/gcode/src/commands/codewiki/paths.rs:139-141] [crates/gcode/src/commands/codewiki/paths.rs:143-145]
[crates/gcode/src/commands/codewiki/paths.rs:147-149] [crates/gcode/src/commands/codewiki/paths.rs:151-153] [crates/gcode/src/commands/codewiki/paths.rs:155-157] [crates/gcode/src/commands/codewiki/prompts.rs:11-33]
[crates/gcode/src/commands/codewiki/prompts.rs:35-56] [crates/gcode/src/commands/codewiki/prompts.rs:58-91] [crates/gcode/src/commands/codewiki/prompts.rs:93-113] [crates/gcode/src/commands/codewiki/prompts.rs:115-148]
[crates/gcode/src/commands/codewiki/prompts.rs:151-159] [crates/gcode/src/commands/codewiki/prompts.rs:162-165] [crates/gcode/src/commands/codewiki/render.rs:5-33] [crates/gcode/src/commands/codewiki/render.rs:35-57]
[crates/gcode/src/commands/codewiki/render.rs:59-82] [crates/gcode/src/commands/codewiki/render.rs:84-172] [crates/gcode/src/commands/codewiki/render.rs:174-203] [crates/gcode/src/commands/codewiki/render.rs:205-255]
[crates/gcode/src/commands/codewiki/render.rs:257-270] [crates/gcode/src/commands/codewiki/render.rs:272-282] [crates/gcode/src/commands/codewiki/render.rs:284-299] [crates/gcode/src/commands/codewiki/render.rs:301-349]
[crates/gcode/src/commands/codewiki/render.rs:351-380] [crates/gcode/src/commands/codewiki/render.rs:382-408] [crates/gcode/src/commands/codewiki/render.rs:410-452] [crates/gcode/src/commands/codewiki/render.rs:454-482]
[crates/gcode/src/commands/codewiki/render.rs:484-526] [crates/gcode/src/commands/codewiki/render.rs:528-587] [crates/gcode/src/commands/codewiki/render.rs:589-627] [crates/gcode/src/commands/codewiki/tests.rs:11-45]
[crates/gcode/src/commands/codewiki/tests.rs:48-110] [crates/gcode/src/commands/codewiki/tests.rs:113-120] [crates/gcode/src/commands/codewiki/tests.rs:123-196] [crates/gcode/src/commands/codewiki/tests.rs:199-212]
[crates/gcode/src/commands/codewiki/tests.rs:215-217] [crates/gcode/src/commands/codewiki/tests.rs:220-225] [crates/gcode/src/commands/codewiki/tests.rs:228-240] [crates/gcode/src/commands/codewiki/tests.rs:243-265]
[crates/gcode/src/commands/codewiki/tests.rs:268-295] [crates/gcode/src/commands/codewiki/tests.rs:298-307] [crates/gcode/src/commands/codewiki/tests.rs:310-317] [crates/gcode/src/commands/codewiki/tests.rs:320-404]
[crates/gcode/src/commands/codewiki/tests.rs:407-475] [crates/gcode/src/commands/codewiki/tests.rs:478-492] [crates/gcode/src/commands/codewiki/tests.rs:495-525] [crates/gcode/src/commands/codewiki/tests.rs:528-549]
[crates/gcode/src/commands/codewiki/tests.rs:552-590] [crates/gcode/src/commands/codewiki/tests.rs:593-605] [crates/gcode/src/commands/codewiki/tests.rs:608-624] [crates/gcode/src/commands/codewiki/tests.rs:627-644]
[crates/gcode/src/commands/codewiki/tests.rs:647-661] [crates/gcode/src/commands/codewiki/tests.rs:664-697] [crates/gcode/src/commands/codewiki/tests.rs:700-750] [crates/gcode/src/commands/codewiki/tests.rs:753-854]
[crates/gcode/src/commands/codewiki/tests.rs:857-880] [crates/gcode/src/commands/codewiki/tests.rs:883-887] [crates/gcode/src/commands/codewiki/tests.rs:891-905] [crates/gcode/src/commands/codewiki/tests.rs:909-923]
[crates/gcode/src/commands/codewiki/tests.rs:925-933] [crates/gcode/src/commands/codewiki/tests.rs:935-937] [crates/gcode/src/commands/codewiki/tests.rs:939-967] [crates/gcode/src/commands/codewiki/tests.rs:969-997]
[crates/gcode/src/commands/codewiki/text.rs:6-19] [crates/gcode/src/commands/codewiki/text.rs:22-25] [crates/gcode/src/commands/codewiki/text.rs:27-58] [crates/gcode/src/commands/codewiki/text.rs:60-76]
[crates/gcode/src/commands/codewiki/text.rs:78-86] [crates/gcode/src/commands/codewiki/text.rs:88-91] [crates/gcode/src/commands/codewiki/text.rs:93-108] [crates/gcode/src/commands/codewiki/text.rs:110-119]
[crates/gcode/src/commands/codewiki/text.rs:121-133] [crates/gcode/src/commands/codewiki/text.rs:135-141] [crates/gcode/src/commands/codewiki/text.rs:143-145] [crates/gcode/src/commands/codewiki/text.rs:147-156]
[crates/gcode/src/commands/codewiki/text.rs:158-170] [crates/gcode/src/commands/codewiki/text.rs:172-185] [crates/gcode/src/commands/codewiki/text.rs:187-213] [crates/gcode/src/commands/codewiki/text.rs:215-232]
[crates/gcode/src/commands/codewiki/text.rs:234-247] [crates/gcode/src/commands/codewiki/text.rs:249-251] [crates/gcode/src/commands/codewiki/text.rs:253-305]

