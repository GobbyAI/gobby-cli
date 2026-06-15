---
title: crates/gwiki/src/ingest/video/assets.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/assets.rs
  ranges:
  - 4-23
  - 25-115
  - 118-122
  - 126-206
  - 208-212
  - 214-224
  - 226-242
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/assets.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

This file implements the video-ingest path for wiki assets. `ingest_video_with_asset` is the public entry point: it delegates the actual work to `ingest_video_with_asset_without_index`, then refreshes the wiki index afterward. The core ingest function registers the video source in the vault using a content hash, writes the video asset and derived raw markdown, gathers media metadata, and prepares frame samples based on the snapshot settings and degradation flags. Supporting types and helpers handle frame persistence and cleanup: `PersistedVideoFrameAssets` groups sampled frames with their output paths and descriptions, `persist_video_frame_assets` writes sampled frames as numbered JPEG assets and removes temporary sources, and the cleanup helpers delete temp frame files best-effort while ignoring missing files or noncritical errors.
[crates/gwiki/src/ingest/video/assets.rs:4-23]
[crates/gwiki/src/ingest/video/assets.rs:25-115]
[crates/gwiki/src/ingest/video/assets.rs:118-122]
[crates/gwiki/src/ingest/video/assets.rs:126-206]
[crates/gwiki/src/ingest/video/assets.rs:208-212]

## API Symbols

- `ingest_video_with_asset` (function) component `ingest_video_with_asset [function]` (`cbf01c09-b53c-596c-a141-2b477d8fa40b`) lines 4-23 [crates/gwiki/src/ingest/video/assets.rs:4-23]
  - Signature: `pub(crate) fn ingest_video_with_asset(`
  - Purpose: Ingests a video asset by delegating to 'ingest_video_with_asset_without_index', then updates the wiki index with 'index_after_ingest', and returns the resulting 'VideoIngestResult' or 'WikiError'. [crates/gwiki/src/ingest/video/assets.rs:4-23]
- `ingest_video_with_asset_without_index` (function) component `ingest_video_with_asset_without_index [function]` (`a8e435e0-1b17-5b2e-a62c-69a4fea7a6aa`) lines 25-115 [crates/gwiki/src/ingest/video/assets.rs:25-115]
  - Signature: `pub(crate) fn ingest_video_with_asset_without_index(`
  - Purpose: Registers a video source in the vault using a content hash, writes its asset and derived raw markdown, computes media metadata, samples and persists frame assets when enabled, and returns the resulting 'VideoIngestResult' without creating an index entry. [crates/gwiki/src/ingest/video/assets.rs:25-115]
- `PersistedVideoFrameAssets` (class) component `PersistedVideoFrameAssets [class]` (`841887f8-f365-5572-926f-ec44648f2c26`) lines 118-122 [crates/gwiki/src/ingest/video/assets.rs:118-122]
  - Signature: `pub(crate) struct PersistedVideoFrameAssets {`
  - Purpose: 'PersistedVideoFrameAssets' is an internal container that persists a set of video frame assets by storing parallel vectors of frame samples, image file paths, and frame descriptions. [crates/gwiki/src/ingest/video/assets.rs:118-122]
- `persist_video_frame_assets` (function) component `persist_video_frame_assets [function]` (`72be120b-fa86-5597-904e-dd257f05417a`) lines 126-206 [crates/gwiki/src/ingest/video/assets.rs:126-206]
  - Signature: `pub(crate) fn persist_video_frame_assets(`
  - Purpose: Persists each sampled video frame image into the vault as a numbered JPEG asset, returning the updated samples, written image paths, and descriptions, while cleaning up temporary frame sources and propagating I/O errors on failure. [crates/gwiki/src/ingest/video/assets.rs:126-206]
- `cleanup_deferred_temp_frame_sources` (function) component `cleanup_deferred_temp_frame_sources [function]` (`e202b50b-cb72-5795-a111-63bee2362785`) lines 208-212 [crates/gwiki/src/ingest/video/assets.rs:208-212]
  - Signature: `fn cleanup_deferred_temp_frame_sources(paths: &[PathBuf]) {`
  - Purpose: Iterates over each 'PathBuf' in 'paths' and invokes 'remove_sampled_temp_frame' on it, discarding any resulting error. [crates/gwiki/src/ingest/video/assets.rs:208-212]
- `remove_sampled_temp_frame` (function) component `remove_sampled_temp_frame [function]` (`c0627ab3-7704-5909-867c-8ffe194fae67`) lines 214-224 [crates/gwiki/src/ingest/video/assets.rs:214-224]
  - Signature: `pub(crate) fn remove_sampled_temp_frame(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Attempts to delete the file at 'path', returns 'Ok(())' if the removal succeeds or the file is already missing, and otherwise wraps the I/O error in 'WikiError::Io' with the action '"remove sampled video frame temp file"' and the path. [crates/gwiki/src/ingest/video/assets.rs:214-224]
- `cleanup_sampled_temp_frame_sources` (function) component `cleanup_sampled_temp_frame_sources [function]` (`3e091d5b-55e6-50c2-9fcc-1e1d5e23504e`) lines 226-242 [crates/gwiki/src/ingest/video/assets.rs:226-242]
  - Signature: `pub(crate) fn cleanup_sampled_temp_frame_sources(`
  - Purpose: Deletes, on a best-effort basis, any sampled frame image files whose path matches the corresponding 'VideoFrameSample.source_asset' and resides under the system temp directory. [crates/gwiki/src/ingest/video/assets.rs:226-242]

