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

## crates/gwiki/src/ingest/file

This module is the primary file-ingestion layer for gwiki, responsible for turning arbitrary files on disk (or bytes arriving via stdin) into indexed wiki entries. It owns the full pipeline from raw path to finished `LocalFileIngestResult`: detecting the file's media type, reading its bytes, routing to a media-specific ingest backend, collecting any quality-degradation signals, and resolving a canonical source location that is stable whether the file lives inside or outside the vault root. The two top-level entry points visible in the test suite — `ingest_path` and `ingest_stdin` — delegate immediately to `ingest_path_without_index` (dispatch.rs:44) and a complementary stdin variant, each of which performs all per-file work before the caller commits a record to the store.

**Source classification and I/O** are handled entirely in `source.rs`. `detect_source_kind` (source.rs:8) matches on the lowercased file extension to return one of the `SourceKind` variants, and `source_location` (source.rs:28) computes a forward-slash-normalised path that is relative to the vault root when possible and falls back to a canonicalised absolute path for external files — a behaviour verified by `source_location_preserves_external_canonical_path` (tests.rs:35). `should_store_asset` (source.rs:44) gates whether binary or large-text content is written to the asset store at all, and `read_source_file` (source.rs:57) wraps `std::fs::read` with structured `WikiError::Io` context.

**Dispatch** (`dispatch.rs`) is the routing hub. After calling `detect_source_kind` and `source_location` it matches on `SourceKind` to call the appropriate sub-system — `ingest_audio_with_transcription_without_index`, `ingest_image_with_production_vision_without_index`, `ingest_video_file_with_production_processing_without_index`, `ingest_pdf_file_without_index`, `ingest_document_without_index`, `ingest_session_file_without_index`, or `ingest_generic_file_without_index` — each imported from sibling ingest crates (dispatch.rs:1-40). Feature flags (`documents`, `ai`) gate the PDF, Office, and vision-augmented paths at compile time. After the per-type call returns, `attach_replay_metadata` (replay.rs) enriches the result and degradation helpers from `degradation.rs` convert structured quality signals into compact string summaries that travel with the manifest.

**Degradation reporting** (`degradation.rs`) provides four `pub(super)` formatters that normalise quality-loss signals from all media backends into a uniform `"domain:reason:fallback"` string scheme. `video_degradation_summaries` (degradation.rs:24) collects multiple per-frame degradations and appends any transcription degradation, returning a `Vec<String>` for aggregation into the source manifest.

### Source-kind routing table

| Extension(s) | SourceKind | Asset stored? |
|---|---|---|
| `pdf` | `Pdf` | Yes |
| `docx xlsx xls ods pptx` | `Office` | Yes |
| `html htm` | `Html` | Yes |
| `mp3 wav m4a aac flac ogg opus` | `Audio` | Yes |
| `png jpg jpeg gif webp bmp tiff` | `Image` | Yes |
| `mp4 mov m4v webm mkv` | `Video` | Yes |
| `md markdown` | `Markdown` | No (inline) |
| `jsonl` | `Session` | No (inline) |
| `txt csv json xml yaml yml toml log ini env …` | `Text` | Only if > `TEXT_INLINE_LIMIT_BYTES` |
| *(unrecognised)* | `File` | Yes |

source.rs:9-25, source.rs:44-54

### Public API symbols

| Symbol | File | Role |
|---|---|---|
| `ingest_path_without_index` | dispatch.rs:44 | Core per-file pipeline, no store commit |
| `detect_source_kind` | source.rs:8 | Extension → `SourceKind` mapping |
| `source_location` | source.rs:28 | Vault-relative or absolute canonical path |
| `should_store_asset` | source.rs:44 | Binary/large-text asset storage gate |
| `read_source_file` | source.rs:57 | Reads bytes with structured error context |
| `transcription_degradation_summary` | degradation.rs:4 | Audio quality signal → string |
| `vision_degradation_summary` | degradation.rs:12 | Vision quality signal → string |
| `document_degradation_summary` | degradation.rs:17 | Document quality signal → string (`documents` feature) |
| `video_degradation_summaries` | degradation.rs:24 | Video quality signals → `Vec<String>` |

### External collaborators

This module is called by the parent `crates/gwiki/src/ingest` layer through `ingest_path` and `ingest_stdin` (tests.rs:62-95) and reaches outward to `gobby_core::ai_context::AiContext`, `gobby_core::config::{AiCapability, AiRouting, EnvOnlySource}`, and the per-media ingest modules (`ingest::audio`, `ingest::image`, `ingest::video`, `ingest::pdf`, `ingest::document`, `ingest::session`) imported at dispatch.rs:10-30. The `crate::sources::{SourceKind, SourceManifest}` and `crate::store::MemoryWikiStore` types anchor it to the wider wiki storage model (tests.rs:8-10).
[crates/gwiki/src/ingest/file/degradation.rs:4-11]
[crates/gwiki/src/ingest/file/dispatch.rs:43-242]
[crates/gwiki/src/ingest/file/generic.rs:11-57]
[crates/gwiki/src/ingest/file/replay.rs:8-32]
[crates/gwiki/src/ingest/file/source.rs:9-25]

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

