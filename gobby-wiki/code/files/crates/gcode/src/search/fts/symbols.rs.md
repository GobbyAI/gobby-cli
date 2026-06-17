---
title: crates/gcode/src/search/fts/symbols.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/symbols.rs
  ranges:
  - 15-18
  - 21-26
  - 28-33
  - 36-73
  - 76-112
  - 114-190
  - 192-225
  - 227-260
  - 262-337
  - 339-371
  - 374-386
  - 388-401
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/fts/symbols.rs:15-18](crates/gcode/src/search/fts/symbols.rs#L15-L18), [crates/gcode/src/search/fts/symbols.rs:21-26](crates/gcode/src/search/fts/symbols.rs#L21-L26), [crates/gcode/src/search/fts/symbols.rs:28-33](crates/gcode/src/search/fts/symbols.rs#L28-L33), [crates/gcode/src/search/fts/symbols.rs:36-73](crates/gcode/src/search/fts/symbols.rs#L36-L73), [crates/gcode/src/search/fts/symbols.rs:76-112](crates/gcode/src/search/fts/symbols.rs#L76-L112), [crates/gcode/src/search/fts/symbols.rs:114-190](crates/gcode/src/search/fts/symbols.rs#L114-L190), [crates/gcode/src/search/fts/symbols.rs:192-225](crates/gcode/src/search/fts/symbols.rs#L192-L225), [crates/gcode/src/search/fts/symbols.rs:227-260](crates/gcode/src/search/fts/symbols.rs#L227-L260), [crates/gcode/src/search/fts/symbols.rs:262-337](crates/gcode/src/search/fts/symbols.rs#L262-L337), [crates/gcode/src/search/fts/symbols.rs:339-371](crates/gcode/src/search/fts/symbols.rs#L339-L371), [crates/gcode/src/search/fts/symbols.rs:374-386](crates/gcode/src/search/fts/symbols.rs#L374-L386), [crates/gcode/src/search/fts/symbols.rs:388-401](crates/gcode/src/search/fts/symbols.rs#L388-L401)

</details>

# crates/gcode/src/search/fts/symbols.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

This file defines the symbol-search layer for the FTS-backed gcode search pipeline. It introduces `VisibleSearchOutcome<T>` as a small wrapper for returned items plus a `degraded` flag, then builds several query paths on top of the shared query helpers and `postgres::Client`: full-text search, name-based LIKE fallback, exact-match-first ranking, and visible-only variants that route through `query_visible_symbols_by_conditions` and return whether the result was degraded.
[crates/gcode/src/search/fts/symbols.rs:15-18]
[crates/gcode/src/search/fts/symbols.rs:21-26]
[crates/gcode/src/search/fts/symbols.rs:28-33]
[crates/gcode/src/search/fts/symbols.rs:36-73]
[crates/gcode/src/search/fts/symbols.rs:76-112]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `VisibleSearchOutcome` | class | `pub struct VisibleSearchOutcome<T> {` | `VisibleSearchOutcome [class]` | `f1ba3605-a9dc-5827-b185-e9d8ece938e9` | 15-18 [crates/gcode/src/search/fts/symbols.rs:15-18] | Indexed class `VisibleSearchOutcome` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:15-18] |
| `ok` | function | `fn ok(results: Vec<T>) -> Self {` | `ok [function]` | `eb9daf75-1417-5e1f-8ef8-a06b2416d482` | 21-26 [crates/gcode/src/search/fts/symbols.rs:21-26] | Indexed function `ok` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:21-26] |
| `degraded` | function | `fn degraded(results: Vec<T>) -> Self {` | `degraded [function]` | `9bde1975-6a34-5b77-bf7c-19bb8fa029b2` | 28-33 [crates/gcode/src/search/fts/symbols.rs:28-33] | Indexed function `degraded` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:28-33] |
| `search_symbols_fts` | function | `pub fn search_symbols_fts(` | `search_symbols_fts [function]` | `ded7d11d-b336-5edf-b8f3-1fbf422eb146` | 36-73 [crates/gcode/src/search/fts/symbols.rs:36-73] | Indexed function `search_symbols_fts` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:36-73] |
| `search_symbols_by_name` | function | `pub fn search_symbols_by_name(` | `search_symbols_by_name [function]` | `7f8858f7-6495-512a-a587-95d455f4fbbe` | 76-112 [crates/gcode/src/search/fts/symbols.rs:76-112] | Indexed function `search_symbols_by_name` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:76-112] |
| `search_symbols_exact_first` | function | `pub fn search_symbols_exact_first(` | `search_symbols_exact_first [function]` | `0b688623-4f21-5b00-a280-a1d2cbb2d5fb` | 114-190 [crates/gcode/src/search/fts/symbols.rs:114-190] | Indexed function `search_symbols_exact_first` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:114-190] |
| `search_symbols_fts_visible` | function | `pub fn search_symbols_fts_visible(` | `search_symbols_fts_visible [function]` | `f4b35aca-bf2c-543e-bf95-11d4a269183c` | 192-225 [crates/gcode/src/search/fts/symbols.rs:192-225] | Indexed function `search_symbols_fts_visible` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:192-225] |
| `search_symbols_by_name_visible` | function | `pub fn search_symbols_by_name_visible(` | `search_symbols_by_name_visible [function]` | `7c7b30bd-72c2-5b36-a1d9-f1afbc529baa` | 227-260 [crates/gcode/src/search/fts/symbols.rs:227-260] | Indexed function `search_symbols_by_name_visible` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:227-260] |
| `search_symbols_exact_first_visible` | function | `pub fn search_symbols_exact_first_visible(` | `search_symbols_exact_first_visible [function]` | `ff6f1083-33c6-59d1-9904-3b13f37ac480` | 262-337 [crates/gcode/src/search/fts/symbols.rs:262-337] | Indexed function `search_symbols_exact_first_visible` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:262-337] |
| `query_visible_symbols_by_conditions` | function | `fn query_visible_symbols_by_conditions(` | `query_visible_symbols_by_conditions [function]` | `ac175e0a-4769-5ecc-a380-df2871381992` | 339-371 [crates/gcode/src/search/fts/symbols.rs:339-371] | Indexed function `query_visible_symbols_by_conditions` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:339-371] |
| `search_text` | function | `pub fn search_text(` | `search_text [function]` | `3d569783-3c97-5d1a-add6-1b31103e4190` | 374-386 [crates/gcode/src/search/fts/symbols.rs:374-386] | Indexed function `search_text` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:374-386] |
| `search_text_visible` | function | `pub fn search_text_visible(` | `search_text_visible [function]` | `54024085-f7fd-576a-b6ed-d61818739cd7` | 388-401 [crates/gcode/src/search/fts/symbols.rs:388-401] | Indexed function `search_text_visible` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:388-401] |
