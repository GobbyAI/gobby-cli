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

`crates/gcode/src/commands/codewiki/build_parts/snapshot.rs` exposes 3 indexed API symbols.
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

## API Symbols

- `build_codewiki_index_snapshot` (function) component `build_codewiki_index_snapshot [function]` (`8a4cda8e-8e1d-539a-a929-f7ec34f73d38`) lines 6-84 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
  - Signature: `pub(crate) fn build_codewiki_index_snapshot(`
  - Purpose: I’m checking the full function body so the summary reflects the actual behavior, not just the truncated excerpt.The symbol isn’t showing up in the checked tree, so I’m relying on the provided source and summarizing only the visible behavior.Builds a `CodewikiIndexSnapshot` by retaining only core files and symbols, computing each file’s content hash and symbol count, materializing per-symbol snapshots, and conditionally deriving graph-neighborhood fingerprints or degraded sources based on graph availability. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
- `hash_snapshot_file` (function) component `hash_snapshot_file [function]` (`fc982987-7570-5095-b7df-450efceae8b5`) lines 86-99 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
  - Signature: `fn hash_snapshot_file(project_root: &Path, file: &str) -> anyhow::Result<String> {`
  - Purpose: It canonicalizes the project root and target file, verifies the resolved file stays within the project root, and returns the file’s content hash as a `String`, propagating any path-resolution or hashing errors as `anyhow::Error`. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
- `graph_neighborhood_fingerprints` (function) component `graph_neighborhood_fingerprints [function]` (`a23d7e7d-f73e-5b17-a94f-daf542fd5cc7`) lines 101-134 [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]
  - Signature: `fn graph_neighborhood_fingerprints(`
  - Purpose: It computes a deterministic fingerprint for each symbol by collecting all incident graph edge descriptors (`call`/`import` with source and target IDs), sorting them, joining them into a newline-delimited string, and hashing that string into a `BTreeMap<String, String>` keyed by symbol ID. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

