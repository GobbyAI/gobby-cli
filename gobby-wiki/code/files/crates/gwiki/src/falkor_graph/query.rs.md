---
title: crates/gwiki/src/falkor_graph/query.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/query.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph/query.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/falkor_graph/query.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/falkor_graph/query.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `scope_params` | function | Maps a SearchScope's optional scope_filter to a HashMap of Cypher-escaped string parameters for scope_kind and scope_id, returning None if no filter exists. [crates/gwiki/src/falkor_graph/query.rs:8-23] |
| `row_string` | function | This function extracts a required string value from a database Row by key, converting the Option returned by 'optional_row_string' into a Result that yields a 'SearchError::Backend' if the value is absent. [crates/gwiki/src/falkor_graph/query.rs:25-28] |
| `optional_row_string` | function | This function retrieves a value from a Row by key, attempts to convert it to a string reference via 'Value::as_str', and returns the result as an owned 'String' wrapped in 'Option', or 'None' if any conversion fails. [crates/gwiki/src/falkor_graph/query.rs:30-34] |
| `optional_row_usize` | function | Retrieves a value from a Row by key, converts it from u64 to usize via fallible conversion, and returns Option<usize>, yielding None if the key is absent or any conversion fails. [crates/gwiki/src/falkor_graph/query.rs:36-40] |

