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

# crates/gwiki/src/ingest/file/replay.rs

Module: [[code/modules/crates/gwiki/src/ingest/file|crates/gwiki/src/ingest/file]]

## Purpose

This file attaches replay metadata for an ingested local file. `attach_replay_metadata` builds a `SourceReplay` from the file path and ingest options, then updates the vault manifest entry whose `id` matches `result.record.id`. If the entry is missing or already has the same replay data, it still copies the replay into `result.record.replay` but reports no manifest change; otherwise it writes the new replay into both the manifest entry and the ingest result, and returns whether the manifest was modified. [crates/gwiki/src/ingest/file/replay.rs:8-32]

## API Symbols

- `attach_replay_metadata` (function) component `attach_replay_metadata [function]` (`f26f2009-6ceb-59de-9a93-702056d13e39`) lines 8-32 [crates/gwiki/src/ingest/file/replay.rs:8-32]
  - Signature: `pub(super) fn attach_replay_metadata(`
  - Purpose: Updates the vault manifest entry matching 'result.record.id' to store a 'SourceReplay' for the given local file and, in all cases, copies that replay metadata into 'result.record.replay', returning whether the manifest was modified. [crates/gwiki/src/ingest/file/replay.rs:8-32]

