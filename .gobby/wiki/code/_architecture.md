---
title: Architecture Overview
type: code_architecture
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
  ranges:
  - 5-110
  - 112-127
  - 129-179
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
  ranges:
  - 5-101
  - 104-113
  - 115-136
  - 138-154
  - 156-161
- file: crates/gcode/src/commands/codewiki/build_parts/file.rs
  ranges:
  - 4-91
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
  ranges:
  - 5-131
  - 133-157
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
  ranges:
  - 4-114
  - 116-126
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
  ranges:
  - 7-52
  - 54-109
  - 111-200
  - 202-208
  - 210-212
  - 214-219
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
  - 81-86
  - 89-93
  - 95-117
  - 96-105
  - 107-116
  - 120-123
  - 126-129
  - 131-152
  - 132-137
  - 139-144
  - 146-151
  - 155-159
  - 162-169
  - 172-178
  - 181-191
  - 194-199
  - 202-206
  - 209-214
  - 217-221
  - 224-229
  - 232-238
  - 241-247
  - 250-257
  - 260-264
  - 267-271
  - 274-278
  - 281-293
  - 296-301
  - 304-306
  - 309-316
  - 319-322
  - 325-331
  - '333'
  - 335-355
  - 336-342
  - 344-350
  - 352-354
  - 357-472
  - 474-479
  - 481-498
  - 500-505
  - 507-519
  - 521-534
  - 537-549
  - 551-668
- file: crates/gcode/src/commands/codewiki/ownership.rs
  ranges:
  - 16-19
  - 21-28
  - 22-27
  - 31-34
  - 37-40
  - 43-49
  - 52-56
  - 59-61
  - 64-67
  - 70-75
  - 78-81
  - 83-128
  - 130-140
  - 142-160
  - 162-181
  - 183-218
  - 220-281
  - 283-285
  - 287-302
  - 304-314
  - 316-318
  - 320-369
  - 371-380
  - 382-396
  - 398-422
  - 424-456
  - 426-440
  - 458-460
  - 462-488
  - 490-502
  - 504-514
  - 516-560
  - 562-568
  - 570-592
  - 603-630
  - 633-657
  - 660-677
  - 680-701
  - 704-727
  - 730-749
  - 752-776
  - 779-784
  - 786-791
  - 793-812
  - 814-823
  - 825-841
  - 843-851
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
- file: crates/gcode/src/commands/codewiki/progress.rs
  ranges:
  - 2-7
  - 10-12
  - 14-55
  - 15-19
  - 21-29
  - 32-36
  - 38-46
  - 49-54
- file: crates/gcode/src/commands/codewiki/prompts.rs
  ranges:
  - 11-33
  - 35-56
  - 58-72
  - 74-94
  - 96-110
  - 112-123
  - 125-154
  - 157-165
  - 168-171
- file: crates/gcode/src/commands/codewiki/render.rs
  ranges:
  - 5-35
  - 37-71
  - 73-87
  - 89-112
  - 114-121
  - 123-211
  - 213-242
  - 244-294
  - 296-309
  - 311-321
  - 323-338
  - 340-390
  - 392-420
  - 422-448
  - 450-486
  - 488-531
  - 533-535
  - 537-596
  - 598-657
  - 659-697
- file: crates/gcode/src/commands/codewiki/tests.rs
  ranges:
  - 14-48
  - 51-113
  - 116-123
  - 126-199
  - 202-215
  - 218-220
  - 223-228
  - 231-243
  - 246-268
  - 271-298
  - 301-310
  - 313-320
  - 323-407
  - 410-478
  - 481-495
  - 498-528
  - 531-552
  - 555-593
  - 596-608
  - 611-627
  - 630-642
  - 645-662
  - 665-679
  - 682-715
  - 718-768
  - 771-872
  - 875-898
  - 901-905
  - 909-923
  - 927-941
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 8-20
  - 23-26
  - 28-59
  - 61-77
  - 79-87
  - 89-92
  - 94-109
  - 111-120
  - 122-134
  - 136-142
  - 144-146
  - 148-157
  - 159-169
  - 171-191
  - 193-200
  - 202-211
  - 213-219
  - 221-231
  - 233-246
  - 248-274
  - 276-293
  - 295-308
  - 310-312
  - 316-367
  - 373-379
  - 382-407
  - 410-424
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# Architecture Overview

## Subsystems

- [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]] - `crates/gcode/src/commands/codewiki` contains 12 direct files and 1 child module.
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-110] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:112-127] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:129-179]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-136]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:138-154] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:156-161] [crates/gcode/src/commands/codewiki/build_parts/file.rs:4-91]
[crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-131] [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:133-157] [crates/gcode/src/commands/codewiki/build_parts/modules.rs:4-114]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:116-126] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-200] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:202-208] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:210-212]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:214-219] [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84] [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134] [crates/gcode/src/commands/codewiki/cluster.rs:3-54] [crates/gcode/src/commands/codewiki/cluster.rs:56-80] [crates/gcode/src/commands/codewiki/cluster.rs:89-130]
[crates/gcode/src/commands/codewiki/cluster.rs:132-156] [crates/gcode/src/commands/codewiki/cluster.rs:158-168] [crates/gcode/src/commands/codewiki/cluster.rs:170-178] [crates/gcode/src/commands/codewiki/cluster.rs:180-196]
[crates/gcode/src/commands/codewiki/cluster.rs:198-206] [crates/gcode/src/commands/codewiki/cluster.rs:208-226] [crates/gcode/src/commands/codewiki/cluster.rs:228-233] [crates/gcode/src/commands/codewiki/graph.rs:4-124]
[crates/gcode/src/commands/codewiki/graph.rs:34-49] [crates/gcode/src/commands/codewiki/graph.rs:126-145] [crates/gcode/src/commands/codewiki/graph.rs:147-165] [crates/gcode/src/commands/codewiki/io.rs:3-9]
[crates/gcode/src/commands/codewiki/io.rs:11-17] [crates/gcode/src/commands/codewiki/io.rs:19-69] [crates/gcode/src/commands/codewiki/io.rs:71-79] [crates/gcode/src/commands/codewiki/io.rs:81-99]
[crates/gcode/src/commands/codewiki/io.rs:101-121] [crates/gcode/src/commands/codewiki/io.rs:123-130] [crates/gcode/src/commands/codewiki/io.rs:132-135] [crates/gcode/src/commands/codewiki/io.rs:137-144]
[crates/gcode/src/commands/codewiki/io.rs:146-149] [crates/gcode/src/commands/codewiki/io.rs:151-172] [crates/gcode/src/commands/codewiki/io.rs:174-207] [crates/gcode/src/commands/codewiki/io.rs:210-240]
[crates/gcode/src/commands/codewiki/io.rs:243-250] [crates/gcode/src/commands/codewiki/io.rs:252-262] [crates/gcode/src/commands/codewiki/mod.rs:81-86] [crates/gcode/src/commands/codewiki/mod.rs:89-93]
[crates/gcode/src/commands/codewiki/mod.rs:95-117] [crates/gcode/src/commands/codewiki/mod.rs:96-105] [crates/gcode/src/commands/codewiki/mod.rs:107-116] [crates/gcode/src/commands/codewiki/mod.rs:120-123]
[crates/gcode/src/commands/codewiki/mod.rs:126-129] [crates/gcode/src/commands/codewiki/mod.rs:131-152] [crates/gcode/src/commands/codewiki/mod.rs:132-137] [crates/gcode/src/commands/codewiki/mod.rs:139-144]
[crates/gcode/src/commands/codewiki/mod.rs:146-151] [crates/gcode/src/commands/codewiki/mod.rs:155-159] [crates/gcode/src/commands/codewiki/mod.rs:162-169] [crates/gcode/src/commands/codewiki/mod.rs:172-178]
[crates/gcode/src/commands/codewiki/mod.rs:181-191] [crates/gcode/src/commands/codewiki/mod.rs:194-199] [crates/gcode/src/commands/codewiki/mod.rs:202-206] [crates/gcode/src/commands/codewiki/mod.rs:209-214]
[crates/gcode/src/commands/codewiki/mod.rs:217-221] [crates/gcode/src/commands/codewiki/mod.rs:224-229] [crates/gcode/src/commands/codewiki/mod.rs:232-238] [crates/gcode/src/commands/codewiki/mod.rs:241-247]
[crates/gcode/src/commands/codewiki/mod.rs:250-257] [crates/gcode/src/commands/codewiki/mod.rs:260-264] [crates/gcode/src/commands/codewiki/mod.rs:267-271] [crates/gcode/src/commands/codewiki/mod.rs:274-278]
[crates/gcode/src/commands/codewiki/mod.rs:281-293] [crates/gcode/src/commands/codewiki/mod.rs:296-301] [crates/gcode/src/commands/codewiki/mod.rs:304-306] [crates/gcode/src/commands/codewiki/mod.rs:309-316]
[crates/gcode/src/commands/codewiki/mod.rs:319-322] [crates/gcode/src/commands/codewiki/mod.rs:325-331] [crates/gcode/src/commands/codewiki/mod.rs:333] [crates/gcode/src/commands/codewiki/mod.rs:335-355]
[crates/gcode/src/commands/codewiki/mod.rs:336-342] [crates/gcode/src/commands/codewiki/mod.rs:344-350] [crates/gcode/src/commands/codewiki/mod.rs:352-354] [crates/gcode/src/commands/codewiki/mod.rs:357-472]
[crates/gcode/src/commands/codewiki/mod.rs:474-479] [crates/gcode/src/commands/codewiki/mod.rs:481-498] [crates/gcode/src/commands/codewiki/mod.rs:500-505] [crates/gcode/src/commands/codewiki/mod.rs:507-519]
[crates/gcode/src/commands/codewiki/mod.rs:521-534] [crates/gcode/src/commands/codewiki/mod.rs:537-549] [crates/gcode/src/commands/codewiki/mod.rs:551-668] [crates/gcode/src/commands/codewiki/ownership.rs:16-19]
[crates/gcode/src/commands/codewiki/ownership.rs:21-28] [crates/gcode/src/commands/codewiki/ownership.rs:22-27] [crates/gcode/src/commands/codewiki/ownership.rs:31-34] [crates/gcode/src/commands/codewiki/ownership.rs:37-40]
[crates/gcode/src/commands/codewiki/ownership.rs:43-49] [crates/gcode/src/commands/codewiki/ownership.rs:52-56] [crates/gcode/src/commands/codewiki/ownership.rs:59-61] [crates/gcode/src/commands/codewiki/ownership.rs:64-67]
[crates/gcode/src/commands/codewiki/ownership.rs:70-75] [crates/gcode/src/commands/codewiki/ownership.rs:78-81] [crates/gcode/src/commands/codewiki/ownership.rs:83-128] [crates/gcode/src/commands/codewiki/ownership.rs:130-140]
[crates/gcode/src/commands/codewiki/ownership.rs:142-160] [crates/gcode/src/commands/codewiki/ownership.rs:162-181] [crates/gcode/src/commands/codewiki/ownership.rs:183-218] [crates/gcode/src/commands/codewiki/ownership.rs:220-281]
[crates/gcode/src/commands/codewiki/ownership.rs:283-285] [crates/gcode/src/commands/codewiki/ownership.rs:287-302] [crates/gcode/src/commands/codewiki/ownership.rs:304-314] [crates/gcode/src/commands/codewiki/ownership.rs:316-318]
[crates/gcode/src/commands/codewiki/ownership.rs:320-369] [crates/gcode/src/commands/codewiki/ownership.rs:371-380] [crates/gcode/src/commands/codewiki/ownership.rs:382-396] [crates/gcode/src/commands/codewiki/ownership.rs:398-422]
[crates/gcode/src/commands/codewiki/ownership.rs:424-456] [crates/gcode/src/commands/codewiki/ownership.rs:426-440] [crates/gcode/src/commands/codewiki/ownership.rs:458-460] [crates/gcode/src/commands/codewiki/ownership.rs:462-488]
[crates/gcode/src/commands/codewiki/ownership.rs:490-502] [crates/gcode/src/commands/codewiki/ownership.rs:504-514] [crates/gcode/src/commands/codewiki/ownership.rs:516-560] [crates/gcode/src/commands/codewiki/ownership.rs:562-568]
[crates/gcode/src/commands/codewiki/ownership.rs:570-592] [crates/gcode/src/commands/codewiki/ownership.rs:603-630] [crates/gcode/src/commands/codewiki/ownership.rs:633-657] [crates/gcode/src/commands/codewiki/ownership.rs:660-677]
[crates/gcode/src/commands/codewiki/ownership.rs:680-701] [crates/gcode/src/commands/codewiki/ownership.rs:704-727] [crates/gcode/src/commands/codewiki/ownership.rs:730-749] [crates/gcode/src/commands/codewiki/ownership.rs:752-776]
[crates/gcode/src/commands/codewiki/ownership.rs:779-784] [crates/gcode/src/commands/codewiki/ownership.rs:786-791] [crates/gcode/src/commands/codewiki/ownership.rs:793-812] [crates/gcode/src/commands/codewiki/ownership.rs:814-823]
[crates/gcode/src/commands/codewiki/ownership.rs:825-841] [crates/gcode/src/commands/codewiki/ownership.rs:843-851] [crates/gcode/src/commands/codewiki/paths.rs:3-14] [crates/gcode/src/commands/codewiki/paths.rs:16-28]
[crates/gcode/src/commands/codewiki/paths.rs:30-32] [crates/gcode/src/commands/codewiki/paths.rs:34-41] [crates/gcode/src/commands/codewiki/paths.rs:43-88] [crates/gcode/src/commands/codewiki/paths.rs:93-101]
[crates/gcode/src/commands/codewiki/paths.rs:103-109] [crates/gcode/src/commands/codewiki/paths.rs:111-119] [crates/gcode/src/commands/codewiki/paths.rs:121-123] [crates/gcode/src/commands/codewiki/paths.rs:125-127]
[crates/gcode/src/commands/codewiki/paths.rs:129-137] [crates/gcode/src/commands/codewiki/paths.rs:139-141] [crates/gcode/src/commands/codewiki/paths.rs:143-145] [crates/gcode/src/commands/codewiki/paths.rs:147-149]
[crates/gcode/src/commands/codewiki/paths.rs:151-153] [crates/gcode/src/commands/codewiki/paths.rs:155-157] [crates/gcode/src/commands/codewiki/progress.rs:2-7] [crates/gcode/src/commands/codewiki/progress.rs:10-12]
[crates/gcode/src/commands/codewiki/progress.rs:14-55] [crates/gcode/src/commands/codewiki/progress.rs:15-19] [crates/gcode/src/commands/codewiki/progress.rs:21-29] [crates/gcode/src/commands/codewiki/progress.rs:32-36]
[crates/gcode/src/commands/codewiki/progress.rs:38-46] [crates/gcode/src/commands/codewiki/progress.rs:49-54] [crates/gcode/src/commands/codewiki/prompts.rs:11-33] [crates/gcode/src/commands/codewiki/prompts.rs:35-56]
[crates/gcode/src/commands/codewiki/prompts.rs:58-72] [crates/gcode/src/commands/codewiki/prompts.rs:74-94] [crates/gcode/src/commands/codewiki/prompts.rs:96-110] [crates/gcode/src/commands/codewiki/prompts.rs:112-123]
[crates/gcode/src/commands/codewiki/prompts.rs:125-154] [crates/gcode/src/commands/codewiki/prompts.rs:157-165] [crates/gcode/src/commands/codewiki/prompts.rs:168-171] [crates/gcode/src/commands/codewiki/render.rs:5-35]
[crates/gcode/src/commands/codewiki/render.rs:37-71] [crates/gcode/src/commands/codewiki/render.rs:73-87] [crates/gcode/src/commands/codewiki/render.rs:89-112] [crates/gcode/src/commands/codewiki/render.rs:114-121]
[crates/gcode/src/commands/codewiki/render.rs:123-211] [crates/gcode/src/commands/codewiki/render.rs:213-242] [crates/gcode/src/commands/codewiki/render.rs:244-294] [crates/gcode/src/commands/codewiki/render.rs:296-309]
[crates/gcode/src/commands/codewiki/render.rs:311-321] [crates/gcode/src/commands/codewiki/render.rs:323-338] [crates/gcode/src/commands/codewiki/render.rs:340-390] [crates/gcode/src/commands/codewiki/render.rs:392-420]
[crates/gcode/src/commands/codewiki/render.rs:422-448] [crates/gcode/src/commands/codewiki/render.rs:450-486] [crates/gcode/src/commands/codewiki/render.rs:488-531] [crates/gcode/src/commands/codewiki/render.rs:533-535]
[crates/gcode/src/commands/codewiki/render.rs:537-596] [crates/gcode/src/commands/codewiki/render.rs:598-657] [crates/gcode/src/commands/codewiki/render.rs:659-697] [crates/gcode/src/commands/codewiki/tests.rs:14-48]
[crates/gcode/src/commands/codewiki/tests.rs:51-113] [crates/gcode/src/commands/codewiki/tests.rs:116-123] [crates/gcode/src/commands/codewiki/tests.rs:126-199] [crates/gcode/src/commands/codewiki/tests.rs:202-215]
[crates/gcode/src/commands/codewiki/tests.rs:218-220] [crates/gcode/src/commands/codewiki/tests.rs:223-228] [crates/gcode/src/commands/codewiki/tests.rs:231-243] [crates/gcode/src/commands/codewiki/tests.rs:246-268]
[crates/gcode/src/commands/codewiki/tests.rs:271-298] [crates/gcode/src/commands/codewiki/tests.rs:301-310] [crates/gcode/src/commands/codewiki/tests.rs:313-320] [crates/gcode/src/commands/codewiki/tests.rs:323-407]
[crates/gcode/src/commands/codewiki/tests.rs:410-478] [crates/gcode/src/commands/codewiki/tests.rs:481-495] [crates/gcode/src/commands/codewiki/tests.rs:498-528] [crates/gcode/src/commands/codewiki/tests.rs:531-552]
[crates/gcode/src/commands/codewiki/tests.rs:555-593] [crates/gcode/src/commands/codewiki/tests.rs:596-608] [crates/gcode/src/commands/codewiki/tests.rs:611-627] [crates/gcode/src/commands/codewiki/tests.rs:630-642]
[crates/gcode/src/commands/codewiki/tests.rs:645-662] [crates/gcode/src/commands/codewiki/tests.rs:665-679] [crates/gcode/src/commands/codewiki/tests.rs:682-715] [crates/gcode/src/commands/codewiki/tests.rs:718-768]
[crates/gcode/src/commands/codewiki/tests.rs:771-872] [crates/gcode/src/commands/codewiki/tests.rs:875-898] [crates/gcode/src/commands/codewiki/tests.rs:901-905] [crates/gcode/src/commands/codewiki/tests.rs:909-923]
[crates/gcode/src/commands/codewiki/tests.rs:927-941] [crates/gcode/src/commands/codewiki/text.rs:8-20] [crates/gcode/src/commands/codewiki/text.rs:23-26] [crates/gcode/src/commands/codewiki/text.rs:28-59]
[crates/gcode/src/commands/codewiki/text.rs:61-77] [crates/gcode/src/commands/codewiki/text.rs:79-87] [crates/gcode/src/commands/codewiki/text.rs:89-92] [crates/gcode/src/commands/codewiki/text.rs:94-109]
[crates/gcode/src/commands/codewiki/text.rs:111-120] [crates/gcode/src/commands/codewiki/text.rs:122-134] [crates/gcode/src/commands/codewiki/text.rs:136-142] [crates/gcode/src/commands/codewiki/text.rs:144-146]
[crates/gcode/src/commands/codewiki/text.rs:148-157] [crates/gcode/src/commands/codewiki/text.rs:159-169] [crates/gcode/src/commands/codewiki/text.rs:171-191] [crates/gcode/src/commands/codewiki/text.rs:193-200]
[crates/gcode/src/commands/codewiki/text.rs:202-211] [crates/gcode/src/commands/codewiki/text.rs:213-219] [crates/gcode/src/commands/codewiki/text.rs:221-231] [crates/gcode/src/commands/codewiki/text.rs:233-246]
[crates/gcode/src/commands/codewiki/text.rs:248-274] [crates/gcode/src/commands/codewiki/text.rs:276-293] [crates/gcode/src/commands/codewiki/text.rs:295-308] [crates/gcode/src/commands/codewiki/text.rs:310-312]
[crates/gcode/src/commands/codewiki/text.rs:316-367] [crates/gcode/src/commands/codewiki/text.rs:373-379] [crates/gcode/src/commands/codewiki/text.rs:382-407] [crates/gcode/src/commands/codewiki/text.rs:410-424]
- [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]] - `crates/gcode/src/commands/codewiki/build_parts` contains 7 direct files and 0 child modules.
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-110] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:112-127] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:129-179]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-136]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:138-154] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:156-161] [crates/gcode/src/commands/codewiki/build_parts/file.rs:4-91]
[crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-131] [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:133-157] [crates/gcode/src/commands/codewiki/build_parts/modules.rs:4-114]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:116-126] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:7-52] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:54-109]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:111-200] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:202-208] [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:210-212]
[crates/gcode/src/commands/codewiki/build_parts/onboarding.rs:214-219] [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84] [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

