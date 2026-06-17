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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/write.rs:47-50](crates/gcode/src/graph/code_graph/write.rs#L47-L50), [crates/gcode/src/graph/code_graph/write.rs:53-56](crates/gcode/src/graph/code_graph/write.rs#L53-L56), [crates/gcode/src/graph/code_graph/write.rs:59-61](crates/gcode/src/graph/code_graph/write.rs#L59-L61), [crates/gcode/src/graph/code_graph/write.rs:63-101](crates/gcode/src/graph/code_graph/write.rs#L63-L101), [crates/gcode/src/graph/code_graph/write.rs:103-108](crates/gcode/src/graph/code_graph/write.rs#L103-L108), [crates/gcode/src/graph/code_graph/write.rs:110-120](crates/gcode/src/graph/code_graph/write.rs#L110-L120), [crates/gcode/src/graph/code_graph/write.rs:122-138](crates/gcode/src/graph/code_graph/write.rs#L122-L138), [crates/gcode/src/graph/code_graph/write.rs:140-159](crates/gcode/src/graph/code_graph/write.rs#L140-L159), [crates/gcode/src/graph/code_graph/write.rs:161-192](crates/gcode/src/graph/code_graph/write.rs#L161-L192), [crates/gcode/src/graph/code_graph/write.rs:194-203](crates/gcode/src/graph/code_graph/write.rs#L194-L203), [crates/gcode/src/graph/code_graph/write.rs:205-214](crates/gcode/src/graph/code_graph/write.rs#L205-L214), [crates/gcode/src/graph/code_graph/write.rs:216-221](crates/gcode/src/graph/code_graph/write.rs#L216-L221), [crates/gcode/src/graph/code_graph/write.rs:223-227](crates/gcode/src/graph/code_graph/write.rs#L223-L227), [crates/gcode/src/graph/code_graph/write.rs:229-234](crates/gcode/src/graph/code_graph/write.rs#L229-L234), [crates/gcode/src/graph/code_graph/write.rs:236-258](crates/gcode/src/graph/code_graph/write.rs#L236-L258), [crates/gcode/src/graph/code_graph/write.rs:260-271](crates/gcode/src/graph/code_graph/write.rs#L260-L271), [crates/gcode/src/graph/code_graph/write.rs:273-282](crates/gcode/src/graph/code_graph/write.rs#L273-L282), [crates/gcode/src/graph/code_graph/write.rs:284-286](crates/gcode/src/graph/code_graph/write.rs#L284-L286), [crates/gcode/src/graph/code_graph/write.rs:289-294](crates/gcode/src/graph/code_graph/write.rs#L289-L294), [crates/gcode/src/graph/code_graph/write.rs:296-307](crates/gcode/src/graph/code_graph/write.rs#L296-L307), [crates/gcode/src/graph/code_graph/write.rs:309-318](crates/gcode/src/graph/code_graph/write.rs#L309-L318), [crates/gcode/src/graph/code_graph/write.rs:320-328](crates/gcode/src/graph/code_graph/write.rs#L320-L328), [crates/gcode/src/graph/code_graph/write.rs:330-334](crates/gcode/src/graph/code_graph/write.rs#L330-L334), [crates/gcode/src/graph/code_graph/write.rs:336-338](crates/gcode/src/graph/code_graph/write.rs#L336-L338), [crates/gcode/src/graph/code_graph/write.rs:340-345](crates/gcode/src/graph/code_graph/write.rs#L340-L345), [crates/gcode/src/graph/code_graph/write.rs:347-351](crates/gcode/src/graph/code_graph/write.rs#L347-L351), [crates/gcode/src/graph/code_graph/write.rs:353-376](crates/gcode/src/graph/code_graph/write.rs#L353-L376)

</details>

# crates/gcode/src/graph/code_graph/write.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Writes and maintains the code-index graph projection for a project in FalkorDB, using `CodeGraph` to sync file-derived `Code*` nodes and edges from PostgreSQL index data. The file also centralizes project/index setup, per-file graph mutation, orphan and deleted-file cleanup, and project-wide clearing, with helper functions and reexports split across the `deletion`, `mutation`, `support`, and `sync_plan` modules.
[crates/gcode/src/graph/code_graph/write.rs:47-50]
[crates/gcode/src/graph/code_graph/write.rs:53-56]
[crates/gcode/src/graph/code_graph/write.rs:59-61]
[crates/gcode/src/graph/code_graph/write.rs:63-101]
[crates/gcode/src/graph/code_graph/write.rs:103-108]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CodeGraph` | class | `pub struct CodeGraph<'a> {` | `CodeGraph [class]` | `a109fa3c-aa08-53d9-97b6-bec8732a396e` | 47-50 [crates/gcode/src/graph/code_graph/write.rs:47-50] | Indexed class `CodeGraph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:47-50] |
| `GraphOrphanCleanup` | class | `pub struct GraphOrphanCleanup {` | `GraphOrphanCleanup [class]` | `a42dac11-4842-5b29-b51e-69d6a802eb22` | 53-56 [crates/gcode/src/graph/code_graph/write.rs:53-56] | Indexed class `GraphOrphanCleanup` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:53-56] |
| `new` | function | `pub fn new(project_id: &'a str, client: &'a mut GraphClient) -> Self {` | `new [function]` | `a309a89b-2829-5b12-8717-54bb07d6915b` | 59-61 [crates/gcode/src/graph/code_graph/write.rs:59-61] | Indexed function `new` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:59-61] |
| `sync_file` | function | `pub fn sync_file(` | `sync_file [function]` | `611d801b-0921-5cc8-ac7f-9d804b1ff3c2` | 63-101 [crates/gcode/src/graph/code_graph/write.rs:63-101] | Indexed function `sync_file` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:63-101] |
| `ensure_project_indexes` | function | `pub fn ensure_project_indexes(&mut self) -> anyhow::Result<()> {` | `ensure_project_indexes [function]` | `ed4ee3be-8ccb-5439-850d-a7a74301091a` | 103-108 [crates/gcode/src/graph/code_graph/write.rs:103-108] | Indexed function `ensure_project_indexes` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:103-108] |
| `ensure_file_node` | function | `pub fn ensure_file_node(` | `ensure_file_node [function]` | `6adcdb5d-c3ba-5a78-ad41-f9cb96881c0c` | 110-120 [crates/gcode/src/graph/code_graph/write.rs:110-120] | Indexed function `ensure_file_node` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:110-120] |
| `add_imports` | function | `pub fn add_imports(` | `add_imports [function]` | `aab36050-4992-591f-92e7-e2e79ce5367a` | 122-138 [crates/gcode/src/graph/code_graph/write.rs:122-138] | Indexed function `add_imports` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:122-138] |
| `add_definitions` | function | `pub fn add_definitions(` | `add_definitions [function]` | `2bce886f-78eb-5947-861a-d9c9128d6249` | 140-159 [crates/gcode/src/graph/code_graph/write.rs:140-159] | Indexed function `add_definitions` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:140-159] |
| `add_calls` | function | `pub fn add_calls(` | `add_calls [function]` | `722ffbeb-9b3c-5d5a-adff-d5ca059b4f70` | 161-192 [crates/gcode/src/graph/code_graph/write.rs:161-192] | Indexed function `add_calls` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:161-192] |
| `delete_stale_file_graph` | function | `pub fn delete_stale_file_graph(` | `delete_stale_file_graph [function]` | `60941c19-4097-5c04-a2a3-727d62ac52ee` | 194-203 [crates/gcode/src/graph/code_graph/write.rs:194-203] | Indexed function `delete_stale_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:194-203] |
| `delete_file_graph` | function | `pub fn delete_file_graph(` | `delete_file_graph [function]` | `2c73ee74-78f9-526f-b6f1-8317a891b14c` | 205-214 [crates/gcode/src/graph/code_graph/write.rs:205-214] | Indexed function `delete_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:205-214] |
| `delete_file_node` | function | `pub fn delete_file_node(&mut self, file_path: &str) -> anyhow::Result<()> {` | `delete_file_node [function]` | `140b6784-d8e2-503e-af1a-8ce1e1cb50af` | 216-221 [crates/gcode/src/graph/code_graph/write.rs:216-221] | Indexed function `delete_file_node` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:216-221] |
| `delete_file_projection` | function | `pub fn delete_file_projection(&mut self, file_path: &str) -> anyhow::Result<()> {` | `delete_file_projection [function]` | `3bcf7942-b6d9-5515-a008-2559f5f89f45` | 223-227 [crates/gcode/src/graph/code_graph/write.rs:223-227] | Indexed function `delete_file_projection` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:223-227] |
| `cleanup_orphans` | function | `pub fn cleanup_orphans(&mut self) -> anyhow::Result<()> {` | `cleanup_orphans [function]` | `5a811e4e-2633-5631-a3c8-98c52714ebd7` | 229-234 [crates/gcode/src/graph/code_graph/write.rs:229-234] | Indexed function `cleanup_orphans` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:229-234] |
| `cleanup_deleted_files` | function | `pub fn cleanup_deleted_files(` | `cleanup_deleted_files [function]` | `6935a390-95e7-5bdd-9688-a5dc13cd2ea1` | 236-258 [crates/gcode/src/graph/code_graph/write.rs:236-258] | Indexed function `cleanup_deleted_files` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:236-258] |
| `project_file_paths` | function | `fn project_file_paths(&mut self) -> anyhow::Result<BTreeSet<String>> {` | `project_file_paths [function]` | `1f9d6b97-1bac-5988-ba86-51dd414df08a` | 260-271 [crates/gcode/src/graph/code_graph/write.rs:260-271] | Indexed function `project_file_paths` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:260-271] |
| `count_file_projection_nodes` | function | `fn count_file_projection_nodes(&mut self, file_path: &str) -> anyhow::Result<usize> {` | `count_file_projection_nodes [function]` | `7abef7d6-9982-5593-a1bc-ccd35458f6af` | 273-282 [crates/gcode/src/graph/code_graph/write.rs:273-282] | Indexed function `count_file_projection_nodes` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:273-282] |
| `clear_project` | function | `pub fn clear_project(&mut self) -> anyhow::Result<()> {` | `clear_project [function]` | `a8ec0f97-48f8-5647-8e4a-ec190bab444f` | 284-286 [crates/gcode/src/graph/code_graph/write.rs:284-286] | Indexed function `clear_project` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:284-286] |
| `value_to_usize` | function | `fn value_to_usize(value: &Value) -> Option<usize> {` | `value_to_usize [function]` | `644596c2-6215-561b-99b8-de283458d035` | 289-294 [crates/gcode/src/graph/code_graph/write.rs:289-294] | Indexed function `value_to_usize` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:289-294] |
| `sync_file_graph` | function | `pub fn sync_file_graph(` | `sync_file_graph [function]` | `1de0cc23-e279-5d38-88a0-b3899851944a` | 296-307 [crates/gcode/src/graph/code_graph/write.rs:296-307] | Indexed function `sync_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:296-307] |
| `with_code_graph` | function | `pub fn with_code_graph<T>(` | `with_code_graph [function]` | `60221519-fb12-5c2c-8ad3-84919acb4fcf` | 309-318 [crates/gcode/src/graph/code_graph/write.rs:309-318] | Indexed function `with_code_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:309-318] |
| `delete_file_graph` | function | `pub fn delete_file_graph(` | `delete_file_graph [function]` | `2966cd9b-ed49-5b76-ab6a-28affe2b73cc` | 320-328 [crates/gcode/src/graph/code_graph/write.rs:320-328] | Indexed function `delete_file_graph` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:320-328] |
| `delete_file_projection` | function | `pub fn delete_file_projection(ctx: &Context, file_path: &str) -> anyhow::Result<()> {` | `delete_file_projection [function]` | `8d341c07-d57c-567a-879a-267e1f913aeb` | 330-334 [crates/gcode/src/graph/code_graph/write.rs:330-334] | Indexed function `delete_file_projection` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:330-334] |
| `cleanup_orphans` | function | `pub fn cleanup_orphans(ctx: &Context) -> anyhow::Result<()> {` | `cleanup_orphans [function]` | `c136afbd-097c-5f63-bcbc-65ba1587dece` | 336-338 [crates/gcode/src/graph/code_graph/write.rs:336-338] | Indexed function `cleanup_orphans` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:336-338] |
| `cleanup_deleted_files` | function | `pub fn cleanup_deleted_files(` | `cleanup_deleted_files [function]` | `58f587c8-526e-515f-85fe-9f45f06fa899` | 340-345 [crates/gcode/src/graph/code_graph/write.rs:340-345] | Indexed function `cleanup_deleted_files` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:340-345] |
| `clear_project` | function | `pub fn clear_project(ctx: &Context) -> anyhow::Result<()> {` | `clear_project [function]` | `a1d50423-9318-5ad2-bd1b-4bf0d39a808a` | 347-351 [crates/gcode/src/graph/code_graph/write.rs:347-351] | Indexed function `clear_project` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:347-351] |
| `clear_all_code_index` | function | `pub fn clear_all_code_index(config: &crate::config::FalkorConfig) -> anyhow::Result<()> {` | `clear_all_code_index [function]` | `4b2d0303-7c2b-5327-a394-70d8431654db` | 353-376 [crates/gcode/src/graph/code_graph/write.rs:353-376] | Indexed function `clear_all_code_index` in `crates/gcode/src/graph/code_graph/write.rs`. [crates/gcode/src/graph/code_graph/write.rs:353-376] |
