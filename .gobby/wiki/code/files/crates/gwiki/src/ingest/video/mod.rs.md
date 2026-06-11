---
title: crates/gwiki/src/ingest/video/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/mod.rs
  ranges:
  - 31-44
  - 47-60
  - 63-72
  - 74-92
  - 94-101
  - 103-122
  - 124-159
  - 161-174
  - 176-226
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/mod.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

`crates/gwiki/src/ingest/video/mod.rs` exposes 9 indexed API symbols.
[crates/gwiki/src/ingest/video/mod.rs:31-44]
[crates/gwiki/src/ingest/video/mod.rs:47-60]
[crates/gwiki/src/ingest/video/mod.rs:63-72]
[crates/gwiki/src/ingest/video/mod.rs:74-92]
[crates/gwiki/src/ingest/video/mod.rs:94-101]

## API Symbols

- `VideoSnapshot` (class) component `VideoSnapshot [class]` (`c657b195-5289-5b67-a0ba-958e3da349da`) lines 31-44 [crates/gwiki/src/ingest/video/mod.rs:31-44]
  - Signature: `pub struct VideoSnapshot {`
  - Purpose: `VideoSnapshot` is a struct that aggregates video binary data, extracted frame samples with descriptions, and transcription segments for comprehensive video content analysis and processing. [crates/gwiki/src/ingest/video/mod.rs:31-44]
- `VideoFileSnapshot` (class) component `VideoFileSnapshot [class]` (`b409c024-aeea-5073-80e1-c17024d47587`) lines 47-60 [crates/gwiki/src/ingest/video/mod.rs:47-60]
  - Signature: `pub struct VideoFileSnapshot {`
  - Purpose: `VideoFileSnapshot` is a struct that encapsulates a video file's metadata (location, path, duration, MIME type), sampled frame data (image paths and descriptions), and transcription artifacts for comprehensive video analysis. [crates/gwiki/src/ingest/video/mod.rs:47-60]
- `VideoIngestResult` (class) component `VideoIngestResult [class]` (`c32fba31-835d-5c73-bd48-880e8cfc3564`) lines 63-72 [crates/gwiki/src/ingest/video/mod.rs:63-72]
  - Signature: `pub struct VideoIngestResult {`
  - Purpose: VideoIngestResult aggregates source metadata, file paths, extracted frame samples, temporally aligned segments, and detected media and transcription degradations from video ingestion processing. [crates/gwiki/src/ingest/video/mod.rs:63-72]
- `ingest_video` (function) component `ingest_video [function]` (`994a622c-ec6c-54f1-b5aa-3b017ad88d7c`) lines 74-92 [crates/gwiki/src/ingest/video/mod.rs:74-92]
  - Signature: `pub fn ingest_video(`
  - Purpose: `ingest_video` computes a content hash for a video snapshot, persists the asset to the vault filesystem, and indexes it in the provided wiki store. [crates/gwiki/src/ingest/video/mod.rs:74-92]
- `ingest_video_file` (function) component `ingest_video_file [function]` (`1396e8ba-e260-5994-b347-daafdfe8aa50`) lines 94-101 [crates/gwiki/src/ingest/video/mod.rs:94-101]
  - Signature: `pub fn ingest_video_file(`
  - Purpose: Ingests a video file snapshot into a wiki index store for a specified vault and scope by delegating to `ingest_video_file_with_degradations` with empty degradations and default processing parameters. [crates/gwiki/src/ingest/video/mod.rs:94-101]
- `ingest_video_file_with_degradations` (function) component `ingest_video_file_with_degradations [function]` (`4905ee1a-2d61-5ef6-8213-c1df0913ab86`) lines 103-122 [crates/gwiki/src/ingest/video/mod.rs:103-122]
  - Signature: `fn ingest_video_file_with_degradations(`
  - Purpose: Ingests a video file with specified media and transcription degradations, then updates the wiki index store with the result. [crates/gwiki/src/ingest/video/mod.rs:103-122]
- `ingest_video_file_with_degradations_without_index` (function) component `ingest_video_file_with_degradations_without_index [function]` (`2431a95c-38da-57fb-bbdb-26047af09bb7`) lines 124-159 [crates/gwiki/src/ingest/video/mod.rs:124-159]
  - Signature: `fn ingest_video_file_with_degradations_without_index(`
  - Purpose: Ingests a video file with specified media and transcription degradations into a vault by computing its content hash and writing the asset without index maintenance. [crates/gwiki/src/ingest/video/mod.rs:124-159]
- `ingest_video_file_with_production_processing` (function) component `ingest_video_file_with_production_processing [function]` (`e2e9faf9-8212-5d16-a63a-4a067a5eb1a7`) lines 161-174 [crates/gwiki/src/ingest/video/mod.rs:161-174]
  - Signature: `pub fn ingest_video_file_with_production_processing(`
  - Purpose: Ingests a video file with production processing and updates the wiki index store with the ingestion results. [crates/gwiki/src/ingest/video/mod.rs:161-174]
- `ingest_video_file_with_production_processing_without_index` (function) component `ingest_video_file_with_production_processing_without_index [function]` (`21182664-a2b5-5cd7-9d99-6ae85a3c7847`) lines 176-226 [crates/gwiki/src/ingest/video/mod.rs:176-226]
  - Signature: `pub(crate) fn ingest_video_file_with_production_processing_without_index(`
  - Purpose: Ingests a video file with production media extraction and transcription, conditionally enabling vision extraction based on AI routing capability availability. [crates/gwiki/src/ingest/video/mod.rs:176-226]

