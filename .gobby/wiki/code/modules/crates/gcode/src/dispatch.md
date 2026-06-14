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
  - 90-107
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/dispatch

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The dispatch module is responsible for turning parsed `gcode` CLI commands into the right early actions, logger settings, and service initialization requirements. Its tests show that dispatch treats stderr logging as warning-only by default, honors a plain `RUST_LOG` level such as `debug`, and lets the quiet flag hard-mute stderr logging even when an environment level is supplied. The `services_for` helper parses CLI arguments through `Cli::try_parse_from` and passes the parsed command into `service_config_selection`, making service resolution a direct consequence of the command variant rather than a separate ad hoc path  .

A key flow is early command dispatch for setup: the parsed `Cli` is passed to `dispatch_early_command` along with the effective output format and a callback that receives the setup request. The test confirms this path uses only the parsed request fields, including standalone mode, database URL, schema, overwrite behavior, and embedding API base, and succeeds without resolving project context first . This keeps setup-style commands independent from the normal project/service bootstrapping path.

The module also distinguishes lookup commands from graph and AI commands when deciding which services to request. Lookup-oriented commands such as `grep`, `tree`, `symbol-at`, and search variants are tested as skipping service config resolution, while separate coverage verifies graph and AI command families request only the services they actually need . Since there are no child modules, collaboration is primarily between dispatch functions, CLI parsing, format selection, and configuration selection within this module’s test surface.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-14]
[crates/gcode/src/dispatch/tests.rs:17-22]
[crates/gcode/src/dispatch/tests.rs:25-27]
[crates/gcode/src/dispatch/tests.rs:30-70]

## Files

- [[code/files/crates/gcode/src/dispatch/tests.rs|crates/gcode/src/dispatch/tests.rs]] - This is a test module for the dispatch functionality that verifies command handling, service resolution, and logging configuration. The file contains helper function `services_for` which parses CLI arguments to extract service configuration, and multiple test functions that validate: stderr logger behavior respects quiet flags and RUST_LOG environment variables; early command dispatch processes parsed requests without resolving project context; and different command types correctly determine which services to request during initialization. The tests collectively ensure the dispatch layer properly routes commands with appropriate service and logging configurations.
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

