---
title: crates/gwiki/src/commands/refresh
type: code_module
provenance:
- file: crates/gwiki/src/commands/refresh/candidate.rs
- file: crates/gwiki/src/commands/refresh/mod.rs
- file: crates/gwiki/src/commands/refresh/model.rs
- file: crates/gwiki/src/commands/refresh/render.rs
- file: crates/gwiki/src/commands/refresh/selection.rs
- file: crates/gwiki/src/commands/refresh/tests.rs
- file: crates/gwiki/src/commands/refresh/vault.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh

Parent: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

## `crates/gwiki/src/commands/refresh`

The `refresh` command re-fetches or re-reads registered wiki sources and reconciles their stored content with the current state of each upstream location. It supports two replay strategies — HTTP URL fetching and local-file read-back — and routes each registered `SourceRecord` through a three-way outcome: refreshed (content changed), unchanged (hash identical), skipped (unsupported kind), or failed (structural or I/O error). The public entry points live in `mod.rs` and are named `execute`, `execute_with_fetcher`, and `execute_resolved_with_fetcher`, the last of which accepts a fully resolved scope and an injectable fetch closure so that tests can drive the entire pipeline without network I/O.

Source selection is handled by `selection.rs`. `select_sources` iterates every `SourceRecord` in the manifest and calls `replay_kind` to classify each one; records with no replay contract are filed as `SkippedRefresh`, records with missing metadata are filed as `RefreshFailure`, and valid records become `RefreshPlan` entries. When explicit source IDs are supplied the function switches to a lookup-by-ID path that emits `not_found` failures for unknown IDs. A parallel entry point, `select_change_triggered_refresh`, builds a `ChangeTriggeredSelection` that additionally collects canonical pages whose code-graph nodes were affected by the change (`crates/gwiki/src/commands/refresh/selection.rs:1-100`). The vault helpers in `vault.rs` (`raw_source_path`, `source_asset_paths_for_id`, `remove_relative_file`, `safe_refresh_relative_path`, `ensure_scope_root`) translate logical source IDs into on-disk paths and enforce safe path operations before any file is touched.

Execution of a planned refresh is split by replay kind in `candidate.rs`. `refresh_url_candidate` calls the injected fetch closure, computes a content hash, and short-circuits with an unchanged result when the hash matches the stored value (`candidate.rs:28-38`). On a hash mismatch it delegates to `refresh_changed_url_source`, which writes the new raw asset and re-ingests the record, then populates a `RefreshedSource` that carries both the old and new IDs, the previous raw path, and any removed asset paths. `refresh_local_candidate` follows the same hash-compare-then-replay pattern for local files; `local_file_hash` reads the file from disk and `local_file_failure` constructs a typed `RefreshFailure` for I/O errors. After all candidates are processed, `finalize_changed_refresh` triggers `index` (imported from `crate::commands::index`) to update the search index, producing an `IndexStatus` that the render layer exposes in the summary output. Rendering is handled by `render.rs` through `render_refresh` and `refresh_status`, which consume a `RefreshRender` aggregate and produce human-readable output for the CLI.

The test suite in `tests.rs` exercises the full pipeline end-to-end using temporary directory fixtures seeded by helpers such as `seed_url`, `seed_local_file`, `seed_file_without_replay`, and `seed_unsupported_connector`. Key behavioral contracts verified include: unchanged content suppresses both disk writes and index updates (`unchanged_content_does_not_rewrite_or_index`); changed URL content replaces the manifest and removes the old raw asset (`changed_content_replaces_manifest_and_removes_old_raw`); local file replay removes stale raw assets (`changed_local_file_replays_and_removes_old_raw_assets`); dry-run mode plans without fetching or writing (`dry_run_plans_without_fetching_or_writing`); and path utilities reject unsafe traversal sequences before joining (`remove_relative_file_rejects_unsafe_paths_before_join`).

### Public API Symbols

| Symbol | Kind | File |
|---|---|---|
| `execute` | function | `mod.rs` |
| `execute_with_fetcher` | function | `mod.rs` |
| `execute_resolved_with_fetcher` | function | `mod.rs` |
| `select_sources` | function | `selection.rs` |
| `select_change_triggered_refresh` | function | `selection.rs` |
| `refresh_url_candidate` | function | `candidate.rs` |
| `refresh_local_candidate` | function | `candidate.rs` |
| `render_refresh` | function | `render.rs` |
| `refresh_status` | function | `render.rs` |
| `raw_source_path` | function | `vault.rs` |
| `source_asset_paths_for_id` | function | `vault.rs` |
| `remove_relative_file` | function | `vault.rs` |
| `safe_refresh_relative_path` | function | `vault.rs` |
| `ensure_scope_root` | function | `vault.rs` |

### Key Model Types

| Type | Role |
|---|---|
| `RefreshPlan` | Validated plan entry for one source; serializable for dry-run output |
| `Selection` | Partitions records into `planned`, `skipped`, and `failed` collections |
| `ChangedRefresh` | Carries ingest result, previous raw path, removed paths, and degradation notes |
| `RefreshSinks<'a>` | Mutable sink bundle threaded through candidate functions |
| `RefreshRender` | Final aggregate consumed by `render_refresh` for CLI display |
| `RefreshedSource` | Outcome record for a changed source (old ID → new ID mapping) |
| `RefreshResult` | Outcome record for an unchanged source |
| `RefreshFailure` | Structured error for any source that could not be refreshed |
| `SkippedRefresh` | Record for sources whose kind has no replay contract |
| `IndexStatus` | Reports index health after refresh: `not_run`, `indexed`, or `degraded` |

### Replay Kinds

| `ReplayKind` | Triggered by |
|---|---|
| URL | `SourceKind::Url` with an HTTP/HTTPS location |
| Local file | `SourceKind::Markdown`, `SourceKind::Text`, or `SourceKind::File` with a relative path |
| Unsupported | All other kinds → `SelectionFailure::UnsupportedSourceKind` → `SkippedRefresh` |
[crates/gwiki/src/commands/refresh/candidate.rs:15-74]
[crates/gwiki/src/commands/refresh/mod.rs:29-37]
[crates/gwiki/src/commands/refresh/model.rs:5-9]
[crates/gwiki/src/commands/refresh/render.rs:3-49]
[crates/gwiki/src/commands/refresh/selection.rs:4-75]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/commands/refresh/candidate.rs\|crates/gwiki/src/commands/refresh/candidate.rs]] | `crates/gwiki/src/commands/refresh/candidate.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/refresh/mod.rs\|crates/gwiki/src/commands/refresh/mod.rs]] | `crates/gwiki/src/commands/refresh/mod.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/refresh/model.rs\|crates/gwiki/src/commands/refresh/model.rs]] | `crates/gwiki/src/commands/refresh/model.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/refresh/render.rs\|crates/gwiki/src/commands/refresh/render.rs]] | `crates/gwiki/src/commands/refresh/render.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/refresh/selection.rs\|crates/gwiki/src/commands/refresh/selection.rs]] | `crates/gwiki/src/commands/refresh/selection.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/refresh/tests.rs\|crates/gwiki/src/commands/refresh/tests.rs]] | `crates/gwiki/src/commands/refresh/tests.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/refresh/vault.rs\|crates/gwiki/src/commands/refresh/vault.rs]] | `crates/gwiki/src/commands/refresh/vault.rs` exposes 5 indexed API symbols. |

