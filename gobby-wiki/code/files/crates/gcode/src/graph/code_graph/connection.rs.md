---
title: crates/gcode/src/graph/code_graph/connection.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/connection.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/connection.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/graph/code_graph/connection.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/connection.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `require_graph_reads` | function | Returns 'Ok(())' only when 'ctx.falkordb' is configured, otherwise returns 'GraphReadError::NotConfigured' converted into 'anyhow::Error'. [crates/gcode/src/graph/code_graph/connection.rs:7-12] |
| `with_required_core_graph` | function | 'with_required_core_graph' requires 'ctx.falkordb' to be configured, opens the named FalkorDB graph with the stored connection settings, executes the provided closure against a mutable 'GraphClient', and maps configuration, connectivity, missing-result, or execution errors into the corresponding 'GraphReadError' variants. [crates/gcode/src/graph/code_graph/connection.rs:14-40] |
| `with_optional_core_graph` | function | Runs 'f' against the configured FalkorDB graph client when 'ctx.falkordb' is present, otherwise returns 'default()', and maps unavailable/not-configured graph states to 'default()' while converting missing results or graph access errors into 'GraphReadError::QueryFailed'. [crates/gcode/src/graph/code_graph/connection.rs:42-68] |

