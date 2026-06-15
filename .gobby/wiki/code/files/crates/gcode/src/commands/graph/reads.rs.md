---
title: crates/gcode/src/commands/graph/reads.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/reads.rs
  ranges:
  - 14-20
  - 22-30
  - 32-38
  - 40-48
  - 50-73
  - 75-90
  - 92-118
  - 120-133
  - 137-158
  - 160-174
  - 176-209
  - 211-262
  - 264-316
  - 318-353
  - 355-402
  - 419-422
  - 424-431
  - 433-440
  - 442-445
  - 447-454
  - 456-469
  - 471-474
  - 476-490
  - 492-501
  - 503-514
  - 516-535
  - 546-572
  - 580-604
  - 612-646
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/reads.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

This file implements the graph-read side of `gcode`: it centralizes backend-availability hints, turns graph-read failures into empty paginated responses with optional user guidance, and provides the shared symbol-resolution and result-formatting machinery used by commands like callers, usages, imports, and blast radius. It resolves inputs either by UUID or full-text search, gates reads when graph data or symbol lookup is unavailable, and emits either JSON `PagedResponse` output or grouped plaintext. The lower half also contains test-only PostgreSQL setup and cleanup helpers plus a small suite of resolution behavior tests.
[crates/gcode/src/commands/graph/reads.rs:14-20]
[crates/gcode/src/commands/graph/reads.rs:22-30]
[crates/gcode/src/commands/graph/reads.rs:32-38]
[crates/gcode/src/commands/graph/reads.rs:40-48]
[crates/gcode/src/commands/graph/reads.rs:50-73]

## API Symbols

- `hint_for` (function) component `hint_for [function]` (`c77c4fac-f2a7-5572-8a3e-164d5de7cf72`) lines 14-20 [crates/gcode/src/commands/graph/reads.rs:14-20]
  - Signature: `fn hint_for(ctx: &Context) -> Option<String> {`
  - Purpose: Returns 'Some(GRAPH_BACKEND_HINT.to_string())' when 'ctx.falkordb' is 'None', otherwise returns 'None'. [crates/gcode/src/commands/graph/reads.rs:14-20]
- `hint_for_error` (function) component `hint_for_error [function]` (`ccb53cb3-3005-5518-a309-1baa2fb9c2fd`) lines 22-30 [crates/gcode/src/commands/graph/reads.rs:22-30]
  - Signature: `fn hint_for_error(ctx: &Context, error: &anyhow::Error) -> Option<String> {`
  - Purpose: Returns a context-derived hint string for graph-related errors, using a specific “FalkorDB configured but unreachable” message for 'GraphReadError::Unreachable' and otherwise delegating to 'hint_for(ctx)' for 'NotConfigured' or all other errors. [crates/gcode/src/commands/graph/reads.rs:22-30]
- `print_graph_hint_text` (function) component `print_graph_hint_text [function]` (`471d1cdf-3a26-5a63-8d83-6a61f1adb340`) lines 32-38 [crates/gcode/src/commands/graph/reads.rs:32-38]
  - Signature: `fn print_graph_hint_text(ctx: &Context, error: Option<&anyhow::Error>) {`
  - Purpose: Prints a 'Hint: ...' line to standard error by first deriving a context-specific hint from the provided error via 'hint_for_error', falling back to 'hint_for(ctx)', and emitting nothing if no hint is available. [crates/gcode/src/commands/graph/reads.rs:32-38]
- `graph_read_unavailable` (function) component `graph_read_unavailable [function]` (`2946cad6-db7b-5b7f-a3d1-4c5ffec3489a`) lines 40-48 [crates/gcode/src/commands/graph/reads.rs:40-48]
  - Signature: `fn graph_read_unavailable(error: &anyhow::Error) -> bool {`
  - Purpose: Returns 'true' when the 'anyhow::Error' downcasts to 'code_graph::GraphReadError' and is either 'NotConfigured' or 'Unreachable { .. }', otherwise 'false'. [crates/gcode/src/commands/graph/reads.rs:40-48]
- `empty_paged_response` (function) component `empty_paged_response [function]` (`dccfb810-0928-5a3e-b9fb-22445a82a241`) lines 50-73 [crates/gcode/src/commands/graph/reads.rs:50-73]
  - Signature: `fn empty_paged_response<T: Serialize>(`
  - Purpose: Emits an empty paginated response for the given context in either JSON, by serializing a 'PagedResponse' with 'total = 0', the supplied 'offset'/'limit', no results, and an optional hint derived from the error or context, or in text format by printing a graph hint and returning 'Ok(())'. [crates/gcode/src/commands/graph/reads.rs:50-73]
- `graph_read_or_empty` (function) component `graph_read_or_empty [function]` (`acbf7de9-663b-5fae-8383-cba38e21f58d`) lines 75-90 [crates/gcode/src/commands/graph/reads.rs:75-90]
  - Signature: `fn graph_read_or_empty<T: Serialize>(`
  - Purpose: 'graph_read_or_empty' executes 'read()', returns 'Ok(Some(value))' on success, maps graph-unavailable errors to an empty paged response via 'empty_paged_response' and returns 'Ok(None)', and propagates all other errors unchanged. [crates/gcode/src/commands/graph/reads.rs:75-90]
- `format_grouped_graph_results` (function) component `format_grouped_graph_results [function]` (`5ab8b804-fe94-55c5-8c25-f494ab365c8e`) lines 92-118 [crates/gcode/src/commands/graph/reads.rs:92-118]
  - Signature: `pub(super) fn format_grouped_graph_results<F>(results: &[GraphResult], format_line: F) -> String`
  - Purpose: Groups 'GraphResult' values by 'file_path' in sorted path order, labels empty paths as '"<unknown>"', sorts each group by 'line', 'name', 'relation', then 'distance', formats each entry with 'format_line', and joins all output lines with newlines. [crates/gcode/src/commands/graph/reads.rs:92-118]
- `resolve_symbol_with_connection` (function) component `resolve_symbol_with_connection [function]` (`9cacd81a-39c9-56e8-b693-fba43062a725`) lines 120-133 [crates/gcode/src/commands/graph/reads.rs:120-133]
  - Signature: `fn resolve_symbol_with_connection(`
  - Purpose: Resolves a graph symbol for a given project by treating 'input' as a UUID and delegating to 'resolve_graph_symbol_by_id' when parsing succeeds, otherwise falling back to full-text symbol resolution via 'fts::resolve_graph_symbol', and returns the resolved symbol plus any associated candidate strings. [crates/gcode/src/commands/graph/reads.rs:120-133]
- `resolve_symbol` (function) component `resolve_symbol [function]` (`e055ceaf-5ae2-56a1-88a0-5a1be654af9a`) lines 137-158 [crates/gcode/src/commands/graph/reads.rs:137-158]
  - Signature: `fn resolve_symbol(ctx: &Context, input: &str) -> anyhow::Result<Option<ResolvedGraphSymbol>> {`
  - Purpose: Attempts to open a read-only database connection, resolves 'input' to a graph symbol for 'ctx.project_id' via 'resolve_symbol_with_connection', logs an error or ambiguity message when no unique match is found, and returns the resolved symbol or 'None'. [crates/gcode/src/commands/graph/reads.rs:137-158]
- `resolve_symbol_or_empty_response` (function) component `resolve_symbol_or_empty_response [function]` (`9d5664b7-3f0a-5321-98ee-9c7152968aef`) lines 160-174 [crates/gcode/src/commands/graph/reads.rs:160-174]
  - Signature: `fn resolve_symbol_or_empty_response(`
  - Purpose: Calls 'resolve_symbol(ctx, input)' and returns the resolved symbol on success, or generates an empty paged 'GraphResult' response via 'empty_paged_response' and returns 'None' when no symbol is found. [crates/gcode/src/commands/graph/reads.rs:160-174]
- `read_paged_symbol_graph_results` (function) component `read_paged_symbol_graph_results [function]` (`073de07c-31ba-547c-8306-03fe619f12ce`) lines 176-209 [crates/gcode/src/commands/graph/reads.rs:176-209]
  - Signature: `fn read_paged_symbol_graph_results(`
  - Purpose: Checks graph-read and symbol-resolution preconditions, resolves the symbol, fetches the total match count and paginated 'GraphResult' list for that symbol, and returns 'Ok(None)' if any empty-response gate triggers or 'Ok(Some((symbol, total, results)))' on success. [crates/gcode/src/commands/graph/reads.rs:176-209]
- `callers` (function) component `callers [function]` (`097b1a01-832f-549f-9c7b-f6951d1a8b56`) lines 211-262 [crates/gcode/src/commands/graph/reads.rs:211-262]
  - Signature: `pub fn callers(`
  - Purpose: Paginates and emits the callers of a symbol by querying the code graph, returning either a JSON 'PagedResponse' or grouped text output with no-results and continuation hints. [crates/gcode/src/commands/graph/reads.rs:211-262]
- `usages` (function) component `usages [function]` (`d5a3ca78-49a4-50b1-b73d-3a95b85a7156`) lines 264-316 [crates/gcode/src/commands/graph/reads.rs:264-316]
  - Signature: `pub fn usages(`
  - Purpose: Queries a code graph for all usages of a specified symbol and outputs paginated results in either JSON or formatted text format. [crates/gcode/src/commands/graph/reads.rs:264-316]
- `imports` (function) component `imports [function]` (`514d6604-7a12-5269-b45a-dc77747a769d`) lines 318-353 [crates/gcode/src/commands/graph/reads.rs:318-353]
  - Signature: `pub fn imports(ctx: &Context, file: &str, format: Format) -> anyhow::Result<()> {`
  - Purpose: # Summary

Fetches imports for a specified file from a code graph and outputs the results as either a paginated JSON response or plaintext list. [crates/gcode/src/commands/graph/reads.rs:318-353]
- `blast_radius` (function) component `blast_radius [function]` (`e51045af-1c30-504b-a711-b8ab64f08e03`) lines 355-402 [crates/gcode/src/commands/graph/reads.rs:355-402]
  - Signature: `pub fn blast_radius(`
  - Purpose: Resolves a target symbol in the code graph and outputs all code elements affected by changes to that symbol within a specified dependency depth, formatted as either JSON or annotated text with distance metrics. [crates/gcode/src/commands/graph/reads.rs:355-402]
- `graph_resolution_database_url` (function) component `graph_resolution_database_url [function]` (`59948c24-5dfd-5eb7-a5a3-f9a57bf054b8`) lines 419-422 [crates/gcode/src/commands/graph/reads.rs:419-422]
  - Signature: `fn graph_resolution_database_url() -> String {`
  - Purpose: Returns the value of the 'GCODE_POSTGRES_TEST_DATABASE_URL' environment variable as a 'String', panicking with a fixed message if the variable is not set. [crates/gcode/src/commands/graph/reads.rs:419-422]
- `connect_graph_resolution_test_db` (function) component `connect_graph_resolution_test_db [function]` (`b36b364f-b9cf-5d04-a9d3-51567ffaa393`) lines 424-431 [crates/gcode/src/commands/graph/reads.rs:424-431]
  - Signature: `fn connect_graph_resolution_test_db() -> Client {`
  - Purpose: Connects to the graph resolution PostgreSQL test database using the resolved database URL, validates the runtime schema on the connection, and returns the read-write 'Client'. [crates/gcode/src/commands/graph/reads.rs:424-431]
- `unique_uuid` (function) component `unique_uuid [function]` (`e6475e3f-066b-50f9-83e6-657e73cdc6c6`) lines 433-440 [crates/gcode/src/commands/graph/reads.rs:433-440]
  - Signature: `fn unique_uuid(label: &str) -> String {`
  - Purpose: Generates a deterministic UUIDv5 string from a namespace constant and a key composed of 'graph-resolution-test', the provided 'label', and the current Unix-time nanoseconds, ensuring uniqueness across calls. [crates/gcode/src/commands/graph/reads.rs:433-440]
- `GraphResolutionProjectCleanup` (class) component `GraphResolutionProjectCleanup [class]` (`18387b32-1052-51ac-ac26-f081685bf55a`) lines 442-445 [crates/gcode/src/commands/graph/reads.rs:442-445]
  - Signature: `struct GraphResolutionProjectCleanup {`
  - Purpose: 'GraphResolutionProjectCleanup' is a data structure that holds a 'database_url' and 'project_id' identifying the database-backed project target for a cleanup operation. [crates/gcode/src/commands/graph/reads.rs:442-445]
- `GraphResolutionProjectCleanup` (class) component `GraphResolutionProjectCleanup [class]` (`b1b1ee2f-b8b0-5004-a3e5-1726a6a24f29`) lines 447-454 [crates/gcode/src/commands/graph/reads.rs:447-454]
  - Signature: `impl GraphResolutionProjectCleanup {`
  - Purpose: 'GraphResolutionProjectCleanup' is a constructor-only helper that captures a 'project_id' and the graph resolution database URL for later project cleanup operations. [crates/gcode/src/commands/graph/reads.rs:447-454]
- `GraphResolutionProjectCleanup.new` (method) component `GraphResolutionProjectCleanup.new [method]` (`27d7bda8-e0ec-506f-97a8-12381bc44b0e`) lines 448-453 [crates/gcode/src/commands/graph/reads.rs:448-453]
  - Signature: `fn new(project_id: &str) -> Self {`
  - Purpose: Constructs and returns a new instance initialized with 'database_url' from 'graph_resolution_database_url()' and 'project_id' cloned from the provided '&str'. [crates/gcode/src/commands/graph/reads.rs:448-453]
- `GraphResolutionProjectCleanup` (class) component `GraphResolutionProjectCleanup [class]` (`d64269fd-3d64-550c-825c-730f2fc1270d`) lines 456-469 [crates/gcode/src/commands/graph/reads.rs:456-469]
  - Signature: `impl Drop for GraphResolutionProjectCleanup {`
  - Purpose: 'GraphResolutionProjectCleanup' is a Rust 'Drop' guard that, when destroyed, opens a read-write PostgreSQL connection using its stored 'database_url' and attempts to clean up the associated 'project_id' via 'try_cleanup_graph_resolution_project', emitting errors to 'stderr' if either the connection or cleanup fails. [crates/gcode/src/commands/graph/reads.rs:456-469]
- `GraphResolutionProjectCleanup.drop` (method) component `GraphResolutionProjectCleanup.drop [method]` (`3e037ddf-301a-5d33-8762-fadad06ccd4f`) lines 457-468 [crates/gcode/src/commands/graph/reads.rs:457-468]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Attempts to open a read-write PostgreSQL connection using 'database_url' and, on success, runs 'try_cleanup_graph_resolution_project' for 'project_id', logging any cleanup or connection errors to stderr without panicking. [crates/gcode/src/commands/graph/reads.rs:457-468]
- `cleanup_graph_resolution_project` (function) component `cleanup_graph_resolution_project [function]` (`4d854215-1cde-583b-b7a4-e833897eca0e`) lines 471-474 [crates/gcode/src/commands/graph/reads.rs:471-474]
  - Signature: `fn cleanup_graph_resolution_project(conn: &mut Client, project_id: &str) {`
  - Purpose: Executes the fallible 'try_cleanup_graph_resolution_project' operation and panics if it returns an error. [crates/gcode/src/commands/graph/reads.rs:471-474]
- `try_cleanup_graph_resolution_project` (function) component `try_cleanup_graph_resolution_project [function]` (`51dfaae5-102c-51ac-8069-eed715c6b054`) lines 476-490 [crates/gcode/src/commands/graph/reads.rs:476-490]
  - Signature: `fn try_cleanup_graph_resolution_project(`
  - Purpose: Begins a PostgreSQL transaction and deletes all rows for the given 'project_id' from each 'GRAPH_RESOLUTION_CHILD_TABLES' table and then from 'code_indexed_projects', committing the transaction if all deletes succeed. [crates/gcode/src/commands/graph/reads.rs:476-490]
- `insert_project` (function) component `insert_project [function]` (`341d23ea-9423-5cfb-8d7c-f1ad44f093cd`) lines 492-501 [crates/gcode/src/commands/graph/reads.rs:492-501]
  - Signature: `fn insert_project(conn: &mut Client, project_id: &str) {`
  - Purpose: Inserts a 'code_indexed_projects' row for the given 'project_id' using a derived '/tmp/gcode-graph-resolution-{project_id}' root path, zeroing file/symbol counts and index duration, setting 'last_indexed_at' to 'NOW()', and panicking on insert failure. [crates/gcode/src/commands/graph/reads.rs:492-501]
- `insert_file` (function) component `insert_file [function]` (`4ba4991e-2360-5330-9915-272f1cca68ef`) lines 503-514 [crates/gcode/src/commands/graph/reads.rs:503-514]
  - Signature: `fn insert_file(conn: &mut Client, project_id: &str, file_path: &str, symbol_count: i32) {`
  - Purpose: Inserts a 'code_indexed_files' row for the given 'project_id' and 'file_path' with 'id = "{project_id}:{file_path}"', hard-coded 'language = 'rust'' and 'content_hash = 'hash'', the supplied 'symbol_count', default byte size and sync fields, 'indexed_at = NOW()', and panics if the database write fails. [crates/gcode/src/commands/graph/reads.rs:503-514]
- `insert_symbol` (function) component `insert_symbol [function]` (`b2f5cf93-e7c6-5c8a-ba42-407285c5e862`) lines 516-535 [crates/gcode/src/commands/graph/reads.rs:516-535]
  - Signature: `fn insert_symbol(`
  - Purpose: Inserts a Rust function symbol record into the 'code_symbols' table for the given project, file, id, name, and starting line, using fixed metadata ('kind='function'', 'language='rust'', placeholder hash/content fields, and current timestamps) and panicking if the database insert fails. [crates/gcode/src/commands/graph/reads.rs:516-535]
- `uuid_input_resolves_exact_symbol_for_active_project` (function) component `uuid_input_resolves_exact_symbol_for_active_project [function]` (`436e92eb-f8d0-5124-b88c-b8b470021ac9`) lines 546-572 [crates/gcode/src/commands/graph/reads.rs:546-572]
  - Signature: `fn uuid_input_resolves_exact_symbol_for_active_project() {`
  - Purpose: Verifies that resolving a UUID symbol input within the active project returns the exact inserted symbol record, with no suggestions, and preserves its id and display name. [crates/gcode/src/commands/graph/reads.rs:546-572]
- `unknown_uuid_input_does_not_fall_back_to_name_resolution` (function) component `unknown_uuid_input_does_not_fall_back_to_name_resolution [function]` (`8451c1b5-5c29-5542-8adb-ae0fd59ab2ac`) lines 580-604 [crates/gcode/src/commands/graph/reads.rs:580-604]
  - Signature: `fn unknown_uuid_input_does_not_fall_back_to_name_resolution() {`
  - Purpose: Verifies that resolving a UUID-shaped symbol name that is not a known UUID does not fall back to name-based lookup, returning no resolved symbol and no suggestions. [crates/gcode/src/commands/graph/reads.rs:580-604]
- `ambiguous_name_behavior_remains_unchanged` (function) component `ambiguous_name_behavior_remains_unchanged [function]` (`0898e987-94f4-5adc-90e8-c49c29878b76`) lines 612-646 [crates/gcode/src/commands/graph/reads.rs:612-646]
  - Signature: `fn ambiguous_name_behavior_remains_unchanged() {`
  - Purpose: Verifies that resolving the ambiguous symbol name 'shared_lookup' returns no single match and instead yields two suggestions identifying the distinct definitions at 'src/a.rs:10' and 'src/b.rs:20'. [crates/gcode/src/commands/graph/reads.rs:612-646]

