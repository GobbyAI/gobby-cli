---
title: crates/gwiki/src/video/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video/types.rs

Module: [[code/modules/crates/gwiki/src/video|crates/gwiki/src/video]]

## Overview

`crates/gwiki/src/video/types.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/video/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FrameSamplingPlan` | class | 'FrameSamplingPlan' is a struct that specifies frame sampling parameters with a required sampling interval in seconds and an optional maximum sampling duration in seconds. [crates/gwiki/src/video/types.rs:6-9] |
| `VideoFrameSample` | class | 'VideoFrameSample' is a struct that encapsulates a video frame's temporal metadata (as both a numeric u32 seconds and String timestamp representation), source asset file path, and a reference identifier string. [crates/gwiki/src/video/types.rs:12-17] |
| `VideoFrameDescription` | class | 'VideoFrameDescription' is a public struct that encapsulates video frame metadata with three String fields: timestamp, source_reference, and description. [crates/gwiki/src/video/types.rs:20-24] |
| `AlignedVideoSegment` | class | 'AlignedVideoSegment' is a struct that groups a timestamp with corresponding vectors of 'VideoFrameDescription' and 'TranscriptSegment' objects, representing temporally synchronized video and transcript data for a single segment. [crates/gwiki/src/video/types.rs:27-31] |
| `VideoAudioReference` | class | 'VideoAudioReference' is a public struct that pairs a file path ('PathBuf') with a string identifier to reference multimedia assets. [crates/gwiki/src/video/types.rs:34-37] |
| `VideoMarkdownResult` | class | VideoMarkdownResult is a struct that contains a filesystem path and a vector of aligned video segments. [crates/gwiki/src/video/types.rs:40-43] |
| `VideoMediaMetadata` | class | 'VideoMediaMetadata' is a Rust struct that encapsulates video file metadata comprising a required file size in bytes ('u64') and an optional duration in seconds ('Option<u32>'). [crates/gwiki/src/video/types.rs:46-49] |
| `VideoMediaDegradation` | class | # Summary 'VideoMediaDegradation' is a public struct with three String fields ('kind', 'reason', 'message') that encapsulates metadata describing video media degradation or playback issues. [crates/gwiki/src/video/types.rs:52-56] |
| `VideoMarkdownRequest` | class | 'VideoMarkdownRequest<'a>' is a lifetime-parameterized struct that aggregates borrowed references and slices of video metadata, frame samples with descriptions, and transcription segments for markdown generation. [crates/gwiki/src/video/types.rs:58-73] |

