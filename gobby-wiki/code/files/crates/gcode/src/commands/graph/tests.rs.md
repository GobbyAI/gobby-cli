---
title: crates/gcode/src/commands/graph/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/tests.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/commands/graph/tests.rs` exposes 24 indexed API symbols.

## How it fits

`crates/gcode/src/commands/graph/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `make_ctx_no_falkordb` | function | Constructs a 'Context' preconfigured for a test project with placeholder Postgres and project paths, 'quiet' enabled, no FalkorDB/Qdrant/embedding/daemon configured, default code-vector and indexing settings, and 'ProjectIndexScope::Single'. [crates/gcode/src/commands/graph/tests.rs:22-36] |
| `graph_reads_degrade_when_falkor_missing` | function | Verifies that 'imports(&ctx, "src/lib.rs", Format::Text)' succeeds and degrades cleanly when 'FalkorDB' is unavailable by using 'make_ctx_no_falkordb()'. [crates/gcode/src/commands/graph/tests.rs:39-45] |
| `report_text_uses_markdown_output` | function | Verifies that formatting an empty graph report produces Markdown text containing the '# Project Graph Report' heading, the project identifier 'project-123', and begins with a Markdown header character. [crates/gcode/src/commands/graph/tests.rs:48-56] |
| `graph_text_groups_by_file_and_sorts_entries` | function | Builds a vector of 'GraphResult's, formats them with 'format_grouped_graph_results' into file-path groups sorted by path and entry line, and asserts the output order is 'src/a.rs' entries before 'src/b.rs'. [crates/gcode/src/commands/graph/tests.rs:59-98] |
| `graph_read_text_lines_surface_confidence_labels` | function | Verifies that the three line-formatting helpers render inferred 'GraphResult' values with the expected confidence label, relation label, and distance annotation in their output strings. [crates/gcode/src/commands/graph/tests.rs:101-125] |
| `graph_read_token_budget_uses_rendered_rows` | function | It verifies that 'token_budget::trim_results' budgets and truncates graph search results based on the rendered row formatter, preserving only the first result when the estimated token budget fits one rendered line and producing the expected pagination/refinement hint. [crates/gcode/src/commands/graph/tests.rs:128-178] |
| `graph_path_text_prints_ordered_chain_with_locations` | function | Verifies that 'format_symbol_path_text("alpha", "beta", &path, 8)' renders an ordered two-step shortest-path summary with hop count and source locations in the exact format 'Shortest path from 'alpha' to 'beta' (1 hop(s)):\n1. alpha (src/a.rs:3)\n2. beta (src/b.rs:9)'. [crates/gcode/src/commands/graph/tests.rs:181-205] |
| `graph_path_text_reports_bounded_no_path` | function | Verifies that 'format_symbol_path_text("alpha", "beta", &[], 8)' returns the bounded failure message 'No path found from 'alpha' to 'beta' within 8 CALLS hop(s).' [crates/gcode/src/commands/graph/tests.rs:208-215] |
| `report_requires_graph_service` | function | Verifies that 'report(&ctx, 10, Format::Json)' fails when the graph service is not configured, returning 'ProjectGraphReportError::GraphServiceNotConfigured' with an error message indicating that project graph reporting requires FalkorDB. [crates/gcode/src/commands/graph/tests.rs:218-232] |
| `SpyLifecycleBackend` | class | 'SpyLifecycleBackend' is a test spy backend that uses 'RefCell' to record a mutable sequence of 'GraphLifecycleAction' values in an internal vector. [crates/gcode/src/commands/graph/tests.rs:235-237] |
| `SpyLifecycleBackend::run` | method | Appends the provided 'GraphLifecycleAction' to 'self.actions' and returns an 'Ok(GraphLifecycleOutput)' echoing the 'project_id' and 'action' from 'ctx', with a fixed '"spy lifecycle"' summary and a success payload JSON. [crates/gcode/src/commands/graph/tests.rs:240-257] |
| `graph_lifecycle_commands_dispatch_to_core_backend` | function | Verifies that 'run_lifecycle_action_with_backend' dispatches 'GraphLifecycleAction::Clear' and 'GraphLifecycleAction::Rebuild' to the supplied backend in order without error. [crates/gcode/src/commands/graph/tests.rs:261-284] |
| `missing_project_sync_error_has_typed_payload` | function | Verifies that 'GraphSyncContractError::project_not_indexed' returns the expected exit code and a typed payload containing 'project_id', 'file_path', 'status: "error"', and 'reason: "project_not_indexed"'. [crates/gcode/src/commands/graph/tests.rs:287-296] |
| `missing_file_sync_error_and_skip_payloads_are_typed` | function | Verifies that a missing indexed file produces the graph-sync contract error with the correct exit code and 'reason', and that the skipped-payload JSON is typed with the expected success/status counters and summary fields for that file. [crates/gcode/src/commands/graph/tests.rs:299-324] |
| `no_graph_facts_skip_payload_is_terminal_success_shape` | function | Verifies that 'skipped_no_graph_facts_payload' returns the exact terminal success JSON shape for a skipped sync with 'reason: "no_graph_facts"', including zeroed counters, 'degraded: false', and a null 'error'. [crates/gcode/src/commands/graph/tests.rs:327-349] |
| `no_graph_facts_requires_empty_imports_definitions_and_calls` | function | Verifies that 'has_no_graph_facts' returns 'true' only when the imports, definitions, and calls slices are all empty, and 'false' if any one of them contains an element. [crates/gcode/src/commands/graph/tests.rs:352-360] |
| `test_build_lifecycle_url_clear_uses_project_id_query` | function | Verifies that 'code_graph::build_lifecycle_url' constructs the clear lifecycle endpoint with a 'project_id' query parameter, yielding 'http://localhost:60887/api/code-index/graph/clear?project_id=project-123'. [crates/gcode/src/commands/graph/tests.rs:363-375] |
| `test_build_lifecycle_url_rebuild_uses_project_id_query` | function | Verifies that 'code_graph::build_lifecycle_url' for 'GraphLifecycleAction::Rebuild' returns a URL with the 'project_id' query parameter set to the provided project ID. [crates/gcode/src/commands/graph/tests.rs:378-390] |
| `test_require_daemon_url_errors_when_missing` | function | Verifies that 'code_graph::require_daemon_url(None, GraphLifecycleAction::Clear)' returns an error whose message states the Gobby daemon URL is not configured and references the 'gcode graph clear' action. [crates/gcode/src/commands/graph/tests.rs:393-406] |
| `test_format_http_error_includes_status_and_body` | function | Verifies that 'code_graph::format_http_error' for 'GraphLifecycleAction::Clear' includes both the HTTP status code ('502') and the response body text ('daemon upstream unavailable') in the returned error message. [crates/gcode/src/commands/graph/tests.rs:409-424] |
| `test_parse_success_payload_fails_on_invalid_json` | function | Verifies that 'code_graph::parse_success_payload' returns an error for a successful 'HTTP 200 OK' response body containing invalid JSON, and that the error message includes both 'invalid JSON' and 'HTTP 200 OK'. [crates/gcode/src/commands/graph/tests.rs:427-443] |
| `test_format_success_text_prefers_message_field` | function | Verifies that 'format_success_text' formats a successful graph-clear result using the payload’s 'message' field, producing the expected project-scoped confirmation text. [crates/gcode/src/commands/graph/tests.rs:446-463] |
| `test_format_success_text_falls_back_to_compact_json` | function | Verifies that 'format_success_text' renders a rebuild success message using the compact JSON representation of the payload summary when no richer text summary is available. [crates/gcode/src/commands/graph/tests.rs:466-483] |
| `top_level_read_commands_preserve_json_shape` | function | Verifies that serializing a 'PagedResponse' for top-level read commands preserves the expected JSON field names and values, including nested 'GraphResult' data, enum/string representations, and omission of 'metadata' when absent. [crates/gcode/src/commands/graph/tests.rs:486-548] |

