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

# crates/gcode/src/setup/identifiers.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

This file provides PostgreSQL identifier formatting helpers for setup code. `quote_identifier` sanitizes a single identifier by trimming whitespace, rejecting empty values, NUL bytes, and names over 63 bytes, then escaping internal double quotes and wrapping the result in quotes. `qualified_relation` builds a schema-qualified name by quoting the schema and relation separately and joining them with a dot, so any validation or quoting failure is returned as a `SetupError`.
[crates/gcode/src/setup/identifiers.rs:5-15]
[crates/gcode/src/setup/identifiers.rs:17-41]

## API Symbols

- `qualified_relation` (function) component `qualified_relation [function]` (`429f260a-6e06-5cd9-9327-4a1010eb26a8`) lines 5-15 [crates/gcode/src/setup/identifiers.rs:5-15]
  - Signature: `pub(super) fn qualified_relation(`
  - Purpose: Constructs a schema-qualified relation identifier by formatting quoted schema and relation identifiers separated by a dot, propagating any identifier quoting errors. [crates/gcode/src/setup/identifiers.rs:5-15]
- `quote_identifier` (function) component `quote_identifier [function]` (`9c35edae-7a37-5e7f-a77f-613d7a1a68a9`) lines 17-41 [crates/gcode/src/setup/identifiers.rs:17-41]
  - Signature: `pub(super) fn quote_identifier(value: &str, label: &str) -> Result<String, SetupError> {`
  - Purpose: Validates and double-quotes a string identifier for PostgreSQL use, enforcing non-empty, NUL-free, and maximum byte-length constraints while escaping internal double quotes. [crates/gcode/src/setup/identifiers.rs:17-41]

