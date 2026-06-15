---
title: crates/gcode/src/graph/code_graph/connection.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/connection.rs
  ranges:
  - 7-12
  - 14-40
  - 42-68
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/connection.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Purpose

This file provides small graph-connection helpers for code-graph reads against FalkorDB. `require_graph_reads` checks that graph reads are configured, `with_required_core_graph` runs a closure against a required graph client and maps missing, unreachable, or failed reads to `GraphReadError`, and `with_optional_core_graph` does the same work but falls back to a caller-supplied default when the graph is unavailable or unconfigured.
[crates/gcode/src/graph/code_graph/connection.rs:7-12]
[crates/gcode/src/graph/code_graph/connection.rs:14-40]
[crates/gcode/src/graph/code_graph/connection.rs:42-68]

## API Symbols

- `require_graph_reads` (function) component `require_graph_reads [function]` (`347ab6bb-ae29-5207-ae9e-d0805653885a`) lines 7-12 [crates/gcode/src/graph/code_graph/connection.rs:7-12]
  - Signature: `pub fn require_graph_reads(ctx: &Context) -> anyhow::Result<()> {`
  - Purpose: Validates that a FalkorDB instance is configured in the provided `Context`, returning `GraphReadError::NotConfigured` if the `falkordb` field is `None`. [crates/gcode/src/graph/code_graph/connection.rs:7-12]
- `with_required_core_graph` (function) component `with_required_core_graph [function]` (`48bed7c5-177e-50e4-abd2-79973010a2e8`) lines 14-40 [crates/gcode/src/graph/code_graph/connection.rs:14-40]
  - Signature: `pub(super) fn with_required_core_graph<T>(`
  - Purpose: Executes a provided closure with a FalkorDB graph client while validating that the graph is configured and reachable, mapping service state outcomes to domain-specific error types. [crates/gcode/src/graph/code_graph/connection.rs:14-40]
- `with_optional_core_graph` (function) component `with_optional_core_graph [function]` (`ca927725-1bad-5ac7-87df-e2ff8a58dfbd`) lines 42-68 [crates/gcode/src/graph/code_graph/connection.rs:42-68]
  - Signature: `pub(super) fn with_optional_core_graph<T>(`
  - Purpose: Executes a provided closure on an optional FalkorDB graph client, returning its result or falling back to a default value if the service is unavailable or unconfigured. [crates/gcode/src/graph/code_graph/connection.rs:42-68]

