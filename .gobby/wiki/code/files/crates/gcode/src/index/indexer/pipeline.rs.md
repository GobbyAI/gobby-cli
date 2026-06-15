---
title: crates/gcode/src/index/indexer/pipeline.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/pipeline.rs
  ranges:
  - 27-30
  - 32-45
  - 47-173
  - 175-302
  - 304-308
  - 310-324
  - 326-340
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/pipeline.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file implements the indexing pipeline for a project: it opens a read-write database connection, then routes the request to overlay indexing, discovered-file indexing, or explicit-file indexing based on the current scope and request contents. The helper functions build discovery options, classify explicit files with or without gitignore-aware discovery rules, and clean up skipped or deleted files by removing stale projections and facts while accumulating an `IndexOutcome` for the run.
[crates/gcode/src/index/indexer/pipeline.rs:27-30]
[crates/gcode/src/index/indexer/pipeline.rs:32-45]
[crates/gcode/src/index/indexer/pipeline.rs:47-173]
[crates/gcode/src/index/indexer/pipeline.rs:175-302]
[crates/gcode/src/index/indexer/pipeline.rs:304-308]

## API Symbols

- `index_files` (function) component `index_files [function]` (`bdb416a7-b6ae-5ba6-a21f-74c21bbb3f2f`) lines 27-30 [crates/gcode/src/index/indexer/pipeline.rs:27-30]
  - Signature: `pub fn index_files(request: IndexRequest, ctx: &Context) -> anyhow::Result<IndexOutcome> {`
  - Purpose: Opens a read-write database connection from 'ctx.database_url' and delegates the indexing work to 'index_files_with_connection', returning its 'IndexOutcome' or any error. [crates/gcode/src/index/indexer/pipeline.rs:27-30]
- `index_files_with_connection` (function) component `index_files_with_connection [function]` (`adeaf14e-284b-5071-97f0-2d17d8c8a6df`) lines 32-45 [crates/gcode/src/index/indexer/pipeline.rs:32-45]
  - Signature: `fn index_files_with_connection(`
  - Purpose: Dispatches file indexing over a 'Client' by first routing overlay scopes to 'index_overlay_files', then choosing discovered-file indexing when no explicit files were requested or explicit-file indexing otherwise, returning an 'IndexOutcome' wrapped in 'anyhow::Result'. [crates/gcode/src/index/indexer/pipeline.rs:32-45]
- `index_discovered_files` (function) component `index_discovered_files [function]` (`84dc976d-70f1-5221-9a0a-7bab5732f0e6`) lines 47-173 [crates/gcode/src/index/indexer/pipeline.rs:47-173]
  - Signature: `fn index_discovered_files(`
  - Purpose: Scans the project tree for discoverable files, applies an optional path filter, records unsupported types, builds import and semantic-resolution context, computes incremental stale/orphan cleanup state, and returns an 'IndexOutcome' after pruning deleted-file projections and facts for whole-project scans. [crates/gcode/src/index/indexer/pipeline.rs:47-173]
- `index_explicit_files_with_connection` (function) component `index_explicit_files_with_connection [function]` (`b21220d8-8ce4-56bc-8ff3-d0b4aba5ba35`) lines 175-302 [crates/gcode/src/index/indexer/pipeline.rs:175-302]
  - Signature: `fn index_explicit_files_with_connection(`
  - Purpose: 'index_explicit_files_with_connection' processes an explicit file list for a project by resolving paths against the project root, deleting stale facts/vectors for missing files, routing existing files into AST, content-only, or skip paths using discovery/exclude rules, and accumulating an 'IndexOutcome' for the index run. [crates/gcode/src/index/indexer/pipeline.rs:175-302]
- `discovery_options` (function) component `discovery_options [function]` (`9277356b-c936-5f0d-b037-815c545cb4bf`) lines 304-308 [crates/gcode/src/index/indexer/pipeline.rs:304-308]
  - Signature: `fn discovery_options(ctx: &Context) -> walker::DiscoveryOptions {`
  - Purpose: 'discovery_options' builds and returns a 'walker::DiscoveryOptions' value that copies the 'respect_gitignore' setting from 'ctx.indexing'. [crates/gcode/src/index/indexer/pipeline.rs:304-308]
- `explicit_route_with_discovery_options` (function) component `explicit_route_with_discovery_options [function]` (`f477c451-1037-581b-b310-35da45fa9472`) lines 310-324 [crates/gcode/src/index/indexer/pipeline.rs:310-324]
  - Signature: `pub(super) fn explicit_route_with_discovery_options(`
  - Purpose: Returns 'ExplicitFileRoute::Ast' or '::ContentOnly' when 'walker::classify_explicit_file_with_options' classifies the file under the given discovery options, falls back to 'explicit_file_route' when '.respect_gitignore' is false, and otherwise yields 'ExplicitFileRoute::Skip' if the file is not classified. [crates/gcode/src/index/indexer/pipeline.rs:310-324]
- `cleanup_skipped_file_if_indexed` (function) component `cleanup_skipped_file_if_indexed [function]` (`e6420dba-4991-5dd4-84e0-88430e3b3b73`) lines 326-340 [crates/gcode/src/index/indexer/pipeline.rs:326-340]
  - Signature: `pub(super) fn cleanup_skipped_file_if_indexed(`
  - Purpose: Increments 'outcome.skipped_files', and if 'file_facts_exist' is true, calls 'cleanup_deleted_file_projections' for 'rel' using the supplied sync state and then executes 'delete_file_facts', returning 'Ok(())' unless the deletion closure errors. [crates/gcode/src/index/indexer/pipeline.rs:326-340]

