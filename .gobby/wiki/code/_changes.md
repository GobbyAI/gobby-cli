---
title: Index Changes
kind: code_changes
generated_by: gcode-codewiki
trust: generated
freshness: indexed
baseline: false
degraded: false
degraded_sources: []
---

# Index Changes

## Current Snapshot

- Files: 434
- Symbols: 7933
- Graph neighborhoods: 7933

## Added Files

- None

## Removed Files

- None

## Changed Files

- `crates/gcode/src/commands/codewiki/text.rs`
- `docs/guides/codewiki.md`

## New Symbols

- `contains_valid_citation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_references` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_fails_fast_on_non_transient_errors` function in `crates/gcode/src/commands/codewiki/text.rs`
- `ground_text` function in `crates/gcode/src/commands/codewiki/text.rs`
- `replace_citations_with_markers` function in `crates/gcode/src/commands/codewiki/text.rs`
- `frontmatter_with_degradation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list_emits_one_fallback_range_per_line` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_markers_are_capped_and_keep_reference_numbering` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list` function in `crates/gcode/src/commands/codewiki/text.rs`
- `write_references` function in `crates/gcode/src/commands/codewiki/text.rs`
- `fallback_spans` function in `crates/gcode/src/commands/codewiki/text.rs`
- `frontmatter` function in `crates/gcode/src/commands/codewiki/text.rs`
- `short_prompts_never_trigger_echo_rejection` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_gives_up_after_bounded_attempts` function in `crates/gcode/src/commands/codewiki/text.rs`
- `references_resolve_only_markers_present_in_doc` function in `crates/gcode/src/commands/codewiki/text.rs`
- `fallback_spans_prefer_distinct_files_over_one_files_span_run` function in `crates/gcode/src/commands/codewiki/text.rs`
- `strip_invalid_citations` function in `crates/gcode/src/commands/codewiki/text.rs`
- `span` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_markers` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list_caps_oversized_span_sets` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_recovers_from_transient_transport_failure` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_parts` function in `crates/gcode/src/commands/codewiki/text.rs`
- `transport_failure` function in `crates/gcode/src/commands/codewiki/text.rs`
- `prompt_echo_is_rejected_as_failed_generation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `wrap_citation_items` function in `crates/gcode/src/commands/codewiki/text.rs`
- `wrap_citation_items_bounds_line_width` function in `crates/gcode/src/commands/codewiki/text.rs`

## Removed Symbols

- `citation_parts` function in `crates/gcode/src/commands/codewiki/text.rs`
- `write_references` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list` function in `crates/gcode/src/commands/codewiki/text.rs`
- `replace_citations_with_markers` function in `crates/gcode/src/commands/codewiki/text.rs`
- `span` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_recovers_from_transient_transport_failure` function in `crates/gcode/src/commands/codewiki/text.rs`
- `strip_invalid_citations` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_gives_up_after_bounded_attempts` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_markers_use_shared_width_wrapper` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list_emits_one_fallback_range_per_line` function in `crates/gcode/src/commands/codewiki/text.rs`
- `wrap_citation_items` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_references` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_fails_fast_on_non_transient_errors` function in `crates/gcode/src/commands/codewiki/text.rs`
- `contains_valid_citation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `frontmatter_with_degradation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `transport_failure` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_markers` function in `crates/gcode/src/commands/codewiki/text.rs`
- `short_prompts_never_trigger_echo_rejection` function in `crates/gcode/src/commands/codewiki/text.rs`
- `ground_text` function in `crates/gcode/src/commands/codewiki/text.rs`
- `prompt_echo_is_rejected_as_failed_generation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `frontmatter` function in `crates/gcode/src/commands/codewiki/text.rs`

## Changed Graph Neighborhoods

- `citation_parts` function in `crates/gcode/src/commands/codewiki/text.rs`
- `contains_valid_citation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_references` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_fails_fast_on_non_transient_errors` function in `crates/gcode/src/commands/codewiki/text.rs`
- `ground_text` function in `crates/gcode/src/commands/codewiki/text.rs`
- `generate_with_bounded_retry` function in `crates/gcode/src/commands/codewiki/text.rs`
- `write_references` function in `crates/gcode/src/commands/codewiki/text.rs`
- `replace_citations_with_markers` function in `crates/gcode/src/commands/codewiki/text.rs`
- `frontmatter_with_degradation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list_emits_one_fallback_range_per_line` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_markers_are_capped_and_keep_reference_numbering` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list` function in `crates/gcode/src/commands/codewiki/text.rs`
- `write_references` function in `crates/gcode/src/commands/codewiki/text.rs`
- `fallback_spans` function in `crates/gcode/src/commands/codewiki/text.rs`
- `replace_citations_with_markers` function in `crates/gcode/src/commands/codewiki/text.rs`
- `span` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_recovers_from_transient_transport_failure` function in `crates/gcode/src/commands/codewiki/text.rs`
- `frontmatter` function in `crates/gcode/src/commands/codewiki/text.rs`
- `strip_invalid_citations` function in `crates/gcode/src/commands/codewiki/text.rs`
- `short_prompts_never_trigger_echo_rejection` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_gives_up_after_bounded_attempts` function in `crates/gcode/src/commands/codewiki/text.rs`
- `references_resolve_only_markers_present_in_doc` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_gives_up_after_bounded_attempts` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_markers_use_shared_width_wrapper` function in `crates/gcode/src/commands/codewiki/text.rs`
- `fallback_spans_prefer_distinct_files_over_one_files_span_run` function in `crates/gcode/src/commands/codewiki/text.rs`
- `strip_invalid_citations` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list_emits_one_fallback_range_per_line` function in `crates/gcode/src/commands/codewiki/text.rs`
- `span` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_markers` function in `crates/gcode/src/commands/codewiki/text.rs`
- `wrap_citation_items` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_references` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_list_caps_oversized_span_sets` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_recovers_from_transient_transport_failure` function in `crates/gcode/src/commands/codewiki/text.rs`
- `maybe_generate` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_parts` function in `crates/gcode/src/commands/codewiki/text.rs`
- `bounded_retry_fails_fast_on_non_transient_errors` function in `crates/gcode/src/commands/codewiki/text.rs`
- `contains_valid_citation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `transport_failure` function in `crates/gcode/src/commands/codewiki/text.rs`
- `frontmatter_with_degradation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `transport_failure` function in `crates/gcode/src/commands/codewiki/text.rs`
- `citation_markers` function in `crates/gcode/src/commands/codewiki/text.rs`
- `short_prompts_never_trigger_echo_rejection` function in `crates/gcode/src/commands/codewiki/text.rs`
- `ground_text` function in `crates/gcode/src/commands/codewiki/text.rs`
- `prompt_echo_is_rejected_as_failed_generation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `prompt_echo_is_rejected_as_failed_generation` function in `crates/gcode/src/commands/codewiki/text.rs`
- `wrap_citation_items` function in `crates/gcode/src/commands/codewiki/text.rs`
- `wrap_citation_items_bounds_line_width` function in `crates/gcode/src/commands/codewiki/text.rs`
- `frontmatter` function in `crates/gcode/src/commands/codewiki/text.rs`

