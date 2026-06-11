---
title: crates/gwiki/src/ingest/video/assets.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/assets.rs
  ranges:
  - 3-22
  - 24-114
  - 117-121
  - 125-205
  - 207-211
  - 213-223
  - 225-241
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/assets.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

`crates/gwiki/src/ingest/video/assets.rs` exposes 7 indexed API symbols.
[crates/gwiki/src/ingest/video/assets.rs:3-22]
[crates/gwiki/src/ingest/video/assets.rs:24-114]
[crates/gwiki/src/ingest/video/assets.rs:117-121]
[crates/gwiki/src/ingest/video/assets.rs:125-205]
[crates/gwiki/src/ingest/video/assets.rs:207-211]

## API Symbols

- `ingest_video_with_asset` (function) component `ingest_video_with_asset [function]` (`0f73f741-684f-5f38-bd36-2a015108be1c`) lines 3-22 [crates/gwiki/src/ingest/video/assets.rs:3-22]
  - Signature: `pub(crate) fn ingest_video_with_asset(`
  - Purpose: Ingests a video asset into a vault with specified degradation context via a write callback function, then updates the wiki index store. [crates/gwiki/src/ingest/video/assets.rs:3-22]
- `ingest_video_with_asset_without_index` (function) component `ingest_video_with_asset_without_index [function]` (`1d80e9b2-5f10-5876-a9d4-5956c0b32e8b`) lines 24-114 [crates/gwiki/src/ingest/video/assets.rs:24-114]
  - Signature: `pub(crate) fn ingest_video_with_asset_without_index(`
  - Purpose: Ingest a video by registering its metadata with a content hash, writing the asset via callback, extracting media metadata, conditionally sampling frames based on degradation context, and persisting frame assets to vault storage without index generation. [crates/gwiki/src/ingest/video/assets.rs:24-114]
- `PersistedVideoFrameAssets` (class) component `PersistedVideoFrameAssets [class]` (`91aa01f0-daef-5cbd-8483-b8b0705f3139`) lines 117-121 [crates/gwiki/src/ingest/video/assets.rs:117-121]
  - Signature: `pub(crate) struct PersistedVideoFrameAssets {`
  - Purpose: `PersistedVideoFrameAssets` is a crate-private struct that aggregates video frame data as three parallel vectors containing frame samples, their file paths, and corresponding descriptions. [crates/gwiki/src/ingest/video/assets.rs:117-121]
- `persist_video_frame_assets` (function) component `persist_video_frame_assets [function]` (`bfece869-38bb-5912-bb51-36cb77bf9350`) lines 125-205 [crates/gwiki/src/ingest/video/assets.rs:125-205]
  - Signature: `pub(crate) fn persist_video_frame_assets(`
  - Purpose: Writes sampled video frame images to vault-rooted storage as indexed JPEG files and returns their persisted paths with frame metadata, managing cleanup of temporary source assets. [crates/gwiki/src/ingest/video/assets.rs:125-205]
- `cleanup_deferred_temp_frame_sources` (function) component `cleanup_deferred_temp_frame_sources [function]` (`3c714090-f85e-5e7e-838b-1c81cd0bc1c3`) lines 207-211 [crates/gwiki/src/ingest/video/assets.rs:207-211]
  - Signature: `fn cleanup_deferred_temp_frame_sources(paths: &[PathBuf]) {`
  - Purpose: Removes temporary frame sources for each provided path, discarding any removal errors. [crates/gwiki/src/ingest/video/assets.rs:207-211]
- `remove_sampled_temp_frame` (function) component `remove_sampled_temp_frame [function]` (`4620ed09-061f-5909-8ffa-96abfbdedcbf`) lines 213-223 [crates/gwiki/src/ingest/video/assets.rs:213-223]
  - Signature: `pub(crate) fn remove_sampled_temp_frame(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Deletes the file at the provided path, treating `NotFound` errors as success while wrapping other I/O failures in a `WikiError`. [crates/gwiki/src/ingest/video/assets.rs:213-223]
- `cleanup_sampled_temp_frame_sources` (function) component `cleanup_sampled_temp_frame_sources [function]` (`80bc3c4e-2d2e-5b52-81b1-aaf1e3e12b1d`) lines 225-241 [crates/gwiki/src/ingest/video/assets.rs:225-241]
  - Signature: `pub(crate) fn cleanup_sampled_temp_frame_sources(`
  - Purpose: # Summary

Performs best-effort deletion of temporary frame image files from `frame_image_paths` that have corresponding `VideoFrameSample` entries and reside in the system temp directory. [crates/gwiki/src/ingest/video/assets.rs:225-241]

