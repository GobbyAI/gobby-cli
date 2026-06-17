---
title: FalkorDB Graph Synchronization
type: code_concept
provenance:
- file: crates/gcode/src/graph/code_graph.rs
  ranges:
  - 1-51
- file: crates/gcode/src/graph/code_graph/connection.rs
  ranges:
  - 7-12
  - 14-40
  - 42-68
- file: crates/gcode/src/graph/code_graph/lifecycle.rs
  ranges:
  - 18-21
  - 24-29
  - 31-36
  - 38-43
  - 47-52
  - 55-61
  - 65-68
  - 71-76
  - 80-88
  - 90-95
  - 98-105
  - 108-113
  - 116-122
  - 125-130
  - 133-149
  - 154-164
  - 166-176
  - 178-191
  - 193-211
  - 213-232
  - 234-248
  - 250-286
- file: crates/gcode/src/graph/code_graph/payload.rs
  ranges:
  - 10-19
  - 22-30
  - 32-43
  - 45-47
  - 49-51
  - 53-75
  - 77-85
  - 89-91
  - 95-112
  - 115-117
  - 120-139
  - 142-159
  - 165-181
  - 183-203
  - 207-218
  - 221-234
  - 236-246
  - 250-266
  - 268-294
  - 296-301
  - 303-320
  - 322-326
  - 328-332
  - 334-343
- file: crates/gcode/src/graph/code_graph/read.rs
  ranges:
  - 1-25
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
  ranges:
  - 19-98
  - 100-126
  - 128-164
  - 166-239
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
  ranges:
  - 10-29
  - 31-47
  - 49-68
  - 70-90
  - 92-106
  - 108-130
  - 132-153
  - 155-169
  - 171-195
  - 197-219
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
  ranges:
  - 9-21
  - 23-38
  - 40-62
  - 64-84
  - 86-102
  - 104-120
  - 122-143
  - 145-162
  - 164-185
  - 187-204
  - 206-220
  - 222-238
  - 240-250
  - 252-278
  - 280-297
  - 304-310
  - 313-318
  - 321-329
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
  ranges:
  - 24-27
  - 29-35
  - 37-48
  - 50-60
  - 62-72
  - 74-85
  - 87-98
  - 100-113
  - 115-124
  - 126-139
  - 141-157
  - 159-172
  - 174-190
  - 192-198
  - 200-225
  - 227-245
  - 247-263
  - 265-302
  - 304-342
  - 344-355
  - 361-366
  - 369-375
  - 378-386
  - 389-397
- file: crates/gcode/src/graph/code_graph/read/support.rs
  ranges:
  - 43-97
  - 99-131
  - 133-142
  - 150-162
  - 165-187
- file: crates/gcode/src/graph/code_graph/tests.rs
  ranges:
  - 7-21
  - 24-33
  - 36-65
  - 68-156
  - 159-164
  - 167-194
  - 197-203
  - 206-223
  - 226-242
  - 245-250
  - 253-276
  - 279-320
  - 323-327
  - 330-344
  - 347-357
  - 360-399
  - 402-449
  - 452-499
  - 502-521
  - 524-534
  - 537-564
  - 567-579
- file: crates/gcode/src/graph/code_graph/write.rs
  ranges:
  - 47-50
  - 53-56
  - 59-61
  - 63-101
  - 103-108
  - 110-120
  - 122-138
  - 140-159
  - 161-192
  - 194-203
  - 205-214
  - 216-221
  - 223-227
  - 229-234
  - 236-258
  - 260-271
  - 273-282
  - 284-286
  - 289-294
  - 296-307
  - 309-318
  - 320-328
  - 330-334
  - 336-338
  - 340-345
  - 347-351
  - 353-376
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
  ranges:
  - 8-66
  - 68-113
  - 115-127
  - 129-145
  - 147-161
  - 163-171
  - 173-189
  - 191-200
  - 202-211
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
  ranges:
  - 89-96
  - 99-102
  - 105-112
  - 115-119
  - 121-128
  - 130-145
  - 147-152
  - 154-182
  - 184-197
  - 199-207
  - 209-227
  - 229-259
  - 261-295
  - 297-301
  - 304-321
  - 323-327
  - 329-334
  - 337-343
  - 345-364
  - 366-377
  - 379-390
  - 392-403
  - 411-435
  - 438-450
- file: crates/gcode/src/graph/code_graph/write/support.rs
  ranges:
  - 6-13
  - 15-21
  - 23-27
  - 29-31
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
  ranges:
  - 30-81
  - 89-110
  - 113-156
  - 159-177
- file: crates/gcode/src/graph/mod.rs
  ranges:
  - 1-4
- file: crates/gcode/src/graph/report.rs
  ranges:
  - 1-21
- file: crates/gcode/src/graph/report/generation.rs
  ranges:
  - 21-23
  - 25-59
  - 61-63
  - 65-76
  - 78-159
- file: crates/gcode/src/graph/report/loading.rs
  ranges:
  - 18-78
  - 80-95
  - 97-111
  - 113-128
  - 130-146
- file: crates/gcode/src/graph/report/queries.rs
  ranges:
  - 7-18
  - 20-22
  - 24-26
  - 28-38
  - 40-49
  - 51-85
  - 87-104
  - 106-126
  - 128-144
- file: crates/gcode/src/graph/report/render.rs
  ranges:
  - 8-18
  - 20-99
  - 101-121
  - 123-141
  - 143-150
  - 152-164
  - 166-177
  - 179-185
- file: crates/gcode/src/graph/report/rows.rs
  ranges:
  - 11-19
  - 21-31
  - 33-39
  - 41-66
  - 68-78
  - 80-106
  - 108-112
  - 119-128
  - 131-140
  - 143-154
  - 157-162
- file: crates/gcode/src/graph/report/summary.rs
  ranges:
  - 14-17
  - 19-41
  - 43-49
  - 51-91
  - 93-100
  - 102-156
  - 158-195
  - 197-231
  - 233-237
  - 239-248
  - 250-290
  - 294-308
  - 310-339
  - 341-349
  - 351-356
- file: crates/gcode/src/graph/report/tests.rs
  ranges:
  - 15-65
  - 68-84
  - 87-127
  - 129-179
  - 181-196
  - 199-225
  - 228-249
  - 252-277
  - 280-317
  - 320-342
  - 345-390
- file: crates/gcode/src/graph/report/time.rs
  ranges:
  - 3-5
- file: crates/gcode/src/graph/report/types.rs
  ranges:
  - 10-17
  - 20-34
  - 36-49
  - 53-68
  - 71-73
  - 76-80
  - 84-88
  - 92-97
  - 100-105
  - 108-118
  - 121-125
  - 128-136
  - 139-142
  - 145-148
  - 151-155
  - 158-162
  - 165-178
  - 184-192
  - 195-200
  - 204-215
  - 218-221
  - 225-229
  - 233-243
  - 247-251
  - 254-256
  - 259-261
  - 265-267
- file: crates/gcode/src/graph/typed_query.rs
  ranges:
  - 7-10
  - 13-21
  - 24-27
  - 30-38
  - 41-46
  - 48-58
  - 60-70
  - 73-75
  - 77-98
  - 100-105
  - 107-109
  - 111-113
  - 115-120
  - 122-141
  - 143-145
  - 147-164
  - 166-178
  - 181-186
  - 190-200
  - 211-276
  - 279-284
  - 287-297
  - 300-315
  - 318-341
  - 344-350
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph.rs:1-51](crates/gcode/src/graph/code_graph.rs#L1-L51)
- [crates/gcode/src/graph/code_graph/connection.rs:7-12](crates/gcode/src/graph/code_graph/connection.rs#L7-L12), [crates/gcode/src/graph/code_graph/connection.rs:14-40](crates/gcode/src/graph/code_graph/connection.rs#L14-L40), [crates/gcode/src/graph/code_graph/connection.rs:42-68](crates/gcode/src/graph/code_graph/connection.rs#L42-L68)
- [crates/gcode/src/graph/code_graph/lifecycle.rs:18-21](crates/gcode/src/graph/code_graph/lifecycle.rs#L18-L21), [crates/gcode/src/graph/code_graph/lifecycle.rs:24-29](crates/gcode/src/graph/code_graph/lifecycle.rs#L24-L29), [crates/gcode/src/graph/code_graph/lifecycle.rs:31-36](crates/gcode/src/graph/code_graph/lifecycle.rs#L31-L36), [crates/gcode/src/graph/code_graph/lifecycle.rs:38-43](crates/gcode/src/graph/code_graph/lifecycle.rs#L38-L43), [crates/gcode/src/graph/code_graph/lifecycle.rs:47-52](crates/gcode/src/graph/code_graph/lifecycle.rs#L47-L52), [crates/gcode/src/graph/code_graph/lifecycle.rs:55-61](crates/gcode/src/graph/code_graph/lifecycle.rs#L55-L61), [crates/gcode/src/graph/code_graph/lifecycle.rs:65-68](crates/gcode/src/graph/code_graph/lifecycle.rs#L65-L68), [crates/gcode/src/graph/code_graph/lifecycle.rs:71-76](crates/gcode/src/graph/code_graph/lifecycle.rs#L71-L76), [crates/gcode/src/graph/code_graph/lifecycle.rs:80-88](crates/gcode/src/graph/code_graph/lifecycle.rs#L80-L88), [crates/gcode/src/graph/code_graph/lifecycle.rs:90-95](crates/gcode/src/graph/code_graph/lifecycle.rs#L90-L95), [crates/gcode/src/graph/code_graph/lifecycle.rs:98-105](crates/gcode/src/graph/code_graph/lifecycle.rs#L98-L105), [crates/gcode/src/graph/code_graph/lifecycle.rs:108-113](crates/gcode/src/graph/code_graph/lifecycle.rs#L108-L113), [crates/gcode/src/graph/code_graph/lifecycle.rs:116-122](crates/gcode/src/graph/code_graph/lifecycle.rs#L116-L122), [crates/gcode/src/graph/code_graph/lifecycle.rs:125-130](crates/gcode/src/graph/code_graph/lifecycle.rs#L125-L130), [crates/gcode/src/graph/code_graph/lifecycle.rs:133-149](crates/gcode/src/graph/code_graph/lifecycle.rs#L133-L149), [crates/gcode/src/graph/code_graph/lifecycle.rs:154-164](crates/gcode/src/graph/code_graph/lifecycle.rs#L154-L164), [crates/gcode/src/graph/code_graph/lifecycle.rs:166-176](crates/gcode/src/graph/code_graph/lifecycle.rs#L166-L176), [crates/gcode/src/graph/code_graph/lifecycle.rs:178-191](crates/gcode/src/graph/code_graph/lifecycle.rs#L178-L191), [crates/gcode/src/graph/code_graph/lifecycle.rs:193-211](crates/gcode/src/graph/code_graph/lifecycle.rs#L193-L211), [crates/gcode/src/graph/code_graph/lifecycle.rs:213-232](crates/gcode/src/graph/code_graph/lifecycle.rs#L213-L232), [crates/gcode/src/graph/code_graph/lifecycle.rs:234-248](crates/gcode/src/graph/code_graph/lifecycle.rs#L234-L248), [crates/gcode/src/graph/code_graph/lifecycle.rs:250-286](crates/gcode/src/graph/code_graph/lifecycle.rs#L250-L286)
- [crates/gcode/src/graph/code_graph/payload.rs:10-19](crates/gcode/src/graph/code_graph/payload.rs#L10-L19), [crates/gcode/src/graph/code_graph/payload.rs:22-30](crates/gcode/src/graph/code_graph/payload.rs#L22-L30), [crates/gcode/src/graph/code_graph/payload.rs:32-43](crates/gcode/src/graph/code_graph/payload.rs#L32-L43), [crates/gcode/src/graph/code_graph/payload.rs:45-47](crates/gcode/src/graph/code_graph/payload.rs#L45-L47), [crates/gcode/src/graph/code_graph/payload.rs:49-51](crates/gcode/src/graph/code_graph/payload.rs#L49-L51), [crates/gcode/src/graph/code_graph/payload.rs:53-75](crates/gcode/src/graph/code_graph/payload.rs#L53-L75), [crates/gcode/src/graph/code_graph/payload.rs:77-85](crates/gcode/src/graph/code_graph/payload.rs#L77-L85), [crates/gcode/src/graph/code_graph/payload.rs:89-91](crates/gcode/src/graph/code_graph/payload.rs#L89-L91), [crates/gcode/src/graph/code_graph/payload.rs:95-112](crates/gcode/src/graph/code_graph/payload.rs#L95-L112), [crates/gcode/src/graph/code_graph/payload.rs:115-117](crates/gcode/src/graph/code_graph/payload.rs#L115-L117), [crates/gcode/src/graph/code_graph/payload.rs:120-139](crates/gcode/src/graph/code_graph/payload.rs#L120-L139), [crates/gcode/src/graph/code_graph/payload.rs:142-159](crates/gcode/src/graph/code_graph/payload.rs#L142-L159), [crates/gcode/src/graph/code_graph/payload.rs:165-181](crates/gcode/src/graph/code_graph/payload.rs#L165-L181), [crates/gcode/src/graph/code_graph/payload.rs:183-203](crates/gcode/src/graph/code_graph/payload.rs#L183-L203), [crates/gcode/src/graph/code_graph/payload.rs:207-218](crates/gcode/src/graph/code_graph/payload.rs#L207-L218), [crates/gcode/src/graph/code_graph/payload.rs:221-234](crates/gcode/src/graph/code_graph/payload.rs#L221-L234), [crates/gcode/src/graph/code_graph/payload.rs:236-246](crates/gcode/src/graph/code_graph/payload.rs#L236-L246), [crates/gcode/src/graph/code_graph/payload.rs:250-266](crates/gcode/src/graph/code_graph/payload.rs#L250-L266), [crates/gcode/src/graph/code_graph/payload.rs:268-294](crates/gcode/src/graph/code_graph/payload.rs#L268-L294), [crates/gcode/src/graph/code_graph/payload.rs:296-301](crates/gcode/src/graph/code_graph/payload.rs#L296-L301), [crates/gcode/src/graph/code_graph/payload.rs:303-320](crates/gcode/src/graph/code_graph/payload.rs#L303-L320), [crates/gcode/src/graph/code_graph/payload.rs:322-326](crates/gcode/src/graph/code_graph/payload.rs#L322-L326), [crates/gcode/src/graph/code_graph/payload.rs:328-332](crates/gcode/src/graph/code_graph/payload.rs#L328-L332), [crates/gcode/src/graph/code_graph/payload.rs:334-343](crates/gcode/src/graph/code_graph/payload.rs#L334-L343)
- [crates/gcode/src/graph/code_graph/read.rs:1-25](crates/gcode/src/graph/code_graph/read.rs#L1-L25)
- [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98](crates/gcode/src/graph/code_graph/read/graph_payloads.rs#L19-L98), [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:100-126](crates/gcode/src/graph/code_graph/read/graph_payloads.rs#L100-L126), [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:128-164](crates/gcode/src/graph/code_graph/read/graph_payloads.rs#L128-L164), [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:166-239](crates/gcode/src/graph/code_graph/read/graph_payloads.rs#L166-L239)
- [crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L10-L29), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:31-47](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L31-L47), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:49-68](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L49-L68), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:70-90](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L70-L90), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:92-106](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L92-L106), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:108-130](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L108-L130), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:132-153](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L132-L153), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:155-169](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L155-L169), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:171-195](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L171-L195), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:197-219](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L197-L219)
- [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L9-L21), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:23-38](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L23-L38), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:40-62](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L40-L62), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:64-84](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L64-L84), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:86-102](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L86-L102), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:104-120](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L104-L120), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:122-143](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L122-L143), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:145-162](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L145-L162), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:164-185](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L164-L185), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:187-204](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L187-L204), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:206-220](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L206-L220), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:222-238](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L222-L238), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:240-250](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L240-L250), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:252-278](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L252-L278), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:280-297](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L280-L297), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:304-310](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L304-L310), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:313-318](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L313-L318), [crates/gcode/src/graph/code_graph/read/relationship_queries.rs:321-329](crates/gcode/src/graph/code_graph/read/relationship_queries.rs#L321-L329)
- [crates/gcode/src/graph/code_graph/read/relationships.rs:24-27](crates/gcode/src/graph/code_graph/read/relationships.rs#L24-L27), [crates/gcode/src/graph/code_graph/read/relationships.rs:29-35](crates/gcode/src/graph/code_graph/read/relationships.rs#L29-L35), [crates/gcode/src/graph/code_graph/read/relationships.rs:37-48](crates/gcode/src/graph/code_graph/read/relationships.rs#L37-L48), [crates/gcode/src/graph/code_graph/read/relationships.rs:50-60](crates/gcode/src/graph/code_graph/read/relationships.rs#L50-L60), [crates/gcode/src/graph/code_graph/read/relationships.rs:62-72](crates/gcode/src/graph/code_graph/read/relationships.rs#L62-L72), [crates/gcode/src/graph/code_graph/read/relationships.rs:74-85](crates/gcode/src/graph/code_graph/read/relationships.rs#L74-L85), [crates/gcode/src/graph/code_graph/read/relationships.rs:87-98](crates/gcode/src/graph/code_graph/read/relationships.rs#L87-L98), [crates/gcode/src/graph/code_graph/read/relationships.rs:100-113](crates/gcode/src/graph/code_graph/read/relationships.rs#L100-L113), [crates/gcode/src/graph/code_graph/read/relationships.rs:115-124](crates/gcode/src/graph/code_graph/read/relationships.rs#L115-L124), [crates/gcode/src/graph/code_graph/read/relationships.rs:126-139](crates/gcode/src/graph/code_graph/read/relationships.rs#L126-L139), [crates/gcode/src/graph/code_graph/read/relationships.rs:141-157](crates/gcode/src/graph/code_graph/read/relationships.rs#L141-L157), [crates/gcode/src/graph/code_graph/read/relationships.rs:159-172](crates/gcode/src/graph/code_graph/read/relationships.rs#L159-L172), [crates/gcode/src/graph/code_graph/read/relationships.rs:174-190](crates/gcode/src/graph/code_graph/read/relationships.rs#L174-L190), [crates/gcode/src/graph/code_graph/read/relationships.rs:192-198](crates/gcode/src/graph/code_graph/read/relationships.rs#L192-L198), [crates/gcode/src/graph/code_graph/read/relationships.rs:200-225](crates/gcode/src/graph/code_graph/read/relationships.rs#L200-L225), [crates/gcode/src/graph/code_graph/read/relationships.rs:227-245](crates/gcode/src/graph/code_graph/read/relationships.rs#L227-L245), [crates/gcode/src/graph/code_graph/read/relationships.rs:247-263](crates/gcode/src/graph/code_graph/read/relationships.rs#L247-L263), [crates/gcode/src/graph/code_graph/read/relationships.rs:265-302](crates/gcode/src/graph/code_graph/read/relationships.rs#L265-L302), [crates/gcode/src/graph/code_graph/read/relationships.rs:304-342](crates/gcode/src/graph/code_graph/read/relationships.rs#L304-L342), [crates/gcode/src/graph/code_graph/read/relationships.rs:344-355](crates/gcode/src/graph/code_graph/read/relationships.rs#L344-L355), [crates/gcode/src/graph/code_graph/read/relationships.rs:361-366](crates/gcode/src/graph/code_graph/read/relationships.rs#L361-L366), [crates/gcode/src/graph/code_graph/read/relationships.rs:369-375](crates/gcode/src/graph/code_graph/read/relationships.rs#L369-L375), [crates/gcode/src/graph/code_graph/read/relationships.rs:378-386](crates/gcode/src/graph/code_graph/read/relationships.rs#L378-L386), [crates/gcode/src/graph/code_graph/read/relationships.rs:389-397](crates/gcode/src/graph/code_graph/read/relationships.rs#L389-L397)
- [crates/gcode/src/graph/code_graph/read/support.rs:43-97](crates/gcode/src/graph/code_graph/read/support.rs#L43-L97), [crates/gcode/src/graph/code_graph/read/support.rs:99-131](crates/gcode/src/graph/code_graph/read/support.rs#L99-L131), [crates/gcode/src/graph/code_graph/read/support.rs:133-142](crates/gcode/src/graph/code_graph/read/support.rs#L133-L142), [crates/gcode/src/graph/code_graph/read/support.rs:150-162](crates/gcode/src/graph/code_graph/read/support.rs#L150-L162), [crates/gcode/src/graph/code_graph/read/support.rs:165-187](crates/gcode/src/graph/code_graph/read/support.rs#L165-L187)
- [crates/gcode/src/graph/code_graph/tests.rs:7-21](crates/gcode/src/graph/code_graph/tests.rs#L7-L21), [crates/gcode/src/graph/code_graph/tests.rs:24-33](crates/gcode/src/graph/code_graph/tests.rs#L24-L33), [crates/gcode/src/graph/code_graph/tests.rs:36-65](crates/gcode/src/graph/code_graph/tests.rs#L36-L65), [crates/gcode/src/graph/code_graph/tests.rs:68-156](crates/gcode/src/graph/code_graph/tests.rs#L68-L156), [crates/gcode/src/graph/code_graph/tests.rs:159-164](crates/gcode/src/graph/code_graph/tests.rs#L159-L164), [crates/gcode/src/graph/code_graph/tests.rs:167-194](crates/gcode/src/graph/code_graph/tests.rs#L167-L194), [crates/gcode/src/graph/code_graph/tests.rs:197-203](crates/gcode/src/graph/code_graph/tests.rs#L197-L203), [crates/gcode/src/graph/code_graph/tests.rs:206-223](crates/gcode/src/graph/code_graph/tests.rs#L206-L223), [crates/gcode/src/graph/code_graph/tests.rs:226-242](crates/gcode/src/graph/code_graph/tests.rs#L226-L242), [crates/gcode/src/graph/code_graph/tests.rs:245-250](crates/gcode/src/graph/code_graph/tests.rs#L245-L250), [crates/gcode/src/graph/code_graph/tests.rs:253-276](crates/gcode/src/graph/code_graph/tests.rs#L253-L276), [crates/gcode/src/graph/code_graph/tests.rs:279-320](crates/gcode/src/graph/code_graph/tests.rs#L279-L320), [crates/gcode/src/graph/code_graph/tests.rs:323-327](crates/gcode/src/graph/code_graph/tests.rs#L323-L327), [crates/gcode/src/graph/code_graph/tests.rs:330-344](crates/gcode/src/graph/code_graph/tests.rs#L330-L344), [crates/gcode/src/graph/code_graph/tests.rs:347-357](crates/gcode/src/graph/code_graph/tests.rs#L347-L357), [crates/gcode/src/graph/code_graph/tests.rs:360-399](crates/gcode/src/graph/code_graph/tests.rs#L360-L399), [crates/gcode/src/graph/code_graph/tests.rs:402-449](crates/gcode/src/graph/code_graph/tests.rs#L402-L449), [crates/gcode/src/graph/code_graph/tests.rs:452-499](crates/gcode/src/graph/code_graph/tests.rs#L452-L499), [crates/gcode/src/graph/code_graph/tests.rs:502-521](crates/gcode/src/graph/code_graph/tests.rs#L502-L521), [crates/gcode/src/graph/code_graph/tests.rs:524-534](crates/gcode/src/graph/code_graph/tests.rs#L524-L534), [crates/gcode/src/graph/code_graph/tests.rs:537-564](crates/gcode/src/graph/code_graph/tests.rs#L537-L564), [crates/gcode/src/graph/code_graph/tests.rs:567-579](crates/gcode/src/graph/code_graph/tests.rs#L567-L579)
- [crates/gcode/src/graph/code_graph/write.rs:47-50](crates/gcode/src/graph/code_graph/write.rs#L47-L50), [crates/gcode/src/graph/code_graph/write.rs:53-56](crates/gcode/src/graph/code_graph/write.rs#L53-L56), [crates/gcode/src/graph/code_graph/write.rs:59-61](crates/gcode/src/graph/code_graph/write.rs#L59-L61), [crates/gcode/src/graph/code_graph/write.rs:63-101](crates/gcode/src/graph/code_graph/write.rs#L63-L101), [crates/gcode/src/graph/code_graph/write.rs:103-108](crates/gcode/src/graph/code_graph/write.rs#L103-L108), [crates/gcode/src/graph/code_graph/write.rs:110-120](crates/gcode/src/graph/code_graph/write.rs#L110-L120), [crates/gcode/src/graph/code_graph/write.rs:122-138](crates/gcode/src/graph/code_graph/write.rs#L122-L138), [crates/gcode/src/graph/code_graph/write.rs:140-159](crates/gcode/src/graph/code_graph/write.rs#L140-L159), [crates/gcode/src/graph/code_graph/write.rs:161-192](crates/gcode/src/graph/code_graph/write.rs#L161-L192), [crates/gcode/src/graph/code_graph/write.rs:194-203](crates/gcode/src/graph/code_graph/write.rs#L194-L203), [crates/gcode/src/graph/code_graph/write.rs:205-214](crates/gcode/src/graph/code_graph/write.rs#L205-L214), [crates/gcode/src/graph/code_graph/write.rs:216-221](crates/gcode/src/graph/code_graph/write.rs#L216-L221), [crates/gcode/src/graph/code_graph/write.rs:223-227](crates/gcode/src/graph/code_graph/write.rs#L223-L227), [crates/gcode/src/graph/code_graph/write.rs:229-234](crates/gcode/src/graph/code_graph/write.rs#L229-L234), [crates/gcode/src/graph/code_graph/write.rs:236-258](crates/gcode/src/graph/code_graph/write.rs#L236-L258), [crates/gcode/src/graph/code_graph/write.rs:260-271](crates/gcode/src/graph/code_graph/write.rs#L260-L271), [crates/gcode/src/graph/code_graph/write.rs:273-282](crates/gcode/src/graph/code_graph/write.rs#L273-L282), [crates/gcode/src/graph/code_graph/write.rs:284-286](crates/gcode/src/graph/code_graph/write.rs#L284-L286), [crates/gcode/src/graph/code_graph/write.rs:289-294](crates/gcode/src/graph/code_graph/write.rs#L289-L294), [crates/gcode/src/graph/code_graph/write.rs:296-307](crates/gcode/src/graph/code_graph/write.rs#L296-L307), [crates/gcode/src/graph/code_graph/write.rs:309-318](crates/gcode/src/graph/code_graph/write.rs#L309-L318), [crates/gcode/src/graph/code_graph/write.rs:320-328](crates/gcode/src/graph/code_graph/write.rs#L320-L328), [crates/gcode/src/graph/code_graph/write.rs:330-334](crates/gcode/src/graph/code_graph/write.rs#L330-L334), [crates/gcode/src/graph/code_graph/write.rs:336-338](crates/gcode/src/graph/code_graph/write.rs#L336-L338), [crates/gcode/src/graph/code_graph/write.rs:340-345](crates/gcode/src/graph/code_graph/write.rs#L340-L345), [crates/gcode/src/graph/code_graph/write.rs:347-351](crates/gcode/src/graph/code_graph/write.rs#L347-L351), [crates/gcode/src/graph/code_graph/write.rs:353-376](crates/gcode/src/graph/code_graph/write.rs#L353-L376)
- [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66](crates/gcode/src/graph/code_graph/write/deletion.rs#L8-L66), [crates/gcode/src/graph/code_graph/write/deletion.rs:68-113](crates/gcode/src/graph/code_graph/write/deletion.rs#L68-L113), [crates/gcode/src/graph/code_graph/write/deletion.rs:115-127](crates/gcode/src/graph/code_graph/write/deletion.rs#L115-L127), [crates/gcode/src/graph/code_graph/write/deletion.rs:129-145](crates/gcode/src/graph/code_graph/write/deletion.rs#L129-L145), [crates/gcode/src/graph/code_graph/write/deletion.rs:147-161](crates/gcode/src/graph/code_graph/write/deletion.rs#L147-L161), [crates/gcode/src/graph/code_graph/write/deletion.rs:163-171](crates/gcode/src/graph/code_graph/write/deletion.rs#L163-L171), [crates/gcode/src/graph/code_graph/write/deletion.rs:173-189](crates/gcode/src/graph/code_graph/write/deletion.rs#L173-L189), [crates/gcode/src/graph/code_graph/write/deletion.rs:191-200](crates/gcode/src/graph/code_graph/write/deletion.rs#L191-L200), [crates/gcode/src/graph/code_graph/write/deletion.rs:202-211](crates/gcode/src/graph/code_graph/write/deletion.rs#L202-L211)
- [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96](crates/gcode/src/graph/code_graph/write/mutation.rs#L89-L96), [crates/gcode/src/graph/code_graph/write/mutation.rs:99-102](crates/gcode/src/graph/code_graph/write/mutation.rs#L99-L102), [crates/gcode/src/graph/code_graph/write/mutation.rs:105-112](crates/gcode/src/graph/code_graph/write/mutation.rs#L105-L112), [crates/gcode/src/graph/code_graph/write/mutation.rs:115-119](crates/gcode/src/graph/code_graph/write/mutation.rs#L115-L119), [crates/gcode/src/graph/code_graph/write/mutation.rs:121-128](crates/gcode/src/graph/code_graph/write/mutation.rs#L121-L128), [crates/gcode/src/graph/code_graph/write/mutation.rs:130-145](crates/gcode/src/graph/code_graph/write/mutation.rs#L130-L145), [crates/gcode/src/graph/code_graph/write/mutation.rs:147-152](crates/gcode/src/graph/code_graph/write/mutation.rs#L147-L152), [crates/gcode/src/graph/code_graph/write/mutation.rs:154-182](crates/gcode/src/graph/code_graph/write/mutation.rs#L154-L182), [crates/gcode/src/graph/code_graph/write/mutation.rs:184-197](crates/gcode/src/graph/code_graph/write/mutation.rs#L184-L197), [crates/gcode/src/graph/code_graph/write/mutation.rs:199-207](crates/gcode/src/graph/code_graph/write/mutation.rs#L199-L207), [crates/gcode/src/graph/code_graph/write/mutation.rs:209-227](crates/gcode/src/graph/code_graph/write/mutation.rs#L209-L227), [crates/gcode/src/graph/code_graph/write/mutation.rs:229-259](crates/gcode/src/graph/code_graph/write/mutation.rs#L229-L259), [crates/gcode/src/graph/code_graph/write/mutation.rs:261-295](crates/gcode/src/graph/code_graph/write/mutation.rs#L261-L295), [crates/gcode/src/graph/code_graph/write/mutation.rs:297-301](crates/gcode/src/graph/code_graph/write/mutation.rs#L297-L301), [crates/gcode/src/graph/code_graph/write/mutation.rs:304-321](crates/gcode/src/graph/code_graph/write/mutation.rs#L304-L321), [crates/gcode/src/graph/code_graph/write/mutation.rs:323-327](crates/gcode/src/graph/code_graph/write/mutation.rs#L323-L327), [crates/gcode/src/graph/code_graph/write/mutation.rs:329-334](crates/gcode/src/graph/code_graph/write/mutation.rs#L329-L334), [crates/gcode/src/graph/code_graph/write/mutation.rs:337-343](crates/gcode/src/graph/code_graph/write/mutation.rs#L337-L343), [crates/gcode/src/graph/code_graph/write/mutation.rs:345-364](crates/gcode/src/graph/code_graph/write/mutation.rs#L345-L364), [crates/gcode/src/graph/code_graph/write/mutation.rs:366-377](crates/gcode/src/graph/code_graph/write/mutation.rs#L366-L377), [crates/gcode/src/graph/code_graph/write/mutation.rs:379-390](crates/gcode/src/graph/code_graph/write/mutation.rs#L379-L390), [crates/gcode/src/graph/code_graph/write/mutation.rs:392-403](crates/gcode/src/graph/code_graph/write/mutation.rs#L392-L403), [crates/gcode/src/graph/code_graph/write/mutation.rs:411-435](crates/gcode/src/graph/code_graph/write/mutation.rs#L411-L435), [crates/gcode/src/graph/code_graph/write/mutation.rs:438-450](crates/gcode/src/graph/code_graph/write/mutation.rs#L438-L450)
- [crates/gcode/src/graph/code_graph/write/support.rs:6-13](crates/gcode/src/graph/code_graph/write/support.rs#L6-L13), [crates/gcode/src/graph/code_graph/write/support.rs:15-21](crates/gcode/src/graph/code_graph/write/support.rs#L15-L21), [crates/gcode/src/graph/code_graph/write/support.rs:23-27](crates/gcode/src/graph/code_graph/write/support.rs#L23-L27), [crates/gcode/src/graph/code_graph/write/support.rs:29-31](crates/gcode/src/graph/code_graph/write/support.rs#L29-L31)
- [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L30-L81), [crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L89-L110), [crates/gcode/src/graph/code_graph/write/sync_plan.rs:113-156](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L113-L156), [crates/gcode/src/graph/code_graph/write/sync_plan.rs:159-177](crates/gcode/src/graph/code_graph/write/sync_plan.rs#L159-L177)
- [crates/gcode/src/graph/mod.rs:1-4](crates/gcode/src/graph/mod.rs#L1-L4)
- [crates/gcode/src/graph/report.rs:1-21](crates/gcode/src/graph/report.rs#L1-L21)
- [crates/gcode/src/graph/report/generation.rs:21-23](crates/gcode/src/graph/report/generation.rs#L21-L23), [crates/gcode/src/graph/report/generation.rs:25-59](crates/gcode/src/graph/report/generation.rs#L25-L59), [crates/gcode/src/graph/report/generation.rs:61-63](crates/gcode/src/graph/report/generation.rs#L61-L63), [crates/gcode/src/graph/report/generation.rs:65-76](crates/gcode/src/graph/report/generation.rs#L65-L76), [crates/gcode/src/graph/report/generation.rs:78-159](crates/gcode/src/graph/report/generation.rs#L78-L159)
- [crates/gcode/src/graph/report/loading.rs:18-78](crates/gcode/src/graph/report/loading.rs#L18-L78), [crates/gcode/src/graph/report/loading.rs:80-95](crates/gcode/src/graph/report/loading.rs#L80-L95), [crates/gcode/src/graph/report/loading.rs:97-111](crates/gcode/src/graph/report/loading.rs#L97-L111), [crates/gcode/src/graph/report/loading.rs:113-128](crates/gcode/src/graph/report/loading.rs#L113-L128), [crates/gcode/src/graph/report/loading.rs:130-146](crates/gcode/src/graph/report/loading.rs#L130-L146)
- [crates/gcode/src/graph/report/queries.rs:7-18](crates/gcode/src/graph/report/queries.rs#L7-L18), [crates/gcode/src/graph/report/queries.rs:20-22](crates/gcode/src/graph/report/queries.rs#L20-L22), [crates/gcode/src/graph/report/queries.rs:24-26](crates/gcode/src/graph/report/queries.rs#L24-L26), [crates/gcode/src/graph/report/queries.rs:28-38](crates/gcode/src/graph/report/queries.rs#L28-L38), [crates/gcode/src/graph/report/queries.rs:40-49](crates/gcode/src/graph/report/queries.rs#L40-L49), [crates/gcode/src/graph/report/queries.rs:51-85](crates/gcode/src/graph/report/queries.rs#L51-L85), [crates/gcode/src/graph/report/queries.rs:87-104](crates/gcode/src/graph/report/queries.rs#L87-L104), [crates/gcode/src/graph/report/queries.rs:106-126](crates/gcode/src/graph/report/queries.rs#L106-L126), [crates/gcode/src/graph/report/queries.rs:128-144](crates/gcode/src/graph/report/queries.rs#L128-L144)
- [crates/gcode/src/graph/report/render.rs:8-18](crates/gcode/src/graph/report/render.rs#L8-L18), [crates/gcode/src/graph/report/render.rs:20-99](crates/gcode/src/graph/report/render.rs#L20-L99), [crates/gcode/src/graph/report/render.rs:101-121](crates/gcode/src/graph/report/render.rs#L101-L121), [crates/gcode/src/graph/report/render.rs:123-141](crates/gcode/src/graph/report/render.rs#L123-L141), [crates/gcode/src/graph/report/render.rs:143-150](crates/gcode/src/graph/report/render.rs#L143-L150), [crates/gcode/src/graph/report/render.rs:152-164](crates/gcode/src/graph/report/render.rs#L152-L164), [crates/gcode/src/graph/report/render.rs:166-177](crates/gcode/src/graph/report/render.rs#L166-L177), [crates/gcode/src/graph/report/render.rs:179-185](crates/gcode/src/graph/report/render.rs#L179-L185)
- [crates/gcode/src/graph/report/rows.rs:11-19](crates/gcode/src/graph/report/rows.rs#L11-L19), [crates/gcode/src/graph/report/rows.rs:21-31](crates/gcode/src/graph/report/rows.rs#L21-L31), [crates/gcode/src/graph/report/rows.rs:33-39](crates/gcode/src/graph/report/rows.rs#L33-L39), [crates/gcode/src/graph/report/rows.rs:41-66](crates/gcode/src/graph/report/rows.rs#L41-L66), [crates/gcode/src/graph/report/rows.rs:68-78](crates/gcode/src/graph/report/rows.rs#L68-L78), [crates/gcode/src/graph/report/rows.rs:80-106](crates/gcode/src/graph/report/rows.rs#L80-L106), [crates/gcode/src/graph/report/rows.rs:108-112](crates/gcode/src/graph/report/rows.rs#L108-L112), [crates/gcode/src/graph/report/rows.rs:119-128](crates/gcode/src/graph/report/rows.rs#L119-L128), [crates/gcode/src/graph/report/rows.rs:131-140](crates/gcode/src/graph/report/rows.rs#L131-L140), [crates/gcode/src/graph/report/rows.rs:143-154](crates/gcode/src/graph/report/rows.rs#L143-L154), [crates/gcode/src/graph/report/rows.rs:157-162](crates/gcode/src/graph/report/rows.rs#L157-L162)
- [crates/gcode/src/graph/report/summary.rs:14-17](crates/gcode/src/graph/report/summary.rs#L14-L17), [crates/gcode/src/graph/report/summary.rs:19-41](crates/gcode/src/graph/report/summary.rs#L19-L41), [crates/gcode/src/graph/report/summary.rs:43-49](crates/gcode/src/graph/report/summary.rs#L43-L49), [crates/gcode/src/graph/report/summary.rs:51-91](crates/gcode/src/graph/report/summary.rs#L51-L91), [crates/gcode/src/graph/report/summary.rs:93-100](crates/gcode/src/graph/report/summary.rs#L93-L100), [crates/gcode/src/graph/report/summary.rs:102-156](crates/gcode/src/graph/report/summary.rs#L102-L156), [crates/gcode/src/graph/report/summary.rs:158-195](crates/gcode/src/graph/report/summary.rs#L158-L195), [crates/gcode/src/graph/report/summary.rs:197-231](crates/gcode/src/graph/report/summary.rs#L197-L231), [crates/gcode/src/graph/report/summary.rs:233-237](crates/gcode/src/graph/report/summary.rs#L233-L237), [crates/gcode/src/graph/report/summary.rs:239-248](crates/gcode/src/graph/report/summary.rs#L239-L248), [crates/gcode/src/graph/report/summary.rs:250-290](crates/gcode/src/graph/report/summary.rs#L250-L290), [crates/gcode/src/graph/report/summary.rs:294-308](crates/gcode/src/graph/report/summary.rs#L294-L308), [crates/gcode/src/graph/report/summary.rs:310-339](crates/gcode/src/graph/report/summary.rs#L310-L339), [crates/gcode/src/graph/report/summary.rs:341-349](crates/gcode/src/graph/report/summary.rs#L341-L349), [crates/gcode/src/graph/report/summary.rs:351-356](crates/gcode/src/graph/report/summary.rs#L351-L356)
- [crates/gcode/src/graph/report/tests.rs:15-65](crates/gcode/src/graph/report/tests.rs#L15-L65), [crates/gcode/src/graph/report/tests.rs:68-84](crates/gcode/src/graph/report/tests.rs#L68-L84), [crates/gcode/src/graph/report/tests.rs:87-127](crates/gcode/src/graph/report/tests.rs#L87-L127), [crates/gcode/src/graph/report/tests.rs:129-179](crates/gcode/src/graph/report/tests.rs#L129-L179), [crates/gcode/src/graph/report/tests.rs:181-196](crates/gcode/src/graph/report/tests.rs#L181-L196), [crates/gcode/src/graph/report/tests.rs:199-225](crates/gcode/src/graph/report/tests.rs#L199-L225), [crates/gcode/src/graph/report/tests.rs:228-249](crates/gcode/src/graph/report/tests.rs#L228-L249), [crates/gcode/src/graph/report/tests.rs:252-277](crates/gcode/src/graph/report/tests.rs#L252-L277), [crates/gcode/src/graph/report/tests.rs:280-317](crates/gcode/src/graph/report/tests.rs#L280-L317), [crates/gcode/src/graph/report/tests.rs:320-342](crates/gcode/src/graph/report/tests.rs#L320-L342), [crates/gcode/src/graph/report/tests.rs:345-390](crates/gcode/src/graph/report/tests.rs#L345-L390)
- [crates/gcode/src/graph/report/time.rs:3-5](crates/gcode/src/graph/report/time.rs#L3-L5)
- [crates/gcode/src/graph/report/types.rs:10-17](crates/gcode/src/graph/report/types.rs#L10-L17), [crates/gcode/src/graph/report/types.rs:20-34](crates/gcode/src/graph/report/types.rs#L20-L34), [crates/gcode/src/graph/report/types.rs:36-49](crates/gcode/src/graph/report/types.rs#L36-L49), [crates/gcode/src/graph/report/types.rs:53-68](crates/gcode/src/graph/report/types.rs#L53-L68), [crates/gcode/src/graph/report/types.rs:71-73](crates/gcode/src/graph/report/types.rs#L71-L73), [crates/gcode/src/graph/report/types.rs:76-80](crates/gcode/src/graph/report/types.rs#L76-L80), [crates/gcode/src/graph/report/types.rs:84-88](crates/gcode/src/graph/report/types.rs#L84-L88), [crates/gcode/src/graph/report/types.rs:92-97](crates/gcode/src/graph/report/types.rs#L92-L97), [crates/gcode/src/graph/report/types.rs:100-105](crates/gcode/src/graph/report/types.rs#L100-L105), [crates/gcode/src/graph/report/types.rs:108-118](crates/gcode/src/graph/report/types.rs#L108-L118), [crates/gcode/src/graph/report/types.rs:121-125](crates/gcode/src/graph/report/types.rs#L121-L125), [crates/gcode/src/graph/report/types.rs:128-136](crates/gcode/src/graph/report/types.rs#L128-L136), [crates/gcode/src/graph/report/types.rs:139-142](crates/gcode/src/graph/report/types.rs#L139-L142), [crates/gcode/src/graph/report/types.rs:145-148](crates/gcode/src/graph/report/types.rs#L145-L148), [crates/gcode/src/graph/report/types.rs:151-155](crates/gcode/src/graph/report/types.rs#L151-L155), [crates/gcode/src/graph/report/types.rs:158-162](crates/gcode/src/graph/report/types.rs#L158-L162), [crates/gcode/src/graph/report/types.rs:165-178](crates/gcode/src/graph/report/types.rs#L165-L178), [crates/gcode/src/graph/report/types.rs:184-192](crates/gcode/src/graph/report/types.rs#L184-L192), [crates/gcode/src/graph/report/types.rs:195-200](crates/gcode/src/graph/report/types.rs#L195-L200), [crates/gcode/src/graph/report/types.rs:204-215](crates/gcode/src/graph/report/types.rs#L204-L215), [crates/gcode/src/graph/report/types.rs:218-221](crates/gcode/src/graph/report/types.rs#L218-L221), [crates/gcode/src/graph/report/types.rs:225-229](crates/gcode/src/graph/report/types.rs#L225-L229), [crates/gcode/src/graph/report/types.rs:233-243](crates/gcode/src/graph/report/types.rs#L233-L243), [crates/gcode/src/graph/report/types.rs:247-251](crates/gcode/src/graph/report/types.rs#L247-L251), [crates/gcode/src/graph/report/types.rs:254-256](crates/gcode/src/graph/report/types.rs#L254-L256), [crates/gcode/src/graph/report/types.rs:259-261](crates/gcode/src/graph/report/types.rs#L259-L261), [crates/gcode/src/graph/report/types.rs:265-267](crates/gcode/src/graph/report/types.rs#L265-L267)
- [crates/gcode/src/graph/typed_query.rs:7-10](crates/gcode/src/graph/typed_query.rs#L7-L10), [crates/gcode/src/graph/typed_query.rs:13-21](crates/gcode/src/graph/typed_query.rs#L13-L21), [crates/gcode/src/graph/typed_query.rs:24-27](crates/gcode/src/graph/typed_query.rs#L24-L27), [crates/gcode/src/graph/typed_query.rs:30-38](crates/gcode/src/graph/typed_query.rs#L30-L38), [crates/gcode/src/graph/typed_query.rs:41-46](crates/gcode/src/graph/typed_query.rs#L41-L46), [crates/gcode/src/graph/typed_query.rs:48-58](crates/gcode/src/graph/typed_query.rs#L48-L58), [crates/gcode/src/graph/typed_query.rs:60-70](crates/gcode/src/graph/typed_query.rs#L60-L70), [crates/gcode/src/graph/typed_query.rs:73-75](crates/gcode/src/graph/typed_query.rs#L73-L75), [crates/gcode/src/graph/typed_query.rs:77-98](crates/gcode/src/graph/typed_query.rs#L77-L98), [crates/gcode/src/graph/typed_query.rs:100-105](crates/gcode/src/graph/typed_query.rs#L100-L105), [crates/gcode/src/graph/typed_query.rs:107-109](crates/gcode/src/graph/typed_query.rs#L107-L109), [crates/gcode/src/graph/typed_query.rs:111-113](crates/gcode/src/graph/typed_query.rs#L111-L113), [crates/gcode/src/graph/typed_query.rs:115-120](crates/gcode/src/graph/typed_query.rs#L115-L120), [crates/gcode/src/graph/typed_query.rs:122-141](crates/gcode/src/graph/typed_query.rs#L122-L141), [crates/gcode/src/graph/typed_query.rs:143-145](crates/gcode/src/graph/typed_query.rs#L143-L145), [crates/gcode/src/graph/typed_query.rs:147-164](crates/gcode/src/graph/typed_query.rs#L147-L164), [crates/gcode/src/graph/typed_query.rs:166-178](crates/gcode/src/graph/typed_query.rs#L166-L178), [crates/gcode/src/graph/typed_query.rs:181-186](crates/gcode/src/graph/typed_query.rs#L181-L186), [crates/gcode/src/graph/typed_query.rs:190-200](crates/gcode/src/graph/typed_query.rs#L190-L200), [crates/gcode/src/graph/typed_query.rs:211-276](crates/gcode/src/graph/typed_query.rs#L211-L276), [crates/gcode/src/graph/typed_query.rs:279-284](crates/gcode/src/graph/typed_query.rs#L279-L284), [crates/gcode/src/graph/typed_query.rs:287-297](crates/gcode/src/graph/typed_query.rs#L287-L297), [crates/gcode/src/graph/typed_query.rs:300-315](crates/gcode/src/graph/typed_query.rs#L300-L315), [crates/gcode/src/graph/typed_query.rs:318-341](crates/gcode/src/graph/typed_query.rs#L318-L341), [crates/gcode/src/graph/typed_query.rs:344-350](crates/gcode/src/graph/typed_query.rs#L344-L350)

</details>

# FalkorDB Graph Synchronization

## Overview

Maintains relational projections representing call graph and dependency trees downstream in a FalkorDB instance.

## Reference Modules

- [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]
- [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]
- [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]
- [[code/modules/crates/gcode/src/graph/code_graph/write|crates/gcode/src/graph/code_graph/write]]
- [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Source Files

- [[code/files/crates/gcode/src/graph/code_graph.rs|crates/gcode/src/graph/code_graph.rs]]
- [[code/files/crates/gcode/src/graph/code_graph/connection.rs|crates/gcode/src/graph/code_graph/connection.rs]]
- [[code/files/crates/gcode/src/graph/code_graph/lifecycle.rs|crates/gcode/src/graph/code_graph/lifecycle.rs]]
- [[code/files/crates/gcode/src/graph/code_graph/payload.rs|crates/gcode/src/graph/code_graph/payload.rs]]
- [[code/files/crates/gcode/src/graph/code_graph/read.rs|crates/gcode/src/graph/code_graph/read.rs]]
- [[code/files/crates/gcode/src/graph/code_graph/read/graph_payloads.rs|crates/gcode/src/graph/code_graph/read/graph_payloads.rs]]
