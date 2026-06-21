---
title: crates/gwiki/src/ingest/video/assets.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/assets.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/assets.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Overview

`crates/gwiki/src/ingest/video/assets.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/video/assets.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ingest_video_with_asset` | function | The 'ingest_video_with_asset' function ingests a video snapshot and its asset payload into a vault by calling 'ingest_video_with_asset_without_index' and subsequently updates the wiki search index using the provided store. [crates/gwiki/src/ingest/video/assets.rs:4-23] |
| `ingest_video_with_asset_without_index` | function | This function registers a video source and its content hash within a manifest, invokes a callback to persist the video asset, writes the corresponding raw markdown, and extracts and persists video frame sample assets. [crates/gwiki/src/ingest/video/assets.rs:25-115] |
| `PersistedVideoFrameAssets` | class | The crate-private 'PersistedVideoFrameAssets' struct represents a collection of persisted video frame resources, containing vectors of video frame samples, associated file paths to stored image assets, and corresponding frame descriptions. [crates/gwiki/src/ingest/video/assets.rs:118-122] |
| `persist_video_frame_assets` | function | This function reads temporary video frame images from a list of paths, persists them as formatted JPEG assets in the vault root using the source record and video name, and returns a struct of the persisted asset paths and descriptions while ensuring proper cleanup of temporary files if an I/O error occurs. [crates/gwiki/src/ingest/video/assets.rs:126-206] |
| `cleanup_deferred_temp_frame_sources` | function | This function iterates over a slice of filesystem paths and attempts to remove the sampled temporary frame associated with each path, silently ignoring any errors that occur during the removal process. [crates/gwiki/src/ingest/video/assets.rs:208-212] |
| `remove_sampled_temp_frame` | function | This crate-private function attempts to delete a file at the specified path, returning success if the file is removed or already absent, and wrapping any other I/O errors in a custom 'WikiError::Io' structure. [crates/gwiki/src/ingest/video/assets.rs:214-224] |
| `cleanup_sampled_temp_frame_sources` | function | The function performs a best-effort deletion of files in 'frame_image_paths' that reside within the system's temporary directory and match the 'source_asset' path of the corresponding 'VideoFrameSample' at the same index. [crates/gwiki/src/ingest/video/assets.rs:226-242] |

