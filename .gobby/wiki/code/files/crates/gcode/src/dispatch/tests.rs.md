---
title: crates/gcode/src/dispatch/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/dispatch/tests.rs
  ranges:
  - 5-9
  - 12-14
  - 17-22
  - 25-27
  - 30-70
  - 73-87
  - 90-115
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/dispatch/tests.rs

Module: [[code/modules/crates/gcode/src/dispatch|crates/gcode/src/dispatch]]

## Purpose

Tests dispatch behavior in `gcode`, covering stderr log-level selection, early `setup` dispatch from parsed CLI input, and command-to-service selection logic. The helper `services_for` parses CLI args into a `Cli` and maps the resulting command to a `ServiceConfigSelection`, and the tests verify that lookup, graph, and AI commands request only the minimal backend services they need.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-14]
[crates/gcode/src/dispatch/tests.rs:17-22]
[crates/gcode/src/dispatch/tests.rs:25-27]
[crates/gcode/src/dispatch/tests.rs:30-70]

## API Symbols

- `services_for` (function) component `services_for [function]` (`fc1559c1-f164-54c8-b94f-ad104dc8e5e8`) lines 5-9 [crates/gcode/src/dispatch/tests.rs:5-9]
  - Signature: `fn services_for(args: &[&str]) -> config::ServiceConfigSelection {`
  - Purpose: Parses 'args' as a 'gcode' CLI invocation into 'Cli' and returns the 'ServiceConfigSelection' derived from the parsed command via 'service_config_selection(&cli.command)'. [crates/gcode/src/dispatch/tests.rs:5-9]
- `stderr_logger_defaults_to_warnings_for_non_quiet_runs` (function) component `stderr_logger_defaults_to_warnings_for_non_quiet_runs [function]` (`894d7367-5246-50e3-8415-e2a1f7b75755`) lines 12-14 [crates/gcode/src/dispatch/tests.rs:12-14]
  - Signature: `fn stderr_logger_defaults_to_warnings_for_non_quiet_runs() {`
  - Purpose: Verifies that 'stderr_log_level(false, None)' returns 'log::LevelFilter::Warn', meaning non-quiet stderr logging defaults to warning level. [crates/gcode/src/dispatch/tests.rs:12-14]
- `stderr_logger_respects_plain_rust_log_level` (function) component `stderr_logger_respects_plain_rust_log_level [function]` (`3cab12e5-190b-5cb2-a374-d6c9f1724611`) lines 17-22 [crates/gcode/src/dispatch/tests.rs:17-22]
  - Signature: `fn stderr_logger_respects_plain_rust_log_level() {`
  - Purpose: Verifies that 'stderr_log_level(false, Some("debug"))' maps a plain 'RUST_LOG' value of 'debug' to 'log::LevelFilter::Debug'. [crates/gcode/src/dispatch/tests.rs:17-22]
- `stderr_logger_uses_quiet_as_hard_mute` (function) component `stderr_logger_uses_quiet_as_hard_mute [function]` (`de6d2aa9-d585-5db3-bb69-408de56a71cc`) lines 25-27 [crates/gcode/src/dispatch/tests.rs:25-27]
  - Signature: `fn stderr_logger_uses_quiet_as_hard_mute() {`
  - Purpose: Verifies that when 'quiet' is enabled, 'stderr_log_level' returns 'log::LevelFilter::Off' even if the configured level is '"warn"'. [crates/gcode/src/dispatch/tests.rs:25-27]
- `setup_early_dispatch_uses_parsed_request_without_context` (function) component `setup_early_dispatch_uses_parsed_request_without_context [function]` (`211d1ec3-d0e8-5133-91ea-33149e2fc071`) lines 30-70 [crates/gcode/src/dispatch/tests.rs:30-70]
  - Signature: `fn setup_early_dispatch_uses_parsed_request_without_context() {`
  - Purpose: Verifies that 'dispatch_early_command' can execute 'setup' directly from a parsed 'Cli' without resolving project context, and that the forwarded request preserves the standalone, database URL, schema, overwrite-code-index, and embedding API base fields. [crates/gcode/src/dispatch/tests.rs:30-70]
- `lookup_commands_skip_service_config_resolution` (function) component `lookup_commands_skip_service_config_resolution [function]` (`cb67f134-ed2e-574d-84f1-9bd74fafa4c7`) lines 73-87 [crates/gcode/src/dispatch/tests.rs:73-87]
  - Signature: `fn lookup_commands_skip_service_config_resolution() {`
  - Purpose: Verifies that 'services_for' returns 'config::ServiceConfigSelection::database_only()' for several command invocations, ensuring command lookup skips service config resolution. [crates/gcode/src/dispatch/tests.rs:73-87]
- `graph_and_ai_commands_request_only_needed_services` (function) component `graph_and_ai_commands_request_only_needed_services [function]` (`b7e577bb-6d1d-5eac-947f-4c8e497c4264`) lines 90-115 [crates/gcode/src/dispatch/tests.rs:90-115]
  - Signature: `fn graph_and_ai_commands_request_only_needed_services() {`
  - Purpose: Verifies that 'services_for' selects the minimal required 'ServiceConfigSelection' for several graph and AI CLI commands, mapping each command pattern to the expected backend service set. [crates/gcode/src/dispatch/tests.rs:90-115]

