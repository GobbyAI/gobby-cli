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

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/commands/grep.rs` exposes 44 indexed API symbols.

## How it fits

`crates/gcode/src/commands/grep.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

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

_5 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/grep.rs` for the full list._

_Verified by 15 in-file unit tests._

