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

The `sources` module owns raw source tracking for a gwiki vault: it defines source metadata types, renders source entries into the generated manifest section, reads existing manifest markers back from the raw source index, and writes updates safely. Core metadata covers source kind, ingestion method, and compile status, all serialized with snake-case names and displayed as stable strings (`crates/gwiki/src/sources/types.rs:9-72`).

The main flow is `SourceManifest::read`, which opens the vault’s source index, scans lines for `SOURCE_MARKER`, parses embedded JSON records, and returns a manifest of `SourceRecord` entries (`crates/gwiki/src/sources/manifest.rs:21-59`). Registration builds on rendering helpers: locations are canonicalized by trimming fragments, lowercasing URL scheme/authority, sorting query params, and removing trailing slashes (`crates/gwiki/src/sources/render.rs:38-57`), while `render_entry` serializes each record into a Markdown list item plus hidden JSON marker (`crates/gwiki/src/sources/render.rs:13-35`).

Collaboration points are intentionally narrow. `manifest.rs` imports `write_atomic` for durable index rewrites, render helpers for canonicalization and Markdown generation, and type definitions for draft and record state (`crates/gwiki/src/sources/manifest.rs:8-18`). `atomic.rs` implements the file-system safety boundary by writing a temporary sibling file, syncing it, renaming it into place, and syncing the parent directory (`crates/gwiki/src/sources/atomic.rs:8-42`). `types.rs` also imports `AiRouting`, `IngestFileOptions`, and `WikiError`, indicating that source replay/routing options bridge this module to ingestion configuration and error handling (`crates/gwiki/src/sources/types.rs:1-7`).

| Public API area | Symbols |
| --- | --- |
| Source classification | `SourceKind`, `SourceKind::fmt` |
| Ingestion state | `IngestionMethod`, `IngestionMethod::fmt`, `CompileStatus`, `CompileStatus::fmt` |
| Draft/record model | `SourceDraft`, `SourceDraft::new`, `SourceDraft::url`, `SourceDraft::with_title`, `SourceDraft::with_citation`, `SourceDraft::with_license`, `SourceDraft::with_ingestion_method`, `SourceDraft::with_compile_status`, `SourceDraftRef`, `SourceRecord` |
| Replay options | `SourceReplay`, `SourceReplay::local_file`, `SourceReplayOptions`, `SourceReplayOptions::from_ingest_file_options`, `SourceReplayOptions::to_ingest_file_options` |
| Routing/helpers | `is_false`, `routing_name`, `parse_routing` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/sources/atomic.rs\|crates/gwiki/src/sources/atomic.rs]] | `crates/gwiki/src/sources/atomic.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/manifest.rs\|crates/gwiki/src/sources/manifest.rs]] | `crates/gwiki/src/sources/manifest.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/mod.rs\|crates/gwiki/src/sources/mod.rs]] | `crates/gwiki/src/sources/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/render.rs\|crates/gwiki/src/sources/render.rs]] | `crates/gwiki/src/sources/render.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/tests.rs\|crates/gwiki/src/sources/tests.rs]] | `crates/gwiki/src/sources/tests.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gwiki/src/sources/types.rs\|crates/gwiki/src/sources/types.rs]] | `crates/gwiki/src/sources/types.rs` exposes 24 indexed API symbols. |

