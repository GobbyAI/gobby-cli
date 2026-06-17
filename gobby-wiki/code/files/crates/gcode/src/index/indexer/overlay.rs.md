---
title: crates/gcode/src/index/indexer/overlay.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/overlay.rs
  ranges:
  - 33-36
  - 39-45
  - 47-83
  - 85-260
  - 262-293
  - 295-304
  - 306-326
  - 328-380
  - 382-398
  - 400-405
  - 407-412
  - 414-419
  - 421-434
  - 436-452
  - 460-467
  - 471-475
  - 479-488
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer/overlay.rs:33-36](crates/gcode/src/index/indexer/overlay.rs#L33-L36), [crates/gcode/src/index/indexer/overlay.rs:39-45](crates/gcode/src/index/indexer/overlay.rs#L39-L45), [crates/gcode/src/index/indexer/overlay.rs:47-83](crates/gcode/src/index/indexer/overlay.rs#L47-L83), [crates/gcode/src/index/indexer/overlay.rs:85-260](crates/gcode/src/index/indexer/overlay.rs#L85-L260), [crates/gcode/src/index/indexer/overlay.rs:262-293](crates/gcode/src/index/indexer/overlay.rs#L262-L293), [crates/gcode/src/index/indexer/overlay.rs:295-304](crates/gcode/src/index/indexer/overlay.rs#L295-L304), [crates/gcode/src/index/indexer/overlay.rs:306-326](crates/gcode/src/index/indexer/overlay.rs#L306-L326), [crates/gcode/src/index/indexer/overlay.rs:328-380](crates/gcode/src/index/indexer/overlay.rs#L328-L380), [crates/gcode/src/index/indexer/overlay.rs:382-398](crates/gcode/src/index/indexer/overlay.rs#L382-L398), [crates/gcode/src/index/indexer/overlay.rs:400-405](crates/gcode/src/index/indexer/overlay.rs#L400-L405), [crates/gcode/src/index/indexer/overlay.rs:407-412](crates/gcode/src/index/indexer/overlay.rs#L407-L412), [crates/gcode/src/index/indexer/overlay.rs:414-419](crates/gcode/src/index/indexer/overlay.rs#L414-L419), [crates/gcode/src/index/indexer/overlay.rs:421-434](crates/gcode/src/index/indexer/overlay.rs#L421-L434), [crates/gcode/src/index/indexer/overlay.rs:436-452](crates/gcode/src/index/indexer/overlay.rs#L436-L452), [crates/gcode/src/index/indexer/overlay.rs:460-467](crates/gcode/src/index/indexer/overlay.rs#L460-L467), [crates/gcode/src/index/indexer/overlay.rs:471-475](crates/gcode/src/index/indexer/overlay.rs#L471-L475), [crates/gcode/src/index/indexer/overlay.rs:479-488](crates/gcode/src/index/indexer/overlay.rs#L479-L488)

</details>

# crates/gcode/src/index/indexer/overlay.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file implements overlay indexing reconciliation for the code indexer: it compares the current filesystem state, parent/overlay indexed state, and git status to decide whether a file should be indexed, inherited, tombstoned, deleted from the overlay, or skipped. `index_overlay_files` drives the main workflow, while helpers like `overlay_reconcile_action`, `overlay_reconcile_candidates`, `indexed_file_states`, `paths_by_relative`, and `git_status_relative_paths` gather file state, group paths, and compute which files need updates; smaller utilities handle git status parsing, stderr compaction, timeout selection from `GCODE_GIT_STATUS_TIMEOUT_SECS`, and writing tombstones when files disappear.
[crates/gcode/src/index/indexer/overlay.rs:33-36]
[crates/gcode/src/index/indexer/overlay.rs:39-45]
[crates/gcode/src/index/indexer/overlay.rs:47-83]
[crates/gcode/src/index/indexer/overlay.rs:85-260]
[crates/gcode/src/index/indexer/overlay.rs:262-293]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `IndexedFileState` | class | `pub(super) struct IndexedFileState {` | `IndexedFileState [class]` | `92517ae0-052c-5b5c-9528-f1694dd9ea2c` | 33-36 [crates/gcode/src/index/indexer/overlay.rs:33-36] | Indexed class `IndexedFileState` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:33-36] |
| `OverlayReconcileAction` | type | `pub(super) enum OverlayReconcileAction {` | `OverlayReconcileAction [type]` | `8939e254-551c-5451-a6b8-36f6bba5bbe4` | 39-45 [crates/gcode/src/index/indexer/overlay.rs:39-45] | Indexed type `OverlayReconcileAction` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:39-45] |
| `overlay_reconcile_action` | function | `pub(super) fn overlay_reconcile_action(` | `overlay_reconcile_action [function]` | `e1ea8842-0610-5512-9bbf-57b142d8772a` | 47-83 [crates/gcode/src/index/indexer/overlay.rs:47-83] | Indexed function `overlay_reconcile_action` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:47-83] |
| `index_overlay_files` | function | `pub(super) fn index_overlay_files(` | `index_overlay_files [function]` | `dc923ce5-b5c5-51ad-88c5-7e6c1d836f0f` | 85-260 [crates/gcode/src/index/indexer/overlay.rs:85-260] | Indexed function `index_overlay_files` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:85-260] |
| `overlay_reconcile_candidates` | function | `fn overlay_reconcile_candidates(` | `overlay_reconcile_candidates [function]` | `c9fa6830-6c2e-50f5-bd2f-0a35c52abaf5` | 262-293 [crates/gcode/src/index/indexer/overlay.rs:262-293] | Indexed function `overlay_reconcile_candidates` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:262-293] |
| `paths_by_relative` | function | `fn paths_by_relative(root_path: &Path, paths: &[PathBuf]) -> HashMap<String, PathBuf> {` | `paths_by_relative [function]` | `91faf730-89fe-54ed-ab15-15c32bbde119` | 295-304 [crates/gcode/src/index/indexer/overlay.rs:295-304] | Indexed function `paths_by_relative` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:295-304] |
| `indexed_file_states` | function | `fn indexed_file_states(` | `indexed_file_states [function]` | `53cb4aab-489e-52f4-943c-2a0ebf67f329` | 306-326 [crates/gcode/src/index/indexer/overlay.rs:306-326] | Indexed function `indexed_file_states` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:306-326] |
| `git_status_relative_paths` | function | `fn git_status_relative_paths(root_path: &Path) -> anyhow::Result<HashSet<String>> {` | `git_status_relative_paths [function]` | `ff7a3eb9-5c78-58dc-a801-5f5f46d7e5ea` | 328-380 [crates/gcode/src/index/indexer/overlay.rs:328-380] | Indexed function `git_status_relative_paths` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:328-380] |
| `git_status_timeout` | function | `fn git_status_timeout() -> Duration {` | `git_status_timeout [function]` | `f6e3ab8a-16c4-5489-a23d-0fbbaed1337f` | 382-398 [crates/gcode/src/index/indexer/overlay.rs:382-398] | Indexed function `git_status_timeout` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:382-398] |
| `compact_stderr` | function | `fn compact_stderr(stderr: &[u8]) -> String {` | `compact_stderr [function]` | `68c65cc0-7742-5233-b827-67eafe6c5823` | 400-405 [crates/gcode/src/index/indexer/overlay.rs:400-405] | Indexed function `compact_stderr` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:400-405] |
| `is_porcelain_status_entry` | function | `fn is_porcelain_status_entry(entry: &[u8]) -> bool {` | `is_porcelain_status_entry [function]` | `cfe799af-3c25-5c8b-93a4-3a1e5ab7afba` | 407-412 [crates/gcode/src/index/indexer/overlay.rs:407-412] | Indexed function `is_porcelain_status_entry` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:407-412] |
| `valid_porcelain_status_byte` | function | `fn valid_porcelain_status_byte(byte: u8) -> bool {` | `valid_porcelain_status_byte [function]` | `8507a95a-1cad-5c99-ba5e-8f648256ed86` | 414-419 [crates/gcode/src/index/indexer/overlay.rs:414-419] | Indexed function `valid_porcelain_status_byte` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:414-419] |
| `rel_matches_filter` | function | `fn rel_matches_filter(root_path: &Path, path_filter: &Path, rel: &str) -> bool {` | `rel_matches_filter [function]` | `e22a0923-3cb4-5e57-92df-d5227a1c9e39` | 421-434 [crates/gcode/src/index/indexer/overlay.rs:421-434] | Indexed function `rel_matches_filter` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:421-434] |
| `write_tombstone` | function | `fn write_tombstone(conn: &mut Client, project_id: &str, rel: &str) -> anyhow::Result<()> {` | `write_tombstone [function]` | `73069262-9112-5800-87e5-515cf430fc94` | 436-452 [crates/gcode/src/index/indexer/overlay.rs:436-452] | Indexed function `write_tombstone` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:436-452] |
| `porcelain_status_byte_validation_matches_git_v1_codes` | function | `fn porcelain_status_byte_validation_matches_git_v1_codes() {` | `porcelain_status_byte_validation_matches_git_v1_codes [function]` | `f558fb83-f046-5001-951f-75f6f494d7af` | 460-467 [crates/gcode/src/index/indexer/overlay.rs:460-467] | Indexed function `porcelain_status_byte_validation_matches_git_v1_codes` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:460-467] |
| `git_status_timeout_reads_positive_env_seconds` | function | `fn git_status_timeout_reads_positive_env_seconds() {` | `git_status_timeout_reads_positive_env_seconds [function]` | `3ed01c63-fb88-5fa2-b57b-dfed7620a178` | 471-475 [crates/gcode/src/index/indexer/overlay.rs:471-475] | Indexed function `git_status_timeout_reads_positive_env_seconds` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:471-475] |
| `git_status_timeout_rejects_invalid_env_values` | function | `fn git_status_timeout_rejects_invalid_env_values() {` | `git_status_timeout_rejects_invalid_env_values [function]` | `08b3cb5c-96a6-55df-b906-5145a710de09` | 479-488 [crates/gcode/src/index/indexer/overlay.rs:479-488] | Indexed function `git_status_timeout_rejects_invalid_env_values` in `crates/gcode/src/index/indexer/overlay.rs`. [crates/gcode/src/index/indexer/overlay.rs:479-488] |
