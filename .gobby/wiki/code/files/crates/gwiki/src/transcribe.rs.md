---
title: crates/gwiki/src/transcribe.rs
type: code_file
provenance:
- file: crates/gwiki/src/transcribe.rs
  ranges:
  - 14-18
  - 21-24
  - 27-39
  - 42-45
  - 47-60
  - 66-71
  - 73-101
  - 104-109
  - 111-121
  - 124-127
  - 130-133
  - 135-183
  - 185-209
  - 211-238
  - 240-259
  - 261-391
  - 393-399
  - 401-407
  - 416-418
  - 420-451
  - 453-469
  - 472-528
  - 531-590
  - 593-633
  - 636-681
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/transcribe.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the transcription pipeline for audio sources: data types for transcript segments, transcription ranges, outputs, and degradation metadata; a `TranscriptionClient` trait with a disabled default translation path; and the markdown rendering/writing flow that turns either a successful transcription or a fallback degradation into a derived source note. The file also provides helpers for empty-output detection, timestamp/range formatting, atomic file creation and directory syncing, plus a fake client and test cases that verify successful transcription, precomputed output, and degraded cases when transcription is missing or empty.
[crates/gwiki/src/transcribe.rs:14-18]
[crates/gwiki/src/transcribe.rs:21-24]
[crates/gwiki/src/transcribe.rs:27-39]
[crates/gwiki/src/transcribe.rs:42-45]
[crates/gwiki/src/transcribe.rs:47-60]

## API Symbols

- `TranscriptSegment` (class) component `TranscriptSegment [class]` (`7fbd01fa-4e31-5535-9145-e0aef5f10e56`) lines 14-18 [crates/gwiki/src/transcribe.rs:14-18]
  - Signature: `pub struct TranscriptSegment {`
  - Purpose: `TranscriptSegment` is a Rust data structure that represents a single transcript fragment with millisecond start and end timestamps and the associated text content. [crates/gwiki/src/transcribe.rs:14-18]
- `TranscriptionRange` (class) component `TranscriptionRange [class]` (`a1f1230b-7287-58cb-b5f2-2d3d552e8398`) lines 21-24 [crates/gwiki/src/transcribe.rs:21-24]
  - Signature: `pub struct TranscriptionRange {`
  - Purpose: `TranscriptionRange` is a value struct that represents a transcription time interval using millisecond offsets for its start (`start_ms`) and end (`end_ms`). [crates/gwiki/src/transcribe.rs:21-24]
- `TranscriptionOutput` (class) component `TranscriptionOutput [class]` (`afc1dbc8-231d-5afa-84c7-ecfd0b0b7efe`) lines 27-39 [crates/gwiki/src/transcribe.rs:27-39]
  - Signature: `pub struct TranscriptionOutput {`
  - Purpose: `TranscriptionOutput` is a Rust data container for a transcription result, holding the extracted `TranscriptSegment`s plus language/model metadata and status flags/range lists that describe translation state, partial completion, and which transcript spans are completed or missing. [crates/gwiki/src/transcribe.rs:27-39]
- `TranscriptionDegradation` (class) component `TranscriptionDegradation [class]` (`93d6d430-4992-5936-893d-8184bcf4638b`) lines 42-45 [crates/gwiki/src/transcribe.rs:42-45]
  - Signature: `pub struct TranscriptionDegradation {`
  - Purpose: `TranscriptionDegradation` is a Rust data structure that records why transcription quality degraded via a `ModalityDegradationReason` and stores the corresponding `fallback` text to use instead. [crates/gwiki/src/transcribe.rs:42-45]
- `TranscriptionDegradation` (class) component `TranscriptionDegradation [class]` (`3f413281-9587-55d5-b0b4-a4d14c6cec18`) lines 47-60 [crates/gwiki/src/transcribe.rs:47-60]
  - Signature: `impl TranscriptionDegradation {`
  - Purpose: `TranscriptionDegradation` is a helper that builds a transcription degradation record by mapping `AiRouting::Off` to `ModalityDegradationReason::Disabled` and all other routing modes to `MissingEndpoint`, while storing the supplied fallback string. [crates/gwiki/src/transcribe.rs:47-60]
- `TranscriptionDegradation.for_routing` (method) component `TranscriptionDegradation.for_routing [method]` (`aa5b7fd0-3db0-5b26-9f02-c668a004fb94`) lines 48-59 [crates/gwiki/src/transcribe.rs:48-59]
  - Signature: `pub(crate) fn for_routing(routing: AiRouting, fallback: &str) -> Self {`
  - Purpose: Constructs a `Self` value by translating `AiRouting::Off` to `ModalityDegradationReason::Disabled` and all other routing modes to `ModalityDegradationReason::MissingEndpoint`, while cloning `fallback` into the `fallback` field. [crates/gwiki/src/transcribe.rs:48-59]
- `transcription_output_is_empty` (function) component `transcription_output_is_empty [function]` (`60951741-0f4e-53b4-b5b5-aad389e9acad`) lines 66-71 [crates/gwiki/src/transcribe.rs:66-71]
  - Signature: `pub(crate) fn transcription_output_is_empty(output: &TranscriptionOutput) -> bool {`
  - Purpose: Returns 'true' only when every segment in 'output.segments' has 'text' that is empty or whitespace-only after trimming, otherwise returns 'false'. [crates/gwiki/src/transcribe.rs:66-71]
- `TranscriptionClient` (type) component `TranscriptionClient [type]` (`2116932d-286f-5b96-9f12-4afd0164c50a`) lines 73-101 [crates/gwiki/src/transcribe.rs:73-101]
  - Signature: `pub trait TranscriptionClient {`
  - Purpose: Indexed type `TranscriptionClient` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:73-101]
- `TranscriptionClient.translate_to_english` (method) component `TranscriptionClient.translate_to_english [method]` (`cb0b1e38-b8cf-579e-b5ea-59665a025929`) lines 80-88 [crates/gwiki/src/transcribe.rs:80-88]
  - Signature: `fn translate_to_english(`
  - Purpose: 'translate_to_english' ignores its request and language hint and always returns 'Err(WikiError::Config)' with the message '"audio translation is not configured"'. [crates/gwiki/src/transcribe.rs:80-88]
- `TranscriptionClient.translate_segments` (method) component `TranscriptionClient.translate_segments [method]` (`ea5d0e39-323a-52f1-96bb-dbac824c7636`) lines 91-100 [crates/gwiki/src/transcribe.rs:91-100]
  - Signature: `fn translate_segments(`
  - Purpose: 'translate_segments' unconditionally returns 'Err(WikiError::Config { detail: "text translation is not configured" })', indicating the translation path is disabled and no segment translation is performed. [crates/gwiki/src/transcribe.rs:91-100]
- `TranscriptionRequest` (class) component `TranscriptionRequest [class]` (`52df6d85-3bbf-5725-9758-9a79872066ea`) lines 104-109 [crates/gwiki/src/transcribe.rs:104-109]
  - Signature: `pub struct TranscriptionRequest<'a> {`
  - Purpose: 'TranscriptionRequest<'a>' is a borrowed request payload that carries an input file’s name, optional MIME type, filesystem path, and raw byte contents for transcription processing. [crates/gwiki/src/transcribe.rs:104-109]
- `TranscriptionEndpoint` (type) component `TranscriptionEndpoint [type]` (`90c28a3a-e3b7-5633-954f-ebb57a3ad603`) lines 111-121 [crates/gwiki/src/transcribe.rs:111-121]
  - Signature: `pub enum TranscriptionEndpoint<'a> {`
  - Purpose: Indexed type `TranscriptionEndpoint` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:111-121]
- `TranscriptionMarkdownResult` (class) component `TranscriptionMarkdownResult [class]` (`f31417d6-f7c5-5d32-bd44-cf854eaf0862`) lines 124-127 [crates/gwiki/src/transcribe.rs:124-127]
  - Signature: `pub struct TranscriptionMarkdownResult {`
  - Purpose: 'TranscriptionMarkdownResult' is a result struct that stores the generated markdown file path and an optional 'TranscriptionDegradation' describing any quality loss during transcription. [crates/gwiki/src/transcribe.rs:124-127]
- `TranscriptionMarkdownInput` (type) component `TranscriptionMarkdownInput [type]` (`9c606d5f-3310-5a24-8c69-7b738abae17d`) lines 130-133 [crates/gwiki/src/transcribe.rs:130-133]
  - Signature: `pub enum TranscriptionMarkdownInput {`
  - Purpose: Indexed type `TranscriptionMarkdownInput` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:130-133]
- `write_audio_transcript_markdown` (function) component `write_audio_transcript_markdown [function]` (`b420b5fa-e7de-5430-95d2-220b01ca93e6`) lines 135-183 [crates/gwiki/src/transcribe.rs:135-183]
  - Signature: `pub fn write_audio_transcript_markdown(`
  - Purpose: Creates the derived markdown path for an audio source record under 'vault_root', renders transcript markdown from either a successful transcription or a degradation fallback, writes it atomically after ensuring parent directories exist, and returns the relative path plus any degradation metadata. [crates/gwiki/src/transcribe.rs:135-183]
- `write_transcript_markdown_atomically` (function) component `write_transcript_markdown_atomically [function]` (`3ab8ba4f-6c9d-5e02-89d7-3159a663959e`) lines 185-209 [crates/gwiki/src/transcribe.rs:185-209]
  - Signature: `fn write_transcript_markdown_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Creates a temporary file, writes the markdown bytes, fsyncs it, atomically persists it to the target path, and then syncs the parent directory, returning 'WikiError::Io' on any I/O failure. [crates/gwiki/src/transcribe.rs:185-209]
- `create_transcript_temp_file` (function) component `create_transcript_temp_file [function]` (`bb4495d4-910b-5049-a5c4-c93c24625529`) lines 211-238 [crates/gwiki/src/transcribe.rs:211-238]
  - Signature: `fn create_transcript_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Creates a temporary file in the target path’s non-empty parent directory, naming it with a '.{filename}.' prefix and '.tmp' suffix, and returns a 'WikiError::Io' if the path has no parent or tempfile creation fails. [crates/gwiki/src/transcribe.rs:211-238]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`855fa9aa-7f03-51fa-9f30-476b2b99614b`) lines 240-259 [crates/gwiki/src/transcribe.rs:240-259]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: On Unix, it opens 'path'’s parent directory and calls 'sync_all' to flush directory metadata to disk, mapping any I/O failure into 'WikiError::Io' with the parent path, while on non-Unix platforms it returns 'Ok(())' without doing anything. [crates/gwiki/src/transcribe.rs:240-259]
- `render_audio_transcript_markdown` (function) component `render_audio_transcript_markdown [function]` (`c4ec0288-32f8-534b-8c44-aca336f7b08f`) lines 261-391 [crates/gwiki/src/transcribe.rs:261-391]
  - Signature: `fn render_audio_transcript_markdown(`
  - Purpose: 'render_audio_transcript_markdown' constructs a Markdown document for an audio transcription record by assembling frontmatter-style metadata from the source record, scope, request, and optional transcription/degradation details, including paths, hashes, byte size, MIME type, and transcription status. [crates/gwiki/src/transcribe.rs:261-391]
- `format_timestamp_ms` (function) component `format_timestamp_ms [function]` (`0da904dc-43a0-54fd-a459-31fff425b6e3`) lines 393-399 [crates/gwiki/src/transcribe.rs:393-399]
  - Signature: `fn format_timestamp_ms(timestamp_ms: u64) -> String {`
  - Purpose: Converts a timestamp in milliseconds into an 'HH:MM:SS' string by truncating to whole seconds and zero-padding hours, minutes, and seconds to two digits each. [crates/gwiki/src/transcribe.rs:393-399]
- `format_ranges_ms` (function) component `format_ranges_ms [function]` (`6f694a11-1a8d-5055-94a8-7a37d630ecf6`) lines 401-407 [crates/gwiki/src/transcribe.rs:401-407]
  - Signature: `fn format_ranges_ms(ranges: &[TranscriptionRange]) -> String {`
  - Purpose: Formats a slice of 'TranscriptionRange' values into a comma-separated string of 'start_ms-end_ms' pairs. [crates/gwiki/src/transcribe.rs:401-407]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`550a7324-801a-565e-9b3d-daeaa8d1c970`) lines 416-418 [crates/gwiki/src/transcribe.rs:416-418]
  - Signature: `struct FakeTranscriptionClient {`
  - Purpose: 'FakeTranscriptionClient' is a test double struct that tracks the number of transcription-related invocations in a 'Cell<usize>' via its 'calls' field. [crates/gwiki/src/transcribe.rs:416-418]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`20176f7b-152b-519a-a863-316e8304c491`) lines 420-451 [crates/gwiki/src/transcribe.rs:420-451]
  - Signature: `impl TranscriptionClient for FakeTranscriptionClient {`
  - Purpose: 'FakeTranscriptionClient' is a test double implementing 'TranscriptionClient' whose 'transcribe' method increments an internal call counter and returns a fixed English 'TranscriptionOutput' with two hard-coded 'TranscriptSegment's and fake STT metadata. [crates/gwiki/src/transcribe.rs:420-451]
- `FakeTranscriptionClient.transcribe` (method) component `FakeTranscriptionClient.transcribe [method]` (`c5d7a41a-daf6-5688-b2cc-d8249f5963f3`) lines 421-450 [crates/gwiki/src/transcribe.rs:421-450]
  - Signature: `fn transcribe(`
  - Purpose: Increments the internal call counter and returns a fixed successful 'TranscriptionOutput' containing two English transcript segments, 'fake-stt' metadata, and default non-translated, non-partial range fields. [crates/gwiki/src/transcribe.rs:421-450]
- `record_for` (function) component `record_for [function]` (`d4b67e40-ebdf-5fb3-94be-7ae5093bd950`) lines 453-469 [crates/gwiki/src/transcribe.rs:453-469]
  - Signature: `fn record_for(temp: &Path) -> SourceRecord {`
  - Purpose: Registers a pending manually ingested audio 'SourceDraft' for '/tmp/interview.wav' in the 'SourceManifest' under 'temp' and returns the resulting 'SourceRecord', panicking if registration fails. [crates/gwiki/src/transcribe.rs:453-469]
- `writes_timestamped_transcript` (function) component `writes_timestamped_transcript [function]` (`712a0319-2409-5298-a6e1-c76265582bb6`) lines 472-528 [crates/gwiki/src/transcribe.rs:472-528]
  - Signature: `fn writes_timestamped_transcript() {`
  - Purpose: Verifies that 'write_audio_transcript_markdown' writes a transcript Markdown file at the expected 'knowledge/sources/{record.id}.md' path with audio/topic frontmatter, transcribed status, timestamped transcript lines, and original audio provenance, while invoking the transcription client exactly once. [crates/gwiki/src/transcribe.rs:472-528]
- `renders_precomputed_output_without_transcribing` (function) component `renders_precomputed_output_without_transcribing [function]` (`32bec997-b130-5825-ba87-990d76cf12f4`) lines 531-590 [crates/gwiki/src/transcribe.rs:531-590]
  - Signature: `fn renders_precomputed_output_without_transcribing() {`
  - Purpose: Verifies that 'write_audio_transcript_markdown' writes a supplied 'TranscriptionMarkdownInput::Transcribed' result directly to markdown without calling the transcription client, and returns no degradation metadata. [crates/gwiki/src/transcribe.rs:531-590]
- `missing_transcription_degrades` (function) component `missing_transcription_degrades [function]` (`4286e9ff-18e8-5930-a704-79136f7b9cfa`) lines 593-633 [crates/gwiki/src/transcribe.rs:593-633]
  - Signature: `fn missing_transcription_degrades() {`
  - Purpose: Verifies that 'write_audio_transcript_markdown' handles a missing transcription endpoint by returning a 'MissingEndpoint' degradation, preserving the original audio asset, and writing markdown marked 'transcription_status: unavailable' with the appropriate degradation metadata and fallback text. [crates/gwiki/src/transcribe.rs:593-633]
- `empty_transcript_degrades` (function) component `empty_transcript_degrades [function]` (`a34a0209-2474-5f6c-bdc6-3426e4d35425`) lines 636-681 [crates/gwiki/src/transcribe.rs:636-681]
  - Signature: `fn empty_transcript_degrades() {`
  - Purpose: Verifies that writing a transcribed transcript with zero speech segments degrades the modality to 'TranscriptionError'/'unavailable' and emits markdown metadata reflecting that degraded status rather than 'transcribed'. [crates/gwiki/src/transcribe.rs:636-681]

