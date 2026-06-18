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

`crates/gwiki/src/ingest/audio.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

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
| `FakeTranscriptionClient` | class | 'FakeTranscriptionClient' is a struct likely used as a test double or stub implementation of a transcription client interface. [crates/gwiki/src/ingest/audio.rs:416] |
| `FakeTranscriptionClient::transcribe` | method | 'transcribe' ignores its request argument and returns 'Ok(TranscriptionOutput)' containing a single hard-coded English transcript segment from 2000–4000 ms with model '"fake-stt"', source/task '"en"'/'"transcribe"', and all translation/partial range fields unset or empty. [crates/gwiki/src/ingest/audio.rs:419-440] |
| `ScriptedTranscriptionClient` | class | 'ScriptedTranscriptionClient' is a scripted mock transcription client that keeps queued transcription and English transcription results, queued translation batches, and a shared call log in 'RefCell's for deterministic testing. [crates/gwiki/src/ingest/audio.rs:444-449] |
| `ScriptedTranscriptionClient::new` | method | Constructs a new instance by storing the provided 'TranscriptionOutput' values as 'Ok' entries in a 'RefCell' queue and initializing the 'english', 'translations', and shared 'calls' collections to empty. [crates/gwiki/src/ingest/audio.rs:453-460] |
| `ScriptedTranscriptionClient::with_english` | method | Constructs a new instance with empty 'transcriptions' and 'translations', seeds 'english' by wrapping each provided 'TranscriptionOutput' in 'Ok' inside a 'RefCell', and initializes 'calls' as a shared empty 'Rc<RefCell<Vec<_>>>'. [crates/gwiki/src/ingest/audio.rs:462-469] |
| `ScriptedTranscriptionClient::calls` | method | Returns a cloned 'Rc' handle to the internal 'RefCell<Vec<&'static str>>' containing the recorded calls, allowing shared mutable access to the same underlying list. [crates/gwiki/src/ingest/audio.rs:471-473] |
| `ScriptedTranscriptionClient::transcribe` | method | 'transcribe' records the invocation by appending '"transcribe"' to 'self.calls' and returns the first queued 'TranscriptionOutput' by removing and yielding 'self.transcriptions[0]' as a 'Result', ignoring the request argument. [crates/gwiki/src/ingest/audio.rs:478-484] |
| `ScriptedTranscriptionClient::translate_to_english` | method | 'translate_to_english' appends '"translate_to_english"' to 'self.calls' and returns 'self.english.borrow_mut().remove(0)', ignoring the request and language hint parameters. [crates/gwiki/src/ingest/audio.rs:486-493] |
| `ScriptedTranscriptionClient::translate_segments` | method | Appends '"translate_segments"' to 'self.calls', then returns either a 'Vec<String>' of '"translated {segment.text}"' for each input segment when 'self.translations' is empty, or removes and returns the first preloaded translation vector from 'self.translations'. [crates/gwiki/src/ingest/audio.rs:495-510] |
| `test_context` | function | Constructs an 'AiContext' for tests by creating a single shared 'CapabilityBinding' with the given 'routing' and optional 'api_base' (defaulting model to 'whisper-1') and assigning cloned copies to all AI bindings, with 'AiTuning' set to 'max_concurrency = 1', no keep-alive, a new single-token 'AiLimiter', and no 'project_id'. [crates/gwiki/src/ingest/audio.rs:513-544] |
| `spawn_transcription_server` | function | Spawns a test HTTP server that serves the provided static JSON response string and returns the server URL string with a 'RequestHandle', panicking if server startup fails. [crates/gwiki/src/ingest/audio.rs:547-551] |
| `test_chunk` | function | Constructs and returns an 'AudioChunk' with the given 'start_ms' and 'end_ms', a 'chunk-{start_ms}.wav' file name and path, and fixed 'bytes' set to the ASCII sequence 'wav'. [crates/gwiki/src/ingest/audio.rs:554-562] |
| `transcript_output` | function | Constructs a 'TranscriptionOutput' by cloning the input segment tuples into 'TranscriptSegment' values, setting 'language' to '"en"' when 'translated' is true otherwise 'source_lang', populating metadata fields ('model', 'source_language', 'task', 'target_language'), and initializing all status/range fields to their default empty or false values. [crates/gwiki/src/ingest/audio.rs:565-591] |
| `english_target_uses_primary_language_subtag` | function | Verifies that 'is_english_target' returns 'true' for English targets identified by the primary language subtag in forms like 'en', 'EN-us', and 'en_US', and 'false' for non-matching strings such as 'eng' and 'fr-en'. [crates/gwiki/src/ingest/audio.rs:595-601] |
| `production_transcription_writes_fields` | function | Verifies that 'ingest_audio' records production transcription metadata and transcript content correctly in the generated markdown, including status, target/source languages, model, task, translation flag, and timestamped text, while making a 'POST /v1/audio/transcriptions' request and reporting no degradation. [crates/gwiki/src/ingest/audio.rs:605-639] |
| `production_path_applies_translation` | function | Verifies that translated audio is ingested via the '/v1/audio/translations' production endpoint, produces no transcription degradation, and writes transcript metadata indicating an English transcription from Spanish with 'task: translate' and the translated segment text. [crates/gwiki/src/ingest/audio.rs:643-677] |
| `production_path_chunks_long_audio` | function | Tests that ingesting long overlapping audio chunks produces a transcript file with the completed range metadata '0-10000,9000-19000' and timestamped transcript entries for both chunks at '00:00:00' and '00:00:09'. [crates/gwiki/src/ingest/audio.rs:681-707] |
| `long_media_chunks_then_translates` | function | Creates overlapping long audio chunks, ingests them through a translating transcription endpoint that converts Spanish transcripts to French, and verifies the generated transcript metadata and timestamped translated output are written correctly. [crates/gwiki/src/ingest/audio.rs:711-748] |
| `long_english_translation_per_chunk` | function | Indexed function `long_english_translation_per_chunk` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:752-790] |
| `off_routing_degrades` | function | Indexed function `off_routing_degrades` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:793-824] |
| `stores_original_audio` | function | Indexed function `stores_original_audio` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:827-862] |
| `transcript_chunks_are_scope_searchable` | function | Indexed function `transcript_chunks_are_scope_searchable` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:865-900] |

