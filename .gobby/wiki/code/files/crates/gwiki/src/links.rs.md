---
title: crates/gwiki/src/links.rs
type: code_file
provenance:
- file: crates/gwiki/src/links.rs
  ranges:
  - 4-7
  - 10-19
  - 21-23
  - 25-61
  - 63-72
  - 74-104
  - 106-141
  - 143-149
  - 151-166
  - 168-185
  - 187-202
  - 204-214
  - 216-225
  - 227-233
  - 235-257
  - 259-283
  - 285-289
  - 291-295
  - 297-309
  - 311-315
  - 317-322
  - 324-338
  - 340-342
  - 348-350
  - 352-383
  - 385-400
  - 402-406
  - 408-414
  - 416-418
  - 420-422
  - 429-468
  - 471-488
  - 491-500
  - 503-508
  - 511-517
  - 520-526
  - 529-536
  - 539-553
  - 556-567
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/links.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/links.rs` exposes 39 indexed API symbols.
[crates/gwiki/src/links.rs:4-7]
[crates/gwiki/src/links.rs:10-19]
[crates/gwiki/src/links.rs:21-23]
[crates/gwiki/src/links.rs:25-61]
[crates/gwiki/src/links.rs:63-72]

## API Symbols

- `LinkKind` (type) component `LinkKind [type]` (`c3305584-8b3b-54da-8949-e1ec856a8e49`) lines 4-7 [crates/gwiki/src/links.rs:4-7]
  - Signature: `pub enum LinkKind {`
  - Purpose: Indexed type `LinkKind` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:4-7]
- `WikiLink` (class) component `WikiLink [class]` (`36972954-71f7-5474-92ce-993dd5151ff7`) lines 10-19 [crates/gwiki/src/links.rs:10-19]
  - Signature: `pub struct WikiLink {`
  - Purpose: WikiLink is a struct representing a parsed wiki hyperlink with its target, normalized form, optional anchor and alias, byte offsets, and resolution state. [crates/gwiki/src/links.rs:10-19]
- `normalize_wiki_path` (function) component `normalize_wiki_path [function]` (`a1a6546d-bf12-5ec0-8d25-4f069ed07d26`) lines 21-23 [crates/gwiki/src/links.rs:21-23]
  - Signature: `pub fn normalize_wiki_path(target: &str) -> String {`
  - Purpose: Normalizes a wiki path string by delegating to `normalized_target_parts()` and returning the first element of the resulting tuple. [crates/gwiki/src/links.rs:21-23]
- `extract_links` (function) component `extract_links [function]` (`b8d9e017-7187-5418-baaf-cd2c4cff6c5a`) lines 25-61 [crates/gwiki/src/links.rs:25-61]
  - Signature: `pub fn extract_links<I, S>(markdown: &str, known_targets: I) -> Vec<WikiLink>`
  - Purpose: Extracts WikiLink objects from markdown by parsing wikilinks (`[[...]]`) and markdown-style links (`[...]`) while skipping code blocks and validating targets against a known set. [crates/gwiki/src/links.rs:25-61]
- `normalized_targets` (function) component `normalized_targets [function]` (`e416dab8-27ae-5a21-9637-278bd45d8f25`) lines 63-72 [crates/gwiki/src/links.rs:63-72]
  - Signature: `pub fn normalized_targets<I, S>(targets: I) -> BTreeSet<String>`
  - Purpose: Converts an iterable of string-like items into a deduplicated, sorted `BTreeSet<String>` by applying wiki path normalization to each element. [crates/gwiki/src/links.rs:63-72]
- `parse_wikilink` (function) component `parse_wikilink [function]` (`606574e6-ea90-52b9-b6f2-d85598c75d6c`) lines 74-104 [crates/gwiki/src/links.rs:74-104]
  - Signature: `fn parse_wikilink(`
  - Purpose: Parses a markdown wikilink at a given byte position, extracting and normalizing the target (with anchor), optional alias, and resolving against known targets, returning a WikiLink structure with the byte end position. [crates/gwiki/src/links.rs:74-104]
- `parse_markdown_link` (function) component `parse_markdown_link [function]` (`c79e8999-9f5b-5d9b-91b0-a2fb5450f159`) lines 106-141 [crates/gwiki/src/links.rs:106-141]
  - Signature: `fn parse_markdown_link(`
  - Purpose: Parses a markdown-style link `[label](destination)` at a given byte offset, normalizes the target with anchor extraction, validates it against a known targets set, and returns a WikiLink structure with complete metadata and resolution status. [crates/gwiki/src/links.rs:106-141]
- `split_alias` (function) component `split_alias [function]` (`96df9446-3bf8-5a46-9e5b-9f317b5d7ec9`) lines 143-149 [crates/gwiki/src/links.rs:143-149]
  - Signature: `fn split_alias(value: &str, delimiter: char) -> (&str, Option<String>) {`
  - Purpose: Splits a string at the first occurrence of a delimiter, returning the left portion as a string slice and the trimmed right portion as an `Option<String>` (or `None` if no delimiter exists or the right portion is empty). [crates/gwiki/src/links.rs:143-149]
- `markdown_destination` (function) component `markdown_destination [function]` (`3c91cd41-8c36-5e34-92c5-0f755d8eb9ab`) lines 151-166 [crates/gwiki/src/links.rs:151-166]
  - Signature: `fn markdown_destination(value: &str) -> Option<String> {`
  - Purpose: Extracts a non-empty Markdown link destination from the input string, supporting both angle-bracket-enclosed (`<dest>`) and whitespace-delimited formats. [crates/gwiki/src/links.rs:151-166]
- `markdown_destination_end` (function) component `markdown_destination_end [function]` (`34bf769d-a7f1-5e72-919c-43b4b2654ae0`) lines 168-185 [crates/gwiki/src/links.rs:168-185]
  - Signature: `fn markdown_destination_end(markdown: &str, start: usize) -> Option<usize> {`
  - Purpose: Finds the index of the closing parenthesis at nesting depth zero that terminates a markdown destination (URL), while correctly handling escape sequences and nested parentheses. [crates/gwiki/src/links.rs:168-185]
- `markdown_label_end` (function) component `markdown_label_end [function]` (`6ab188cc-300a-5d65-8c14-f3405f68ff7f`) lines 187-202 [crates/gwiki/src/links.rs:187-202]
  - Signature: `fn markdown_label_end(markdown: &str, start: usize) -> Option<usize> {`
  - Purpose: Finds the position of the closing bracket `]` that terminates a markdown label by tracking bracket nesting depth and skipping escaped characters. [crates/gwiki/src/links.rs:187-202]
- `wikilink_close_start` (function) component `wikilink_close_start [function]` (`4e95c61c-26b3-59a5-b3b1-5df6ac8cc5ae`) lines 204-214 [crates/gwiki/src/links.rs:204-214]
  - Signature: `fn wikilink_close_start(markdown: &str, start: usize) -> Option<usize> {`
  - Purpose: Returns the index of the first unescaped `]]` wikilink closing delimiter found in the markdown string starting from the given position, or None if not found. [crates/gwiki/src/links.rs:204-214]
- `is_escaped` (function) component `is_escaped [function]` (`c0f68b8f-6f8b-58d5-962f-8076d60bd204`) lines 216-225 [crates/gwiki/src/links.rs:216-225]
  - Signature: `fn is_escaped(markdown: &str, byte_index: usize) -> bool {`
  - Purpose: Returns `true` if the character at the specified byte index is escaped, determined by counting the preceding consecutive backslashes and checking if the count is odd. [crates/gwiki/src/links.rs:216-225]
- `markdown_code_ranges` (function) component `markdown_code_ranges [function]` (`24c5c361-25b7-58c3-8c16-e8543c0cbdfa`) lines 227-233 [crates/gwiki/src/links.rs:227-233]
  - Signature: `fn markdown_code_ranges(markdown: &str) -> Vec<(usize, usize)> {`
  - Purpose: Returns a sorted vector of byte offset ranges for all code regions (both fenced code blocks and inline code) in a markdown string. [crates/gwiki/src/links.rs:227-233]
- `fenced_code_ranges` (function) component `fenced_code_ranges [function]` (`f6d9beb9-db4b-538b-b6e9-b120b06cc0d2`) lines 235-257 [crates/gwiki/src/links.rs:235-257]
  - Signature: `fn fenced_code_ranges(markdown: &str) -> Vec<(usize, usize)> {`
  - Purpose: Returns byte-range tuples marking the start and end positions of all fenced code blocks in a markdown string. [crates/gwiki/src/links.rs:235-257]
- `inline_code_ranges` (function) component `inline_code_ranges [function]` (`72047410-2803-52da-b051-0ef46e172a3b`) lines 259-283 [crates/gwiki/src/links.rs:259-283]
  - Signature: `fn inline_code_ranges(markdown: &str, excluded_ranges: &[(usize, usize)]) -> Vec<(usize, usize)> {`
  - Purpose: Returns the byte-offset ranges of inline code blocks (delimited by matching backtick runs) in markdown text, excluding specified ranges and handling escaped backticks. [crates/gwiki/src/links.rs:259-283]
- `code_range_end_containing` (function) component `code_range_end_containing [function]` (`9fd18be0-6fbd-524a-8e03-4e8f060757f0`) lines 285-289 [crates/gwiki/src/links.rs:285-289]
  - Signature: `fn code_range_end_containing(ranges: &[(usize, usize)], offset: usize) -> Option<usize> {`
  - Purpose: Returns the end offset of the first range containing the given offset, or `None` if no range contains it. [crates/gwiki/src/links.rs:285-289]
- `line_end` (function) component `line_end [function]` (`2e80ed0e-ed6a-52af-b063-54786ff73b93`) lines 291-295 [crates/gwiki/src/links.rs:291-295]
  - Signature: `fn line_end(markdown: &str, offset: usize) -> usize {`
  - Purpose: Returns the byte offset immediately following the first newline character at or after the given offset, or the string length if no newline exists. [crates/gwiki/src/links.rs:291-295]
- `fence_marker` (function) component `fence_marker [function]` (`83b37a4f-8aac-5b5c-8dd7-54432b588ce3`) lines 297-309 [crates/gwiki/src/links.rs:297-309]
  - Signature: `fn fence_marker(line: &str) -> Option<(u8, usize)> {`
  - Purpose: Detects markdown code fence markers (backtick or tilde) and returns the marker character and consecutive count if found after up to 3 leading spaces with length ≥3. [crates/gwiki/src/links.rs:297-309]
- `fence_closes` (function) component `fence_closes [function]` (`20accf3f-5aa8-5966-a364-b5895223b76c`) lines 311-315 [crates/gwiki/src/links.rs:311-315]
  - Signature: `fn fence_closes(line: &str, marker: u8, marker_len: usize) -> bool {`
  - Purpose: Returns `true` if the line contains a fence marker matching the specified marker byte with a length at least equal to `marker_len`. [crates/gwiki/src/links.rs:311-315]
- `repeated_byte_count` (function) component `repeated_byte_count [function]` (`551e3cbe-026b-5c3e-b7f0-5e5b1768b610`) lines 317-322 [crates/gwiki/src/links.rs:317-322]
  - Signature: `fn repeated_byte_count(markdown: &str, offset: usize, byte: u8) -> usize {`
  - Purpose: Counts the number of consecutive bytes matching the specified value starting from the given offset in the markdown string. [crates/gwiki/src/links.rs:317-322]
- `matching_backtick_run` (function) component `matching_backtick_run [function]` (`3c81d08a-f0ab-5f14-971a-7611374ffaad`) lines 324-338 [crates/gwiki/src/links.rs:324-338]
  - Signature: `fn matching_backtick_run(markdown: &str, start: usize, tick_count: usize) -> Option<usize> {`
  - Purpose: Searches forward from a given offset in a markdown string to locate the next unescaped backtick run matching a specified count, returning its offset if found. [crates/gwiki/src/links.rs:324-338]
- `normalized_target_parts` (function) component `normalized_target_parts [function]` (`f6a91923-c90c-5ae7-a965-db93f28914dd`) lines 340-342 [crates/gwiki/src/links.rs:340-342]
  - Signature: `fn normalized_target_parts(target: &str) -> (String, Option<String>) {`
  - Purpose: This function normalizes a target string into a tuple of a primary component (String) and an optional secondary component by delegating to `normalized_target_parts_with` with a fixed `true` argument. [crates/gwiki/src/links.rs:340-342]
- `wikilink_target_parts` (function) component `wikilink_target_parts [function]` (`14d59288-d1fd-58fd-80c7-4cf7214e7a9f`) lines 348-350 [crates/gwiki/src/links.rs:348-350]
  - Signature: `fn wikilink_target_parts(target: &str) -> (String, Option<String>) {`
  - Purpose: Parses a wikilink target string into a tuple containing a normalized path component and an optional anchor component by delegating to `normalized_target_parts_with` with normalization disabled. [crates/gwiki/src/links.rs:348-350]
- `normalized_target_parts_with` (function) component `normalized_target_parts_with [function]` (`78eab15c-f841-5814-9f5d-5782685fc08e`) lines 352-383 [crates/gwiki/src/links.rs:352-383]
  - Signature: `fn normalized_target_parts_with(`
  - Purpose: Normalizes a target string by separating its anchor fragment and collapsing relative path prefixes, redundant slashes, and optionally removing markdown file extensions from non-URL paths. [crates/gwiki/src/links.rs:352-383]
- `collapse_repeated_slashes` (function) component `collapse_repeated_slashes [function]` (`32039dfe-4eb0-5063-ab36-750cec5249f5`) lines 385-400 [crates/gwiki/src/links.rs:385-400]
  - Signature: `fn collapse_repeated_slashes(value: &str) -> String {`
  - Purpose: Collapses consecutive forward slashes into single slashes by skipping any slash character that immediately follows another slash. [crates/gwiki/src/links.rs:385-400]
- `is_url_like_target` (function) component `is_url_like_target [function]` (`a2da1f62-1649-51d8-90b3-c9810edf6e4a`) lines 402-406 [crates/gwiki/src/links.rs:402-406]
  - Signature: `fn is_url_like_target(target: &str) -> bool {`
  - Purpose: Returns `true` if the target string contains an absolute URI scheme (`://`), is protocol-relative (`//`), or is a Windows UNC path (`\\`), indicating it should be preserved as-is rather than normalized as a vault-relative path. [crates/gwiki/src/links.rs:402-406]
- `non_empty` (function) component `non_empty [function]` (`b6f5f6d5-3a96-5482-9d2a-0c31e80aeb3d`) lines 408-414 [crates/gwiki/src/links.rs:408-414]
  - Signature: `fn non_empty(value: &str) -> Option<String> {`
  - Purpose: Converts a non-empty string reference to `Some(String)` containing an owned copy, or returns `None` if the input is empty. [crates/gwiki/src/links.rs:408-414]
- `is_image_marker` (function) component `is_image_marker [function]` (`45e88573-2f19-513e-9f17-fa75d0059659`) lines 416-418 [crates/gwiki/src/links.rs:416-418]
  - Signature: `fn is_image_marker(markdown: &str, offset: usize) -> bool {`
  - Purpose: Checks whether the byte immediately preceding the given offset in a markdown string is an exclamation mark, indicating the start of an image link syntax. [crates/gwiki/src/links.rs:416-418]
- `next_char_len` (function) component `next_char_len [function]` (`d2d4970c-6517-5660-ba7a-b71bb23ba0be`) lines 420-422 [crates/gwiki/src/links.rs:420-422]
  - Signature: `fn next_char_len(markdown: &str, offset: usize) -> usize {`
  - Purpose: Returns the UTF-8 byte length of the character at the specified offset in the string, or 1 if no character exists at that position. [crates/gwiki/src/links.rs:420-422]
- `extracts_all_link_shapes` (function) component `extracts_all_link_shapes [function]` (`ac5536fe-f46b-507e-817f-b271feb6ff96`) lines 429-468 [crates/gwiki/src/links.rs:429-468]
  - Signature: `fn extracts_all_link_shapes() {`
  - Purpose: This test verifies that `extract_links()` correctly extracts, parses, and classifies both wikilink and markdown hyperlink formats while normalizing targets, tracking aliases, and resolving references against a known path list. [crates/gwiki/src/links.rs:429-468]
- `wikilink_targets_keep_md_suffix_as_page_name` (function) component `wikilink_targets_keep_md_suffix_as_page_name [function]` (`e5ee12fc-96a8-563f-8f8f-9e280a7a1542`) lines 471-488 [crates/gwiki/src/links.rs:471-488]
  - Signature: `fn wikilink_targets_keep_md_suffix_as_page_name() {`
  - Purpose: This test verifies that `extract_links` correctly normalizes and resolves wikilinks and markdown links pointing to files with double `.md.md` extensions down to single `.md` page name targets. [crates/gwiki/src/links.rs:471-488]
- `url_like_targets_are_not_normalized_as_vault_paths` (function) component `url_like_targets_are_not_normalized_as_vault_paths [function]` (`69b76f87-ae9d-50d9-8e46-7a37974ee86e`) lines 491-500 [crates/gwiki/src/links.rs:491-500]
  - Signature: `fn url_like_targets_are_not_normalized_as_vault_paths() {`
  - Purpose: This test verifies that `normalize_wiki_path` preserves URL-like and UNC network paths (with leading `//` or `\\`) rather than normalizing them as vault-relative paths, converting Windows UNC syntax to forward slashes while maintaining their network-path status. [crates/gwiki/src/links.rs:491-500]
- `markdown_links_accept_balanced_parentheses_in_destinations` (function) component `markdown_links_accept_balanced_parentheses_in_destinations [function]` (`c96e9d05-5332-5f37-97b4-efc508835842`) lines 503-508 [crates/gwiki/src/links.rs:503-508]
  - Signature: `fn markdown_links_accept_balanced_parentheses_in_destinations() {`
  - Purpose: Tests that markdown link extraction correctly parses link destinations containing balanced parentheses, producing the expected target and normalized target values. [crates/gwiki/src/links.rs:503-508]
- `markdown_link_labels_ignore_escaped_brackets` (function) component `markdown_link_labels_ignore_escaped_brackets [function]` (`f394b649-f6da-5670-a482-9b7c80913b45`) lines 511-517 [crates/gwiki/src/links.rs:511-517]
  - Signature: `fn markdown_link_labels_ignore_escaped_brackets() {`
  - Purpose: This unit test verifies that `extract_links()` correctly parses markdown links with escaped closing brackets in the label portion, extracting the proper target URL while preserving the escaped bracket in the alias. [crates/gwiki/src/links.rs:511-517]
- `markdown_link_labels_accept_nested_brackets` (function) component `markdown_link_labels_accept_nested_brackets [function]` (`650d1fd5-e516-5b3d-82b4-2573b100715b`) lines 520-526 [crates/gwiki/src/links.rs:520-526]
  - Signature: `fn markdown_link_labels_accept_nested_brackets() {`
  - Purpose: Verifies that the `extract_links` function correctly parses markdown links with nested square brackets in the link label portion. [crates/gwiki/src/links.rs:520-526]
- `wikilinks_ignore_escaped_closing_brackets` (function) component `wikilinks_ignore_escaped_closing_brackets [function]` (`6922e4e2-5135-59d7-939d-6c72d0d28591`) lines 529-536 [crates/gwiki/src/links.rs:529-536]
  - Signature: `fn wikilinks_ignore_escaped_closing_brackets() {`
  - Purpose: This test verifies that the wikilink parser correctly treats escaped closing brackets (`\]]`) as literal content within links rather than as link terminators. [crates/gwiki/src/links.rs:529-536]
- `links_ignore_code_spans_and_fences` (function) component `links_ignore_code_spans_and_fences [function]` (`dae03354-de34-5e70-850e-8c50973b6702`) lines 539-553 [crates/gwiki/src/links.rs:539-553]
  - Signature: `fn links_ignore_code_spans_and_fences() {`
  - Purpose: This test verifies that `extract_links` correctly ignores wiki-style and markdown links appearing within inline code spans and fenced code blocks, extracting only those from unescaped markdown content. [crates/gwiki/src/links.rs:539-553]
- `inline_code_inside_fenced_blocks_is_excluded` (function) component `inline_code_inside_fenced_blocks_is_excluded [function]` (`969a6f0b-bdb8-5e89-9d51-a73790975521`) lines 556-567 [crates/gwiki/src/links.rs:556-567]
  - Signature: `fn inline_code_inside_fenced_blocks_is_excluded() {`
  - Purpose: # Summary

Tests that the `extract_links` function excludes wiki-style link patterns (`[[...]]`) contained within fenced code blocks while still extracting matching patterns from unenclosed content. [crates/gwiki/src/links.rs:556-567]

