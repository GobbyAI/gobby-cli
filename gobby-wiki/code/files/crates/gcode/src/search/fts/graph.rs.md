---
title: crates/gcode/src/search/fts/graph.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/graph.rs
  ranges:
  - 16-50
  - 52-55
  - 57-62
  - 64-69
  - 71-78
  - 80-96
  - 98-103
  - 108-147
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/fts/graph.rs:16-50](crates/gcode/src/search/fts/graph.rs#L16-L50), [crates/gcode/src/search/fts/graph.rs:52-55](crates/gcode/src/search/fts/graph.rs#L52-L55), [crates/gcode/src/search/fts/graph.rs:57-62](crates/gcode/src/search/fts/graph.rs#L57-L62), [crates/gcode/src/search/fts/graph.rs:64-69](crates/gcode/src/search/fts/graph.rs#L64-L69), [crates/gcode/src/search/fts/graph.rs:71-78](crates/gcode/src/search/fts/graph.rs#L71-L78), [crates/gcode/src/search/fts/graph.rs:80-96](crates/gcode/src/search/fts/graph.rs#L80-L96), [crates/gcode/src/search/fts/graph.rs:98-103](crates/gcode/src/search/fts/graph.rs#L98-L103), [crates/gcode/src/search/fts/graph.rs:108-147](crates/gcode/src/search/fts/graph.rs#L108-L147)

</details>

# crates/gcode/src/search/fts/graph.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

Provides symbol resolution for graph/search queries against `code_symbols` in Postgres. The helpers first run exact lookups on `id`, `qualified_name`, or `name`, using a small result limit and converting valid rows into `Symbol` values while logging and skipping malformed rows. Those matches are then turned into lightweight `ResolvedGraphSymbol` values, with `suggestion_label` formatting human-readable labels and `row_string` supporting warning logs. The public resolver by ID delegates to the exact-match path, and the remaining resolution pipeline combines candidate selection, decisive-choice logic, and symbol-name/FTS search to return either a single resolved graph symbol or fallback suggestions.
[crates/gcode/src/search/fts/graph.rs:16-50]
[crates/gcode/src/search/fts/graph.rs:52-55]
[crates/gcode/src/search/fts/graph.rs:57-62]
[crates/gcode/src/search/fts/graph.rs:64-69]
[crates/gcode/src/search/fts/graph.rs:71-78]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `exact_symbol_matches_result` | function | `fn exact_symbol_matches_result(` | `exact_symbol_matches_result [function]` | `842c67f7-b4e2-5d99-8a88-32cad789aa2c` | 16-50 [crates/gcode/src/search/fts/graph.rs:16-50] | Indexed function `exact_symbol_matches_result` in `crates/gcode/src/search/fts/graph.rs`. [crates/gcode/src/search/fts/graph.rs:16-50] |
| `row_string` | function | `fn row_string(row: &Row, column: &str) -> String {` | `row_string [function]` | `b4cc47ee-1f6a-5e5a-8441-d13a2e35cd07` | 52-55 [crates/gcode/src/search/fts/graph.rs:52-55] | Indexed function `row_string` in `crates/gcode/src/search/fts/graph.rs`. [crates/gcode/src/search/fts/graph.rs:52-55] |
| `suggestion_label` | function | `fn suggestion_label(symbol: &Symbol) -> String {` | `suggestion_label [function]` | `0ff8ece5-1205-58ae-905a-49ce8f454e17` | 57-62 [crates/gcode/src/search/fts/graph.rs:57-62] | Indexed function `suggestion_label` in `crates/gcode/src/search/fts/graph.rs`. [crates/gcode/src/search/fts/graph.rs:57-62] |
| `resolved_symbol` | function | `fn resolved_symbol(symbol: &Symbol) -> ResolvedGraphSymbol {` | `resolved_symbol [function]` | `d1f8a2d2-61fd-58e2-b068-7689eccb3887` | 64-69 [crates/gcode/src/search/fts/graph.rs:64-69] | Indexed function `resolved_symbol` in `crates/gcode/src/search/fts/graph.rs`. [crates/gcode/src/search/fts/graph.rs:64-69] |
| `resolve_graph_symbol_by_id` | function | `pub fn resolve_graph_symbol_by_id(` | `resolve_graph_symbol_by_id [function]` | `3d1bee9a-3709-57f9-a28d-e88b9c8785a7` | 71-78 [crates/gcode/src/search/fts/graph.rs:71-78] | Indexed function `resolve_graph_symbol_by_id` in `crates/gcode/src/search/fts/graph.rs`. [crates/gcode/src/search/fts/graph.rs:71-78] |
| `resolve_from_candidates` | function | `fn resolve_from_candidates(candidates: Vec<Symbol>) -> (Option<ResolvedGraphSymbol>, Vec<String>) {` | `resolve_from_candidates [function]` | `a28d9b77-15e0-501a-8023-399c91273ecf` | 80-96 [crates/gcode/src/search/fts/graph.rs:80-96] | Indexed function `resolve_from_candidates` in `crates/gcode/src/search/fts/graph.rs`. [crates/gcode/src/search/fts/graph.rs:80-96] |
| `decisive_resolution` | function | `fn decisive_resolution(` | `decisive_resolution [function]` | `f5aa9fa1-b1c7-562f-9575-b6658bdfd99c` | 98-103 [crates/gcode/src/search/fts/graph.rs:98-103] | Indexed function `decisive_resolution` in `crates/gcode/src/search/fts/graph.rs`. [crates/gcode/src/search/fts/graph.rs:98-103] |
| `resolve_graph_symbol` | function | `pub fn resolve_graph_symbol(` | `resolve_graph_symbol [function]` | `c405005b-f37b-5014-9917-2ce4df0bf22c` | 108-147 [crates/gcode/src/search/fts/graph.rs:108-147] | Indexed function `resolve_graph_symbol` in `crates/gcode/src/search/fts/graph.rs`. [crates/gcode/src/search/fts/graph.rs:108-147] |
