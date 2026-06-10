---
title: crates/gwiki/src/ai/chunk.rs
type: code_file
provenance:
- file: crates/gwiki/src/ai/chunk.rs
  ranges:
  - 20-26
  - 29-31
  - 34-43
  - 45-52
  - '54'
  - 56-87
  - 57-86
  - 89-95
  - 97-109
  - 111-113
  - 115-126
  - 128-192
  - 194-209
  - 211-224
  - 226-240
  - 242-260
  - 262-267
  - 269-276
  - 278-284
  - 286-288
  - '296'
  - 299-305
  - 300-304
  - 308-314
  - 317-319
  - 330-338
  - 341-346
  - 349-380
  - 383-398
  - 401-427
  - 430-482
  - 484-487
  - 489-496
  - 490-495
  - 498-508
  - 499-507
  - 510-512
  - 514-520
  - 515-519
  - 522-529
  - 523-528
  - 531-534
  - 536-557
  - 537-543
  - 545-556
  - 559-566
  - 569-579
  - 581-589
  - 591-612
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ai/chunk.rs

Module: [[code/modules/crates/gwiki/src/ai|crates/gwiki/src/ai]]

## Purpose

`crates/gwiki/src/ai/chunk.rs` exposes 49 indexed API symbols.
[crates/gwiki/src/ai/chunk.rs:20-26]
[crates/gwiki/src/ai/chunk.rs:29-31]
[crates/gwiki/src/ai/chunk.rs:34-43]
[crates/gwiki/src/ai/chunk.rs:45-52]
[crates/gwiki/src/ai/chunk.rs:54]
[crates/gwiki/src/ai/chunk.rs:56-87]
[crates/gwiki/src/ai/chunk.rs:57-86]
[crates/gwiki/src/ai/chunk.rs:89-95]
[crates/gwiki/src/ai/chunk.rs:97-109]
[crates/gwiki/src/ai/chunk.rs:111-113]
[crates/gwiki/src/ai/chunk.rs:115-126]
[crates/gwiki/src/ai/chunk.rs:128-192]
[crates/gwiki/src/ai/chunk.rs:194-209]
[crates/gwiki/src/ai/chunk.rs:211-224]
[crates/gwiki/src/ai/chunk.rs:226-240]
[crates/gwiki/src/ai/chunk.rs:242-260]
[crates/gwiki/src/ai/chunk.rs:262-267]
[crates/gwiki/src/ai/chunk.rs:269-276]
[crates/gwiki/src/ai/chunk.rs:278-284]
[crates/gwiki/src/ai/chunk.rs:286-288]
[crates/gwiki/src/ai/chunk.rs:296]
[crates/gwiki/src/ai/chunk.rs:299-305]
[crates/gwiki/src/ai/chunk.rs:300-304]
[crates/gwiki/src/ai/chunk.rs:308-314]
[crates/gwiki/src/ai/chunk.rs:317-319]
[crates/gwiki/src/ai/chunk.rs:330-338]
[crates/gwiki/src/ai/chunk.rs:341-346]
[crates/gwiki/src/ai/chunk.rs:349-380]
[crates/gwiki/src/ai/chunk.rs:383-398]
[crates/gwiki/src/ai/chunk.rs:401-427]
[crates/gwiki/src/ai/chunk.rs:430-482]
[crates/gwiki/src/ai/chunk.rs:484-487]
[crates/gwiki/src/ai/chunk.rs:489-496]
[crates/gwiki/src/ai/chunk.rs:490-495]
[crates/gwiki/src/ai/chunk.rs:498-508]
[crates/gwiki/src/ai/chunk.rs:499-507]
[crates/gwiki/src/ai/chunk.rs:510-512]
[crates/gwiki/src/ai/chunk.rs:514-520]
[crates/gwiki/src/ai/chunk.rs:515-519]
[crates/gwiki/src/ai/chunk.rs:522-529]
[crates/gwiki/src/ai/chunk.rs:523-528]
[crates/gwiki/src/ai/chunk.rs:531-534]
[crates/gwiki/src/ai/chunk.rs:536-557]
[crates/gwiki/src/ai/chunk.rs:537-543]
[crates/gwiki/src/ai/chunk.rs:545-556]
[crates/gwiki/src/ai/chunk.rs:559-566]
[crates/gwiki/src/ai/chunk.rs:569-579]
[crates/gwiki/src/ai/chunk.rs:581-589]
[crates/gwiki/src/ai/chunk.rs:591-612]

## API Symbols

- `AudioChunk` (class) component `AudioChunk [class]` (`5b10656e-3a0b-5921-96d0-391a1d456e7f`) lines 20-26 [crates/gwiki/src/ai/chunk.rs:20-26]
  - Signature: `pub(crate) struct AudioChunk {`
  - Purpose: AudioChunk is a crate-private struct that encapsulates a temporal segment of audio data, bounded by millisecond-precision start and end timestamps, along with source file metadata and raw audio bytes. [crates/gwiki/src/ai/chunk.rs:20-26]
- `ChunkedTranscription` (class) component `ChunkedTranscription [class]` (`18b40579-1b07-5698-98e4-4fc191dfc07f`) lines 29-31 [crates/gwiki/src/ai/chunk.rs:29-31]
  - Signature: `pub(crate) struct ChunkedTranscription {`
  - Purpose: `ChunkedTranscription` is a crate-private wrapper struct that encapsulates a single `TranscriptionOutput` field. [crates/gwiki/src/ai/chunk.rs:29-31]
- `ChunkTranscriptionMode` (type) component `ChunkTranscriptionMode [type]` (`1e6cc1e0-a2ad-5e11-939a-4595a7330122`) lines 34-43 [crates/gwiki/src/ai/chunk.rs:34-43]
  - Signature: `pub(crate) enum ChunkTranscriptionMode<'a> {`
  - Purpose: Indexed type `ChunkTranscriptionMode` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:34-43]
- `AudioChunker` (type) component `AudioChunker [type]` (`99e4d193-357a-5965-a495-991a8c04b3f8`) lines 45-52 [crates/gwiki/src/ai/chunk.rs:45-52]
  - Signature: `pub(crate) trait AudioChunker {`
  - Purpose: Indexed type `AudioChunker` in `crates/gwiki/src/ai/chunk.rs`. [crates/gwiki/src/ai/chunk.rs:45-52]
- `MediaAudioChunker` (class) component `MediaAudioChunker [class]` (`9ec8c88b-d3aa-5559-98b7-5926db987124`) lines 54-54 [crates/gwiki/src/ai/chunk.rs:54]
  - Signature: `pub(crate) struct MediaAudioChunker;`
  - Purpose: MediaAudioChunker is a crate-internal unit struct designed to handle segmentation of audio media data into chunks. [crates/gwiki/src/ai/chunk.rs:54]
- `MediaAudioChunker` (class) component `MediaAudioChunker [class]` (`c459975b-a378-5c2a-a14c-bb6059bbb3fd`) lines 56-87 [crates/gwiki/src/ai/chunk.rs:56-87]
  - Signature: `impl AudioChunker for MediaAudioChunker {`
  - Purpose: `MediaAudioChunker` implements `AudioChunker` to partition an audio file into overlapping temporal chunks based on specified window and overlap durations, load each chunk's bytes from disk, and return `AudioChunk` structs with timing metadata and enumerated filenames. [crates/gwiki/src/ai/chunk.rs:56-87]
- `MediaAudioChunker.split` (method) component `MediaAudioChunker.split [method]` (`8e5e97c7-d111-5e56-b2e0-ee9443dd827c`) lines 57-86 [crates/gwiki/src/ai/chunk.rs:57-86]
  - Signature: `fn split(`
  - Purpose: Splits an audio file into overlapping chunks with specified window and overlap durations, loads each chunk's bytes from disk, and returns indexed `AudioChunk` objects containing audio data and temporal metadata. [crates/gwiki/src/ai/chunk.rs:57-86]
- `transcribe_audio_request` (function) component `transcribe_audio_request [function]` (`085c5ced-b37b-53e0-9884-d2bb904cdf99`) lines 89-95 [crates/gwiki/src/ai/chunk.rs:89-95]
  - Signature: `pub(crate) fn transcribe_audio_request(`
  - Purpose: This function transcribes audio by delegating to `transcribe_audio_request_with_chunker` with a `MediaAudioChunker` as the default chunking strategy. [crates/gwiki/src/ai/chunk.rs:89-95]
- `transcribe_audio_request_with_chunker` (function) component `transcribe_audio_request_with_chunker [function]` (`2868c726-d5cc-5c20-9d65-393b7a63b3d0`) lines 97-109 [crates/gwiki/src/ai/chunk.rs:97-109]
  - Signature: `pub(crate) fn transcribe_audio_request_with_chunker(`
  - Purpose: Transcribes audio by conditionally splitting it into overlapping chunks based on a size threshold and delegating transcription to a client, returning the aggregated output. [crates/gwiki/src/ai/chunk.rs:97-109]
- `requires_chunking` (function) component `requires_chunking [function]` (`ea36564b-0daf-5412-b21e-e17a2b86ddc9`) lines 111-113 [crates/gwiki/src/ai/chunk.rs:111-113]
  - Signature: `pub(crate) fn requires_chunking(byte_len: usize) -> bool {`
  - Purpose: Returns `true` if the provided byte length exceeds the `MAX_AUDIO_UPLOAD_BYTES` threshold, indicating the audio file requires chunked uploading. [crates/gwiki/src/ai/chunk.rs:111-113]
- `fixed_codec_bytes_for_duration` (function) component `fixed_codec_bytes_for_duration [function]` (`6fe1dc03-111d-58cc-a1d2-74e8f423d35e`) lines 115-126 [crates/gwiki/src/ai/chunk.rs:115-126]
  - Signature: `pub(crate) fn fixed_codec_bytes_for_duration(duration: Duration) -> u64 {`
  - Purpose: Calculates the total byte size of a fixed PCM WAV file (including header) for a given duration, using ceiling division to round up partial sample frames. [crates/gwiki/src/ai/chunk.rs:115-126]
- `transcribe_chunks` (function) component `transcribe_chunks [function]` (`00e01ad6-2c4c-53c8-8b4e-89e3a518d83f`) lines 128-192 [crates/gwiki/src/ai/chunk.rs:128-192]
  - Signature: `fn transcribe_chunks(`
  - Purpose: Transcribes sorted audio chunks via a client interface, aggregates deduplicated segments with temporal offset correction, tracks completed and missing time ranges, optionally translates segments, and returns partial results unless all chunks fail. [crates/gwiki/src/ai/chunk.rs:128-192]
- `transcribe_single_request` (function) component `transcribe_single_request [function]` (`e449740a-8e56-565a-8f03-369da3f56d96`) lines 194-209 [crates/gwiki/src/ai/chunk.rs:194-209]
  - Signature: `fn transcribe_single_request(`
  - Purpose: Routes a transcription request to either direct transcription or audio translation (to a specified target language or English) based on the `ChunkTranscriptionMode` variant. [crates/gwiki/src/ai/chunk.rs:194-209]
- `transcribe_chunk_request` (function) component `transcribe_chunk_request [function]` (`a943c16c-1ab4-518d-b4d9-2c3d1cfcf200`) lines 211-224 [crates/gwiki/src/ai/chunk.rs:211-224]
  - Signature: `fn transcribe_chunk_request(`
  - Purpose: This function dispatches a transcription request to either the client's transcription method or an audio-to-English translation function based on the specified `ChunkTranscriptionMode`. [crates/gwiki/src/ai/chunk.rs:211-224]
- `empty_output` (function) component `empty_output [function]` (`5c6c7259-d9a3-58dc-b550-d07aa5872039`) lines 226-240 [crates/gwiki/src/ai/chunk.rs:226-240]
  - Signature: `fn empty_output() -> TranscriptionOutput {`
  - Purpose: Returns a `TranscriptionOutput` struct initialized with empty vectors for segments and ranges, and `None`/`false` defaults for all metadata fields. [crates/gwiki/src/ai/chunk.rs:226-240]
- `merge_metadata` (function) component `merge_metadata [function]` (`d86dd1f2-05eb-58d3-a3f3-adb5877b58da`) lines 242-260 [crates/gwiki/src/ai/chunk.rs:242-260]
  - Signature: `fn merge_metadata(aggregate: &mut TranscriptionOutput, output: &TranscriptionOutput) {`
  - Purpose: Merges transcription metadata from one `TranscriptionOutput` into another by populating unset optional fields and combining boolean translation flags via bitwise OR. [crates/gwiki/src/ai/chunk.rs:242-260]
- `offset_segments` (function) component `offset_segments [function]` (`14c37a4e-3851-52d7-ae88-6584ec83cbd0`) lines 262-267 [crates/gwiki/src/ai/chunk.rs:262-267]
  - Signature: `fn offset_segments(segments: &mut [TranscriptSegment], chunk_start_ms: u64) {`
  - Purpose: Offsets the start and end timestamps of all transcript segments forward by a specified millisecond value using saturating addition to prevent integer overflow. [crates/gwiki/src/ai/chunk.rs:262-267]
- `append_deduped` (function) component `append_deduped [function]` (`c0cf3a88-92ae-568a-bd3d-1330889e2486`) lines 269-276 [crates/gwiki/src/ai/chunk.rs:269-276]
  - Signature: `fn append_deduped(segments: &mut Vec<TranscriptSegment>, incoming: Vec<TranscriptSegment>) {`
  - Purpose: Appends incoming transcript segments to a mutable vector while skipping any that are overlap duplicates of the last segment. [crates/gwiki/src/ai/chunk.rs:269-276]
- `is_overlap_duplicate` (function) component `is_overlap_duplicate [function]` (`7a638868-928d-5626-982a-b5411b7f9beb`) lines 278-284 [crates/gwiki/src/ai/chunk.rs:278-284]
  - Signature: `fn is_overlap_duplicate(previous: Option<&TranscriptSegment>, segment: &TranscriptSegment) -> bool {`
  - Purpose: Returns true if a segment's trimmed text matches the previous segment's and its start time falls within a configured overlap duration after the previous segment ends. [crates/gwiki/src/ai/chunk.rs:278-284]
- `duration_ms` (function) component `duration_ms [function]` (`e0f6fc3f-7dc5-5322-a7df-d2b1ff4f19ed`) lines 286-288 [crates/gwiki/src/ai/chunk.rs:286-288]
  - Signature: `fn duration_ms(duration: Duration) -> u64 {`
  - Purpose: Converts a Duration to milliseconds and returns the result as a u64, saturating to u64::MAX on overflow. [crates/gwiki/src/ai/chunk.rs:286-288]
- `TestChunkGuard` (class) component `TestChunkGuard [class]` (`c9161009-6e95-5ce8-85ea-2124523840fe`) lines 296-296 [crates/gwiki/src/ai/chunk.rs:296]
  - Signature: `pub(crate) struct TestChunkGuard;`
  - Purpose: TestChunkGuard is a crate-private, zero-sized unit struct likely serving as a type-level guard or scope marker for test chunk management. [crates/gwiki/src/ai/chunk.rs:296]
- `TestChunkGuard` (class) component `TestChunkGuard [class]` (`29e2c101-8b05-56a0-a2c0-596c23fe23dd`) lines 299-305 [crates/gwiki/src/ai/chunk.rs:299-305]
  - Signature: `impl Drop for TestChunkGuard {`
  - Purpose: `TestChunkGuard` is a RAII guard that clears the thread-local `TEST_CHUNKS` variable by calling `take()` when the instance is dropped. [crates/gwiki/src/ai/chunk.rs:299-305]
- `TestChunkGuard.drop` (method) component `TestChunkGuard.drop [method]` (`4aee73d4-4114-555d-be95-cb146f47d8fa`) lines 300-304 [crates/gwiki/src/ai/chunk.rs:300-304]
  - Signature: `fn drop(&mut self) {`
  - Purpose: The `drop` method resets the thread-local `TEST_CHUNKS` storage to `None` by taking ownership of its contents via `RefCell::borrow_mut().take()`. [crates/gwiki/src/ai/chunk.rs:300-304]
- `install_test_chunks` (function) component `install_test_chunks [function]` (`6deac8da-cea2-5625-8db8-a17c2679d156`) lines 308-314 [crates/gwiki/src/ai/chunk.rs:308-314]
  - Signature: `pub(crate) fn install_test_chunks(chunks: Vec<AudioChunk>) -> TestChunkGuard {`
  - Purpose: Installs a vector of `AudioChunk` objects into thread-local storage after asserting it hasn't been previously installed, and returns a `TestChunkGuard` for cleanup. [crates/gwiki/src/ai/chunk.rs:308-314]
- `take_test_chunks` (function) component `take_test_chunks [function]` (`7e08a5f7-98f8-569f-b6d0-fcaee5ff6fbb`) lines 317-319 [crates/gwiki/src/ai/chunk.rs:317-319]
  - Signature: `fn take_test_chunks() -> Option<Vec<AudioChunk>> {`
  - Purpose: Extracts and clears the thread-local `TEST_CHUNKS` variable, returning the contained `Vec<AudioChunk>` wrapped in an `Option`. [crates/gwiki/src/ai/chunk.rs:317-319]
- `chunks_under_limit_fixed_codec` (function) component `chunks_under_limit_fixed_codec [function]` (`9ed109d6-8c72-50d2-9715-cdbce24accfc`) lines 330-338 [crates/gwiki/src/ai/chunk.rs:330-338]
  - Signature: `fn chunks_under_limit_fixed_codec() {`
  - Purpose: Asserts that fixed-codec audio with 16kHz sample rate, mono, and 2 bytes-per-sample produces chunks compliant with maximum upload size and duration (≤750 seconds) constraints. [crates/gwiki/src/ai/chunk.rs:330-338]
- `fixed_codec_bytes_include_subsecond_durations` (function) component `fixed_codec_bytes_include_subsecond_durations [function]` (`8183464d-1237-583c-a35a-c1734d59854c`) lines 341-346 [crates/gwiki/src/ai/chunk.rs:341-346]
  - Signature: `fn fixed_codec_bytes_include_subsecond_durations() {`
  - Purpose: This test asserts that calculating fixed-codec bytes for a 500-millisecond audio duration yields a result equal to the PCM WAV header size plus 16,000 data bytes. [crates/gwiki/src/ai/chunk.rs:341-346]
- `offsets_and_dedups` (function) component `offsets_and_dedups [function]` (`92d28312-6e59-5904-b7e9-197c41d49e34`) lines 349-380 [crates/gwiki/src/ai/chunk.rs:349-380]
  - Signature: `fn offsets_and_dedups() {`
  - Purpose: Tests that the transcription stitcher correctly deduplicates and merges overlapping transcription segments from multiple chunked audio sources while preserving their time offsets. [crates/gwiki/src/ai/chunk.rs:349-380]
- `short_audio_bypasses_ffmpeg` (function) component `short_audio_bypasses_ffmpeg [function]` (`ec3d501d-f4ac-54b7-abf4-4b2c07678580`) lines 383-398 [crates/gwiki/src/ai/chunk.rs:383-398]
  - Signature: `fn short_audio_bypasses_ffmpeg() {`
  - Purpose: This test verifies that short-duration audio transcription bypasses FFmpeg chunking by asserting zero chunker invocations while successfully producing the expected transcribed output. [crates/gwiki/src/ai/chunk.rs:383-398]
- `short_translate_segments_translates_without_chunking` (function) component `short_translate_segments_translates_without_chunking [function]` (`44c3426d-0abf-50d8-a705-a1ca91f8ac20`) lines 401-427 [crates/gwiki/src/ai/chunk.rs:401-427]
  - Signature: `fn short_translate_segments_translates_without_chunking() {`
  - Purpose: Tests that `TranslateSegments` mode successfully translates a short audio request directly to the target language without invoking the chunker. [crates/gwiki/src/ai/chunk.rs:401-427]
- `partial_chunk_outcome` (function) component `partial_chunk_outcome [function]` (`d96567d8-2f46-5bc6-a996-c817ab11619e`) lines 430-482 [crates/gwiki/src/ai/chunk.rs:430-482]
  - Signature: `fn partial_chunk_outcome() {`
  - Purpose: Tests that chunked audio transcription correctly segregates completed and missing ranges while preserving text segments from successful chunks when an intermediate chunk provider fails. [crates/gwiki/src/ai/chunk.rs:430-482]
- `FakeChunker` (class) component `FakeChunker [class]` (`dbd1c122-7fa0-5029-b1c3-67ecd4ae4c7d`) lines 484-487 [crates/gwiki/src/ai/chunk.rs:484-487]
  - Signature: `struct FakeChunker {`
  - Purpose: `FakeChunker` is a mock struct that stores a vector of `AudioChunk` objects and uses interior-mutable `Cell<usize>` to track call count. [crates/gwiki/src/ai/chunk.rs:484-487]
- `FakeChunker` (class) component `FakeChunker [class]` (`a04f14da-bf64-5e44-a903-d941c8425915`) lines 489-496 [crates/gwiki/src/ai/chunk.rs:489-496]
  - Signature: `impl FakeChunker {`
  - Purpose: FakeChunker's constructor initializes an instance with a provided vector of AudioChunks and a zero-initialized Cell for tracking method invocations. [crates/gwiki/src/ai/chunk.rs:489-496]
- `FakeChunker.new` (method) component `FakeChunker.new [method]` (`88cfb154-cd5c-5aca-aca3-b8f000d9c9cf`) lines 490-495 [crates/gwiki/src/ai/chunk.rs:490-495]
  - Signature: `fn new(chunks: Vec<AudioChunk>) -> Self {`
  - Purpose: This constructor initializes a new instance with a provided vector of `AudioChunk` objects and a zero-initialized `Cell`-wrapped call counter for interior mutability. [crates/gwiki/src/ai/chunk.rs:490-495]
- `FakeChunker` (class) component `FakeChunker [class]` (`31655919-16a4-531c-b175-4aef9a54e0ab`) lines 498-508 [crates/gwiki/src/ai/chunk.rs:498-508]
  - Signature: `impl AudioChunker for FakeChunker {`
  - Purpose: FakeChunker is a test stub implementing AudioChunker that returns precomputed audio chunks while ignoring input parameters and tracking invocation count via an internal counter. [crates/gwiki/src/ai/chunk.rs:498-508]
- `FakeChunker.split` (method) component `FakeChunker.split [method]` (`4394be31-3799-5a17-8ad6-5d9afade09bd`) lines 499-507 [crates/gwiki/src/ai/chunk.rs:499-507]
  - Signature: `fn split(`
  - Purpose: Increments an internal call counter and returns a cloned collection of pre-stored audio chunks, disregarding all input parameters. [crates/gwiki/src/ai/chunk.rs:499-507]
- `ScriptedClient` (class) component `ScriptedClient [class]` (`5dfb0e36-52c9-5de2-af31-6d19926a377d`) lines 510-512 [crates/gwiki/src/ai/chunk.rs:510-512]
  - Signature: `struct ScriptedClient {`
  - Purpose: `ScriptedClient` is a struct providing interior-mutable access to a vector of transcription operation results, each represented as `Result<TranscriptionOutput, WikiError>`. [crates/gwiki/src/ai/chunk.rs:510-512]
- `ScriptedClient` (class) component `ScriptedClient [class]` (`bafc2c98-7ea6-5049-9e1d-5e1588f3608f`) lines 514-520 [crates/gwiki/src/ai/chunk.rs:514-520]
  - Signature: `impl ScriptedClient {`
  - Purpose: `ScriptedClient::new` is a constructor that instantiates the struct by wrapping a vector of `Result<TranscriptionOutput, WikiError>` in a `RefCell` to enable interior mutable access to transcription outputs. [crates/gwiki/src/ai/chunk.rs:514-520]
- `ScriptedClient.new` (method) component `ScriptedClient.new [method]` (`cffc1da3-05c6-570e-aa13-ad5d90d06bc2`) lines 515-519 [crates/gwiki/src/ai/chunk.rs:515-519]
  - Signature: `fn new(outputs: Vec<Result<TranscriptionOutput, WikiError>>) -> Self {`
  - Purpose: Constructs a new instance by wrapping a vector of `Result<TranscriptionOutput, WikiError>` in a `RefCell` for interior mutability. [crates/gwiki/src/ai/chunk.rs:515-519]
- `ScriptedClient` (class) component `ScriptedClient [class]` (`c1051d2a-6773-518e-9b49-bf2b3d9849ae`) lines 522-529 [crates/gwiki/src/ai/chunk.rs:522-529]
  - Signature: `impl TranscriptionClient for ScriptedClient {`
  - Purpose: ScriptedClient implements TranscriptionClient as a mock that sequentially returns pre-recorded transcription outputs from an internal mutable queue, ignoring the input request parameter. [crates/gwiki/src/ai/chunk.rs:522-529]
- `ScriptedClient.transcribe` (method) component `ScriptedClient.transcribe [method]` (`22e1b517-1d5e-55ad-b4db-fcd23ad037e4`) lines 523-528 [crates/gwiki/src/ai/chunk.rs:523-528]
  - Signature: `fn transcribe(`
  - Purpose: Removes and returns the first `TranscriptionOutput` from a mutable-borrowed internal collection, disregarding the input request parameter. [crates/gwiki/src/ai/chunk.rs:523-528]
- `TranslatingClient` (class) component `TranslatingClient [class]` (`e3e475b5-98d4-5dec-8285-80aafac566a2`) lines 531-534 [crates/gwiki/src/ai/chunk.rs:531-534]
  - Signature: `struct TranslatingClient {`
  - Purpose: TranslatingClient is a struct that maintains interior-mutable counters for transcribe and translate operation calls using Cell fields. [crates/gwiki/src/ai/chunk.rs:531-534]
- `TranslatingClient` (class) component `TranslatingClient [class]` (`180fa25d-6fe1-5469-a8b9-943db0d9b0ac`) lines 536-557 [crates/gwiki/src/ai/chunk.rs:536-557]
  - Signature: `impl TranscriptionClient for TranslatingClient {`
  - Purpose: `TranslatingClient` is a test mock implementing `TranscriptionClient` that returns hardcoded Spanish transcription ("hola") and validates Spanish-to-French segment translation while tracking method invocation counts. [crates/gwiki/src/ai/chunk.rs:536-557]
- `TranslatingClient.transcribe` (method) component `TranslatingClient.transcribe [method]` (`6c2c0d30-f3d0-5423-a666-2e78fe908e45`) lines 537-543 [crates/gwiki/src/ai/chunk.rs:537-543]
  - Signature: `fn transcribe(`
  - Purpose: This method increments a call counter and returns a mocked `TranscriptionOutput` containing a Spanish ('es') transcript with the text "hola" at byte positions 0–1000. [crates/gwiki/src/ai/chunk.rs:537-543]
- `TranslatingClient.translate_segments` (method) component `TranslatingClient.translate_segments [method]` (`477dcb78-6fdd-5304-bcd5-5f9ffffca6ff`) lines 545-556 [crates/gwiki/src/ai/chunk.rs:545-556]
  - Signature: `fn translate_segments(`
  - Purpose: Increments a call counter and returns a hardcoded French translation after asserting that exactly one Spanish-to-French segment is provided. [crates/gwiki/src/ai/chunk.rs:545-556]
- `short_request` (function) component `short_request [function]` (`022ccdf7-ea80-5298-9202-800872e8d3fa`) lines 559-566 [crates/gwiki/src/ai/chunk.rs:559-566]
  - Signature: `fn short_request<'a>() -> TranscriptionRequest<'a> {`
  - Purpose: Constructs and returns a `TranscriptionRequest` with hardcoded test data for a short WAV audio file containing minimal sample bytes. [crates/gwiki/src/ai/chunk.rs:559-566]
- `long_request` (function) component `long_request [function]` (`e55f96c0-a1ed-50c6-b088-1f0f29722758`) lines 569-579 [crates/gwiki/src/ai/chunk.rs:569-579]
  - Signature: `fn long_request<'a>() -> TranscriptionRequest<'a> {`
  - Purpose: Returns a `TranscriptionRequest` test fixture containing an intentionally oversized, leaked byte buffer (exceeding `MAX_AUDIO_UPLOAD_BYTES` by one byte) to efficiently test boundary conditions without repeated allocations. [crates/gwiki/src/ai/chunk.rs:569-579]
- `chunk` (function) component `chunk [function]` (`a3a1c2ea-368b-5f90-994c-f470fe8e0241`) lines 581-589 [crates/gwiki/src/ai/chunk.rs:581-589]
  - Signature: `fn chunk(start_ms: u64, end_ms: u64) -> AudioChunk {`
  - Purpose: This function constructs and returns an `AudioChunk` struct initialized with provided time boundaries (start_ms, end_ms) and a filename/path derived from the start timestamp. [crates/gwiki/src/ai/chunk.rs:581-589]
- `output` (function) component `output [function]` (`0188eefd-a7cc-5cf7-a711-1462f6afdd6d`) lines 591-612 [crates/gwiki/src/ai/chunk.rs:591-612]
  - Signature: `fn output(source_lang: &str, segments: &[(u64, u64, &str)]) -> TranscriptionOutput {`
  - Purpose: Constructs a TranscriptionOutput by mapping timing-annotated text segments into TranscriptSegment objects and initializing transcription metadata with the provided source language and default parameters. [crates/gwiki/src/ai/chunk.rs:591-612]

