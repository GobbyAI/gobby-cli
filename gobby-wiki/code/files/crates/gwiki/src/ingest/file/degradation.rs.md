---
title: crates/gwiki/src/ingest/file/degradation.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/degradation.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file/degradation.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/file/degradation.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/file/degradation.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `transcription_degradation_summary` | function | This function formats a reference to a 'TranscriptionDegradation' struct into a colon-separated string prefixed with "audio_transcription" and containing the degradation's reason and fallback values. [crates/gwiki/src/ingest/file/degradation.rs:4-11] |
| `vision_degradation_summary` | function | The 'vision_degradation_summary' function formats a 'VisionDegradation' struct into a colon-delimited string containing the literal prefix 'vision', the degradation's reason, and its fallback mechanism. [crates/gwiki/src/ingest/file/degradation.rs:13-15] |
| `document_degradation_summary` | function | The function formats a 'DocumentDegradation' reference into a colon-delimited string containing the literal prefix "document", the degradation's reason, and its fallback value. [crates/gwiki/src/ingest/file/degradation.rs:18-22] |
| `video_degradation_summaries` | function | The 'video_degradation_summaries' function compiles a list of degradation summary strings by formatting the media degradations within a 'VideoIngestResult' and appending an optional transcription degradation summary. [crates/gwiki/src/ingest/file/degradation.rs:24-39] |

