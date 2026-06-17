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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/video/assets.rs:4-23](crates/gwiki/src/ingest/video/assets.rs#L4-L23), [crates/gwiki/src/ingest/video/assets.rs:25-115](crates/gwiki/src/ingest/video/assets.rs#L25-L115), [crates/gwiki/src/ingest/video/assets.rs:118-122](crates/gwiki/src/ingest/video/assets.rs#L118-L122), [crates/gwiki/src/ingest/video/assets.rs:126-206](crates/gwiki/src/ingest/video/assets.rs#L126-L206), [crates/gwiki/src/ingest/video/assets.rs:208-212](crates/gwiki/src/ingest/video/assets.rs#L208-L212), [crates/gwiki/src/ingest/video/assets.rs:214-224](crates/gwiki/src/ingest/video/assets.rs#L214-L224), [crates/gwiki/src/ingest/video/assets.rs:226-242](crates/gwiki/src/ingest/video/assets.rs#L226-L242)

</details>

# crates/gwiki/src/ingest/video/assets.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

This file implements the video-asset ingestion pipeline for gwiki. `ingest_video_with_asset` is the indexed entry point that delegates to `ingest_video_with_asset_without_index` and then reindexes the vault, while the main ingest path registers the video source, writes the asset, gathers media metadata, renders raw markdown, determines frame samples, persists frame assets, and then cleans up temporary frame sources.
[crates/gwiki/src/ingest/video/assets.rs:4-23]
[crates/gwiki/src/ingest/video/assets.rs:25-115]
[crates/gwiki/src/ingest/video/assets.rs:118-122]
[crates/gwiki/src/ingest/video/assets.rs:126-206]
[crates/gwiki/src/ingest/video/assets.rs:208-212]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ingest_video_with_asset` | function | `pub(crate) fn ingest_video_with_asset(` | `ingest_video_with_asset [function]` | `cbf01c09-b53c-596c-a141-2b477d8fa40b` | 4-23 [crates/gwiki/src/ingest/video/assets.rs:4-23] | Indexed function `ingest_video_with_asset` in `crates/gwiki/src/ingest/video/assets.rs`. [crates/gwiki/src/ingest/video/assets.rs:4-23] |
| `ingest_video_with_asset_without_index` | function | `pub(crate) fn ingest_video_with_asset_without_index(` | `ingest_video_with_asset_without_index [function]` | `a8e435e0-1b17-5b2e-a62c-69a4fea7a6aa` | 25-115 [crates/gwiki/src/ingest/video/assets.rs:25-115] | Indexed function `ingest_video_with_asset_without_index` in `crates/gwiki/src/ingest/video/assets.rs`. [crates/gwiki/src/ingest/video/assets.rs:25-115] |
| `PersistedVideoFrameAssets` | class | `pub(crate) struct PersistedVideoFrameAssets {` | `PersistedVideoFrameAssets [class]` | `841887f8-f365-5572-926f-ec44648f2c26` | 118-122 [crates/gwiki/src/ingest/video/assets.rs:118-122] | Indexed class `PersistedVideoFrameAssets` in `crates/gwiki/src/ingest/video/assets.rs`. [crates/gwiki/src/ingest/video/assets.rs:118-122] |
| `persist_video_frame_assets` | function | `pub(crate) fn persist_video_frame_assets(` | `persist_video_frame_assets [function]` | `72be120b-fa86-5597-904e-dd257f05417a` | 126-206 [crates/gwiki/src/ingest/video/assets.rs:126-206] | Indexed function `persist_video_frame_assets` in `crates/gwiki/src/ingest/video/assets.rs`. [crates/gwiki/src/ingest/video/assets.rs:126-206] |
| `cleanup_deferred_temp_frame_sources` | function | `fn cleanup_deferred_temp_frame_sources(paths: &[PathBuf]) {` | `cleanup_deferred_temp_frame_sources [function]` | `e202b50b-cb72-5795-a111-63bee2362785` | 208-212 [crates/gwiki/src/ingest/video/assets.rs:208-212] | Indexed function `cleanup_deferred_temp_frame_sources` in `crates/gwiki/src/ingest/video/assets.rs`. [crates/gwiki/src/ingest/video/assets.rs:208-212] |
| `remove_sampled_temp_frame` | function | `pub(crate) fn remove_sampled_temp_frame(path: &Path) -> Result<(), WikiError> {` | `remove_sampled_temp_frame [function]` | `c0627ab3-7704-5909-867c-8ffe194fae67` | 214-224 [crates/gwiki/src/ingest/video/assets.rs:214-224] | Indexed function `remove_sampled_temp_frame` in `crates/gwiki/src/ingest/video/assets.rs`. [crates/gwiki/src/ingest/video/assets.rs:214-224] |
| `cleanup_sampled_temp_frame_sources` | function | `pub(crate) fn cleanup_sampled_temp_frame_sources(` | `cleanup_sampled_temp_frame_sources [function]` | `3e091d5b-55e6-50c2-9fcc-1e1d5e23504e` | 226-242 [crates/gwiki/src/ingest/video/assets.rs:226-242] | Indexed function `cleanup_sampled_temp_frame_sources` in `crates/gwiki/src/ingest/video/assets.rs`. [crates/gwiki/src/ingest/video/assets.rs:226-242] |
