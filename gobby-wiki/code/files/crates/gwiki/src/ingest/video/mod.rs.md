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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/video/mod.rs:32-45](crates/gwiki/src/ingest/video/mod.rs#L32-L45), [crates/gwiki/src/ingest/video/mod.rs:48-61](crates/gwiki/src/ingest/video/mod.rs#L48-L61), [crates/gwiki/src/ingest/video/mod.rs:64-73](crates/gwiki/src/ingest/video/mod.rs#L64-L73), [crates/gwiki/src/ingest/video/mod.rs:76-94](crates/gwiki/src/ingest/video/mod.rs#L76-L94), [crates/gwiki/src/ingest/video/mod.rs:97-104](crates/gwiki/src/ingest/video/mod.rs#L97-L104), [crates/gwiki/src/ingest/video/mod.rs:107-126](crates/gwiki/src/ingest/video/mod.rs#L107-L126), [crates/gwiki/src/ingest/video/mod.rs:128-163](crates/gwiki/src/ingest/video/mod.rs#L128-L163), [crates/gwiki/src/ingest/video/mod.rs:166-179](crates/gwiki/src/ingest/video/mod.rs#L166-L179), [crates/gwiki/src/ingest/video/mod.rs:181-235](crates/gwiki/src/ingest/video/mod.rs#L181-L235)

</details>

# crates/gwiki/src/ingest/video/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Handles video ingestion for the wiki pipeline. It defines in-memory snapshot types for fetched video data and file-backed video data, plus a result wrapper that carries the ingest record and related outputs. The public ingest functions build on shared helpers to transcribe audio, sample frames, generate frame descriptions, write derived markdown/assets, and optionally index the ingested content, with separate paths for degraded processing and production vision processing.
[crates/gwiki/src/ingest/video/mod.rs:32-45]
[crates/gwiki/src/ingest/video/mod.rs:48-61]
[crates/gwiki/src/ingest/video/mod.rs:64-73]
[crates/gwiki/src/ingest/video/mod.rs:76-94]
[crates/gwiki/src/ingest/video/mod.rs:97-104]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `VideoSnapshot` | class | `pub struct VideoSnapshot {` | `VideoSnapshot [class]` | `dd142d97-67d1-5b19-8944-61495d5dbd56` | 32-45 [crates/gwiki/src/ingest/video/mod.rs:32-45] | Indexed class `VideoSnapshot` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:32-45] |
| `VideoFileSnapshot` | class | `pub struct VideoFileSnapshot {` | `VideoFileSnapshot [class]` | `37a00017-4190-5aed-af26-17a9be16f909` | 48-61 [crates/gwiki/src/ingest/video/mod.rs:48-61] | Indexed class `VideoFileSnapshot` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:48-61] |
| `VideoIngestResult` | class | `pub struct VideoIngestResult {` | `VideoIngestResult [class]` | `90aa09d2-4e3d-5179-80a2-29d1ac9a90e7` | 64-73 [crates/gwiki/src/ingest/video/mod.rs:64-73] | Indexed class `VideoIngestResult` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:64-73] |
| `ingest_video` | function | `pub fn ingest_video(` | `ingest_video [function]` | `da11a34a-ca1b-5284-bfb4-5460849abd5c` | 76-94 [crates/gwiki/src/ingest/video/mod.rs:76-94] | Indexed function `ingest_video` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:76-94] |
| `ingest_video_file` | function | `pub fn ingest_video_file(` | `ingest_video_file [function]` | `2f4bef6e-9032-5bfb-a651-6e62ae0b3fab` | 97-104 [crates/gwiki/src/ingest/video/mod.rs:97-104] | Indexed function `ingest_video_file` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:97-104] |
| `ingest_video_file_with_degradations` | function | `fn ingest_video_file_with_degradations(` | `ingest_video_file_with_degradations [function]` | `05e2eb59-486c-5722-8d2a-9911584d43a2` | 107-126 [crates/gwiki/src/ingest/video/mod.rs:107-126] | Indexed function `ingest_video_file_with_degradations` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:107-126] |
| `ingest_video_file_with_degradations_without_index` | function | `fn ingest_video_file_with_degradations_without_index(` | `ingest_video_file_with_degradations_without_index [function]` | `91beae62-064b-50ee-a889-d2fb4e4e8d44` | 128-163 [crates/gwiki/src/ingest/video/mod.rs:128-163] | Indexed function `ingest_video_file_with_degradations_without_index` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:128-163] |
| `ingest_video_file_with_production_processing` | function | `pub fn ingest_video_file_with_production_processing(` | `ingest_video_file_with_production_processing [function]` | `e1826708-fc51-5518-8657-df2ea7c4d3f3` | 166-179 [crates/gwiki/src/ingest/video/mod.rs:166-179] | Indexed function `ingest_video_file_with_production_processing` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:166-179] |
| `ingest_video_file_with_production_processing_without_index` | function | `pub(crate) fn ingest_video_file_with_production_processing_without_index(` | `ingest_video_file_with_production_processing_without_index [function]` | `8d9c3b8e-052f-5f35-bfc8-9a4fa176a9db` | 181-235 [crates/gwiki/src/ingest/video/mod.rs:181-235] | Indexed function `ingest_video_file_with_production_processing_without_index` in `crates/gwiki/src/ingest/video/mod.rs`. [crates/gwiki/src/ingest/video/mod.rs:181-235] |
