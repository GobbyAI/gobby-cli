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

`crates/gcode/src/commands/codewiki/text/sanitize.rs` exposes 33 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/sanitize.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `sanitize_model_markdown_links` | function | Returns a new string with unsafe markdown links removed from the input and then citation-style anchor links normalized on the sanitized text. [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10] |
| `citation_anchor_replacements` | function | Parses the input Markdown, tracks the text of each link whose destination can be converted by 'anchor_citation_target', and returns 'Replacement' edits that rewrite the entire link span into a Markdown link using the accumulated label and anchored target. [crates/gcode/src/commands/codewiki/text/sanitize.rs:20-59] |
| `anchor_citation_target` | function | Parses a trimmed 'target' of the form 'path:start' or 'path:start-end' into an anchorized string like 'path#Lstart' or 'path#Lstart-Lend', rejecting empty inputs, fragment-bearing or URI targets, and any non-ASCII line-number components. [crates/gcode/src/commands/codewiki/text/sanitize.rs:64-84] |
| `is_ascii_line_number` | function | Returns 'true' if and only if 'value' is non-empty and every byte in it is an ASCII digit ('0'-'9'), otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:86-88] |
| `neutralize_symbol_purpose_links` | function | Returns a new string with Markdown links and wikilinks in 'text' replaced according to the detected code spans, effectively neutralizing symbol-purpose links outside code. [crates/gcode/src/commands/codewiki/text/sanitize.rs:90-95] |
| `markdown_link_replacements` | function | Parses the input Markdown with 'pulldown-cmark' using empty options, iterates events with byte offsets, and collects a 'Replacement' for each 'Event::Start(Tag::Link { .. })' span returned by 'replacement_for_range'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:97-105] |
| `markdown_code_ranges` | function | Returns the byte ranges of all inline code spans and code block start events found by parsing the input as Markdown with 'Parser::new_ext(..., Options::empty())'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:107-115] |
| `wikilink_replacements` | function | Scans 'text' for '`[[...]]`' wikilinks outside 'code_ranges', skipping any link starts inside code and collecting a 'Replacement' for each non-overlapping matched span. [crates/gcode/src/commands/codewiki/text/sanitize.rs:117-140] |
| `replacement_for_range` | function | Constructs a 'Replacement' whose 'label' is the 'text' slice for the given 'range' formatted with 'inline_code', and whose 'range' field is the same range. [crates/gcode/src/commands/codewiki/text/sanitize.rs:142-147] |
| `range_contains` | function | Returns 'true' if any 'Range<usize>' in 'ranges' contains 'index' using half-open interval semantics ('start <= index < end'), otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:149-153] |
| `range_overlaps` | function | Returns 'true' if any range in 'ranges' intersects 'candidate' using half-open range overlap semantics ('start < other.end && other.start < end'), otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:155-159] |
| `apply_replacements` | function | Returns a new string by sorting non-overlapping 'Replacement' ranges by start/end, skipping any replacement that overlaps already-processed text, and splicing each replacement’s 'label' into 'text' while preserving all untouched segments. [crates/gcode/src/commands/codewiki/text/sanitize.rs:161-180] |
| `LinkFrame` | class | 'LinkFrame' is a struct that stores a byte/character 'range: Range<usize>' and an associated 'label: String', representing the span and text of a link frame. [crates/gcode/src/commands/codewiki/text/sanitize.rs:183-186] |
| `Replacement` | class | 'Replacement' is a struct that describes a text substitution by storing a byte index range ('Range<usize>') to replace and a string 'label' containing the replacement content. [crates/gcode/src/commands/codewiki/text/sanitize.rs:189-192] |
| `unsafe_link_replacements` | function | Parses Markdown into an event stream, tracks currently open links whose destination is deemed unsafe, accumulates their rendered label text from nested content and line breaks, and returns 'Replacement' spans for each matching link range. [crates/gcode/src/commands/codewiki/text/sanitize.rs:194-234] |
| `push_label_text` | function | Appends the provided string slice to the 'label' field of every 'LinkFrame' in the 'active_links' slice, mutating each frame in place. [crates/gcode/src/commands/codewiki/text/sanitize.rs:236-240] |
| `is_unsafe_link_target` | function | Returns 'true' for non-empty, non-fragment link targets that are 'file:' URIs, Windows absolute paths, or other path-like values starting with '/', '\', '~', or containing parent-directory segments, and 'false' for empty strings, fragment-only targets, and other URI schemes. [crates/gcode/src/commands/codewiki/text/sanitize.rs:242-264] |
| `is_windows_absolute_path` | function | Returns 'true' when 'target' is at least three bytes long and matches a Windows drive-root absolute path of the form '<ASCII letter>:' followed by either '/' or '\' as the third byte. [crates/gcode/src/commands/codewiki/text/sanitize.rs:266-272] |
| `has_uri_scheme` | function | Returns 'true' if 'target' contains a colon and the substring before it is a valid URI scheme name starting with an ASCII letter and followed only by ASCII alphanumerics or '+', '-', or '.', otherwise 'false'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:274-284] |
| `contains_parent_dir_segment` | function | Returns 'true' if the input path, after stripping any query or fragment suffix at '?' or '#', contains any path segment equal to '..' when split on '/' or '\'. [crates/gcode/src/commands/codewiki/text/sanitize.rs:286-289] |
| `starts_with_ignore_ascii_case` | function | Returns 'true' if 'value' begins with 'prefix' when compared case-insensitively using ASCII rules, by checking the 'prefix.len()' byte slice at the start of 'value' and returning 'false' if 'value' is too short. [crates/gcode/src/commands/codewiki/text/sanitize.rs:291-295] |
| `span` | function | Creates and returns a 'SourceSpan' from the given file path and inclusive line range by converting 'file' into a 'String' and storing 'line_start' and 'line_end' unchanged. [crates/gcode/src/commands/codewiki/text/sanitize.rs:303-309] |

_Verified by 11 in-file unit tests._

