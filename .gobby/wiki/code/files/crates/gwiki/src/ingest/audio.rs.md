---
title: crates/gwiki/src/ingest/audio.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/audio.rs
  ranges:
  - 21-28
  - 31-37
  - 39-53
  - 55-80
  - 82-84
  - 87-89
  - 92-94
  - 97-118
  - 121-127
  - 129-140
  - 142-183
  - 185-207
  - 209-215
  - 218-227
  - 230-235
  - 238-259
  - 262-272
  - 274-288
  - 291-298
  - 300-314
  - 316-324
  - 317-323
  - 326-354
  - 374-383
  - 386-392
  - '394'
  - 396-419
  - 397-418
  - 422-427
  - 430-452
  - 431-438
  - 440-447
  - 449-451
  - 455-489
  - 456-462
  - 464-471
  - 473-488
  - 491-518
  - 521-525
  - 528-536
  - 539-565
  - 569-575
  - 579-613
  - 617-651
  - 655-681
  - 685-722
  - 726-764
  - 767-798
  - 801-836
  - 839-874
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/audio.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

`crates/gwiki/src/ingest/audio.rs` exposes 50 indexed API symbols.
[crates/gwiki/src/ingest/audio.rs:21-28]
[crates/gwiki/src/ingest/audio.rs:31-37]
[crates/gwiki/src/ingest/audio.rs:39-53]
[crates/gwiki/src/ingest/audio.rs:55-80]
[crates/gwiki/src/ingest/audio.rs:82-84]
[crates/gwiki/src/ingest/audio.rs:87-89]
[crates/gwiki/src/ingest/audio.rs:92-94]
[crates/gwiki/src/ingest/audio.rs:97-118]
[crates/gwiki/src/ingest/audio.rs:121-127]
[crates/gwiki/src/ingest/audio.rs:129-140]
[crates/gwiki/src/ingest/audio.rs:142-183]
[crates/gwiki/src/ingest/audio.rs:185-207]
[crates/gwiki/src/ingest/audio.rs:209-215]
[crates/gwiki/src/ingest/audio.rs:218-227]
[crates/gwiki/src/ingest/audio.rs:230-235]
[crates/gwiki/src/ingest/audio.rs:238-259]
[crates/gwiki/src/ingest/audio.rs:262-272]
[crates/gwiki/src/ingest/audio.rs:274-288]
[crates/gwiki/src/ingest/audio.rs:291-298]
[crates/gwiki/src/ingest/audio.rs:300-314]
[crates/gwiki/src/ingest/audio.rs:316-324]
[crates/gwiki/src/ingest/audio.rs:317-323]
[crates/gwiki/src/ingest/audio.rs:326-354]
[crates/gwiki/src/ingest/audio.rs:374-383]
[crates/gwiki/src/ingest/audio.rs:386-392]
[crates/gwiki/src/ingest/audio.rs:394]
[crates/gwiki/src/ingest/audio.rs:396-419]
[crates/gwiki/src/ingest/audio.rs:397-418]
[crates/gwiki/src/ingest/audio.rs:422-427]
[crates/gwiki/src/ingest/audio.rs:430-452]
[crates/gwiki/src/ingest/audio.rs:431-438]
[crates/gwiki/src/ingest/audio.rs:440-447]
[crates/gwiki/src/ingest/audio.rs:449-451]
[crates/gwiki/src/ingest/audio.rs:455-489]
[crates/gwiki/src/ingest/audio.rs:456-462]
[crates/gwiki/src/ingest/audio.rs:464-471]
[crates/gwiki/src/ingest/audio.rs:473-488]
[crates/gwiki/src/ingest/audio.rs:491-518]
[crates/gwiki/src/ingest/audio.rs:521-525]
[crates/gwiki/src/ingest/audio.rs:528-536]
[crates/gwiki/src/ingest/audio.rs:539-565]
[crates/gwiki/src/ingest/audio.rs:569-575]
[crates/gwiki/src/ingest/audio.rs:579-613]
[crates/gwiki/src/ingest/audio.rs:617-651]
[crates/gwiki/src/ingest/audio.rs:655-681]
[crates/gwiki/src/ingest/audio.rs:685-722]
[crates/gwiki/src/ingest/audio.rs:726-764]
[crates/gwiki/src/ingest/audio.rs:767-798]
[crates/gwiki/src/ingest/audio.rs:801-836]
[crates/gwiki/src/ingest/audio.rs:839-874]

## API Symbols

- `AudioSnapshot` (class) component `AudioSnapshot [class]` (`003c630c-73fb-540c-89b2-8e5b0c1147a0`) lines 21-28 [crates/gwiki/src/ingest/audio.rs:21-28]
  - Signature: `pub struct AudioSnapshot {`
  - Purpose: `AudioSnapshot` is a struct that encapsulates audio file data as bytes alongside metadata including source location, filename, fetch timestamp, MIME type, and optional duration. [crates/gwiki/src/ingest/audio.rs:21-28]
- `AudioIngestResult` (class) component `AudioIngestResult [class]` (`33266ed3-9a67-5693-913b-32bfa8ee9449`) lines 31-37 [crates/gwiki/src/ingest/audio.rs:31-37]
  - Signature: `pub struct AudioIngestResult {`
  - Purpose: `AudioIngestResult` is a struct that bundles a `SourceRecord` with file paths for raw audio, processed asset, and transcript outputs, plus optional transcription degradation metadata from an audio ingestion operation. [crates/gwiki/src/ingest/audio.rs:31-37]
- `ingest_audio` (function) component `ingest_audio [function]` (`8ab99296-fbaf-5dd3-8f9f-99ab8fe96bc0`) lines 39-53 [crates/gwiki/src/ingest/audio.rs:39-53]
  - Signature: `pub fn ingest_audio(`
  - Purpose: Ingests an audio snapshot into a wiki index store with automatic transcription using a production endpoint derived from the provided AI context. [crates/gwiki/src/ingest/audio.rs:39-53]
- `production_transcription_endpoint` (function) component `production_transcription_endpoint [function]` (`1c5fcf02-79a6-5a2d-9ec7-5f3c73993503`) lines 55-80 [crates/gwiki/src/ingest/audio.rs:55-80]
  - Signature: `pub fn production_transcription_endpoint(`
  - Purpose: Determines a production transcription endpoint by routing audio transcription or translation requests through resolved AI capability routes, returning an available endpoint if the primary or applicable fallback routes are operational, otherwise returning an unavailable endpoint with degradation metadata. [crates/gwiki/src/ingest/audio.rs:55-80]
- `route_available` (function) component `route_available [function]` (`9ec2b79b-51bd-512c-b00d-1cb34421dace`) lines 82-84 [crates/gwiki/src/ingest/audio.rs:82-84]
  - Signature: `fn route_available(route: AiRouting) -> bool {`
  - Purpose: Returns true if the provided AiRouting enum variant is either `Daemon` or `Direct`, false otherwise. [crates/gwiki/src/ingest/audio.rs:82-84]
- `resolved_transcription_route` (function) component `resolved_transcription_route [function]` (`1a694818-0d94-5b68-9dc6-f7d376129947`) lines 87-89 [crates/gwiki/src/ingest/audio.rs:87-89]
  - Signature: `fn resolved_transcription_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: This function resolves the appropriate AI routing strategy for transcription operations by delegating to `gobby_core::ai::effective_route` with the provided context and capability parameters. [crates/gwiki/src/ingest/audio.rs:87-89]
- `resolved_transcription_route` (function) component `resolved_transcription_route [function]` (`d8b9c81e-16f0-525e-b45c-ea826ac266a7`) lines 92-94 [crates/gwiki/src/ingest/audio.rs:92-94]
  - Signature: `fn resolved_transcription_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Retrieves the routing configuration for a given AiCapability by accessing its binding in the provided AiContext. [crates/gwiki/src/ingest/audio.rs:92-94]
- `available_production_transcription_endpoint` (function) component `available_production_transcription_endpoint [function]` (`89389f5c-dbcb-518d-9f74-2ed83242fd3c`) lines 97-118 [crates/gwiki/src/ingest/audio.rs:97-118]
  - Signature: `fn available_production_transcription_endpoint(`
  - Purpose: Constructs a `TranscriptionEndpoint` wrapping a `ProductionTranscriptionClient` that conditionally enables audio translation mode with language configurations from the `AiContext` based on the `translate` flag. [crates/gwiki/src/ingest/audio.rs:97-118]
- `available_production_transcription_endpoint` (function) component `available_production_transcription_endpoint [function]` (`0ca1aa16-1057-5429-b903-5b653255b540`) lines 121-127 [crates/gwiki/src/ingest/audio.rs:121-127]
  - Signature: `fn available_production_transcription_endpoint(`
  - Purpose: This function returns a `TranscriptionEndpoint` in an `Unavailable` state with degradation information computed from the provided routing and translation parameters. [crates/gwiki/src/ingest/audio.rs:121-127]
- `ingest_audio_with_transcription` (function) component `ingest_audio_with_transcription [function]` (`c64a827d-4773-5476-8fe4-e68e4fa4879f`) lines 129-140 [crates/gwiki/src/ingest/audio.rs:129-140]
  - Signature: `pub fn ingest_audio_with_transcription(`
  - Purpose: Ingests an audio snapshot with transcription into a vault and re-indexes the wiki store. [crates/gwiki/src/ingest/audio.rs:129-140]
- `ingest_audio_with_transcription_without_index` (function) component `ingest_audio_with_transcription_without_index [function]` (`e5896bba-3939-5366-85c4-02a6208cb003`) lines 142-183 [crates/gwiki/src/ingest/audio.rs:142-183]
  - Signature: `pub(crate) fn ingest_audio_with_transcription_without_index(`
  - Purpose: Registers an audio source with content hash, persists its asset and raw markdown representation, transcribes via the provided endpoint, and returns ingestion metadata without creating an index. [crates/gwiki/src/ingest/audio.rs:142-183]
- `transcribe_for_markdown` (function) component `transcribe_for_markdown [function]` (`736947d1-dc7e-5b7f-bd3b-ef635bc29351`) lines 185-207 [crates/gwiki/src/ingest/audio.rs:185-207]
  - Signature: `pub(crate) fn transcribe_for_markdown(`
  - Purpose: Routes a transcription request through pattern matching on the endpoint's state (available, unavailable/degraded, or translating) to the appropriate handler, returning markdown-formatted transcription input. [crates/gwiki/src/ingest/audio.rs:185-207]
- `transcription_result_for_markdown` (function) component `transcription_result_for_markdown [function]` (`fca4bbfc-995b-567b-b539-f54445414787`) lines 209-215 [crates/gwiki/src/ingest/audio.rs:209-215]
  - Signature: `fn transcription_result_for_markdown(`
  - Purpose: Transcribes audio using a provided client and converts the result to markdown format with standardized error handling. [crates/gwiki/src/ingest/audio.rs:209-215]
- `transcribe_available` (function) component `transcribe_available [function]` (`d63cb5bc-16ec-5a7b-8c70-cb68a30c51e7`) lines 218-227 [crates/gwiki/src/ingest/audio.rs:218-227]
  - Signature: `fn transcribe_available(`
  - Purpose: Delegates audio transcription to `transcribe_audio_request` using `ChunkTranscriptionMode::Transcribe` with the provided request and client, returning a `TranscriptionOutput` or `WikiError`. [crates/gwiki/src/ingest/audio.rs:218-227]
- `transcribe_available` (function) component `transcribe_available [function]` (`91b17b95-47d0-5529-8671-91a2cd1976e8`) lines 230-235 [crates/gwiki/src/ingest/audio.rs:230-235]
  - Signature: `fn transcribe_available(`
  - Purpose: This function delegates a transcription request to a provided TranscriptionClient trait object and returns the result as either a TranscriptionOutput or WikiError. [crates/gwiki/src/ingest/audio.rs:230-235]
- `translate_for_markdown` (function) component `translate_for_markdown [function]` (`416f6869-3149-5db7-be85-3b2b6f5a8274`) lines 238-259 [crates/gwiki/src/ingest/audio.rs:238-259]
  - Signature: `fn translate_for_markdown(`
  - Purpose: Translates audio to a target language using file-size-adaptive chunked or direct transcription, and returns markdown-formatted output. [crates/gwiki/src/ingest/audio.rs:238-259]
- `translate_for_markdown` (function) component `translate_for_markdown [function]` (`4947a350-58f1-5f97-a75c-5a29afac159e`) lines 262-272 [crates/gwiki/src/ingest/audio.rs:262-272]
  - Signature: `fn translate_for_markdown(`
  - Purpose: Returns a `TranscriptionMarkdownInput::Degraded` stub indicating that translation functionality is unavailable without the AI feature enabled. [crates/gwiki/src/ingest/audio.rs:262-272]
- `transcription_result_to_markdown` (function) component `transcription_result_to_markdown [function]` (`e4414351-617e-50bf-afc8-20ccefe86ffc`) lines 274-288 [crates/gwiki/src/ingest/audio.rs:274-288]
  - Signature: `fn transcription_result_to_markdown(`
  - Purpose: Converts a transcription `Result` into a `TranscriptionMarkdownInput`, mapping `Ok` variants to a transcribed state and `Err` variants to a degraded state with a formatted error fallback message. [crates/gwiki/src/ingest/audio.rs:274-288]
- `is_english_target` (function) component `is_english_target [function]` (`4d99f272-8524-5425-8ca5-549090a16d63`) lines 291-298 [crates/gwiki/src/ingest/audio.rs:291-298]
  - Signature: `fn is_english_target(target_lang: &str) -> bool {`
  - Purpose: This function determines whether the root language component of a language code string (the segment before any '-' or '_' delimiter) is 'en' via case-insensitive ASCII comparison. [crates/gwiki/src/ingest/audio.rs:291-298]
- `transcription_degradation` (function) component `transcription_degradation [function]` (`b16377b5-85a1-5bfd-b320-6912db9c4913`) lines 300-314 [crates/gwiki/src/ingest/audio.rs:300-314]
  - Signature: `fn transcription_degradation(routing: AiRouting, translate: bool) -> TranscriptionDegradation {`
  - Purpose: Creates a `TranscriptionDegradation` structure populated with a routing-dependent failure reason ("disabled" or "missing_endpoint") and a fallback directive to skip transcription or translation and preserve raw audio. [crates/gwiki/src/ingest/audio.rs:300-314]
- `IngestResult` (class) component `IngestResult [class]` (`dd0d16fd-d77f-5bcd-ba10-2184b683bb33`) lines 316-324 [crates/gwiki/src/ingest/audio.rs:316-324]
  - Signature: `impl From<AudioIngestResult> for IngestResult {`
  - Purpose: This trait implementation converts `AudioIngestResult` into `IngestResult` by transferring the `record` and `raw_path` fields while wrapping the `asset_path` field in `Some()`. [crates/gwiki/src/ingest/audio.rs:316-324]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`7a8de00f-1465-5d83-81b0-8cc2f50f7ada`) lines 317-323 [crates/gwiki/src/ingest/audio.rs:317-323]
  - Signature: `fn from(result: AudioIngestResult) -> Self {`
  - Purpose: Converts an `AudioIngestResult` to `Self` by extracting `record` and `raw_path` fields and wrapping `asset_path` in `Some`. [crates/gwiki/src/ingest/audio.rs:317-323]
- `render_raw_audio_markdown` (function) component `render_raw_audio_markdown [function]` (`8a2707e4-bff9-5c84-b4f1-ea93f4730763`) lines 326-354 [crates/gwiki/src/ingest/audio.rs:326-354]
  - Signature: `fn render_raw_audio_markdown(`
  - Purpose: # Summary

Generates a markdown string containing audio metadata fields (source location, fetch timestamp, source hash, MIME type, duration) and asset file path reference from an AudioSnapshot. [crates/gwiki/src/ingest/audio.rs:326-354]
- `sample_snapshot` (function) component `sample_snapshot [function]` (`ada8e408-a04f-5c5e-b948-5783b7397938`) lines 374-383 [crates/gwiki/src/ingest/audio.rs:374-383]
  - Signature: `fn sample_snapshot() -> AudioSnapshot {`
  - Purpose: Instantiates and returns an `AudioSnapshot` struct populated with hardcoded test data representing a 12-second WAV audio file. [crates/gwiki/src/ingest/audio.rs:374-383]
- `long_snapshot` (function) component `long_snapshot [function]` (`74959d6f-ee81-50a9-9ce8-1e900af587e4`) lines 386-392 [crates/gwiki/src/ingest/audio.rs:386-392]
  - Signature: `fn long_snapshot() -> AudioSnapshot {`
  - Purpose: Constructs an `AudioSnapshot` with a byte vector exceeding `MAX_AUDIO_UPLOAD_BYTES` by one byte and a duration of 1200 seconds, using sample values for remaining fields. [crates/gwiki/src/ingest/audio.rs:386-392]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`f49e4d48-e63c-5bae-836a-ac15d7922012`) lines 394-394 [crates/gwiki/src/ingest/audio.rs:394]
  - Signature: `struct FakeTranscriptionClient;`
  - Purpose: FakeTranscriptionClient is a Rust struct serving as a test double or mock implementation of a transcription client interface. [crates/gwiki/src/ingest/audio.rs:394]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`79e6db28-ce89-5196-874e-5b959035d781`) lines 396-419 [crates/gwiki/src/ingest/audio.rs:396-419]
  - Signature: `impl TranscriptionClient for FakeTranscriptionClient {`
  - Purpose: FakeTranscriptionClient is a mock implementation of the TranscriptionClient trait that unconditionally returns a hardcoded English-language TranscriptionOutput with a single transcript segment for testing purposes. [crates/gwiki/src/ingest/audio.rs:396-419]
- `FakeTranscriptionClient.transcribe` (method) component `FakeTranscriptionClient.transcribe [method]` (`aaef4fa3-5eb6-55e0-b463-c628620b62a1`) lines 397-418 [crates/gwiki/src/ingest/audio.rs:397-418]
  - Signature: `fn transcribe(`
  - Purpose: Returns a hardcoded `TranscriptionOutput` with a single English transcript segment spanning 2-4 seconds and 'fake-stt' model metadata, ignoring the input request. [crates/gwiki/src/ingest/audio.rs:397-418]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`c627f246-d280-5f8e-acd0-93b68dcf1d97`) lines 422-427 [crates/gwiki/src/ingest/audio.rs:422-427]
  - Signature: `struct ScriptedTranscriptionClient {`
  - Purpose: ScriptedTranscriptionClient is a test mock that employs RefCell for interior-mutable caching of transcription results and translations, with Rc-wrapped shared call tracking for verifying method invocation order. [crates/gwiki/src/ingest/audio.rs:422-427]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`aef287f7-0c92-5941-b56e-c7364db62bba`) lines 430-452 [crates/gwiki/src/ingest/audio.rs:430-452]
  - Signature: `impl ScriptedTranscriptionClient {`
  - Purpose: `ScriptedTranscriptionClient` is a mock transcription client that stores pre-configured transcription and translation outputs using interior mutability (RefCell) and shared reference counting (Rc) to track method calls during testing. [crates/gwiki/src/ingest/audio.rs:430-452]
- `ScriptedTranscriptionClient.new` (method) component `ScriptedTranscriptionClient.new [method]` (`d3bcd39b-1760-573f-af2b-c03dabbc054d`) lines 431-438 [crates/gwiki/src/ingest/audio.rs:431-438]
  - Signature: `fn new(transcriptions: Vec<TranscriptionOutput>) -> Self {`
  - Purpose: Constructs a new instance by wrapping the input transcriptions as `Ok` results in a `RefCell`, and initializing empty `RefCell`-wrapped vectors for english and translations, plus an `Rc<RefCell<Vec>>`-wrapped vector for calls. [crates/gwiki/src/ingest/audio.rs:431-438]
- `ScriptedTranscriptionClient.with_english` (method) component `ScriptedTranscriptionClient.with_english [method]` (`bfa7b564-b25c-5bfa-93c9-537c665c9ec1`) lines 440-447 [crates/gwiki/src/ingest/audio.rs:440-447]
  - Signature: `fn with_english(english: Vec<TranscriptionOutput>) -> Self {`
  - Purpose: Constructs a new instance with the provided English transcriptions mapped to `Result::Ok` and stored in a `RefCell`, while initializing transcriptions, translations, and calls as empty `RefCell`s. [crates/gwiki/src/ingest/audio.rs:440-447]
- `ScriptedTranscriptionClient.calls` (method) component `ScriptedTranscriptionClient.calls [method]` (`e8d7fbde-4018-5423-903d-47bac3d8d682`) lines 449-451 [crates/gwiki/src/ingest/audio.rs:449-451]
  - Signature: `fn calls(&self) -> Rc<RefCell<Vec<&'static str>>> {`
  - Purpose: Returns a reference-counted handle to an interior-mutable vector of static string references. [crates/gwiki/src/ingest/audio.rs:449-451]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`72ba206f-554a-50fe-96b9-dc9fb1950acb`) lines 455-489 [crates/gwiki/src/ingest/audio.rs:455-489]
  - Signature: `impl TranscriptionClient for ScriptedTranscriptionClient {`
  - Purpose: ScriptedTranscriptionClient is a test mock implementation of TranscriptionClient that records method invocations and returns pre-queued transcription/translation results, with a fallback formatter for segment translations. [crates/gwiki/src/ingest/audio.rs:455-489]
- `ScriptedTranscriptionClient.transcribe` (method) component `ScriptedTranscriptionClient.transcribe [method]` (`56937311-625d-518e-bd64-d14e07762afb`) lines 456-462 [crates/gwiki/src/ingest/audio.rs:456-462]
  - Signature: `fn transcribe(`
  - Purpose: This method logs the invocation and returns the first pre-queued transcription result from an internal collection, ignoring the input request parameter. [crates/gwiki/src/ingest/audio.rs:456-462]
- `ScriptedTranscriptionClient.translate_to_english` (method) component `ScriptedTranscriptionClient.translate_to_english [method]` (`6645a42d-aac5-5187-a60c-92715d64196e`) lines 464-471 [crates/gwiki/src/ingest/audio.rs:464-471]
  - Signature: `fn translate_to_english(`
  - Purpose: This method records its invocation to a call tracker and returns the first TranscriptionOutput from an internal english vector (or a WikiError if empty), functioning as a mock/test implementation. [crates/gwiki/src/ingest/audio.rs:464-471]
- `ScriptedTranscriptionClient.translate_segments` (method) component `ScriptedTranscriptionClient.translate_segments [method]` (`dd21f5e7-4af9-5708-a249-a617a833792e`) lines 473-488 [crates/gwiki/src/ingest/audio.rs:473-488]
  - Signature: `fn translate_segments(`
  - Purpose: Records the method invocation and returns either a pre-configured translation vector from internal state or auto-generates translations by prefixing each segment's text with "translated". [crates/gwiki/src/ingest/audio.rs:473-488]
- `test_context` (function) component `test_context [function]` (`5ed5304a-f262-59db-9c28-9557927bc505`) lines 491-518 [crates/gwiki/src/ingest/audio.rs:491-518]
  - Signature: `fn test_context(routing: AiRouting, api_base: Option<String>) -> AiContext {`
  - Purpose: Creates a test `AiContext` with a unified `CapabilityBinding` configured for the whisper-1 model, bound to all AI capability types (embed, audio transcribe/translate, vision extract, text generate), and set with a concurrency limit of 1. [crates/gwiki/src/ingest/audio.rs:491-518]
- `spawn_transcription_server` (function) component `spawn_transcription_server [function]` (`7cdac59c-df98-5461-acc7-2439fe44069c`) lines 521-525 [crates/gwiki/src/ingest/audio.rs:521-525]
  - Signature: `fn spawn_transcription_server(`
  - Purpose: Spawns a test HTTP server that responds with the provided static JSON string, returning a tuple of the server URL and a request handle. [crates/gwiki/src/ingest/audio.rs:521-525]
- `test_chunk` (function) component `test_chunk [function]` (`c8474b2c-5c94-545b-b725-1e55f62411d7`) lines 528-536 [crates/gwiki/src/ingest/audio.rs:528-536]
  - Signature: `fn test_chunk(start_ms: u64, end_ms: u64) -> crate::ai::chunk::AudioChunk {`
  - Purpose: Constructs a test AudioChunk with the provided start/end millisecond timestamps, auto-generated filename and path derived from start_ms, and dummy WAV byte payload. [crates/gwiki/src/ingest/audio.rs:528-536]
- `transcript_output` (function) component `transcript_output [function]` (`5cd814bd-6b65-5b2c-9117-88cf843d551a`) lines 539-565 [crates/gwiki/src/ingest/audio.rs:539-565]
  - Signature: `fn transcript_output(`
  - Purpose: Constructs a `TranscriptionOutput` from transcript segments and metadata, conditionally setting the output language to English for translated content or the source language otherwise. [crates/gwiki/src/ingest/audio.rs:539-565]
- `english_target_uses_primary_language_subtag` (function) component `english_target_uses_primary_language_subtag [function]` (`0604c271-eb58-5330-a1a5-2b117a1e7be7`) lines 569-575 [crates/gwiki/src/ingest/audio.rs:569-575]
  - Signature: `fn english_target_uses_primary_language_subtag() {`
  - Purpose: This test verifies that `is_english_target()` correctly identifies English language targets using the ISO 639-1 primary language subtag "en" (in various case and delimiter formats) while rejecting non-primary representations such as the three-letter code "eng" and secondary positions like "fr-en". [crates/gwiki/src/ingest/audio.rs:569-575]
- `production_transcription_writes_fields` (function) component `production_transcription_writes_fields [function]` (`69cd9fc1-11ae-5fd9-9639-02ff225e29a0`) lines 579-613 [crates/gwiki/src/ingest/audio.rs:579-613]
  - Signature: `fn production_transcription_writes_fields() {`
  - Purpose: Tests that the `ingest_audio` function correctly writes transcription metadata fields (status, languages, model, task) and timestamped transcript content to the markdown output file when processing audio through the production transcription endpoint. [crates/gwiki/src/ingest/audio.rs:579-613]
- `production_path_applies_translation` (function) component `production_path_applies_translation [function]` (`7d1da0a2-9266-55ee-98a8-0ae1e06096bf`) lines 617-651 [crates/gwiki/src/ingest/audio.rs:617-651]
  - Signature: `fn production_path_applies_translation() {`
  - Purpose: Verifies that audio ingestion with production transcription routing sends a POST request to the /v1/audio/translations endpoint and correctly persists source language, translation task metadata, and translated transcript to markdown output. [crates/gwiki/src/ingest/audio.rs:617-651]
- `production_path_chunks_long_audio` (function) component `production_path_chunks_long_audio [function]` (`b6bf070a-47c2-5921-bf1e-2cd7952f23e0`) lines 655-681 [crates/gwiki/src/ingest/audio.rs:655-681]
  - Signature: `fn production_path_chunks_long_audio() {`
  - Purpose: This function tests the production pathway for ingesting long audio with overlapping chunks by validating that the transcription markdown output contains properly timestamped transcription segments and transcription completion range metadata. [crates/gwiki/src/ingest/audio.rs:655-681]
- `long_media_chunks_then_translates` (function) component `long_media_chunks_then_translates [function]` (`763dad4d-767b-53c2-82ab-6099639f6f46`) lines 685-722 [crates/gwiki/src/ingest/audio.rs:685-722]
  - Signature: `fn long_media_chunks_then_translates() {`
  - Purpose: This function tests the audio ingestion pipeline's ability to transcribe and translate overlapping long-duration audio chunks, verifying that Spanish transcriptions are correctly converted to French with appropriate metadata and timestamps persisted in the output markdown. [crates/gwiki/src/ingest/audio.rs:685-722]
- `long_english_translation_per_chunk` (function) component `long_english_translation_per_chunk [function]` (`214eea78-3327-5c76-ab2a-bbc39a358dff`) lines 726-764 [crates/gwiki/src/ingest/audio.rs:726-764]
  - Signature: `fn long_english_translation_per_chunk() {`
  - Purpose: Tests that `ingest_audio_with_transcription` correctly translates overlapping Spanish audio chunks to English, producing markdown output with proper language metadata, timestamps, and exactly two translation API calls. [crates/gwiki/src/ingest/audio.rs:726-764]
- `off_routing_degrades` (function) component `off_routing_degrades [function]` (`f1ea50d9-f84b-50d8-9a84-8e943b62fd2b`) lines 767-798 [crates/gwiki/src/ingest/audio.rs:767-798]
  - Signature: `fn off_routing_degrades() {`
  - Purpose: Tests that audio ingestion with AI routing disabled degrades gracefully, marking transcription as unavailable with a 'disabled' degradation reason and preserving the original audio bytes. [crates/gwiki/src/ingest/audio.rs:767-798]
- `stores_original_audio` (function) component `stores_original_audio [function]` (`0ac1fa88-5bfa-592e-a16b-bd6efabd8b25`) lines 801-836 [crates/gwiki/src/ingest/audio.rs:801-836]
  - Signature: `fn stores_original_audio() {`
  - Purpose: Test verifying that `ingest_audio` stores original audio bytes at the correct asset path, generates metadata with audio properties (MIME type, duration), and creates a manifest entry with content hash validation. [crates/gwiki/src/ingest/audio.rs:801-836]
- `transcript_chunks_are_scope_searchable` (function) component `transcript_chunks_are_scope_searchable [function]` (`2716028f-eafb-5195-876e-c976c6bdd9ab`) lines 839-874 [crates/gwiki/src/ingest/audio.rs:839-874]
  - Signature: `fn transcript_chunks_are_scope_searchable() {`
  - Purpose: Tests that audio transcription chunks are correctly indexed and searchable by content within a specified project scope context. [crates/gwiki/src/ingest/audio.rs:839-874]

