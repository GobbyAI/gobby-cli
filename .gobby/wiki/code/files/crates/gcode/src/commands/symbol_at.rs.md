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

Resolves a requested source location to the most relevant visible symbol in a file. It parses `PATH:LINE[:COLUMN]` or separate path/line inputs into a normalized `ParsedLocation`, converts any 1-based column to a byte offset, loads visible symbols for the file, and uses `select_symbol` plus the line/byte distance helpers to choose either a containing symbol or the nearest fallback. The selected symbol is then paired with lookup metadata, source text, and an optional fallback diagnostic, and `run` emits the result in JSON or plain text while the small test helpers verify parsing, offset conversion, selection tie-breaks, and diagnostic behavior.
[crates/gcode/src/commands/symbol_at.rs:16-20]
[crates/gcode/src/commands/symbol_at.rs:23-26]
[crates/gcode/src/commands/symbol_at.rs:30-33]
[crates/gcode/src/commands/symbol_at.rs:36-47]
[crates/gcode/src/commands/symbol_at.rs:50-55]

## API Symbols

- `ParsedLocation` (class) component `ParsedLocation [class]` (`23a18fcf-f191-5f18-8f90-f96c31be5e74`) lines 16-20 [crates/gcode/src/commands/symbol_at.rs:16-20]
  - Signature: `struct ParsedLocation {`
  - Purpose: 'ParsedLocation' is a data-only struct representing a source location with a file path, a 1-based line number, and an optional 1-based column offset. [crates/gcode/src/commands/symbol_at.rs:16-20]
- `SymbolAtTarget` (class) component `SymbolAtTarget [class]` (`9ab78ade-aec5-51c5-bed0-826bc898d12a`) lines 23-26 [crates/gcode/src/commands/symbol_at.rs:23-26]
  - Signature: `struct SymbolAtTarget {`
  - Purpose: 'SymbolAtTarget' is a source-location struct that identifies a symbol by 1-based line number plus an optional byte offset within that line. [crates/gcode/src/commands/symbol_at.rs:23-26]
- `MatchKind` (type) component `MatchKind [type]` (`f1fb17f6-d9a7-5b93-acf7-25ccfaddde73`) lines 30-33 [crates/gcode/src/commands/symbol_at.rs:30-33]
  - Signature: `enum MatchKind {`
  - Purpose: Indexed type `MatchKind` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:30-33]
- `SymbolAtLookup` (class) component `SymbolAtLookup [class]` (`a281f804-6a20-5d49-9471-61b0972ea102`) lines 36-47 [crates/gcode/src/commands/symbol_at.rs:36-47]
  - Signature: `struct SymbolAtLookup {`
  - Purpose: 'SymbolAtLookup' records a symbol-location lookup request and its resolution metadata, including the requested file, line and optional column/unit, the match kind, and line/byte distance from the matched symbol. [crates/gcode/src/commands/symbol_at.rs:36-47]
- `SelectedSymbol` (class) component `SelectedSymbol [class]` (`b1661aec-3cb2-5c81-ac62-cf91adba92a9`) lines 50-55 [crates/gcode/src/commands/symbol_at.rs:50-55]
  - Signature: `struct SelectedSymbol<'a> {`
  - Purpose: 'SelectedSymbol<'a>' is a borrowed symbol selection record that pairs a 'Symbol' reference with its 'MatchKind' and proximity metrics expressed as line distance plus an optional byte distance. [crates/gcode/src/commands/symbol_at.rs:50-55]
- `requested_file_for_freshness` (function) component `requested_file_for_freshness [function]` (`16ef6bf6-1d54-57b8-b278-3596c704aad1`) lines 57-64 [crates/gcode/src/commands/symbol_at.rs:57-64]
  - Signature: `pub fn requested_file_for_freshness(`
  - Purpose: Parses the given 'location' and optional 'line' into a file reference, then returns the normalized file argument for that path via 'scope::normalize_file_arg', propagating any parsing or normalization errors. [crates/gcode/src/commands/symbol_at.rs:57-64]
- `run` (function) component `run [function]` (`ebf44413-29e7-5c34-b640-89e53e9a7be2`) lines 66-122 [crates/gcode/src/commands/symbol_at.rs:66-122]
  - Signature: `pub fn run(`
  - Purpose: Resolves a location to a visible symbol in the requested file, reads and slices its source snippet, optionally reports byte-savings and emits a fallback diagnostic, then prints the symbol as JSON or plain text depending on 'format'. [crates/gcode/src/commands/symbol_at.rs:66-122]
- `parse_location` (function) component `parse_location [function]` (`71d67d90-12e7-5f13-8802-a13b3ace34d0`) lines 124-171 [crates/gcode/src/commands/symbol_at.rs:124-171]
  - Signature: `fn parse_location(location: &str, explicit_line: Option<usize>) -> anyhow::Result<ParsedLocation> {`
  - Purpose: Parses a location string and optional explicit line into a 'ParsedLocation', validating that the path is non-empty, line numbers are positive, duplicate line specification is rejected, and supporting 'PATH:LINE', 'PATH:LINE:COLUMN', or separate 'PATH' plus 'explicit_line' formats. [crates/gcode/src/commands/symbol_at.rs:124-171]
- `has_encoded_line` (function) component `has_encoded_line [function]` (`69dec041-4f6c-5ca9-b704-1651529382ca`) lines 173-183 [crates/gcode/src/commands/symbol_at.rs:173-183]
  - Signature: `fn has_encoded_line(location: &str) -> bool {`
  - Purpose: Returns 'true' when 'location' ends with a ':number' suffix or contains a trailing ':line:column' pattern where the penultimate segment is numeric, otherwise 'false'. [crates/gcode/src/commands/symbol_at.rs:173-183]
- `parse_positive_component` (function) component `parse_positive_component [function]` (`cb59795f-fe69-59d4-9ec6-2021e45743d9`) lines 185-193 [crates/gcode/src/commands/symbol_at.rs:185-193]
  - Signature: `fn parse_positive_component(kind: &str, value: &str) -> anyhow::Result<usize> {`
  - Purpose: Parses 'value' as a 'usize' and returns it only if it is strictly greater than zero, otherwise returns an 'anyhow' error indicating the 'kind' must be a positive integer or greater than '0'. [crates/gcode/src/commands/symbol_at.rs:185-193]
- `is_numeric_text` (function) component `is_numeric_text [function]` (`b36003a1-765f-5330-80ef-049c68dfe737`) lines 195-197 [crates/gcode/src/commands/symbol_at.rs:195-197]
  - Signature: `fn is_numeric_text(value: &str) -> bool {`
  - Purpose: Returns 'true' if and only if 'value' is non-empty and every byte in it is an ASCII digit ('0'-'9'); otherwise returns 'false'. [crates/gcode/src/commands/symbol_at.rs:195-197]
- `line_column_to_byte_offset` (function) component `line_column_to_byte_offset [function]` (`2ef0e4f8-9c7e-58a6-9035-2418d830249e`) lines 202-218 [crates/gcode/src/commands/symbol_at.rs:202-218]
  - Signature: `fn line_column_to_byte_offset(source: &[u8], line: usize, column: usize) -> anyhow::Result<usize> {`
  - Purpose: Validates that 'line' and 'column' are 1-based and in range for the given byte source, then returns the zero-based byte offset of the specified position as 'start_of_line + column - 1' or an error if the line/column is invalid. [crates/gcode/src/commands/symbol_at.rs:202-218]
- `line_bounds` (function) component `line_bounds [function]` (`de1f726f-83f1-5bb4-8453-edb3c34206d4`) lines 220-233 [crates/gcode/src/commands/symbol_at.rs:220-233]
  - Signature: `fn line_bounds(source: &[u8], line: usize) -> Option<(usize, usize)> {`
  - Purpose: Returns the byte range for the requested 1-based line in a '\n'-delimited byte slice, trimming a trailing '\r' before the line break or at end-of-input, and returns 'None' if the line does not exist. [crates/gcode/src/commands/symbol_at.rs:220-233]
- `trim_cr` (function) component `trim_cr [function]` (`f3e332d2-ddd3-5df2-b0f8-bab6194a9123`) lines 235-241 [crates/gcode/src/commands/symbol_at.rs:235-241]
  - Signature: `fn trim_cr(source: &[u8], start: usize, end: usize) -> usize {`
  - Purpose: Returns 'end - 1' when the byte slice segment '[start..end)' is non-empty and its last byte is '\r', otherwise returns 'end'. [crates/gcode/src/commands/symbol_at.rs:235-241]
- `select_symbol` (function) component `select_symbol [function]` (`ddbfc0d3-511f-5a27-88e3-a161f21da5a8`) lines 243-268 [crates/gcode/src/commands/symbol_at.rs:243-268]
  - Signature: `fn select_symbol(symbols: &[Symbol], target: SymbolAtTarget) -> Option<SelectedSymbol<'_>> {`
  - Purpose: 'select_symbol' returns the best matching symbol for a target by first choosing the smallest symbol that contains the target and, if none do, falling back to the nearest symbol by line/byte distance while annotating the result with the corresponding 'MatchKind' and computed distances. [crates/gcode/src/commands/symbol_at.rs:243-268]
- `contains_target` (function) component `contains_target [function]` (`01602b75-b275-5c90-9ee9-f4284326e428`) lines 270-275 [crates/gcode/src/commands/symbol_at.rs:270-275]
  - Signature: `fn contains_target(symbol: &Symbol, target: SymbolAtTarget) -> bool {`
  - Purpose: Returns 'true' when the target’s byte offset, if present, lies within the symbol’s half-open byte range '[byte_start, byte_end)', otherwise when the target line falls within the symbol’s inclusive line range '[line_start, line_end]'. [crates/gcode/src/commands/symbol_at.rs:270-275]
- `compare_containing` (function) component `compare_containing [function]` (`83181fd3-18a9-5f79-b67e-583758271ce6`) lines 277-282 [crates/gcode/src/commands/symbol_at.rs:277-282]
  - Signature: `fn compare_containing(left: &Symbol, right: &Symbol) -> Ordering {`
  - Purpose: Returns an 'Ordering' that sorts symbols by their 'line_span', then by 'byte_span', and finally by descending 'byte_start' to break ties. [crates/gcode/src/commands/symbol_at.rs:277-282]
- `compare_nearest` (function) component `compare_nearest [function]` (`d1ea1907-4191-55a5-90b3-582609b9b9a2`) lines 284-292 [crates/gcode/src/commands/symbol_at.rs:284-292]
  - Signature: `fn compare_nearest(left: &Symbol, right: &Symbol, target: SymbolAtTarget) -> Ordering {`
  - Purpose: Returns an 'Ordering' that ranks two symbols by increasing distance from the target line, then by byte-offset distance when available, and finally by a previous-preference tie-breaker. [crates/gcode/src/commands/symbol_at.rs:284-292]
- `compare_previous_preference` (function) component `compare_previous_preference [function]` (`72955b3a-4c61-57ca-bd2b-0c584060951e`) lines 294-311 [crates/gcode/src/commands/symbol_at.rs:294-311]
  - Signature: `fn compare_previous_preference(left: &Symbol, right: &Symbol, target: SymbolAtTarget) -> Ordering {`
  - Purpose: Returns an 'Ordering' that prioritizes symbols identified as the previous symbol relative to 'target', placing a previous 'left' before a non-previous 'right', a non-previous 'left' after a previous 'right', and otherwise breaking ties by descending end position for two previous symbols or ascending start position for two non-previous symbols. [crates/gcode/src/commands/symbol_at.rs:294-311]
- `is_previous_symbol` (function) component `is_previous_symbol [function]` (`1f6c60b2-a56c-5c2f-9434-c831a04eb76b`) lines 313-323 [crates/gcode/src/commands/symbol_at.rs:313-323]
  - Signature: `fn is_previous_symbol(symbol: &Symbol, target: SymbolAtTarget) -> bool {`
  - Purpose: Returns 'true' when the symbol is entirely before the target position by byte offset if available ('byte_end <= offset', or if the symbol starts after the offset then 'false'), otherwise by line order ('symbol.line_end < target.line'). [crates/gcode/src/commands/symbol_at.rs:313-323]
- `line_span` (function) component `line_span [function]` (`46d9e4b6-f3f9-548f-8677-243aa0cba19f`) lines 325-327 [crates/gcode/src/commands/symbol_at.rs:325-327]
  - Signature: `fn line_span(symbol: &Symbol) -> usize {`
  - Purpose: Returns the non-negative difference between 'symbol.line_end' and 'symbol.line_start' using saturating subtraction, yielding the symbol’s line span in lines as a 'usize'. [crates/gcode/src/commands/symbol_at.rs:325-327]
- `byte_span` (function) component `byte_span [function]` (`88360e0e-6793-5775-ac15-040e8863dabf`) lines 329-331 [crates/gcode/src/commands/symbol_at.rs:329-331]
  - Signature: `fn byte_span(symbol: &Symbol) -> usize {`
  - Purpose: Returns the symbol’s byte-length as 'byte_end - byte_start', using saturating subtraction to avoid underflow. [crates/gcode/src/commands/symbol_at.rs:329-331]
- `line_distance` (function) component `line_distance [function]` (`725c0860-177d-54b8-9461-8e21407b1aad`) lines 333-339 [crates/gcode/src/commands/symbol_at.rs:333-339]
  - Signature: `fn line_distance(symbol: &Symbol, line: usize) -> usize {`
  - Purpose: 'line_distance' returns the nonnegative distance from a given line number to a symbol’s line span, yielding 'symbol.line_start - line' when the line is above the symbol, 'line - symbol.line_end' when it is below, and '0' when it falls within the symbol’s range. [crates/gcode/src/commands/symbol_at.rs:333-339]
- `byte_distance` (function) component `byte_distance [function]` (`805f80ac-a6a8-5708-a6e9-2c52f96d342d`) lines 341-349 [crates/gcode/src/commands/symbol_at.rs:341-349]
  - Signature: `fn byte_distance(symbol: &Symbol, offset: usize) -> usize {`
  - Purpose: Returns the unsigned byte gap between 'offset' and 'symbol'’s byte range, yielding 'symbol.byte_start - offset' when before the range, 'offset - symbol.byte_end' with saturation when after it, and '0' when 'offset' lies within '[byte_start, byte_end)'. [crates/gcode/src/commands/symbol_at.rs:341-349]
- `lookup_for_selection` (function) component `lookup_for_selection [function]` (`b135c06c-67c6-5ab8-b0fb-3ef517e4544e`) lines 351-365 [crates/gcode/src/commands/symbol_at.rs:351-365]
  - Signature: `fn lookup_for_selection(`
  - Purpose: 'lookup_for_selection' constructs and returns a 'SymbolAtLookup' by copying the requested file path, the parsed location’s line and column, setting 'column_unit' to '"byte"' when a column is present, and propagating the selected symbol’s match kind and distance metrics. [crates/gcode/src/commands/symbol_at.rs:351-365]
- `symbol_source` (function) component `symbol_source [function]` (`b8d73228-d8e6-501c-ae29-87edbf4f6e0c`) lines 367-372 [crates/gcode/src/commands/symbol_at.rs:367-372]
  - Signature: `fn symbol_source(source: &[u8], symbol: &Symbol) -> (String, usize) {`
  - Purpose: Returns the UTF-8 lossy string slice for the byte range covered by 'symbol', clamped to 'source' bounds, along with the number of bytes actually extracted. [crates/gcode/src/commands/symbol_at.rs:367-372]
- `symbol_at_json_value` (function) component `symbol_at_json_value [function]` (`e22dde31-2a1c-594d-b067-bc21209e9961`) lines 374-383 [crates/gcode/src/commands/symbol_at.rs:374-383]
  - Signature: `fn symbol_at_json_value(`
  - Purpose: Serializes a 'Symbol' and its associated 'SymbolAtLookup' into a 'serde_json::Value', then injects the provided 'source' string and returns the augmented JSON object. [crates/gcode/src/commands/symbol_at.rs:374-383]
- `fallback_diagnostic` (function) component `fallback_diagnostic [function]` (`bc63b2c2-a007-5b5d-b4d4-d9c59f3a435f`) lines 385-410 [crates/gcode/src/commands/symbol_at.rs:385-410]
  - Signature: `fn fallback_diagnostic(symbol: &Symbol, lookup: &SymbolAtLookup, quiet: bool) -> Option<String> {`
  - Purpose: Returns 'None' unless 'quiet' is false and 'lookup.match_kind' is 'MatchKind::Nearest'; otherwise it formats and returns a fallback diagnostic string explaining that no symbol contains the requested file/line[/column], so the nearest visible symbol was used, including the symbol’s location, kind, qualified name, and line/byte distance. [crates/gcode/src/commands/symbol_at.rs:385-410]
- `plural` (function) component `plural [function]` (`cdbc3afb-939b-582f-a532-dbc689e26d88`) lines 412-422 [crates/gcode/src/commands/symbol_at.rs:412-422]
  - Signature: `fn plural(unit: &'static str, value: usize) -> &'static str {`
  - Purpose: Returns 'unit' unchanged when 'value == 1', otherwise maps '"line"' to '"lines"' and '"byte"' to '"bytes"', falling back to the original 'unit' for all other strings. [crates/gcode/src/commands/symbol_at.rs:412-422]
- `symbol` (function) component `symbol [function]` (`46d192ab-301d-5dc0-bdc7-2a183442a67b`) lines 429-456 [crates/gcode/src/commands/symbol_at.rs:429-456]
  - Signature: `fn symbol(`
  - Purpose: Constructs and returns a 'Symbol' for a TypeScript function using the provided name and source-range bounds, populating fixed metadata fields and a generated 'function {name}()' signature. [crates/gcode/src/commands/symbol_at.rs:429-456]
- `error_text` (function) component `error_text [function]` (`9cd2d7c4-e33a-51f5-9a82-9bc1260d123e`) lines 458-463 [crates/gcode/src/commands/symbol_at.rs:458-463]
  - Signature: `fn error_text<T>(result: anyhow::Result<T>) -> String {`
  - Purpose: Returns the error message string from an 'anyhow::Result<T>', and panics with '"expected error"' if the result is 'Ok(_)'. [crates/gcode/src/commands/symbol_at.rs:458-463]
- `parses_path_line_and_column_from_the_right` (function) component `parses_path_line_and_column_from_the_right [function]` (`94cbf927-c0b3-517a-957e-864cdd08d096`) lines 466-476 [crates/gcode/src/commands/symbol_at.rs:466-476]
  - Signature: `fn parses_path_line_and_column_from_the_right() {`
  - Purpose: Verifies that 'parse_location' splits 'PATH:LINE' and 'PATH:LINE:COLUMN' from the right so colons in the file path are preserved, yielding the correct 'file', 'line', and optional 'column' values. [crates/gcode/src/commands/symbol_at.rs:466-476]
- `parses_path_with_separate_line` (function) component `parses_path_with_separate_line [function]` (`1b4a8d5a-4007-58c5-a62b-98c4d6dbc895`) lines 479-485 [crates/gcode/src/commands/symbol_at.rs:479-485]
  - Signature: `fn parses_path_with_separate_line() {`
  - Purpose: Verifies that 'parse_location' treats 'src:auth.ts' as the file path when the line number is supplied separately, producing a parsed location with file 'src:auth.ts', line '42', and no column. [crates/gcode/src/commands/symbol_at.rs:479-485]
- `rejects_invalid_location_forms` (function) component `rejects_invalid_location_forms [function]` (`95673617-cb70-5189-ab43-969497a27780`) lines 488-509 [crates/gcode/src/commands/symbol_at.rs:488-509]
  - Signature: `fn rejects_invalid_location_forms() {`
  - Purpose: Verifies that 'parse_location' rejects malformed location strings and duplicate line inputs by producing the expected validation errors for missing line, repeated line, nonpositive line/column values, and non-integer line/column fields. [crates/gcode/src/commands/symbol_at.rs:488-509]
- `converts_one_based_byte_columns_to_offsets` (function) component `converts_one_based_byte_columns_to_offsets [function]` (`4916be6e-bffb-5339-a423-ff5691947193`) lines 512-520 [crates/gcode/src/commands/symbol_at.rs:512-520]
  - Signature: `fn converts_one_based_byte_columns_to_offsets() {`
  - Purpose: Verifies that 'line_column_to_byte_offset' converts 1-based line/byte-column pairs into correct zero-based byte offsets across ASCII and multibyte UTF-8 text. [crates/gcode/src/commands/symbol_at.rs:512-520]
- `rejects_out_of_range_columns` (function) component `rejects_out_of_range_columns [function]` (`2b10c626-8177-5b38-bff2-b4e51ceea8ea`) lines 523-528 [crates/gcode/src/commands/symbol_at.rs:523-528]
  - Signature: `fn rejects_out_of_range_columns() {`
  - Purpose: Verifies that 'line_column_to_byte_offset' returns an error for a column index beyond the end of the line, and that the error text contains 'column 4 is out of range'. [crates/gcode/src/commands/symbol_at.rs:523-528]
- `containing_selection_prefers_smallest_span_then_later_start` (function) component `containing_selection_prefers_smallest_span_then_later_start [function]` (`f2ffa2e8-24cf-5b06-8989-86418b9f77c1`) lines 531-549 [crates/gcode/src/commands/symbol_at.rs:531-549]
  - Signature: `fn containing_selection_prefers_smallest_span_then_later_start() {`
  - Purpose: Verifies that 'select_symbol' chooses, among containing symbols on the target line, the one with the smallest span and breaks ties by preferring the later start, yielding 'later' as a 'MatchKind::Containing' match with 'distance_lines == 0'. [crates/gcode/src/commands/symbol_at.rs:531-549]
- `nearest_selection_prefers_previous_on_equal_line_distance` (function) component `nearest_selection_prefers_previous_on_equal_line_distance [function]` (`63a0a1b8-4aad-59d1-adc6-a16393cb0a93`) lines 552-569 [crates/gcode/src/commands/symbol_at.rs:552-569]
  - Signature: `fn nearest_selection_prefers_previous_on_equal_line_distance() {`
  - Purpose: Verifies that 'select_symbol' breaks a tie in line-distance proximity by choosing the previous symbol and reports a 'Nearest' match with a 2-line distance. [crates/gcode/src/commands/symbol_at.rs:552-569]
- `nearest_selection_uses_byte_distance_for_column_ties` (function) component `nearest_selection_uses_byte_distance_for_column_ties [function]` (`2b489723-649f-57ee-bd29-005f34a22191`) lines 572-590 [crates/gcode/src/commands/symbol_at.rs:572-590]
  - Signature: `fn nearest_selection_uses_byte_distance_for_column_ties() {`
  - Purpose: Verifies that 'select_symbol' breaks ties on the same line by choosing the symbol with the smallest byte-distance to the target offset, returning the right symbol as a 'Nearest' match with 'distance_lines == 0' and 'distance_bytes == Some(1)'. [crates/gcode/src/commands/symbol_at.rs:572-590]
- `lookup_json_includes_source_and_metadata` (function) component `lookup_json_includes_source_and_metadata [function]` (`c75781ef-95fc-5aa2-ae9f-2f9c7a3da0cf`) lines 593-616 [crates/gcode/src/commands/symbol_at.rs:593-616]
  - Signature: `fn lookup_json_includes_source_and_metadata() {`
  - Purpose: Verifies that 'symbol_at_json_value' serializes a symbol lookup into JSON containing the symbol name, the provided source text, and all requested lookup metadata fields with the expected values. [crates/gcode/src/commands/symbol_at.rs:593-616]
- `nearest_diagnostic_is_suppressed_when_quiet_or_containing` (function) component `nearest_diagnostic_is_suppressed_when_quiet_or_containing [function]` (`e3005cae-ebe9-5794-b6c0-2bc6ef8183bd`) lines 619-640 [crates/gcode/src/commands/symbol_at.rs:619-640]
  - Signature: `fn nearest_diagnostic_is_suppressed_when_quiet_or_containing() {`
  - Purpose: Verifies that 'fallback_diagnostic' emits a nearest-symbol diagnostic only when 'MatchKind::Nearest' is used with 'quiet' false, and suppresses diagnostics when 'quiet' is true or when the lookup uses 'MatchKind::Containing'. [crates/gcode/src/commands/symbol_at.rs:619-640]

