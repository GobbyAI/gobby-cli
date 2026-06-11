---
title: crates/gwiki/src/ingest/video
type: code_module
provenance:
- file: crates/gwiki/src/ingest/video/assets.rs
  ranges:
  - 3-22
  - 24-114
  - 117-121
  - 125-205
  - 207-211
  - 213-223
  - 225-241
- file: crates/gwiki/src/ingest/video/metadata.rs
  ranges:
  - 4-8
  - 10-25
  - 27-39
  - 42-56
  - 58-72
  - 75-83
  - 76-82
  - 85-126
  - 128-133
- file: crates/gwiki/src/ingest/video/mod.rs
  ranges:
  - 31-44
  - 47-60
  - 63-72
  - 74-92
  - 94-101
  - 103-122
  - 124-159
  - 161-174
  - 176-226
- file: crates/gwiki/src/ingest/video/processing.rs
  ranges:
  - 19-27
  - '29'
  - 31-43
  - 32-34
  - 36-42
  - 45-64
  - 66-179
  - 181-197
  - 199-209
  - 212-216
  - 218-223
  - 225-329
  - 331-335
  - 337-346
- file: crates/gwiki/src/ingest/video/tests.rs
  ranges:
  - 18-55
  - 57-62
  - 64-89
  - 65-72
  - 74-88
  - 91-111
  - '113'
  - 115-131
  - 116-130
  - '133'
  - 135-144
  - 136-143
  - '146'
  - 148-160
  - 149-159
  - '162'
  - 164-170
  - 165-169
  - 172-198
  - 201-273
  - 276-323
  - 326-329
  - 332-350
  - 333-340
  - 342-349
  - 354-446
  - 449-451
  - 454-461
  - 455-460
  - 464-617
  - 620-638
  - 641-656
  - 659-707
  - 710-765
  - 767-799
  - 801-803
  - 805-810
  - 813-843
  - 846-883
  - 886-922
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

The video ingest module processes video media into wiki-ready artifacts, producing transcripts, sampled frame images, and rendered markdown. The `mod.rs` entry point exposes the primary `ingest_video` and `ingest_video_file` family of functions (including degradation-aware and production-processing variants), backed by `VideoSnapshot`/`VideoFileSnapshot` inputs and `VideoIngestResult`/`IngestResult` outputs.

`processing.rs` defines the `VideoMediaExtractor` trait and its `ProductionVideoMediaExtractor` implementation for extracting audio and sampling frame images, plus frame-description orchestration (`describe_frame_images`), transcription/vision degradation handling, and ffmpeg-availability detection. `metadata.rs` derives video media metadata and degradation context. `assets.rs` persists frame assets (`PersistedVideoFrameAssets`) and manages cleanup of temporary frame sources across deferred, sampled, and kept lifecycles.

`tests.rs` provides extensive coverage via fake and failing transcription/vision/extractor clients, validating transcript and frame generation, translation chunking, degradation matrices, vision-failure fallbacks, temp-frame cleanup, and asset provenance preservation.
[crates/gwiki/src/ingest/video/assets.rs:3-22]
[crates/gwiki/src/ingest/video/metadata.rs:4-8]
[crates/gwiki/src/ingest/video/mod.rs:31-44]
[crates/gwiki/src/ingest/video/processing.rs:19-27]
[crates/gwiki/src/ingest/video/tests.rs:18-55]

## Call Diagram

```mermaid
sequenceDiagram
    participant m_0112e846_ae5c_5943_9155_b825f5da1b6e as assert_asset_preserved &#91;function&#93;
    participant m_0f73f741_684f_5f38_bd36_2a015108be1c as ingest_video_with_asset &#91;function&#93;
    participant m_1396e8ba_e260_5994_b347_daafdfe8aa50 as ingest_video_file &#91;function&#93;
    participant m_1d80e9b2_5f10_5876_a9d4_5956c0b32e8b as ingest_video_with_asset_without_index &#91;function&#93;
    participant m_2431a95c_38da_57fb_bbdb_26047af09bb7 as ingest_video_file_with_degradations_without_index &#91;function&#93;
    participant m_25fc4dd3_52da_590c_940d_eb8b45c68bf5 as production_ingest_applies_degradation_matrix &#91;function&#93;
    participant m_28f836b4_c6ff_5d8f_984d_d99c991de698 as sample_snapshot &#91;function&#93;
    participant m_2d55b0d0_332d_5041_9eea_c36fc7e1304f as message_is_ffmpeg_unavailable &#91;function&#93;
    participant m_3836250a_4708_52e4_b189_353890de8382 as stores_file_backed_video &#91;function&#93;
    participant m_3b3378c5_f3ac_5c93_a480_85348f94f8a8 as video_media_degradation &#91;function&#93;
    participant m_3c714090_f85e_5e7e_838b_1c81cd0bc1c3 as cleanup_deferred_temp_frame_sources &#91;function&#93;
    participant m_427a3ebd_198d_5509_a7f8_0abaf4d4a319 as describe_frame_images &#91;function&#93;
    participant m_4620ed09_061f_5909_8ffa_96abfbdedcbf as remove_sampled_temp_frame &#91;function&#93;
    participant m_4905ee1a_2d61_5ef6_8213_c1df0913ab86 as ingest_video_file_with_degradations &#91;function&#93;
    participant m_49640cb4_d1e6_50ac_be41_b0b703a8d66e as ingest_video_file_with_processing &#91;function&#93;
    participant m_69f4c775_a8b9_5257_8d30_c4b1054bdb4b as video_derivatives_keep_provenance &#91;function&#93;
    participant m_6fe6a29e_fafe_53be_b386_2eeb025e3a01 as FakeVideoMediaExtractor.extract_audio &#91;method&#93;
    participant m_77753645_33aa_5eb6_addd_cf1b2d84b23d as stores_original_video &#91;function&#93;
    participant m_80bc3c4e_2d2e_5b52_81b1_aaf1e3e12b1d as cleanup_sampled_temp_frame_sources &#91;function&#93;
    participant m_84e42e3a_b0bf_5ae2_9354_0815178cd1f2 as cleanup_kept_temp_frames &#91;function&#93;
    participant m_886701b0_1a31_5b4c_8e77_b243e3b8f736 as ingest_with_media &#91;function&#93;
    participant m_8ee2d07c_6db2_55a0_83ea_57e8e95e69b0 as read_derived &#91;function&#93;
    participant m_9146306b_2686_5e09_b94b_d5b169eb23dc as FakeVideoMediaExtractor.sample_frame_images &#91;method&#93;
    participant m_a3834ae2_950b_523b_92bb_d69eb0d6195a as temp_file_with_bytes &#91;function&#93;
    participant m_bfece869_38bb_5912_bb51_36cb77bf9350 as persist_video_frame_assets &#91;function&#93;
    participant m_c26036ec_d3f9_5685_a445_2c62c4ae7dbf as persisted_frame_sources_are_removed_after_successful_loop &#91;function&#93;
    participant m_f93bceec_197e_5356_9fca_063082335497 as ingest_video_file_with_processing_without_index &#91;function&#93;
    m_0f73f741_684f_5f38_bd36_2a015108be1c->>m_1d80e9b2_5f10_5876_a9d4_5956c0b32e8b: calls
    m_1396e8ba_e260_5994_b347_daafdfe8aa50->>m_4905ee1a_2d61_5ef6_8213_c1df0913ab86: calls
    m_1d80e9b2_5f10_5876_a9d4_5956c0b32e8b->>m_bfece869_38bb_5912_bb51_36cb77bf9350: calls
    m_25fc4dd3_52da_590c_940d_eb8b45c68bf5->>m_0112e846_ae5c_5943_9155_b825f5da1b6e: calls
    m_25fc4dd3_52da_590c_940d_eb8b45c68bf5->>m_886701b0_1a31_5b4c_8e77_b243e3b8f736: calls
    m_25fc4dd3_52da_590c_940d_eb8b45c68bf5->>m_8ee2d07c_6db2_55a0_83ea_57e8e95e69b0: calls
    m_3836250a_4708_52e4_b189_353890de8382->>m_28f836b4_c6ff_5d8f_984d_d99c991de698: calls
    m_3b3378c5_f3ac_5c93_a480_85348f94f8a8->>m_2d55b0d0_332d_5041_9eea_c36fc7e1304f: calls
    m_3c714090_f85e_5e7e_838b_1c81cd0bc1c3->>m_4620ed09_061f_5909_8ffa_96abfbdedcbf: calls
    m_427a3ebd_198d_5509_a7f8_0abaf4d4a319->>m_84e42e3a_b0bf_5ae2_9354_0815178cd1f2: calls
    m_4905ee1a_2d61_5ef6_8213_c1df0913ab86->>m_2431a95c_38da_57fb_bbdb_26047af09bb7: calls
    m_49640cb4_d1e6_50ac_be41_b0b703a8d66e->>m_f93bceec_197e_5356_9fca_063082335497: calls
    m_69f4c775_a8b9_5257_8d30_c4b1054bdb4b->>m_28f836b4_c6ff_5d8f_984d_d99c991de698: calls
    m_6fe6a29e_fafe_53be_b386_2eeb025e3a01->>m_a3834ae2_950b_523b_92bb_d69eb0d6195a: calls
    m_77753645_33aa_5eb6_addd_cf1b2d84b23d->>m_28f836b4_c6ff_5d8f_984d_d99c991de698: calls
    m_9146306b_2686_5e09_b94b_d5b169eb23dc->>m_a3834ae2_950b_523b_92bb_d69eb0d6195a: calls
    m_bfece869_38bb_5912_bb51_36cb77bf9350->>m_3c714090_f85e_5e7e_838b_1c81cd0bc1c3: calls
    m_bfece869_38bb_5912_bb51_36cb77bf9350->>m_4620ed09_061f_5909_8ffa_96abfbdedcbf: calls
    m_bfece869_38bb_5912_bb51_36cb77bf9350->>m_80bc3c4e_2d2e_5b52_81b1_aaf1e3e12b1d: calls
    m_c26036ec_d3f9_5685_a445_2c62c4ae7dbf->>m_a3834ae2_950b_523b_92bb_d69eb0d6195a: calls
```

## Files

- [[code/files/crates/gwiki/src/ingest/video/assets.rs|crates/gwiki/src/ingest/video/assets.rs]] - `crates/gwiki/src/ingest/video/assets.rs` exposes 7 indexed API symbols.
[crates/gwiki/src/ingest/video/assets.rs:3-22]
[crates/gwiki/src/ingest/video/assets.rs:24-114]
[crates/gwiki/src/ingest/video/assets.rs:117-121]
[crates/gwiki/src/ingest/video/assets.rs:125-205]
[crates/gwiki/src/ingest/video/assets.rs:207-211]
- [[code/files/crates/gwiki/src/ingest/video/metadata.rs|crates/gwiki/src/ingest/video/metadata.rs]] - `crates/gwiki/src/ingest/video/metadata.rs` exposes 9 indexed API symbols.
[crates/gwiki/src/ingest/video/metadata.rs:4-8]
[crates/gwiki/src/ingest/video/metadata.rs:10-25]
[crates/gwiki/src/ingest/video/metadata.rs:27-39]
[crates/gwiki/src/ingest/video/metadata.rs:42-56]
[crates/gwiki/src/ingest/video/metadata.rs:58-72]
- [[code/files/crates/gwiki/src/ingest/video/mod.rs|crates/gwiki/src/ingest/video/mod.rs]] - `crates/gwiki/src/ingest/video/mod.rs` exposes 9 indexed API symbols.
[crates/gwiki/src/ingest/video/mod.rs:31-44]
[crates/gwiki/src/ingest/video/mod.rs:47-60]
[crates/gwiki/src/ingest/video/mod.rs:63-72]
[crates/gwiki/src/ingest/video/mod.rs:74-92]
[crates/gwiki/src/ingest/video/mod.rs:94-101]
- [[code/files/crates/gwiki/src/ingest/video/processing.rs|crates/gwiki/src/ingest/video/processing.rs]] - `crates/gwiki/src/ingest/video/processing.rs` exposes 14 indexed API symbols.
[crates/gwiki/src/ingest/video/processing.rs:19-27]
[crates/gwiki/src/ingest/video/processing.rs:29]
[crates/gwiki/src/ingest/video/processing.rs:31-43]
[crates/gwiki/src/ingest/video/processing.rs:32-34]
[crates/gwiki/src/ingest/video/processing.rs:36-42]
- [[code/files/crates/gwiki/src/ingest/video/tests.rs|crates/gwiki/src/ingest/video/tests.rs]] - `crates/gwiki/src/ingest/video/tests.rs` exposes 40 indexed API symbols.
[crates/gwiki/src/ingest/video/tests.rs:18-55]
[crates/gwiki/src/ingest/video/tests.rs:57-62]
[crates/gwiki/src/ingest/video/tests.rs:64-89]
[crates/gwiki/src/ingest/video/tests.rs:65-72]
[crates/gwiki/src/ingest/video/tests.rs:74-88]

## Components

- `0f73f741-684f-5f38-bd36-2a015108be1c`
- `1d80e9b2-5f10-5876-a9d4-5956c0b32e8b`
- `91aa01f0-daef-5cbd-8483-b8b0705f3139`
- `bfece869-38bb-5912-bb51-36cb77bf9350`
- `3c714090-f85e-5e7e-838b-1c81cd0bc1c3`
- `4620ed09-061f-5909-8ffa-96abfbdedcbf`
- `80bc3c4e-2d2e-5b52-81b1-aaf1e3e12b1d`
- `5cef0615-849a-5088-9727-c0d3a43555eb`
- `50c14da7-1f27-51f7-a67b-5c60ec275906`
- `972281b0-e102-5a09-82ba-87d19a7ebc0b`
- `9133f29e-aa1d-5869-9bf9-5c593208edd8`
- `99efb05f-bbb7-5205-b58f-843ed69390ab`
- `e81b3e56-aedc-5b3a-935f-bd7f603553ff`
- `521c2914-23e3-5739-8188-2fe2932edb7a`
- `3beca2e6-d782-5ffb-b886-407e6a2de49e`
- `bbc51501-3e90-5f4b-871a-535f22479abd`
- `c657b195-5289-5b67-a0ba-958e3da349da`
- `b409c024-aeea-5073-80e1-c17024d47587`
- `c32fba31-835d-5c73-bd48-880e8cfc3564`
- `994a622c-ec6c-54f1-b5aa-3b017ad88d7c`
- `1396e8ba-e260-5994-b347-daafdfe8aa50`
- `4905ee1a-2d61-5ef6-8213-c1df0913ab86`
- `2431a95c-38da-57fb-bbdb-26047af09bb7`
- `e2e9faf9-8212-5d16-a63a-4a067a5eb1a7`
- `21182664-a2b5-5cd7-9d99-6ae85a3c7847`
- `1e146573-9caf-54df-bde3-29dc65f89ef0`
- `1eb6254e-6880-53bb-85cc-7c4fad4c027b`
- `aa4e5ece-e989-5cf2-8588-90ff29913d28`
- `bf8a078a-8d39-5807-953b-efef9318eba4`
- `ba46913c-27c4-5ba6-8b10-a41a88f447fb`
- `49640cb4-d1e6-50ac-be41-b0b703a8d66e`
- `f93bceec-197e-5356-9fca-063082335497`
- `3b3378c5-f3ac-5c93-a480-85348f94f8a8`
- `2d55b0d0-332d-5041-9eea-c36fc7e1304f`
- `6599d8b6-68b7-50cd-84ae-046dd4e3ed5c`
- `ed0c7b5a-9b6d-588d-ae66-3a030e0a15c3`
- `427a3ebd-198d-5509-a7f8-0abaf4d4a319`
- `84e42e3a-b0bf-5ae2-9354-0815178cd1f2`
- `627958e7-df90-555d-a36a-fc08fbf14048`
- `28f836b4-c6ff-5d8f-984d-d99c991de698`
- `bc0764a2-32f9-571e-87ee-d99e82f20ccc`
- `a0a23429-0424-57a3-b5fd-13ea091bbfdd`
- `6fe6a29e-fafe-53be-b386-2eeb025e3a01`
- `9146306b-2686-5e09-b94b-d5b169eb23dc`
- `a3834ae2-950b-523b-92bb-d69eb0d6195a`
- `8a5f752e-85ed-5180-b3fe-34068e4b3548`
- `7634aaa1-d856-536e-985b-11ab648dec09`
- `c2f5b665-933d-5f81-afa2-fc56cebe3e4b`
- `c6035b26-69a5-5b46-a077-07fedb3d4c87`
- `2b5129ed-040c-551b-8d54-da41506f32e7`
- `074f384b-69b7-5eb6-bba7-e0bb059f81f0`
- `0bd60ab9-5261-536e-a80e-788ea3c857c5`
- `a603bcad-4fcd-54f2-81b2-5ba9b97a405a`
- `79609895-2dcb-52d1-9033-b874fb68b239`
- `b104f54a-e209-5f01-bcc7-d4d1bf64f502`
- `de4eecf8-ad8d-5b21-9473-0a4eb960ea34`
- `4bc6d4ed-8301-5a02-90e9-be584007143c`
- `547464b0-b252-56cc-a798-5164906d7626`
- `e9605554-53ea-5ac0-b5dc-c3b7f3949db5`
- `ae72fad5-9e80-5735-9934-af36d7695c41`
- `f34e3ae0-b8f4-53d2-8da9-44382bf277dc`
- `02593ae8-1a2f-50d9-82a1-1dea8d53fdc2`
- `847c1a28-b1ce-5592-ab9f-5825914b7c91`
- `71cd094a-16cc-5dd6-8843-fc486168dab4`
- `0aa4f156-daae-5d72-a3f8-b83095fb513b`
- `895d57e3-7ad0-5a75-8a35-cc62da58f7c0`
- `b77dc663-8a9c-5d29-a57c-6ea055071c98`
- `0e1f4984-bc24-5a06-92a9-b83da3b5ee3c`
- `25fc4dd3-52da-590c-940d-eb8b45c68bf5`
- `2ac4734d-0a13-58fa-a225-8e35329ea7e6`
- `cd99e40c-1b79-5bb7-b2ca-50f931bdcc45`
- `c26036ec-d3f9-5685-a445-2c62c4ae7dbf`
- `fe46f63f-87ee-5162-b3b0-726f2450a800`
- `886701b0-1a31-5b4c-8e77-b243e3b8f736`
- `8ee2d07c-6db2-55a0-83ea-57e8e95e69b0`
- `0112e846-ae5c-5943-9155-b825f5da1b6e`
- `77753645-33aa-5eb6-addd-cf1b2d84b23d`
- `3836250a-4708-52e4-b189-353890de8382`
- `69f4c775-a8b9-5257-8d30-c4b1054bdb4b`

