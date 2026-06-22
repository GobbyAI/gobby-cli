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

`crates/gcode/src/commands/codewiki/build_parts/snapshot.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_codewiki_index_snapshot` | function | The 'build_codewiki_index_snapshot' function generates a 'CodewikiIndexSnapshot' by filtering input files and symbols for core files, computing file content hashes, aggregating symbol counts, and mapping symbol and graph neighborhood metadata. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:6-75] |
| `hash_snapshot_file` | function | This function canonicalizes the project root and source file paths, verifies that the file is located within the project root directory, and returns the content hash of the file. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:77-90] |
| `graph_neighborhood_fingerprints` | function | This function computes a content-hash fingerprint for each symbol's graph neighborhood by aggregating its incident call and import edges, formatting them as standardized strings, and hashing their sorted, newline-joined representations. [crates/gcode/src/commands/codewiki/build_parts/snapshot.rs:92-125] |

