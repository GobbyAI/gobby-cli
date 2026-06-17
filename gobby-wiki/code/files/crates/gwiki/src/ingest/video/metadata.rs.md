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
  - 77-83
  - 86-127
  - 129-134
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/video/metadata.rs:4-8](crates/gwiki/src/ingest/video/metadata.rs#L4-L8), [crates/gwiki/src/ingest/video/metadata.rs:10-25](crates/gwiki/src/ingest/video/metadata.rs#L10-L25), [crates/gwiki/src/ingest/video/metadata.rs:27-39](crates/gwiki/src/ingest/video/metadata.rs#L27-L39), [crates/gwiki/src/ingest/video/metadata.rs:43-57](crates/gwiki/src/ingest/video/metadata.rs#L43-L57), [crates/gwiki/src/ingest/video/metadata.rs:59-73](crates/gwiki/src/ingest/video/metadata.rs#L59-L73), [crates/gwiki/src/ingest/video/metadata.rs:77-83](crates/gwiki/src/ingest/video/metadata.rs#L77-L83), [crates/gwiki/src/ingest/video/metadata.rs:86-127](crates/gwiki/src/ingest/video/metadata.rs#L86-L127), [crates/gwiki/src/ingest/video/metadata.rs:129-134](crates/gwiki/src/ingest/video/metadata.rs#L129-L134)

</details>

# crates/gwiki/src/ingest/video/metadata.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Purpose

This file provides the video-ingest metadata and rendering helpers used by `gwiki` to describe a video asset, its snapshots, and related degradation state. `VideoDegradationContext` carries the media and transcription degradation inputs plus a flag to suppress frame sampling, `video_media_metadata` reads the on-disk file size and pairs it with an optional duration, and `VideoSnapshotRef` offers borrowed views over either a full `VideoSnapshot` or `VideoFileSnapshot` via `from_snapshot` and `from_file_snapshot`. The remaining helpers convert ingest results, format timestamps, and render raw video markdown from the collected snapshot, frame, and transcript data.
[crates/gwiki/src/ingest/video/metadata.rs:4-8]
[crates/gwiki/src/ingest/video/metadata.rs:10-25]
[crates/gwiki/src/ingest/video/metadata.rs:27-39]
[crates/gwiki/src/ingest/video/metadata.rs:43-57]
[crates/gwiki/src/ingest/video/metadata.rs:59-73]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `VideoDegradationContext` | class | `pub(crate) struct VideoDegradationContext<'a> {` | `VideoDegradationContext [class]` | `5cef0615-849a-5088-9727-c0d3a43555eb` | 4-8 [crates/gwiki/src/ingest/video/metadata.rs:4-8] | Indexed class `VideoDegradationContext` in `crates/gwiki/src/ingest/video/metadata.rs`. [crates/gwiki/src/ingest/video/metadata.rs:4-8] |
| `video_media_metadata` | function | `pub(crate) fn video_media_metadata(` | `video_media_metadata [function]` | `50c14da7-1f27-51f7-a67b-5c60ec275906` | 10-25 [crates/gwiki/src/ingest/video/metadata.rs:10-25] | Indexed function `video_media_metadata` in `crates/gwiki/src/ingest/video/metadata.rs`. [crates/gwiki/src/ingest/video/metadata.rs:10-25] |
| `VideoSnapshotRef` | class | `pub(crate) struct VideoSnapshotRef<'a> {` | `VideoSnapshotRef [class]` | `972281b0-e102-5a09-82ba-87d19a7ebc0b` | 27-39 [crates/gwiki/src/ingest/video/metadata.rs:27-39] | Indexed class `VideoSnapshotRef` in `crates/gwiki/src/ingest/video/metadata.rs`. [crates/gwiki/src/ingest/video/metadata.rs:27-39] |
| `from_snapshot` | function | `pub(crate) fn from_snapshot(snapshot: &'a VideoSnapshot) -> Self {` | `from_snapshot [function]` | `3522703e-16f5-5898-9feb-e0b52ecbb815` | 43-57 [crates/gwiki/src/ingest/video/metadata.rs:43-57] | Indexed function `from_snapshot` in `crates/gwiki/src/ingest/video/metadata.rs`. [crates/gwiki/src/ingest/video/metadata.rs:43-57] |
| `from_file_snapshot` | function | `pub(crate) fn from_file_snapshot(snapshot: &'a VideoFileSnapshot) -> Self {` | `from_file_snapshot [function]` | `75e3be97-d080-5235-bd93-6bcc2727e1bb` | 59-73 [crates/gwiki/src/ingest/video/metadata.rs:59-73] | Indexed function `from_file_snapshot` in `crates/gwiki/src/ingest/video/metadata.rs`. [crates/gwiki/src/ingest/video/metadata.rs:59-73] |
| `IngestResult::from` | method | `fn from(result: VideoIngestResult) -> Self {` | `IngestResult::from [method]` | `e26ab6b0-6585-5980-b440-3ac9a7b01222` | 77-83 [crates/gwiki/src/ingest/video/metadata.rs:77-83] | Indexed method `IngestResult::from` in `crates/gwiki/src/ingest/video/metadata.rs`. [crates/gwiki/src/ingest/video/metadata.rs:77-83] |
| `render_raw_video_markdown` | function | `pub(crate) fn render_raw_video_markdown(` | `render_raw_video_markdown [function]` | `c50d2c8f-1fc1-52f7-8b50-2ddcbec19ec6` | 86-127 [crates/gwiki/src/ingest/video/metadata.rs:86-127] | Indexed function `render_raw_video_markdown` in `crates/gwiki/src/ingest/video/metadata.rs`. [crates/gwiki/src/ingest/video/metadata.rs:86-127] |
| `format_timestamp` | function | `pub(crate) fn format_timestamp(seconds: u32) -> String {` | `format_timestamp [function]` | `cd0dca05-9cc7-5c6f-a9d2-87f9d92709fe` | 129-134 [crates/gwiki/src/ingest/video/metadata.rs:129-134] | Indexed function `format_timestamp` in `crates/gwiki/src/ingest/video/metadata.rs`. [crates/gwiki/src/ingest/video/metadata.rs:129-134] |
