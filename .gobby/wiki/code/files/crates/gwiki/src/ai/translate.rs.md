---
title: crates/gwiki/src/ai/translate.rs
type: code_file
provenance:
- file: crates/gwiki/src/ai/translate.rs
  ranges:
  - 6-29
  - 31-55
  - 57-87
  - 89-93
  - 95-97
  - 99-110
  - 112-122
  - 124-129
  - 131-133
  - 135-137
  - 147-154
  - 156-170
  - 172-207
  - 210-236
  - 239-259
  - 262-290
  - 293-316
  - 318-325
  - 327-349
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ai/translate.rs

Module: [[code/modules/crates/gwiki/src/ai|crates/gwiki/src/ai]]

## Purpose

Orchestrates audio transcription and translation for wiki content, choosing between direct English translation and segment-by-segment translation based on the target language and client support. The main path normalizes the requested language, prefers `translate_to_english` for English targets with a transcription fallback, and otherwise transcribes first then rewrites the output via `translate_transcription_segments`, which resolves the source language, skips work when source and target match, and updates translation metadata after replacing segment text. Supporting helpers normalize and compare language codes, emit batch-translation warnings, and mark English translation outputs. The file also includes a `FakeTranslationClient` plus test fixtures and cases that verify fallback behavior, language precedence, and batch retry logic.
[crates/gwiki/src/ai/translate.rs:6-29]
[crates/gwiki/src/ai/translate.rs:31-55]
[crates/gwiki/src/ai/translate.rs:57-87]
[crates/gwiki/src/ai/translate.rs:89-93]
[crates/gwiki/src/ai/translate.rs:95-97]

## API Symbols

- `translate_audio` (function) component `translate_audio [function]` (`b904720c-a279-5107-93cd-ceb111199ebb`) lines 6-29 [crates/gwiki/src/ai/translate.rs:6-29]
  - Signature: `pub(crate) fn translate_audio(`
  - Purpose: Transcribes audio and translates it to the normalized target language, attempting direct English translation via client with fallback to segment-level translation on failure or for non-English targets. [crates/gwiki/src/ai/translate.rs:6-29]
- `translate_transcription_segments` (function) component `translate_transcription_segments [function]` (`fa2ba574-019a-5c1f-8ab3-c03457e92d76`) lines 31-55 [crates/gwiki/src/ai/translate.rs:31-55]
  - Signature: `pub(crate) fn translate_transcription_segments(`
  - Purpose: Translates all text segments in a TranscriptionOutput from a detected source language to a target language, updating metadata and early-returning if source and target languages are identical. [crates/gwiki/src/ai/translate.rs:31-55]
- `translate_segment_texts` (function) component `translate_segment_texts [function]` (`75234a29-8f78-5c9c-b4c9-5156438a6f52`) lines 57-87 [crates/gwiki/src/ai/translate.rs:57-87]
  - Signature: `fn translate_segment_texts(`
  - Purpose: Translates an array of transcript segments between languages using attempted batch translation with per-segment fallback on failure or count mismatch. [crates/gwiki/src/ai/translate.rs:57-87]
- `warn_translation_batch_mismatch` (function) component `warn_translation_batch_mismatch [function]` (`5cb8e8a4-6c7c-5404-bf44-79b8aabdf79e`) lines 89-93 [crates/gwiki/src/ai/translate.rs:89-93]
  - Signature: `fn warn_translation_batch_mismatch(attempt: &str, actual_len: usize, expected_len: usize) {`
  - Purpose: Emits a warning to stderr when a translation batch returns an actual text count that differs from the expected segment count, signaling a retry or batch size reduction. [crates/gwiki/src/ai/translate.rs:89-93]
- `warn_translation_batch_error` (function) component `warn_translation_batch_error [function]` (`34e97701-071f-5687-a91d-1f60fad485fe`) lines 95-97 [crates/gwiki/src/ai/translate.rs:95-97]
  - Signature: `fn warn_translation_batch_error(attempt: &str, error: &WikiError) {`
  - Purpose: Logs a warning message to stderr indicating that a translation batch failed for the given attempt and will be retried, including the error details. [crates/gwiki/src/ai/translate.rs:95-97]
- `mark_english_translation` (function) component `mark_english_translation [function]` (`8dc9c1df-7963-5d80-a5f9-b69640ae2953`) lines 99-110 [crates/gwiki/src/ai/translate.rs:99-110]
  - Signature: `fn mark_english_translation(`
  - Purpose: Marks a `TranscriptionOutput` as an English translation task by detecting the source language, setting target language to English, and flagging the `translated` field. [crates/gwiki/src/ai/translate.rs:99-110]
- `source_language` (function) component `source_language [function]` (`59fe7e0a-4ca2-57ec-956d-4ecb5827a710`) lines 112-122 [crates/gwiki/src/ai/translate.rs:112-122]
  - Signature: `fn source_language(`
  - Purpose: Resolves a normalized source language by chaining fallback attempts across a language hint and transcription output language fields using `or_else` combinators, returning `WikiError` if all options fail. [crates/gwiki/src/ai/translate.rs:112-122]
- `normalized_lang` (function) component `normalized_lang [function]` (`01638c48-e500-5fb3-a4cf-568060442b50`) lines 124-129 [crates/gwiki/src/ai/translate.rs:124-129]
  - Signature: `fn normalized_lang(language: Option<&str>) -> Option<String> {`
  - Purpose: Normalizes an optional language string by trimming whitespace, converting to lowercase ASCII, and filtering out empty values, returning `None` if the input is `None` or becomes empty after trimming. [crates/gwiki/src/ai/translate.rs:124-129]
- `is_english` (function) component `is_english [function]` (`8ccba966-5de2-5b71-af16-ec89187881e8`) lines 131-133 [crates/gwiki/src/ai/translate.rs:131-133]
  - Signature: `fn is_english(language: &str) -> bool {`
  - Purpose: Checks whether a language code represents English or an English variant by testing for exact match to "en" or string prefixes "en-" and "en_". [crates/gwiki/src/ai/translate.rs:131-133]
- `same_lang` (function) component `same_lang [function]` (`691d805f-24f1-536b-8d59-034074a18677`) lines 135-137 [crates/gwiki/src/ai/translate.rs:135-137]
  - Signature: `fn same_lang(left: &str, right: &str) -> bool {`
  - Purpose: `same_lang` performs a case-insensitive ASCII comparison of two strings, returning true if they are equal. [crates/gwiki/src/ai/translate.rs:135-137]
- `FakeTranslationClient` (class) component `FakeTranslationClient [class]` (`a9d8267d-048d-54dc-9edf-011805a7e220`) lines 147-154 [crates/gwiki/src/ai/translate.rs:147-154]
  - Signature: `struct FakeTranslationClient {`
  - Purpose: A Rust mock translation client using `RefCell` for interior mutability to capture transcription outputs, segment batches, translations, errors, and method invocations for testing purposes. [crates/gwiki/src/ai/translate.rs:147-154]
- `FakeTranslationClient` (class) component `FakeTranslationClient [class]` (`d3dd22df-a7ef-5764-85fa-0303397ab5f0`) lines 156-170 [crates/gwiki/src/ai/translate.rs:156-170]
  - Signature: `impl FakeTranslationClient {`
  - Purpose: FakeTranslationClient implements a builder pattern using RefCell interior mutability to fluently construct test instances with predefined transcription outputs. [crates/gwiki/src/ai/translate.rs:156-170]
- `FakeTranslationClient.with_transcript` (method) component `FakeTranslationClient.with_transcript [method]` (`ea14b0e9-af0c-5d8c-ab93-95efbed1971c`) lines 157-162 [crates/gwiki/src/ai/translate.rs:157-162]
  - Signature: `fn with_transcript(output: TranscriptionOutput) -> Self {`
  - Purpose: Creates a new instance with the provided `TranscriptionOutput` wrapped in `RefCell<Option>` for the transcript field and all other fields initialized to their default values. [crates/gwiki/src/ai/translate.rs:157-162]
- `FakeTranslationClient.with_english` (method) component `FakeTranslationClient.with_english [method]` (`dddcff40-4a13-5cec-bc16-cc60d7211b6e`) lines 164-169 [crates/gwiki/src/ai/translate.rs:164-169]
  - Signature: `fn with_english(output: Result<TranscriptionOutput, WikiError>) -> Self {`
  - Purpose: This method constructs a new instance of the containing struct with the `english` field initialized to a `RefCell`-wrapped `Option` of the provided `Result<TranscriptionOutput, WikiError>`, while remaining fields are populated with their default values. [crates/gwiki/src/ai/translate.rs:164-169]
- `FakeTranslationClient` (class) component `FakeTranslationClient [class]` (`aa2a3d17-8560-57dc-87db-2fdcac38de25`) lines 172-207 [crates/gwiki/src/ai/translate.rs:172-207]
  - Signature: `impl TranscriptionClient for FakeTranslationClient {`
  - Purpose: A mock implementation of `TranscriptionClient` that records method invocations, stores request parameters for assertion, and returns pre-configured or injected responses/errors for testing. [crates/gwiki/src/ai/translate.rs:172-207]
- `FakeTranslationClient.transcribe` (method) component `FakeTranslationClient.transcribe [method]` (`c07c2840-0bce-5c5e-9b83-67b78977d3de`) lines 173-179 [crates/gwiki/src/ai/translate.rs:173-179]
  - Signature: `fn transcribe(`
  - Purpose: This method records a transcribe call to an internal log and returns a pre-stored `TranscriptionOutput` by consuming and unwrapping an `Option` value. [crates/gwiki/src/ai/translate.rs:173-179]
- `FakeTranslationClient.translate_to_english` (method) component `FakeTranslationClient.translate_to_english [method]` (`2bc08167-d8f3-53cf-9db9-2e391f29c55e`) lines 181-188 [crates/gwiki/src/ai/translate.rs:181-188]
  - Signature: `fn translate_to_english(`
  - Purpose: This mock method records the function call and returns a pre-configured `TranscriptionOutput` by consuming an internal optional field via `take()` and `unwrap()`. [crates/gwiki/src/ai/translate.rs:181-188]
- `FakeTranslationClient.translate_segments` (method) component `FakeTranslationClient.translate_segments [method]` (`ac2ce153-4332-5df8-b32c-1badba9dadcc`) lines 190-206 [crates/gwiki/src/ai/translate.rs:190-206]
  - Signature: `fn translate_segments(`
  - Purpose: This method records a translation request and returns either a pre-configured error or translated text result from internal queues, functioning as a mock translator for testing. [crates/gwiki/src/ai/translate.rs:190-206]
- `precedence_and_segment_wise` (function) component `precedence_and_segment_wise [function]` (`e9ae3f4b-b63a-5cee-8160-1227c46015bc`) lines 210-236 [crates/gwiki/src/ai/translate.rs:210-236]
  - Signature: `fn precedence_and_segment_wise() {`
  - Purpose: This test function verifies that `translate_audio` skips translation when the source and target languages match, and correctly preserves segment-wise timing and translated text content when translating between different language pairs. [crates/gwiki/src/ai/translate.rs:210-236]
- `translations_unsupported_fallback` (function) component `translations_unsupported_fallback [function]` (`a071841e-7555-5f02-9fbf-5f3420be4379`) lines 239-259 [crates/gwiki/src/ai/translate.rs:239-259]
  - Signature: `fn translations_unsupported_fallback() {`
  - Purpose: This test verifies that `translate_audio` gracefully falls back to transcribing and translating segments when the audio translations endpoint is unsupported, while correctly setting the `translation_degraded` flag. [crates/gwiki/src/ai/translate.rs:239-259]
- `english_one_pass_vs_target_first` (function) component `english_one_pass_vs_target_first [function]` (`01a578a5-71ed-5a3f-a7a4-153605f04415`) lines 262-290 [crates/gwiki/src/ai/translate.rs:262-290]
  - Signature: `fn english_one_pass_vs_target_first() {`
  - Purpose: This test verifies that `translate_audio` invokes `translate_to_english` when the target language is English, but calls `transcribe` directly when the target language is non-English, confirming the function bypasses English translation as an intermediary for non-English targets. [crates/gwiki/src/ai/translate.rs:262-290]
- `batch_translation_errors_retry_batch_before_success` (function) component `batch_translation_errors_retry_batch_before_success [function]` (`16981315-7346-53b6-adc6-111f88d159df`) lines 293-316 [crates/gwiki/src/ai/translate.rs:293-316]
  - Signature: `fn batch_translation_errors_retry_batch_before_success() {`
  - Purpose: Verifies that `translate_audio` recovers from a `WikiError::Config` "batch unavailable" error by retrying the segment batch, ultimately producing correct translations across two batch attempts. [crates/gwiki/src/ai/translate.rs:293-316]
- `request` (function) component `request [function]` (`8c66f12f-4bbb-5a85-b464-7dc9611dfb24`) lines 318-325 [crates/gwiki/src/ai/translate.rs:318-325]
  - Signature: `fn request<'a>() -> TranscriptionRequest<'a> {`
  - Purpose: Constructs a `TranscriptionRequest<'a>` with hardcoded WebM audio metadata (filename, MIME type, asset path) and mock audio bytes for testing purposes. [crates/gwiki/src/ai/translate.rs:318-325]
- `output` (function) component `output [function]` (`c68dee89-e779-5e4f-998c-585372ffeab9`) lines 327-349 [crates/gwiki/src/ai/translate.rs:327-349]
  - Signature: `fn output(source_lang: &str, texts: &[&str]) -> TranscriptionOutput {`
  - Purpose: Constructs a `TranscriptionOutput` from an array of texts by creating sequentially-timed `TranscriptSegment` entries at uniform 1-second intervals, initialized with the specified source language and test-model metadata. [crates/gwiki/src/ai/translate.rs:327-349]

