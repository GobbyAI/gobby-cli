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

# crates/gwiki/src/commands/export.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the wiki export command by resolving the requested scope, running the export against that scope’s root, and packaging the result into a command outcome. It converts the export output into JSON for structured payload data, while also building a human-readable summary that includes the resolved scope and exported artifact paths. [crates/gwiki/src/commands/export.rs:4-30]

## API Symbols

- `execute` (function) component `execute [function]` (`0f23b04d-70d9-5c08-85bf-3dccb81bfb1c`) lines 4-30 [crates/gwiki/src/commands/export.rs:4-30]
  - Signature: `pub(crate) fn execute(`
  - Purpose: This function executes an export command on a resolved scope, serializes the resulting artifacts to JSON, and returns a CommandOutcome containing the export scope and artifact file paths. [crates/gwiki/src/commands/export.rs:4-30]

