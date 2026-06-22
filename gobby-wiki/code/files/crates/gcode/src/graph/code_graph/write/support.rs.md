---
title: crates/gcode/src/graph/code_graph/write/support.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write/support.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write/support.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/graph/code_graph/write/support.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/write/support.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute_write_query` | function | Executes a typed Cypher write query by destructuring its 'cypher' string and 'params', sending them to 'client.query', and returning 'Ok(())' if the query succeeds. [crates/gcode/src/graph/code_graph/write/support.rs:6-13] |
| `typed_query` | function | Constructs a 'TypedQuery' from a Cypher string and an iterator of '(key, TypedValue)' parameters by delegating to 'TypedQuery::with_params', propagating any error through 'anyhow::Result'. [crates/gcode/src/graph/code_graph/write/support.rs:15-21] |
| `usize_value` | function | Converts a 'usize' into a 'TypedValue::Integer' by fallibly narrowing it to 'i64', returning an error if the value exceeds FalkorDB’s 'i64' range. [crates/gcode/src/graph/code_graph/write/support.rs:23-27] |
| `sync_token_param` | function | Converts the input 'sync_token' string into a '( "sync_token", TypedValue::String(...) )' parameter pair by cloning it into an owned 'String'. [crates/gcode/src/graph/code_graph/write/support.rs:29-31] |

