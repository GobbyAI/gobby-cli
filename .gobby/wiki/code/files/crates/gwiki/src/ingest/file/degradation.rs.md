---
title: crates/gwiki/src/ingest/file/degradation.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/degradation.rs
  ranges:
  - 4-11
  - 13-15
  - 18-22
  - 24-39
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file/degradation.rs

Module: [[code/modules/crates/gwiki/src/ingest/file|crates/gwiki/src/ingest/file]]

## Purpose

Builds compact degradation-summary strings for ingest errors across media types. The helper functions format transcription, vision, and optional document degradations into fixed `type:reason:fallback` strings, and `video_degradation_summaries` collects all video media degradations plus any transcription degradation into a `Vec<String>` for downstream reporting.
[crates/gwiki/src/ingest/file/degradation.rs:4-11]
[crates/gwiki/src/ingest/file/degradation.rs:13-15]
[crates/gwiki/src/ingest/file/degradation.rs:18-22]
[crates/gwiki/src/ingest/file/degradation.rs:24-39]

## API Symbols

- `transcription_degradation_summary` (function) component `transcription_degradation_summary [function]` (`d864d1c9-a5d4-56d1-9044-ef2972a76b3e`) lines 4-11 [crates/gwiki/src/ingest/file/degradation.rs:4-11]
  - Signature: `pub(super) fn transcription_degradation_summary(`
  - Purpose: Returns a 'String' of the form 'audio_transcription:<reason>:<fallback>' by formatting the 'TranscriptionDegradation'’s 'reason' and 'fallback' fields. [crates/gwiki/src/ingest/file/degradation.rs:4-11]
- `vision_degradation_summary` (function) component `vision_degradation_summary [function]` (`387e4be4-1a32-5b50-b2d8-46c532d02e50`) lines 13-15 [crates/gwiki/src/ingest/file/degradation.rs:13-15]
  - Signature: `pub(super) fn vision_degradation_summary(degradation: &VisionDegradation) -> String {`
  - Purpose: Returns a formatted string 'vision:<reason>:<fallback>' using the 'reason' and 'fallback' fields of the provided 'VisionDegradation'. [crates/gwiki/src/ingest/file/degradation.rs:13-15]
- `document_degradation_summary` (function) component `document_degradation_summary [function]` (`01d024dc-1ebe-518e-8db2-97d3d9195193`) lines 18-22 [crates/gwiki/src/ingest/file/degradation.rs:18-22]
  - Signature: `pub(super) fn document_degradation_summary(`
  - Purpose: Formats a degradation summary string as 'document:<reason>:<fallback>' using 'degradation.reason()' and 'degradation.fallback'. [crates/gwiki/src/ingest/file/degradation.rs:18-22]
- `video_degradation_summaries` (function) component `video_degradation_summaries [function]` (`a1fd8178-96ce-546d-ad0b-f19e41840cf8`) lines 24-39 [crates/gwiki/src/ingest/file/degradation.rs:24-39]
  - Signature: `pub(super) fn video_degradation_summaries(result: &VideoIngestResult) -> Vec<String> {`
  - Purpose: Builds a 'Vec<String>' of video ingest degradation summaries by formatting each 'media_degradations' entry as 'video_<kind>:<reason>:<message>' and appending the transcription degradation summary if present. [crates/gwiki/src/ingest/file/degradation.rs:24-39]

