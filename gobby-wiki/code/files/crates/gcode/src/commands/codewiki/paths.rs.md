---
title: crates/gcode/src/commands/codewiki/paths.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/paths.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/paths.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

A major role of this file is text normalization and Markdown generation. It ensures that code and table data are output correctly without breaking Markdown syntax. For instance, it formats inline code segments in `crates/gcode/src/commands/codewiki/paths.rs:3-14` and writes escaped table headers and rows in `crates/gcode/src/commands/codewiki/paths.rs:16-19` and `crates/gcode/src/commands/codewiki/paths.rs:21-33`.

## How it fits
[crates/gcode/src/commands/codewiki/paths.rs:3-14]
[crates/gcode/src/commands/codewiki/paths.rs:16-19]
[crates/gcode/src/commands/codewiki/paths.rs:21-33]
[crates/gcode/src/commands/codewiki/paths.rs:35-41]
[crates/gcode/src/commands/codewiki/paths.rs:43-55]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `inline_code` | function | Collapses all whitespace in 'value' to single spaces, returns '''' for empty input, and otherwise wraps the text in a delimiter repeated one character longer than the longest backtick run in the content, inserting surrounding spaces if the content already starts or ends with that delimiter. [crates/gcode/src/commands/codewiki/paths.rs:3-14] |
| `write_markdown_table_header` | function | Appends a Markdown table header row and a matching separator row of '---' cells to 'doc' using the provided 'headers' slice. [crates/gcode/src/commands/codewiki/paths.rs:16-19] |
| `write_markdown_table_row` | function | Appends a Markdown table row to 'doc' by writing a leading '\|', then each provided cell escaped via 'markdown_table_cell' and delimited as '\| cell \|', and finally a newline. [crates/gcode/src/commands/codewiki/paths.rs:21-33] |
| `markdown_table_cell` | function | Normalizes 'value' by collapsing all whitespace sequences to single spaces and escaping every '\|' character with a backslash for safe Markdown table cell output. [crates/gcode/src/commands/codewiki/paths.rs:35-41] |
| `max_backtick_run` | function | Returns the length of the longest contiguous run of backtick characters in 'value' by scanning its chars and tracking the current and maximum run lengths. [crates/gcode/src/commands/codewiki/paths.rs:43-55] |
| `plural` | function | Returns the empty string when 'count == 1', and '"s"' for all other values, to support simple English pluralization. [crates/gcode/src/commands/codewiki/paths.rs:57-59] |
| `component_label` | function | Returns a display label for a 'Symbol' by choosing 'qualified_name' when present or 'name' otherwise, then appending the symbol kind in brackets. [crates/gcode/src/commands/codewiki/paths.rs:61-68] |
| `is_core_file` | function | Returns 'true' only for non-hidden, non-'gobby-wiki' paths that do not look generated, test/spec-related, or located under excluded directories such as 'tests', 'fixtures', 'vendor', 'generated', 'dist', 'build', 'target', or 'node_modules'. [crates/gcode/src/commands/codewiki/paths.rs:70-131] |
| `in_scope` | function | Returns 'true' when 'scopes' is empty, contains an empty string, or when 'file' exactly matches a scope or lies under a scope prefix with a '/' path boundary after trimming any trailing slash from the scope. [crates/gcode/src/commands/codewiki/paths.rs:136-144] |
| `module_for_file` | function | Returns the parent directory of 'file' as a UTF-8 lossy 'String' with backslashes normalized to forward slashes, or an empty string if there is no parent or the parent is '"."'. [crates/gcode/src/commands/codewiki/paths.rs:146-152] |
| `module_ancestors` | function | Returns a 'Vec<String>' containing the input module name and each successive parent module up to the root, stopping when 'parent_module' yields 'None' or an empty string. [crates/gcode/src/commands/codewiki/paths.rs:154-162] |
| `parent_module` | function | Returns the substring before the last ''/'' in 'module', or 'None' if no slash is present. [crates/gcode/src/commands/codewiki/paths.rs:164-166] |
| `module_is_ancestor` | function | Returns 'true' when 'module' is non-empty and 'child' has 'module/' as a prefix, indicating that 'module' is an ancestor module path of 'child'. [crates/gcode/src/commands/codewiki/paths.rs:168-170] |
| `direct_child_modules` | function | Returns a 'Vec<String>' of all candidate module paths whose immediate parent module, as determined by 'parent_module', exactly matches the given 'module'. [crates/gcode/src/commands/codewiki/paths.rs:172-180] |
| `module_depth` | function | Returns the number of non-empty path segments in 'module' by splitting on '/' and counting the resulting components. [crates/gcode/src/commands/codewiki/paths.rs:182-184] |
| `file_doc_path` | function | Constructs and returns the documentation path string 'code/files/{file}.md' by interpolating the provided 'file' name into that template. [crates/gcode/src/commands/codewiki/paths.rs:186-188] |
| `module_doc_path` | function | Constructs and returns a documentation file path string of the form 'code/modules/{module}.md' for the given module name. [crates/gcode/src/commands/codewiki/paths.rs:190-192] |
| `file_wikilink` | function | Formats the input file name into a wiki-style link string of the form '`[[code/files/{file}\|{file}]]`'. [crates/gcode/src/commands/codewiki/paths.rs:194-196] |
| `module_wikilink` | function | Returns a wiki-style link string of the form '`[[code/modules/{module}\|{module}]]`' for the given module name. [crates/gcode/src/commands/codewiki/paths.rs:198-200] |

