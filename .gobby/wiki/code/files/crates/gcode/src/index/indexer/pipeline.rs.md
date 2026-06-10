---
title: crates/gcode/src/index/indexer/pipeline.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/pipeline.rs
  ranges:
  - 27-30
  - 32-45
  - 47-164
  - 166-293
  - 295-299
  - 301-315
  - 317-331
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/pipeline.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

`crates/gcode/src/index/indexer/pipeline.rs` exposes 7 indexed API symbols.
[crates/gcode/src/index/indexer/pipeline.rs:27-30]
[crates/gcode/src/index/indexer/pipeline.rs:32-45]
[crates/gcode/src/index/indexer/pipeline.rs:47-164]
[crates/gcode/src/index/indexer/pipeline.rs:166-293]
[crates/gcode/src/index/indexer/pipeline.rs:295-299]
[crates/gcode/src/index/indexer/pipeline.rs:301-315]
[crates/gcode/src/index/indexer/pipeline.rs:317-331]

## API Symbols

- `index_files` (function) component `index_files [function]` (`bdb416a7-b6ae-5ba6-a21f-74c21bbb3f2f`) lines 27-30 [crates/gcode/src/index/indexer/pipeline.rs:27-30]
  - Signature: `pub fn index_files(request: IndexRequest, ctx: &Context) -> anyhow::Result<IndexOutcome> {`
  - Purpose: Indexed function `index_files` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:27-30]
- `index_files_with_connection` (function) component `index_files_with_connection [function]` (`adeaf14e-284b-5071-97f0-2d17d8c8a6df`) lines 32-45 [crates/gcode/src/index/indexer/pipeline.rs:32-45]
  - Signature: `fn index_files_with_connection(`
  - Purpose: Indexed function `index_files_with_connection` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:32-45]
- `index_discovered_files` (function) component `index_discovered_files [function]` (`84dc976d-70f1-5221-9a0a-7bab5732f0e6`) lines 47-164 [crates/gcode/src/index/indexer/pipeline.rs:47-164]
  - Signature: `fn index_discovered_files(`
  - Purpose: Indexed function `index_discovered_files` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:47-164]
- `index_explicit_files_with_connection` (function) component `index_explicit_files_with_connection [function]` (`388791a3-c68c-5526-ae2b-22228a5abf9a`) lines 166-293 [crates/gcode/src/index/indexer/pipeline.rs:166-293]
  - Signature: `fn index_explicit_files_with_connection(`
  - Purpose: Indexed function `index_explicit_files_with_connection` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:166-293]
- `discovery_options` (function) component `discovery_options [function]` (`d861f7ac-d503-569e-92bf-7af185d9864c`) lines 295-299 [crates/gcode/src/index/indexer/pipeline.rs:295-299]
  - Signature: `fn discovery_options(ctx: &Context) -> walker::DiscoveryOptions {`
  - Purpose: Indexed function `discovery_options` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:295-299]
- `explicit_route_with_discovery_options` (function) component `explicit_route_with_discovery_options [function]` (`afebe3bb-85a7-55ec-b928-6b32ca3b56aa`) lines 301-315 [crates/gcode/src/index/indexer/pipeline.rs:301-315]
  - Signature: `pub(super) fn explicit_route_with_discovery_options(`
  - Purpose: Indexed function `explicit_route_with_discovery_options` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:301-315]
- `cleanup_skipped_explicit_file_if_indexed` (function) component `cleanup_skipped_explicit_file_if_indexed [function]` (`fa0d9e06-8afa-5fa5-bf9e-598a4849028b`) lines 317-331 [crates/gcode/src/index/indexer/pipeline.rs:317-331]
  - Signature: `pub(super) fn cleanup_skipped_explicit_file_if_indexed(`
  - Purpose: Indexed function `cleanup_skipped_explicit_file_if_indexed` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:317-331]

