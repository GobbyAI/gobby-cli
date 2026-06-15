---
title: Architecture Overview
type: code_architecture
provenance:
- file: crates/gcode/contract/gcode.contract.json
  ranges:
  - 2-928
- file: crates/gcode/src/commands/codewiki/types.rs
  ranges:
  - 11-21
  - 26-30
  - 33-45
  - 50-62
  - 65-69
  - 71-93
  - 96-99
  - 102-105
  - 107-128
  - 131-135
  - 138-150
  - 153-159
  - 162-177
  - 180-186
  - 189-194
  - 197-202
  - 205-209
  - 212-217
  - 220-226
  - 229-235
  - 238-245
  - 248-252
  - 255-259
  - 262-266
  - 269-281
  - 284-291
  - 294-310
  - 315-322
  - 324-333
  - 336-343
  - 346-349
  - 352-358
  - '360'
  - 367-371
  - 376-384
  - 386-402
  - 405-411
  - 413-433
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
  - 198-222
  - '224'
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
- file: crates/gcode/src/index/semantic.rs
  ranges:
  - 15-23
  - 26-29
  - 31-36
  - 39-41
  - 43-71
  - 73-91
  - 93-110
  - 112-123
  - 125-133
  - 135-141
  - 143-163
  - 165-198
  - 200-206
  - 208-215
  - 217-223
  - 226-231
  - 234-246
  - 249-270
  - 272-277
  - 279-305
  - 307-310
  - 312-314
  - 316-331
  - 333-341
  - 343-470
  - 472-480
  - 482-519
  - 521-527
  - 529-547
  - 549-571
  - 573-605
  - 607-615
  - 626-633
  - 636-648
  - 651-660
  - 663-668
  - 671-677
  - 680-695
  - 698-742
  - 745-763
  - 767-771
  - 775-779
  - 783-788
  - 792-797
  - 802-826
  - 829-864
- file: crates/gcode/src/models.rs
  ranges:
  - 18-22
  - 24-33
  - 37-50
  - 52-108
  - 112-138
  - 140-217
  - 219-222
  - 224-232
  - 236-245
  - 247-252
  - 256-266
  - 268-273
  - 277-280
  - 284-288
  - 290-298
  - 302-310
  - 312-346
  - 350-359
  - 363-381
  - 385-396
  - 399-405
  - 409-416
  - 421-429
  - 433-441
  - 445-452
  - 459-507
  - 510-523
  - 525-536
  - 539-553
  - 556-590
- file: crates/gcore/assets/docker-compose.services.yml
  ranges:
  - 5-117
  - 119-128
- file: crates/gcore/src/ai_context.rs
  ranges:
  - 25-30
  - 32-69
  - 73-76
  - 80-86
  - 88-124
  - 127-129
  - 133-135
  - 137-141
  - 143-191
  - 193-199
  - 203-205
  - 207-217
  - 219-225
  - 232-235
  - '237'
  - 239-246
  - 252-257
  - 259-267
  - 274-283
  - 285-296
  - 299-302
  - '306'
  - 308-319
  - 323-327
  - 334-340
  - 342-344
  - 352-367
  - 369-374
  - 378-385
  - 399-402
  - 404-425
  - 427-438
  - 440-443
  - 445-457
  - 459-463
  - 465-469
  - 472-525
  - 528-548
  - 551-579
  - 582-606
  - 609-625
  - 628-637
  - 640-651
  - 654-713
  - 716-738
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
  ranges:
  - 2-79
- file: crates/gsqz/config.yaml
  ranges:
  - 12-15
  - 17-204
  - 206-214
- file: crates/gsqz/src/config.rs
  ranges:
  - 26-35
  - 38-47
  - 49-58
  - 60-62
  - 64-66
  - 69-76
  - 79-87
  - 91-166
  - 169-172
  - 175-177
  - 180-189
  - 191-193
  - 195-197
  - '200'
  - 203-205
  - 208-211
  - 214-216
  - 219-224
  - 227-230
  - 232-234
  - 237-240
  - 242-248
  - 250-257
  - 259-326
  - 333-338
  - 341-345
  - 348-353
  - 356-359
  - 362-368
  - 371-374
  - 377-381
  - 384-388
  - 391-398
  - 401-408
  - 411-423
  - 426-436
  - 439-443
  - 446-457
  - 460-473
  - 476-480
  - 483-490
  - 493-503
  - 506-513
  - 516-526
- file: crates/gwiki/contract/gwiki.contract.json
  ranges:
  - 2-887
- file: crates/gwiki/src/benchmark.rs
  ranges:
  - 30-39
  - 42-48
  - 51-58
  - 61-67
  - 70-75
  - 78-85
  - 88-91
  - 94-99
  - 104-114
  - 117-120
  - 122-145
  - 147-157
  - 159-193
  - 195-249
  - 251-264
  - 266-281
  - 283-299
  - 301-305
  - 307-331
  - 333-342
  - 344-377
  - 379-395
  - 397-489
  - 491-501
  - 503-509
  - 511-513
  - 515-534
  - 536-554
  - 556-562
  - 564-570
  - 572-584
  - 586-602
  - 604-611
  - 613-626
  - 628-631
  - 633-635
  - 637-639
  - 641-643
  - 645-649
  - '657'
  - 659-667
  - 669-671
  - 673-679
  - 681-702
  - 704-719
  - 721-737
  - 740-771
  - 774-818
  - 821-860
  - 863-873
  - 876-881
  - 884-893
- file: crates/gwiki/src/graph/mod.rs
  ranges:
  - 22-26
  - 29-33
  - 36-39
  - 42-47
  - 50-59
  - 62-67
  - 70-72
  - 74-82
  - 85-92
  - 95-103
  - 106-113
  - 116-122
  - 125-127
  - 130-135
  - 138-143
  - 146-148
  - 150-156
  - 158-239
  - 242-244
  - 246-414
  - 416-418
  - 420-422
  - 424-426
  - 428-430
  - 432-440
  - 442-449
  - 451-453
  - 455-464
  - 466-475
  - 477-486
  - 488-497
  - 499-501
  - 503-505
  - 507-513
  - 515-517
  - 519-521
  - 523-532
  - 534-554
  - 556-565
  - 567-593
  - 595-599
  - 601-606
  - 613-679
  - 682-715
  - 718-725
  - 728-771
  - 774-817
  - 820-862
  - 864-870
  - 872-884
  - 886-893
- file: crates/gwiki/src/health.rs
  ranges:
  - 22-34
  - 37-41
  - 44-47
  - 49-53
  - 55-95
  - 97-106
  - 108-132
  - 134-142
  - 144-169
  - 171-188
  - 190-192
  - 194-197
  - 199-211
  - 213-226
  - 228-236
  - 238-240
  - 242-247
  - 249-253
  - 255-262
  - 265-276
  - 279-281
  - 283-287
  - 289-327
  - 329-339
  - 341-350
  - 353-360
  - 362-381
  - 384-386
  - 389-391
  - 393-398
  - 400-403
  - 406-435
  - 439-441
  - 443-459
  - 461-467
  - 469-489
  - 491-504
  - 506-521
  - 523-538
  - 540-560
  - 568-611
  - 614-638
  - 641-654
  - 657-695
  - 698-700
  - 703-712
  - 715-726
  - 729-735
  - 738-745
  - 748-753
  - 756-769
  - 772-807
  - 809-813
  - 815-830
- file: crates/gwiki/src/ingest/audio.rs
  ranges:
  - 21-28
  - 31-37
  - 40-54
  - 56-87
  - 89-91
  - 94-96
  - 99-101
  - 104-125
  - 128-137
  - 139-145
  - 148-159
  - 161-202
  - 204-226
  - 228-238
  - 241-250
  - 253-258
  - 261-286
  - 289-299
  - 301-326
  - 329-336
  - 338-346
  - 348-376
  - 396-405
  - 408-414
  - '416'
  - 418-441
  - 444-449
  - 452-474
  - 477-511
  - 513-541
  - 544-548
  - 551-559
  - 562-588
  - 592-598
  - 602-636
  - 640-674
  - 678-704
  - 708-745
  - 749-787
  - 790-821
  - 824-859
  - 862-897
- file: crates/gwiki/src/ingest/mod.rs
  ranges:
  - 25-29
  - 31-36
  - 38-46
  - 48-57
  - 59-73
  - 75-85
  - 87-107
  - 109-117
  - 120-135
  - 137-143
  - 146-149
  - 151-159
  - 161-171
  - 173-178
  - 180-186
  - 188-195
  - 197-204
  - 206-226
  - 228-230
  - 232-235
  - 237-244
  - 246-248
  - 250-252
  - 254-256
  - 258-260
  - 262-264
  - 266-305
  - 307-357
  - 359-374
  - 376-391
  - 393-410
  - 412-420
  - 422-449
  - 453-458
  - 460-474
  - 476-482
  - 508-517
  - 519-525
  - 527-542
  - 545-556
  - 559-585
  - 588-598
  - 601-618
  - 621-670
  - 673-719
  - 722-727
  - 729-746
  - 748-797
  - 800-833
- file: crates/gwiki/src/search/semantic.rs
  ranges:
  - 18-22
  - 25-28
  - 30-35
  - 37-54
  - 57-61
  - 63-70
  - 72-163
  - 165-170
  - 172-174
  - 176-182
  - 184-204
  - 206-211
  - 214-226
  - 234-245
  - 250-252
  - 255-261
  - 264-268
  - 271-306
  - 309-323
  - '327'
  - 330-334
  - 337-351
  - 354-365
  - 368-376
  - '379'
  - 381-390
  - 392-396
  - 398-411
  - 413-457
  - 459-461
  - 463-468
  - 470-478
  - 480-509
  - '512'
  - 515-525
  - 528-531
  - 534-541
  - 544-553
  - 556-560
  - 563-571
  - 574-585
  - '588'
  - 591-599
  - '602'
  - 605-614
  - 617-619
  - 622-638
- file: crates/gwiki/src/vector.rs
  ranges:
  - 17-26
  - 29-33
  - 36-40
  - 43-48
  - 50-59
  - '61'
  - 63-67
  - 69-73
  - 75-77
  - 79-99
  - 101-193
  - 195-197
  - 199-205
  - 207-245
  - 247-249
  - 251-253
  - 255-257
  - 260-262
  - 266-282
  - 284-298
  - 301-323
  - 325-330
  - 332-340
  - 342-345
  - 347-354
  - 356-371
  - 373-375
  - 377-381
  - 383-416
  - 425-452
  - 455-522
  - 525-566
  - 570-604
  - 607-617
  - 619-622
  - 624-635
  - 637-640
  - 642-648
  - 651-655
  - 657-660
  - 662-693
  - 695-704
- file: docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json
  ranges:
  - 2-90
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json
  ranges:
  - 3-299
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json
  ranges:
  - 3-295
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json
  ranges:
  - 2-113
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json
  ranges:
  - 3-341
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json
  ranges:
  - 2-84
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json
  ranges:
  - 3-327
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json
  ranges:
  - 3-341
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json
  ranges:
  - 2-84
- file: docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json
  ranges:
  - 3-137
- file: docs/evidence/wiki-parity-2026-06/wp3-search-sources.json
  ranges:
  - 3-227
provenance_truncated: 427
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# Architecture Overview

## Overview

The foundation is `crates/gcore`, which defines shared, transport-neutral contracts for configuration, AI context, daemon/bootstrap behavior, setup and degradation handling, and optional datastore, search, and indexing primitives. Its schemas and packaged service assets give the rest of the repository a common vocabulary for daemon requests, local services, and feature-gated integrations without forcing direct subsystem coupling.

On top of that shared contract layer sit independent tool subsystems. `crates/gcode` provides the fast code indexing CLI and owns project resolution, indexing, search, graph and vector projection, output, and progress behavior. `crates/gwiki` provides local-first wiki capture, storage, indexing, search, synthesis, and export. `crates/ghook` bridges host CLI hook invocations into durable daemon-facing envelopes, while `crates/gloc` launches AI CLI clients against detected local backends, and `crates/gsqz` compresses command output into concise LLM-oriented summaries. These tools interact through stable contracts, configuration conventions, daemon-facing envelopes, and optional shared services such as Postgres, FalkorDB, Qdrant, clangd, graph storage, and vector search rather than through direct cross-subsystem dependencies.

The outer evidence layer is `docs/evidence`, which records auditable generated artifacts from wiki-parity workflows. It preserves compile, ingestion, search, validation, and ask outputs, including metadata, hashes, citations, rankings, and warning states. This layer does not drive runtime behavior; it documents and verifies the behavior of subsystems such as `gwiki` and `ghook`, making generated content and synthesized answers traceable back to concrete source paths and code citations.
[crates/gcode/src/vector/code_symbols/qdrant.rs:21-27]
[crates/gcode/src/vector/code_symbols/repository.rs:6-18]
[crates/gcode/src/vector/code_symbols/search.rs:8-14]
[crates/gcode/src/graph/code_graph.rs:1-47]
[crates/gcode/src/graph/code_graph/connection.rs:7-12]

## Subsystems

- [[code/modules/crates/gcode|crates/gcode]] - crates/gcode implements the `gcode` CLI, a fast code indexing interface for Gobby that owns command contracts, project/config resolution, indexing, search, graph/vector projection, output, and progress behavior. It collaborates with the rest of the system through its daemon-consumed contract, shared project identity and service configuration, static import-root assets, Postgres-backed test/config gates, and optional external services such as clangd, graph storage, and vector search.
[crates/gcode/src/index/import_resolution/parser/rest.rs:10-54]
[crates/gcode/src/vector/code_symbols/search.rs:8-14]
[crates/gcode/src/config/services.rs:20-22]
[crates/gcode/src/graph/code_graph.rs:1-47]
[crates/gcode/src/graph/code_graph/connection.rs:7-12]
  - [[code/modules/crates/gcode/assets|crates/gcode/assets]]
  - [[code/modules/crates/gcode/contract|crates/gcode/contract]]
  - [[code/modules/crates/gcode/src|crates/gcode/src]]
- [[code/modules/crates/gcore|crates/gcore]] - crates/gcore is Gobby’s shared core layer, defining transport-neutral configuration, AI context/types, daemon/bootstrap contracts, setup/degradation handling, and optional datastore/search/indexing primitives. It collaborates with higher-level crates by supplying stable schemas and feature-gated integrations, while its packaged assets provision the local FalkorDB, Qdrant, and Postgres services those consumers can depend on.
[crates/gcore/src/ai/daemon/transport.rs:8-12]
[crates/gcore/src/ai/daemon/types.rs:4-9]
[crates/gcore/src/ai/daemon.rs:1-15]
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/request.rs:11-19]
  - [[code/modules/crates/gcore/assets|crates/gcore/assets]]
  - [[code/modules/crates/gcore/src|crates/gcore/src]]
- [[code/modules/crates/ghook|crates/ghook]] - crates/ghook is the CLI-side hook bridge that recognizes host CLIs, diagnoses hook behavior, and converts owned hook invocations into durable daemon-facing envelopes. It collaborates with the daemon through fixed JSON-schema contracts for diagnose output and inbox replay, preserving host-specific hook semantics, criticality, source mapping, headers, and optional terminal context.
[crates/ghook/src/terminal_context.rs:18-23]
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/diagnose.rs:15-32]
[crates/ghook/src/json_value.rs:3-20]
[crates/ghook/src/output.rs:3-5]
  - [[code/modules/crates/ghook/schemas|crates/ghook/schemas]]
  - [[code/modules/crates/ghook/src|crates/ghook/src]]
- [[code/modules/crates/gloc|crates/gloc]] - `crates/gloc` provides a configurable launcher that detects a local LLM backend, resolves client/model settings, validates readiness, and execs into AI CLI tools such as Claude or Codex. It collaborates with shared core configuration and backend probing facilities while exposing project/global/built-in config layers, status/init/dump commands, model aliases, and environment/argument templating for downstream client processes.
[crates/gloc/src/backend.rs:7-12]
[crates/gloc/src/config.rs:13-22]
[crates/gloc/src/exec.rs:9-21]
[crates/gloc/src/main.rs:16-52]
[crates/gloc/config.yaml:11-17]
  - [[code/modules/crates/gloc/src|crates/gloc/src]]
- [[code/modules/crates/gsqz|crates/gsqz]] - `crates/gsqz` provides the configurable output-compression subsystem and CLI, turning command or stdin output into concise LLM-oriented summaries while preserving failures, diagnostics, and important results. It collaborates through layered YAML configuration and command-matched pipelines, applying reusable steps such as filtering, grouping, deduplication, replacement, truncation, prose compression, fallback handling, exclusions, and optional daemon-provided config.
[crates/gsqz/src/command_split.rs:5-85]
[crates/gsqz/src/config.rs:26-35]
[crates/gsqz/src/daemon.rs:11-23]
[crates/gsqz/src/primitives/match_output.rs:8-33]
[crates/gsqz/src/primitives/prose.rs:5-9]
  - [[code/modules/crates/gsqz/src|crates/gsqz/src]]
- [[code/modules/crates/gwiki|crates/gwiki]] - crates/gwiki provides the local-first wiki CLI and library surface for capturing, indexing, searching, maintaining, synthesizing, and exporting scoped wiki vaults. It collaborates with the rest of the system through a pinned CLI contract, shared command dispatch, scope/vault resolution, PostgreSQL-backed storage and schema setup, and optional search/AI integrations such as embeddings and Qdrant.
[crates/gwiki/src/commands/refresh/vault.rs:7-9]
[crates/gwiki/src/commands/search.rs:27-30]
[crates/gwiki/src/commands/setup.rs:18]
[crates/gwiki/src/contract.rs:6-470]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98]
  - [[code/modules/crates/gwiki/contract|crates/gwiki/contract]]
  - [[code/modules/crates/gwiki/src|crates/gwiki/src]]
- [[code/modules/docs/evidence|docs/evidence]] - docs/evidence stores generated, auditable evidence bundles for wiki-parity workstreams, capturing compile, ingestion, search, validation, and ask outputs with AI metadata, source hashes, citations, rankings, and warning states. It collaborates with gwiki and ghook by preserving their run artifacts so generated wiki content, search behavior, and synthesized answers can be traced back to source paths and code citations.
[docs/evidence/wiki-parity-2026-06/wp3-compile-source.json:2]
[docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json:3-10]
[docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json:3-10]
[docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json:2-15]
[docs/evidence/wiki-parity-2026-06/wp3-compile-explainer-v2.json:3-12]
  - [[code/modules/docs/evidence/wiki-parity-2026-06|docs/evidence/wiki-parity-2026-06]]

