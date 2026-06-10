---
title: crates/gcode/src/setup/contracts.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/contracts.rs
  ranges:
  - 5-8
  - 10-14
  - 191-193
  - 195-197
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/contracts.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

`crates/gcode/src/setup/contracts.rs` exposes 4 indexed API symbols.
[crates/gcode/src/setup/contracts.rs:5-8]
[crates/gcode/src/setup/contracts.rs:10-14]
[crates/gcode/src/setup/contracts.rs:191-193]
[crates/gcode/src/setup/contracts.rs:195-197]

## API Symbols

- `TableContract` (class) component `TableContract [class]` (`9426972f-bf72-59a5-96ad-bafb1885ab42`) lines 5-8 [crates/gcode/src/setup/contracts.rs:5-8]
  - Signature: `pub(super) struct TableContract {`
  - Purpose: `TableContract` is a struct that defines a database table schema contract by specifying static string references to the table name and its required columns. [crates/gcode/src/setup/contracts.rs:5-8]
- `IndexContract` (class) component `IndexContract [class]` (`037b752b-0eb2-5991-a7f3-034ebde7efff`) lines 10-14 [crates/gcode/src/setup/contracts.rs:10-14]
  - Signature: `pub(super) struct IndexContract {`
  - Purpose: IndexContract is a crate-private struct that encapsulates three static string references defining a database index contract: its name, associated table, and method identifier. [crates/gcode/src/setup/contracts.rs:10-14]
- `code_index_table_names` (function) component `code_index_table_names [function]` (`4fdc5ee8-66b7-5b70-b834-9795f392563f`) lines 191-193 [crates/gcode/src/setup/contracts.rs:191-193]
  - Signature: `pub(super) fn code_index_table_names() -> impl DoubleEndedIterator<Item = &'static str> {`
  - Purpose: Returns a double-ended iterator over the static string names of all contracts in `TABLE_CONTRACTS`. [crates/gcode/src/setup/contracts.rs:191-193]
- `code_index_index_names` (function) component `code_index_index_names [function]` (`8f2de110-e5a0-5da9-854e-c2a1311ce6aa`) lines 195-197 [crates/gcode/src/setup/contracts.rs:195-197]
  - Signature: `pub(super) fn code_index_index_names() -> impl DoubleEndedIterator<Item = &'static str> {`
  - Purpose: Returns a double-ended iterator that yields the static string names of each contract in `INDEX_CONTRACTS`. [crates/gcode/src/setup/contracts.rs:195-197]

