---
title: crates/gwiki/src/ingest/file
type: code_module
provenance:
- file: crates/gwiki/src/ingest/file/degradation.rs
- file: crates/gwiki/src/ingest/file/dispatch.rs
- file: crates/gwiki/src/ingest/file/generic.rs
- file: crates/gwiki/src/ingest/file/render.rs
- file: crates/gwiki/src/ingest/file/replay.rs
- file: crates/gwiki/src/ingest/file/source.rs
- file: crates/gwiki/src/ingest/file/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

This module ingests local files and stdin-like snapshots into wiki source records, choosing specialized media/document pipelines by file type and preserving source identity. `source.rs` classifies paths by extension into `SourceKind` variants such as PDF, Office, HTML, audio, image, video, Markdown, session JSONL, text, or generic file, and computes a stable display location relative to the vault when possible or as a canonical external path otherwise (`crates/gwiki/src/ingest/file/source.rs:8`, `crates/gwiki/src/ingest/file/source.rs:26`). It also decides whether bytes should be stored as an asset, notably large text beyond `TEXT_INLINE_LIMIT_BYTES` and binary/document/media kinds (`crates/gwiki/src/ingest/file/source.rs:43`).

The central flow is `ingest_path_without_index`, which detects the source kind, derives the file name and source location, then dispatches to the appropriate lower-level ingestion path (`crates/gwiki/src/ingest/file/dispatch.rs:40`). Audio calls transcription ingestion, documents/PDFs use document or PDF handlers behind feature gates, images use production vision ingestion, sessions use the session replay pipeline, videos use production video processing, and remaining file types go through generic ingestion (`crates/gwiki/src/ingest/file/dispatch.rs:11`, `crates/gwiki/src/ingest/file/dispatch.rs:14`, `crates/gwiki/src/ingest/file/dispatch.rs:18`, `crates/gwiki/src/ingest/file/dispatch.rs:21`, `crates/gwiki/src/ingest/file/dispatch.rs:24`, `crates/gwiki/src/ingest/file/dispatch.rs:35`). Degradation helpers normalize partial-failure metadata into compact strings for transcription, vision, documents, and video, including video media degradations plus optional transcription degradation (`crates/gwiki/src/ingest/file/degradation.rs:4`, `crates/gwiki/src/ingest/file/degradation.rs:11`, `crates/gwiki/src/ingest/file/degradation.rs:18`, `crates/gwiki/src/ingest/file/degradation.rs:22`).

The module collaborates upward with the public ingest API through `IngestFileOptions` and `ScopeIdentity`, and downward with media/document/session submodules that return unindexed ingest results for later storage/indexing (`crates/gwiki/src/ingest/file/dispatch.rs:10`, `crates/gwiki/src/ingest/file/dispatch.rs:27`, `crates/gwiki/src/ingest/file/dispatch.rs:40`). Tests exercise these boundaries with `MemoryWikiStore`, `SourceManifest`, `content_hash`, and explicit no-AI ingest options, verifying that external source paths remain canonical and that file/stdin ingestion hashes their byte sources (`crates/gwiki/src/ingest/file/tests.rs:3`, `crates/gwiki/src/ingest/file/tests.rs:8`, `crates/gwiki/src/ingest/file/tests.rs:20`, `crates/gwiki/src/ingest/file/tests.rs:35`, `crates/gwiki/src/ingest/file/tests.rs:52`).

| Public/API Symbol | Responsibility | Evidence |
| --- | --- | --- |
| `detect_source_kind` | Map file extensions to `SourceKind` dispatch categories. | `crates/gwiki/src/ingest/file/source.rs:8` |
| `source_location` | Produce vault-relative or canonical display paths with normalized separators. | `crates/gwiki/src/ingest/file/source.rs:26` |
| `should_store_asset` | Decide whether source bytes are stored as assets. | `crates/gwiki/src/ingest/file/source.rs:43` |
| `read_source_file` | Read source bytes and wrap I/O failures as `WikiError::Io`. | `crates/gwiki/src/ingest/file/source.rs:57` |
| `ingest_path_without_index` | Dispatch a local path to the correct unindexed ingest pipeline. | `crates/gwiki/src/ingest/file/dispatch.rs:40` |
| `video_degradation_summaries` | Flatten video media and transcription degradations into summary strings. | `crates/gwiki/src/ingest/file/degradation.rs:22` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/file/degradation.rs\|crates/gwiki/src/ingest/file/degradation.rs]] | `crates/gwiki/src/ingest/file/degradation.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/file/dispatch.rs\|crates/gwiki/src/ingest/file/dispatch.rs]] | `crates/gwiki/src/ingest/file/dispatch.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/ingest/file/generic.rs\|crates/gwiki/src/ingest/file/generic.rs]] | `crates/gwiki/src/ingest/file/generic.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/ingest/file/render.rs\|crates/gwiki/src/ingest/file/render.rs]] | `crates/gwiki/src/ingest/file/render.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/ingest/file/replay.rs\|crates/gwiki/src/ingest/file/replay.rs]] | `crates/gwiki/src/ingest/file/replay.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/ingest/file/source.rs\|crates/gwiki/src/ingest/file/source.rs]] | `crates/gwiki/src/ingest/file/source.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/file/tests.rs\|crates/gwiki/src/ingest/file/tests.rs]] | `crates/gwiki/src/ingest/file/tests.rs` exposes 21 indexed API symbols. |

