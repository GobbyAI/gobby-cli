---
title: crates/gwiki/src/sources
type: code_module
provenance:
- file: crates/gwiki/src/sources/atomic.rs
- file: crates/gwiki/src/sources/manifest.rs
- file: crates/gwiki/src/sources/mod.rs
- file: crates/gwiki/src/sources/render.rs
- file: crates/gwiki/src/sources/tests.rs
- file: crates/gwiki/src/sources/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

## crates/gwiki/src/sources

This module is the source-tracking subsystem of gwiki. It owns the full lifecycle of a "source" — a piece of ingested content (URL, audio, PDF, Git repository, Wayback snapshot, and more) — from its initial draft through registration in a persistent manifest and eventual compilation. The module is composed of four cooperating files: `types.rs` defines the domain model, `render.rs` converts records into human-readable Markdown with embedded JSON sentinels, `manifest.rs` reads and writes the on-disk index file under a file-level advisory lock, and `atomic.rs` guarantees crash-safe writes by staging changes to a named temporary file before an atomic rename. `tests.rs` exercises the round-trip behaviour of those layers.

The primary write flow runs through `SourceManifest::register` (manifest.rs): a caller constructs a `SourceDraft` using its builder API, passes it to `register`, which calls `render::source_id` and `render::canonicalize_location` to derive stable identifiers, serialises the resulting `SourceRecord` via `render::render_entry` into a Markdown bullet with an embedded `<!-- gwiki-source{…} -->` JSON comment, and then flushes the updated index file through `atomic::write_atomic`. The read path in `SourceManifest::read` scans each line of the index for the `SOURCE_MARKER` sentinel, extracts and deserialises the JSON payload, and reconstructs the `Vec<SourceRecord>` without touching the human-readable Markdown. The lock/retry loop in `manifest.rs` polls a `.lock` sibling file and respects the `SOURCE_MANIFEST_LOCK_TIMEOUT_ENV` environment variable for timeout tuning.

`render::canonicalize_location` normalises URLs before they are stored: it lowercases the scheme and authority, strips trailing slashes, drops the fragment, and sorts query parameters for stable deduplication. `SourceReplayOptions` bridges the manifest layer to the broader ingestion pipeline — its `from_ingest_file_options` / `to_ingest_file_options` methods (types.rs) translate between `IngestFileOptions` (imported from the `crate` root) and the replay representation, while `routing_name` and `parse_routing` handle AI-routing label serialisation by delegating to `gobby_core::config::AiRouting`.

### Public types

| Type | Variants / Notes |
|---|---|
| `SourceKind` | `url`, `audio`, `image`, `video`, `pdf`, `office`, `html`, `markdown`, `text`, `file`, `stdin`, `session`, `research_note`, `mediawiki`, `wayback`, `git_repository` |
| `IngestionMethod` | `manual`, `research` |
| `CompileStatus` | `pending`, `compiled` |
| `SourceDraft` | Builder; fields: `location`, `kind`, `fetched_at`, `content`, `title`, `citation`, `license`, `ingestion_method`, `compile_status` |
| `SourceRecord` | Persisted form; adds `id`, `canonical_location`, `content_hash` |
| `SourceReplay` | Enum; `local_file` variant carries a `PathBuf` |
| `SourceReplayOptions` | Converts to/from `IngestFileOptions` |

### `SourceDraft` builder API

| Method | Purpose |
|---|---|
| `new` | Construct with required `location`, `kind`, `fetched_at`, `content` |
| `url` | Return the location string |
| `with_title` | Set optional display title |
| `with_citation` | Set optional citation string |
| `with_license` | Set optional license string |
| `with_ingestion_method` | Override `IngestionMethod` (default `Manual`) |
| `with_compile_status` | Override `CompileStatus` (default `Pending`) |

### Environment variables

| Variable | Default | Effect |
|---|---|---|
| `SOURCE_MANIFEST_LOCK_TIMEOUT_ENV` | `DEFAULT_SOURCE_MANIFEST_LOCK_TIMEOUT` | Maximum duration to wait for the manifest `.lock` file before returning an error |

The module imports `IngestFileOptions` and `WikiError` from the parent `crate` (types.rs:7–8) and `AiRouting` from `gobby_core::config` (types.rs:5). `manifest.rs` calls into `render.rs` for `canonicalize_location`, `existing_index_without_manifest`, `render_entry`, and `source_id`, and delegates all file I/O to `atomic::write_atomic` (manifest.rs:8–9). Nothing outside this module is expected to reach into the submodules directly; callers interact through `SourceManifest`, `SourceDraft`, and the type definitions re-exported via `mod.rs`.
[crates/gwiki/src/sources/atomic.rs:7-44]
[crates/gwiki/src/sources/manifest.rs:23-25]
[crates/gwiki/src/sources/mod.rs:1-24]
[crates/gwiki/src/sources/render.rs:15-45]
[crates/gwiki/src/sources/tests.rs:8-50]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/sources/atomic.rs\|crates/gwiki/src/sources/atomic.rs]] | `crates/gwiki/src/sources/atomic.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/manifest.rs\|crates/gwiki/src/sources/manifest.rs]] | `crates/gwiki/src/sources/manifest.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/mod.rs\|crates/gwiki/src/sources/mod.rs]] | `crates/gwiki/src/sources/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/render.rs\|crates/gwiki/src/sources/render.rs]] | `crates/gwiki/src/sources/render.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/tests.rs\|crates/gwiki/src/sources/tests.rs]] | `crates/gwiki/src/sources/tests.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/types.rs\|crates/gwiki/src/sources/types.rs]] | `crates/gwiki/src/sources/types.rs` exposes 24 indexed API symbols. |

