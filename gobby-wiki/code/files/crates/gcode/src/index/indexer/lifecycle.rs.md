---
title: crates/gcode/src/index/indexer/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/lifecycle.rs
  ranges:
  - 16-54
  - 56-69
  - 71-81
  - 84-121
  - 125-152
  - 154-181
  - 183-229
  - 232-235
  - 237-260
  - 262-294
  - 296-305
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer/lifecycle.rs:16-54](crates/gcode/src/index/indexer/lifecycle.rs#L16-L54), [crates/gcode/src/index/indexer/lifecycle.rs:56-69](crates/gcode/src/index/indexer/lifecycle.rs#L56-L69), [crates/gcode/src/index/indexer/lifecycle.rs:71-81](crates/gcode/src/index/indexer/lifecycle.rs#L71-L81), [crates/gcode/src/index/indexer/lifecycle.rs:84-121](crates/gcode/src/index/indexer/lifecycle.rs#L84-L121), [crates/gcode/src/index/indexer/lifecycle.rs:125-152](crates/gcode/src/index/indexer/lifecycle.rs#L125-L152), [crates/gcode/src/index/indexer/lifecycle.rs:154-181](crates/gcode/src/index/indexer/lifecycle.rs#L154-L181), [crates/gcode/src/index/indexer/lifecycle.rs:183-229](crates/gcode/src/index/indexer/lifecycle.rs#L183-L229), [crates/gcode/src/index/indexer/lifecycle.rs:232-235](crates/gcode/src/index/indexer/lifecycle.rs#L232-L235), [crates/gcode/src/index/indexer/lifecycle.rs:237-260](crates/gcode/src/index/indexer/lifecycle.rs#L237-L260), [crates/gcode/src/index/indexer/lifecycle.rs:262-294](crates/gcode/src/index/indexer/lifecycle.rs#L262-L294), [crates/gcode/src/index/indexer/lifecycle.rs:296-305](crates/gcode/src/index/indexer/lifecycle.rs#L296-L305)

</details>

# crates/gcode/src/index/indexer/lifecycle.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file implements lifecycle helpers for the indexer: it cleans up deleted-file projections, records cleanup failures as degradations, optionally attaches deferred projection sync work, and handles invalidation and daemon notification for indexed project state. It also refreshes project stats, identifies stale and orphaned files, inspects current file state, and counts rows, tying together graph, vector, and database-backed index maintenance.
[crates/gcode/src/index/indexer/lifecycle.rs:16-54]
[crates/gcode/src/index/indexer/lifecycle.rs:56-69]
[crates/gcode/src/index/indexer/lifecycle.rs:71-81]
[crates/gcode/src/index/indexer/lifecycle.rs:84-121]
[crates/gcode/src/index/indexer/lifecycle.rs:125-152]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `cleanup_deleted_file_projections` | function | `pub(super) fn cleanup_deleted_file_projections(` | `cleanup_deleted_file_projections [function]` | `27cff566-a652-5c21-906c-54247b567ec0` | 16-54 [crates/gcode/src/index/indexer/lifecycle.rs:16-54] | Indexed function `cleanup_deleted_file_projections` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:16-54] |
| `push_projection_cleanup_degradation` | function | `fn push_projection_cleanup_degradation(` | `push_projection_cleanup_degradation [function]` | `5ea81afb-c78f-589e-9c62-6ad75a49ad6b` | 56-69 [crates/gcode/src/index/indexer/lifecycle.rs:56-69] | Indexed function `push_projection_cleanup_degradation` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:56-69] |
| `attach_projection_sync` | function | `pub(super) fn attach_projection_sync(outcome: &mut IndexOutcome, request: &IndexRequest) {` | `attach_projection_sync [function]` | `9fd4f6ac-7ca7-5f00-8eda-97975a6e638f` | 71-81 [crates/gcode/src/index/indexer/lifecycle.rs:71-81] | Indexed function `attach_projection_sync` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:71-81] |
| `invalidate` | function | `pub fn invalidate(` | `invalidate [function]` | `baa7789a-c6ed-5e9d-8147-e2f915311202` | 84-121 [crates/gcode/src/index/indexer/lifecycle.rs:84-121] | Indexed function `invalidate` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:84-121] |
| `notify_daemon_invalidate` | function | `fn notify_daemon_invalidate(base_url: &str, project_id: &str) {` | `notify_daemon_invalidate [function]` | `2b812e49-5999-553b-a85d-aebd28c2e43e` | 125-152 [crates/gcode/src/index/indexer/lifecycle.rs:125-152] | Indexed function `notify_daemon_invalidate` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:125-152] |
| `refresh_project_stats` | function | `pub(super) fn refresh_project_stats(` | `refresh_project_stats [function]` | `88cf7807-7b3d-54fd-a997-c4c1cc9e39f8` | 154-181 [crates/gcode/src/index/indexer/lifecycle.rs:154-181] | Indexed function `refresh_project_stats` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:154-181] |
| `get_stale_files` | function | `pub(super) fn get_stale_files(` | `get_stale_files [function]` | `e5ef0115-76fe-5b3b-9fa4-26706f94b854` | 183-229 [crates/gcode/src/index/indexer/lifecycle.rs:183-229] | Indexed function `get_stale_files` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:183-229] |
| `CurrentFileState` | class | `pub(super) struct CurrentFileState {` | `CurrentFileState [class]` | `55465b3a-9f29-555e-a54d-a6c4e7c8b590` | 232-235 [crates/gcode/src/index/indexer/lifecycle.rs:232-235] | Indexed class `CurrentFileState` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:232-235] |
| `current_file_state` | function | `pub(super) fn current_file_state(` | `current_file_state [function]` | `9fee873c-a767-5fba-a249-877666585ef9` | 237-260 [crates/gcode/src/index/indexer/lifecycle.rs:237-260] | Indexed function `current_file_state` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:237-260] |
| `get_orphan_files` | function | `pub(super) fn get_orphan_files(` | `get_orphan_files [function]` | `38e31014-9d04-56a9-961a-fac722544e40` | 262-294 [crates/gcode/src/index/indexer/lifecycle.rs:262-294] | Indexed function `get_orphan_files` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:262-294] |
| `count_rows` | function | `fn count_rows(conn: &mut Client, table: &str, project_id: &str) -> usize {` | `count_rows [function]` | `9facb226-8885-5b36-a141-3365f419c479` | 296-305 [crates/gcode/src/index/indexer/lifecycle.rs:296-305] | Indexed function `count_rows` in `crates/gcode/src/index/indexer/lifecycle.rs`. [crates/gcode/src/index/indexer/lifecycle.rs:296-305] |
