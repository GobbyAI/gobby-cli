---
title: crates/gwiki/src/ingest/file/degradation.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/degradation.rs
  ranges:
  - 4-11
  - 13-15
  - 18-22
  - 24-39
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/file/degradation.rs:4-11](crates/gwiki/src/ingest/file/degradation.rs#L4-L11), [crates/gwiki/src/ingest/file/degradation.rs:13-15](crates/gwiki/src/ingest/file/degradation.rs#L13-L15), [crates/gwiki/src/ingest/file/degradation.rs:18-22](crates/gwiki/src/ingest/file/degradation.rs#L18-L22), [crates/gwiki/src/ingest/file/degradation.rs:24-39](crates/gwiki/src/ingest/file/degradation.rs#L24-L39)

</details>

# crates/gwiki/src/ingest/file/degradation.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines small formatting helpers that turn different ingest degradation records into standardized summary strings. `transcription_degradation_summary`, `vision_degradation_summary`, and the feature-gated `document_degradation_summary` each encode a single degradation as a type-prefixed `reason`/`fallback` string, while `video_degradation_summaries` collects all media degradations from a `VideoIngestResult` into `Vec<String>` and appends the transcription degradation summary when present.
[crates/gwiki/src/ingest/file/degradation.rs:4-11]
[crates/gwiki/src/ingest/file/degradation.rs:13-15]
[crates/gwiki/src/ingest/file/degradation.rs:18-22]
[crates/gwiki/src/ingest/file/degradation.rs:24-39]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `transcription_degradation_summary` | function | `pub(super) fn transcription_degradation_summary(` | `transcription_degradation_summary [function]` | `d864d1c9-a5d4-56d1-9044-ef2972a76b3e` | 4-11 [crates/gwiki/src/ingest/file/degradation.rs:4-11] | Indexed function `transcription_degradation_summary` in `crates/gwiki/src/ingest/file/degradation.rs`. [crates/gwiki/src/ingest/file/degradation.rs:4-11] |
| `vision_degradation_summary` | function | `pub(super) fn vision_degradation_summary(degradation: &VisionDegradation) -> String {` | `vision_degradation_summary [function]` | `387e4be4-1a32-5b50-b2d8-46c532d02e50` | 13-15 [crates/gwiki/src/ingest/file/degradation.rs:13-15] | Indexed function `vision_degradation_summary` in `crates/gwiki/src/ingest/file/degradation.rs`. [crates/gwiki/src/ingest/file/degradation.rs:13-15] |
| `document_degradation_summary` | function | `pub(super) fn document_degradation_summary(` | `document_degradation_summary [function]` | `01d024dc-1ebe-518e-8db2-97d3d9195193` | 18-22 [crates/gwiki/src/ingest/file/degradation.rs:18-22] | Indexed function `document_degradation_summary` in `crates/gwiki/src/ingest/file/degradation.rs`. [crates/gwiki/src/ingest/file/degradation.rs:18-22] |
| `video_degradation_summaries` | function | `pub(super) fn video_degradation_summaries(result: &VideoIngestResult) -> Vec<String> {` | `video_degradation_summaries [function]` | `a1fd8178-96ce-546d-ad0b-f19e41840cf8` | 24-39 [crates/gwiki/src/ingest/file/degradation.rs:24-39] | Indexed function `video_degradation_summaries` in `crates/gwiki/src/ingest/file/degradation.rs`. [crates/gwiki/src/ingest/file/degradation.rs:24-39] |
