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

This file provides utilities for managing FalkorDB graph client connections with configurable error handling semantics. It contains three functions that work together to validate and access graph clients from a Context object.

`require_graph_reads` serves as a guard that fails early if FalkorDB is not configured. `with_required_core_graph` wraps graph operations that must succeed, executing a provided closure with a graph client and explicitly mapping service state outcomes (unavailable, unreachable, query failures) to domain-specific GraphReadError types. `with_optional_core_graph` provides a fallback pattern for operations that can gracefully degrade—it either executes the closure on an available client or returns a default value when the service is unconfigured or unreachable, only failing on actual query execution errors.

Together, these functions allow callers to express whether graph reads are mandatory or optional, with the appropriate error behavior for each case.
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

