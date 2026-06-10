---
title: crates/gwiki/src/ingest/video/processing.rs
type: code_file
provenance:
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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/processing.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

`crates/gwiki/src/ingest/video/processing.rs` exposes 14 indexed API symbols.
[crates/gwiki/src/ingest/video/processing.rs:19-27]
[crates/gwiki/src/ingest/video/processing.rs:29]
[crates/gwiki/src/ingest/video/processing.rs:31-43]
[crates/gwiki/src/ingest/video/processing.rs:32-34]
[crates/gwiki/src/ingest/video/processing.rs:36-42]
[crates/gwiki/src/ingest/video/processing.rs:45-64]
[crates/gwiki/src/ingest/video/processing.rs:66-179]
[crates/gwiki/src/ingest/video/processing.rs:181-197]
[crates/gwiki/src/ingest/video/processing.rs:199-209]
[crates/gwiki/src/ingest/video/processing.rs:212-216]
[crates/gwiki/src/ingest/video/processing.rs:218-223]
[crates/gwiki/src/ingest/video/processing.rs:225-329]
[crates/gwiki/src/ingest/video/processing.rs:331-335]
[crates/gwiki/src/ingest/video/processing.rs:337-346]

## API Symbols

- `VideoMediaExtractor` (type) component `VideoMediaExtractor [type]` (`1e146573-9caf-54df-bde3-29dc65f89ef0`) lines 19-27 [crates/gwiki/src/ingest/video/processing.rs:19-27]
  - Signature: `pub(crate) trait VideoMediaExtractor {`
  - Purpose: Indexed type `VideoMediaExtractor` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:19-27]
- `ProductionVideoMediaExtractor` (class) component `ProductionVideoMediaExtractor [class]` (`1eb6254e-6880-53bb-85cc-7c4fad4c027b`) lines 29-29 [crates/gwiki/src/ingest/video/processing.rs:29]
  - Signature: `pub(crate) struct ProductionVideoMediaExtractor;`
  - Purpose: `ProductionVideoMediaExtractor` is a crate-private, zero-sized unit struct that serves as a stateless extractor for production video media. [crates/gwiki/src/ingest/video/processing.rs:29]
- `ProductionVideoMediaExtractor` (class) component `ProductionVideoMediaExtractor [class]` (`aa4e5ece-e989-5cf2-8588-90ff29913d28`) lines 31-43 [crates/gwiki/src/ingest/video/processing.rs:31-43]
  - Signature: `impl VideoMediaExtractor for ProductionVideoMediaExtractor {`
  - Purpose: ProductionVideoMediaExtractor is a trait implementation that delegates audio extraction and frame image sampling from video files to underlying media utility functions. [crates/gwiki/src/ingest/video/processing.rs:31-43]
- `ProductionVideoMediaExtractor.extract_audio` (method) component `ProductionVideoMediaExtractor.extract_audio [method]` (`bf8a078a-8d39-5807-953b-efef9318eba4`) lines 32-34 [crates/gwiki/src/ingest/video/processing.rs:32-34]
  - Signature: `fn extract_audio(&self, video: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Delegates audio extraction from a video file to the media module, returning either a temporary file containing the extracted audio or a `WikiError`. [crates/gwiki/src/ingest/video/processing.rs:32-34]
- `ProductionVideoMediaExtractor.sample_frame_images` (method) component `ProductionVideoMediaExtractor.sample_frame_images [method]` (`ba46913c-27c4-5ba6-8b10-a41a88f447fb`) lines 36-42 [crates/gwiki/src/ingest/video/processing.rs:36-42]
  - Signature: `fn sample_frame_images(`
  - Purpose: Wrapper method that delegates to the media module to sample frames from a video file at the specified interval, returning a vector of frame indices paired with temporary image files. [crates/gwiki/src/ingest/video/processing.rs:36-42]
- `ingest_video_file_with_processing` (function) component `ingest_video_file_with_processing [function]` (`49640cb4-d1e6-50ac-be41-b0b703a8d66e`) lines 45-64 [crates/gwiki/src/ingest/video/processing.rs:45-64]
  - Signature: `pub(crate) fn ingest_video_file_with_processing(`
  - Purpose: Ingests a video file by processing it with transcription and vision endpoints, then indexes the result in the wiki store. [crates/gwiki/src/ingest/video/processing.rs:45-64]
- `ingest_video_file_with_processing_without_index` (function) component `ingest_video_file_with_processing_without_index [function]` (`f93bceec-197e-5356-9fca-063082335497`) lines 66-179 [crates/gwiki/src/ingest/video/processing.rs:66-179]
  - Signature: `pub(crate) fn ingest_video_file_with_processing_without_index(`
  - Purpose: Ingests a video file by extracting and transcribing its audio content, gracefully handling cases where transcription endpoints are unavailable or fail by capturing degradation states. [crates/gwiki/src/ingest/video/processing.rs:66-179]
- `video_media_degradation` (function) component `video_media_degradation [function]` (`3b3378c5-f3ac-5c93-a480-85348f94f8a8`) lines 181-197 [crates/gwiki/src/ingest/video/processing.rs:181-197]
  - Signature: `pub(crate) fn video_media_degradation(`
  - Purpose: Converts a `WikiError` into a `VideoMediaDegradation` struct, setting the reason to "ffmpeg_unavailable" if the error indicates ffmpeg unavailability, otherwise using the provided fallback reason. [crates/gwiki/src/ingest/video/processing.rs:181-197]
- `message_is_ffmpeg_unavailable` (function) component `message_is_ffmpeg_unavailable [function]` (`2d55b0d0-332d-5041-9eea-c36fc7e1304f`) lines 199-209 [crates/gwiki/src/ingest/video/processing.rs:199-209]
  - Signature: `fn message_is_ffmpeg_unavailable(message: &str) -> bool {`
  - Purpose: Checks if a message contains any of several ffmpeg unavailability error indicators using case-insensitive substring matching. [crates/gwiki/src/ingest/video/processing.rs:199-209]
- `DescribedFrameImages` (class) component `DescribedFrameImages [class]` (`6599d8b6-68b7-50cd-84ae-046dd4e3ed5c`) lines 212-216 [crates/gwiki/src/ingest/video/processing.rs:212-216]
  - Signature: `pub(crate) struct DescribedFrameImages {`
  - Purpose: `DescribedFrameImages` is a crate-private struct that aggregates three parallel vectors containing video frame samples, their corresponding file paths, and textual descriptions. [crates/gwiki/src/ingest/video/processing.rs:212-216]
- `PendingFrameImage` (class) component `PendingFrameImage [class]` (`ed0c7b5a-9b6d-588d-ae66-3a030e0a15c3`) lines 218-223 [crates/gwiki/src/ingest/video/processing.rs:218-223]
  - Signature: `pub(crate) struct PendingFrameImage {`
  - Purpose: `PendingFrameImage` is a crate-private struct that encapsulates a temporary frame file with dual-format timestamp fields (u32 seconds and String representation) and an optional description. [crates/gwiki/src/ingest/video/processing.rs:218-223]
- `describe_frame_images` (function) component `describe_frame_images [function]` (`427a3ebd-198d-5509-a7f8-0abaf4d4a319`) lines 225-329 [crates/gwiki/src/ingest/video/processing.rs:225-329]
  - Signature: `pub(crate) fn describe_frame_images(`
  - Purpose: Extracts vision API descriptions for sampled video frames by reading each from disk and invoking the vision client on the frame bytes, returning descriptions paired with formatted timestamps. [crates/gwiki/src/ingest/video/processing.rs:225-329]
- `cleanup_kept_temp_frames` (function) component `cleanup_kept_temp_frames [function]` (`84e42e3a-b0bf-5ae2-9354-0815178cd1f2`) lines 331-335 [crates/gwiki/src/ingest/video/processing.rs:331-335]
  - Signature: `pub(crate) fn cleanup_kept_temp_frames(paths: &[PathBuf]) {`
  - Purpose: This crate-internal function removes temporary frame files from the filesystem, iterating through the provided paths slice and silently discarding any deletion errors. [crates/gwiki/src/ingest/video/processing.rs:331-335]
- `vision_degradation` (function) component `vision_degradation [function]` (`627958e7-df90-555d-a36a-fc08fbf14048`) lines 337-346 [crates/gwiki/src/ingest/video/processing.rs:337-346]
  - Signature: `pub(crate) fn vision_degradation(routing: AiRouting) -> VisionDegradation {`
  - Purpose: # Summary

Converts an `AiRouting` configuration into a `VisionDegradation` struct, assigning a reason of "disabled" (if routing is `Off`) or "missing_endpoint" (otherwise), with a fixed fallback directive to skip frame vision. [crates/gwiki/src/ingest/video/processing.rs:337-346]

