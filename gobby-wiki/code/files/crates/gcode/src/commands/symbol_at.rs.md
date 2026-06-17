---
title: crates/gcode/src/commands/symbol_at.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/symbol_at.rs
  ranges:
  - 16-20
  - 23-26
  - 30-33
  - 36-47
  - 50-55
  - 57-64
  - 66-122
  - 124-171
  - 173-183
  - 185-193
  - 195-197
  - 202-218
  - 220-233
  - 235-241
  - 243-268
  - 270-275
  - 277-282
  - 284-292
  - 294-311
  - 313-323
  - 325-327
  - 329-331
  - 333-339
  - 341-349
  - 351-365
  - 367-372
  - 374-383
  - 385-410
  - 412-422
  - 429-456
  - 458-463
  - 466-476
  - 479-485
  - 488-509
  - 512-520
  - 523-528
  - 531-549
  - 552-569
  - 572-590
  - 593-616
  - 619-640
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/symbol_at.rs:16-20](crates/gcode/src/commands/symbol_at.rs#L16-L20), [crates/gcode/src/commands/symbol_at.rs:23-26](crates/gcode/src/commands/symbol_at.rs#L23-L26), [crates/gcode/src/commands/symbol_at.rs:30-33](crates/gcode/src/commands/symbol_at.rs#L30-L33), [crates/gcode/src/commands/symbol_at.rs:36-47](crates/gcode/src/commands/symbol_at.rs#L36-L47), [crates/gcode/src/commands/symbol_at.rs:50-55](crates/gcode/src/commands/symbol_at.rs#L50-L55), [crates/gcode/src/commands/symbol_at.rs:57-64](crates/gcode/src/commands/symbol_at.rs#L57-L64), [crates/gcode/src/commands/symbol_at.rs:66-122](crates/gcode/src/commands/symbol_at.rs#L66-L122), [crates/gcode/src/commands/symbol_at.rs:124-171](crates/gcode/src/commands/symbol_at.rs#L124-L171), [crates/gcode/src/commands/symbol_at.rs:173-183](crates/gcode/src/commands/symbol_at.rs#L173-L183), [crates/gcode/src/commands/symbol_at.rs:185-193](crates/gcode/src/commands/symbol_at.rs#L185-L193), [crates/gcode/src/commands/symbol_at.rs:195-197](crates/gcode/src/commands/symbol_at.rs#L195-L197), [crates/gcode/src/commands/symbol_at.rs:202-218](crates/gcode/src/commands/symbol_at.rs#L202-L218), [crates/gcode/src/commands/symbol_at.rs:220-233](crates/gcode/src/commands/symbol_at.rs#L220-L233), [crates/gcode/src/commands/symbol_at.rs:235-241](crates/gcode/src/commands/symbol_at.rs#L235-L241), [crates/gcode/src/commands/symbol_at.rs:243-268](crates/gcode/src/commands/symbol_at.rs#L243-L268), [crates/gcode/src/commands/symbol_at.rs:270-275](crates/gcode/src/commands/symbol_at.rs#L270-L275), [crates/gcode/src/commands/symbol_at.rs:277-282](crates/gcode/src/commands/symbol_at.rs#L277-L282), [crates/gcode/src/commands/symbol_at.rs:284-292](crates/gcode/src/commands/symbol_at.rs#L284-L292), [crates/gcode/src/commands/symbol_at.rs:294-311](crates/gcode/src/commands/symbol_at.rs#L294-L311), [crates/gcode/src/commands/symbol_at.rs:313-323](crates/gcode/src/commands/symbol_at.rs#L313-L323), [crates/gcode/src/commands/symbol_at.rs:325-327](crates/gcode/src/commands/symbol_at.rs#L325-L327), [crates/gcode/src/commands/symbol_at.rs:329-331](crates/gcode/src/commands/symbol_at.rs#L329-L331), [crates/gcode/src/commands/symbol_at.rs:333-339](crates/gcode/src/commands/symbol_at.rs#L333-L339), [crates/gcode/src/commands/symbol_at.rs:341-349](crates/gcode/src/commands/symbol_at.rs#L341-L349), [crates/gcode/src/commands/symbol_at.rs:351-365](crates/gcode/src/commands/symbol_at.rs#L351-L365), [crates/gcode/src/commands/symbol_at.rs:367-372](crates/gcode/src/commands/symbol_at.rs#L367-L372), [crates/gcode/src/commands/symbol_at.rs:374-383](crates/gcode/src/commands/symbol_at.rs#L374-L383), [crates/gcode/src/commands/symbol_at.rs:385-410](crates/gcode/src/commands/symbol_at.rs#L385-L410), [crates/gcode/src/commands/symbol_at.rs:412-422](crates/gcode/src/commands/symbol_at.rs#L412-L422), [crates/gcode/src/commands/symbol_at.rs:429-456](crates/gcode/src/commands/symbol_at.rs#L429-L456), [crates/gcode/src/commands/symbol_at.rs:458-463](crates/gcode/src/commands/symbol_at.rs#L458-L463), [crates/gcode/src/commands/symbol_at.rs:466-476](crates/gcode/src/commands/symbol_at.rs#L466-L476), [crates/gcode/src/commands/symbol_at.rs:479-485](crates/gcode/src/commands/symbol_at.rs#L479-L485), [crates/gcode/src/commands/symbol_at.rs:488-509](crates/gcode/src/commands/symbol_at.rs#L488-L509), [crates/gcode/src/commands/symbol_at.rs:512-520](crates/gcode/src/commands/symbol_at.rs#L512-L520), [crates/gcode/src/commands/symbol_at.rs:523-528](crates/gcode/src/commands/symbol_at.rs#L523-L528), [crates/gcode/src/commands/symbol_at.rs:531-549](crates/gcode/src/commands/symbol_at.rs#L531-L549), [crates/gcode/src/commands/symbol_at.rs:552-569](crates/gcode/src/commands/symbol_at.rs#L552-L569), [crates/gcode/src/commands/symbol_at.rs:572-590](crates/gcode/src/commands/symbol_at.rs#L572-L590), [crates/gcode/src/commands/symbol_at.rs:593-616](crates/gcode/src/commands/symbol_at.rs#L593-L616), [crates/gcode/src/commands/symbol_at.rs:619-640](crates/gcode/src/commands/symbol_at.rs#L619-L640)

</details>

# crates/gcode/src/commands/symbol_at.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

Parses a user-supplied file location, resolves it against the project root, and selects the most relevant visible symbol at or near that position. The file ties together location parsing, byte-offset and line-distance helpers, symbol ranking and selection logic, and output formatting so `run` can return either a matched symbol or a structured fallback diagnostic with request metadata.
[crates/gcode/src/commands/symbol_at.rs:16-20]
[crates/gcode/src/commands/symbol_at.rs:23-26]
[crates/gcode/src/commands/symbol_at.rs:30-33]
[crates/gcode/src/commands/symbol_at.rs:36-47]
[crates/gcode/src/commands/symbol_at.rs:50-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ParsedLocation` | class | `struct ParsedLocation {` | `ParsedLocation [class]` | `23a18fcf-f191-5f18-8f90-f96c31be5e74` | 16-20 [crates/gcode/src/commands/symbol_at.rs:16-20] | Indexed class `ParsedLocation` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:16-20] |
| `SymbolAtTarget` | class | `struct SymbolAtTarget {` | `SymbolAtTarget [class]` | `9ab78ade-aec5-51c5-bed0-826bc898d12a` | 23-26 [crates/gcode/src/commands/symbol_at.rs:23-26] | Indexed class `SymbolAtTarget` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:23-26] |
| `MatchKind` | type | `enum MatchKind {` | `MatchKind [type]` | `f1fb17f6-d9a7-5b93-acf7-25ccfaddde73` | 30-33 [crates/gcode/src/commands/symbol_at.rs:30-33] | Indexed type `MatchKind` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:30-33] |
| `SymbolAtLookup` | class | `struct SymbolAtLookup {` | `SymbolAtLookup [class]` | `a281f804-6a20-5d49-9471-61b0972ea102` | 36-47 [crates/gcode/src/commands/symbol_at.rs:36-47] | Indexed class `SymbolAtLookup` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:36-47] |
| `SelectedSymbol` | class | `struct SelectedSymbol<'a> {` | `SelectedSymbol [class]` | `b1661aec-3cb2-5c81-ac62-cf91adba92a9` | 50-55 [crates/gcode/src/commands/symbol_at.rs:50-55] | Indexed class `SelectedSymbol` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:50-55] |
| `requested_file_for_freshness` | function | `pub fn requested_file_for_freshness(` | `requested_file_for_freshness [function]` | `16ef6bf6-1d54-57b8-b278-3596c704aad1` | 57-64 [crates/gcode/src/commands/symbol_at.rs:57-64] | Indexed function `requested_file_for_freshness` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:57-64] |
| `run` | function | `pub fn run(` | `run [function]` | `ebf44413-29e7-5c34-b640-89e53e9a7be2` | 66-122 [crates/gcode/src/commands/symbol_at.rs:66-122] | Indexed function `run` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:66-122] |
| `parse_location` | function | `fn parse_location(location: &str, explicit_line: Option<usize>) -> anyhow::Result<ParsedLocation> {` | `parse_location [function]` | `71d67d90-12e7-5f13-8802-a13b3ace34d0` | 124-171 [crates/gcode/src/commands/symbol_at.rs:124-171] | Indexed function `parse_location` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:124-171] |
| `has_encoded_line` | function | `fn has_encoded_line(location: &str) -> bool {` | `has_encoded_line [function]` | `69dec041-4f6c-5ca9-b704-1651529382ca` | 173-183 [crates/gcode/src/commands/symbol_at.rs:173-183] | Indexed function `has_encoded_line` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:173-183] |
| `parse_positive_component` | function | `fn parse_positive_component(kind: &str, value: &str) -> anyhow::Result<usize> {` | `parse_positive_component [function]` | `cb59795f-fe69-59d4-9ec6-2021e45743d9` | 185-193 [crates/gcode/src/commands/symbol_at.rs:185-193] | Indexed function `parse_positive_component` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:185-193] |
| `is_numeric_text` | function | `fn is_numeric_text(value: &str) -> bool {` | `is_numeric_text [function]` | `b36003a1-765f-5330-80ef-049c68dfe737` | 195-197 [crates/gcode/src/commands/symbol_at.rs:195-197] | Indexed function `is_numeric_text` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:195-197] |
| `line_column_to_byte_offset` | function | `fn line_column_to_byte_offset(source: &[u8], line: usize, column: usize) -> anyhow::Result<usize> {` | `line_column_to_byte_offset [function]` | `2ef0e4f8-9c7e-58a6-9035-2418d830249e` | 202-218 [crates/gcode/src/commands/symbol_at.rs:202-218] | Indexed function `line_column_to_byte_offset` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:202-218] |
| `line_bounds` | function | `fn line_bounds(source: &[u8], line: usize) -> Option<(usize, usize)> {` | `line_bounds [function]` | `de1f726f-83f1-5bb4-8453-edb3c34206d4` | 220-233 [crates/gcode/src/commands/symbol_at.rs:220-233] | Indexed function `line_bounds` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:220-233] |
| `trim_cr` | function | `fn trim_cr(source: &[u8], start: usize, end: usize) -> usize {` | `trim_cr [function]` | `f3e332d2-ddd3-5df2-b0f8-bab6194a9123` | 235-241 [crates/gcode/src/commands/symbol_at.rs:235-241] | Indexed function `trim_cr` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:235-241] |
| `select_symbol` | function | `fn select_symbol(symbols: &[Symbol], target: SymbolAtTarget) -> Option<SelectedSymbol<'_>> {` | `select_symbol [function]` | `ddbfc0d3-511f-5a27-88e3-a161f21da5a8` | 243-268 [crates/gcode/src/commands/symbol_at.rs:243-268] | Indexed function `select_symbol` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:243-268] |
| `contains_target` | function | `fn contains_target(symbol: &Symbol, target: SymbolAtTarget) -> bool {` | `contains_target [function]` | `01602b75-b275-5c90-9ee9-f4284326e428` | 270-275 [crates/gcode/src/commands/symbol_at.rs:270-275] | Indexed function `contains_target` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:270-275] |
| `compare_containing` | function | `fn compare_containing(left: &Symbol, right: &Symbol) -> Ordering {` | `compare_containing [function]` | `83181fd3-18a9-5f79-b67e-583758271ce6` | 277-282 [crates/gcode/src/commands/symbol_at.rs:277-282] | Indexed function `compare_containing` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:277-282] |
| `compare_nearest` | function | `fn compare_nearest(left: &Symbol, right: &Symbol, target: SymbolAtTarget) -> Ordering {` | `compare_nearest [function]` | `d1ea1907-4191-55a5-90b3-582609b9b9a2` | 284-292 [crates/gcode/src/commands/symbol_at.rs:284-292] | Indexed function `compare_nearest` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:284-292] |
| `compare_previous_preference` | function | `fn compare_previous_preference(left: &Symbol, right: &Symbol, target: SymbolAtTarget) -> Ordering {` | `compare_previous_preference [function]` | `72955b3a-4c61-57ca-bd2b-0c584060951e` | 294-311 [crates/gcode/src/commands/symbol_at.rs:294-311] | Indexed function `compare_previous_preference` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:294-311] |
| `is_previous_symbol` | function | `fn is_previous_symbol(symbol: &Symbol, target: SymbolAtTarget) -> bool {` | `is_previous_symbol [function]` | `1f6c60b2-a56c-5c2f-9434-c831a04eb76b` | 313-323 [crates/gcode/src/commands/symbol_at.rs:313-323] | Indexed function `is_previous_symbol` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:313-323] |
| `line_span` | function | `fn line_span(symbol: &Symbol) -> usize {` | `line_span [function]` | `46d9e4b6-f3f9-548f-8677-243aa0cba19f` | 325-327 [crates/gcode/src/commands/symbol_at.rs:325-327] | Indexed function `line_span` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:325-327] |
| `byte_span` | function | `fn byte_span(symbol: &Symbol) -> usize {` | `byte_span [function]` | `88360e0e-6793-5775-ac15-040e8863dabf` | 329-331 [crates/gcode/src/commands/symbol_at.rs:329-331] | Indexed function `byte_span` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:329-331] |
| `line_distance` | function | `fn line_distance(symbol: &Symbol, line: usize) -> usize {` | `line_distance [function]` | `725c0860-177d-54b8-9461-8e21407b1aad` | 333-339 [crates/gcode/src/commands/symbol_at.rs:333-339] | Indexed function `line_distance` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:333-339] |
| `byte_distance` | function | `fn byte_distance(symbol: &Symbol, offset: usize) -> usize {` | `byte_distance [function]` | `805f80ac-a6a8-5708-a6e9-2c52f96d342d` | 341-349 [crates/gcode/src/commands/symbol_at.rs:341-349] | Indexed function `byte_distance` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:341-349] |
| `lookup_for_selection` | function | `fn lookup_for_selection(` | `lookup_for_selection [function]` | `b135c06c-67c6-5ab8-b0fb-3ef517e4544e` | 351-365 [crates/gcode/src/commands/symbol_at.rs:351-365] | Indexed function `lookup_for_selection` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:351-365] |
| `symbol_source` | function | `fn symbol_source(source: &[u8], symbol: &Symbol) -> (String, usize) {` | `symbol_source [function]` | `b8d73228-d8e6-501c-ae29-87edbf4f6e0c` | 367-372 [crates/gcode/src/commands/symbol_at.rs:367-372] | Indexed function `symbol_source` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:367-372] |
| `symbol_at_json_value` | function | `fn symbol_at_json_value(` | `symbol_at_json_value [function]` | `e22dde31-2a1c-594d-b067-bc21209e9961` | 374-383 [crates/gcode/src/commands/symbol_at.rs:374-383] | Indexed function `symbol_at_json_value` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:374-383] |
| `fallback_diagnostic` | function | `fn fallback_diagnostic(symbol: &Symbol, lookup: &SymbolAtLookup, quiet: bool) -> Option<String> {` | `fallback_diagnostic [function]` | `bc63b2c2-a007-5b5d-b4d4-d9c59f3a435f` | 385-410 [crates/gcode/src/commands/symbol_at.rs:385-410] | Indexed function `fallback_diagnostic` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:385-410] |
| `plural` | function | `fn plural(unit: &'static str, value: usize) -> &'static str {` | `plural [function]` | `cdbc3afb-939b-582f-a532-dbc689e26d88` | 412-422 [crates/gcode/src/commands/symbol_at.rs:412-422] | Indexed function `plural` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:412-422] |
| `symbol` | function | `fn symbol(` | `symbol [function]` | `46d192ab-301d-5dc0-bdc7-2a183442a67b` | 429-456 [crates/gcode/src/commands/symbol_at.rs:429-456] | Indexed function `symbol` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:429-456] |
| `error_text` | function | `fn error_text<T>(result: anyhow::Result<T>) -> String {` | `error_text [function]` | `9cd2d7c4-e33a-51f5-9a82-9bc1260d123e` | 458-463 [crates/gcode/src/commands/symbol_at.rs:458-463] | Indexed function `error_text` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:458-463] |
| `parses_path_line_and_column_from_the_right` | function | `fn parses_path_line_and_column_from_the_right() {` | `parses_path_line_and_column_from_the_right [function]` | `94cbf927-c0b3-517a-957e-864cdd08d096` | 466-476 [crates/gcode/src/commands/symbol_at.rs:466-476] | Indexed function `parses_path_line_and_column_from_the_right` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:466-476] |
| `parses_path_with_separate_line` | function | `fn parses_path_with_separate_line() {` | `parses_path_with_separate_line [function]` | `1b4a8d5a-4007-58c5-a62b-98c4d6dbc895` | 479-485 [crates/gcode/src/commands/symbol_at.rs:479-485] | Indexed function `parses_path_with_separate_line` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:479-485] |
| `rejects_invalid_location_forms` | function | `fn rejects_invalid_location_forms() {` | `rejects_invalid_location_forms [function]` | `95673617-cb70-5189-ab43-969497a27780` | 488-509 [crates/gcode/src/commands/symbol_at.rs:488-509] | Indexed function `rejects_invalid_location_forms` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:488-509] |
| `converts_one_based_byte_columns_to_offsets` | function | `fn converts_one_based_byte_columns_to_offsets() {` | `converts_one_based_byte_columns_to_offsets [function]` | `4916be6e-bffb-5339-a423-ff5691947193` | 512-520 [crates/gcode/src/commands/symbol_at.rs:512-520] | Indexed function `converts_one_based_byte_columns_to_offsets` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:512-520] |
| `rejects_out_of_range_columns` | function | `fn rejects_out_of_range_columns() {` | `rejects_out_of_range_columns [function]` | `2b10c626-8177-5b38-bff2-b4e51ceea8ea` | 523-528 [crates/gcode/src/commands/symbol_at.rs:523-528] | Indexed function `rejects_out_of_range_columns` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:523-528] |
| `containing_selection_prefers_smallest_span_then_later_start` | function | `fn containing_selection_prefers_smallest_span_then_later_start() {` | `containing_selection_prefers_smallest_span_then_later_start [function]` | `f2ffa2e8-24cf-5b06-8989-86418b9f77c1` | 531-549 [crates/gcode/src/commands/symbol_at.rs:531-549] | Indexed function `containing_selection_prefers_smallest_span_then_later_start` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:531-549] |
| `nearest_selection_prefers_previous_on_equal_line_distance` | function | `fn nearest_selection_prefers_previous_on_equal_line_distance() {` | `nearest_selection_prefers_previous_on_equal_line_distance [function]` | `63a0a1b8-4aad-59d1-adc6-a16393cb0a93` | 552-569 [crates/gcode/src/commands/symbol_at.rs:552-569] | Indexed function `nearest_selection_prefers_previous_on_equal_line_distance` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:552-569] |
| `nearest_selection_uses_byte_distance_for_column_ties` | function | `fn nearest_selection_uses_byte_distance_for_column_ties() {` | `nearest_selection_uses_byte_distance_for_column_ties [function]` | `2b489723-649f-57ee-bd29-005f34a22191` | 572-590 [crates/gcode/src/commands/symbol_at.rs:572-590] | Indexed function `nearest_selection_uses_byte_distance_for_column_ties` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:572-590] |
| `lookup_json_includes_source_and_metadata` | function | `fn lookup_json_includes_source_and_metadata() {` | `lookup_json_includes_source_and_metadata [function]` | `c75781ef-95fc-5aa2-ae9f-2f9c7a3da0cf` | 593-616 [crates/gcode/src/commands/symbol_at.rs:593-616] | Indexed function `lookup_json_includes_source_and_metadata` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:593-616] |
| `nearest_diagnostic_is_suppressed_when_quiet_or_containing` | function | `fn nearest_diagnostic_is_suppressed_when_quiet_or_containing() {` | `nearest_diagnostic_is_suppressed_when_quiet_or_containing [function]` | `e3005cae-ebe9-5794-b6c0-2bc6ef8183bd` | 619-640 [crates/gcode/src/commands/symbol_at.rs:619-640] | Indexed function `nearest_diagnostic_is_suppressed_when_quiet_or_containing` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:619-640] |
