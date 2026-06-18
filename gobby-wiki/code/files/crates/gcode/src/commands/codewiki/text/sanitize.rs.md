---
title: crates/gcode/src/commands/codewiki/text/sanitize.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/sanitize.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Overview

`crates/gcode/src/commands/codewiki/text/sanitize.rs` exposes 27 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/sanitize.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `sanitize_model_markdown_links` | function | Returns a new string by computing unsafe link replacements for the input text and applying them to sanitize Markdown links. [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10] |
| `neutralize_symbol_purpose_links` | function | Returns a new string with Markdown links and wikilinks in 'text' neutralized by collecting code spans to exclude, building link replacements, and applying those replacements to the original text. [crates/gcode/src/commands/codewiki/text/sanitize.rs:12-17] |
| `markdown_link_replacements` | function | Parses the input Markdown with pulldown-cmark and returns a 'Vec<Replacement>' containing one replacement for each 'Event::Start(Tag::Link { .. })' range it encounters. [crates/gcode/src/commands/codewiki/text/sanitize.rs:19-27] |
| `markdown_code_ranges` | function | Returns the byte ranges of all inline code spans and fenced/indented code blocks in the input Markdown by parsing with 'pulldown_cmark' and collecting the offsets of 'Event::Code' and 'Event::Start(Tag::CodeBlock(_))' events. [crates/gcode/src/commands/codewiki/text/sanitize.rs:29-37] |
| `wikilink_replacements` | function | Scans 'text' for '`[[...]]`' wikilink spans outside 'code_ranges', skips any start position inside code, and returns a 'Vec<Replacement>' for each non-overlapping matched range. [crates/gcode/src/commands/codewiki/text/sanitize.rs:39-62] |
| `replacement_for_range` | function | Creates a 'Replacement' whose 'label' is the inline-code rendering of the substring of 'text' at 'range', and whose 'range' field preserves the original 'Range<usize>'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:64-69] |
| `range_contains` | function | Returns 'true' if any 'Range<usize>' in 'ranges' contains 'index' using the half-open interval check 'start <= index < end', otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:71-75] |
| `range_overlaps` | function | Returns 'true' if any range in 'ranges' has a non-empty intersection with 'candidate' under half-open interval semantics ('start < other.end && other.start < end'), otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:77-81] |
| `apply_replacements` | function | Sorts non-overlapping replacements by start/end offset and builds a new string by copying unchanged text segments and splicing in each replacement’s 'label', skipping any replacement that overlaps earlier applied output. [crates/gcode/src/commands/codewiki/text/sanitize.rs:83-102] |
| `LinkFrame` | class | 'LinkFrame' is a struct that stores a byte-index range ('Range<usize>') and an associated link label ('String'). [crates/gcode/src/commands/codewiki/text/sanitize.rs:105-108] |
| `Replacement` | class | 'Replacement' is a struct that represents a labeled span in a source sequence, storing a 'Range<usize>' and an associated 'String' label. [crates/gcode/src/commands/codewiki/text/sanitize.rs:111-114] |
| `unsafe_link_replacements` | function | Parses Markdown with 'pulldown_cmark', tracks nested link frames whose destination URLs are deemed unsafe, accumulates their rendered label text from contained events, and returns 'Replacement' records for each matched unsafe link span. [crates/gcode/src/commands/codewiki/text/sanitize.rs:116-156] |
| `push_label_text` | function | Appends the provided string slice to the 'label' field of every 'LinkFrame' in the mutable slice 'active_links'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:158-162] |
| `is_unsafe_link_target` | function | Returns 'true' for trimmed link targets that are potentially dangerous local or absolute paths, including 'file:' URIs, Windows absolute paths, Unix/UNC/home-style absolute paths, and targets containing parent-directory segments, but returns 'false' for empty strings, fragment-only links, and other URI schemes. [crates/gcode/src/commands/codewiki/text/sanitize.rs:164-186] |
| `is_windows_absolute_path` | function | Returns 'true' if 'target' begins with a Windows drive-absolute path prefix of the form 'letter + ':' + '/' or '\\'' and has at least three bytes, otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:188-194] |
| `has_uri_scheme` | function | Returns 'true' iff 'target' contains a ':' and the substring before it is a valid URI scheme name: it starts with an ASCII alphabetic character and all remaining characters are ASCII alphanumeric or '+', '-', or '.'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:196-206] |
| `contains_parent_dir_segment` | function | Returns 'true' if the input string’s path portion, after stripping any query or fragment suffix at '?' or '#', contains any '..' segment when split on '/' or '\\', otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:208-211] |
| `starts_with_ignore_ascii_case` | function | Returns 'true' if 'value' begins with 'prefix' when compared case-insensitively using ASCII rules, and 'false' otherwise, including when 'value' is shorter than 'prefix'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:213-217] |
| `span` | function | Constructs and returns a 'SourceSpan' by converting 'file' into a 'String' and populating its 'file', 'line_start', and 'line_end' fields with the provided arguments. [crates/gcode/src/commands/codewiki/text/sanitize.rs:225-231] |
| `ground_text_strips_absolute_markdown_links_and_keeps_valid_citations` | function | Verifies that 'ground_text' removes absolute Markdown links while preserving valid in-range citation spans, yielding plain linked text plus the accepted citation and ignoring the fallback. [crates/gcode/src/commands/codewiki/text/sanitize.rs:234-249] |
| `ground_text_strips_invalid_citations_then_sanitizes_links_before_fallback` | function | Verifies that 'ground_text' removes invalid citation markup and 'file://' links, preserves surrounding link text, and falls back to the provided citation suffix. [crates/gcode/src/commands/codewiki/text/sanitize.rs:252-264] |
| `strips_traversal_windows_unc_file_and_tilde_targets_to_label_text` | function | Verifies that 'sanitize_model_markdown_links' strips the link targets from markdown links whose URLs are traversal, Windows drive, UNC path, 'file://' URI, or tilde-based local paths, leaving only the visible label text. [crates/gcode/src/commands/codewiki/text/sanitize.rs:267-279] |
| `keeps_external_anchors_safe_relative_plain_brackets_and_code_links` | function | Verifies that 'sanitize_model_markdown_links' preserves safe external links, same-page anchors, relative links, plain bracketed text, and code-fenced or quoted markdown that contains local file paths. [crates/gcode/src/commands/codewiki/text/sanitize.rs:282-293] |
| `neutralizes_literal_wikilinks_in_symbol_purpose` | function | Verifies that 'neutralize_symbol_purpose_links' rewrites a literal wikilink in prose by enclosing '`[[relative_path\|title]]`' in single quotes. [crates/gcode/src/commands/codewiki/text/sanitize.rs:296-303] |
| `neutralizes_literal_markdown_links_in_symbol_purpose` | function | Checks that 'neutralize_symbol_purpose_links' rewrites literal Markdown link text in prose by surrounding it with single quotes so it is no longer interpreted as an active link. [crates/gcode/src/commands/codewiki/text/sanitize.rs:306-313] |
| `neutralizing_symbol_purpose_links_leaves_code_spans_and_fences_unchanged` | function | Verifies that 'neutralize_symbol_purpose_links' leaves symbol-purpose link-like syntax unchanged when it appears inside inline code or fenced code blocks. [crates/gcode/src/commands/codewiki/text/sanitize.rs:316-326] |
| `neutralizing_symbol_purpose_links_leaves_source_citations_plain` | function | Tests that 'neutralize_symbol_purpose_links' leaves a plain source citation like '' unchanged while neutralizing symbol-purpose links. [crates/gcode/src/commands/codewiki/text/sanitize.rs:329-333] |

