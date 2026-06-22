---
title: crates/gcode/src/index/indexer/types.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/types.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Overview

`crates/gcode/src/index/indexer/types.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gcode/src/index/indexer/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IndexRequest` | class | 'IndexRequest' is a serialized request payload that specifies a project root plus optional path filtering and explicit file lists, along with flags controlling full indexing, C++ semantic handling, and projection synchronization. [crates/gcode/src/index/indexer/types.rs:8-17] |
| `IndexDurations` | class | 'IndexDurations' is a timing aggregate struct that records the elapsed milliseconds spent in discovery, indexing, and stats collection, along with the overall total duration. [crates/gcode/src/index/indexer/types.rs:20-25] |
| `IndexDegradation` | type | Indexed type `IndexDegradation` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:29-42] |
| `IndexOutcome` | class | 'IndexOutcome' is a Rust struct that reports the results and metadata of a project indexing run, including file counts, unsupported types, indexed symbol/import/call/chunk/tombstone totals, indexed paths, timing data, degradation details, and optional projection-sync and overlay status. [crates/gcode/src/index/indexer/types.rs:45-68] |
| `UnsupportedFileType` | class | 'UnsupportedFileType' is a serializable Rust struct that records an unsupported file extension, the number of matching files, and an optional list of example filenames. [crates/gcode/src/index/indexer/types.rs:71-76] |
| `OverlayIndexMetadata` | class | 'OverlayIndexMetadata' stores the overlay and parent project identifiers and their corresponding root paths as four 'String' fields. [crates/gcode/src/index/indexer/types.rs:79-84] |
| `IndexOutcome::new` | method | Creates a new 'Self' by storing 'project_id' as an owned 'String' and initializing all other fields from 'Self::default()'. [crates/gcode/src/index/indexer/types.rs:87-92] |
| `IndexOutcome::add_counts` | method | 'add_counts' merges a 'FileIndexCounts' value into the receiver by element-wise adding all indexed-item counters and, when 'indexed_files > 0', appending the associated 'file_path' to 'indexed_file_paths'. [crates/gcode/src/index/indexer/types.rs:94-104] |
| `IndexOutcome::set_unsupported_file_types` | method | Replaces the current 'unsupported_file_types' field with the provided 'Vec<UnsupportedFileType>' value. [crates/gcode/src/index/indexer/types.rs:106-108] |
| `is_zero` | function | Returns 'true' if the referenced 'usize' is equal to '0', and 'false' otherwise. [crates/gcode/src/index/indexer/types.rs:111-113] |
| `FileIndexCounts` | class | 'FileIndexCounts' is a package-visible struct that records a file path together with per-file indexing totals for files, symbols, imports, calls, unresolved targets, and chunks. [crates/gcode/src/index/indexer/types.rs:116-124] |

