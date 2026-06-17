---
title: crates/gwiki/src/ingest/file/dispatch.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/dispatch.rs
  ranges:
  - 43-242
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/file/dispatch.rs:43-242](crates/gwiki/src/ingest/file/dispatch.rs#L43-L242)

</details>

# crates/gwiki/src/ingest/file/dispatch.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides the no-index ingest dispatcher for local files. `ingest_path_without_index` inspects a path to determine the `SourceKind`, derives a fallback file name and source location, then routes the file through the appropriate specialized ingestor: audio, image, video, session, and, when enabled, document or PDF handling. If no specialized path applies, it falls back to the generic file ingester. The resulting `LocalFileIngestResult` is then normalized with replay metadata and returned, so this file acts as the central entry point that coordinates source detection, format-specific ingestion, and shared result post-processing. [crates/gwiki/src/ingest/file/dispatch.rs:43-242]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ingest_path_without_index` | function | `pub(crate) fn ingest_path_without_index(` | `ingest_path_without_index [function]` | `90056d6c-fb43-5530-a1b4-6117c5481458` | 43-242 [crates/gwiki/src/ingest/file/dispatch.rs:43-242] | Indexed function `ingest_path_without_index` in `crates/gwiki/src/ingest/file/dispatch.rs`. [crates/gwiki/src/ingest/file/dispatch.rs:43-242] |
