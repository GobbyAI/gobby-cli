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
  - 301-315
  - 318-325
  - 327-335
  - 337-365
  - 385-394
  - 397-403
  - '405'
  - 407-430
  - 433-438
  - 441-463
  - 466-500
  - 502-530
  - 533-537
  - 540-548
  - 551-577
  - 581-587
  - 591-625
  - 629-663
  - 667-693
  - 697-734
  - 738-776
  - 779-810
  - 813-848
  - 851-886
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
[crates/gwiki/src/ingest/audio.rs:40-54]
[crates/gwiki/src/ingest/audio.rs:56-87]
[crates/gwiki/src/ingest/audio.rs:89-91]

## API Symbols

- `AudioSnapshot` (class) component `AudioSnapshot [class]` (`003c630c-73fb-540c-89b2-8e5b0c1147a0`) lines 21-28 [crates/gwiki/src/ingest/audio.rs:21-28]
  - Signature: `pub struct AudioSnapshot {`
  - Purpose: Indexed class `AudioSnapshot` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:21-28]
- `AudioIngestResult` (class) component `AudioIngestResult [class]` (`33266ed3-9a67-5693-913b-32bfa8ee9449`) lines 31-37 [crates/gwiki/src/ingest/audio.rs:31-37]
  - Signature: `pub struct AudioIngestResult {`
  - Purpose: Indexed class `AudioIngestResult` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:31-37]
- `ingest_audio` (function) component `ingest_audio [function]` (`c6476a84-0ff8-5c83-9c94-4711a935eea8`) lines 40-54 [crates/gwiki/src/ingest/audio.rs:40-54]
  - Signature: `pub fn ingest_audio(`
  - Purpose: Indexed function `ingest_audio` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:40-54]
- `production_transcription_endpoint` (function) component `production_transcription_endpoint [function]` (`ac34e907-e976-5cee-95fe-1bb6b882663a`) lines 56-87 [crates/gwiki/src/ingest/audio.rs:56-87]
  - Signature: `pub fn production_transcription_endpoint(`
  - Purpose: Indexed function `production_transcription_endpoint` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:56-87]
- `route_available` (function) component `route_available [function]` (`cc4c7b6a-742d-5e8a-bb61-f7e3c21d2825`) lines 89-91 [crates/gwiki/src/ingest/audio.rs:89-91]
  - Signature: `fn route_available(route: AiRouting) -> bool {`
  - Purpose: Indexed function `route_available` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:89-91]
- `resolved_transcription_route` (function) component `resolved_transcription_route [function]` (`4aa3d418-19e9-5e46-956b-717bb5df5f6d`) lines 94-96 [crates/gwiki/src/ingest/audio.rs:94-96]
  - Signature: `fn resolved_transcription_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Indexed function `resolved_transcription_route` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:94-96]
- `resolved_transcription_route` (function) component `resolved_transcription_route [function]` (`d10dacab-01b7-5a51-bfe5-df484c9399e6`) lines 99-101 [crates/gwiki/src/ingest/audio.rs:99-101]
  - Signature: `fn resolved_transcription_route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Indexed function `resolved_transcription_route` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:99-101]
- `available_production_transcription_endpoint` (function) component `available_production_transcription_endpoint [function]` (`808b0692-32d9-50f4-a5a9-2b2ebff56db8`) lines 104-125 [crates/gwiki/src/ingest/audio.rs:104-125]
  - Signature: `fn available_production_transcription_endpoint(`
  - Purpose: Indexed function `available_production_transcription_endpoint` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:104-125]
- `available_production_transcription_endpoint` (function) component `available_production_transcription_endpoint [function]` (`5de176c9-2796-546f-8c19-126f9e96ebca`) lines 128-137 [crates/gwiki/src/ingest/audio.rs:128-137]
  - Signature: `fn available_production_transcription_endpoint(`
  - Purpose: Indexed function `available_production_transcription_endpoint` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:128-137]
- `transcription_fallback` (function) component `transcription_fallback [function]` (`2834d8b5-a541-55fd-9288-c55e623cbb09`) lines 139-145 [crates/gwiki/src/ingest/audio.rs:139-145]
  - Signature: `fn transcription_fallback(translate: bool) -> &'static str {`
  - Purpose: Indexed function `transcription_fallback` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:139-145]
- `ingest_audio_with_transcription` (function) component `ingest_audio_with_transcription [function]` (`5b21522b-ad17-5a68-8968-9327904e4c3d`) lines 148-159 [crates/gwiki/src/ingest/audio.rs:148-159]
  - Signature: `pub fn ingest_audio_with_transcription(`
  - Purpose: Indexed function `ingest_audio_with_transcription` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:148-159]
- `ingest_audio_with_transcription_without_index` (function) component `ingest_audio_with_transcription_without_index [function]` (`02d14539-2527-53e3-a472-18449d0abb5d`) lines 161-202 [crates/gwiki/src/ingest/audio.rs:161-202]
  - Signature: `pub(crate) fn ingest_audio_with_transcription_without_index(`
  - Purpose: Indexed function `ingest_audio_with_transcription_without_index` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:161-202]
- `transcribe_for_markdown` (function) component `transcribe_for_markdown [function]` (`3543c95c-df70-5fa5-9de5-b2376e07fccc`) lines 204-226 [crates/gwiki/src/ingest/audio.rs:204-226]
  - Signature: `pub(crate) fn transcribe_for_markdown(`
  - Purpose: Indexed function `transcribe_for_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:204-226]
- `transcription_result_for_markdown` (function) component `transcription_result_for_markdown [function]` (`5acbbdbd-c6e7-548a-b0b4-5afdf7a9952a`) lines 228-238 [crates/gwiki/src/ingest/audio.rs:228-238]
  - Signature: `fn transcription_result_for_markdown(`
  - Purpose: Indexed function `transcription_result_for_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:228-238]
- `transcribe_available` (function) component `transcribe_available [function]` (`fcf5a57b-0932-5058-b450-a6a5a63c7786`) lines 241-250 [crates/gwiki/src/ingest/audio.rs:241-250]
  - Signature: `fn transcribe_available(`
  - Purpose: Indexed function `transcribe_available` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:241-250]
- `transcribe_available` (function) component `transcribe_available [function]` (`d7adbabe-c8ce-5efc-bfc0-d6d3c6cdbf7e`) lines 253-258 [crates/gwiki/src/ingest/audio.rs:253-258]
  - Signature: `fn transcribe_available(`
  - Purpose: Indexed function `transcribe_available` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:253-258]
- `translate_for_markdown` (function) component `translate_for_markdown [function]` (`5a3b5953-e6a2-51ac-acae-6cba2367b755`) lines 261-286 [crates/gwiki/src/ingest/audio.rs:261-286]
  - Signature: `fn translate_for_markdown(`
  - Purpose: Indexed function `translate_for_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:261-286]
- `translate_for_markdown` (function) component `translate_for_markdown [function]` (`d8187d6d-cd9e-56c5-ad05-4663eddd5930`) lines 289-299 [crates/gwiki/src/ingest/audio.rs:289-299]
  - Signature: `fn translate_for_markdown(`
  - Purpose: Indexed function `translate_for_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:289-299]
- `transcription_result_to_markdown` (function) component `transcription_result_to_markdown [function]` (`3786153c-d3b1-59db-9482-6a79a93a45ca`) lines 301-315 [crates/gwiki/src/ingest/audio.rs:301-315]
  - Signature: `fn transcription_result_to_markdown(`
  - Purpose: Indexed function `transcription_result_to_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:301-315]
- `is_english_target` (function) component `is_english_target [function]` (`079290d7-29a7-524b-8d4f-e07b94a91ca9`) lines 318-325 [crates/gwiki/src/ingest/audio.rs:318-325]
  - Signature: `fn is_english_target(target_lang: &str) -> bool {`
  - Purpose: Indexed function `is_english_target` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:318-325]
- `IngestResult` (class) component `IngestResult [class]` (`e9f91ab6-ea87-5d09-a4d5-ef526014010e`) lines 327-335 [crates/gwiki/src/ingest/audio.rs:327-335]
  - Signature: `impl From<AudioIngestResult> for IngestResult {`
  - Purpose: Indexed class `IngestResult` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:327-335]
- `IngestResult.from` (method) component `IngestResult.from [method]` (`877e19dd-e5de-51ff-8019-72634801405a`) lines 328-334 [crates/gwiki/src/ingest/audio.rs:328-334]
  - Signature: `fn from(result: AudioIngestResult) -> Self {`
  - Purpose: Indexed method `IngestResult.from` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:328-334]
- `render_raw_audio_markdown` (function) component `render_raw_audio_markdown [function]` (`e9ec2fbf-b985-51da-b9a8-e713382a55d4`) lines 337-365 [crates/gwiki/src/ingest/audio.rs:337-365]
  - Signature: `fn render_raw_audio_markdown(`
  - Purpose: Indexed function `render_raw_audio_markdown` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:337-365]
- `sample_snapshot` (function) component `sample_snapshot [function]` (`83d8044e-2948-5e7e-bc14-780512f683a8`) lines 385-394 [crates/gwiki/src/ingest/audio.rs:385-394]
  - Signature: `fn sample_snapshot() -> AudioSnapshot {`
  - Purpose: Indexed function `sample_snapshot` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:385-394]
- `long_snapshot` (function) component `long_snapshot [function]` (`43a1381e-6497-57db-8906-347206fe9065`) lines 397-403 [crates/gwiki/src/ingest/audio.rs:397-403]
  - Signature: `fn long_snapshot() -> AudioSnapshot {`
  - Purpose: Indexed function `long_snapshot` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:397-403]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`b8dd79ca-e136-5be6-9a52-baae39d15ee1`) lines 405-405 [crates/gwiki/src/ingest/audio.rs:405]
  - Signature: `struct FakeTranscriptionClient;`
  - Purpose: Indexed class `FakeTranscriptionClient` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:405]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`adc8beda-87fd-55b6-8fc3-00cc7c72fc85`) lines 407-430 [crates/gwiki/src/ingest/audio.rs:407-430]
  - Signature: `impl TranscriptionClient for FakeTranscriptionClient {`
  - Purpose: Indexed class `FakeTranscriptionClient` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:407-430]
- `FakeTranscriptionClient.transcribe` (method) component `FakeTranscriptionClient.transcribe [method]` (`f582d7db-5d09-5c3b-b775-24d3812b540b`) lines 408-429 [crates/gwiki/src/ingest/audio.rs:408-429]
  - Signature: `fn transcribe(`
  - Purpose: Indexed method `FakeTranscriptionClient.transcribe` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:408-429]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`5fa5393c-0c52-5650-a003-c3c5b369fb99`) lines 433-438 [crates/gwiki/src/ingest/audio.rs:433-438]
  - Signature: `struct ScriptedTranscriptionClient {`
  - Purpose: Indexed class `ScriptedTranscriptionClient` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:433-438]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`f8a17112-e824-58d4-a5e6-e389e38aa94e`) lines 441-463 [crates/gwiki/src/ingest/audio.rs:441-463]
  - Signature: `impl ScriptedTranscriptionClient {`
  - Purpose: Indexed class `ScriptedTranscriptionClient` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:441-463]
- `ScriptedTranscriptionClient.new` (method) component `ScriptedTranscriptionClient.new [method]` (`59c7ac5a-8fa0-54b2-a068-1b38fc6ee609`) lines 442-449 [crates/gwiki/src/ingest/audio.rs:442-449]
  - Signature: `fn new(transcriptions: Vec<TranscriptionOutput>) -> Self {`
  - Purpose: Indexed method `ScriptedTranscriptionClient.new` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:442-449]
- `ScriptedTranscriptionClient.with_english` (method) component `ScriptedTranscriptionClient.with_english [method]` (`ff5279e8-0b6b-5ea0-91c9-845ac43ce01c`) lines 451-458 [crates/gwiki/src/ingest/audio.rs:451-458]
  - Signature: `fn with_english(english: Vec<TranscriptionOutput>) -> Self {`
  - Purpose: Indexed method `ScriptedTranscriptionClient.with_english` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:451-458]
- `ScriptedTranscriptionClient.calls` (method) component `ScriptedTranscriptionClient.calls [method]` (`295202ba-a744-5ff7-b800-c2fb9d547eaa`) lines 460-462 [crates/gwiki/src/ingest/audio.rs:460-462]
  - Signature: `fn calls(&self) -> Rc<RefCell<Vec<&'static str>>> {`
  - Purpose: Indexed method `ScriptedTranscriptionClient.calls` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:460-462]
- `ScriptedTranscriptionClient` (class) component `ScriptedTranscriptionClient [class]` (`cfb1375d-868c-5991-8267-f103b7da819c`) lines 466-500 [crates/gwiki/src/ingest/audio.rs:466-500]
  - Signature: `impl TranscriptionClient for ScriptedTranscriptionClient {`
  - Purpose: Indexed class `ScriptedTranscriptionClient` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:466-500]
- `ScriptedTranscriptionClient.transcribe` (method) component `ScriptedTranscriptionClient.transcribe [method]` (`3d287f97-51bc-5c29-b04d-53cd1903fc7e`) lines 467-473 [crates/gwiki/src/ingest/audio.rs:467-473]
  - Signature: `fn transcribe(`
  - Purpose: Indexed method `ScriptedTranscriptionClient.transcribe` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:467-473]
- `ScriptedTranscriptionClient.translate_to_english` (method) component `ScriptedTranscriptionClient.translate_to_english [method]` (`90f9c915-e54d-5a7d-8655-f8d7e30613a1`) lines 475-482 [crates/gwiki/src/ingest/audio.rs:475-482]
  - Signature: `fn translate_to_english(`
  - Purpose: Indexed method `ScriptedTranscriptionClient.translate_to_english` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:475-482]
- `ScriptedTranscriptionClient.translate_segments` (method) component `ScriptedTranscriptionClient.translate_segments [method]` (`d716b3c0-b1f5-5dd8-a415-0f68f295299f`) lines 484-499 [crates/gwiki/src/ingest/audio.rs:484-499]
  - Signature: `fn translate_segments(`
  - Purpose: Indexed method `ScriptedTranscriptionClient.translate_segments` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:484-499]
- `test_context` (function) component `test_context [function]` (`efeab892-9cf0-5013-aa28-d5dc0e350af3`) lines 502-530 [crates/gwiki/src/ingest/audio.rs:502-530]
  - Signature: `fn test_context(routing: AiRouting, api_base: Option<String>) -> AiContext {`
  - Purpose: Indexed function `test_context` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:502-530]
- `spawn_transcription_server` (function) component `spawn_transcription_server [function]` (`44c797e1-cc73-5036-971c-41cc55132df6`) lines 533-537 [crates/gwiki/src/ingest/audio.rs:533-537]
  - Signature: `fn spawn_transcription_server(`
  - Purpose: Indexed function `spawn_transcription_server` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:533-537]
- `test_chunk` (function) component `test_chunk [function]` (`b198b3aa-e517-512e-a92f-a9322d80e0a2`) lines 540-548 [crates/gwiki/src/ingest/audio.rs:540-548]
  - Signature: `fn test_chunk(start_ms: u64, end_ms: u64) -> crate::ai::chunk::AudioChunk {`
  - Purpose: Indexed function `test_chunk` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:540-548]
- `transcript_output` (function) component `transcript_output [function]` (`7fc19776-e4b2-5760-80d8-aebbf3674cf2`) lines 551-577 [crates/gwiki/src/ingest/audio.rs:551-577]
  - Signature: `fn transcript_output(`
  - Purpose: Indexed function `transcript_output` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:551-577]
- `english_target_uses_primary_language_subtag` (function) component `english_target_uses_primary_language_subtag [function]` (`84c8e7bc-718a-587f-a16c-44e6cdb6c910`) lines 581-587 [crates/gwiki/src/ingest/audio.rs:581-587]
  - Signature: `fn english_target_uses_primary_language_subtag() {`
  - Purpose: Indexed function `english_target_uses_primary_language_subtag` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:581-587]
- `production_transcription_writes_fields` (function) component `production_transcription_writes_fields [function]` (`856ad106-e452-508f-8776-80a6c1f61c6e`) lines 591-625 [crates/gwiki/src/ingest/audio.rs:591-625]
  - Signature: `fn production_transcription_writes_fields() {`
  - Purpose: Indexed function `production_transcription_writes_fields` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:591-625]
- `production_path_applies_translation` (function) component `production_path_applies_translation [function]` (`8970c416-07ba-5032-a379-8be456bf20a0`) lines 629-663 [crates/gwiki/src/ingest/audio.rs:629-663]
  - Signature: `fn production_path_applies_translation() {`
  - Purpose: Indexed function `production_path_applies_translation` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:629-663]
- `production_path_chunks_long_audio` (function) component `production_path_chunks_long_audio [function]` (`034da3bd-8d49-5feb-ab68-d7af7f3d4587`) lines 667-693 [crates/gwiki/src/ingest/audio.rs:667-693]
  - Signature: `fn production_path_chunks_long_audio() {`
  - Purpose: Indexed function `production_path_chunks_long_audio` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:667-693]
- `long_media_chunks_then_translates` (function) component `long_media_chunks_then_translates [function]` (`952eb600-04f6-5dd1-841e-9f216d8ab5bf`) lines 697-734 [crates/gwiki/src/ingest/audio.rs:697-734]
  - Signature: `fn long_media_chunks_then_translates() {`
  - Purpose: Indexed function `long_media_chunks_then_translates` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:697-734]
- `long_english_translation_per_chunk` (function) component `long_english_translation_per_chunk [function]` (`f29d2b19-c1a6-5e40-be90-1c3633695d47`) lines 738-776 [crates/gwiki/src/ingest/audio.rs:738-776]
  - Signature: `fn long_english_translation_per_chunk() {`
  - Purpose: Indexed function `long_english_translation_per_chunk` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:738-776]
- `off_routing_degrades` (function) component `off_routing_degrades [function]` (`f95accc2-d77a-55b1-b36b-a81cea4b2f22`) lines 779-810 [crates/gwiki/src/ingest/audio.rs:779-810]
  - Signature: `fn off_routing_degrades() {`
  - Purpose: Indexed function `off_routing_degrades` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:779-810]
- `stores_original_audio` (function) component `stores_original_audio [function]` (`13b267a0-6988-5489-b75f-0a40366ee2eb`) lines 813-848 [crates/gwiki/src/ingest/audio.rs:813-848]
  - Signature: `fn stores_original_audio() {`
  - Purpose: Indexed function `stores_original_audio` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:813-848]
- `transcript_chunks_are_scope_searchable` (function) component `transcript_chunks_are_scope_searchable [function]` (`5231f9bc-1b57-58ab-b15d-8d840410c96f`) lines 851-886 [crates/gwiki/src/ingest/audio.rs:851-886]
  - Signature: `fn transcript_chunks_are_scope_searchable() {`
  - Purpose: Indexed function `transcript_chunks_are_scope_searchable` in `crates/gwiki/src/ingest/audio.rs`. [crates/gwiki/src/ingest/audio.rs:851-886]

