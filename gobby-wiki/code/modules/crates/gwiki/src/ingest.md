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

## `crates/gwiki/src/ingest`

The `ingest` module is the central pipeline for converting immutable raw wiki sources into structured, indexed Markdown stored in the vault. Its opening doc comment — "Ingestion helpers for immutable raw wiki sources" (mod.rs:1) — captures the design constraint that every write operation is append-only and content-addressed. The module owns a set of shared primitives used by every sub-ingester: `IngestResult` (mod.rs:28–32), `write_raw_markdown` (mod.rs:41–48), `write_asset` / `write_asset_with_suffix` / `write_asset_from_path` (mod.rs:50–85), and `lowercase_extension` (mod.rs:34–40). Together these helpers normalise paths, sanitise file suffixes, and delegate the actual atomic-write mechanics to `crate::sources::atomic::sync_parent_dir` (mod.rs:24).

Each top-level file in the module handles a distinct content kind and exposes a typed snapshot struct plus an ingest entry-point function. `audio.rs` defines `AudioSnapshot` and `AudioIngestResult` (audio.rs:21–38) and routes transcription through `TranscriptionEndpoint`, selecting between `AiCapability::AudioTranscribe` and `AiCapability::AudioTranslate` based on the resolved AI routing context (audio.rs:51–80). `session.rs` parses AI-assistant chat exports (Codex, Gemini, Grok, Droid, Qwen) via a `SessionTranscriptAdapter` trait (session.rs:64–72), redacts sensitive content, and writes both raw and derived Markdown. `wayback.rs` decodes Wayback Machine HTML captures with charset-aware `encoding_rs` decoding, validates the content type, and renders Markdown before calling `write_raw_then_index` (wayback.rs:29–46). `image.rs` and `pdf.rs` (child module) handle visual assets; `git.rs` handles repository snapshots; `mediawiki.rs` handles MediaWiki export XML; `url.rs` drives generic HTTP fetches; and `video.rs` coordinates frame sampling and AI vision extraction through `VideoSnapshotRef` and `PersistedVideoFrameAssets`.

The module integrates tightly with several sibling crates. It imports `crate::WikiError`, `crate::indexer`, `crate::sources::{SourceRecord, SourceDraft, SourceManifest}`, and `crate::store::WikiIndexStore` (mod.rs:21–25), and audio ingestion additionally pulls from `crate::transcribe::{TranscriptionEndpoint, TranscriptionRequest, write_audio_transcript_markdown}` (audio.rs:13–17) and — behind the `ai` feature flag — `crate::ai::clients::ProductionTranscriptionClient` (audio.rs:6–7). The `session_archive` sub-module is `pub(crate)` only (mod.rs:11), keeping envelope parsing internal. The `document` sub-module is guarded by `#[cfg(feature = "documents")]` (mod.rs:3–4). External callers in the broader `gwiki` crate reach ingestion through the public sub-module paths exported here; nothing in this module is intended as a user-facing CLI surface — the `#[allow(dead_code, reason = "reserved gwiki CLI/API split")]` annotations throughout (audio.rs:39, wayback.rs:17, wayback.rs:28) signal that several entry points are reserved for a future CLI/API boundary.

### Public Sub-modules

| Sub-module | Feature gate | Visibility | Primary purpose |
|---|---|---|---|
| `audio` | — | `pub` | Audio file transcription |
| `document` | `documents` | `pub` | Office document extraction (DOCX, PPTX, XLSX) |
| `file` | — | `pub` | Generic local-file ingestion |
| `git` | — | `pub` | Git repository snapshots |
| `image` | — | `pub` | Image asset ingestion |
| `mediawiki` | — | `pub` | MediaWiki XML export ingestion |
| `pdf` | — | `pub` | PDF page rendering to Markdown |
| `session` | — | `pub` | AI chat-session transcript ingestion |
| `session_archive` | — | `pub(crate)` | Session envelope deserialisation (internal) |
| `url` | — | `pub` | HTTP URL fetch and ingestion |
| `video` | — | `pub` | Video frame sampling + AI vision extraction |
| `wayback` | — | `pub` | Wayback Machine capture ingestion |

### Key Shared Primitives (mod.rs)

| Symbol | Kind | Role |
|---|---|---|
| `IngestResult` | struct | Bundles `SourceRecord`, `raw_path`, and optional `asset_path` returned to callers |
| `write_raw_markdown` | fn | Writes content-addressed `.md` under `raw/` |
| `write_asset` | fn | Writes a binary asset under `raw/assets/` keyed by record ID |
| `write_asset_with_suffix` | fn | Writes a suffixed asset (e.g. per video frame) |
| `write_asset_from_path` | fn | Copies an existing file path as a content-addressed asset |
| `lowercase_extension` | fn | Normalises path extensions for MIME/routing decisions |

### Session Adapter Coverage (`session.rs`)

| Adapter constant | AI assistant handled |
|---|---|
| `CODEX_SESSION_ADAPTER` | OpenAI Codex |
| `DROID_SESSION_ADAPTER` | Android AI assistant |
| `GEMINI_SESSION_ADAPTER` | Google Gemini |
| `GROK_SESSION_ADAPTER` | xAI Grok |
| `QWEN_SESSION_ADAPTER` | Alibaba Qwen |
[crates/gwiki/src/ingest/document/html.rs:8-39]
[crates/gwiki/src/ingest/document/mod.rs:21-27]
[crates/gwiki/src/ingest/document/office.rs:39-52]
[crates/gwiki/src/ingest/file/generic.rs:11-57]
[crates/gwiki/src/ingest/pdf/markdown.rs:15-89]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gwiki/src/ingest/document\|crates/gwiki/src/ingest/document]] | ## `crates/gwiki/src/ingest/document` |
| [[code/modules/crates/gwiki/src/ingest/file\|crates/gwiki/src/ingest/file]] | ## crates/gwiki/src/ingest/file |
| [[code/modules/crates/gwiki/src/ingest/pdf\|crates/gwiki/src/ingest/pdf]] | ## crates/gwiki/src/ingest/pdf |
| [[code/modules/crates/gwiki/src/ingest/session\|crates/gwiki/src/ingest/session]] | ## crates/gwiki/src/ingest/session |
| [[code/modules/crates/gwiki/src/ingest/url\|crates/gwiki/src/ingest/url]] | ## Module: `crates/gwiki/src/ingest/url` |
| [[code/modules/crates/gwiki/src/ingest/video\|crates/gwiki/src/ingest/video]] | ## crates/gwiki/src/ingest/video |

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

