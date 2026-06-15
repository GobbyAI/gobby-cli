---
title: crates/gwiki/src/commands/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/mod.rs
  ranges:
  - 30-102
  - 104-115
  - 117-141
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/mod.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Defines the `gwiki` command dispatcher and shared outcome helpers. `run` matches each `Command` variant to the corresponding module’s `execute` function, while `scoped_outcome` and `run_analysis_command` standardize successful scoped results by building a `CommandOutcome`, serializing analysis payloads to JSON, and turning serialization failures into `WikiError::Json`.
[crates/gwiki/src/commands/mod.rs:30-102]
[crates/gwiki/src/commands/mod.rs:104-115]
[crates/gwiki/src/commands/mod.rs:117-141]

## API Symbols

- `run` (function) component `run [function]` (`63fcda6c-5ef5-54e9-a083-1227a81bf596`) lines 30-102 [crates/gwiki/src/commands/mod.rs:30-102]
  - Signature: `pub(crate) fn run(command: Command) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Dispatches a 'Command' enum variant to the corresponding module-level 'execute' function, forwarding its fields and returning that operation’s 'Result<CommandOutcome, WikiError>'. [crates/gwiki/src/commands/mod.rs:30-102]
- `scoped_outcome` (function) component `scoped_outcome [function]` (`af0e246b-2c42-5569-848c-0547f9271fb2`) lines 104-115 [crates/gwiki/src/commands/mod.rs:104-115]
  - Signature: `pub(crate) fn scoped_outcome(`
  - Purpose: Constructs a successful 'CommandOutcome' with exit code '0', a single status message of the form '"{command} resolved scope {scope}"', and a 'CommandResult' containing the provided JSON 'payload' and 'text'. [crates/gwiki/src/commands/mod.rs:104-115]
- `run_analysis_command` (function) component `run_analysis_command [function]` (`45b770b5-4e8a-5024-ba76-482432efe843`) lines 117-141 [crates/gwiki/src/commands/mod.rs:117-141]
  - Signature: `pub(crate) fn run_analysis_command<T>(`
  - Purpose: Resolves the selected command scope, invokes the provided analysis closure on the scope root and identity, serializes the returned report to JSON, and packages both the rendered string and payload into a scoped 'CommandOutcome', mapping serialization failures to 'WikiError::Json'. [crates/gwiki/src/commands/mod.rs:117-141]

