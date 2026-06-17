---
title: crates/gcode/src/output.rs
type: code_file
provenance:
- file: crates/gcode/src/output.rs
  ranges:
  - 5-8
  - 11-14
  - 17-20
  - 23-26
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/output.rs:5-8](crates/gcode/src/output.rs#L5-L8), [crates/gcode/src/output.rs:11-14](crates/gcode/src/output.rs#L11-L14), [crates/gcode/src/output.rs:17-20](crates/gcode/src/output.rs#L17-L20), [crates/gcode/src/output.rs:23-26](crates/gcode/src/output.rs#L23-L26)

</details>

# crates/gcode/src/output.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file defines the output formatting layer for gcode commands. `Format` is a CLI-selectable enum with `Json` and `Text` variants, and the three helper functions handle writing results to stdout: `print_json` emits pretty-printed JSON for any serializable value, `print_json_compact` emits compact JSON, and `print_text` prints plain text. All three return `anyhow::Result<()>` so callers can propagate serialization or I/O failures consistently.
[crates/gcode/src/output.rs:5-8]
[crates/gcode/src/output.rs:11-14]
[crates/gcode/src/output.rs:17-20]
[crates/gcode/src/output.rs:23-26]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Format` | type | `pub enum Format {` | `Format [type]` | `32d8d097-db0e-56fc-aa13-f7a3e6b0a01d` | 5-8 [crates/gcode/src/output.rs:5-8] | Indexed type `Format` in `crates/gcode/src/output.rs`. [crates/gcode/src/output.rs:5-8] |
| `print_json` | function | `pub fn print_json<T: Serialize + ?Sized>(value: &T) -> anyhow::Result<()> {` | `print_json [function]` | `f6317c63-2ed5-51d5-af06-f5d20a6abaef` | 11-14 [crates/gcode/src/output.rs:11-14] | Indexed function `print_json` in `crates/gcode/src/output.rs`. [crates/gcode/src/output.rs:11-14] |
| `print_json_compact` | function | `pub fn print_json_compact<T: Serialize + ?Sized>(value: &T) -> anyhow::Result<()> {` | `print_json_compact [function]` | `5ee2672b-46db-5f12-917f-949b6030dffb` | 17-20 [crates/gcode/src/output.rs:17-20] | Indexed function `print_json_compact` in `crates/gcode/src/output.rs`. [crates/gcode/src/output.rs:17-20] |
| `print_text` | function | `pub fn print_text(text: &str) -> anyhow::Result<()> {` | `print_text [function]` | `b1cbcdf7-c9a6-5ef2-bdbc-bbe7a7f3219e` | 23-26 [crates/gcode/src/output.rs:23-26] | Indexed function `print_text` in `crates/gcode/src/output.rs`. [crates/gcode/src/output.rs:23-26] |
