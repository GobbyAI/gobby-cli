---
title: crates/gwiki/src/ingest/file.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file.rs
  ranges:
  - 34-38
  - 41-44
  - 46-59
  - 62-94
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/file.rs:34-38](crates/gwiki/src/ingest/file.rs#L34-L38), [crates/gwiki/src/ingest/file.rs:41-44](crates/gwiki/src/ingest/file.rs#L41-L44), [crates/gwiki/src/ingest/file.rs:46-59](crates/gwiki/src/ingest/file.rs#L46-L59), [crates/gwiki/src/ingest/file.rs:62-94](crates/gwiki/src/ingest/file.rs#L62-L94)

</details>

# crates/gwiki/src/ingest/file.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file provides the file-ingest entry points for gwiki, connecting path-based and stdin-based inputs to the shared ingest pipeline. `ingest_path` delegates to `ingest_path_without_index` and then updates the wiki index, while `ingest_stdin` wraps raw stdin bytes in a `StdinSnapshot`, builds a `SourceDraft`/`SourceManifest` record, and ingests it as a stdin source before indexing. The two small result/snapshot types carry stdin metadata and local ingest degradations, and the module is split into helpers for degradation handling, dispatch, generic ingest, rendering, replay, and source registration.
[crates/gwiki/src/ingest/file.rs:34-38]
[crates/gwiki/src/ingest/file.rs:41-44]
[crates/gwiki/src/ingest/file.rs:46-59]
[crates/gwiki/src/ingest/file.rs:62-94]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `StdinSnapshot` | class | `pub struct StdinSnapshot {` | `StdinSnapshot [class]` | `b9ed125c-564c-56c9-9d5c-95c5e05d583e` | 34-38 [crates/gwiki/src/ingest/file.rs:34-38] | Indexed class `StdinSnapshot` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:34-38] |
| `LocalFileIngestResult` | class | `pub(crate) struct LocalFileIngestResult {` | `LocalFileIngestResult [class]` | `8f47278b-b904-5d63-a869-3086d56965e6` | 41-44 [crates/gwiki/src/ingest/file.rs:41-44] | Indexed class `LocalFileIngestResult` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:41-44] |
| `ingest_path` | function | `pub fn ingest_path(` | `ingest_path [function]` | `e9e4425e-8125-53ae-bcf0-af650e5c1bdf` | 46-59 [crates/gwiki/src/ingest/file.rs:46-59] | Indexed function `ingest_path` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:46-59] |
| `ingest_stdin` | function | `pub fn ingest_stdin(` | `ingest_stdin [function]` | `b860b1e3-9eba-5669-947a-9bcb5e68bb16` | 62-94 [crates/gwiki/src/ingest/file.rs:62-94] | Indexed function `ingest_stdin` in `crates/gwiki/src/ingest/file.rs`. [crates/gwiki/src/ingest/file.rs:62-94] |
