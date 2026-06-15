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

# crates/gwiki/src/video/sampling.rs

Module: [[code/modules/crates/gwiki/src/video|crates/gwiki/src/video]]

## Purpose

This file builds video source references for downstream processing. `sample_frames` turns a `FrameSamplingPlan` into a list of `VideoFrameSample`s by emitting frame 0 first and then stepping by `interval_seconds` up to `duration_seconds`, with edge cases for zero interval and unknown duration. `frame_sample` centralizes construction of each frame sample by formatting the timestamp and generating a `path#t=<timestamp>` reference. `audio_reference_for_video` similarly creates a `VideoAudioReference` for the same asset, pointing to the display path with an `#audio` fragment.
[crates/gwiki/src/video/sampling.rs:8-32]
[crates/gwiki/src/video/sampling.rs:34-41]
[crates/gwiki/src/video/sampling.rs:43-54]

## API Symbols

- `sample_frames` (function) component `sample_frames [function]` (`a4cff237-0f26-5236-b79a-a2c68949c40f`) lines 8-32 [crates/gwiki/src/video/sampling.rs:8-32]
  - Signature: `pub fn sample_frames(asset_path: &Path, plan: FrameSamplingPlan) -> Vec<VideoFrameSample> {`
  - Purpose: Returns a vector of 'VideoFrameSample's by sampling the asset at '0' and then every 'plan.interval_seconds' up to 'plan.duration_seconds' inclusive, or an empty vector if the interval is zero, with a special case of sampling only the first frame when duration is unspecified. [crates/gwiki/src/video/sampling.rs:8-32]
- `audio_reference_for_video` (function) component `audio_reference_for_video [function]` (`ddeba91d-f1f9-5b9b-a1a9-62a80b0766a0`) lines 34-41 [crates/gwiki/src/video/sampling.rs:34-41]
  - Signature: `pub fn audio_reference_for_video(asset_path: &Path) -> VideoAudioReference {`
  - Purpose: Constructs a 'VideoAudioReference' for the given asset by cloning 'asset_path' into 'source_asset' and setting 'source_reference' to the asset’s display path with '#audio' appended. [crates/gwiki/src/video/sampling.rs:34-41]
- `frame_sample` (function) component `frame_sample [function]` (`6797d9d6-ffdd-5ca6-9955-2c5029dfe431`) lines 43-54 [crates/gwiki/src/video/sampling.rs:43-54]
  - Signature: `fn frame_sample(asset_path: &Path, timestamp_seconds: u32) -> VideoFrameSample {`
  - Purpose: Constructs a 'VideoFrameSample' from an asset path and timestamp by formatting the timestamp, cloning the path into 'source_asset', and generating a 'source_reference' URI fragment of the form 'path#t=<timestamp>'. [crates/gwiki/src/video/sampling.rs:43-54]

