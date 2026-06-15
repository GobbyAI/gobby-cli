---
title: crates/gcode/src/dispatch
type: code_module
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

# crates/gcode/src/dispatch

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The dispatch module is responsible for turning parsed CLI intent into the right runtime behavior without doing unnecessary setup. Its stderr logging policy defaults normal runs to warnings, honors a plain Rust log level when one is supplied, and treats quiet mode as a hard mute even if a level is provided. The tests capture those behaviors through `stderr_log_level(false, None)`, `stderr_log_level(false, Some("debug"))`, and `stderr_log_level(true, Some("warn"))`. 

A key flow is early handling for `setup`: the test builds a parsed `Cli` with project path, standalone mode, database URL, index overwrite, and embedding API base, then calls `dispatch_early_command` with `effective_format(cli.format, &cli.command)`. The closure receives the already-parsed request and asserts the request fields directly, showing that setup can dispatch successfully before resolving broader project context. 

The module also decides which backend services a command needs. The local `services_for` helper parses synthetic CLI arguments into `Cli` and passes `cli.command` to `service_config_selection`, giving tests a compact way to verify command-to-service selection. Lookup-oriented commands such as `grep`, `tree`, `symbol-at`, and search variants are covered as commands that skip service config resolution, while the file summary notes that graph and AI commands are separately checked to request only the minimal services they require. [crates/gcode/src/dispatch/tests.rs:5-9] [crates/gcode/src/dispatch/tests.rs:62-70]

## Files

- [[code/files/crates/gcode/src/dispatch/tests.rs|crates/gcode/src/dispatch/tests.rs]] - Tests dispatch behavior in `gcode`, covering stderr log-level selection, early `setup` dispatch from parsed CLI input, and command-to-service selection logic. The helper `services_for` parses CLI args into a `Cli` and maps the resulting command to a `ServiceConfigSelection`, and the tests verify that lookup, graph, and AI commands request only the minimal backend services they need.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-14]
[crates/gcode/src/dispatch/tests.rs:17-22]
[crates/gcode/src/dispatch/tests.rs:25-27]
[crates/gcode/src/dispatch/tests.rs:30-70]

## Components

- `fc1559c1-f164-54c8-b94f-ad104dc8e5e8`
- `894d7367-5246-50e3-8415-e2a1f7b75755`
- `3cab12e5-190b-5cb2-a374-d6c9f1724611`
- `de6d2aa9-d585-5db3-bb69-408de56a71cc`
- `211d1ec3-d0e8-5133-91ea-33149e2fc071`
- `cb67f134-ed2e-574d-84f1-9bd74fafa4c7`
- `b7e577bb-6d1d-5eac-947f-4c8e497c4264`

