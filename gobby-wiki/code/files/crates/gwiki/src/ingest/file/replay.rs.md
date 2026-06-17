---
title: crates/gwiki/src/ingest/file/replay.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/replay.rs
  ranges:
  - 8-32
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/file/replay.rs:8-32](crates/gwiki/src/ingest/file/replay.rs#L8-L32)

</details>

# crates/gwiki/src/ingest/file/replay.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides the ingest-time replay metadata hookup for a file. `attach_replay_metadata` builds a `SourceReplay` for the local file path, then updates the `SourceManifest` entry matching the ingested record ID. If the manifest has no matching entry, it still records the replay on the in-memory ingest result and reports no manifest change; if the entry already has the same replay, it only syncs the result record; otherwise it writes the replay into both the manifest entry and the ingest result, returning whether the manifest was modified. [crates/gwiki/src/ingest/file/replay.rs:8-32]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `attach_replay_metadata` | function | `pub(super) fn attach_replay_metadata(` | `attach_replay_metadata [function]` | `f26f2009-6ceb-59de-9a93-702056d13e39` | 8-32 [crates/gwiki/src/ingest/file/replay.rs:8-32] | Indexed function `attach_replay_metadata` in `crates/gwiki/src/ingest/file/replay.rs`. [crates/gwiki/src/ingest/file/replay.rs:8-32] |
