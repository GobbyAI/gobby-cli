---
title: crates/gcode/src/lib.rs
type: code_file
provenance:
- file: crates/gcode/src/lib.rs
  ranges:
  - 34-42
  - 45-75
  - 78-142
  - 145-172
  - 175-204
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/lib.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

The file serves as the root library module organizing code analysis and indexing functionality through multiple sub-modules (index, graph, vector, projection, etc.). It re-exports key public APIs including IndexRequest, IndexOutcome, and related types for indexing operations. The test module enforces architectural boundaries through assert_cli_independent_contract, a generic validation helper that ensures types don't reference CLI-specific modules (commands, output, clap), and public_projection_api_is_cli_independent, which verifies that core public APIs remain decoupled from CLI code. Additional functions like foundation_consumer_migration, indexing_search_primitive_migration, and falkor_facade_uses_core_graph_client_only support internal system evolution and constraint validation. Together these pieces maintain clean separation between the core library and command-line interface layers while supporting system migrations.
[crates/gcode/src/lib.rs:34-42]
[crates/gcode/src/lib.rs:45-75]
[crates/gcode/src/lib.rs:78-142]
[crates/gcode/src/lib.rs:145-172]
[crates/gcode/src/lib.rs:175-204]

## API Symbols

- `assert_cli_independent_contract` (function) component `assert_cli_independent_contract [function]` (`44b94af2-7a42-5fd8-8e11-8fd9e7dcdf2a`) lines 34-42 [crates/gcode/src/lib.rs:34-42]
  - Signature: `fn assert_cli_independent_contract<T>()`
  - Purpose: Indexed function `assert_cli_independent_contract` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:34-42]
- `public_projection_api_is_cli_independent` (function) component `public_projection_api_is_cli_independent [function]` (`5d684f92-1512-5642-aecc-03e9de62f772`) lines 45-75 [crates/gcode/src/lib.rs:45-75]
  - Signature: `fn public_projection_api_is_cli_independent() {`
  - Purpose: Indexed function `public_projection_api_is_cli_independent` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:45-75]
- `foundation_consumer_migration` (function) component `foundation_consumer_migration [function]` (`76b62a69-0285-5800-a977-6f72e0b92710`) lines 78-142 [crates/gcode/src/lib.rs:78-142]
  - Signature: `fn foundation_consumer_migration() {`
  - Purpose: Indexed function `foundation_consumer_migration` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:78-142]
- `indexing_search_primitive_migration` (function) component `indexing_search_primitive_migration [function]` (`95e75a28-a70e-5a1b-8aaa-71ae12e30565`) lines 145-172 [crates/gcode/src/lib.rs:145-172]
  - Signature: `fn indexing_search_primitive_migration() {`
  - Purpose: Indexed function `indexing_search_primitive_migration` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:145-172]
- `falkor_facade_uses_core_graph_client_only` (function) component `falkor_facade_uses_core_graph_client_only [function]` (`58b22d9b-9122-5061-9624-3486abb84abd`) lines 175-204 [crates/gcode/src/lib.rs:175-204]
  - Signature: `fn falkor_facade_uses_core_graph_client_only() {`
  - Purpose: Indexed function `falkor_facade_uses_core_graph_client_only` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:175-204]
- `visit` (function) component `visit [function]` (`4fbaa328-4c50-53cd-b212-a774e7caa2c2`) lines 180-197 [crates/gcode/src/lib.rs:180-197]
  - Signature: `fn visit(path: &std::path::Path, offenders: &mut Vec<std::path::PathBuf>) {`
  - Purpose: Indexed function `visit` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:180-197]

