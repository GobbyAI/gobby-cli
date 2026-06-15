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

Builds a graph-context command for a selected wiki scope. `execute` resolves the requested selection, opens a read-only PostgreSQL connection from the graph-context config, loads wiki graph facts, and when the scope is a project and FalkorDB config is available, attempts to add shared code-graph edges while recording truncation or degraded sources before returning a `CommandOutcome` or `WikiError`; `optional_falkor_config` handles the optional FalkorDB config lookup and maps configuration failures into `WikiError::Config`.
[crates/gwiki/src/commands/graph_context.rs:13-83]
[crates/gwiki/src/commands/graph_context.rs:85-98]

## API Symbols

- `execute` (function) component `execute [function]` (`2dae974e-88f7-5adc-9fa3-f48631f3a61b`) lines 13-83 [crates/gwiki/src/commands/graph_context.rs:13-83]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Resolves the requested scope, opens a read-only PostgreSQL connection using the graph-context configuration, loads wiki graph facts and optionally project code-graph edges with truncation/degradation tracking, and returns a 'CommandOutcome' or 'WikiError'. [crates/gwiki/src/commands/graph_context.rs:13-83]
- `optional_falkor_config` (function) component `optional_falkor_config [function]` (`8b9db018-ee54-58b6-9b78-261136331485`) lines 85-98 [crates/gwiki/src/commands/graph_context.rs:85-98]
  - Signature: `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {`
  - Purpose: Resolves and returns the optional FalkorDB graph-context configuration by building a config source from the provided PostgreSQL client and Gobby home, mapping any resolution errors into 'WikiError::Config'. [crates/gwiki/src/commands/graph_context.rs:85-98]

