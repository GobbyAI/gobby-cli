---
title: crates/gcode/src/index/indexer/pipeline.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/pipeline.rs
  ranges:
  - 28-31
  - 33-46
  - 48-180
  - 182-312
  - 314-318
  - 320-334
  - 336-350
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer/pipeline.rs:28-31](crates/gcode/src/index/indexer/pipeline.rs#L28-L31), [crates/gcode/src/index/indexer/pipeline.rs:33-46](crates/gcode/src/index/indexer/pipeline.rs#L33-L46), [crates/gcode/src/index/indexer/pipeline.rs:48-180](crates/gcode/src/index/indexer/pipeline.rs#L48-L180), [crates/gcode/src/index/indexer/pipeline.rs:182-312](crates/gcode/src/index/indexer/pipeline.rs#L182-L312), [crates/gcode/src/index/indexer/pipeline.rs:314-318](crates/gcode/src/index/indexer/pipeline.rs#L314-L318), [crates/gcode/src/index/indexer/pipeline.rs:320-334](crates/gcode/src/index/indexer/pipeline.rs#L320-L334), [crates/gcode/src/index/indexer/pipeline.rs:336-350](crates/gcode/src/index/indexer/pipeline.rs#L336-L350)

</details>

# crates/gcode/src/index/indexer/pipeline.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

Implements the top-level indexing pipeline for a project. `index_files` opens a read-write database connection and dispatches to overlay indexing, discovered-file indexing, or explicit-file indexing; the helper functions split out discovery configuration, explicit-route handling, and cleanup for files that were skipped or already indexed.
[crates/gcode/src/index/indexer/pipeline.rs:28-31]
[crates/gcode/src/index/indexer/pipeline.rs:33-46]
[crates/gcode/src/index/indexer/pipeline.rs:48-180]
[crates/gcode/src/index/indexer/pipeline.rs:182-312]
[crates/gcode/src/index/indexer/pipeline.rs:314-318]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `index_files` | function | `pub fn index_files(request: IndexRequest, ctx: &Context) -> anyhow::Result<IndexOutcome> {` | `index_files [function]` | `6cd767b0-3903-5503-be7c-9488680a3b16` | 28-31 [crates/gcode/src/index/indexer/pipeline.rs:28-31] | Indexed function `index_files` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:28-31] |
| `index_files_with_connection` | function | `fn index_files_with_connection(` | `index_files_with_connection [function]` | `8e7f5655-bc34-5ee7-87d5-ce406ef86886` | 33-46 [crates/gcode/src/index/indexer/pipeline.rs:33-46] | Indexed function `index_files_with_connection` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:33-46] |
| `index_discovered_files` | function | `fn index_discovered_files(` | `index_discovered_files [function]` | `3d6aa723-2339-5aa1-b97d-6303ffa07ddb` | 48-180 [crates/gcode/src/index/indexer/pipeline.rs:48-180] | Indexed function `index_discovered_files` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:48-180] |
| `index_explicit_files_with_connection` | function | `fn index_explicit_files_with_connection(` | `index_explicit_files_with_connection [function]` | `480f4240-fe66-5be4-b249-271b32dca49f` | 182-312 [crates/gcode/src/index/indexer/pipeline.rs:182-312] | Indexed function `index_explicit_files_with_connection` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:182-312] |
| `discovery_options` | function | `fn discovery_options(ctx: &Context) -> walker::DiscoveryOptions {` | `discovery_options [function]` | `8683212b-99b4-580a-8f88-79f8dc1255a5` | 314-318 [crates/gcode/src/index/indexer/pipeline.rs:314-318] | Indexed function `discovery_options` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:314-318] |
| `explicit_route_with_discovery_options` | function | `pub(super) fn explicit_route_with_discovery_options(` | `explicit_route_with_discovery_options [function]` | `1941e30b-2603-5c59-be4f-875426a38cf2` | 320-334 [crates/gcode/src/index/indexer/pipeline.rs:320-334] | Indexed function `explicit_route_with_discovery_options` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:320-334] |
| `cleanup_skipped_file_if_indexed` | function | `pub(super) fn cleanup_skipped_file_if_indexed(` | `cleanup_skipped_file_if_indexed [function]` | `c8fd4e80-6d1c-5cf1-a1a7-5b58ec1a6548` | 336-350 [crates/gcode/src/index/indexer/pipeline.rs:336-350] | Indexed function `cleanup_skipped_file_if_indexed` in `crates/gcode/src/index/indexer/pipeline.rs`. [crates/gcode/src/index/indexer/pipeline.rs:336-350] |
