---
title: crates/gcode/src/commands/graph/payload.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/payload.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/graph/payload.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The file crates/gcode/src/commands/graph/payload.rs orchestrates and formats graph-related command outputs for the gcode CLI tool. Its main role is to fetch code graph structures and render them into human-readable text or structured JSON payloads.

This file acts as the primary presentation layer for various graph operations, transforming raw node and link details into clean, structured results. It ensures a consistent user interface when visualizing project structures, file dependencies, neighboring symbols, or the potential blast radius of a change.

## How it fits

This file sits directly between high-level command handlers and the lower-level graph generation engine. It processes requests, communicates with graph-building functions, and routes the outputs to output rendering utility functions.

The resulting payloads are processed by print_graph_payload in crates/gcode/src/commands/graph/payload.rs:39-44, which routes JSON formatting directly to output::print_json. For text formats, it relies on format_graph_payload_text in crates/gcode/src/commands/graph/payload.rs:6-37 to generate a detailed summary showing nodes, types, file paths, and directional links, which is then printed using output::print_text.

Additionally, the report function in crates/gcode/src/commands/graph/payload.rs:50-59 handles markdown report generation. It prints the raw JSON structure for JSON requests, or uses format_report_text in crates/gcode/src/commands/graph/payload.rs:46-48 to extract the markdown text and output it as standard terminal text.
[crates/gcode/src/commands/graph/payload.rs:6-37]
[crates/gcode/src/commands/graph/payload.rs:39-44]
[crates/gcode/src/commands/graph/payload.rs:46-48]
[crates/gcode/src/commands/graph/payload.rs:50-59]
[crates/gcode/src/commands/graph/payload.rs:61-64]

## Key components

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

