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

This file builds and snapshots code index data for a codewiki system. The primary function, build_codewiki_index_snapshot, orchestrates the snapshot creation by filtering core files and symbols, computing content hashes for each file, and capturing symbol metadata. It delegates to hash_snapshot_file to securely compute file content hashes while preventing directory traversal attacks through path canonicalization and root validation. For symbol relationships, it calls graph_neighborhood_fingerprints to generate deterministic fingerprints by hashing each symbol's sorted incoming and outgoing edges, enabling change detection in code dependencies. The functions work together to produce a complete, integrity-checked snapshot of the codebase state suitable for indexing and tracking code structure changes.
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

## API Symbols

- `build_codewiki_index_snapshot` (function) component `build_codewiki_index_snapshot [function]` (`8a4cda8e-8e1d-539a-a929-f7ec34f73d38`) lines 6-84 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
  - Signature: `pub(crate) fn build_codewiki_index_snapshot(`
  - Purpose: Indexed function `build_codewiki_index_snapshot` in `crates/gcode/src/commands/codewiki/build_parts/snapshot.rs`. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
- `hash_snapshot_file` (function) component `hash_snapshot_file [function]` (`fc982987-7570-5095-b7df-450efceae8b5`) lines 86-99 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
  - Signature: `fn hash_snapshot_file(project_root: &Path, file: &str) -> anyhow::Result<String> {`
  - Purpose: Canonicalizes a file path and computes its content hash while validating that the file resides within the project root to prevent directory traversal attacks. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
- `graph_neighborhood_fingerprints` (function) component `graph_neighborhood_fingerprints [function]` (`a23d7e7d-f73e-5b17-a94f-daf542fd5cc7`) lines 101-134 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]
  - Signature: `fn graph_neighborhood_fingerprints(`
  - Purpose: Computes deterministic hash fingerprints for each code symbol by hashing its sorted set of incoming and outgoing call/import edges. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

