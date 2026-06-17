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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/ask/narration.rs:7-58](crates/gwiki/src/commands/ask/narration.rs#L7-L58), [crates/gwiki/src/commands/ask/narration.rs:60-64](crates/gwiki/src/commands/ask/narration.rs#L60-L64), [crates/gwiki/src/commands/ask/narration.rs:89-103](crates/gwiki/src/commands/ask/narration.rs#L89-L103), [crates/gwiki/src/commands/ask/narration.rs:105-123](crates/gwiki/src/commands/ask/narration.rs#L105-L123), [crates/gwiki/src/commands/ask/narration.rs:130-162](crates/gwiki/src/commands/ask/narration.rs#L130-L162), [crates/gwiki/src/commands/ask/narration.rs:165-169](crates/gwiki/src/commands/ask/narration.rs#L165-L169), [crates/gwiki/src/commands/ask/narration.rs:172-181](crates/gwiki/src/commands/ask/narration.rs#L172-L181), [crates/gwiki/src/commands/ask/narration.rs:184-187](crates/gwiki/src/commands/ask/narration.rs#L184-L187), [crates/gwiki/src/commands/ask/narration.rs:190-214](crates/gwiki/src/commands/ask/narration.rs#L190-L214)

</details>

# crates/gwiki/src/commands/ask/narration.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements heuristics for trimming leading model narration from an answer before returning it. `strip_leading_model_narration` scans up to a fixed sentence limit, uses `leading_sentence_end` to walk sentence-by-sentence, classifies each opening sentence with `is_model_narration_sentence`, and then strips either the initial contiguous narration run or a longer narration-heavy preamble when narration still dominates. `strip_narration_discourse_markers` supports that classification by removing common discourse markers, and the tests exercise the main cases: interleaved narration, content openers that disable stripping, low-density narration that only trims the front, fully narrated answers that stay intact, and narration introduced by discourse markers.
[crates/gwiki/src/commands/ask/narration.rs:7-58]
[crates/gwiki/src/commands/ask/narration.rs:60-64]
[crates/gwiki/src/commands/ask/narration.rs:89-103]
[crates/gwiki/src/commands/ask/narration.rs:105-123]
[crates/gwiki/src/commands/ask/narration.rs:130-162]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `strip_leading_model_narration` | function | `pub(super) fn strip_leading_model_narration(answer: &str) -> String {` | `strip_leading_model_narration [function]` | `72e0fcf5-bdc0-503e-aee3-a8bee08fe46e` | 7-58 [crates/gwiki/src/commands/ask/narration.rs:7-58] | Indexed function `strip_leading_model_narration` in `crates/gwiki/src/commands/ask/narration.rs`. [crates/gwiki/src/commands/ask/narration.rs:7-58] |
| `leading_sentence_end` | function | `fn leading_sentence_end(text: &str) -> Option<usize> {` | `leading_sentence_end [function]` | `45e7cd34-35a4-5bf5-83f3-06c38392d127` | 60-64 [crates/gwiki/src/commands/ask/narration.rs:60-64] | Indexed function `leading_sentence_end` in `crates/gwiki/src/commands/ask/narration.rs`. [crates/gwiki/src/commands/ask/narration.rs:60-64] |
| `is_model_narration_sentence` | function | `fn is_model_narration_sentence(sentence: &str) -> bool {` | `is_model_narration_sentence [function]` | `870dd309-7988-53a4-9e74-d2ea911921c1` | 89-103 [crates/gwiki/src/commands/ask/narration.rs:89-103] | Indexed function `is_model_narration_sentence` in `crates/gwiki/src/commands/ask/narration.rs`. [crates/gwiki/src/commands/ask/narration.rs:89-103] |
| `strip_narration_discourse_markers` | function | `fn strip_narration_discourse_markers(normalized: &str) -> &str {` | `strip_narration_discourse_markers [function]` | `937d9223-7e9f-55aa-94d7-0e6c86cdaa60` | 105-123 [crates/gwiki/src/commands/ask/narration.rs:105-123] | Indexed function `strip_narration_discourse_markers` in `crates/gwiki/src/commands/ask/narration.rs`. [crates/gwiki/src/commands/ask/narration.rs:105-123] |
| `interleaved_narration_preamble_is_stripped_to_answer` | function | `fn interleaved_narration_preamble_is_stripped_to_answer() {` | `interleaved_narration_preamble_is_stripped_to_answer [function]` | `55273cc5-ccf0-545a-9890-2994a3bca5ec` | 130-162 [crates/gwiki/src/commands/ask/narration.rs:130-162] | Indexed function `interleaved_narration_preamble_is_stripped_to_answer` in `crates/gwiki/src/commands/ask/narration.rs`. [crates/gwiki/src/commands/ask/narration.rs:130-162] |
| `content_opener_disables_narration_stripping` | function | `fn content_opener_disables_narration_stripping() {` | `content_opener_disables_narration_stripping [function]` | `36e213fd-7621-5f1e-9e51-662fe3621976` | 165-169 [crates/gwiki/src/commands/ask/narration.rs:165-169] | Indexed function `content_opener_disables_narration_stripping` in `crates/gwiki/src/commands/ask/narration.rs`. [crates/gwiki/src/commands/ask/narration.rs:165-169] |
| `low_narration_density_strips_only_the_leading_run` | function | `fn low_narration_density_strips_only_the_leading_run() {` | `low_narration_density_strips_only_the_leading_run [function]` | `09d151b0-4123-59ee-ae14-74eeaa3db0c9` | 172-181 [crates/gwiki/src/commands/ask/narration.rs:172-181] | Indexed function `low_narration_density_strips_only_the_leading_run` in `crates/gwiki/src/commands/ask/narration.rs`. [crates/gwiki/src/commands/ask/narration.rs:172-181] |
| `all_narration_answer_is_kept_verbatim` | function | `fn all_narration_answer_is_kept_verbatim() {` | `all_narration_answer_is_kept_verbatim [function]` | `f5f3ea15-3be0-581b-a677-266f9bf6be9f` | 184-187 [crates/gwiki/src/commands/ask/narration.rs:184-187] | Indexed function `all_narration_answer_is_kept_verbatim` in `crates/gwiki/src/commands/ask/narration.rs`. [crates/gwiki/src/commands/ask/narration.rs:184-187] |
| `discourse_markers_before_first_person_openers_are_narration` | function | `fn discourse_markers_before_first_person_openers_are_narration() {` | `discourse_markers_before_first_person_openers_are_narration [function]` | `65bdbe82-112d-537d-8a4d-d4d24a21d479` | 190-214 [crates/gwiki/src/commands/ask/narration.rs:190-214] | Indexed function `discourse_markers_before_first_person_openers_are_narration` in `crates/gwiki/src/commands/ask/narration.rs`. [crates/gwiki/src/commands/ask/narration.rs:190-214] |
