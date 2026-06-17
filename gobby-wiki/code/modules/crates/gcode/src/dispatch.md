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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/dispatch/tests.rs:5-9](crates/gcode/src/dispatch/tests.rs#L5-L9), [crates/gcode/src/dispatch/tests.rs:12-14](crates/gcode/src/dispatch/tests.rs#L12-L14), [crates/gcode/src/dispatch/tests.rs:17-22](crates/gcode/src/dispatch/tests.rs#L17-L22), [crates/gcode/src/dispatch/tests.rs:25-27](crates/gcode/src/dispatch/tests.rs#L25-L27), [crates/gcode/src/dispatch/tests.rs:30-70](crates/gcode/src/dispatch/tests.rs#L30-L70), [crates/gcode/src/dispatch/tests.rs:73-87](crates/gcode/src/dispatch/tests.rs#L73-L87), [crates/gcode/src/dispatch/tests.rs:90-115](crates/gcode/src/dispatch/tests.rs#L90-L115)

</details>

# crates/gcode/src/dispatch

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The crates/gcode/src/dispatch module handles CLI command routing, early initialization checks, and log level evaluation for the gcode CLI tool. It evaluates quiet mode settings alongside the RUST_LOG environment variable to configure the global logger's stderr severity via stderr_log_level . Additionally, it intercepts early-stage commands like setup via dispatch_early_command, processing critical configurations directly from parsed request fields without resolving full project contexts or loading heavy backend resources [crates/gcode/src/dispatch/tests.rs:30-70].

To minimize initialization overhead, the module partitions commands into distinct families, skipping service configuration resolution for basic lookup, graph, and AI commands [crates/gcode/src/dispatch/tests.rs:5-9, crates/gcode/src/dispatch/tests.rs:73-83]. It integrates closely with the crate::cli parsing layer and uses command selection mappings via service_config_selection to load only the subset of services required for execution, ensuring a highly performant and target-specific application bootstrap [crates/gcode/src/dispatch/tests.rs:5-9].

### Public API Symbols
| Symbol | Description | Source |
| --- | --- | --- |
| stderr_log_level | Computes stderr logger severity using quiet mode and optional RUST_LOG values | crates/gcode/src/dispatch/tests.rs:12-27 |
| dispatch_early_command | Executes early CLI commands utilizing only parsed request fields without full context | crates/gcode/src/dispatch/tests.rs:30-70 |
| service_config_selection | Identifies the minimal set of services needed based on the selected CLI command | crates/gcode/src/dispatch/tests.rs:5-9 |

### Environment Variables
| Variable | Description | Source |
| --- | --- | --- |
| RUST_LOG | Standard Rust logging level specification, honored unless quiet mode forces mute | crates/gcode/src/dispatch/tests.rs:17-27 |

### Setup CLI Command Flags
| Flag | Purpose | Source |
| --- | --- | --- |
| --standalone | Identifies a standalone project setup configuration | crates/gcode/src/dispatch/tests.rs:30-70 |
| --database-url | Specifies the database connection string | crates/gcode/src/dispatch/tests.rs:30-70 |
| --overwrite-code-index | Forces overwriting of any existing index | crates/gcode/src/dispatch/tests.rs:30-70 |
| --embedding-api-base | Sets the base API endpoint for embeddings | crates/gcode/src/dispatch/tests.rs:30-70 |

### Lookup Commands Bypassing Full Service Setup
| Command | Source |
| --- | --- |
| grep | crates/gcode/src/dispatch/tests.rs:73-83 |
| tree | crates/gcode/src/dispatch/tests.rs:73-83 |
| symbol-at | crates/gcode/src/dispatch/tests.rs:73-83 |
| search-content | crates/gcode/src/dispatch/tests.rs:73-83 |
| search-text | crates/gcode/src/dispatch/tests.rs:73-83 |
| search-symbol | crates/gcode/src/dispatch/tests.rs:73-83 |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/dispatch/tests.rs\|crates/gcode/src/dispatch/tests.rs]] | Tests for the gcode dispatch layer, covering stderr log-level selection, early command dispatch, and which service configurations are requested for different command families. A small `services_for` helper parses CLI args into a command and feeds them through service selection, while the test cases verify that non-quiet runs default to warnings, `RUST_LOG` is honored unless quiet mode forces mute, setup dispatch uses parsed request fields without needing project context, and lookup/graph/AI commands only trigger the minimal needed service resolution. [crates/gcode/src/dispatch/tests.rs:5-9] [crates/gcode/src/dispatch/tests.rs:12-14] [crates/gcode/src/dispatch/tests.rs:17-22] [crates/gcode/src/dispatch/tests.rs:25-27] [crates/gcode/src/dispatch/tests.rs:30-70] |

## Components

| Component ID |
| --- |
| `fc1559c1-f164-54c8-b94f-ad104dc8e5e8` |
| `894d7367-5246-50e3-8415-e2a1f7b75755` |
| `3cab12e5-190b-5cb2-a374-d6c9f1724611` |
| `de6d2aa9-d585-5db3-bb69-408de56a71cc` |
| `211d1ec3-d0e8-5133-91ea-33149e2fc071` |
| `cb67f134-ed2e-574d-84f1-9bd74fafa4c7` |
| `b7e577bb-6d1d-5eac-947f-4c8e497c4264` |
