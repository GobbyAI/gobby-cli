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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/projection/sync.rs:11-14](crates/gcode/src/projection/sync.rs#L11-L14), [crates/gcode/src/projection/sync.rs:17-21](crates/gcode/src/projection/sync.rs#L17-L21), [crates/gcode/src/projection/sync.rs:24-29](crates/gcode/src/projection/sync.rs#L24-L29), [crates/gcode/src/projection/sync.rs:33-37](crates/gcode/src/projection/sync.rs#L33-L37), [crates/gcode/src/projection/sync.rs:40-43](crates/gcode/src/projection/sync.rs#L40-L43), [crates/gcode/src/projection/sync.rs:46-52](crates/gcode/src/projection/sync.rs#L46-L52), [crates/gcode/src/projection/sync.rs:55-63](crates/gcode/src/projection/sync.rs#L55-L63), [crates/gcode/src/projection/sync.rs:65-81](crates/gcode/src/projection/sync.rs#L65-L81), [crates/gcode/src/projection/sync.rs:83-96](crates/gcode/src/projection/sync.rs#L83-L96), [crates/gcode/src/projection/sync.rs:100-103](crates/gcode/src/projection/sync.rs#L100-L103), [crates/gcode/src/projection/sync.rs:105-112](crates/gcode/src/projection/sync.rs#L105-L112), [crates/gcode/src/projection/sync.rs:114-122](crates/gcode/src/projection/sync.rs#L114-L122), [crates/gcode/src/projection/sync.rs:124-151](crates/gcode/src/projection/sync.rs#L124-L151), [crates/gcode/src/projection/sync.rs:153-205](crates/gcode/src/projection/sync.rs#L153-L205), [crates/gcode/src/projection/sync.rs:207-235](crates/gcode/src/projection/sync.rs#L207-L235), [crates/gcode/src/projection/sync.rs:237-264](crates/gcode/src/projection/sync.rs#L237-L264), [crates/gcode/src/projection/sync.rs:266-270](crates/gcode/src/projection/sync.rs#L266-L270), [crates/gcode/src/projection/sync.rs:273-285](crates/gcode/src/projection/sync.rs#L273-L285), [crates/gcode/src/projection/sync.rs:287-296](crates/gcode/src/projection/sync.rs#L287-L296), [crates/gcode/src/projection/sync.rs:299-314](crates/gcode/src/projection/sync.rs#L299-L314), [crates/gcode/src/projection/sync.rs:316-326](crates/gcode/src/projection/sync.rs#L316-L326), [crates/gcode/src/projection/sync.rs:328-335](crates/gcode/src/projection/sync.rs#L328-L335), [crates/gcode/src/projection/sync.rs:337-348](crates/gcode/src/projection/sync.rs#L337-L348), [crates/gcode/src/projection/sync.rs:355-390](crates/gcode/src/projection/sync.rs#L355-L390)

</details>

# crates/gcode/src/projection/sync.rs

Module: [[code/modules/crates/gcode/src/projection|crates/gcode/src/projection]]

## Purpose

Defines the data model and orchestration helpers for syncing a project’s projections into graph and vector views. It introduces request/status/report types and a `ProjectionStatus`/`ProjectionTarget` enum so callers can ask for specific sync targets, inspect pending work, and receive structured success, degraded, or failed results. The sync helpers then fan out across files, graph entries, and vector state, convert graph/vector-specific errors into typed projection errors, and update tracking state so completed work is marked synced and projection success is reflected in the stored state.
[crates/gcode/src/projection/sync.rs:11-14]
[crates/gcode/src/projection/sync.rs:17-21]
[crates/gcode/src/projection/sync.rs:24-29]
[crates/gcode/src/projection/sync.rs:33-37]
[crates/gcode/src/projection/sync.rs:40-43]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ProjectionTarget` | type | `pub enum ProjectionTarget {` | `ProjectionTarget [type]` | `0c0b8a4d-6a94-5ce6-9a69-a0a30262bbcc` | 11-14 [crates/gcode/src/projection/sync.rs:11-14] | Indexed type `ProjectionTarget` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:11-14] |
| `ProjectionSyncRequest` | class | `pub struct ProjectionSyncRequest {` | `ProjectionSyncRequest [class]` | `e5c70e76-cf95-5dbc-b40a-d82007b50bec` | 17-21 [crates/gcode/src/projection/sync.rs:17-21] | Indexed class `ProjectionSyncRequest` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:17-21] |
| `ProjectionSyncStatus` | class | `pub struct ProjectionSyncStatus {` | `ProjectionSyncStatus [class]` | `b447d6c7-91c3-5840-bac3-ced3aeb159ef` | 24-29 [crates/gcode/src/projection/sync.rs:24-29] | Indexed class `ProjectionSyncStatus` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:24-29] |
| `ProjectionStatus` | type | `pub enum ProjectionStatus {` | `ProjectionStatus [type]` | `5a9822b7-3dd6-5b08-8f9a-28756a55b602` | 33-37 [crates/gcode/src/projection/sync.rs:33-37] | Indexed type `ProjectionStatus` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:33-37] |
| `ProjectionSyncError` | class | `pub struct ProjectionSyncError {` | `ProjectionSyncError [class]` | `a24abf65-d285-5c46-87e4-43436cfbc0b1` | 40-43 [crates/gcode/src/projection/sync.rs:40-43] | Indexed class `ProjectionSyncError` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:40-43] |
| `ProjectionSyncReport` | class | `pub struct ProjectionSyncReport {` | `ProjectionSyncReport [class]` | `a4f54b72-9fbd-5028-83a0-601dfee3566b` | 46-52 [crates/gcode/src/projection/sync.rs:46-52] | Indexed class `ProjectionSyncReport` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:46-52] |
| `ProjectionSyncReport::ok` | method | `pub fn ok(synced_files: usize, synced_symbols: usize) -> Self {` | `ProjectionSyncReport::ok [method]` | `7de48d77-64a6-5f5f-a635-5986ca06f1ee` | 55-63 [crates/gcode/src/projection/sync.rs:55-63] | Indexed method `ProjectionSyncReport::ok` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:55-63] |
| `ProjectionSyncReport::degraded` | method | `pub fn degraded(` | `ProjectionSyncReport::degraded [method]` | `140f6cf2-1cb9-5f69-ae66-c7c2b26a9a22` | 65-81 [crates/gcode/src/projection/sync.rs:65-81] | Indexed method `ProjectionSyncReport::degraded` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:65-81] |
| `ProjectionSyncReport::degraded_from_error` | method | `fn degraded_from_error(` | `ProjectionSyncReport::degraded_from_error [method]` | `269b6103-252d-5ed8-b3f0-59d05722799e` | 83-96 [crates/gcode/src/projection/sync.rs:83-96] | Indexed method `ProjectionSyncReport::degraded_from_error` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:83-96] |
| `ProjectionSyncReports` | class | `pub struct ProjectionSyncReports {` | `ProjectionSyncReports [class]` | `dcf6732c-e15c-5b7a-9b17-86f72a875f39` | 100-103 [crates/gcode/src/projection/sync.rs:100-103] | Indexed class `ProjectionSyncReports` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:100-103] |
| `pending_after_code_fact_write` | function | `pub fn pending_after_code_fact_write(request: ProjectionSyncRequest) -> ProjectionSyncStatus {` | `pending_after_code_fact_write [function]` | `dc2a84bb-c770-572b-bb04-67044649fb2d` | 105-112 [crates/gcode/src/projection/sync.rs:105-112] | Indexed function `pending_after_code_fact_write` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:105-112] |
| `sync_after_index` | function | `pub fn sync_after_index(` | `sync_after_index [function]` | `1fb25c8d-88c7-5a92-be95-c601568e0423` | 114-122 [crates/gcode/src/projection/sync.rs:114-122] | Indexed function `sync_after_index` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:114-122] |
| `sync_files_with_state` | function | `pub(crate) fn sync_files_with_state<S>(` | `sync_files_with_state [function]` | `2bb27fdb-99c6-56aa-a764-a6d9fb95c6e0` | 124-151 [crates/gcode/src/projection/sync.rs:124-151] | Indexed function `sync_files_with_state` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:124-151] |
| `sync_graph_files` | function | `fn sync_graph_files(ctx: &Context, file_paths: &[String]) -> anyhow::Result<ProjectionSyncReport> {` | `sync_graph_files [function]` | `ce1c9ecb-0734-5296-aedb-5d74b16b7c75` | 153-205 [crates/gcode/src/projection/sync.rs:153-205] | Indexed function `sync_graph_files` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:153-205] |
| `sync_vector_files` | function | `fn sync_vector_files(ctx: &Context, file_paths: &[String]) -> anyhow::Result<ProjectionSyncReport> {` | `sync_vector_files [function]` | `e75cfd1f-f99e-5003-9de7-4ab35c4dbc1d` | 207-235 [crates/gcode/src/projection/sync.rs:207-235] | Indexed function `sync_vector_files` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:207-235] |
| `sync_graph_file` | function | `fn sync_graph_file(` | `sync_graph_file [function]` | `3e668ccd-fd85-549d-b6ac-f402a11baee1` | 237-264 [crates/gcode/src/projection/sync.rs:237-264] | Indexed function `sync_graph_file` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:237-264] |
| `VectorProjectionState` | class | `struct VectorProjectionState<'a> {` | `VectorProjectionState [class]` | `3d58588c-b7a5-5459-bf41-e92d1ecd4f40` | 266-270 [crates/gcode/src/projection/sync.rs:266-270] | Indexed class `VectorProjectionState` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:266-270] |
| `sync_file` | function | `fn sync_file(&mut self, file_path: &str) -> anyhow::Result<usize> {` | `sync_file [function]` | `eda0613d-0503-50c5-a592-c651b382789f` | 273-285 [crates/gcode/src/projection/sync.rs:273-285] | Indexed function `sync_file` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:273-285] |
| `mark_synced` | function | `fn mark_synced(&mut self, file_path: &str) -> anyhow::Result<()> {` | `mark_synced [function]` | `1e8ab4c9-8d3d-5dbc-bfc2-6622b9957681` | 287-296 [crates/gcode/src/projection/sync.rs:287-296] | Indexed function `mark_synced` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:287-296] |
| `vector_lifecycle_from_context` | function | `fn vector_lifecycle_from_context(` | `vector_lifecycle_from_context [function]` | `46afde92-9447-539c-b7e3-462d26e8764d` | 299-314 [crates/gcode/src/projection/sync.rs:299-314] | Indexed function `vector_lifecycle_from_context` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:299-314] |
| `typed_projection_error` | function | `fn typed_projection_error(error: &anyhow::Error) -> ProjectionSyncError {` | `typed_projection_error [function]` | `969b0bb3-d2c3-58e5-b07f-1c6092a8213b` | 316-326 [crates/gcode/src/projection/sync.rs:316-326] | Indexed function `typed_projection_error` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:316-326] |
| `graph_error_kind` | function | `fn graph_error_kind(error: &GraphReadError) -> &'static str {` | `graph_error_kind [function]` | `0fe5ae3e-7f0f-55f6-9a41-f29b84034521` | 328-335 [crates/gcode/src/projection/sync.rs:328-335] | Indexed function `graph_error_kind` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:328-335] |
| `vector_error_kind` | function | `fn vector_error_kind(error: &VectorLifecycleError) -> &'static str {` | `vector_error_kind [function]` | `16509372-aa0a-5eae-8b43-7d21f610156c` | 337-348 [crates/gcode/src/projection/sync.rs:337-348] | Indexed function `vector_error_kind` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:337-348] |
| `sync_state_tracks_projection_success` | function | `fn sync_state_tracks_projection_success() {` | `sync_state_tracks_projection_success [function]` | `4996d22b-8002-5af6-aceb-07aff60cb48a` | 355-390 [crates/gcode/src/projection/sync.rs:355-390] | Indexed function `sync_state_tracks_projection_success` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:355-390] |
| `State` | class | `struct State {` | `State [class]` | `37690df0-453d-50e3-91cc-5d75ab647002` | 358-361 [crates/gcode/src/projection/sync.rs:358-361] | Indexed class `State` in `crates/gcode/src/projection/sync.rs`. [crates/gcode/src/projection/sync.rs:358-361] |
