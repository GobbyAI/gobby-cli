---
title: crates/gwiki/src/ingest/video/metadata.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/metadata.rs
  ranges:
  - 4-8
  - 10-25
  - 27-39
  - 42-56
  - 58-72
  - 75-83
  - 76-82
  - 85-126
  - 128-133
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/metadata.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

`crates/gwiki/src/ingest/video/metadata.rs` exposes 9 indexed API symbols.
[crates/gwiki/src/ingest/video/metadata.rs:4-8]
[crates/gwiki/src/ingest/video/metadata.rs:10-25]
[crates/gwiki/src/ingest/video/metadata.rs:27-39]
[crates/gwiki/src/ingest/video/metadata.rs:42-56]
[crates/gwiki/src/ingest/video/metadata.rs:58-72]

## API Symbols

- `VideoDegradationContext` (class) component `VideoDegradationContext [class]` (`5cef0615-849a-5088-9727-c0d3a43555eb`) lines 4-8 [crates/gwiki/src/ingest/video/metadata.rs:4-8]
  - Signature: `pub(crate) struct VideoDegradationContext<'a> {`
  - Purpose: `VideoDegradationContext` is a crate-private struct that holds borrowed references to video media degradations, optional transcription degradation metadata, and a boolean flag controlling frame sampling suppression. [crates/gwiki/src/ingest/video/metadata.rs:4-8]
- `video_media_metadata` (function) component `video_media_metadata [function]` (`50c14da7-1f27-51f7-a67b-5c60ec275906`) lines 10-25 [crates/gwiki/src/ingest/video/metadata.rs:10-25]
  - Signature: `pub(crate) fn video_media_metadata(`
  - Purpose: Resolves a video asset's absolute path and returns its file size combined with optional duration as `VideoMediaMetadata`, or a `WikiError` on I/O failure. [crates/gwiki/src/ingest/video/metadata.rs:10-25]
- `VideoSnapshotRef` (class) component `VideoSnapshotRef [class]` (`972281b0-e102-5a09-82ba-87d19a7ebc0b`) lines 27-39 [crates/gwiki/src/ingest/video/metadata.rs:27-39]
  - Signature: `pub(crate) struct VideoSnapshotRef<'a> {`
  - Purpose: `VideoSnapshotRef<'a>` is a lifetime-parameterized borrowed-reference struct that aggregates a video's metadata, sampled frame data with descriptions, and transcription information. [crates/gwiki/src/ingest/video/metadata.rs:27-39]
- `from_snapshot` (function) component `from_snapshot [function]` (`9133f29e-aa1d-5869-9bf9-5c593208edd8`) lines 42-56 [crates/gwiki/src/ingest/video/metadata.rs:42-56]
  - Signature: `pub(crate) fn from_snapshot(snapshot: &'a VideoSnapshot) -> Self {`
  - Purpose: Constructs a new instance by borrowing fields from a `VideoSnapshot` reference while unwrapping optional types for `mime_type` and `transcription`. [crates/gwiki/src/ingest/video/metadata.rs:42-56]
- `from_file_snapshot` (function) component `from_file_snapshot [function]` (`99efb05f-bbb7-5205-b58f-843ed69390ab`) lines 58-72 [crates/gwiki/src/ingest/video/metadata.rs:58-72]
  - Signature: `pub(crate) fn from_file_snapshot(snapshot: &'a VideoFileSnapshot) -> Self {`
  - Purpose: Constructs a borrowed-reference struct instance from a `VideoFileSnapshot` by aliasing its fields and converting owned/optional types to borrowed equivalents. [crates/gwiki/src/ingest/video/metadata.rs:58-72]
- `IngestResult` (class) component `IngestResult [class]` (`e81b3e56-aedc-5b3a-935f-bd7f603553ff`) lines 75-83 [crates/gwiki/src/ingest/video/metadata.rs:75-83]
  - Signature: `impl From<VideoIngestResult> for IngestResult {`
  - Purpose: Implements infallible `From<VideoIngestResult>` trait conversion that maps `record` and `raw_path` fields directly while wrapping `asset_path` in `Option::Some`. [crates/gwiki/src/ingest/video/metadata.rs:75-83]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`521c2914-23e3-5739-8188-2fe2932edb7a`) lines 76-82 [crates/gwiki/src/ingest/video/metadata.rs:76-82]
  - Signature: `fn from(result: VideoIngestResult) -> Self {`
  - Purpose: Converts a `VideoIngestResult` into `Self` via the `From` trait, mapping `record` and `raw_path` directly while wrapping `asset_path` in `Some()`. [crates/gwiki/src/ingest/video/metadata.rs:76-82]
- `render_raw_video_markdown` (function) component `render_raw_video_markdown [function]` (`3beca2e6-d782-5ffb-b886-407e6a2de49e`) lines 85-126 [crates/gwiki/src/ingest/video/metadata.rs:85-126]
  - Signature: `pub(crate) fn render_raw_video_markdown(`
  - Purpose: # Summary

Generates a markdown document containing video snapshot metadata fields (source hash, duration, mime type, frame/transcript counts) and asset location reference. [crates/gwiki/src/ingest/video/metadata.rs:85-126]
- `format_timestamp` (function) component `format_timestamp [function]` (`bbc51501-3e90-5f4b-871a-535f22479abd`) lines 128-133 [crates/gwiki/src/ingest/video/metadata.rs:128-133]
  - Signature: `pub(crate) fn format_timestamp(seconds: u32) -> String {`
  - Purpose: Converts a total second count into a zero-padded HH:MM:SS formatted time string using integer arithmetic decomposition. [crates/gwiki/src/ingest/video/metadata.rs:128-133]

