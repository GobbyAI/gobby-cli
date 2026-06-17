---
title: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
  ranges:
  - 6-84
  - 86-99
  - 101-134
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84](crates/gcode/src/commands/codewiki/build_parts/snapshot.rs#L6-L84), [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99](crates/gcode/src/commands/codewiki/build_parts/snapshot.rs#L86-L99), [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134](crates/gcode/src/commands/codewiki/build_parts/snapshot.rs#L101-L134)

</details>

# crates/gcode/src/commands/codewiki/build_parts/snapshot.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds a `CodewikiIndexSnapshot` from the input index data by filtering to core files, collecting per-file metadata, and packaging core symbols into snapshot records. It hashes each file’s contents with `hash_snapshot_file`, counts symbols per file, and conditionally computes graph-neighborhood fingerprints with `graph_neighborhood_fingerprints` when graph data is available, recording degraded sources when it is truncated or unavailable.
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_codewiki_index_snapshot` | function | `pub(crate) fn build_codewiki_index_snapshot(` | `build_codewiki_index_snapshot [function]` | `8a4cda8e-8e1d-539a-a929-f7ec34f73d38` | 6-84 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84] | Indexed function `build_codewiki_index_snapshot` in `crates/gcode/src/commands/codewiki/build_parts/snapshot.rs`. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84] |
| `hash_snapshot_file` | function | `fn hash_snapshot_file(project_root: &Path, file: &str) -> anyhow::Result<String> {` | `hash_snapshot_file [function]` | `fc982987-7570-5095-b7df-450efceae8b5` | 86-99 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99] | Indexed function `hash_snapshot_file` in `crates/gcode/src/commands/codewiki/build_parts/snapshot.rs`. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99] |
| `graph_neighborhood_fingerprints` | function | `fn graph_neighborhood_fingerprints(` | `graph_neighborhood_fingerprints [function]` | `a23d7e7d-f73e-5b17-a94f-daf542fd5cc7` | 101-134 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134] | Indexed function `graph_neighborhood_fingerprints` in `crates/gcode/src/commands/codewiki/build_parts/snapshot.rs`. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134] |
