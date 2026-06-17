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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/video/tests.rs:12-39](crates/gwiki/src/video/tests.rs#L12-L39), [crates/gwiki/src/video/tests.rs:42-52](crates/gwiki/src/video/tests.rs#L42-L52), [crates/gwiki/src/video/tests.rs:55-90](crates/gwiki/src/video/tests.rs#L55-L90), [crates/gwiki/src/video/tests.rs:93-128](crates/gwiki/src/video/tests.rs#L93-L128), [crates/gwiki/src/video/tests.rs:131-224](crates/gwiki/src/video/tests.rs#L131-L224), [crates/gwiki/src/video/tests.rs:227-269](crates/gwiki/src/video/tests.rs#L227-L269), [crates/gwiki/src/video/tests.rs:271-287](crates/gwiki/src/video/tests.rs#L271-L287), [crates/gwiki/src/video/tests.rs:289-303](crates/gwiki/src/video/tests.rs#L289-L303)

</details>

# crates/gwiki/src/video/tests.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file contains unit tests for the video processing pipeline in `gwiki`. It verifies that frame sampling produces the expected timestamps and source references, that a zero interval disables sampling, that transcript segments are aligned to frame descriptions both by timestamp and numeric `start_ms`, and that partial-failure/degradation handling preserves metadata like size and duration. The `record_for` and `transcription_output` helpers build reusable source records and transcription outputs so the tests can exercise these behaviors consistently.
[crates/gwiki/src/video/tests.rs:12-39]
[crates/gwiki/src/video/tests.rs:42-52]
[crates/gwiki/src/video/tests.rs:55-90]
[crates/gwiki/src/video/tests.rs:93-128]
[crates/gwiki/src/video/tests.rs:131-224]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `frame_sampling_records_timestamps` | function | `fn frame_sampling_records_timestamps() {` | `frame_sampling_records_timestamps [function]` | `769ded0d-c741-55d4-90d5-76aa79cee96b` | 12-39 [crates/gwiki/src/video/tests.rs:12-39] | Indexed function `frame_sampling_records_timestamps` in `crates/gwiki/src/video/tests.rs`. [crates/gwiki/src/video/tests.rs:12-39] |
| `zero_frame_interval_disables_sampling` | function | `fn zero_frame_interval_disables_sampling() {` | `zero_frame_interval_disables_sampling [function]` | `c9cb4807-f063-51ef-89ab-e8ec3ff6d653` | 42-52 [crates/gwiki/src/video/tests.rs:42-52] | Indexed function `zero_frame_interval_disables_sampling` in `crates/gwiki/src/video/tests.rs`. [crates/gwiki/src/video/tests.rs:42-52] |
| `aligns_transcript_and_frames` | function | `fn aligns_transcript_and_frames() {` | `aligns_transcript_and_frames [function]` | `d32901ed-1285-5ba8-8591-15195b8c86cd` | 55-90 [crates/gwiki/src/video/tests.rs:55-90] | Indexed function `aligns_transcript_and_frames` in `crates/gwiki/src/video/tests.rs`. [crates/gwiki/src/video/tests.rs:55-90] |
| `aligns_on_numeric_start_ms` | function | `fn aligns_on_numeric_start_ms() {` | `aligns_on_numeric_start_ms [function]` | `136f56f0-2bf3-5059-bbd9-ebf2a7b60798` | 93-128 [crates/gwiki/src/video/tests.rs:93-128] | Indexed function `aligns_on_numeric_start_ms` in `crates/gwiki/src/video/tests.rs`. [crates/gwiki/src/video/tests.rs:93-128] |
| `partial_failure_matrix` | function | `fn partial_failure_matrix() {` | `partial_failure_matrix [function]` | `aede4e76-4c9d-5c7c-95ec-498ce45db5f9` | 131-224 [crates/gwiki/src/video/tests.rs:131-224] | Indexed function `partial_failure_matrix` in `crates/gwiki/src/video/tests.rs`. [crates/gwiki/src/video/tests.rs:131-224] |
| `degradation_metadata_has_size_and_duration` | function | `fn degradation_metadata_has_size_and_duration() {` | `degradation_metadata_has_size_and_duration [function]` | `ab37aabd-60ce-567f-88f3-d8751ff3489e` | 227-269 [crates/gwiki/src/video/tests.rs:227-269] | Indexed function `degradation_metadata_has_size_and_duration` in `crates/gwiki/src/video/tests.rs`. [crates/gwiki/src/video/tests.rs:227-269] |
| `record_for` | function | `fn record_for(temp: &Path) -> SourceRecord {` | `record_for [function]` | `f3de798d-c73f-5e8c-9d01-d6012f9bfc3e` | 271-287 [crates/gwiki/src/video/tests.rs:271-287] | Indexed function `record_for` in `crates/gwiki/src/video/tests.rs`. [crates/gwiki/src/video/tests.rs:271-287] |
| `transcription_output` | function | `fn transcription_output(segments: &[TranscriptSegment]) -> TranscriptionOutput {` | `transcription_output [function]` | `d2654acd-d611-5d33-8ce2-0b290487ca2c` | 289-303 [crates/gwiki/src/video/tests.rs:289-303] | Indexed function `transcription_output` in `crates/gwiki/src/video/tests.rs`. [crates/gwiki/src/video/tests.rs:289-303] |
