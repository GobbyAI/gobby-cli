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

`crates/gwiki/src/links.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `LinkKind` | type | Indexed type `LinkKind` in `crates/gwiki/src/links.rs`. [crates/gwiki/src/links.rs:4-7] |
| `WikiLink` | class | WikiLink is a struct representing a parsed wiki hyperlink with normalized target resolution, optional anchor and display alias, byte offset positions, and resolution status. [crates/gwiki/src/links.rs:10-19] |
| `normalize_wiki_path` | function | Normalizes a wiki path string by extracting the first element of the tuple returned from 'normalized_target_parts'. [crates/gwiki/src/links.rs:21-23] |
| `extract_links` | function | Extracts WikiLink ('`[[...]]`') and Markdown-formatted link references from markdown text while excluding matches within code ranges and validating against known targets. [crates/gwiki/src/links.rs:25-61] |
| `normalized_targets` | function | This function transforms an iterable of string references into a lexicographically sorted, deduplicated set of normalized wiki paths. [crates/gwiki/src/links.rs:63-72] |
| `parse_wikilink` | function | # Summary Parses a wikilink from markdown at a given byte position, extracts and normalizes the target and alias components, resolves the target against a known targets set, and returns a WikiLink struct with full metadata. [crates/gwiki/src/links.rs:74-104] |
| `parse_markdown_link` | function | Parses markdown link syntax '`[label](destination)`' from a given byte offset, validates the extracted destination against a set of known targets, and returns a 'WikiLink' structure containing the parsed components, normalized target, anchor, and ending byte position. [crates/gwiki/src/links.rs:106-141] |
| `split_alias` | function | Partitions a string at the first delimiter occurrence into a target reference and an optional trimmed alias string, defaulting to the whole input paired with 'None' if no delimiter is found. [crates/gwiki/src/links.rs:143-149] |
| `markdown_destination` | function | Extracts a markdown link destination by parsing angle-bracket-enclosed content ('<...>') or the first whitespace-delimited token, returning the non-empty trimmed result or 'None'. [crates/gwiki/src/links.rs:151-166] |
| `markdown_destination_end` | function | This function finds the index of the closing parenthesis that terminates a parenthesis-delimited sequence starting at position 'start', accounting for escaped characters and nested parentheses through depth tracking. [crates/gwiki/src/links.rs:168-185] |
| `markdown_label_end` | function | Returns the index of the closing bracket ']' that terminates a markdown label starting at the given position, while accounting for nested bracket depth and escaped characters. [crates/gwiki/src/links.rs:187-202] |
| `wikilink_close_start` | function | This function returns the byte index of the first unescaped ']]' sequence in a markdown string starting from a given position, or 'None' if not found. [crates/gwiki/src/links.rs:204-214] |
| `is_escaped` | function | Returns true if the character at the given byte index is escaped by an odd number of consecutive preceding backslashes. [crates/gwiki/src/links.rs:216-225] |
| `markdown_code_ranges` | function | Identifies and returns a sorted vector of (start, end) byte-position tuples for all fenced and inline code regions in a markdown string. [crates/gwiki/src/links.rs:227-233] |
| `fenced_code_ranges` | function | Returns byte-offset ranges of all fenced code blocks in a markdown string. [crates/gwiki/src/links.rs:235-257] |
| `inline_code_ranges` | function | This function identifies and returns the byte offset ranges of all backtick-delimited inline code blocks in a markdown string while excluding specified ranges and handling escaped backticks. [crates/gwiki/src/links.rs:259-283] |
| `code_range_end_containing` | function | Returns the end bound of the first range containing the given offset, or 'None' if no range contains it. [crates/gwiki/src/links.rs:285-289] |
| `line_end` | function | Returns the position immediately after the next newline character starting from the given offset, or the length of the markdown string if no newline is found. [crates/gwiki/src/links.rs:291-295] |
| `fence_marker` | function | Identifies a Markdown code fence marker (backtick or tilde) occurring at least 3 consecutive times after up to 3 leading spaces, returning the marker character and its count. [crates/gwiki/src/links.rs:297-309] |
| `fence_closes` | function | Returns 'true' if and only if the provided line contains a fence marker matching the specified marker byte with length at least 'marker_len'. [crates/gwiki/src/links.rs:311-315] |
| `repeated_byte_count` | function | Returns the count of consecutive occurrences of a specified byte value starting from a given offset within the input string's byte representation. [crates/gwiki/src/links.rs:317-322] |
| `matching_backtick_run` | function | Searches for and returns the byte offset of the first unescaped run of exactly 'tick_count' consecutive backticks in 'markdown' starting from position 'start', or 'None' if no match is found. [crates/gwiki/src/links.rs:324-338] |
| `normalized_target_parts` | function | This function normalizes a target string into a tuple of '(String, Option<String>)' by delegating to 'normalized_target_parts_with' with a fixed 'true' parameter. [crates/gwiki/src/links.rs:340-342] |
| `wikilink_target_parts` | function | Parses a wikilink target string and returns its normalized component parts as a tuple of a required String and an optional String by delegating to 'normalized_target_parts_with(target, false)'. [crates/gwiki/src/links.rs:348-350] |

_6 more symbol(s) not shown — run `gcode outline crates/gwiki/src/links.rs` for the full list._

_Verified by 9 in-file unit tests._

