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
  - 62-90
  - 93-98
  - 100-110
  - 113-116
  - 119-122
  - 124-159
  - 161-185
  - 187-214
  - 216-235
  - 237-367
  - 369-375
  - 377-383
  - 392-394
  - 396-427
  - 429-445
  - 448-504
  - 507-566
  - 569-609
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/transcribe.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/transcribe.rs` exposes 27 indexed API symbols.
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
- `TranscriptionClient` (type) component `TranscriptionClient [type]` (`daa24d7d-7449-5261-a1e7-2674e7911b49`) lines 62-90 [crates/gwiki/src/transcribe.rs:62-90]
  - Signature: `pub trait TranscriptionClient {`
  - Purpose: Indexed type `TranscriptionClient` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:62-90]
- `TranscriptionClient.translate_to_english` (method) component `TranscriptionClient.translate_to_english [method]` (`57dcb168-2c9d-5e37-ae02-4b1395f78cb0`) lines 69-77 [crates/gwiki/src/transcribe.rs:69-77]
  - Signature: `fn translate_to_english(`
  - Purpose: This method unconditionally returns `Err(WikiError::Config)` with the message `"audio translation is not configured"`, indicating that English translation is disabled regardless of the request or language hint. [crates/gwiki/src/transcribe.rs:69-77]
- `TranscriptionClient.translate_segments` (method) component `TranscriptionClient.translate_segments [method]` (`bb5687cf-7bf7-52b2-812e-198f1f58add4`) lines 80-89 [crates/gwiki/src/transcribe.rs:80-89]
  - Signature: `fn translate_segments(`
  - Purpose: `translate_segments` is a stub implementation that ignores its inputs and always returns `Err(WikiError::Config { detail: "text translation is not configured" })`, indicating translation support is unavailable. [crates/gwiki/src/transcribe.rs:80-89]
- `TranscriptionRequest` (class) component `TranscriptionRequest [class]` (`0b59e683-1f25-52e2-a9c0-33c17957d051`) lines 93-98 [crates/gwiki/src/transcribe.rs:93-98]
  - Signature: `pub struct TranscriptionRequest<'a> {`
  - Purpose: `TranscriptionRequest<'a>` is a borrowed request payload for a transcription job that carries the input file’s name, optional MIME type, asset path, and raw byte contents. [crates/gwiki/src/transcribe.rs:93-98]
- `TranscriptionEndpoint` (type) component `TranscriptionEndpoint [type]` (`31afa17d-562c-51cf-94c9-06bbc1321c2d`) lines 100-110 [crates/gwiki/src/transcribe.rs:100-110]
  - Signature: `pub enum TranscriptionEndpoint<'a> {`
  - Purpose: Indexed type `TranscriptionEndpoint` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:100-110]
- `TranscriptionMarkdownResult` (class) component `TranscriptionMarkdownResult [class]` (`75c8e303-7615-5856-ad6b-3fc28071c9a5`) lines 113-116 [crates/gwiki/src/transcribe.rs:113-116]
  - Signature: `pub struct TranscriptionMarkdownResult {`
  - Purpose: `TranscriptionMarkdownResult` is a result container for a generated transcription Markdown file, storing its filesystem `PathBuf` and an optional `TranscriptionDegradation` describing quality loss or fallback behavior. [crates/gwiki/src/transcribe.rs:113-116]
- `TranscriptionMarkdownInput` (type) component `TranscriptionMarkdownInput [type]` (`baacf877-c7b4-5a91-837b-fcb33a2cfc33`) lines 119-122 [crates/gwiki/src/transcribe.rs:119-122]
  - Signature: `pub enum TranscriptionMarkdownInput {`
  - Purpose: Indexed type `TranscriptionMarkdownInput` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:119-122]
- `write_audio_transcript_markdown` (function) component `write_audio_transcript_markdown [function]` (`690c6720-af4e-58bf-9779-7252bb4bfc64`) lines 124-159 [crates/gwiki/src/transcribe.rs:124-159]
  - Signature: `pub fn write_audio_transcript_markdown(`
  - Purpose: Writes the transcript markdown for a source record to its derived path under `vault_root` atomically after creating parent directories, rendering the content from `scope`, `record`, `request`, and either a transcription or degradation, and returns the relative path plus any degradation metadata. [crates/gwiki/src/transcribe.rs:124-159]
- `write_transcript_markdown_atomically` (function) component `write_transcript_markdown_atomically [function]` (`6bd0d58e-9026-5a1b-863e-c7e2b5c173a7`) lines 161-185 [crates/gwiki/src/transcribe.rs:161-185]
  - Signature: `fn write_transcript_markdown_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Creates a temporary transcript markdown file, writes and `fsync`s the bytes to it, atomically renames it over `path`, and then syncs the parent directory, returning a `WikiError::Io` on any step failure. [crates/gwiki/src/transcribe.rs:161-185]
- `create_transcript_temp_file` (function) component `create_transcript_temp_file [function]` (`31308ae9-9b11-5c67-ae9e-4815495770e9`) lines 187-214 [crates/gwiki/src/transcribe.rs:187-214]
  - Signature: `fn create_transcript_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Creates a `NamedTempFile` in the target path’s non-empty parent directory, using a hidden `.{file_name}.` prefix and `.tmp` suffix for the transcript temp file, and returns `WikiError::Io` if the path has no parent or temp-file creation fails. [crates/gwiki/src/transcribe.rs:187-214]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`dcc81203-f8ab-526f-a008-03fd4fa30b78`) lines 216-235 [crates/gwiki/src/transcribe.rs:216-235]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: On Unix, it opens the parent directory of `path` and calls `sync_all()` to flush directory metadata to disk, returning a `WikiError::Io` with the parent path on failure, while on non-Unix platforms it is a no-op that always returns `Ok(())`. [crates/gwiki/src/transcribe.rs:216-235]
- `render_audio_transcript_markdown` (function) component `render_audio_transcript_markdown [function]` (`94ab4bbe-0b37-52e0-8f16-db5d390abdf0`) lines 237-367 [crates/gwiki/src/transcribe.rs:237-367]
  - Signature: `fn render_audio_transcript_markdown(`
  - Purpose: Builds and returns a markdown document for an audio transcript by assembling frontmatter metadata from the scope, source record, transcription request, and any available transcription or degradation details. [crates/gwiki/src/transcribe.rs:237-367]
- `format_timestamp_ms` (function) component `format_timestamp_ms [function]` (`b09bd4e4-deeb-5427-98dc-85b682efdde1`) lines 369-375 [crates/gwiki/src/transcribe.rs:369-375]
  - Signature: `fn format_timestamp_ms(timestamp_ms: u64) -> String {`
  - Purpose: Converts a millisecond timestamp to a zero-padded `HH:MM:SS` string by truncating to whole seconds and deriving hours, minutes, and seconds with integer division and modulo. [crates/gwiki/src/transcribe.rs:369-375]
- `format_ranges_ms` (function) component `format_ranges_ms [function]` (`d3988338-05ed-5db4-9faf-510499a598ea`) lines 377-383 [crates/gwiki/src/transcribe.rs:377-383]
  - Signature: `fn format_ranges_ms(ranges: &[TranscriptionRange]) -> String {`
  - Purpose: Formats a slice of `TranscriptionRange` values into a comma-separated string of `start_ms-end_ms` pairs. [crates/gwiki/src/transcribe.rs:377-383]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`2711905a-53f0-5af0-9eaa-5afd3a6c8e2b`) lines 392-394 [crates/gwiki/src/transcribe.rs:392-394]
  - Signature: `struct FakeTranscriptionClient {`
  - Purpose: A test double that uses interior mutability to count how many times the transcription client has been called via a `Cell<usize>` counter. [crates/gwiki/src/transcribe.rs:392-394]
- `FakeTranscriptionClient` (class) component `FakeTranscriptionClient [class]` (`d96a1999-ece3-5d2d-91f1-f3014bc3cbf1`) lines 396-427 [crates/gwiki/src/transcribe.rs:396-427]
  - Signature: `impl TranscriptionClient for FakeTranscriptionClient {`
  - Purpose: `FakeTranscriptionClient` is a test double for `TranscriptionClient` that increments an internal call counter and returns a fixed, English `TranscriptionOutput` with two hard-coded transcript segments and no translation or range metadata. [crates/gwiki/src/transcribe.rs:396-427]
- `FakeTranscriptionClient.transcribe` (method) component `FakeTranscriptionClient.transcribe [method]` (`27e74d06-d0cf-5219-b4ac-751d3979f22b`) lines 397-426 [crates/gwiki/src/transcribe.rs:397-426]
  - Signature: `fn transcribe(`
  - Purpose: It increments `self.calls` and returns a deterministic `TranscriptionOutput` containing two hard-coded transcript segments plus English/fake-STT metadata, ignoring the input request. [crates/gwiki/src/transcribe.rs:397-426]
- `record_for` (function) component `record_for [function]` (`a4cb50da-d54c-5078-aa14-e1ffc9b21903`) lines 429-445 [crates/gwiki/src/transcribe.rs:429-445]
  - Signature: `fn record_for(temp: &Path) -> SourceRecord {`
  - Purpose: `record_for` registers a fixed, manually ingested pending audio `SourceDraft` with `SourceManifest` at the given `temp` path and returns the resulting `SourceRecord`, panicking if registration fails. [crates/gwiki/src/transcribe.rs:429-445]
- `writes_timestamped_transcript` (function) component `writes_timestamped_transcript [function]` (`e2439d90-b13e-511a-8b96-2ae9182baed3`) lines 448-504 [crates/gwiki/src/transcribe.rs:448-504]
  - Signature: `fn writes_timestamped_transcript() {`
  - Purpose: It verifies that `write_audio_transcript_markdown` calls the transcription client exactly once and writes a `knowledge/sources/{record.id}.md` transcript containing audio/topic metadata, `transcription_status: transcribed`, the original asset path, and timestamped transcript lines with no degradation. [crates/gwiki/src/transcribe.rs:448-504]
- `renders_precomputed_output_without_transcribing` (function) component `renders_precomputed_output_without_transcribing [function]` (`fee4e573-da5f-5e26-94e8-7849b0602b7b`) lines 507-566 [crates/gwiki/src/transcribe.rs:507-566]
  - Signature: `fn renders_precomputed_output_without_transcribing() {`
  - Purpose: This test verifies that `write_audio_transcript_markdown` serializes a precomputed `Transcribed` `TranscriptionOutput` to markdown without calling the transcription client and without surfacing any degradation metadata. [crates/gwiki/src/transcribe.rs:507-566]
- `missing_transcription_degrades` (function) component `missing_transcription_degrades [function]` (`fad472b8-abe4-52d8-bc56-35627bcec966`) lines 569-609 [crates/gwiki/src/transcribe.rs:569-609]
  - Signature: `fn missing_transcription_degrades() {`
  - Purpose: Verifies that `write_audio_transcript_markdown` emits degraded transcript markdown for a missing transcription endpoint while preserving the raw audio asset, carrying through the degradation reason, and marking the output as `transcription_status: unavailable` with `transcription_degradation: missing_endpoint`. [crates/gwiki/src/transcribe.rs:569-609]

