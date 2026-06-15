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
  - 135-158
  - 161-170
  - 173-189
  - 192-210
  - 213-221
  - 224-236
  - 239-251
  - 254-267
  - 270-285
  - 288-304
  - 307-324
  - 327-344
  - 347-405
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/tests.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

Tests for the graph command layer, covering read/report formatting, lifecycle dispatch, sync contract payloads, daemon URL and HTTP error handling, success-text formatting, and JSON shape preservation. The file builds a minimal `Context` without FalkorDB for degradation checks, uses a `SpyLifecycleBackend` to verify backend calls and outputs, and exercises helper functions to ensure graph features fail, skip, or render consistently under the expected edge cases.
[crates/gcode/src/commands/graph/tests.rs:16-30]
[crates/gcode/src/commands/graph/tests.rs:33-39]
[crates/gcode/src/commands/graph/tests.rs:42-50]
[crates/gcode/src/commands/graph/tests.rs:53-89]
[crates/gcode/src/commands/graph/tests.rs:92-106]

## API Symbols

- `make_ctx_no_falkordb` (function) component `make_ctx_no_falkordb [function]` (`1bab4f0f-16c6-52e8-9e2b-62d90e03e8a7`) lines 16-30 [crates/gcode/src/commands/graph/tests.rs:16-30]
  - Signature: `fn make_ctx_no_falkordb() -> Context {`
  - Purpose: Constructs a 'Context' configured for a nonexistent test project with PostgreSQL and project paths pointing to '/nonexistent', quiet mode enabled, all FalkorDB/Qdrant/embedding/daemon fields unset, and default code-vector/indexing settings with a single-project index scope. [crates/gcode/src/commands/graph/tests.rs:16-30]
- `graph_reads_degrade_when_falkor_missing` (function) component `graph_reads_degrade_when_falkor_missing [function]` (`90a68843-0512-5599-8523-6fff5eb0e31a`) lines 33-39 [crates/gcode/src/commands/graph/tests.rs:33-39]
  - Signature: `fn graph_reads_degrade_when_falkor_missing() {`
  - Purpose: Verifies that 'imports(&ctx, "src/lib.rs", Format::Text)' succeeds and degrades gracefully when FalkorDB is unavailable by using a context created without it. [crates/gcode/src/commands/graph/tests.rs:33-39]
- `report_text_uses_markdown_output` (function) component `report_text_uses_markdown_output [function]` (`63780a07-3574-5fa7-91a0-1f7f03ebdf9d`) lines 42-50 [crates/gcode/src/commands/graph/tests.rs:42-50]
  - Signature: `fn report_text_uses_markdown_output() {`
  - Purpose: Verifies that 'format_report_text' renders an empty project graph report as Markdown by asserting the output starts with a heading and includes the expected title and project identifier. [crates/gcode/src/commands/graph/tests.rs:42-50]
- `graph_text_groups_by_file_and_sorts_entries` (function) component `graph_text_groups_by_file_and_sorts_entries [function]` (`59586d5c-8210-5d43-a746-84a1b0c95dc2`) lines 53-89 [crates/gcode/src/commands/graph/tests.rs:53-89]
  - Signature: `fn graph_text_groups_by_file_and_sorts_entries() {`
  - Purpose: Verifies that 'format_grouped_graph_results' groups 'GraphResult' items by 'file_path' and emits each group with entries sorted by ascending 'line' number. [crates/gcode/src/commands/graph/tests.rs:53-89]
- `report_requires_graph_service` (function) component `report_requires_graph_service [function]` (`a438fc27-960c-525d-9a5c-7383fb389247`) lines 92-106 [crates/gcode/src/commands/graph/tests.rs:92-106]
  - Signature: `fn report_requires_graph_service() {`
  - Purpose: Verifies that 'report' called with a context lacking FalkorDB fails with 'ProjectGraphReportError::GraphServiceNotConfigured' and an error message stating that the project graph report requires FalkorDB. [crates/gcode/src/commands/graph/tests.rs:92-106]
- `SpyLifecycleBackend` (class) component `SpyLifecycleBackend [class]` (`973301c2-73c2-5806-adca-ab53c0ae3a92`) lines 109-111 [crates/gcode/src/commands/graph/tests.rs:109-111]
  - Signature: `struct SpyLifecycleBackend {`
  - Purpose: 'SpyLifecycleBackend' is a test spy struct that records 'GraphLifecycleAction' values in an interiorly mutable 'RefCell<Vec<GraphLifecycleAction>>' for later inspection. [crates/gcode/src/commands/graph/tests.rs:109-111]
- `SpyLifecycleBackend` (class) component `SpyLifecycleBackend [class]` (`9b7af865-ab57-5ec5-9c9b-e44fb920f6b3`) lines 113-132 [crates/gcode/src/commands/graph/tests.rs:113-132]
  - Signature: `impl super::lifecycle::LifecycleBackend for SpyLifecycleBackend {`
  - Purpose: 'SpyLifecycleBackend' is a test double implementing 'LifecycleBackend' that records each 'GraphLifecycleAction' it receives and returns a synthetic 'GraphLifecycleOutput' echoing the project ID and action with a fixed '"spy lifecycle"' summary and success payload. [crates/gcode/src/commands/graph/tests.rs:113-132]
- `SpyLifecycleBackend.run` (method) component `SpyLifecycleBackend.run [method]` (`54c0c9fa-cad1-5a9d-9bcc-b2bae105a7bf`) lines 114-131 [crates/gcode/src/commands/graph/tests.rs:114-131]
  - Signature: `fn run(`
  - Purpose: Appends the supplied 'GraphLifecycleAction' to 'self.actions' and returns an 'Ok(GraphLifecycleOutput)' containing the current 'project_id', the action, a fixed '"spy lifecycle"' summary, and a JSON payload echoing those fields with 'success: true'. [crates/gcode/src/commands/graph/tests.rs:114-131]
- `graph_lifecycle_commands_dispatch_to_core_backend` (function) component `graph_lifecycle_commands_dispatch_to_core_backend [function]` (`aa64aa3f-bb46-5c02-8799-e69ff8d34282`) lines 135-158 [crates/gcode/src/commands/graph/tests.rs:135-158]
  - Signature: `fn graph_lifecycle_commands_dispatch_to_core_backend() {`
  - Purpose: Verifies that 'run_lifecycle_action_with_backend' dispatches 'GraphLifecycleAction::Clear' and 'GraphLifecycleAction::Rebuild' to the provided backend in order and completes successfully. [crates/gcode/src/commands/graph/tests.rs:135-158]
- `missing_project_sync_error_has_typed_payload` (function) component `missing_project_sync_error_has_typed_payload [function]` (`740c136f-0d34-52a3-8235-a91658e72555`) lines 161-170 [crates/gcode/src/commands/graph/tests.rs:161-170]
  - Signature: `fn missing_project_sync_error_has_typed_payload() {`
  - Purpose: Verifies that 'GraphSyncContractError::project_not_indexed' returns the expected exit code and a typed payload containing 'project_id', 'file_path', 'status: "error"', and 'reason: "project_not_indexed"'. [crates/gcode/src/commands/graph/tests.rs:161-170]
- `missing_file_sync_error_and_skip_payloads_are_typed` (function) component `missing_file_sync_error_and_skip_payloads_are_typed [function]` (`f715d046-8fdc-5a74-9a3c-146689af1e92`) lines 173-189 [crates/gcode/src/commands/graph/tests.rs:173-189]
  - Signature: `fn missing_file_sync_error_and_skip_payloads_are_typed() {`
  - Purpose: Verifies that an indexed-file-not-found sync error uses the 'GRAPH_SYNC_CONTRACT_EXIT_CODE' and 'reason' payload, and that the corresponding skipped-file payload is a typed JSON object with 'project_id', 'file_path', 'status: "skipped"', and 'reason: "indexed_file_not_found"'. [crates/gcode/src/commands/graph/tests.rs:173-189]
- `no_graph_facts_skip_payload_is_terminal_success_shape` (function) component `no_graph_facts_skip_payload_is_terminal_success_shape [function]` (`170c2f8c-d4cc-50b2-94de-6fde03ebf677`) lines 192-210 [crates/gcode/src/commands/graph/tests.rs:192-210]
  - Signature: `fn no_graph_facts_skip_payload_is_terminal_success_shape() {`
  - Purpose: Verifies that 'skipped_no_graph_facts_payload(&ctx, "docs/generated.json")' returns the expected terminal success JSON payload with 'success: true', 'status: "skipped"', 'reason: "no_graph_facts"', and zero graph-write counts. [crates/gcode/src/commands/graph/tests.rs:192-210]
- `no_graph_facts_requires_empty_imports_definitions_and_calls` (function) component `no_graph_facts_requires_empty_imports_definitions_and_calls [function]` (`1801b675-a119-5b16-b031-61df635063f8`) lines 213-221 [crates/gcode/src/commands/graph/tests.rs:213-221]
  - Signature: `fn no_graph_facts_requires_empty_imports_definitions_and_calls() {`
  - Purpose: Verifies that 'has_no_graph_facts' returns 'true' only when imports, definitions, and calls are all empty slices, and 'false' if any one of the three contains an element. [crates/gcode/src/commands/graph/tests.rs:213-221]
- `test_build_lifecycle_url_clear_uses_project_id_query` (function) component `test_build_lifecycle_url_clear_uses_project_id_query [function]` (`ff74e32d-6725-5a78-8beb-da63f76ae83e`) lines 224-236 [crates/gcode/src/commands/graph/tests.rs:224-236]
  - Signature: `fn test_build_lifecycle_url_clear_uses_project_id_query() {`
  - Purpose: Verifies that 'code_graph::build_lifecycle_url' constructs the graph clear endpoint with the 'project_id' query parameter appended to the base URL for 'GraphLifecycleAction::Clear'. [crates/gcode/src/commands/graph/tests.rs:224-236]
- `test_build_lifecycle_url_rebuild_uses_project_id_query` (function) component `test_build_lifecycle_url_rebuild_uses_project_id_query [function]` (`8027b4df-2b55-556e-96be-65ec775e103c`) lines 239-251 [crates/gcode/src/commands/graph/tests.rs:239-251]
  - Signature: `fn test_build_lifecycle_url_rebuild_uses_project_id_query() {`
  - Purpose: Verifies that 'code_graph::build_lifecycle_url' formats a 'GraphLifecycleAction::Rebuild' URL by appending 'api/code-index/graph/rebuild?project_id=project-123' to the base host. [crates/gcode/src/commands/graph/tests.rs:239-251]
- `test_require_daemon_url_errors_when_missing` (function) component `test_require_daemon_url_errors_when_missing [function]` (`f4cccdd9-e8c8-520b-93a6-cb7f47212417`) lines 254-267 [crates/gcode/src/commands/graph/tests.rs:254-267]
  - Signature: `fn test_require_daemon_url_errors_when_missing() {`
  - Purpose: Verifies that 'code_graph::require_daemon_url(None, GraphLifecycleAction::Clear)' returns an error when the daemon URL is absent, and that the error message mentions both the missing configuration and 'gcode graph clear'. [crates/gcode/src/commands/graph/tests.rs:254-267]
- `test_format_http_error_includes_status_and_body` (function) component `test_format_http_error_includes_status_and_body [function]` (`3d7c3a90-4b3d-5a0a-8ba7-688dffae6aa7`) lines 270-285 [crates/gcode/src/commands/graph/tests.rs:270-285]
  - Signature: `fn test_format_http_error_includes_status_and_body() {`
  - Purpose: Verifies that 'code_graph::format_http_error' for 'GraphLifecycleAction::Clear' includes both the HTTP status code ('502') and the response body text ('daemon upstream unavailable') in the formatted error message. [crates/gcode/src/commands/graph/tests.rs:270-285]
- `test_parse_success_payload_fails_on_invalid_json` (function) component `test_parse_success_payload_fails_on_invalid_json [function]` (`2ad8dae3-cf53-5dcc-96ab-636705fce049`) lines 288-304 [crates/gcode/src/commands/graph/tests.rs:288-304]
  - Signature: `fn test_parse_success_payload_fails_on_invalid_json() {`
  - Purpose: Verifies that 'code_graph::parse_success_payload' returns an error for a '200 OK' response body that is not valid JSON, and that the error message includes both 'invalid JSON' and 'HTTP 200 OK'. [crates/gcode/src/commands/graph/tests.rs:288-304]
- `test_format_success_text_prefers_message_field` (function) component `test_format_success_text_prefers_message_field [function]` (`7c1dff1c-649e-5be3-91e8-62fa1f2a29ff`) lines 307-324 [crates/gcode/src/commands/graph/tests.rs:307-324]
  - Signature: `fn test_format_success_text_prefers_message_field() {`
  - Purpose: Verifies that 'format_success_text' formats a clear-action 'GraphLifecycleOutput' using the payload’s 'message' field, producing 'Cleared code-index graph for project <id>: <message>' for the given project. [crates/gcode/src/commands/graph/tests.rs:307-324]
- `test_format_success_text_falls_back_to_compact_json` (function) component `test_format_success_text_falls_back_to_compact_json [function]` (`95774098-1ace-5f98-a778-16f990dfda80`) lines 327-344 [crates/gcode/src/commands/graph/tests.rs:327-344]
  - Signature: `fn test_format_success_text_falls_back_to_compact_json() {`
  - Purpose: Verifies that 'format_success_text' falls back to compact JSON serialization when the output summary is non-human-readable, producing 'Rebuilt code-index graph for project project-123: {"replayed":18,"synced":18}' for a rebuild action. [crates/gcode/src/commands/graph/tests.rs:327-344]
- `top_level_read_commands_preserve_json_shape` (function) component `top_level_read_commands_preserve_json_shape [function]` (`f6811ecc-48f0-58d6-bafb-32249d2bade9`) lines 347-405 [crates/gcode/src/commands/graph/tests.rs:347-405]
  - Signature: `fn top_level_read_commands_preserve_json_shape() {`
  - Purpose: Verifies that serializing 'PagedResponse<GraphResult>' preserves the expected JSON field shape and null/omitted semantics for top-level and nested fields, including optional 'metadata' appearing only when present. [crates/gcode/src/commands/graph/tests.rs:347-405]

