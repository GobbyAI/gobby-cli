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

The `crates/gwiki/src/video` module models and assembles video-derived wiki content: sampled frames, frame descriptions, transcript alignment, audio references, media metadata/degradations, and the final markdown result. Its central request type, `VideoMarkdownRequest`, carries the original asset/raw paths, MIME and duration metadata, degradation records, frame samples/images/descriptions, transcript segments, and optional transcription output into markdown generation (`crates/gwiki/src/video/types.rs:55-74`).

The main sampling flow starts with `sample_frames`, which returns no samples when the interval is zero, samples timestamp `0` when duration is unknown, and otherwise walks from `00:00:00` by the configured interval until it would exceed the duration (`crates/gwiki/src/video/sampling.rs:7-32`). Each sample stores both numeric and formatted timestamps plus a source reference like `path#t=00:00:03`, using shared timestamp formatting and display-path helpers (`crates/gwiki/src/video/sampling.rs:34-55`; `crates/gwiki/src/video/timestamps.rs:32-37`). Tests cover timestamp recording, disabled sampling, and alignment behavior against transcript segments (`crates/gwiki/src/video/tests.rs:10-39`; `crates/gwiki/src/video/tests.rs:41-100`).

The module collaborates with transcription code through imported `TranscriptSegment`, `TranscriptionOutput`, `TranscriptionDegradation`, and `TranscriptionRange` types (`crates/gwiki/src/video/types.rs:3`; `crates/gwiki/src/video/timestamps.rs:1`). It also calls out to `crate::support::text::display_path` when constructing stable media references (`crates/gwiki/src/video/sampling.rs:3`; `crates/gwiki/src/video/sampling.rs:36-53`). Test code shows wider ingestion/source integration by importing `ScopeIdentity` and source manifest/draft/status types alongside video APIs (`crates/gwiki/src/video/tests.rs:4-8`).

| Public symbol | Responsibility |
| --- | --- |
| `FrameSamplingPlan` | Defines optional duration and frame interval for sampling (`crates/gwiki/src/video/types.rs:5-9`). |
| `VideoFrameSample` | Captures sampled frame timestamp, source asset, and source reference (`crates/gwiki/src/video/types.rs:11-17`). |
| `VideoFrameDescription` | Associates a timestamped source reference with generated visual description text (`crates/gwiki/src/video/types.rs:19-24`). |
| `AlignedVideoSegment` | Groups frame descriptions with transcript segments at a timestamp (`crates/gwiki/src/video/types.rs:26-31`). |
| `VideoAudioReference` | Represents the video asset’s audio reference (`crates/gwiki/src/video/types.rs:33-37`). |
| `VideoMarkdownResult` | Returns generated markdown path plus aligned segments (`crates/gwiki/src/video/types.rs:39-43`). |
| `VideoMediaMetadata` | Stores file size and optional duration (`crates/gwiki/src/video/types.rs:45-49`). |
| `VideoMediaDegradation` | Records degradation kind, reason, and message (`crates/gwiki/src/video/types.rs:51-55`). |
| `VideoMarkdownRequest<'a>` | Bundles inputs for video markdown generation (`crates/gwiki/src/video/types.rs:57-74`). |
| `sample_frames` | Produces timestamped frame samples from an asset path and sampling plan (`crates/gwiki/src/video/sampling.rs:7-32`). |
| `audio_reference_for_video` | Produces a `#audio` source reference for the video asset (`crates/gwiki/src/video/sampling.rs:34-42`). |
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

