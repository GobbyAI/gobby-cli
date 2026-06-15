---
title: crates/gwiki/src/commands/health.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/health.rs
  ranges:
  - 4-19
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/health.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Resolves a command scope for the selected wiki target, runs a health check against that scope’s root, and packages the result into a scoped `CommandOutcome`. It converts the health report to JSON for machine use, renders the same report as text for display, and returns both under the `health` command name while propagating scope resolution and serialization errors as `WikiError`. [crates/gwiki/src/commands/health.rs:4-19]

## API Symbols

- `execute` (function) component `execute [function]` (`1bfb51ea-113b-5885-af3d-f5ac0d32b8fc`) lines 4-19 [crates/gwiki/src/commands/health.rs:4-19]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Resolves the selected scope, runs a health check for that scope’s root, serializes the resulting report to JSON, and returns a scoped 'CommandOutcome' named 'health' containing both the JSON payload and rendered text. [crates/gwiki/src/commands/health.rs:4-19]

