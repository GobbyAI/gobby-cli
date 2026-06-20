---
title: crates/gcode/src/commands/index.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/index.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/index.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

`crates/gcode/src/commands/index.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gcode/src/commands/index.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `run` | function | Resolves the target indexing context, builds an 'IndexRequest' from the optional file list and flags, runs 'api::index_files' under a waited project lock, optionally syncs projections afterward, and prints either JSON or text output for the resulting index or sync payload. [crates/gcode/src/commands/index.rs:10-60] |
| `index_text` | function | Returns a formatted summary string reporting indexed files, skipped files, indexed symbols, indexed chunks, and total duration in milliseconds, optionally appending a per-extension list of unsupported file types that were indexed as text only with file counts and examples. [crates/gcode/src/commands/index.rs:62-92] |
| `pluralize` | function | Returns a string slice that pluralizes only the hard-coded nouns '"file"' and '"example"' based on 'count' ('1' keeps singular, otherwise plural), and falls back to 'singular' unchanged for all other inputs. [crates/gcode/src/commands/index.rs:96-104] |
| `IndexSyncProjectionsOutput` | class | 'IndexSyncProjectionsOutput' is a crate-visible aggregation struct that reports an index-sync run’s file and symbol/chunk counts, skipped files, unsupported file types, degradation records, and nested projection synchronization reports. [crates/gcode/src/commands/index.rs:107-117] |
| `sync_projections_payload` | function | Constructs an 'IndexSyncProjectionsOutput' by copying indexed/skipped file counts, unsupported file types, symbol and chunk counts, and degraded state from 'IndexOutcome', while attaching the provided 'ProjectionSyncReports'. [crates/gcode/src/commands/index.rs:119-132] |
| `sync_projections_text` | function | Serializes the provided 'IndexSyncProjectionsOutput' payload to a JSON 'String' with 'serde_json::to_string' and returns it as an 'anyhow::Result'. [crates/gcode/src/commands/index.rs:134-138] |
| `resolve_index_context` | function | Resolves a path-scoped 'Context' for an optional input path by returning a cloned context for the current project when 'path' is 'None', or by detecting the target project root from the path and, if it differs from the current context, reloading that project’s identity and index scope before returning the updated context plus an optional path filter. [crates/gcode/src/commands/index.rs:140-195] |
| `clone_context` | function | Creates a new 'Context' by cloning the source context’s configuration fields, replacing 'project_root', 'project_id', and 'index_scope' with the provided values. [crates/gcode/src/commands/index.rs:197-216] |
| `path_filter_for` | function | Resolves 'target' to an absolute path relative to the current directory or 'project_root', canonicalizes both paths when possible, and returns 'None' only when the resolved target matches the canonicalized project root, otherwise 'Some(target_abs)'. [crates/gcode/src/commands/index.rs:218-240] |
| `sample_outcome` | function | Returns an 'IndexOutcome' initialized with 'indexed_files = 12', 'skipped_files = 0', 'symbols_indexed = 348', and 'chunks_indexed = 921', with all remaining fields taken from 'IndexOutcome::default()'. [crates/gcode/src/commands/index.rs:264-272] |
| `sample_reports` | function | Returns a 'ProjectionSyncReports' value containing a healthy 'graph' report with fixed sync counts and no error, and a degraded 'vector' report with zero syncs plus a 'missing_qdrant_config' error. [crates/gcode/src/commands/index.rs:274-298] |

_Verified by 6 in-file unit tests._

