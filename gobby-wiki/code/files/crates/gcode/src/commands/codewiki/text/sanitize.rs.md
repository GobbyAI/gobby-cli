---
title: crates/gcode/src/commands/codewiki/text/sanitize.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
  ranges:
  - 7-10
  - 12-17
  - 19-27
  - 29-37
  - 39-62
  - 64-69
  - 71-75
  - 77-81
  - 83-102
  - 105-108
  - 111-114
  - 116-156
  - 158-162
  - 164-186
  - 188-194
  - 196-206
  - 208-211
  - 213-217
  - 225-231
  - 234-249
  - 252-264
  - 267-279
  - 282-293
  - 296-303
  - 306-313
  - 316-326
  - 329-333
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10](crates/gcode/src/commands/codewiki/text/sanitize.rs#L7-L10), [crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17](crates/gcode/src/commands/codewiki/text/sanitize.rs#L12-L17), [crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27](crates/gcode/src/commands/codewiki/text/sanitize.rs#L19-L27), [crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37](crates/gcode/src/commands/codewiki/text/sanitize.rs#L29-L37), [crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62](crates/gcode/src/commands/codewiki/text/sanitize.rs#L39-L62), [crates/gcode/src/commands/codewiki/text/sanitize.rs:64-69](crates/gcode/src/commands/codewiki/text/sanitize.rs#L64-L69), [crates/gcode/src/commands/codewiki/text/sanitize.rs:71-75](crates/gcode/src/commands/codewiki/text/sanitize.rs#L71-L75), [crates/gcode/src/commands/codewiki/text/sanitize.rs:77-81](crates/gcode/src/commands/codewiki/text/sanitize.rs#L77-L81), [crates/gcode/src/commands/codewiki/text/sanitize.rs:83-102](crates/gcode/src/commands/codewiki/text/sanitize.rs#L83-L102), [crates/gcode/src/commands/codewiki/text/sanitize.rs:105-108](crates/gcode/src/commands/codewiki/text/sanitize.rs#L105-L108), [crates/gcode/src/commands/codewiki/text/sanitize.rs:111-114](crates/gcode/src/commands/codewiki/text/sanitize.rs#L111-L114), [crates/gcode/src/commands/codewiki/text/sanitize.rs:116-156](crates/gcode/src/commands/codewiki/text/sanitize.rs#L116-L156), [crates/gcode/src/commands/codewiki/text/sanitize.rs:158-162](crates/gcode/src/commands/codewiki/text/sanitize.rs#L158-L162), [crates/gcode/src/commands/codewiki/text/sanitize.rs:164-186](crates/gcode/src/commands/codewiki/text/sanitize.rs#L164-L186), [crates/gcode/src/commands/codewiki/text/sanitize.rs:188-194](crates/gcode/src/commands/codewiki/text/sanitize.rs#L188-L194), [crates/gcode/src/commands/codewiki/text/sanitize.rs:196-206](crates/gcode/src/commands/codewiki/text/sanitize.rs#L196-L206), [crates/gcode/src/commands/codewiki/text/sanitize.rs:208-211](crates/gcode/src/commands/codewiki/text/sanitize.rs#L208-L211), [crates/gcode/src/commands/codewiki/text/sanitize.rs:213-217](crates/gcode/src/commands/codewiki/text/sanitize.rs#L213-L217), [crates/gcode/src/commands/codewiki/text/sanitize.rs:225-231](crates/gcode/src/commands/codewiki/text/sanitize.rs#L225-L231), [crates/gcode/src/commands/codewiki/text/sanitize.rs:234-249](crates/gcode/src/commands/codewiki/text/sanitize.rs#L234-L249), [crates/gcode/src/commands/codewiki/text/sanitize.rs:252-264](crates/gcode/src/commands/codewiki/text/sanitize.rs#L252-L264), [crates/gcode/src/commands/codewiki/text/sanitize.rs:267-279](crates/gcode/src/commands/codewiki/text/sanitize.rs#L267-L279), [crates/gcode/src/commands/codewiki/text/sanitize.rs:282-293](crates/gcode/src/commands/codewiki/text/sanitize.rs#L282-L293), [crates/gcode/src/commands/codewiki/text/sanitize.rs:296-303](crates/gcode/src/commands/codewiki/text/sanitize.rs#L296-L303), [crates/gcode/src/commands/codewiki/text/sanitize.rs:306-313](crates/gcode/src/commands/codewiki/text/sanitize.rs#L306-L313), [crates/gcode/src/commands/codewiki/text/sanitize.rs:316-326](crates/gcode/src/commands/codewiki/text/sanitize.rs#L316-L326), [crates/gcode/src/commands/codewiki/text/sanitize.rs:329-333](crates/gcode/src/commands/codewiki/text/sanitize.rs#L329-L333)

</details>

# crates/gcode/src/commands/codewiki/text/sanitize.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

Sanitizes link-like text in CodeWiki content by scanning Markdown, identifying link and code ranges, and replacing unsafe or literal links with neutralized inline-code text. `sanitize_model_markdown_links` is the top-level entry point for model text, while `neutralize_symbol_purpose_links` combines Markdown-link and wikilink detection, skips code spans and fenced code blocks, and applies the collected replacements. The helper functions break that work into parsing link/code ranges, finding wikilink targets, checking whether ranges overlap or are contained, classifying unsafe targets such as absolute paths or URI schemes, and building the replacement text from the original label.
[crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `sanitize_model_markdown_links` | function | `pub(super) fn sanitize_model_markdown_links(text: &str) -> String {` | `sanitize_model_markdown_links [function]` | `ecb7b1b5-c702-56ff-ae9c-0b1ed393ad12` | 7-10 [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10] | Indexed function `sanitize_model_markdown_links` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10] |
| `neutralize_symbol_purpose_links` | function | `pub(crate) fn neutralize_symbol_purpose_links(text: &str) -> String {` | `neutralize_symbol_purpose_links [function]` | `db6bcba6-bb62-5c6c-a896-81e73ccbcd87` | 12-17 [crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17] | Indexed function `neutralize_symbol_purpose_links` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17] |
| `markdown_link_replacements` | function | `fn markdown_link_replacements(text: &str) -> Vec<Replacement> {` | `markdown_link_replacements [function]` | `9211fd49-090a-5e0f-9001-a4571c881563` | 19-27 [crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27] | Indexed function `markdown_link_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27] |
| `markdown_code_ranges` | function | `fn markdown_code_ranges(text: &str) -> Vec<Range<usize>> {` | `markdown_code_ranges [function]` | `55cf6a57-0936-5e0c-bd7f-3782705320b3` | 29-37 [crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37] | Indexed function `markdown_code_ranges` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37] |
| `wikilink_replacements` | function | `fn wikilink_replacements(text: &str, code_ranges: &[Range<usize>]) -> Vec<Replacement> {` | `wikilink_replacements [function]` | `b6b139f4-73a9-5448-9a34-b2d859d41518` | 39-62 [crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62] | Indexed function `wikilink_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62] |
| `replacement_for_range` | function | `fn replacement_for_range(text: &str, range: Range<usize>) -> Replacement {` | `replacement_for_range [function]` | `796b0f08-23b8-5038-8890-4d75602e8f92` | 64-69 [crates/gcode/src/commands/codewiki/text/sanitize.rs:64-69] | Indexed function `replacement_for_range` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:64-69] |
| `range_contains` | function | `fn range_contains(ranges: &[Range<usize>], index: usize) -> bool {` | `range_contains [function]` | `cb4f7495-89f3-513f-b67a-1b4b01a072b1` | 71-75 [crates/gcode/src/commands/codewiki/text/sanitize.rs:71-75] | Indexed function `range_contains` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:71-75] |
| `range_overlaps` | function | `fn range_overlaps(ranges: &[Range<usize>], candidate: Range<usize>) -> bool {` | `range_overlaps [function]` | `3f648b8a-1625-530f-a2ed-b5627efa58bb` | 77-81 [crates/gcode/src/commands/codewiki/text/sanitize.rs:77-81] | Indexed function `range_overlaps` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:77-81] |
| `apply_replacements` | function | `fn apply_replacements(text: &str, mut replacements: Vec<Replacement>) -> String {` | `apply_replacements [function]` | `cf9428f2-a22e-59e7-bf6c-7822e69d4393` | 83-102 [crates/gcode/src/commands/codewiki/text/sanitize.rs:83-102] | Indexed function `apply_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:83-102] |
| `LinkFrame` | class | `struct LinkFrame {` | `LinkFrame [class]` | `09affee9-e168-511f-b1e1-e20c6523556a` | 105-108 [crates/gcode/src/commands/codewiki/text/sanitize.rs:105-108] | Indexed class `LinkFrame` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:105-108] |
| `Replacement` | class | `struct Replacement {` | `Replacement [class]` | `7ae53d93-79f3-51f4-90e3-6cbf4b0b97db` | 111-114 [crates/gcode/src/commands/codewiki/text/sanitize.rs:111-114] | Indexed class `Replacement` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:111-114] |
| `unsafe_link_replacements` | function | `fn unsafe_link_replacements(text: &str) -> Vec<Replacement> {` | `unsafe_link_replacements [function]` | `7c8c580f-762a-5ed4-865f-96dec151660a` | 116-156 [crates/gcode/src/commands/codewiki/text/sanitize.rs:116-156] | Indexed function `unsafe_link_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:116-156] |
| `push_label_text` | function | `fn push_label_text(active_links: &mut [LinkFrame], value: &str) {` | `push_label_text [function]` | `d62c5e6c-5d65-5a4b-bb57-f1944c6b2c64` | 158-162 [crates/gcode/src/commands/codewiki/text/sanitize.rs:158-162] | Indexed function `push_label_text` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:158-162] |
| `is_unsafe_link_target` | function | `fn is_unsafe_link_target(target: &str) -> bool {` | `is_unsafe_link_target [function]` | `16ed05cb-f0ea-5d15-b151-f8a5bb191548` | 164-186 [crates/gcode/src/commands/codewiki/text/sanitize.rs:164-186] | Indexed function `is_unsafe_link_target` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:164-186] |
| `is_windows_absolute_path` | function | `fn is_windows_absolute_path(target: &str) -> bool {` | `is_windows_absolute_path [function]` | `b2017898-cf41-5719-973f-42e381dfec57` | 188-194 [crates/gcode/src/commands/codewiki/text/sanitize.rs:188-194] | Indexed function `is_windows_absolute_path` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:188-194] |
| `has_uri_scheme` | function | `fn has_uri_scheme(target: &str) -> bool {` | `has_uri_scheme [function]` | `485b0a91-7b90-5150-83cd-3daedfcdaa7c` | 196-206 [crates/gcode/src/commands/codewiki/text/sanitize.rs:196-206] | Indexed function `has_uri_scheme` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:196-206] |
| `contains_parent_dir_segment` | function | `fn contains_parent_dir_segment(target: &str) -> bool {` | `contains_parent_dir_segment [function]` | `509b1b6c-9fa0-50a5-9032-e7cc2466c478` | 208-211 [crates/gcode/src/commands/codewiki/text/sanitize.rs:208-211] | Indexed function `contains_parent_dir_segment` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:208-211] |
| `starts_with_ignore_ascii_case` | function | `fn starts_with_ignore_ascii_case(value: &str, prefix: &str) -> bool {` | `starts_with_ignore_ascii_case [function]` | `ed367e4e-8304-5624-82a7-279b95149d47` | 213-217 [crates/gcode/src/commands/codewiki/text/sanitize.rs:213-217] | Indexed function `starts_with_ignore_ascii_case` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:213-217] |
| `span` | function | `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {` | `span [function]` | `fbdbb4f0-9e51-5b01-ac7a-6a6b61cb5248` | 225-231 [crates/gcode/src/commands/codewiki/text/sanitize.rs:225-231] | Indexed function `span` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:225-231] |
| `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` | function | `fn ground_text_strips_absolute_markdown_links_and_keeps_valid_citations() {` | `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations [function]` | `ff81065f-9165-522c-8a33-e44eeee2f445` | 234-249 [crates/gcode/src/commands/codewiki/text/sanitize.rs:234-249] | Indexed function `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:234-249] |
| `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` | function | `fn ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback() {` | `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback [function]` | `2f77300c-c0ee-56a5-9647-a305a1ba001f` | 252-264 [crates/gcode/src/commands/codewiki/text/sanitize.rs:252-264] | Indexed function `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:252-264] |
| `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` | function | `fn strips_traversal_windows_unc_file_and_tilde_targets_to_label_text() {` | `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text [function]` | `2f3b2ef9-885f-5f2c-990c-88af4b8e53e5` | 267-279 [crates/gcode/src/commands/codewiki/text/sanitize.rs:267-279] | Indexed function `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:267-279] |
| `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` | function | `fn keeps_external_anchors_safe_relative_plain_brackets_and_code_links() {` | `keeps_external_anchors_safe_relative_plain_brackets_and_code_links [function]` | `ecbfc74a-7b8a-5df3-b07a-1a7c9d9f1d7c` | 282-293 [crates/gcode/src/commands/codewiki/text/sanitize.rs:282-293] | Indexed function `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:282-293] |
| `neutralizes_literal_wikilinks_in_symbol_purpose` | function | `fn neutralizes_literal_wikilinks_in_symbol_purpose() {` | `neutralizes_literal_wikilinks_in_symbol_purpose [function]` | `8a299454-c5ef-5f8b-81a4-2108f5e9e084` | 296-303 [crates/gcode/src/commands/codewiki/text/sanitize.rs:296-303] | Indexed function `neutralizes_literal_wikilinks_in_symbol_purpose` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:296-303] |
| `neutralizes_literal_markdown_links_in_symbol_purpose` | function | `fn neutralizes_literal_markdown_links_in_symbol_purpose() {` | `neutralizes_literal_markdown_links_in_symbol_purpose [function]` | `64ea0b9e-7a54-5e5c-bcd1-6390134c1f00` | 306-313 [crates/gcode/src/commands/codewiki/text/sanitize.rs:306-313] | Indexed function `neutralizes_literal_markdown_links_in_symbol_purpose` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:306-313] |
| `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged` | function | `fn neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged() {` | `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged [function]` | `3ff7b766-e91a-5acc-9f6e-c0ea42c8230f` | 316-326 [crates/gcode/src/commands/codewiki/text/sanitize.rs:316-326] | Indexed function `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:316-326] |
| `neutralizing_symbol_purpose_links_leaves_source_citations_plain` | function | `fn neutralizing_symbol_purpose_links_leaves_source_citations_plain() {` | `neutralizing_symbol_purpose_links_leaves_source_citations_plain [function]` | `4eb90fec-2fc4-58af-8adc-a2bd1693cec8` | 329-333 [crates/gcode/src/commands/codewiki/text/sanitize.rs:329-333] | Indexed function `neutralizing_symbol_purpose_links_leaves_source_citations_plain` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:329-333] |
