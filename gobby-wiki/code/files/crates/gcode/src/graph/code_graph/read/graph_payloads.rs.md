---
title: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/graph_payloads.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Overview

`crates/gcode/src/graph/code_graph/read/graph_payloads.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/read/graph_payloads.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `project_overview_graph` | function | Builds a 'GraphPayload' for a project by querying a bounded set of file nodes, then adding import and definition links plus corresponding module/symbol nodes until a clamped node limit is reached. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98] |
| `file_graph` | function | Builds a 'GraphPayload' for a given file by adding a file node, querying the project’s symbols to add function nodes and 'DEFINES' links from the file to each symbol, then querying file call edges to add source/target nodes and their links. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:100-126] |
| `symbol_neighbors` | function | 'symbol_neighbors' queries the core graph for a symbol’s center node and up to 'limit' neighboring symbols, then builds a 'GraphPayload' containing the center, resolved neighbor nodes, and 'CALLS' links oriented by edge direction with line and projection metadata. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:128-164] |
| `blast_radius_graph` | function | 'blast_radius_graph' builds a 'GraphPayload' for a project-centered blast-radius traversal from either a symbol ID or file path by querying the core graph for nearby call/import nodes up to the given 'depth' and 'limit', deduplicating file-target results, and initializing the center node at distance '0'. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:166-239] |

