---
title: crates/gcode/src/index/indexer
type: code_module
provenance:
- file: crates/gcode/src/index/indexer/file.rs
  ranges:
  - 15-91
  - 93-108
  - 111-115
  - 117-127
  - 130-177
  - 179-229
  - 231-264
- file: crates/gcode/src/index/indexer/freshness_probe.rs
  ranges:
  - 37-81
  - 89-96
  - 98-105
  - 109-111
  - 113-115
  - 118-138
  - 141-156
  - 159-176
  - 179-195
  - 198-235
  - 238-265
- file: crates/gcode/src/index/indexer/lifecycle.rs
  ranges:
  - 16-54
  - 56-69
  - 71-81
  - 84-121
  - 125-152
  - 154-181
  - 183-229
  - 232-235
  - 237-260
  - 262-294
  - 296-305
- file: crates/gcode/src/index/indexer/overlay.rs
  ranges:
  - 32-35
  - 38-44
  - 46-82
  - 84-255
  - 257-288
  - 290-299
  - 301-321
  - 323-375
  - 377-393
  - 395-400
  - 402-407
  - 409-414
  - 416-429
  - 431-447
  - 455-462
  - 466-470
  - 474-483
- file: crates/gcode/src/index/indexer/pipeline.rs
  ranges:
  - 27-30
  - 32-45
  - 47-173
  - 175-302
  - 304-308
  - 310-324
  - 326-340
- file: crates/gcode/src/index/indexer/sink.rs
  ranges:
  - 6-34
  - 36-38
  - 41-43
  - 50-52
  - 54-60
  - 62-69
  - 71-73
  - 75-77
  - 79-86
  - 88-95
  - 97-99
- file: crates/gcode/src/index/indexer/tests.rs
  ranges:
  - 24-30
  - 32-40
  - 43-62
  - 65-84
  - 87-105
  - 108-152
  - 155-164
  - 166-235
  - 238-314
  - 318-391
  - 393-402
  - 404-410
  - 412-415
  - 417-423
  - 425-456
  - 458-485
  - 487-514
  - 516-524
  - 526-536
  - 539-561
  - 564-600
  - 603-639
  - 642-672
  - 675-701
  - 704-726
  - 729-744
  - 747-796
  - 799-827
  - 830-880
  - 883-920
  - 923-949
- file: crates/gcode/src/index/indexer/types.rs
  ranges:
  - 8-17
  - 20-25
  - 29-42
  - 45-68
  - 71-76
  - 79-84
  - 86-109
  - 111-113
  - 116-124
- file: crates/gcode/src/index/indexer/util.rs
  ranges:
  - 28-66
  - 70-93
  - 95-101
  - 103-111
  - 113-142
  - 144-154
  - 156-160
  - 162-169
  - 176-186
  - 189-194
  - 197-205
  - 209-214
  - 218-223
  - 227-232
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer

Parent: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

The indexer module orchestrates the extraction, reconciliation, and storage of code facts from project files. It manages the full indexing lifecycle—including file discovery, path normalization, overlay file reconciliation, change/freshness detection, and writing parsed facts (symbols, imports, calls, and content chunks) to a persistent database sink.
[crates/gcode/src/index/indexer/file.rs:15-91]
[crates/gcode/src/index/indexer/freshness_probe.rs:37-81]
[crates/gcode/src/index/indexer/lifecycle.rs:16-54]
[crates/gcode/src/index/indexer/overlay.rs:32-35]
[crates/gcode/src/index/indexer/pipeline.rs:27-30]

## Call Diagram

```mermaid
sequenceDiagram
    participant m_01ec77cc_48df_5af6_ad42_b9d5800cf9ad as index_overlay_files &#91;function&#93;
    participant m_06f747c0_d77a_5408_802b_60d142616c74 as skew_margin_boundary_only_ever_makes_the_gate_more_eager &#91;function&#93;
    participant m_0787f1d1_704a_51e3_826d_c429ef009eef as explicit_file_route_indexes_mjs_and_routes_markdown_to_content_only &#91;function&#93;
    participant m_10340c10_e576_5d26_badb_81bc9e42948a as indexed_file_states &#91;function&#93;
    participant m_1338b69e_01ae_51af_800c_39edd113f6fd as SummaryPreservationCleanup.drop &#91;method&#93;
    participant m_1f671963_1e36_5bcb_8b36_35136e72d054 as lexical_relative_path &#91;function&#93;
    participant m_227a3a94_2cb5_5705_a228_e26c9bbab506 as explicit_file_route_sends_unsupported_text_to_content_only &#91;function&#93;
    participant m_271a6fa6_20dd_501e_bd1a_35ee1d99229f as is_porcelain_status_entry &#91;function&#93;
    participant m_27cff566_a652_5c21_906c_54247b567ec0 as cleanup_deleted_file_projections &#91;function&#93;
    participant m_2b097022_1ca0_54ab_9167_230f31715fe8 as set_mtime &#91;function&#93;
    participant m_2c3d5dde_70fb_517d_9a30_a57fc029d55a as requested_relative_path &#91;function&#93;
    participant m_2d437509_ec07_545d_8636_48f4a49d61ce as cleanup_summary_preservation_project &#91;function&#93;
    participant m_4024a0a6_07dc_543a_9b66_60e72d24e7d8 as git_status_timeout &#91;function&#93;
    participant m_4b108bd2_677f_5b6f_baae_1a9687543be0 as git_status_relative_paths &#91;function&#93;
    participant m_4b12832a_8119_5965_b9c6_d91d8cb4122e as index_file &#91;function&#93;
    participant m_4d80ef56_1326_501d_ad99_6e76e8e39313 as base_time &#91;function&#93;
    participant m_5ea81afb_c78f_589e_9c62_6ad75a49ad6b as push_projection_cleanup_degradation &#91;function&#93;
    participant m_7c9b4b5f_c2f2_5a8a_a844_5837e9288643 as normalized_components &#91;function&#93;
    participant m_8db19430_dba8_52b8_b94c_ebd14b9c1b71 as write_parsed_file_facts &#91;function&#93;
    participant m_93b52f75_55a1_5025_a3a4_7e3d067416a6 as write_file &#91;function&#93;
    participant m_af592e27_20e6_5df0_b6b1_1ca5703f5d03 as compact_stderr &#91;function&#93;
    participant m_be1729cf_c48d_5d6e_8ccf_bfee68ce411e as overlay_reconcile_action &#91;function&#93;
    participant m_c37b5340_8902_5b1c_a469_944a66f25bf7 as write_tombstone &#91;function&#93;
    participant m_d0c535c9_f938_5584_99a0_02a2a7c3c113 as paths_by_relative &#91;function&#93;
    participant m_d4fc0ae1_b01a_5027_9c1c_91ce4e5a2e64 as write_file &#91;function&#93;
    participant m_d8a9fdbf_e6be_5cef_ba09_479c03c7e522 as overlay_reconcile_candidates &#91;function&#93;
    participant m_ea312341_5b87_59ce_b013_88a15ba48909 as valid_porcelain_status_byte &#91;function&#93;
    participant m_f6a4f46d_0e79_54eb_b222_2cd0b7d7fb2d as rel_matches_filter &#91;function&#93;
    m_01ec77cc_48df_5af6_ad42_b9d5800cf9ad->>m_10340c10_e576_5d26_badb_81bc9e42948a: calls
    m_01ec77cc_48df_5af6_ad42_b9d5800cf9ad->>m_be1729cf_c48d_5d6e_8ccf_bfee68ce411e: calls
    m_01ec77cc_48df_5af6_ad42_b9d5800cf9ad->>m_c37b5340_8902_5b1c_a469_944a66f25bf7: calls
    m_01ec77cc_48df_5af6_ad42_b9d5800cf9ad->>m_d0c535c9_f938_5584_99a0_02a2a7c3c113: calls
    m_01ec77cc_48df_5af6_ad42_b9d5800cf9ad->>m_d8a9fdbf_e6be_5cef_ba09_479c03c7e522: calls
    m_01ec77cc_48df_5af6_ad42_b9d5800cf9ad->>m_f6a4f46d_0e79_54eb_b222_2cd0b7d7fb2d: calls
    m_06f747c0_d77a_5408_802b_60d142616c74->>m_2b097022_1ca0_54ab_9167_230f31715fe8: calls
    m_06f747c0_d77a_5408_802b_60d142616c74->>m_4d80ef56_1326_501d_ad99_6e76e8e39313: calls
    m_06f747c0_d77a_5408_802b_60d142616c74->>m_d4fc0ae1_b01a_5027_9c1c_91ce4e5a2e64: calls
    m_0787f1d1_704a_51e3_826d_c429ef009eef->>m_93b52f75_55a1_5025_a3a4_7e3d067416a6: calls
    m_1338b69e_01ae_51af_800c_39edd113f6fd->>m_2d437509_ec07_545d_8636_48f4a49d61ce: calls
    m_1f671963_1e36_5bcb_8b36_35136e72d054->>m_7c9b4b5f_c2f2_5a8a_a844_5837e9288643: calls
    m_227a3a94_2cb5_5705_a228_e26c9bbab506->>m_93b52f75_55a1_5025_a3a4_7e3d067416a6: calls
    m_271a6fa6_20dd_501e_bd1a_35ee1d99229f->>m_ea312341_5b87_59ce_b013_88a15ba48909: calls
    m_27cff566_a652_5c21_906c_54247b567ec0->>m_5ea81afb_c78f_589e_9c62_6ad75a49ad6b: calls
    m_2c3d5dde_70fb_517d_9a30_a57fc029d55a->>m_1f671963_1e36_5bcb_8b36_35136e72d054: calls
    m_4b108bd2_677f_5b6f_baae_1a9687543be0->>m_271a6fa6_20dd_501e_bd1a_35ee1d99229f: calls
    m_4b108bd2_677f_5b6f_baae_1a9687543be0->>m_4024a0a6_07dc_543a_9b66_60e72d24e7d8: calls
    m_4b108bd2_677f_5b6f_baae_1a9687543be0->>m_af592e27_20e6_5df0_b6b1_1ca5703f5d03: calls
    m_4b12832a_8119_5965_b9c6_d91d8cb4122e->>m_8db19430_dba8_52b8_b94c_ebd14b9c1b71: calls
```

## Files

- [[code/files/crates/gcode/src/index/indexer/file.rs|crates/gcode/src/index/indexer/file.rs]] - `crates/gcode/src/index/indexer/file.rs` exposes 7 indexed API symbols.
[crates/gcode/src/index/indexer/file.rs:15-91]
[crates/gcode/src/index/indexer/file.rs:93-108]
[crates/gcode/src/index/indexer/file.rs:111-115]
[crates/gcode/src/index/indexer/file.rs:117-127]
[crates/gcode/src/index/indexer/file.rs:130-177]
- [[code/files/crates/gcode/src/index/indexer/freshness_probe.rs|crates/gcode/src/index/indexer/freshness_probe.rs]] - `crates/gcode/src/index/indexer/freshness_probe.rs` exposes 11 indexed API symbols.
[crates/gcode/src/index/indexer/freshness_probe.rs:37-81]
[crates/gcode/src/index/indexer/freshness_probe.rs:89-96]
[crates/gcode/src/index/indexer/freshness_probe.rs:98-105]
[crates/gcode/src/index/indexer/freshness_probe.rs:109-111]
[crates/gcode/src/index/indexer/freshness_probe.rs:113-115]
- [[code/files/crates/gcode/src/index/indexer/lifecycle.rs|crates/gcode/src/index/indexer/lifecycle.rs]] - `crates/gcode/src/index/indexer/lifecycle.rs` exposes 11 indexed API symbols.
[crates/gcode/src/index/indexer/lifecycle.rs:16-54]
[crates/gcode/src/index/indexer/lifecycle.rs:56-69]
[crates/gcode/src/index/indexer/lifecycle.rs:71-81]
[crates/gcode/src/index/indexer/lifecycle.rs:84-121]
[crates/gcode/src/index/indexer/lifecycle.rs:125-152]
- [[code/files/crates/gcode/src/index/indexer/overlay.rs|crates/gcode/src/index/indexer/overlay.rs]] - `crates/gcode/src/index/indexer/overlay.rs` exposes 17 indexed API symbols.
[crates/gcode/src/index/indexer/overlay.rs:32-35]
[crates/gcode/src/index/indexer/overlay.rs:38-44]
[crates/gcode/src/index/indexer/overlay.rs:46-82]
[crates/gcode/src/index/indexer/overlay.rs:84-255]
[crates/gcode/src/index/indexer/overlay.rs:257-288]
- [[code/files/crates/gcode/src/index/indexer/pipeline.rs|crates/gcode/src/index/indexer/pipeline.rs]] - `crates/gcode/src/index/indexer/pipeline.rs` exposes 7 indexed API symbols.
[crates/gcode/src/index/indexer/pipeline.rs:27-30]
[crates/gcode/src/index/indexer/pipeline.rs:32-45]
[crates/gcode/src/index/indexer/pipeline.rs:47-173]
[crates/gcode/src/index/indexer/pipeline.rs:175-302]
[crates/gcode/src/index/indexer/pipeline.rs:304-308]
- [[code/files/crates/gcode/src/index/indexer/sink.rs|crates/gcode/src/index/indexer/sink.rs]] - `crates/gcode/src/index/indexer/sink.rs` exposes 11 indexed API symbols.
[crates/gcode/src/index/indexer/sink.rs:6-34]
[crates/gcode/src/index/indexer/sink.rs:36-38]
[crates/gcode/src/index/indexer/sink.rs:41-43]
[crates/gcode/src/index/indexer/sink.rs:50-52]
[crates/gcode/src/index/indexer/sink.rs:54-60]
- [[code/files/crates/gcode/src/index/indexer/tests.rs|crates/gcode/src/index/indexer/tests.rs]] - `crates/gcode/src/index/indexer/tests.rs` exposes 40 indexed API symbols.
[crates/gcode/src/index/indexer/tests.rs:24-30]
[crates/gcode/src/index/indexer/tests.rs:32-40]
[crates/gcode/src/index/indexer/tests.rs:43-62]
[crates/gcode/src/index/indexer/tests.rs:65-84]
[crates/gcode/src/index/indexer/tests.rs:87-105]
- [[code/files/crates/gcode/src/index/indexer/types.rs|crates/gcode/src/index/indexer/types.rs]] - `crates/gcode/src/index/indexer/types.rs` exposes 12 indexed API symbols.
[crates/gcode/src/index/indexer/types.rs:8-17]
[crates/gcode/src/index/indexer/types.rs:20-25]
[crates/gcode/src/index/indexer/types.rs:29-42]
[crates/gcode/src/index/indexer/types.rs:45-68]
[crates/gcode/src/index/indexer/types.rs:71-76]
- [[code/files/crates/gcode/src/index/indexer/util.rs|crates/gcode/src/index/indexer/util.rs]] - `crates/gcode/src/index/indexer/util.rs` exposes 14 indexed API symbols.
[crates/gcode/src/index/indexer/util.rs:28-66]
[crates/gcode/src/index/indexer/util.rs:70-93]
[crates/gcode/src/index/indexer/util.rs:95-101]
[crates/gcode/src/index/indexer/util.rs:103-111]
[crates/gcode/src/index/indexer/util.rs:113-142]

## Components

- `4b12832a-8119-5965-b9c6-d91d8cb4122e`
- `c13ce350-3af8-5341-ba85-f91321f40cb2`
- `e0425afb-6091-5f4b-8ed8-0077a7cbdbc8`
- `a46733a5-8a30-596e-a98c-6214e9693bde`
- `b07b2215-4ef6-53de-9d92-eef5f90e3aec`
- `8db19430-dba8-52b8-b94c-ebd14b9c1b71`
- `30dacd9b-2dd5-5b96-ae60-f434036b7dca`
- `d30b24ca-520a-57b2-885f-fb0f1d2fe538`
- `d4fc0ae1-b01a-5027-9c1c-91ce4e5a2e64`
- `2b097022-1ca0-54ab-9167-230f31715fe8`
- `4d80ef56-1326-501d-ad99-6e76e8e39313`
- `3cced7cf-62ab-5c52-8e0f-591a88557847`
- `dcaf9766-7e19-519d-adc8-445c84c6402d`
- `9cac490e-8989-5a1b-a5fc-e393f19f9aac`
- `b8ca0cd0-0cde-5646-866f-ff724633a2c9`
- `8452e4b9-b88a-5e12-af81-285c2aaf39fe`
- `06f747c0-d77a-5408-802b-60d142616c74`
- `4fc2ee8c-d38a-51cf-97de-7c9fa10bf90c`
- `27cff566-a652-5c21-906c-54247b567ec0`
- `5ea81afb-c78f-589e-9c62-6ad75a49ad6b`
- `9fd4f6ac-7ca7-5f00-8eda-97975a6e638f`
- `baa7789a-c6ed-5e9d-8147-e2f915311202`
- `2b812e49-5999-553b-a85d-aebd28c2e43e`
- `88cf7807-7b3d-54fd-a997-c4c1cc9e39f8`
- `e5ef0115-76fe-5b3b-9fa4-26706f94b854`
- `55465b3a-9f29-555e-a54d-a6c4e7c8b590`
- `9fee873c-a767-5fba-a249-877666585ef9`
- `38e31014-9d04-56a9-961a-fac722544e40`
- `9facb226-8885-5b36-a141-3365f419c479`
- `ac812838-0378-5a0c-b089-0b10d8c497c8`
- `6be8f7b3-67d5-5a31-9d4d-5e27f5ddc9f0`
- `be1729cf-c48d-5d6e-8ccf-bfee68ce411e`
- `01ec77cc-48df-5af6-ad42-b9d5800cf9ad`
- `d8a9fdbf-e6be-5cef-ba09-479c03c7e522`
- `d0c535c9-f938-5584-99a0-02a2a7c3c113`
- `10340c10-e576-5d26-badb-81bc9e42948a`
- `4b108bd2-677f-5b6f-baae-1a9687543be0`
- `4024a0a6-07dc-543a-9b66-60e72d24e7d8`
- `af592e27-20e6-5df0-b6b1-1ca5703f5d03`
- `271a6fa6-20dd-501e-bd1a-35ee1d99229f`
- `ea312341-5b87-59ce-b013-88a15ba48909`
- `f6a4f46d-0e79-54eb-b222-2cd0b7d7fb2d`
- `c37b5340-8902-5b1c-a469-944a66f25bf7`
- `a63915cd-692d-554d-8c7f-dd8ea3ea7ee5`
- `c9bef015-43b7-5f85-a5cc-342eed480209`
- `02ff068b-adbd-5741-8b94-ffcdbb71daa9`
- `bdb416a7-b6ae-5ba6-a21f-74c21bbb3f2f`
- `adeaf14e-284b-5071-97f0-2d17d8c8a6df`
- `84dc976d-70f1-5221-9a0a-7bab5732f0e6`
- `b21220d8-8ce4-56bc-8ff3-d0b4aba5ba35`
- `9277356b-c936-5f0d-b037-815c545cb4bf`
- `f477c451-1037-581b-b310-35da45fa9472`
- `e6420dba-4991-5dd4-84e0-88430e3b3b73`
- `4beb9119-9fd1-58f8-95af-7e14c1d44a43`
- `519b1645-56e3-50f6-bcf8-ece8c93623d0`
- `f66039bb-8d68-531b-96d3-7d0f7f01ee33`
- `6f175061-24d5-5b38-9496-113a1f6e9a8f`
- `e97c7665-91dc-5e5f-853e-c000add5a733`
- `7a4de9ca-1c4c-5b93-b739-f5d7061ce532`
- `2039da60-88d9-5567-a021-f3c6b66cec2a`
- `4fd617f2-fa69-5f18-b533-aafb5806be6d`
- `5a0d366b-f54c-5559-a559-34ed1702125b`
- `e0e15eb2-cccd-5aa8-854e-8076d3687047`
- `0d1aa3ba-2660-51b7-946a-8e929bfccee1`
- `93b52f75-55a1-5025-a3a4-7e3d067416a6`
- `c9ca8599-c3b6-56f5-a793-8464d6dd688a`
- `a75050de-6e71-506b-b6d9-97a4765ea6b7`
- `b35c0484-ef88-5e10-bcc0-132cc5775747`
- `bc26aaea-8070-5ffb-a5f3-5ffd1e0dddda`
- `b15fe3b0-af43-55b5-a6bf-e1a7641fa3c0`
- `5227db9f-8954-5910-81bf-40152c3b2374`
- `1ca5dd93-8369-586f-90a3-1b1f414fddef`
- `2cbfe908-794d-506c-927c-a073cc7bb09d`
- `57e95b23-33f2-56f1-9d50-18e93bae14a3`
- `0b0bf71f-fe23-500b-9d8a-3c9a2afc8c62`
- `90ed7a42-9cd0-5329-96ed-d6884fc38008`
- `4b97fd8d-91c4-5de4-ba7c-1f29360ca45b`
- `d9cfd64d-fc55-5dfa-a38b-362fbc1f3114`
- `1f23c1ce-dc5f-5a3a-b7d7-6d0460aa821a`
- `337e0088-4236-5a84-956d-8ef4e82ed3a6`
- `d345608e-3d2e-57d3-b30d-2559654276aa`
- `894d5e2d-a7da-580c-842c-13e50be5da5d`
- `9e1a0adf-229d-5e34-abb2-f86683ad9418`
- `113ea5cb-b5c7-53b5-93d9-d0f30984f2d3`
- `4925aa95-6138-52b2-b41b-cdf6a7fb7a9a`
- `4a1039df-6e46-5825-b39e-40bf6d2df066`
- `1338b69e-01ae-51af-800c-39edd113f6fd`
- `2d437509-ec07-545d-8636-48f4a49d61ce`
- `af4856e6-f5f1-5b04-a546-c239f80014bd`
- `271f35b2-97ab-56dc-9dfd-7d14c1eb86a7`
- `ad01f186-a9b3-58bd-b3e6-cf89a069c04c`
- `4ad66c05-518e-58ee-9787-9821aeed46be`
- `62d2d834-f427-5750-9174-7e1e362a10ea`
- `227a3a94-2cb5-5705-a228-e26c9bbab506`
- `bcd05110-747d-5ffa-9749-c33026443c53`
- `e2e0c4ea-52ff-5e40-ab16-db3ba6f2a7e4`
- `0787f1d1-704a-51e3-826d-c429ef009eef`
- `79356024-2ab3-5387-8ad2-b88db3ee902d`
- `52d63b8a-e778-516b-870a-b9864e279df4`
- `c90f37e8-2143-555b-93b3-afb981479de4`
- `67751663-d09a-5b66-9770-29891765fc32`
- `e74aee9d-a324-59ae-ae81-d016a5986d89`
- `caeb3605-e379-545b-9cb0-dfd7edf99b26`
- `69a88f91-a48b-5461-9f2d-37daa87902f2`
- `f008b690-f127-5149-ab35-de6fde0893a2`
- `59e57725-f26f-5161-91e4-37a99b8855d3`
- `d196f3e6-dc4d-5be8-826c-fb269952d95d`
- `d4b4995c-dbf3-5265-9317-bd4c2c318e4a`
- `54396602-75ae-5b77-bc8b-0410746b2566`
- `bd704bf0-da3f-5561-b346-73369db80095`
- `bff99496-be66-54ac-a7e1-7b51f6553e86`
- `38f2c05b-417b-542c-aec1-bee3adf7654f`
- `b32fcc3e-3403-585e-8072-a6c6f1261f86`
- `bd3b3e97-15cd-5557-a5b6-3769e6a2f397`
- `945b3776-c46f-51d5-bddc-b405641cd578`
- `af868d53-8ad5-5409-aa39-c4b7f522ffc9`
- `5c2ff8bb-3bed-50a9-ad92-ab66a0a34c28`
- `f3a89c34-7edf-5690-ba9c-92c07901cf9e`
- `21ee0949-01a8-5b35-b124-7a3e12a280d1`
- `2c3d5dde-70fb-517d-9a30-a57fc029d55a`
- `1f671963-1e36-5bcb-8b36-35136e72d054`
- `7c9b4b5f-c2f2-5a8a-a844-5837e9288643`
- `134005ee-5574-5385-9b33-18f72d9de8bb`
- `80ceb895-29f8-566e-b983-c292429f5278`
- `745d791b-9ff5-5a66-acc5-84f77ba6796d`
- `11da72a1-c6bc-5d09-b79c-f9ba71a8ad1b`
- `56916c1b-faee-5acd-9f09-68af8ccb74cb`
- `1f800663-4932-5759-add5-3b7173a3506c`
- `4980e3bc-72a2-52fa-a5bd-9884d5659412`
- `e0a54663-b2b3-53fc-acda-5f3c78028f84`

