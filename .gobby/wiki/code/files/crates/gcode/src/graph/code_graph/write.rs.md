---
title: crates/gcode/src/graph/code_graph/write.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write.rs
  ranges:
  - 47-50
  - 53-56
  - 59-61
  - 63-101
  - 103-108
  - 110-120
  - 122-138
  - 140-159
  - 161-192
  - 194-203
  - 205-214
  - 216-221
  - 223-227
  - 229-234
  - 236-258
  - 260-271
  - 273-282
  - 284-286
  - 289-294
  - 296-307
  - 309-318
  - 320-328
  - 330-334
  - 336-338
  - 340-345
  - 347-351
  - 353-376
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

This file implements the write path for the code-index graph projection owned by `gcode`: it wraps a project-scoped `GraphClient` in `CodeGraph` and provides methods to sync file-level imports, symbol definitions, and call relations into FalkorDB, using per-file sync tokens and batched writes to keep the graph aligned with PostgreSQL-derived index data.

Its pieces work together around that sync flow: `ensure_project_indexes` and `ensure_file_node` prepare graph state, `add_imports`, `add_definitions`, and `add_calls` write the per-file relationship groups, `sync_file` coordinates the full update and optional orphan cleanup, and the deletion/cleanup helpers support stale-file removal, project clearing, projection node counting, and whole-project reset operations.
[crates/gcode/src/graph/code_graph/write.rs:47-50]
[crates/gcode/src/graph/code_graph/write.rs:53-56]
[crates/gcode/src/graph/code_graph/write.rs:59-61]
[crates/gcode/src/graph/code_graph/write.rs:63-101]
[crates/gcode/src/graph/code_graph/write.rs:103-108]

## API Symbols

- `CodeGraph` (class) component `CodeGraph [class]` (`a109fa3c-aa08-53d9-97b6-bec8732a396e`) lines 47-50 [crates/gcode/src/graph/code_graph/write.rs:47-50]
  - Signature: `pub struct CodeGraph<'a> {`
  - Purpose: 'CodeGraph<'a>' is a borrowed wrapper over a 'project_id' string slice and a mutable 'GraphClient' reference, likely used to operate on a specific project's code graph through the client. [crates/gcode/src/graph/code_graph/write.rs:47-50]
- `GraphOrphanCleanup` (class) component `GraphOrphanCleanup [class]` (`a42dac11-4842-5b29-b51e-69d6a802eb22`) lines 53-56 [crates/gcode/src/graph/code_graph/write.rs:53-56]
  - Signature: `pub struct GraphOrphanCleanup {`
  - Purpose: 'GraphOrphanCleanup' is a struct that records cleanup results by counting how many stale files were deleted and how many graph nodes were deleted. [crates/gcode/src/graph/code_graph/write.rs:53-56]
- `new` (function) component `new [function]` (`a309a89b-2829-5b12-8717-54bb07d6915b`) lines 59-61 [crates/gcode/src/graph/code_graph/write.rs:59-61]
  - Signature: `pub fn new(project_id: &'a str, client: &'a mut GraphClient) -> Self {`
  - Purpose: Constructs and returns a new instance by storing the provided 'project_id' string slice and mutable 'GraphClient' reference in the struct. [crates/gcode/src/graph/code_graph/write.rs:59-61]
- `sync_file` (function) component `sync_file [function]` (`611d801b-0921-5cc8-ac7f-9d804b1ff3c2`) lines 63-101 [crates/gcode/src/graph/code_graph/write.rs:63-101]
  - Signature: `pub fn sync_file(`
  - Purpose: Synchronizes a file’s import, symbol, and call graph data into the backing database in bounded write batches, deletes stale rows using a per-file sync token, optionally cleans up orphaned graph records, and returns the total number of relationships processed. [crates/gcode/src/graph/code_graph/write.rs:63-101]
- `ensure_project_indexes` (function) component `ensure_project_indexes [function]` (`ed4ee3be-8ccb-5439-850d-a7a74301091a`) lines 103-108 [crates/gcode/src/graph/code_graph/write.rs:103-108]
  - Signature: `pub fn ensure_project_indexes(&mut self) -> anyhow::Result<()> {`
  - Purpose: Iterates over 'PROJECT_INDEXED_LABELS' and calls 'self.client.ensure_exact_node_index(label, "project")' for each label, returning any error encountered. [crates/gcode/src/graph/code_graph/write.rs:103-108]
- `ensure_file_node` (function) component `ensure_file_node [function]` (`6adcdb5d-c3ba-5a78-ad41-f9cb96881c0c`) lines 110-120 [crates/gcode/src/graph/code_graph/write.rs:110-120]
  - Signature: `pub fn ensure_file_node(`
  - Purpose: Executes a write query that ensures a file node exists or is updated for the given 'file_path' with the provided 'symbol_count' and 'sync_token' in the current project, returning any query execution error as 'anyhow::Result<()>'. [crates/gcode/src/graph/code_graph/write.rs:110-120]
- `add_imports` (function) component `add_imports [function]` (`aab36050-4992-591f-92e7-e2e79ce5367a`) lines 122-138 [crates/gcode/src/graph/code_graph/write.rs:122-138]
  - Signature: `pub fn add_imports(`
  - Purpose: Builds the import-graph items for a file, returns 'Ok(0)' if none exist, otherwise writes them to the database with a sync token and returns the number of imported items. [crates/gcode/src/graph/code_graph/write.rs:122-138]
- `add_definitions` (function) component `add_definitions [function]` (`2bce886f-78eb-5947-861a-d9c9128d6249`) lines 140-159 [crates/gcode/src/graph/code_graph/write.rs:140-159]
  - Signature: `pub fn add_definitions(`
  - Purpose: Filters the provided 'Symbol' definitions to those with non-empty 'id' and 'name', writes them to the database via 'add_definitions_query' using 'file_path' and 'sync_token', and returns the number of valid definitions written (or '0' if none). [crates/gcode/src/graph/code_graph/write.rs:140-159]
- `add_calls` (function) component `add_calls [function]` (`722ffbeb-9b3c-5d5a-adff-d5ca059b4f70`) lines 161-192 [crates/gcode/src/graph/code_graph/write.rs:161-192]
  - Signature: `pub fn add_calls(`
  - Purpose: Partitions the provided 'CallRelation' slice for a file into symbol, external, and unresolved groups, writes each non-empty group to the database with the given 'sync_token', and returns the total number of call records written. [crates/gcode/src/graph/code_graph/write.rs:161-192]
- `delete_stale_file_graph` (function) component `delete_stale_file_graph [function]` (`60941c19-4097-5c04-a2a3-727d62ac52ee`) lines 194-203 [crates/gcode/src/graph/code_graph/write.rs:194-203]
  - Signature: `pub fn delete_stale_file_graph(`
  - Purpose: Indexed function `delete_stale_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:194-203]
- `delete_file_graph` (function) component `delete_file_graph [function]` (`2c73ee74-78f9-526f-b6f1-8317a891b14c`) lines 205-214 [crates/gcode/src/graph/code_graph/write.rs:205-214]
  - Signature: `pub fn delete_file_graph(`
  - Purpose: Indexed function `delete_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:205-214]
- `delete_file_node` (function) component `delete_file_node [function]` (`140b6784-d8e2-503e-af1a-8ce1e1cb50af`) lines 216-221 [crates/gcode/src/graph/code_graph/write.rs:216-221]
  - Signature: `pub fn delete_file_node(&mut self, file_path: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `delete_file_node` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:216-221]
- `delete_file_projection` (function) component `delete_file_projection [function]` (`3bcf7942-b6d9-5515-a008-2559f5f89f45`) lines 223-227 [crates/gcode/src/graph/code_graph/write.rs:223-227]
  - Signature: `pub fn delete_file_projection(&mut self, file_path: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `delete_file_projection` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:223-227]
- `cleanup_orphans` (function) component `cleanup_orphans [function]` (`5a811e4e-2633-5631-a3c8-98c52714ebd7`) lines 229-234 [crates/gcode/src/graph/code_graph/write.rs:229-234]
  - Signature: `pub fn cleanup_orphans(&mut self) -> anyhow::Result<()> {`
  - Purpose: Indexed function `cleanup_orphans` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:229-234]
- `cleanup_deleted_files` (function) component `cleanup_deleted_files [function]` (`6935a390-95e7-5bdd-9688-a5dc13cd2ea1`) lines 236-258 [crates/gcode/src/graph/code_graph/write.rs:236-258]
  - Signature: `pub fn cleanup_deleted_files(`
  - Purpose: Indexed function `cleanup_deleted_files` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:236-258]
- `project_file_paths` (function) component `project_file_paths [function]` (`1f9d6b97-1bac-5988-ba86-51dd414df08a`) lines 260-271 [crates/gcode/src/graph/code_graph/write.rs:260-271]
  - Signature: `fn project_file_paths(&mut self) -> anyhow::Result<BTreeSet<String>> {`
  - Purpose: Executes each query returned by 'project_file_path_queries(self.project_id)', extracts any string 'path' values from the returned rows via 'self.client.query(...)', deduplicates them in a 'BTreeSet<String>', and returns the set. [crates/gcode/src/graph/code_graph/write.rs:260-271]
- `count_file_projection_nodes` (function) component `count_file_projection_nodes [function]` (`7abef7d6-9982-5593-a1bc-ccd35458f6af`) lines 273-282 [crates/gcode/src/graph/code_graph/write.rs:273-282]
  - Signature: `fn count_file_projection_nodes(&mut self, file_path: &str) -> anyhow::Result<usize> {`
  - Purpose: Builds a typed Cypher query for the given 'file_path' and current 'project_id', executes it against the graph client, and returns the first row’s '"nodes"' value as a 'usize' count, defaulting to '0' if absent or unparseable. [crates/gcode/src/graph/code_graph/write.rs:273-282]
- `clear_project` (function) component `clear_project [function]` (`a8ec0f97-48f8-5647-8e4a-ec190bab444f`) lines 284-286 [crates/gcode/src/graph/code_graph/write.rs:284-286]
  - Signature: `pub fn clear_project(&mut self) -> anyhow::Result<()> {`
  - Purpose: Indexed function `clear_project` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:284-286]
- `value_to_usize` (function) component `value_to_usize [function]` (`644596c2-6215-561b-99b8-de283458d035`) lines 289-294 [crates/gcode/src/graph/code_graph/write.rs:289-294]
  - Signature: `fn value_to_usize(value: &Value) -> Option<usize> {`
  - Purpose: Returns 'Some(usize)' when the 'Value' can be losslessly converted from either a 'u64' or a nonnegative 'i64' within 'usize' range, otherwise returns 'None'. [crates/gcode/src/graph/code_graph/write.rs:289-294]
- `sync_file_graph` (function) component `sync_file_graph [function]` (`1de0cc23-e279-5d38-88a0-b3899851944a`) lines 296-307 [crates/gcode/src/graph/code_graph/write.rs:296-307]
  - Signature: `pub fn sync_file_graph(`
  - Purpose: 'sync_file_graph' acquires the code graph from 'ctx' and delegates to 'graph.sync_file' to synchronize the specified file’s imports, definitions, and call relations, optionally cleaning up orphaned nodes, returning the resulting 'usize' count or an error. [crates/gcode/src/graph/code_graph/write.rs:296-307]
- `with_code_graph` (function) component `with_code_graph [function]` (`60221519-fb12-5c2c-8ad3-84919acb4fcf`) lines 309-318 [crates/gcode/src/graph/code_graph/write.rs:309-318]
  - Signature: `pub fn with_code_graph<T>(`
  - Purpose: Indexed function `with_code_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:309-318]
- `delete_file_graph` (function) component `delete_file_graph [function]` (`2966cd9b-ed49-5b76-ab6a-28affe2b73cc`) lines 320-328 [crates/gcode/src/graph/code_graph/write.rs:320-328]
  - Signature: `pub fn delete_file_graph(`
  - Purpose: Indexed function `delete_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:320-328]
- `delete_file_projection` (function) component `delete_file_projection [function]` (`8d341c07-d57c-567a-879a-267e1f913aeb`) lines 330-334 [crates/gcode/src/graph/code_graph/write.rs:330-334]
  - Signature: `pub fn delete_file_projection(ctx: &Context, file_path: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `delete_file_projection` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:330-334]
- `cleanup_orphans` (function) component `cleanup_orphans [function]` (`c136afbd-097c-5f63-bcbc-65ba1587dece`) lines 336-338 [crates/gcode/src/graph/code_graph/write.rs:336-338]
  - Signature: `pub fn cleanup_orphans(ctx: &Context) -> anyhow::Result<()> {`
  - Purpose: Indexed function `cleanup_orphans` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:336-338]
- `cleanup_deleted_files` (function) component `cleanup_deleted_files [function]` (`58f587c8-526e-515f-85fe-9f45f06fa899`) lines 340-345 [crates/gcode/src/graph/code_graph/write.rs:340-345]
  - Signature: `pub fn cleanup_deleted_files(`
  - Purpose: Indexed function `cleanup_deleted_files` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:340-345]
- `clear_project` (function) component `clear_project [function]` (`a1d50423-9318-5ad2-bd1b-4bf0d39a808a`) lines 347-351 [crates/gcode/src/graph/code_graph/write.rs:347-351]
  - Signature: `pub fn clear_project(ctx: &Context) -> anyhow::Result<()> {`
  - Purpose: Indexed function `clear_project` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:347-351]
- `clear_all_code_index` (function) component `clear_all_code_index [function]` (`4b2d0303-7c2b-5327-a394-70d8431654db`) lines 353-376 [crates/gcode/src/graph/code_graph/write.rs:353-376]
  - Signature: `pub fn clear_all_code_index(config: &crate::config::FalkorConfig) -> anyhow::Result<()> {`
  - Purpose: Indexed function `clear_all_code_index` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:353-376]

