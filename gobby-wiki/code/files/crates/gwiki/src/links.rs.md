---
title: crates/gwiki/src/links.rs
type: code_file
provenance:
- file: crates/gwiki/src/links.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/links.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/links.rs` exposes 39 indexed API symbols.

## How it fits

`crates/gwiki/src/links.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `LinkKind` | type | Indexed type `LinkKind` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:4-7] |
| `WikiLink` | class | Indexed class `WikiLink` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:10-19] |
| `normalize_wiki_path` | function | Indexed function `normalize_wiki_path` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:21-23] |
| `extract_links` | function | Indexed function `extract_links` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:25-61] |
| `normalized_targets` | function | Indexed function `normalized_targets` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:63-72] |
| `parse_wikilink` | function | Indexed function `parse_wikilink` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:74-104] |
| `parse_markdown_link` | function | Indexed function `parse_markdown_link` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:106-141] |
| `split_alias` | function | Indexed function `split_alias` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:143-149] |
| `markdown_destination` | function | Indexed function `markdown_destination` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:151-166] |
| `markdown_destination_end` | function | Indexed function `markdown_destination_end` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:168-185] |
| `markdown_label_end` | function | Indexed function `markdown_label_end` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:187-202] |
| `wikilink_close_start` | function | Indexed function `wikilink_close_start` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:204-214] |
| `is_escaped` | function | Indexed function `is_escaped` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:216-225] |
| `markdown_code_ranges` | function | Indexed function `markdown_code_ranges` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:227-233] |
| `fenced_code_ranges` | function | Indexed function `fenced_code_ranges` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:235-257] |
| `inline_code_ranges` | function | Indexed function `inline_code_ranges` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:259-283] |
| `code_range_end_containing` | function | Indexed function `code_range_end_containing` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:285-289] |
| `line_end` | function | Indexed function `line_end` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:291-295] |
| `fence_marker` | function | Indexed function `fence_marker` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:297-309] |
| `fence_closes` | function | Indexed function `fence_closes` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:311-315] |
| `repeated_byte_count` | function | Indexed function `repeated_byte_count` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:317-322] |
| `matching_backtick_run` | function | Indexed function `matching_backtick_run` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:324-338] |
| `normalized_target_parts` | function | Indexed function `normalized_target_parts` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:340-342] |
| `wikilink_target_parts` | function | Indexed function `wikilink_target_parts` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:348-350] |
| `normalized_target_parts_with` | function | Indexed function `normalized_target_parts_with` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:352-383] |
| `collapse_repeated_slashes` | function | Indexed function `collapse_repeated_slashes` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:385-400] |
| `is_url_like_target` | function | Indexed function `is_url_like_target` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:402-406] |
| `non_empty` | function | Indexed function `non_empty` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:408-414] |
| `is_image_marker` | function | Indexed function `is_image_marker` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:416-418] |
| `next_char_len` | function | Indexed function `next_char_len` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:420-422] |
| `extracts_all_link_shapes` | function | Indexed function `extracts_all_link_shapes` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:429-468] |
| `wikilink_targets_keep_md_suffix_as_page_name` | function | Indexed function `wikilink_targets_keep_md_suffix_as_page_name` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:471-488] |
| `url_like_targets_are_not_normalized_as_vault_paths` | function | Indexed function `url_like_targets_are_not_normalized_as_vault_paths` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:491-500] |
| `markdown_links_accept_balanced_parentheses_in_destinations` | function | Indexed function `markdown_links_accept_balanced_parentheses_in_destinations` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:503-508] |
| `markdown_link_labels_ignore_escaped_brackets` | function | Indexed function `markdown_link_labels_ignore_escaped_brackets` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:511-517] |
| `markdown_link_labels_accept_nested_brackets` | function | Indexed function `markdown_link_labels_accept_nested_brackets` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:520-526] |
| `wikilinks_ignore_escaped_closing_brackets` | function | Indexed function `wikilinks_ignore_escaped_closing_brackets` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:529-536] |
| `links_ignore_code_spans_and_fences` | function | Indexed function `links_ignore_code_spans_and_fences` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:539-553] |
| `inline_code_inside_fenced_blocks_is_excluded` | function | Indexed function `inline_code_inside_fenced_blocks_is_excluded` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:556-567] |

