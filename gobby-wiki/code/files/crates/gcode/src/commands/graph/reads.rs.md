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

`crates/gcode/src/commands/graph/reads.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

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
| `usages` | function | 'usages' queries paginated usage locations for a symbol from the code graph, trims them to an optional token budget while merging hints, and renders either JSON or human-readable text with appropriate empty-result and pagination messaging. [crates/gcode/src/commands/graph/reads.rs:438-502] |
| `imports` | function | 'imports' checks whether graph reads are available, fetches the import graph results for the given file, and prints them as either JSON paginated output or plain text names, with a “no imports found” message when the text result set is empty. [crates/gcode/src/commands/graph/reads.rs:504-539] |
| `path` | function | Resolves two symbols, clamps the requested search depth to the allowed range, computes the shortest symbol path between their IDs if both resolve, and prints the path response in the requested format. [crates/gcode/src/commands/graph/reads.rs:541-562] |
| `blast_radius` | function | 'blast_radius' resolves the target symbol, computes its dependency impact set to the specified depth via 'code_graph::blast_radius', trims the results to an optional token budget, and emits either JSON or grouped text output with any relevant hint metadata. [crates/gcode/src/commands/graph/reads.rs:564-623] |
| `graph_resolution_database_url` | function | Returns the value of the 'GCODE_POSTGRES_TEST_DATABASE_URL' environment variable as a 'String', panicking with a fixed message if the variable is unset. [crates/gcode/src/commands/graph/reads.rs:640-643] |
| `connect_graph_resolution_test_db` | function | Connects to the graph resolution PostgreSQL test database using the configured database URL, validates the runtime schema on the opened connection, and returns the 'Client'. [crates/gcode/src/commands/graph/reads.rs:645-652] |
| `unique_uuid` | function | Generates a deterministic UUIDv5 string by hashing the provided 'label' together with the current UNIX-epoch nanosecond timestamp under 'CODE_INDEX_UUID_NAMESPACE', ensuring a unique value per call. [crates/gcode/src/commands/graph/reads.rs:654-661] |
| `GraphResolutionProjectCleanup` | class | 'GraphResolutionProjectCleanup' is a struct that holds the 'database_url' and 'project_id' needed to identify and clean up graph resolution state for a specific project in a database-backed system. [crates/gcode/src/commands/graph/reads.rs:663-666] |
| `GraphResolutionProjectCleanup::new` | method | Constructs a new instance by populating 'database_url' from 'graph_resolution_database_url()' and storing 'project_id' as an owned 'String' copied from the input '&str'. [crates/gcode/src/commands/graph/reads.rs:669-674] |
| `GraphResolutionProjectCleanup::drop` | method | On drop, it attempts to open a read-write PostgreSQL connection to 'self.database_url' and, if successful, invokes 'try_cleanup_graph_resolution_project' for 'self.project_id', logging any cleanup or connection errors to stderr. [crates/gcode/src/commands/graph/reads.rs:678-689] |
| `cleanup_graph_resolution_project` | function | Calls 'try_cleanup_graph_resolution_project' with the provided 'Client' and 'project_id', then panics with '"cleanup graph resolution project"' if the cleanup fails. [crates/gcode/src/commands/graph/reads.rs:692-695] |
| `try_cleanup_graph_resolution_project` | function | Begins a PostgreSQL transaction and deletes all rows for the given 'project_id' from each 'GRAPH_RESOLUTION_CHILD_TABLES' table and from 'code_indexed_projects', then commits the transaction and returns any 'postgres::Error' encountered. [crates/gcode/src/commands/graph/reads.rs:697-711] |
| `insert_project` | function | Inserts a new row into 'code_indexed_projects' for the given 'project_id', using '/tmp/gcode-graph-resolution-{project_id}' as 'root_path', zeroing file/symbol counts and indexing duration, setting 'last_indexed_at' to 'NOW()', and panicking if the database insert fails. [crates/gcode/src/commands/graph/reads.rs:713-722] |
| `insert_file` | function | Inserts a 'code_indexed_files' record for the given project and file path, using '{project_id}:{file_path}' as the primary id and storing the provided 'symbol_count' along with hardcoded metadata and default sync/index timestamps. [crates/gcode/src/commands/graph/reads.rs:724-735] |
| `insert_symbol` | function | Inserts a Rust function symbol record into the 'code_symbols' table for the given project, file, ID, name, and starting line, hardcoding its metadata as a 'function' in 'rust' with placeholder offsets, hash, and timestamps. [crates/gcode/src/commands/graph/reads.rs:737-756] |
| `uuid_input_resolves_exact_symbol_for_active_project` | function | Verifies that resolving a symbol by UUID within the active project returns the exact inserted symbol with no suggestions, matching both its ID and display name. [crates/gcode/src/commands/graph/reads.rs:767-793] |
| `unknown_uuid_input_does_not_fall_back_to_name_resolution` | function | Verifies that resolving a UUID-shaped symbol name not present in the project returns no match and no suggestions, rather than falling back to name-based resolution. [crates/gcode/src/commands/graph/reads.rs:801-825] |
| `ambiguous_name_behavior_remains_unchanged` | function | Verifies that resolving the ambiguous symbol name 'shared_lookup' returns no single match and instead produces two suggestions containing 'src/a.rs:10' and 'src/b.rs:20'. [crates/gcode/src/commands/graph/reads.rs:833-867] |

