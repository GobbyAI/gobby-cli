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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/graph/payload.rs:6-37](crates/gcode/src/commands/graph/payload.rs#L6-L37), [crates/gcode/src/commands/graph/payload.rs:39-44](crates/gcode/src/commands/graph/payload.rs#L39-L44), [crates/gcode/src/commands/graph/payload.rs:46-48](crates/gcode/src/commands/graph/payload.rs#L46-L48), [crates/gcode/src/commands/graph/payload.rs:50-59](crates/gcode/src/commands/graph/payload.rs#L50-L59), [crates/gcode/src/commands/graph/payload.rs:61-64](crates/gcode/src/commands/graph/payload.rs#L61-L64), [crates/gcode/src/commands/graph/payload.rs:66-69](crates/gcode/src/commands/graph/payload.rs#L66-L69), [crates/gcode/src/commands/graph/payload.rs:71-79](crates/gcode/src/commands/graph/payload.rs#L71-L79), [crates/gcode/src/commands/graph/payload.rs:81-96](crates/gcode/src/commands/graph/payload.rs#L81-L96)

</details>

# crates/gcode/src/commands/graph/payload.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

Provides the `graph` command’s payload/output layer: it turns `GraphPayload` and project graph reports into either JSON or plain text, then exposes command entry points that build specific graph views and print them. `format_graph_payload_text` renders node/link summaries, `print_graph_payload` dispatches between JSON and text, and `report`, `overview`, `file`, `neighbors`, and `graph_blast_radius` assemble the appropriate graph data from `Context` before handing it to the shared printers.
[crates/gcode/src/commands/graph/payload.rs:6-37]
[crates/gcode/src/commands/graph/payload.rs:39-44]
[crates/gcode/src/commands/graph/payload.rs:46-48]
[crates/gcode/src/commands/graph/payload.rs:50-59]
[crates/gcode/src/commands/graph/payload.rs:61-64]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `format_graph_payload_text` | function | `fn format_graph_payload_text(payload: &GraphPayload) -> String {` | `format_graph_payload_text [function]` | `3d28836a-3131-57ef-9d9d-7b47405155cc` | 6-37 [crates/gcode/src/commands/graph/payload.rs:6-37] | Indexed function `format_graph_payload_text` in `crates/gcode/src/commands/graph/payload.rs`. [crates/gcode/src/commands/graph/payload.rs:6-37] |
| `print_graph_payload` | function | `fn print_graph_payload(payload: &GraphPayload, format: Format) -> anyhow::Result<()> {` | `print_graph_payload [function]` | `eae59979-bc5d-5c0f-a67b-fadf5ff52825` | 39-44 [crates/gcode/src/commands/graph/payload.rs:39-44] | Indexed function `print_graph_payload` in `crates/gcode/src/commands/graph/payload.rs`. [crates/gcode/src/commands/graph/payload.rs:39-44] |
| `format_report_text` | function | `pub(super) fn format_report_text(report: &ProjectGraphReport) -> &str {` | `format_report_text [function]` | `b1011ef1-d6a0-5841-bf9e-aea33a9feaf8` | 46-48 [crates/gcode/src/commands/graph/payload.rs:46-48] | Indexed function `format_report_text` in `crates/gcode/src/commands/graph/payload.rs`. [crates/gcode/src/commands/graph/payload.rs:46-48] |
| `report` | function | `pub fn report(ctx: &Context, top_n: usize, format: Format) -> anyhow::Result<()> {` | `report [function]` | `bd2049dd-9c75-5e96-a74b-400a199fc004` | 50-59 [crates/gcode/src/commands/graph/payload.rs:50-59] | Indexed function `report` in `crates/gcode/src/commands/graph/payload.rs`. [crates/gcode/src/commands/graph/payload.rs:50-59] |
| `overview` | function | `pub fn overview(ctx: &Context, limit: usize, format: Format) -> anyhow::Result<()> {` | `overview [function]` | `a11de9f9-24a2-5c45-914e-05c652a70def` | 61-64 [crates/gcode/src/commands/graph/payload.rs:61-64] | Indexed function `overview` in `crates/gcode/src/commands/graph/payload.rs`. [crates/gcode/src/commands/graph/payload.rs:61-64] |
| `file` | function | `pub fn file(ctx: &Context, file_path: &str, format: Format) -> anyhow::Result<()> {` | `file [function]` | `088ce1b3-b2ca-506f-b95e-31536517658b` | 66-69 [crates/gcode/src/commands/graph/payload.rs:66-69] | Indexed function `file` in `crates/gcode/src/commands/graph/payload.rs`. [crates/gcode/src/commands/graph/payload.rs:66-69] |
| `neighbors` | function | `pub fn neighbors(` | `neighbors [function]` | `52816628-b5e3-5102-9b08-0a024a0e7fb1` | 71-79 [crates/gcode/src/commands/graph/payload.rs:71-79] | Indexed function `neighbors` in `crates/gcode/src/commands/graph/payload.rs`. [crates/gcode/src/commands/graph/payload.rs:71-79] |
| `graph_blast_radius` | function | `pub fn graph_blast_radius(` | `graph_blast_radius [function]` | `a4088741-10dc-5f7b-9197-c6357c877462` | 81-96 [crates/gcode/src/commands/graph/payload.rs:81-96] | Indexed function `graph_blast_radius` in `crates/gcode/src/commands/graph/payload.rs`. [crates/gcode/src/commands/graph/payload.rs:81-96] |
