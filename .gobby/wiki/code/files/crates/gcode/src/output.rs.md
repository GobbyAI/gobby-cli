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

This file defines the output formatting API for the gcode crate. `Format` is a `clap::ValueEnum` used to select between JSON and plain text output, and the three helper functions write results to stdout: `print_json` emits pretty-printed JSON, `print_json_compact` emits compact JSON, and `print_text` prints raw text. All three return `anyhow::Result<()>` so serialization or I/O-related formatting failures can be propagated consistently.
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
  - Purpose: Serializes 'value' to pretty-printed JSON with 'serde_json::to_string_pretty', writes it to stdout via 'println!', and returns 'Ok(())' or propagates serialization errors as 'anyhow::Result<()>'. [crates/gcode/src/output.rs:11-14]
- `print_json_compact` (function) component `print_json_compact [function]` (`5ee2672b-46db-5f12-917f-949b6030dffb`) lines 17-20 [crates/gcode/src/output.rs:17-20]
  - Signature: `pub fn print_json_compact<T: Serialize + ?Sized>(value: &T) -> anyhow::Result<()> {`
  - Purpose: Serializes the given 'serde::Serialize' value to a compact JSON string, prints it to stdout with a trailing newline, and returns 'Ok(())' or propagates serialization errors via 'anyhow::Result'. [crates/gcode/src/output.rs:17-20]
- `print_text` (function) component `print_text [function]` (`b1cbcdf7-c9a6-5ef2-bdbc-bbe7a7f3219e`) lines 23-26 [crates/gcode/src/output.rs:23-26]
  - Signature: `pub fn print_text(text: &str) -> anyhow::Result<()> {`
  - Purpose: Prints the provided 'text' to standard output with 'println!' and returns 'Ok(())' as an 'anyhow::Result<()>'. [crates/gcode/src/output.rs:23-26]

