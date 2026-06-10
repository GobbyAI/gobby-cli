---
title: crates/gcode/src/commands/graph/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/tests.rs
  ranges:
  - 16-30
  - 33-39
  - 42-50
  - 53-89
  - 92-106
  - 109-111
  - 113-132
  - 114-131
  - 135-158
  - 161-170
  - 173-189
  - 192-204
  - 207-219
  - 222-235
  - 238-253
  - 256-272
  - 275-292
  - 295-312
  - 315-373
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/tests.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

`crates/gcode/src/commands/graph/tests.rs` exposes 19 indexed API symbols.
[crates/gcode/src/commands/graph/tests.rs:16-30]
[crates/gcode/src/commands/graph/tests.rs:33-39]
[crates/gcode/src/commands/graph/tests.rs:42-50]
[crates/gcode/src/commands/graph/tests.rs:53-89]
[crates/gcode/src/commands/graph/tests.rs:92-106]
[crates/gcode/src/commands/graph/tests.rs:109-111]
[crates/gcode/src/commands/graph/tests.rs:113-132]
[crates/gcode/src/commands/graph/tests.rs:114-131]
[crates/gcode/src/commands/graph/tests.rs:135-158]
[crates/gcode/src/commands/graph/tests.rs:161-170]
[crates/gcode/src/commands/graph/tests.rs:173-189]
[crates/gcode/src/commands/graph/tests.rs:192-204]
[crates/gcode/src/commands/graph/tests.rs:207-219]
[crates/gcode/src/commands/graph/tests.rs:222-235]
[crates/gcode/src/commands/graph/tests.rs:238-253]
[crates/gcode/src/commands/graph/tests.rs:256-272]
[crates/gcode/src/commands/graph/tests.rs:275-292]
[crates/gcode/src/commands/graph/tests.rs:295-312]
[crates/gcode/src/commands/graph/tests.rs:315-373]

## API Symbols

- `make_ctx_no_falkordb` (function) component `make_ctx_no_falkordb [function]` (`52fdb0e8-6610-5b5d-9a9d-86aac8eaed49`) lines 16-30 [crates/gcode/src/commands/graph/tests.rs:16-30]
  - Signature: `fn make_ctx_no_falkordb() -> Context {`
  - Purpose: Constructs a test `Context` struct with nonexistent database paths and all vector database integrations (falkordb, qdrant, embedding) disabled by setting them to `None`. [crates/gcode/src/commands/graph/tests.rs:16-30]
- `graph_reads_degrade_when_falkor_missing` (function) component `graph_reads_degrade_when_falkor_missing [function]` (`3c3a6d7e-5e30-57d5-9fd5-46c2185bb40e`) lines 33-39 [crates/gcode/src/commands/graph/tests.rs:33-39]
  - Signature: `fn graph_reads_degrade_when_falkor_missing() {`
  - Purpose: Tests that the `imports` function successfully completes when FalkorDB is unavailable, verifying graceful degradation in its absence. [crates/gcode/src/commands/graph/tests.rs:33-39]
- `report_text_uses_markdown_output` (function) component `report_text_uses_markdown_output [function]` (`7198e6e3-e89e-53e5-9ead-46c268c9ade4`) lines 42-50 [crates/gcode/src/commands/graph/tests.rs:42-50]
  - Signature: `fn report_text_uses_markdown_output() {`
  - Purpose: Tests that `format_report_text` produces markdown-formatted output containing a top-level header and project identifier metadata. [crates/gcode/src/commands/graph/tests.rs:42-50]
- `graph_text_groups_by_file_and_sorts_entries` (function) component `graph_text_groups_by_file_and_sorts_entries [function]` (`040301e3-6066-5889-8821-fef23433b0b5`) lines 53-89 [crates/gcode/src/commands/graph/tests.rs:53-89]
  - Signature: `fn graph_text_groups_by_file_and_sorts_entries() {`
  - Purpose: Tests that `format_grouped_graph_results` groups `GraphResult` entries by `file_path` and sorts entries within each group by `line` number in ascending order. [crates/gcode/src/commands/graph/tests.rs:53-89]
- `report_requires_graph_service` (function) component `report_requires_graph_service [function]` (`ee9e8cd2-e12b-5432-a691-32dcbe289f4e`) lines 92-106 [crates/gcode/src/commands/graph/tests.rs:92-106]
  - Signature: `fn report_requires_graph_service() {`
  - Purpose: This test asserts that the `report()` function fails with a `ProjectGraphReportError::GraphServiceNotConfigured` error when the FalkorDB graph service is not configured. [crates/gcode/src/commands/graph/tests.rs:92-106]
- `SpyLifecycleBackend` (class) component `SpyLifecycleBackend [class]` (`a7462ddc-fb26-5a29-93b7-e9062feb08e1`) lines 109-111 [crates/gcode/src/commands/graph/tests.rs:109-111]
  - Signature: `struct SpyLifecycleBackend {`
  - Purpose: SpyLifecycleBackend is a struct that collects GraphLifecycleAction events in an interior-mutable RefCell-wrapped vector for introspection and testing. [crates/gcode/src/commands/graph/tests.rs:109-111]
- `SpyLifecycleBackend` (class) component `SpyLifecycleBackend [class]` (`8b89641a-4224-5586-8024-522b59f61dd3`) lines 113-132 [crates/gcode/src/commands/graph/tests.rs:113-132]
  - Signature: `impl super::lifecycle::LifecycleBackend for SpyLifecycleBackend {`
  - Purpose: SpyLifecycleBackend is a test spy implementation of the LifecycleBackend trait that records GraphLifecycleAction invocations into an internal collection and returns deterministic mock GraphLifecycleOutput responses. [crates/gcode/src/commands/graph/tests.rs:113-132]
- `SpyLifecycleBackend.run` (method) component `SpyLifecycleBackend.run [method]` (`1228ce2a-d619-5e71-8ea1-0d735c0e9120`) lines 114-131 [crates/gcode/src/commands/graph/tests.rs:114-131]
  - Signature: `fn run(`
  - Purpose: Records a `GraphLifecycleAction` to an internal buffer and returns a `GraphLifecycleOutput` containing the action, project ID, and a JSON payload documenting the lifecycle event. [crates/gcode/src/commands/graph/tests.rs:114-131]
- `graph_lifecycle_commands_dispatch_to_core_backend` (function) component `graph_lifecycle_commands_dispatch_to_core_backend [function]` (`c00eb613-66b3-552d-aa21-54fb5443e8ce`) lines 135-158 [crates/gcode/src/commands/graph/tests.rs:135-158]
  - Signature: `fn graph_lifecycle_commands_dispatch_to_core_backend() {`
  - Purpose: Verifies that `Clear` and `Rebuild` graph lifecycle actions are correctly dispatched to a spy backend and recorded in the expected sequence. [crates/gcode/src/commands/graph/tests.rs:135-158]
- `missing_project_sync_error_has_typed_payload` (function) component `missing_project_sync_error_has_typed_payload [function]` (`f1b08e81-1850-58b0-aca0-ef21225c8b6c`) lines 161-170 [crates/gcode/src/commands/graph/tests.rs:161-170]
  - Signature: `fn missing_project_sync_error_has_typed_payload() {`
  - Purpose: This test verifies that a `GraphSyncContractError` generated for an unindexed project contains the expected exit code and typed payload fields (project_id, file_path, status, reason). [crates/gcode/src/commands/graph/tests.rs:161-170]
- `missing_file_sync_error_and_skip_payloads_are_typed` (function) component `missing_file_sync_error_and_skip_payloads_are_typed [function]` (`38a24efd-2bcd-51ec-8037-cf812200fd7f`) lines 173-189 [crates/gcode/src/commands/graph/tests.rs:173-189]
  - Signature: `fn missing_file_sync_error_and_skip_payloads_are_typed() {`
  - Purpose: This test function validates that `GraphSyncContractError::indexed_file_not_found` and its corresponding skipped payload are properly typed, asserting correct exit codes and matching JSON structures for a missing indexed file scenario. [crates/gcode/src/commands/graph/tests.rs:173-189]
- `test_build_lifecycle_url_clear_uses_project_id_query` (function) component `test_build_lifecycle_url_clear_uses_project_id_query [function]` (`f93f458f-8d57-5a7d-8d24-585dc5e362ab`) lines 192-204 [crates/gcode/src/commands/graph/tests.rs:192-204]
  - Signature: `fn test_build_lifecycle_url_clear_uses_project_id_query() {`
  - Purpose: This test verifies that `build_lifecycle_url` correctly constructs a code-graph clear-action API endpoint URL with the project ID as a query parameter. [crates/gcode/src/commands/graph/tests.rs:192-204]
- `test_build_lifecycle_url_rebuild_uses_project_id_query` (function) component `test_build_lifecycle_url_rebuild_uses_project_id_query [function]` (`8945eca6-45cd-57dc-8977-2d89320dc732`) lines 207-219 [crates/gcode/src/commands/graph/tests.rs:207-219]
  - Signature: `fn test_build_lifecycle_url_rebuild_uses_project_id_query() {`
  - Purpose: Tests that `build_lifecycle_url` correctly constructs a rebuild lifecycle URL with the project ID as a query parameter. [crates/gcode/src/commands/graph/tests.rs:207-219]
- `test_require_daemon_url_errors_when_missing` (function) component `test_require_daemon_url_errors_when_missing [function]` (`7fdd8f5e-235e-5645-96fb-0ef7d2ece101`) lines 222-235 [crates/gcode/src/commands/graph/tests.rs:222-235]
  - Signature: `fn test_require_daemon_url_errors_when_missing() {`
  - Purpose: This test validates that `code_graph::require_daemon_url()` returns an error containing "Gobby daemon URL is not configured" and "gcode graph clear" when invoked with `None` and `GraphLifecycleAction::Clear`. [crates/gcode/src/commands/graph/tests.rs:222-235]
- `test_format_http_error_includes_status_and_body` (function) component `test_format_http_error_includes_status_and_body [function]` (`d65de84a-82a5-590d-a6e1-db0e655e9d99`) lines 238-253 [crates/gcode/src/commands/graph/tests.rs:238-253]
  - Signature: `fn test_format_http_error_includes_status_and_body() {`
  - Purpose: This test verifies that `code_graph::format_http_error()` includes both the HTTP status code (502) and the response body text in the formatted error message. [crates/gcode/src/commands/graph/tests.rs:238-253]
- `test_parse_success_payload_fails_on_invalid_json` (function) component `test_parse_success_payload_fails_on_invalid_json [function]` (`5a12d2a5-0e4c-5e16-adf8-744f5c4eb38d`) lines 256-272 [crates/gcode/src/commands/graph/tests.rs:256-272]
  - Signature: `fn test_parse_success_payload_fails_on_invalid_json() {`
  - Purpose: Asserts that `parse_success_payload` fails with an error containing both "invalid JSON" and "HTTP 200 OK" when passed non-JSON content. [crates/gcode/src/commands/graph/tests.rs:256-272]
- `test_format_success_text_prefers_message_field` (function) component `test_format_success_text_prefers_message_field [function]` (`992fa618-8cac-57dd-a599-537ac4a5916b`) lines 275-292 [crates/gcode/src/commands/graph/tests.rs:275-292]
  - Signature: `fn test_format_success_text_prefers_message_field() {`
  - Purpose: This test asserts that `format_success_text` incorporates the `message` field from a `GraphLifecycleOutput` payload into the formatted output text for a `Clear` action. [crates/gcode/src/commands/graph/tests.rs:275-292]
- `test_format_success_text_falls_back_to_compact_json` (function) component `test_format_success_text_falls_back_to_compact_json [function]` (`72717bc6-fd55-5354-af25-e0bdf6805aab`) lines 295-312 [crates/gcode/src/commands/graph/tests.rs:295-312]
  - Signature: `fn test_format_success_text_falls_back_to_compact_json() {`
  - Purpose: Verifies that `format_success_text` produces a properly formatted success message containing the rebuild action, project ID, and compact JSON payload for a completed graph lifecycle operation. [crates/gcode/src/commands/graph/tests.rs:295-312]
- `top_level_read_commands_preserve_json_shape` (function) component `top_level_read_commands_preserve_json_shape [function]` (`2d4644fa-5bb0-5a24-8eff-65a582c11880`) lines 315-373 [crates/gcode/src/commands/graph/tests.rs:315-373]
  - Signature: `fn top_level_read_commands_preserve_json_shape() {`
  - Purpose: This test validates that `PagedResponse` and `GraphResult` structs serialize to JSON via `serde_json` while preserving field structure and correctly representing optional `Option` fields, with and without metadata. [crates/gcode/src/commands/graph/tests.rs:315-373]

