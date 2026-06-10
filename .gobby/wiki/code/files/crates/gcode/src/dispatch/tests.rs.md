---
title: crates/gcode/src/dispatch/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/dispatch/tests.rs
  ranges:
  - 5-9
  - 12-52
  - 55-69
  - 72-89
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/dispatch/tests.rs

Module: [[code/modules/crates/gcode/src/dispatch|crates/gcode/src/dispatch]]

## Purpose

`crates/gcode/src/dispatch/tests.rs` exposes 4 indexed API symbols.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-52]
[crates/gcode/src/dispatch/tests.rs:55-69]
[crates/gcode/src/dispatch/tests.rs:72-89]

## API Symbols

- `services_for` (function) component `services_for [function]` (`fc1559c1-f164-54c8-b94f-ad104dc8e5e8`) lines 5-9 [crates/gcode/src/dispatch/tests.rs:5-9]
  - Signature: `fn services_for(args: &[&str]) -> config::ServiceConfigSelection {`
  - Purpose: Parses CLI arguments prepended with "gcode" and returns a `ServiceConfigSelection` derived from the parsed command. [crates/gcode/src/dispatch/tests.rs:5-9]
- `setup_early_dispatch_uses_parsed_request_without_context` (function) component `setup_early_dispatch_uses_parsed_request_without_context [function]` (`2fca8eb4-00af-5c4d-8c50-88191dd4205c`) lines 12-52 [crates/gcode/src/dispatch/tests.rs:12-52]
  - Signature: `fn setup_early_dispatch_uses_parsed_request_without_context() {`
  - Purpose: Verifies that early command dispatch correctly parses CLI arguments into a request object and executes the handler without resolving project context. [crates/gcode/src/dispatch/tests.rs:12-52]
- `lookup_commands_skip_service_config_resolution` (function) component `lookup_commands_skip_service_config_resolution [function]` (`5253d1cd-23d7-5140-81a5-8d9180840fc5`) lines 55-69 [crates/gcode/src/dispatch/tests.rs:55-69]
  - Signature: `fn lookup_commands_skip_service_config_resolution() {`
  - Purpose: This test asserts that multiple lookup command variants (grep, tree, symbol-at, and search operations) all unconditionally resolve to `ServiceConfigSelection::database_only()` when passed to the `services_for` function. [crates/gcode/src/dispatch/tests.rs:55-69]
- `graph_and_ai_commands_request_only_needed_services` (function) component `graph_and_ai_commands_request_only_needed_services [function]` (`b90e3843-b015-5222-b4fd-b2f92d553ea3`) lines 72-89 [crates/gcode/src/dispatch/tests.rs:72-89]
  - Signature: `fn graph_and_ai_commands_request_only_needed_services() {`
  - Purpose: This test verifies that the `services_for` function correctly maps command inputs to their minimum required service configurations (hybrid search, graph-only, or vector-only). [crates/gcode/src/dispatch/tests.rs:72-89]

