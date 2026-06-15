---
title: crates/gwiki/src/ingest/video/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/mod.rs
  ranges:
  - 32-45
  - 48-61
  - 64-73
  - 76-94
  - 97-104
  - 107-126
  - 128-163
  - 166-179
  - 181-235
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/mod.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

This module defines the video-ingest data model and orchestration entry points. `VideoSnapshot` and `VideoFileSnapshot` carry the source identity, timing, MIME, frame-sampling, extracted frame, transcript, and optional transcription data for in-memory and file-backed video assets, while `VideoIngestResult` collects the record plus derived asset and degradation outputs produced by ingestion. The `ingest_video*` functions are thin wrappers around the lower-level ingest pipeline: they compute or forward the source hash, choose the appropriate degradation, processing, and transcription settings, write the asset into the vault, and optionally refresh the wiki index afterward so video ingestion ends with a fully indexed result.
[crates/gwiki/src/ingest/video/mod.rs:32-45]
[crates/gwiki/src/ingest/video/mod.rs:48-61]
[crates/gwiki/src/ingest/video/mod.rs:64-73]
[crates/gwiki/src/ingest/video/mod.rs:76-94]
[crates/gwiki/src/ingest/video/mod.rs:97-104]

## API Symbols

- `VideoSnapshot` (class) component `VideoSnapshot [class]` (`dd142d97-67d1-5b19-8944-61495d5dbd56`) lines 32-45 [crates/gwiki/src/ingest/video/mod.rs:32-45]
  - Signature: `pub struct VideoSnapshot {`
  - Purpose: 'VideoSnapshot' is a data container for a fetched video asset, including its source metadata, raw bytes, optional MIME type and timing information, extracted frame sample metadata and file paths, frame descriptions, transcript segments, and an optional transcription result. [crates/gwiki/src/ingest/video/mod.rs:32-45]
- `VideoFileSnapshot` (class) component `VideoFileSnapshot [class]` (`37a00017-4190-5aed-af26-17a9be16f909`) lines 48-61 [crates/gwiki/src/ingest/video/mod.rs:48-61]
  - Signature: `pub struct VideoFileSnapshot {`
  - Purpose: 'VideoFileSnapshot' is a data container describing a fetched video file’s identity, storage location, media metadata, sampled frame outputs, transcript segments, and optional transcription result. [crates/gwiki/src/ingest/video/mod.rs:48-61]
- `VideoIngestResult` (class) component `VideoIngestResult [class]` (`90aa09d2-4e3d-5179-80a2-29d1ac9a90e7`) lines 64-73 [crates/gwiki/src/ingest/video/mod.rs:64-73]
  - Signature: `pub struct VideoIngestResult {`
  - Purpose: 'VideoIngestResult' aggregates the outputs of a video ingestion pipeline, including the source record, raw and processed asset paths, sampled frames, aligned segments, detected media degradations, and an optional transcription degradation. [crates/gwiki/src/ingest/video/mod.rs:64-73]
- `ingest_video` (function) component `ingest_video [function]` (`da11a34a-ca1b-5284-bfb4-5460849abd5c`) lines 76-94 [crates/gwiki/src/ingest/video/mod.rs:76-94]
  - Signature: `pub fn ingest_video(`
  - Purpose: Computes a content hash for the video snapshot, ingests the asset into the vault without indexing via 'ingest_video_with_asset_without_index' using default degradation context and a writer closure, then rebuilds the wiki index and returns the resulting 'VideoIngestResult'. [crates/gwiki/src/ingest/video/mod.rs:76-94]
- `ingest_video_file` (function) component `ingest_video_file [function]` (`2f4bef6e-9032-5bfb-a651-6e62ae0b3fab`) lines 97-104 [crates/gwiki/src/ingest/video/mod.rs:97-104]
  - Signature: `pub fn ingest_video_file(`
  - Purpose: 'ingest_video_file' is a thin wrapper that forwards its vault root, index store, scope, and snapshot to 'ingest_video_file_with_degradations' with empty degradations, no extra context, and 'false' for the final flag, returning the resulting 'VideoIngestResult' or 'WikiError'. [crates/gwiki/src/ingest/video/mod.rs:97-104]
- `ingest_video_file_with_degradations` (function) component `ingest_video_file_with_degradations [function]` (`05e2eb59-486c-5722-8d2a-9911584d43a2`) lines 107-126 [crates/gwiki/src/ingest/video/mod.rs:107-126]
  - Signature: `fn ingest_video_file_with_degradations(`
  - Purpose: Runs 'ingest_video_file_with_degradations_without_index' to ingest a video snapshot with optional media/transcription degradations and frame-sampling suppression, then updates the wiki index via 'index_after_ingest' before returning the resulting 'VideoIngestResult'. [crates/gwiki/src/ingest/video/mod.rs:107-126]
- `ingest_video_file_with_degradations_without_index` (function) component `ingest_video_file_with_degradations_without_index [function]` (`91beae62-064b-50ee-a889-d2fb4e4e8d44`) lines 128-163 [crates/gwiki/src/ingest/video/mod.rs:128-163]
  - Signature: `fn ingest_video_file_with_degradations_without_index(`
  - Purpose: Computes the source video’s content hash, builds a 'VideoSnapshotRef' plus degradation context, and delegates to 'ingest_video_with_asset_without_index' with a closure that writes the asset from the snapshot path, returning the resulting 'VideoIngestResult' or a wrapped 'WikiError' on hash failure. [crates/gwiki/src/ingest/video/mod.rs:128-163]
- `ingest_video_file_with_production_processing` (function) component `ingest_video_file_with_production_processing [function]` (`e1826708-fc51-5518-8657-df2ea7c4d3f3`) lines 166-179 [crates/gwiki/src/ingest/video/mod.rs:166-179]
  - Signature: `pub fn ingest_video_file_with_production_processing(`
  - Purpose: Runs 'ingest_video_file_with_production_processing_without_index' to ingest the video, then refreshes the wiki index via 'index_after_ingest', and returns the ingestion result or propagates any 'WikiError'. [crates/gwiki/src/ingest/video/mod.rs:166-179]
- `ingest_video_file_with_production_processing_without_index` (function) component `ingest_video_file_with_production_processing_without_index [function]` (`8d9c3b8e-052f-5f35-bfc8-9a4fa176a9db`) lines 181-235 [crates/gwiki/src/ingest/video/mod.rs:181-235]
  - Signature: `pub(crate) fn ingest_video_file_with_production_processing_without_index(`
  - Purpose: Ensures a video snapshot has a duration, selects the production transcription endpoint and a production media extractor, and then delegates to 'ingest_video_file_with_processing_without_index', enabling vision extraction only when the AI routing supports it and otherwise degrading to a no-vision path. [crates/gwiki/src/ingest/video/mod.rs:181-235]

