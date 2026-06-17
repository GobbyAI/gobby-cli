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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/text/structural.rs:7-22](crates/gcode/src/commands/codewiki/text/structural.rs#L7-L22), [crates/gcode/src/commands/codewiki/text/structural.rs:24-33](crates/gcode/src/commands/codewiki/text/structural.rs#L24-L33), [crates/gcode/src/commands/codewiki/text/structural.rs:38-41](crates/gcode/src/commands/codewiki/text/structural.rs#L38-L41), [crates/gcode/src/commands/codewiki/text/structural.rs:43-55](crates/gcode/src/commands/codewiki/text/structural.rs#L43-L55), [crates/gcode/src/commands/codewiki/text/structural.rs:57-63](crates/gcode/src/commands/codewiki/text/structural.rs#L57-L63), [crates/gcode/src/commands/codewiki/text/structural.rs:65-67](crates/gcode/src/commands/codewiki/text/structural.rs#L65-L67), [crates/gcode/src/commands/codewiki/text/structural.rs:69-78](crates/gcode/src/commands/codewiki/text/structural.rs#L69-L78)

</details>

# crates/gcode/src/commands/codewiki/text/structural.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

Builds structural summary text for codewiki documentation. It chooses a symbol’s purpose from its own summary, then docstring, then a fallback “Indexed …” sentence; generates file, module, and repository overview strings with plural-aware counts; suppresses the generic empty-file filler in child listings; writes formatted markdown sections; and collects unique source spans from linked files and modules, likely to support aggregated navigation or highlighting.
[crates/gcode/src/commands/codewiki/text/structural.rs:7-22]
[crates/gcode/src/commands/codewiki/text/structural.rs:24-33]
[crates/gcode/src/commands/codewiki/text/structural.rs:38-41]
[crates/gcode/src/commands/codewiki/text/structural.rs:43-55]
[crates/gcode/src/commands/codewiki/text/structural.rs:57-63]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `structural_symbol_purpose` | function | `pub(crate) fn structural_symbol_purpose(symbol: &Symbol) -> String {` | `structural_symbol_purpose [function]` | `08c689ee-2680-5227-9833-f389907b0d39` | 7-22 [crates/gcode/src/commands/codewiki/text/structural.rs:7-22] | Indexed function `structural_symbol_purpose` in `crates/gcode/src/commands/codewiki/text/structural.rs`. [crates/gcode/src/commands/codewiki/text/structural.rs:7-22] |
| `structural_file_summary` | function | `pub(crate) fn structural_file_summary(file: &str, symbols: &[SymbolDoc]) -> String {` | `structural_file_summary [function]` | `b7650a83-1deb-5c2a-be4d-8cf288ac70ca` | 24-33 [crates/gcode/src/commands/codewiki/text/structural.rs:24-33] | Indexed function `structural_file_summary` in `crates/gcode/src/commands/codewiki/text/structural.rs`. [crates/gcode/src/commands/codewiki/text/structural.rs:24-33] |
| `display_child_summary` | function | `pub(crate) fn display_child_summary(summary: &str, file: &str) -> Option<String> {` | `display_child_summary [function]` | `549d8297-848c-57c5-a259-5ba0d6895f6b` | 38-41 [crates/gcode/src/commands/codewiki/text/structural.rs:38-41] | Indexed function `display_child_summary` in `crates/gcode/src/commands/codewiki/text/structural.rs`. [crates/gcode/src/commands/codewiki/text/structural.rs:38-41] |
| `structural_module_summary` | function | `pub(crate) fn structural_module_summary(` | `structural_module_summary [function]` | `1e9f1190-f3d0-520d-8779-4f9c4952c293` | 43-55 [crates/gcode/src/commands/codewiki/text/structural.rs:43-55] | Indexed function `structural_module_summary` in `crates/gcode/src/commands/codewiki/text/structural.rs`. [crates/gcode/src/commands/codewiki/text/structural.rs:43-55] |
| `structural_repo_summary` | function | `pub(crate) fn structural_repo_summary(file_count: usize, module_count: usize) -> String {` | `structural_repo_summary [function]` | `11a45104-8d40-571e-bac0-4fe317017823` | 57-63 [crates/gcode/src/commands/codewiki/text/structural.rs:57-63] | Indexed function `structural_repo_summary` in `crates/gcode/src/commands/codewiki/text/structural.rs`. [crates/gcode/src/commands/codewiki/text/structural.rs:57-63] |
| `write_section` | function | `pub(crate) fn write_section(doc: &mut String, heading: &str, body: &str) {` | `write_section [function]` | `67ca6480-45b2-5bba-984a-5a93d04ed906` | 65-67 [crates/gcode/src/commands/codewiki/text/structural.rs:65-67] | Indexed function `write_section` in `crates/gcode/src/commands/codewiki/text/structural.rs`. [crates/gcode/src/commands/codewiki/text/structural.rs:65-67] |
| `collect_link_spans` | function | `pub(crate) fn collect_link_spans(files: &[FileLink], modules: &[ModuleLink]) -> Vec<SourceSpan> {` | `collect_link_spans [function]` | `a1844f77-7674-5b7f-aa17-d5fbd34bd53a` | 69-78 [crates/gcode/src/commands/codewiki/text/structural.rs:69-78] | Indexed function `collect_link_spans` in `crates/gcode/src/commands/codewiki/text/structural.rs`. [crates/gcode/src/commands/codewiki/text/structural.rs:69-78] |
