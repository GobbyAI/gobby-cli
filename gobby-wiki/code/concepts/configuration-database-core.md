---
title: Configuration & Database Core
type: code_concept
provenance:
- file: crates/gcode/src/config.rs
  ranges:
  - 1-25
- file: crates/gcode/src/config/context.rs
  ranges:
  - 26-31
  - '34'
  - '37'
  - 51-53
  - '55'
  - 58-63
  - 66-73
  - 75-82
  - 84-91
  - 93-100
  - 102-109
  - 111-118
  - 120-127
  - 131-133
  - 137-140
  - 143-151
  - 157-163
  - 168-191
  - 194-203
  - 206-209
  - 212-219
  - 222-229
  - 233-235
  - 237-302
  - 305-352
  - 355-408
  - 410-464
  - 466-474
  - 476-484
  - 486-494
  - 496-527
  - 529-536
  - 541-565
  - 567-569
  - 577-580
  - 582-618
  - 627-629
  - 631-639
- file: crates/gcode/src/config/services.rs
  ranges:
  - 20-22
  - 24-27
  - 29-39
  - 41-48
  - 51-57
  - 59-61
  - 64-67
  - 70-81
  - 83-85
  - 89-93
  - 95-99
  - 102-104
  - 108-125
  - 127-129
  - 132-135
  - 138-143
  - 150-162
  - 164-166
  - 169-178
  - 181-196
  - 199-221
  - 226-241
  - 244-247
  - 255-257
  - 259-261
  - 270-276
  - 278-280
  - 284-287
  - 295-301
  - 303-305
  - 309-322
  - 325-338
  - 341-354
  - 357-370
  - 373-384
  - 389-399
  - 401-416
  - 421-431
  - 433-442
  - 444-452
  - 454-469
  - 471-494
  - 501-511
  - 513-533
  - 535-545
  - 547-557
  - 559-568
  - 570-576
  - 578-587
  - 589-603
  - 605-611
  - 613-624
  - 626-635
- file: crates/gcode/src/config/tests.rs
  ranges:
  - 14-22
  - 24-38
  - 40-70
  - 80-90
  - 92-96
  - 100-140
  - 143-148
  - 152-166
  - 170-191
  - 195-229
  - 232-242
  - 246-268
  - 272-295
  - 299-313
  - 317-333
  - 336-348
  - 351-367
  - 370-389
  - 392-426
  - 429-449
  - 452-466
  - 469-500
  - 503-515
  - 518-529
  - 532-539
  - 542-553
- file: crates/gcode/src/db/mod.rs
  ranges:
  - 16-20
  - 27-31
  - 33-35
- file: crates/gcode/src/db/queries.rs
  ranges:
  - 8-13
  - 15-26
  - 28-38
  - 40-55
  - 57-69
  - 71-83
  - 85-97
  - 99-109
  - 111-123
  - 125-135
  - 141-156
  - 158-168
  - 170-190
  - 192-205
  - 207-221
  - 223-236
  - 241-259
  - 261-274
  - 289-321
  - 323-357
  - 360-364
  - 366-413
  - 415-425
  - 427-432
  - 434-436
  - 438-449
  - 451-470
  - 472-481
  - 487-497
  - 500-507
  - 510-520
  - 523-530
  - 533-544
  - 547-554
  - 557-561
  - 565-567
- file: crates/gcode/src/db/resolution.rs
  ranges:
  - 16-18
  - 21-24
  - 27-29
  - 31-33
  - 39-48
  - 51-64
  - 67-81
  - 83-138
  - 140-156
  - 158-166
  - 168-175
  - 177-186
  - 188-211
  - 213-226
  - 228-235
  - 237-244
  - 246-255
  - 257-280
  - 282-284
  - 286-300
  - 302-323
  - 325-353
  - 362-367
  - 370-378
  - 381-388
  - 391-399
  - 402-417
  - 420-432
  - 435-452
  - 455-472
  - 475-500
  - 503-511
  - 514-521
  - 524-529
  - 532-537
  - 540-552
  - 555-572
  - 575-583
  - 586-597
  - 600-604
  - 607-613
  - 616-622
  - 625-633
  - 636-648
  - 651-665
  - 668-682
  - 685-696
  - 699-711
  - 714-722
  - 725-733
  - 736-744
  - 746-754
  - 756-761
  - 763-765
  - 767-794
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/config.rs:1-25](crates/gcode/src/config.rs#L1-L25)
- [crates/gcode/src/config/context.rs:26-31](crates/gcode/src/config/context.rs#L26-L31), [crates/gcode/src/config/context.rs:34](crates/gcode/src/config/context.rs#L34), [crates/gcode/src/config/context.rs:37](crates/gcode/src/config/context.rs#L37), [crates/gcode/src/config/context.rs:51-53](crates/gcode/src/config/context.rs#L51-L53), [crates/gcode/src/config/context.rs:55](crates/gcode/src/config/context.rs#L55), [crates/gcode/src/config/context.rs:58-63](crates/gcode/src/config/context.rs#L58-L63), [crates/gcode/src/config/context.rs:66-73](crates/gcode/src/config/context.rs#L66-L73), [crates/gcode/src/config/context.rs:75-82](crates/gcode/src/config/context.rs#L75-L82), [crates/gcode/src/config/context.rs:84-91](crates/gcode/src/config/context.rs#L84-L91), [crates/gcode/src/config/context.rs:93-100](crates/gcode/src/config/context.rs#L93-L100), [crates/gcode/src/config/context.rs:102-109](crates/gcode/src/config/context.rs#L102-L109), [crates/gcode/src/config/context.rs:111-118](crates/gcode/src/config/context.rs#L111-L118), [crates/gcode/src/config/context.rs:120-127](crates/gcode/src/config/context.rs#L120-L127), [crates/gcode/src/config/context.rs:131-133](crates/gcode/src/config/context.rs#L131-L133), [crates/gcode/src/config/context.rs:137-140](crates/gcode/src/config/context.rs#L137-L140), [crates/gcode/src/config/context.rs:143-151](crates/gcode/src/config/context.rs#L143-L151), [crates/gcode/src/config/context.rs:157-163](crates/gcode/src/config/context.rs#L157-L163), [crates/gcode/src/config/context.rs:168-191](crates/gcode/src/config/context.rs#L168-L191), [crates/gcode/src/config/context.rs:194-203](crates/gcode/src/config/context.rs#L194-L203), [crates/gcode/src/config/context.rs:206-209](crates/gcode/src/config/context.rs#L206-L209), [crates/gcode/src/config/context.rs:212-219](crates/gcode/src/config/context.rs#L212-L219), [crates/gcode/src/config/context.rs:222-229](crates/gcode/src/config/context.rs#L222-L229), [crates/gcode/src/config/context.rs:233-235](crates/gcode/src/config/context.rs#L233-L235), [crates/gcode/src/config/context.rs:237-302](crates/gcode/src/config/context.rs#L237-L302), [crates/gcode/src/config/context.rs:305-352](crates/gcode/src/config/context.rs#L305-L352), [crates/gcode/src/config/context.rs:355-408](crates/gcode/src/config/context.rs#L355-L408), [crates/gcode/src/config/context.rs:410-464](crates/gcode/src/config/context.rs#L410-L464), [crates/gcode/src/config/context.rs:466-474](crates/gcode/src/config/context.rs#L466-L474), [crates/gcode/src/config/context.rs:476-484](crates/gcode/src/config/context.rs#L476-L484), [crates/gcode/src/config/context.rs:486-494](crates/gcode/src/config/context.rs#L486-L494), [crates/gcode/src/config/context.rs:496-527](crates/gcode/src/config/context.rs#L496-L527), [crates/gcode/src/config/context.rs:529-536](crates/gcode/src/config/context.rs#L529-L536), [crates/gcode/src/config/context.rs:541-565](crates/gcode/src/config/context.rs#L541-L565), [crates/gcode/src/config/context.rs:567-569](crates/gcode/src/config/context.rs#L567-L569), [crates/gcode/src/config/context.rs:577-580](crates/gcode/src/config/context.rs#L577-L580), [crates/gcode/src/config/context.rs:582-618](crates/gcode/src/config/context.rs#L582-L618), [crates/gcode/src/config/context.rs:627-629](crates/gcode/src/config/context.rs#L627-L629), [crates/gcode/src/config/context.rs:631-639](crates/gcode/src/config/context.rs#L631-L639)
- [crates/gcode/src/config/services.rs:20-22](crates/gcode/src/config/services.rs#L20-L22), [crates/gcode/src/config/services.rs:24-27](crates/gcode/src/config/services.rs#L24-L27), [crates/gcode/src/config/services.rs:29-39](crates/gcode/src/config/services.rs#L29-L39), [crates/gcode/src/config/services.rs:41-48](crates/gcode/src/config/services.rs#L41-L48), [crates/gcode/src/config/services.rs:51-57](crates/gcode/src/config/services.rs#L51-L57), [crates/gcode/src/config/services.rs:59-61](crates/gcode/src/config/services.rs#L59-L61), [crates/gcode/src/config/services.rs:64-67](crates/gcode/src/config/services.rs#L64-L67), [crates/gcode/src/config/services.rs:70-81](crates/gcode/src/config/services.rs#L70-L81), [crates/gcode/src/config/services.rs:83-85](crates/gcode/src/config/services.rs#L83-L85), [crates/gcode/src/config/services.rs:89-93](crates/gcode/src/config/services.rs#L89-L93), [crates/gcode/src/config/services.rs:95-99](crates/gcode/src/config/services.rs#L95-L99), [crates/gcode/src/config/services.rs:102-104](crates/gcode/src/config/services.rs#L102-L104), [crates/gcode/src/config/services.rs:108-125](crates/gcode/src/config/services.rs#L108-L125), [crates/gcode/src/config/services.rs:127-129](crates/gcode/src/config/services.rs#L127-L129), [crates/gcode/src/config/services.rs:132-135](crates/gcode/src/config/services.rs#L132-L135), [crates/gcode/src/config/services.rs:138-143](crates/gcode/src/config/services.rs#L138-L143), [crates/gcode/src/config/services.rs:150-162](crates/gcode/src/config/services.rs#L150-L162), [crates/gcode/src/config/services.rs:164-166](crates/gcode/src/config/services.rs#L164-L166), [crates/gcode/src/config/services.rs:169-178](crates/gcode/src/config/services.rs#L169-L178), [crates/gcode/src/config/services.rs:181-196](crates/gcode/src/config/services.rs#L181-L196), [crates/gcode/src/config/services.rs:199-221](crates/gcode/src/config/services.rs#L199-L221), [crates/gcode/src/config/services.rs:226-241](crates/gcode/src/config/services.rs#L226-L241), [crates/gcode/src/config/services.rs:244-247](crates/gcode/src/config/services.rs#L244-L247), [crates/gcode/src/config/services.rs:255-257](crates/gcode/src/config/services.rs#L255-L257), [crates/gcode/src/config/services.rs:259-261](crates/gcode/src/config/services.rs#L259-L261), [crates/gcode/src/config/services.rs:270-276](crates/gcode/src/config/services.rs#L270-L276), [crates/gcode/src/config/services.rs:278-280](crates/gcode/src/config/services.rs#L278-L280), [crates/gcode/src/config/services.rs:284-287](crates/gcode/src/config/services.rs#L284-L287), [crates/gcode/src/config/services.rs:295-301](crates/gcode/src/config/services.rs#L295-L301), [crates/gcode/src/config/services.rs:303-305](crates/gcode/src/config/services.rs#L303-L305), [crates/gcode/src/config/services.rs:309-322](crates/gcode/src/config/services.rs#L309-L322), [crates/gcode/src/config/services.rs:325-338](crates/gcode/src/config/services.rs#L325-L338), [crates/gcode/src/config/services.rs:341-354](crates/gcode/src/config/services.rs#L341-L354), [crates/gcode/src/config/services.rs:357-370](crates/gcode/src/config/services.rs#L357-L370), [crates/gcode/src/config/services.rs:373-384](crates/gcode/src/config/services.rs#L373-L384), [crates/gcode/src/config/services.rs:389-399](crates/gcode/src/config/services.rs#L389-L399), [crates/gcode/src/config/services.rs:401-416](crates/gcode/src/config/services.rs#L401-L416), [crates/gcode/src/config/services.rs:421-431](crates/gcode/src/config/services.rs#L421-L431), [crates/gcode/src/config/services.rs:433-442](crates/gcode/src/config/services.rs#L433-L442), [crates/gcode/src/config/services.rs:444-452](crates/gcode/src/config/services.rs#L444-L452), [crates/gcode/src/config/services.rs:454-469](crates/gcode/src/config/services.rs#L454-L469), [crates/gcode/src/config/services.rs:471-494](crates/gcode/src/config/services.rs#L471-L494), [crates/gcode/src/config/services.rs:501-511](crates/gcode/src/config/services.rs#L501-L511), [crates/gcode/src/config/services.rs:513-533](crates/gcode/src/config/services.rs#L513-L533), [crates/gcode/src/config/services.rs:535-545](crates/gcode/src/config/services.rs#L535-L545), [crates/gcode/src/config/services.rs:547-557](crates/gcode/src/config/services.rs#L547-L557), [crates/gcode/src/config/services.rs:559-568](crates/gcode/src/config/services.rs#L559-L568), [crates/gcode/src/config/services.rs:570-576](crates/gcode/src/config/services.rs#L570-L576), [crates/gcode/src/config/services.rs:578-587](crates/gcode/src/config/services.rs#L578-L587), [crates/gcode/src/config/services.rs:589-603](crates/gcode/src/config/services.rs#L589-L603), [crates/gcode/src/config/services.rs:605-611](crates/gcode/src/config/services.rs#L605-L611), [crates/gcode/src/config/services.rs:613-624](crates/gcode/src/config/services.rs#L613-L624), [crates/gcode/src/config/services.rs:626-635](crates/gcode/src/config/services.rs#L626-L635)
- [crates/gcode/src/config/tests.rs:14-22](crates/gcode/src/config/tests.rs#L14-L22), [crates/gcode/src/config/tests.rs:24-38](crates/gcode/src/config/tests.rs#L24-L38), [crates/gcode/src/config/tests.rs:40-70](crates/gcode/src/config/tests.rs#L40-L70), [crates/gcode/src/config/tests.rs:80-90](crates/gcode/src/config/tests.rs#L80-L90), [crates/gcode/src/config/tests.rs:92-96](crates/gcode/src/config/tests.rs#L92-L96), [crates/gcode/src/config/tests.rs:100-140](crates/gcode/src/config/tests.rs#L100-L140), [crates/gcode/src/config/tests.rs:143-148](crates/gcode/src/config/tests.rs#L143-L148), [crates/gcode/src/config/tests.rs:152-166](crates/gcode/src/config/tests.rs#L152-L166), [crates/gcode/src/config/tests.rs:170-191](crates/gcode/src/config/tests.rs#L170-L191), [crates/gcode/src/config/tests.rs:195-229](crates/gcode/src/config/tests.rs#L195-L229), [crates/gcode/src/config/tests.rs:232-242](crates/gcode/src/config/tests.rs#L232-L242), [crates/gcode/src/config/tests.rs:246-268](crates/gcode/src/config/tests.rs#L246-L268), [crates/gcode/src/config/tests.rs:272-295](crates/gcode/src/config/tests.rs#L272-L295), [crates/gcode/src/config/tests.rs:299-313](crates/gcode/src/config/tests.rs#L299-L313), [crates/gcode/src/config/tests.rs:317-333](crates/gcode/src/config/tests.rs#L317-L333), [crates/gcode/src/config/tests.rs:336-348](crates/gcode/src/config/tests.rs#L336-L348), [crates/gcode/src/config/tests.rs:351-367](crates/gcode/src/config/tests.rs#L351-L367), [crates/gcode/src/config/tests.rs:370-389](crates/gcode/src/config/tests.rs#L370-L389), [crates/gcode/src/config/tests.rs:392-426](crates/gcode/src/config/tests.rs#L392-L426), [crates/gcode/src/config/tests.rs:429-449](crates/gcode/src/config/tests.rs#L429-L449), [crates/gcode/src/config/tests.rs:452-466](crates/gcode/src/config/tests.rs#L452-L466), [crates/gcode/src/config/tests.rs:469-500](crates/gcode/src/config/tests.rs#L469-L500), [crates/gcode/src/config/tests.rs:503-515](crates/gcode/src/config/tests.rs#L503-L515), [crates/gcode/src/config/tests.rs:518-529](crates/gcode/src/config/tests.rs#L518-L529), [crates/gcode/src/config/tests.rs:532-539](crates/gcode/src/config/tests.rs#L532-L539), [crates/gcode/src/config/tests.rs:542-553](crates/gcode/src/config/tests.rs#L542-L553)
- [crates/gcode/src/db/mod.rs:16-20](crates/gcode/src/db/mod.rs#L16-L20), [crates/gcode/src/db/mod.rs:27-31](crates/gcode/src/db/mod.rs#L27-L31), [crates/gcode/src/db/mod.rs:33-35](crates/gcode/src/db/mod.rs#L33-L35)
- [crates/gcode/src/db/queries.rs:8-13](crates/gcode/src/db/queries.rs#L8-L13), [crates/gcode/src/db/queries.rs:15-26](crates/gcode/src/db/queries.rs#L15-L26), [crates/gcode/src/db/queries.rs:28-38](crates/gcode/src/db/queries.rs#L28-L38), [crates/gcode/src/db/queries.rs:40-55](crates/gcode/src/db/queries.rs#L40-L55), [crates/gcode/src/db/queries.rs:57-69](crates/gcode/src/db/queries.rs#L57-L69), [crates/gcode/src/db/queries.rs:71-83](crates/gcode/src/db/queries.rs#L71-L83), [crates/gcode/src/db/queries.rs:85-97](crates/gcode/src/db/queries.rs#L85-L97), [crates/gcode/src/db/queries.rs:99-109](crates/gcode/src/db/queries.rs#L99-L109), [crates/gcode/src/db/queries.rs:111-123](crates/gcode/src/db/queries.rs#L111-L123), [crates/gcode/src/db/queries.rs:125-135](crates/gcode/src/db/queries.rs#L125-L135), [crates/gcode/src/db/queries.rs:141-156](crates/gcode/src/db/queries.rs#L141-L156), [crates/gcode/src/db/queries.rs:158-168](crates/gcode/src/db/queries.rs#L158-L168), [crates/gcode/src/db/queries.rs:170-190](crates/gcode/src/db/queries.rs#L170-L190), [crates/gcode/src/db/queries.rs:192-205](crates/gcode/src/db/queries.rs#L192-L205), [crates/gcode/src/db/queries.rs:207-221](crates/gcode/src/db/queries.rs#L207-L221), [crates/gcode/src/db/queries.rs:223-236](crates/gcode/src/db/queries.rs#L223-L236), [crates/gcode/src/db/queries.rs:241-259](crates/gcode/src/db/queries.rs#L241-L259), [crates/gcode/src/db/queries.rs:261-274](crates/gcode/src/db/queries.rs#L261-L274), [crates/gcode/src/db/queries.rs:289-321](crates/gcode/src/db/queries.rs#L289-L321), [crates/gcode/src/db/queries.rs:323-357](crates/gcode/src/db/queries.rs#L323-L357), [crates/gcode/src/db/queries.rs:360-364](crates/gcode/src/db/queries.rs#L360-L364), [crates/gcode/src/db/queries.rs:366-413](crates/gcode/src/db/queries.rs#L366-L413), [crates/gcode/src/db/queries.rs:415-425](crates/gcode/src/db/queries.rs#L415-L425), [crates/gcode/src/db/queries.rs:427-432](crates/gcode/src/db/queries.rs#L427-L432), [crates/gcode/src/db/queries.rs:434-436](crates/gcode/src/db/queries.rs#L434-L436), [crates/gcode/src/db/queries.rs:438-449](crates/gcode/src/db/queries.rs#L438-L449), [crates/gcode/src/db/queries.rs:451-470](crates/gcode/src/db/queries.rs#L451-L470), [crates/gcode/src/db/queries.rs:472-481](crates/gcode/src/db/queries.rs#L472-L481), [crates/gcode/src/db/queries.rs:487-497](crates/gcode/src/db/queries.rs#L487-L497), [crates/gcode/src/db/queries.rs:500-507](crates/gcode/src/db/queries.rs#L500-L507), [crates/gcode/src/db/queries.rs:510-520](crates/gcode/src/db/queries.rs#L510-L520), [crates/gcode/src/db/queries.rs:523-530](crates/gcode/src/db/queries.rs#L523-L530), [crates/gcode/src/db/queries.rs:533-544](crates/gcode/src/db/queries.rs#L533-L544), [crates/gcode/src/db/queries.rs:547-554](crates/gcode/src/db/queries.rs#L547-L554), [crates/gcode/src/db/queries.rs:557-561](crates/gcode/src/db/queries.rs#L557-L561), [crates/gcode/src/db/queries.rs:565-567](crates/gcode/src/db/queries.rs#L565-L567)
- [crates/gcode/src/db/resolution.rs:16-18](crates/gcode/src/db/resolution.rs#L16-L18), [crates/gcode/src/db/resolution.rs:21-24](crates/gcode/src/db/resolution.rs#L21-L24), [crates/gcode/src/db/resolution.rs:27-29](crates/gcode/src/db/resolution.rs#L27-L29), [crates/gcode/src/db/resolution.rs:31-33](crates/gcode/src/db/resolution.rs#L31-L33), [crates/gcode/src/db/resolution.rs:39-48](crates/gcode/src/db/resolution.rs#L39-L48), [crates/gcode/src/db/resolution.rs:51-64](crates/gcode/src/db/resolution.rs#L51-L64), [crates/gcode/src/db/resolution.rs:67-81](crates/gcode/src/db/resolution.rs#L67-L81), [crates/gcode/src/db/resolution.rs:83-138](crates/gcode/src/db/resolution.rs#L83-L138), [crates/gcode/src/db/resolution.rs:140-156](crates/gcode/src/db/resolution.rs#L140-L156), [crates/gcode/src/db/resolution.rs:158-166](crates/gcode/src/db/resolution.rs#L158-L166), [crates/gcode/src/db/resolution.rs:168-175](crates/gcode/src/db/resolution.rs#L168-L175), [crates/gcode/src/db/resolution.rs:177-186](crates/gcode/src/db/resolution.rs#L177-L186), [crates/gcode/src/db/resolution.rs:188-211](crates/gcode/src/db/resolution.rs#L188-L211), [crates/gcode/src/db/resolution.rs:213-226](crates/gcode/src/db/resolution.rs#L213-L226), [crates/gcode/src/db/resolution.rs:228-235](crates/gcode/src/db/resolution.rs#L228-L235), [crates/gcode/src/db/resolution.rs:237-244](crates/gcode/src/db/resolution.rs#L237-L244), [crates/gcode/src/db/resolution.rs:246-255](crates/gcode/src/db/resolution.rs#L246-L255), [crates/gcode/src/db/resolution.rs:257-280](crates/gcode/src/db/resolution.rs#L257-L280), [crates/gcode/src/db/resolution.rs:282-284](crates/gcode/src/db/resolution.rs#L282-L284), [crates/gcode/src/db/resolution.rs:286-300](crates/gcode/src/db/resolution.rs#L286-L300), [crates/gcode/src/db/resolution.rs:302-323](crates/gcode/src/db/resolution.rs#L302-L323), [crates/gcode/src/db/resolution.rs:325-353](crates/gcode/src/db/resolution.rs#L325-L353), [crates/gcode/src/db/resolution.rs:362-367](crates/gcode/src/db/resolution.rs#L362-L367), [crates/gcode/src/db/resolution.rs:370-378](crates/gcode/src/db/resolution.rs#L370-L378), [crates/gcode/src/db/resolution.rs:381-388](crates/gcode/src/db/resolution.rs#L381-L388), [crates/gcode/src/db/resolution.rs:391-399](crates/gcode/src/db/resolution.rs#L391-L399), [crates/gcode/src/db/resolution.rs:402-417](crates/gcode/src/db/resolution.rs#L402-L417), [crates/gcode/src/db/resolution.rs:420-432](crates/gcode/src/db/resolution.rs#L420-L432), [crates/gcode/src/db/resolution.rs:435-452](crates/gcode/src/db/resolution.rs#L435-L452), [crates/gcode/src/db/resolution.rs:455-472](crates/gcode/src/db/resolution.rs#L455-L472), [crates/gcode/src/db/resolution.rs:475-500](crates/gcode/src/db/resolution.rs#L475-L500), [crates/gcode/src/db/resolution.rs:503-511](crates/gcode/src/db/resolution.rs#L503-L511), [crates/gcode/src/db/resolution.rs:514-521](crates/gcode/src/db/resolution.rs#L514-L521), [crates/gcode/src/db/resolution.rs:524-529](crates/gcode/src/db/resolution.rs#L524-L529), [crates/gcode/src/db/resolution.rs:532-537](crates/gcode/src/db/resolution.rs#L532-L537), [crates/gcode/src/db/resolution.rs:540-552](crates/gcode/src/db/resolution.rs#L540-L552), [crates/gcode/src/db/resolution.rs:555-572](crates/gcode/src/db/resolution.rs#L555-L572), [crates/gcode/src/db/resolution.rs:575-583](crates/gcode/src/db/resolution.rs#L575-L583), [crates/gcode/src/db/resolution.rs:586-597](crates/gcode/src/db/resolution.rs#L586-L597), [crates/gcode/src/db/resolution.rs:600-604](crates/gcode/src/db/resolution.rs#L600-L604), [crates/gcode/src/db/resolution.rs:607-613](crates/gcode/src/db/resolution.rs#L607-L613), [crates/gcode/src/db/resolution.rs:616-622](crates/gcode/src/db/resolution.rs#L616-L622), [crates/gcode/src/db/resolution.rs:625-633](crates/gcode/src/db/resolution.rs#L625-L633), [crates/gcode/src/db/resolution.rs:636-648](crates/gcode/src/db/resolution.rs#L636-L648), [crates/gcode/src/db/resolution.rs:651-665](crates/gcode/src/db/resolution.rs#L651-L665), [crates/gcode/src/db/resolution.rs:668-682](crates/gcode/src/db/resolution.rs#L668-L682), [crates/gcode/src/db/resolution.rs:685-696](crates/gcode/src/db/resolution.rs#L685-L696), [crates/gcode/src/db/resolution.rs:699-711](crates/gcode/src/db/resolution.rs#L699-L711), [crates/gcode/src/db/resolution.rs:714-722](crates/gcode/src/db/resolution.rs#L714-L722), [crates/gcode/src/db/resolution.rs:725-733](crates/gcode/src/db/resolution.rs#L725-L733), [crates/gcode/src/db/resolution.rs:736-744](crates/gcode/src/db/resolution.rs#L736-L744), [crates/gcode/src/db/resolution.rs:746-754](crates/gcode/src/db/resolution.rs#L746-L754), [crates/gcode/src/db/resolution.rs:756-761](crates/gcode/src/db/resolution.rs#L756-L761), [crates/gcode/src/db/resolution.rs:763-765](crates/gcode/src/db/resolution.rs#L763-L765), [crates/gcode/src/db/resolution.rs:767-794](crates/gcode/src/db/resolution.rs#L767-L794)

</details>

# Configuration & Database Core

## Overview

Handles workspace root and identity detection, config resolution with environment overrides, and PostgreSQL relational connection pooling.

## Reference Modules

- [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]
- [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

## Source Files

- [[code/files/crates/gcode/src/config.rs|crates/gcode/src/config.rs]]
- [[code/files/crates/gcode/src/config/context.rs|crates/gcode/src/config/context.rs]]
- [[code/files/crates/gcode/src/config/services.rs|crates/gcode/src/config/services.rs]]
- [[code/files/crates/gcode/src/config/tests.rs|crates/gcode/src/config/tests.rs]]
- [[code/files/crates/gcode/src/db/mod.rs|crates/gcode/src/db/mod.rs]]
- [[code/files/crates/gcode/src/db/queries.rs|crates/gcode/src/db/queries.rs]]
