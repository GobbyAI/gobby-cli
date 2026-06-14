---
title: crates/gwiki/src/ingest/audio.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/audio.rs
  ranges:
  - 21-28
  - 31-37
  - 40-54
  - 56-87
  - 89-91
  - 94-96
  - 99-101
  - 104-125
  - 128-137
  - 139-145
  - 148-159
  - 161-202
  - 204-226
  - 228-238
  - 241-250
  - 253-258
  - 261-286
  - 289-299
  - 301-326
  - 329-336
  - 338-346
  - 348-376
  - 396-405
  - 408-414
  - '416'
  - 418-441
  - 444-449
  - 452-474
  - 477-511
  - 513-541
  - 544-548
  - 551-559
  - 562-588
  - 592-598
  - 602-636
  - 640-674
  - 678-704
  - 708-745
  - 749-787
  - 790-821
  - 824-859
  - 862-897
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/audio.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

This file implements audio ingestion for gwiki: it defines `AudioSnapshot` and `AudioIngestResult` as the input and output data shapes, then wires `ingest_audio` through production transcription routing into `ingest_audio_with_transcription`, which stores the raw audio, generates raw markdown metadata, transcribes or translates the content into transcript markdown, and rebuilds the wiki index. The routing helpers decide whether production transcription is available, whether translation can fall back through transcribe-plus-text generation, and what degradation metadata to attach when transcription is unavailable. The markdown conversion helpers turn successful transcription output into searchable transcript content or degrade to retained-raw-audio notes on failure or unsupported routing. The bottom of the file is mostly test support: fake and scripted transcription clients, test fixtures for audio snapshots and transcript outputs, and integration-style tests that verify direct transcription, translation, chunking, degradation, storage, and search indexing behavior.
[crates/gwiki/src/ingest/audio.rs:21-28]
[crates/gwiki/src/ingest/audio.rs:31-37]
[crates/gwiki/src/ingest/audio.rs:40-54]
[crates/gwiki/src/ingest/audio.rs:56-87]
[crates/gwiki/src/ingest/audio.rs:89-91]

## API Symbols

- `AudioSnapshot` (class) component `AudioSnapshot [class]` (`003c630c-73fb-540c-89b2-8e5b0c1147a0`) lines 21-28 [crates/gwiki/src/ingest/audio.rs:21-28]
  - Signature: `pub struct AudioSnapshot {`
  - Purpose: 'AudioSnapshot' is a data container for a fetched audio asset, storing its source location, file name, retrieval timestamp, raw bytes, optional MIME type, and optional duration in seconds. [crates/gwiki/src/ingest/audio.rs:21-28]
- `AudioIngestResult` (class) component `AudioIngestResult [class]` (`33266ed3-9a67-5693-913b-32bfa8ee9449`) lines 31-37 [crates/gwiki/src/ingest/audio.rs:31-37]
  - Signature: `pub struct AudioIngestResult {`
  - Purpose: 'AudioIngestResult' is a data carrier for an ingested audio source, bundling the associated 'SourceRecord' with filesystem paths to the raw audio, derived asset, and transcript artifacts, plus optional 'TranscriptionDegradation' metadata. [crates/gwiki/src/ingest/audio.rs:31-37]
- `ingest_audio` (function) component `ingest_audio [function]` (`c6476a84-0ff8-5c83-9c94-4711a935eea8`) lines 40-54 [crates/gwiki/src/ingest/audio.rs:40-54]
  - Signature: `pub fn ingest_audio(`
  - Purpose: 'ingest_audio' delegates audio ingestion to 'ingest_audio_with_transcription', passing the vault root, index store, scope, snapshot, and a production transcription endpoint derived from 'ai_context' with 'false' for the second argument. [crates/gwiki/src/ingest/audio.rs:40-54]
- `production_transcription_endpoint` (function) component `production_transcription_endpoint [function]` (`ac34e907-e976-5cee-95fe-1bb6b882663a`) lines 56-87 [crates/gwiki/src/ingest/audio.rs:56-87]
  - Signature: `pub fn production_transcription_endpoint(`
  - Purpose: Returns a production transcription endpoint for the given 'AiContext' by resolving the appropriate audio route, allowing translation only when either the translate route is available or transcribe-plus-text generation fallback is available, and otherwise returning an 'Unavailable' degradation. [crates/gwiki/src/ingest/audio.rs:56-87]
- `route_available` (function) component `route_available [function]` (`cc4c7b6a-742d-5e8a-bb61-f7e3c21d2825`) lines 89-91 [crates/gwiki/src/ingest/audio.rs:89-91]
  - Signature: `fn route_available(route: AiRouting) -> bool {`
  - Purpose: Returns 'true' only when 'route' is 'AiRouting::Daemon' or 'AiRouting::Direct', and 'false' for all other variants. [crates/gwiki/src/ingest/audio.rs:89-91]
- `resolved_transcription_route` (function) component `resolved_transcription_route [function]` (`4aa3d418-19e9-5e46-956b-717bb5df5f6d`) lines 94-96 [crates/gwiki/src/ingest/audio.rs:94-96]
  - Signature: `fn resolved_transcription_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: 'resolved_transcription_route' returns the effective AI routing for the given 'AiContext' and 'AiCapability' by directly delegating to 'gobby_core::ai::effective_route'. [crates/gwiki/src/ingest/audio.rs:94-96]
- `resolved_transcription_route` (function) component `resolved_transcription_route [function]` (`d10dacab-01b7-5a51-bfe5-df484c9399e6`) lines 99-101 [crates/gwiki/src/ingest/audio.rs:99-101]
  - Signature: `fn resolved_transcription_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: 'resolved_transcription_route' returns the 'routing' value from the 'AiContext' binding associated with the given 'AiCapability'. [crates/gwiki/src/ingest/audio.rs:99-101]
- `available_production_transcription_endpoint` (function) component `available_production_transcription_endpoint [function]` (`808b0692-32d9-50f4-a5a9-2b2ebff56db8`) lines 104-125 [crates/gwiki/src/ingest/audio.rs:104-125]
  - Signature: `fn available_production_transcription_endpoint(`
  - Purpose: Creates a 'ProductionTranscriptionClient' from a cloned 'AiContext' and returns either an 'Available' transcription endpoint or a 'Translating' endpoint populated with the audio-translate target language and audio-transcribe language hint depending on the 'translate' flag. [crates/gwiki/src/ingest/audio.rs:104-125]
- `available_production_transcription_endpoint` (function) component `available_production_transcription_endpoint [function]` (`5de176c9-2796-546f-8c19-126f9e96ebca`) lines 128-137 [crates/gwiki/src/ingest/audio.rs:128-137]
  - Signature: `fn available_production_transcription_endpoint(`
  - Purpose: Returns an 'Unavailable' 'TranscriptionEndpoint' for the given routing context, wrapping a routing-specific 'TranscriptionDegradation' built from 'transcription_fallback(translate)'. [crates/gwiki/src/ingest/audio.rs:128-137]
- `transcription_fallback` (function) component `transcription_fallback [function]` (`2834d8b5-a541-55fd-9288-c55e623cbb09`) lines 139-145 [crates/gwiki/src/ingest/audio.rs:139-145]
  - Signature: `fn transcription_fallback(translate: bool) -> &'static str {`
  - Purpose: Returns a static fallback message that depends on 'translate': '"Keep raw audio assets and skip daemon translation."' when 'translate' is 'true', otherwise '"Keep raw audio assets and skip daemon transcription."' [crates/gwiki/src/ingest/audio.rs:139-145]
- `ingest_audio_with_transcription` (function) component `ingest_audio_with_transcription [function]` (`5b21522b-ad17-5a68-8968-9327904e4c3d`) lines 148-159 [crates/gwiki/src/ingest/audio.rs:148-159]
  - Signature: `pub fn ingest_audio_with_transcription(`
  - Purpose: Calls 'ingest_audio_with_transcription_without_index' to ingest and transcribe an audio snapshot, then rebuilds the wiki index via 'index_after_ingest' before returning the resulting 'AudioIngestResult'. [crates/gwiki/src/ingest/audio.rs:148-159]
- `ingest_audio_with_transcription_without_index` (function) component `ingest_audio_with_transcription_without_index [function]` (`02d14539-2527-53e3-a472-18449d0abb5d`) lines 161-202 [crates/gwiki/src/ingest/audio.rs:161-202]
  - Signature: `pub(crate) fn ingest_audio_with_transcription_without_index(`
  - Purpose: Registers an audio source draft keyed by its content hash, writes the audio asset and raw markdown, transcribes the audio into markdown for the given scope, and returns the resulting file paths plus any transcription degradation metadata. [crates/gwiki/src/ingest/audio.rs:161-202]
- `transcribe_for_markdown` (function) component `transcribe_for_markdown [function]` (`3543c95c-df70-5fa5-9de5-b2376e07fccc`) lines 204-226 [crates/gwiki/src/ingest/audio.rs:204-226]
  - Signature: `pub(crate) fn transcribe_for_markdown(`
  - Purpose: Dispatches a transcription request to either produce markdown from an available transcription client, return a degraded markdown input when the endpoint is unavailable, or route through translation-to-markdown using the provided target language and language hint. [crates/gwiki/src/ingest/audio.rs:204-226]
- `transcription_result_for_markdown` (function) component `transcription_result_for_markdown [function]` (`5acbbdbd-c6e7-548a-b0b4-5afdf7a9952a`) lines 228-238 [crates/gwiki/src/ingest/audio.rs:228-238]
  - Signature: `fn transcription_result_for_markdown(`
  - Purpose: Calls 'transcribe_available' with the provided request and client, then converts the result into 'TranscriptionMarkdownInput' using the 'TranscriptionError' degradation reason and the fallback message '"Transcription failed"'. [crates/gwiki/src/ingest/audio.rs:228-238]
- `transcribe_available` (function) component `transcribe_available [function]` (`fcf5a57b-0932-5058-b450-a6a5a63c7786`) lines 241-250 [crates/gwiki/src/ingest/audio.rs:241-250]
  - Signature: `fn transcribe_available(`
  - Purpose: 'transcribe_available' forwards a 'TranscriptionRequest' and 'TranscriptionClient' to 'crate::ai::chunk::transcribe_audio_request' with 'ChunkTranscriptionMode::Transcribe', returning the resulting 'TranscriptionOutput' or 'WikiError'. [crates/gwiki/src/ingest/audio.rs:241-250]
- `transcribe_available` (function) component `transcribe_available [function]` (`d7adbabe-c8ce-5efc-bfc0-d6d3c6cdbf7e`) lines 253-258 [crates/gwiki/src/ingest/audio.rs:253-258]
  - Signature: `fn transcribe_available(`
  - Purpose: 'transcribe_available' delegates the given 'TranscriptionRequest' to the provided 'TranscriptionClient' by calling 'client.transcribe(request)' and returns the resulting 'TranscriptionOutput' or 'WikiError'. [crates/gwiki/src/ingest/audio.rs:253-258]
- `translate_for_markdown` (function) component `translate_for_markdown [function]` (`5a3b5953-e6a2-51ac-acae-6cba2367b755`) lines 261-286 [crates/gwiki/src/ingest/audio.rs:261-286]
  - Signature: `fn translate_for_markdown(`
  - Purpose: 'translate_for_markdown' chooses between chunked transcription-based translation and direct audio translation based on input size, then converts the resulting transcription outcome into a 'TranscriptionMarkdownInput' with 'TranslationError' degradation metadata and a '"Translation failed"' fallback message. [crates/gwiki/src/ingest/audio.rs:261-286]
- `translate_for_markdown` (function) component `translate_for_markdown [function]` (`d8187d6d-cd9e-56c5-ad05-4663eddd5930`) lines 289-299 [crates/gwiki/src/ingest/audio.rs:289-299]
  - Signature: `fn translate_for_markdown(`
  - Purpose: 'translate_for_markdown' ignores its request, client, and language parameters and returns a 'TranscriptionMarkdownInput::Degraded' value indicating 'TranslationUnavailable' with the fallback message '"Translation requires the ai feature."' [crates/gwiki/src/ingest/audio.rs:289-299]
- `transcription_result_to_markdown` (function) component `transcription_result_to_markdown [function]` (`3786153c-d3b1-59db-9482-6a79a93a45ca`) lines 301-326 [crates/gwiki/src/ingest/audio.rs:301-326]
  - Signature: `fn transcription_result_to_markdown(`
  - Purpose: It converts a transcription 'Result' into 'TranscriptionMarkdownInput', returning 'Transcribed(output)' for non-empty successes and otherwise degrading with the given reason plus a fallback message that instructs callers to retain raw audio assets and require supplied transcripts. [crates/gwiki/src/ingest/audio.rs:301-326]
- `is_english_target` (function) component `is_english_target [function]` (`88bec159-4771-550b-9f29-22b89d007f2a`) lines 329-336 [crates/gwiki/src/ingest/audio.rs:329-336]
  - Signature: `fn is_english_target(target_lang: &str) -> bool {`
  - Purpose: Returns 'true' when the trimmed 'target_lang' begins with a language subtag equal to 'en' case-insensitively, treating '-' and '_' as subtag separators. [crates/gwiki/src/ingest/audio.rs:329-336]
- `IngestResult` (class) component `IngestResult [class]` (`99ca6ef0-2635-56c1-9242-365cee771a29`) lines 338-346 [crates/gwiki/src/ingest/audio.rs:338-346]
  - Signature: `impl From<AudioIngestResult> for IngestResult {`
  - Purpose: 'IngestResult' is a conversion target for 'AudioIngestResult' that moves over 'record' and 'raw_path' unchanged while wrapping 'asset_path' in 'Some(...)' to populate the corresponding optional field. [crates/gwiki/src/ingest/audio.rs:338-346]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`b9f5cee3-9599-5a66-b7f6-2e9328d97725`) lines 339-345 [crates/gwiki/src/ingest/audio.rs:339-345]
  - Signature: `fn from(result: AudioIngestResult) -> Self {`
  - Purpose: Constructs 'Self' by moving 'result.record' and 'result.raw_path' through unchanged and wrapping 'result.asset_path' in 'Some' for the 'asset_path' field. [crates/gwiki/src/ingest/audio.rs:339-345]
- `render_raw_audio_markdown` (function) component `render_raw_audio_markdown [function]` (`abcbd023-5ca6-5268-8972-4c4d361d8fbe`) lines 348-376 [crates/gwiki/src/ingest/audio.rs:348-376]
  - Signature: `fn render_raw_audio_markdown(`
  - Purpose: Builds a markdown document for an audio snapshot by emitting metadata fields for the source, hash, asset path, and optional MIME type/duration, then appending a title from the file name and a short note pointing to the stored audio asset. [crates/gwiki/src/ingest/audio.rs:348-376]
- `sample_snapshot` (function) component `sample_snapshot [function]` (`5eaf7359-6733-56b6-9ce1-e6399953a579`) lines 396-405 [crates/gwiki/src/ingest/audio.rs:396-405]
  - Signature: `fn sample_snapshot() -> AudioSnapshot {`
  - Purpose: Constructs and returns an 'AudioSnapshot' for '/tmp/interview.wav' with a WAVE byte payload, MIME type 'audio/wav', a fetch timestamp of '2026-05-29T21:15:00Z', and an optional duration of 12 seconds. [crates/gwiki/src/ingest/audio.rs:396-405]
- `long_snapshot` (function) component `long_snapshot [function]` (`40f82c5d-4153-52c1-84dc-c1cbada0d6f4`) lines 408-414 [crates/gwiki/src/ingest/audio.rs:408-414]
  - Signature: `fn long_snapshot() -> AudioSnapshot {`
  - Purpose: Creates an 'AudioSnapshot' seeded from 'sample_snapshot()' but with 'bytes' set to a buffer of 'b'a'' repeated 'MAX_AUDIO_UPLOAD_BYTES + 1' times and 'duration_seconds' set to 'Some(1_200)'. [crates/gwiki/src/ingest/audio.rs:408-414]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`8d6ba8a4-6750-57e6-8b15-e4b23eefc31d`) lines 416-416 [crates/gwiki/src/ingest/audio.rs:416]
  - Signature: `struct FakeTranscriptionClient;`
  - Purpose: 'FakeTranscriptionClient' is a placeholder 'struct' type representing a mock transcription client, with no fields or behavior specified in the given signature. [crates/gwiki/src/ingest/audio.rs:416]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`83995412-5c6c-5d42-9550-d509eb717353`) lines 418-441 [crates/gwiki/src/ingest/audio.rs:418-441]
  - Signature: `impl TranscriptionClient for FakeTranscriptionClient {`
  - Purpose: 'FakeTranscriptionClient' is a test 'TranscriptionClient' implementation that ignores the request and returns a fixed English 'TranscriptionOutput' with one hard-coded segment, metadata, and no partial or missing ranges. [crates/gwiki/src/ingest/audio.rs:418-441]
- `FakeTranscriptionClient.transcribe` (method) component `FakeTranscriptionClient.transcribe [method]` (`fe3609ae-bad2-58a4-8d24-db958d5cec95`) lines 419-440 [crates/gwiki/src/ingest/audio.rs:419-440]
  - Signature: `fn transcribe(`
  - Purpose: 'transcribe' ignores the request and returns a fixed successful 'TranscriptionOutput' containing one English segment from 2000 to 4000 ms with the text '"Scope searchable hydrophone transcript phrase."', marked as non-translated, non-partial, and using the fake model '"fake-stt"'. [crates/gwiki/src/ingest/audio.rs:419-440]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`b2adc447-ecd8-5ec1-9dc0-8631f390fcdb`) lines 444-449 [crates/gwiki/src/ingest/audio.rs:444-449]
  - Signature: `struct ScriptedTranscriptionClient {`
  - Purpose: 'ScriptedTranscriptionClient' is a stateful test double that records method invocations and returns pre-scripted transcription and translation results from interior-mutable queues. [crates/gwiki/src/ingest/audio.rs:444-449]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`0ce2fc6f-440e-5f71-9d92-58f44a6f091c`) lines 452-474 [crates/gwiki/src/ingest/audio.rs:452-474]
  - Signature: `impl ScriptedTranscriptionClient {`
  - Purpose: 'ScriptedTranscriptionClient' is a test double that initializes mutable queues of scripted transcription or English outputs and records invoked method names in a shared call log. [crates/gwiki/src/ingest/audio.rs:452-474]
- `ScriptedTranscriptionClient.new` (method) component `ScriptedTranscriptionClient.new [method]` (`fbead57d-4850-5534-9ad2-9ca0989dcc45`) lines 453-460 [crates/gwiki/src/ingest/audio.rs:453-460]
  - Signature: `fn new(transcriptions: Vec<TranscriptionOutput>) -> Self {`
  - Purpose: Creates a new instance by wrapping the provided 'TranscriptionOutput' values as 'Ok' entries in a 'RefCell'-backed transcription queue, initializing empty 'english' and 'translations' buffers, and allocating an empty shared 'calls' log in 'Rc<RefCell<_>>'. [crates/gwiki/src/ingest/audio.rs:453-460]
- `ScriptedTranscriptionClient.with_english` (method) component `ScriptedTranscriptionClient.with_english [method]` (`facf006b-b0ec-5ed5-8a89-7cb9fce2f1d3`) lines 462-469 [crates/gwiki/src/ingest/audio.rs:462-469]
  - Signature: `fn with_english(english: Vec<TranscriptionOutput>) -> Self {`
  - Purpose: Constructs a new instance with empty 'transcriptions' and 'translations', initializes 'english' as a 'RefCell<Vec<Result<TranscriptionOutput, _>>>' by wrapping each input item in 'Ok', and creates an empty shared 'calls' log. [crates/gwiki/src/ingest/audio.rs:462-469]
- `ScriptedTranscriptionClient.calls` (method) component `ScriptedTranscriptionClient.calls [method]` (`3a43edfc-8c11-5b83-9cf4-0db0d54783af`) lines 471-473 [crates/gwiki/src/ingest/audio.rs:471-473]
  - Signature: `fn calls(&self) -> Rc<RefCell<Vec<&'static str>>> {`
  - Purpose: Returns a cloned 'Rc' handle to the internal 'RefCell<Vec<&'static str>>' call log, allowing shared access to the same underlying vector. [crates/gwiki/src/ingest/audio.rs:471-473]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`f114a1d7-aee2-55a2-a3ac-a5f93f00d76d`) lines 477-511 [crates/gwiki/src/ingest/audio.rs:477-511]
  - Signature: `impl TranscriptionClient for ScriptedTranscriptionClient {`
  - Purpose: 'ScriptedTranscriptionClient' is a test double for 'TranscriptionClient' that records each method invocation and returns preloaded transcription, English-translation, or segment-translation results from internal queues, falling back to '"translated {text}"' for segment translation when no scripted translations remain. [crates/gwiki/src/ingest/audio.rs:477-511]
- `ScriptedTranscriptionClient.transcribe` (method) component `ScriptedTranscriptionClient.transcribe [method]` (`26fd6bf4-6e60-59a2-b5b5-5df3c497d33a`) lines 478-484 [crates/gwiki/src/ingest/audio.rs:478-484]
  - Signature: `fn transcribe(`
  - Purpose: Records the '"transcribe"' call in 'self.calls' and returns the first queued 'TranscriptionOutput' by removing and yielding 'self.transcriptions[0]', propagating any 'WikiError'. [crates/gwiki/src/ingest/audio.rs:478-484]
- `ScriptedTranscriptionClient.translate_to_english` (method) component `ScriptedTranscriptionClient.translate_to_english [method]` (`e2fd85d2-1c28-577e-a33e-a828028b4229`) lines 486-493 [crates/gwiki/src/ingest/audio.rs:486-493]
  - Signature: `fn translate_to_english(`
  - Purpose: Records the '"translate_to_english"' call in 'self.calls' and returns the first 'TranscriptionOutput' from 'self.english' by removing index '0', ignoring both '_request' and '_language_hint' and propagating any 'WikiError'. [crates/gwiki/src/ingest/audio.rs:486-493]
- `ScriptedTranscriptionClient.translate_segments` (method) component `ScriptedTranscriptionClient.translate_segments [method]` (`58740a20-3822-5006-9132-81f3edc5bd88`) lines 495-510 [crates/gwiki/src/ingest/audio.rs:495-510]
  - Signature: `fn translate_segments(`
  - Purpose: Records a '"translate_segments"' call, then returns either a 'Vec<String>' of '"translated {segment.text}"' for each input segment when no queued translations exist, or the first preloaded translation batch by removing and returning it from 'self.translations'. [crates/gwiki/src/ingest/audio.rs:495-510]
- `test_context` (function) component `test_context [function]` (`0171f70b-fa5e-53e4-8a1c-93801edad135`) lines 513-541 [crates/gwiki/src/ingest/audio.rs:513-541]
  - Signature: `fn test_context(routing: AiRouting, api_base: Option<String>) -> AiContext {`
  - Purpose: Constructs an 'AiContext' for tests by creating a shared 'CapabilityBinding' with the supplied routing and optional API base, assigning it to all AI capability bindings, and configuring single-concurrency tuning with a new limiter and no project ID. [crates/gwiki/src/ingest/audio.rs:513-541]
- `spawn_transcription_server` (function) component `spawn_transcription_server [function]` (`671d921d-86c5-5769-89fe-2fc5136fec1f`) lines 544-548 [crates/gwiki/src/ingest/audio.rs:544-548]
  - Signature: `fn spawn_transcription_server(`
  - Purpose: Spawns a test HTTP server that serves the provided static JSON response and returns its URL string together with a 'RequestHandle', panicking if server creation fails. [crates/gwiki/src/ingest/audio.rs:544-548]
- `test_chunk` (function) component `test_chunk [function]` (`9f6d18e8-9e0d-5ddd-8334-a70f35e763ad`) lines 551-559 [crates/gwiki/src/ingest/audio.rs:551-559]
  - Signature: `fn test_chunk(start_ms: u64, end_ms: u64) -> crate::ai::chunk::AudioChunk {`
  - Purpose: Constructs a 'crate::ai::chunk::AudioChunk' test fixture with the given 'start_ms' and 'end_ms', a 'chunk-{start_ms}.wav' filename/path, and fixed 'b"wav"' bytes. [crates/gwiki/src/ingest/audio.rs:551-559]
- `transcript_output` (function) component `transcript_output [function]` (`4ddc1ea8-2561-52a1-b123-5627c9ec69f8`) lines 562-588 [crates/gwiki/src/ingest/audio.rs:562-588]
  - Signature: `fn transcript_output(`
  - Purpose: Constructs a 'TranscriptionOutput' from input segments by copying timestamps and text into 'TranscriptSegment's, setting the effective language to English when 'translated' is true, recording the source language, task, and fixed model '"fake-stt"', and initializing all completion/missing-range and status fields to empty or false. [crates/gwiki/src/ingest/audio.rs:562-588]
- `english_target_uses_primary_language_subtag` (function) component `english_target_uses_primary_language_subtag [function]` (`1d341077-93f2-5f67-a594-7f8e6a7e8dce`) lines 592-598 [crates/gwiki/src/ingest/audio.rs:592-598]
  - Signature: `fn english_target_uses_primary_language_subtag() {`
  - Purpose: Verifies that 'is_english_target' returns true for English locale identifiers whose primary language subtag is 'en' regardless of case or separator/region suffixes, and false for non-'en' or non-primary matches. [crates/gwiki/src/ingest/audio.rs:592-598]
- `production_transcription_writes_fields` (function) component `production_transcription_writes_fields [function]` (`3034ec15-5b98-56d3-82b0-c18401963cf1`) lines 602-636 [crates/gwiki/src/ingest/audio.rs:602-636]
  - Signature: `fn production_transcription_writes_fields() {`
  - Purpose: Verifies that 'ingest_audio' preserves production transcription metadata and transcript text in the generated markdown for a successful direct-routed transcription, including status, target/source languages, model, task, translated flag, and timestamped segment output. [crates/gwiki/src/ingest/audio.rs:602-636]
- `production_path_applies_translation` (function) component `production_path_applies_translation [function]` (`a383f2d8-0cdb-5a7d-8f57-23a771f72f9a`) lines 640-674 [crates/gwiki/src/ingest/audio.rs:640-674]
  - Signature: `fn production_path_applies_translation() {`
  - Purpose: Verifies that the production transcription path uses the translations endpoint for translated audio, preserves no degradation, and writes transcript metadata indicating 'transcribed', source 'es', target 'en', 'translate' task, 'translated: true', and the translated segment text. [crates/gwiki/src/ingest/audio.rs:640-674]
- `production_path_chunks_long_audio` (function) component `production_path_chunks_long_audio [function]` (`cfe115d3-30eb-5335-b547-c0150c99e649`) lines 678-704 [crates/gwiki/src/ingest/audio.rs:678-704]
  - Signature: `fn production_path_chunks_long_audio() {`
  - Purpose: Verifies that long-audio ingestion with overlapping test chunks writes a transcript containing the completed range metadata and the expected timestamped transcription lines for each chunk. [crates/gwiki/src/ingest/audio.rs:678-704]
- `long_media_chunks_then_translates` (function) component `long_media_chunks_then_translates [function]` (`7434c8ac-7d40-505a-b34f-2e6cc048f1e9`) lines 708-745 [crates/gwiki/src/ingest/audio.rs:708-745]
  - Signature: `fn long_media_chunks_then_translates() {`
  - Purpose: Verifies that long overlapping audio is ingested in chunks and translated from Spanish to French, producing a transcript markdown file with the expected translation metadata and timestamped lines. [crates/gwiki/src/ingest/audio.rs:708-745]
- `long_english_translation_per_chunk` (function) component `long_english_translation_per_chunk [function]` (`3e2b8d11-5872-592c-8838-f169e417a49a`) lines 749-787 [crates/gwiki/src/ingest/audio.rs:749-787]
  - Signature: `fn long_english_translation_per_chunk() {`
  - Purpose: Tests that long, overlapping chunked audio is ingested through the English translation path, producing transcript metadata and timestamped translated lines while invoking 'translate_to_english' once per chunk. [crates/gwiki/src/ingest/audio.rs:749-787]
- `off_routing_degrades` (function) component `off_routing_degrades [function]` (`293e77aa-b0a4-54c2-9f87-18ae277515f5`) lines 790-821 [crates/gwiki/src/ingest/audio.rs:790-821]
  - Signature: `fn off_routing_degrades() {`
  - Purpose: Verifies that 'ingest_audio' with 'AiRouting::Off' preserves the raw audio asset, records a transcription degradation reason of 'disabled', and writes a transcript marked 'unavailable' with the expected degradation metadata and retention note. [crates/gwiki/src/ingest/audio.rs:790-821]
- `stores_original_audio` (function) component `stores_original_audio [function]` (`0f981cd1-7d73-5d8d-ba02-38756ffa79a9`) lines 824-859 [crates/gwiki/src/ingest/audio.rs:824-859]
  - Signature: `fn stores_original_audio() {`
  - Purpose: Verifies that 'ingest_audio' persists the original audio bytes under 'raw/assets/', writes a raw markdown record with the expected audio metadata fields, and records a matching 'SourceManifest' entry with 'SourceKind::Audio' and the snapshot’s content hash. [crates/gwiki/src/ingest/audio.rs:824-859]
- `transcript_chunks_are_scope_searchable` (function) component `transcript_chunks_are_scope_searchable [function]` (`4a08b009-b68c-5dc7-adaa-f538a5d45b79`) lines 862-897 [crates/gwiki/src/ingest/audio.rs:862-897]
  - Signature: `fn transcript_chunks_are_scope_searchable() {`
  - Purpose: Verifies that ingesting a transcribed audio file indexes the transcript as a 'SourceNote' with project scope metadata and creates searchable chunks containing the transcript text. [crates/gwiki/src/ingest/audio.rs:862-897]

