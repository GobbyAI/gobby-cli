---
title: crates/gcode/src/commands/graph/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/tests.rs
  ranges:
  - 22-36
  - 39-45
  - 48-56
  - 59-98
  - 101-125
  - 128-178
  - 181-205
  - 208-215
  - 218-232
  - 235-237
  - 240-257
  - 261-284
  - 287-296
  - 299-315
  - 318-336
  - 339-347
  - 350-362
  - 365-377
  - 380-393
  - 396-411
  - 414-430
  - 433-450
  - 453-470
  - 473-535
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/graph/tests.rs:22-36](crates/gcode/src/commands/graph/tests.rs#L22-L36), [crates/gcode/src/commands/graph/tests.rs:39-45](crates/gcode/src/commands/graph/tests.rs#L39-L45), [crates/gcode/src/commands/graph/tests.rs:48-56](crates/gcode/src/commands/graph/tests.rs#L48-L56), [crates/gcode/src/commands/graph/tests.rs:59-98](crates/gcode/src/commands/graph/tests.rs#L59-L98), [crates/gcode/src/commands/graph/tests.rs:101-125](crates/gcode/src/commands/graph/tests.rs#L101-L125), [crates/gcode/src/commands/graph/tests.rs:128-178](crates/gcode/src/commands/graph/tests.rs#L128-L178), [crates/gcode/src/commands/graph/tests.rs:181-205](crates/gcode/src/commands/graph/tests.rs#L181-L205), [crates/gcode/src/commands/graph/tests.rs:208-215](crates/gcode/src/commands/graph/tests.rs#L208-L215), [crates/gcode/src/commands/graph/tests.rs:218-232](crates/gcode/src/commands/graph/tests.rs#L218-L232), [crates/gcode/src/commands/graph/tests.rs:235-237](crates/gcode/src/commands/graph/tests.rs#L235-L237), [crates/gcode/src/commands/graph/tests.rs:240-257](crates/gcode/src/commands/graph/tests.rs#L240-L257), [crates/gcode/src/commands/graph/tests.rs:261-284](crates/gcode/src/commands/graph/tests.rs#L261-L284), [crates/gcode/src/commands/graph/tests.rs:287-296](crates/gcode/src/commands/graph/tests.rs#L287-L296), [crates/gcode/src/commands/graph/tests.rs:299-315](crates/gcode/src/commands/graph/tests.rs#L299-L315), [crates/gcode/src/commands/graph/tests.rs:318-336](crates/gcode/src/commands/graph/tests.rs#L318-L336), [crates/gcode/src/commands/graph/tests.rs:339-347](crates/gcode/src/commands/graph/tests.rs#L339-L347), [crates/gcode/src/commands/graph/tests.rs:350-362](crates/gcode/src/commands/graph/tests.rs#L350-L362), [crates/gcode/src/commands/graph/tests.rs:365-377](crates/gcode/src/commands/graph/tests.rs#L365-L377), [crates/gcode/src/commands/graph/tests.rs:380-393](crates/gcode/src/commands/graph/tests.rs#L380-L393), [crates/gcode/src/commands/graph/tests.rs:396-411](crates/gcode/src/commands/graph/tests.rs#L396-L411), [crates/gcode/src/commands/graph/tests.rs:414-430](crates/gcode/src/commands/graph/tests.rs#L414-L430), [crates/gcode/src/commands/graph/tests.rs:433-450](crates/gcode/src/commands/graph/tests.rs#L433-L450), [crates/gcode/src/commands/graph/tests.rs:453-470](crates/gcode/src/commands/graph/tests.rs#L453-L470), [crates/gcode/src/commands/graph/tests.rs:473-535](crates/gcode/src/commands/graph/tests.rs#L473-L535)

</details>

# crates/gcode/src/commands/graph/tests.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

This test module validates the graph command layer end to end: it builds a minimal `Context`, exercises read/report/lifecycle helpers, and checks that graph output degrades cleanly when backends are missing. The tests cover text and markdown formatting, grouping and ordering of graph results, confidence labels, token-budget rendering, path formatting, lifecycle dispatch and URL construction, typed error/skip payloads, JSON parsing, and top-level read command response shapes.
[crates/gcode/src/commands/graph/tests.rs:22-36]
[crates/gcode/src/commands/graph/tests.rs:39-45]
[crates/gcode/src/commands/graph/tests.rs:48-56]
[crates/gcode/src/commands/graph/tests.rs:59-98]
[crates/gcode/src/commands/graph/tests.rs:101-125]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `make_ctx_no_falkordb` | function | `fn make_ctx_no_falkordb() -> Context {` | `make_ctx_no_falkordb [function]` | `9a1a06db-26b1-5a5b-bdb3-74ea81940ddc` | 22-36 [crates/gcode/src/commands/graph/tests.rs:22-36] | Indexed function `make_ctx_no_falkordb` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:22-36] |
| `graph_reads_degrade_when_falkor_missing` | function | `fn graph_reads_degrade_when_falkor_missing() {` | `graph_reads_degrade_when_falkor_missing [function]` | `24280c5c-c157-5ee5-b1d4-a2c905c04f91` | 39-45 [crates/gcode/src/commands/graph/tests.rs:39-45] | Indexed function `graph_reads_degrade_when_falkor_missing` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:39-45] |
| `report_text_uses_markdown_output` | function | `fn report_text_uses_markdown_output() {` | `report_text_uses_markdown_output [function]` | `134e04fb-264a-5824-80ae-cd391b14e434` | 48-56 [crates/gcode/src/commands/graph/tests.rs:48-56] | Indexed function `report_text_uses_markdown_output` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:48-56] |
| `graph_text_groups_by_file_and_sorts_entries` | function | `fn graph_text_groups_by_file_and_sorts_entries() {` | `graph_text_groups_by_file_and_sorts_entries [function]` | `5e5f77dd-893e-520a-b1ee-c26faf3420f6` | 59-98 [crates/gcode/src/commands/graph/tests.rs:59-98] | Indexed function `graph_text_groups_by_file_and_sorts_entries` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:59-98] |
| `graph_read_text_lines_surface_confidence_labels` | function | `fn graph_read_text_lines_surface_confidence_labels() {` | `graph_read_text_lines_surface_confidence_labels [function]` | `f67306b6-88ee-537f-8ac1-5fe4e3ce7ed4` | 101-125 [crates/gcode/src/commands/graph/tests.rs:101-125] | Indexed function `graph_read_text_lines_surface_confidence_labels` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:101-125] |
| `graph_read_token_budget_uses_rendered_rows` | function | `fn graph_read_token_budget_uses_rendered_rows() {` | `graph_read_token_budget_uses_rendered_rows [function]` | `1652b2a0-c85a-58d0-a87f-0362e2fcdf36` | 128-178 [crates/gcode/src/commands/graph/tests.rs:128-178] | Indexed function `graph_read_token_budget_uses_rendered_rows` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:128-178] |
| `graph_path_text_prints_ordered_chain_with_locations` | function | `fn graph_path_text_prints_ordered_chain_with_locations() {` | `graph_path_text_prints_ordered_chain_with_locations [function]` | `11a8ae68-ac10-5d7e-81b5-9d4d746cf9bf` | 181-205 [crates/gcode/src/commands/graph/tests.rs:181-205] | Indexed function `graph_path_text_prints_ordered_chain_with_locations` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:181-205] |
| `graph_path_text_reports_bounded_no_path` | function | `fn graph_path_text_reports_bounded_no_path() {` | `graph_path_text_reports_bounded_no_path [function]` | `19d55c70-9814-5de6-a16d-37fe896c0aad` | 208-215 [crates/gcode/src/commands/graph/tests.rs:208-215] | Indexed function `graph_path_text_reports_bounded_no_path` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:208-215] |
| `report_requires_graph_service` | function | `fn report_requires_graph_service() {` | `report_requires_graph_service [function]` | `ecbe5cc2-9faf-5391-af84-76d4d4786519` | 218-232 [crates/gcode/src/commands/graph/tests.rs:218-232] | Indexed function `report_requires_graph_service` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:218-232] |
| `SpyLifecycleBackend` | class | `struct SpyLifecycleBackend {` | `SpyLifecycleBackend [class]` | `5b0b0e22-9a9b-5f0b-93c9-82de8c0d51fb` | 235-237 [crates/gcode/src/commands/graph/tests.rs:235-237] | Indexed class `SpyLifecycleBackend` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:235-237] |
| `SpyLifecycleBackend::run` | method | `fn run(` | `SpyLifecycleBackend::run [method]` | `9f5c1a14-5ee6-5672-8c24-f7b5e881bcca` | 240-257 [crates/gcode/src/commands/graph/tests.rs:240-257] | Indexed method `SpyLifecycleBackend::run` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:240-257] |
| `graph_lifecycle_commands_dispatch_to_core_backend` | function | `fn graph_lifecycle_commands_dispatch_to_core_backend() {` | `graph_lifecycle_commands_dispatch_to_core_backend [function]` | `479e3fb4-951b-5978-bde8-ed6aecb0b54a` | 261-284 [crates/gcode/src/commands/graph/tests.rs:261-284] | Indexed function `graph_lifecycle_commands_dispatch_to_core_backend` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:261-284] |
| `missing_project_sync_error_has_typed_payload` | function | `fn missing_project_sync_error_has_typed_payload() {` | `missing_project_sync_error_has_typed_payload [function]` | `4d8b9d52-f782-5b02-9b16-ccf6a1c5c124` | 287-296 [crates/gcode/src/commands/graph/tests.rs:287-296] | Indexed function `missing_project_sync_error_has_typed_payload` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:287-296] |
| `missing_file_sync_error_and_skip_payloads_are_typed` | function | `fn missing_file_sync_error_and_skip_payloads_are_typed() {` | `missing_file_sync_error_and_skip_payloads_are_typed [function]` | `453b8c16-c790-5ef5-8e1e-6700b16c8002` | 299-315 [crates/gcode/src/commands/graph/tests.rs:299-315] | Indexed function `missing_file_sync_error_and_skip_payloads_are_typed` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:299-315] |
| `no_graph_facts_skip_payload_is_terminal_success_shape` | function | `fn no_graph_facts_skip_payload_is_terminal_success_shape() {` | `no_graph_facts_skip_payload_is_terminal_success_shape [function]` | `33e42b59-9899-5ddb-9777-fce1998c3944` | 318-336 [crates/gcode/src/commands/graph/tests.rs:318-336] | Indexed function `no_graph_facts_skip_payload_is_terminal_success_shape` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:318-336] |
| `no_graph_facts_requires_empty_imports_definitions_and_calls` | function | `fn no_graph_facts_requires_empty_imports_definitions_and_calls() {` | `no_graph_facts_requires_empty_imports_definitions_and_calls [function]` | `bf19ece1-84a6-5add-a80a-d296919b6c39` | 339-347 [crates/gcode/src/commands/graph/tests.rs:339-347] | Indexed function `no_graph_facts_requires_empty_imports_definitions_and_calls` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:339-347] |
| `test_build_lifecycle_url_clear_uses_project_id_query` | function | `fn test_build_lifecycle_url_clear_uses_project_id_query() {` | `test_build_lifecycle_url_clear_uses_project_id_query [function]` | `751498bf-2a10-5aec-8e23-ed672f040475` | 350-362 [crates/gcode/src/commands/graph/tests.rs:350-362] | Indexed function `test_build_lifecycle_url_clear_uses_project_id_query` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:350-362] |
| `test_build_lifecycle_url_rebuild_uses_project_id_query` | function | `fn test_build_lifecycle_url_rebuild_uses_project_id_query() {` | `test_build_lifecycle_url_rebuild_uses_project_id_query [function]` | `745636dc-b284-5c9a-a01d-556ed7735f05` | 365-377 [crates/gcode/src/commands/graph/tests.rs:365-377] | Indexed function `test_build_lifecycle_url_rebuild_uses_project_id_query` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:365-377] |
| `test_require_daemon_url_errors_when_missing` | function | `fn test_require_daemon_url_errors_when_missing() {` | `test_require_daemon_url_errors_when_missing [function]` | `d7991012-488b-5c18-987a-e2077dca1ee2` | 380-393 [crates/gcode/src/commands/graph/tests.rs:380-393] | Indexed function `test_require_daemon_url_errors_when_missing` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:380-393] |
| `test_format_http_error_includes_status_and_body` | function | `fn test_format_http_error_includes_status_and_body() {` | `test_format_http_error_includes_status_and_body [function]` | `db5902aa-41cc-5700-a4f4-2a57a0d38934` | 396-411 [crates/gcode/src/commands/graph/tests.rs:396-411] | Indexed function `test_format_http_error_includes_status_and_body` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:396-411] |
| `test_parse_success_payload_fails_on_invalid_json` | function | `fn test_parse_success_payload_fails_on_invalid_json() {` | `test_parse_success_payload_fails_on_invalid_json [function]` | `eded9078-a7c9-58dc-89c8-2d529b4ccc7f` | 414-430 [crates/gcode/src/commands/graph/tests.rs:414-430] | Indexed function `test_parse_success_payload_fails_on_invalid_json` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:414-430] |
| `test_format_success_text_prefers_message_field` | function | `fn test_format_success_text_prefers_message_field() {` | `test_format_success_text_prefers_message_field [function]` | `93c21955-8e13-51f0-a7ab-ea5ba67d0704` | 433-450 [crates/gcode/src/commands/graph/tests.rs:433-450] | Indexed function `test_format_success_text_prefers_message_field` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:433-450] |
| `test_format_success_text_falls_back_to_compact_json` | function | `fn test_format_success_text_falls_back_to_compact_json() {` | `test_format_success_text_falls_back_to_compact_json [function]` | `671690ce-f214-50c6-a535-9b4545acf8ba` | 453-470 [crates/gcode/src/commands/graph/tests.rs:453-470] | Indexed function `test_format_success_text_falls_back_to_compact_json` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:453-470] |
| `top_level_read_commands_preserve_json_shape` | function | `fn top_level_read_commands_preserve_json_shape() {` | `top_level_read_commands_preserve_json_shape [function]` | `9a819916-ce95-54fc-a184-e65769d03be3` | 473-535 [crates/gcode/src/commands/graph/tests.rs:473-535] | Indexed function `top_level_read_commands_preserve_json_shape` in `crates/gcode/src/commands/graph/tests.rs`. [crates/gcode/src/commands/graph/tests.rs:473-535] |
