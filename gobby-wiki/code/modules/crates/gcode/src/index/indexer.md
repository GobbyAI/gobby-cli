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

## crates/gcode/src/index/indexer

The `indexer` module is the execution engine for all code-fact extraction in the `gcode` crate. It owns the full lifecycle of converting source files into indexed database records: discovering files on disk, parsing them for symbols, calls, and imports, writing structured facts through a transactional sink, and maintaining freshness across incremental and overlay (branch-scoped) indexing runs. The module is organized into a set of focused sub-files — pipeline, file, overlay, sink, lifecycle, freshness probe, local imports, types, and util — that together form a layered pipeline from raw filesystem paths to committed PostgreSQL rows.

The primary indexing flow begins in `pipeline.rs` with `index_files` / `index_files_with_connection` (components `6cd767b0`, `8e7f5655`), which discover files via `walker::discover_files` using `DEFAULT_EXCLUDES` (util.rs:9-25), then drive per-file indexing through `index_file` in `file.rs` (component `4b12832a`). Each call to `index_file` opens a Postgres transaction, invokes `parser::parse_file_with_semantic`, hashes the file with `hasher::file_content_hash`, and writes all extracted facts through a `PostgresCodeFactSink` (sink.rs). A lighter `index_content_only` path (component `69dcf621`) skips semantic parsing and writes only content chunks via `write_content_only_file_facts` (component `3cf1724d`). Before any advisory lock is taken, `project_changed_since` in `freshness_probe.rs` (component `d30b24ca`) provides a lock-free mtime pre-gate — walking the same discovery set and short-circuiting on the first stale or deleted file, absorbing clock skew via a two-second `SKEW_MARGIN` (freshness_probe.rs:23). Overlay (branch-scoped) indexing runs through `index_overlay_files` in `overlay.rs` (component `dc923ce5`), which queries `git status --porcelain` via `git_status_relative_paths` (component `ff7a3eb9`), computes an `OverlayReconcileAction` per candidate (Index / Inherit / Tombstone / DeleteOverlay / Skip), and re-uses the same `index_file` / sink machinery for changed files while writing tombstones for deletions. After all files are indexed, `resolve_local_import_calls` in `local_imports.rs` (component `e9d7b8d0`) runs a project-scoped pass to resolve pending import call sites that could not be resolved at parse time.

The `CodeFactSink` trait in `sink.rs` (component `4beb9119`) is the sole write abstraction; `PostgresCodeFactSink` (component `519b1645`) implements it with individual transactional methods covering every fact category. Lifecycle housekeeping (`lifecycle.rs`) provides `cleanup_deleted_file_projections` (component `27cff566`), `attach_projection_sync` (component `9fd4f6ac`), `refresh_project_stats` (component `88cf7807`), `get_stale_files` (component `e5ef0115`), and `get_orphan_files` (component `38e31014`), which are called by higher-level orchestrators after indexing batches complete. Path normalization, exclude patterns, and unsupported-file-type reporting are centralized in `util.rs` and consumed throughout the module.

### Public Types

| Symbol | Kind | Component ID | Purpose |
|---|---|---|---|
| `IndexRequest` | struct | `f008b690` | Parameters for a single index invocation |
| `IndexOutcome` | struct | `d4b4995c` | Aggregated result counts and degradations |
| `IndexDurations` | struct | `59e57725` | Per-phase timing for an index run |
| `IndexDegradation` | type | `d196f3e6` | Enum of recoverable error/warning conditions |
| `FileIndexCounts` | struct | `af868d53` | Symbol/import/call counts for one file |
| `UnsupportedFileType` | struct | `54396602` | Extension label + example paths for unsupported files |
| `OverlayIndexMetadata` | struct | `bd704bf0` | Metadata returned from an overlay index pass |
| `IndexedFileState` | struct | `92517ae0` | Content hash + language for a previously indexed file |
| `OverlayReconcileAction` | enum | `8939e254` | Decision per overlay candidate (Index/Inherit/Tombstone/DeleteOverlay/Skip) |
| `CurrentFileState` | struct | `55465b3a` | On-disk state snapshot for staleness comparison |
| `ExplicitFileRoute` | type | `eab781bf` | Routing tag for explicitly requested file paths |

### CodeFactSink Operations (sink.rs)

| Method | Component ID | Description |
|---|---|---|
| `delete_file_facts` | `6f175061` | Remove all facts for a file |
| `delete_file_non_symbol_facts` | `e97c7665` | Remove non-symbol facts only |
| `delete_stale_file_symbols` | `7a4de9ca` | Prune symbols absent from latest parse |
| `upsert_symbols` | `2039da60` | Write/update extracted symbol definitions |
| `upsert_file` | `4fd617f2` | Write/update file metadata row |
| `upsert_imports` | `5a0d366b` | Write/update import edges |
| `upsert_calls` | `e0e15eb2` | Write/update call-site edges |
| `upsert_content_chunks` | `0d1aa3ba` | Write/update content embedding chunks |

### Key Pipeline Entry Points (pipeline.rs)

| Function | Component ID | Description |
|---|---|---|
| `index_files` | `6cd767b0` | Top-level discovery + index, manages connection |
| `index_files_with_connection` | `8e7f5655` | As above with caller-supplied connection |
| `index_discovered_files` | `3d6aa723` | Index a pre-discovered path list |
| `index_explicit_files_with_connection` | `480f4240` | Index an explicit path set, bypassing discovery |
| `cleanup_skipped_file_if_indexed` | `c8fd4e80` | Remove DB facts for a file skipped this run |

### Overlay Reconcile Decision Matrix (overlay.rs:46-82)

| file_exists | current_hash == parent_hash | parent present | overlay present | indexable | Action |
|---|---|---|---|---|---|
| false | — | yes | tombstone | — | Skip |
| false | — | yes | other/none | — | Tombstone |
| false | — | no | yes | — | DeleteOverlay |
| false | — | no | no | — | Skip |
| true | yes | yes | yes | — | Inherit |
| true | yes | yes | no | — | Skip |
| true | no | — | — | yes | Index |
| true | no | — | — | no (parent present) | Tombstone |

### Environment Variables

| Variable | Default | Description |
|---|---|---|
| `GCODE_GIT_STATUS_TIMEOUT_SECS` | `5` | Seconds before `git status` is killed in overlay probing (overlay.rs:28-29, component `3ed01c63`) |

### External Collaborators

The module imports from `crate::index::{walker, parser, hasher, chunker, languages, semantic}` for discovery, parsing, hashing, chunking, language detection, and semantic call resolution respectively. It calls `crate::db` for raw connection helpers, `crate::config::{Context, ProjectIndexScope}` for project-scoped configuration, and `crate::visibility` to detect tombstone languages during overlay reconciliation (overlay.rs:9-26). Lifecycle functions call into `crate::index::api` for projection sync operations. Higher-level orchestrators in the parent `crate::index` module (and the daemon layer above it) call into this module via `index_files`, `index_overlay_files`, `project_changed_since`, and the lifecycle helpers.
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

