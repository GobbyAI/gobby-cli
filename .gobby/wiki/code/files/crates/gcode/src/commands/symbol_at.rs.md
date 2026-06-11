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
  - 66-124
  - 126-173
  - 175-185
  - 187-195
  - 197-199
  - 204-220
  - 222-235
  - 237-243
  - 245-270
  - 272-277
  - 279-284
  - 286-294
  - 296-313
  - 315-325
  - 327-329
  - 331-333
  - 335-341
  - 343-351
  - 353-367
  - 369-374
  - 376-385
  - 387-412
  - 414-424
  - 431-458
  - 460-465
  - 468-478
  - 481-487
  - 490-511
  - 514-522
  - 525-530
  - 533-551
  - 554-571
  - 574-592
  - 595-618
  - 621-642
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/symbol_at.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/symbol_at.rs` exposes 41 indexed API symbols.
[crates/gcode/src/commands/symbol_at.rs:16-20]
[crates/gcode/src/commands/symbol_at.rs:23-26]
[crates/gcode/src/commands/symbol_at.rs:30-33]
[crates/gcode/src/commands/symbol_at.rs:36-47]
[crates/gcode/src/commands/symbol_at.rs:50-55]

## API Symbols

- `ParsedLocation` (class) component `ParsedLocation [class]` (`23a18fcf-f191-5f18-8f90-f96c31be5e74`) lines 16-20 [crates/gcode/src/commands/symbol_at.rs:16-20]
  - Signature: `struct ParsedLocation {`
  - Purpose: ParsedLocation is a struct that represents a source code location with a required file path and line number, and an optional column offset. [crates/gcode/src/commands/symbol_at.rs:16-20]
- `SymbolAtTarget` (class) component `SymbolAtTarget [class]` (`9ab78ade-aec5-51c5-bed0-826bc898d12a`) lines 23-26 [crates/gcode/src/commands/symbol_at.rs:23-26]
  - Signature: `struct SymbolAtTarget {`
  - Purpose: SymbolAtTarget is a struct that represents a symbol's location in source code using a required line number and an optional byte offset. [crates/gcode/src/commands/symbol_at.rs:23-26]
- `MatchKind` (type) component `MatchKind [type]` (`f1fb17f6-d9a7-5b93-acf7-25ccfaddde73`) lines 30-33 [crates/gcode/src/commands/symbol_at.rs:30-33]
  - Signature: `enum MatchKind {`
  - Purpose: Indexed type `MatchKind` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:30-33]
- `SymbolAtLookup` (class) component `SymbolAtLookup [class]` (`a281f804-6a20-5d49-9471-61b0972ea102`) lines 36-47 [crates/gcode/src/commands/symbol_at.rs:36-47]
  - Signature: `struct SymbolAtLookup {`
  - Purpose: `SymbolAtLookup` is a struct that encapsulates a symbol lookup query containing target file coordinates (with optional column specificity), match classification, and distance-to-match metrics in both lines and bytes. [crates/gcode/src/commands/symbol_at.rs:36-47]
- `SelectedSymbol` (class) component `SelectedSymbol [class]` (`b1661aec-3cb2-5c81-ac62-cf91adba92a9`) lines 50-55 [crates/gcode/src/commands/symbol_at.rs:50-55]
  - Signature: `struct SelectedSymbol<'a> {`
  - Purpose: `SelectedSymbol<'a>` is a generic struct that encapsulates a borrowed `Symbol` reference along with its match classification (`MatchKind`) and positional distance metrics measured in lines and optional bytes. [crates/gcode/src/commands/symbol_at.rs:50-55]
- `requested_file_for_freshness` (function) component `requested_file_for_freshness [function]` (`16ef6bf6-1d54-57b8-b278-3596c704aad1`) lines 57-64 [crates/gcode/src/commands/symbol_at.rs:57-64]
  - Signature: `pub fn requested_file_for_freshness(`
  - Purpose: Parses a location specification with an optional line number and returns the context-normalized file path. [crates/gcode/src/commands/symbol_at.rs:57-64]
- `run` (function) component `run [function]` (`ebf44413-29e7-5c34-b640-89e53e9a7be2`) lines 66-124 [crates/gcode/src/commands/symbol_at.rs:66-124]
  - Signature: `pub fn run(`
  - Purpose: Parses a source location, retrieves the corresponding symbol from a visibility-filtered database, and outputs its source code in JSON or text format with optional diagnostics. [crates/gcode/src/commands/symbol_at.rs:66-124]
- `parse_location` (function) component `parse_location [function]` (`b87b66d9-f346-5aa0-bb4b-25321813cddd`) lines 126-173 [crates/gcode/src/commands/symbol_at.rs:126-173]
  - Signature: `fn parse_location(location: &str, explicit_line: Option<usize>) -> anyhow::Result<ParsedLocation> {`
  - Purpose: Parses a file location string into file path, line number, and optional column components, supporting PATH:LINE and PATH:LINE:COLUMN formats or an explicit line parameter, with validation of required fields and numeric constraints. [crates/gcode/src/commands/symbol_at.rs:126-173]
- `has_encoded_line` (function) component `has_encoded_line [function]` (`6f18ef83-0017-5241-9d3c-ccb6ea736eb9`) lines 175-185 [crates/gcode/src/commands/symbol_at.rs:175-185]
  - Signature: `fn has_encoded_line(location: &str) -> bool {`
  - Purpose: Returns true if the location string contains numeric text in either the final or penultimate colon-delimited segment. [crates/gcode/src/commands/symbol_at.rs:175-185]
- `parse_positive_component` (function) component `parse_positive_component [function]` (`aaf8ed9b-33e1-5d5b-8578-e380989e03b8`) lines 187-195 [crates/gcode/src/commands/symbol_at.rs:187-195]
  - Signature: `fn parse_positive_component(kind: &str, value: &str) -> anyhow::Result<usize> {`
  - Purpose: Parses a string into a non-zero `usize`, returning a context-specific error message if the value is invalid or not strictly positive. [crates/gcode/src/commands/symbol_at.rs:187-195]
- `is_numeric_text` (function) component `is_numeric_text [function]` (`65fe92ff-06d3-5eef-839f-e8024738b66e`) lines 197-199 [crates/gcode/src/commands/symbol_at.rs:197-199]
  - Signature: `fn is_numeric_text(value: &str) -> bool {`
  - Purpose: Returns `true` if the string is non-empty and contains exclusively ASCII digit characters (0-9). [crates/gcode/src/commands/symbol_at.rs:197-199]
- `line_column_to_byte_offset` (function) component `line_column_to_byte_offset [function]` (`9436bfed-4f32-5c30-b763-32d42adabf92`) lines 204-220 [crates/gcode/src/commands/symbol_at.rs:204-220]
  - Signature: `fn line_column_to_byte_offset(source: &[u8], line: usize, column: usize) -> anyhow::Result<usize> {`
  - Purpose: Converts a 1-indexed (line, column) coordinate to its corresponding byte offset in a source, validating that both coordinates are in bounds. [crates/gcode/src/commands/symbol_at.rs:204-220]
- `line_bounds` (function) component `line_bounds [function]` (`f6061a37-7259-545d-9d02-423363dfb01a`) lines 222-235 [crates/gcode/src/commands/symbol_at.rs:222-235]
  - Signature: `fn line_bounds(source: &[u8], line: usize) -> Option<(usize, usize)> {`
  - Purpose: Returns the byte offset bounds of a specified line number in a byte buffer, scanning for newline delimiters and trimming carriage returns from line endings. [crates/gcode/src/commands/symbol_at.rs:222-235]
- `trim_cr` (function) component `trim_cr [function]` (`559f19c0-2dac-5638-82d3-0c07edb2e376`) lines 237-243 [crates/gcode/src/commands/symbol_at.rs:237-243]
  - Signature: `fn trim_cr(source: &[u8], start: usize, end: usize) -> usize {`
  - Purpose: Returns the adjusted end index of the byte range, decremented by one if the byte at position `end - 1` is a carriage return (`\r`), otherwise unchanged. [crates/gcode/src/commands/symbol_at.rs:237-243]
- `select_symbol` (function) component `select_symbol [function]` (`2a456788-4130-5809-bc1c-873659422345`) lines 245-270 [crates/gcode/src/commands/symbol_at.rs:245-270]
  - Signature: `fn select_symbol(symbols: &[Symbol], target: SymbolAtTarget) -> Option<SelectedSymbol<'_>> {`
  - Purpose: Selects the smallest symbol containing a target position, or if none exists, the nearest symbol, returning the selection with match kind and distance metrics. [crates/gcode/src/commands/symbol_at.rs:245-270]
- `contains_target` (function) component `contains_target [function]` (`2e347167-7918-5063-996e-0c3df126e3c4`) lines 272-277 [crates/gcode/src/commands/symbol_at.rs:272-277]
  - Signature: `fn contains_target(symbol: &Symbol, target: SymbolAtTarget) -> bool {`
  - Purpose: Checks whether a target position falls within a symbol's byte range (if byte offset is specified) or line range (otherwise). [crates/gcode/src/commands/symbol_at.rs:272-277]
- `compare_containing` (function) component `compare_containing [function]` (`501c0820-4ab5-5055-963f-5b29880830cb`) lines 279-284 [crates/gcode/src/commands/symbol_at.rs:279-284]
  - Signature: `fn compare_containing(left: &Symbol, right: &Symbol) -> Ordering {`
  - Purpose: # Summary

`compare_containing` establishes a total ordering of symbols by comparing their line spans, then byte spans, and finally by reverse byte start position to determine containment relationships. [crates/gcode/src/commands/symbol_at.rs:279-284]
- `compare_nearest` (function) component `compare_nearest [function]` (`c21c34bd-6813-5ac7-b599-73cef8b4cb08`) lines 286-294 [crates/gcode/src/commands/symbol_at.rs:286-294]
  - Signature: `fn compare_nearest(left: &Symbol, right: &Symbol, target: SymbolAtTarget) -> Ordering {`
  - Purpose: Compares two symbols by their proximity to a target location, using line distance as the primary ordering criterion, byte offset distance as a secondary tiebreaker when present, and previous preference as a final fallback. [crates/gcode/src/commands/symbol_at.rs:286-294]
- `compare_previous_preference` (function) component `compare_previous_preference [function]` (`01e1138b-b604-590d-9c47-a37e90a70ca3`) lines 296-313 [crates/gcode/src/commands/symbol_at.rs:296-313]
  - Signature: `fn compare_previous_preference(left: &Symbol, right: &Symbol, target: SymbolAtTarget) -> Ordering {`
  - Purpose: Comparatively orders two symbols by prioritizing those matching the target's previous-symbol condition, using reversed positional comparison for previous symbols and forward positional comparison for non-previous symbols. [crates/gcode/src/commands/symbol_at.rs:296-313]
- `is_previous_symbol` (function) component `is_previous_symbol [function]` (`d76deb34-b57d-5ee3-9081-b6f71b239c64`) lines 315-325 [crates/gcode/src/commands/symbol_at.rs:315-325]
  - Signature: `fn is_previous_symbol(symbol: &Symbol, target: SymbolAtTarget) -> bool {`
  - Purpose: Determines whether a symbol precedes a target location by prioritizing byte offset comparison when available, otherwise falling back to end-line comparison. [crates/gcode/src/commands/symbol_at.rs:315-325]
- `line_span` (function) component `line_span [function]` (`d73aaa27-f7e1-5dce-8b18-31db9593f048`) lines 327-329 [crates/gcode/src/commands/symbol_at.rs:327-329]
  - Signature: `fn line_span(symbol: &Symbol) -> usize {`
  - Purpose: Calculates the number of lines spanned by a symbol as the saturating difference between its end and start line numbers. [crates/gcode/src/commands/symbol_at.rs:327-329]
- `byte_span` (function) component `byte_span [function]` (`9a142e77-333b-5643-a9ae-399f3dacd0b6`) lines 331-333 [crates/gcode/src/commands/symbol_at.rs:331-333]
  - Signature: `fn byte_span(symbol: &Symbol) -> usize {`
  - Purpose: Indexed function `byte_span` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:331-333]
- `line_distance` (function) component `line_distance [function]` (`de9fe7a5-c293-5819-bff4-a71384836047`) lines 335-341 [crates/gcode/src/commands/symbol_at.rs:335-341]
  - Signature: `fn line_distance(symbol: &Symbol, line: usize) -> usize {`
  - Purpose: Indexed function `line_distance` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:335-341]
- `byte_distance` (function) component `byte_distance [function]` (`5c422dca-29b9-5d43-9be3-ee3ff17cb7b0`) lines 343-351 [crates/gcode/src/commands/symbol_at.rs:343-351]
  - Signature: `fn byte_distance(symbol: &Symbol, offset: usize) -> usize {`
  - Purpose: Indexed function `byte_distance` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:343-351]
- `lookup_for_selection` (function) component `lookup_for_selection [function]` (`bab6d1ae-4f2c-51ec-a09d-6275d2b73e0a`) lines 353-367 [crates/gcode/src/commands/symbol_at.rs:353-367]
  - Signature: `fn lookup_for_selection(`
  - Purpose: Indexed function `lookup_for_selection` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:353-367]
- `symbol_source` (function) component `symbol_source [function]` (`b17f356e-ce79-52b3-9ec4-7fac59ef1189`) lines 369-374 [crates/gcode/src/commands/symbol_at.rs:369-374]
  - Signature: `fn symbol_source(source: &[u8], symbol: &Symbol) -> (String, usize) {`
  - Purpose: Indexed function `symbol_source` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:369-374]
- `symbol_at_json_value` (function) component `symbol_at_json_value [function]` (`7f5ab302-7052-535a-a6c7-fb81f026c6d6`) lines 376-385 [crates/gcode/src/commands/symbol_at.rs:376-385]
  - Signature: `fn symbol_at_json_value(`
  - Purpose: Indexed function `symbol_at_json_value` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:376-385]
- `fallback_diagnostic` (function) component `fallback_diagnostic [function]` (`b6aec16a-acee-5796-9dee-a27daba25f41`) lines 387-412 [crates/gcode/src/commands/symbol_at.rs:387-412]
  - Signature: `fn fallback_diagnostic(symbol: &Symbol, lookup: &SymbolAtLookup, quiet: bool) -> Option<String> {`
  - Purpose: Indexed function `fallback_diagnostic` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:387-412]
- `plural` (function) component `plural [function]` (`8380ffc1-58af-5ba3-b1e3-9aafea6d5b34`) lines 414-424 [crates/gcode/src/commands/symbol_at.rs:414-424]
  - Signature: `fn plural(unit: &'static str, value: usize) -> &'static str {`
  - Purpose: Indexed function `plural` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:414-424]
- `symbol` (function) component `symbol [function]` (`6c23ec01-90d0-5284-80ed-9baebfe4b2b2`) lines 431-458 [crates/gcode/src/commands/symbol_at.rs:431-458]
  - Signature: `fn symbol(`
  - Purpose: Indexed function `symbol` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:431-458]
- `error_text` (function) component `error_text [function]` (`18d84262-71d9-5603-b1e5-cfb2831480c2`) lines 460-465 [crates/gcode/src/commands/symbol_at.rs:460-465]
  - Signature: `fn error_text<T>(result: anyhow::Result<T>) -> String {`
  - Purpose: Indexed function `error_text` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:460-465]
- `parses_path_line_and_column_from_the_right` (function) component `parses_path_line_and_column_from_the_right [function]` (`82e79384-db9e-59cd-9817-0f5fc76bdfc7`) lines 468-478 [crates/gcode/src/commands/symbol_at.rs:468-478]
  - Signature: `fn parses_path_line_and_column_from_the_right() {`
  - Purpose: Indexed function `parses_path_line_and_column_from_the_right` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:468-478]
- `parses_path_with_separate_line` (function) component `parses_path_with_separate_line [function]` (`7b4bca8a-3d15-5382-8b25-37ea440de766`) lines 481-487 [crates/gcode/src/commands/symbol_at.rs:481-487]
  - Signature: `fn parses_path_with_separate_line() {`
  - Purpose: Indexed function `parses_path_with_separate_line` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:481-487]
- `rejects_invalid_location_forms` (function) component `rejects_invalid_location_forms [function]` (`a9c17528-2482-5a2b-977e-6bf788beac2c`) lines 490-511 [crates/gcode/src/commands/symbol_at.rs:490-511]
  - Signature: `fn rejects_invalid_location_forms() {`
  - Purpose: Indexed function `rejects_invalid_location_forms` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:490-511]
- `converts_one_based_byte_columns_to_offsets` (function) component `converts_one_based_byte_columns_to_offsets [function]` (`8b3b1663-7f95-5640-addd-e6b11ee4c6c5`) lines 514-522 [crates/gcode/src/commands/symbol_at.rs:514-522]
  - Signature: `fn converts_one_based_byte_columns_to_offsets() {`
  - Purpose: Indexed function `converts_one_based_byte_columns_to_offsets` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:514-522]
- `rejects_out_of_range_columns` (function) component `rejects_out_of_range_columns [function]` (`c9e305c0-1025-5722-aaf2-cd2e3b16d725`) lines 525-530 [crates/gcode/src/commands/symbol_at.rs:525-530]
  - Signature: `fn rejects_out_of_range_columns() {`
  - Purpose: Indexed function `rejects_out_of_range_columns` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:525-530]
- `containing_selection_prefers_smallest_span_then_later_start` (function) component `containing_selection_prefers_smallest_span_then_later_start [function]` (`b96893c0-f575-5296-8abc-1ac1d83ddec0`) lines 533-551 [crates/gcode/src/commands/symbol_at.rs:533-551]
  - Signature: `fn containing_selection_prefers_smallest_span_then_later_start() {`
  - Purpose: Indexed function `containing_selection_prefers_smallest_span_then_later_start` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:533-551]
- `nearest_selection_prefers_previous_on_equal_line_distance` (function) component `nearest_selection_prefers_previous_on_equal_line_distance [function]` (`c807afb7-6a47-5965-8ea8-a7ce28f42179`) lines 554-571 [crates/gcode/src/commands/symbol_at.rs:554-571]
  - Signature: `fn nearest_selection_prefers_previous_on_equal_line_distance() {`
  - Purpose: Indexed function `nearest_selection_prefers_previous_on_equal_line_distance` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:554-571]
- `nearest_selection_uses_byte_distance_for_column_ties` (function) component `nearest_selection_uses_byte_distance_for_column_ties [function]` (`dfe72ec9-d211-5eb2-bfeb-8f646308dcdf`) lines 574-592 [crates/gcode/src/commands/symbol_at.rs:574-592]
  - Signature: `fn nearest_selection_uses_byte_distance_for_column_ties() {`
  - Purpose: Indexed function `nearest_selection_uses_byte_distance_for_column_ties` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:574-592]
- `lookup_json_includes_source_and_metadata` (function) component `lookup_json_includes_source_and_metadata [function]` (`cc535d2f-dd22-5fdf-9efa-05c5b0d82670`) lines 595-618 [crates/gcode/src/commands/symbol_at.rs:595-618]
  - Signature: `fn lookup_json_includes_source_and_metadata() {`
  - Purpose: Indexed function `lookup_json_includes_source_and_metadata` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:595-618]
- `nearest_diagnostic_is_suppressed_when_quiet_or_containing` (function) component `nearest_diagnostic_is_suppressed_when_quiet_or_containing [function]` (`5a34ebb8-4ae3-54a8-87ed-cc4946a4cc5f`) lines 621-642 [crates/gcode/src/commands/symbol_at.rs:621-642]
  - Signature: `fn nearest_diagnostic_is_suppressed_when_quiet_or_containing() {`
  - Purpose: Indexed function `nearest_diagnostic_is_suppressed_when_quiet_or_containing` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:621-642]

