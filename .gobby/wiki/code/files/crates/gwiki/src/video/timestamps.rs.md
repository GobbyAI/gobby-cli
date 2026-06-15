---
title: crates/gwiki/src/video/timestamps.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/timestamps.rs
  ranges:
  - 3-6
  - 8-23
  - 25-32
  - 34-39
  - 41-47
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video/timestamps.rs

Module: [[code/modules/crates/gwiki/src/video|crates/gwiki/src/video]]

## Purpose

This file provides timestamp utilities for video transcription data. It converts a transcript segment’s millisecond start time into clamped whole seconds, parses colon-separated timestamp strings in `SS`, `MM:SS`, or `HH:MM:SS` form by accepting trimmed integer parts and ignoring fractional suffixes, formats second counts back into zero-padded `HH:MM:SS`, and serializes transcription ranges as comma-separated `start_ms-end_ms` pairs. The parser and formatter functions work together to move between human-readable timestamps and the numeric time values used elsewhere in the video code.
[crates/gwiki/src/video/timestamps.rs:3-6]
[crates/gwiki/src/video/timestamps.rs:8-23]
[crates/gwiki/src/video/timestamps.rs:25-32]
[crates/gwiki/src/video/timestamps.rs:34-39]
[crates/gwiki/src/video/timestamps.rs:41-47]

## API Symbols

- `transcript_start_seconds` (function) component `transcript_start_seconds [function]` (`6a783710-46ae-5509-bb2d-b289c602287c`) lines 3-6 [crates/gwiki/src/video/timestamps.rs:3-6]
  - Signature: `pub(super) fn transcript_start_seconds(segment: &TranscriptSegment) -> u32 {`
  - Purpose: Returns the segment’s start time in whole seconds by dividing 'start_ms' by 1,000 and clamping the result to 'u32::MAX' before casting to 'u32'. [crates/gwiki/src/video/timestamps.rs:3-6]
- `parse_timestamp_seconds` (function) component `parse_timestamp_seconds [function]` (`bf62ccaa-7515-594a-87cf-42439c2d93bb`) lines 8-23 [crates/gwiki/src/video/timestamps.rs:8-23]
  - Signature: `pub(super) fn parse_timestamp_seconds(value: &str) -> Option<u32> {`
  - Purpose: Parses a colon-separated timestamp string into total seconds as 'u32', accepting 'SS', 'MM:SS', or 'HH:MM:SS' formats and returning 'None' on invalid parts, arity, or arithmetic overflow. [crates/gwiki/src/video/timestamps.rs:8-23]
- `parse_timestamp_part` (function) component `parse_timestamp_part [function]` (`9e8faf50-0062-51bc-a7e7-0c10a59423d1`) lines 25-32 [crates/gwiki/src/video/timestamps.rs:25-32]
  - Signature: `fn parse_timestamp_part(value: &str) -> Option<u32> {`
  - Purpose: Parses the string as an unsigned 32-bit integer timestamp component by discarding any fractional part after the first '.' and trimming whitespace, returning 'None' on parse failure. [crates/gwiki/src/video/timestamps.rs:25-32]
- `format_timestamp` (function) component `format_timestamp [function]` (`bff9ee35-e9a8-56c5-91f8-eb806eaba451`) lines 34-39 [crates/gwiki/src/video/timestamps.rs:34-39]
  - Signature: `pub(super) fn format_timestamp(seconds: u32) -> String {`
  - Purpose: Converts a 'u32' duration in seconds into a zero-padded 'HH:MM:SS' string by deriving hours, minutes, and remaining seconds. [crates/gwiki/src/video/timestamps.rs:34-39]
- `format_ranges_ms` (function) component `format_ranges_ms [function]` (`452654ed-932d-5da0-9733-3b216c21dd9f`) lines 41-47 [crates/gwiki/src/video/timestamps.rs:41-47]
  - Signature: `pub(super) fn format_ranges_ms(ranges: &[TranscriptionRange]) -> String {`
  - Purpose: Returns a comma-separated string of 'start_ms-end_ms' pairs for each 'TranscriptionRange' in 'ranges'. [crates/gwiki/src/video/timestamps.rs:41-47]

