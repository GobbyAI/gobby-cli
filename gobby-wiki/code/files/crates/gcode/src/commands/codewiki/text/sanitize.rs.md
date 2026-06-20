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
| `sanitize_model_markdown_links` | function | Indexed function `sanitize_model_markdown_links` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10] |
| `citation_anchor_replacements` | function | Indexed function `citation_anchor_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:20-59] |
| `anchor_citation_target` | function | Indexed function `anchor_citation_target` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:64-84] |
| `is_ascii_line_number` | function | Indexed function `is_ascii_line_number` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:86-88] |
| `neutralize_symbol_purpose_links` | function | Indexed function `neutralize_symbol_purpose_links` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:90-95] |
| `markdown_link_replacements` | function | Indexed function `markdown_link_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:97-105] |
| `markdown_code_ranges` | function | Indexed function `markdown_code_ranges` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:107-115] |
| `wikilink_replacements` | function | Indexed function `wikilink_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:117-140] |
| `replacement_for_range` | function | Indexed function `replacement_for_range` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:142-147] |
| `range_contains` | function | Indexed function `range_contains` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:149-153] |
| `range_overlaps` | function | Indexed function `range_overlaps` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:155-159] |
| `apply_replacements` | function | Indexed function `apply_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:161-180] |
| `LinkFrame` | class | Indexed class `LinkFrame` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:183-186] |
| `Replacement` | class | Indexed class `Replacement` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:189-192] |
| `unsafe_link_replacements` | function | Indexed function `unsafe_link_replacements` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:194-234] |
| `push_label_text` | function | Indexed function `push_label_text` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:236-240] |
| `is_unsafe_link_target` | function | Indexed function `is_unsafe_link_target` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:242-264] |
| `is_windows_absolute_path` | function | Indexed function `is_windows_absolute_path` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:266-272] |
| `has_uri_scheme` | function | Indexed function `has_uri_scheme` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:274-284] |
| `contains_parent_dir_segment` | function | Indexed function `contains_parent_dir_segment` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:286-289] |
| `starts_with_ignore_ascii_case` | function | Indexed function `starts_with_ignore_ascii_case` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:291-295] |
| `span` | function | Indexed function `span` in `crates/gcode/src/commands/codewiki/text/sanitize.rs`. [crates/gcode/src/commands/codewiki/text/sanitize.rs:303-309] |

_Verified by 11 in-file unit tests._

