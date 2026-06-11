---
title: crates/gcode/src/commands/codewiki/text.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 15-27
  - 30-33
  - 35-83
  - 88-102
  - 104-112
  - 114-130
  - 137-141
  - 143-160
  - 144-146
  - 150-159
  - 162-176
  - 185-195
  - 197-200
  - 202-217
  - 219-228
  - 230-242
  - 244-250
  - 252-254
  - 256-265
  - 276-297
  - 299-305
  - 307-327
  - 329-341
  - 343-352
  - 354-360
  - 365-378
  - 380-396
  - 398-424
  - 426-443
  - 445-458
  - 461-463
  - 467-518
  - 524-530
  - 533-553
  - 556-568
  - 571-584
  - 587-600
  - 603-618
  - 621-628
  - 631-663
  - 666-669
  - 671-677
  - 680-693
  - 696-705
  - 708-720
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/text.rs` exposes 45 indexed API symbols.
[crates/gcode/src/commands/codewiki/text.rs:15-27]
[crates/gcode/src/commands/codewiki/text.rs:30-33]
[crates/gcode/src/commands/codewiki/text.rs:35-83]
[crates/gcode/src/commands/codewiki/text.rs:88-102]
[crates/gcode/src/commands/codewiki/text.rs:104-112]

## API Symbols

- `Frontmatter` (class) component `Frontmatter [class]` (`eae0ca11-c8fa-584f-b3b2-e66838546e27`) lines 15-27 [crates/gcode/src/commands/codewiki/text.rs:15-27]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: A generic struct storing serializable document metadata that tracks provenance, content type, quality indicators (trust/freshness), and optional degradation status. [crates/gcode/src/commands/codewiki/text.rs:15-27]
- `FrontmatterSourceFile` (class) component `FrontmatterSourceFile [class]` (`c1009587-d58e-5878-977d-ce6795a0e388`) lines 30-33 [crates/gcode/src/commands/codewiki/text.rs:30-33]
  - Signature: `struct FrontmatterSourceFile<'a> {`
  - Purpose: A lifetime-parameterized struct that pairs a borrowed string reference to source file content with a vector of string-based range identifiers. [crates/gcode/src/commands/codewiki/text.rs:30-33]
- `resolve_text_generator` (function) component `resolve_text_generator [function]` (`e9ad9673-1e08-554b-aaf6-c0c78aab209e`) lines 35-83 [crates/gcode/src/commands/codewiki/text.rs:35-83]
  - Signature: `pub(crate) fn resolve_text_generator(`
  - Purpose: # Summary

Returns an optional boxed closure that performs AI-driven text generation with configurable routing strategy (daemon or direct) and tier-dependent prompt profiling, with graceful error handling. [crates/gcode/src/commands/codewiki/text.rs:35-83]
- `generate_with_bounded_retry` (function) component `generate_with_bounded_retry [function]` (`138df8dd-5300-5989-a3df-f581bf4df188`) lines 88-102 [crates/gcode/src/commands/codewiki/text.rs:88-102]
  - Signature: `pub(crate) fn generate_with_bounded_retry<T>(`
  - Purpose: Retries a provided fallible function across exponential backoff intervals, terminating on success or non-retryable errors. [crates/gcode/src/commands/codewiki/text.rs:88-102]
- `retryable_generation_error` (function) component `retryable_generation_error [function]` (`75d86435-692c-595e-acb3-bbf5fcecad51`) lines 104-112 [crates/gcode/src/commands/codewiki/text.rs:104-112]
  - Signature: `fn retryable_generation_error(error: &AiError) -> bool {`
  - Purpose: Returns `true` for transient AI errors (transport failures, rate-limiting, and 5xx HTTP status codes) and `false` for permanent errors (capability unavailable, misconfiguration, and parse failures). [crates/gcode/src/commands/codewiki/text.rs:104-112]
- `resolve_ai_context` (function) component `resolve_ai_context [function]` (`249984a8-522d-5c7d-b5f7-df1dbb07c6d5`) lines 114-130 [crates/gcode/src/commands/codewiki/text.rs:114-130]
  - Signature: `pub(crate) fn resolve_ai_context(`
  - Purpose: Resolves an `AiContext` by combining PostgreSQL-backed and optional standalone AI configurations with an optional routing override for the given project. [crates/gcode/src/commands/codewiki/text.rs:114-130]
- `Generation` (type) component `Generation [type]` (`099f9834-1687-550f-88dc-d7924d0f08a4`) lines 137-141 [crates/gcode/src/commands/codewiki/text.rs:137-141]
  - Signature: `pub(crate) enum Generation {`
  - Purpose: Indexed type `Generation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:137-141]
- `Generation` (class) component `Generation [class]` (`aada1d46-2c07-55dd-b2cc-e8e1046d56a8`) lines 143-160 [crates/gcode/src/commands/codewiki/text.rs:143-160]
  - Signature: `impl Generation {`
  - Purpose: `Generation` implements failure checking and fallback-based unwrapping with degradation flagging for a text generation enum that handles three states: successful generation, skipped generation, and generation failure. [crates/gcode/src/commands/codewiki/text.rs:143-160]
- `Generation.failed` (method) component `Generation.failed [method]` (`c0baa214-5d65-5c7d-9a87-1d3628be8672`) lines 144-146 [crates/gcode/src/commands/codewiki/text.rs:144-146]
  - Signature: `pub(crate) fn failed(&self) -> bool {`
  - Purpose: Returns `true` if the `Generation` enum variant is `Failed`, otherwise `false`. [crates/gcode/src/commands/codewiki/text.rs:144-146]
- `Generation.unwrap_or_record` (method) component `Generation.unwrap_or_record [method]` (`7ef3ec93-f03b-5705-9e6e-1fa87393bd59`) lines 150-159 [crates/gcode/src/commands/codewiki/text.rs:150-159]
  - Signature: `pub(crate) fn unwrap_or_record(self, fallback: String, degraded: &mut bool) -> String {`
  - Purpose: Unwraps a `Generation` enum, returning the generated text on success or a fallback string while setting the degraded flag only on generation failure. [crates/gcode/src/commands/codewiki/text.rs:150-159]
- `maybe_generate` (function) component `maybe_generate [function]` (`b51d9bf1-bef5-5f15-8fd0-0ee4e702df71`) lines 162-176 [crates/gcode/src/commands/codewiki/text.rs:162-176]
  - Signature: `pub(crate) fn maybe_generate(`
  - Purpose: Invokes an optional TextGenerator with the provided prompt, system instruction, and tier, returning `Generation::Skipped` if unavailable, `Generation::Failed` if generation fails or echoes the prompt, or `Generation::Generated(text)` upon success. [crates/gcode/src/commands/codewiki/text.rs:162-176]
- `is_prompt_echo` (function) component `is_prompt_echo [function]` (`cb64ebc3-49b9-5264-8664-9350c69d626d`) lines 185-195 [crates/gcode/src/commands/codewiki/text.rs:185-195]
  - Signature: `pub(crate) fn is_prompt_echo(text: &str, prompt: &str) -> bool {`
  - Purpose: Checks if the trimmed text starts with a prefix of the first `PROMPT_ECHO_PREFIX_CHARS` characters from the trimmed prompt. [crates/gcode/src/commands/codewiki/text.rs:185-195]
- `clean_generated` (function) component `clean_generated [function]` (`a2e82610-1662-504c-92c4-40dfd9e7cc1e`) lines 197-200 [crates/gcode/src/commands/codewiki/text.rs:197-200]
  - Signature: `pub(crate) fn clean_generated(text: String) -> Option<String> {`
  - Purpose: Trims whitespace from the input string and returns `Some(String)` if the result is non-empty, otherwise `None`. [crates/gcode/src/commands/codewiki/text.rs:197-200]
- `structural_symbol_purpose` (function) component `structural_symbol_purpose [function]` (`7eb4bf51-87f3-5167-aff7-e96f1a764a2e`) lines 202-217 [crates/gcode/src/commands/codewiki/text.rs:202-217]
  - Signature: `pub(crate) fn structural_symbol_purpose(symbol: &Symbol) -> String {`
  - Purpose: Returns a symbol's purpose string by prioritizing its non-empty summary, then docstring, and falling back to a formatted description containing the symbol's kind, qualified name, and file path. [crates/gcode/src/commands/codewiki/text.rs:202-217]
- `structural_file_summary` (function) component `structural_file_summary [function]` (`03c5c769-a004-5bd6-bdde-054f7bc89ca4`) lines 219-228 [crates/gcode/src/commands/codewiki/text.rs:219-228]
  - Signature: `pub(crate) fn structural_file_summary(file: &str, symbols: &[SymbolDoc]) -> String {`
  - Purpose: Returns a formatted string that reports the count of indexed API symbols exposed by a specified file, or indicates no symbols if the list is empty. [crates/gcode/src/commands/codewiki/text.rs:219-228]
- `structural_module_summary` (function) component `structural_module_summary [function]` (`290bba2b-63a2-5f6e-bee3-edb6d2298882`) lines 230-242 [crates/gcode/src/commands/codewiki/text.rs:230-242]
  - Signature: `pub(crate) fn structural_module_summary(`
  - Purpose: Generates a formatted string that reports the count of direct files and child modules contained within a specified module. [crates/gcode/src/commands/codewiki/text.rs:230-242]
- `structural_repo_summary` (function) component `structural_repo_summary [function]` (`cc78ad52-51a2-5a13-959d-8b3d905a190f`) lines 244-250 [crates/gcode/src/commands/codewiki/text.rs:244-250]
  - Signature: `pub(crate) fn structural_repo_summary(file_count: usize, module_count: usize) -> String {`
  - Purpose: This function constructs a formatted String describing repository structure by interpolating file and module counts with grammatically correct plural suffixes. [crates/gcode/src/commands/codewiki/text.rs:244-250]
- `write_section` (function) component `write_section [function]` (`125cf2c8-09cf-5e14-9f18-e315f6c382e0`) lines 252-254 [crates/gcode/src/commands/codewiki/text.rs:252-254]
  - Signature: `pub(crate) fn write_section(doc: &mut String, heading: &str, body: &str) {`
  - Purpose: Appends a Markdown level-2 section header followed by trimmed body text to a mutable string. [crates/gcode/src/commands/codewiki/text.rs:252-254]
- `collect_link_spans` (function) component `collect_link_spans [function]` (`0774440a-f6df-56f9-bd96-570928ef6657`) lines 256-265 [crates/gcode/src/commands/codewiki/text.rs:256-265]
  - Signature: `pub(crate) fn collect_link_spans(files: &[FileLink], modules: &[ModuleLink]) -> Vec<SourceSpan> {`
  - Purpose: Collects source spans from FileLink and ModuleLink slices, deduplicates them via BTreeSet, and returns the sorted result as a Vec. [crates/gcode/src/commands/codewiki/text.rs:256-265]
- `fallback_spans` (function) component `fallback_spans [function]` (`4e79fcb8-c575-5773-9567-b3dd6b3ad877`) lines 276-297 [crates/gcode/src/commands/codewiki/text.rs:276-297]
  - Signature: `fn fallback_spans(spans: &[SourceSpan]) -> Vec<SourceSpan> {`
  - Purpose: Deduplicates source spans and returns up to `MAX_FALLBACK_CITATIONS` selections, prioritizing one representative span per unique source file before filling remaining slots. [crates/gcode/src/commands/codewiki/text.rs:276-297]
- `citation_list` (function) component `citation_list [function]` (`40c4ed28-c0aa-5148-b4a6-e62c82174ef8`) lines 299-305 [crates/gcode/src/commands/codewiki/text.rs:299-305]
  - Signature: `pub(crate) fn citation_list(spans: &[SourceSpan]) -> String {`
  - Purpose: Transforms a slice of SourceSpans into a newline-delimited String of citations after applying fallback span resolution. [crates/gcode/src/commands/codewiki/text.rs:299-305]
- `wrap_citation_items` (function) component `wrap_citation_items [function]` (`e6eb617b-872e-589f-bbeb-c5780c06ed6d`) lines 307-327 [crates/gcode/src/commands/codewiki/text.rs:307-327]
  - Signature: `fn wrap_citation_items<I>(items: I, max_line_width: usize) -> String`
  - Purpose: Indexed function `wrap_citation_items` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:307-327]
- `citation_markers` (function) component `citation_markers [function]` (`972ee894-54a7-51b6-af6d-11d71473953e`) lines 329-341 [crates/gcode/src/commands/codewiki/text.rs:329-341]
  - Signature: `pub(crate) fn citation_markers(spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `citation_markers` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:329-341]
- `citation_references` (function) component `citation_references [function]` (`09baee22-3bd1-5013-8675-b87154a00379`) lines 343-352 [crates/gcode/src/commands/codewiki/text.rs:343-352]
  - Signature: `fn citation_references(spans: &[SourceSpan]) -> Vec<(usize, String)> {`
  - Purpose: Indexed function `citation_references` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:343-352]
- `replace_citations_with_markers` (function) component `replace_citations_with_markers [function]` (`1bc16305-c41f-56f9-948b-d62cfe3a18e1`) lines 354-360 [crates/gcode/src/commands/codewiki/text.rs:354-360]
  - Signature: `pub(crate) fn replace_citations_with_markers(text: &str, spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `replace_citations_with_markers` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:354-360]
- `write_references` (function) component `write_references [function]` (`4a017ef1-97e7-5a04-a7ee-512c9a0c2fbe`) lines 365-378 [crates/gcode/src/commands/codewiki/text.rs:365-378]
  - Signature: `pub(crate) fn write_references(doc: &mut String, spans: &[SourceSpan]) {`
  - Purpose: Indexed function `write_references` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:365-378]
- `ground_text` (function) component `ground_text [function]` (`0fa1a27b-0c9a-5b2d-addb-540f3f746f0e`) lines 380-396 [crates/gcode/src/commands/codewiki/text.rs:380-396]
  - Signature: `pub(crate) fn ground_text(`
  - Purpose: Indexed function `ground_text` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:380-396]
- `strip_invalid_citations` (function) component `strip_invalid_citations [function]` (`8bd10d41-b3d8-54b4-9a63-b3a37ab195b9`) lines 398-424 [crates/gcode/src/commands/codewiki/text.rs:398-424]
  - Signature: `pub(crate) fn strip_invalid_citations(text: &str, valid_spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `strip_invalid_citations` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:398-424]
- `contains_valid_citation` (function) component `contains_valid_citation [function]` (`0644798e-c3f2-5a9f-be8e-1e81d392c04c`) lines 426-443 [crates/gcode/src/commands/codewiki/text.rs:426-443]
  - Signature: `pub(crate) fn contains_valid_citation(text: &str, valid_spans: &[SourceSpan]) -> bool {`
  - Purpose: Indexed function `contains_valid_citation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:426-443]
- `citation_parts` (function) component `citation_parts [function]` (`b67fd401-e487-514e-ae91-4557fb67c28b`) lines 445-458 [crates/gcode/src/commands/codewiki/text.rs:445-458]
  - Signature: `pub(crate) fn citation_parts(value: &str) -> Option<(&str, usize, usize)> {`
  - Purpose: Indexed function `citation_parts` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:445-458]
- `frontmatter` (function) component `frontmatter [function]` (`69f4fe63-c10a-5121-a8d6-a232ba1be7ec`) lines 461-463 [crates/gcode/src/commands/codewiki/text.rs:461-463]
  - Signature: `pub(crate) fn frontmatter(title: &str, kind: &str, source_spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `frontmatter` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:461-463]
- `frontmatter_with_degradation` (function) component `frontmatter_with_degradation [function]` (`214e0be7-f57d-5472-b6ad-61ccef3b0788`) lines 467-518 [crates/gcode/src/commands/codewiki/text.rs:467-518]
  - Signature: `pub(crate) fn frontmatter_with_degradation(`
  - Purpose: Indexed function `frontmatter_with_degradation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:467-518]
- `span` (function) component `span [function]` (`900b7579-ff41-52ba-858e-6948ee59a980`) lines 524-530 [crates/gcode/src/commands/codewiki/text.rs:524-530]
  - Signature: `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {`
  - Purpose: Indexed function `span` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:524-530]
- `citation_list_emits_one_fallback_range_per_line` (function) component `citation_list_emits_one_fallback_range_per_line [function]` (`37a7c69f-ebf7-5d23-9799-a644761d8661`) lines 533-553 [crates/gcode/src/commands/codewiki/text.rs:533-553]
  - Signature: `fn citation_list_emits_one_fallback_range_per_line() {`
  - Purpose: Indexed function `citation_list_emits_one_fallback_range_per_line` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:533-553]
- `citation_list_caps_oversized_span_sets` (function) component `citation_list_caps_oversized_span_sets [function]` (`afffc235-fc7f-52d0-a4d6-ea7cfe775618`) lines 556-568 [crates/gcode/src/commands/codewiki/text.rs:556-568]
  - Signature: `fn citation_list_caps_oversized_span_sets() {`
  - Purpose: Indexed function `citation_list_caps_oversized_span_sets` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:556-568]
- `fallback_spans_prefer_distinct_files_over_one_files_span_run` (function) component `fallback_spans_prefer_distinct_files_over_one_files_span_run [function]` (`80d12a0e-eb40-5c42-92bc-4cecaaec23f7`) lines 571-584 [crates/gcode/src/commands/codewiki/text.rs:571-584]
  - Signature: `fn fallback_spans_prefer_distinct_files_over_one_files_span_run() {`
  - Purpose: Indexed function `fallback_spans_prefer_distinct_files_over_one_files_span_run` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:571-584]
- `citation_markers_are_capped_and_keep_reference_numbering` (function) component `citation_markers_are_capped_and_keep_reference_numbering [function]` (`3be1e97d-74a8-5cab-9a27-963c7d575e50`) lines 587-600 [crates/gcode/src/commands/codewiki/text.rs:587-600]
  - Signature: `fn citation_markers_are_capped_and_keep_reference_numbering() {`
  - Purpose: Indexed function `citation_markers_are_capped_and_keep_reference_numbering` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:587-600]
- `references_resolve_only_markers_present_in_doc` (function) component `references_resolve_only_markers_present_in_doc [function]` (`7897d31f-5683-55ff-8a12-e07b0d42d40f`) lines 603-618 [crates/gcode/src/commands/codewiki/text.rs:603-618]
  - Signature: `fn references_resolve_only_markers_present_in_doc() {`
  - Purpose: Indexed function `references_resolve_only_markers_present_in_doc` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:603-618]
- `wrap_citation_items_bounds_line_width` (function) component `wrap_citation_items_bounds_line_width [function]` (`f576f0ea-b6cd-5027-83f0-acc2123d5b24`) lines 621-628 [crates/gcode/src/commands/codewiki/text.rs:621-628]
  - Signature: `fn wrap_citation_items_bounds_line_width() {`
  - Purpose: Indexed function `wrap_citation_items_bounds_line_width` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:621-628]
- `prompt_echo_is_rejected_as_failed_generation` (function) component `prompt_echo_is_rejected_as_failed_generation [function]` (`e0ab63e6-70d9-5dcd-b798-d7d9490d8bdd`) lines 631-663 [crates/gcode/src/commands/codewiki/text.rs:631-663]
  - Signature: `fn prompt_echo_is_rejected_as_failed_generation() {`
  - Purpose: Indexed function `prompt_echo_is_rejected_as_failed_generation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:631-663]
- `short_prompts_never_trigger_echo_rejection` (function) component `short_prompts_never_trigger_echo_rejection [function]` (`71b3a9d5-2017-5d49-9774-c439dfdeecbd`) lines 666-669 [crates/gcode/src/commands/codewiki/text.rs:666-669]
  - Signature: `fn short_prompts_never_trigger_echo_rejection() {`
  - Purpose: Indexed function `short_prompts_never_trigger_echo_rejection` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:666-669]
- `transport_failure` (function) component `transport_failure [function]` (`c7d4109b-7136-57fc-bf3f-836d5ec9c494`) lines 671-677 [crates/gcode/src/commands/codewiki/text.rs:671-677]
  - Signature: `fn transport_failure() -> AiError {`
  - Purpose: Indexed function `transport_failure` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:671-677]
- `bounded_retry_recovers_from_transient_transport_failure` (function) component `bounded_retry_recovers_from_transient_transport_failure [function]` (`b2cec2ca-54fc-5ba1-aa5d-36a03c9e5cd4`) lines 680-693 [crates/gcode/src/commands/codewiki/text.rs:680-693]
  - Signature: `fn bounded_retry_recovers_from_transient_transport_failure() {`
  - Purpose: Indexed function `bounded_retry_recovers_from_transient_transport_failure` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:680-693]
- `bounded_retry_gives_up_after_bounded_attempts` (function) component `bounded_retry_gives_up_after_bounded_attempts [function]` (`747851bf-ba82-534f-9de5-370a33d70668`) lines 696-705 [crates/gcode/src/commands/codewiki/text.rs:696-705]
  - Signature: `fn bounded_retry_gives_up_after_bounded_attempts() {`
  - Purpose: Indexed function `bounded_retry_gives_up_after_bounded_attempts` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:696-705]
- `bounded_retry_fails_fast_on_non_transient_errors` (function) component `bounded_retry_fails_fast_on_non_transient_errors [function]` (`0c0335fa-e3fc-51f5-b47d-f7ae99a39e42`) lines 708-720 [crates/gcode/src/commands/codewiki/text.rs:708-720]
  - Signature: `fn bounded_retry_fails_fast_on_non_transient_errors() {`
  - Purpose: Indexed function `bounded_retry_fails_fast_on_non_transient_errors` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:708-720]

