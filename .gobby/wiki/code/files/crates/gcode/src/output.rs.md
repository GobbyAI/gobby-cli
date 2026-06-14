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

# crates/gcode/src/output.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file provides output formatting utilities for the gcode crate. It defines a `Format` enum with Json and Text variants for specifying output format, and implements three printing functions: `print_json` outputs serializable values as pretty-printed JSON, `print_json_compact` outputs them as compact JSON without whitespace, and `print_text` prints plain string output. Together these functions enable flexible stdout output in multiple formats.
[crates/gcode/src/output.rs:5-8]
[crates/gcode/src/output.rs:11-14]
[crates/gcode/src/output.rs:17-20]
[crates/gcode/src/output.rs:23-26]

## API Symbols

- `Format` (type) component `Format [type]` (`32d8d097-db0e-56fc-aa13-f7a3e6b0a01d`) lines 5-8 [crates/gcode/src/output.rs:5-8]
  - Signature: `pub enum Format {`
  - Purpose: Indexed type `Format` in `crates/gcode/src/output.rs`. [crates/gcode/src/output.rs:5-8]
- `print_json` (function) component `print_json [function]` (`f6317c63-2ed5-51d5-af06-f5d20a6abaef`) lines 11-14 [crates/gcode/src/output.rs:11-14]
  - Signature: `pub fn print_json<T: Serialize + ?Sized>(value: &T) -> anyhow::Result<()> {`
  - Purpose: Indexed function `print_json` in `crates/gcode/src/output.rs`. [crates/gcode/src/output.rs:11-14]
- `print_json_compact` (function) component `print_json_compact [function]` (`5ee2672b-46db-5f12-917f-949b6030dffb`) lines 17-20 [crates/gcode/src/output.rs:17-20]
  - Signature: `pub fn print_json_compact<T: Serialize + ?Sized>(value: &T) -> anyhow::Result<()> {`
  - Purpose: Indexed function `print_json_compact` in `crates/gcode/src/output.rs`. [crates/gcode/src/output.rs:17-20]
- `print_text` (function) component `print_text [function]` (`b1cbcdf7-c9a6-5ef2-bdbc-bbe7a7f3219e`) lines 23-26 [crates/gcode/src/output.rs:23-26]
  - Signature: `pub fn print_text(text: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `print_text` in `crates/gcode/src/output.rs`. [crates/gcode/src/output.rs:23-26]

