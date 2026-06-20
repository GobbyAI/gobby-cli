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

The `refresh` module plans and executes source replays for the wiki vault. Selection turns manifest records into `RefreshPlan`s, either for all refreshable records or for explicit source IDs; unsupported source kinds are skipped in broad refreshes, while missing explicit IDs and replay-metadata problems become `RefreshFailure`s ((crates/gwiki/src/commands/refresh/selection.rs:1), (crates/gwiki/src/commands/refresh/selection.rs:5), (crates/gwiki/src/commands/refresh/selection.rs:36)). Plans validate that a stored source ID maps to a raw source path before entering the refresh flow, and serialize the replay kind, raw path, and content hash for reporting or dry-run output ((crates/gwiki/src/commands/refresh/model.rs:39), (crates/gwiki/src/commands/refresh/model.rs:46), (crates/gwiki/src/commands/refresh/model.rs:54)).

Execution is split between URL and local-file candidates. URL refreshes call a supplied fetcher, hash the returned snapshot body, report unchanged records without rewriting, and hand changed content to `refresh_changed_url_source`; failures are accumulated rather than aborting the whole run ((crates/gwiki/src/commands/refresh/candidate.rs:13), (crates/gwiki/src/commands/refresh/candidate.rs:23), (crates/gwiki/src/commands/refresh/candidate.rs:30), (crates/gwiki/src/commands/refresh/candidate.rs:44)). Local refresh support is modeled by replay metadata and helpers such as `local_file_replay`, with tests covering Markdown/Text/File replay, unchanged content, changed replays, stale raw-asset cleanup, malformed source IDs, and path-safety behavior ((crates/gwiki/src/commands/refresh/tests.rs:43), (crates/gwiki/src/commands/refresh/tests.rs:60)).

The module collaborates with the ingest, source manifest, indexing, scope, and vault-path layers. `candidate.rs` imports `crate::ingest`, URL snapshot/failure types, `SourceManifest`/`SourceRecord`, `ResolvedScope`, `ScopeIdentity`, and `WikiError`; it also calls into `gobby_core::indexing::content_hash` and the local vault helpers for raw paths and asset removal ((crates/gwiki/src/commands/refresh/candidate.rs:1), (crates/gwiki/src/commands/refresh/candidate.rs:4), (crates/gwiki/src/commands/refresh/candidate.rs:9), (crates/gwiki/src/commands/refresh/candidate.rs:24)). Tests seed data through `SourceManifest::register` using `SourceDraft`, `SourceKind`, `IngestionMethod`, and `CompileStatus`, showing that refresh operates over persisted manifest records rather than ad hoc file scans ((crates/gwiki/src/commands/refresh/tests.rs:2), (crates/gwiki/src/commands/refresh/tests.rs:13)).

| Public symbol | Kind | Role |
| --- | --- | --- |
| `execute`, `execute_with_fetcher`, `execute_resolved_with_fetcher` | functions | Top-level refresh entry points |
| `select_sources` | function | Builds planned, skipped, and failed selections |
| `RefreshPlan::from_record` | method | Validates a record before planning |
| `RefreshPlan::serialize` | method | Emits refresh plan fields for reporting |
| `refresh_url_candidate`, `refresh_local_candidate` | functions | Execute per-source refresh candidates |
| `render_refresh`, `refresh_status` | functions | Render refresh results/status |
| `raw_source_path`, `source_asset_paths_for_id`, `remove_relative_file`, `safe_refresh_relative_path`, `ensure_scope_root` | functions | Vault path and cleanup helpers |
| `RefreshRender`, `RefreshedSource`, `RefreshResult`, `RefreshFailure`, `SkippedRefresh`, `IndexStatus` | structs/classes | Result model for reporting and downstream handling |

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

