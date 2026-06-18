---
title: crates/gcode/src/graph/code_graph/connection.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/connection.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/graph/code_graph/connection.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The crates/gcode/src/graph/code_graph/connection.rs file manages connection lifecycle and error mapping for operations interacting with the FalkorDB graph database. It provides a standardized wrapper around the database client, ensuring that database queries are executed safely within the context of the application's service configuration and system degradation state.

By abstracting client access, this file enables other parts of the graph module to query the database without managing raw connection configuration or dealing with low-level connection states directly. It distinguishes between mandatory database access and optional access, supporting graceful degradation when the database is unavailable.

## How it fits

For workflows that strictly require a graph database connection, the with_required_core_graph function at crates/gcode/src/graph/code_graph/connection.rs:14-40 resolves the database configuration, executes a provided query closure using a GraphClient, and translates any connectivity, missing-result, or execution errors into corresponding GraphReadError variants.

For non-essential features that can fallback when the database is offline or unconfigured, the with_optional_core_graph function at crates/gcode/src/graph/code_graph/connection.rs:42-68 executes the query closure when the database is available, but automatically returns a default value without failing if the database is not configured or is unreachable.
[crates/gcode/src/graph/code_graph/connection.rs:7-12]
[crates/gcode/src/graph/code_graph/connection.rs:14-40]
[crates/gcode/src/graph/code_graph/connection.rs:42-68]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `require_graph_reads` | function | Returns 'Ok(())' only when 'ctx.falkordb' is configured, otherwise returns 'GraphReadError::NotConfigured' converted into 'anyhow::Error'. [crates/gcode/src/graph/code_graph/connection.rs:7-12] |
| `with_required_core_graph` | function | 'with_required_core_graph' requires 'ctx.falkordb' to be configured, opens the named FalkorDB graph with the stored connection settings, executes the provided closure against a mutable 'GraphClient', and maps configuration, connectivity, missing-result, or execution errors into the corresponding 'GraphReadError' variants. [crates/gcode/src/graph/code_graph/connection.rs:14-40] |
| `with_optional_core_graph` | function | Runs 'f' against the configured FalkorDB graph client when 'ctx.falkordb' is present, otherwise returns 'default()', and maps unavailable/not-configured graph states to 'default()' while converting missing results or graph access errors into 'GraphReadError::QueryFailed'. [crates/gcode/src/graph/code_graph/connection.rs:42-68] |

