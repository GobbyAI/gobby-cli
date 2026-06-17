---
title: crates/gwiki/src/video
type: code_module
provenance:
- file: crates/gwiki/src/video/alignment.rs
  ranges:
  - 8-66
  - 68-76
- file: crates/gwiki/src/video/markdown.rs
  ranges:
  - 15-40
  - 42-300
- file: crates/gwiki/src/video/sampling.rs
  ranges:
  - 8-32
  - 34-41
  - 43-54
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
- file: crates/gwiki/src/video/timestamps.rs
  ranges:
  - 3-6
  - 8-23
  - 25-32
  - 34-39
  - 41-47
- file: crates/gwiki/src/video/types.rs
  ranges:
  - 6-9
  - 12-17
  - 20-24
  - 27-31
  - 34-37
  - 40-43
  - 46-49
  - 52-56
  - 58-73
- file: crates/gwiki/src/video/write.rs
  ranges:
  - 9-65
  - 67-77
  - 79-98
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/video/alignment.rs:8-66](crates/gwiki/src/video/alignment.rs#L8-L66), [crates/gwiki/src/video/alignment.rs:68-76](crates/gwiki/src/video/alignment.rs#L68-L76)
- [crates/gwiki/src/video/markdown.rs:15-40](crates/gwiki/src/video/markdown.rs#L15-L40), [crates/gwiki/src/video/markdown.rs:42-300](crates/gwiki/src/video/markdown.rs#L42-L300)
- [crates/gwiki/src/video/sampling.rs:8-32](crates/gwiki/src/video/sampling.rs#L8-L32), [crates/gwiki/src/video/sampling.rs:34-41](crates/gwiki/src/video/sampling.rs#L34-L41), [crates/gwiki/src/video/sampling.rs:43-54](crates/gwiki/src/video/sampling.rs#L43-L54)
- [crates/gwiki/src/video/tests.rs:12-39](crates/gwiki/src/video/tests.rs#L12-L39), [crates/gwiki/src/video/tests.rs:42-52](crates/gwiki/src/video/tests.rs#L42-L52), [crates/gwiki/src/video/tests.rs:55-90](crates/gwiki/src/video/tests.rs#L55-L90), [crates/gwiki/src/video/tests.rs:93-128](crates/gwiki/src/video/tests.rs#L93-L128), [crates/gwiki/src/video/tests.rs:131-224](crates/gwiki/src/video/tests.rs#L131-L224), [crates/gwiki/src/video/tests.rs:227-269](crates/gwiki/src/video/tests.rs#L227-L269), [crates/gwiki/src/video/tests.rs:271-287](crates/gwiki/src/video/tests.rs#L271-L287), [crates/gwiki/src/video/tests.rs:289-303](crates/gwiki/src/video/tests.rs#L289-L303)
- [crates/gwiki/src/video/timestamps.rs:3-6](crates/gwiki/src/video/timestamps.rs#L3-L6), [crates/gwiki/src/video/timestamps.rs:8-23](crates/gwiki/src/video/timestamps.rs#L8-L23), [crates/gwiki/src/video/timestamps.rs:25-32](crates/gwiki/src/video/timestamps.rs#L25-L32), [crates/gwiki/src/video/timestamps.rs:34-39](crates/gwiki/src/video/timestamps.rs#L34-L39), [crates/gwiki/src/video/timestamps.rs:41-47](crates/gwiki/src/video/timestamps.rs#L41-L47)
- [crates/gwiki/src/video/types.rs:6-9](crates/gwiki/src/video/types.rs#L6-L9), [crates/gwiki/src/video/types.rs:12-17](crates/gwiki/src/video/types.rs#L12-L17), [crates/gwiki/src/video/types.rs:20-24](crates/gwiki/src/video/types.rs#L20-L24), [crates/gwiki/src/video/types.rs:27-31](crates/gwiki/src/video/types.rs#L27-L31), [crates/gwiki/src/video/types.rs:34-37](crates/gwiki/src/video/types.rs#L34-L37), [crates/gwiki/src/video/types.rs:40-43](crates/gwiki/src/video/types.rs#L40-L43), [crates/gwiki/src/video/types.rs:46-49](crates/gwiki/src/video/types.rs#L46-L49), [crates/gwiki/src/video/types.rs:52-56](crates/gwiki/src/video/types.rs#L52-L56), [crates/gwiki/src/video/types.rs:58-73](crates/gwiki/src/video/types.rs#L58-L73)
- [crates/gwiki/src/video/write.rs:9-65](crates/gwiki/src/video/write.rs#L9-L65), [crates/gwiki/src/video/write.rs:67-77](crates/gwiki/src/video/write.rs#L67-L77), [crates/gwiki/src/video/write.rs:79-98](crates/gwiki/src/video/write.rs#L79-L98)

</details>

# crates/gwiki/src/video

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

The `video` module in `gwiki` is responsible for processing video sources and their accompanying transcripts to generate structured, derived markdown documentation within a vault. It establishes the core data models for representing frame sampling configurations, frame-by-frame metadata, transcript alignment segments, and degradation logs . Key functionalities include generating periodic video frame samples and corresponding audio reference assets [crates/gwiki/src/video/sampling.rs:8-32, 34-41], converting between milliseconds, seconds, and displayable `HH:MM:SS` timestamp strings [crates/gwiki/src/video/timestamps.rs:3-6, 8-23, 25-32], and aligning video frame descriptions with transcript segments under shared or nearest-prior timestamps [crates/gwiki/src/video/alignment.rs:8-66].

The main pipeline flow begins with a `VideoMarkdownRequest` bundle that packages all input assets, metadata, transcriptions, and frame descriptions . The function `write_video_derived_markdown` drives the pipeline: it invokes `align_transcript_and_frames` to synchronize transcript segments with frame descriptions, renders the cohesive document using `render_video_derived_markdown`, and writes the final markdown atomically to the target vault path [crates/gwiki/src/video/markdown.rs:15-40, 42-300]. Atomic write safety is maintained by writing to a temporary sibling file, executing `fsync` on the bytes, and performing a durable rename operation [crates/gwiki/src/video/write.rs:9-65].

### Public API Symbols and Core Models

| Symbol | Kind | Description | Source |
| --- | --- | --- | --- |
| FrameSamplingPlan | struct | Configuration specifying video duration and frame sampling interval. | [crates/gwiki/src/video/types.rs:6-9] |
| VideoFrameSample | struct | Details of a sampled frame including timestamp representation and source paths. | [crates/gwiki/src/video/types.rs:12-17] |
| VideoFrameDescription | struct | Textual description of a video frame mapped to a specific timestamp. | [crates/gwiki/src/video/types.rs:20-24] |
| AlignedVideoSegment | struct | High-level segment pairing a timestamp with matching frame descriptions and transcripts. | [crates/gwiki/src/video/types.rs:27-31] |
| VideoAudioReference | struct | Identifies the companion audio asset extracted from or linked to a video source. | [crates/gwiki/src/video/types.rs:34-37] |
| VideoMarkdownResult | struct | The output path and list of aligned segments resulting from markdown compilation. | [crates/gwiki/src/video/types.rs:40-43] |
| VideoMediaMetadata | struct | Core video file metadata such as size in bytes and optional duration in seconds. | [crates/gwiki/src/video/types.rs:46-49] |
| VideoMediaDegradation | struct | Records quality degradations, containing kind, reason, and descriptive messages. | [crates/gwiki/src/video/types.rs:52-56] |
| VideoMarkdownRequest | struct | Complete parameter bundle requested to compile and write video derived markdown. |  |
| sample_frames | fn | Produces periodic frame samples from an asset path and a sampling plan. | [crates/gwiki/src/video/sampling.rs:8-32] |
| audio_reference_for_video | fn | Generates a standard display-path reference appending `#audio` for the video asset. | [crates/gwiki/src/video/sampling.rs:34-41] |
| align_transcript_and_frames | fn | Builds aligned video segments by grouping frame descriptions and transcript segments. | [crates/gwiki/src/video/alignment.rs:8-66] |
| write_video_derived_markdown | fn | Drives the alignment, markdown rendering, and atomic file-writing process. | [crates/gwiki/src/video/markdown.rs:15-40] |
| render_video_derived_markdown | fn | Assembles and renders the final markdown document text from video metadata and segments. | [crates/gwiki/src/video/markdown.rs:42-300] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/video/alignment.rs\|crates/gwiki/src/video/alignment.rs]] | Builds aligned video segments by grouping frame descriptions and transcript segments under shared timestamps. `align_transcript_and_frames` first indexes frames by parsed timestamp, falls back to transcript-start timestamps when there are no frames, and otherwise assigns each transcript segment to the latest frame timestamp at or before its start; `timestamp_seconds_or_zero` safely converts a timestamp string to seconds, defaulting to `0` for video frames when parsing fails. [crates/gwiki/src/video/alignment.rs:8-66] [crates/gwiki/src/video/alignment.rs:68-76] |
| [[code/files/crates/gwiki/src/video/markdown.rs\|crates/gwiki/src/video/markdown.rs]] | This file generates derived markdown for a video source. `write_video_derived_markdown` aligns transcript segments with frame descriptions, resolves the derived output path under the vault, creates parent directories if needed, renders the markdown, writes it atomically, and returns the output path plus the aligned segments. `render_video_derived_markdown` assembles the actual markdown text by combining scope, source record, request data, audio/video references, metadata fields, timestamps, and aligned segment content into a single document. [crates/gwiki/src/video/markdown.rs:15-40] [crates/gwiki/src/video/markdown.rs:42-300] |
| [[code/files/crates/gwiki/src/video/sampling.rs\|crates/gwiki/src/video/sampling.rs]] | Builds video sampling references from an asset path and a sampling plan. `sample_frames` emits frame samples at a fixed interval, handling edge cases for zero interval and unknown duration by returning no samples or a single frame at `t=0`; it delegates per-frame construction to `frame_sample`. `frame_sample` formats the timestamp and creates the source asset/reference metadata for each sampled frame. `audio_reference_for_video` produces the matching audio reference by reusing the asset path and appending `#audio` to the display path. [crates/gwiki/src/video/sampling.rs:8-32] [crates/gwiki/src/video/sampling.rs:34-41] [crates/gwiki/src/video/sampling.rs:43-54] |
| [[code/files/crates/gwiki/src/video/tests.rs\|crates/gwiki/src/video/tests.rs]] | This file contains unit tests for the video processing pipeline in `gwiki`. It verifies that frame sampling produces the expected timestamps and source references, that a zero interval disables sampling, that transcript segments are aligned to frame descriptions both by timestamp and numeric `start_ms`, and that partial-failure/degradation handling preserves metadata like size and duration. The `record_for` and `transcription_output` helpers build reusable source records and transcription outputs so the tests can exercise these behaviors consistently. [crates/gwiki/src/video/tests.rs:12-39] [crates/gwiki/src/video/tests.rs:42-52] [crates/gwiki/src/video/tests.rs:55-90] [crates/gwiki/src/video/tests.rs:93-128] [crates/gwiki/src/video/tests.rs:131-224] |
| [[code/files/crates/gwiki/src/video/timestamps.rs\|crates/gwiki/src/video/timestamps.rs]] | Utilities for converting between video transcript timestamps and displayable time strings. `transcript_start_seconds` derives a segment’s start time in whole seconds from millisecond input, `parse_timestamp_seconds` and the helper `parse_timestamp_part` accept `SS`, `MM:SS`, or `HH:MM:SS` text and safely turn it into seconds with overflow checks, `format_timestamp` renders seconds as `HH:MM:SS`, and `format_ranges_ms` serializes transcription ranges as comma-separated `start_ms-end_ms` pairs. [crates/gwiki/src/video/timestamps.rs:3-6] [crates/gwiki/src/video/timestamps.rs:8-23] [crates/gwiki/src/video/timestamps.rs:25-32] [crates/gwiki/src/video/timestamps.rs:34-39] [crates/gwiki/src/video/timestamps.rs:41-47] |
| [[code/files/crates/gwiki/src/video/types.rs\|crates/gwiki/src/video/types.rs]] | Defines the data model used by the video-to-markdown pipeline. It covers frame sampling and per-frame metadata, alignment of frame descriptions with transcript segments, references back to source video/audio assets, media metadata and degradation reporting, and the `VideoMarkdownRequest` bundle that passes all inputs needed to generate a `VideoMarkdownResult`. [crates/gwiki/src/video/types.rs:6-9] [crates/gwiki/src/video/types.rs:12-17] [crates/gwiki/src/video/types.rs:20-24] [crates/gwiki/src/video/types.rs:27-31] [crates/gwiki/src/video/types.rs:34-37] |
| [[code/files/crates/gwiki/src/video/write.rs\|crates/gwiki/src/video/write.rs]] | Provides an atomic write path for video-derived markdown files: it creates a temporary sibling file, writes and fsyncs the bytes, then renames it into place so the target is replaced safely. The helper functions choose a temporary filename next to the destination and sync the parent directory afterward to make the rename durable, with special handling for existing targets and cleanup on failure. [crates/gwiki/src/video/write.rs:9-65] [crates/gwiki/src/video/write.rs:67-77] [crates/gwiki/src/video/write.rs:79-98] |

## Components

| Component ID |
| --- |
| `c7e4e34c-ab3c-5038-b99c-c87129530f46` |
| `a0e2ac4b-9490-5618-a6d6-4637bc99547c` |
| `5872cc23-1676-599d-b273-32a4f1b149ba` |
| `4150cec7-1348-5e19-864c-054dfe51b997` |
| `a4cff237-0f26-5236-b79a-a2c68949c40f` |
| `ddeba91d-f1f9-5b9b-a1a9-62a80b0766a0` |
| `6797d9d6-ffdd-5ca6-9955-2c5029dfe431` |
| `769ded0d-c741-55d4-90d5-76aa79cee96b` |
| `c9cb4807-f063-51ef-89ab-e8ec3ff6d653` |
| `d32901ed-1285-5ba8-8591-15195b8c86cd` |
| `136f56f0-2bf3-5059-bbd9-ebf2a7b60798` |
| `aede4e76-4c9d-5c7c-95ec-498ce45db5f9` |
| `ab37aabd-60ce-567f-88f3-d8751ff3489e` |
| `f3de798d-c73f-5e8c-9d01-d6012f9bfc3e` |
| `d2654acd-d611-5d33-8ce2-0b290487ca2c` |
| `6a783710-46ae-5509-bb2d-b289c602287c` |
| `bf62ccaa-7515-594a-87cf-42439c2d93bb` |
| `9e8faf50-0062-51bc-a7e7-0c10a59423d1` |
| `bff9ee35-e9a8-56c5-91f8-eb806eaba451` |
| `452654ed-932d-5da0-9733-3b216c21dd9f` |
| `d3ccb48c-5fdf-561e-8b4b-4083a831d59b` |
| `86956c5f-ad2c-532a-a5ab-6dde564425f8` |
| `cb00a920-6569-542b-bd6e-2679411bf30a` |
| `19b2f3b8-524d-59c2-a879-9088072b35e3` |
| `b0f3c0fe-c88d-517c-b003-cfb6479f83d7` |
| `ae9bb369-5991-5ff4-bbce-64480d5e0a72` |
| `72a7dc30-b5d4-5f49-abd7-d2eb5a5e8dec` |
| `1fae5c29-e587-59de-b5e9-5ab0b5bed290` |
| `22446b6f-de7f-5b4b-867e-00bcf324acc4` |
| `eeefc41f-ce3c-5f36-8395-c52b9dce3854` |
| `82f22277-4b79-50ad-bddd-1aa65100561f` |
| `20d24412-1afe-5535-952f-2b26a5764613` |
