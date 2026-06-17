---
title: crates/gwiki/src/commands/export.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/export.rs
  ranges:
  - 4-30
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/export.rs:4-30](crates/gwiki/src/commands/export.rs#L4-L30)

</details>

# crates/gwiki/src/commands/export.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `export` command by resolving the selected wiki scope, running the export pipeline at that scope’s root, and packaging the results into a `CommandOutcome`. It converts the export result into a JSON payload, formats a human-readable summary listing the scope and exported artifact paths, and returns both through the shared scoped outcome helper. [crates/gwiki/src/commands/export.rs:4-30]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `0f23b04d-70d9-5c08-85bf-3dccb81bfb1c` | 4-30 [crates/gwiki/src/commands/export.rs:4-30] | Indexed function `execute` in `crates/gwiki/src/commands/export.rs`. [crates/gwiki/src/commands/export.rs:4-30] |
