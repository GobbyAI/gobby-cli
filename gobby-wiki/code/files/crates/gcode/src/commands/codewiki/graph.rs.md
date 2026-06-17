---
title: crates/gcode/src/commands/codewiki/graph.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/graph.rs
  ranges:
  - 5-110
  - 114-143
  - 149-164
  - 166-181
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/graph.rs:5-110](crates/gcode/src/commands/codewiki/graph.rs#L5-L110), [crates/gcode/src/commands/codewiki/graph.rs:114-143](crates/gcode/src/commands/codewiki/graph.rs#L114-L143), [crates/gcode/src/commands/codewiki/graph.rs:149-164](crates/gcode/src/commands/codewiki/graph.rs#L149-L164), [crates/gcode/src/commands/codewiki/graph.rs:166-181](crates/gcode/src/commands/codewiki/graph.rs#L166-L181)

</details>

# crates/gcode/src/commands/codewiki/graph.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Builds the Codewiki dependency graph by querying FalkorDB for call and import relationships, then turning those query results into graph edges. `fetch_codewiki_graph_edges` gates the work on core-file symbols, opens a FalkorDB client from the current context, and uses `query_or_unavailable` to downgrade query or connection failures to an unavailable graph instead of hard erroring. `codewiki_call_edges_query` and `codewiki_import_edges_query` assemble the two graph queries, while `import_edges_from_pairs` converts parsed source-target pairs into imported edges so the caller gets a unified `CodewikiGraph` result with truncation and availability handling baked in.
[crates/gcode/src/commands/codewiki/graph.rs:5-110]
[crates/gcode/src/commands/codewiki/graph.rs:35-50]
[crates/gcode/src/commands/codewiki/graph.rs:114-143]
[crates/gcode/src/commands/codewiki/graph.rs:149-164]
[crates/gcode/src/commands/codewiki/graph.rs:166-181]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `fetch_codewiki_graph_edges` | function | `pub(crate) fn fetch_codewiki_graph_edges(` | `fetch_codewiki_graph_edges [function]` | `44dfe8d0-2fa6-573e-9ce3-ec77e5bfd076` | 5-110 [crates/gcode/src/commands/codewiki/graph.rs:5-110] | Indexed function `fetch_codewiki_graph_edges` in `crates/gcode/src/commands/codewiki/graph.rs`. [crates/gcode/src/commands/codewiki/graph.rs:5-110] |
| `query_or_unavailable` | function | `fn query_or_unavailable(` | `query_or_unavailable [function]` | `f32e2489-a73a-5598-bcd0-f56db06d0742` | 35-50 [crates/gcode/src/commands/codewiki/graph.rs:35-50] | Indexed function `query_or_unavailable` in `crates/gcode/src/commands/codewiki/graph.rs`. [crates/gcode/src/commands/codewiki/graph.rs:35-50] |
| `import_edges_from_pairs` | function | `pub(crate) fn import_edges_from_pairs(` | `import_edges_from_pairs [function]` | `ea534b97-87ed-523b-a237-0630b2735f70` | 114-143 [crates/gcode/src/commands/codewiki/graph.rs:114-143] | Indexed function `import_edges_from_pairs` in `crates/gcode/src/commands/codewiki/graph.rs`. [crates/gcode/src/commands/codewiki/graph.rs:114-143] |
| `codewiki_call_edges_query` | function | `pub(crate) fn codewiki_call_edges_query(` | `codewiki_call_edges_query [function]` | `9c90a7ea-835e-5fa5-a2f8-ee25e4dfbabf` | 149-164 [crates/gcode/src/commands/codewiki/graph.rs:149-164] | Indexed function `codewiki_call_edges_query` in `crates/gcode/src/commands/codewiki/graph.rs`. [crates/gcode/src/commands/codewiki/graph.rs:149-164] |
| `codewiki_import_edges_query` | function | `pub(crate) fn codewiki_import_edges_query(` | `codewiki_import_edges_query [function]` | `664e6e45-ca66-5fb8-8554-b30b5f396afa` | 166-181 [crates/gcode/src/commands/codewiki/graph.rs:166-181] | Indexed function `codewiki_import_edges_query` in `crates/gcode/src/commands/codewiki/graph.rs`. [crates/gcode/src/commands/codewiki/graph.rs:166-181] |
