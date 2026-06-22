---
title: crates/gwiki/src/video/alignment.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/alignment.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video/alignment.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/video/alignment.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gwiki/src/video/alignment.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `align_transcript_and_frames` | function | # Summary 'align_transcript_and_frames' aligns transcript segments with video frame descriptions by associating each transcript segment to its nearest preceding frame timestamp, returning a chronologically-ordered collection of composite 'AlignedVideoSegment' objects. [crates/gwiki/src/video/alignment.rs:8-66] |
| `timestamp_seconds_or_zero` | function | Parses a string value as a timestamp in seconds, returning the parsed u32 result or defaulting to 0 on parse failure while logging the error at debug level. [crates/gwiki/src/video/alignment.rs:68-76] |

