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
  - 48-59
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
  - 421-450
  - 453-469
  - 472-528
  - 531-590
  - 593-633
  - 636-681
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/transcribe.rs:14-18](crates/gwiki/src/transcribe.rs#L14-L18), [crates/gwiki/src/transcribe.rs:21-24](crates/gwiki/src/transcribe.rs#L21-L24), [crates/gwiki/src/transcribe.rs:27-39](crates/gwiki/src/transcribe.rs#L27-L39), [crates/gwiki/src/transcribe.rs:42-45](crates/gwiki/src/transcribe.rs#L42-L45), [crates/gwiki/src/transcribe.rs:48-59](crates/gwiki/src/transcribe.rs#L48-L59), [crates/gwiki/src/transcribe.rs:66-71](crates/gwiki/src/transcribe.rs#L66-L71), [crates/gwiki/src/transcribe.rs:73-101](crates/gwiki/src/transcribe.rs#L73-L101), [crates/gwiki/src/transcribe.rs:104-109](crates/gwiki/src/transcribe.rs#L104-L109), [crates/gwiki/src/transcribe.rs:111-121](crates/gwiki/src/transcribe.rs#L111-L121), [crates/gwiki/src/transcribe.rs:124-127](crates/gwiki/src/transcribe.rs#L124-L127), [crates/gwiki/src/transcribe.rs:130-133](crates/gwiki/src/transcribe.rs#L130-L133), [crates/gwiki/src/transcribe.rs:135-183](crates/gwiki/src/transcribe.rs#L135-L183), [crates/gwiki/src/transcribe.rs:185-209](crates/gwiki/src/transcribe.rs#L185-L209), [crates/gwiki/src/transcribe.rs:211-238](crates/gwiki/src/transcribe.rs#L211-L238), [crates/gwiki/src/transcribe.rs:240-259](crates/gwiki/src/transcribe.rs#L240-L259), [crates/gwiki/src/transcribe.rs:261-391](crates/gwiki/src/transcribe.rs#L261-L391), [crates/gwiki/src/transcribe.rs:393-399](crates/gwiki/src/transcribe.rs#L393-L399), [crates/gwiki/src/transcribe.rs:401-407](crates/gwiki/src/transcribe.rs#L401-L407), [crates/gwiki/src/transcribe.rs:416-418](crates/gwiki/src/transcribe.rs#L416-L418), [crates/gwiki/src/transcribe.rs:421-450](crates/gwiki/src/transcribe.rs#L421-L450), [crates/gwiki/src/transcribe.rs:453-469](crates/gwiki/src/transcribe.rs#L453-L469), [crates/gwiki/src/transcribe.rs:472-528](crates/gwiki/src/transcribe.rs#L472-L528), [crates/gwiki/src/transcribe.rs:531-590](crates/gwiki/src/transcribe.rs#L531-L590), [crates/gwiki/src/transcribe.rs:593-633](crates/gwiki/src/transcribe.rs#L593-L633), [crates/gwiki/src/transcribe.rs:636-681](crates/gwiki/src/transcribe.rs#L636-L681)

</details>

# crates/gwiki/src/transcribe.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the transcription pipeline for audio transcripts in `gwiki`: it models transcript segments, ranges, outputs, and degradation state; provides a `TranscriptionClient` abstraction plus a fake client for tests; and renders transcription results into markdown and writes them atomically to the derived transcript path. The helpers also format timestamps/ranges, detect empty or missing transcript output so those cases degrade instead of being treated as successful transcriptions, and the tests cover timestamped rendering, precomputed-output rendering, and degradation behavior.
[crates/gwiki/src/transcribe.rs:14-18]
[crates/gwiki/src/transcribe.rs:21-24]
[crates/gwiki/src/transcribe.rs:27-39]
[crates/gwiki/src/transcribe.rs:42-45]
[crates/gwiki/src/transcribe.rs:48-59]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `TranscriptSegment` | class | `pub struct TranscriptSegment {` | `TranscriptSegment [class]` | `7fbd01fa-4e31-5535-9145-e0aef5f10e56` | 14-18 [crates/gwiki/src/transcribe.rs:14-18] | Indexed class `TranscriptSegment` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:14-18] |
| `TranscriptionRange` | class | `pub struct TranscriptionRange {` | `TranscriptionRange [class]` | `a1f1230b-7287-58cb-b5f2-2d3d552e8398` | 21-24 [crates/gwiki/src/transcribe.rs:21-24] | Indexed class `TranscriptionRange` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:21-24] |
| `TranscriptionOutput` | class | `pub struct TranscriptionOutput {` | `TranscriptionOutput [class]` | `afc1dbc8-231d-5afa-84c7-ecfd0b0b7efe` | 27-39 [crates/gwiki/src/transcribe.rs:27-39] | Indexed class `TranscriptionOutput` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:27-39] |
| `TranscriptionDegradation` | class | `pub struct TranscriptionDegradation {` | `TranscriptionDegradation [class]` | `93d6d430-4992-5936-893d-8184bcf4638b` | 42-45 [crates/gwiki/src/transcribe.rs:42-45] | Indexed class `TranscriptionDegradation` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:42-45] |
| `TranscriptionDegradation::for_routing` | method | `pub(crate) fn for_routing(routing: AiRouting, fallback: &str) -> Self {` | `TranscriptionDegradation::for_routing [method]` | `aa5b7fd0-3db0-5b26-9f02-c668a004fb94` | 48-59 [crates/gwiki/src/transcribe.rs:48-59] | Indexed method `TranscriptionDegradation::for_routing` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:48-59] |
| `transcription_output_is_empty` | function | `pub(crate) fn transcription_output_is_empty(output: &TranscriptionOutput) -> bool {` | `transcription_output_is_empty [function]` | `60951741-0f4e-53b4-b5b5-aad389e9acad` | 66-71 [crates/gwiki/src/transcribe.rs:66-71] | Indexed function `transcription_output_is_empty` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:66-71] |
| `TranscriptionClient` | type | `pub trait TranscriptionClient {` | `TranscriptionClient [type]` | `2116932d-286f-5b96-9f12-4afd0164c50a` | 73-101 [crates/gwiki/src/transcribe.rs:73-101] | Indexed type `TranscriptionClient` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:73-101] |
| `TranscriptionClient.translate_to_english` | method | `fn translate_to_english(` | `TranscriptionClient.translate_to_english [method]` | `cb0b1e38-b8cf-579e-b5ea-59665a025929` | 80-88 [crates/gwiki/src/transcribe.rs:80-88] | Indexed method `TranscriptionClient.translate_to_english` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:80-88] |
| `TranscriptionClient.translate_segments` | method | `fn translate_segments(` | `TranscriptionClient.translate_segments [method]` | `ea5d0e39-323a-52f1-96bb-dbac824c7636` | 91-100 [crates/gwiki/src/transcribe.rs:91-100] | Indexed method `TranscriptionClient.translate_segments` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:91-100] |
| `TranscriptionRequest` | class | `pub struct TranscriptionRequest<'a> {` | `TranscriptionRequest [class]` | `52df6d85-3bbf-5725-9758-9a79872066ea` | 104-109 [crates/gwiki/src/transcribe.rs:104-109] | Indexed class `TranscriptionRequest` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:104-109] |
| `TranscriptionEndpoint` | type | `pub enum TranscriptionEndpoint<'a> {` | `TranscriptionEndpoint [type]` | `90c28a3a-e3b7-5633-954f-ebb57a3ad603` | 111-121 [crates/gwiki/src/transcribe.rs:111-121] | Indexed type `TranscriptionEndpoint` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:111-121] |
| `TranscriptionMarkdownResult` | class | `pub struct TranscriptionMarkdownResult {` | `TranscriptionMarkdownResult [class]` | `f31417d6-f7c5-5d32-bd44-cf854eaf0862` | 124-127 [crates/gwiki/src/transcribe.rs:124-127] | Indexed class `TranscriptionMarkdownResult` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:124-127] |
| `TranscriptionMarkdownInput` | type | `pub enum TranscriptionMarkdownInput {` | `TranscriptionMarkdownInput [type]` | `9c606d5f-3310-5a24-8c69-7b738abae17d` | 130-133 [crates/gwiki/src/transcribe.rs:130-133] | Indexed type `TranscriptionMarkdownInput` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:130-133] |
| `write_audio_transcript_markdown` | function | `pub fn write_audio_transcript_markdown(` | `write_audio_transcript_markdown [function]` | `b420b5fa-e7de-5430-95d2-220b01ca93e6` | 135-183 [crates/gwiki/src/transcribe.rs:135-183] | Indexed function `write_audio_transcript_markdown` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:135-183] |
| `write_transcript_markdown_atomically` | function | `fn write_transcript_markdown_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {` | `write_transcript_markdown_atomically [function]` | `3ab8ba4f-6c9d-5e02-89d7-3159a663959e` | 185-209 [crates/gwiki/src/transcribe.rs:185-209] | Indexed function `write_transcript_markdown_atomically` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:185-209] |
| `create_transcript_temp_file` | function | `fn create_transcript_temp_file(path: &Path) -> Result<NamedTempFile, WikiError> {` | `create_transcript_temp_file [function]` | `bb4495d4-910b-5049-a5c4-c93c24625529` | 211-238 [crates/gwiki/src/transcribe.rs:211-238] | Indexed function `create_transcript_temp_file` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:211-238] |
| `sync_parent_dir` | function | `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {` | `sync_parent_dir [function]` | `855fa9aa-7f03-51fa-9f30-476b2b99614b` | 240-259 [crates/gwiki/src/transcribe.rs:240-259] | Indexed function `sync_parent_dir` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:240-259] |
| `render_audio_transcript_markdown` | function | `fn render_audio_transcript_markdown(` | `render_audio_transcript_markdown [function]` | `c4ec0288-32f8-534b-8c44-aca336f7b08f` | 261-391 [crates/gwiki/src/transcribe.rs:261-391] | Indexed function `render_audio_transcript_markdown` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:261-391] |
| `format_timestamp_ms` | function | `fn format_timestamp_ms(timestamp_ms: u64) -> String {` | `format_timestamp_ms [function]` | `0da904dc-43a0-54fd-a459-31fff425b6e3` | 393-399 [crates/gwiki/src/transcribe.rs:393-399] | Indexed function `format_timestamp_ms` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:393-399] |
| `format_ranges_ms` | function | `fn format_ranges_ms(ranges: &[TranscriptionRange]) -> String {` | `format_ranges_ms [function]` | `6f694a11-1a8d-5055-94a8-7a37d630ecf6` | 401-407 [crates/gwiki/src/transcribe.rs:401-407] | Indexed function `format_ranges_ms` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:401-407] |
| `FakeTranscriptionClient` | class | `struct FakeTranscriptionClient {` | `FakeTranscriptionClient [class]` | `550a7324-801a-565e-9b3d-daeaa8d1c970` | 416-418 [crates/gwiki/src/transcribe.rs:416-418] | Indexed class `FakeTranscriptionClient` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:416-418] |
| `FakeTranscriptionClient::transcribe` | method | `fn transcribe(` | `FakeTranscriptionClient::transcribe [method]` | `c5d7a41a-daf6-5688-b2cc-d8249f5963f3` | 421-450 [crates/gwiki/src/transcribe.rs:421-450] | Indexed method `FakeTranscriptionClient::transcribe` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:421-450] |
| `record_for` | function | `fn record_for(temp: &Path) -> SourceRecord {` | `record_for [function]` | `d4b67e40-ebdf-5fb3-94be-7ae5093bd950` | 453-469 [crates/gwiki/src/transcribe.rs:453-469] | Indexed function `record_for` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:453-469] |
| `writes_timestamped_transcript` | function | `fn writes_timestamped_transcript() {` | `writes_timestamped_transcript [function]` | `712a0319-2409-5298-a6e1-c76265582bb6` | 472-528 [crates/gwiki/src/transcribe.rs:472-528] | Indexed function `writes_timestamped_transcript` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:472-528] |
| `renders_precomputed_output_without_transcribing` | function | `fn renders_precomputed_output_without_transcribing() {` | `renders_precomputed_output_without_transcribing [function]` | `32bec997-b130-5825-ba87-990d76cf12f4` | 531-590 [crates/gwiki/src/transcribe.rs:531-590] | Indexed function `renders_precomputed_output_without_transcribing` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:531-590] |
| `missing_transcription_degrades` | function | `fn missing_transcription_degrades() {` | `missing_transcription_degrades [function]` | `4286e9ff-18e8-5930-a704-79136f7b9cfa` | 593-633 [crates/gwiki/src/transcribe.rs:593-633] | Indexed function `missing_transcription_degrades` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:593-633] |
| `empty_transcript_degrades` | function | `fn empty_transcript_degrades() {` | `empty_transcript_degrades [function]` | `a34a0209-2474-5f6c-bdc6-3426e4d35425` | 636-681 [crates/gwiki/src/transcribe.rs:636-681] | Indexed function `empty_transcript_degrades` in `crates/gwiki/src/transcribe.rs`. [crates/gwiki/src/transcribe.rs:636-681] |
