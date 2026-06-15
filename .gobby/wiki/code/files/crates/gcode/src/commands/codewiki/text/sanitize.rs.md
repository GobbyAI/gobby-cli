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

# crates/gcode/src/commands/codewiki/text/sanitize.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

Utilities for sanitizing codewiki text by neutralizing link-like syntax before it is rendered or grounded. `sanitize_model_markdown_links` replaces only unsafe Markdown links, while `neutralize_symbol_purpose_links` first marks Markdown code spans/blocks, then collects Markdown links and `[[wikilinks]]` outside those code ranges and rewrites them into inline-code labels. The helper functions parse Markdown with `pulldown_cmark`, detect unsafe targets and overlapping spans, and apply all collected `Replacement`s in a single pass so the final text keeps readable labels but strips or neutralizes link destinations.
[crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62]

## API Symbols

- `sanitize_model_markdown_links` (function) component `sanitize_model_markdown_links [function]` (`ecb7b1b5-c702-56ff-ae9c-0b1ed393ad12`) lines 7-10 [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10]
  - Signature: `pub(super) fn sanitize_model_markdown_links(text: &str) -> String {`
  - Purpose: Creates a sanitized copy of 'text' by computing unsafe markdown link replacements and applying them to the input string. [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10]
- `neutralize_symbol_purpose_links` (function) component `neutralize_symbol_purpose_links [function]` (`db6bcba6-bb62-5c6c-a896-81e73ccbcd87`) lines 12-17 [crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17]
  - Signature: `pub(crate) fn neutralize_symbol_purpose_links(text: &str) -> String {`
  - Purpose: Returns a new string with markdown and wikilink targets inside the input neutralized by collecting code spans, generating link replacements, and applying all replacements to the original text. [crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17]
- `markdown_link_replacements` (function) component `markdown_link_replacements [function]` (`9211fd49-090a-5e0f-9001-a4571c881563`) lines 19-27 [crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27]
  - Signature: `fn markdown_link_replacements(text: &str) -> Vec<Replacement> {`
  - Purpose: Parses the input Markdown text with 'pulldown_cmark', iterates over events with byte offsets, and collects a 'Replacement' for each 'Event::Start(Tag::Link { .. })' span. [crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27]
- `markdown_code_ranges` (function) component `markdown_code_ranges [function]` (`55cf6a57-0936-5e0c-bd7f-3782705320b3`) lines 29-37 [crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37]
  - Signature: `fn markdown_code_ranges(text: &str) -> Vec<Range<usize>> {`
  - Purpose: Returns the byte ranges of all inline code spans and fenced/indented code blocks in the input Markdown by parsing it with 'pulldown_cmark' and collecting the offsets for 'Event::Code' and 'Event::Start(Tag::CodeBlock(_))'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37]
- `wikilink_replacements` (function) component `wikilink_replacements [function]` (`b6b139f4-73a9-5448-9a34-b2d859d41518`) lines 39-62 [crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62]
  - Signature: `fn wikilink_replacements(text: &str, code_ranges: &[Range<usize>]) -> Vec<Replacement> {`
  - Purpose: Scans 'text' for '`[[...]]`' wikilink spans outside 'code_ranges', converts each non-overlapping match into a 'Replacement' via 'replacement_for_range', and returns the collected replacements. [crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62]
- `replacement_for_range` (function) component `replacement_for_range [function]` (`796b0f08-23b8-5038-8890-4d75602e8f92`) lines 64-69 [crates/gcode/src/commands/codewiki/text/sanitize.rs:64-69]
  - Signature: `fn replacement_for_range(text: &str, range: Range<usize>) -> Replacement {`
  - Purpose: Constructs a 'Replacement' by using the substring of 'text' covered by 'range' as the inline-code 'label' and storing the original 'range' unchanged. [crates/gcode/src/commands/codewiki/text/sanitize.rs:64-69]
- `range_contains` (function) component `range_contains [function]` (`cb4f7495-89f3-513f-b67a-1b4b01a072b1`) lines 71-75 [crates/gcode/src/commands/codewiki/text/sanitize.rs:71-75]
  - Signature: `fn range_contains(ranges: &[Range<usize>], index: usize) -> bool {`
  - Purpose: Returns 'true' if 'index' lies within any half-open range in 'ranges' ('range.start <= index < range.end'), otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:71-75]
- `range_overlaps` (function) component `range_overlaps [function]` (`3f648b8a-1625-530f-a2ed-b5627efa58bb`) lines 77-81 [crates/gcode/src/commands/codewiki/text/sanitize.rs:77-81]
  - Signature: `fn range_overlaps(ranges: &[Range<usize>], candidate: Range<usize>) -> bool {`
  - Purpose: Returns 'true' if any range in 'ranges' has a non-empty intersection with 'candidate' by checking whether 'range.start < candidate.end' and 'candidate.start < range.end'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:77-81]
- `apply_replacements` (function) component `apply_replacements [function]` (`cf9428f2-a22e-59e7-bf6c-7822e69d4393`) lines 83-102 [crates/gcode/src/commands/codewiki/text/sanitize.rs:83-102]
  - Signature: `fn apply_replacements(text: &str, mut replacements: Vec<Replacement>) -> String {`
  - Purpose: 'apply_replacements' sorts a list of 'Replacement's by start/end offset, then scans 'text' once to build a new string by copying untouched spans and inserting each non-overlapping replacement’s 'label', skipping any replacement whose range starts before the current cursor. [crates/gcode/src/commands/codewiki/text/sanitize.rs:83-102]
- `LinkFrame` (class) component `LinkFrame [class]` (`09affee9-e168-511f-b1e1-e20c6523556a`) lines 105-108 [crates/gcode/src/commands/codewiki/text/sanitize.rs:105-108]
  - Signature: `struct LinkFrame {`
  - Purpose: 'LinkFrame' is a Rust struct that stores a 'Range<usize>' and a 'String' label, representing a labeled span over an index range. [crates/gcode/src/commands/codewiki/text/sanitize.rs:105-108]
- `Replacement` (class) component `Replacement [class]` (`7ae53d93-79f3-51f4-90e3-6cbf4b0b97db`) lines 111-114 [crates/gcode/src/commands/codewiki/text/sanitize.rs:111-114]
  - Signature: `struct Replacement {`
  - Purpose: 'Replacement' is a struct that represents a text substitution target by pairing a byte-indexed 'Range<usize>' with a replacement 'label' string. [crates/gcode/src/commands/codewiki/text/sanitize.rs:111-114]
- `unsafe_link_replacements` (function) component `unsafe_link_replacements [function]` (`7c8c580f-762a-5ed4-865f-96dec151660a`) lines 116-156 [crates/gcode/src/commands/codewiki/text/sanitize.rs:116-156]
  - Signature: `fn unsafe_link_replacements(text: &str) -> Vec<Replacement> {`
  - Purpose: Parses the Markdown text, tracks only link spans whose destination is deemed unsafe, accumulates their rendered label text from nested events, and returns 'Replacement' records for each matched link range. [crates/gcode/src/commands/codewiki/text/sanitize.rs:116-156]
- `push_label_text` (function) component `push_label_text [function]` (`d62c5e6c-5d65-5a4b-bb57-f1944c6b2c64`) lines 158-162 [crates/gcode/src/commands/codewiki/text/sanitize.rs:158-162]
  - Signature: `fn push_label_text(active_links: &mut [LinkFrame], value: &str) {`
  - Purpose: Appends the provided 'value' string to the 'label' field of every 'LinkFrame' in the mutable slice 'active_links'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:158-162]
- `is_unsafe_link_target` (function) component `is_unsafe_link_target [function]` (`16ed05cb-f0ea-5d15-b151-f8a5bb191548`) lines 164-186 [crates/gcode/src/commands/codewiki/text/sanitize.rs:164-186]
  - Signature: `fn is_unsafe_link_target(target: &str) -> bool {`
  - Purpose: Returns 'true' for non-empty link targets that are unsafe because they use a 'file:' URI, are Windows absolute paths, or are otherwise absolute/path-traversal-like ('/', '\', '~', or '..' segments), while treating empty strings, fragment-only targets, and other URI schemes as safe. [crates/gcode/src/commands/codewiki/text/sanitize.rs:164-186]
- `is_windows_absolute_path` (function) component `is_windows_absolute_path [function]` (`b2017898-cf41-5719-973f-42e381dfec57`) lines 188-194 [crates/gcode/src/commands/codewiki/text/sanitize.rs:188-194]
  - Signature: `fn is_windows_absolute_path(target: &str) -> bool {`
  - Purpose: Returns 'true' when 'target' is at least three bytes long and matches a Windows drive-root absolute path prefix of the form '<ASCII letter>:' followed by '/' or '\'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:188-194]
- `has_uri_scheme` (function) component `has_uri_scheme [function]` (`485b0a91-7b90-5150-83cd-3daedfcdaa7c`) lines 196-206 [crates/gcode/src/commands/codewiki/text/sanitize.rs:196-206]
  - Signature: `fn has_uri_scheme(target: &str) -> bool {`
  - Purpose: Returns 'true' if 'target' contains a colon-delimited prefix whose first character is ASCII alphabetic and whose remaining characters are ASCII alphanumeric or '+', '-', or '.', indicating a syntactically valid URI scheme, otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:196-206]
- `contains_parent_dir_segment` (function) component `contains_parent_dir_segment [function]` (`509b1b6c-9fa0-50a5-9032-e7cc2466c478`) lines 208-211 [crates/gcode/src/commands/codewiki/text/sanitize.rs:208-211]
  - Signature: `fn contains_parent_dir_segment(target: &str) -> bool {`
  - Purpose: Returns 'true' if the input string’s path component, after stripping any query ('?') or fragment ('#') suffix, contains a path segment exactly equal to '..' when split on '/' or '\'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:208-211]
- `starts_with_ignore_ascii_case` (function) component `starts_with_ignore_ascii_case [function]` (`ed367e4e-8304-5624-82a7-279b95149d47`) lines 213-217 [crates/gcode/src/commands/codewiki/text/sanitize.rs:213-217]
  - Signature: `fn starts_with_ignore_ascii_case(value: &str, prefix: &str) -> bool {`
  - Purpose: Returns 'true' if 'value' has a leading substring of the same byte length as 'prefix' and that substring equals 'prefix' under ASCII case-insensitive comparison, otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:213-217]
- `span` (function) component `span [function]` (`fbdbb4f0-9e51-5b01-ac7a-6a6b61cb5248`) lines 225-231 [crates/gcode/src/commands/codewiki/text/sanitize.rs:225-231]
  - Signature: `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {`
  - Purpose: Constructs and returns a 'SourceSpan' by converting 'file' into a 'String' and populating its 'file', 'line_start', and 'line_end' fields with the provided arguments. [crates/gcode/src/commands/codewiki/text/sanitize.rs:225-231]
- `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` (function) component `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations [function]` (`ff81065f-9165-522c-8a33-e44eeee2f445`) lines 234-249 [crates/gcode/src/commands/codewiki/text/sanitize.rs:234-249]
  - Signature: `fn ground_text_strips_absolute_markdown_links_and_keeps_valid_citations() {`
  - Purpose: Verifies that 'ground_text' strips absolute Markdown links from the text while preserving valid citation spans and leaving the matching citation marker intact. [crates/gcode/src/commands/codewiki/text/sanitize.rs:234-249]
- `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` (function) component `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback [function]` (`2f77300c-c0ee-56a5-9647-a305a1ba001f`) lines 252-264 [crates/gcode/src/commands/codewiki/text/sanitize.rs:252-264]
  - Signature: `fn ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback() {`
  - Purpose: Verifies that 'ground_text' removes invalid citation markup and unsafe 'file://' links from the input, preserves the readable text, and appends the fallback grounded citation when no valid grounding is emitted. [crates/gcode/src/commands/codewiki/text/sanitize.rs:252-264]
- `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` (function) component `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text [function]` (`2f3b2ef9-885f-5f2c-990c-88af4b8e53e5`) lines 267-279 [crates/gcode/src/commands/codewiki/text/sanitize.rs:267-279]
  - Signature: `fn strips_traversal_windows_unc_file_and_tilde_targets_to_label_text() {`
  - Purpose: Verifies that 'sanitize_model_markdown_links' strips markdown link targets containing path traversal, Windows drive/UNC paths, 'file://' URLs, and '~'-prefixed paths, leaving only the link labels as plain text. [crates/gcode/src/commands/codewiki/text/sanitize.rs:267-279]
- `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` (function) component `keeps_external_anchors_safe_relative_plain_brackets_and_code_links [function]` (`ecbfc74a-7b8a-5df3-b07a-1a7c9d9f1d7c`) lines 282-293 [crates/gcode/src/commands/codewiki/text/sanitize.rs:282-293]
  - Signature: `fn keeps_external_anchors_safe_relative_plain_brackets_and_code_links() {`
  - Purpose: Verifies that 'sanitize_model_markdown_links' leaves markdown unchanged when it contains an external URL link, an in-page anchor, a relative path link, plain brackets, and bracketed local file paths inside quotes or fenced code. [crates/gcode/src/commands/codewiki/text/sanitize.rs:282-293]
- `neutralizes_literal_wikilinks_in_symbol_purpose` (function) component `neutralizes_literal_wikilinks_in_symbol_purpose [function]` (`8a299454-c5ef-5f8b-81a4-2108f5e9e084`) lines 296-303 [crates/gcode/src/commands/codewiki/text/sanitize.rs:296-303]
  - Signature: `fn neutralizes_literal_wikilinks_in_symbol_purpose() {`
  - Purpose: Verifies that 'neutralize_symbol_purpose_links' converts a literal '`[[relative_path|title]]`' wikilink-like substring into quoted prose (''`[[relative_path|title]]`'') without altering the surrounding text. [crates/gcode/src/commands/codewiki/text/sanitize.rs:296-303]
- `neutralizes_literal_markdown_links_in_symbol_purpose` (function) component `neutralizes_literal_markdown_links_in_symbol_purpose [function]` (`64ea0b9e-7a54-5e5c-bcd1-6390134c1f00`) lines 306-313 [crates/gcode/src/commands/codewiki/text/sanitize.rs:306-313]
  - Signature: `fn neutralizes_literal_markdown_links_in_symbol_purpose() {`
  - Purpose: Verifies that 'neutralize_symbol_purpose_links' rewrites a literal Markdown link in prose by surrounding the entire '`[text](path/to/page.md)`' span with single quotes. [crates/gcode/src/commands/codewiki/text/sanitize.rs:306-313]
- `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged` (function) component `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged [function]` (`3ff7b766-e91a-5acc-9f6e-c0ea42c8230f`) lines 316-326 [crates/gcode/src/commands/codewiki/text/sanitize.rs:316-326]
  - Signature: `fn neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged() {`
  - Purpose: Verifies that 'neutralize_symbol_purpose_links' leaves link-like syntax inside inline code spans and fenced code blocks unchanged. [crates/gcode/src/commands/codewiki/text/sanitize.rs:316-326]
- `neutralizing_symbol_purpose_links_leaves_source_citations_plain` (function) component `neutralizing_symbol_purpose_links_leaves_source_citations_plain [function]` (`4eb90fec-2fc4-58af-8adc-a2bd1693cec8`) lines 329-333 [crates/gcode/src/commands/codewiki/text/sanitize.rs:329-333]
  - Signature: `fn neutralizing_symbol_purpose_links_leaves_source_citations_plain() {`
  - Purpose: Verifies that 'neutralize_symbol_purpose_links' leaves a plain source citation like '' unchanged. [crates/gcode/src/commands/codewiki/text/sanitize.rs:329-333]

