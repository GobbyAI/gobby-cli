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
  - 206-211
  - 213-217
  - 219-224
  - 227-233
  - 236-242
  - 245-252
  - 255-259
  - 262-266
  - 269-273
  - 276-288
  - 291-296
  - 299-301
  - 304-311
  - 314-317
  - 320-326
  - '328'
  - 330-350
  - 331-337
  - 339-345
  - 347-349
  - 352-446
  - 448-453
  - 455-460
  - 462-473
  - 475-482
  - 484-587
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
  - 315-349
  - 317-332
  - 351-353
  - 355-381
  - 383-395
  - 397-407
  - 409-431
  - 433-439
  - 441-463
  - 474-501
  - 504-524
  - 527-548
  - 551-574
  - 577-596
  - 598-603
  - 605-624
  - 626-635
  - 637-653
  - 655-663
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
  - 435-477
  - 479-507
  - 509-551
  - 553-612
  - 614-652
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
  - 172-178
  - 180-186
  - 188-198
  - 200-209
  - 211-224
  - 226-252
  - 254-271
  - 273-286
  - 288-290
  - 292-344
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
  - 206-211
  - 213-217
  - 219-224
  - 227-233
  - 236-242
  - 245-252
  - 255-259
  - 262-266
  - 269-273
  - 276-288
  - 291-296
  - 299-301
  - 304-311
  - 314-317
  - 320-326
  - '328'
  - 330-350
  - 331-337
  - 339-345
  - 347-349
  - 352-446
  - 448-453
  - 455-460
  - 462-473
  - 475-482
  - 484-587
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
  - 315-349
  - 317-332
  - 351-353
  - 355-381
  - 383-395
  - 397-407
  - 409-431
  - 433-439
  - 441-463
  - 474-501
  - 504-524
  - 527-548
  - 551-574
  - 577-596
  - 598-603
  - 605-624
  - 626-635
  - 637-653
  - 655-663
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
  - 435-477
  - 479-507
  - 509-551
  - 553-612
  - 614-652
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
  - 172-178
  - 180-186
  - 188-198
  - 200-209
  - 211-224
  - 226-252
  - 254-271
  - 273-286
  - 288-290
  - 292-344
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
[crates/gcode/src/commands/codewiki/io.rs:243-250] [crates/gcode/src/commands/codewiki/io.rs:252-262] [crates/gcode/src/commands/codewiki/mod.rs:79-84] [crates/gcode/src/commands/codewiki/mod.rs:87-91]
[crates/gcode/src/commands/codewiki/mod.rs:93-115] [crates/gcode/src/commands/codewiki/mod.rs:94-103] [crates/gcode/src/commands/codewiki/mod.rs:105-114] [crates/gcode/src/commands/codewiki/mod.rs:118-121]
[crates/gcode/src/commands/codewiki/mod.rs:124-127] [crates/gcode/src/commands/codewiki/mod.rs:129-150] [crates/gcode/src/commands/codewiki/mod.rs:130-135] [crates/gcode/src/commands/codewiki/mod.rs:137-142]
[crates/gcode/src/commands/codewiki/mod.rs:144-149] [crates/gcode/src/commands/codewiki/mod.rs:153-157] [crates/gcode/src/commands/codewiki/mod.rs:160-167] [crates/gcode/src/commands/codewiki/mod.rs:170-176]
[crates/gcode/src/commands/codewiki/mod.rs:179-189] [crates/gcode/src/commands/codewiki/mod.rs:192-197] [crates/gcode/src/commands/codewiki/mod.rs:200-204] [crates/gcode/src/commands/codewiki/mod.rs:206-211]
[crates/gcode/src/commands/codewiki/mod.rs:213-217] [crates/gcode/src/commands/codewiki/mod.rs:219-224] [crates/gcode/src/commands/codewiki/mod.rs:227-233] [crates/gcode/src/commands/codewiki/mod.rs:236-242]
[crates/gcode/src/commands/codewiki/mod.rs:245-252] [crates/gcode/src/commands/codewiki/mod.rs:255-259] [crates/gcode/src/commands/codewiki/mod.rs:262-266] [crates/gcode/src/commands/codewiki/mod.rs:269-273]
[crates/gcode/src/commands/codewiki/mod.rs:276-288] [crates/gcode/src/commands/codewiki/mod.rs:291-296] [crates/gcode/src/commands/codewiki/mod.rs:299-301] [crates/gcode/src/commands/codewiki/mod.rs:304-311]
[crates/gcode/src/commands/codewiki/mod.rs:314-317] [crates/gcode/src/commands/codewiki/mod.rs:320-326] [crates/gcode/src/commands/codewiki/mod.rs:328] [crates/gcode/src/commands/codewiki/mod.rs:330-350]
[crates/gcode/src/commands/codewiki/mod.rs:331-337] [crates/gcode/src/commands/codewiki/mod.rs:339-345] [crates/gcode/src/commands/codewiki/mod.rs:347-349] [crates/gcode/src/commands/codewiki/mod.rs:352-446]
[crates/gcode/src/commands/codewiki/mod.rs:448-453] [crates/gcode/src/commands/codewiki/mod.rs:455-460] [crates/gcode/src/commands/codewiki/mod.rs:462-473] [crates/gcode/src/commands/codewiki/mod.rs:475-482]
[crates/gcode/src/commands/codewiki/mod.rs:484-587] [crates/gcode/src/commands/codewiki/ownership.rs:13-16] [crates/gcode/src/commands/codewiki/ownership.rs:18-25] [crates/gcode/src/commands/codewiki/ownership.rs:19-24]
[crates/gcode/src/commands/codewiki/ownership.rs:28-31] [crates/gcode/src/commands/codewiki/ownership.rs:34-37] [crates/gcode/src/commands/codewiki/ownership.rs:40-45] [crates/gcode/src/commands/codewiki/ownership.rs:48-50]
[crates/gcode/src/commands/codewiki/ownership.rs:53-56] [crates/gcode/src/commands/codewiki/ownership.rs:59-63] [crates/gcode/src/commands/codewiki/ownership.rs:66-69] [crates/gcode/src/commands/codewiki/ownership.rs:71-116]
[crates/gcode/src/commands/codewiki/ownership.rs:118-128] [crates/gcode/src/commands/codewiki/ownership.rs:130-148] [crates/gcode/src/commands/codewiki/ownership.rs:150-169] [crates/gcode/src/commands/codewiki/ownership.rs:171-206]
[crates/gcode/src/commands/codewiki/ownership.rs:208-253] [crates/gcode/src/commands/codewiki/ownership.rs:255-257] [crates/gcode/src/commands/codewiki/ownership.rs:259-290] [crates/gcode/src/commands/codewiki/ownership.rs:292-313]
[crates/gcode/src/commands/codewiki/ownership.rs:315-349] [crates/gcode/src/commands/codewiki/ownership.rs:317-332] [crates/gcode/src/commands/codewiki/ownership.rs:351-353] [crates/gcode/src/commands/codewiki/ownership.rs:355-381]
[crates/gcode/src/commands/codewiki/ownership.rs:383-395] [crates/gcode/src/commands/codewiki/ownership.rs:397-407] [crates/gcode/src/commands/codewiki/ownership.rs:409-431] [crates/gcode/src/commands/codewiki/ownership.rs:433-439]
[crates/gcode/src/commands/codewiki/ownership.rs:441-463] [crates/gcode/src/commands/codewiki/ownership.rs:474-501] [crates/gcode/src/commands/codewiki/ownership.rs:504-524] [crates/gcode/src/commands/codewiki/ownership.rs:527-548]
[crates/gcode/src/commands/codewiki/ownership.rs:551-574] [crates/gcode/src/commands/codewiki/ownership.rs:577-596] [crates/gcode/src/commands/codewiki/ownership.rs:598-603] [crates/gcode/src/commands/codewiki/ownership.rs:605-624]
[crates/gcode/src/commands/codewiki/ownership.rs:626-635] [crates/gcode/src/commands/codewiki/ownership.rs:637-653] [crates/gcode/src/commands/codewiki/ownership.rs:655-663] [crates/gcode/src/commands/codewiki/paths.rs:3-14]
[crates/gcode/src/commands/codewiki/paths.rs:16-28] [crates/gcode/src/commands/codewiki/paths.rs:30-32] [crates/gcode/src/commands/codewiki/paths.rs:34-41] [crates/gcode/src/commands/codewiki/paths.rs:43-88]
[crates/gcode/src/commands/codewiki/paths.rs:93-101] [crates/gcode/src/commands/codewiki/paths.rs:103-109] [crates/gcode/src/commands/codewiki/paths.rs:111-119] [crates/gcode/src/commands/codewiki/paths.rs:121-123]
[crates/gcode/src/commands/codewiki/paths.rs:125-127] [crates/gcode/src/commands/codewiki/paths.rs:129-137] [crates/gcode/src/commands/codewiki/paths.rs:139-141] [crates/gcode/src/commands/codewiki/paths.rs:143-145]
[crates/gcode/src/commands/codewiki/paths.rs:147-149] [crates/gcode/src/commands/codewiki/paths.rs:151-153] [crates/gcode/src/commands/codewiki/paths.rs:155-157] [crates/gcode/src/commands/codewiki/prompts.rs:11-33]
[crates/gcode/src/commands/codewiki/prompts.rs:35-56] [crates/gcode/src/commands/codewiki/prompts.rs:58-91] [crates/gcode/src/commands/codewiki/prompts.rs:93-113] [crates/gcode/src/commands/codewiki/prompts.rs:115-148]
[crates/gcode/src/commands/codewiki/prompts.rs:151-159] [crates/gcode/src/commands/codewiki/prompts.rs:162-165] [crates/gcode/src/commands/codewiki/render.rs:5-33] [crates/gcode/src/commands/codewiki/render.rs:35-67]
[crates/gcode/src/commands/codewiki/render.rs:69-83] [crates/gcode/src/commands/codewiki/render.rs:85-108] [crates/gcode/src/commands/codewiki/render.rs:110-198] [crates/gcode/src/commands/codewiki/render.rs:200-229]
[crates/gcode/src/commands/codewiki/render.rs:231-281] [crates/gcode/src/commands/codewiki/render.rs:283-296] [crates/gcode/src/commands/codewiki/render.rs:298-308] [crates/gcode/src/commands/codewiki/render.rs:310-325]
[crates/gcode/src/commands/codewiki/render.rs:327-375] [crates/gcode/src/commands/codewiki/render.rs:377-405] [crates/gcode/src/commands/codewiki/render.rs:407-433] [crates/gcode/src/commands/codewiki/render.rs:435-477]
[crates/gcode/src/commands/codewiki/render.rs:479-507] [crates/gcode/src/commands/codewiki/render.rs:509-551] [crates/gcode/src/commands/codewiki/render.rs:553-612] [crates/gcode/src/commands/codewiki/render.rs:614-652]
[crates/gcode/src/commands/codewiki/tests.rs:11-45] [crates/gcode/src/commands/codewiki/tests.rs:48-110] [crates/gcode/src/commands/codewiki/tests.rs:113-120] [crates/gcode/src/commands/codewiki/tests.rs:123-196]
[crates/gcode/src/commands/codewiki/tests.rs:199-212] [crates/gcode/src/commands/codewiki/tests.rs:215-217] [crates/gcode/src/commands/codewiki/tests.rs:220-225] [crates/gcode/src/commands/codewiki/tests.rs:228-240]
[crates/gcode/src/commands/codewiki/tests.rs:243-265] [crates/gcode/src/commands/codewiki/tests.rs:268-295] [crates/gcode/src/commands/codewiki/tests.rs:298-307] [crates/gcode/src/commands/codewiki/tests.rs:310-317]
[crates/gcode/src/commands/codewiki/tests.rs:320-404] [crates/gcode/src/commands/codewiki/tests.rs:407-475] [crates/gcode/src/commands/codewiki/tests.rs:478-492] [crates/gcode/src/commands/codewiki/tests.rs:495-525]
[crates/gcode/src/commands/codewiki/tests.rs:528-549] [crates/gcode/src/commands/codewiki/tests.rs:552-590] [crates/gcode/src/commands/codewiki/tests.rs:593-605] [crates/gcode/src/commands/codewiki/tests.rs:608-624]
[crates/gcode/src/commands/codewiki/tests.rs:627-644] [crates/gcode/src/commands/codewiki/tests.rs:647-661] [crates/gcode/src/commands/codewiki/tests.rs:664-697] [crates/gcode/src/commands/codewiki/tests.rs:700-750]
[crates/gcode/src/commands/codewiki/tests.rs:753-854] [crates/gcode/src/commands/codewiki/tests.rs:857-880] [crates/gcode/src/commands/codewiki/tests.rs:883-887] [crates/gcode/src/commands/codewiki/tests.rs:891-905]
[crates/gcode/src/commands/codewiki/tests.rs:909-923] [crates/gcode/src/commands/codewiki/tests.rs:925-933] [crates/gcode/src/commands/codewiki/tests.rs:935-937] [crates/gcode/src/commands/codewiki/tests.rs:939-967]
[crates/gcode/src/commands/codewiki/tests.rs:969-997] [crates/gcode/src/commands/codewiki/text.rs:6-19] [crates/gcode/src/commands/codewiki/text.rs:22-25] [crates/gcode/src/commands/codewiki/text.rs:27-58]
[crates/gcode/src/commands/codewiki/text.rs:60-76] [crates/gcode/src/commands/codewiki/text.rs:78-86] [crates/gcode/src/commands/codewiki/text.rs:88-91] [crates/gcode/src/commands/codewiki/text.rs:93-108]
[crates/gcode/src/commands/codewiki/text.rs:110-119] [crates/gcode/src/commands/codewiki/text.rs:121-133] [crates/gcode/src/commands/codewiki/text.rs:135-141] [crates/gcode/src/commands/codewiki/text.rs:143-145]
[crates/gcode/src/commands/codewiki/text.rs:147-156] [crates/gcode/src/commands/codewiki/text.rs:158-170] [crates/gcode/src/commands/codewiki/text.rs:172-178] [crates/gcode/src/commands/codewiki/text.rs:180-186]
[crates/gcode/src/commands/codewiki/text.rs:188-198] [crates/gcode/src/commands/codewiki/text.rs:200-209] [crates/gcode/src/commands/codewiki/text.rs:211-224] [crates/gcode/src/commands/codewiki/text.rs:226-252]
[crates/gcode/src/commands/codewiki/text.rs:254-271] [crates/gcode/src/commands/codewiki/text.rs:273-286] [crates/gcode/src/commands/codewiki/text.rs:288-290] [crates/gcode/src/commands/codewiki/text.rs:292-344]

