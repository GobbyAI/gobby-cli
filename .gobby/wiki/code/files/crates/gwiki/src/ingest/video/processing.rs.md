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
  - 225-333
  - 335-339
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/processing.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

This file defines the video-processing pipeline used during ingest: a `VideoMediaExtractor` abstraction with a production implementation that delegates audio extraction and frame sampling to `crate::media`, plus entry points that ingest a video with processing and optionally reindex the vault afterward. The main ingest path derives frame intervals, runs transcription and vision-based frame description work, records media degradations when extraction fails or FFmpeg is unavailable, and packages the results into a `VideoIngestResult`; helper types and functions support frame-description assembly, error classification, timestamp labeling, and best-effort cleanup of kept temporary frame files.
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
  - Purpose: A crate-private unit-like struct ('ProductionVideoMediaExtractor') that serves as a zero-sized type marker for production video media extraction logic. [crates/gwiki/src/ingest/video/processing.rs:28]
- `ProductionVideoMediaExtractor` (class) component `ProductionVideoMediaExtractor [class]` (`d28d9fed-47c0-5683-89b3-92e0b8a462ce`) lines 30-42 [crates/gwiki/src/ingest/video/processing.rs:30-42]
  - Signature: `impl VideoMediaExtractor for ProductionVideoMediaExtractor {`
  - Purpose: 'ProductionVideoMediaExtractor' is a 'VideoMediaExtractor' implementation that delegates audio extraction and interval-based frame sampling to 'crate::media::extract_audio_file' and 'crate::media::sample_frame_images', returning temporary files and timestamps as 'WikiError'-wrapped results. [crates/gwiki/src/ingest/video/processing.rs:30-42]
- `ProductionVideoMediaExtractor.extract_audio` (method) component `ProductionVideoMediaExtractor.extract_audio [method]` (`ecaf1caf-2d02-5431-b0c3-2ac9526efde9`) lines 31-33 [crates/gwiki/src/ingest/video/processing.rs:31-33]
  - Signature: `fn extract_audio(&self, video: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Delegates to 'crate::media::extract_audio_file(video)' to extract audio from the given video path and return it as a temporary file or 'WikiError' on failure. [crates/gwiki/src/ingest/video/processing.rs:31-33]
- `ProductionVideoMediaExtractor.sample_frame_images` (method) component `ProductionVideoMediaExtractor.sample_frame_images [method]` (`6eeb7aba-df07-5af4-8da7-dc95e75b8acd`) lines 35-41 [crates/gwiki/src/ingest/video/processing.rs:35-41]
  - Signature: `fn sample_frame_images(`
  - Purpose: Delegates to 'crate::media::sample_frame_images(video, interval)' to sample frame images from the given video at the specified interval and return them as 'Result<Vec<(u64, NamedTempFile)>, WikiError>'. [crates/gwiki/src/ingest/video/processing.rs:35-41]
- `ingest_video_file_with_processing` (function) component `ingest_video_file_with_processing [function]` (`9ab8814d-fbde-559b-93d7-7f2a1255caae`) lines 45-64 [crates/gwiki/src/ingest/video/processing.rs:45-64]
  - Signature: `pub(crate) fn ingest_video_file_with_processing(`
  - Purpose: Calls 'ingest_video_file_with_processing_without_index' to ingest a video file, then reindexes the vault via 'index_after_ingest', and returns the resulting 'VideoIngestResult' or propagates any 'WikiError'. [crates/gwiki/src/ingest/video/processing.rs:45-64]
- `ingest_video_file_with_processing_without_index` (function) component `ingest_video_file_with_processing_without_index [function]` (`2dd8e101-7a17-5aaa-a693-020813b3ab27`) lines 66-179 [crates/gwiki/src/ingest/video/processing.rs:66-179]
  - Signature: `pub(crate) fn ingest_video_file_with_processing_without_index(`
  - Purpose: Ingests a video file by deriving a frame-sampling interval, attempting audio transcription while recording any transcription degradation, and returning a 'VideoIngestResult' from processed media without using an index. [crates/gwiki/src/ingest/video/processing.rs:66-179]
- `video_media_degradation` (function) component `video_media_degradation [function]` (`1a71190e-9caf-5a2d-aa02-dbcd3509a583`) lines 181-197 [crates/gwiki/src/ingest/video/processing.rs:181-197]
  - Signature: `pub(crate) fn video_media_degradation(`
  - Purpose: Constructs a 'VideoMediaDegradation' by converting 'kind' to a 'String', extracting the error message, setting 'reason' to '"ffmpeg_unavailable"' when the 'WikiError' indicates FFmpeg is unavailable otherwise using 'fallback_reason', and storing both the chosen reason and message in the returned struct. [crates/gwiki/src/ingest/video/processing.rs:181-197]
- `message_is_ffmpeg_unavailable` (function) component `message_is_ffmpeg_unavailable [function]` (`973f3faf-ba04-5707-bb88-b95f33938319`) lines 199-209 [crates/gwiki/src/ingest/video/processing.rs:199-209]
  - Signature: `fn message_is_ffmpeg_unavailable(message: &str) -> bool {`
  - Purpose: Returns 'true' when the input string, case-insensitively normalized to ASCII lowercase, contains any of several FFmpeg-missing indicators such as “ffmpeg is unavailable,” “ffmpeg executable not found,” or “ffmpeg was not found.” [crates/gwiki/src/ingest/video/processing.rs:199-209]
- `DescribedFrameImages` (class) component `DescribedFrameImages [class]` (`dd498a39-6aca-56f5-a7a8-3672a4892e7e`) lines 212-216 [crates/gwiki/src/ingest/video/processing.rs:212-216]
  - Signature: `pub(crate) struct DescribedFrameImages {`
  - Purpose: 'DescribedFrameImages' is a crate-visible struct that groups parallel vectors of 'VideoFrameSample's, 'PathBuf's, and 'VideoFrameDescription's for a set of described frame images. [crates/gwiki/src/ingest/video/processing.rs:212-216]
- `PendingFrameImage` (class) component `PendingFrameImage [class]` (`4e412cc1-28bd-572f-bf6c-a91bd5bfc35a`) lines 218-223 [crates/gwiki/src/ingest/video/processing.rs:218-223]
  - Signature: `pub(crate) struct PendingFrameImage {`
  - Purpose: 'PendingFrameImage' is a crate-private struct that packages a frame stored in a temporary file together with its numeric and string timestamps and an optional description. [crates/gwiki/src/ingest/video/processing.rs:218-223]
- `describe_frame_images` (function) component `describe_frame_images [function]` (`e87fb9d9-8b4d-59b8-87b7-589e77628835`) lines 225-333 [crates/gwiki/src/ingest/video/processing.rs:225-333]
  - Signature: `pub(crate) fn describe_frame_images(`
  - Purpose: Iterates over video frame temp files, converts each timestamp to a capped seconds-based label, optionally sends each JPEG to a vision endpoint for description extraction, logs and skips read/extraction failures or blank responses, and returns a 'DescribedFrameImages' collection. [crates/gwiki/src/ingest/video/processing.rs:225-333]
- `cleanup_kept_temp_frames` (function) component `cleanup_kept_temp_frames [function]` (`8c7b0327-80cc-5b3a-ac12-1ce0464a5efa`) lines 335-339 [crates/gwiki/src/ingest/video/processing.rs:335-339]
  - Signature: `pub(crate) fn cleanup_kept_temp_frames(paths: &[PathBuf]) {`
  - Purpose: Attempts to delete each file path in the provided slice with 'std::fs::remove_file', ignoring any deletion errors. [crates/gwiki/src/ingest/video/processing.rs:335-339]

