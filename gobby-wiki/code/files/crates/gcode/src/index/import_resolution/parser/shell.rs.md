---
title: crates/gcode/src/index/import_resolution/parser/shell.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/shell.rs
  ranges:
  - 8-40
  - 42-57
  - 59-78
  - 80-96
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/shell.rs:8-40](crates/gcode/src/index/import_resolution/parser/shell.rs#L8-L40), [crates/gcode/src/index/import_resolution/parser/shell.rs:42-57](crates/gcode/src/index/import_resolution/parser/shell.rs#L42-L57), [crates/gcode/src/index/import_resolution/parser/shell.rs:59-78](crates/gcode/src/index/import_resolution/parser/shell.rs#L59-L78), [crates/gcode/src/index/import_resolution/parser/shell.rs:80-96](crates/gcode/src/index/import_resolution/parser/shell.rs#L80-L96)

</details>

# crates/gcode/src/index/import_resolution/parser/shell.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This file handles shell import detection and shell-local call resolution for import indexing. `parse_shell_import_statement` normalizes a line of shell text, recognizes `source` and `.` statements, extracts the referenced path, records an `ImportRelation`, and, when the target is a safe relative path, adds the resolved file to `shell_source_files`. `resolve_shell_local_callee` then uses those sourced files to build a `LocalCallBinding` for bare calls only when no existing symbol in the file already matches the callee name. The helper `shell_source_target` filters out absolute, interpolated, or otherwise dynamic paths and resolves safe relative paths against the importing file, while `normalize_project_path` canonicalizes the resulting project path form.
[crates/gcode/src/index/import_resolution/parser/shell.rs:8-40]
[crates/gcode/src/index/import_resolution/parser/shell.rs:42-57]
[crates/gcode/src/index/import_resolution/parser/shell.rs:59-78]
[crates/gcode/src/index/import_resolution/parser/shell.rs:80-96]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_shell_import_statement` | function | `pub(crate) fn parse_shell_import_statement(` | `parse_shell_import_statement [function]` | `00447dc2-bfc5-5aa9-bc0e-11a47087513d` | 8-40 [crates/gcode/src/index/import_resolution/parser/shell.rs:8-40] | Indexed function `parse_shell_import_statement` in `crates/gcode/src/index/import_resolution/parser/shell.rs`. [crates/gcode/src/index/import_resolution/parser/shell.rs:8-40] |
| `resolve_shell_local_callee` | function | `pub(crate) fn resolve_shell_local_callee(` | `resolve_shell_local_callee [function]` | `2fc09547-bb5d-5ce6-b830-e6262a5eb599` | 42-57 [crates/gcode/src/index/import_resolution/parser/shell.rs:42-57] | Indexed function `resolve_shell_local_callee` in `crates/gcode/src/index/import_resolution/parser/shell.rs`. [crates/gcode/src/index/import_resolution/parser/shell.rs:42-57] |
| `shell_source_target` | function | `fn shell_source_target(rel_path: &str, source_path: &str) -> Option<String> {` | `shell_source_target [function]` | `f3d5fddd-d9a7-5917-9fd0-c7b03fdc3961` | 59-78 [crates/gcode/src/index/import_resolution/parser/shell.rs:59-78] | Indexed function `shell_source_target` in `crates/gcode/src/index/import_resolution/parser/shell.rs`. [crates/gcode/src/index/import_resolution/parser/shell.rs:59-78] |
| `normalize_project_path` | function | `fn normalize_project_path(path: &Path) -> Option<String> {` | `normalize_project_path [function]` | `66aaedd2-8099-54da-b607-d9c86b9928ee` | 80-96 [crates/gcode/src/index/import_resolution/parser/shell.rs:80-96] | Indexed function `normalize_project_path` in `crates/gcode/src/index/import_resolution/parser/shell.rs`. [crates/gcode/src/index/import_resolution/parser/shell.rs:80-96] |
