---
title: crates/gwiki/src/ingest/video/processing.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/processing.rs
  ranges:
  - 18-26
  - '28'
  - 31-33
  - 35-41
  - 45-64
  - 66-179
  - 181-197
  - 199-209
  - 212-216
  - 218-223
  - 225-333
  - 335-339
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/video/processing.rs:18-26](crates/gwiki/src/ingest/video/processing.rs#L18-L26), [crates/gwiki/src/ingest/video/processing.rs:28](crates/gwiki/src/ingest/video/processing.rs#L28), [crates/gwiki/src/ingest/video/processing.rs:31-33](crates/gwiki/src/ingest/video/processing.rs#L31-L33), [crates/gwiki/src/ingest/video/processing.rs:35-41](crates/gwiki/src/ingest/video/processing.rs#L35-L41), [crates/gwiki/src/ingest/video/processing.rs:45-64](crates/gwiki/src/ingest/video/processing.rs#L45-L64), [crates/gwiki/src/ingest/video/processing.rs:66-179](crates/gwiki/src/ingest/video/processing.rs#L66-L179), [crates/gwiki/src/ingest/video/processing.rs:181-197](crates/gwiki/src/ingest/video/processing.rs#L181-L197), [crates/gwiki/src/ingest/video/processing.rs:199-209](crates/gwiki/src/ingest/video/processing.rs#L199-L209), [crates/gwiki/src/ingest/video/processing.rs:212-216](crates/gwiki/src/ingest/video/processing.rs#L212-L216), [crates/gwiki/src/ingest/video/processing.rs:218-223](crates/gwiki/src/ingest/video/processing.rs#L218-L223), [crates/gwiki/src/ingest/video/processing.rs:225-333](crates/gwiki/src/ingest/video/processing.rs#L225-L333), [crates/gwiki/src/ingest/video/processing.rs:335-339](crates/gwiki/src/ingest/video/processing.rs#L335-L339)

</details>

# crates/gwiki/src/ingest/video/processing.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the video-ingest processing pipeline. It abstracts media access behind `VideoMediaExtractor`, provides the production extractor that delegates to the crate’s audio and frame-sampling helpers, and exposes two ingest entry points: one that runs processing and then reindexes the vault, and one that performs the same work without indexing. The rest of the file supports that workflow by classifying video media degradations, detecting ffmpeg-unavailable errors, wrapping described and pending frame images, generating frame descriptions from sampled images via the vision endpoint, and cleaning up temporary frame files that should be kept.
[crates/gwiki/src/ingest/video/processing.rs:18-26]
[crates/gwiki/src/ingest/video/processing.rs:28]
[crates/gwiki/src/ingest/video/processing.rs:31-33]
[crates/gwiki/src/ingest/video/processing.rs:35-41]
[crates/gwiki/src/ingest/video/processing.rs:45-64]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `VideoMediaExtractor` | type | `pub(crate) trait VideoMediaExtractor {` | `VideoMediaExtractor [type]` | `feea3095-1de5-5d20-841d-a034f7b03e2c` | 18-26 [crates/gwiki/src/ingest/video/processing.rs:18-26] | Indexed type `VideoMediaExtractor` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:18-26] |
| `ProductionVideoMediaExtractor` | class | `pub(crate) struct ProductionVideoMediaExtractor;` | `ProductionVideoMediaExtractor [class]` | `7182cf5d-71b8-5945-ad4c-d57b815a0f73` | 28-28 [crates/gwiki/src/ingest/video/processing.rs:28] | Indexed class `ProductionVideoMediaExtractor` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:28] |
| `ProductionVideoMediaExtractor::extract_audio` | method | `fn extract_audio(&self, video: &Path) -> Result<NamedTempFile, WikiError> {` | `ProductionVideoMediaExtractor::extract_audio [method]` | `ecaf1caf-2d02-5431-b0c3-2ac9526efde9` | 31-33 [crates/gwiki/src/ingest/video/processing.rs:31-33] | Indexed method `ProductionVideoMediaExtractor::extract_audio` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:31-33] |
| `ProductionVideoMediaExtractor::sample_frame_images` | method | `fn sample_frame_images(` | `ProductionVideoMediaExtractor::sample_frame_images [method]` | `6eeb7aba-df07-5af4-8da7-dc95e75b8acd` | 35-41 [crates/gwiki/src/ingest/video/processing.rs:35-41] | Indexed method `ProductionVideoMediaExtractor::sample_frame_images` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:35-41] |
| `ingest_video_file_with_processing` | function | `pub(crate) fn ingest_video_file_with_processing(` | `ingest_video_file_with_processing [function]` | `9ab8814d-fbde-559b-93d7-7f2a1255caae` | 45-64 [crates/gwiki/src/ingest/video/processing.rs:45-64] | Indexed function `ingest_video_file_with_processing` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:45-64] |
| `ingest_video_file_with_processing_without_index` | function | `pub(crate) fn ingest_video_file_with_processing_without_index(` | `ingest_video_file_with_processing_without_index [function]` | `2dd8e101-7a17-5aaa-a693-020813b3ab27` | 66-179 [crates/gwiki/src/ingest/video/processing.rs:66-179] | Indexed function `ingest_video_file_with_processing_without_index` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:66-179] |
| `video_media_degradation` | function | `pub(crate) fn video_media_degradation(` | `video_media_degradation [function]` | `1a71190e-9caf-5a2d-aa02-dbcd3509a583` | 181-197 [crates/gwiki/src/ingest/video/processing.rs:181-197] | Indexed function `video_media_degradation` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:181-197] |
| `message_is_ffmpeg_unavailable` | function | `fn message_is_ffmpeg_unavailable(message: &str) -> bool {` | `message_is_ffmpeg_unavailable [function]` | `973f3faf-ba04-5707-bb88-b95f33938319` | 199-209 [crates/gwiki/src/ingest/video/processing.rs:199-209] | Indexed function `message_is_ffmpeg_unavailable` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:199-209] |
| `DescribedFrameImages` | class | `pub(crate) struct DescribedFrameImages {` | `DescribedFrameImages [class]` | `dd498a39-6aca-56f5-a7a8-3672a4892e7e` | 212-216 [crates/gwiki/src/ingest/video/processing.rs:212-216] | Indexed class `DescribedFrameImages` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:212-216] |
| `PendingFrameImage` | class | `pub(crate) struct PendingFrameImage {` | `PendingFrameImage [class]` | `4e412cc1-28bd-572f-bf6c-a91bd5bfc35a` | 218-223 [crates/gwiki/src/ingest/video/processing.rs:218-223] | Indexed class `PendingFrameImage` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:218-223] |
| `describe_frame_images` | function | `pub(crate) fn describe_frame_images(` | `describe_frame_images [function]` | `e87fb9d9-8b4d-59b8-87b7-589e77628835` | 225-333 [crates/gwiki/src/ingest/video/processing.rs:225-333] | Indexed function `describe_frame_images` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:225-333] |
| `cleanup_kept_temp_frames` | function | `pub(crate) fn cleanup_kept_temp_frames(paths: &[PathBuf]) {` | `cleanup_kept_temp_frames [function]` | `8c7b0327-80cc-5b3a-ac12-1ce0464a5efa` | 335-339 [crates/gwiki/src/ingest/video/processing.rs:335-339] | Indexed function `cleanup_kept_temp_frames` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:335-339] |
