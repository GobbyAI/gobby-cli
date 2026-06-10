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

# crates/gcode/src/search/fts/graph.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

`crates/gcode/src/search/fts/graph.rs` exposes 8 indexed API symbols.
[crates/gcode/src/search/fts/graph.rs:16-50]
[crates/gcode/src/search/fts/graph.rs:52-55]
[crates/gcode/src/search/fts/graph.rs:57-62]
[crates/gcode/src/search/fts/graph.rs:64-69]
[crates/gcode/src/search/fts/graph.rs:71-78]
[crates/gcode/src/search/fts/graph.rs:80-96]
[crates/gcode/src/search/fts/graph.rs:98-103]
[crates/gcode/src/search/fts/graph.rs:108-147]

## API Symbols

- `exact_symbol_matches_result` (function) component `exact_symbol_matches_result [function]` (`842c67f7-b4e2-5d99-8a88-32cad789aa2c`) lines 16-50 [crates/gcode/src/search/fts/graph.rs:16-50]
  - Signature: `fn exact_symbol_matches_result(`
  - Purpose: # Summary

Executes an exact match query on a validated column (id, qualified_name, or name) in the code_symbols table for a given project, returning up to limit Symbol objects sorted by file location. [crates/gcode/src/search/fts/graph.rs:16-50]
- `row_string` (function) component `row_string [function]` (`b4cc47ee-1f6a-5e5a-8441-d13a2e35cd07`) lines 52-55 [crates/gcode/src/search/fts/graph.rs:52-55]
  - Signature: `fn row_string(row: &Row, column: &str) -> String {`
  - Purpose: Attempts to extract a `String` value from the specified column of a database row, returning `"<unavailable>"` as a fallback if the retrieval fails. [crates/gcode/src/search/fts/graph.rs:52-55]
- `suggestion_label` (function) component `suggestion_label [function]` (`0ff8ece5-1205-58ae-905a-49ce8f454e17`) lines 57-62 [crates/gcode/src/search/fts/graph.rs:57-62]
  - Signature: `fn suggestion_label(symbol: &Symbol) -> String {`
  - Purpose: This function returns a formatted string combining a symbol's qualified name with its source location (file path and line number) in the format `name (path:line)`. [crates/gcode/src/search/fts/graph.rs:57-62]
- `resolved_symbol` (function) component `resolved_symbol [function]` (`d1f8a2d2-61fd-58e2-b068-7689eccb3887`) lines 64-69 [crates/gcode/src/search/fts/graph.rs:64-69]
  - Signature: `fn resolved_symbol(symbol: &Symbol) -> ResolvedGraphSymbol {`
  - Purpose: This function constructs a `ResolvedGraphSymbol` from a `Symbol` by cloning its `id` and mapping its `name` field to `display_name`. [crates/gcode/src/search/fts/graph.rs:64-69]
- `resolve_graph_symbol_by_id` (function) component `resolve_graph_symbol_by_id [function]` (`3d1bee9a-3709-57f9-a28d-e88b9c8785a7`) lines 71-78 [crates/gcode/src/search/fts/graph.rs:71-78]
  - Signature: `pub fn resolve_graph_symbol_by_id(`
  - Purpose: Queries the database for an exact symbol match by ID within a specified project and returns the first result as a ResolvedGraphSymbol, or None if not found. [crates/gcode/src/search/fts/graph.rs:71-78]
- `resolve_from_candidates` (function) component `resolve_from_candidates [function]` (`a28d9b77-15e0-501a-8023-399c91273ecf`) lines 80-96 [crates/gcode/src/search/fts/graph.rs:80-96]
  - Signature: `fn resolve_from_candidates(candidates: Vec<Symbol>) -> (Option<ResolvedGraphSymbol>, Vec<String>) {`
  - Purpose: Returns a resolved symbol if exactly one candidate exists, deduplicated suggestion labels if multiple candidates exist, or None if no candidates are provided. [crates/gcode/src/search/fts/graph.rs:80-96]
- `decisive_resolution` (function) component `decisive_resolution [function]` (`f5aa9fa1-b1c7-562f-9575-b6658bdfd99c`) lines 98-103 [crates/gcode/src/search/fts/graph.rs:98-103]
  - Signature: `fn decisive_resolution(`
  - Purpose: # Summary

`decisive_resolution` attempts to resolve a symbol from candidates and returns the resolution with suggestions wrapped in `Option::Some` only if either a resolution is found or suggestions exist; otherwise returns `None`. [crates/gcode/src/search/fts/graph.rs:98-103]
- `resolve_graph_symbol` (function) component `resolve_graph_symbol [function]` (`c405005b-f37b-5014-9917-2ce4df0bf22c`) lines 108-147 [crates/gcode/src/search/fts/graph.rs:108-147]
  - Signature: `pub fn resolve_graph_symbol(`
  - Purpose: Resolves a symbol identifier within a project using cascading exact-match queries (id → qualified_name → name) with fuzzy and full-text search fallbacks. [crates/gcode/src/search/fts/graph.rs:108-147]

