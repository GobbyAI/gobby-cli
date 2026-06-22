---
title: crates/gwiki/src/ingest/video/processing.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/video/processing.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/video/processing.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/video/processing.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/video/processing.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VideoMediaExtractor` | type | Indexed type `VideoMediaExtractor` in `crates/gwiki/src/ingest/video/processing.rs`. [crates/gwiki/src/ingest/video/processing.rs:18-26] |
| `ProductionVideoMediaExtractor` | class | 'ProductionVideoMediaExtractor' is a crate-private zero-sized struct, likely used as a type-level marker or extractor implementation for production video media handling. [crates/gwiki/src/ingest/video/processing.rs:28] |
| `ProductionVideoMediaExtractor::extract_audio` | method | Delegates to 'crate::media::extract_audio_file(video)' to extract audio from the given video path and return it as a 'NamedTempFile', propagating any 'WikiError'. [crates/gwiki/src/ingest/video/processing.rs:31-33] |
| `ProductionVideoMediaExtractor::sample_frame_images` | method | Delegates to 'crate::media::sample_frame_images' to extract video frame images at the specified 'interval', returning a 'Result' containing a vector of '(u64 timestamp, NamedTempFile)' pairs or a 'WikiError'. [crates/gwiki/src/ingest/video/processing.rs:35-41] |
| `ingest_video_file_with_processing` | function | Ingests a video file by first running the processing-only ingestion pipeline and then reindexing the vault store, returning the resulting 'VideoIngestResult' or propagating any 'WikiError'. [crates/gwiki/src/ingest/video/processing.rs:45-64] |
| `ingest_video_file_with_processing_without_index` | function | Ingests a video file without indexing by using a default or snapshot-provided frame interval, extracting audio for transcription when available, storing transcript output or degradation metadata on the snapshot, and accumulating media/transcription degradations for the final 'VideoIngestResult'. [crates/gwiki/src/ingest/video/processing.rs:66-179] |
| `video_media_degradation` | function | Constructs a 'VideoMediaDegradation' from a media kind and 'WikiError' by stringifying the error, choosing the reason as '"ffmpeg_unavailable"' when the error indicates FFmpeg is unavailable otherwise using the provided fallback reason, and storing the resulting 'kind', 'reason', and 'message'. [crates/gwiki/src/ingest/video/processing.rs:181-197] |
| `message_is_ffmpeg_unavailable` | function | Returns 'true' if the lowercased message contains any known substring indicating FFmpeg is unavailable or missing, otherwise 'false'. [crates/gwiki/src/ingest/video/processing.rs:199-209] |
| `DescribedFrameImages` | class | 'DescribedFrameImages' is a crate-private container that groups parallel vectors of 'VideoFrameSample', 'PathBuf', and 'VideoFrameDescription' values for a set of described frame images. [crates/gwiki/src/ingest/video/processing.rs:212-216] |
| `PendingFrameImage` | class | The 'PendingFrameImage' struct is a crate-private representation of a pending video frame, storing timestamp metadata, an optional description, and the frame's image data within a named temporary file. [crates/gwiki/src/ingest/video/processing.rs:218-223] |
| `describe_frame_images` | function | Iterates over video frame temp files, converts each frame timestamp to a formatted second-resolution label, optionally sends the JPEG bytes to a vision client for description extraction, suppresses blank or failed descriptions with a warning, and returns a 'DescribedFrameImages' collection or 'WikiError'. [crates/gwiki/src/ingest/video/processing.rs:225-333] |
| `cleanup_kept_temp_frames` | function | This function iterates over a slice of filesystem paths and attempts to delete each corresponding file, ignoring any errors that may occur during the deletion process. [crates/gwiki/src/ingest/video/processing.rs:335-339] |

