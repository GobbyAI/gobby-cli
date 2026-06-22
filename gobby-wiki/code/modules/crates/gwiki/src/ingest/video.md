---
title: crates/gwiki/src/ingest/video
type: code_module
provenance:
- file: crates/gwiki/src/ingest/video/assets.rs
- file: crates/gwiki/src/ingest/video/metadata.rs
- file: crates/gwiki/src/ingest/video/mod.rs
- file: crates/gwiki/src/ingest/video/processing.rs
- file: crates/gwiki/src/ingest/video/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video

Parent: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Overview

## crates/gwiki/src/ingest/video

### Responsibilities

The `ingest/video` module is gwiki's video ingestion pipeline. It accepts a raw video file (or an in-memory byte snapshot) and drives the full enrichment sequence: audio extraction and transcription, frame sampling and vision-based description, markdown rendering, asset persistence, and search-index update. Two parallel snapshot types—`VideoSnapshot` (owns raw bytes) and `VideoFileSnapshot` (holds a filesystem `PathBuf`)—share a common borrowed view `VideoSnapshotRef<'a>` (metadata.rs:26-40) so that the downstream rendering and storage code is snapshot-agnostic. `VideoIngestResult` carries the finished `SourceRecord` and any degradation signals back to callers.

### Key Processing Flow

The primary entry points are `ingest_video_with_asset` / `ingest_video_with_asset_without_index` (mod.rs) for pre-enriched snapshots and `ingest_video_file_with_processing` / `ingest_video_file_with_processing_without_index` (processing.rs:44-64) for raw files that still need media work. The file-based path delegates to the `VideoMediaExtractor` trait (processing.rs:17-26): `ProductionVideoMediaExtractor` calls `crate::media::extract_audio_file` and `crate::media::sample_frame_images`, while tests inject `FakeVideoMediaExtractor`. After extraction the pipeline calls into `crate::transcribe` for speech-to-text and `crate::vision` for per-frame descriptions, controlled by `VideoDegradationContext` (metadata.rs:3-8). Resulting enriched data is rendered to Markdown via `render_raw_video_markdown` / `format_timestamp` and then written through `crate::ingest::{write_asset, write_raw_markdown}` helpers. `persist_video_frame_assets` (assets.rs) records the frame image files as `PersistedVideoFrameAssets`; the three cleanup functions (`cleanup_deferred_temp_frame_sources`, `cleanup_sampled_temp_frame_sources`, `remove_sampled_temp_frame`) handle temp-file lifetime so frame images do not leak across ingestion boundaries. The `_without_index` variants skip the final `index_after_ingest` call (processing.rs:55) for callers that batch-index later.

### Collaboration Points

| Direction | Collaborator | Role |
|---|---|---|
| calls out | `crate::media` | `extract_audio_file`, `sample_frame_images` |
| calls out | `crate::transcribe` | `TranscriptionEndpoint`, `TranscriptionOutput`, segment types |
| calls out | `crate::vision` | `VisionEndpoint`, `VisionClient`, `VisionExtraction` |
| calls out | `crate::video` | `write_video_derived_markdown`, `VideoMarkdownRequest`, frame/segment types |
| calls out | `crate::ingest` | `index_after_ingest`, `write_asset`, `write_raw_markdown`, metadata helpers |
| calls out | `crate::store` | `WikiIndexStore`, `WikiDocumentKind` |
| calls out | `gobby_core` | `AiContext`, `AiCapability`, `content_hash` |
| feature-gated | `crate::ai::clients::ProductionVisionClient` | production vision under `#[cfg(feature = "ai")]` (mod.rs:4) |
| called by | parent `crate::ingest` module | dispatches video source kinds here |

`VideoSnapshotRef::from_snapshot` (metadata.rs:43) and `from_file_snapshot` (metadata.rs:56) convert owned snapshot types into the shared borrowed form; downstream rendering and `video_media_metadata` (metadata.rs:9-23) accept this reference to read file size and duration without copying data.

### Public API Surface

| Symbol | Kind | Description |
|---|---|---|
| `VideoSnapshot` | struct | Owned in-memory video snapshot with raw bytes |
| `VideoFileSnapshot` | struct | File-path-based snapshot for on-disk video |
| `VideoSnapshotRef<'a>` | struct | Borrowed, snapshot-agnostic view |
| `VideoIngestResult` | struct | Completed ingestion result and record |
| `VideoDegradationContext<'a>` | struct | Controls which enrichment steps are skipped |
| `PersistedVideoFrameAssets` | struct | Tracks frame image paths after persistence |
| `ingest_video_with_asset` | fn | Ingest pre-enriched snapshot, then index |
| `ingest_video_with_asset_without_index` | fn | Ingest without final index update |
| `ingest_video_file_with_processing` | fn | Full media-processing pipeline, then index |
| `persist_video_frame_assets` | fn | Write frame images to the wiki store |
| `video_media_metadata` | fn | Stat asset file for size/duration metadata |
| `render_raw_video_markdown` | fn | Render enriched video data to Markdown |
| `format_timestamp` | fn | Format millisecond offset as `HH:MM:SS` |
| `DEFAULT_FRAME_INTERVAL_SECONDS` | const | Default frame sampling cadence (5 s) |

### Test Infrastructure

`tests.rs` provides a rich set of fakes and scripted doubles so that no real media or AI services are needed during unit testing. `FakeVideoMediaExtractor` (tests.rs:64-70) can be configured to return preset audio bytes and frame pairs or to inject failures. Transcription is covered by `FakeTranscriptionClient`, `FailingTranscriptionClient`, `ScriptedTranscriptionClient`, and `ScriptedChunkTranscriptionClient`; vision by `FakeVisionClient` and `FailingVisionClient`. The `sample_snapshot` helper (tests.rs:23-61) builds a realistic `VideoSnapshot` with two frame descriptions and two transcript segments, serving as the baseline fixture across the `degradation`, `frame_assets`, `processing`, `storage`, and (feature-gated) `translation` sub-test modules.
[crates/gwiki/src/ingest/video/assets.rs:4-23]
[crates/gwiki/src/ingest/video/metadata.rs:4-8]
[crates/gwiki/src/ingest/video/mod.rs:32-45]
[crates/gwiki/src/ingest/video/processing.rs:18-26]
[crates/gwiki/src/ingest/video/tests.rs:25-62]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/video/assets.rs\|crates/gwiki/src/ingest/video/assets.rs]] | `crates/gwiki/src/ingest/video/assets.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/metadata.rs\|crates/gwiki/src/ingest/video/metadata.rs]] | `crates/gwiki/src/ingest/video/metadata.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/mod.rs\|crates/gwiki/src/ingest/video/mod.rs]] | `crates/gwiki/src/ingest/video/mod.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/processing.rs\|crates/gwiki/src/ingest/video/processing.rs]] | `crates/gwiki/src/ingest/video/processing.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/tests.rs\|crates/gwiki/src/ingest/video/tests.rs]] | `crates/gwiki/src/ingest/video/tests.rs` exposes 22 indexed API symbols. |

