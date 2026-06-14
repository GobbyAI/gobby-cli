---
title: crates/gwiki/src/commands/audit.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/audit.rs
  ranges:
  - 3-13
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/audit.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This file wires the `audit` command into the shared analysis-command pipeline. Its `execute` function takes a `ScopeSelection`, runs `audit::run_with_options` with audit options loaded from the environment, and then renders the resulting report as text via `audit::render_text`. [crates/gwiki/src/commands/audit.rs:3-13]

## API Symbols

- `execute` (function) component `execute [function]` (`120069a4-7de5-57d0-8c26-8107d8dc8144`) lines 3-13 [crates/gwiki/src/commands/audit.rs:3-13]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Executes an audit analysis command on the specified scope selection using environment-configured audit options and renders the output as text. [crates/gwiki/src/commands/audit.rs:3-13]

