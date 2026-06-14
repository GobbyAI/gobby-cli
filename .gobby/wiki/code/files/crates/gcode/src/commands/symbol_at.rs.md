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

# crates/gcode/src/commands/symbol_at.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

This file implements a symbol-at-location lookup command. It parses a location specification (file path, line, and optional column), retrieves symbols from the database for that file, reads the source code, and finds the best-matching symbol at the requested position.

The core workflow: `parse_location` converts a location string and line number into a ParsedLocation with file, line, and optional column. `run` then normalizes the file path, fetches visible symbols from the database, and uses `line_column_to_byte_offset` to convert the location to a SymbolAtTarget (line and byte offset). The `select_symbol` function chooses the best match from candidates using two strategies: "containing" (symbols that encompass the target position, preferring smallest span then latest start) or "nearest" (closest symbol by line then byte distance, preferring previous symbols on ties). Helper functions like `contains_target`, `compare_containing`, and `compare_nearest` implement the selection logic. Finally, `lookup_for_selection` packages the result with metadata (match kind, distances) for JSON serialization. Utility functions handle source parsing (detecting line bounds, trimming carriage returns, validating numeric components) and output formatting.
[crates/gcode/src/commands/symbol_at.rs:16-20]
[crates/gcode/src/commands/symbol_at.rs:23-26]
[crates/gcode/src/commands/symbol_at.rs:30-33]
[crates/gcode/src/commands/symbol_at.rs:36-47]
[crates/gcode/src/commands/symbol_at.rs:50-55]

## API Symbols

- `ParsedLocation` (class) component `ParsedLocation [class]` (`23a18fcf-f191-5f18-8f90-f96c31be5e74`) lines 16-20 [crates/gcode/src/commands/symbol_at.rs:16-20]
  - Signature: `struct ParsedLocation {`
  - Purpose: Indexed class `ParsedLocation` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:16-20]
- `SymbolAtTarget` (class) component `SymbolAtTarget [class]` (`9ab78ade-aec5-51c5-bed0-826bc898d12a`) lines 23-26 [crates/gcode/src/commands/symbol_at.rs:23-26]
  - Signature: `struct SymbolAtTarget {`
  - Purpose: Indexed class `SymbolAtTarget` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:23-26]
- `MatchKind` (type) component `MatchKind [type]` (`f1fb17f6-d9a7-5b93-acf7-25ccfaddde73`) lines 30-33 [crates/gcode/src/commands/symbol_at.rs:30-33]
  - Signature: `enum MatchKind {`
  - Purpose: Indexed type `MatchKind` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:30-33]
- `SymbolAtLookup` (class) component `SymbolAtLookup [class]` (`a281f804-6a20-5d49-9471-61b0972ea102`) lines 36-47 [crates/gcode/src/commands/symbol_at.rs:36-47]
  - Signature: `struct SymbolAtLookup {`
  - Purpose: Indexed class `SymbolAtLookup` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:36-47]
- `SelectedSymbol` (class) component `SelectedSymbol [class]` (`b1661aec-3cb2-5c81-ac62-cf91adba92a9`) lines 50-55 [crates/gcode/src/commands/symbol_at.rs:50-55]
  - Signature: `struct SelectedSymbol<'a> {`
  - Purpose: Indexed class `SelectedSymbol` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:50-55]
- `requested_file_for_freshness` (function) component `requested_file_for_freshness [function]` (`16ef6bf6-1d54-57b8-b278-3596c704aad1`) lines 57-64 [crates/gcode/src/commands/symbol_at.rs:57-64]
  - Signature: `pub fn requested_file_for_freshness(`
  - Purpose: Indexed function `requested_file_for_freshness` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:57-64]
- `run` (function) component `run [function]` (`ebf44413-29e7-5c34-b640-89e53e9a7be2`) lines 66-122 [crates/gcode/src/commands/symbol_at.rs:66-122]
  - Signature: `pub fn run(`
  - Purpose: Indexed function `run` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:66-122]
- `parse_location` (function) component `parse_location [function]` (`71d67d90-12e7-5f13-8802-a13b3ace34d0`) lines 124-171 [crates/gcode/src/commands/symbol_at.rs:124-171]
  - Signature: `fn parse_location(location: &str, explicit_line: Option<usize>) -> anyhow::Result<ParsedLocation> {`
  - Purpose: Indexed function `parse_location` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:124-171]
- `has_encoded_line` (function) component `has_encoded_line [function]` (`69dec041-4f6c-5ca9-b704-1651529382ca`) lines 173-183 [crates/gcode/src/commands/symbol_at.rs:173-183]
  - Signature: `fn has_encoded_line(location: &str) -> bool {`
  - Purpose: Indexed function `has_encoded_line` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:173-183]
- `parse_positive_component` (function) component `parse_positive_component [function]` (`cb59795f-fe69-59d4-9ec6-2021e45743d9`) lines 185-193 [crates/gcode/src/commands/symbol_at.rs:185-193]
  - Signature: `fn parse_positive_component(kind: &str, value: &str) -> anyhow::Result<usize> {`
  - Purpose: Indexed function `parse_positive_component` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:185-193]
- `is_numeric_text` (function) component `is_numeric_text [function]` (`b36003a1-765f-5330-80ef-049c68dfe737`) lines 195-197 [crates/gcode/src/commands/symbol_at.rs:195-197]
  - Signature: `fn is_numeric_text(value: &str) -> bool {`
  - Purpose: Indexed function `is_numeric_text` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:195-197]
- `line_column_to_byte_offset` (function) component `line_column_to_byte_offset [function]` (`2ef0e4f8-9c7e-58a6-9035-2418d830249e`) lines 202-218 [crates/gcode/src/commands/symbol_at.rs:202-218]
  - Signature: `fn line_column_to_byte_offset(source: &[u8], line: usize, column: usize) -> anyhow::Result<usize> {`
  - Purpose: Indexed function `line_column_to_byte_offset` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:202-218]
- `line_bounds` (function) component `line_bounds [function]` (`de1f726f-83f1-5bb4-8453-edb3c34206d4`) lines 220-233 [crates/gcode/src/commands/symbol_at.rs:220-233]
  - Signature: `fn line_bounds(source: &[u8], line: usize) -> Option<(usize, usize)> {`
  - Purpose: Indexed function `line_bounds` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:220-233]
- `trim_cr` (function) component `trim_cr [function]` (`f3e332d2-ddd3-5df2-b0f8-bab6194a9123`) lines 235-241 [crates/gcode/src/commands/symbol_at.rs:235-241]
  - Signature: `fn trim_cr(source: &[u8], start: usize, end: usize) -> usize {`
  - Purpose: Indexed function `trim_cr` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:235-241]
- `select_symbol` (function) component `select_symbol [function]` (`ddbfc0d3-511f-5a27-88e3-a161f21da5a8`) lines 243-268 [crates/gcode/src/commands/symbol_at.rs:243-268]
  - Signature: `fn select_symbol(symbols: &[Symbol], target: SymbolAtTarget) -> Option<SelectedSymbol<'_>> {`
  - Purpose: Indexed function `select_symbol` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:243-268]
- `contains_target` (function) component `contains_target [function]` (`01602b75-b275-5c90-9ee9-f4284326e428`) lines 270-275 [crates/gcode/src/commands/symbol_at.rs:270-275]
  - Signature: `fn contains_target(symbol: &Symbol, target: SymbolAtTarget) -> bool {`
  - Purpose: Indexed function `contains_target` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:270-275]
- `compare_containing` (function) component `compare_containing [function]` (`83181fd3-18a9-5f79-b67e-583758271ce6`) lines 277-282 [crates/gcode/src/commands/symbol_at.rs:277-282]
  - Signature: `fn compare_containing(left: &Symbol, right: &Symbol) -> Ordering {`
  - Purpose: Indexed function `compare_containing` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:277-282]
- `compare_nearest` (function) component `compare_nearest [function]` (`d1ea1907-4191-55a5-90b3-582609b9b9a2`) lines 284-292 [crates/gcode/src/commands/symbol_at.rs:284-292]
  - Signature: `fn compare_nearest(left: &Symbol, right: &Symbol, target: SymbolAtTarget) -> Ordering {`
  - Purpose: Indexed function `compare_nearest` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:284-292]
- `compare_previous_preference` (function) component `compare_previous_preference [function]` (`72955b3a-4c61-57ca-bd2b-0c584060951e`) lines 294-311 [crates/gcode/src/commands/symbol_at.rs:294-311]
  - Signature: `fn compare_previous_preference(left: &Symbol, right: &Symbol, target: SymbolAtTarget) -> Ordering {`
  - Purpose: Indexed function `compare_previous_preference` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:294-311]
- `is_previous_symbol` (function) component `is_previous_symbol [function]` (`1f6c60b2-a56c-5c2f-9434-c831a04eb76b`) lines 313-323 [crates/gcode/src/commands/symbol_at.rs:313-323]
  - Signature: `fn is_previous_symbol(symbol: &Symbol, target: SymbolAtTarget) -> bool {`
  - Purpose: Indexed function `is_previous_symbol` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:313-323]
- `line_span` (function) component `line_span [function]` (`46d9e4b6-f3f9-548f-8677-243aa0cba19f`) lines 325-327 [crates/gcode/src/commands/symbol_at.rs:325-327]
  - Signature: `fn line_span(symbol: &Symbol) -> usize {`
  - Purpose: Indexed function `line_span` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:325-327]
- `byte_span` (function) component `byte_span [function]` (`88360e0e-6793-5775-ac15-040e8863dabf`) lines 329-331 [crates/gcode/src/commands/symbol_at.rs:329-331]
  - Signature: `fn byte_span(symbol: &Symbol) -> usize {`
  - Purpose: Indexed function `byte_span` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:329-331]
- `line_distance` (function) component `line_distance [function]` (`725c0860-177d-54b8-9461-8e21407b1aad`) lines 333-339 [crates/gcode/src/commands/symbol_at.rs:333-339]
  - Signature: `fn line_distance(symbol: &Symbol, line: usize) -> usize {`
  - Purpose: Indexed function `line_distance` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:333-339]
- `byte_distance` (function) component `byte_distance [function]` (`805f80ac-a6a8-5708-a6e9-2c52f96d342d`) lines 341-349 [crates/gcode/src/commands/symbol_at.rs:341-349]
  - Signature: `fn byte_distance(symbol: &Symbol, offset: usize) -> usize {`
  - Purpose: Indexed function `byte_distance` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:341-349]
- `lookup_for_selection` (function) component `lookup_for_selection [function]` (`b135c06c-67c6-5ab8-b0fb-3ef517e4544e`) lines 351-365 [crates/gcode/src/commands/symbol_at.rs:351-365]
  - Signature: `fn lookup_for_selection(`
  - Purpose: Indexed function `lookup_for_selection` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:351-365]
- `symbol_source` (function) component `symbol_source [function]` (`b8d73228-d8e6-501c-ae29-87edbf4f6e0c`) lines 367-372 [crates/gcode/src/commands/symbol_at.rs:367-372]
  - Signature: `fn symbol_source(source: &[u8], symbol: &Symbol) -> (String, usize) {`
  - Purpose: Indexed function `symbol_source` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:367-372]
- `symbol_at_json_value` (function) component `symbol_at_json_value [function]` (`e22dde31-2a1c-594d-b067-bc21209e9961`) lines 374-383 [crates/gcode/src/commands/symbol_at.rs:374-383]
  - Signature: `fn symbol_at_json_value(`
  - Purpose: Indexed function `symbol_at_json_value` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:374-383]
- `fallback_diagnostic` (function) component `fallback_diagnostic [function]` (`bc63b2c2-a007-5b5d-b4d4-d9c59f3a435f`) lines 385-410 [crates/gcode/src/commands/symbol_at.rs:385-410]
  - Signature: `fn fallback_diagnostic(symbol: &Symbol, lookup: &SymbolAtLookup, quiet: bool) -> Option<String> {`
  - Purpose: Indexed function `fallback_diagnostic` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:385-410]
- `plural` (function) component `plural [function]` (`cdbc3afb-939b-582f-a532-dbc689e26d88`) lines 412-422 [crates/gcode/src/commands/symbol_at.rs:412-422]
  - Signature: `fn plural(unit: &'static str, value: usize) -> &'static str {`
  - Purpose: Indexed function `plural` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:412-422]
- `symbol` (function) component `symbol [function]` (`46d192ab-301d-5dc0-bdc7-2a183442a67b`) lines 429-456 [crates/gcode/src/commands/symbol_at.rs:429-456]
  - Signature: `fn symbol(`
  - Purpose: Indexed function `symbol` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:429-456]
- `error_text` (function) component `error_text [function]` (`9cd2d7c4-e33a-51f5-9a82-9bc1260d123e`) lines 458-463 [crates/gcode/src/commands/symbol_at.rs:458-463]
  - Signature: `fn error_text<T>(result: anyhow::Result<T>) -> String {`
  - Purpose: Indexed function `error_text` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:458-463]
- `parses_path_line_and_column_from_the_right` (function) component `parses_path_line_and_column_from_the_right [function]` (`94cbf927-c0b3-517a-957e-864cdd08d096`) lines 466-476 [crates/gcode/src/commands/symbol_at.rs:466-476]
  - Signature: `fn parses_path_line_and_column_from_the_right() {`
  - Purpose: Indexed function `parses_path_line_and_column_from_the_right` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:466-476]
- `parses_path_with_separate_line` (function) component `parses_path_with_separate_line [function]` (`1b4a8d5a-4007-58c5-a62b-98c4d6dbc895`) lines 479-485 [crates/gcode/src/commands/symbol_at.rs:479-485]
  - Signature: `fn parses_path_with_separate_line() {`
  - Purpose: Indexed function `parses_path_with_separate_line` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:479-485]
- `rejects_invalid_location_forms` (function) component `rejects_invalid_location_forms [function]` (`95673617-cb70-5189-ab43-969497a27780`) lines 488-509 [crates/gcode/src/commands/symbol_at.rs:488-509]
  - Signature: `fn rejects_invalid_location_forms() {`
  - Purpose: Indexed function `rejects_invalid_location_forms` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:488-509]
- `converts_one_based_byte_columns_to_offsets` (function) component `converts_one_based_byte_columns_to_offsets [function]` (`4916be6e-bffb-5339-a423-ff5691947193`) lines 512-520 [crates/gcode/src/commands/symbol_at.rs:512-520]
  - Signature: `fn converts_one_based_byte_columns_to_offsets() {`
  - Purpose: Indexed function `converts_one_based_byte_columns_to_offsets` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:512-520]
- `rejects_out_of_range_columns` (function) component `rejects_out_of_range_columns [function]` (`2b10c626-8177-5b38-bff2-b4e51ceea8ea`) lines 523-528 [crates/gcode/src/commands/symbol_at.rs:523-528]
  - Signature: `fn rejects_out_of_range_columns() {`
  - Purpose: Indexed function `rejects_out_of_range_columns` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:523-528]
- `containing_selection_prefers_smallest_span_then_later_start` (function) component `containing_selection_prefers_smallest_span_then_later_start [function]` (`f2ffa2e8-24cf-5b06-8989-86418b9f77c1`) lines 531-549 [crates/gcode/src/commands/symbol_at.rs:531-549]
  - Signature: `fn containing_selection_prefers_smallest_span_then_later_start() {`
  - Purpose: Indexed function `containing_selection_prefers_smallest_span_then_later_start` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:531-549]
- `nearest_selection_prefers_previous_on_equal_line_distance` (function) component `nearest_selection_prefers_previous_on_equal_line_distance [function]` (`63a0a1b8-4aad-59d1-adc6-a16393cb0a93`) lines 552-569 [crates/gcode/src/commands/symbol_at.rs:552-569]
  - Signature: `fn nearest_selection_prefers_previous_on_equal_line_distance() {`
  - Purpose: Indexed function `nearest_selection_prefers_previous_on_equal_line_distance` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:552-569]
- `nearest_selection_uses_byte_distance_for_column_ties` (function) component `nearest_selection_uses_byte_distance_for_column_ties [function]` (`2b489723-649f-57ee-bd29-005f34a22191`) lines 572-590 [crates/gcode/src/commands/symbol_at.rs:572-590]
  - Signature: `fn nearest_selection_uses_byte_distance_for_column_ties() {`
  - Purpose: Indexed function `nearest_selection_uses_byte_distance_for_column_ties` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:572-590]
- `lookup_json_includes_source_and_metadata` (function) component `lookup_json_includes_source_and_metadata [function]` (`c75781ef-95fc-5aa2-ae9f-2f9c7a3da0cf`) lines 593-616 [crates/gcode/src/commands/symbol_at.rs:593-616]
  - Signature: `fn lookup_json_includes_source_and_metadata() {`
  - Purpose: Indexed function `lookup_json_includes_source_and_metadata` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:593-616]
- `nearest_diagnostic_is_suppressed_when_quiet_or_containing` (function) component `nearest_diagnostic_is_suppressed_when_quiet_or_containing [function]` (`e3005cae-ebe9-5794-b6c0-2bc6ef8183bd`) lines 619-640 [crates/gcode/src/commands/symbol_at.rs:619-640]
  - Signature: `fn nearest_diagnostic_is_suppressed_when_quiet_or_containing() {`
  - Purpose: Indexed function `nearest_diagnostic_is_suppressed_when_quiet_or_containing` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:619-640]

