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

# crates/gcode/src/commands/codewiki/build_parts/snapshot.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds a `CodewikiIndexSnapshot` from `CodewikiInput` by keeping only core files and symbols, counting symbols per file, hashing each retained file after validating it stays under the project root, and materializing per-symbol snapshots keyed by symbol ID. When graph data is available, it also derives deterministic neighborhood fingerprints from the graph edges, and records degraded sources when the graph is truncated or unavailable.
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

## API Symbols

- `build_codewiki_index_snapshot` (function) component `build_codewiki_index_snapshot [function]` (`8a4cda8e-8e1d-539a-a929-f7ec34f73d38`) lines 6-84 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
  - Signature: `pub(crate) fn build_codewiki_index_snapshot(`
  - Purpose: Builds a 'CodewikiIndexSnapshot' by retaining only core files and symbols, counting symbols per file, hashing each file’s contents, materializing per-symbol snapshots keyed by ID, and deriving graph-neighborhood fingerprints when graph data is available. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
- `hash_snapshot_file` (function) component `hash_snapshot_file [function]` (`fc982987-7570-5095-b7df-450efceae8b5`) lines 86-99 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
  - Signature: `fn hash_snapshot_file(project_root: &Path, file: &str) -> anyhow::Result<String> {`
  - Purpose: Canonicalizes a file path and computes its content hash while validating that the file resides within the project root to prevent directory traversal attacks. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
- `graph_neighborhood_fingerprints` (function) component `graph_neighborhood_fingerprints [function]` (`a23d7e7d-f73e-5b17-a94f-daf542fd5cc7`) lines 101-134 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]
  - Signature: `fn graph_neighborhood_fingerprints(`
  - Purpose: Computes deterministic hash fingerprints for each code symbol by hashing its sorted set of incoming and outgoing call/import edges. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

