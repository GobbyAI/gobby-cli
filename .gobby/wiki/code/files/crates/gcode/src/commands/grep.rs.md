---
title: crates/gcode/src/commands/grep.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/grep.rs
  ranges:
  - 21-33
  - 36-40
  - 43-46
  - 49-52
  - 55-58
  - 61-68
  - 71-84
  - 87-92
  - 94-125
  - 127-234
  - 236-254
  - 256-276
  - 279-285
  - 287-352
  - 354-375
  - 377-407
  - 409-414
  - 416-439
  - 417-430
  - 432-438
  - 441-456
  - 458-467
  - 469-472
  - 474-497
  - 475-481
  - 483-496
  - 499-515
  - 517-533
  - 535-582
  - 584-597
  - 603-609
  - 611-625
  - 628-633
  - 636-647
  - 650-664
  - 667-674
  - 677-685
  - 688-703
  - 706-738
  - 741-759
  - 762-776
  - 779-799
  - 802-817
  - 820-837
  - 840-868
  - 871-879
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/grep.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/grep.rs` exposes 46 indexed API symbols.
[crates/gcode/src/commands/grep.rs:21-33]
[crates/gcode/src/commands/grep.rs:36-40]
[crates/gcode/src/commands/grep.rs:43-46]
[crates/gcode/src/commands/grep.rs:49-52]
[crates/gcode/src/commands/grep.rs:55-58]
[crates/gcode/src/commands/grep.rs:61-68]
[crates/gcode/src/commands/grep.rs:71-84]
[crates/gcode/src/commands/grep.rs:87-92]
[crates/gcode/src/commands/grep.rs:94-125]
[crates/gcode/src/commands/grep.rs:127-234]
[crates/gcode/src/commands/grep.rs:236-254]
[crates/gcode/src/commands/grep.rs:256-276]
[crates/gcode/src/commands/grep.rs:279-285]
[crates/gcode/src/commands/grep.rs:287-352]
[crates/gcode/src/commands/grep.rs:354-375]
[crates/gcode/src/commands/grep.rs:377-407]
[crates/gcode/src/commands/grep.rs:409-414]
[crates/gcode/src/commands/grep.rs:416-439]
[crates/gcode/src/commands/grep.rs:417-430]
[crates/gcode/src/commands/grep.rs:432-438]
[crates/gcode/src/commands/grep.rs:441-456]
[crates/gcode/src/commands/grep.rs:458-467]
[crates/gcode/src/commands/grep.rs:469-472]
[crates/gcode/src/commands/grep.rs:474-497]
[crates/gcode/src/commands/grep.rs:475-481]
[crates/gcode/src/commands/grep.rs:483-496]
[crates/gcode/src/commands/grep.rs:499-515]
[crates/gcode/src/commands/grep.rs:517-533]
[crates/gcode/src/commands/grep.rs:535-582]
[crates/gcode/src/commands/grep.rs:584-597]
[crates/gcode/src/commands/grep.rs:603-609]
[crates/gcode/src/commands/grep.rs:611-625]
[crates/gcode/src/commands/grep.rs:628-633]
[crates/gcode/src/commands/grep.rs:636-647]
[crates/gcode/src/commands/grep.rs:650-664]
[crates/gcode/src/commands/grep.rs:667-674]
[crates/gcode/src/commands/grep.rs:677-685]
[crates/gcode/src/commands/grep.rs:688-703]
[crates/gcode/src/commands/grep.rs:706-738]
[crates/gcode/src/commands/grep.rs:741-759]
[crates/gcode/src/commands/grep.rs:762-776]
[crates/gcode/src/commands/grep.rs:779-799]
[crates/gcode/src/commands/grep.rs:802-817]
[crates/gcode/src/commands/grep.rs:820-837]
[crates/gcode/src/commands/grep.rs:840-868]
[crates/gcode/src/commands/grep.rs:871-879]

## API Symbols

- `GrepOptions` (class) component `GrepOptions [class]` (`9f43ffb2-a0e2-584d-8dfe-82f0ce874a24`) lines 21-33 [crates/gcode/src/commands/grep.rs:21-33]
  - Signature: `pub struct GrepOptions<'a> {`
  - Purpose: `GrepOptions<'a>` is a configuration struct with borrowed references that encapsulates search parameters (pattern, file paths/globs), matching flags (fixed-string, case-insensitive, word-boundary), context boundaries, match limits, and output formatting for grep operations. [crates/gcode/src/commands/grep.rs:21-33]
- `IndexedContentChunk` (class) component `IndexedContentChunk [class]` (`a65c0559-e81e-5a17-9e34-ebeed224caec`) lines 36-40 [crates/gcode/src/commands/grep.rs:36-40]
  - Signature: `struct IndexedContentChunk {`
  - Purpose: `IndexedContentChunk` is a struct that pairs a content string with its source file path and starting line number for location-indexed retrieval. [crates/gcode/src/commands/grep.rs:36-40]
- `LoadedIndexedChunks` (class) component `LoadedIndexedChunks [class]` (`6fc15fb0-bb89-5936-9db4-bcaa6d6f7df6`) lines 43-46 [crates/gcode/src/commands/grep.rs:43-46]
  - Signature: `struct LoadedIndexedChunks {`
  - Purpose: `LoadedIndexedChunks` is a struct that encapsulates a vector of indexed content chunks alongside a boolean flag indicating whether the result set was truncated. [crates/gcode/src/commands/grep.rs:43-46]
- `GrepSpan` (class) component `GrepSpan [class]` (`a878e6c4-236b-53fc-a236-408cf43fdbd2`) lines 49-52 [crates/gcode/src/commands/grep.rs:49-52]
  - Signature: `pub(crate) struct GrepSpan {`
  - Purpose: `GrepSpan` is a crate-private struct that represents a byte-range span defined by start and end position indices. [crates/gcode/src/commands/grep.rs:49-52]
- `GrepContextLine` (class) component `GrepContextLine [class]` (`b8e8d047-8f26-5940-971b-710d77152bf7`) lines 55-58 [crates/gcode/src/commands/grep.rs:55-58]
  - Signature: `pub(crate) struct GrepContextLine {`
  - Purpose: `GrepContextLine` is a crate-internal struct that pairs a line number (`usize`) with its corresponding text content (`String`) to represent a single line in grep search results. [crates/gcode/src/commands/grep.rs:55-58]
- `GrepMatch` (class) component `GrepMatch [class]` (`86f41bac-4649-5bd6-97d6-9fd4f872ff30`) lines 61-68 [crates/gcode/src/commands/grep.rs:61-68]
  - Signature: `pub(crate) struct GrepMatch {`
  - Purpose: `GrepMatch` is a crate-private struct representing a single grep search result, containing the file path, line number, matched text with highlighted spans, and surrounding context lines. [crates/gcode/src/commands/grep.rs:61-68]
- `GrepResponse` (class) component `GrepResponse [class]` (`58726474-5973-560c-9146-2faff91c89a3`) lines 71-84 [crates/gcode/src/commands/grep.rs:71-84]
  - Signature: `struct GrepResponse {`
  - Purpose: GrepResponse encapsulates a configurable pattern search operation's parameters, matching results, and execution metadata including truncation status and scanned chunk count. [crates/gcode/src/commands/grep.rs:71-84]
- `GrepResult` (class) component `GrepResult [class]` (`27c1f00b-2e90-5b76-809a-1b4bea5df859`) lines 87-92 [crates/gcode/src/commands/grep.rs:87-92]
  - Signature: `struct GrepResult {`
  - Purpose: GrepResult is a struct that encapsulates grep search results, containing metadata (scanned chunk count, matched line count, truncation flag) and a vector of individual pattern matches. [crates/gcode/src/commands/grep.rs:87-92]
- `run` (function) component `run [function]` (`e4ad18ed-bf49-5e30-9643-c4663ca79386`) lines 94-125 [crates/gcode/src/commands/grep.rs:94-125]
  - Signature: `pub fn run(ctx: &Context, options: GrepOptions<'_>) -> anyhow::Result<()> {`
  - Purpose: Performs pattern matching on indexed database chunks with path/glob filtering and outputs results in the specified format (JSON or text). [crates/gcode/src/commands/grep.rs:94-125]
- `load_indexed_chunks` (function) component `load_indexed_chunks [function]` (`83404754-52be-5b49-a427-5ebe679917e5`) lines 127-234 [crates/gcode/src/commands/grep.rs:127-234]
  - Signature: `fn load_indexed_chunks(`
  - Purpose: Loads indexed code chunks from a database for single or overlay project scopes, applying grep filters and excluding tombstoned language files, with results ordered by file path and line position. [crates/gcode/src/commands/grep.rs:127-234]
- `push_grep_sql_prefilters` (function) component `push_grep_sql_prefilters [function]` (`2ff26069-514a-56c1-a80e-1a6be42ecbce`) lines 236-254 [crates/gcode/src/commands/grep.rs:236-254]
  - Signature: `fn push_grep_sql_prefilters<'a>(`
  - Purpose: Appends SQL WHERE conditions and their ToSql parameter references for path and glob prefix filters from a GrepFilters struct to mutable condition and parameter vectors. [crates/gcode/src/commands/grep.rs:236-254]
- `push_grep_sql_prefix_filter` (function) component `push_grep_sql_prefix_filter [function]` (`7c0008e1-a6c7-54e5-a63b-b063ec39052f`) lines 256-276 [crates/gcode/src/commands/grep.rs:256-276]
  - Signature: `fn push_grep_sql_prefix_filter<'a>(`
  - Purpose: Appends a parameterized SQL EXISTS condition using UNNEST to filter file paths matching any prefix pattern in an array via LIKE comparison with backslash escaping. [crates/gcode/src/commands/grep.rs:256-276]
- `grep_chunks` (function) component `grep_chunks [function]` (`954329a6-d4a3-5a62-817d-5bf3efe8d331`) lines 279-285 [crates/gcode/src/commands/grep.rs:279-285]
  - Signature: `fn grep_chunks(`
  - Purpose: **Constructs `GrepFilters` from the provided path and glob options, then delegates filtered grep searching on the indexed content chunks to `grep_chunks_with_filters`.** [crates/gcode/src/commands/grep.rs:279-285]
- `grep_chunks_with_filters` (function) component `grep_chunks_with_filters [function]` (`8d76e759-dbab-5321-9fab-32689530c947`) lines 287-352 [crates/gcode/src/commands/grep.rs:287-352]
  - Signature: `fn grep_chunks_with_filters(`
  - Purpose: Searches indexed content chunks for pattern matches using optional file path filters, deduplicates results by (file_path, line_number) coordinates, enforces a maximum count limit, and attaches before/after context lines to matches. [crates/gcode/src/commands/grep.rs:287-352]
- `context_line_numbers` (function) component `context_line_numbers [function]` (`dcc025cd-e9eb-576c-b9df-4e1316cbda62`) lines 354-375 [crates/gcode/src/commands/grep.rs:354-375]
  - Signature: `fn context_line_numbers(`
  - Purpose: Aggregates context line numbers surrounding each grep match into a file-path-indexed map, including a configurable number of lines before and after each match. [crates/gcode/src/commands/grep.rs:354-375]
- `collect_context_lines` (function) component `collect_context_lines [function]` (`45706af7-f610-56ef-a836-ce2fc419b8c2`) lines 377-407 [crates/gcode/src/commands/grep.rs:377-407]
  - Signature: `fn collect_context_lines(`
  - Purpose: Extracts specified lines from indexed content chunks that match file path filters, returning a nested map indexed by file path and line number. [crates/gcode/src/commands/grep.rs:377-407]
- `GrepFilters` (class) component `GrepFilters [class]` (`bd62ccd2-646e-5409-a0db-1ad365e2cdf0`) lines 409-414 [crates/gcode/src/commands/grep.rs:409-414]
  - Signature: `struct GrepFilters {`
  - Purpose: GrepFilters is a struct that encapsulates glob patterns (both raw and compiled) for path filtering along with optional SQL prefix representations to optimize pattern-based queries. [crates/gcode/src/commands/grep.rs:409-414]
- `GrepFilters` (class) component `GrepFilters [class]` (`e13afc24-2daf-53d8-b92e-792ca9241336`) lines 416-439 [crates/gcode/src/commands/grep.rs:416-439]
  - Signature: `impl GrepFilters {`
  - Purpose: GrepFilters filters file paths by requiring conjunctive matching against compiled regex patterns and glob patterns, where empty filter sets default to true. [crates/gcode/src/commands/grep.rs:416-439]
- `GrepFilters.new` (method) component `GrepFilters.new [method]` (`cf1f9046-be13-5808-831b-256769c7b1b8`) lines 417-430 [crates/gcode/src/commands/grep.rs:417-430]
  - Signature: `fn new(paths: &[String], globs: &[String]) -> anyhow::Result<Self> {`
  - Purpose: Initializes a pattern matcher by expanding and compiling file paths and glob patterns into optimized compiled forms with SQL-like prefixes for efficient filtering. [crates/gcode/src/commands/grep.rs:417-430]
- `GrepFilters.matches` (method) component `GrepFilters.matches [method]` (`c641df2d-cacd-550c-ad50-e07cf000e199`) lines 432-438 [crates/gcode/src/commands/grep.rs:432-438]
  - Signature: `fn matches(&self, file_path: &str) -> bool {`
  - Purpose: Returns true if the file_path matches all configured filters (paths and globs), treating empty filter collections as unconditional matches. [crates/gcode/src/commands/grep.rs:432-438]
- `sql_like_prefixes` (function) component `sql_like_prefixes [function]` (`644f2010-69d2-55f5-b0af-22fed8545f29`) lines 441-456 [crates/gcode/src/commands/grep.rs:441-456]
  - Signature: `fn sql_like_prefixes(patterns: &[String]) -> Option<Vec<String>> {`
  - Purpose: Extracts leading literal prefixes from wildcard patterns, escapes them for SQL LIKE context, and returns them with appended `%` wildcards or `None` if no prefixes exist. [crates/gcode/src/commands/grep.rs:441-456]
- `escape_like_prefix` (function) component `escape_like_prefix [function]` (`13033af0-a185-5280-a5f8-3afe00b8251b`) lines 458-467 [crates/gcode/src/commands/grep.rs:458-467]
  - Signature: `fn escape_like_prefix(value: &str) -> String {`
  - Purpose: Escapes SQL LIKE metacharacters by prefixing each occurrence of `%`, `_`, and `\` with a backslash. [crates/gcode/src/commands/grep.rs:458-467]
- `CompiledGlob` (class) component `CompiledGlob [class]` (`2799976f-1742-50e4-baed-e05e472703a0`) lines 469-472 [crates/gcode/src/commands/grep.rs:469-472]
  - Signature: `struct CompiledGlob {`
  - Purpose: `CompiledGlob` is a struct that encapsulates both the raw glob pattern string and its compiled `glob::Pattern` representation for efficient pattern matching. [crates/gcode/src/commands/grep.rs:469-472]
- `CompiledGlob` (class) component `CompiledGlob [class]` (`ed326f9c-7cb7-55d0-b99c-e166e877f2ad`) lines 474-497 [crates/gcode/src/commands/grep.rs:474-497]
  - Signature: `impl CompiledGlob {`
  - Purpose: CompiledGlob is a compiled glob pattern wrapper that implements ripgrep-style dual-scope matching, where patterns without slashes match against file basenames and patterns with slashes match against full paths. [crates/gcode/src/commands/grep.rs:474-497]
- `CompiledGlob.new` (method) component `CompiledGlob.new [method]` (`074e9aa6-d4fa-5edd-87f1-8d351cf9b842`) lines 475-481 [crates/gcode/src/commands/grep.rs:475-481]
  - Signature: `fn new(raw: &str) -> anyhow::Result<Self> {`
  - Purpose: Creates a new instance from a raw string by compiling it into a `glob::Pattern` and converting any glob parse errors to `anyhow` errors. [crates/gcode/src/commands/grep.rs:475-481]
- `CompiledGlob.matches` (method) component `CompiledGlob.matches [method]` (`eb3daa05-3f26-5757-bee5-fce82627e4b0`) lines 483-496 [crates/gcode/src/commands/grep.rs:483-496]
  - Signature: `fn matches(&self, file_path: &str) -> bool {`
  - Purpose: Returns true if the pattern matches the full file path, or if the pattern contains no slashes, matches just the file's basename. [crates/gcode/src/commands/grep.rs:483-496]
- `context_before` (function) component `context_before [function]` (`b52b9585-424c-50f4-8867-c41a7db63ba5`) lines 499-515 [crates/gcode/src/commands/grep.rs:499-515]
  - Signature: `fn context_before(`
  - Purpose: Extracts the `context` number of lines immediately preceding a target line number from a BTreeMap of indexed strings and returns them as a vector of `GrepContextLine` structures. [crates/gcode/src/commands/grep.rs:499-515]
- `context_after` (function) component `context_after [function]` (`15cf79b4-25cf-5ac9-bbe7-b0b89c82c4e0`) lines 517-533 [crates/gcode/src/commands/grep.rs:517-533]
  - Signature: `fn context_after(`
  - Purpose: Retrieves the next `context` lines immediately following a specified line number from a sorted map of lines, returning them as `GrepContextLine` objects. [crates/gcode/src/commands/grep.rs:517-533]
- `format_text_matches` (function) component `format_text_matches [function]` (`c02cd8cb-a29e-55f8-9b93-ccd228274be1`) lines 535-582 [crates/gcode/src/commands/grep.rs:535-582]
  - Signature: `fn format_text_matches(matches: &[GrepMatch]) -> String {`
  - Purpose: Formats grep matches with their surrounding context lines, deduplicated against actual matches and grouped by file path. [crates/gcode/src/commands/grep.rs:535-582]
- `push_grouped_grep_line` (function) component `push_grouped_grep_line [function]` (`ec2e1060-afcb-5065-af30-f0cde31e01b5`) lines 584-597 [crates/gcode/src/commands/grep.rs:584-597]
  - Signature: `fn push_grouped_grep_line<'a>(`
  - Purpose: Accumulates grep-style formatted output grouped by file path, inserting the path header only when it changes and appending each match as a formatted line (line number + marker + trimmed text). [crates/gcode/src/commands/grep.rs:584-597]
- `chunk` (function) component `chunk [function]` (`ac573f3c-d5e8-5888-baa5-1b865c37f9bc`) lines 603-609 [crates/gcode/src/commands/grep.rs:603-609]
  - Signature: `fn chunk(path: &str, line_start: usize, content: &str) -> IndexedContentChunk {`
  - Purpose: Constructs and returns an `IndexedContentChunk` struct by converting the provided file path and content string references to owned `String` values and pairing them with the starting line number. [crates/gcode/src/commands/grep.rs:603-609]
- `options` (function) component `options [function]` (`6f61f38a-5454-559a-974c-5071faabe799`) lines 611-625 [crates/gcode/src/commands/grep.rs:611-625]
  - Signature: `fn options(pattern: &str) -> GrepOptions<'_> {`
  - Purpose: Constructs a `GrepOptions` struct with the provided search pattern and default configuration: empty paths/globs, all matching options disabled, and JSON output format. [crates/gcode/src/commands/grep.rs:611-625]
- `text_renders_grouped_grep_shape` (function) component `text_renders_grouped_grep_shape [function]` (`e0017516-64f8-5a21-bf17-16be7dd0b3e9`) lines 628-633 [crates/gcode/src/commands/grep.rs:628-633]
  - Signature: `fn text_renders_grouped_grep_shape() {`
  - Purpose: This test verifies that `grep_chunks` correctly identifies a pattern match within a text chunk and that `format_text_matches` renders the results in the expected grouped format showing the file path, line number, and matched text. [crates/gcode/src/commands/grep.rs:628-633]
- `text_groups_multiple_files` (function) component `text_groups_multiple_files [function]` (`a3d33973-a772-5cf8-b823-8598a2371b51`) lines 636-647 [crates/gcode/src/commands/grep.rs:636-647]
  - Signature: `fn text_groups_multiple_files() {`
  - Purpose: Tests that `grep_chunks` correctly searches multiple files for a pattern and formats the results with file paths, line numbers, and matched content. [crates/gcode/src/commands/grep.rs:636-647]
- `ordering_is_path_then_line` (function) component `ordering_is_path_then_line [function]` (`2bdd7782-cac8-5f88-9a7e-c2cf791486a3`) lines 650-664 [crates/gcode/src/commands/grep.rs:650-664]
  - Signature: `fn ordering_is_path_then_line() {`
  - Purpose: This function verifies that `grep_chunks` returns search matches sorted lexicographically by file path, then numerically by line number within each file. [crates/gcode/src/commands/grep.rs:650-664]
- `ignore_case_matches_case_insensitively` (function) component `ignore_case_matches_case_insensitively [function]` (`7e756417-f504-5fc1-8c4f-ab0542086d9e`) lines 667-674 [crates/gcode/src/commands/grep.rs:667-674]
  - Signature: `fn ignore_case_matches_case_insensitively() {`
  - Purpose: A test that validates case-insensitive grep matching by asserting that the search term "needle" matches "Needle" when the `ignore_case` option is enabled. [crates/gcode/src/commands/grep.rs:667-674]
- `fixed_strings_treat_regex_metacharacters_literally` (function) component `fixed_strings_treat_regex_metacharacters_literally [function]` (`3a304aaf-8f7d-5b7d-b921-37295bd0af53`) lines 677-685 [crates/gcode/src/commands/grep.rs:677-685]
  - Signature: `fn fixed_strings_treat_regex_metacharacters_literally() {`
  - Purpose: This test verifies that enabling the `fixed_strings` option causes the grep function to treat the search pattern "a.b" as a literal string rather than a regex pattern, matching only the exact sequence and not the regex metacharacter dot. [crates/gcode/src/commands/grep.rs:677-685]
- `sql_prefix_prefilter_requires_convertible_globs` (function) component `sql_prefix_prefilter_requires_convertible_globs [function]` (`ecad04ae-9a94-54de-808f-2bee566c70bf`) lines 688-703 [crates/gcode/src/commands/grep.rs:688-703]
  - Signature: `fn sql_prefix_prefilter_requires_convertible_globs() {`
  - Purpose: This test validates that `sql_like_prefixes` correctly converts filesystem paths and glob patterns into SQL LIKE predicates with properly escaped special characters, extracting common prefixes where applicable and returning `None` for non-convertible inputs. [crates/gcode/src/commands/grep.rs:688-703]
- `context_flags_include_bounded_neighbors` (function) component `context_flags_include_bounded_neighbors [function]` (`e068ba8c-f043-5a69-8dea-f72530f8a667`) lines 706-738 [crates/gcode/src/commands/grep.rs:706-738]
  - Signature: `fn context_flags_include_bounded_neighbors() {`
  - Purpose: # Summary

This function tests that `grep_chunks` correctly includes the specified number of context lines before and after a matched pattern, as determined by the `before_context` and `after_context` options. [crates/gcode/src/commands/grep.rs:706-738]
- `text_output_trims_leading_whitespace_without_changing_matches` (function) component `text_output_trims_leading_whitespace_without_changing_matches [function]` (`2551b512-edc2-5703-960d-1965d2dacff3`) lines 741-759 [crates/gcode/src/commands/grep.rs:741-759]
  - Signature: `fn text_output_trims_leading_whitespace_without_changing_matches() {`
  - Purpose: This test verifies that formatted grep output trims leading whitespace for display while the underlying match objects preserve their original whitespace. [crates/gcode/src/commands/grep.rs:741-759]
- `text_suppresses_duplicate_context_lines` (function) component `text_suppresses_duplicate_context_lines [function]` (`23478b36-66d4-5eb3-80ab-3ba256c877bb`) lines 762-776 [crates/gcode/src/commands/grep.rs:762-776]
  - Signature: `fn text_suppresses_duplicate_context_lines() {`
  - Purpose: # Summary

Tests that grep output with context correctly suppresses duplicate context lines when multiple matches have overlapping surrounding line ranges. [crates/gcode/src/commands/grep.rs:762-776]
- `max_count_caps_retained_matches_not_total_matching_lines` (function) component `max_count_caps_retained_matches_not_total_matching_lines [function]` (`b735aac2-8f6b-5d7c-bf1b-bfca81a1ddfd`) lines 779-799 [crates/gcode/src/commands/grep.rs:779-799]
  - Signature: `fn max_count_caps_retained_matches_not_total_matching_lines() {`
  - Purpose: # Summary

This test verifies that the `max_count` option limits the number of match instances returned (not the total matching lines in the source), and that `matched_lines` reflects only the lines in the truncated result set including context. [crates/gcode/src/commands/grep.rs:779-799]
- `json_match_contains_spans_and_context` (function) component `json_match_contains_spans_and_context [function]` (`e0d0bcee-eada-5623-9706-6f81ef7be175`) lines 802-817 [crates/gcode/src/commands/grep.rs:802-817]
  - Signature: `fn json_match_contains_spans_and_context() {`
  - Purpose: This test verifies that `grep_chunks` correctly serializes match results to JSON with multiple span positions within a matched line and includes before/after context lines. [crates/gcode/src/commands/grep.rs:802-817]
- `path_and_glob_filters_compose` (function) component `path_and_glob_filters_compose [function]` (`f92c30a6-8c83-59b4-a63b-d5d3a2a61c04`) lines 820-837 [crates/gcode/src/commands/grep.rs:820-837]
  - Signature: `fn path_and_glob_filters_compose() {`
  - Purpose: This test verifies that path and glob filters compose correctly to select only chunks matching both directory and filename pattern constraints simultaneously. [crates/gcode/src/commands/grep.rs:820-837]
- `bare_globs_match_basenames_but_slash_globs_match_paths` (function) component `bare_globs_match_basenames_but_slash_globs_match_paths [function]` (`c5305f9f-a236-51cf-89bb-3fa90015f6da`) lines 840-868 [crates/gcode/src/commands/grep.rs:840-868]
  - Signature: `fn bare_globs_match_basenames_but_slash_globs_match_paths() {`
  - Purpose: This function verifies that bare glob patterns match against file basenames only, while glob patterns containing path separators match against the full file path. [crates/gcode/src/commands/grep.rs:840-868]
- `overlapping_chunks_dedupe_by_file_and_line` (function) component `overlapping_chunks_dedupe_by_file_and_line [function]` (`73f14613-cf9a-5d14-b7bc-eccbe524a8ad`) lines 871-879 [crates/gcode/src/commands/grep.rs:871-879]
  - Signature: `fn overlapping_chunks_dedupe_by_file_and_line() {`
  - Purpose: This test verifies that `grep_chunks` correctly deduplicates identical chunk results originating from the same file and line number, reducing two matching chunks to a single result. [crates/gcode/src/commands/grep.rs:871-879]

