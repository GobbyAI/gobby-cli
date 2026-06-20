---
title: crates/gcode/src/setup/identifiers.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/identifiers.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/identifiers.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Overview

`crates/gcode/src/setup/identifiers.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gcode/src/setup/identifiers.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `qualified_relation` | function | Returns a quoted fully qualified relation name by concatenating the schema and relation identifiers as 'schema.relation', using 'quote_identifier' for validation/escaping and propagating any 'SetupError'. [crates/gcode/src/setup/identifiers.rs:5-15] |
| `quote_identifier` | function | 'quote_identifier' validates that the trimmed identifier is non-empty, contains no NUL bytes, and does not exceed 'POSTGRES_IDENTIFIER_MAX_BYTES', then escapes embedded double quotes by doubling them and returns the identifier wrapped in double quotes, or a 'SetupError::CreationFailed' with the provided label on validation failure. [crates/gcode/src/setup/identifiers.rs:17-41] |

