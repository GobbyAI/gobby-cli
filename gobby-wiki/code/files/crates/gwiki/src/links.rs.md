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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/links.rs:4-7](crates/gwiki/src/links.rs#L4-L7), [crates/gwiki/src/links.rs:10-19](crates/gwiki/src/links.rs#L10-L19), [crates/gwiki/src/links.rs:21-23](crates/gwiki/src/links.rs#L21-L23), [crates/gwiki/src/links.rs:25-61](crates/gwiki/src/links.rs#L25-L61), [crates/gwiki/src/links.rs:63-72](crates/gwiki/src/links.rs#L63-L72), [crates/gwiki/src/links.rs:74-104](crates/gwiki/src/links.rs#L74-L104), [crates/gwiki/src/links.rs:106-141](crates/gwiki/src/links.rs#L106-L141), [crates/gwiki/src/links.rs:143-149](crates/gwiki/src/links.rs#L143-L149), [crates/gwiki/src/links.rs:151-166](crates/gwiki/src/links.rs#L151-L166), [crates/gwiki/src/links.rs:168-185](crates/gwiki/src/links.rs#L168-L185), [crates/gwiki/src/links.rs:187-202](crates/gwiki/src/links.rs#L187-L202), [crates/gwiki/src/links.rs:204-214](crates/gwiki/src/links.rs#L204-L214), [crates/gwiki/src/links.rs:216-225](crates/gwiki/src/links.rs#L216-L225), [crates/gwiki/src/links.rs:227-233](crates/gwiki/src/links.rs#L227-L233), [crates/gwiki/src/links.rs:235-257](crates/gwiki/src/links.rs#L235-L257), [crates/gwiki/src/links.rs:259-283](crates/gwiki/src/links.rs#L259-L283), [crates/gwiki/src/links.rs:285-289](crates/gwiki/src/links.rs#L285-L289), [crates/gwiki/src/links.rs:291-295](crates/gwiki/src/links.rs#L291-L295), [crates/gwiki/src/links.rs:297-309](crates/gwiki/src/links.rs#L297-L309), [crates/gwiki/src/links.rs:311-315](crates/gwiki/src/links.rs#L311-L315), [crates/gwiki/src/links.rs:317-322](crates/gwiki/src/links.rs#L317-L322), [crates/gwiki/src/links.rs:324-338](crates/gwiki/src/links.rs#L324-L338), [crates/gwiki/src/links.rs:340-342](crates/gwiki/src/links.rs#L340-L342), [crates/gwiki/src/links.rs:348-350](crates/gwiki/src/links.rs#L348-L350), [crates/gwiki/src/links.rs:352-383](crates/gwiki/src/links.rs#L352-L383), [crates/gwiki/src/links.rs:385-400](crates/gwiki/src/links.rs#L385-L400), [crates/gwiki/src/links.rs:402-406](crates/gwiki/src/links.rs#L402-L406), [crates/gwiki/src/links.rs:408-414](crates/gwiki/src/links.rs#L408-L414), [crates/gwiki/src/links.rs:416-418](crates/gwiki/src/links.rs#L416-L418), [crates/gwiki/src/links.rs:420-422](crates/gwiki/src/links.rs#L420-L422), [crates/gwiki/src/links.rs:429-468](crates/gwiki/src/links.rs#L429-L468), [crates/gwiki/src/links.rs:471-488](crates/gwiki/src/links.rs#L471-L488), [crates/gwiki/src/links.rs:491-500](crates/gwiki/src/links.rs#L491-L500), [crates/gwiki/src/links.rs:503-508](crates/gwiki/src/links.rs#L503-L508), [crates/gwiki/src/links.rs:511-517](crates/gwiki/src/links.rs#L511-L517), [crates/gwiki/src/links.rs:520-526](crates/gwiki/src/links.rs#L520-L526), [crates/gwiki/src/links.rs:529-536](crates/gwiki/src/links.rs#L529-L536), [crates/gwiki/src/links.rs:539-553](crates/gwiki/src/links.rs#L539-L553), [crates/gwiki/src/links.rs:556-567](crates/gwiki/src/links.rs#L556-L567)

</details>

# crates/gwiki/src/links.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements link detection and normalization for wiki-style markdown content. It defines `LinkKind` and `WikiLink` to represent extracted links, then provides `extract_links` plus helpers to scan markdown while skipping code spans/fenced blocks, parse `[[wikilink]]` and standard markdown links, split aliases and anchors, normalize targets into vault paths, and mark whether each link matches a known target.
[crates/gwiki/src/links.rs:4-7]
[crates/gwiki/src/links.rs:10-19]
[crates/gwiki/src/links.rs:21-23]
[crates/gwiki/src/links.rs:25-61]
[crates/gwiki/src/links.rs:63-72]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `LinkKind` | type | `pub enum LinkKind {` | `LinkKind [type]` | `c3305584-8b3b-54da-8949-e1ec856a8e49` | 4-7 [crates/gwiki/src/links.rs:4-7] | Indexed type `LinkKind` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:4-7] |
| `WikiLink` | class | `pub struct WikiLink {` | `WikiLink [class]` | `36972954-71f7-5474-92ce-993dd5151ff7` | 10-19 [crates/gwiki/src/links.rs:10-19] | Indexed class `WikiLink` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:10-19] |
| `normalize_wiki_path` | function | `pub fn normalize_wiki_path(target: &str) -> String {` | `normalize_wiki_path [function]` | `a1a6546d-bf12-5ec0-8d25-4f069ed07d26` | 21-23 [crates/gwiki/src/links.rs:21-23] | Indexed function `normalize_wiki_path` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:21-23] |
| `extract_links` | function | `pub fn extract_links<I, S>(markdown: &str, known_targets: I) -> Vec<WikiLink>` | `extract_links [function]` | `b8d9e017-7187-5418-baaf-cd2c4cff6c5a` | 25-61 [crates/gwiki/src/links.rs:25-61] | Indexed function `extract_links` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:25-61] |
| `normalized_targets` | function | `pub fn normalized_targets<I, S>(targets: I) -> BTreeSet<String>` | `normalized_targets [function]` | `e416dab8-27ae-5a21-9637-278bd45d8f25` | 63-72 [crates/gwiki/src/links.rs:63-72] | Indexed function `normalized_targets` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:63-72] |
| `parse_wikilink` | function | `fn parse_wikilink(` | `parse_wikilink [function]` | `606574e6-ea90-52b9-b6f2-d85598c75d6c` | 74-104 [crates/gwiki/src/links.rs:74-104] | Indexed function `parse_wikilink` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:74-104] |
| `parse_markdown_link` | function | `fn parse_markdown_link(` | `parse_markdown_link [function]` | `c79e8999-9f5b-5d9b-91b0-a2fb5450f159` | 106-141 [crates/gwiki/src/links.rs:106-141] | Indexed function `parse_markdown_link` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:106-141] |
| `split_alias` | function | `fn split_alias(value: &str, delimiter: char) -> (&str, Option<String>) {` | `split_alias [function]` | `96df9446-3bf8-5a46-9e5b-9f317b5d7ec9` | 143-149 [crates/gwiki/src/links.rs:143-149] | Indexed function `split_alias` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:143-149] |
| `markdown_destination` | function | `fn markdown_destination(value: &str) -> Option<String> {` | `markdown_destination [function]` | `3c91cd41-8c36-5e34-92c5-0f755d8eb9ab` | 151-166 [crates/gwiki/src/links.rs:151-166] | Indexed function `markdown_destination` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:151-166] |
| `markdown_destination_end` | function | `fn markdown_destination_end(markdown: &str, start: usize) -> Option<usize> {` | `markdown_destination_end [function]` | `34bf769d-a7f1-5e72-919c-43b4b2654ae0` | 168-185 [crates/gwiki/src/links.rs:168-185] | Indexed function `markdown_destination_end` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:168-185] |
| `markdown_label_end` | function | `fn markdown_label_end(markdown: &str, start: usize) -> Option<usize> {` | `markdown_label_end [function]` | `6ab188cc-300a-5d65-8c14-f3405f68ff7f` | 187-202 [crates/gwiki/src/links.rs:187-202] | Indexed function `markdown_label_end` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:187-202] |
| `wikilink_close_start` | function | `fn wikilink_close_start(markdown: &str, start: usize) -> Option<usize> {` | `wikilink_close_start [function]` | `4e95c61c-26b3-59a5-b3b1-5df6ac8cc5ae` | 204-214 [crates/gwiki/src/links.rs:204-214] | Indexed function `wikilink_close_start` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:204-214] |
| `is_escaped` | function | `fn is_escaped(markdown: &str, byte_index: usize) -> bool {` | `is_escaped [function]` | `c0f68b8f-6f8b-58d5-962f-8076d60bd204` | 216-225 [crates/gwiki/src/links.rs:216-225] | Indexed function `is_escaped` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:216-225] |
| `markdown_code_ranges` | function | `fn markdown_code_ranges(markdown: &str) -> Vec<(usize, usize)> {` | `markdown_code_ranges [function]` | `24c5c361-25b7-58c3-8c16-e8543c0cbdfa` | 227-233 [crates/gwiki/src/links.rs:227-233] | Indexed function `markdown_code_ranges` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:227-233] |
| `fenced_code_ranges` | function | `fn fenced_code_ranges(markdown: &str) -> Vec<(usize, usize)> {` | `fenced_code_ranges [function]` | `f6d9beb9-db4b-538b-b6e9-b120b06cc0d2` | 235-257 [crates/gwiki/src/links.rs:235-257] | Indexed function `fenced_code_ranges` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:235-257] |
| `inline_code_ranges` | function | `fn inline_code_ranges(markdown: &str, excluded_ranges: &[(usize, usize)]) -> Vec<(usize, usize)> {` | `inline_code_ranges [function]` | `72047410-2803-52da-b051-0ef46e172a3b` | 259-283 [crates/gwiki/src/links.rs:259-283] | Indexed function `inline_code_ranges` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:259-283] |
| `code_range_end_containing` | function | `fn code_range_end_containing(ranges: &[(usize, usize)], offset: usize) -> Option<usize> {` | `code_range_end_containing [function]` | `9fd18be0-6fbd-524a-8e03-4e8f060757f0` | 285-289 [crates/gwiki/src/links.rs:285-289] | Indexed function `code_range_end_containing` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:285-289] |
| `line_end` | function | `fn line_end(markdown: &str, offset: usize) -> usize {` | `line_end [function]` | `2e80ed0e-ed6a-52af-b063-54786ff73b93` | 291-295 [crates/gwiki/src/links.rs:291-295] | Indexed function `line_end` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:291-295] |
| `fence_marker` | function | `fn fence_marker(line: &str) -> Option<(u8, usize)> {` | `fence_marker [function]` | `83b37a4f-8aac-5b5c-8dd7-54432b588ce3` | 297-309 [crates/gwiki/src/links.rs:297-309] | Indexed function `fence_marker` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:297-309] |
| `fence_closes` | function | `fn fence_closes(line: &str, marker: u8, marker_len: usize) -> bool {` | `fence_closes [function]` | `20accf3f-5aa8-5966-a364-b5895223b76c` | 311-315 [crates/gwiki/src/links.rs:311-315] | Indexed function `fence_closes` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:311-315] |
| `repeated_byte_count` | function | `fn repeated_byte_count(markdown: &str, offset: usize, byte: u8) -> usize {` | `repeated_byte_count [function]` | `551e3cbe-026b-5c3e-b7f0-5e5b1768b610` | 317-322 [crates/gwiki/src/links.rs:317-322] | Indexed function `repeated_byte_count` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:317-322] |
| `matching_backtick_run` | function | `fn matching_backtick_run(markdown: &str, start: usize, tick_count: usize) -> Option<usize> {` | `matching_backtick_run [function]` | `3c81d08a-f0ab-5f14-971a-7611374ffaad` | 324-338 [crates/gwiki/src/links.rs:324-338] | Indexed function `matching_backtick_run` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:324-338] |
| `normalized_target_parts` | function | `fn normalized_target_parts(target: &str) -> (String, Option<String>) {` | `normalized_target_parts [function]` | `f6a91923-c90c-5ae7-a965-db93f28914dd` | 340-342 [crates/gwiki/src/links.rs:340-342] | Indexed function `normalized_target_parts` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:340-342] |
| `wikilink_target_parts` | function | `fn wikilink_target_parts(target: &str) -> (String, Option<String>) {` | `wikilink_target_parts [function]` | `14d59288-d1fd-58fd-80c7-4cf7214e7a9f` | 348-350 [crates/gwiki/src/links.rs:348-350] | Indexed function `wikilink_target_parts` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:348-350] |
| `normalized_target_parts_with` | function | `fn normalized_target_parts_with(` | `normalized_target_parts_with [function]` | `78eab15c-f841-5814-9f5d-5782685fc08e` | 352-383 [crates/gwiki/src/links.rs:352-383] | Indexed function `normalized_target_parts_with` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:352-383] |
| `collapse_repeated_slashes` | function | `fn collapse_repeated_slashes(value: &str) -> String {` | `collapse_repeated_slashes [function]` | `32039dfe-4eb0-5063-ab36-750cec5249f5` | 385-400 [crates/gwiki/src/links.rs:385-400] | Indexed function `collapse_repeated_slashes` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:385-400] |
| `is_url_like_target` | function | `fn is_url_like_target(target: &str) -> bool {` | `is_url_like_target [function]` | `a2da1f62-1649-51d8-90b3-c9810edf6e4a` | 402-406 [crates/gwiki/src/links.rs:402-406] | Indexed function `is_url_like_target` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:402-406] |
| `non_empty` | function | `fn non_empty(value: &str) -> Option<String> {` | `non_empty [function]` | `b6f5f6d5-3a96-5482-9d2a-0c31e80aeb3d` | 408-414 [crates/gwiki/src/links.rs:408-414] | Indexed function `non_empty` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:408-414] |
| `is_image_marker` | function | `fn is_image_marker(markdown: &str, offset: usize) -> bool {` | `is_image_marker [function]` | `45e88573-2f19-513e-9f17-fa75d0059659` | 416-418 [crates/gwiki/src/links.rs:416-418] | Indexed function `is_image_marker` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:416-418] |
| `next_char_len` | function | `fn next_char_len(markdown: &str, offset: usize) -> usize {` | `next_char_len [function]` | `d2d4970c-6517-5660-ba7a-b71bb23ba0be` | 420-422 [crates/gwiki/src/links.rs:420-422] | Indexed function `next_char_len` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:420-422] |
| `extracts_all_link_shapes` | function | `fn extracts_all_link_shapes() {` | `extracts_all_link_shapes [function]` | `ac5536fe-f46b-507e-817f-b271feb6ff96` | 429-468 [crates/gwiki/src/links.rs:429-468] | Indexed function `extracts_all_link_shapes` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:429-468] |
| `wikilink_targets_keep_md_suffix_as_page_name` | function | `fn wikilink_targets_keep_md_suffix_as_page_name() {` | `wikilink_targets_keep_md_suffix_as_page_name [function]` | `e5ee12fc-96a8-563f-8f8f-9e280a7a1542` | 471-488 [crates/gwiki/src/links.rs:471-488] | Indexed function `wikilink_targets_keep_md_suffix_as_page_name` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:471-488] |
| `url_like_targets_are_not_normalized_as_vault_paths` | function | `fn url_like_targets_are_not_normalized_as_vault_paths() {` | `url_like_targets_are_not_normalized_as_vault_paths [function]` | `69b76f87-ae9d-50d9-8e46-7a37974ee86e` | 491-500 [crates/gwiki/src/links.rs:491-500] | Indexed function `url_like_targets_are_not_normalized_as_vault_paths` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:491-500] |
| `markdown_links_accept_balanced_parentheses_in_destinations` | function | `fn markdown_links_accept_balanced_parentheses_in_destinations() {` | `markdown_links_accept_balanced_parentheses_in_destinations [function]` | `c96e9d05-5332-5f37-97b4-efc508835842` | 503-508 [crates/gwiki/src/links.rs:503-508] | Indexed function `markdown_links_accept_balanced_parentheses_in_destinations` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:503-508] |
| `markdown_link_labels_ignore_escaped_brackets` | function | `fn markdown_link_labels_ignore_escaped_brackets() {` | `markdown_link_labels_ignore_escaped_brackets [function]` | `f394b649-f6da-5670-a482-9b7c80913b45` | 511-517 [crates/gwiki/src/links.rs:511-517] | Indexed function `markdown_link_labels_ignore_escaped_brackets` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:511-517] |
| `markdown_link_labels_accept_nested_brackets` | function | `fn markdown_link_labels_accept_nested_brackets() {` | `markdown_link_labels_accept_nested_brackets [function]` | `650d1fd5-e516-5b3d-82b4-2573b100715b` | 520-526 [crates/gwiki/src/links.rs:520-526] | Indexed function `markdown_link_labels_accept_nested_brackets` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:520-526] |
| `wikilinks_ignore_escaped_closing_brackets` | function | `fn wikilinks_ignore_escaped_closing_brackets() {` | `wikilinks_ignore_escaped_closing_brackets [function]` | `6922e4e2-5135-59d7-939d-6c72d0d28591` | 529-536 [crates/gwiki/src/links.rs:529-536] | Indexed function `wikilinks_ignore_escaped_closing_brackets` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:529-536] |
| `links_ignore_code_spans_and_fences` | function | `fn links_ignore_code_spans_and_fences() {` | `links_ignore_code_spans_and_fences [function]` | `dae03354-de34-5e70-850e-8c50973b6702` | 539-553 [crates/gwiki/src/links.rs:539-553] | Indexed function `links_ignore_code_spans_and_fences` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:539-553] |
| `inline_code_inside_fenced_blocks_is_excluded` | function | `fn inline_code_inside_fenced_blocks_is_excluded() {` | `inline_code_inside_fenced_blocks_is_excluded [function]` | `969a6f0b-bdb8-5e89-9d51-a73790975521` | 556-567 [crates/gwiki/src/links.rs:556-567] | Indexed function `inline_code_inside_fenced_blocks_is_excluded` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:556-567] |
