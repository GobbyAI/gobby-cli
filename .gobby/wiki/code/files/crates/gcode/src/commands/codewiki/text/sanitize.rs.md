---
title: crates/gcode/src/commands/codewiki/text/sanitize.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
  ranges:
  - 5-24
  - 27-30
  - 33-36
  - 38-82
  - 84-88
  - 90-112
  - 114-120
  - 122-132
  - 134-137
  - 139-143
  - 151-157
  - 160-175
  - 178-190
  - 193-205
  - 208-219
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/sanitize.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

This file sanitizes Markdown produced for model-facing text by finding unsafe link targets and replacing the entire Markdown link with its visible label, while leaving safe content untouched. It parses the text with `pulldown_cmark`, tracks active unsafe link frames while accumulating label text from nested events, classifies targets as unsafe when they are absolute paths, URI-schemed, parent-traversal, Windows/UNC, file, or tilde-based, and uses small helpers plus tests to verify that unsafe links are stripped while valid citations, anchors, relative links, plain brackets, and code links are preserved.
[crates/gcode/src/commands/codewiki/text/sanitize.rs:5-24]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:27-30]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:33-36]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:38-82]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:84-88]

## API Symbols

- `sanitize_model_markdown_links` (function) component `sanitize_model_markdown_links [function]` (`603232f7-037b-5e25-83f0-e3a330d28302`) lines 5-24 [crates/gcode/src/commands/codewiki/text/sanitize.rs:5-24]
  - Signature: `pub(super) fn sanitize_model_markdown_links(text: &str) -> String {`
  - Purpose: Indexed function `sanitize_model_markdown_links` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:5-24]
- `LinkFrame` (class) component `LinkFrame [class]` (`10c47607-241b-5f11-9d2d-ca3b42c30d92`) lines 27-30 [crates/gcode/src/commands/codewiki/text/sanitize.rs:27-30]
  - Signature: `struct LinkFrame {`
  - Purpose: Indexed class `LinkFrame` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:27-30]
- `Replacement` (class) component `Replacement [class]` (`711ddb46-16bb-534b-9269-5436e7b754b2`) lines 33-36 [crates/gcode/src/commands/codewiki/text/sanitize.rs:33-36]
  - Signature: `struct Replacement {`
  - Purpose: Indexed class `Replacement` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:33-36]
- `unsafe_link_replacements` (function) component `unsafe_link_replacements [function]` (`de5a0140-64fe-59ec-8495-9483d3c38b63`) lines 38-82 [crates/gcode/src/commands/codewiki/text/sanitize.rs:38-82]
  - Signature: `fn unsafe_link_replacements(text: &str) -> Vec<Replacement> {`
  - Purpose: Indexed function `unsafe_link_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:38-82]
- `push_label_text` (function) component `push_label_text [function]` (`e24f5092-674d-5bd3-99c2-6d5b2cc71f74`) lines 84-88 [crates/gcode/src/commands/codewiki/text/sanitize.rs:84-88]
  - Signature: `fn push_label_text(active_links: &mut [LinkFrame], value: &str) {`
  - Purpose: Indexed function `push_label_text` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:84-88]
- `is_unsafe_link_target` (function) component `is_unsafe_link_target [function]` (`e82a46fb-e025-5599-92da-454a485fee48`) lines 90-112 [crates/gcode/src/commands/codewiki/text/sanitize.rs:90-112]
  - Signature: `fn is_unsafe_link_target(target: &str) -> bool {`
  - Purpose: Indexed function `is_unsafe_link_target` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:90-112]
- `is_windows_absolute_path` (function) component `is_windows_absolute_path [function]` (`c48b989f-9f8c-53ab-8695-7d4c0246fcca`) lines 114-120 [crates/gcode/src/commands/codewiki/text/sanitize.rs:114-120]
  - Signature: `fn is_windows_absolute_path(target: &str) -> bool {`
  - Purpose: Indexed function `is_windows_absolute_path` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:114-120]
- `has_uri_scheme` (function) component `has_uri_scheme [function]` (`2b94576c-0602-5bc6-a2b7-5e683a2d3ae6`) lines 122-132 [crates/gcode/src/commands/codewiki/text/sanitize.rs:122-132]
  - Signature: `fn has_uri_scheme(target: &str) -> bool {`
  - Purpose: Indexed function `has_uri_scheme` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:122-132]
- `contains_parent_dir_segment` (function) component `contains_parent_dir_segment [function]` (`d3c12fd3-aff2-5b28-94fd-1b8900febe39`) lines 134-137 [crates/gcode/src/commands/codewiki/text/sanitize.rs:134-137]
  - Signature: `fn contains_parent_dir_segment(target: &str) -> bool {`
  - Purpose: Indexed function `contains_parent_dir_segment` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:134-137]
- `starts_with_ignore_ascii_case` (function) component `starts_with_ignore_ascii_case [function]` (`e7dd9262-9242-57c2-8abe-fd206add94b0`) lines 139-143 [crates/gcode/src/commands/codewiki/text/sanitize.rs:139-143]
  - Signature: `fn starts_with_ignore_ascii_case(value: &str, prefix: &str) -> bool {`
  - Purpose: Indexed function `starts_with_ignore_ascii_case` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:139-143]
- `span` (function) component `span [function]` (`5d41e458-b9cc-5e4d-8fe8-5a8bb93d9059`) lines 151-157 [crates/gcode/src/commands/codewiki/text/sanitize.rs:151-157]
  - Signature: `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {`
  - Purpose: Indexed function `span` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:151-157]
- `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` (function) component `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations [function]` (`fe805a9d-246f-5bf7-a10e-b3d155f9884a`) lines 160-175 [crates/gcode/src/commands/codewiki/text/sanitize.rs:160-175]
  - Signature: `fn ground_text_strips_absolute_markdown_links_and_keeps_valid_citations() {`
  - Purpose: Indexed function `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:160-175]
- `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` (function) component `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback [function]` (`c1c89b2c-c87a-5abe-ad7f-7f74360608ad`) lines 178-190 [crates/gcode/src/commands/codewiki/text/sanitize.rs:178-190]
  - Signature: `fn ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback() {`
  - Purpose: Indexed function `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:178-190]
- `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` (function) component `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text [function]` (`72a9cf85-3962-5979-9aa3-c5202c0541b0`) lines 193-205 [crates/gcode/src/commands/codewiki/text/sanitize.rs:193-205]
  - Signature: `fn strips_traversal_windows_unc_file_and_tilde_targets_to_label_text() {`
  - Purpose: Indexed function `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:193-205]
- `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` (function) component `keeps_external_anchors_safe_relative_plain_brackets_and_code_links [function]` (`78d8d39c-223f-5898-86e4-ffa3204a1985`) lines 208-219 [crates/gcode/src/commands/codewiki/text/sanitize.rs:208-219]
  - Signature: `fn keeps_external_anchors_safe_relative_plain_brackets_and_code_links() {`
  - Purpose: Indexed function `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:208-219]

