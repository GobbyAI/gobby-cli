---
title: crates/gcode/src/commands/codewiki/text.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 45-51
  - 54-73
  - 76-96
  - 99-111
  - 114-127
  - 130-143
  - 146-156
  - 159-170
  - 173-205
  - 208-223
  - 226-233
  - 236-269
  - 272-275
  - 277-283
  - 286-299
  - 302-311
  - 314-326
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file is the `codewiki/text` module’s public facade: it re-exports text-generation helpers for citations, frontmatter, generation, sanitization, and structural summaries so other code can assemble CodeWiki prose from source spans and prompts. Its test module ties those pieces together by exercising span construction, provenance frontmatter formatting and truncation, citation marker/list generation, fallback span selection and ranking, reference emission, line wrapping, prompt-echo rejection, and bounded retry behavior for transient generation failures.
[crates/gcode/src/commands/codewiki/text.rs:45-51]
[crates/gcode/src/commands/codewiki/text.rs:54-73]
[crates/gcode/src/commands/codewiki/text.rs:76-96]
[crates/gcode/src/commands/codewiki/text.rs:99-111]
[crates/gcode/src/commands/codewiki/text.rs:114-127]

## API Symbols

- `span` (function) component `span [function]` (`d03702cc-9c07-5411-9449-1d95784cae8d`) lines 45-51 [crates/gcode/src/commands/codewiki/text.rs:45-51]
  - Signature: `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {`
  - Purpose: Constructs and returns a 'SourceSpan' by converting 'file' into a 'String' and storing it with the provided 'line_start' and 'line_end' values. [crates/gcode/src/commands/codewiki/text.rs:45-51]
- `frontmatter_coalesces_contiguous_provenance_ranges` (function) component `frontmatter_coalesces_contiguous_provenance_ranges [function]` (`f086fc1a-927c-5cb4-b8c3-70510af1b4bd`) lines 54-73 [crates/gcode/src/commands/codewiki/text.rs:54-73]
  - Signature: `fn frontmatter_coalesces_contiguous_provenance_ranges() {`
  - Purpose: Verifies that 'frontmatter' merges contiguous provenance spans from the same file into combined ranges in the generated document, while leaving isolated spans as single quoted line numbers. [crates/gcode/src/commands/codewiki/text.rs:54-73]
- `citation_list_emits_one_fallback_range_per_line` (function) component `citation_list_emits_one_fallback_range_per_line [function]` (`0f7d3ab4-1f09-56bf-af1c-ff0fcfa63755`) lines 76-96 [crates/gcode/src/commands/codewiki/text.rs:76-96]
  - Signature: `fn citation_list_emits_one_fallback_range_per_line() {`
  - Purpose: Verifies that 'citation_list' returns exactly one citation line per input span and that, when given an empty prefix, each emitted line matches the span’s fallback 'citation()' string. [crates/gcode/src/commands/codewiki/text.rs:76-96]
- `citation_list_caps_oversized_span_sets` (function) component `citation_list_caps_oversized_span_sets [function]` (`dcad9469-e964-5eb2-b4d3-c6395927371f`) lines 99-111 [crates/gcode/src/commands/codewiki/text.rs:99-111]
  - Signature: `fn citation_list_caps_oversized_span_sets() {`
  - Purpose: Verifies that 'citation_list' truncates an oversized set of 200 spans to exactly 'MAX_FALLBACK_CITATIONS' output lines. [crates/gcode/src/commands/codewiki/text.rs:99-111]
- `fallback_spans_prefer_distinct_files_over_one_files_span_run` (function) component `fallback_spans_prefer_distinct_files_over_one_files_span_run [function]` (`81a8f8f4-2122-5337-8170-8c7db3bed8cf`) lines 114-127 [crates/gcode/src/commands/codewiki/text.rs:114-127]
  - Signature: `fn fallback_spans_prefer_distinct_files_over_one_files_span_run() {`
  - Purpose: Verifies that 'fallback_spans' returns at most 'MAX_FALLBACK_CITATIONS' spans while preferring coverage from a distinct file, ensuring 'src/other.rs' is included even when most candidate spans come from 'src/big.rs'. [crates/gcode/src/commands/codewiki/text.rs:114-127]
- `citation_markers_are_capped_and_keep_reference_numbering` (function) component `citation_markers_are_capped_and_keep_reference_numbering [function]` (`13e52dd1-8d41-5a95-b61c-f7b3d69bcd29`) lines 130-143 [crates/gcode/src/commands/codewiki/text.rs:130-143]
  - Signature: `fn citation_markers_are_capped_and_keep_reference_numbering() {`
  - Purpose: Verifies that 'citation_markers' caps the number of fallback citation markers at 'MAX_FALLBACK_CITATIONS' while preserving sequential numbering from '[1]' onward. [crates/gcode/src/commands/codewiki/text.rs:130-143]
- `fallback_citations_rank_lexically_relevant_files_first` (function) component `fallback_citations_rank_lexically_relevant_files_first [function]` (`c6b44493-1d50-5a77-828a-5ced88fe5c08`) lines 146-156 [crates/gcode/src/commands/codewiki/text.rs:146-156]
  - Signature: `fn fallback_citations_rank_lexically_relevant_files_first() {`
  - Purpose: Tests that 'fallback_spans' ranks files by lexical relevance and selects 'src/parser.rs' first for the query about a parser walking an AST and emitting tokens. [crates/gcode/src/commands/codewiki/text.rs:146-156]
- `asset_data_files_rank_behind_source_unless_sole_provenance` (function) component `asset_data_files_rank_behind_source_unless_sole_provenance [function]` (`1f74cba0-5227-5243-bbcc-dac9326dcd5c`) lines 159-170 [crates/gcode/src/commands/codewiki/text.rs:159-170]
  - Signature: `fn asset_data_files_rank_behind_source_unless_sole_provenance() {`
  - Purpose: Verifies that 'fallback_spans' prefers source-file spans over 'assets/data.json' spans when both are present, but returns the asset-data span when it is the only available provenance. [crates/gcode/src/commands/codewiki/text.rs:159-170]
- `frontmatter_caps_provenance_and_records_truncation` (function) component `frontmatter_caps_provenance_and_records_truncation [function]` (`faf2699c-67e4-533f-ab9d-92c3bb3e8fae`) lines 173-205 [crates/gcode/src/commands/codewiki/text.rs:173-205]
  - Signature: `fn frontmatter_caps_provenance_and_records_truncation() {`
  - Purpose: Verifies that frontmatter generation caps provenance to 'MAX_FRONTMATTER_PROVENANCE_FILES', preserves the busiest file’s spans when truncating and records the exact overflow count via 'PROVENANCE_TRUNCATED_KEY', while omitting the truncation marker when provenance stays within bounds. [crates/gcode/src/commands/codewiki/text.rs:173-205]
- `references_resolve_only_markers_present_in_doc` (function) component `references_resolve_only_markers_present_in_doc [function]` (`360a4b2d-e775-5a44-b54f-25be7f901e9a`) lines 208-223 [crates/gcode/src/commands/codewiki/text.rs:208-223]
  - Signature: `fn references_resolve_only_markers_present_in_doc() {`
  - Purpose: Verifies that 'write_references' appends only the reference entries for marker IDs actually present in the document text, preserving the expected order and excluding unused spans. [crates/gcode/src/commands/codewiki/text.rs:208-223]
- `wrap_citation_items_bounds_line_width` (function) component `wrap_citation_items_bounds_line_width [function]` (`67b72f03-182e-51f3-afe5-25698bef4d53`) lines 226-233 [crates/gcode/src/commands/codewiki/text.rs:226-233]
  - Signature: `fn wrap_citation_items_bounds_line_width() {`
  - Purpose: Verifies that 'wrap_citation_items' wraps a sequence of 80 citation strings at a 40-character line width, producing multiple lines with every line length at most 40 characters. [crates/gcode/src/commands/codewiki/text.rs:226-233]
- `prompt_echo_is_rejected_as_failed_generation` (function) component `prompt_echo_is_rejected_as_failed_generation [function]` (`532815ef-2ca4-53ec-b3f2-a7a41039de20`) lines 236-269 [crates/gcode/src/commands/codewiki/text.rs:236-269]
  - Signature: `fn prompt_echo_is_rejected_as_failed_generation() {`
  - Purpose: Verifies that 'maybe_generate' marks an output that merely echoes the prompt as a failed generation, while accepting a non-echoing response as 'Generation::Generated'. [crates/gcode/src/commands/codewiki/text.rs:236-269]
- `short_prompts_never_trigger_echo_rejection` (function) component `short_prompts_never_trigger_echo_rejection [function]` (`4c468d6c-dbd7-5fdf-8544-ae463a85b5e7`) lines 272-275 [crates/gcode/src/commands/codewiki/text.rs:272-275]
  - Signature: `fn short_prompts_never_trigger_echo_rejection() {`
  - Purpose: Asserts that 'is_prompt_echo("Short prompt.", prompt)' returns 'false' when 'prompt' is exactly the short string '"Short prompt."'. [crates/gcode/src/commands/codewiki/text.rs:272-275]
- `transport_failure` (function) component `transport_failure [function]` (`8797dcbf-4983-5b9b-8aaf-233a45647f07`) lines 277-283 [crates/gcode/src/commands/codewiki/text.rs:277-283]
  - Signature: `fn transport_failure() -> AiError {`
  - Purpose: Returns an 'AiError::TransportFailure' with 'status' and 'body' set to 'None' and 'source' set to '"connection reset"'. [crates/gcode/src/commands/codewiki/text.rs:277-283]
- `bounded_retry_recovers_from_transient_transport_failure` (function) component `bounded_retry_recovers_from_transient_transport_failure [function]` (`217a697b-84e4-516f-9a0e-6fde2af5c1c3`) lines 286-299 [crates/gcode/src/commands/codewiki/text.rs:286-299]
  - Signature: `fn bounded_retry_recovers_from_transient_transport_failure() {`
  - Purpose: Verifies that 'generate_with_bounded_retry' retries once after an initial transient transport failure and then returns the successful '"generated"' result on the second call. [crates/gcode/src/commands/codewiki/text.rs:286-299]
- `bounded_retry_gives_up_after_bounded_attempts` (function) component `bounded_retry_gives_up_after_bounded_attempts [function]` (`b9d15450-b4dc-5d19-baf7-59e19f7b2165`) lines 302-311 [crates/gcode/src/commands/codewiki/text.rs:302-311]
  - Signature: `fn bounded_retry_gives_up_after_bounded_attempts() {`
  - Purpose: Verifies that 'generate_with_bounded_retry' stops after the configured number of retries by returning an error and invoking the closure exactly '1 + GENERATION_RETRY_BACKOFF.len()' times. [crates/gcode/src/commands/codewiki/text.rs:302-311]
- `bounded_retry_fails_fast_on_non_transient_errors` (function) component `bounded_retry_fails_fast_on_non_transient_errors [function]` (`1aa3c17f-bd7c-57ec-8785-c01a7f958014`) lines 314-326 [crates/gcode/src/commands/codewiki/text.rs:314-326]
  - Signature: `fn bounded_retry_fails_fast_on_non_transient_errors() {`
  - Purpose: Verifies that 'generate_with_bounded_retry' does not retry and returns an error immediately when the closure yields a non-transient 'AiError::NotConfigured', by asserting it is called exactly once. [crates/gcode/src/commands/codewiki/text.rs:314-326]

