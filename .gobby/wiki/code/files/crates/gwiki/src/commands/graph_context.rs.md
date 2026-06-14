---
title: crates/gwiki/src/commands/graph_context.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/graph_context.rs
  ranges:
  - 13-83
  - 85-98
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/graph_context.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Builds the `gwiki graph-context` command. `execute` resolves the user’s scope selection, connects read-only to PostgreSQL, fetches the wiki graph facts, and, when available for a project scope, augments them with shared code-graph edges from Falkor while tracking degraded sources and truncated components before returning the final context outcome. `optional_falkor_config` reads Falkor configuration from the current database connection and lets the command degrade gracefully when that integration is not configured.
[crates/gwiki/src/commands/graph_context.rs:13-83]
[crates/gwiki/src/commands/graph_context.rs:85-98]

## API Symbols

- `execute` (function) component `execute [function]` (`2dae974e-88f7-5adc-9fa3-f48631f3a61b`) lines 13-83 [crates/gwiki/src/commands/graph_context.rs:13-83]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/graph_context.rs`. [crates/gwiki/src/commands/graph_context.rs:13-83]
- `optional_falkor_config` (function) component `optional_falkor_config [function]` (`8b9db018-ee54-58b6-9b78-261136331485`) lines 85-98 [crates/gwiki/src/commands/graph_context.rs:85-98]
  - Signature: `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {`
  - Purpose: Indexed function `optional_falkor_config` in `crates/gwiki/src/commands/graph_context.rs`. [crates/gwiki/src/commands/graph_context.rs:85-98]

