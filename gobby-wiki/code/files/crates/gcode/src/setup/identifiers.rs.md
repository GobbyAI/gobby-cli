---
title: crates/gcode/src/setup/identifiers.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/identifiers.rs
  ranges:
  - 5-15
  - 17-41
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/setup/identifiers.rs:5-15](crates/gcode/src/setup/identifiers.rs#L5-L15), [crates/gcode/src/setup/identifiers.rs:17-41](crates/gcode/src/setup/identifiers.rs#L17-L41)

</details>

# crates/gcode/src/setup/identifiers.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

This file provides identifier validation and quoting helpers for setup code that needs to build PostgreSQL relation names safely.

`quote_identifier` trims input, rejects empty strings, NUL bytes, and identifiers over PostgreSQL’s 63-byte limit, then escapes embedded double quotes and wraps the value in quotes; `qualified_relation` applies that logic to a schema and relation name and combines them into a quoted `schema.relation` string, propagating any setup errors.
[crates/gcode/src/setup/identifiers.rs:5-15]
[crates/gcode/src/setup/identifiers.rs:17-41]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `qualified_relation` | function | `pub(super) fn qualified_relation(` | `qualified_relation [function]` | `429f260a-6e06-5cd9-9327-4a1010eb26a8` | 5-15 [crates/gcode/src/setup/identifiers.rs:5-15] | Indexed function `qualified_relation` in `crates/gcode/src/setup/identifiers.rs`. [crates/gcode/src/setup/identifiers.rs:5-15] |
| `quote_identifier` | function | `pub(super) fn quote_identifier(value: &str, label: &str) -> Result<String, SetupError> {` | `quote_identifier [function]` | `9c35edae-7a37-5e7f-a77f-613d7a1a68a9` | 17-41 [crates/gcode/src/setup/identifiers.rs:17-41] | Indexed function `quote_identifier` in `crates/gcode/src/setup/identifiers.rs`. [crates/gcode/src/setup/identifiers.rs:17-41] |
