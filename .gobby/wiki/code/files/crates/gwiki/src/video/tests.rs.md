---
title: crates/gwiki/src/video/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/tests.rs
  ranges:
  - 12-39
  - 42-52
  - 55-90
  - 93-128
  - 131-224
  - 227-269
  - 271-287
  - 289-303
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video/tests.rs

Module: [[code/modules/crates/gwiki/src/video|crates/gwiki/src/video]]

## Purpose

This file contains tests and test helpers for the video-processing pipeline in `gwiki`. It verifies that frame sampling emits the expected timestamps and source references, that transcript segments are aligned to frame descriptions by time, and that video-derived markdown preserves available modalities while recording degradation metadata when extraction or transcription fails. The helper constructors at the end build a fixed `SourceRecord` and a fake `TranscriptionOutput` so the tests can exercise those behaviors with controlled video and transcript data.
[crates/gwiki/src/video/tests.rs:12-39]
[crates/gwiki/src/video/tests.rs:42-52]
[crates/gwiki/src/video/tests.rs:55-90]
[crates/gwiki/src/video/tests.rs:93-128]
[crates/gwiki/src/video/tests.rs:131-224]

## API Symbols

- `frame_sampling_records_timestamps` (function) component `frame_sampling_records_timestamps [function]` (`769ded0d-c741-55d4-90d5-76aa79cee96b`) lines 12-39 [crates/gwiki/src/video/tests.rs:12-39]
  - Signature: `fn frame_sampling_records_timestamps() {`
  - Purpose: Verifies that 'sample_frames' records timestamps at 3-second intervals over a 7-second duration, preserves the source asset path for every sample, and formats each sample’s 'source_reference' with a '#t=' timestamp fragment. [crates/gwiki/src/video/tests.rs:12-39]
- `zero_frame_interval_disables_sampling` (function) component `zero_frame_interval_disables_sampling [function]` (`c9cb4807-f063-51ef-89ab-e8ec3ff6d653`) lines 42-52 [crates/gwiki/src/video/tests.rs:42-52]
  - Signature: `fn zero_frame_interval_disables_sampling() {`
  - Purpose: Verifies that 'sample_frames' returns no frames when 'interval_seconds' is set to '0' in the 'FrameSamplingPlan', even with a finite duration. [crates/gwiki/src/video/tests.rs:42-52]
- `aligns_transcript_and_frames` (function) component `aligns_transcript_and_frames [function]` (`d32901ed-1285-5ba8-8591-15195b8c86cd`) lines 55-90 [crates/gwiki/src/video/tests.rs:55-90]
  - Signature: `fn aligns_transcript_and_frames() {`
  - Purpose: It builds time-aligned records by matching each 'TranscriptSegment' to the corresponding 'VideoFrameDescription' timestamp and returning a sequence of aligned entries containing the shared timestamp plus the associated frame and transcript data. [crates/gwiki/src/video/tests.rs:55-90]
- `aligns_on_numeric_start_ms` (function) component `aligns_on_numeric_start_ms [function]` (`136f56f0-2bf3-5059-bbd9-ebf2a7b60798`) lines 93-128 [crates/gwiki/src/video/tests.rs:93-128]
  - Signature: `fn aligns_on_numeric_start_ms() {`
  - Purpose: Verifies that 'align_transcript_and_frames' correctly aligns transcript segments to frame descriptions by matching the nearest numeric start timestamps, producing two aligned groups at '00:00:00' and '00:00:05' with the expected segment and frame associations. [crates/gwiki/src/video/tests.rs:93-128]
- `partial_failure_matrix` (function) component `partial_failure_matrix [function]` (`aede4e76-4c9d-5c7c-95ec-498ce45db5f9`) lines 131-224 [crates/gwiki/src/video/tests.rs:131-224]
  - Signature: `fn partial_failure_matrix() {`
  - Purpose: Verifies that 'write_video_derived_markdown' preserves whichever video-derived modality succeeds and records the appropriate degradation metadata when either frame extraction or transcription fails. [crates/gwiki/src/video/tests.rs:131-224]
- `degradation_metadata_has_size_and_duration` (function) component `degradation_metadata_has_size_and_duration [function]` (`ab37aabd-60ce-567f-88f3-d8751ff3489e`) lines 227-269 [crates/gwiki/src/video/tests.rs:227-269]
  - Signature: `fn degradation_metadata_has_size_and_duration() {`
  - Purpose: Verifies that 'write_video_derived_markdown' emits a document containing video duration, file size, media duration, and the expected media degradation metadata/message for a degraded video asset. [crates/gwiki/src/video/tests.rs:227-269]
- `record_for` (function) component `record_for [function]` (`f3de798d-c73f-5e8c-9d01-d6012f9bfc3e`) lines 271-287 [crates/gwiki/src/video/tests.rs:271-287]
  - Signature: `fn record_for(temp: &Path) -> SourceRecord {`
  - Purpose: Registers a video 'SourceDraft' for '/tmp/lecture.mp4' with hardcoded metadata and content, then returns the resulting 'SourceRecord', panicking if registration fails. [crates/gwiki/src/video/tests.rs:271-287]
- `transcription_output` (function) component `transcription_output [function]` (`d2654acd-d611-5d33-8ce2-0b290487ca2c`) lines 289-303 [crates/gwiki/src/video/tests.rs:289-303]
  - Signature: `fn transcription_output(segments: &[TranscriptSegment]) -> TranscriptionOutput {`
  - Purpose: Constructs a 'TranscriptionOutput' by cloning the input 'TranscriptSegment' slice into 'segments' and populating fixed metadata for English transcription with '"fake-stt"', while marking the result as non-translated, non-partial, and with no completed or missing ranges. [crates/gwiki/src/video/tests.rs:289-303]

