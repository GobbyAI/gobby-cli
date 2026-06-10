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

# crates/gcode/src/search/fts/symbols.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

`crates/gcode/src/search/fts/symbols.rs` exposes 12 indexed API symbols.
[crates/gcode/src/search/fts/symbols.rs:15-18]
[crates/gcode/src/search/fts/symbols.rs:21-26]
[crates/gcode/src/search/fts/symbols.rs:28-33]
[crates/gcode/src/search/fts/symbols.rs:36-73]
[crates/gcode/src/search/fts/symbols.rs:76-112]
[crates/gcode/src/search/fts/symbols.rs:114-190]
[crates/gcode/src/search/fts/symbols.rs:192-225]
[crates/gcode/src/search/fts/symbols.rs:227-260]
[crates/gcode/src/search/fts/symbols.rs:262-337]
[crates/gcode/src/search/fts/symbols.rs:339-371]
[crates/gcode/src/search/fts/symbols.rs:374-386]
[crates/gcode/src/search/fts/symbols.rs:388-401]

## API Symbols

- `VisibleSearchOutcome` (class) component `VisibleSearchOutcome [class]` (`f1ba3605-a9dc-5827-b185-e9d8ece938e9`) lines 15-18 [crates/gcode/src/search/fts/symbols.rs:15-18]
  - Signature: `pub struct VisibleSearchOutcome<T> {`
  - Purpose: Indexed class `VisibleSearchOutcome` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:15-18]
- `ok` (function) component `ok [function]` (`eb9daf75-1417-5e1f-8ef8-a06b2416d482`) lines 21-26 [crates/gcode/src/search/fts/symbols.rs:21-26]
  - Signature: `fn ok(results: Vec<T>) -> Self {`
  - Purpose: Indexed function `ok` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:21-26]
- `degraded` (function) component `degraded [function]` (`9bde1975-6a34-5b77-bf7c-19bb8fa029b2`) lines 28-33 [crates/gcode/src/search/fts/symbols.rs:28-33]
  - Signature: `fn degraded(results: Vec<T>) -> Self {`
  - Purpose: Indexed function `degraded` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:28-33]
- `search_symbols_fts` (function) component `search_symbols_fts [function]` (`ded7d11d-b336-5edf-b8f3-1fbf422eb146`) lines 36-73 [crates/gcode/src/search/fts/symbols.rs:36-73]
  - Signature: `pub fn search_symbols_fts(`
  - Purpose: Indexed function `search_symbols_fts` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:36-73]
- `search_symbols_by_name` (function) component `search_symbols_by_name [function]` (`7f8858f7-6495-512a-a587-95d455f4fbbe`) lines 76-112 [crates/gcode/src/search/fts/symbols.rs:76-112]
  - Signature: `pub fn search_symbols_by_name(`
  - Purpose: Indexed function `search_symbols_by_name` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:76-112]
- `search_symbols_exact_first` (function) component `search_symbols_exact_first [function]` (`0b688623-4f21-5b00-a280-a1d2cbb2d5fb`) lines 114-190 [crates/gcode/src/search/fts/symbols.rs:114-190]
  - Signature: `pub fn search_symbols_exact_first(`
  - Purpose: Indexed function `search_symbols_exact_first` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:114-190]
- `search_symbols_fts_visible` (function) component `search_symbols_fts_visible [function]` (`f4b35aca-bf2c-543e-bf95-11d4a269183c`) lines 192-225 [crates/gcode/src/search/fts/symbols.rs:192-225]
  - Signature: `pub fn search_symbols_fts_visible(`
  - Purpose: Indexed function `search_symbols_fts_visible` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:192-225]
- `search_symbols_by_name_visible` (function) component `search_symbols_by_name_visible [function]` (`7c7b30bd-72c2-5b36-a1d9-f1afbc529baa`) lines 227-260 [crates/gcode/src/search/fts/symbols.rs:227-260]
  - Signature: `pub fn search_symbols_by_name_visible(`
  - Purpose: Indexed function `search_symbols_by_name_visible` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:227-260]
- `search_symbols_exact_first_visible` (function) component `search_symbols_exact_first_visible [function]` (`ff6f1083-33c6-59d1-9904-3b13f37ac480`) lines 262-337 [crates/gcode/src/search/fts/symbols.rs:262-337]
  - Signature: `pub fn search_symbols_exact_first_visible(`
  - Purpose: Indexed function `search_symbols_exact_first_visible` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:262-337]
- `query_visible_symbols_by_conditions` (function) component `query_visible_symbols_by_conditions [function]` (`ac175e0a-4769-5ecc-a380-df2871381992`) lines 339-371 [crates/gcode/src/search/fts/symbols.rs:339-371]
  - Signature: `fn query_visible_symbols_by_conditions(`
  - Purpose: Indexed function `query_visible_symbols_by_conditions` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:339-371]
- `search_text` (function) component `search_text [function]` (`3d569783-3c97-5d1a-add6-1b31103e4190`) lines 374-386 [crates/gcode/src/search/fts/symbols.rs:374-386]
  - Signature: `pub fn search_text(`
  - Purpose: Indexed function `search_text` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:374-386]
- `search_text_visible` (function) component `search_text_visible [function]` (`54024085-f7fd-576a-b6ed-d61818739cd7`) lines 388-401 [crates/gcode/src/search/fts/symbols.rs:388-401]
  - Signature: `pub fn search_text_visible(`
  - Purpose: Indexed function `search_text_visible` in `crates/gcode/src/search/fts/symbols.rs`. [crates/gcode/src/search/fts/symbols.rs:388-401]

