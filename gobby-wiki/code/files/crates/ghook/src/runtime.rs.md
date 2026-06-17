---
title: crates/ghook/src/runtime.rs
type: code_file
provenance:
- file: crates/ghook/src/runtime.rs
  ranges:
  - 4-16
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/runtime.rs:4-16](crates/ghook/src/runtime.rs#L4-L16)

</details>

# crates/ghook/src/runtime.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Writes the ghook runtime stamp under the user’s gobby `bin` directory by creating the directory if needed, serializing a JSON file with the current envelope schema version and ghook version, and atomically writing it to `.ghook-runtime.json`. It then prints the ghook version to stdout, so the function both records runtime metadata and reports the installed version in one step. [crates/ghook/src/runtime.rs:4-16]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `write_runtime_stamp` | function | `pub(crate) fn write_runtime_stamp() -> Result<()> {` | `write_runtime_stamp [function]` | `56de4550-bc82-5099-9930-43415fd43d07` | 4-16 [crates/ghook/src/runtime.rs:4-16] | Indexed function `write_runtime_stamp` in `crates/ghook/src/runtime.rs`. [crates/ghook/src/runtime.rs:4-16] |
