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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/setup/contracts.rs:5-8](crates/gcode/src/setup/contracts.rs#L5-L8), [crates/gcode/src/setup/contracts.rs:10-14](crates/gcode/src/setup/contracts.rs#L10-L14), [crates/gcode/src/setup/contracts.rs:191-193](crates/gcode/src/setup/contracts.rs#L191-L193), [crates/gcode/src/setup/contracts.rs:195-197](crates/gcode/src/setup/contracts.rs#L195-L197)

</details>

# crates/gcode/src/setup/contracts.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

Defines the contract metadata for the `gcode` setup flow: the default schema and namespace, a user-facing overwrite hint, and structured `TableContract`/`IndexContract` records that describe the expected code-index tables, their required columns, and the indexes tied to specific tables and methods. The contract lists are then used by helper functions like `code_index_table_names` and `code_index_index_names` to derive the relevant object names for setup and validation.
[crates/gcode/src/setup/contracts.rs:5-8]
[crates/gcode/src/setup/contracts.rs:10-14]
[crates/gcode/src/setup/contracts.rs:191-193]
[crates/gcode/src/setup/contracts.rs:195-197]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `TableContract` | class | `pub(super) struct TableContract {` | `TableContract [class]` | `9426972f-bf72-59a5-96ad-bafb1885ab42` | 5-8 [crates/gcode/src/setup/contracts.rs:5-8] | Indexed class `TableContract` in `crates/gcode/src/setup/contracts.rs`. [crates/gcode/src/setup/contracts.rs:5-8] |
| `IndexContract` | class | `pub(super) struct IndexContract {` | `IndexContract [class]` | `037b752b-0eb2-5991-a7f3-034ebde7efff` | 10-14 [crates/gcode/src/setup/contracts.rs:10-14] | Indexed class `IndexContract` in `crates/gcode/src/setup/contracts.rs`. [crates/gcode/src/setup/contracts.rs:10-14] |
| `code_index_table_names` | function | `pub(super) fn code_index_table_names() -> impl DoubleEndedIterator<Item = &'static str> {` | `code_index_table_names [function]` | `4fdc5ee8-66b7-5b70-b834-9795f392563f` | 191-193 [crates/gcode/src/setup/contracts.rs:191-193] | Indexed function `code_index_table_names` in `crates/gcode/src/setup/contracts.rs`. [crates/gcode/src/setup/contracts.rs:191-193] |
| `code_index_index_names` | function | `pub(super) fn code_index_index_names() -> impl DoubleEndedIterator<Item = &'static str> {` | `code_index_index_names [function]` | `8f2de110-e5a0-5da9-854e-c2a1311ce6aa` | 195-197 [crates/gcode/src/setup/contracts.rs:195-197] | Indexed function `code_index_index_names` in `crates/gcode/src/setup/contracts.rs`. [crates/gcode/src/setup/contracts.rs:195-197] |
