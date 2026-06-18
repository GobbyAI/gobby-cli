---
title: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/build_parts/snapshot.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview
This file implements the mechanisms required to generate a deterministic structural snapshot of a project's core codebase. Its primary purpose is to capture file and symbol states, which serves as a foundation for building a Codewiki index.

Additionally, the file is responsible for verifying file locations and tracking the relational context of code elements. It calculates deterministic hashes for local file contents and maps out dependencies between symbols, handling cases where the project graph data might be degraded or missing.

## How it fits
As a building block of the `codewiki` build pipeline, this file transforms incoming raw `CodewikiInput` data into a structured `CodewikiIndexSnapshot`. It coordinates closely with structural hashing utility functions and dependency analysis modules.
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99]
[crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_codewiki_index_snapshot` | function | Builds a 'CodewikiIndexSnapshot' for core project files by collecting core-file snapshots with content hashes and symbol counts, snapshotting core symbols by ID, and deriving graph-neighborhood data or degradation metadata depending on graph availability. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84] |
| `hash_snapshot_file` | function | Resolves and validates 'file' against 'project_root', rejects paths outside the canonical root, and returns the content hash of the canonicalized source file with contextual error messages on failure. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99] |
| `graph_neighborhood_fingerprints` | function | Builds a deterministic fingerprint map for each symbol by collecting all incident call/import graph edges for that symbol, sorting their formatted edge keys, hashing the newline-joined list, and returning 'BTreeMap<String, String>' of symbol ID to content hash. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134] |

