---
title: crates/gwiki/src/commands/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/mod.rs
  ranges:
  - 30-100
  - 102-113
  - 115-139
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/mod.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This module is the command router for `gwiki`: it declares the subcommand modules and centralizes execution by matching the top-level `Command` enum to the appropriate module-specific `execute` function, returning that handler’s `CommandOutcome` or `WikiError`. It also provides shared helpers for building successful scoped outcomes and for running analysis-style commands, which resolve the active scope, invoke an analysis closure on the scope root and identity, serialize the report to JSON, and package both machine-readable JSON and rendered text into a consistent `CommandOutcome`.
[crates/gwiki/src/commands/mod.rs:30-100]
[crates/gwiki/src/commands/mod.rs:102-113]
[crates/gwiki/src/commands/mod.rs:115-139]

## API Symbols

- `run` (function) component `run [function]` (`63fcda6c-5ef5-54e9-a083-1227a81bf596`) lines 30-100 [crates/gwiki/src/commands/mod.rs:30-100]
  - Signature: `pub(crate) fn run(command: Command) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Dispatches a 'Command' enum by pattern matching each variant to the შესაბამის module’s 'execute' function and returns that handler’s 'Result<CommandOutcome, WikiError>'. [crates/gwiki/src/commands/mod.rs:30-100]
- `scoped_outcome` (function) component `scoped_outcome [function]` (`c64b4c8e-f90a-5f11-9267-336ec5c750dd`) lines 102-113 [crates/gwiki/src/commands/mod.rs:102-113]
  - Signature: `pub(crate) fn scoped_outcome(`
  - Purpose: 'scoped_outcome' constructs a successful 'CommandOutcome' with 'exit_code' 0, a single status message of the form '"{command} resolved scope {scope}"', and a 'CommandResult' containing the given JSON payload and text. [crates/gwiki/src/commands/mod.rs:102-113]
- `run_analysis_command` (function) component `run_analysis_command [function]` (`ac7c3075-5fef-5616-8d13-3cf39377cdfd`) lines 115-139 [crates/gwiki/src/commands/mod.rs:115-139]
  - Signature: `pub(crate) fn run_analysis_command<T>(`
  - Purpose: Resolves the selected scope, runs the provided analysis closure against the scope root and identity, serializes the returned report to JSON, and packages both the JSON payload and rendered text into a scoped 'CommandOutcome', mapping serialization failures to 'WikiError::Json'. [crates/gwiki/src/commands/mod.rs:115-139]

