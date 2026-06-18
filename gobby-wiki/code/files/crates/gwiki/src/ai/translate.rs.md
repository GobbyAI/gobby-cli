---
title: crates/gwiki/src/ai/translate.rs
type: code_file
provenance:
- file: crates/gwiki/src/ai/translate.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ai/translate.rs

Module: [[code/modules/crates/gwiki/src/ai|crates/gwiki/src/ai]]

## Overview

`crates/gwiki/src/ai/translate.rs` exposes 22 indexed API symbols.

## How it fits

`crates/gwiki/src/ai/translate.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `translate_audio` | function | Indexed function `translate_audio` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:6-29] |
| `translate_transcription_segments` | function | Indexed function `translate_transcription_segments` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:31-55] |
| `translate_segment_texts` | function | Indexed function `translate_segment_texts` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:57-87] |
| `warn_translation_batch_mismatch` | function | Indexed function `warn_translation_batch_mismatch` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:89-93] |
| `warn_translation_batch_error` | function | Indexed function `warn_translation_batch_error` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:95-97] |
| `mark_english_translation` | function | Indexed function `mark_english_translation` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:99-110] |
| `source_language` | function | Indexed function `source_language` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:112-122] |
| `normalized_lang` | function | Indexed function `normalized_lang` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:124-129] |
| `is_english` | function | Indexed function `is_english` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:131-133] |
| `same_lang` | function | Indexed function `same_lang` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:135-137] |
| `FakeTranslationClient` | class | Indexed class `FakeTranslationClient` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:147-154] |
| `FakeTranslationClient::with_transcript` | method | Indexed method `FakeTranslationClient::with_transcript` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:157-162] |
| `FakeTranslationClient::with_english` | method | Indexed method `FakeTranslationClient::with_english` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:164-169] |
| `FakeTranslationClient::transcribe` | method | Indexed method `FakeTranslationClient::transcribe` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:173-179] |
| `FakeTranslationClient::translate_to_english` | method | Indexed method `FakeTranslationClient::translate_to_english` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:181-188] |
| `FakeTranslationClient::translate_segments` | method | Indexed method `FakeTranslationClient::translate_segments` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:190-206] |
| `precedence_and_segment_wise` | function | Indexed function `precedence_and_segment_wise` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:210-236] |
| `translations_unsupported_fallback` | function | Indexed function `translations_unsupported_fallback` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:239-259] |
| `english_one_pass_vs_target_first` | function | Indexed function `english_one_pass_vs_target_first` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:262-290] |
| `batch_translation_errors_retry_batch_before_success` | function | Indexed function `batch_translation_errors_retry_batch_before_success` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:293-316] |
| `request` | function | Indexed function `request` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:318-325] |
| `output` | function | Indexed function `output` in `crates/gwiki/src/ai/translate.rs`. [crates/gwiki/src/ai/translate.rs:327-349] |

