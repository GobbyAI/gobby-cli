---
title: crates/gwiki/src/ingest/video
type: code_module
provenance:
- file: crates/gwiki/src/ingest/video/assets.rs
  ranges:
  - 4-23
  - 25-115
  - 118-122
  - 126-206
  - 208-212
  - 214-224
  - 226-242
- file: crates/gwiki/src/ingest/video/metadata.rs
  ranges:
  - 4-8
  - 10-25
  - 27-39
  - 43-57
  - 59-73
  - 76-84
  - 86-127
  - 129-134
- file: crates/gwiki/src/ingest/video/mod.rs
  ranges:
  - 32-45
  - 48-61
  - 64-73
  - 76-94
  - 97-104
  - 107-126
  - 128-163
  - 166-179
  - 181-235
- file: crates/gwiki/src/ingest/video/processing.rs
  ranges:
  - 18-26
  - '28'
  - 30-42
  - 45-64
  - 66-179
  - 181-197
  - 199-209
  - 212-216
  - 218-223
  - 225-333
  - 335-339
- file: crates/gwiki/src/ingest/video/tests.rs
  ranges:
  - 18-55
  - 57-62
  - 64-89
  - 91-111
  - '113'
  - 115-131
  - '133'
  - 135-144
  - '146'
  - 148-160
  - '162'
  - 164-170
  - 172-198
  - 201-273
  - 276-323
  - 326-329
  - 332-350
  - 354-446
  - 449-451
  - 454-461
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

The video ingest module turns fetched or file-backed video sources into wiki assets, metadata, transcripts, frame samples, and derived markdown. Its central data shapes are `VideoSnapshot`, `VideoFileSnapshot`, and `VideoIngestResult`, which carry source identity, media bytes or paths, timing, extracted frame information, transcript segments, optional transcription output, and the resulting source record [crates/gwiki/src/ingest/video/mod.rs:32-45] [crates/gwiki/src/ingest/video/mod.rs:48-61] [crates/gwiki/src/ingest/video/mod.rs:64-73]. The public orchestration layers start from generic video ingest entry points and branch into file-based, degraded, production-processing, and without-index variants so callers can choose whether extraction/transcription work is followed by vault reindexing [crates/gwiki/src/ingest/video/mod.rs:76-94] [crates/gwiki/src/ingest/video/mod.rs:97-104].

The asset path owns persistence: it registers the source, writes the original asset, gathers file metadata, renders raw markdown, optionally samples frames, persists frame assets, and cleans up temporary frame sources afterward [crates/gwiki/src/ingest/video/assets.rs:25-115] [crates/gwiki/src/ingest/video/assets.rs:126-206] [crates/gwiki/src/ingest/video/assets.rs:208-212]. The processing path supplies the media-heavy work through a `VideoMediaExtractor` trait; the production implementation delegates audio extraction and frame sampling to `crate::media`, then the ingest flow transcribes audio, describes sampled frames through vision, classifies degradations, and packages the result before optional indexing [crates/gwiki/src/ingest/video/processing.rs:18-26] [crates/gwiki/src/ingest/video/processing.rs:30-42] [crates/gwiki/src/ingest/video/processing.rs:35-41].

The metadata helpers keep the rest of the module’s data transformation small and shared. `VideoDegradationContext` carries media and transcription degradation state, `video_media_metadata` stats the stored asset, `VideoSnapshotRef` provides borrowed access over either snapshot type, and render helpers convert snapshots, transcripts, frame descriptions, and timestamps into raw ingest output and markdown [crates/gwiki/src/ingest/video/metadata.rs:4-8] [crates/gwiki/src/ingest/video/metadata.rs:10-25] [crates/gwiki/src/ingest/video/metadata.rs:27-39] [crates/gwiki/src/ingest/video/metadata.rs:43-57] [crates/gwiki/src/ingest/video/metadata.rs:59-73]. Tests mirror those collaboration points with fake media extractors, transcription clients, vision clients, temporary file helpers, and coverage for success and failure paths including transcript/frame generation, disabled frame sampling, degradation classification, and cleanup behavior .

## Call Diagram

```mermaid
sequenceDiagram
    participant m_05e2eb59_486c_5722_8d2a_9911584d43a2 as ingest_video_file_with_degradations &#91;function&#93;
    participant m_14dc0b77_aa41_552a_8225_43d99624d4cb as ingest_with_media &#91;function&#93;
    participant m_1a71190e_9caf_5a2d_aa02_dbcd3509a583 as video_media_degradation &#91;function&#93;
    participant m_20cdcda4_4cc2_5909_88a4_4b3e55563ae5 as stores_file_backed_video &#91;function&#93;
    participant m_28f836b4_c6ff_5d8f_984d_d99c991de698 as sample_snapshot &#91;function&#93;
    participant m_2dd8e101_7a17_5aaa_a693_020813b3ab27 as ingest_video_file_with_processing_without_index &#91;function&#93;
    participant m_2f4bef6e_9032_5bfb_a651_6e62ae0b3fab as ingest_video_file &#91;function&#93;
    participant m_3d56c967_3261_504b_adaa_7baee72ec3b3 as assert_asset_preserved &#91;function&#93;
    participant m_3e091d5b_55e6_50c2_9fcc_1e1d5e23504e as cleanup_sampled_temp_frame_sources &#91;function&#93;
    participant m_547464b0_b252_56cc_a798_5164906d7626 as transcript_output &#91;function&#93;
    participant m_6fe6a29e_fafe_53be_b386_2eeb025e3a01 as FakeVideoMediaExtractor.extract_audio &#91;method&#93;
    participant m_72be120b_fa86_5597_904e_dd257f05417a as persist_video_frame_assets &#91;function&#93;
    participant m_8cf190f9_bad1_5a10_bc1a_1e9f953f3aa6 as production_ingest_applies_degradation_matrix &#91;function&#93;
    participant m_9146306b_2686_5e09_b94b_d5b169eb23dc as FakeVideoMediaExtractor.sample_frame_images &#91;method&#93;
    participant m_91beae62_064b_50ee_a889_d2fb4e4e8d44 as ingest_video_file_with_degradations_without_index &#91;function&#93;
    participant m_973f3faf_ba04_5707_bb88_b95f33938319 as message_is_ffmpeg_unavailable &#91;function&#93;
    participant m_9ab8814d_fbde_559b_93d7_7f2a1255caae as ingest_video_file_with_processing &#91;function&#93;
    participant m_a3834ae2_950b_523b_92bb_d69eb0d6195a as temp_file_with_bytes &#91;function&#93;
    participant m_a5edac93_13d8_5d97_8a14_c3f378fed35c as persisted_frame_read_failure_drops_remaining_kept_temp_frames &#91;function&#93;
    participant m_a8e435e0_1b17_5b2e_a62c_69a4fea7a6aa as ingest_video_with_asset_without_index &#91;function&#93;
    participant m_c0627ab3_7704_5909_867c_8ffe194fae67 as remove_sampled_temp_frame &#91;function&#93;
    participant m_c07db945_5200_5fa4_9820_a9f82b6d1b50 as read_derived &#91;function&#93;
    participant m_c2f5b665_933d_5f81_afa2_fc56cebe3e4b as FakeTranscriptionClient.transcribe &#91;method&#93;
    participant m_cbf01c09_b53c_596c_a141_2b477d8fa40b as ingest_video_with_asset &#91;function&#93;
    participant m_dd3d356f_1fcf_55b8_bad0_1fbb2a9cd1d5 as frame_vision_failure_keeps_sample_without_description &#91;function&#93;
    participant m_e202b50b_cb72_5795_a111_63bee2362785 as cleanup_deferred_temp_frame_sources &#91;function&#93;
    participant m_e87fb9d9_8b4d_59b8_87b7_589e77628835 as describe_frame_images &#91;function&#93;
    m_05e2eb59_486c_5722_8d2a_9911584d43a2->>m_91beae62_064b_50ee_a889_d2fb4e4e8d44: calls
    m_1a71190e_9caf_5a2d_aa02_dbcd3509a583->>m_973f3faf_ba04_5707_bb88_b95f33938319: calls
    m_20cdcda4_4cc2_5909_88a4_4b3e55563ae5->>m_28f836b4_c6ff_5d8f_984d_d99c991de698: calls
    m_2dd8e101_7a17_5aaa_a693_020813b3ab27->>m_1a71190e_9caf_5a2d_aa02_dbcd3509a583: calls
    m_2dd8e101_7a17_5aaa_a693_020813b3ab27->>m_e87fb9d9_8b4d_59b8_87b7_589e77628835: calls
    m_2f4bef6e_9032_5bfb_a651_6e62ae0b3fab->>m_05e2eb59_486c_5722_8d2a_9911584d43a2: calls
    m_6fe6a29e_fafe_53be_b386_2eeb025e3a01->>m_a3834ae2_950b_523b_92bb_d69eb0d6195a: calls
    m_72be120b_fa86_5597_904e_dd257f05417a->>m_3e091d5b_55e6_50c2_9fcc_1e1d5e23504e: calls
    m_72be120b_fa86_5597_904e_dd257f05417a->>m_c0627ab3_7704_5909_867c_8ffe194fae67: calls
    m_72be120b_fa86_5597_904e_dd257f05417a->>m_e202b50b_cb72_5795_a111_63bee2362785: calls
    m_8cf190f9_bad1_5a10_bc1a_1e9f953f3aa6->>m_14dc0b77_aa41_552a_8225_43d99624d4cb: calls
    m_8cf190f9_bad1_5a10_bc1a_1e9f953f3aa6->>m_3d56c967_3261_504b_adaa_7baee72ec3b3: calls
    m_8cf190f9_bad1_5a10_bc1a_1e9f953f3aa6->>m_c07db945_5200_5fa4_9820_a9f82b6d1b50: calls
    m_9146306b_2686_5e09_b94b_d5b169eb23dc->>m_a3834ae2_950b_523b_92bb_d69eb0d6195a: calls
    m_9ab8814d_fbde_559b_93d7_7f2a1255caae->>m_2dd8e101_7a17_5aaa_a693_020813b3ab27: calls
    m_a5edac93_13d8_5d97_8a14_c3f378fed35c->>m_a3834ae2_950b_523b_92bb_d69eb0d6195a: calls
    m_a8e435e0_1b17_5b2e_a62c_69a4fea7a6aa->>m_72be120b_fa86_5597_904e_dd257f05417a: calls
    m_c2f5b665_933d_5f81_afa2_fc56cebe3e4b->>m_547464b0_b252_56cc_a798_5164906d7626: calls
    m_cbf01c09_b53c_596c_a141_2b477d8fa40b->>m_a8e435e0_1b17_5b2e_a62c_69a4fea7a6aa: calls
    m_dd3d356f_1fcf_55b8_bad0_1fbb2a9cd1d5->>m_a3834ae2_950b_523b_92bb_d69eb0d6195a: calls
```

## Files

- [[code/files/crates/gwiki/src/ingest/video/assets.rs|crates/gwiki/src/ingest/video/assets.rs]] - This file implements video ingestion when an asset file is being written, with one wrapper that also reindexes the vault afterward and a core path that performs the ingest work without indexing. The main flow registers the video source, writes the asset, gathers media metadata, renders and saves raw markdown, samples frames when enabled, and then persists the resulting frame assets. The cleanup helpers remove deferred or sampled temporary frame sources after persistence so the ingest pipeline leaves only the finalized video assets behind.
[crates/gwiki/src/ingest/video/assets.rs:4-23]
[crates/gwiki/src/ingest/video/assets.rs:25-115]
[crates/gwiki/src/ingest/video/assets.rs:118-122]
[crates/gwiki/src/ingest/video/assets.rs:126-206]
[crates/gwiki/src/ingest/video/assets.rs:208-212]
- [[code/files/crates/gwiki/src/ingest/video/metadata.rs|crates/gwiki/src/ingest/video/metadata.rs]] - This module collects the small data-shaping helpers used by video ingestion. It defines `VideoDegradationContext` to carry degradation settings, `video_media_metadata` to stat the video asset and build `VideoMediaMetadata`, and `VideoSnapshotRef` plus its `from_snapshot`/`from_file_snapshot` constructors to expose borrowed views over full or file-backed video snapshots. It also provides `IngestResult::from`, `render_raw_video_markdown`, and `format_timestamp` to turn snapshot and transcript data into ingest output and formatted markdown.
[crates/gwiki/src/ingest/video/metadata.rs:4-8]
[crates/gwiki/src/ingest/video/metadata.rs:10-25]
[crates/gwiki/src/ingest/video/metadata.rs:27-39]
[crates/gwiki/src/ingest/video/metadata.rs:43-57]
[crates/gwiki/src/ingest/video/metadata.rs:59-73]
- [[code/files/crates/gwiki/src/ingest/video/mod.rs|crates/gwiki/src/ingest/video/mod.rs]] - This module defines the video-ingest data shapes and orchestration entry points for turning a video source into derived wiki assets. `VideoSnapshot` and `VideoFileSnapshot` capture the fetched media state plus extracted frames, frame descriptions, transcript segments, and optional transcription output, while `VideoIngestResult` packages the resulting source record and any generated metadata. The ingest functions layer the workflow from a generic `ingest_video` entry point down through file-based paths, with variants that either use degraded processing or production processing, and corresponding “without_index” helpers that perform the extraction/transcription work and then feed the results into the shared ingest/indexing pipeline.
[crates/gwiki/src/ingest/video/mod.rs:32-45]
[crates/gwiki/src/ingest/video/mod.rs:48-61]
[crates/gwiki/src/ingest/video/mod.rs:64-73]
[crates/gwiki/src/ingest/video/mod.rs:76-94]
[crates/gwiki/src/ingest/video/mod.rs:97-104]
- [[code/files/crates/gwiki/src/ingest/video/processing.rs|crates/gwiki/src/ingest/video/processing.rs]] - This file defines the video-processing pipeline used during ingest: a `VideoMediaExtractor` abstraction with a production implementation that delegates audio extraction and frame sampling to `crate::media`, plus entry points that ingest a video with processing and optionally reindex the vault afterward. The main ingest path derives frame intervals, runs transcription and vision-based frame description work, records media degradations when extraction fails or FFmpeg is unavailable, and packages the results into a `VideoIngestResult`; helper types and functions support frame-description assembly, error classification, timestamp labeling, and best-effort cleanup of kept temporary frame files.
[crates/gwiki/src/ingest/video/processing.rs:18-26]
[crates/gwiki/src/ingest/video/processing.rs:28]
[crates/gwiki/src/ingest/video/processing.rs:30-42]
[crates/gwiki/src/ingest/video/processing.rs:31-33]
[crates/gwiki/src/ingest/video/processing.rs:35-41]
- [[code/files/crates/gwiki/src/ingest/video/tests.rs|crates/gwiki/src/ingest/video/tests.rs]] - Test support and integration coverage for video ingestion. The file defines fixtures and mock `VideoMediaExtractor`, `TranscriptionClient`, and `VisionClient` implementations for both success and failure paths, plus a helper for writing temporary files and building transcription outputs.

Those pieces feed a suite of ingestion tests that verify frame sampling, transcript alignment, media degradation behavior, persistence of original and derived assets, and provenance metadata across normal and error scenarios.
[crates/gwiki/src/ingest/video/tests.rs:18-55]
[crates/gwiki/src/ingest/video/tests.rs:57-62]
[crates/gwiki/src/ingest/video/tests.rs:64-89]
[crates/gwiki/src/ingest/video/tests.rs:65-72]
[crates/gwiki/src/ingest/video/tests.rs:74-88]

## Components

- `cbf01c09-b53c-596c-a141-2b477d8fa40b`
- `a8e435e0-1b17-5b2e-a62c-69a4fea7a6aa`
- `841887f8-f365-5572-926f-ec44648f2c26`
- `72be120b-fa86-5597-904e-dd257f05417a`
- `e202b50b-cb72-5795-a111-63bee2362785`
- `c0627ab3-7704-5909-867c-8ffe194fae67`
- `3e091d5b-55e6-50c2-9fcc-1e1d5e23504e`
- `5cef0615-849a-5088-9727-c0d3a43555eb`
- `50c14da7-1f27-51f7-a67b-5c60ec275906`
- `972281b0-e102-5a09-82ba-87d19a7ebc0b`
- `3522703e-16f5-5898-9feb-e0b52ecbb815`
- `75e3be97-d080-5235-bd93-6bcc2727e1bb`
- `9b8d0d23-cc4d-5679-b896-9f2d56f3ffbf`
- `e26ab6b0-6585-5980-b440-3ac9a7b01222`
- `c50d2c8f-1fc1-52f7-8b50-2ddcbec19ec6`
- `cd0dca05-9cc7-5c6f-a9d2-87f9d92709fe`
- `dd142d97-67d1-5b19-8944-61495d5dbd56`
- `37a00017-4190-5aed-af26-17a9be16f909`
- `90aa09d2-4e3d-5179-80a2-29d1ac9a90e7`
- `da11a34a-ca1b-5284-bfb4-5460849abd5c`
- `2f4bef6e-9032-5bfb-a651-6e62ae0b3fab`
- `05e2eb59-486c-5722-8d2a-9911584d43a2`
- `91beae62-064b-50ee-a889-d2fb4e4e8d44`
- `e1826708-fc51-5518-8657-df2ea7c4d3f3`
- `8d9c3b8e-052f-5f35-bfc8-9a4fa176a9db`
- `feea3095-1de5-5d20-841d-a034f7b03e2c`
- `7182cf5d-71b8-5945-ad4c-d57b815a0f73`
- `d28d9fed-47c0-5683-89b3-92e0b8a462ce`
- `ecaf1caf-2d02-5431-b0c3-2ac9526efde9`
- `6eeb7aba-df07-5af4-8da7-dc95e75b8acd`
- `9ab8814d-fbde-559b-93d7-7f2a1255caae`
- `2dd8e101-7a17-5aaa-a693-020813b3ab27`
- `1a71190e-9caf-5a2d-aa02-dbcd3509a583`
- `973f3faf-ba04-5707-bb88-b95f33938319`
- `dd498a39-6aca-56f5-a7a8-3672a4892e7e`
- `4e412cc1-28bd-572f-bf6c-a91bd5bfc35a`
- `e87fb9d9-8b4d-59b8-87b7-589e77628835`
- `8c7b0327-80cc-5b3a-ac12-1ce0464a5efa`
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
- `1464dc9d-e3b8-54c1-94bb-7c970a24ae49`
- `0eb69051-4979-5da3-b89a-8d20dcec381b`
- `616c329d-4177-548a-b3ea-acc4b7d7a671`
- `8cf190f9-bad1-5a10-bc1a-1e9f953f3aa6`
- `0cf6073c-f8fc-50a3-9a1a-0b48baa93ec4`
- `dd3d356f-1fcf-55b8-bad0-1fbb2a9cd1d5`
- `f1e9a1f7-f166-5142-ac72-764d7ee39ff2`
- `a5edac93-13d8-5d97-8a14-c3f378fed35c`
- `14dc0b77-aa41-552a-8225-43d99624d4cb`
- `c07db945-5200-5fa4-9820-a9f82b6d1b50`
- `3d56c967-3261-504b-adaa-7baee72ec3b3`
- `ebd3a24f-e915-5078-a16a-46c06578e2e3`
- `20cdcda4-4cc2-5909-88a4-4b3e55563ae5`
- `f5a59646-decf-5327-80f2-95c90cd74d8e`

