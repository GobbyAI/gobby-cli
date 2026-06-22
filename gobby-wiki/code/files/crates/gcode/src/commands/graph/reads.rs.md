---
title: crates/gcode/src/commands/graph/reads.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/reads.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/reads.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/commands/graph/reads.rs` exposes 42 indexed API symbols.

## How it fits

`crates/gcode/src/commands/graph/reads.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `hint_for` | function | Returns 'Some(GRAPH_BACKEND_HINT.to_string())' when 'ctx.falkordb' is 'None', otherwise returns 'None'. [crates/gcode/src/commands/graph/reads.rs:19-25] |
| `hint_for_error` | function | Returns a context-dependent hint for a graph-related error, mapping 'GraphReadError::NotConfigured' and all non-'GraphReadError' cases to 'hint_for(ctx)', 'GraphReadError::Unreachable' to a FalkorDB-unreachable message, and otherwise producing no special handling beyond the default hint. [crates/gcode/src/commands/graph/reads.rs:27-35] |
| `print_graph_hint_text` | function | Prints a 'Hint: ...' message to stderr using the first available hint derived from 'error' via 'hint_for_error(ctx, err)' or, if absent, from 'hint_for(ctx)', and emits nothing when no hint is available. [crates/gcode/src/commands/graph/reads.rs:37-43] |
| `print_hint_text` | function | Prints 'Hint: {hint}' to standard error only when 'hint' is 'Some(&str)', and does nothing for 'None'. [crates/gcode/src/commands/graph/reads.rs:45-49] |
| `graph_read_unavailable` | function | Returns 'true' when the error can be downcast to 'code_graph::GraphReadError' and is either 'NotConfigured' or 'Unreachable { .. }', otherwise 'false'. [crates/gcode/src/commands/graph/reads.rs:51-59] |
| `empty_paged_response` | function | Returns an empty paged response in either JSON or text format: for JSON it prints a 'PagedResponse<T>' with 'total = 0', the given 'offset' and 'limit', no results, and an optional hint derived from an error or context, and for text it prints a graph hint and returns 'Ok(())'. [crates/gcode/src/commands/graph/reads.rs:61-84] |
| `graph_read_or_empty` | function | 'graph_read_or_empty' executes a reader closure and returns 'Ok(Some(value))' on success, converts 'graph_read_unavailable' errors into an empty paged response via 'empty_paged_response' and returns 'Ok(None)', and otherwise propagates the original error. [crates/gcode/src/commands/graph/reads.rs:86-101] |
| `format_grouped_graph_results` | function | 'format_grouped_graph_results' groups 'GraphResult' values by 'file_path' in sorted key order, emits each file header as the path or '"<unknown>"' for empty paths, sorts each group by 'line', 'name', 'relation', then 'distance', formats each entry with 'format_line', and joins all lines with newline separators. [crates/gcode/src/commands/graph/reads.rs:103-129] |
| `format_caller_result_line` | function | Formats a 'GraphResult' into a single caller-result string as '"{line} [{confidence}] {name} -> {target_name}"'. [crates/gcode/src/commands/graph/reads.rs:131-136] |
| `format_usage_result_line` | function | Formats a 'GraphResult' into a single usage-line string containing its line number, confidence, relation name or 'unknown', source name, and the provided target name in the form '"{line} [{confidence}] [{relation}] {name} -> {target_name}"'. [crates/gcode/src/commands/graph/reads.rs:138-144] |
| `format_blast_radius_result_line` | function | Formats a 'GraphResult' into a single line as '"{line} [{confidence}] [distance={distance}] {name}"', substituting '0' when 'distance' is 'None'. [crates/gcode/src/commands/graph/reads.rs:146-152] |
| `GraphPathEndpoint` | class | 'GraphPathEndpoint' is a serde-serializable struct representing a path endpoint with an optional 'id' field omitted when 'None' and a required 'display_name' string. [crates/gcode/src/commands/graph/reads.rs:155-159] |
| `GraphPathResponse` | class | 'GraphPathResponse' is a serialized response struct describing whether a path was found between two graph endpoints in a project, along with the search depth, hop count, ordered path steps, and an optional hint. [crates/gcode/src/commands/graph/reads.rs:162-172] |
| `path_endpoint` | function | Constructs a 'GraphPathEndpoint' by copying the resolved symbol’s 'id' and 'display_name' when present, otherwise leaving 'id' as 'None' and using 'input' as the 'display_name'. [crates/gcode/src/commands/graph/reads.rs:174-181] |
| `format_symbol_path_text` | function | Formats a human-readable symbol path summary by returning a no-path message when 'path' is empty, otherwise emitting a header with the hop count followed by one numbered line per 'GraphPathStep' showing the symbol name and 'file_path:line', substituting '"<unknown>"' for empty file paths. [crates/gcode/src/commands/graph/reads.rs:183-214] |
| `print_symbol_path_response` | function | Constructs a 'GraphPathResponse' from the given endpoints and path, then renders it as JSON or human-readable text, including a graph hint when no path is found. [crates/gcode/src/commands/graph/reads.rs:216-251] |
| `resolve_symbol_with_connection` | function | Resolves a graph symbol for a given 'project_id' using a PostgreSQL client, short-circuiting to ID-based lookup when 'input' parses as a UUID and otherwise delegating to full-text symbol resolution, returning the resolved symbol plus any candidate strings. [crates/gcode/src/commands/graph/reads.rs:253-266] |
| `resolve_symbol_candidates` | function | Opens a read-only database connection from 'ctx.database_url', logs and returns '(None, Vec::new())' if the connection fails, otherwise delegates to 'resolve_symbol_with_connection' with the project ID and input string. [crates/gcode/src/commands/graph/reads.rs:268-280] |
| `print_symbol_resolution_failure` | function | Prints an error message to stderr indicating either that no symbol matched 'input' or that the symbol resolution is ambiguous, listing the provided 'suggestions' when present. [crates/gcode/src/commands/graph/reads.rs:282-291] |
| `resolve_symbol` | function | Resolves 'input' to an optional 'ResolvedGraphSymbol' via 'resolve_symbol_candidates', prints a resolution failure message with suggestions when no symbol is found, and returns the resolved value or error. [crates/gcode/src/commands/graph/reads.rs:295-301] |
| `resolve_blast_radius_target` | function | Attempts to resolve 'input' first as an internal symbol via 'resolve_symbol_candidates', then as an external call target via 'code_graph::resolve_external_call_target', returning 'Some(ResolvedGraphSymbol)' on success and otherwise emitting an appropriate error/suggestion message and 'Ok(None)'. [crates/gcode/src/commands/graph/reads.rs:303-332] |
| `resolve_symbol_or_empty_response` | function | Calls 'resolve_symbol(ctx, input)' and returns the resolved symbol if present, otherwise emits an empty paged 'GraphResult' response using the provided 'offset', 'limit', and 'format', then returns 'Ok(None)'. [crates/gcode/src/commands/graph/reads.rs:334-348] |
| `read_paged_symbol_graph_results` | function | Performs paginated graph-read gating and symbol resolution, then returns 'Some((ResolvedGraphSymbol, total_count, page_results))' by invoking 'count' and 'find' for the resolved symbol ID, or 'None' if any empty-response condition applies. [crates/gcode/src/commands/graph/reads.rs:350-383] |
| `callers` | function | Fetches a paginated list of callers for the given symbol via the code graph, then emits either JSON 'PagedResponse' output or formatted text with empty-result and pagination hints. [crates/gcode/src/commands/graph/reads.rs:385-436] |

_18 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/graph/reads.rs` for the full list._

