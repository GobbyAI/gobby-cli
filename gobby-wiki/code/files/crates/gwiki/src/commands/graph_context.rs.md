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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/graph_context.rs:13-83](crates/gwiki/src/commands/graph_context.rs#L13-L83), [crates/gwiki/src/commands/graph_context.rs:85-98](crates/gwiki/src/commands/graph_context.rs#L85-L98)

</details>

# crates/gwiki/src/commands/graph_context.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `gwiki graph-context` command by resolving the selected scope, opening a read-only PostgreSQL connection, and assembling a graph context payload from wiki graph facts plus optional shared code-graph data. `execute` coordinates the flow, records degraded or truncated sources when code-graph loading is unavailable or clipped, and then returns the final command outcome. `optional_falkor_config` encapsulates the lookup of Falkor-related configuration from the database connection so code-graph enrichment is attempted only when that config is present.
[crates/gwiki/src/commands/graph_context.rs:13-83]
[crates/gwiki/src/commands/graph_context.rs:85-98]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `2dae974e-88f7-5adc-9fa3-f48631f3a61b` | 13-83 [crates/gwiki/src/commands/graph_context.rs:13-83] | Indexed function `execute` in `crates/gwiki/src/commands/graph_context.rs`. [crates/gwiki/src/commands/graph_context.rs:13-83] |
| `optional_falkor_config` | function | `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {` | `optional_falkor_config [function]` | `8b9db018-ee54-58b6-9b78-261136331485` | 85-98 [crates/gwiki/src/commands/graph_context.rs:85-98] | Indexed function `optional_falkor_config` in `crates/gwiki/src/commands/graph_context.rs`. [crates/gwiki/src/commands/graph_context.rs:85-98] |
