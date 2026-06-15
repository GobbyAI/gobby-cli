---
title: crates/gwiki/src/video/types.rs
type: code_file
provenance:
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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video/types.rs

Module: [[code/modules/crates/gwiki/src/video|crates/gwiki/src/video]]

## Purpose

Defines the core data types used by the video-to-markdown pipeline. It models how frames are sampled (`FrameSamplingPlan`, `VideoFrameSample`), annotated (`VideoFrameDescription`), and aligned with transcript text (`AlignedVideoSegment`), along with source references, media metadata, and degradation reporting. The borrowed `VideoMarkdownRequest` gathers all inputs needed to generate markdown from a video, and `VideoMarkdownResult` վերադարձs the output path plus the ordered aligned segments produced from those inputs.
[crates/gwiki/src/video/types.rs:6-9]
[crates/gwiki/src/video/types.rs:12-17]
[crates/gwiki/src/video/types.rs:20-24]
[crates/gwiki/src/video/types.rs:27-31]
[crates/gwiki/src/video/types.rs:34-37]

## API Symbols

- `FrameSamplingPlan` (class) component `FrameSamplingPlan [class]` (`d3ccb48c-5fdf-561e-8b4b-4083a831d59b`) lines 6-9 [crates/gwiki/src/video/types.rs:6-9]
  - Signature: `pub struct FrameSamplingPlan {`
  - Purpose: 'FrameSamplingPlan' is a configuration struct that specifies an optional total sampling duration in seconds and a required frame sampling interval in seconds. [crates/gwiki/src/video/types.rs:6-9]
- `VideoFrameSample` (class) component `VideoFrameSample [class]` (`86956c5f-ad2c-532a-a5ab-6dde564425f8`) lines 12-17 [crates/gwiki/src/video/types.rs:12-17]
  - Signature: `pub struct VideoFrameSample {`
  - Purpose: 'VideoFrameSample' is a Rust struct representing a sampled video frame with a numeric timestamp in seconds, a string timestamp, and the originating asset path plus a source reference identifier. [crates/gwiki/src/video/types.rs:12-17]
- `VideoFrameDescription` (class) component `VideoFrameDescription [class]` (`cb00a920-6569-542b-bd6e-2679411bf30a`) lines 20-24 [crates/gwiki/src/video/types.rs:20-24]
  - Signature: `pub struct VideoFrameDescription {`
  - Purpose: 'VideoFrameDescription' is a struct that groups a video frame’s 'timestamp', 'source_reference', and textual 'description' as 'String' fields. [crates/gwiki/src/video/types.rs:20-24]
- `AlignedVideoSegment` (class) component `AlignedVideoSegment [class]` (`19b2f3b8-524d-59c2-a879-9088072b35e3`) lines 27-31 [crates/gwiki/src/video/types.rs:27-31]
  - Signature: `pub struct AlignedVideoSegment {`
  - Purpose: 'AlignedVideoSegment' is a data structure representing a time-stamped video segment that groups a 'timestamp' string with associated 'VideoFrameDescription' items and 'TranscriptSegment' items. [crates/gwiki/src/video/types.rs:27-31]
- `VideoAudioReference` (class) component `VideoAudioReference [class]` (`b0f3c0fe-c88d-517c-b003-cfb6479f83d7`) lines 34-37 [crates/gwiki/src/video/types.rs:34-37]
  - Signature: `pub struct VideoAudioReference {`
  - Purpose: 'VideoAudioReference' is a Rust struct that pairs a video/audio source file path ('source_asset: PathBuf') with an associated reference identifier or label ('source_reference: String'). [crates/gwiki/src/video/types.rs:34-37]
- `VideoMarkdownResult` (class) component `VideoMarkdownResult [class]` (`ae9bb369-5991-5ff4-bbce-64480d5e0a72`) lines 40-43 [crates/gwiki/src/video/types.rs:40-43]
  - Signature: `pub struct VideoMarkdownResult {`
  - Purpose: 'VideoMarkdownResult' is a result container that stores the output markdown file path as a 'PathBuf' and the ordered collection of aligned video segments as 'Vec<AlignedVideoSegment>'. [crates/gwiki/src/video/types.rs:40-43]
- `VideoMediaMetadata` (class) component `VideoMediaMetadata [class]` (`72a7dc30-b5d4-5f49-abd7-d2eb5a5e8dec`) lines 46-49 [crates/gwiki/src/video/types.rs:46-49]
  - Signature: `pub struct VideoMediaMetadata {`
  - Purpose: 'VideoMediaMetadata' is a struct that stores a video file’s size in bytes and an optional duration in seconds. [crates/gwiki/src/video/types.rs:46-49]
- `VideoMediaDegradation` (class) component `VideoMediaDegradation [class]` (`1fae5c29-e587-59de-b5e9-5ab0b5bed290`) lines 52-56 [crates/gwiki/src/video/types.rs:52-56]
  - Signature: `pub struct VideoMediaDegradation {`
  - Purpose: 'VideoMediaDegradation' is a struct that records a video media degradation event using three string fields: 'kind' for the degradation type, 'reason' for the cause, and 'message' for a descriptive explanation. [crates/gwiki/src/video/types.rs:52-56]
- `VideoMarkdownRequest` (class) component `VideoMarkdownRequest [class]` (`22446b6f-de7f-5b4b-867e-00bcf324acc4`) lines 58-73 [crates/gwiki/src/video/types.rs:58-73]
  - Signature: `pub struct VideoMarkdownRequest<'a> {`
  - Purpose: 'VideoMarkdownRequest<'a>' is a borrowed request struct that packages a video’s identity, paths, media metadata and degradations, frame-sampling configuration and artifacts, and optional transcription data needed to generate Markdown from the video. [crates/gwiki/src/video/types.rs:58-73]

