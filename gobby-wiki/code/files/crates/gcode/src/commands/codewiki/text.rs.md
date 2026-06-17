---
title: crates/gcode/src/commands/codewiki/text.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 46-52
  - 55-74
  - 77-97
  - 100-112
  - 115-128
  - 131-144
  - 147-157
  - 160-171
  - 174-206
  - 209-224
  - 227-234
  - 237-270
  - 273-276
  - 278-284
  - 287-300
  - 303-312
  - 315-327
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/text.rs:46-52](crates/gcode/src/commands/codewiki/text.rs#L46-L52), [crates/gcode/src/commands/codewiki/text.rs:55-74](crates/gcode/src/commands/codewiki/text.rs#L55-L74), [crates/gcode/src/commands/codewiki/text.rs:77-97](crates/gcode/src/commands/codewiki/text.rs#L77-L97), [crates/gcode/src/commands/codewiki/text.rs:100-112](crates/gcode/src/commands/codewiki/text.rs#L100-L112), [crates/gcode/src/commands/codewiki/text.rs:115-128](crates/gcode/src/commands/codewiki/text.rs#L115-L128), [crates/gcode/src/commands/codewiki/text.rs:131-144](crates/gcode/src/commands/codewiki/text.rs#L131-L144), [crates/gcode/src/commands/codewiki/text.rs:147-157](crates/gcode/src/commands/codewiki/text.rs#L147-L157), [crates/gcode/src/commands/codewiki/text.rs:160-171](crates/gcode/src/commands/codewiki/text.rs#L160-L171), [crates/gcode/src/commands/codewiki/text.rs:174-206](crates/gcode/src/commands/codewiki/text.rs#L174-L206), [crates/gcode/src/commands/codewiki/text.rs:209-224](crates/gcode/src/commands/codewiki/text.rs#L209-L224), [crates/gcode/src/commands/codewiki/text.rs:227-234](crates/gcode/src/commands/codewiki/text.rs#L227-L234), [crates/gcode/src/commands/codewiki/text.rs:237-270](crates/gcode/src/commands/codewiki/text.rs#L237-L270), [crates/gcode/src/commands/codewiki/text.rs:273-276](crates/gcode/src/commands/codewiki/text.rs#L273-L276), [crates/gcode/src/commands/codewiki/text.rs:278-284](crates/gcode/src/commands/codewiki/text.rs#L278-L284), [crates/gcode/src/commands/codewiki/text.rs:287-300](crates/gcode/src/commands/codewiki/text.rs#L287-L300), [crates/gcode/src/commands/codewiki/text.rs:303-312](crates/gcode/src/commands/codewiki/text.rs#L303-L312), [crates/gcode/src/commands/codewiki/text.rs:315-327](crates/gcode/src/commands/codewiki/text.rs#L315-L327)

</details>

# crates/gcode/src/commands/codewiki/text.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file is the `codewiki` text-layer glue for the crate: it pulls together citation handling, frontmatter construction, generation, sanitization, and structural summarization helpers behind a small public surface. Its test module exercises the supporting pieces end to end, checking provenance coalescing, fallback citation selection and ordering, citation marker limits, prompt-echo rejection, and bounded retry behavior for transient transport failures.
[crates/gcode/src/commands/codewiki/text.rs:46-52]
[crates/gcode/src/commands/codewiki/text.rs:55-74]
[crates/gcode/src/commands/codewiki/text.rs:77-97]
[crates/gcode/src/commands/codewiki/text.rs:100-112]
[crates/gcode/src/commands/codewiki/text.rs:115-128]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `span` | function | `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {` | `span [function]` | `ee28c354-b4d9-5c05-8423-94bd760511bc` | 46-52 [crates/gcode/src/commands/codewiki/text.rs:46-52] | Indexed function `span` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:46-52] |
| `frontmatter_coalesces_contiguous_provenance_ranges` | function | `fn frontmatter_coalesces_contiguous_provenance_ranges() {` | `frontmatter_coalesces_contiguous_provenance_ranges [function]` | `4e0c025d-76b6-5351-bb23-7819464e59e4` | 55-74 [crates/gcode/src/commands/codewiki/text.rs:55-74] | Indexed function `frontmatter_coalesces_contiguous_provenance_ranges` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:55-74] |
| `citation_list_emits_one_fallback_range_per_line` | function | `fn citation_list_emits_one_fallback_range_per_line() {` | `citation_list_emits_one_fallback_range_per_line [function]` | `519d1e35-7cee-59ea-a210-74e04b9a34c1` | 77-97 [crates/gcode/src/commands/codewiki/text.rs:77-97] | Indexed function `citation_list_emits_one_fallback_range_per_line` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:77-97] |
| `citation_list_caps_oversized_span_sets` | function | `fn citation_list_caps_oversized_span_sets() {` | `citation_list_caps_oversized_span_sets [function]` | `2111649a-939d-516f-8d9f-7322428faba3` | 100-112 [crates/gcode/src/commands/codewiki/text.rs:100-112] | Indexed function `citation_list_caps_oversized_span_sets` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:100-112] |
| `fallback_spans_prefer_distinct_files_over_one_files_span_run` | function | `fn fallback_spans_prefer_distinct_files_over_one_files_span_run() {` | `fallback_spans_prefer_distinct_files_over_one_files_span_run [function]` | `67388690-2428-58a3-a44b-2b4dc63e3d49` | 115-128 [crates/gcode/src/commands/codewiki/text.rs:115-128] | Indexed function `fallback_spans_prefer_distinct_files_over_one_files_span_run` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:115-128] |
| `citation_markers_are_capped_and_keep_reference_numbering` | function | `fn citation_markers_are_capped_and_keep_reference_numbering() {` | `citation_markers_are_capped_and_keep_reference_numbering [function]` | `eac7b60f-79a7-5b35-aba6-c9bdfd769928` | 131-144 [crates/gcode/src/commands/codewiki/text.rs:131-144] | Indexed function `citation_markers_are_capped_and_keep_reference_numbering` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:131-144] |
| `fallback_citations_rank_lexically_relevant_files_first` | function | `fn fallback_citations_rank_lexically_relevant_files_first() {` | `fallback_citations_rank_lexically_relevant_files_first [function]` | `8d920000-d1e2-5407-968e-785b90a9101a` | 147-157 [crates/gcode/src/commands/codewiki/text.rs:147-157] | Indexed function `fallback_citations_rank_lexically_relevant_files_first` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:147-157] |
| `asset_data_files_rank_behind_source_unless_sole_provenance` | function | `fn asset_data_files_rank_behind_source_unless_sole_provenance() {` | `asset_data_files_rank_behind_source_unless_sole_provenance [function]` | `03c3e55c-251f-5c90-aaf3-598af3fa0f55` | 160-171 [crates/gcode/src/commands/codewiki/text.rs:160-171] | Indexed function `asset_data_files_rank_behind_source_unless_sole_provenance` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:160-171] |
| `frontmatter_caps_provenance_and_records_truncation` | function | `fn frontmatter_caps_provenance_and_records_truncation() {` | `frontmatter_caps_provenance_and_records_truncation [function]` | `b61eb353-97a2-56cb-a333-3575d40fa3fd` | 174-206 [crates/gcode/src/commands/codewiki/text.rs:174-206] | Indexed function `frontmatter_caps_provenance_and_records_truncation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:174-206] |
| `references_resolve_only_markers_present_in_doc` | function | `fn references_resolve_only_markers_present_in_doc() {` | `references_resolve_only_markers_present_in_doc [function]` | `25595012-ba9d-57c5-9f98-a12eaf0cde61` | 209-224 [crates/gcode/src/commands/codewiki/text.rs:209-224] | Indexed function `references_resolve_only_markers_present_in_doc` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:209-224] |
| `wrap_citation_items_bounds_line_width` | function | `fn wrap_citation_items_bounds_line_width() {` | `wrap_citation_items_bounds_line_width [function]` | `8f1d2950-8f5e-5aed-bb20-3df5564fa52c` | 227-234 [crates/gcode/src/commands/codewiki/text.rs:227-234] | Indexed function `wrap_citation_items_bounds_line_width` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:227-234] |
| `prompt_echo_is_rejected_as_failed_generation` | function | `fn prompt_echo_is_rejected_as_failed_generation() {` | `prompt_echo_is_rejected_as_failed_generation [function]` | `8599e27b-48f1-5030-987b-4f33a31b0426` | 237-270 [crates/gcode/src/commands/codewiki/text.rs:237-270] | Indexed function `prompt_echo_is_rejected_as_failed_generation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:237-270] |
| `short_prompts_never_trigger_echo_rejection` | function | `fn short_prompts_never_trigger_echo_rejection() {` | `short_prompts_never_trigger_echo_rejection [function]` | `587c2a8f-ba47-58c8-99e9-bd57e5348cbf` | 273-276 [crates/gcode/src/commands/codewiki/text.rs:273-276] | Indexed function `short_prompts_never_trigger_echo_rejection` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:273-276] |
| `transport_failure` | function | `fn transport_failure() -> AiError {` | `transport_failure [function]` | `e6559696-071b-510d-8496-b875803b83bf` | 278-284 [crates/gcode/src/commands/codewiki/text.rs:278-284] | Indexed function `transport_failure` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:278-284] |
| `bounded_retry_recovers_from_transient_transport_failure` | function | `fn bounded_retry_recovers_from_transient_transport_failure() {` | `bounded_retry_recovers_from_transient_transport_failure [function]` | `45b4b07c-9f2c-54a0-a1fa-eefaa4323203` | 287-300 [crates/gcode/src/commands/codewiki/text.rs:287-300] | Indexed function `bounded_retry_recovers_from_transient_transport_failure` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:287-300] |
| `bounded_retry_gives_up_after_bounded_attempts` | function | `fn bounded_retry_gives_up_after_bounded_attempts() {` | `bounded_retry_gives_up_after_bounded_attempts [function]` | `dffadd99-2d91-51f5-9a2b-06da6c6cb48a` | 303-312 [crates/gcode/src/commands/codewiki/text.rs:303-312] | Indexed function `bounded_retry_gives_up_after_bounded_attempts` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:303-312] |
| `bounded_retry_fails_fast_on_non_transient_errors` | function | `fn bounded_retry_fails_fast_on_non_transient_errors() {` | `bounded_retry_fails_fast_on_non_transient_errors [function]` | `4c5080e1-9a0c-5024-852c-1724df08c5c1` | 315-327 [crates/gcode/src/commands/codewiki/text.rs:315-327] | Indexed function `bounded_retry_fails_fast_on_non_transient_errors` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:315-327] |
