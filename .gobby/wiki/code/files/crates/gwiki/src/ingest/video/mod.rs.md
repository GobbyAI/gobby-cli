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

This module defines the video-ingest data shapes and orchestration entry points for turning a video source into derived wiki assets. `VideoSnapshot` and `VideoFileSnapshot` capture the fetched media state plus extracted frames, frame descriptions, transcript segments, and optional transcription output, while `VideoIngestResult` packages the resulting source record and any generated metadata. The ingest functions layer the workflow from a generic `ingest_video` entry point down through file-based paths, with variants that either use degraded processing or production processing, and corresponding “without_index” helpers that perform the extraction/transcription work and then feed the results into the shared ingest/indexing pipeline.
[crates/gwiki/src/ingest/video/mod.rs:32-45]
[crates/gwiki/src/ingest/video/mod.rs:48-61]
[crates/gwiki/src/ingest/video/mod.rs:64-73]
[crates/gwiki/src/ingest/video/mod.rs:76-94]
[crates/gwiki/src/ingest/video/mod.rs:97-104]

## API Symbols

- `VideoSnapshot` (class) component `VideoSnapshot [class]` (`dd142d97-67d1-5b19-8944-61495d5dbd56`) lines 32-45 [crates/gwiki/src/ingest/video/mod.rs:32-45]
  - Signature: `pub struct VideoSnapshot {`
  - Purpose: Indexed class `VideoSnapshot` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:32-45]
- `VideoFileSnapshot` (class) component `VideoFileSnapshot [class]` (`37a00017-4190-5aed-af26-17a9be16f909`) lines 48-61 [crates/gwiki/src/ingest/video/mod.rs:48-61]
  - Signature: `pub struct VideoFileSnapshot {`
  - Purpose: Indexed class `VideoFileSnapshot` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:48-61]
- `VideoIngestResult` (class) component `VideoIngestResult [class]` (`90aa09d2-4e3d-5179-80a2-29d1ac9a90e7`) lines 64-73 [crates/gwiki/src/ingest/video/mod.rs:64-73]
  - Signature: `pub struct VideoIngestResult {`
  - Purpose: Indexed class `VideoIngestResult` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:64-73]
- `ingest_video` (function) component `ingest_video [function]` (`da11a34a-ca1b-5284-bfb4-5460849abd5c`) lines 76-94 [crates/gwiki/src/ingest/video/mod.rs:76-94]
  - Signature: `pub fn ingest_video(`
  - Purpose: Indexed function `ingest_video` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:76-94]
- `ingest_video_file` (function) component `ingest_video_file [function]` (`2f4bef6e-9032-5bfb-a651-6e62ae0b3fab`) lines 97-104 [crates/gwiki/src/ingest/video/mod.rs:97-104]
  - Signature: `pub fn ingest_video_file(`
  - Purpose: Indexed function `ingest_video_file` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:97-104]
- `ingest_video_file_with_degradations` (function) component `ingest_video_file_with_degradations [function]` (`05e2eb59-486c-5722-8d2a-9911584d43a2`) lines 107-126 [crates/gwiki/src/ingest/video/mod.rs:107-126]
  - Signature: `fn ingest_video_file_with_degradations(`
  - Purpose: Indexed function `ingest_video_file_with_degradations` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:107-126]
- `ingest_video_file_with_degradations_without_index` (function) component `ingest_video_file_with_degradations_without_index [function]` (`91beae62-064b-50ee-a889-d2fb4e4e8d44`) lines 128-163 [crates/gwiki/src/ingest/video/mod.rs:128-163]
  - Signature: `fn ingest_video_file_with_degradations_without_index(`
  - Purpose: Indexed function `ingest_video_file_with_degradations_without_index` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:128-163]
- `ingest_video_file_with_production_processing` (function) component `ingest_video_file_with_production_processing [function]` (`e1826708-fc51-5518-8657-df2ea7c4d3f3`) lines 166-179 [crates/gwiki/src/ingest/video/mod.rs:166-179]
  - Signature: `pub fn ingest_video_file_with_production_processing(`
  - Purpose: Indexed function `ingest_video_file_with_production_processing` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:166-179]
- `ingest_video_file_with_production_processing_without_index` (function) component `ingest_video_file_with_production_processing_without_index [function]` (`8d9c3b8e-052f-5f35-bfc8-9a4fa176a9db`) lines 181-235 [crates/gwiki/src/ingest/video/mod.rs:181-235]
  - Signature: `pub(crate) fn ingest_video_file_with_production_processing_without_index(`
  - Purpose: Indexed function `ingest_video_file_with_production_processing_without_index` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:181-235]

