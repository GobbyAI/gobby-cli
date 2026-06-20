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

The `ingest/video` module owns video ingestion from either in-memory bytes or file snapshots, normalizing video inputs into wiki source records, raw assets, derived markdown, metadata, and index updates. Its main data shapes are `VideoSnapshot`, `VideoFileSnapshot`, and `VideoIngestResult`; snapshots carry location, filename, fetch time, MIME type, duration, sampled frames, frame descriptions, transcript segments, and optional full transcription output (`crates/gwiki/src/ingest/video/mod.rs:26-65`). The module imports the shared ingest helpers for asset writing, markdown metadata/title generation, raw markdown writing, path conversion, and indexing, and collaborates with source manifests, wiki index stores, transcription, vision, and video markdown/rendering types (`crates/gwiki/src/ingest/video/mod.rs:11-24`).

The processing path wraps media extraction behind `VideoMediaExtractor`, with `ProductionVideoMediaExtractor` delegating to `crate::media::extract_audio_file` and `crate::media::sample_frame_images` (`crates/gwiki/src/ingest/video/processing.rs:18-38`). `ingest_video_file_with_processing` runs the no-index variant first, then calls `index_after_ingest`, while `ingest_video_file_with_processing_without_index` accepts a `VideoFileSnapshot`, transcription endpoint, vision endpoint, and media extractor so callers can inject production or fake processing (`crates/gwiki/src/ingest/video/processing.rs:40-68`). A default frame interval of five seconds is defined for the module (`crates/gwiki/src/ingest/video/mod.rs:26`).

Metadata support centralizes degradation and snapshot views. `VideoDegradationContext` carries media degradations, optional transcription degradation, and whether frame sampling was suppressed (`crates/gwiki/src/ingest/video/metadata.rs:3-8`). `video_media_metadata` stats the persisted asset under the vault root and returns file size plus duration (`crates/gwiki/src/ingest/video/metadata.rs:10-24`). `VideoSnapshotRef` provides a borrowed view over both byte-backed and file-backed snapshots through `from_snapshot` and `from_file_snapshot`, avoiding duplicate downstream code for metadata and markdown assembly (`crates/gwiki/src/ingest/video/metadata.rs:26-63`).

Tests exercise the module through fake extractors and fake transcription/vision clients. The test harness imports core hashing, source manifests, memory stores, transcription endpoints/outputs/requests, and vision endpoints/extractions/requests, then splits coverage into degradation, frame assets, processing, storage, and AI-gated translation test modules (`crates/gwiki/src/ingest/video/tests.rs:1-19`). Its sample snapshot includes frame descriptions aligned to source references and transcript segments aligned to millisecond ranges, reflecting the module’s core job of combining video assets, sampled visual context, and transcript text into derived wiki content (`crates/gwiki/src/ingest/video/tests.rs:21-58`).

| Symbol | Kind | Responsibility |
| --- | --- | --- |
| `DEFAULT_FRAME_INTERVAL_SECONDS` | constant | Default sampling interval, set to `5` seconds (`crates/gwiki/src/ingest/video/mod.rs:26`) |
| `VideoSnapshot` | struct | Byte-backed video ingest snapshot (`crates/gwiki/src/ingest/video/mod.rs:29-43`) |
| `VideoFileSnapshot` | struct | Path-backed video ingest snapshot (`crates/gwiki/src/ingest/video/mod.rs:47-62`) |
| `VideoMediaExtractor` | trait | Abstracts audio extraction and frame sampling (`crates/gwiki/src/ingest/video/processing.rs:18-26`) |
| `ProductionVideoMediaExtractor` | struct | Production adapter over `crate::media` helpers (`crates/gwiki/src/ingest/video/processing.rs:28-38`) |
| `VideoDegradationContext` | struct | Carries media/transcription degradation state (`crates/gwiki/src/ingest/video/metadata.rs:3-8`) |
| `VideoSnapshotRef` | struct | Borrowed common view over snapshot variants (`crates/gwiki/src/ingest/video/metadata.rs:26-39`) |
| `video_media_metadata` | function | Reads persisted asset size and duration metadata (`crates/gwiki/src/ingest/video/metadata.rs:10-24`) |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/ingest/video/assets.rs\|crates/gwiki/src/ingest/video/assets.rs]] | `crates/gwiki/src/ingest/video/assets.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/metadata.rs\|crates/gwiki/src/ingest/video/metadata.rs]] | `crates/gwiki/src/ingest/video/metadata.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/mod.rs\|crates/gwiki/src/ingest/video/mod.rs]] | `crates/gwiki/src/ingest/video/mod.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/processing.rs\|crates/gwiki/src/ingest/video/processing.rs]] | `crates/gwiki/src/ingest/video/processing.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/ingest/video/tests.rs\|crates/gwiki/src/ingest/video/tests.rs]] | `crates/gwiki/src/ingest/video/tests.rs` exposes 22 indexed API symbols. |

