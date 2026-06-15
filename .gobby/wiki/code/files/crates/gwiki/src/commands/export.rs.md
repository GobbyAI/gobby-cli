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

Implements the `export` command entry point: it resolves the selected wiki scope, runs the export against that root, and packages the result into an `ExportOutput` plus a human-readable status message. The pieces work together by deriving the scope identity for output, serializing the export result to JSON for the command payload, collecting artifact file paths for the summary text, and returning a scoped `CommandOutcome`. [crates/gwiki/src/commands/export.rs:4-30]

## API Symbols

- `execute` (function) component `execute [function]` (`0f23b04d-70d9-5c08-85bf-3dccb81bfb1c`) lines 4-30 [crates/gwiki/src/commands/export.rs:4-30]
  - Signature: `pub(crate) fn execute(`
  - Purpose: This function executes an export command on a resolved scope, serializes the resulting artifacts to JSON, and returns a CommandOutcome containing the export scope and artifact file paths. [crates/gwiki/src/commands/export.rs:4-30]

