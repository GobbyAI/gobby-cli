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
  - 419-421
  - 423-440
  - 442-449
  - 451-454
  - 456-464
  - 457-463
  - 466-479
  - 467-478
  - 481-484
  - 486-500
  - 502-511
  - 513-524
  - 526-545
  - 552-580
  - 584-610
  - 614-650
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/reads.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

`crates/gcode/src/commands/graph/reads.rs` exposes 31 indexed API symbols.
[crates/gcode/src/commands/graph/reads.rs:14-20]
[crates/gcode/src/commands/graph/reads.rs:22-30]
[crates/gcode/src/commands/graph/reads.rs:32-38]
[crates/gcode/src/commands/graph/reads.rs:40-48]
[crates/gcode/src/commands/graph/reads.rs:50-73]

## API Symbols

- `hint_for` (function) component `hint_for [function]` (`c77c4fac-f2a7-5572-8a3e-164d5de7cf72`) lines 14-20 [crates/gcode/src/commands/graph/reads.rs:14-20]
  - Signature: `fn hint_for(ctx: &Context) -> Option<String> {`
  - Purpose: Indexed function `hint_for` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:14-20]
- `hint_for_error` (function) component `hint_for_error [function]` (`ccb53cb3-3005-5518-a309-1baa2fb9c2fd`) lines 22-30 [crates/gcode/src/commands/graph/reads.rs:22-30]
  - Signature: `fn hint_for_error(ctx: &Context, error: &anyhow::Error) -> Option<String> {`
  - Purpose: Indexed function `hint_for_error` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:22-30]
- `print_graph_hint_text` (function) component `print_graph_hint_text [function]` (`471d1cdf-3a26-5a63-8d83-6a61f1adb340`) lines 32-38 [crates/gcode/src/commands/graph/reads.rs:32-38]
  - Signature: `fn print_graph_hint_text(ctx: &Context, error: Option<&anyhow::Error>) {`
  - Purpose: Indexed function `print_graph_hint_text` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:32-38]
- `graph_read_unavailable` (function) component `graph_read_unavailable [function]` (`2946cad6-db7b-5b7f-a3d1-4c5ffec3489a`) lines 40-48 [crates/gcode/src/commands/graph/reads.rs:40-48]
  - Signature: `fn graph_read_unavailable(error: &anyhow::Error) -> bool {`
  - Purpose: Indexed function `graph_read_unavailable` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:40-48]
- `empty_paged_response` (function) component `empty_paged_response [function]` (`dccfb810-0928-5a3e-b9fb-22445a82a241`) lines 50-73 [crates/gcode/src/commands/graph/reads.rs:50-73]
  - Signature: `fn empty_paged_response<T: Serialize>(`
  - Purpose: Indexed function `empty_paged_response` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:50-73]
- `graph_read_or_empty` (function) component `graph_read_or_empty [function]` (`acbf7de9-663b-5fae-8383-cba38e21f58d`) lines 75-90 [crates/gcode/src/commands/graph/reads.rs:75-90]
  - Signature: `fn graph_read_or_empty<T: Serialize>(`
  - Purpose: Indexed function `graph_read_or_empty` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:75-90]
- `format_grouped_graph_results` (function) component `format_grouped_graph_results [function]` (`5ab8b804-fe94-55c5-8c25-f494ab365c8e`) lines 92-118 [crates/gcode/src/commands/graph/reads.rs:92-118]
  - Signature: `pub(super) fn format_grouped_graph_results<F>(results: &[GraphResult], format_line: F) -> String`
  - Purpose: Indexed function `format_grouped_graph_results` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:92-118]
- `resolve_symbol_with_connection` (function) component `resolve_symbol_with_connection [function]` (`9cacd81a-39c9-56e8-b693-fba43062a725`) lines 120-133 [crates/gcode/src/commands/graph/reads.rs:120-133]
  - Signature: `fn resolve_symbol_with_connection(`
  - Purpose: Indexed function `resolve_symbol_with_connection` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:120-133]
- `resolve_symbol` (function) component `resolve_symbol [function]` (`e055ceaf-5ae2-56a1-88a0-5a1be654af9a`) lines 137-158 [crates/gcode/src/commands/graph/reads.rs:137-158]
  - Signature: `fn resolve_symbol(ctx: &Context, input: &str) -> anyhow::Result<Option<ResolvedGraphSymbol>> {`
  - Purpose: Indexed function `resolve_symbol` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:137-158]
- `resolve_symbol_or_empty_response` (function) component `resolve_symbol_or_empty_response [function]` (`9d5664b7-3f0a-5321-98ee-9c7152968aef`) lines 160-174 [crates/gcode/src/commands/graph/reads.rs:160-174]
  - Signature: `fn resolve_symbol_or_empty_response(`
  - Purpose: Indexed function `resolve_symbol_or_empty_response` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:160-174]
- `read_paged_symbol_graph_results` (function) component `read_paged_symbol_graph_results [function]` (`073de07c-31ba-547c-8306-03fe619f12ce`) lines 176-209 [crates/gcode/src/commands/graph/reads.rs:176-209]
  - Signature: `fn read_paged_symbol_graph_results(`
  - Purpose: Indexed function `read_paged_symbol_graph_results` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:176-209]
- `callers` (function) component `callers [function]` (`097b1a01-832f-549f-9c7b-f6951d1a8b56`) lines 211-262 [crates/gcode/src/commands/graph/reads.rs:211-262]
  - Signature: `pub fn callers(`
  - Purpose: Indexed function `callers` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:211-262]
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
- `graph_resolution_database_url` (function) component `graph_resolution_database_url [function]` (`59948c24-5dfd-5eb7-a5a3-f9a57bf054b8`) lines 419-421 [crates/gcode/src/commands/graph/reads.rs:419-421]
  - Signature: `fn graph_resolution_database_url() -> Option<String> {`
  - Purpose: Retrieves the `GCODE_POSTGRES_TEST_DATABASE_URL` environment variable and returns it as an `Option<String>`, or `None` if the variable is not set. [crates/gcode/src/commands/graph/reads.rs:419-421]
- `connect_graph_resolution_test_db` (function) component `connect_graph_resolution_test_db [function]` (`f913e0e1-17df-5b79-89f6-7058a398ba5f`) lines 423-440 [crates/gcode/src/commands/graph/reads.rs:423-440]
  - Signature: `fn connect_graph_resolution_test_db() -> Option<Client> {`
  - Purpose: Connects to and validates a PostgreSQL read-write client for graph resolution testing, returning `Some(Client)` on success or `None` if connection or schema validation fails. [crates/gcode/src/commands/graph/reads.rs:423-440]
- `unique_uuid` (function) component `unique_uuid [function]` (`3bb847cb-17df-57ca-947e-a3e2f0dbd974`) lines 442-449 [crates/gcode/src/commands/graph/reads.rs:442-449]
  - Signature: `fn unique_uuid(label: &str) -> String {`
  - Purpose: Generates a deterministic UUID v5 from a composite key combining the provided label with the current nanosecond timestamp using the CODE_INDEX_UUID_NAMESPACE identifier. [crates/gcode/src/commands/graph/reads.rs:442-449]
- `GraphResolutionProjectCleanup` (class) component `GraphResolutionProjectCleanup [class]` (`699c1131-ee3f-51eb-8dec-1d131af0e6f8`) lines 451-454 [crates/gcode/src/commands/graph/reads.rs:451-454]
  - Signature: `struct GraphResolutionProjectCleanup {`
  - Purpose: Indexed class `GraphResolutionProjectCleanup` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:451-454]
- `GraphResolutionProjectCleanup` (class) component `GraphResolutionProjectCleanup [class]` (`88a90fed-bdab-5022-8a80-0e9aada1e621`) lines 456-464 [crates/gcode/src/commands/graph/reads.rs:456-464]
  - Signature: `impl GraphResolutionProjectCleanup {`
  - Purpose: Implements a constructor for `GraphResolutionProjectCleanup` that initializes a graph resolution database connection URL and project identifier. [crates/gcode/src/commands/graph/reads.rs:456-464]
- `GraphResolutionProjectCleanup.new` (method) component `GraphResolutionProjectCleanup.new [method]` (`b8a6659c-dee5-505b-b865-989603f26640`) lines 457-463 [crates/gcode/src/commands/graph/reads.rs:457-463]
  - Signature: `fn new(project_id: &str) -> Self {`
  - Purpose: Constructs a new instance by resolving the graph resolution database URL from configuration (panicking if unavailable) and converting the provided project_id reference to an owned String. [crates/gcode/src/commands/graph/reads.rs:457-463]
- `GraphResolutionProjectCleanup` (class) component `GraphResolutionProjectCleanup [class]` (`5bf38ccc-ca94-562a-9f95-023ee40d2626`) lines 466-479 [crates/gcode/src/commands/graph/reads.rs:466-479]
  - Signature: `impl Drop for GraphResolutionProjectCleanup {`
  - Purpose: Implements Drop to attempt cleanup of a graph resolution project in PostgreSQL when the struct is deallocated, with non-fatal error logging to stderr for connection or cleanup failures. [crates/gcode/src/commands/graph/reads.rs:466-479]
- `GraphResolutionProjectCleanup.drop` (method) component `GraphResolutionProjectCleanup.drop [method]` (`5ad02bec-dda6-56fd-a30c-2a5c0a3d7c42`) lines 467-478 [crates/gcode/src/commands/graph/reads.rs:467-478]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Indexed method `GraphResolutionProjectCleanup.drop` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:467-478]
- `cleanup_graph_resolution_project` (function) component `cleanup_graph_resolution_project [function]` (`7b2f6758-f4e7-5192-a556-a04286fdc3df`) lines 481-484 [crates/gcode/src/commands/graph/reads.rs:481-484]
  - Signature: `fn cleanup_graph_resolution_project(conn: &mut Client, project_id: &str) {`
  - Purpose: Indexed function `cleanup_graph_resolution_project` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:481-484]
- `try_cleanup_graph_resolution_project` (function) component `try_cleanup_graph_resolution_project [function]` (`86cc4a2f-6f66-548b-9478-38eb6d868ff5`) lines 486-500 [crates/gcode/src/commands/graph/reads.rs:486-500]
  - Signature: `fn try_cleanup_graph_resolution_project(`
  - Purpose: Indexed function `try_cleanup_graph_resolution_project` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:486-500]
- `insert_project` (function) component `insert_project [function]` (`caad8438-a9d2-5a5b-9752-3f39b8f5be95`) lines 502-511 [crates/gcode/src/commands/graph/reads.rs:502-511]
  - Signature: `fn insert_project(conn: &mut Client, project_id: &str) {`
  - Purpose: Indexed function `insert_project` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:502-511]
- `insert_file` (function) component `insert_file [function]` (`ffacd6c3-c856-5a94-990b-d614a99d16dc`) lines 513-524 [crates/gcode/src/commands/graph/reads.rs:513-524]
  - Signature: `fn insert_file(conn: &mut Client, project_id: &str, file_path: &str, symbol_count: i32) {`
  - Purpose: Indexed function `insert_file` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:513-524]
- `insert_symbol` (function) component `insert_symbol [function]` (`ddb67797-13a4-582f-ac7a-1337c1425a04`) lines 526-545 [crates/gcode/src/commands/graph/reads.rs:526-545]
  - Signature: `fn insert_symbol(`
  - Purpose: Indexed function `insert_symbol` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:526-545]
- `uuid_input_resolves_exact_symbol_for_active_project` (function) component `uuid_input_resolves_exact_symbol_for_active_project [function]` (`4cc7bd06-32aa-5577-a0a6-bebf3f886481`) lines 552-580 [crates/gcode/src/commands/graph/reads.rs:552-580]
  - Signature: `fn uuid_input_resolves_exact_symbol_for_active_project() {`
  - Purpose: Indexed function `uuid_input_resolves_exact_symbol_for_active_project` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:552-580]
- `unknown_uuid_input_does_not_fall_back_to_name_resolution` (function) component `unknown_uuid_input_does_not_fall_back_to_name_resolution [function]` (`4aefc65d-bf64-514b-acec-4a41b53fed68`) lines 584-610 [crates/gcode/src/commands/graph/reads.rs:584-610]
  - Signature: `fn unknown_uuid_input_does_not_fall_back_to_name_resolution() {`
  - Purpose: Indexed function `unknown_uuid_input_does_not_fall_back_to_name_resolution` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:584-610]
- `ambiguous_name_behavior_remains_unchanged` (function) component `ambiguous_name_behavior_remains_unchanged [function]` (`5cbe2db9-a160-5ece-95ae-bda37698fc64`) lines 614-650 [crates/gcode/src/commands/graph/reads.rs:614-650]
  - Signature: `fn ambiguous_name_behavior_remains_unchanged() {`
  - Purpose: Indexed function `ambiguous_name_behavior_remains_unchanged` in `crates/gcode/src/commands/graph/reads.rs`. [crates/gcode/src/commands/graph/reads.rs:614-650]

