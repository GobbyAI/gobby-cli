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
  - 339-345
  - 348-376
  - 396-405
  - 408-414
  - '416'
  - 419-440
  - 444-449
  - 453-460
  - 462-469
  - 471-473
  - 478-484
  - 486-493
  - 495-510
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/audio.rs:21-28](crates/gwiki/src/ingest/audio.rs#L21-L28), [crates/gwiki/src/ingest/audio.rs:31-37](crates/gwiki/src/ingest/audio.rs#L31-L37), [crates/gwiki/src/ingest/audio.rs:40-54](crates/gwiki/src/ingest/audio.rs#L40-L54), [crates/gwiki/src/ingest/audio.rs:56-87](crates/gwiki/src/ingest/audio.rs#L56-L87), [crates/gwiki/src/ingest/audio.rs:89-91](crates/gwiki/src/ingest/audio.rs#L89-L91), [crates/gwiki/src/ingest/audio.rs:94-96](crates/gwiki/src/ingest/audio.rs#L94-L96), [crates/gwiki/src/ingest/audio.rs:99-101](crates/gwiki/src/ingest/audio.rs#L99-L101), [crates/gwiki/src/ingest/audio.rs:104-125](crates/gwiki/src/ingest/audio.rs#L104-L125), [crates/gwiki/src/ingest/audio.rs:128-137](crates/gwiki/src/ingest/audio.rs#L128-L137), [crates/gwiki/src/ingest/audio.rs:139-145](crates/gwiki/src/ingest/audio.rs#L139-L145), [crates/gwiki/src/ingest/audio.rs:148-159](crates/gwiki/src/ingest/audio.rs#L148-L159), [crates/gwiki/src/ingest/audio.rs:161-202](crates/gwiki/src/ingest/audio.rs#L161-L202), [crates/gwiki/src/ingest/audio.rs:204-226](crates/gwiki/src/ingest/audio.rs#L204-L226), [crates/gwiki/src/ingest/audio.rs:228-238](crates/gwiki/src/ingest/audio.rs#L228-L238), [crates/gwiki/src/ingest/audio.rs:241-250](crates/gwiki/src/ingest/audio.rs#L241-L250), [crates/gwiki/src/ingest/audio.rs:253-258](crates/gwiki/src/ingest/audio.rs#L253-L258), [crates/gwiki/src/ingest/audio.rs:261-286](crates/gwiki/src/ingest/audio.rs#L261-L286), [crates/gwiki/src/ingest/audio.rs:289-299](crates/gwiki/src/ingest/audio.rs#L289-L299), [crates/gwiki/src/ingest/audio.rs:301-326](crates/gwiki/src/ingest/audio.rs#L301-L326), [crates/gwiki/src/ingest/audio.rs:329-336](crates/gwiki/src/ingest/audio.rs#L329-L336), [crates/gwiki/src/ingest/audio.rs:339-345](crates/gwiki/src/ingest/audio.rs#L339-L345), [crates/gwiki/src/ingest/audio.rs:348-376](crates/gwiki/src/ingest/audio.rs#L348-L376), [crates/gwiki/src/ingest/audio.rs:396-405](crates/gwiki/src/ingest/audio.rs#L396-L405), [crates/gwiki/src/ingest/audio.rs:408-414](crates/gwiki/src/ingest/audio.rs#L408-L414), [crates/gwiki/src/ingest/audio.rs:416](crates/gwiki/src/ingest/audio.rs#L416), [crates/gwiki/src/ingest/audio.rs:419-440](crates/gwiki/src/ingest/audio.rs#L419-L440), [crates/gwiki/src/ingest/audio.rs:444-449](crates/gwiki/src/ingest/audio.rs#L444-L449), [crates/gwiki/src/ingest/audio.rs:453-460](crates/gwiki/src/ingest/audio.rs#L453-L460), [crates/gwiki/src/ingest/audio.rs:462-469](crates/gwiki/src/ingest/audio.rs#L462-L469), [crates/gwiki/src/ingest/audio.rs:471-473](crates/gwiki/src/ingest/audio.rs#L471-L473), [crates/gwiki/src/ingest/audio.rs:478-484](crates/gwiki/src/ingest/audio.rs#L478-L484), [crates/gwiki/src/ingest/audio.rs:486-493](crates/gwiki/src/ingest/audio.rs#L486-L493), [crates/gwiki/src/ingest/audio.rs:495-510](crates/gwiki/src/ingest/audio.rs#L495-L510), [crates/gwiki/src/ingest/audio.rs:513-541](crates/gwiki/src/ingest/audio.rs#L513-L541), [crates/gwiki/src/ingest/audio.rs:544-548](crates/gwiki/src/ingest/audio.rs#L544-L548), [crates/gwiki/src/ingest/audio.rs:551-559](crates/gwiki/src/ingest/audio.rs#L551-L559), [crates/gwiki/src/ingest/audio.rs:562-588](crates/gwiki/src/ingest/audio.rs#L562-L588), [crates/gwiki/src/ingest/audio.rs:592-598](crates/gwiki/src/ingest/audio.rs#L592-L598), [crates/gwiki/src/ingest/audio.rs:602-636](crates/gwiki/src/ingest/audio.rs#L602-L636), [crates/gwiki/src/ingest/audio.rs:640-674](crates/gwiki/src/ingest/audio.rs#L640-L674), [crates/gwiki/src/ingest/audio.rs:678-704](crates/gwiki/src/ingest/audio.rs#L678-L704), [crates/gwiki/src/ingest/audio.rs:708-745](crates/gwiki/src/ingest/audio.rs#L708-L745), [crates/gwiki/src/ingest/audio.rs:749-787](crates/gwiki/src/ingest/audio.rs#L749-L787), [crates/gwiki/src/ingest/audio.rs:790-821](crates/gwiki/src/ingest/audio.rs#L790-L821), [crates/gwiki/src/ingest/audio.rs:824-859](crates/gwiki/src/ingest/audio.rs#L824-L859), [crates/gwiki/src/ingest/audio.rs:862-897](crates/gwiki/src/ingest/audio.rs#L862-L897)

</details>

# crates/gwiki/src/ingest/audio.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements audio ingestion for gwiki. It takes an `AudioSnapshot`, resolves the appropriate transcription or translation route from AI context, and produces an `AudioIngestResult` containing the source record plus paths for the raw markdown, stored audio asset, and transcript, along with any transcription degradation. The helper functions split the workflow into route selection and fallback handling, transcription-to-markdown rendering, and translation support, while the fake/scripted transcription clients and fixture helpers drive the extensive tests that verify production routing, chunking, translation behavior, storage of original audio, and searchable transcript output.
[crates/gwiki/src/ingest/audio.rs:21-28]
[crates/gwiki/src/ingest/audio.rs:31-37]
[crates/gwiki/src/ingest/audio.rs:40-54]
[crates/gwiki/src/ingest/audio.rs:56-87]
[crates/gwiki/src/ingest/audio.rs:89-91]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `AudioSnapshot` | class | `pub struct AudioSnapshot {` | `AudioSnapshot [class]` | `003c630c-73fb-540c-89b2-8e5b0c1147a0` | 21-28 [crates/gwiki/src/ingest/audio.rs:21-28] | Indexed class `AudioSnapshot` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:21-28] |
| `AudioIngestResult` | class | `pub struct AudioIngestResult {` | `AudioIngestResult [class]` | `33266ed3-9a67-5693-913b-32bfa8ee9449` | 31-37 [crates/gwiki/src/ingest/audio.rs:31-37] | Indexed class `AudioIngestResult` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:31-37] |
| `ingest_audio` | function | `pub fn ingest_audio(` | `ingest_audio [function]` | `c6476a84-0ff8-5c83-9c94-4711a935eea8` | 40-54 [crates/gwiki/src/ingest/audio.rs:40-54] | Indexed function `ingest_audio` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:40-54] |
| `production_transcription_endpoint` | function | `pub fn production_transcription_endpoint(` | `production_transcription_endpoint [function]` | `ac34e907-e976-5cee-95fe-1bb6b882663a` | 56-87 [crates/gwiki/src/ingest/audio.rs:56-87] | Indexed function `production_transcription_endpoint` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:56-87] |
| `route_available` | function | `fn route_available(route: AiRouting) -> bool {` | `route_available [function]` | `cc4c7b6a-742d-5e8a-bb61-f7e3c21d2825` | 89-91 [crates/gwiki/src/ingest/audio.rs:89-91] | Indexed function `route_available` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:89-91] |
| `resolved_transcription_route` | function | `fn resolved_transcription_route(context: &AiContext, capability: AiCapability) -> AiRouting {` | `resolved_transcription_route [function]` | `4aa3d418-19e9-5e46-956b-717bb5df5f6d` | 94-96 [crates/gwiki/src/ingest/audio.rs:94-96] | Indexed function `resolved_transcription_route` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:94-96] |
| `resolved_transcription_route` | function | `fn resolved_transcription_route(context: &AiContext, capability: AiCapability) -> AiRouting {` | `resolved_transcription_route [function]` | `d10dacab-01b7-5a51-bfe5-df484c9399e6` | 99-101 [crates/gwiki/src/ingest/audio.rs:99-101] | Indexed function `resolved_transcription_route` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:99-101] |
| `available_production_transcription_endpoint` | function | `fn available_production_transcription_endpoint(` | `available_production_transcription_endpoint [function]` | `808b0692-32d9-50f4-a5a9-2b2ebff56db8` | 104-125 [crates/gwiki/src/ingest/audio.rs:104-125] | Indexed function `available_production_transcription_endpoint` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:104-125] |
| `available_production_transcription_endpoint` | function | `fn available_production_transcription_endpoint(` | `available_production_transcription_endpoint [function]` | `5de176c9-2796-546f-8c19-126f9e96ebca` | 128-137 [crates/gwiki/src/ingest/audio.rs:128-137] | Indexed function `available_production_transcription_endpoint` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:128-137] |
| `transcription_fallback` | function | `fn transcription_fallback(translate: bool) -> &'static str {` | `transcription_fallback [function]` | `2834d8b5-a541-55fd-9288-c55e623cbb09` | 139-145 [crates/gwiki/src/ingest/audio.rs:139-145] | Indexed function `transcription_fallback` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:139-145] |
| `ingest_audio_with_transcription` | function | `pub fn ingest_audio_with_transcription(` | `ingest_audio_with_transcription [function]` | `5b21522b-ad17-5a68-8968-9327904e4c3d` | 148-159 [crates/gwiki/src/ingest/audio.rs:148-159] | Indexed function `ingest_audio_with_transcription` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:148-159] |
| `ingest_audio_with_transcription_without_index` | function | `pub(crate) fn ingest_audio_with_transcription_without_index(` | `ingest_audio_with_transcription_without_index [function]` | `02d14539-2527-53e3-a472-18449d0abb5d` | 161-202 [crates/gwiki/src/ingest/audio.rs:161-202] | Indexed function `ingest_audio_with_transcription_without_index` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:161-202] |
| `transcribe_for_markdown` | function | `pub(crate) fn transcribe_for_markdown(` | `transcribe_for_markdown [function]` | `3543c95c-df70-5fa5-9de5-b2376e07fccc` | 204-226 [crates/gwiki/src/ingest/audio.rs:204-226] | Indexed function `transcribe_for_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:204-226] |
| `transcription_result_for_markdown` | function | `fn transcription_result_for_markdown(` | `transcription_result_for_markdown [function]` | `5acbbdbd-c6e7-548a-b0b4-5afdf7a9952a` | 228-238 [crates/gwiki/src/ingest/audio.rs:228-238] | Indexed function `transcription_result_for_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:228-238] |
| `transcribe_available` | function | `fn transcribe_available(` | `transcribe_available [function]` | `fcf5a57b-0932-5058-b450-a6a5a63c7786` | 241-250 [crates/gwiki/src/ingest/audio.rs:241-250] | Indexed function `transcribe_available` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:241-250] |
| `transcribe_available` | function | `fn transcribe_available(` | `transcribe_available [function]` | `d7adbabe-c8ce-5efc-bfc0-d6d3c6cdbf7e` | 253-258 [crates/gwiki/src/ingest/audio.rs:253-258] | Indexed function `transcribe_available` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:253-258] |
| `translate_for_markdown` | function | `fn translate_for_markdown(` | `translate_for_markdown [function]` | `5a3b5953-e6a2-51ac-acae-6cba2367b755` | 261-286 [crates/gwiki/src/ingest/audio.rs:261-286] | Indexed function `translate_for_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:261-286] |
| `translate_for_markdown` | function | `fn translate_for_markdown(` | `translate_for_markdown [function]` | `d8187d6d-cd9e-56c5-ad05-4663eddd5930` | 289-299 [crates/gwiki/src/ingest/audio.rs:289-299] | Indexed function `translate_for_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:289-299] |
| `transcription_result_to_markdown` | function | `fn transcription_result_to_markdown(` | `transcription_result_to_markdown [function]` | `3786153c-d3b1-59db-9482-6a79a93a45ca` | 301-326 [crates/gwiki/src/ingest/audio.rs:301-326] | Indexed function `transcription_result_to_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:301-326] |
| `is_english_target` | function | `fn is_english_target(target_lang: &str) -> bool {` | `is_english_target [function]` | `88bec159-4771-550b-9f29-22b89d007f2a` | 329-336 [crates/gwiki/src/ingest/audio.rs:329-336] | Indexed function `is_english_target` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:329-336] |
| `IngestResult::from` | method | `fn from(result: AudioIngestResult) -> Self {` | `IngestResult::from [method]` | `b9f5cee3-9599-5a66-b7f6-2e9328d97725` | 339-345 [crates/gwiki/src/ingest/audio.rs:339-345] | Indexed method `IngestResult::from` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:339-345] |
| `render_raw_audio_markdown` | function | `fn render_raw_audio_markdown(` | `render_raw_audio_markdown [function]` | `abcbd023-5ca6-5268-8972-4c4d361d8fbe` | 348-376 [crates/gwiki/src/ingest/audio.rs:348-376] | Indexed function `render_raw_audio_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:348-376] |
| `sample_snapshot` | function | `fn sample_snapshot() -> AudioSnapshot {` | `sample_snapshot [function]` | `5eaf7359-6733-56b6-9ce1-e6399953a579` | 396-405 [crates/gwiki/src/ingest/audio.rs:396-405] | Indexed function `sample_snapshot` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:396-405] |
| `long_snapshot` | function | `fn long_snapshot() -> AudioSnapshot {` | `long_snapshot [function]` | `40f82c5d-4153-52c1-84dc-c1cbada0d6f4` | 408-414 [crates/gwiki/src/ingest/audio.rs:408-414] | Indexed function `long_snapshot` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:408-414] |
| `FakeTranscriptionClient` | class | `struct FakeTranscriptionClient;` | `FakeTranscriptionClient [class]` | `8d6ba8a4-6750-57e6-8b15-e4b23eefc31d` | 416-416 [crates/gwiki/src/ingest/audio.rs:416] | Indexed class `FakeTranscriptionClient` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:416] |
| `FakeTranscriptionClient::transcribe` | method | `fn transcribe(` | `FakeTranscriptionClient::transcribe [method]` | `fe3609ae-bad2-58a4-8d24-db958d5cec95` | 419-440 [crates/gwiki/src/ingest/audio.rs:419-440] | Indexed method `FakeTranscriptionClient::transcribe` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:419-440] |
| `ScriptedTranscriptionClient` | class | `struct ScriptedTranscriptionClient {` | `ScriptedTranscriptionClient [class]` | `b2adc447-ecd8-5ec1-9dc0-8631f390fcdb` | 444-449 [crates/gwiki/src/ingest/audio.rs:444-449] | Indexed class `ScriptedTranscriptionClient` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:444-449] |
| `ScriptedTranscriptionClient::new` | method | `fn new(transcriptions: Vec<TranscriptionOutput>) -> Self {` | `ScriptedTranscriptionClient::new [method]` | `fbead57d-4850-5534-9ad2-9ca0989dcc45` | 453-460 [crates/gwiki/src/ingest/audio.rs:453-460] | Indexed method `ScriptedTranscriptionClient::new` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:453-460] |
| `ScriptedTranscriptionClient::with_english` | method | `fn with_english(english: Vec<TranscriptionOutput>) -> Self {` | `ScriptedTranscriptionClient::with_english [method]` | `facf006b-b0ec-5ed5-8a89-7cb9fce2f1d3` | 462-469 [crates/gwiki/src/ingest/audio.rs:462-469] | Indexed method `ScriptedTranscriptionClient::with_english` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:462-469] |
| `ScriptedTranscriptionClient::calls` | method | `fn calls(&self) -> Rc<RefCell<Vec<&'static str>>> {` | `ScriptedTranscriptionClient::calls [method]` | `3a43edfc-8c11-5b83-9cf4-0db0d54783af` | 471-473 [crates/gwiki/src/ingest/audio.rs:471-473] | Indexed method `ScriptedTranscriptionClient::calls` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:471-473] |
| `ScriptedTranscriptionClient::transcribe` | method | `fn transcribe(` | `ScriptedTranscriptionClient::transcribe [method]` | `26fd6bf4-6e60-59a2-b5b5-5df3c497d33a` | 478-484 [crates/gwiki/src/ingest/audio.rs:478-484] | Indexed method `ScriptedTranscriptionClient::transcribe` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:478-484] |
| `ScriptedTranscriptionClient::translate_to_english` | method | `fn translate_to_english(` | `ScriptedTranscriptionClient::translate_to_english [method]` | `e2fd85d2-1c28-577e-a33e-a828028b4229` | 486-493 [crates/gwiki/src/ingest/audio.rs:486-493] | Indexed method `ScriptedTranscriptionClient::translate_to_english` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:486-493] |
| `ScriptedTranscriptionClient::translate_segments` | method | `fn translate_segments(` | `ScriptedTranscriptionClient::translate_segments [method]` | `58740a20-3822-5006-9132-81f3edc5bd88` | 495-510 [crates/gwiki/src/ingest/audio.rs:495-510] | Indexed method `ScriptedTranscriptionClient::translate_segments` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:495-510] |
| `test_context` | function | `fn test_context(routing: AiRouting, api_base: Option<String>) -> AiContext {` | `test_context [function]` | `0171f70b-fa5e-53e4-8a1c-93801edad135` | 513-541 [crates/gwiki/src/ingest/audio.rs:513-541] | Indexed function `test_context` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:513-541] |
| `spawn_transcription_server` | function | `fn spawn_transcription_server(` | `spawn_transcription_server [function]` | `671d921d-86c5-5769-89fe-2fc5136fec1f` | 544-548 [crates/gwiki/src/ingest/audio.rs:544-548] | Indexed function `spawn_transcription_server` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:544-548] |
| `test_chunk` | function | `fn test_chunk(start_ms: u64, end_ms: u64) -> crate::ai::chunk::AudioChunk {` | `test_chunk [function]` | `9f6d18e8-9e0d-5ddd-8334-a70f35e763ad` | 551-559 [crates/gwiki/src/ingest/audio.rs:551-559] | Indexed function `test_chunk` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:551-559] |
| `transcript_output` | function | `fn transcript_output(` | `transcript_output [function]` | `4ddc1ea8-2561-52a1-b123-5627c9ec69f8` | 562-588 [crates/gwiki/src/ingest/audio.rs:562-588] | Indexed function `transcript_output` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:562-588] |
| `english_target_uses_primary_language_subtag` | function | `fn english_target_uses_primary_language_subtag() {` | `english_target_uses_primary_language_subtag [function]` | `1d341077-93f2-5f67-a594-7f8e6a7e8dce` | 592-598 [crates/gwiki/src/ingest/audio.rs:592-598] | Indexed function `english_target_uses_primary_language_subtag` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:592-598] |
| `production_transcription_writes_fields` | function | `fn production_transcription_writes_fields() {` | `production_transcription_writes_fields [function]` | `3034ec15-5b98-56d3-82b0-c18401963cf1` | 602-636 [crates/gwiki/src/ingest/audio.rs:602-636] | Indexed function `production_transcription_writes_fields` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:602-636] |
| `production_path_applies_translation` | function | `fn production_path_applies_translation() {` | `production_path_applies_translation [function]` | `a383f2d8-0cdb-5a7d-8f57-23a771f72f9a` | 640-674 [crates/gwiki/src/ingest/audio.rs:640-674] | Indexed function `production_path_applies_translation` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:640-674] |
| `production_path_chunks_long_audio` | function | `fn production_path_chunks_long_audio() {` | `production_path_chunks_long_audio [function]` | `cfe115d3-30eb-5335-b547-c0150c99e649` | 678-704 [crates/gwiki/src/ingest/audio.rs:678-704] | Indexed function `production_path_chunks_long_audio` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:678-704] |
| `long_media_chunks_then_translates` | function | `fn long_media_chunks_then_translates() {` | `long_media_chunks_then_translates [function]` | `7434c8ac-7d40-505a-b34f-2e6cc048f1e9` | 708-745 [crates/gwiki/src/ingest/audio.rs:708-745] | Indexed function `long_media_chunks_then_translates` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:708-745] |
| `long_english_translation_per_chunk` | function | `fn long_english_translation_per_chunk() {` | `long_english_translation_per_chunk [function]` | `3e2b8d11-5872-592c-8838-f169e417a49a` | 749-787 [crates/gwiki/src/ingest/audio.rs:749-787] | Indexed function `long_english_translation_per_chunk` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:749-787] |
| `off_routing_degrades` | function | `fn off_routing_degrades() {` | `off_routing_degrades [function]` | `293e77aa-b0a4-54c2-9f87-18ae277515f5` | 790-821 [crates/gwiki/src/ingest/audio.rs:790-821] | Indexed function `off_routing_degrades` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:790-821] |
| `stores_original_audio` | function | `fn stores_original_audio() {` | `stores_original_audio [function]` | `0f981cd1-7d73-5d8d-ba02-38756ffa79a9` | 824-859 [crates/gwiki/src/ingest/audio.rs:824-859] | Indexed function `stores_original_audio` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:824-859] |
| `transcript_chunks_are_scope_searchable` | function | `fn transcript_chunks_are_scope_searchable() {` | `transcript_chunks_are_scope_searchable [function]` | `4a08b009-b68c-5dc7-adaa-f538a5d45b79` | 862-897 [crates/gwiki/src/ingest/audio.rs:862-897] | Indexed function `transcript_chunks_are_scope_searchable` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:862-897] |
