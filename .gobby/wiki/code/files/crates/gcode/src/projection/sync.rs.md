---
title: crates/gcode/src/projection/sync.rs
type: code_file
provenance:
- file: crates/gcode/src/projection/sync.rs
  ranges:
  - 11-14
  - 17-21
  - 24-29
  - 33-37
  - 40-43
  - 46-52
  - 54-97
  - 55-63
  - 65-81
  - 83-96
  - 100-103
  - 105-112
  - 114-122
  - 124-151
  - 153-205
  - 207-235
  - 237-264
  - 266-270
  - 273-285
  - 287-296
  - 299-314
  - 316-326
  - 328-335
  - 337-348
  - 355-390
  - 358-361
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/projection/sync.rs

Module: [[code/modules/crates/gcode/src/projection|crates/gcode/src/projection]]

## Purpose

`crates/gcode/src/projection/sync.rs` exposes 26 indexed API symbols.
[crates/gcode/src/projection/sync.rs:11-14]
[crates/gcode/src/projection/sync.rs:17-21]
[crates/gcode/src/projection/sync.rs:24-29]
[crates/gcode/src/projection/sync.rs:33-37]
[crates/gcode/src/projection/sync.rs:40-43]
[crates/gcode/src/projection/sync.rs:46-52]
[crates/gcode/src/projection/sync.rs:54-97]
[crates/gcode/src/projection/sync.rs:55-63]
[crates/gcode/src/projection/sync.rs:65-81]
[crates/gcode/src/projection/sync.rs:83-96]
[crates/gcode/src/projection/sync.rs:100-103]
[crates/gcode/src/projection/sync.rs:105-112]
[crates/gcode/src/projection/sync.rs:114-122]
[crates/gcode/src/projection/sync.rs:124-151]
[crates/gcode/src/projection/sync.rs:153-205]
[crates/gcode/src/projection/sync.rs:207-235]
[crates/gcode/src/projection/sync.rs:237-264]
[crates/gcode/src/projection/sync.rs:266-270]
[crates/gcode/src/projection/sync.rs:273-285]
[crates/gcode/src/projection/sync.rs:287-296]
[crates/gcode/src/projection/sync.rs:299-314]
[crates/gcode/src/projection/sync.rs:316-326]
[crates/gcode/src/projection/sync.rs:328-335]
[crates/gcode/src/projection/sync.rs:337-348]
[crates/gcode/src/projection/sync.rs:355-390]
[crates/gcode/src/projection/sync.rs:358-361]

## API Symbols

- `ProjectionTarget` (type) component `ProjectionTarget [type]` (`0c0b8a4d-6a94-5ce6-9a69-a0a30262bbcc`) lines 11-14 [crates/gcode/src/projection/sync.rs:11-14]
  - Signature: `pub enum ProjectionTarget {`
  - Purpose: Indexed type `ProjectionTarget` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:11-14]
- `ProjectionSyncRequest` (class) component `ProjectionSyncRequest [class]` (`e5c70e76-cf95-5dbc-b40a-d82007b50bec`) lines 17-21 [crates/gcode/src/projection/sync.rs:17-21]
  - Signature: `pub struct ProjectionSyncRequest {`
  - Purpose: Indexed class `ProjectionSyncRequest` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:17-21]
- `ProjectionSyncStatus` (class) component `ProjectionSyncStatus [class]` (`b447d6c7-91c3-5840-bac3-ced3aeb159ef`) lines 24-29 [crates/gcode/src/projection/sync.rs:24-29]
  - Signature: `pub struct ProjectionSyncStatus {`
  - Purpose: Indexed class `ProjectionSyncStatus` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:24-29]
- `ProjectionStatus` (type) component `ProjectionStatus [type]` (`5a9822b7-3dd6-5b08-8f9a-28756a55b602`) lines 33-37 [crates/gcode/src/projection/sync.rs:33-37]
  - Signature: `pub enum ProjectionStatus {`
  - Purpose: Indexed type `ProjectionStatus` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:33-37]
- `ProjectionSyncError` (class) component `ProjectionSyncError [class]` (`a24abf65-d285-5c46-87e4-43436cfbc0b1`) lines 40-43 [crates/gcode/src/projection/sync.rs:40-43]
  - Signature: `pub struct ProjectionSyncError {`
  - Purpose: Indexed class `ProjectionSyncError` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:40-43]
- `ProjectionSyncReport` (class) component `ProjectionSyncReport [class]` (`a4f54b72-9fbd-5028-83a0-601dfee3566b`) lines 46-52 [crates/gcode/src/projection/sync.rs:46-52]
  - Signature: `pub struct ProjectionSyncReport {`
  - Purpose: Indexed class `ProjectionSyncReport` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:46-52]
- `ProjectionSyncReport` (class) component `ProjectionSyncReport [class]` (`c0831aee-a230-5bee-9213-b41b95d3f0df`) lines 54-97 [crates/gcode/src/projection/sync.rs:54-97]
  - Signature: `impl ProjectionSyncReport {`
  - Purpose: Indexed class `ProjectionSyncReport` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:54-97]
- `ProjectionSyncReport.ok` (method) component `ProjectionSyncReport.ok [method]` (`7de48d77-64a6-5f5f-a635-5986ca06f1ee`) lines 55-63 [crates/gcode/src/projection/sync.rs:55-63]
  - Signature: `pub fn ok(synced_files: usize, synced_symbols: usize) -> Self {`
  - Purpose: Indexed method `ProjectionSyncReport.ok` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:55-63]
- `ProjectionSyncReport.degraded` (method) component `ProjectionSyncReport.degraded [method]` (`140f6cf2-1cb9-5f69-ae66-c7c2b26a9a22`) lines 65-81 [crates/gcode/src/projection/sync.rs:65-81]
  - Signature: `pub fn degraded(`
  - Purpose: Indexed method `ProjectionSyncReport.degraded` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:65-81]
- `ProjectionSyncReport.degraded_from_error` (method) component `ProjectionSyncReport.degraded_from_error [method]` (`269b6103-252d-5ed8-b3f0-59d05722799e`) lines 83-96 [crates/gcode/src/projection/sync.rs:83-96]
  - Signature: `fn degraded_from_error(`
  - Purpose: Indexed method `ProjectionSyncReport.degraded_from_error` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:83-96]
- `ProjectionSyncReports` (class) component `ProjectionSyncReports [class]` (`dcf6732c-e15c-5b7a-9b17-86f72a875f39`) lines 100-103 [crates/gcode/src/projection/sync.rs:100-103]
  - Signature: `pub struct ProjectionSyncReports {`
  - Purpose: Indexed class `ProjectionSyncReports` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:100-103]
- `pending_after_code_fact_write` (function) component `pending_after_code_fact_write [function]` (`dc2a84bb-c770-572b-bb04-67044649fb2d`) lines 105-112 [crates/gcode/src/projection/sync.rs:105-112]
  - Signature: `pub fn pending_after_code_fact_write(request: ProjectionSyncRequest) -> ProjectionSyncStatus {`
  - Purpose: Indexed function `pending_after_code_fact_write` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:105-112]
- `sync_after_index` (function) component `sync_after_index [function]` (`1fb25c8d-88c7-5a92-be95-c601568e0423`) lines 114-122 [crates/gcode/src/projection/sync.rs:114-122]
  - Signature: `pub fn sync_after_index(`
  - Purpose: Indexed function `sync_after_index` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:114-122]
- `sync_files_with_state` (function) component `sync_files_with_state [function]` (`2bb27fdb-99c6-56aa-a764-a6d9fb95c6e0`) lines 124-151 [crates/gcode/src/projection/sync.rs:124-151]
  - Signature: `pub(crate) fn sync_files_with_state<S>(`
  - Purpose: Indexed function `sync_files_with_state` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:124-151]
- `sync_graph_files` (function) component `sync_graph_files [function]` (`ce1c9ecb-0734-5296-aedb-5d74b16b7c75`) lines 153-205 [crates/gcode/src/projection/sync.rs:153-205]
  - Signature: `fn sync_graph_files(ctx: &Context, file_paths: &[String]) -> anyhow::Result<ProjectionSyncReport> {`
  - Purpose: Indexed function `sync_graph_files` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:153-205]
- `sync_vector_files` (function) component `sync_vector_files [function]` (`e75cfd1f-f99e-5003-9de7-4ab35c4dbc1d`) lines 207-235 [crates/gcode/src/projection/sync.rs:207-235]
  - Signature: `fn sync_vector_files(ctx: &Context, file_paths: &[String]) -> anyhow::Result<ProjectionSyncReport> {`
  - Purpose: Indexed function `sync_vector_files` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:207-235]
- `sync_graph_file` (function) component `sync_graph_file [function]` (`3e668ccd-fd85-549d-b6ac-f402a11baee1`) lines 237-264 [crates/gcode/src/projection/sync.rs:237-264]
  - Signature: `fn sync_graph_file(`
  - Purpose: Indexed function `sync_graph_file` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:237-264]
- `VectorProjectionState` (class) component `VectorProjectionState [class]` (`3d58588c-b7a5-5459-bf41-e92d1ecd4f40`) lines 266-270 [crates/gcode/src/projection/sync.rs:266-270]
  - Signature: `struct VectorProjectionState<'a> {`
  - Purpose: Indexed class `VectorProjectionState` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:266-270]
- `sync_file` (function) component `sync_file [function]` (`eda0613d-0503-50c5-a592-c651b382789f`) lines 273-285 [crates/gcode/src/projection/sync.rs:273-285]
  - Signature: `fn sync_file(&mut self, file_path: &str) -> anyhow::Result<usize> {`
  - Purpose: Indexed function `sync_file` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:273-285]
- `mark_synced` (function) component `mark_synced [function]` (`1e8ab4c9-8d3d-5dbc-bfc2-6622b9957681`) lines 287-296 [crates/gcode/src/projection/sync.rs:287-296]
  - Signature: `fn mark_synced(&mut self, file_path: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `mark_synced` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:287-296]
- `vector_lifecycle_from_context` (function) component `vector_lifecycle_from_context [function]` (`46afde92-9447-539c-b7e3-462d26e8764d`) lines 299-314 [crates/gcode/src/projection/sync.rs:299-314]
  - Signature: `fn vector_lifecycle_from_context(`
  - Purpose: Indexed function `vector_lifecycle_from_context` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:299-314]
- `typed_projection_error` (function) component `typed_projection_error [function]` (`969b0bb3-d2c3-58e5-b07f-1c6092a8213b`) lines 316-326 [crates/gcode/src/projection/sync.rs:316-326]
  - Signature: `fn typed_projection_error(error: &anyhow::Error) -> ProjectionSyncError {`
  - Purpose: Indexed function `typed_projection_error` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:316-326]
- `graph_error_kind` (function) component `graph_error_kind [function]` (`0fe5ae3e-7f0f-55f6-9a41-f29b84034521`) lines 328-335 [crates/gcode/src/projection/sync.rs:328-335]
  - Signature: `fn graph_error_kind(error: &GraphReadError) -> &'static str {`
  - Purpose: Indexed function `graph_error_kind` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:328-335]
- `vector_error_kind` (function) component `vector_error_kind [function]` (`16509372-aa0a-5eae-8b43-7d21f610156c`) lines 337-348 [crates/gcode/src/projection/sync.rs:337-348]
  - Signature: `fn vector_error_kind(error: &VectorLifecycleError) -> &'static str {`
  - Purpose: Indexed function `vector_error_kind` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:337-348]
- `sync_state_tracks_projection_success` (function) component `sync_state_tracks_projection_success [function]` (`4996d22b-8002-5af6-aceb-07aff60cb48a`) lines 355-390 [crates/gcode/src/projection/sync.rs:355-390]
  - Signature: `fn sync_state_tracks_projection_success() {`
  - Purpose: Indexed function `sync_state_tracks_projection_success` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:355-390]
- `State` (class) component `State [class]` (`37690df0-453d-50e3-91cc-5d75ab647002`) lines 358-361 [crates/gcode/src/projection/sync.rs:358-361]
  - Signature: `struct State {`
  - Purpose: Indexed class `State` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:358-361]

