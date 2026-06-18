---
title: crates/gcode/src/commands/codewiki/text/structural.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/structural.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/text/structural.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Overview

For symbols, `structural_symbol_purpose` at crates/gcode/src/commands/codewiki/text/structural.rs:7-22 attempts to retrieve a non-empty summary or docstring. If neither is available, it generates a standard fallback index description that identifies the symbol kind, qualified name, and source file path. Similarly, file, module, and repository structures are described using pluralized counts and descriptive labels through `structural_file_summary` at crates/gcode/src/commands/codewiki/text/structural.rs:24-33, `structural_module_summary` at crates/gcode/src/commands/codewiki/text/structural.rs:43-55, and `structural_repo_summary` at crates/gcode/src/commands/codewiki/text/structural.rs:57-63.

Additionally, the module assists with formatting layout and organizing source references. The function `write_section` at crates/gcode/src/commands/codewiki/text/structural.rs:65-67 appends properly spaced Markdown H2 sections to a document, while `collect_link_spans` at crates/gcode/src/commands/codewiki/text/structural.rs:69-78 processes and consolidates related source file and module spans into a sorted, unique collection.

## How it fits

A key workflow optimization is implemented in `display_child_summary` at crates/gcode/src/commands/codewiki/text/structural.rs:38-41. It uses `structural_file_summary` to filter out generic "no-symbol" filler text, returning `None` instead of standard stubs. This ensures index pages list file links cleanly without cluttering the final output with redundant placeholders.
[crates/gcode/src/commands/codewiki/text/structural.rs:7-22]
[crates/gcode/src/commands/codewiki/text/structural.rs:24-33]
[crates/gcode/src/commands/codewiki/text/structural.rs:38-41]
[crates/gcode/src/commands/codewiki/text/structural.rs:43-55]
[crates/gcode/src/commands/codewiki/text/structural.rs:57-63]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `structural_symbol_purpose` | function | Returns the symbol’s non-empty 'summary' if present, otherwise its non-empty 'docstring', and falls back to a formatted index description using the symbol kind, qualified name, and file path. [crates/gcode/src/commands/codewiki/text/structural.rs:7-22] |
| `structural_file_summary` | function | Returns a string summary stating that the given file has no indexed API symbols when 'symbols' is empty, otherwise reporting the number of indexed API symbols it exposes. [crates/gcode/src/commands/codewiki/text/structural.rs:24-33] |
| `display_child_summary` | function | Returns 'Some(summary.trim().to_string())' only when the trimmed 'summary' differs from the structural filler summary for 'file', otherwise returns 'None'. [crates/gcode/src/commands/codewiki/text/structural.rs:38-41] |
| `structural_module_summary` | function | Returns a formatted summary string stating how many direct files and child modules a given module contains, using pluralization based on the counts. [crates/gcode/src/commands/codewiki/text/structural.rs:43-55] |
| `structural_repo_summary` | function | Returns a formatted repository summary string stating how many files and modules are covered, with pluralization adjusted for each count. [crates/gcode/src/commands/codewiki/text/structural.rs:57-63] |
| `write_section` | function | Appends a Markdown H2 section to 'doc' in the form '## {heading}' followed by a blank line and the trimmed 'body', ending with a trailing newline, while ignoring any 'writeln!' formatting error. [crates/gcode/src/commands/codewiki/text/structural.rs:65-67] |
| `collect_link_spans` | function | Collects all 'SourceSpan' values from the 'source_spans' of the provided 'FileLink' and 'ModuleLink' slices, deduplicates and sorts them via a 'BTreeSet', and returns the result as a 'Vec<SourceSpan>'. [crates/gcode/src/commands/codewiki/text/structural.rs:69-78] |

