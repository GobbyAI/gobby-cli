---
title: crates/gwiki/src/video
type: code_module
provenance:
- file: crates/gwiki/src/video/alignment.rs
- file: crates/gwiki/src/video/markdown.rs
- file: crates/gwiki/src/video/sampling.rs
- file: crates/gwiki/src/video/tests.rs
- file: crates/gwiki/src/video/timestamps.rs
- file: crates/gwiki/src/video/types.rs
- file: crates/gwiki/src/video/write.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

## crates/gwiki/src/video

The `video` module is responsible for the full pipeline that converts a raw video asset into a structured Markdown document. It covers four distinct concerns: computing a frame-sampling schedule from a video's duration and a configurable interval, aligning the resulting frame descriptions against a speech transcript, assembling the aligned data into a `VideoMarkdownResult`, and serialising that result to disk. The module imports transcript primitives — `TranscriptSegment`, `TranscriptionDegradation`, and `TranscriptionOutput` — from `crate::transcribe` (types.rs:3), and uses `crate::support::text::display_path` for portable path rendering inside source-reference strings (sampling.rs:3).

The frame-sampling flow starts in `sampling.rs`. `sample_frames` consumes a `FrameSamplingPlan` and iterates from zero up to `duration_seconds` in steps of `interval_seconds`, emitting a `VideoFrameSample` per step (sampling.rs:8-31). A zero interval short-circuits to an empty list (sampling.rs:9-11), and an unknown duration produces a single sample at t=0 (sampling.rs:14-17). `audio_reference_for_video` constructs a companion `VideoAudioReference` whose `source_reference` carries a `#audio` fragment (sampling.rs:33-40). Raw timestamp arithmetic — parsing `HH:MM:SS` strings and formatting integer seconds back to that form — lives entirely in `timestamps.rs`, with `parse_timestamp_seconds` handling one-, two-, and three-part colon-delimited inputs (timestamps.rs:8-22) and `format_timestamp` zero-padding each component (timestamps.rs:33-38).

Alignment is performed in `alignment.rs` via `align_transcript_and_frames`, which joins `VideoFrameDescription` objects with `TranscriptSegment` objects into `AlignedVideoSegment` values grouped by video timestamp. The tests in `tests.rs` verify that a 7-second video sampled every 3 seconds yields timestamps `00:00:00`, `00:00:03`, and `00:00:06` (tests.rs:20-28), that a zero interval produces no samples (tests.rs:40-50), and that transcript segments correctly merge with the nearest preceding frame (tests.rs:52-end). Markdown rendering (`markdown.rs`) accepts a `VideoMarkdownRequest` — a rich borrow-heavy struct carrying metadata, degradation notices, frame images, descriptions, and transcript data (types.rs:55-74) — and returns a `VideoMarkdownResult`. The `write.rs` file then persists that result under the resolved output path.

### Public API symbols

| Symbol | Kind | File | Description |
|---|---|---|---|
| `FrameSamplingPlan` | struct | types.rs:5 | Holds `duration_seconds` and `interval_seconds` to drive frame extraction |
| `VideoFrameSample` | struct | types.rs:11 | One sampled frame: numeric and string timestamp, source asset path and URI reference |
| `VideoFrameDescription` | struct | types.rs:18 | Pairs a frame timestamp and source reference with a free-text visual description |
| `AlignedVideoSegment` | struct | types.rs:25 | Groups frame descriptions and transcript segments under a shared timestamp |
| `VideoAudioReference` | struct | types.rs:32 | Asset path and `#audio` fragment reference for the video's audio track |
| `VideoMarkdownResult` | struct | types.rs:37 | Output path paired with the full list of aligned segments |
| `VideoMediaMetadata` | struct | types.rs:42 | File size and optional duration for the source asset |
| `VideoMediaDegradation` | struct | types.rs:48 | Structured quality-warning record (`kind`, `reason`, `message`) |
| `VideoMarkdownRequest<'a>` | struct | types.rs:55 | Borrow-aggregating input to the Markdown renderer; carries all frame, transcript, and metadata references |
| `sample_frames` | fn | sampling.rs:8 | Computes `Vec<VideoFrameSample>` from an asset path and a `FrameSamplingPlan` |
| `audio_reference_for_video` | fn | sampling.rs:33 | Builds a `VideoAudioReference` for a given asset path |

### Timestamp helpers (internal)

| Function | Signature | Notes |
|---|---|---|
| `format_timestamp` | `(u32) -> String` | Formats seconds as `HH:MM:SS` (timestamps.rs:33) |
| `parse_timestamp_seconds` | `(&str) -> Option<u32>` | Parses 1-, 2-, or 3-part colon-delimited timestamps (timestamps.rs:8) |
| `transcript_start_seconds` | `(&TranscriptSegment) -> u32` | Converts `start_ms` to saturating seconds (timestamps.rs:4) |
| `format_ranges_ms` | `(&[TranscriptionRange]) -> String` | Serialises ranges as `start-end` pairs joined by commas (timestamps.rs:40) |
[crates/gwiki/src/video/alignment.rs:8-66]
[crates/gwiki/src/video/markdown.rs:15-40]
[crates/gwiki/src/video/sampling.rs:8-32]
[crates/gwiki/src/video/tests.rs:12-39]
[crates/gwiki/src/video/timestamps.rs:3-6]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/video/alignment.rs\|crates/gwiki/src/video/alignment.rs]] | `crates/gwiki/src/video/alignment.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/markdown.rs\|crates/gwiki/src/video/markdown.rs]] | `crates/gwiki/src/video/markdown.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/sampling.rs\|crates/gwiki/src/video/sampling.rs]] | `crates/gwiki/src/video/sampling.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/tests.rs\|crates/gwiki/src/video/tests.rs]] | `crates/gwiki/src/video/tests.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/timestamps.rs\|crates/gwiki/src/video/timestamps.rs]] | `crates/gwiki/src/video/timestamps.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/types.rs\|crates/gwiki/src/video/types.rs]] | `crates/gwiki/src/video/types.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/video/write.rs\|crates/gwiki/src/video/write.rs]] | `crates/gwiki/src/video/write.rs` exposes 3 indexed API symbols. |

