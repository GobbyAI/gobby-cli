---
title: crates/gcode/src/projection
type: code_module
provenance:
- file: crates/gcode/src/projection/mod.rs
  ranges:
  - 1-2
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

- [crates/gcode/src/projection/mod.rs:1-2](crates/gcode/src/projection/mod.rs#L1-L2)
- [crates/gcode/src/projection/sync.rs:11-14](crates/gcode/src/projection/sync.rs#L11-L14), [crates/gcode/src/projection/sync.rs:17-21](crates/gcode/src/projection/sync.rs#L17-L21), [crates/gcode/src/projection/sync.rs:24-29](crates/gcode/src/projection/sync.rs#L24-L29), [crates/gcode/src/projection/sync.rs:33-37](crates/gcode/src/projection/sync.rs#L33-L37), [crates/gcode/src/projection/sync.rs:40-43](crates/gcode/src/projection/sync.rs#L40-L43), [crates/gcode/src/projection/sync.rs:46-52](crates/gcode/src/projection/sync.rs#L46-L52), [crates/gcode/src/projection/sync.rs:55-63](crates/gcode/src/projection/sync.rs#L55-L63), [crates/gcode/src/projection/sync.rs:65-81](crates/gcode/src/projection/sync.rs#L65-L81), [crates/gcode/src/projection/sync.rs:83-96](crates/gcode/src/projection/sync.rs#L83-L96), [crates/gcode/src/projection/sync.rs:100-103](crates/gcode/src/projection/sync.rs#L100-L103), [crates/gcode/src/projection/sync.rs:105-112](crates/gcode/src/projection/sync.rs#L105-L112), [crates/gcode/src/projection/sync.rs:114-122](crates/gcode/src/projection/sync.rs#L114-L122), [crates/gcode/src/projection/sync.rs:124-151](crates/gcode/src/projection/sync.rs#L124-L151), [crates/gcode/src/projection/sync.rs:153-205](crates/gcode/src/projection/sync.rs#L153-L205), [crates/gcode/src/projection/sync.rs:207-235](crates/gcode/src/projection/sync.rs#L207-L235), [crates/gcode/src/projection/sync.rs:237-264](crates/gcode/src/projection/sync.rs#L237-L264), [crates/gcode/src/projection/sync.rs:266-270](crates/gcode/src/projection/sync.rs#L266-L270), [crates/gcode/src/projection/sync.rs:273-285](crates/gcode/src/projection/sync.rs#L273-L285), [crates/gcode/src/projection/sync.rs:287-296](crates/gcode/src/projection/sync.rs#L287-L296), [crates/gcode/src/projection/sync.rs:299-314](crates/gcode/src/projection/sync.rs#L299-L314), [crates/gcode/src/projection/sync.rs:316-326](crates/gcode/src/projection/sync.rs#L316-L326), [crates/gcode/src/projection/sync.rs:328-335](crates/gcode/src/projection/sync.rs#L328-L335), [crates/gcode/src/projection/sync.rs:337-348](crates/gcode/src/projection/sync.rs#L337-L348), [crates/gcode/src/projection/sync.rs:355-390](crates/gcode/src/projection/sync.rs#L355-L390)

</details>

# crates/gcode/src/projection

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `projection` module is responsible for orchestrating the synchronization of a project's projections into distinct graph and vector views [crates/gcode/src/projection/mod.rs:1-2, crates/gcode/src/projection/sync.rs:11-14]. Through the `sync` submodule, the module defines a comprehensive data model and helper functions to track pending projection changes, manage sync requests, and handle synchronization outcomes [crates/gcode/src/projection/sync.rs:11-14, crates/gcode/src/projection/sync.rs:17-21, crates/gcode/src/projection/sync.rs:24-29]. Key execution flows trigger synchronization across files, graph entries, and vector states, transforming database or storage facts into indexed representations [crates/gcode/src/projection/sync.rs:11-14]. It safely handles failures by converting underlying graph or vector engine errors into typed projection errors, ensuring tracking state is updated and projection success is accurately reflected in the stored state [crates/gcode/src/projection/sync.rs:11-14].

This module collaborates closely with configuration contexts (`Context`), database engines, graph stores, and vector stores to process sync requests and map project definitions . Callers specify targets using the `ProjectionTarget` enum and monitor status with `ProjectionSyncStatus` [crates/gcode/src/projection/sync.rs:11-14, crates/gcode/src/projection/sync.rs:17-21]. Tracking functions like `mark_synced` and state components like `VectorProjectionState` ensure that ongoing progress is properly recorded and that overall projection success is reflected in the stored state [crates/gcode/src/projection/sync.rs:11-14].

| Symbol / Type | Category | Description | Citation |
| --- | --- | --- | --- |
| `ProjectionTarget` | Enum | Specifies the sync target: either `Graph` or `Vectors` | [crates/gcode/src/projection/sync.rs:11-14] |
| `ProjectionSyncRequest` | Struct | Captures the project identifier, target paths, and sync destinations | [crates/gcode/src/projection/sync.rs:17-21] |
| `ProjectionSyncStatus` | Struct | Describes sync pending state for graph and vector targets | [crates/gcode/src/projection/sync.rs:24-29] |
| `ProjectionStatus` | Enum | Denotes the result of a projection execution (`Ok`, `Degraded`, or `Failed`) | [crates/gcode/src/projection/sync.rs:33-37] |
| `ProjectionSyncError` | Struct | Details a typed projection synchronization error kind and message | [crates/gcode/src/projection/sync.rs:40-43] |
| `ProjectionSyncReport` | Struct | Summarizes execution metrics including synced file/symbol counts and statuses | [crates/gcode/src/projection/sync.rs:11-14] |
| `VectorProjectionState` | Class / Struct | Tracks the projection state of vector indices | [crates/gcode/src/projection/sync.rs:11-14] |
| `State` | Class / Struct | Represents state storage for projection workflows | [crates/gcode/src/projection/sync.rs:11-14] |

| Core Synchronization Functions | Description | Citation |
| --- | --- | --- |
| `pending_after_code_fact_write` | Detects pending projection work after a code fact is written | [crates/gcode/src/projection/sync.rs:11-14] |
| `sync_after_index` | Drives synchronization tasks once indexing completes | [crates/gcode/src/projection/sync.rs:11-14] |
| `sync_files_with_state` | Synchronizes files and updates their stored tracking status | [crates/gcode/src/projection/sync.rs:11-14] |
| `sync_graph_files` / `sync_graph_file` | Coordinates fanning out projections to the code graph | [crates/gcode/src/projection/sync.rs:11-14] |
| `sync_vector_files` | Directs the generation and persistence of vector views | [crates/gcode/src/projection/sync.rs:11-14] |
| `sync_file` | Drives sync for a single file's projections | [crates/gcode/src/projection/sync.rs:11-14] |
| `mark_synced` | Marks completed work as successfully synced | [crates/gcode/src/projection/sync.rs:11-14] |
| `vector_lifecycle_from_context` | Resolves the vector lifecycle helper from context | [crates/gcode/src/projection/sync.rs:11-14] |
| `typed_projection_error` | Converts raw errors into structured projection sync errors | [crates/gcode/src/projection/sync.rs:11-14] |
| `graph_error_kind` / `vector_error_kind` | Resolves target-specific error kinds | [crates/gcode/src/projection/sync.rs:11-14] |
| `sync_state_tracks_projection_success` | Validates and stores successful projection states | [crates/gcode/src/projection/sync.rs:11-14] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/projection/mod.rs\|crates/gcode/src/projection/mod.rs]] | Defines the `projection` module and re-exports its `sync` submodule, which likely contains synchronization-related projection logic for the GCode crate. [crates/gcode/src/projection/mod.rs:1-2] |
| [[code/files/crates/gcode/src/projection/sync.rs\|crates/gcode/src/projection/sync.rs]] | Defines the data model and orchestration helpers for syncing a project’s projections into graph and vector views. It introduces request/status/report types and a `ProjectionStatus`/`ProjectionTarget` enum so callers can ask for specific sync targets, inspect pending work, and receive structured success, degraded, or failed results. The sync helpers then fan out across files, graph entries, and vector state, convert graph/vector-specific errors into typed projection errors, and update tracking state so completed work is marked synced and projection success is reflected in the stored state. [crates/gcode/src/projection/sync.rs:11-14] [crates/gcode/src/projection/sync.rs:17-21] [crates/gcode/src/projection/sync.rs:24-29] [crates/gcode/src/projection/sync.rs:33-37] [crates/gcode/src/projection/sync.rs:40-43] |

## Components

| Component ID |
| --- |
| `0c0b8a4d-6a94-5ce6-9a69-a0a30262bbcc` |
| `e5c70e76-cf95-5dbc-b40a-d82007b50bec` |
| `b447d6c7-91c3-5840-bac3-ced3aeb159ef` |
| `5a9822b7-3dd6-5b08-8f9a-28756a55b602` |
| `a24abf65-d285-5c46-87e4-43436cfbc0b1` |
| `a4f54b72-9fbd-5028-83a0-601dfee3566b` |
| `7de48d77-64a6-5f5f-a635-5986ca06f1ee` |
| `140f6cf2-1cb9-5f69-ae66-c7c2b26a9a22` |
| `269b6103-252d-5ed8-b3f0-59d05722799e` |
| `dcf6732c-e15c-5b7a-9b17-86f72a875f39` |
| `dc2a84bb-c770-572b-bb04-67044649fb2d` |
| `1fb25c8d-88c7-5a92-be95-c601568e0423` |
| `2bb27fdb-99c6-56aa-a764-a6d9fb95c6e0` |
| `ce1c9ecb-0734-5296-aedb-5d74b16b7c75` |
| `e75cfd1f-f99e-5003-9de7-4ab35c4dbc1d` |
| `3e668ccd-fd85-549d-b6ac-f402a11baee1` |
| `3d58588c-b7a5-5459-bf41-e92d1ecd4f40` |
| `eda0613d-0503-50c5-a592-c651b382789f` |
| `1e8ab4c9-8d3d-5dbc-bfc2-6622b9957681` |
| `46afde92-9447-539c-b7e3-462d26e8764d` |
| `969b0bb3-d2c3-58e5-b07f-1c6092a8213b` |
| `0fe5ae3e-7f0f-55f6-9a41-f29b84034521` |
| `16509372-aa0a-5eae-8b43-7d21f610156c` |
| `4996d22b-8002-5af6-aceb-07aff60cb48a` |
| `37690df0-453d-50e3-91cc-5d75ab647002` |
