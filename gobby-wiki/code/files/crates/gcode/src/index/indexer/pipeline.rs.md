---
title: crates/gcode/src/index/indexer/pipeline.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/pipeline.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/pipeline.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Overview

`crates/gcode/src/index/indexer/pipeline.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcode/src/index/indexer/pipeline.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `index_files` | function | Opens a read-write database connection using 'ctx.database_url' and delegates the actual indexing work to 'index_files_with_connection', returning its 'IndexOutcome' or any error. [crates/gcode/src/index/indexer/pipeline.rs:28-31] |
| `index_files_with_connection` | function | Dispatches indexing to 'index_overlay_files' when the context uses an overlay scope, otherwise indexes discovered files if no explicit files were requested, or explicit files via 'index_explicit_files_with_connection' when they were. [crates/gcode/src/index/indexer/pipeline.rs:33-46] |
| `index_discovered_files` | function | 'index_discovered_files' discovers project files under 'request.project_root' with exclusion and optional path filtering, records unsupported types, builds import/semantic context, computes incremental stale-file state, and removes orphaned database projections/facts for whole-project scans before continuing indexing. [crates/gcode/src/index/indexer/pipeline.rs:48-180] |
| `index_explicit_files_with_connection` | function | Indexes the request’s explicitly listed files relative to the project root by routing each existing file to AST or content-only processing, deleting projections/facts for missing or skipped files, and recording the resulting indexing outcome. [crates/gcode/src/index/indexer/pipeline.rs:182-312] |
| `discovery_options` | function | Constructs and returns a 'walker::DiscoveryOptions' value that sets 'respect_gitignore' from 'ctx.indexing.respect_gitignore'. [crates/gcode/src/index/indexer/pipeline.rs:314-318] |
| `explicit_route_with_discovery_options` | function | Returns an 'ExplicitFileRoute' for 'abs' relative to 'root_path', using 'explicit_file_route' when 'respect_gitignore' is false and otherwise mapping 'walker::classify_explicit_file_with_options' to 'Ast', 'ContentOnly', or 'Skip' depending on the file classification result. [crates/gcode/src/index/indexer/pipeline.rs:320-334] |
| `cleanup_skipped_file_if_indexed` | function | Increments 'outcome.skipped_files', and if 'file_facts_exist' is true, invokes 'cleanup_deleted_file_projections' for 'rel' and then runs 'delete_file_facts()', propagating any error and otherwise returning 'Ok(())'. [crates/gcode/src/index/indexer/pipeline.rs:336-350] |

