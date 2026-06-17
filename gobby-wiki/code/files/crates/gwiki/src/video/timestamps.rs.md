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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/video/timestamps.rs:3-6](crates/gwiki/src/video/timestamps.rs#L3-L6), [crates/gwiki/src/video/timestamps.rs:8-23](crates/gwiki/src/video/timestamps.rs#L8-L23), [crates/gwiki/src/video/timestamps.rs:25-32](crates/gwiki/src/video/timestamps.rs#L25-L32), [crates/gwiki/src/video/timestamps.rs:34-39](crates/gwiki/src/video/timestamps.rs#L34-L39), [crates/gwiki/src/video/timestamps.rs:41-47](crates/gwiki/src/video/timestamps.rs#L41-L47)

</details>

# crates/gwiki/src/video/timestamps.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Utilities for converting between video transcript timestamps and displayable time strings. `transcript_start_seconds` derives a segment’s start time in whole seconds from millisecond input, `parse_timestamp_seconds` and the helper `parse_timestamp_part` accept `SS`, `MM:SS`, or `HH:MM:SS` text and safely turn it into seconds with overflow checks, `format_timestamp` renders seconds as `HH:MM:SS`, and `format_ranges_ms` serializes transcription ranges as comma-separated `start_ms-end_ms` pairs.
[crates/gwiki/src/video/timestamps.rs:3-6]
[crates/gwiki/src/video/timestamps.rs:8-23]
[crates/gwiki/src/video/timestamps.rs:25-32]
[crates/gwiki/src/video/timestamps.rs:34-39]
[crates/gwiki/src/video/timestamps.rs:41-47]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `transcript_start_seconds` | function | `pub(super) fn transcript_start_seconds(segment: &TranscriptSegment) -> u32 {` | `transcript_start_seconds [function]` | `6a783710-46ae-5509-bb2d-b289c602287c` | 3-6 [crates/gwiki/src/video/timestamps.rs:3-6] | Indexed function `transcript_start_seconds` in `crates/gwiki/src/video/timestamps.rs`. [crates/gwiki/src/video/timestamps.rs:3-6] |
| `parse_timestamp_seconds` | function | `pub(super) fn parse_timestamp_seconds(value: &str) -> Option<u32> {` | `parse_timestamp_seconds [function]` | `bf62ccaa-7515-594a-87cf-42439c2d93bb` | 8-23 [crates/gwiki/src/video/timestamps.rs:8-23] | Indexed function `parse_timestamp_seconds` in `crates/gwiki/src/video/timestamps.rs`. [crates/gwiki/src/video/timestamps.rs:8-23] |
| `parse_timestamp_part` | function | `fn parse_timestamp_part(value: &str) -> Option<u32> {` | `parse_timestamp_part [function]` | `9e8faf50-0062-51bc-a7e7-0c10a59423d1` | 25-32 [crates/gwiki/src/video/timestamps.rs:25-32] | Indexed function `parse_timestamp_part` in `crates/gwiki/src/video/timestamps.rs`. [crates/gwiki/src/video/timestamps.rs:25-32] |
| `format_timestamp` | function | `pub(super) fn format_timestamp(seconds: u32) -> String {` | `format_timestamp [function]` | `bff9ee35-e9a8-56c5-91f8-eb806eaba451` | 34-39 [crates/gwiki/src/video/timestamps.rs:34-39] | Indexed function `format_timestamp` in `crates/gwiki/src/video/timestamps.rs`. [crates/gwiki/src/video/timestamps.rs:34-39] |
| `format_ranges_ms` | function | `pub(super) fn format_ranges_ms(ranges: &[TranscriptionRange]) -> String {` | `format_ranges_ms [function]` | `452654ed-932d-5da0-9733-3b216c21dd9f` | 41-47 [crates/gwiki/src/video/timestamps.rs:41-47] | Indexed function `format_ranges_ms` in `crates/gwiki/src/video/timestamps.rs`. [crates/gwiki/src/video/timestamps.rs:41-47] |
