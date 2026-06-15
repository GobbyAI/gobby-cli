---
title: crates/gwiki/src/commands/ask/narration.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/narration.rs
  ranges:
  - 7-58
  - 60-64
  - 89-103
  - 105-123
  - 130-162
  - 165-169
  - 172-181
  - 184-187
  - 190-214
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask/narration.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Purpose

Provides narration-stripping logic for `ask` responses: it trims leading whitespace, scans up to `NARRATION_SCAN_LIMIT` sentence boundaries, and removes a leading preamble of model narration only when the output opens with narration and the skipped prefix is still mostly narration. `leading_sentence_end` finds sentence boundaries, `strip_narration_discourse_markers` normalizes and removes leading discourse markers, and `is_model_narration_sentence` identifies narration by matching cleaned sentence openers plus required process markers. The tests cover the main cases: stripping an interleaved narration preamble, leaving substantive answers unchanged, preserving later narration-like sentences, keeping plain answers verbatim, and classifying discourse-marked first-person openers as narration.
[crates/gwiki/src/commands/ask/narration.rs:7-58]
[crates/gwiki/src/commands/ask/narration.rs:60-64]
[crates/gwiki/src/commands/ask/narration.rs:89-103]
[crates/gwiki/src/commands/ask/narration.rs:105-123]
[crates/gwiki/src/commands/ask/narration.rs:130-162]

## API Symbols

- `strip_leading_model_narration` (function) component `strip_leading_model_narration [function]` (`72e0fcf5-bdc0-503e-aee3-a8bee08fe46e`) lines 7-58 [crates/gwiki/src/commands/ask/narration.rs:7-58]
  - Signature: `pub(super) fn strip_leading_model_narration(answer: &str) -> String {`
  - Purpose: Trims leading whitespace, scans up to 'NARRATION_SCAN_LIMIT' initial sentences, and removes the longest leading run of sentences classified as model narration when narration starts the string and remains the majority of the skipped prefix, otherwise returning the trimmed input unchanged. [crates/gwiki/src/commands/ask/narration.rs:7-58]
- `leading_sentence_end` (function) component `leading_sentence_end [function]` (`45e7cd34-35a4-5bf5-83f3-06c38392d127`) lines 60-64 [crates/gwiki/src/commands/ask/narration.rs:60-64]
  - Signature: `fn leading_sentence_end(text: &str) -> Option<usize> {`
  - Purpose: Returns the byte offset immediately after the first '.', '!', or '?' in 'text', or 'None' if no such sentence-ending punctuation exists. [crates/gwiki/src/commands/ask/narration.rs:60-64]
- `is_model_narration_sentence` (function) component `is_model_narration_sentence [function]` (`870dd309-7988-53a4-9e74-d2ea911921c1`) lines 89-103 [crates/gwiki/src/commands/ask/narration.rs:89-103]
  - Signature: `fn is_model_narration_sentence(sentence: &str) -> bool {`
  - Purpose: It trims and normalizes the sentence to lowercase ASCII apostrophes, strips leading discourse markers, and returns 'true' only if the resulting opener matches a configured narration prefix and the normalized text contains a configured process marker. [crates/gwiki/src/commands/ask/narration.rs:89-103]
- `strip_narration_discourse_markers` (function) component `strip_narration_discourse_markers [function]` (`937d9223-7e9f-55aa-94d7-0e6c86cdaa60`) lines 105-123 [crates/gwiki/src/commands/ask/narration.rs:105-123]
  - Signature: `fn strip_narration_discourse_markers(normalized: &str) -> &str {`
  - Purpose: It repeatedly strips any leading 'NARRATION_DISCOURSE_MARKERS' entry, optionally consuming a following comma and whitespace, and returns the remaining prefix of 'normalized'. [crates/gwiki/src/commands/ask/narration.rs:105-123]
- `interleaved_narration_preamble_is_stripped_to_answer` (function) component `interleaved_narration_preamble_is_stripped_to_answer [function]` (`55273cc5-ccf0-545a-9890-2994a3bca5ec`) lines 130-162 [crates/gwiki/src/commands/ask/narration.rs:130-162]
  - Signature: `fn interleaved_narration_preamble_is_stripped_to_answer() {`
  - Purpose: I’m locating the test body so I can summarize the actual assertion, not just the name. After that I’ll compress it to one precise sentence.'gcode' can’t reach the local hub from this environment, so I’m falling back to a direct source search in the checkout to verify the test body.This test verifies that the response parser removes any interleaved narration preamble from a model output and retains only the final answer text. [crates/gwiki/src/commands/ask/narration.rs:130-162]
- `content_opener_disables_narration_stripping` (function) component `content_opener_disables_narration_stripping [function]` (`36e213fd-7621-5f1e-9e51-662fe3621976`) lines 165-169 [crates/gwiki/src/commands/ask/narration.rs:165-169]
  - Signature: `fn content_opener_disables_narration_stripping() {`
  - Purpose: This test verifies that 'strip_leading_model_narration' returns the input unchanged when the response starts with substantive content rather than leading narration. [crates/gwiki/src/commands/ask/narration.rs:165-169]
- `low_narration_density_strips_only_the_leading_run` (function) component `low_narration_density_strips_only_the_leading_run [function]` (`09d151b0-4123-59ee-ae14-74eeaa3db0c9`) lines 172-181 [crates/gwiki/src/commands/ask/narration.rs:172-181]
  - Signature: `fn low_narration_density_strips_only_the_leading_run() {`
  - Purpose: It asserts that 'strip_leading_model_narration' strips only the leading contiguous narration prefix from the input while preserving the remaining content, including any later narration-like sentence. [crates/gwiki/src/commands/ask/narration.rs:172-181]
- `all_narration_answer_is_kept_verbatim` (function) component `all_narration_answer_is_kept_verbatim [function]` (`f5f3ea15-3be0-581b-a677-266f9bf6be9f`) lines 184-187 [crates/gwiki/src/commands/ask/narration.rs:184-187]
  - Signature: `fn all_narration_answer_is_kept_verbatim() {`
  - Purpose: This test asserts that 'strip_leading_model_narration' leaves a plain answer string unchanged, preserving it verbatim when no leading model narration is present. [crates/gwiki/src/commands/ask/narration.rs:184-187]
- `discourse_markers_before_first_person_openers_are_narration` (function) component `discourse_markers_before_first_person_openers_are_narration [function]` (`65bdbe82-112d-537d-8a4d-d4d24a21d479`) lines 190-214 [crates/gwiki/src/commands/ask/narration.rs:190-214]
  - Signature: `fn discourse_markers_before_first_person_openers_are_narration() {`
  - Purpose: It verifies that 'is_model_narration_sentence' classifies sentences starting with discourse markers followed by first-person openers as narration, while rejecting ordinary content sentences and bare first-person statements. [crates/gwiki/src/commands/ask/narration.rs:190-214]

