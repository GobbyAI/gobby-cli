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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/video/types.rs:6-9](crates/gwiki/src/video/types.rs#L6-L9), [crates/gwiki/src/video/types.rs:12-17](crates/gwiki/src/video/types.rs#L12-L17), [crates/gwiki/src/video/types.rs:20-24](crates/gwiki/src/video/types.rs#L20-L24), [crates/gwiki/src/video/types.rs:27-31](crates/gwiki/src/video/types.rs#L27-L31), [crates/gwiki/src/video/types.rs:34-37](crates/gwiki/src/video/types.rs#L34-L37), [crates/gwiki/src/video/types.rs:40-43](crates/gwiki/src/video/types.rs#L40-L43), [crates/gwiki/src/video/types.rs:46-49](crates/gwiki/src/video/types.rs#L46-L49), [crates/gwiki/src/video/types.rs:52-56](crates/gwiki/src/video/types.rs#L52-L56), [crates/gwiki/src/video/types.rs:58-73](crates/gwiki/src/video/types.rs#L58-L73)

</details>

# crates/gwiki/src/video/types.rs

Module: [[code/modules/crates/gwiki/src/video|crates/gwiki/src/video]]

## Purpose

Defines the data model used by the video-to-markdown pipeline. It covers frame sampling and per-frame metadata, alignment of frame descriptions with transcript segments, references back to source video/audio assets, media metadata and degradation reporting, and the `VideoMarkdownRequest` bundle that passes all inputs needed to generate a `VideoMarkdownResult`.
[crates/gwiki/src/video/types.rs:6-9]
[crates/gwiki/src/video/types.rs:12-17]
[crates/gwiki/src/video/types.rs:20-24]
[crates/gwiki/src/video/types.rs:27-31]
[crates/gwiki/src/video/types.rs:34-37]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `FrameSamplingPlan` | class | `pub struct FrameSamplingPlan {` | `FrameSamplingPlan [class]` | `d3ccb48c-5fdf-561e-8b4b-4083a831d59b` | 6-9 [crates/gwiki/src/video/types.rs:6-9] | Indexed class `FrameSamplingPlan` in `crates/gwiki/src/video/types.rs`. [crates/gwiki/src/video/types.rs:6-9] |
| `VideoFrameSample` | class | `pub struct VideoFrameSample {` | `VideoFrameSample [class]` | `86956c5f-ad2c-532a-a5ab-6dde564425f8` | 12-17 [crates/gwiki/src/video/types.rs:12-17] | Indexed class `VideoFrameSample` in `crates/gwiki/src/video/types.rs`. [crates/gwiki/src/video/types.rs:12-17] |
| `VideoFrameDescription` | class | `pub struct VideoFrameDescription {` | `VideoFrameDescription [class]` | `cb00a920-6569-542b-bd6e-2679411bf30a` | 20-24 [crates/gwiki/src/video/types.rs:20-24] | Indexed class `VideoFrameDescription` in `crates/gwiki/src/video/types.rs`. [crates/gwiki/src/video/types.rs:20-24] |
| `AlignedVideoSegment` | class | `pub struct AlignedVideoSegment {` | `AlignedVideoSegment [class]` | `19b2f3b8-524d-59c2-a879-9088072b35e3` | 27-31 [crates/gwiki/src/video/types.rs:27-31] | Indexed class `AlignedVideoSegment` in `crates/gwiki/src/video/types.rs`. [crates/gwiki/src/video/types.rs:27-31] |
| `VideoAudioReference` | class | `pub struct VideoAudioReference {` | `VideoAudioReference [class]` | `b0f3c0fe-c88d-517c-b003-cfb6479f83d7` | 34-37 [crates/gwiki/src/video/types.rs:34-37] | Indexed class `VideoAudioReference` in `crates/gwiki/src/video/types.rs`. [crates/gwiki/src/video/types.rs:34-37] |
| `VideoMarkdownResult` | class | `pub struct VideoMarkdownResult {` | `VideoMarkdownResult [class]` | `ae9bb369-5991-5ff4-bbce-64480d5e0a72` | 40-43 [crates/gwiki/src/video/types.rs:40-43] | Indexed class `VideoMarkdownResult` in `crates/gwiki/src/video/types.rs`. [crates/gwiki/src/video/types.rs:40-43] |
| `VideoMediaMetadata` | class | `pub struct VideoMediaMetadata {` | `VideoMediaMetadata [class]` | `72a7dc30-b5d4-5f49-abd7-d2eb5a5e8dec` | 46-49 [crates/gwiki/src/video/types.rs:46-49] | Indexed class `VideoMediaMetadata` in `crates/gwiki/src/video/types.rs`. [crates/gwiki/src/video/types.rs:46-49] |
| `VideoMediaDegradation` | class | `pub struct VideoMediaDegradation {` | `VideoMediaDegradation [class]` | `1fae5c29-e587-59de-b5e9-5ab0b5bed290` | 52-56 [crates/gwiki/src/video/types.rs:52-56] | Indexed class `VideoMediaDegradation` in `crates/gwiki/src/video/types.rs`. [crates/gwiki/src/video/types.rs:52-56] |
| `VideoMarkdownRequest` | class | `pub struct VideoMarkdownRequest<'a> {` | `VideoMarkdownRequest [class]` | `22446b6f-de7f-5b4b-867e-00bcf324acc4` | 58-73 [crates/gwiki/src/video/types.rs:58-73] | Indexed class `VideoMarkdownRequest` in `crates/gwiki/src/video/types.rs`. [crates/gwiki/src/video/types.rs:58-73] |
