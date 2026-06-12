---
title: crates/gcode/src/commands/codewiki/text.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 15-27
  - 30-34
  - 36-84
  - 89-103
  - 105-113
  - 115-131
  - 138-142
  - 144-161
  - 163-177
  - 186-196
  - 198-201
  - 203-218
  - 220-229
  - 231-243
  - 245-251
  - 253-255
  - 257-266
  - 277-298
  - 300-306
  - 308-328
  - 330-342
  - 344-353
  - 355-361
  - 366-379
  - 381-397
  - 399-425
  - 427-444
  - 446-459
  - 462-464
  - 468-475
  - 477-484
  - 486-533
  - 535-559
  - 565-571
  - 574-593
  - 596-616
  - 619-631
  - 634-647
  - 650-663
  - 666-681
  - 684-691
  - 694-726
  - 729-732
  - 734-740
  - 743-756
  - 759-768
  - 771-783
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/text.rs` exposes 49 indexed API symbols.
[crates/gcode/src/commands/codewiki/text.rs:15-27]
[crates/gcode/src/commands/codewiki/text.rs:30-34]
[crates/gcode/src/commands/codewiki/text.rs:36-84]
[crates/gcode/src/commands/codewiki/text.rs:89-103]
[crates/gcode/src/commands/codewiki/text.rs:105-113]

## API Symbols

- `Frontmatter` (class) component `Frontmatter [class]` (`eae0ca11-c8fa-584f-b3b2-e66838546e27`) lines 15-27 [crates/gcode/src/commands/codewiki/text.rs:15-27]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: Indexed class `Frontmatter` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:15-27]
- `FrontmatterSourceFile` (class) component `FrontmatterSourceFile [class]` (`c1009587-d58e-5878-977d-ce6795a0e388`) lines 30-34 [crates/gcode/src/commands/codewiki/text.rs:30-34]
  - Signature: `struct FrontmatterSourceFile<'a> {`
  - Purpose: Indexed class `FrontmatterSourceFile` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:30-34]
- `resolve_text_generator` (function) component `resolve_text_generator [function]` (`bd896574-ba30-557f-8d30-9a987b8d334d`) lines 36-84 [crates/gcode/src/commands/codewiki/text.rs:36-84]
  - Signature: `pub(crate) fn resolve_text_generator(`
  - Purpose: Indexed function `resolve_text_generator` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:36-84]
- `generate_with_bounded_retry` (function) component `generate_with_bounded_retry [function]` (`3a40a621-fc89-5847-992a-db3a44c4a833`) lines 89-103 [crates/gcode/src/commands/codewiki/text.rs:89-103]
  - Signature: `pub(crate) fn generate_with_bounded_retry<T>(`
  - Purpose: Indexed function `generate_with_bounded_retry` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:89-103]
- `retryable_generation_error` (function) component `retryable_generation_error [function]` (`c025b0ee-ca2a-5088-8f4c-591e66098fd7`) lines 105-113 [crates/gcode/src/commands/codewiki/text.rs:105-113]
  - Signature: `fn retryable_generation_error(error: &AiError) -> bool {`
  - Purpose: Indexed function `retryable_generation_error` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:105-113]
- `resolve_ai_context` (function) component `resolve_ai_context [function]` (`828f374f-dad9-5af5-ab2c-74f2c1c4fa15`) lines 115-131 [crates/gcode/src/commands/codewiki/text.rs:115-131]
  - Signature: `pub(crate) fn resolve_ai_context(`
  - Purpose: Indexed function `resolve_ai_context` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:115-131]
- `Generation` (type) component `Generation [type]` (`997e24bd-9868-58ff-9e0a-d7088a4be9ab`) lines 138-142 [crates/gcode/src/commands/codewiki/text.rs:138-142]
  - Signature: `pub(crate) enum Generation {`
  - Purpose: Indexed type `Generation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:138-142]
- `Generation` (class) component `Generation [class]` (`b8f063bb-ccfc-5732-81bf-d300725b94aa`) lines 144-161 [crates/gcode/src/commands/codewiki/text.rs:144-161]
  - Signature: `impl Generation {`
  - Purpose: Indexed class `Generation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:144-161]
- `Generation.failed` (method) component `Generation.failed [method]` (`980f3dba-ec93-555f-a209-0359d1755a6c`) lines 145-147 [crates/gcode/src/commands/codewiki/text.rs:145-147]
  - Signature: `pub(crate) fn failed(&self) -> bool {`
  - Purpose: Indexed method `Generation.failed` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:145-147]
- `Generation.unwrap_or_record` (method) component `Generation.unwrap_or_record [method]` (`6fa87ff6-e6de-5a3c-99c7-a1431ba79109`) lines 151-160 [crates/gcode/src/commands/codewiki/text.rs:151-160]
  - Signature: `pub(crate) fn unwrap_or_record(self, fallback: String, degraded: &mut bool) -> String {`
  - Purpose: Indexed method `Generation.unwrap_or_record` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:151-160]
- `maybe_generate` (function) component `maybe_generate [function]` (`f8243263-3dd9-5554-b108-5490661d618d`) lines 163-177 [crates/gcode/src/commands/codewiki/text.rs:163-177]
  - Signature: `pub(crate) fn maybe_generate(`
  - Purpose: Indexed function `maybe_generate` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:163-177]
- `is_prompt_echo` (function) component `is_prompt_echo [function]` (`bfd4eba5-a8ea-5bf0-925f-1fb7836fbb6f`) lines 186-196 [crates/gcode/src/commands/codewiki/text.rs:186-196]
  - Signature: `pub(crate) fn is_prompt_echo(text: &str, prompt: &str) -> bool {`
  - Purpose: Indexed function `is_prompt_echo` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:186-196]
- `clean_generated` (function) component `clean_generated [function]` (`4e86bc23-b0ce-546d-94e9-a08c1a4d130f`) lines 198-201 [crates/gcode/src/commands/codewiki/text.rs:198-201]
  - Signature: `pub(crate) fn clean_generated(text: String) -> Option<String> {`
  - Purpose: Indexed function `clean_generated` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:198-201]
- `structural_symbol_purpose` (function) component `structural_symbol_purpose [function]` (`3e8baba0-4bc2-5673-bfe3-0fd245d4bc5a`) lines 203-218 [crates/gcode/src/commands/codewiki/text.rs:203-218]
  - Signature: `pub(crate) fn structural_symbol_purpose(symbol: &Symbol) -> String {`
  - Purpose: Indexed function `structural_symbol_purpose` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:203-218]
- `structural_file_summary` (function) component `structural_file_summary [function]` (`558b277f-e6c6-501d-82b7-64950c6cb87c`) lines 220-229 [crates/gcode/src/commands/codewiki/text.rs:220-229]
  - Signature: `pub(crate) fn structural_file_summary(file: &str, symbols: &[SymbolDoc]) -> String {`
  - Purpose: Indexed function `structural_file_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:220-229]
- `structural_module_summary` (function) component `structural_module_summary [function]` (`29b6e986-f1cc-5438-98af-0fda093bfa77`) lines 231-243 [crates/gcode/src/commands/codewiki/text.rs:231-243]
  - Signature: `pub(crate) fn structural_module_summary(`
  - Purpose: Indexed function `structural_module_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:231-243]
- `structural_repo_summary` (function) component `structural_repo_summary [function]` (`9d102d5a-70a7-5466-9930-b2598f414d8c`) lines 245-251 [crates/gcode/src/commands/codewiki/text.rs:245-251]
  - Signature: `pub(crate) fn structural_repo_summary(file_count: usize, module_count: usize) -> String {`
  - Purpose: Indexed function `structural_repo_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:245-251]
- `write_section` (function) component `write_section [function]` (`991e67bc-6202-5f08-bed4-d52481655e14`) lines 253-255 [crates/gcode/src/commands/codewiki/text.rs:253-255]
  - Signature: `pub(crate) fn write_section(doc: &mut String, heading: &str, body: &str) {`
  - Purpose: Indexed function `write_section` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:253-255]
- `collect_link_spans` (function) component `collect_link_spans [function]` (`04af31e4-9e17-5e45-a33c-63d6a0fcd627`) lines 257-266 [crates/gcode/src/commands/codewiki/text.rs:257-266]
  - Signature: `pub(crate) fn collect_link_spans(files: &[FileLink], modules: &[ModuleLink]) -> Vec<SourceSpan> {`
  - Purpose: Indexed function `collect_link_spans` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:257-266]
- `fallback_spans` (function) component `fallback_spans [function]` (`bfde9422-38d1-5a55-a282-a3dd86a0d9fb`) lines 277-298 [crates/gcode/src/commands/codewiki/text.rs:277-298]
  - Signature: `fn fallback_spans(spans: &[SourceSpan]) -> Vec<SourceSpan> {`
  - Purpose: Indexed function `fallback_spans` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:277-298]
- `citation_list` (function) component `citation_list [function]` (`e7bb3861-6b73-567c-90bb-53d1399d95b7`) lines 300-306 [crates/gcode/src/commands/codewiki/text.rs:300-306]
  - Signature: `pub(crate) fn citation_list(spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `citation_list` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:300-306]
- `wrap_citation_items` (function) component `wrap_citation_items [function]` (`d738dc4a-3472-5654-a130-b4cfba2ec07f`) lines 308-328 [crates/gcode/src/commands/codewiki/text.rs:308-328]
  - Signature: `fn wrap_citation_items<I>(items: I, max_line_width: usize) -> String`
  - Purpose: Indexed function `wrap_citation_items` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:308-328]
- `citation_markers` (function) component `citation_markers [function]` (`ea1ad37a-03db-546a-aa70-7e053aa1c946`) lines 330-342 [crates/gcode/src/commands/codewiki/text.rs:330-342]
  - Signature: `pub(crate) fn citation_markers(spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `citation_markers` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:330-342]
- `citation_references` (function) component `citation_references [function]` (`4299f052-fb38-5aab-aba1-29aff86117e3`) lines 344-353 [crates/gcode/src/commands/codewiki/text.rs:344-353]
  - Signature: `fn citation_references(spans: &[SourceSpan]) -> Vec<(usize, String)> {`
  - Purpose: Indexed function `citation_references` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:344-353]
- `replace_citations_with_markers` (function) component `replace_citations_with_markers [function]` (`5f746ac1-38ff-5630-bdb4-0dd2a24c189a`) lines 355-361 [crates/gcode/src/commands/codewiki/text.rs:355-361]
  - Signature: `pub(crate) fn replace_citations_with_markers(text: &str, spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `replace_citations_with_markers` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:355-361]
- `write_references` (function) component `write_references [function]` (`be457f9c-2602-56d0-9009-ae022206da6f`) lines 366-379 [crates/gcode/src/commands/codewiki/text.rs:366-379]
  - Signature: `pub(crate) fn write_references(doc: &mut String, spans: &[SourceSpan]) {`
  - Purpose: Indexed function `write_references` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:366-379]
- `ground_text` (function) component `ground_text [function]` (`b6aba247-1602-542b-a457-d19ad4afe711`) lines 381-397 [crates/gcode/src/commands/codewiki/text.rs:381-397]
  - Signature: `pub(crate) fn ground_text(`
  - Purpose: Indexed function `ground_text` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:381-397]
- `strip_invalid_citations` (function) component `strip_invalid_citations [function]` (`b1af5d54-f1c2-5d96-912f-78cb30fda211`) lines 399-425 [crates/gcode/src/commands/codewiki/text.rs:399-425]
  - Signature: `pub(crate) fn strip_invalid_citations(text: &str, valid_spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `strip_invalid_citations` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:399-425]
- `contains_valid_citation` (function) component `contains_valid_citation [function]` (`489817c9-adcf-5987-a0e5-07821fab7daf`) lines 427-444 [crates/gcode/src/commands/codewiki/text.rs:427-444]
  - Signature: `pub(crate) fn contains_valid_citation(text: &str, valid_spans: &[SourceSpan]) -> bool {`
  - Purpose: Indexed function `contains_valid_citation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:427-444]
- `citation_parts` (function) component `citation_parts [function]` (`a790f62d-995b-5f97-aeda-5804f58f7fff`) lines 446-459 [crates/gcode/src/commands/codewiki/text.rs:446-459]
  - Signature: `pub(crate) fn citation_parts(value: &str) -> Option<(&str, usize, usize)> {`
  - Purpose: Indexed function `citation_parts` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:446-459]
- `frontmatter` (function) component `frontmatter [function]` (`7d2da148-f467-5773-afb5-eec86049cc13`) lines 462-464 [crates/gcode/src/commands/codewiki/text.rs:462-464]
  - Signature: `pub(crate) fn frontmatter(title: &str, kind: &str, source_spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `frontmatter` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:462-464]
- `frontmatter_with_degradation` (function) component `frontmatter_with_degradation [function]` (`ea649be6-6fad-51d4-8acc-c33bb794ed3d`) lines 468-475 [crates/gcode/src/commands/codewiki/text.rs:468-475]
  - Signature: `pub(crate) fn frontmatter_with_degradation(`
  - Purpose: Indexed function `frontmatter_with_degradation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:468-475]
- `frontmatter_with_degradation_without_ranges` (function) component `frontmatter_with_degradation_without_ranges [function]` (`5aa4dbd8-1964-5628-b445-56ade0bc0bc1`) lines 477-484 [crates/gcode/src/commands/codewiki/text.rs:477-484]
  - Signature: `pub(crate) fn frontmatter_with_degradation_without_ranges(`
  - Purpose: Indexed function `frontmatter_with_degradation_without_ranges` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:477-484]
- `frontmatter_with_options` (function) component `frontmatter_with_options [function]` (`e8eb7e21-1599-5d8d-b0e1-9b6b7b0a5d33`) lines 486-533 [crates/gcode/src/commands/codewiki/text.rs:486-533]
  - Signature: `fn frontmatter_with_options(`
  - Purpose: Indexed function `frontmatter_with_options` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:486-533]
- `format_frontmatter_ranges` (function) component `format_frontmatter_ranges [function]` (`caeeca1d-857a-5612-b31a-e9a92181f47e`) lines 535-559 [crates/gcode/src/commands/codewiki/text.rs:535-559]
  - Signature: `fn format_frontmatter_ranges(ranges: BTreeSet<(usize, usize)>) -> Vec<String> {`
  - Purpose: Indexed function `format_frontmatter_ranges` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:535-559]
- `span` (function) component `span [function]` (`fb421126-f976-5b90-b348-fcb670268f8e`) lines 565-571 [crates/gcode/src/commands/codewiki/text.rs:565-571]
  - Signature: `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {`
  - Purpose: Indexed function `span` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:565-571]
- `frontmatter_coalesces_contiguous_provenance_ranges` (function) component `frontmatter_coalesces_contiguous_provenance_ranges [function]` (`127d83b5-cb84-5d51-bfe3-3ad23ec6ea1f`) lines 574-593 [crates/gcode/src/commands/codewiki/text.rs:574-593]
  - Signature: `fn frontmatter_coalesces_contiguous_provenance_ranges() {`
  - Purpose: Indexed function `frontmatter_coalesces_contiguous_provenance_ranges` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:574-593]
- `citation_list_emits_one_fallback_range_per_line` (function) component `citation_list_emits_one_fallback_range_per_line [function]` (`9877a440-1a05-56b5-aa3f-edb13b3eeb61`) lines 596-616 [crates/gcode/src/commands/codewiki/text.rs:596-616]
  - Signature: `fn citation_list_emits_one_fallback_range_per_line() {`
  - Purpose: Indexed function `citation_list_emits_one_fallback_range_per_line` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:596-616]
- `citation_list_caps_oversized_span_sets` (function) component `citation_list_caps_oversized_span_sets [function]` (`0e2358a2-d88c-5916-9165-cc23fe902135`) lines 619-631 [crates/gcode/src/commands/codewiki/text.rs:619-631]
  - Signature: `fn citation_list_caps_oversized_span_sets() {`
  - Purpose: Indexed function `citation_list_caps_oversized_span_sets` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:619-631]
- `fallback_spans_prefer_distinct_files_over_one_files_span_run` (function) component `fallback_spans_prefer_distinct_files_over_one_files_span_run [function]` (`b3019623-9b78-5cbf-88dd-96e835a8636c`) lines 634-647 [crates/gcode/src/commands/codewiki/text.rs:634-647]
  - Signature: `fn fallback_spans_prefer_distinct_files_over_one_files_span_run() {`
  - Purpose: Indexed function `fallback_spans_prefer_distinct_files_over_one_files_span_run` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:634-647]
- `citation_markers_are_capped_and_keep_reference_numbering` (function) component `citation_markers_are_capped_and_keep_reference_numbering [function]` (`d31616d1-6eaa-56bb-b53b-bbbe5897ce10`) lines 650-663 [crates/gcode/src/commands/codewiki/text.rs:650-663]
  - Signature: `fn citation_markers_are_capped_and_keep_reference_numbering() {`
  - Purpose: Indexed function `citation_markers_are_capped_and_keep_reference_numbering` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:650-663]
- `references_resolve_only_markers_present_in_doc` (function) component `references_resolve_only_markers_present_in_doc [function]` (`c848b691-f5c6-55eb-ba1c-d515c2a0b46c`) lines 666-681 [crates/gcode/src/commands/codewiki/text.rs:666-681]
  - Signature: `fn references_resolve_only_markers_present_in_doc() {`
  - Purpose: Indexed function `references_resolve_only_markers_present_in_doc` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:666-681]
- `wrap_citation_items_bounds_line_width` (function) component `wrap_citation_items_bounds_line_width [function]` (`f18c59a2-fcd4-58d3-b989-de02c74043d8`) lines 684-691 [crates/gcode/src/commands/codewiki/text.rs:684-691]
  - Signature: `fn wrap_citation_items_bounds_line_width() {`
  - Purpose: Indexed function `wrap_citation_items_bounds_line_width` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:684-691]
- `prompt_echo_is_rejected_as_failed_generation` (function) component `prompt_echo_is_rejected_as_failed_generation [function]` (`454a782e-c838-5a44-98bf-7f9b19c6f587`) lines 694-726 [crates/gcode/src/commands/codewiki/text.rs:694-726]
  - Signature: `fn prompt_echo_is_rejected_as_failed_generation() {`
  - Purpose: Indexed function `prompt_echo_is_rejected_as_failed_generation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:694-726]
- `short_prompts_never_trigger_echo_rejection` (function) component `short_prompts_never_trigger_echo_rejection [function]` (`40805f72-712b-59b5-85be-adcf06e21d03`) lines 729-732 [crates/gcode/src/commands/codewiki/text.rs:729-732]
  - Signature: `fn short_prompts_never_trigger_echo_rejection() {`
  - Purpose: Indexed function `short_prompts_never_trigger_echo_rejection` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:729-732]
- `transport_failure` (function) component `transport_failure [function]` (`6096cf84-99e1-55a6-aa2e-03ea8f06b183`) lines 734-740 [crates/gcode/src/commands/codewiki/text.rs:734-740]
  - Signature: `fn transport_failure() -> AiError {`
  - Purpose: Indexed function `transport_failure` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:734-740]
- `bounded_retry_recovers_from_transient_transport_failure` (function) component `bounded_retry_recovers_from_transient_transport_failure [function]` (`5ecfe02d-d15e-5541-a00e-175cc38cb434`) lines 743-756 [crates/gcode/src/commands/codewiki/text.rs:743-756]
  - Signature: `fn bounded_retry_recovers_from_transient_transport_failure() {`
  - Purpose: Indexed function `bounded_retry_recovers_from_transient_transport_failure` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:743-756]
- `bounded_retry_gives_up_after_bounded_attempts` (function) component `bounded_retry_gives_up_after_bounded_attempts [function]` (`1e9935b5-6cd1-5388-a4a4-4c8869534b9d`) lines 759-768 [crates/gcode/src/commands/codewiki/text.rs:759-768]
  - Signature: `fn bounded_retry_gives_up_after_bounded_attempts() {`
  - Purpose: Indexed function `bounded_retry_gives_up_after_bounded_attempts` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:759-768]
- `bounded_retry_fails_fast_on_non_transient_errors` (function) component `bounded_retry_fails_fast_on_non_transient_errors [function]` (`d8d761e8-2797-5f10-9739-47c1b077d25d`) lines 771-783 [crates/gcode/src/commands/codewiki/text.rs:771-783]
  - Signature: `fn bounded_retry_fails_fast_on_non_transient_errors() {`
  - Purpose: Indexed function `bounded_retry_fails_fast_on_non_transient_errors` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:771-783]

