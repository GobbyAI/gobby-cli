---
title: crates/gcode/src/commands/codewiki/text/structural.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/structural.rs
  ranges:
  - 7-22
  - 24-33
  - 38-41
  - 43-55
  - 57-63
  - 65-67
  - 69-78
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/structural.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

This file provides the text-building helpers for codewiki’s structural documentation output. It formats concise summaries for symbols, files, modules, and the repository itself, choosing a symbol’s summary or docstring when available and otherwise falling back to an indexed placeholder description. It also filters out boilerplate child summaries, writes trimmed Markdown sections into the document buffer, and collects unique source spans from file and module links so structural listings can be rendered cleanly and consistently.
[crates/gcode/src/commands/codewiki/text/structural.rs:7-22]
[crates/gcode/src/commands/codewiki/text/structural.rs:24-33]
[crates/gcode/src/commands/codewiki/text/structural.rs:38-41]
[crates/gcode/src/commands/codewiki/text/structural.rs:43-55]
[crates/gcode/src/commands/codewiki/text/structural.rs:57-63]

## API Symbols

- `structural_symbol_purpose` (function) component `structural_symbol_purpose [function]` (`08c689ee-2680-5227-9833-f389907b0d39`) lines 7-22 [crates/gcode/src/commands/codewiki/text/structural.rs:7-22]
  - Signature: `pub(crate) fn structural_symbol_purpose(symbol: &Symbol) -> String {`
  - Purpose: Returns the symbol’s non-empty 'summary' if present, otherwise its non-empty 'docstring', and falls back to a formatted index description using the symbol’s kind, qualified name, and file path. [crates/gcode/src/commands/codewiki/text/structural.rs:7-22]
- `structural_file_summary` (function) component `structural_file_summary [function]` (`b7650a83-1deb-5c2a-be4d-8cf288ac70ca`) lines 24-33 [crates/gcode/src/commands/codewiki/text/structural.rs:24-33]
  - Signature: `pub(crate) fn structural_file_summary(file: &str, symbols: &[SymbolDoc]) -> String {`
  - Purpose: Returns a string stating either that the given file has no indexed API symbols or, otherwise, how many indexed API symbols it exposes, with pluralization handled by 'plural(symbols.len())'. [crates/gcode/src/commands/codewiki/text/structural.rs:24-33]
- `display_child_summary` (function) component `display_child_summary [function]` (`549d8297-848c-57c5-a259-5ba0d6895f6b`) lines 38-41 [crates/gcode/src/commands/codewiki/text/structural.rs:38-41]
  - Signature: `pub(crate) fn display_child_summary(summary: &str, file: &str) -> Option<String> {`
  - Purpose: Returns 'Some(trimmed summary)' only when the trimmed 'summary' differs from the structural summary of 'file' with no children, otherwise returns 'None'. [crates/gcode/src/commands/codewiki/text/structural.rs:38-41]
- `structural_module_summary` (function) component `structural_module_summary [function]` (`1e9f1190-f3d0-520d-8779-4f9c4952c293`) lines 43-55 [crates/gcode/src/commands/codewiki/text/structural.rs:43-55]
  - Signature: `pub(crate) fn structural_module_summary(`
  - Purpose: Returns a 'String' that formats the module name with the number of direct files and child modules it contains, using pluralized nouns for each count. [crates/gcode/src/commands/codewiki/text/structural.rs:43-55]
- `structural_repo_summary` (function) component `structural_repo_summary [function]` (`11a45104-8d40-571e-bac0-4fe317017823`) lines 57-63 [crates/gcode/src/commands/codewiki/text/structural.rs:57-63]
  - Signature: `pub(crate) fn structural_repo_summary(file_count: usize, module_count: usize) -> String {`
  - Purpose: Returns a formatted repository summary string stating how many files and modules are covered by the code documentation, with correct pluralization. [crates/gcode/src/commands/codewiki/text/structural.rs:57-63]
- `write_section` (function) component `write_section [function]` (`67ca6480-45b2-5bba-984a-5a93d04ed906`) lines 65-67 [crates/gcode/src/commands/codewiki/text/structural.rs:65-67]
  - Signature: `pub(crate) fn write_section(doc: &mut String, heading: &str, body: &str) {`
  - Purpose: Appends a Markdown section to 'doc' by writing a level-2 heading from 'heading' followed by the trimmed 'body' and a trailing newline. [crates/gcode/src/commands/codewiki/text/structural.rs:65-67]
- `collect_link_spans` (function) component `collect_link_spans [function]` (`a1844f77-7674-5b7f-aa17-d5fbd34bd53a`) lines 69-78 [crates/gcode/src/commands/codewiki/text/structural.rs:69-78]
  - Signature: `pub(crate) fn collect_link_spans(files: &[FileLink], modules: &[ModuleLink]) -> Vec<SourceSpan> {`
  - Purpose: Collects all 'SourceSpan' values from the 'source_spans' fields of the provided 'FileLink' and 'ModuleLink' slices, deduplicates and sorts them via a 'BTreeSet', and returns the unique spans as a 'Vec<SourceSpan>'. [crates/gcode/src/commands/codewiki/text/structural.rs:69-78]

