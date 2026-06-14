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

This file implements the indexing pipeline orchestration for the gcode indexer. It provides the main entry point `index_files` which establishes a database connection and routes to the appropriate indexing strategy via `index_files_with_connection`. That router dispatches to either overlay indexing, discovered file indexing, or explicit file indexing based on project scope and request contents. The discovered files flow uses `walker::discover_files_with_options` with configuration from `discovery_options` to find candidates, then processes them through `index_discovered_files`. The explicit files flow uses `index_explicit_files_with_connection` for directly specified paths, optionally incorporating discovery through `explicit_route_with_discovery_options`. Supporting utilities like `cleanup_skipped_file_if_indexed` manage state cleanup. Together these functions form the decision tree and orchestration logic that coordinates file discovery, filtering, semantic resolution, and indexing outcomes.
[crates/gcode/src/index/indexer/pipeline.rs:27-30]
[crates/gcode/src/index/indexer/pipeline.rs:32-45]
[crates/gcode/src/index/indexer/pipeline.rs:47-173]
[crates/gcode/src/index/indexer/pipeline.rs:175-302]
[crates/gcode/src/index/indexer/pipeline.rs:304-308]

## API Symbols

- `index_files` (function) component `index_files [function]` (`bdb416a7-b6ae-5ba6-a21f-74c21bbb3f2f`) lines 27-30 [crates/gcode/src/index/indexer/pipeline.rs:27-30]
  - Signature: `pub fn index_files(request: IndexRequest, ctx: &Context) -> anyhow::Result<IndexOutcome> {`
  - Purpose: Indexed function `index_files` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:27-30]
- `index_files_with_connection` (function) component `index_files_with_connection [function]` (`adeaf14e-284b-5071-97f0-2d17d8c8a6df`) lines 32-45 [crates/gcode/src/index/indexer/pipeline.rs:32-45]
  - Signature: `fn index_files_with_connection(`
  - Purpose: Indexed function `index_files_with_connection` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:32-45]
- `index_discovered_files` (function) component `index_discovered_files [function]` (`84dc976d-70f1-5221-9a0a-7bab5732f0e6`) lines 47-173 [crates/gcode/src/index/indexer/pipeline.rs:47-173]
  - Signature: `fn index_discovered_files(`
  - Purpose: Indexed function `index_discovered_files` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:47-173]
- `index_explicit_files_with_connection` (function) component `index_explicit_files_with_connection [function]` (`b21220d8-8ce4-56bc-8ff3-d0b4aba5ba35`) lines 175-302 [crates/gcode/src/index/indexer/pipeline.rs:175-302]
  - Signature: `fn index_explicit_files_with_connection(`
  - Purpose: Indexed function `index_explicit_files_with_connection` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:175-302]
- `discovery_options` (function) component `discovery_options [function]` (`9277356b-c936-5f0d-b037-815c545cb4bf`) lines 304-308 [crates/gcode/src/index/indexer/pipeline.rs:304-308]
  - Signature: `fn discovery_options(ctx: &Context) -> walker::DiscoveryOptions {`
  - Purpose: Indexed function `discovery_options` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:304-308]
- `explicit_route_with_discovery_options` (function) component `explicit_route_with_discovery_options [function]` (`f477c451-1037-581b-b310-35da45fa9472`) lines 310-324 [crates/gcode/src/index/indexer/pipeline.rs:310-324]
  - Signature: `pub(super) fn explicit_route_with_discovery_options(`
  - Purpose: Indexed function `explicit_route_with_discovery_options` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:310-324]
- `cleanup_skipped_file_if_indexed` (function) component `cleanup_skipped_file_if_indexed [function]` (`e6420dba-4991-5dd4-84e0-88430e3b3b73`) lines 326-340 [crates/gcode/src/index/indexer/pipeline.rs:326-340]
  - Signature: `pub(super) fn cleanup_skipped_file_if_indexed(`
  - Purpose: Indexed function `cleanup_skipped_file_if_indexed` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:326-340]

