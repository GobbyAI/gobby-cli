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

# crates/gwiki/src/video/alignment.rs

Module: [[code/modules/crates/gwiki/src/video|crates/gwiki/src/video]]

## Purpose

Aligns transcript segments with video frame descriptions into ordered `AlignedVideoSegment`s. It groups frames by parsed timestamp in a `BTreeMap`, then attaches each transcript segment to the latest frame timestamp at or before its start time, or to the first frame when needed; if there are no frames, it instead groups transcript segments by their own start times. The helper `timestamp_seconds_or_zero` parses frame timestamps for that grouping and logs a debug fallback to `0` when parsing fails.
[crates/gwiki/src/video/alignment.rs:8-66]
[crates/gwiki/src/video/alignment.rs:68-76]

## API Symbols

- `align_transcript_and_frames` (function) component `align_transcript_and_frames [function]` (`c7e4e34c-ab3c-5038-b99c-c87129530f46`) lines 8-66 [crates/gwiki/src/video/alignment.rs:8-66]
  - Signature: `pub fn align_transcript_and_frames(`
  - Purpose: Groups video frames by timestamp into ordered 'AlignedVideoSegment's and attaches each transcript segment to the latest frame timestamp at or before its start time, falling back to the first frame timestamp or, if no frames exist, grouping transcript segments by their own start times. [crates/gwiki/src/video/alignment.rs:8-66]
- `timestamp_seconds_or_zero` (function) component `timestamp_seconds_or_zero [function]` (`a0e2ac4b-9490-5618-a6d6-4637bc99547c`) lines 68-76 [crates/gwiki/src/video/alignment.rs:68-76]
  - Signature: `fn timestamp_seconds_or_zero(value: &str, label: &str) -> u32 {`
  - Purpose: Parses 'value' as a timestamp in seconds and returns the parsed 'u32', or logs a debug message with 'label' and 'value' and returns '0' if parsing fails. [crates/gwiki/src/video/alignment.rs:68-76]

