---
title: crates/gwiki/src/video/alignment.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/alignment.rs
  ranges:
  - 8-66
  - 68-76
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/video/alignment.rs:8-66](crates/gwiki/src/video/alignment.rs#L8-L66), [crates/gwiki/src/video/alignment.rs:68-76](crates/gwiki/src/video/alignment.rs#L68-L76)

</details>

# crates/gwiki/src/video/alignment.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds aligned video segments by grouping frame descriptions and transcript segments under shared timestamps. `align_transcript_and_frames` first indexes frames by parsed timestamp, falls back to transcript-start timestamps when there are no frames, and otherwise assigns each transcript segment to the latest frame timestamp at or before its start; `timestamp_seconds_or_zero` safely converts a timestamp string to seconds, defaulting to `0` for video frames when parsing fails.
[crates/gwiki/src/video/alignment.rs:8-66]
[crates/gwiki/src/video/alignment.rs:68-76]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `align_transcript_and_frames` | function | `pub fn align_transcript_and_frames(` | `align_transcript_and_frames [function]` | `c7e4e34c-ab3c-5038-b99c-c87129530f46` | 8-66 [crates/gwiki/src/video/alignment.rs:8-66] | Indexed function `align_transcript_and_frames` in `crates/gwiki/src/video/alignment.rs`. [crates/gwiki/src/video/alignment.rs:8-66] |
| `timestamp_seconds_or_zero` | function | `fn timestamp_seconds_or_zero(value: &str, label: &str) -> u32 {` | `timestamp_seconds_or_zero [function]` | `a0e2ac4b-9490-5618-a6d6-4637bc99547c` | 68-76 [crates/gwiki/src/video/alignment.rs:68-76] | Indexed function `timestamp_seconds_or_zero` in `crates/gwiki/src/video/alignment.rs`. [crates/gwiki/src/video/alignment.rs:68-76] |
