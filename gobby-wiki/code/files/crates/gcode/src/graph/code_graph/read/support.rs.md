---
title: crates/gcode/src/graph/code_graph/read/support.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/support.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/support.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Overview

`crates/gcode/src/graph/code_graph/read/support.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/read/support.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `row_to_graph_result` | function | Constructs a 'GraphResult' from a 'Row' by extracting the first available matching fields for each property ('id', 'name', 'file_path', 'confidence', 'relation'), parsing numeric 'line' and 'distance' values with fallbacks to defaults, and populating 'metadata' via 'row_to_projection_metadata'. [crates/gcode/src/graph/code_graph/read/support.rs:43-94] |
| `clamp_limit` | function | Returns 'limit' clamped to 'MAX_GRAPH_LIMIT' by delegating to 'typed_query::clamp_limit'. [crates/gcode/src/graph/code_graph/read/support.rs:95-97] |
| `clamp_offset` | function | Returns 'typed_query::clamp_offset(offset, MAX_GRAPH_LIMIT)', clamping the given 'offset' to the maximum graph limit. [crates/gcode/src/graph/code_graph/read/support.rs:99-101] |
| `dedupe_limited_blast_rows` | function | Sorts 'rows' by 'distance', then 'node_name', then 'node_id', removes duplicate entries by 'node_id' while discarding rows missing that field, truncates the result to 'clamp_limit(limit)', and returns the deduplicated vector. [crates/gcode/src/graph/code_graph/read/support.rs:102-131] |
| `count_from_rows` | function | Returns the 'cnt' field from the first row as a 'usize' by accepting either unsigned or nonnegative signed integer values and falling back to '0' if the row, field, or conversion is missing or invalid. [crates/gcode/src/graph/code_graph/read/support.rs:133-142] |

_Verified by 2 in-file unit tests._

