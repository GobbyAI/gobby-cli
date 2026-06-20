---
title: crates/gwiki/src/ingest
type: code_module
provenance:
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/document/html.rs
- file: crates/gwiki/src/ingest/document/mod.rs
- file: crates/gwiki/src/ingest/document/office.rs
- file: crates/gwiki/src/ingest/document/render.rs
- file: crates/gwiki/src/ingest/document/tests.rs
- file: crates/gwiki/src/ingest/file/tests.rs
- file: crates/gwiki/src/ingest/git.rs
- file: crates/gwiki/src/ingest/image.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/ingest/pdf/ingest.rs
- file: crates/gwiki/src/ingest/pdf/markdown.rs
- file: crates/gwiki/src/ingest/pdf/render.rs
- file: crates/gwiki/src/ingest/pdf/tests.rs
- file: crates/gwiki/src/ingest/pdf/text.rs
- file: crates/gwiki/src/ingest/session.rs
- file: crates/gwiki/src/ingest/session/codex.rs
- file: crates/gwiki/src/ingest/session/droid.rs
- file: crates/gwiki/src/ingest/session/gemini.rs
- file: crates/gwiki/src/ingest/session/grok.rs
- file: crates/gwiki/src/ingest/session/metadata.rs
- file: crates/gwiki/src/ingest/session/qwen.rs
- file: crates/gwiki/src/ingest/session_archive.rs
- file: crates/gwiki/src/ingest/url.rs
- file: crates/gwiki/src/ingest/url/fetch.rs
- file: crates/gwiki/src/ingest/url/render.rs
- file: crates/gwiki/src/ingest/url/tests.rs
- file: crates/gwiki/src/ingest/video/processing.rs
- file: crates/gwiki/src/ingest/video/tests.rs
- file: crates/gwiki/src/ingest/wayback.rs
provenance_truncated: 15
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

The `ingest` module is the shared boundary for turning external inputs into immutable wiki sources. Its root declares the ingest submodules and central result type, `IngestResult`, which carries the registered `SourceRecord`, raw markdown path, and optional asset path; it also provides common helpers for extension normalization, raw markdown writes, asset writes, suffixed asset writes, and source-path asset preservation (`crates/gwiki/src/ingest/mod.rs:1-100`). Child modules specialize that pattern for local files, URLs, documents, PDFs, audio, video, images, session archives, MediaWiki/git sources, and Wayback captures (`crates/gwiki/src/ingest/mod.rs:1-100`).

The typical flow is: classify or fetch a snapshot, register a `SourceDraft` through `SourceManifest`, preserve source bytes as needed, derive markdown, then index through `WikiIndexStore`. Audio ingestion adds transcription routing through `AiContext`, `AiCapability`, `AiRouting`, and `TranscriptionEndpoint`, producing an `AudioIngestResult` with asset, raw markdown, transcript path, and degradation metadata (`crates/gwiki/src/ingest/audio.rs:1-100`). Session ingestion reads archive envelopes, selects adapters for Codex/Droid/Gemini/Grok/Qwen formats, parses shared `ParsedSession` messages and metadata, redacts text, and writes derived markdown (`crates/gwiki/src/ingest/session.rs:1-100`). Wayback ingestion validates and decodes HTML, parses it with `scraper`, registers a `SourceKind::Wayback` record, renders capture markdown, and writes/indexes the result (`crates/gwiki/src/ingest/wayback.rs:1-100`).

This module sits between source/storage/indexing infrastructure and format-specific extractors. It imports `WikiError`, source records/manifests/kinds, atomic directory syncing, and `WikiIndexStore` at the root (`crates/gwiki/src/ingest/mod.rs:1-100`); media/document children call back into shared helpers such as `write_asset`, `write_raw_markdown`, `markdown_title`, and `index_after_ingest` while collaborating with source manifests and store/index types (`crates/gwiki/src/ingest/document/mod.rs:1-100`, `crates/gwiki/src/ingest/pdf/ingest.rs:4-20`, `crates/gwiki/src/ingest/video/mod.rs:11-24`). URL ingestion calls out through a blocking `ureq` fetch layer with timeout, manual redirect handling, URL/IP validation, user-agent configuration, and structured fetch errors before handing snapshots to downstream renderers (`crates/gwiki/src/ingest/url/fetch.rs:1-100`).

| Public API / Symbol | Role | Evidence |
| --- | --- | --- |
| `IngestResult` | Common ingest return value with source record, raw path, optional asset path | `crates/gwiki/src/ingest/mod.rs:1-100` |
| `AudioSnapshot` | Audio source snapshot with location, file name, fetch time, bytes, MIME type, duration | `crates/gwiki/src/ingest/audio.rs:1-100` |
| `AudioIngestResult` | Audio ingest output including asset, transcript, and degradation details | `crates/gwiki/src/ingest/audio.rs:1-100` |
| `SessionFileSnapshot` | Session archive file snapshot with path and bytes | `crates/gwiki/src/ingest/session.rs:1-100` |
| `SessionTranscriptAdapter` | Adapter trait for detecting and parsing session archive formats | `crates/gwiki/src/ingest/session.rs:1-100` |
| `WaybackCaptureSnapshot` | Captured Wayback HTML snapshot metadata and body | `crates/gwiki/src/ingest/wayback.rs:1-100` |
| `ingest_capture` | Wayback capture ingest entry point | `crates/gwiki/src/ingest/wayback.rs:1-100` |

| Shared Helper | Responsibility | Evidence |
| --- | --- | --- |
| `lowercase_extension` | Normalize file extensions for classification | `crates/gwiki/src/ingest/mod.rs:1-100` |
| `write_raw_markdown` | Persist derived markdown under `raw/{record.id}.md` | `crates/gwiki/src/ingest/mod.rs:1-100` |
| `write_asset` | Persist source bytes as a raw asset | `crates/gwiki/src/ingest/mod.rs:1-100` |
| `write_asset_with_suffix` | Persist derived/suffixed assets under `raw/assets` | `crates/gwiki/src/ingest/mod.rs:1-100` |
| `write_asset_from_path` | Preserve an asset from an existing filesystem path | `crates/gwiki/src/ingest/mod.rs:1-100` |
[crates/gwiki/src/ingest/document/html.rs:8-39]
[crates/gwiki/src/ingest/document/mod.rs:21-27]
[crates/gwiki/src/ingest/file/degradation.rs:4-11]
[crates/gwiki/src/ingest/file/source.rs:9-25]
[crates/gwiki/src/ingest/pdf/markdown.rs:15-89]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gwiki/src/ingest/document\|crates/gwiki/src/ingest/document]] | The `ingest/document` module turns fetched document bytes into wiki-ingestable content while preserving the original asset. Its core types model the ingest boundary: `DocumentSnapshot` carries the source bytes and metadata, `DocumentRequest` is passed to extractors, `DocumentExtraction` returns markdown/title/unit/degradation details, and `DocumentIngestResult` links the source record with raw, asset, and derived paths (`crates/gwiki/src/ingest/document/mod.rs:1-100`). The ingest path collaborates with `crate::ingest` helpers such as `write_asset`, `write_raw_markdown`, `markdown_title`, and… |
| [[code/modules/crates/gwiki/src/ingest/file\|crates/gwiki/src/ingest/file]] | This module ingests local files and stdin-like snapshots into wiki source records, choosing specialized media/document pipelines by file type and preserving source identity. `source.rs` classifies paths by extension into `SourceKind` variants such as PDF, Office, HTML, audio, image, video, Markdown, session JSONL, text, or generic file, and computes a stable display location relative to the vault when possible or as a canonical external path otherwise (`crates/gwiki/src/ingest/file/source.rs:8`, `crates/gwiki/src/ingest/file/source.rs:26`). It also decides whether bytes should be stored as an… |
| [[code/modules/crates/gwiki/src/ingest/pdf\|crates/gwiki/src/ingest/pdf]] | The `crates/gwiki/src/ingest/pdf` module owns PDF ingestion into wiki content: it accepts PDF snapshots, extracts page text when available, optionally renders pages for document/vision handling, and produces markdown plus assets for indexing. Its ingestion entry points connect to the wider ingest/store layer through `IngestResult`, `index_after_ingest`, `write_asset`, `write_raw_markdown`, `WikiIndexStore`, and source manifests, while sharing scope and vision contracts through `ScopeIdentity` and `VisionEndpoint` (`crates/gwiki/src/ingest/pdf/ingest.rs:4-20`). |
| [[code/modules/crates/gwiki/src/ingest/session\|crates/gwiki/src/ingest/session]] | The session ingest module normalizes archived assistant-session records into shared `ParsedSession` structures. Its adapters import the common session contract and helpers from the parent module, including `ParsedSession`, `ParsedSessionMessage`, `ParsedSessionMetadata`, `SessionArchiveEnvelope`, `SessionTranscriptAdapter`, JSON/string helpers, and `pretty_json`, while surfacing failures through `crate::WikiError` (`crates/gwiki/src/ingest/session/codex.rs:1-9`, `crates/gwiki/src/ingest/session/droid.rs:1-9`). |
| [[code/modules/crates/gwiki/src/ingest/url\|crates/gwiki/src/ingest/url]] | The `crates/gwiki/src/ingest/url` module ingests URL-backed sources by fetching a snapshot, classifying/rendering it, and producing wiki-facing source material. Fetching is handled by a blocking `ureq` agent with a fixed timeout, disabled automatic redirects, manual redirect handling, URL/IP validation, user-agent setting, and structured `UrlIngestFailure` errors for HTTP status and transport failures (`crates/gwiki/src/ingest/url/fetch.rs:1-100`). |
| [[code/modules/crates/gwiki/src/ingest/video\|crates/gwiki/src/ingest/video]] | The `ingest/video` module owns video ingestion from either in-memory bytes or file snapshots, normalizing video inputs into wiki source records, raw assets, derived markdown, metadata, and index updates. Its main data shapes are `VideoSnapshot`, `VideoFileSnapshot`, and `VideoIngestResult`; snapshots carry location, filename, fetch time, MIME type, duration, sampled frames, frame descriptions, transcript segments, and optional full transcription output (`crates/gwiki/src/ingest/video/mod.rs:26-65`). The module imports the shared ingest helpers for asset writing, markdown metadata/title… |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/audio.rs\|crates/gwiki/src/ingest/audio.rs]] | `crates/gwiki/src/ingest/audio.rs` exposes 46 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/file.rs\|crates/gwiki/src/ingest/file.rs]] | `crates/gwiki/src/ingest/file.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/git.rs\|crates/gwiki/src/ingest/git.rs]] | `crates/gwiki/src/ingest/git.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/image.rs\|crates/gwiki/src/ingest/image.rs]] | `crates/gwiki/src/ingest/image.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/mediawiki.rs\|crates/gwiki/src/ingest/mediawiki.rs]] | `crates/gwiki/src/ingest/mediawiki.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/mod.rs\|crates/gwiki/src/ingest/mod.rs]] | `crates/gwiki/src/ingest/mod.rs` exposes 61 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session.rs\|crates/gwiki/src/ingest/session.rs]] | `crates/gwiki/src/ingest/session.rs` exposes 45 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/session_archive.rs\|crates/gwiki/src/ingest/session_archive.rs]] | `crates/gwiki/src/ingest/session_archive.rs` exposes 19 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/url.rs\|crates/gwiki/src/ingest/url.rs]] | `crates/gwiki/src/ingest/url.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/wayback.rs\|crates/gwiki/src/ingest/wayback.rs]] | `crates/gwiki/src/ingest/wayback.rs` exposes 31 indexed API symbols. |

