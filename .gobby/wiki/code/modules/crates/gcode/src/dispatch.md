---
title: crates/gcode/src/dispatch
type: code_module
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

# crates/gcode/src/dispatch

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/dispatch/tests.rs` is a focused test module for the dispatch layer’s service/command resolution logic.

- `services_for` is the central helper/exposed symbol used in this module to derive the set of services involved in dispatch scenarios.
- `setup_early_dispatch_uses_parsed_request_without_context` verifies early-dispatch setup can proceed from a parsed request alone, without requiring external context state.
- `lookup_commands_skip_service_config_resolution` verifies command lookup behavior avoids unnecessary service-config resolution during lookup.
- `graph_and_ai_commands_request_only_needed_services` verifies graph/AI command paths request only the services that are actually required.

Overall, the module validates that dispatch uses minimal, request-driven service dependencies and avoids eager/extra service resolution.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-52]
[crates/gcode/src/dispatch/tests.rs:55-69]
[crates/gcode/src/dispatch/tests.rs:72-89]

## Files

- [[code/files/crates/gcode/src/dispatch/tests.rs|crates/gcode/src/dispatch/tests.rs]] - `crates/gcode/src/dispatch/tests.rs` exposes 4 indexed API symbols.
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-52]
[crates/gcode/src/dispatch/tests.rs:55-69]
[crates/gcode/src/dispatch/tests.rs:72-89]

## Components

- `fc1559c1-f164-54c8-b94f-ad104dc8e5e8`
- `2fca8eb4-00af-5c4d-8c50-88191dd4205c`
- `5253d1cd-23d7-5140-81a5-8d9180840fc5`
- `b90e3843-b015-5222-b4fd-b2f92d553ea3`

