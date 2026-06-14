---
title: crates/gcode/src/commands/graph/payload.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/payload.rs
  ranges:
  - 6-37
  - 39-44
  - 46-48
  - 50-59
  - 61-64
  - 66-69
  - 71-79
  - 81-96
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/payload.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

This file provides a command layer for code graph analysis output and reporting. It defines formatting functions that convert GraphPayload and ProjectGraphReport structures into human-readable text (node/link counts, node definitions with types and paths, typed edges), then exposes public functions for generating and displaying various graph queries: project overview, file-specific graphs, neighboring symbol searches, blast radius dependency analysis, and summary reports. Each public function queries the underlying code graph module to generate the requested analysis, then dispatches the result through a unified print function that outputs in either JSON or text format based on the Format parameter.
[crates/gcode/src/commands/graph/payload.rs:6-37]
[crates/gcode/src/commands/graph/payload.rs:39-44]
[crates/gcode/src/commands/graph/payload.rs:46-48]
[crates/gcode/src/commands/graph/payload.rs:50-59]
[crates/gcode/src/commands/graph/payload.rs:61-64]

## API Symbols

- `format_graph_payload_text` (function) component `format_graph_payload_text [function]` (`3d28836a-3131-57ef-9d9d-7b47405155cc`) lines 6-37 [crates/gcode/src/commands/graph/payload.rs:6-37]
  - Signature: `fn format_graph_payload_text(payload: &GraphPayload) -> String {`
  - Purpose: Serializes a GraphPayload struct into a newline-delimited text representation containing node/link counts, optional center coordinate, node definitions with types and file paths, and typed directed edges. [crates/gcode/src/commands/graph/payload.rs:6-37]
- `print_graph_payload` (function) component `print_graph_payload [function]` (`eae59979-bc5d-5c0f-a67b-fadf5ff52825`) lines 39-44 [crates/gcode/src/commands/graph/payload.rs:39-44]
  - Signature: `fn print_graph_payload(payload: &GraphPayload, format: Format) -> anyhow::Result<()> {`
  - Purpose: Outputs a `GraphPayload` in either JSON or formatted text format based on the `Format` enum parameter, returning an `anyhow::Result`. [crates/gcode/src/commands/graph/payload.rs:39-44]
- `format_report_text` (function) component `format_report_text [function]` (`b1011ef1-d6a0-5841-bf9e-aea33a9feaf8`) lines 46-48 [crates/gcode/src/commands/graph/payload.rs:46-48]
  - Signature: `pub(super) fn format_report_text(report: &ProjectGraphReport) -> &str {`
  - Purpose: This function extracts and returns a reference to the markdown string field from a ProjectGraphReport. [crates/gcode/src/commands/graph/payload.rs:46-48]
- `report` (function) component `report [function]` (`bd2049dd-9c75-5e96-a74b-400a199fc004`) lines 50-59 [crates/gcode/src/commands/graph/payload.rs:50-59]
  - Signature: `pub fn report(ctx: &Context, top_n: usize, format: Format) -> anyhow::Result<()> {`
  - Purpose: Generates a project graph report limited to the top N items and outputs it in either JSON or formatted text based on the specified format parameter. [crates/gcode/src/commands/graph/payload.rs:50-59]
- `overview` (function) component `overview [function]` (`a11de9f9-24a2-5c45-914e-05c652a70def`) lines 61-64 [crates/gcode/src/commands/graph/payload.rs:61-64]
  - Signature: `pub fn overview(ctx: &Context, limit: usize, format: Format) -> anyhow::Result<()> {`
  - Purpose: Generates a project overview code graph for the given context with a specified limit, then prints the resulting graph payload in the requested format. [crates/gcode/src/commands/graph/payload.rs:61-64]
- `file` (function) component `file [function]` (`088ce1b3-b2ca-506f-b95e-31536517658b`) lines 66-69 [crates/gcode/src/commands/graph/payload.rs:66-69]
  - Signature: `pub fn file(ctx: &Context, file_path: &str, format: Format) -> anyhow::Result<()> {`
  - Purpose: Generates a code graph for a specified file and outputs it in the requested format, propagating any errors via `anyhow::Result`. [crates/gcode/src/commands/graph/payload.rs:66-69]
- `neighbors` (function) component `neighbors [function]` (`52816628-b5e3-5102-9b08-0a024a0e7fb1`) lines 71-79 [crates/gcode/src/commands/graph/payload.rs:71-79]
  - Signature: `pub fn neighbors(`
  - Purpose: Queries the code graph for neighboring symbols of a given identifier up to a specified limit and prints the result in the requested format. [crates/gcode/src/commands/graph/payload.rs:71-79]
- `graph_blast_radius` (function) component `graph_blast_radius [function]` (`a4088741-10dc-5f7b-9197-c6357c877462`) lines 81-96 [crates/gcode/src/commands/graph/payload.rs:81-96]
  - Signature: `pub fn graph_blast_radius(`
  - Purpose: Computes and outputs the blast radius dependency graph for a specified symbol or file with configurable depth, result limit, and output format. [crates/gcode/src/commands/graph/payload.rs:81-96]

