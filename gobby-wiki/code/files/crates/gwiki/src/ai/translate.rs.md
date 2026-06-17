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
  - 157-162
  - 164-169
  - 173-179
  - 181-188
  - 190-206
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ai/translate.rs:6-29](crates/gwiki/src/ai/translate.rs#L6-L29), [crates/gwiki/src/ai/translate.rs:31-55](crates/gwiki/src/ai/translate.rs#L31-L55), [crates/gwiki/src/ai/translate.rs:57-87](crates/gwiki/src/ai/translate.rs#L57-L87), [crates/gwiki/src/ai/translate.rs:89-93](crates/gwiki/src/ai/translate.rs#L89-L93), [crates/gwiki/src/ai/translate.rs:95-97](crates/gwiki/src/ai/translate.rs#L95-L97), [crates/gwiki/src/ai/translate.rs:99-110](crates/gwiki/src/ai/translate.rs#L99-L110), [crates/gwiki/src/ai/translate.rs:112-122](crates/gwiki/src/ai/translate.rs#L112-L122), [crates/gwiki/src/ai/translate.rs:124-129](crates/gwiki/src/ai/translate.rs#L124-L129), [crates/gwiki/src/ai/translate.rs:131-133](crates/gwiki/src/ai/translate.rs#L131-L133), [crates/gwiki/src/ai/translate.rs:135-137](crates/gwiki/src/ai/translate.rs#L135-L137), [crates/gwiki/src/ai/translate.rs:147-154](crates/gwiki/src/ai/translate.rs#L147-L154), [crates/gwiki/src/ai/translate.rs:157-162](crates/gwiki/src/ai/translate.rs#L157-L162), [crates/gwiki/src/ai/translate.rs:164-169](crates/gwiki/src/ai/translate.rs#L164-L169), [crates/gwiki/src/ai/translate.rs:173-179](crates/gwiki/src/ai/translate.rs#L173-L179), [crates/gwiki/src/ai/translate.rs:181-188](crates/gwiki/src/ai/translate.rs#L181-L188), [crates/gwiki/src/ai/translate.rs:190-206](crates/gwiki/src/ai/translate.rs#L190-L206), [crates/gwiki/src/ai/translate.rs:210-236](crates/gwiki/src/ai/translate.rs#L210-L236), [crates/gwiki/src/ai/translate.rs:239-259](crates/gwiki/src/ai/translate.rs#L239-L259), [crates/gwiki/src/ai/translate.rs:262-290](crates/gwiki/src/ai/translate.rs#L262-L290), [crates/gwiki/src/ai/translate.rs:293-316](crates/gwiki/src/ai/translate.rs#L293-L316), [crates/gwiki/src/ai/translate.rs:318-325](crates/gwiki/src/ai/translate.rs#L318-L325), [crates/gwiki/src/ai/translate.rs:327-349](crates/gwiki/src/ai/translate.rs#L327-L349)

</details>

# crates/gwiki/src/ai/translate.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides translation orchestration for transcribed audio. `translate_audio` normalizes the target language, uses a direct `translate_to_english` path when the target is English, and falls back to plain transcription plus segment-by-segment translation if that fails. `translate_transcription_segments` and `translate_segment_texts` apply the source-language detection, skip work when source and target already match, and merge translated text back into the transcript while setting the output metadata. The remaining helpers handle language normalization, English marking, and warning paths, while `FakeTranslationClient` plus the test functions exercise precedence, fallback behavior, and batch-translation retry/error handling.
[crates/gwiki/src/ai/translate.rs:6-29]
[crates/gwiki/src/ai/translate.rs:31-55]
[crates/gwiki/src/ai/translate.rs:57-87]
[crates/gwiki/src/ai/translate.rs:89-93]
[crates/gwiki/src/ai/translate.rs:95-97]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `translate_audio` | function | `pub(crate) fn translate_audio(` | `translate_audio [function]` | `b904720c-a279-5107-93cd-ceb111199ebb` | 6-29 [crates/gwiki/src/ai/translate.rs:6-29] | Indexed function `translate_audio` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:6-29] |
| `translate_transcription_segments` | function | `pub(crate) fn translate_transcription_segments(` | `translate_transcription_segments [function]` | `fa2ba574-019a-5c1f-8ab3-c03457e92d76` | 31-55 [crates/gwiki/src/ai/translate.rs:31-55] | Indexed function `translate_transcription_segments` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:31-55] |
| `translate_segment_texts` | function | `fn translate_segment_texts(` | `translate_segment_texts [function]` | `75234a29-8f78-5c9c-b4c9-5156438a6f52` | 57-87 [crates/gwiki/src/ai/translate.rs:57-87] | Indexed function `translate_segment_texts` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:57-87] |
| `warn_translation_batch_mismatch` | function | `fn warn_translation_batch_mismatch(attempt: &str, actual_len: usize, expected_len: usize) {` | `warn_translation_batch_mismatch [function]` | `5cb8e8a4-6c7c-5404-bf44-79b8aabdf79e` | 89-93 [crates/gwiki/src/ai/translate.rs:89-93] | Indexed function `warn_translation_batch_mismatch` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:89-93] |
| `warn_translation_batch_error` | function | `fn warn_translation_batch_error(attempt: &str, error: &WikiError) {` | `warn_translation_batch_error [function]` | `34e97701-071f-5687-a91d-1f60fad485fe` | 95-97 [crates/gwiki/src/ai/translate.rs:95-97] | Indexed function `warn_translation_batch_error` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:95-97] |
| `mark_english_translation` | function | `fn mark_english_translation(` | `mark_english_translation [function]` | `8dc9c1df-7963-5d80-a5f9-b69640ae2953` | 99-110 [crates/gwiki/src/ai/translate.rs:99-110] | Indexed function `mark_english_translation` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:99-110] |
| `source_language` | function | `fn source_language(` | `source_language [function]` | `59fe7e0a-4ca2-57ec-956d-4ecb5827a710` | 112-122 [crates/gwiki/src/ai/translate.rs:112-122] | Indexed function `source_language` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:112-122] |
| `normalized_lang` | function | `fn normalized_lang(language: Option<&str>) -> Option<String> {` | `normalized_lang [function]` | `01638c48-e500-5fb3-a4cf-568060442b50` | 124-129 [crates/gwiki/src/ai/translate.rs:124-129] | Indexed function `normalized_lang` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:124-129] |
| `is_english` | function | `fn is_english(language: &str) -> bool {` | `is_english [function]` | `8ccba966-5de2-5b71-af16-ec89187881e8` | 131-133 [crates/gwiki/src/ai/translate.rs:131-133] | Indexed function `is_english` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:131-133] |
| `same_lang` | function | `fn same_lang(left: &str, right: &str) -> bool {` | `same_lang [function]` | `691d805f-24f1-536b-8d59-034074a18677` | 135-137 [crates/gwiki/src/ai/translate.rs:135-137] | Indexed function `same_lang` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:135-137] |
| `FakeTranslationClient` | class | `struct FakeTranslationClient {` | `FakeTranslationClient [class]` | `a9d8267d-048d-54dc-9edf-011805a7e220` | 147-154 [crates/gwiki/src/ai/translate.rs:147-154] | Indexed class `FakeTranslationClient` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:147-154] |
| `FakeTranslationClient::with_transcript` | method | `fn with_transcript(output: TranscriptionOutput) -> Self {` | `FakeTranslationClient::with_transcript [method]` | `ea14b0e9-af0c-5d8c-ab93-95efbed1971c` | 157-162 [crates/gwiki/src/ai/translate.rs:157-162] | Indexed method `FakeTranslationClient::with_transcript` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:157-162] |
| `FakeTranslationClient::with_english` | method | `fn with_english(output: Result<TranscriptionOutput, WikiError>) -> Self {` | `FakeTranslationClient::with_english [method]` | `dddcff40-4a13-5cec-bc16-cc60d7211b6e` | 164-169 [crates/gwiki/src/ai/translate.rs:164-169] | Indexed method `FakeTranslationClient::with_english` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:164-169] |
| `FakeTranslationClient::transcribe` | method | `fn transcribe(` | `FakeTranslationClient::transcribe [method]` | `c07c2840-0bce-5c5e-9b83-67b78977d3de` | 173-179 [crates/gwiki/src/ai/translate.rs:173-179] | Indexed method `FakeTranslationClient::transcribe` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:173-179] |
| `FakeTranslationClient::translate_to_english` | method | `fn translate_to_english(` | `FakeTranslationClient::translate_to_english [method]` | `2bc08167-d8f3-53cf-9db9-2e391f29c55e` | 181-188 [crates/gwiki/src/ai/translate.rs:181-188] | Indexed method `FakeTranslationClient::translate_to_english` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:181-188] |
| `FakeTranslationClient::translate_segments` | method | `fn translate_segments(` | `FakeTranslationClient::translate_segments [method]` | `ac2ce153-4332-5df8-b32c-1badba9dadcc` | 190-206 [crates/gwiki/src/ai/translate.rs:190-206] | Indexed method `FakeTranslationClient::translate_segments` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:190-206] |
| `precedence_and_segment_wise` | function | `fn precedence_and_segment_wise() {` | `precedence_and_segment_wise [function]` | `e9ae3f4b-b63a-5cee-8160-1227c46015bc` | 210-236 [crates/gwiki/src/ai/translate.rs:210-236] | Indexed function `precedence_and_segment_wise` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:210-236] |
| `translations_unsupported_fallback` | function | `fn translations_unsupported_fallback() {` | `translations_unsupported_fallback [function]` | `a071841e-7555-5f02-9fbf-5f3420be4379` | 239-259 [crates/gwiki/src/ai/translate.rs:239-259] | Indexed function `translations_unsupported_fallback` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:239-259] |
| `english_one_pass_vs_target_first` | function | `fn english_one_pass_vs_target_first() {` | `english_one_pass_vs_target_first [function]` | `01a578a5-71ed-5a3f-a7a4-153605f04415` | 262-290 [crates/gwiki/src/ai/translate.rs:262-290] | Indexed function `english_one_pass_vs_target_first` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:262-290] |
| `batch_translation_errors_retry_batch_before_success` | function | `fn batch_translation_errors_retry_batch_before_success() {` | `batch_translation_errors_retry_batch_before_success [function]` | `16981315-7346-53b6-adc6-111f88d159df` | 293-316 [crates/gwiki/src/ai/translate.rs:293-316] | Indexed function `batch_translation_errors_retry_batch_before_success` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:293-316] |
| `request` | function | `fn request<'a>() -> TranscriptionRequest<'a> {` | `request [function]` | `8c66f12f-4bbb-5a85-b464-7dc9611dfb24` | 318-325 [crates/gwiki/src/ai/translate.rs:318-325] | Indexed function `request` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:318-325] |
| `output` | function | `fn output(source_lang: &str, texts: &[&str]) -> TranscriptionOutput {` | `output [function]` | `c68dee89-e779-5e4f-998c-585372ffeab9` | 327-349 [crates/gwiki/src/ai/translate.rs:327-349] | Indexed function `output` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:327-349] |
