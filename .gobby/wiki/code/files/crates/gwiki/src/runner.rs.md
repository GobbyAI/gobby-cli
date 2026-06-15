---
title: crates/gwiki/src/runner.rs
type: code_file
provenance:
- file: crates/gwiki/src/runner.rs
  ranges:
  - 7-9
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/runner.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Thin public entry point for executing a parsed `gwiki` command. It simply forwards the `Command` to `commands::run`, returning the resulting `CommandOutcome` or `WikiError` so embedders use the same dispatch path as the CLI. [crates/gwiki/src/runner.rs:7-9]

## API Symbols

- `run` (function) component `run [function]` (`b2e10e08-1c60-55dc-a672-6c3177316550`) lines 7-9 [crates/gwiki/src/runner.rs:7-9]
  - Signature: `pub fn run(command: Command) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Delegates execution of the given 'Command' to 'commands::run' and returns its 'Result<CommandOutcome, WikiError>'. [crates/gwiki/src/runner.rs:7-9]

