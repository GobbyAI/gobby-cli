---
title: crates/gcode/src/graph/report/render.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/render.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Overview

`crates/gcode/src/graph/report/render.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/graph/report/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `RenderMarkdownInput` | class | 'RenderMarkdownInput<'a>' is a borrowed parameter bundle for generating a Markdown render of a graph report, carrying the project ID, timestamp, summary, hotspot and target frequency data, optional bridge summary, degradation details, and a 'top_n' limit. [crates/gcode/src/graph/report/render.rs:8-18] |
| `render_markdown` | function | Formats a 'RenderMarkdownInput' into a Markdown project graph report string by emitting the project metadata, summary counts, optional code-edge and bridge-confidence details, and ranked hotspot/target sections. [crates/gcode/src/graph/report/render.rs:20-99] |
| `append_hotspot_section` | function | Appends a blank line, a Markdown '##' section header, and up to 'top_n' hotspot entries formatted with their name, degree, incoming, and outgoing counts to 'lines', returning early if 'top_n == 0' or 'hotspots' is empty. [crates/gcode/src/graph/report/render.rs:101-121] |
| `append_target_section` | function | Appends a blank line, a Markdown '##' heading with the given title, and up to 'top_n' target entries formatted as '- <inline_code(name)> (<count>)' to 'lines', unless 'top_n' is zero or 'targets' is empty. [crates/gcode/src/graph/report/render.rs:123-141] |
| `inline_code` | function | Returns 'value' wrapped in a run of apostrophes one character longer than the maximum backtick run found in 'value', inserting spaces inside the delimiters if the string already starts or ends with an apostrophe to avoid ambiguity. [crates/gcode/src/graph/report/render.rs:143-150] |
| `max_backtick_run` | function | Returns the length of the longest contiguous run of backtick characters in 'value', scanning the string by Unicode scalar values and resetting the current run on any non-backtick character. [crates/gcode/src/graph/report/render.rs:152-164] |
| `markdown_text` | function | Escapes backslashes, apostrophes, '*', '_', '[', ']', '<', and '>' in a string, then replaces newlines with spaces to produce Markdown-safe text. [crates/gcode/src/graph/report/render.rs:166-177] |
| `named_counts_inline` | function | Formats a 'BTreeMap<String, usize>' into a comma-separated inline string of 'name=count' pairs in iteration order. [crates/gcode/src/graph/report/render.rs:179-185] |

