---
title: crates/gwiki/src/video.rs
type: code_file
provenance:
- file: crates/gwiki/src/video.rs
  ranges:
  - 18-21
  - 24-29
  - 32-36
  - 39-43
  - 46-49
  - 52-55
  - 58-61
  - 64-68
  - 70-94
  - 96-103
  - 105-163
  - 165-168
  - 170-178
  - 180-195
  - 197-222
  - 224-280
  - 282-292
  - 294-313
  - 315-326
  - 328-586
  - 588-603
  - 605-612
  - 614-619
  - 621-627
  - 636-663
  - 666-676
  - 679-714
  - 717-752
  - 755-848
  - 851-893
  - 895-911
  - 913-927
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/video.rs` exposes 32 indexed API symbols.
[crates/gwiki/src/video.rs:18-21]
[crates/gwiki/src/video.rs:24-29]
[crates/gwiki/src/video.rs:32-36]
[crates/gwiki/src/video.rs:39-43]
[crates/gwiki/src/video.rs:46-49]

## API Symbols

- `FrameSamplingPlan` (class) component `FrameSamplingPlan [class]` (`d0f2d47c-2e6f-5706-b30c-ac596664547f`) lines 18-21 [crates/gwiki/src/video.rs:18-21]
  - Signature: `pub struct FrameSamplingPlan {`
  - Purpose: `FrameSamplingPlan` is a configuration struct that specifies periodic frame sampling with a required `interval_seconds` and optional `duration_seconds` duration limit. [crates/gwiki/src/video.rs:18-21]
- `VideoFrameSample` (class) component `VideoFrameSample [class]` (`2a88a901-9d79-5811-b8a6-6c3e87baed44`) lines 24-29 [crates/gwiki/src/video.rs:24-29]
  - Signature: `pub struct VideoFrameSample {`
  - Purpose: `VideoFrameSample` is a public struct that stores metadata for a sampled video frame, including dual-format timestamps (numeric seconds and string representation), a source asset file path, and a source reference identifier. [crates/gwiki/src/video.rs:24-29]
- `VideoFrameDescription` (class) component `VideoFrameDescription [class]` (`149a6fb8-3ffb-59bd-bbb0-2d51344f70fd`) lines 32-36 [crates/gwiki/src/video.rs:32-36]
  - Signature: `pub struct VideoFrameDescription {`
  - Purpose: `VideoFrameDescription` is a public struct that encapsulates textual metadata for a video frame, comprising a timestamp, source reference, and descriptive string. [crates/gwiki/src/video.rs:32-36]
- `AlignedVideoSegment` (class) component `AlignedVideoSegment [class]` (`1b16f91c-f47f-5cd2-9bff-7949fa2728e9`) lines 39-43 [crates/gwiki/src/video.rs:39-43]
  - Signature: `pub struct AlignedVideoSegment {`
  - Purpose: `AlignedVideoSegment` is a struct that pairs a timestamp with vectors of video frame descriptions and transcript segments to synchronize visual and textual video content at a specific point in time. [crates/gwiki/src/video.rs:39-43]
- `VideoAudioReference` (class) component `VideoAudioReference [class]` (`0efa446c-3614-5459-932c-f9b00ec6c809`) lines 46-49 [crates/gwiki/src/video.rs:46-49]
  - Signature: `pub struct VideoAudioReference {`
  - Purpose: VideoAudioReference is a struct that associates a source media asset's filesystem path with a string reference identifier. [crates/gwiki/src/video.rs:46-49]
- `VideoMarkdownResult` (class) component `VideoMarkdownResult [class]` (`4f92ff6a-8d3c-5f09-9eeb-f138e4286704`) lines 52-55 [crates/gwiki/src/video.rs:52-55]
  - Signature: `pub struct VideoMarkdownResult {`
  - Purpose: `VideoMarkdownResult` is a struct that pairs a file path with a vector of temporally-aligned video segments produced by markdown-based video processing. [crates/gwiki/src/video.rs:52-55]
- `VideoMediaMetadata` (class) component `VideoMediaMetadata [class]` (`cf9f500a-4c93-534e-b363-7ee467d2f0bd`) lines 58-61 [crates/gwiki/src/video.rs:58-61]
  - Signature: `pub struct VideoMediaMetadata {`
  - Purpose: `VideoMediaMetadata` is a public struct that holds video file metadata comprising a required file size in bytes (`u64`) and an optional duration in seconds (`Option<u32>`). [crates/gwiki/src/video.rs:58-61]
- `VideoMediaDegradation` (class) component `VideoMediaDegradation [class]` (`c40ae7e0-1054-5cca-8b7f-6a0c2749e59b`) lines 64-68 [crates/gwiki/src/video.rs:64-68]
  - Signature: `pub struct VideoMediaDegradation {`
  - Purpose: `VideoMediaDegradation` is a public struct that encapsulates video media degradation information through three String fields: `kind` (the type of degradation), `reason` (the cause), and `message` (a descriptive explanation). [crates/gwiki/src/video.rs:64-68]
- `sample_frames` (function) component `sample_frames [function]` (`eeda002c-4818-5091-8a0a-5d594d14ed3d`) lines 70-94 [crates/gwiki/src/video.rs:70-94]
  - Signature: `pub fn sample_frames(asset_path: &Path, plan: FrameSamplingPlan) -> Vec<VideoFrameSample> {`
  - Purpose: Extracts video frame samples from an asset at uniform time intervals specified by a FrameSamplingPlan, sampling from 0 seconds up to the duration_seconds in interval_seconds increments. [crates/gwiki/src/video.rs:70-94]
- `audio_reference_for_video` (function) component `audio_reference_for_video [function]` (`c9090ac8-7375-5727-9da6-b4c3a029e231`) lines 96-103 [crates/gwiki/src/video.rs:96-103]
  - Signature: `pub fn audio_reference_for_video(asset_path: &Path) -> VideoAudioReference {`
  - Purpose: Constructs a `VideoAudioReference` containing the asset path as a `PathBuf` and a formatted reference string with the `#audio` fragment identifier appended. [crates/gwiki/src/video.rs:96-103]
- `align_transcript_and_frames` (function) component `align_transcript_and_frames [function]` (`d9d9324e-7d2a-58da-aab3-043f02a67dcb`) lines 105-163 [crates/gwiki/src/video.rs:105-163]
  - Signature: `pub fn align_transcript_and_frames(`
  - Purpose: # Function Summary

**`align_transcript_and_frames` aligns transcript segments to video frame timestamps by associating each transcript segment with the nearest preceding frame timestamp, returning time-sorted combined segments.** [crates/gwiki/src/video.rs:105-163]
- `transcript_start_seconds` (function) component `transcript_start_seconds [function]` (`b081830f-1b4e-57ac-8972-4cb069a76990`) lines 165-168 [crates/gwiki/src/video.rs:165-168]
  - Signature: `fn transcript_start_seconds(segment: &TranscriptSegment) -> u32 {`
  - Purpose: Converts a `TranscriptSegment`'s start time from milliseconds to seconds, clamped to `u32::MAX` to prevent overflow. [crates/gwiki/src/video.rs:165-168]
- `timestamp_seconds_or_zero` (function) component `timestamp_seconds_or_zero [function]` (`4258d3fc-bf86-555b-80e6-20d340157adb`) lines 170-178 [crates/gwiki/src/video.rs:170-178]
  - Signature: `fn timestamp_seconds_or_zero(value: &str, label: &str) -> u32 {`
  - Purpose: Parses a timestamp string into seconds, returning the parsed value or zero with a debug log if parsing fails. [crates/gwiki/src/video.rs:170-178]
- `VideoMarkdownRequest` (class) component `VideoMarkdownRequest [class]` (`afe4dc74-f6fd-5fe6-8be2-fa2723794124`) lines 180-195 [crates/gwiki/src/video.rs:180-195]
  - Signature: `pub struct VideoMarkdownRequest<'a> {`
  - Purpose: `VideoMarkdownRequest<'a>` is a lifetime-parameterized struct that aggregates video file metadata, processed frame samples with descriptions, and transcription data required for converting video content to markdown format. [crates/gwiki/src/video.rs:180-195]
- `write_video_derived_markdown` (function) component `write_video_derived_markdown [function]` (`8c81b61f-d00f-5108-bede-57a48beaf518`) lines 197-222 [crates/gwiki/src/video.rs:197-222]
  - Signature: `pub fn write_video_derived_markdown(`
  - Purpose: Aligns transcript segments with frame descriptions, generates and atomically writes video-derived markdown to the vault directory structure, and returns the relative file path and aligned segments. [crates/gwiki/src/video.rs:197-222]
- `write_video_markdown_atomic` (function) component `write_video_markdown_atomic [function]` (`a391ee85-e936-5ecc-a4fb-19d42cd8f17a`) lines 224-280 [crates/gwiki/src/video.rs:224-280]
  - Signature: `fn write_video_markdown_atomic(path: &Path, bytes: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Atomically writes a byte buffer to a file using the write-to-temporary-then-rename pattern, with automatic overwrite of existing files and explicit fsync operations for durability. [crates/gwiki/src/video.rs:224-280]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`0180c287-f318-541e-b5b8-418691f8fd8c`) lines 282-292 [crates/gwiki/src/video.rs:282-292]
  - Signature: `fn temp_sibling_path(path: &Path) -> PathBuf {`
  - Purpose: Generates a uniquely-named temporary sibling file path using the pattern `.{filename}.{pid}.{nanos}.tmp`, where the temporary file resides in the same directory as the original path. [crates/gwiki/src/video.rs:282-292]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`dd9b2a2c-6eb5-5e8a-a3ae-5d9926dd73b5`) lines 294-313 [crates/gwiki/src/video.rs:294-313]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Syncs the parent directory to persistent storage on Unix systems (no-op on other platforms), returning a `WikiError` on IO failure. [crates/gwiki/src/video.rs:294-313]
- `frame_sample` (function) component `frame_sample [function]` (`06daa396-97fe-5de7-b5ab-3b11625878ba`) lines 315-326 [crates/gwiki/src/video.rs:315-326]
  - Signature: `fn frame_sample(asset_path: &Path, timestamp_seconds: u32) -> VideoFrameSample {`
  - Purpose: Constructs a `VideoFrameSample` by formatting a timestamp value and generating a time-indexed media fragment URI reference from an asset path. [crates/gwiki/src/video.rs:315-326]
- `render_video_derived_markdown` (function) component `render_video_derived_markdown [function]` (`cd796e9c-3b86-53c4-aec1-cd8170bab155`) lines 328-586 [crates/gwiki/src/video.rs:328-586]
  - Signature: `fn render_video_derived_markdown(`
  - Purpose: Generates a markdown string representation of a video source by aggregating metadata fields including source location, content hash, asset paths, frame sampling parameters, transcript segments, and audio references into a structured metadata collection. [crates/gwiki/src/video.rs:328-586]
- `parse_timestamp_seconds` (function) component `parse_timestamp_seconds [function]` (`e3b939d9-f8ab-5a0a-87d5-4ea5a3f75a47`) lines 588-603 [crates/gwiki/src/video.rs:588-603]
  - Signature: `fn parse_timestamp_seconds(value: &str) -> Option<u32> {`
  - Purpose: Parses a colon-separated timestamp string in S, M:S, or H:M:S format and converts it to total seconds as a u32, with checked arithmetic preventing overflow. [crates/gwiki/src/video.rs:588-603]
- `parse_timestamp_part` (function) component `parse_timestamp_part [function]` (`a67cdb5e-18e6-5bd6-b266-9f8aabdf7610`) lines 605-612 [crates/gwiki/src/video.rs:605-612]
  - Signature: `fn parse_timestamp_part(value: &str) -> Option<u32> {`
  - Purpose: Parses a string as u32, removing any fractional seconds after the first decimal point, returning None if parsing fails. [crates/gwiki/src/video.rs:605-612]
- `format_timestamp` (function) component `format_timestamp [function]` (`2552f9f8-f7cc-585e-873a-bb503d319586`) lines 614-619 [crates/gwiki/src/video.rs:614-619]
  - Signature: `fn format_timestamp(seconds: u32) -> String {`
  - Purpose: Converts a duration given in total seconds (u32) into a zero-padded HH:MM:SS timestamp string. [crates/gwiki/src/video.rs:614-619]
- `format_ranges_ms` (function) component `format_ranges_ms [function]` (`52f0a97b-37c9-5901-b698-5ae69562936a`) lines 621-627 [crates/gwiki/src/video.rs:621-627]
  - Signature: `fn format_ranges_ms(ranges: &[TranscriptionRange]) -> String {`
  - Purpose: Converts a slice of `TranscriptionRange` objects into a comma-separated string where each range is formatted as "start_ms-end_ms". [crates/gwiki/src/video.rs:621-627]
- `frame_sampling_records_timestamps` (function) component `frame_sampling_records_timestamps [function]` (`75ebc35c-75f3-53bd-bc81-1ae1d08fe05c`) lines 636-663 [crates/gwiki/src/video.rs:636-663]
  - Signature: `fn frame_sampling_records_timestamps() {`
  - Purpose: Unit test validating that frame sampling produces correct temporal timestamps and media fragment URI references when sampling a video at regular intervals. [crates/gwiki/src/video.rs:636-663]
- `zero_frame_interval_disables_sampling` (function) component `zero_frame_interval_disables_sampling [function]` (`7abf4a0e-d83a-528f-a254-875884fa9f46`) lines 666-676 [crates/gwiki/src/video.rs:666-676]
  - Signature: `fn zero_frame_interval_disables_sampling() {`
  - Purpose: This test asserts that `sample_frames()` returns an empty collection when `FrameSamplingPlan` specifies an `interval_seconds` of zero. [crates/gwiki/src/video.rs:666-676]
- `aligns_transcript_and_frames` (function) component `aligns_transcript_and_frames [function]` (`a8b58fbb-0d2a-5497-af95-79876ab0c14a`) lines 679-714 [crates/gwiki/src/video.rs:679-714]
  - Signature: `fn aligns_transcript_and_frames() {`
  - Purpose: Unit test that verifies the `align_transcript_and_frames` function correctly correlates `VideoFrameDescription` and `TranscriptSegment` objects by temporal alignment, producing synchronized pairs at matching timestamps. [crates/gwiki/src/video.rs:679-714]
- `aligns_on_numeric_start_ms` (function) component `aligns_on_numeric_start_ms [function]` (`475e3973-e502-5d1a-901b-3277d8968ac8`) lines 717-752 [crates/gwiki/src/video.rs:717-752]
  - Signature: `fn aligns_on_numeric_start_ms() {`
  - Purpose: Unit test verifying that `align_transcript_and_frames` correctly pairs transcript segments (specified in milliseconds) with video frame descriptions (specified in MM:SS:MS format) at temporally matching boundaries. [crates/gwiki/src/video.rs:717-752]
- `partial_failure_matrix` (function) component `partial_failure_matrix [function]` (`988cb5b4-bc54-56d2-9fb6-c3b9025411f8`) lines 755-848 [crates/gwiki/src/video.rs:755-848]
  - Signature: `fn partial_failure_matrix() {`
  - Purpose: Tests video-derived markdown generation when frame extraction fails but transcript segments and frame descriptions remain available as fallbacks. [crates/gwiki/src/video.rs:755-848]
- `degradation_metadata_has_size_and_duration` (function) component `degradation_metadata_has_size_and_duration [function]` (`ede4372c-ac09-50a3-a1a9-1b7d64e1484a`) lines 851-893 [crates/gwiki/src/video.rs:851-893]
  - Signature: `fn degradation_metadata_has_size_and_duration() {`
  - Purpose: Tests that `write_video_derived_markdown` correctly includes video metadata (file size and duration) and media degradation information in the generated markdown document when ffmpeg is unavailable. [crates/gwiki/src/video.rs:851-893]
- `record_for` (function) component `record_for [function]` (`0dda79d0-958f-5b1c-8335-84fe6077d802`) lines 895-911 [crates/gwiki/src/video.rs:895-911]
  - Signature: `fn record_for(temp: &Path) -> SourceRecord {`
  - Purpose: Registers a video source draft with hardcoded lecture.mp4 metadata to SourceManifest and returns the resulting SourceRecord, panicking on registration failure. [crates/gwiki/src/video.rs:895-911]
- `transcription_output` (function) component `transcription_output [function]` (`7b6d8ccc-859e-5ce1-ad48-fe5e2a3e4811`) lines 913-927 [crates/gwiki/src/video.rs:913-927]
  - Signature: `fn transcription_output(segments: &[TranscriptSegment]) -> TranscriptionOutput {`
  - Purpose: Constructs a `TranscriptionOutput` struct from the provided transcript segments with hardcoded English language metadata and empty completion/missing ranges. [crates/gwiki/src/video.rs:913-927]

