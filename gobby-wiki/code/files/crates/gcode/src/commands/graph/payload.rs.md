---
title: crates/gcode/src/commands/graph/payload.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/payload.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/payload.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/commands/graph/payload.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/commands/graph/payload.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `format_graph_payload_text` | function | Formats a 'GraphPayload' into a newline-separated text summary listing the node and link counts, optional center, each node with id/type/name and optional file path, and each link as 'source -[type]-> target'. [crates/gcode/src/commands/graph/payload.rs:6-37] |
| `print_graph_payload` | function | Dispatches a 'GraphPayload' to either JSON or text output by calling 'output::print_json(payload)' for 'Format::Json' or formatting it with 'format_graph_payload_text' and printing that with 'output::print_text' for 'Format::Text'. [crates/gcode/src/commands/graph/payload.rs:39-44] |
| `format_report_text` | function | Returns an immutable string slice of the report’s Markdown text by borrowing 'report.markdown'. [crates/gcode/src/commands/graph/payload.rs:46-48] |
| `report` | function | Generates a project graph report with the given 'top_n' limit from 'ctx' and prints it as either JSON or formatted text depending on 'format', returning any error from report generation. [crates/gcode/src/commands/graph/payload.rs:50-59] |
| `overview` | function | Builds a project overview graph from the given 'Context' and 'limit' via 'code_graph::project_overview_graph', then renders it with 'print_graph_payload' in the requested 'Format', returning any error from either step. [crates/gcode/src/commands/graph/payload.rs:61-64] |
| `file` | function | Builds a file-level code graph for 'file_path' using 'code_graph::file_graph(ctx, file_path)?' and then renders it via 'print_graph_payload(&payload, format)', propagating any error as 'anyhow::Result<()>'. [crates/gcode/src/commands/graph/payload.rs:66-69] |
| `neighbors` | function | Fetches up to 'limit' neighbors for the symbol identified by 'symbol_id' from 'ctx' via 'code_graph::symbol_neighbors' and then renders the resulting graph payload with 'print_graph_payload' in the requested 'format'. [crates/gcode/src/commands/graph/payload.rs:71-79] |
| `graph_blast_radius` | function | Constructs a 'GraphBlastRadiusTarget' from exactly one of 'symbol_id' or 'file_path', computes a blast-radius graph with the given 'depth' and 'limit' via 'code_graph::blast_radius_graph', and prints the resulting payload in the requested 'format'. [crates/gcode/src/commands/graph/payload.rs:81-96] |

