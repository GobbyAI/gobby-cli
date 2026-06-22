---
title: crates/gwiki/src/video/sampling.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/sampling.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video/sampling.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/video/sampling.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/video/sampling.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `sample_frames` | function | Samples video frames from an asset file at regular time intervals specified by a 'FrameSamplingPlan', returning a vector of frame samples with overflow-safe timestamp arithmetic. [crates/gwiki/src/video/sampling.rs:8-32] |
| `audio_reference_for_video` | function | This function constructs a 'VideoAudioReference' struct containing the provided asset path as an owned 'PathBuf' and a URI reference string formed by appending the '#audio' fragment identifier to the displayed asset path. [crates/gwiki/src/video/sampling.rs:34-41] |
| `frame_sample` | function | Creates a 'VideoFrameSample' struct by formatting a timestamp and constructing a time-indexed URI reference from the provided asset path. [crates/gwiki/src/video/sampling.rs:43-54] |

