---
title: crates/gcode/src/index/indexer
type: code_module
provenance:
- file: crates/gcode/src/index/indexer/file.rs
- file: crates/gcode/src/index/indexer/freshness_probe.rs
- file: crates/gcode/src/index/indexer/lifecycle.rs
- file: crates/gcode/src/index/indexer/local_imports.rs
- file: crates/gcode/src/index/indexer/overlay.rs
- file: crates/gcode/src/index/indexer/pipeline.rs
- file: crates/gcode/src/index/indexer/sink.rs
- file: crates/gcode/src/index/indexer/tests.rs
- file: crates/gcode/src/index/indexer/types.rs
- file: crates/gcode/src/index/indexer/util.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer

Parent: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

The `crates/gcode/src/index/indexer` module owns project indexing from discovery through persistence: it indexes individual files, handles content-only fallback, reconciles overlay indexes, probes freshness, resolves local imports, cleans stale projections, and writes facts through a sink abstraction. `index_file` is the core single-file flow: it derives a relative path, parses with semantic resolution, detects language, hashes content, reads metadata, then writes transactional facts through `PostgresCodeFactSink` (`crates/gcode/src/index/indexer/file.rs:1-100`).

At the project level, freshness checks avoid unnecessary work. `project_changed_since` is explicitly a lock-free, hash-free pre-gate that checks mtimes for added/modified files and existence for deleted indexed paths before falling through to the locked incremental reconcile path (`crates/gcode/src/index/indexer/freshness_probe.rs:1-100`). Overlay indexing then compares parent, overlay, disk state, hashes, and indexability to choose `Index`, `Inherit`, `Tombstone`, `DeleteOverlay`, or `Skip`; deleted files can become tombstones when inherited from a parent, while unchanged parent hashes can inherit or skip (`crates/gcode/src/index/indexer/overlay.rs:1-100`).

The module collaborates heavily with the wider indexing stack. It imports configuration scope, database access, API helpers, hashing, parsing, walking, visibility, and indexed-file models from sibling crate areas, then calls back into its own submodules for file indexing, lifecycle cleanup/stat refresh, local import resolution, fact sinks, shared types, and path/unsupported-file utilities (`crates/gcode/src/index/indexer/overlay.rs:1-100`). Utility code keeps discovery behavior consistent with the legacy Python defaults via `DEFAULT_EXCLUDES`, filters discovered paths lexically before optional canonical fallback, and groups unsupported file extensions with bounded examples (`crates/gcode/src/index/indexer/util.rs:1-100`).

| Public surface | Role |
| --- | --- |
| `index_files`, `index_files_with_connection`, `index_discovered_files`, `index_explicit_files_with_connection` | Project/file-set indexing entry points |
| `index_file`, `index_content_only` | Per-file AST or content-only indexing |
| `project_changed_since` | Fast freshness pre-gate before full reconcile |
| `overlay_reconcile_action`, `index_overlay_files` | Overlay state reconciliation and indexing |
| `resolve_local_import_calls`, `resolve_project_local_import_calls`, `resolve_pending_local_import_calls` | Local import call resolution |
| `CodeFactSink`, `PostgresCodeFactSink` | Persistence abstraction and PostgreSQL implementation |
| `IndexRequest`, `IndexOutcome`, `IndexDurations`, `IndexDegradation`, `OverlayIndexMetadata` | Indexing request/result metadata |
| `filter_discovered_paths`, `unsupported_file_types`, `relative_path`, `requested_relative_path` | Path filtering, reporting, and normalization helpers |

| Constant / env var | Purpose | Default |
| --- | --- | --- |
| `DEFAULT_EXCLUDES` | Shared discovery exclusions such as `node_modules`, `.git`, `target`, `.next`, and cache/build directories (`crates/gcode/src/index/indexer/util.rs:1-100`) | Built-in list |
| `GCODE_GIT_STATUS_TIMEOUT_SECS` | Overlay git-status timeout override (`crates/gcode/src/index/indexer/overlay.rs:1-100`) | `5` seconds |
| `SKEW_MARGIN` | Freshness mtime safety margin subtracted from `last_indexed_at` (`crates/gcode/src/index/indexer/freshness_probe.rs:1-100`) | `2` seconds |
[crates/gcode/src/index/indexer/freshness_probe.rs:37-81]
[crates/gcode/src/index/indexer/local_imports.rs:31-38]
[crates/gcode/src/index/indexer/file.rs:15-91]
[crates/gcode/src/index/indexer/lifecycle.rs:16-54]
[crates/gcode/src/index/indexer/overlay.rs:33-36]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/indexer/file.rs\|crates/gcode/src/index/indexer/file.rs]] | `crates/gcode/src/index/indexer/file.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer/freshness_probe.rs\|crates/gcode/src/index/indexer/freshness_probe.rs]] | `crates/gcode/src/index/indexer/freshness_probe.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer/lifecycle.rs\|crates/gcode/src/index/indexer/lifecycle.rs]] | `crates/gcode/src/index/indexer/lifecycle.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer/local_imports.rs\|crates/gcode/src/index/indexer/local_imports.rs]] | `crates/gcode/src/index/indexer/local_imports.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer/overlay.rs\|crates/gcode/src/index/indexer/overlay.rs]] | `crates/gcode/src/index/indexer/overlay.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer/pipeline.rs\|crates/gcode/src/index/indexer/pipeline.rs]] | `crates/gcode/src/index/indexer/pipeline.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer/sink.rs\|crates/gcode/src/index/indexer/sink.rs]] | `crates/gcode/src/index/indexer/sink.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer/tests.rs\|crates/gcode/src/index/indexer/tests.rs]] | `crates/gcode/src/index/indexer/tests.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer/types.rs\|crates/gcode/src/index/indexer/types.rs]] | `crates/gcode/src/index/indexer/types.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer/util.rs\|crates/gcode/src/index/indexer/util.rs]] | `crates/gcode/src/index/indexer/util.rs` exposes 14 indexed API symbols. |

