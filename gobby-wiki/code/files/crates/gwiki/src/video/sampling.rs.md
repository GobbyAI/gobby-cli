---
title: crates/gwiki/src/video/sampling.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/sampling.rs
  ranges:
  - 8-32
  - 34-41
  - 43-54
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/video/sampling.rs:8-32](crates/gwiki/src/video/sampling.rs#L8-L32), [crates/gwiki/src/video/sampling.rs:34-41](crates/gwiki/src/video/sampling.rs#L34-L41), [crates/gwiki/src/video/sampling.rs:43-54](crates/gwiki/src/video/sampling.rs#L43-L54)

</details>

# crates/gwiki/src/video/sampling.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds video sampling references from an asset path and a sampling plan. `sample_frames` emits frame samples at a fixed interval, handling edge cases for zero interval and unknown duration by returning no samples or a single frame at `t=0`; it delegates per-frame construction to `frame_sample`. `frame_sample` formats the timestamp and creates the source asset/reference metadata for each sampled frame. `audio_reference_for_video` produces the matching audio reference by reusing the asset path and appending `#audio` to the display path.
[crates/gwiki/src/video/sampling.rs:8-32]
[crates/gwiki/src/video/sampling.rs:34-41]
[crates/gwiki/src/video/sampling.rs:43-54]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `sample_frames` | function | `pub fn sample_frames(asset_path: &Path, plan: FrameSamplingPlan) -> Vec<VideoFrameSample> {` | `sample_frames [function]` | `a4cff237-0f26-5236-b79a-a2c68949c40f` | 8-32 [crates/gwiki/src/video/sampling.rs:8-32] | Indexed function `sample_frames` in `crates/gwiki/src/video/sampling.rs`. [crates/gwiki/src/video/sampling.rs:8-32] |
| `audio_reference_for_video` | function | `pub fn audio_reference_for_video(asset_path: &Path) -> VideoAudioReference {` | `audio_reference_for_video [function]` | `ddeba91d-f1f9-5b9b-a1a9-62a80b0766a0` | 34-41 [crates/gwiki/src/video/sampling.rs:34-41] | Indexed function `audio_reference_for_video` in `crates/gwiki/src/video/sampling.rs`. [crates/gwiki/src/video/sampling.rs:34-41] |
| `frame_sample` | function | `fn frame_sample(asset_path: &Path, timestamp_seconds: u32) -> VideoFrameSample {` | `frame_sample [function]` | `6797d9d6-ffdd-5ca6-9955-2c5029dfe431` | 43-54 [crates/gwiki/src/video/sampling.rs:43-54] | Indexed function `frame_sample` in `crates/gwiki/src/video/sampling.rs`. [crates/gwiki/src/video/sampling.rs:43-54] |
