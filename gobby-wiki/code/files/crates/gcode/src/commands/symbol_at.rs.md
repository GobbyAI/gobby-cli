---
title: crates/gcode/src/commands/symbol_at.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/symbol_at.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/symbol_at.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

## How it fits
[crates/gcode/src/commands/symbol_at.rs:16-20]
[crates/gcode/src/commands/symbol_at.rs:23-26]
[crates/gcode/src/commands/symbol_at.rs:30-33]
[crates/gcode/src/commands/symbol_at.rs:36-47]
[crates/gcode/src/commands/symbol_at.rs:50-55]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ParsedLocation` | class | 'ParsedLocation' is a struct representing a source code position with a required 'file' path, a 1-based 'line' number, and an optional 'column' offset. [crates/gcode/src/commands/symbol_at.rs:16-20] |
| `SymbolAtTarget` | class | 'SymbolAtTarget' is a struct that records a target position using a zero-based 'line' index and an optional 'byte_offset' within that line. [crates/gcode/src/commands/symbol_at.rs:23-26] |
| `MatchKind` | type | Indexed type `MatchKind` in `crates/gcode/src/commands/symbol_at.rs`. [crates/gcode/src/commands/symbol_at.rs:30-33] |
| `SymbolAtLookup` | class | 'SymbolAtLookup' records a source-location lookup request and its resolution metadata, including the requested file, line, optional column and column unit, match kind, and line/byte distance to the matched symbol. [crates/gcode/src/commands/symbol_at.rs:36-47] |
| `SelectedSymbol` | class | 'SelectedSymbol<'a>' is a borrowed record that pairs a 'Symbol' reference with its 'MatchKind' and line/byte proximity metrics ('distance_lines' and optional 'distance_bytes') used to describe a selected match. [crates/gcode/src/commands/symbol_at.rs:50-55] |
| `requested_file_for_freshness` | function | Parses a file location with an optional line number and returns the normalized file path for freshness checking using 'scope::normalize_file_arg', propagating any parsing or normalization errors. [crates/gcode/src/commands/symbol_at.rs:57-64] |
| `run` | function | Resolves a requested file location to the visible symbol covering it, reads the source to extract that symbol’s snippet, optionally reports byte-savings and emits a fallback diagnostic, then prints the snippet as JSON or plain text. [crates/gcode/src/commands/symbol_at.rs:66-122] |
| `parse_location` | function | 'parse_location' validates a location string and optional explicit line number, then parses it into a 'ParsedLocation' with 'file', required positive 'line', and optional positive 'column', rejecting empty paths, zero lines, duplicate line specification, and malformed 'PATH:LINE' or 'PATH:LINE:COLUMN' forms. [crates/gcode/src/commands/symbol_at.rs:124-171] |
| `has_encoded_line` | function | Returns 'true' if 'location' ends with a numeric ':line' segment, either as the final colon-delimited component or as the component before a trailing non-numeric suffix, and 'false' otherwise. [crates/gcode/src/commands/symbol_at.rs:173-183] |
| `parse_positive_component` | function | Parses 'value' as a 'usize' and returns it if it is strictly greater than zero, otherwise it returns an 'anyhow' error indicating that 'kind' must be a positive integer or greater than 0. [crates/gcode/src/commands/symbol_at.rs:185-193] |
| `is_numeric_text` | function | Returns 'true' only when 'value' is non-empty and every byte in it is an ASCII digit ('0'-'9'), otherwise 'false'. [crates/gcode/src/commands/symbol_at.rs:195-197] |
| `line_column_to_byte_offset` | function | Converts a 1-based '(line, column)' pair into a byte offset within 'source' by validating both are nonzero, ensuring the line exists, checking the column is within that line’s byte length, and returning 'start + column - 1' or an error otherwise. [crates/gcode/src/commands/symbol_at.rs:202-218] |
| `line_bounds` | function | Returns the byte-range bounds of the 1-based 'line' in 'source', treating '\n' as the line separator and excluding a trailing '\r' before the line break if present, or 'None' if the requested line does not exist. [crates/gcode/src/commands/symbol_at.rs:220-233] |
| `trim_cr` | function | Returns 'end - 1' when the slice range '[start, end)' is non-empty and the last byte is '\r', otherwise returns 'end'. [crates/gcode/src/commands/symbol_at.rs:235-241] |
| `select_symbol` | function | 'select_symbol' returns the best matching 'Symbol' for a 'SymbolAtTarget', preferring the smallest symbol that contains the target and otherwise choosing the nearest symbol by position, while annotating the result with 'MatchKind' and computed line/byte distances. [crates/gcode/src/commands/symbol_at.rs:243-268] |
| `contains_target` | function | Returns 'true' if the given 'SymbolAtTarget' falls within the symbol’s byte range when 'byte_offset' is present, otherwise if its line number lies within the symbol’s inclusive line range. [crates/gcode/src/commands/symbol_at.rs:270-275] |
| `compare_containing` | function | Compares two 'Symbol's by their containing 'line_span', then by 'byte_span', and finally by descending 'byte_start' of the left versus right symbol to break ties. [crates/gcode/src/commands/symbol_at.rs:277-282] |
| `compare_nearest` | function | Compares two symbols by proximity to a target position, ordering first by line distance, then by byte offset distance when available, and finally by a previous-selection preference tie-breaker. [crates/gcode/src/commands/symbol_at.rs:284-292] |
| `compare_previous_preference` | function | Returns an 'Ordering' that prioritizes symbols marked as “previous” for the given target, ordering previous over non-previous, sorting two previous symbols by descending 'line_end' then 'byte_end' then 'byte_start', and sorting two non-previous symbols by ascending 'line_start' then 'byte_start'. [crates/gcode/src/commands/symbol_at.rs:294-311] |
| `is_previous_symbol` | function | Returns 'true' if the symbol ends before the target byte offset or, when no byte-offset decision applies, if the symbol’s ending line is strictly before the target line. [crates/gcode/src/commands/symbol_at.rs:313-323] |
| `line_span` | function | Returns the number of lines spanned by 'symbol' by computing 'line_end - line_start' with saturation at zero to avoid underflow. [crates/gcode/src/commands/symbol_at.rs:325-327] |
| `byte_span` | function | Returns the non-negative byte length of 'symbol' by subtracting 'byte_start' from 'byte_end' with saturating arithmetic to avoid underflow. [crates/gcode/src/commands/symbol_at.rs:329-331] |
| `line_distance` | function | Returns the unsigned distance from 'line' to 'symbol'’s line span, using 'symbol.line_start - line' when 'line' is before the symbol and 'line.saturating_sub(symbol.line_end)' otherwise, which yields '0' for lines within the span. [crates/gcode/src/commands/symbol_at.rs:333-339] |
| `byte_distance` | function | Returns the absolute byte distance from 'offset' to the 'symbol'’s byte range, yielding 'symbol.byte_start - offset' when 'offset' is before the symbol, 'offset.saturating_sub(symbol.byte_end)' when it is after, and '0' when it falls within the symbol. [crates/gcode/src/commands/symbol_at.rs:341-349] |
| `lookup_for_selection` | function | Constructs and returns a 'SymbolAtLookup' by copying the requested file and location from 'request' and propagating the selected symbol’s 'match_kind', 'distance_lines', and 'distance_bytes', while marking the column unit as '"byte"' when a column is present. [crates/gcode/src/commands/symbol_at.rs:351-365] |
| `symbol_source` | function | Returns the UTF-8 lossy string decoded from the byte range 'source[symbol.byte_start..symbol.byte_end]' clamped to 'source' bounds, together with the number of bytes actually sliced. [crates/gcode/src/commands/symbol_at.rs:367-372] |
| `symbol_at_json_value` | function | Serializes a 'Symbol' to 'serde_json::Value', injects '"source"' as the provided string and '"lookup"' as the serialized 'SymbolAtLookup', and returns the augmented JSON value. [crates/gcode/src/commands/symbol_at.rs:374-383] |
| `fallback_diagnostic` | function | Returns a human-readable diagnostic string only when 'quiet' is false and the lookup used 'MatchKind::Nearest', describing the requested file/line[/column], the nearest visible symbol’s location, kind, qualified name, and line/byte distance, otherwise 'None'. [crates/gcode/src/commands/symbol_at.rs:385-410] |
| `plural` | function | Returns the singular 'unit' when 'value == 1', otherwise maps '"line"' to '"lines"' and '"byte"' to '"bytes"', falling back to the original 'unit' for all other inputs. [crates/gcode/src/commands/symbol_at.rs:412-422] |
| `symbol` | function | Constructs and returns a 'Symbol' for a TypeScript function using the provided name and source span, populating fixed metadata fields and setting 'signature' to 'Some("function {name}()")' while leaving 'docstring', 'parent_symbol_id', 'content_hash', 'summary', 'created_at', and 'updated_at' empty or 'None'. [crates/gcode/src/commands/symbol_at.rs:429-456] |
| `error_text` | function | Returns the 'anyhow::Error' message as a 'String' when 'result' is 'Err', and panics with '"expected error"' if 'result' is 'Ok'. [crates/gcode/src/commands/symbol_at.rs:458-463] |
| `parses_path_line_and_column_from_the_right` | function | Verifies that 'parse_location' splits a location string from the right so a colon-containing path is preserved while the final one or two numeric segments are parsed as 'line' and optional 'column'. [crates/gcode/src/commands/symbol_at.rs:466-476] |
| `parses_path_with_separate_line` | function | Verifies that 'parse_location("src:auth.ts", Some(42))' parses a path containing a colon as the file name and assigns the separate line argument to 'line' with 'column' left 'None'. [crates/gcode/src/commands/symbol_at.rs:479-485] |
| `rejects_invalid_location_forms` | function | Verifies that 'parse_location' rejects malformed location strings by emitting specific errors for missing or duplicated line numbers, zero or non-integer line values, and zero or non-integer column values. [crates/gcode/src/commands/symbol_at.rs:488-509] |
| `converts_one_based_byte_columns_to_offsets` | function | Verifies that 'line_column_to_byte_offset' correctly converts 1-based line/byte-column pairs into zero-based byte offsets for ASCII and multibyte UTF-8 text, including offsets at line starts and after a multibyte character. [crates/gcode/src/commands/symbol_at.rs:512-520] |
| `rejects_out_of_range_columns` | function | Verifies that 'line_column_to_byte_offset' returns an error whose text contains 'column 4 is out of range' when asked for column 4 on the single-line input 'abc\n'. [crates/gcode/src/commands/symbol_at.rs:523-528] |
| `containing_selection_prefers_smallest_span_then_later_start` | function | Verifies that 'select_symbol' chooses the smallest containing symbol for a line-based target and, when spans are equal, breaks ties by preferring the later start offset, yielding the 'later' symbol as a 'Containing' match with zero line distance. [crates/gcode/src/commands/symbol_at.rs:531-549] |
| `nearest_selection_prefers_previous_on_equal_line_distance` | function | Verifies that 'select_symbol' chooses the previous symbol as the nearest match when two candidates are equally distant in lines from the target line, and that the result is tagged 'MatchKind::Nearest' with a two-line distance. [crates/gcode/src/commands/symbol_at.rs:552-569] |
| `nearest_selection_uses_byte_distance_for_column_ties` | function | Verifies that when two symbols are equally close by line and column, 'select_symbol' breaks the tie using byte-offset distance, selecting the symbol whose range is nearest in bytes and reporting a 'Nearest' match with zero line distance and one-byte distance. [crates/gcode/src/commands/symbol_at.rs:572-590] |
| `lookup_json_includes_source_and_metadata` | function | Verifies that 'symbol_at_json_value' emits JSON containing the symbol name, source text, and a nested 'lookup' object with the requested file, line, optional column, column unit, match kind, and distance metadata. [crates/gcode/src/commands/symbol_at.rs:593-616] |
| `nearest_diagnostic_is_suppressed_when_quiet_or_containing` | function | Verifies that 'fallback_diagnostic' emits a nearest-symbol diagnostic only for 'MatchKind::Nearest' when not quiet, including the nearest visible symbol and source location, but returns 'None' when quiet or when 'match_kind' is 'Containing'. [crates/gcode/src/commands/symbol_at.rs:619-640] |

