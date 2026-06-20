---
title: crates/gwiki/src/ingest/audio.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/audio.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/audio.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/audio.rs` exposes 46 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/audio.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AudioSnapshot` | class | 'AudioSnapshot' is a data container for an audio asset snapshot, storing its source location, filename, fetch timestamp, raw bytes, optional MIME type, and optional duration in seconds. [crates/gwiki/src/ingest/audio.rs:21-28] |
| `AudioIngestResult` | class | 'AudioIngestResult' is a Rust data container holding an ingested audio source record plus the filesystem paths to its raw, asset, and transcript outputs, along with an optional 'TranscriptionDegradation' describing transcript quality loss. [crates/gwiki/src/ingest/audio.rs:31-37] |
| `ingest_audio` | function | 'ingest_audio' is a thin wrapper that forwards the provided vault path, index store, scope, and audio snapshot to 'ingest_audio_with_transcription', using a non-production transcription endpoint derived from 'ai_context', and returns the resulting 'AudioIngestResult' or 'WikiError'. [crates/gwiki/src/ingest/audio.rs:40-54] |
| `production_transcription_endpoint` | function | Constructs a production 'TranscriptionEndpoint' for the given 'AiContext' by selecting either audio transcribe or audio translate routing, returning an available endpoint when the required route(s) are supported and otherwise returning an unavailable endpoint with a routing-based degradation fallback. [crates/gwiki/src/ingest/audio.rs:56-87] |
| `route_available` | function | Returns 'true' only when 'route' is 'AiRouting::Daemon' or 'AiRouting::Direct', and 'false' for all other variants. [crates/gwiki/src/ingest/audio.rs:89-91] |
| `resolved_transcription_route` | function | Returns the effective AI routing for the given 'capability' by delegating to 'gobby_core::ai::effective_route(context, capability)'. [crates/gwiki/src/ingest/audio.rs:94-96] |
| `resolved_transcription_route` | function | Returns the 'routing' field from the 'AiContext' binding associated with the given 'AiCapability', producing the resolved 'AiRouting'. [crates/gwiki/src/ingest/audio.rs:99-101] |
| `available_production_transcription_endpoint` | function | Constructs and returns a 'TranscriptionEndpoint' backed by a new 'ProductionTranscriptionClient' cloned from 'context', using the translating variant with 'AudioTranslate.target_lang' and 'AudioTranscribe.language' hints when 'translate' is true, otherwise returning the available variant. [crates/gwiki/src/ingest/audio.rs:104-125] |
| `available_production_transcription_endpoint` | function | Returns an 'Unavailable' 'TranscriptionEndpoint' built from 'TranscriptionDegradation::for_routing(route, transcription_fallback(translate))', indicating the production transcription endpoint is not available for the given routing and translation mode. [crates/gwiki/src/ingest/audio.rs:128-137] |
| `transcription_fallback` | function | Returns a static message indicating that raw audio assets should be kept and daemon processing skipped, choosing “translation” when 'translate' is 'true' and “transcription” otherwise. [crates/gwiki/src/ingest/audio.rs:139-145] |
| `ingest_audio_with_transcription` | function | Ingests an audio snapshot by first running transcription-based ingestion without indexing, then re-indexes the vault store, and returns the resulting 'AudioIngestResult' or a 'WikiError' on failure. [crates/gwiki/src/ingest/audio.rs:148-159] |
| `ingest_audio_with_transcription_without_index` | function | Ingests an audio snapshot into the vault by registering a source record from its content hash, writing the audio asset and raw markdown, then transcribing the audio and returning the resulting record and file paths along with transcription degradation. [crates/gwiki/src/ingest/audio.rs:161-202] |
| `transcribe_for_markdown` | function | Dispatches a transcription request to either produce markdown from an available transcription client, return a degraded marker when unavailable, or invoke translation-to-markdown with the configured target language and language hint. [crates/gwiki/src/ingest/audio.rs:204-226] |
| `transcription_result_for_markdown` | function | Calls 'transcribe_available' with the provided request and client, then converts the result into a 'TranscriptionMarkdownInput', using 'ModalityDegradationReason::TranscriptionError' and the message '"Transcription failed"' if transcription does not succeed. [crates/gwiki/src/ingest/audio.rs:228-238] |
| `transcribe_available` | function | Delegates the transcription request to 'crate::ai::chunk::transcribe_audio_request' using 'ChunkTranscriptionMode::Transcribe', returning the resulting 'TranscriptionOutput' or 'WikiError'. [crates/gwiki/src/ingest/audio.rs:241-250] |
| `transcribe_available` | function | Delegates the provided 'TranscriptionRequest' to the supplied 'TranscriptionClient' by calling 'client.transcribe(request)' and returns its 'TranscriptionOutput' or a 'WikiError'. [crates/gwiki/src/ingest/audio.rs:253-258] |
| `translate_for_markdown` | function | 'translate_for_markdown' translates a transcription request by choosing chunked audio transcription/translation when the input is large or direct translation otherwise, then converts the result into 'TranscriptionMarkdownInput' with translation-error degradation handling and a fixed failure message. [crates/gwiki/src/ingest/audio.rs:261-286] |
| `translate_for_markdown` | function | 'translate_for_markdown' ignores all inputs and returns 'TranscriptionMarkdownInput::Degraded' with 'ModalityDegradationReason::TranslationUnavailable' and the fallback message '"Translation requires the ai feature."' [crates/gwiki/src/ingest/audio.rs:289-299] |
| `transcription_result_to_markdown` | function | Converts a transcription 'Result' into 'TranscriptionMarkdownInput', returning 'Transcribed(output)' for non-empty successful transcriptions and otherwise 'Degraded(TranscriptionDegradation)' with the given reason and a fallback message that preserves raw audio assets and requires supplied transcripts. [crates/gwiki/src/ingest/audio.rs:301-326] |
| `is_english_target` | function | Returns 'true' when the trimmed 'target_lang' string begins with a language subtag equal to 'en' case-insensitively, ignoring any '-' or '_' suffixes, and 'false' otherwise. [crates/gwiki/src/ingest/audio.rs:329-336] |
| `IngestResult::from` | method | Converts an 'AudioIngestResult' into 'Self' by moving 'record' and 'raw_path' directly and storing 'asset_path' as 'Some(result.asset_path)'. [crates/gwiki/src/ingest/audio.rs:339-345] |
| `render_raw_audio_markdown` | function | Builds a markdown document for an audio snapshot by emitting metadata fields for the audio source and optional MIME type/duration, then adding a title from the file name and a note pointing to the stored asset path. [crates/gwiki/src/ingest/audio.rs:348-376] |
| `sample_snapshot` | function | Returns a fixed 'AudioSnapshot' for '/tmp/interview.wav' with filename 'interview.wav', fetch time '2026-05-29T21:15:00Z', WAV bytes, MIME type 'audio/wav', and a 12-second duration. [crates/gwiki/src/ingest/audio.rs:396-405] |
| `long_snapshot` | function | Creates an 'AudioSnapshot' by taking 'sample_snapshot()', overriding 'bytes' with a vector of 'b'a'' whose length is 'crate::ai::chunk::MAX_AUDIO_UPLOAD_BYTES + 1', and setting 'duration_seconds' to 'Some(1_200)'. [crates/gwiki/src/ingest/audio.rs:408-414] |

_13 more symbol(s) not shown — run `gcode outline crates/gwiki/src/ingest/audio.rs` for the full list._

_Verified by 9 in-file unit tests._

