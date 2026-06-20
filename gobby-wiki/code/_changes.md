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

- Files: 491
- Symbols: 9813
- Graph neighborhoods: 9813

## Added Files

- None

## Removed Files

- None

## Changed Files

- `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `crates/gcode/src/commands/codewiki/render/common.rs`
- `crates/gcode/src/commands/codewiki/text/citations.rs`
- `crates/gcode/src/commands/codewiki/text/sanitize.rs`

## New Symbols

- `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `reanchors_relative_citation_link_targets_to_line_anchors` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `Replacement` class in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `service_matrix_lists_services_with_fixed_requirement_classes` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `cell_summary_caps_runaway_single_paragraph_on_a_word_boundary` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `apply_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ReanchorResult` class in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `reanchor_citations` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `is_windows_absolute_path` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `cell_summary_flattens_when_text_opens_with_a_table` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `validator_rejects_unbalanced_node_shape` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_rejects_empty_diagram` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `push_label_text` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `wikilink_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `service_matrix_empty_when_model_reaches_no_services` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `is_unsafe_link_target` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizes_literal_markdown_links_in_symbol_purpose` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `runtime_flow_sequence_is_valid_and_model_seeded` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `span` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `is_ascii_line_number` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `empty_model_draws_nothing_but_is_not_an_error` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `LinkFrame` class in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `diagram_section_caption_explains_required_but_degraded_framing` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `ground_text_still_appends_fallback_when_page_is_uncited` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `range_overlaps` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `replacement_for_range` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `citation_anchor_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `has_uri_scheme` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `unsafe_link_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_rejects_nested_fence` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `ghook_flow_used_when_no_ai_boundary` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `starts_with_ignore_ascii_case` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `citation_inner` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `validator_rejects_content_after_close` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_rejects_unclosed_fence` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `range_contains` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `section_render_includes_prose_and_only_valid_fences` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `ground_text_keeps_bare_anchor_and_skips_the_trailing_citation_dump` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `markdown_link_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_rejects_unrecognized_header` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `anchor_citation_target` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizing_symbol_purpose_links_leaves_source_citations_plain` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizes_literal_wikilinks_in_symbol_purpose` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_accepts_minimal_flowchart` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `cell_summary_stops_at_first_table_row_without_a_blank_line` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `neutralize_symbol_purpose_links` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `citation_parts` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `markdown_code_ranges` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `CitationResolver` type in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `contains_parent_dir_segment` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_accepts_sequence_diagram` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`

## Removed Symbols

- `cell_summary_flattens_when_text_opens_with_a_table` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `LinkFrame` class in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `cell_summary_caps_runaway_single_paragraph_on_a_word_boundary` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `validator_accepts_sequence_diagram` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `is_unsafe_link_target` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ReanchorResult` class in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `validator_rejects_content_after_close` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `empty_model_draws_nothing_but_is_not_an_error` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `range_overlaps` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `service_matrix_empty_when_model_reaches_no_services` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `has_uri_scheme` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizes_literal_wikilinks_in_symbol_purpose` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ghook_flow_used_when_no_ai_boundary` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `contains_parent_dir_segment` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `markdown_code_ranges` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `diagram_section_caption_explains_required_but_degraded_framing` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_rejects_empty_diagram` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `cell_summary_stops_at_first_table_row_without_a_blank_line` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `replacement_for_range` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `runtime_flow_sequence_is_valid_and_model_seeded` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `Replacement` class in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `unsafe_link_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizing_symbol_purpose_links_leaves_source_citations_plain` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `markdown_link_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `service_matrix_lists_services_with_fixed_requirement_classes` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_accepts_minimal_flowchart` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `is_windows_absolute_path` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizes_literal_markdown_links_in_symbol_purpose` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `wikilink_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `reanchor_citations` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `CitationResolver` type in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `citation_inner` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `validator_rejects_unbalanced_node_shape` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `range_contains` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_rejects_unclosed_fence` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `apply_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `section_render_includes_prose_and_only_valid_fences` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `push_label_text` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralize_symbol_purpose_links` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `citation_parts` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `ground_text_still_appends_fallback_when_page_is_uncited` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `starts_with_ignore_ascii_case` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_rejects_unrecognized_header` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_rejects_nested_fence` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `ground_text_keeps_bare_anchor_and_skips_the_trailing_citation_dump` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `span` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`

## Changed Graph Neighborhoods

- `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `cell_summary_flattens_when_text_opens_with_a_table` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `reanchors_relative_citation_link_targets_to_line_anchors` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `Replacement` class in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `service_matrix_lists_services_with_fixed_requirement_classes` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `cell_summary_caps_runaway_single_paragraph_on_a_word_boundary` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `LinkFrame` class in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `cell_summary_caps_runaway_single_paragraph_on_a_word_boundary` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `validator_accepts_sequence_diagram` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `apply_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `is_unsafe_link_target` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ReanchorResult` class in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `reanchor_citations` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `ReanchorResult` class in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `is_windows_absolute_path` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `cell_summary_flattens_when_text_opens_with_a_table` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `validator_rejects_content_after_close` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_rejects_unbalanced_node_shape` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_rejects_empty_diagram` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `push_label_text` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `wikilink_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `empty_model_draws_nothing_but_is_not_an_error` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `service_matrix_empty_when_model_reaches_no_services` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `range_overlaps` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `is_unsafe_link_target` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizes_literal_markdown_links_in_symbol_purpose` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `runtime_flow_sequence_is_valid_and_model_seeded` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `service_matrix_empty_when_model_reaches_no_services` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `has_uri_scheme` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `span` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `is_ascii_line_number` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizes_literal_wikilinks_in_symbol_purpose` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ghook_flow_used_when_no_ai_boundary` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `contains_parent_dir_segment` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `markdown_code_ranges` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `diagram_section_caption_explains_required_but_degraded_framing` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `empty_model_draws_nothing_but_is_not_an_error` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `LinkFrame` class in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `diagram_section_caption_explains_required_but_degraded_framing` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_rejects_empty_diagram` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `ground_text_still_appends_fallback_when_page_is_uncited` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `range_overlaps` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `replacement_for_range` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `citation_anchor_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `cell_summary_stops_at_first_table_row_without_a_blank_line` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `replacement_for_range` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `runtime_flow_sequence_is_valid_and_model_seeded` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `has_uri_scheme` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `Replacement` class in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `unsafe_link_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `unsafe_link_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_rejects_nested_fence` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `neutralizing_symbol_purpose_links_leaves_source_citations_plain` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ghook_flow_used_when_no_ai_boundary` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `markdown_link_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `starts_with_ignore_ascii_case` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `service_matrix_lists_services_with_fixed_requirement_classes` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_accepts_minimal_flowchart` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `citation_inner` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `validator_rejects_content_after_close` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_rejects_unclosed_fence` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `range_contains` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `section_render_includes_prose_and_only_valid_fences` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `is_windows_absolute_path` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizes_literal_markdown_links_in_symbol_purpose` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ground_text_keeps_bare_anchor_and_skips_the_trailing_citation_dump` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `wikilink_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `reanchor_citations` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `markdown_link_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `CitationResolver` type in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `citation_inner` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `validator_rejects_unrecognized_header` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `anchor_citation_target` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizing_symbol_purpose_links_leaves_source_citations_plain` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_rejects_unbalanced_node_shape` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `neutralizes_literal_wikilinks_in_symbol_purpose` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `range_contains` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_rejects_unclosed_fence` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `apply_replacements` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_accepts_minimal_flowchart` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `section_render_includes_prose_and_only_valid_fences` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `push_label_text` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `cell_summary_stops_at_first_table_row_without_a_blank_line` function in `crates/gcode/src/commands/codewiki/render/common.rs`
- `neutralize_symbol_purpose_links` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `citation_parts` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `neutralize_symbol_purpose_links` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `ground_text_still_appends_fallback_when_page_is_uncited` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `citation_parts` function in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `markdown_code_ranges` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `CitationResolver` type in `crates/gcode/src/commands/codewiki/text/citations.rs`
- `contains_parent_dir_segment` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `starts_with_ignore_ascii_case` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_rejects_unrecognized_header` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `validator_rejects_nested_fence` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `ground_text_keeps_bare_anchor_and_skips_the_trailing_citation_dump` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `span` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`
- `validator_accepts_sequence_diagram` function in `crates/gcode/src/commands/codewiki/architecture_diagrams.rs`
- `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` function in `crates/gcode/src/commands/codewiki/text/sanitize.rs`

