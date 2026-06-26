---
title: crates/gcode/src/commands/codewiki/prompts/tables.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/prompts/tables.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/prompts/tables.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/prompts|crates/gcode/src/commands/codewiki/prompts]]

## Overview

`crates/gcode/src/commands/codewiki/prompts/tables.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/prompts/tables.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `append_child_summary_table` | function | Appends a markdown-formatted table to a string with specified headers and rows containing each ChildSummary's name and summary excerpt. [crates/gcode/src/commands/codewiki/prompts/tables.rs:6-18] |
| `append_component_table` | function | Appends a markdown table with a "Component" column header and one row per input component string to a mutable string reference. [crates/gcode/src/commands/codewiki/prompts/tables.rs:20-25] |
| `append_table_guidance` | function | Appends table guidance text, including a header and predefined enumerable facts guidance, to a mutable string. [crates/gcode/src/commands/codewiki/prompts/tables.rs:27-31] |
| `append_evidence_table` | function | Appends a markdown-formatted evidence table to a mutable String by writing a header row and data rows extracted from PageEvidenceRow objects containing name, kind, citation, and summary excerpt fields. [crates/gcode/src/commands/codewiki/prompts/tables.rs:33-50] |
| `append_symbol_summary_table` | function | Appends a markdown-formatted table of symbol metadata to a mutable string, with columns for name, kind, component information, line range, and purpose, or a placeholder message if the symbols slice is empty. [crates/gcode/src/commands/codewiki/prompts/tables.rs:52-82] |
| `append_relationship_section` | function | Appends markdown-formatted tables documenting cross-file relationships (inbound calls, outbound calls, and imports) to a mutable prompt string. [crates/gcode/src/commands/codewiki/prompts/tables.rs:90-132] |

