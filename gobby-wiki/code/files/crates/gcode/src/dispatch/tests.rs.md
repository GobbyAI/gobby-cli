---
title: crates/gcode/src/dispatch/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/dispatch/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/dispatch/tests.rs

Module: [[code/modules/crates/gcode/src/dispatch|crates/gcode/src/dispatch]]

## Overview

## How it fits

The file is located in the dispatch module at crates/gcode/src/dispatch/tests.rs. It closely integrates with the command-line interface logic from `crate::cli` and the main dispatch implementation in its parent module.

The tests also verify the initial bootstrapping phase of the application. They confirm that `dispatch_early_command` successfully handles early actions like project setup without waiting for full context resolution crates/gcode/src/dispatch/tests.rs:30-70. Additionally, they test the configuration of the system logger via `stderr_log_level`, validating default warnings crates/gcode/src/dispatch/tests.rs:12-14, custom environment log levels crates/gcode/src/dispatch/tests.rs:17-22, and quiet mode muting crates/gcode/src/dispatch/tests.rs:25-27.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-14]
[crates/gcode/src/dispatch/tests.rs:17-22]
[crates/gcode/src/dispatch/tests.rs:25-27]
[crates/gcode/src/dispatch/tests.rs:30-70]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `services_for` | function | Parses 'args' as a 'Cli' invocation prefixed with program name '"gcode"' and returns the corresponding 'config::ServiceConfigSelection' by delegating to 'service_config_selection(&cli.command)'. [crates/gcode/src/dispatch/tests.rs:5-9] |
| `stderr_logger_defaults_to_warnings_for_non_quiet_runs` | function | Verifies that 'stderr_log_level(false, None)' returns 'log::LevelFilter::Warn', meaning non-quiet stderr logging defaults to warning level. [crates/gcode/src/dispatch/tests.rs:12-14] |
| `stderr_logger_respects_plain_rust_log_level` | function | Verifies that 'stderr_log_level(false, Some("debug"))' resolves to 'log::LevelFilter::Debug' when a plain 'RUST_LOG' level string is provided. [crates/gcode/src/dispatch/tests.rs:17-22] |
| `stderr_logger_uses_quiet_as_hard_mute` | function | Verifies that when 'quiet' is enabled, 'stderr_log_level' returns 'log::LevelFilter::Off' even if the configured level is 'warn'. [crates/gcode/src/dispatch/tests.rs:25-27] |
| `setup_early_dispatch_uses_parsed_request_without_context` | function | Verifies that 'dispatch_early_command' handles the parsed 'setup' CLI request directly, without resolving project context, and forwards the expected 'standalone', 'database_url', 'schema', 'overwrite_code_index', and 'embedding_api_base' fields to the handler. [crates/gcode/src/dispatch/tests.rs:30-70] |
| `lookup_commands_skip_service_config_resolution` | function | Verifies that 'services_for' returns 'config::ServiceConfigSelection::database_only()' for several command arguments that should skip service config resolution. [crates/gcode/src/dispatch/tests.rs:73-87] |
| `graph_and_ai_commands_request_only_needed_services` | function | Verifies that 'services_for' selects the minimal required 'ServiceConfigSelection' for several graph/AI command argument patterns, including hybrid search, FalkorDB-only, Qdrant-only, projection cleanup, and vector services. [crates/gcode/src/dispatch/tests.rs:90-115] |

