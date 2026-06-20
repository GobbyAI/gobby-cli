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

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ai/translate.rs` exposes 22 indexed API symbols.

## How it fits

`crates/gwiki/src/ai/translate.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `translate_audio` | function | 'translate_audio' normalizes the requested target language, uses the transcription client’s English translation path when the target is English with a fallback to transcription plus segment-wise translation on failure, and otherwise always transcribes first and then translates the resulting segments into the target language. [crates/gwiki/src/ai/translate.rs:6-29] |
| `translate_transcription_segments` | function | Determines the source language for a 'TranscriptionOutput', returns it unchanged if it already matches 'target_lang', otherwise translates each segment’s text via 'TranscriptionClient', updates the output’s language/task metadata, and marks it as translated. [crates/gwiki/src/ai/translate.rs:31-55] |
| `translate_segment_texts` | function | Attempts to translate all transcript segments in batch with up to two retries on batch mismatch/error, then falls back to per-segment translation and returns a 'Vec<String>' or propagates a 'WikiError'. [crates/gwiki/src/ai/translate.rs:57-87] |
| `warn_translation_batch_mismatch` | function | Prints a warning to stderr indicating that a translation batch returned 'actual_len' texts for 'expected_len' segments during 'attempt', suggesting the caller should retry or fall back to smaller batches. [crates/gwiki/src/ai/translate.rs:89-93] |
| `warn_translation_batch_error` | function | Prints a warning to standard error indicating that the specified translation batch attempt failed and the entire batch will be retried, including the associated 'WikiError'. [crates/gwiki/src/ai/translate.rs:95-97] |
| `mark_english_translation` | function | Marks a 'TranscriptionOutput' as an English translation by setting its source language from 'source_language(...)', forcing 'language' and 'target_language' to '"en"', setting 'task' to '"translate"', and flagging 'translated' as 'true'. [crates/gwiki/src/ai/translate.rs:99-110] |
| `source_language` | function | 'source_language' returns the first normalized language identifier found from 'language_hint', 'output.source_language', or 'output.language', and otherwise returns a 'WikiError::Config' stating that the transcription did not report a source language. [crates/gwiki/src/ai/translate.rs:112-122] |
| `normalized_lang` | function | Returns the input language string trimmed of surrounding whitespace, discards it if empty, and otherwise lowercases it with ASCII-only case folding, preserving 'None' as 'None'. [crates/gwiki/src/ai/translate.rs:124-129] |
| `is_english` | function | Returns 'true' when 'language' is exactly '"en"' or begins with the locale prefixes '"en-"' or '"en_"', otherwise 'false'. [crates/gwiki/src/ai/translate.rs:131-133] |
| `same_lang` | function | Returns 'true' when 'left' and 'right' are equal under ASCII case-insensitive comparison, otherwise 'false'. [crates/gwiki/src/ai/translate.rs:135-137] |
| `FakeTranslationClient` | class | A test double for a translation client that records transcript/translation state, queued segment batches and errors, captured translated texts, and the sequence of method calls. [crates/gwiki/src/ai/translate.rs:147-154] |
| `FakeTranslationClient::with_transcript` | method | Constructs a default 'Self' instance with its 'transcript' field initialized to 'Some(output)' wrapped in a 'RefCell'. [crates/gwiki/src/ai/translate.rs:157-162] |
| `FakeTranslationClient::with_english` | method | Creates a 'Self' instance whose 'english' field is initialized to 'RefCell::new(Some(output))' and whose remaining fields use 'Self::default()'. [crates/gwiki/src/ai/translate.rs:164-169] |
| `FakeTranslationClient::transcribe` | method | Records the '"transcribe"' call in 'self.calls' and returns the current 'TranscriptionOutput' by taking and unwrapping 'self.transcript', ignoring the request argument. [crates/gwiki/src/ai/translate.rs:173-179] |
| `FakeTranslationClient::translate_to_english` | method | 'translate_to_english' records the call by pushing '"translate_to_english"' into 'self.calls' and then returns the single stored 'TranscriptionOutput' from 'self.english' by taking it and unwrapping the result. [crates/gwiki/src/ai/translate.rs:181-188] |
| `FakeTranslationClient::translate_segments` | method | Records the 'translate_segments' call and its inputs, returns the first queued 'WikiError' if any segment error is pending, otherwise removes and returns the next preloaded 'Vec<String>' translation result. [crates/gwiki/src/ai/translate.rs:190-206] |
| `request` | function | Returns a 'TranscriptionRequest<'a>' initialized with 'file_name' '"clip.webm"', 'mime_type' 'Some("audio/webm")', 'asset_path' set to 'clip.webm', and 'bytes' pointing to the static byte string 'b"audio"'. [crates/gwiki/src/ai/translate.rs:318-325] |
| `output` | function | Constructs a 'TranscriptionOutput' with one 1-second 'TranscriptSegment' per input text, sequentially timestamped from 0 ms, and populates language/model/task metadata from 'source_lang' while marking the result as a non-partial, non-translated transcription. [crates/gwiki/src/ai/translate.rs:327-349] |

_Verified by 4 in-file unit tests._

