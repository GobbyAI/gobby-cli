---
title: crates/gwiki/src/ingest/video/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/video/mod.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/video/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VideoSnapshot` | class | The 'VideoSnapshot' struct represents a retrieved video file, capturing its location, raw bytes, and metadata alongside its sampled frames, corresponding image paths, frame descriptions, and transcription details. [crates/gwiki/src/ingest/video/mod.rs:32-45] |
| `VideoFileSnapshot` | class | The 'VideoFileSnapshot' struct encapsulates metadata and extracted analytical data for a specific video file, including file system properties, sampled video frames with visual descriptions, and audio transcription segments. [crates/gwiki/src/ingest/video/mod.rs:48-61] |
| `VideoIngestResult` | class | The 'VideoIngestResult' struct encapsulates the comprehensive output of a video ingestion pipeline, containing the source record, filesystem paths (raw, asset, and derived), extracted frame samples, aligned video segments, and detected media or transcription degradations. [crates/gwiki/src/ingest/video/mod.rs:64-73] |
| `ingest_video` | function | The 'ingest_video' function ingests a video snapshot into a local vault by calculating its content hash, generating metadata, writing the video file as an asset, and updating the associated wiki search index. [crates/gwiki/src/ingest/video/mod.rs:76-94] |
| `ingest_video_file` | function | The 'ingest_video_file' function ingests a video file into a wiki index store under a specified scope by delegating to 'ingest_video_file_with_degradations' with default parameters. [crates/gwiki/src/ingest/video/mod.rs:97-104] |
| `ingest_video_file_with_degradations` | function | This function ingests a video file snapshot with specified media and transcription degradations under a given vault scope, updates the wiki index store, and returns the resulting video ingestion details. [crates/gwiki/src/ingest/video/mod.rs:107-126] |
| `ingest_video_file_with_degradations_without_index` | function | This function calculates the content hash of a video file snapshot, extracts its metadata, and invokes 'ingest_video_with_asset_without_index' to ingest the video under a specified degradation context and write its asset from the source path without indexing. [crates/gwiki/src/ingest/video/mod.rs:128-163] |
| `ingest_video_file_with_production_processing` | function | This function ingests a video file with production processing by delegating to a non-indexing ingestion routine and then updates the specified WikiIndexStore with the newly ingested assets. [crates/gwiki/src/ingest/video/mod.rs:166-179] |
| `ingest_video_file_with_production_processing_without_index` | function | This function probes and updates the video file duration, resolves production-specific transcription and vision extraction endpoints based on conditional feature compilation and runtime AI routing configurations, and delegates the core processing to 'ingest_video_file_with_processing_without_index'. [crates/gwiki/src/ingest/video/mod.rs:181-235] |

