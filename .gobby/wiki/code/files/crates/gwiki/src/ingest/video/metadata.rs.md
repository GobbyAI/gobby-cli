---
title: crates/gwiki/src/ingest/video/metadata.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/metadata.rs
  ranges:
  - 4-8
  - 10-25
  - 27-39
  - 43-57
  - 59-73
  - 76-84
  - 86-127
  - 129-134
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/metadata.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

This file provides borrowed metadata views and rendering helpers for video ingest. It defines a degradation context for controlling video processing, reads file metadata to build `VideoMediaMetadata`, exposes `VideoSnapshotRef` wrappers over full and file-only snapshots without cloning, converts ingest results into the local `IngestResult` form, and renders a raw-video markdown document with a formatted timestamp helper.
[crates/gwiki/src/ingest/video/metadata.rs:4-8]
[crates/gwiki/src/ingest/video/metadata.rs:10-25]
[crates/gwiki/src/ingest/video/metadata.rs:27-39]
[crates/gwiki/src/ingest/video/metadata.rs:43-57]
[crates/gwiki/src/ingest/video/metadata.rs:59-73]

## API Symbols

- `VideoDegradationContext` (class) component `VideoDegradationContext [class]` (`5cef0615-849a-5088-9727-c0d3a43555eb`) lines 4-8 [crates/gwiki/src/ingest/video/metadata.rs:4-8]
  - Signature: `pub(crate) struct VideoDegradationContext<'a> {`
  - Purpose: 'VideoDegradationContext<'a>' is a borrowed configuration object that bundles a slice of 'VideoMediaDegradation' entries, an optional 'TranscriptionDegradation' reference, and a flag indicating whether frame sampling should be suppressed. [crates/gwiki/src/ingest/video/metadata.rs:4-8]
- `video_media_metadata` (function) component `video_media_metadata [function]` (`50c14da7-1f27-51f7-a67b-5c60ec275906`) lines 10-25 [crates/gwiki/src/ingest/video/metadata.rs:10-25]
  - Signature: `pub(crate) fn video_media_metadata(`
  - Purpose: Returns a 'VideoMediaMetadata' containing the file size in bytes of 'vault_root.join(asset_path)' and the provided optional duration, or maps filesystem stat failures to 'WikiError::Io' with action '"stat video asset"'. [crates/gwiki/src/ingest/video/metadata.rs:10-25]
- `VideoSnapshotRef` (class) component `VideoSnapshotRef [class]` (`972281b0-e102-5a09-82ba-87d19a7ebc0b`) lines 27-39 [crates/gwiki/src/ingest/video/metadata.rs:27-39]
  - Signature: `pub(crate) struct VideoSnapshotRef<'a> {`
  - Purpose: 'VideoSnapshotRef' is a borrowed, read-only aggregate of a video snapshot’s metadata, frame sample data, frame image paths, frame descriptions, transcript segments, and optional transcription output. [crates/gwiki/src/ingest/video/metadata.rs:27-39]
- `from_snapshot` (function) component `from_snapshot [function]` (`3522703e-16f5-5898-9feb-e0b52ecbb815`) lines 43-57 [crates/gwiki/src/ingest/video/metadata.rs:43-57]
  - Signature: `pub(crate) fn from_snapshot(snapshot: &'a VideoSnapshot) -> Self {`
  - Purpose: Constructs a borrowed view of a 'VideoSnapshot' by copying references to its string, timestamp, vector, and optional fields into the returned value without cloning or allocation. [crates/gwiki/src/ingest/video/metadata.rs:43-57]
- `from_file_snapshot` (function) component `from_file_snapshot [function]` (`75e3be97-d080-5235-bd93-6bcc2727e1bb`) lines 59-73 [crates/gwiki/src/ingest/video/metadata.rs:59-73]
  - Signature: `pub(crate) fn from_file_snapshot(snapshot: &'a VideoFileSnapshot) -> Self {`
  - Purpose: Constructs a borrowed view of a 'VideoFileSnapshot' by copying references to its fields and converting optional 'mime_type' and 'transcription' into 'Option<&str>' and 'Option<&T>' respectively. [crates/gwiki/src/ingest/video/metadata.rs:59-73]
- `IngestResult` (class) component `IngestResult [class]` (`9b8d0d23-cc4d-5679-b896-9f2d56f3ffbf`) lines 76-84 [crates/gwiki/src/ingest/video/metadata.rs:76-84]
  - Signature: `impl From<VideoIngestResult> for IngestResult {`
  - Purpose: 'IngestResult' is a conversion target that constructs an 'IngestResult' from a 'VideoIngestResult' by moving over 'record' and 'raw_path' and wrapping 'asset_path' in 'Some'. [crates/gwiki/src/ingest/video/metadata.rs:76-84]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`e26ab6b0-6585-5980-b440-3ac9a7b01222`) lines 77-83 [crates/gwiki/src/ingest/video/metadata.rs:77-83]
  - Signature: `fn from(result: VideoIngestResult) -> Self {`
  - Purpose: Converts a 'VideoIngestResult' into 'Self' by moving 'record' and 'raw_path' through unchanged and wrapping 'asset_path' in 'Some'. [crates/gwiki/src/ingest/video/metadata.rs:77-83]
- `render_raw_video_markdown` (function) component `render_raw_video_markdown [function]` (`c50d2c8f-1fc1-52f7-8b50-2ddcbec19ec6`) lines 86-127 [crates/gwiki/src/ingest/video/metadata.rs:86-127]
  - Signature: `pub(crate) fn render_raw_video_markdown(`
  - Purpose: Builds a markdown document for a raw video snapshot by assembling metadata fields, emitting a title from the file name, and appending a note with the stored asset path. [crates/gwiki/src/ingest/video/metadata.rs:86-127]
- `format_timestamp` (function) component `format_timestamp [function]` (`cd0dca05-9cc7-5c6f-a9d2-87f9d92709fe`) lines 129-134 [crates/gwiki/src/ingest/video/metadata.rs:129-134]
  - Signature: `pub(crate) fn format_timestamp(seconds: u32) -> String {`
  - Purpose: Formats a 'u32' number of seconds into a zero-padded 'HH:MM:SS' timestamp string by computing hours, minutes, and remaining seconds. [crates/gwiki/src/ingest/video/metadata.rs:129-134]

