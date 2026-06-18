---
title: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/snapshot.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/snapshot.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/snapshot.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_codewiki_index_snapshot` | function | Builds a 'CodewikiIndexSnapshot' for core project files by collecting core-file snapshots with content hashes and symbol counts, snapshotting core symbols by ID, and deriving graph-neighborhood data or degradation metadata depending on graph availability. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-84] |
| `hash_snapshot_file` | function | Resolves and validates 'file' against 'project_root', rejects paths outside the canonical root, and returns the content hash of the canonicalized source file with contextual error messages on failure. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:86-99] |
| `graph_neighborhood_fingerprints` | function | Builds a deterministic fingerprint map for each symbol by collecting all incident call/import graph edges for that symbol, sorting their formatted edge keys, hashing the newline-joined list, and returning 'BTreeMap<String, String>' of symbol ID to content hash. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:101-134] |

