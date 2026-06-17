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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/dispatch/tests.rs:5-9](crates/gcode/src/dispatch/tests.rs#L5-L9), [crates/gcode/src/dispatch/tests.rs:12-14](crates/gcode/src/dispatch/tests.rs#L12-L14), [crates/gcode/src/dispatch/tests.rs:17-22](crates/gcode/src/dispatch/tests.rs#L17-L22), [crates/gcode/src/dispatch/tests.rs:25-27](crates/gcode/src/dispatch/tests.rs#L25-L27), [crates/gcode/src/dispatch/tests.rs:30-70](crates/gcode/src/dispatch/tests.rs#L30-L70), [crates/gcode/src/dispatch/tests.rs:73-87](crates/gcode/src/dispatch/tests.rs#L73-L87), [crates/gcode/src/dispatch/tests.rs:90-115](crates/gcode/src/dispatch/tests.rs#L90-L115)

</details>

# crates/gcode/src/dispatch/tests.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Tests for the gcode dispatch layer, covering stderr log-level selection, early command dispatch, and which service configurations are requested for different command families. A small `services_for` helper parses CLI args into a command and feeds them through service selection, while the test cases verify that non-quiet runs default to warnings, `RUST_LOG` is honored unless quiet mode forces mute, setup dispatch uses parsed request fields without needing project context, and lookup/graph/AI commands only trigger the minimal needed service resolution.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-14]
[crates/gcode/src/dispatch/tests.rs:17-22]
[crates/gcode/src/dispatch/tests.rs:25-27]
[crates/gcode/src/dispatch/tests.rs:30-70]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `services_for` | function | `fn services_for(args: &[&str]) -> config::ServiceConfigSelection {` | `services_for [function]` | `fc1559c1-f164-54c8-b94f-ad104dc8e5e8` | 5-9 [crates/gcode/src/dispatch/tests.rs:5-9] | Indexed function `services_for` in `crates/gcode/src/dispatch/tests.rs`. [crates/gcode/src/dispatch/tests.rs:5-9] |
| `stderr_logger_defaults_to_warnings_for_non_quiet_runs` | function | `fn stderr_logger_defaults_to_warnings_for_non_quiet_runs() {` | `stderr_logger_defaults_to_warnings_for_non_quiet_runs [function]` | `894d7367-5246-50e3-8415-e2a1f7b75755` | 12-14 [crates/gcode/src/dispatch/tests.rs:12-14] | Indexed function `stderr_logger_defaults_to_warnings_for_non_quiet_runs` in `crates/gcode/src/dispatch/tests.rs`. [crates/gcode/src/dispatch/tests.rs:12-14] |
| `stderr_logger_respects_plain_rust_log_level` | function | `fn stderr_logger_respects_plain_rust_log_level() {` | `stderr_logger_respects_plain_rust_log_level [function]` | `3cab12e5-190b-5cb2-a374-d6c9f1724611` | 17-22 [crates/gcode/src/dispatch/tests.rs:17-22] | Indexed function `stderr_logger_respects_plain_rust_log_level` in `crates/gcode/src/dispatch/tests.rs`. [crates/gcode/src/dispatch/tests.rs:17-22] |
| `stderr_logger_uses_quiet_as_hard_mute` | function | `fn stderr_logger_uses_quiet_as_hard_mute() {` | `stderr_logger_uses_quiet_as_hard_mute [function]` | `de6d2aa9-d585-5db3-bb69-408de56a71cc` | 25-27 [crates/gcode/src/dispatch/tests.rs:25-27] | Indexed function `stderr_logger_uses_quiet_as_hard_mute` in `crates/gcode/src/dispatch/tests.rs`. [crates/gcode/src/dispatch/tests.rs:25-27] |
| `setup_early_dispatch_uses_parsed_request_without_context` | function | `fn setup_early_dispatch_uses_parsed_request_without_context() {` | `setup_early_dispatch_uses_parsed_request_without_context [function]` | `211d1ec3-d0e8-5133-91ea-33149e2fc071` | 30-70 [crates/gcode/src/dispatch/tests.rs:30-70] | Indexed function `setup_early_dispatch_uses_parsed_request_without_context` in `crates/gcode/src/dispatch/tests.rs`. [crates/gcode/src/dispatch/tests.rs:30-70] |
| `lookup_commands_skip_service_config_resolution` | function | `fn lookup_commands_skip_service_config_resolution() {` | `lookup_commands_skip_service_config_resolution [function]` | `cb67f134-ed2e-574d-84f1-9bd74fafa4c7` | 73-87 [crates/gcode/src/dispatch/tests.rs:73-87] | Indexed function `lookup_commands_skip_service_config_resolution` in `crates/gcode/src/dispatch/tests.rs`. [crates/gcode/src/dispatch/tests.rs:73-87] |
| `graph_and_ai_commands_request_only_needed_services` | function | `fn graph_and_ai_commands_request_only_needed_services() {` | `graph_and_ai_commands_request_only_needed_services [function]` | `b7e577bb-6d1d-5eac-947f-4c8e497c4264` | 90-115 [crates/gcode/src/dispatch/tests.rs:90-115] | Indexed function `graph_and_ai_commands_request_only_needed_services` in `crates/gcode/src/dispatch/tests.rs`. [crates/gcode/src/dispatch/tests.rs:90-115] |
