---
title: crates/gcode/src/graph/report/rows.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/rows.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/rows.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Overview

`crates/gcode/src/graph/report/rows.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gcode/src/graph/report/rows.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `rows_to_named_counts` | function | Converts a 'Vec<Row>' into a 'BTreeMap<String, usize>' by extracting each row’s '"name"' and '"count"' fields, discarding rows missing either field, and collecting the remaining '(name, count)' pairs. [crates/gcode/src/graph/report/rows.rs:11-19] |
| `row_to_graph_hotspot` | function | Builds a 'GraphHotspot' from a database 'Row' by requiring 'id' and 'name', defaulting 'node_type' to '"node"' and numeric fields to '0' when absent or invalid, and optionally carrying over 'file_path'. [crates/gcode/src/graph/report/rows.rs:21-31] |
| `row_to_target_frequency` | function | Constructs a 'TargetFrequency' from a database 'Row' by requiring string values for 'id' and 'name', defaulting 'count' to '0' if missing or invalid, and returning 'None' if either required field cannot be read. [crates/gcode/src/graph/report/rows.rs:33-39] |
| `row_to_bridge_edge_hypothesis` | function | Parses a 'Row' into a 'BridgeEdgeHypothesis' by requiring 'source_id' and 'target_symbol_id', defaulting 'relation' to 'RELATES_TO_CODE' and 'source_system' to '"gobby-memory"', populating 'ProjectionMetadata' from optional provenance/confidence/source fields, and returning 'None' if either required ID is missing. [crates/gcode/src/graph/report/rows.rs:41-66] |
| `row_string` | function | Returns the first non-empty string value found in 'row' for the provided 'keys', or 'None' if none of the keys map to a non-empty string. [crates/gcode/src/graph/report/rows.rs:68-78] |
| `row_usize` | function | 'row_usize' scans the provided keys in order and returns the first row value that can be losslessly converted to a non-negative 'usize' from 'u64', 'i64', or integral 'f64', logging a warning and returning 'None' immediately for negative 'i64' values. [crates/gcode/src/graph/report/rows.rs:80-106] |
| `row_f64` | function | Returns the first value found in 'row' for any of the provided 'keys', converting it to 'f64' via 'Value::as_f64' and yielding 'None' if no key exists or the value is not a float. [crates/gcode/src/graph/report/rows.rs:108-112] |

_Verified by 4 in-file unit tests._

