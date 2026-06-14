---
title: crates/gcode/src/commands/codewiki/text.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 18-32
  - 35-39
  - 41-89
  - 94-108
  - 110-118
  - 120-136
  - 143-147
  - 149-166
  - 168-182
  - 191-201
  - 203-206
  - 208-223
  - 225-234
  - 239-242
  - 244-256
  - 258-264
  - 266-268
  - 270-279
  - 303-311
  - 315-321
  - 323-328
  - 335-375
  - 377-383
  - 385-405
  - 407-419
  - 421-430
  - 432-438
  - 443-456
  - 458-474
  - 476-502
  - 504-521
  - 523-536
  - 539-541
  - 545-552
  - 554-561
  - 563-630
  - 632-656
  - 662-668
  - 671-690
  - 693-713
  - 716-728
  - 731-744
  - 747-760
  - 763-773
  - 776-787
  - 790-822
  - 825-840
  - 843-850
  - 853-886
  - 889-892
  - 894-900
  - 903-916
  - 919-928
  - 931-943
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Provides the text-generation and citation-grounding pipeline for codewiki output. It resolves an AI text generator from the current routing, retries transient generation failures with bounded backoff, detects prompt-echo failures, and sanitizes generated text before returning it.

The rest of the file builds the document structure around that output: it serializes frontmatter with provenance, degradation, and truncation metadata; computes structural summaries and fallback citation spans; emits citation markers, references, and wrapping within line-width limits; and includes tests covering provenance coalescing, citation ranking/capping, asset-file handling, and retry behavior.
[crates/gcode/src/commands/codewiki/text.rs:18-32]
[crates/gcode/src/commands/codewiki/text.rs:35-39]
[crates/gcode/src/commands/codewiki/text.rs:41-89]
[crates/gcode/src/commands/codewiki/text.rs:94-108]
[crates/gcode/src/commands/codewiki/text.rs:110-118]

## API Symbols

- `Frontmatter` (class) component `Frontmatter [class]` (`70d27c9e-91e5-5027-af65-007cbd41eb95`) lines 18-32 [crates/gcode/src/commands/codewiki/text.rs:18-32]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: Indexed class `Frontmatter` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:18-32]
- `FrontmatterSourceFile` (class) component `FrontmatterSourceFile [class]` (`7b3c6d04-93db-5fda-bbfb-9fd57e5f9fba`) lines 35-39 [crates/gcode/src/commands/codewiki/text.rs:35-39]
  - Signature: `struct FrontmatterSourceFile<'a> {`
  - Purpose: Indexed class `FrontmatterSourceFile` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:35-39]
- `resolve_text_generator` (function) component `resolve_text_generator [function]` (`60556538-4dd8-5007-b9f9-b71962ac8b85`) lines 41-89 [crates/gcode/src/commands/codewiki/text.rs:41-89]
  - Signature: `pub(crate) fn resolve_text_generator(`
  - Purpose: Indexed function `resolve_text_generator` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:41-89]
- `generate_with_bounded_retry` (function) component `generate_with_bounded_retry [function]` (`a3303708-f5eb-579c-8889-395203d1ef18`) lines 94-108 [crates/gcode/src/commands/codewiki/text.rs:94-108]
  - Signature: `pub(crate) fn generate_with_bounded_retry<T>(`
  - Purpose: Indexed function `generate_with_bounded_retry` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:94-108]
- `retryable_generation_error` (function) component `retryable_generation_error [function]` (`c4b2a34d-4e61-5fab-85f3-84e7f283ada9`) lines 110-118 [crates/gcode/src/commands/codewiki/text.rs:110-118]
  - Signature: `fn retryable_generation_error(error: &AiError) -> bool {`
  - Purpose: Indexed function `retryable_generation_error` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:110-118]
- `resolve_ai_context` (function) component `resolve_ai_context [function]` (`44a31795-e989-5481-94dd-8656b8715981`) lines 120-136 [crates/gcode/src/commands/codewiki/text.rs:120-136]
  - Signature: `pub(crate) fn resolve_ai_context(`
  - Purpose: Indexed function `resolve_ai_context` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:120-136]
- `Generation` (type) component `Generation [type]` (`0aa2407e-d7dc-5fae-b6f3-6c83090d7ceb`) lines 143-147 [crates/gcode/src/commands/codewiki/text.rs:143-147]
  - Signature: `pub(crate) enum Generation {`
  - Purpose: Indexed type `Generation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:143-147]
- `Generation` (class) component `Generation [class]` (`abc0cfbd-901c-5816-aa5b-8b89ecfb0b3d`) lines 149-166 [crates/gcode/src/commands/codewiki/text.rs:149-166]
  - Signature: `impl Generation {`
  - Purpose: Indexed class `Generation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:149-166]
- `Generation.failed` (method) component `Generation.failed [method]` (`b4d40701-420e-536d-8475-eb8b5aa14609`) lines 150-152 [crates/gcode/src/commands/codewiki/text.rs:150-152]
  - Signature: `pub(crate) fn failed(&self) -> bool {`
  - Purpose: Indexed method `Generation.failed` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:150-152]
- `Generation.unwrap_or_record` (method) component `Generation.unwrap_or_record [method]` (`6a96976b-15a7-59af-95dc-be35580a8157`) lines 156-165 [crates/gcode/src/commands/codewiki/text.rs:156-165]
  - Signature: `pub(crate) fn unwrap_or_record(self, fallback: String, degraded: &mut bool) -> String {`
  - Purpose: Indexed method `Generation.unwrap_or_record` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:156-165]
- `maybe_generate` (function) component `maybe_generate [function]` (`20be3d0a-783c-5091-80fe-51dfeb57c8b4`) lines 168-182 [crates/gcode/src/commands/codewiki/text.rs:168-182]
  - Signature: `pub(crate) fn maybe_generate(`
  - Purpose: Indexed function `maybe_generate` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:168-182]
- `is_prompt_echo` (function) component `is_prompt_echo [function]` (`5b034170-eb58-5289-b882-ee8b8995ccfd`) lines 191-201 [crates/gcode/src/commands/codewiki/text.rs:191-201]
  - Signature: `pub(crate) fn is_prompt_echo(text: &str, prompt: &str) -> bool {`
  - Purpose: Indexed function `is_prompt_echo` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:191-201]
- `clean_generated` (function) component `clean_generated [function]` (`3d19ff2f-28e4-5289-b85e-912dcfbba363`) lines 203-206 [crates/gcode/src/commands/codewiki/text.rs:203-206]
  - Signature: `pub(crate) fn clean_generated(text: String) -> Option<String> {`
  - Purpose: Indexed function `clean_generated` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:203-206]
- `structural_symbol_purpose` (function) component `structural_symbol_purpose [function]` (`c93d9602-c72b-51c1-842f-f10ab8059aac`) lines 208-223 [crates/gcode/src/commands/codewiki/text.rs:208-223]
  - Signature: `pub(crate) fn structural_symbol_purpose(symbol: &Symbol) -> String {`
  - Purpose: Indexed function `structural_symbol_purpose` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:208-223]
- `structural_file_summary` (function) component `structural_file_summary [function]` (`d4852aa7-7d1d-54fc-a7a8-1aea05dbac4e`) lines 225-234 [crates/gcode/src/commands/codewiki/text.rs:225-234]
  - Signature: `pub(crate) fn structural_file_summary(file: &str, symbols: &[SymbolDoc]) -> String {`
  - Purpose: Indexed function `structural_file_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:225-234]
- `display_child_summary` (function) component `display_child_summary [function]` (`826753a6-bf85-5737-8878-9232f02140e6`) lines 239-242 [crates/gcode/src/commands/codewiki/text.rs:239-242]
  - Signature: `pub(crate) fn display_child_summary(summary: &str, file: &str) -> Option<String> {`
  - Purpose: Indexed function `display_child_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:239-242]
- `structural_module_summary` (function) component `structural_module_summary [function]` (`abf80200-01ed-53d5-930c-df01093c7ecd`) lines 244-256 [crates/gcode/src/commands/codewiki/text.rs:244-256]
  - Signature: `pub(crate) fn structural_module_summary(`
  - Purpose: Indexed function `structural_module_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:244-256]
- `structural_repo_summary` (function) component `structural_repo_summary [function]` (`237bdbab-8ab9-5330-93b5-4ec8d42f2caf`) lines 258-264 [crates/gcode/src/commands/codewiki/text.rs:258-264]
  - Signature: `pub(crate) fn structural_repo_summary(file_count: usize, module_count: usize) -> String {`
  - Purpose: Indexed function `structural_repo_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:258-264]
- `write_section` (function) component `write_section [function]` (`0c72521d-6f0e-5ac2-9cf8-493ce1f9cff9`) lines 266-268 [crates/gcode/src/commands/codewiki/text.rs:266-268]
  - Signature: `pub(crate) fn write_section(doc: &mut String, heading: &str, body: &str) {`
  - Purpose: Indexed function `write_section` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:266-268]
- `collect_link_spans` (function) component `collect_link_spans [function]` (`f51f54af-3a0b-5c3a-aae9-d0aee54cdcf0`) lines 270-279 [crates/gcode/src/commands/codewiki/text.rs:270-279]
  - Signature: `pub(crate) fn collect_link_spans(files: &[FileLink], modules: &[ModuleLink]) -> Vec<SourceSpan> {`
  - Purpose: Indexed function `collect_link_spans` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:270-279]
- `is_asset_or_data_file` (function) component `is_asset_or_data_file [function]` (`20c5af58-c905-59cb-911a-f183685184e9`) lines 303-311 [crates/gcode/src/commands/codewiki/text.rs:303-311]
  - Signature: `fn is_asset_or_data_file(file: &str) -> bool {`
  - Purpose: Indexed function `is_asset_or_data_file` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:303-311]
- `lexical_tokens` (function) component `lexical_tokens [function]` (`bed50496-03bb-5db3-a42b-152f2dfc568c`) lines 315-321 [crates/gcode/src/commands/codewiki/text.rs:315-321]
  - Signature: `fn lexical_tokens(value: &str) -> BTreeSet<String> {`
  - Purpose: Indexed function `lexical_tokens` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:315-321]
- `citation_relevance` (function) component `citation_relevance [function]` (`7cecc22d-32b4-5c35-a5b9-c434a2c97bde`) lines 323-328 [crates/gcode/src/commands/codewiki/text.rs:323-328]
  - Signature: `fn citation_relevance(text_tokens: &BTreeSet<String>, file: &str) -> usize {`
  - Purpose: Indexed function `citation_relevance` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:323-328]
- `fallback_spans` (function) component `fallback_spans [function]` (`2e7d9dce-e017-558b-90e5-bafe7364263b`) lines 335-375 [crates/gcode/src/commands/codewiki/text.rs:335-375]
  - Signature: `fn fallback_spans(spans: &[SourceSpan], text: &str) -> Vec<SourceSpan> {`
  - Purpose: Indexed function `fallback_spans` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:335-375]
- `citation_list` (function) component `citation_list [function]` (`bea9be6a-0ed5-541e-b97d-c0f9dfea3eb1`) lines 377-383 [crates/gcode/src/commands/codewiki/text.rs:377-383]
  - Signature: `pub(crate) fn citation_list(spans: &[SourceSpan], text: &str) -> String {`
  - Purpose: Indexed function `citation_list` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:377-383]
- `wrap_citation_items` (function) component `wrap_citation_items [function]` (`9020efaa-77cf-579d-b341-268a8aba2211`) lines 385-405 [crates/gcode/src/commands/codewiki/text.rs:385-405]
  - Signature: `fn wrap_citation_items<I>(items: I, max_line_width: usize) -> String`
  - Purpose: Indexed function `wrap_citation_items` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:385-405]
- `citation_markers` (function) component `citation_markers [function]` (`f16fd9ef-77be-59d5-b73a-a520eccc7463`) lines 407-419 [crates/gcode/src/commands/codewiki/text.rs:407-419]
  - Signature: `pub(crate) fn citation_markers(spans: &[SourceSpan], text: &str) -> String {`
  - Purpose: Indexed function `citation_markers` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:407-419]
- `citation_references` (function) component `citation_references [function]` (`9220de91-1fd1-5899-9253-bab1776ede3d`) lines 421-430 [crates/gcode/src/commands/codewiki/text.rs:421-430]
  - Signature: `fn citation_references(spans: &[SourceSpan]) -> Vec<(usize, String)> {`
  - Purpose: Indexed function `citation_references` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:421-430]
- `replace_citations_with_markers` (function) component `replace_citations_with_markers [function]` (`cf380792-cd80-5189-b3a0-5bece0b90854`) lines 432-438 [crates/gcode/src/commands/codewiki/text.rs:432-438]
  - Signature: `pub(crate) fn replace_citations_with_markers(text: &str, spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `replace_citations_with_markers` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:432-438]
- `write_references` (function) component `write_references [function]` (`63df8e5e-833b-54ff-9205-d50d9ee87d05`) lines 443-456 [crates/gcode/src/commands/codewiki/text.rs:443-456]
  - Signature: `pub(crate) fn write_references(doc: &mut String, spans: &[SourceSpan]) {`
  - Purpose: Indexed function `write_references` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:443-456]
- `ground_text` (function) component `ground_text [function]` (`0c3c0665-ca87-520d-91c3-e67e6d760e3e`) lines 458-474 [crates/gcode/src/commands/codewiki/text.rs:458-474]
  - Signature: `pub(crate) fn ground_text(`
  - Purpose: Indexed function `ground_text` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:458-474]
- `strip_invalid_citations` (function) component `strip_invalid_citations [function]` (`6cd166ff-9928-5901-91a6-59dff8b908e3`) lines 476-502 [crates/gcode/src/commands/codewiki/text.rs:476-502]
  - Signature: `pub(crate) fn strip_invalid_citations(text: &str, valid_spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `strip_invalid_citations` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:476-502]
- `contains_valid_citation` (function) component `contains_valid_citation [function]` (`dea54e31-468f-5014-ab03-07982e80d172`) lines 504-521 [crates/gcode/src/commands/codewiki/text.rs:504-521]
  - Signature: `pub(crate) fn contains_valid_citation(text: &str, valid_spans: &[SourceSpan]) -> bool {`
  - Purpose: Indexed function `contains_valid_citation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:504-521]
- `citation_parts` (function) component `citation_parts [function]` (`d23186e5-3c2c-5b90-a2eb-b104de1004a4`) lines 523-536 [crates/gcode/src/commands/codewiki/text.rs:523-536]
  - Signature: `pub(crate) fn citation_parts(value: &str) -> Option<(&str, usize, usize)> {`
  - Purpose: Indexed function `citation_parts` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:523-536]
- `frontmatter` (function) component `frontmatter [function]` (`f2213013-83d6-5e0d-b0c2-2f7d395ac0fa`) lines 539-541 [crates/gcode/src/commands/codewiki/text.rs:539-541]
  - Signature: `pub(crate) fn frontmatter(title: &str, kind: &str, source_spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `frontmatter` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:539-541]
- `frontmatter_with_degradation` (function) component `frontmatter_with_degradation [function]` (`bf2e3709-b7d2-5007-aaea-874370ed65c8`) lines 545-552 [crates/gcode/src/commands/codewiki/text.rs:545-552]
  - Signature: `pub(crate) fn frontmatter_with_degradation(`
  - Purpose: Indexed function `frontmatter_with_degradation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:545-552]
- `frontmatter_with_degradation_without_ranges` (function) component `frontmatter_with_degradation_without_ranges [function]` (`9b59fac5-35fa-5d34-98ac-cbc282c5c41b`) lines 554-561 [crates/gcode/src/commands/codewiki/text.rs:554-561]
  - Signature: `pub(crate) fn frontmatter_with_degradation_without_ranges(`
  - Purpose: Indexed function `frontmatter_with_degradation_without_ranges` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:554-561]
- `frontmatter_with_options` (function) component `frontmatter_with_options [function]` (`82c65b8d-81b1-5198-b011-95ce2674e8f3`) lines 563-630 [crates/gcode/src/commands/codewiki/text.rs:563-630]
  - Signature: `fn frontmatter_with_options(`
  - Purpose: Indexed function `frontmatter_with_options` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:563-630]
- `format_frontmatter_ranges` (function) component `format_frontmatter_ranges [function]` (`bde7b8c9-185f-58c5-8fa0-092a251de2dd`) lines 632-656 [crates/gcode/src/commands/codewiki/text.rs:632-656]
  - Signature: `fn format_frontmatter_ranges(ranges: BTreeSet<(usize, usize)>) -> Vec<String> {`
  - Purpose: Indexed function `format_frontmatter_ranges` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:632-656]
- `span` (function) component `span [function]` (`79b102e6-70e2-587e-8983-e545855e8178`) lines 662-668 [crates/gcode/src/commands/codewiki/text.rs:662-668]
  - Signature: `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {`
  - Purpose: Indexed function `span` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:662-668]
- `frontmatter_coalesces_contiguous_provenance_ranges` (function) component `frontmatter_coalesces_contiguous_provenance_ranges [function]` (`5f4d51e3-8117-5689-8737-6b48b05eed5b`) lines 671-690 [crates/gcode/src/commands/codewiki/text.rs:671-690]
  - Signature: `fn frontmatter_coalesces_contiguous_provenance_ranges() {`
  - Purpose: Indexed function `frontmatter_coalesces_contiguous_provenance_ranges` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:671-690]
- `citation_list_emits_one_fallback_range_per_line` (function) component `citation_list_emits_one_fallback_range_per_line [function]` (`e3ddd4ae-d8c5-54ea-ad92-cc6c04ddc55e`) lines 693-713 [crates/gcode/src/commands/codewiki/text.rs:693-713]
  - Signature: `fn citation_list_emits_one_fallback_range_per_line() {`
  - Purpose: Indexed function `citation_list_emits_one_fallback_range_per_line` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:693-713]
- `citation_list_caps_oversized_span_sets` (function) component `citation_list_caps_oversized_span_sets [function]` (`ad203f44-05ee-5bed-9ed9-7349fba80606`) lines 716-728 [crates/gcode/src/commands/codewiki/text.rs:716-728]
  - Signature: `fn citation_list_caps_oversized_span_sets() {`
  - Purpose: Indexed function `citation_list_caps_oversized_span_sets` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:716-728]
- `fallback_spans_prefer_distinct_files_over_one_files_span_run` (function) component `fallback_spans_prefer_distinct_files_over_one_files_span_run [function]` (`4ce0bbc2-8c41-51e3-bd2e-56be2d46d4f6`) lines 731-744 [crates/gcode/src/commands/codewiki/text.rs:731-744]
  - Signature: `fn fallback_spans_prefer_distinct_files_over_one_files_span_run() {`
  - Purpose: Indexed function `fallback_spans_prefer_distinct_files_over_one_files_span_run` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:731-744]
- `citation_markers_are_capped_and_keep_reference_numbering` (function) component `citation_markers_are_capped_and_keep_reference_numbering [function]` (`ee2204e7-a0aa-5a02-8104-7c2f8e00c3b2`) lines 747-760 [crates/gcode/src/commands/codewiki/text.rs:747-760]
  - Signature: `fn citation_markers_are_capped_and_keep_reference_numbering() {`
  - Purpose: Indexed function `citation_markers_are_capped_and_keep_reference_numbering` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:747-760]
- `fallback_citations_rank_lexically_relevant_files_first` (function) component `fallback_citations_rank_lexically_relevant_files_first [function]` (`11f49d8b-0cfd-5c49-b009-a2141fb61a2f`) lines 763-773 [crates/gcode/src/commands/codewiki/text.rs:763-773]
  - Signature: `fn fallback_citations_rank_lexically_relevant_files_first() {`
  - Purpose: Indexed function `fallback_citations_rank_lexically_relevant_files_first` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:763-773]
- `asset_data_files_rank_behind_source_unless_sole_provenance` (function) component `asset_data_files_rank_behind_source_unless_sole_provenance [function]` (`5c66940a-4ee7-5543-a93e-4df28438ad01`) lines 776-787 [crates/gcode/src/commands/codewiki/text.rs:776-787]
  - Signature: `fn asset_data_files_rank_behind_source_unless_sole_provenance() {`
  - Purpose: Indexed function `asset_data_files_rank_behind_source_unless_sole_provenance` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:776-787]
- `frontmatter_caps_provenance_and_records_truncation` (function) component `frontmatter_caps_provenance_and_records_truncation [function]` (`1380b187-b9be-5a8e-9d33-94bf69a6b979`) lines 790-822 [crates/gcode/src/commands/codewiki/text.rs:790-822]
  - Signature: `fn frontmatter_caps_provenance_and_records_truncation() {`
  - Purpose: Indexed function `frontmatter_caps_provenance_and_records_truncation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:790-822]
- `references_resolve_only_markers_present_in_doc` (function) component `references_resolve_only_markers_present_in_doc [function]` (`f0b4757d-f694-5900-8e37-94d875dd584e`) lines 825-840 [crates/gcode/src/commands/codewiki/text.rs:825-840]
  - Signature: `fn references_resolve_only_markers_present_in_doc() {`
  - Purpose: Indexed function `references_resolve_only_markers_present_in_doc` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:825-840]
- `wrap_citation_items_bounds_line_width` (function) component `wrap_citation_items_bounds_line_width [function]` (`b6732f37-b441-59a3-996f-29edd572b030`) lines 843-850 [crates/gcode/src/commands/codewiki/text.rs:843-850]
  - Signature: `fn wrap_citation_items_bounds_line_width() {`
  - Purpose: Indexed function `wrap_citation_items_bounds_line_width` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:843-850]
- `prompt_echo_is_rejected_as_failed_generation` (function) component `prompt_echo_is_rejected_as_failed_generation [function]` (`729b4ad6-213c-5142-972a-f6ba7b1046c4`) lines 853-886 [crates/gcode/src/commands/codewiki/text.rs:853-886]
  - Signature: `fn prompt_echo_is_rejected_as_failed_generation() {`
  - Purpose: Indexed function `prompt_echo_is_rejected_as_failed_generation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:853-886]
- `short_prompts_never_trigger_echo_rejection` (function) component `short_prompts_never_trigger_echo_rejection [function]` (`80d78791-24c9-5923-b7e7-1266b5fcd982`) lines 889-892 [crates/gcode/src/commands/codewiki/text.rs:889-892]
  - Signature: `fn short_prompts_never_trigger_echo_rejection() {`
  - Purpose: Indexed function `short_prompts_never_trigger_echo_rejection` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:889-892]
- `transport_failure` (function) component `transport_failure [function]` (`25e0fcbe-8878-5172-8478-152037daff2c`) lines 894-900 [crates/gcode/src/commands/codewiki/text.rs:894-900]
  - Signature: `fn transport_failure() -> AiError {`
  - Purpose: Indexed function `transport_failure` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:894-900]
- `bounded_retry_recovers_from_transient_transport_failure` (function) component `bounded_retry_recovers_from_transient_transport_failure [function]` (`c91b7807-fba1-5bbf-9d77-63e2aef38c53`) lines 903-916 [crates/gcode/src/commands/codewiki/text.rs:903-916]
  - Signature: `fn bounded_retry_recovers_from_transient_transport_failure() {`
  - Purpose: Indexed function `bounded_retry_recovers_from_transient_transport_failure` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:903-916]
- `bounded_retry_gives_up_after_bounded_attempts` (function) component `bounded_retry_gives_up_after_bounded_attempts [function]` (`16c53d91-6fbf-5921-96ff-85583dc4317c`) lines 919-928 [crates/gcode/src/commands/codewiki/text.rs:919-928]
  - Signature: `fn bounded_retry_gives_up_after_bounded_attempts() {`
  - Purpose: Indexed function `bounded_retry_gives_up_after_bounded_attempts` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:919-928]
- `bounded_retry_fails_fast_on_non_transient_errors` (function) component `bounded_retry_fails_fast_on_non_transient_errors [function]` (`f37cdd69-44ed-5606-97d4-b64db59dbe68`) lines 931-943 [crates/gcode/src/commands/codewiki/text.rs:931-943]
  - Signature: `fn bounded_retry_fails_fast_on_non_transient_errors() {`
  - Purpose: Indexed function `bounded_retry_fails_fast_on_non_transient_errors` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:931-943]

