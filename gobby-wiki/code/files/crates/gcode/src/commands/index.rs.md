---
title: crates/gcode/src/commands/index.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/index.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/index.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The file crates/gcode/src/commands/index.rs provides the execution logic and formatting utilities for the indexing command in the gcode toolset. It is responsible for initializing the correct directory and target scope context, executing the files indexer under a project lock, and presenting structured feedback to the caller in either plain text or JSON.

The core command driver is the run function, which maps command-line arguments to internal API requests and coordinates downstream processes crates/gcode/src/commands/index.rs:10-60. To keep index operations safe from race conditions across processes, it acquires a project-wide indexing lock before running the core logic crates/gcode/src/commands/index.rs:10-60.

## How it fits

Next, it coordinates with index-locking systems and the core API engine. The lock layer index_lock::with_project_lock ensures safe exclusive access crates/gcode/src/commands/index.rs:10-60 before calling into the index engine api::index_files crates/gcode/src/commands/index.rs:10-60.
[crates/gcode/src/commands/index.rs:10-60]
[crates/gcode/src/commands/index.rs:62-92]
[crates/gcode/src/commands/index.rs:96-104]
[crates/gcode/src/commands/index.rs:107-117]
[crates/gcode/src/commands/index.rs:119-132]

## Key components

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
| `pluralize_handles_index_status_nouns` | function | Verifies that 'pluralize' returns the singular noun when the count is '1' and the plural form otherwise, including the '0' case. [crates/gcode/src/commands/index.rs:252-257] |
| `pluralize_leaves_unknown_nouns_unchanged` | function | Verifies that 'pluralize(2, "symbol")' returns the unmodified unknown noun '"symbol"' rather than attempting to inflect it. [crates/gcode/src/commands/index.rs:260-262] |
| `sample_outcome` | function | Returns an 'IndexOutcome' initialized with 'indexed_files = 12', 'skipped_files = 0', 'symbols_indexed = 348', and 'chunks_indexed = 921', with all remaining fields taken from 'IndexOutcome::default()'. [crates/gcode/src/commands/index.rs:264-272] |
| `sample_reports` | function | Returns a 'ProjectionSyncReports' value containing a healthy 'graph' report with fixed sync counts and no error, and a degraded 'vector' report with zero syncs plus a 'missing_qdrant_config' error. [crates/gcode/src/commands/index.rs:274-298] |
| `sync_projections_json_contract` | function | Builds a 'sync_projections_payload' from 'sample_outcome()' and 'sample_reports()', then asserts its JSON snapshot against 'sync_projections_payload'. [crates/gcode/src/commands/index.rs:301-305] |
| `sync_projections_text_contract` | function | Creates a sample projections payload from 'sample_outcome()' and 'sample_reports()', renders it to text with 'sync_projections_text', and snapshot-tests the resulting string. [crates/gcode/src/commands/index.rs:308-313] |
| `index_outcome_json_contract_redacts_durations` | function | Constructs a sample indexing outcome with populated counts and file paths, serializes it to JSON, replaces each 'durations' field ('discovery_ms', 'indexing_ms', 'stats_ms', 'total_ms') with the placeholder string '[duration-ms]', and snapshot-tests the redacted result. [crates/gcode/src/commands/index.rs:316-342] |
| `index_text_reports_unsupported_file_types` | function | Builds a sample outcome with unsupported file type entries for '.md', '.txt', and extensionless files, renders it via 'index_text', and asserts the output against a snapshot. [crates/gcode/src/commands/index.rs:345-368] |

