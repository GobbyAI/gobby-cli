---
title: crates/gcode/src/search/fts/graph.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/graph.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/fts/graph.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Overview

`crates/gcode/src/search/fts/graph.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/search/fts/graph.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `exact_symbol_matches_result` | function | Queries 'code_symbols' for rows in a given 'project_id' whose specified validated column ('id', 'qualified_name', or 'name') exactly equals 'input', orders matches by 'file_path' and 'line_start', limits the result set, and returns successfully parsed 'Symbol' values while logging and skipping malformed rows. [crates/gcode/src/search/fts/graph.rs:16-50] |
| `row_string` | function | Attempts to extract the specified column from the database 'Row' as a 'String', returning '"<unavailable>"' if the lookup or type conversion fails. [crates/gcode/src/search/fts/graph.rs:52-55] |
| `suggestion_label` | function | Returns a formatted label string containing the symbol’s qualified name followed by its file path and starting line number in the form 'name (path:line)'. [crates/gcode/src/search/fts/graph.rs:57-62] |
| `resolved_symbol` | function | Creates a 'ResolvedGraphSymbol' by cloning the input 'Symbol'’s 'id' into 'id' and its 'name' into 'display_name'. [crates/gcode/src/search/fts/graph.rs:64-69] |
| `resolve_graph_symbol_by_id` | function | Queries the symbol index for an exact 'id' match within the given project and returns the first matching 'ResolvedGraphSymbol' wrapped in 'Option', or 'None' if no match is found. [crates/gcode/src/search/fts/graph.rs:71-78] |
| `resolve_from_candidates` | function | Returns 'Some(resolved_symbol(&candidates[0]))' when exactly one candidate is provided, otherwise returns 'None' with either no suggestions for zero candidates or a de-duplicated list of 'suggestion_label' values for all candidates. [crates/gcode/src/search/fts/graph.rs:80-96] |
| `decisive_resolution` | function | Calls 'resolve_from_candidates' on the input 'candidates' and returns 'Some((resolved, suggestions))' only when a resolution was found or any suggestions were produced, otherwise 'None'. [crates/gcode/src/search/fts/graph.rs:98-103] |
| `resolve_graph_symbol` | function | Resolves a graph symbol by trying exact matches on 'id', 'qualified_name', and 'name' in priority order, then falling back to fuzzy name search and finally full-text search, returning the resolved symbol and any candidate labels. [crates/gcode/src/search/fts/graph.rs:108-147] |

