---
title: crates/gwiki/src/transcribe.rs
type: code_file
provenance:
- file: crates/gwiki/src/transcribe.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/transcribe.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/transcribe.rs` exposes 27 indexed API symbols.

## How it fits

`crates/gwiki/src/transcribe.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TranscriptSegment` | class | 'TranscriptSegment' is a data structure representing a transcript interval with millisecond start and end timestamps ('u64') and the associated text content ('String'). [crates/gwiki/src/transcribe.rs:14-18] |
| `TranscriptionRange` | class | 'TranscriptionRange' is a data structure representing a time interval in milliseconds, with inclusive 'start_ms' and 'end_ms' bounds stored as 'u64' values. [crates/gwiki/src/transcribe.rs:21-24] |
| `TranscriptionOutput` | class | 'TranscriptionOutput' is a transcription result container holding the produced 'TranscriptSegment's plus optional metadata about language, model, source/target languages, and task, along with status flags for translation/partial completion and range lists indicating completed and missing portions of the transcript. [crates/gwiki/src/transcribe.rs:27-39] |
| `TranscriptionDegradation` | class | 'TranscriptionDegradation' is a struct that records a transcription fallback by pairing a 'ModalityDegradationReason' with the 'String' used as the fallback output. [crates/gwiki/src/transcribe.rs:42-45] |
| `TranscriptionDegradation::for_routing` | method | 'for_routing' constructs a 'Self' value by mapping 'AiRouting::Off' to 'ModalityDegradationReason::Disabled' and all other routing modes to 'ModalityDegradationReason::MissingEndpoint', then storing 'fallback' as an owned 'String'. [crates/gwiki/src/transcribe.rs:48-59] |
| `transcription_output_is_empty` | function | Returns 'true' if every segment in 'output.segments' has 'text' that is empty or whitespace-only after trimming, and 'false' otherwise. [crates/gwiki/src/transcribe.rs:66-71] |
| `TranscriptionClient` | type | Indexed type `TranscriptionClient` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:73-101] |
| `TranscriptionClient.translate_to_english` | method | 'translate_to_english' is a stub implementation that ignores its inputs and immediately returns 'Err(WikiError::Config { detail: "audio translation is not configured" })'. [crates/gwiki/src/transcribe.rs:80-88] |
| `TranscriptionClient.translate_segments` | method | 'translate_segments' always returns 'Err(WikiError::Config { detail: "text translation is not configured" })' and never translates the provided transcript segments. [crates/gwiki/src/transcribe.rs:91-100] |
| `TranscriptionRequest` | class | 'TranscriptionRequest<'a>' is a borrowed request payload for transcription that carries the source file name, optional MIME type, asset path, and raw file bytes. [crates/gwiki/src/transcribe.rs:104-109] |
| `TranscriptionEndpoint` | type | Indexed type `TranscriptionEndpoint` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:111-121] |
| `TranscriptionMarkdownResult` | class | 'TranscriptionMarkdownResult' is a result record containing the output markdown file path and an optional 'TranscriptionDegradation' describing any quality loss during transcription. [crates/gwiki/src/transcribe.rs:124-127] |
| `TranscriptionMarkdownInput` | type | Indexed type `TranscriptionMarkdownInput` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:130-133] |
| `write_audio_transcript_markdown` | function | Creates the derived markdown path for an audio record, ensures its parent directory exists, renders transcript markdown from an optional transcription or degradation state, writes it atomically to disk under 'vault_root', and վերադարձs the relative path plus any degradation metadata. [crates/gwiki/src/transcribe.rs:135-183] |
| `write_transcript_markdown_atomically` | function | Writes 'contents' to a temporary transcript Markdown file, fsyncs it, atomically renames it into 'path', and then syncs the parent directory, returning a 'WikiError::Io' on any filesystem failure. [crates/gwiki/src/transcribe.rs:185-209] |
| `create_transcript_temp_file` | function | Creates a temporary file in the target path’s parent directory using a '.{filename}.' prefix and '.tmp' suffix, or returns a 'WikiError::Io' if the path has no parent directory or tempfile creation fails. [crates/gwiki/src/transcribe.rs:211-238] |
| `sync_parent_dir` | function | On Unix, this function opens 'path'’s parent directory and calls 'sync_all()' to flush directory metadata to disk, returning a 'WikiError::Io' on failure, while on non-Unix platforms it is a no-op that returns 'Ok(())'. [crates/gwiki/src/transcribe.rs:240-259] |
| `render_audio_transcript_markdown` | function | 'render_audio_transcript_markdown' serializes an audio transcript and its available metadata into a Markdown string, including frontmatter-like fields for source, scope, transcription status, audio properties, and optional transcription details. [crates/gwiki/src/transcribe.rs:261-391] |
| `format_timestamp_ms` | function | Converts a millisecond timestamp to an 'HH:MM:SS' string by truncating to whole seconds and zero-padding hours, minutes, and seconds to two digits each. [crates/gwiki/src/transcribe.rs:393-399] |
| `format_ranges_ms` | function | Formats a slice of 'TranscriptionRange' values into a comma-separated string of 'start_ms-end_ms' pairs. [crates/gwiki/src/transcribe.rs:401-407] |
| `FakeTranscriptionClient` | class | 'FakeTranscriptionClient' is a struct containing a 'Cell<usize>' named 'calls' used to track the number of transcription client invocations with interior mutability. [crates/gwiki/src/transcribe.rs:416-418] |
| `FakeTranscriptionClient::transcribe` | method | 'transcribe' increments an internal call counter and returns a fixed 'TranscriptionOutput' containing two English transcript segments with hardcoded timestamps/text plus metadata ('model="fake-stt"', 'task="transcribe"', 'translated=false', 'partial=false'). [crates/gwiki/src/transcribe.rs:421-450] |
| `record_for` | function | Registers an 'Audio' 'SourceDraft' for '/tmp/interview.wav' in 'SourceManifest' with fixed metadata, manual ingestion, and pending compile status, then returns the resulting 'SourceRecord' or panics if registration fails. [crates/gwiki/src/transcribe.rs:453-469] |

_Verified by 4 in-file unit tests._

