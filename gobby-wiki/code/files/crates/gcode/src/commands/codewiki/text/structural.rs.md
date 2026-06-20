---
title: crates/gcode/src/commands/codewiki/text/structural.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/structural.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/structural.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Overview

`crates/gcode/src/commands/codewiki/text/structural.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/structural.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `structural_symbol_purpose` | function | Returns the symbol’s non-empty 'summary' if present, otherwise its non-empty 'docstring', and falls back to a formatted index description using the symbol kind, qualified name, and file path. [crates/gcode/src/commands/codewiki/text/structural.rs:7-22] |
| `structural_file_summary` | function | Returns a string summary stating that the given file has no indexed API symbols when 'symbols' is empty, otherwise reporting the number of indexed API symbols it exposes. [crates/gcode/src/commands/codewiki/text/structural.rs:24-33] |
| `display_child_summary` | function | Returns 'Some(summary.trim().to_string())' only when the trimmed 'summary' differs from the structural filler summary for 'file', otherwise returns 'None'. [crates/gcode/src/commands/codewiki/text/structural.rs:38-41] |
| `structural_module_summary` | function | Returns a formatted summary string stating how many direct files and child modules a given module contains, using pluralization based on the counts. [crates/gcode/src/commands/codewiki/text/structural.rs:43-55] |
| `structural_repo_summary` | function | Returns a formatted repository summary string stating how many files and modules are covered, with pluralization adjusted for each count. [crates/gcode/src/commands/codewiki/text/structural.rs:57-63] |
| `write_section` | function | Appends a Markdown H2 section to 'doc' in the form '## {heading}' followed by a blank line and the trimmed 'body', ending with a trailing newline, while ignoring any 'writeln!' formatting error. [crates/gcode/src/commands/codewiki/text/structural.rs:65-67] |
| `collect_link_spans` | function | Collects all 'SourceSpan' values from the 'source_spans' of the provided 'FileLink' and 'ModuleLink' slices, deduplicates and sorts them via a 'BTreeSet', and returns the result as a 'Vec<SourceSpan>'. [crates/gcode/src/commands/codewiki/text/structural.rs:69-78] |

