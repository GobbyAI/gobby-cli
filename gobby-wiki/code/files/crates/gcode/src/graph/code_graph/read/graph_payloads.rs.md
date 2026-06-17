---
title: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
  ranges:
  - 19-98
  - 100-126
  - 128-164
  - 166-239
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98](crates/gcode/src/graph/code_graph/read/graph_payloads.rs#L19-L98), [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:100-126](crates/gcode/src/graph/code_graph/read/graph_payloads.rs#L100-L126), [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:128-164](crates/gcode/src/graph/code_graph/read/graph_payloads.rs#L128-L164), [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:166-239](crates/gcode/src/graph/code_graph/read/graph_payloads.rs#L166-L239)

</details>

# crates/gcode/src/graph/code_graph/read/graph_payloads.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

Builds `GraphPayload` responses for several read-side graph views in the code graph system: project overview, per-file graph, symbol neighborhood, and blast-radius expansion. Each function uses the shared optional core-graph client plus query builders and payload helpers to fetch rows, clamp or dedupe results, and incrementally add nodes and links so the final graph stays bounded and type-tagged.
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:100-126]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:128-164]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:166-239]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `project_overview_graph` | function | `pub fn project_overview_graph(ctx: &Context, limit: usize) -> anyhow::Result<GraphPayload> {` | `project_overview_graph [function]` | `39d3125a-94cc-53e8-8317-11ad473c5029` | 19-98 [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98] | Indexed function `project_overview_graph` in `crates/gcode/src/graph/code_graph/read/graph_payloads.rs`. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98] |
| `file_graph` | function | `pub fn file_graph(ctx: &Context, file_path: &str) -> anyhow::Result<GraphPayload> {` | `file_graph [function]` | `21810cf0-1169-5f2b-af49-61f0e0af250e` | 100-126 [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:100-126] | Indexed function `file_graph` in `crates/gcode/src/graph/code_graph/read/graph_payloads.rs`. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:100-126] |
| `symbol_neighbors` | function | `pub fn symbol_neighbors(` | `symbol_neighbors [function]` | `2611c2e5-47f5-5547-a6ad-7bb227d987e3` | 128-164 [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:128-164] | Indexed function `symbol_neighbors` in `crates/gcode/src/graph/code_graph/read/graph_payloads.rs`. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:128-164] |
| `blast_radius_graph` | function | `pub fn blast_radius_graph(` | `blast_radius_graph [function]` | `4525912e-48ac-59e3-8a09-bb5064171c7d` | 166-239 [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:166-239] | Indexed function `blast_radius_graph` in `crates/gcode/src/graph/code_graph/read/graph_payloads.rs`. [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:166-239] |
