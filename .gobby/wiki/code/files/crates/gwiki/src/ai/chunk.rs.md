---
title: crates/gwiki/src/ai/chunk.rs
type: code_file
provenance:
- file: crates/gwiki/src/ai/chunk.rs
  ranges:
  - 24-30
  - 33-35
  - 38-47
  - 49-56
  - '58'
  - 60-91
  - 93-99
  - 101-113
  - 115-117
  - 120-131
  - 133-197
  - 199-214
  - 216-229
  - 231-245
  - 247-265
  - 267-272
  - 274-281
  - 283-289
  - 291-293
  - '301'
  - 304-310
  - 313-319
  - 322-324
  - 335-343
  - 346-351
  - 354-385
  - 388-403
  - 406-432
  - 435-487
  - 489-492
  - 494-501
  - 503-513
  - 515-517
  - 519-525
  - 527-534
  - 536-539
  - 541-562
  - 564-571
  - 574-584
  - 586-594
  - 596-617
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ai/chunk.rs

Module: [[code/modules/crates/gwiki/src/ai|crates/gwiki/src/ai]]

## Purpose

Provides the audio chunking and chunk-aware transcription pipeline for `gwiki`. It defines the chunk data model and transcription mode enum, an `AudioChunker` abstraction with a media-backed implementation that splits input audio into overlapping windows, plus orchestration helpers that decide whether chunking is needed, run single or multi-chunk transcription/translation requests, merge chunk metadata and segment offsets, deduplicate overlaps, and expose test-only chunk/client fakes for deterministic validation.
[crates/gwiki/src/ai/chunk.rs:24-30]
[crates/gwiki/src/ai/chunk.rs:33-35]
[crates/gwiki/src/ai/chunk.rs:38-47]
[crates/gwiki/src/ai/chunk.rs:49-56]
[crates/gwiki/src/ai/chunk.rs:58]

## API Symbols

- `AudioChunk` (class) component `AudioChunk [class]` (`99d4c691-dfda-5bf7-9154-8ca2a31b3a61`) lines 24-30 [crates/gwiki/src/ai/chunk.rs:24-30]
  - Signature: `pub(crate) struct AudioChunk {`
  - Purpose: Indexed class `AudioChunk` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:24-30]
- `ChunkedTranscription` (class) component `ChunkedTranscription [class]` (`270c9a29-9b4c-5d6c-ad9f-73b10e5bf6ad`) lines 33-35 [crates/gwiki/src/ai/chunk.rs:33-35]
  - Signature: `pub(crate) struct ChunkedTranscription {`
  - Purpose: Indexed class `ChunkedTranscription` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:33-35]
- `ChunkTranscriptionMode` (type) component `ChunkTranscriptionMode [type]` (`8ae08779-b852-5d7a-8763-1c6d65a30177`) lines 38-47 [crates/gwiki/src/ai/chunk.rs:38-47]
  - Signature: `pub(crate) enum ChunkTranscriptionMode<'a> {`
  - Purpose: Indexed type `ChunkTranscriptionMode` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:38-47]
- `AudioChunker` (type) component `AudioChunker [type]` (`759d49c3-03e6-523a-a287-171a836bc3ba`) lines 49-56 [crates/gwiki/src/ai/chunk.rs:49-56]
  - Signature: `pub(crate) trait AudioChunker {`
  - Purpose: Indexed type `AudioChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:49-56]
- `MediaAudioChunker` (class) component `MediaAudioChunker [class]` (`945ab5b2-6115-5b67-9a6d-9b0b5a1be1e6`) lines 58-58 [crates/gwiki/src/ai/chunk.rs:58]
  - Signature: `pub(crate) struct MediaAudioChunker;`
  - Purpose: Indexed class `MediaAudioChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:58]
- `MediaAudioChunker` (class) component `MediaAudioChunker [class]` (`bb4b3224-97f0-5bde-8d4a-958ee4e72772`) lines 60-91 [crates/gwiki/src/ai/chunk.rs:60-91]
  - Signature: `impl AudioChunker for MediaAudioChunker {`
  - Purpose: Indexed class `MediaAudioChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:60-91]
- `MediaAudioChunker.split` (method) component `MediaAudioChunker.split [method]` (`9fea3e6c-e32d-529f-8bc4-8ba89de1b308`) lines 61-90 [crates/gwiki/src/ai/chunk.rs:61-90]
  - Signature: `fn split(`
  - Purpose: Indexed method `MediaAudioChunker.split` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:61-90]
- `transcribe_audio_request` (function) component `transcribe_audio_request [function]` (`d9f09b8a-7270-5c34-bb73-ea61d59b2414`) lines 93-99 [crates/gwiki/src/ai/chunk.rs:93-99]
  - Signature: `pub(crate) fn transcribe_audio_request(`
  - Purpose: Indexed function `transcribe_audio_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:93-99]
- `transcribe_audio_request_with_chunker` (function) component `transcribe_audio_request_with_chunker [function]` (`6c99fd97-6662-57c3-85ab-4c96e3ab185a`) lines 101-113 [crates/gwiki/src/ai/chunk.rs:101-113]
  - Signature: `pub(crate) fn transcribe_audio_request_with_chunker(`
  - Purpose: Indexed function `transcribe_audio_request_with_chunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:101-113]
- `requires_chunking` (function) component `requires_chunking [function]` (`116f69a0-f880-5019-975f-def711dc9e64`) lines 115-117 [crates/gwiki/src/ai/chunk.rs:115-117]
  - Signature: `pub(crate) fn requires_chunking(byte_len: usize) -> bool {`
  - Purpose: Indexed function `requires_chunking` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:115-117]
- `fixed_codec_bytes_for_duration` (function) component `fixed_codec_bytes_for_duration [function]` (`8d97b2cb-14ed-5d70-a5b5-e0d4c8a1cc6f`) lines 120-131 [crates/gwiki/src/ai/chunk.rs:120-131]
  - Signature: `pub(crate) fn fixed_codec_bytes_for_duration(duration: Duration) -> u64 {`
  - Purpose: Indexed function `fixed_codec_bytes_for_duration` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:120-131]
- `transcribe_chunks` (function) component `transcribe_chunks [function]` (`e2ed3550-e591-5579-b61a-dff45e20be66`) lines 133-197 [crates/gwiki/src/ai/chunk.rs:133-197]
  - Signature: `fn transcribe_chunks(`
  - Purpose: Indexed function `transcribe_chunks` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:133-197]
- `transcribe_single_request` (function) component `transcribe_single_request [function]` (`f04c0c9a-ce85-57c8-b735-92cb547957e1`) lines 199-214 [crates/gwiki/src/ai/chunk.rs:199-214]
  - Signature: `fn transcribe_single_request(`
  - Purpose: Indexed function `transcribe_single_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:199-214]
- `transcribe_chunk_request` (function) component `transcribe_chunk_request [function]` (`8462dc1a-17dc-5d4e-bad8-9089e0480b28`) lines 216-229 [crates/gwiki/src/ai/chunk.rs:216-229]
  - Signature: `fn transcribe_chunk_request(`
  - Purpose: Indexed function `transcribe_chunk_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:216-229]
- `empty_output` (function) component `empty_output [function]` (`0bba5ae7-9a7f-54ae-b259-59a3cb38c74e`) lines 231-245 [crates/gwiki/src/ai/chunk.rs:231-245]
  - Signature: `fn empty_output() -> TranscriptionOutput {`
  - Purpose: Indexed function `empty_output` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:231-245]
- `merge_metadata` (function) component `merge_metadata [function]` (`c16fb735-7edd-5650-ae57-4a05685a9854`) lines 247-265 [crates/gwiki/src/ai/chunk.rs:247-265]
  - Signature: `fn merge_metadata(aggregate: &mut TranscriptionOutput, output: &TranscriptionOutput) {`
  - Purpose: Indexed function `merge_metadata` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:247-265]
- `offset_segments` (function) component `offset_segments [function]` (`64b197d7-5940-5ead-a8b0-f4199f288211`) lines 267-272 [crates/gwiki/src/ai/chunk.rs:267-272]
  - Signature: `fn offset_segments(segments: &mut [TranscriptSegment], chunk_start_ms: u64) {`
  - Purpose: Indexed function `offset_segments` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:267-272]
- `append_deduped` (function) component `append_deduped [function]` (`340fe496-9134-530a-ad48-cce32b041a1c`) lines 274-281 [crates/gwiki/src/ai/chunk.rs:274-281]
  - Signature: `fn append_deduped(segments: &mut Vec<TranscriptSegment>, incoming: Vec<TranscriptSegment>) {`
  - Purpose: Indexed function `append_deduped` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:274-281]
- `is_overlap_duplicate` (function) component `is_overlap_duplicate [function]` (`8e81426b-4c28-50f7-a59b-c80b51ac411d`) lines 283-289 [crates/gwiki/src/ai/chunk.rs:283-289]
  - Signature: `fn is_overlap_duplicate(previous: Option<&TranscriptSegment>, segment: &TranscriptSegment) -> bool {`
  - Purpose: Indexed function `is_overlap_duplicate` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:283-289]
- `duration_ms` (function) component `duration_ms [function]` (`ea13568e-a8ec-5239-acb8-e827a3cafdff`) lines 291-293 [crates/gwiki/src/ai/chunk.rs:291-293]
  - Signature: `fn duration_ms(duration: Duration) -> u64 {`
  - Purpose: Indexed function `duration_ms` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:291-293]
- `TestChunkGuard` (class) component `TestChunkGuard [class]` (`dc135a34-d790-5b00-9645-aad4234cd1a4`) lines 301-301 [crates/gwiki/src/ai/chunk.rs:301]
  - Signature: `pub(crate) struct TestChunkGuard;`
  - Purpose: Indexed class `TestChunkGuard` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:301]
- `TestChunkGuard` (class) component `TestChunkGuard [class]` (`931b1fbf-615c-5db8-9954-9555606dcc0a`) lines 304-310 [crates/gwiki/src/ai/chunk.rs:304-310]
  - Signature: `impl Drop for TestChunkGuard {`
  - Purpose: Indexed class `TestChunkGuard` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:304-310]
- `TestChunkGuard.drop` (method) component `TestChunkGuard.drop [method]` (`f1587e0b-59e4-5bfb-8592-a1834ddd9854`) lines 305-309 [crates/gwiki/src/ai/chunk.rs:305-309]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Indexed method `TestChunkGuard.drop` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:305-309]
- `install_test_chunks` (function) component `install_test_chunks [function]` (`f6dcf15f-318c-5efa-a2e6-5a5dcc125a0c`) lines 313-319 [crates/gwiki/src/ai/chunk.rs:313-319]
  - Signature: `pub(crate) fn install_test_chunks(chunks: Vec<AudioChunk>) -> TestChunkGuard {`
  - Purpose: Indexed function `install_test_chunks` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:313-319]
- `take_test_chunks` (function) component `take_test_chunks [function]` (`fff4cd9f-4ce5-5e8e-9a32-d325b7f71656`) lines 322-324 [crates/gwiki/src/ai/chunk.rs:322-324]
  - Signature: `fn take_test_chunks() -> Option<Vec<AudioChunk>> {`
  - Purpose: Indexed function `take_test_chunks` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:322-324]
- `chunks_under_limit_fixed_codec` (function) component `chunks_under_limit_fixed_codec [function]` (`cae3c47e-f4b3-55e8-8d41-b2f2bc71a58d`) lines 335-343 [crates/gwiki/src/ai/chunk.rs:335-343]
  - Signature: `fn chunks_under_limit_fixed_codec() {`
  - Purpose: Indexed function `chunks_under_limit_fixed_codec` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:335-343]
- `fixed_codec_bytes_include_subsecond_durations` (function) component `fixed_codec_bytes_include_subsecond_durations [function]` (`b83e0c76-dd3b-59bb-b51c-015cae7f3c0c`) lines 346-351 [crates/gwiki/src/ai/chunk.rs:346-351]
  - Signature: `fn fixed_codec_bytes_include_subsecond_durations() {`
  - Purpose: Indexed function `fixed_codec_bytes_include_subsecond_durations` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:346-351]
- `offsets_and_dedups` (function) component `offsets_and_dedups [function]` (`8f8dd60c-a0cb-564f-8ad4-c3a2e22fffbf`) lines 354-385 [crates/gwiki/src/ai/chunk.rs:354-385]
  - Signature: `fn offsets_and_dedups() {`
  - Purpose: Indexed function `offsets_and_dedups` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:354-385]
- `short_audio_bypasses_ffmpeg` (function) component `short_audio_bypasses_ffmpeg [function]` (`df38bf33-83af-5cdd-a861-109997a590f2`) lines 388-403 [crates/gwiki/src/ai/chunk.rs:388-403]
  - Signature: `fn short_audio_bypasses_ffmpeg() {`
  - Purpose: Indexed function `short_audio_bypasses_ffmpeg` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:388-403]
- `short_translate_segments_translates_without_chunking` (function) component `short_translate_segments_translates_without_chunking [function]` (`1db02227-f21d-509d-af5e-e9863d7f7e82`) lines 406-432 [crates/gwiki/src/ai/chunk.rs:406-432]
  - Signature: `fn short_translate_segments_translates_without_chunking() {`
  - Purpose: Indexed function `short_translate_segments_translates_without_chunking` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:406-432]
- `partial_chunk_outcome` (function) component `partial_chunk_outcome [function]` (`33651774-9616-55ab-b2e0-9b83d8ea2f2b`) lines 435-487 [crates/gwiki/src/ai/chunk.rs:435-487]
  - Signature: `fn partial_chunk_outcome() {`
  - Purpose: Indexed function `partial_chunk_outcome` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:435-487]
- `FakeChunker` (class) component `FakeChunker [class]` (`8745a368-f755-5409-8110-0b408b1a8fb4`) lines 489-492 [crates/gwiki/src/ai/chunk.rs:489-492]
  - Signature: `struct FakeChunker {`
  - Purpose: Indexed class `FakeChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:489-492]
- `FakeChunker` (class) component `FakeChunker [class]` (`132683f6-686e-52e6-884b-ecb74706b366`) lines 494-501 [crates/gwiki/src/ai/chunk.rs:494-501]
  - Signature: `impl FakeChunker {`
  - Purpose: Indexed class `FakeChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:494-501]
- `FakeChunker.new` (method) component `FakeChunker.new [method]` (`348b0eb2-6d72-5b77-a2da-b91ae7b03925`) lines 495-500 [crates/gwiki/src/ai/chunk.rs:495-500]
  - Signature: `fn new(chunks: Vec<AudioChunk>) -> Self {`
  - Purpose: Indexed method `FakeChunker.new` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:495-500]
- `FakeChunker` (class) component `FakeChunker [class]` (`595ea295-5833-5355-88e3-9b64c6144f8a`) lines 503-513 [crates/gwiki/src/ai/chunk.rs:503-513]
  - Signature: `impl AudioChunker for FakeChunker {`
  - Purpose: Indexed class `FakeChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:503-513]
- `FakeChunker.split` (method) component `FakeChunker.split [method]` (`5f7381a4-e384-588c-97a4-3bfd8474b77e`) lines 504-512 [crates/gwiki/src/ai/chunk.rs:504-512]
  - Signature: `fn split(`
  - Purpose: Indexed method `FakeChunker.split` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:504-512]
- `ScriptedClient` (class) component `ScriptedClient [class]` (`e219f739-7eb5-5511-b039-3375b9eaaaff`) lines 515-517 [crates/gwiki/src/ai/chunk.rs:515-517]
  - Signature: `struct ScriptedClient {`
  - Purpose: Indexed class `ScriptedClient` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:515-517]
- `ScriptedClient` (class) component `ScriptedClient [class]` (`5a28af47-796c-5967-8ad4-f1860bfe5ee7`) lines 519-525 [crates/gwiki/src/ai/chunk.rs:519-525]
  - Signature: `impl ScriptedClient {`
  - Purpose: Indexed class `ScriptedClient` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:519-525]
- `ScriptedClient.new` (method) component `ScriptedClient.new [method]` (`bcb7e389-6c80-5e7e-82c5-d7732c5296e3`) lines 520-524 [crates/gwiki/src/ai/chunk.rs:520-524]
  - Signature: `fn new(outputs: Vec<Result<TranscriptionOutput, WikiError>>) -> Self {`
  - Purpose: Indexed method `ScriptedClient.new` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:520-524]
- `ScriptedClient` (class) component `ScriptedClient [class]` (`13f6e579-d6c0-5889-8ef2-7115f618f0fd`) lines 527-534 [crates/gwiki/src/ai/chunk.rs:527-534]
  - Signature: `impl TranscriptionClient for ScriptedClient {`
  - Purpose: Indexed class `ScriptedClient` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:527-534]
- `ScriptedClient.transcribe` (method) component `ScriptedClient.transcribe [method]` (`bfeb0041-b4ea-5a79-8868-2bf9b076c202`) lines 528-533 [crates/gwiki/src/ai/chunk.rs:528-533]
  - Signature: `fn transcribe(`
  - Purpose: Indexed method `ScriptedClient.transcribe` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:528-533]
- `TranslatingClient` (class) component `TranslatingClient [class]` (`1b5c2e4b-76f6-50d8-b5e2-29fe6b68672e`) lines 536-539 [crates/gwiki/src/ai/chunk.rs:536-539]
  - Signature: `struct TranslatingClient {`
  - Purpose: Indexed class `TranslatingClient` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:536-539]
- `TranslatingClient` (class) component `TranslatingClient [class]` (`f17d0805-d0eb-5047-80f7-713c22e6b054`) lines 541-562 [crates/gwiki/src/ai/chunk.rs:541-562]
  - Signature: `impl TranscriptionClient for TranslatingClient {`
  - Purpose: Indexed class `TranslatingClient` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:541-562]
- `TranslatingClient.transcribe` (method) component `TranslatingClient.transcribe [method]` (`43cd0fa7-96a0-562d-9cdd-ea1ee1be8ead`) lines 542-548 [crates/gwiki/src/ai/chunk.rs:542-548]
  - Signature: `fn transcribe(`
  - Purpose: Indexed method `TranslatingClient.transcribe` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:542-548]
- `TranslatingClient.translate_segments` (method) component `TranslatingClient.translate_segments [method]` (`4cdc5c5f-093b-5106-b927-b7377fb4ddd4`) lines 550-561 [crates/gwiki/src/ai/chunk.rs:550-561]
  - Signature: `fn translate_segments(`
  - Purpose: Indexed method `TranslatingClient.translate_segments` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:550-561]
- `short_request` (function) component `short_request [function]` (`bdc4c9b3-8191-57c9-bb3f-cd9a57bb1fb3`) lines 564-571 [crates/gwiki/src/ai/chunk.rs:564-571]
  - Signature: `fn short_request<'a>() -> TranscriptionRequest<'a> {`
  - Purpose: Indexed function `short_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:564-571]
- `long_request` (function) component `long_request [function]` (`09a675c3-26fa-564c-ae87-db20b2741545`) lines 574-584 [crates/gwiki/src/ai/chunk.rs:574-584]
  - Signature: `fn long_request<'a>() -> TranscriptionRequest<'a> {`
  - Purpose: Indexed function `long_request` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:574-584]
- `chunk` (function) component `chunk [function]` (`ec725125-cb3a-5a67-ac1d-68001f0e2d11`) lines 586-594 [crates/gwiki/src/ai/chunk.rs:586-594]
  - Signature: `fn chunk(start_ms: u64, end_ms: u64) -> AudioChunk {`
  - Purpose: Indexed function `chunk` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:586-594]
- `output` (function) component `output [function]` (`ab32eb8d-5a46-5b17-960a-2bc77e4e7b6e`) lines 596-617 [crates/gwiki/src/ai/chunk.rs:596-617]
  - Signature: `fn output(source_lang: &str, segments: &[(u64, u64, &str)]) -> TranscriptionOutput {`
  - Purpose: Indexed function `output` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:596-617]

