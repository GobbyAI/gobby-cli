---
title: crates/gcode/src/commands/grep.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/grep.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/grep.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

`crates/gcode/src/commands/grep.rs` exposes 44 indexed API symbols.

## How it fits

`crates/gcode/src/commands/grep.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GrepOptions` | class | 'GrepOptions<'a>' is a borrowed configuration struct for a grep-style search, carrying the search pattern, target paths and glob filters, matching flags, optional context/count limits, and an output 'Format'. [crates/gcode/src/commands/grep.rs:21-33] |
| `IndexedContentChunk` | class | 'IndexedContentChunk' is a struct that represents a snippet of file content annotated with its source file path and the starting line number within that file. [crates/gcode/src/commands/grep.rs:36-40] |
| `LoadedIndexedChunks` | class | 'LoadedIndexedChunks' is a struct that stores a 'Vec<IndexedContentChunk>' plus a 'truncated' boolean indicating whether the chunk set was incompletely loaded or cut off. [crates/gcode/src/commands/grep.rs:43-46] |
| `GrepSpan` | class | 'GrepSpan' is a crate-visible struct representing a half-open span of text or bytes with inclusive start and exclusive end offsets, both stored as 'usize'. [crates/gcode/src/commands/grep.rs:49-52] |
| `GrepContextLine` | class | 'GrepContextLine' is a crate-visible struct that represents a single grep context line by storing its 1-based line number as a 'usize' and its full line contents as a 'String'. [crates/gcode/src/commands/grep.rs:55-58] |
| `GrepMatch` | class | 'GrepMatch' is a crate-private struct representing a single grep result, containing the matched file path, 1-based line number, matched text, highlighted match spans, and the surrounding before/after context lines. [crates/gcode/src/commands/grep.rs:61-68] |
| `GrepResponse` | class | 'GrepResponse' is a search-result payload that records the query parameters and execution metadata for a grep operation, including the project and pattern used, matching options, scoped paths/globs, optional result limit, match count, truncation status, scanned chunk count, and the collected 'GrepMatch' entries. [crates/gcode/src/commands/grep.rs:71-84] |
| `GrepResult` | class | 'GrepResult' is a result struct that records how many chunks were scanned, how many lines matched, whether output was truncated, and the collected 'GrepMatch' entries. [crates/gcode/src/commands/grep.rs:87-92] |
| `run` | function | 'run' opens a readonly database connection, builds grep filters from the requested paths and globs, loads indexed chunks, searches them with the supplied 'GrepOptions', propagates any truncation, and then emits either a JSON 'GrepResponse' or formatted text matches. [crates/gcode/src/commands/grep.rs:94-125] |
| `load_indexed_chunks` | function | Queries 'code_content_chunks' joined with 'code_indexed_files' to load at most 'GREP_SQL_SAFETY_LIMIT + 1' indexed text chunks for the current project scope, excluding tombstone-language files and applying grep prefilters, returning them as 'LoadedIndexedChunks'. [crates/gcode/src/commands/grep.rs:127-234] |
| `push_grep_sql_prefilters` | function | Appends SQL prefilter clauses and their bound parameters for both 'path_sql_prefixes' and 'glob_sql_prefixes' by delegating to 'push_grep_sql_prefix_filter' with the provided table alias and 'GrepFilters'. [crates/gcode/src/commands/grep.rs:236-254] |
| `push_grep_sql_prefix_filter` | function | Adds an 'EXISTS' SQL predicate that filters '{alias}.file_path' by 'LIKE'-matching any provided text prefix array via 'unnest', appending the array as the next query parameter, and is a no-op when 'prefixes' is 'None' or empty. [crates/gcode/src/commands/grep.rs:256-276] |
| `grep_chunks` | function | Constructs 'GrepFilters' from 'options.paths' and 'options.globs', then delegates to 'grep_chunks_with_filters' to search the provided 'IndexedContentChunk' slice and return a 'GrepResult' or error. [crates/gcode/src/commands/grep.rs:279-285] |
| `grep_chunks_with_filters` | function | Filters the input chunks by path, scans each remaining line for pattern spans with a 'GrepMatcher', deduplicates matches by '(file_path, line)', truncates to 'max_count', gathers requested before/after context lines, and returns a 'GrepResult'. [crates/gcode/src/commands/grep.rs:287-352] |
| `context_line_numbers` | function | Builds, per file path, a deduplicated sorted set of line numbers surrounding each grep match by adding the specified number of preceding and following context lines around each match line. [crates/gcode/src/commands/grep.rs:354-375] |
| `collect_context_lines` | function | It returns a nested 'BTreeMap' of requested source lines, grouped by file path, by scanning only chunks whose paths match 'filters' and inserting the text of lines whose absolute numbers appear in 'needed', with early exit on an empty 'needed' set. [crates/gcode/src/commands/grep.rs:377-407] |
| `GrepFilters` | class | 'GrepFilters' is a filter-configuration struct that stores path and glob matchers, plus optional SQL prefix lists for path and glob constraints. [crates/gcode/src/commands/grep.rs:409-414] |
| `GrepFilters::new` | method | Constructs 'Self' by expanding 'paths', computing SQL 'LIKE' prefixes for the expanded paths and raw 'globs', compiling the expanded path patterns and each glob into validated internal representations, and propagating any compilation errors via 'anyhow::Result'. [crates/gcode/src/commands/grep.rs:417-430] |
| `GrepFilters::matches` | method | Returns 'true' when 'file_path' satisfies both filters: either 'self.paths' is empty or at least one path pattern matches it, and either 'self.globs' is empty or at least one glob matches it. [crates/gcode/src/commands/grep.rs:432-438] |
| `sql_like_prefixes` | function | Returns 'None' for an empty input, otherwise extracts the literal leading segment before any '*', '?', or '[' from each pattern, escapes it for SQL 'LIKE', appends '%', and returns 'Some' only if at least one non-empty prefix was produced. [crates/gcode/src/commands/grep.rs:441-456] |
| `escape_like_prefix` | function | Returns a new 'String' containing 'value' with every SQL 'LIKE' wildcard or escape character ('%', '_', '\') prefixed by '\' so the result can be used as a literal prefix pattern. [crates/gcode/src/commands/grep.rs:458-467] |
| `CompiledGlob` | class | 'CompiledGlob' is a struct that stores both the original glob string ('raw') and its precompiled 'glob::Pattern' representation ('pattern') for efficient matching. [crates/gcode/src/commands/grep.rs:469-472] |
| `CompiledGlob::new` | method | Constructs 'Self' from 'raw' by storing the input string and compiling it into a 'glob::Pattern', returning an 'anyhow::Error' with a formatted message if pattern parsing fails. [crates/gcode/src/commands/grep.rs:475-481] |
| `CompiledGlob::matches` | method | Returns 'true' if the compiled glob matches the full 'file_path', or, for patterns without '/', if it matches the path’s basename; otherwise returns 'false'. [crates/gcode/src/commands/grep.rs:483-496] |
| `context_before` | function | Returns the preceding 'context' lines before 'line' from a 'BTreeMap' of line numbers to text, cloning each matching entry into a 'Vec<GrepContextLine>' and yielding an empty vector when 'context' is zero. [crates/gcode/src/commands/grep.rs:499-515] |
| `context_after` | function | Returns up to 'context' lines after 'line' from the 'BTreeMap', cloning each matching entry into 'GrepContextLine' values and returning an empty vector when 'context == 0'. [crates/gcode/src/commands/grep.rs:517-533] |
| `format_text_matches` | function | Formats a slice of 'GrepMatch' records into a newline-joined grep-style text block by emitting each unique non-matching before/after context line once per path, then the matching line with ':' separators, while grouping consecutive lines by file path. [crates/gcode/src/commands/grep.rs:535-582] |
| `push_grouped_grep_line` | function | Appends a path header to 'lines' whenever the input 'path' differs from 'current_path', updates 'current_path', and then appends the formatted grep line as '"{line}{marker}{text.trim_start()}"'. [crates/gcode/src/commands/grep.rs:584-597] |
| `chunk` | function | Constructs and returns an 'IndexedContentChunk' by copying the provided 'path' and 'content' into owned 'String' fields and setting 'line_start' to the supplied starting line. [crates/gcode/src/commands/grep.rs:603-609] |
| `options` | function | Constructs and returns a 'GrepOptions<'_>' initialized with the provided 'pattern', empty 'paths' and 'globs', all match modifiers disabled, no context or count limits, and 'Format::Json' output. [crates/gcode/src/commands/grep.rs:611-625] |
| `text_renders_grouped_grep_shape` | function | Verifies that 'grep_chunks' formats a single matching line as grouped text output with the file name on its own line followed by the 1-based line number and matched line content ('src/lib.rs\n2:needle'). [crates/gcode/src/commands/grep.rs:628-633] |
| `text_groups_multiple_files` | function | Verifies that 'grep_chunks' groups matches by file and formats results for multiple files as 'path', then line-numbered match text, preserving order across 'src/a.rs' and 'tests/b.rs'. [crates/gcode/src/commands/grep.rs:636-647] |
| `ordering_is_path_then_line` | function | Verifies that 'grep_chunks' returns matches ordered lexicographically by file path and, within the same path, by ascending line number. [crates/gcode/src/commands/grep.rs:650-664] |
| `ignore_case_matches_case_insensitively` | function | Verifies that enabling 'ignore_case' causes 'grep_chunks' to match the chunk text '"Needle"' against the lowercase pattern '"needle"' and return exactly one match. [crates/gcode/src/commands/grep.rs:667-674] |
| `fixed_strings_treat_regex_metacharacters_literally` | function | Verifies that when 'fixed_strings' is enabled, the pattern 'a.b' is matched literally rather than as a regex, yielding exactly one match on line 1 of the input chunk. [crates/gcode/src/commands/grep.rs:677-685] |
| `sql_prefix_prefilter_requires_convertible_globs` | function | Verifies that 'sql_like_prefixes' only returns SQL 'LIKE' prefilter prefixes for inputs that can be losslessly converted from paths or globs, escaping special characters like '_', and returns 'None' for empty or non-convertible glob sets. [crates/gcode/src/commands/grep.rs:688-703] |
| `context_flags_include_bounded_neighbors` | function | Verifies that 'grep_chunks' includes the requested bounded before/after context lines around a match and formats them correctly in the output. [crates/gcode/src/commands/grep.rs:706-738] |
| `text_output_trims_leading_whitespace_without_changing_matches` | function | Verifies that 'grep_chunks' preserves the original matched and surrounding line contents while 'format_text_matches' trims leading whitespace only for displayed match text, yielding 'needle' at the match site without altering match or context line selection. [crates/gcode/src/commands/grep.rs:741-759] |
| `text_suppresses_duplicate_context_lines` | function | Verifies that 'format_text_matches' suppresses duplicate context lines between adjacent matches so a shared middle line is emitted once as both trailing and leading context in the rendered grep output. [crates/gcode/src/commands/grep.rs:762-776] |
| `max_count_caps_retained_matches_not_total_matching_lines` | function | Verifies that 'max_count' limits the number of retained match records while 'matched_lines' still counts all matching lines in the chunk, and that context lines are preserved around the retained match with 'truncated' set. [crates/gcode/src/commands/grep.rs:779-799] |
| `json_match_contains_spans_and_context` | function | Verifies that a grep match serialized to JSON includes the expected path, line number, matched text, span offsets for both occurrences of 'needle', and one line of before/after context. [crates/gcode/src/commands/grep.rs:802-817] |
| `path_and_glob_filters_compose` | function | Verifies that 'grep_chunks' composes path and glob filters with logical intersection, scanning only chunks under 'src/gobby' that also match '*.py' and returning just 'src/gobby/app.py'. [crates/gcode/src/commands/grep.rs:820-837] |
| `bare_globs_match_basenames_but_slash_globs_match_paths` | function | Verifies that a bare glob like '*.py' matches file basenames in multiple directories, while a slash-containing glob like 'src/*.py' matches only paths under the specified directory, yielding two matches for the former and one for the latter. [crates/gcode/src/commands/grep.rs:840-868] |
| `overlapping_chunks_dedupe_by_file_and_line` | function | Verifies that 'grep_chunks' deduplicates overlapping duplicate chunks by file and starting line, producing a single match for identical 'src/lib.rs' chunks containing 'needle'. [crates/gcode/src/commands/grep.rs:871-879] |

