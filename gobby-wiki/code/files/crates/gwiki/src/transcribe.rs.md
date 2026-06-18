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

`crates/gwiki/src/transcribe.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TranscriptSegment` | class | Indexed class `TranscriptSegment` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:14-18] |
| `TranscriptionRange` | class | Indexed class `TranscriptionRange` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:21-24] |
| `TranscriptionOutput` | class | Indexed class `TranscriptionOutput` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:27-39] |
| `TranscriptionDegradation` | class | Indexed class `TranscriptionDegradation` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:42-45] |
| `TranscriptionDegradation::for_routing` | method | Indexed method `TranscriptionDegradation::for_routing` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:48-59] |
| `transcription_output_is_empty` | function | Indexed function `transcription_output_is_empty` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:66-71] |
| `TranscriptionClient` | type | Indexed type `TranscriptionClient` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:73-101] |
| `TranscriptionClient.translate_to_english` | method | Indexed method `TranscriptionClient.translate_to_english` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:80-88] |
| `TranscriptionClient.translate_segments` | method | Indexed method `TranscriptionClient.translate_segments` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:91-100] |
| `TranscriptionRequest` | class | Indexed class `TranscriptionRequest` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:104-109] |
| `TranscriptionEndpoint` | type | Indexed type `TranscriptionEndpoint` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:111-121] |
| `TranscriptionMarkdownResult` | class | Indexed class `TranscriptionMarkdownResult` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:124-127] |
| `TranscriptionMarkdownInput` | type | Indexed type `TranscriptionMarkdownInput` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:130-133] |
| `write_audio_transcript_markdown` | function | Indexed function `write_audio_transcript_markdown` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:135-183] |
| `write_transcript_markdown_atomically` | function | Indexed function `write_transcript_markdown_atomically` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:185-209] |
| `create_transcript_temp_file` | function | Indexed function `create_transcript_temp_file` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:211-238] |
| `sync_parent_dir` | function | Indexed function `sync_parent_dir` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:240-259] |
| `render_audio_transcript_markdown` | function | Indexed function `render_audio_transcript_markdown` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:261-391] |
| `format_timestamp_ms` | function | Indexed function `format_timestamp_ms` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:393-399] |
| `format_ranges_ms` | function | Indexed function `format_ranges_ms` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:401-407] |
| `FakeTranscriptionClient` | class | Indexed class `FakeTranscriptionClient` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:416-418] |
| `FakeTranscriptionClient::transcribe` | method | Indexed method `FakeTranscriptionClient::transcribe` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:421-450] |
| `record_for` | function | Indexed function `record_for` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:453-469] |
| `writes_timestamped_transcript` | function | Indexed function `writes_timestamped_transcript` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:472-528] |
| `renders_precomputed_output_without_transcribing` | function | Indexed function `renders_precomputed_output_without_transcribing` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:531-590] |
| `missing_transcription_degrades` | function | Indexed function `missing_transcription_degrades` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:593-633] |
| `empty_transcript_degrades` | function | Indexed function `empty_transcript_degrades` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:636-681] |

