---
title: crates/gwiki/src/ingest/video/metadata.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/metadata.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/metadata.rs

Module: [[code/modules/crates/gwiki/src/ingest/video|crates/gwiki/src/ingest/video]]

## Overview

`crates/gwiki/src/ingest/video/metadata.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/video/metadata.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VideoDegradationContext` | class | 'VideoDegradationContext' is a crate-private struct that encapsulates lifetime-bound configuration data for video degradation, including a slice of video media degradation parameters, an optional reference to transcription degradation settings, and a boolean flag to suppress frame sampling. [crates/gwiki/src/ingest/video/metadata.rs:4-8] |
| `video_media_metadata` | function | This function resolves the absolute path of a video asset, queries the filesystem to retrieve its size, and returns a 'VideoMediaMetadata' struct containing the file size in bytes and the provided optional duration, wrapping any I/O error in a 'WikiError'. [crates/gwiki/src/ingest/video/metadata.rs:10-25] |
| `VideoSnapshotRef` | class | 'VideoSnapshotRef' is a crate-private, lifetime-parameterized struct that holds borrowed references to a video snapshot's metadata, frame samples, image paths, frame descriptions, and transcription data. [crates/gwiki/src/ingest/video/metadata.rs:27-39] |
| `from_snapshot` | function | This constructor instantiates the implementing type by copying scalar values and borrowing reference or option-wrapped fields from a reference to a 'VideoSnapshot'. [crates/gwiki/src/ingest/video/metadata.rs:43-57] |
| `from_file_snapshot` | function | This crate-visible function constructs a new instance of 'Self' by borrowing references to, and copying primitive or dereferenced values from, the fields of a borrowed 'VideoFileSnapshot' instance. [crates/gwiki/src/ingest/video/metadata.rs:59-73] |
| `IngestResult::from` | method | This method converts a 'VideoIngestResult' into an instance of 'Self' by directly transferring the 'record' and 'raw_path' fields and wrapping the 'asset_path' field in a 'Some' option. [crates/gwiki/src/ingest/video/metadata.rs:77-83] |
| `render_raw_video_markdown` | function | This function generates a Markdown string containing structured metadata, a title header, and an asset path reference compiled from a video snapshot, source hash, local asset path, and frame interval. [crates/gwiki/src/ingest/video/metadata.rs:86-127] |
| `format_timestamp` | function | The 'format_timestamp' function converts a duration in seconds, represented as a 32-bit unsigned integer, into a zero-padded 'HH:MM:SS' formatted string. [crates/gwiki/src/ingest/video/metadata.rs:129-134] |

