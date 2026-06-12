---
title: crates/gwiki/src/ingest/video/processing.rs
type: code_file
provenance:
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
  - 225-329
  - 331-335
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/processing.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

`crates/gwiki/src/ingest/video/processing.rs` exposes 13 indexed API symbols.
[crates/gwiki/src/ingest/video/processing.rs:18-26]
[crates/gwiki/src/ingest/video/processing.rs:28]
[crates/gwiki/src/ingest/video/processing.rs:30-42]
[crates/gwiki/src/ingest/video/processing.rs:31-33]
[crates/gwiki/src/ingest/video/processing.rs:35-41]

## API Symbols

- `VideoMediaExtractor` (type) component `VideoMediaExtractor [type]` (`feea3095-1de5-5d20-841d-a034f7b03e2c`) lines 18-26 [crates/gwiki/src/ingest/video/processing.rs:18-26]
  - Signature: `pub(crate) trait VideoMediaExtractor {`
  - Purpose: Indexed type `VideoMediaExtractor` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:18-26]
- `ProductionVideoMediaExtractor` (class) component `ProductionVideoMediaExtractor [class]` (`7182cf5d-71b8-5945-ad4c-d57b815a0f73`) lines 28-28 [crates/gwiki/src/ingest/video/processing.rs:28]
  - Signature: `pub(crate) struct ProductionVideoMediaExtractor;`
  - Purpose: Indexed class `ProductionVideoMediaExtractor` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:28]
- `ProductionVideoMediaExtractor` (class) component `ProductionVideoMediaExtractor [class]` (`d28d9fed-47c0-5683-89b3-92e0b8a462ce`) lines 30-42 [crates/gwiki/src/ingest/video/processing.rs:30-42]
  - Signature: `impl VideoMediaExtractor for ProductionVideoMediaExtractor {`
  - Purpose: Indexed class `ProductionVideoMediaExtractor` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:30-42]
- `ProductionVideoMediaExtractor.extract_audio` (method) component `ProductionVideoMediaExtractor.extract_audio [method]` (`ecaf1caf-2d02-5431-b0c3-2ac9526efde9`) lines 31-33 [crates/gwiki/src/ingest/video/processing.rs:31-33]
  - Signature: `fn extract_audio(&self, video: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Indexed method `ProductionVideoMediaExtractor.extract_audio` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:31-33]
- `ProductionVideoMediaExtractor.sample_frame_images` (method) component `ProductionVideoMediaExtractor.sample_frame_images [method]` (`6eeb7aba-df07-5af4-8da7-dc95e75b8acd`) lines 35-41 [crates/gwiki/src/ingest/video/processing.rs:35-41]
  - Signature: `fn sample_frame_images(`
  - Purpose: Indexed method `ProductionVideoMediaExtractor.sample_frame_images` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:35-41]
- `ingest_video_file_with_processing` (function) component `ingest_video_file_with_processing [function]` (`9ab8814d-fbde-559b-93d7-7f2a1255caae`) lines 45-64 [crates/gwiki/src/ingest/video/processing.rs:45-64]
  - Signature: `pub(crate) fn ingest_video_file_with_processing(`
  - Purpose: Indexed function `ingest_video_file_with_processing` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:45-64]
- `ingest_video_file_with_processing_without_index` (function) component `ingest_video_file_with_processing_without_index [function]` (`2dd8e101-7a17-5aaa-a693-020813b3ab27`) lines 66-179 [crates/gwiki/src/ingest/video/processing.rs:66-179]
  - Signature: `pub(crate) fn ingest_video_file_with_processing_without_index(`
  - Purpose: Indexed function `ingest_video_file_with_processing_without_index` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:66-179]
- `video_media_degradation` (function) component `video_media_degradation [function]` (`1a71190e-9caf-5a2d-aa02-dbcd3509a583`) lines 181-197 [crates/gwiki/src/ingest/video/processing.rs:181-197]
  - Signature: `pub(crate) fn video_media_degradation(`
  - Purpose: Indexed function `video_media_degradation` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:181-197]
- `message_is_ffmpeg_unavailable` (function) component `message_is_ffmpeg_unavailable [function]` (`973f3faf-ba04-5707-bb88-b95f33938319`) lines 199-209 [crates/gwiki/src/ingest/video/processing.rs:199-209]
  - Signature: `fn message_is_ffmpeg_unavailable(message: &str) -> bool {`
  - Purpose: Indexed function `message_is_ffmpeg_unavailable` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:199-209]
- `DescribedFrameImages` (class) component `DescribedFrameImages [class]` (`dd498a39-6aca-56f5-a7a8-3672a4892e7e`) lines 212-216 [crates/gwiki/src/ingest/video/processing.rs:212-216]
  - Signature: `pub(crate) struct DescribedFrameImages {`
  - Purpose: Indexed class `DescribedFrameImages` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:212-216]
- `PendingFrameImage` (class) component `PendingFrameImage [class]` (`4e412cc1-28bd-572f-bf6c-a91bd5bfc35a`) lines 218-223 [crates/gwiki/src/ingest/video/processing.rs:218-223]
  - Signature: `pub(crate) struct PendingFrameImage {`
  - Purpose: Indexed class `PendingFrameImage` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:218-223]
- `describe_frame_images` (function) component `describe_frame_images [function]` (`e87fb9d9-8b4d-59b8-87b7-589e77628835`) lines 225-329 [crates/gwiki/src/ingest/video/processing.rs:225-329]
  - Signature: `pub(crate) fn describe_frame_images(`
  - Purpose: Indexed function `describe_frame_images` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:225-329]
- `cleanup_kept_temp_frames` (function) component `cleanup_kept_temp_frames [function]` (`95b17763-51ac-5490-95e9-5aa1ba2dba46`) lines 331-335 [crates/gwiki/src/ingest/video/processing.rs:331-335]
  - Signature: `pub(crate) fn cleanup_kept_temp_frames(paths: &[PathBuf]) {`
  - Purpose: Indexed function `cleanup_kept_temp_frames` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:331-335]

