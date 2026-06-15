---
title: crates/gcode/src/lib.rs
type: code_file
provenance:
- file: crates/gcode/src/lib.rs
  ranges:
  - 34-42
  - 45-75
  - 78-142
  - 145-179
  - 182-211
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/lib.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This crate root wires together the `gcode` domain modules, re-exports the public indexing API, and defines test-only contract checks that enforce architectural boundaries. The tests verify that projection-facing types remain CLI-independent, required projection modules exist, foundation-consumer code has moved to `gobby_core`-backed APIs, indexing/search primitives now use core implementations instead of local ones, and no source file still directly uses `FalkorClientBuilder`.
[crates/gcode/src/lib.rs:34-42]
[crates/gcode/src/lib.rs:45-75]
[crates/gcode/src/lib.rs:78-142]
[crates/gcode/src/lib.rs:145-179]
[crates/gcode/src/lib.rs:182-211]

## API Symbols

- `assert_cli_independent_contract` (function) component `assert_cli_independent_contract [function]` (`44b94af2-7a42-5fd8-8e11-8fd9e7dcdf2a`) lines 34-42 [crates/gcode/src/lib.rs:34-42]
  - Signature: `fn assert_cli_independent_contract<T>()`
  - Purpose: Asserts at runtime that the generic type 'T' is CLI-independent by rejecting any type whose Rust type name contains 'commands::', 'output::', or 'clap'. [crates/gcode/src/lib.rs:34-42]
- `public_projection_api_is_cli_independent` (function) component `public_projection_api_is_cli_independent [function]` (`5d684f92-1512-5642-aecc-03e9de62f772`) lines 45-75 [crates/gcode/src/lib.rs:45-75]
  - Signature: `fn public_projection_api_is_cli_independent() {`
  - Purpose: Verifies that the projection-boundary source modules exist and that the listed public API types satisfy the 'assert_cli_independent_contract' invariant, ensuring the projection API remains independent of CLI-specific dependencies. [crates/gcode/src/lib.rs:45-75]
- `foundation_consumer_migration` (function) component `foundation_consumer_migration [function]` (`76b62a69-0285-5800-a977-6f72e0b92710`) lines 78-142 [crates/gcode/src/lib.rs:78-142]
  - Signature: `fn foundation_consumer_migration() {`
  - Purpose: Verifies that 'gobby-code' has migrated foundation consumers to 'gobby-core' by asserting required Cargo features and checking source files use the new config, PostgreSQL, and home-resolution APIs while removing obsolete local implementations. [crates/gcode/src/lib.rs:78-142]
- `indexing_search_primitive_migration` (function) component `indexing_search_primitive_migration [function]` (`95e75a28-a70e-5a1b-8aaa-71ae12e30565`) lines 145-179 [crates/gcode/src/lib.rs:145-179]
  - Signature: `fn indexing_search_primitive_migration() {`
  - Purpose: Verifies that indexing/search primitives have been migrated to 'gobby_core' by reading several source files and asserting they reference the core APIs while no longer containing the old local builder, buffer, RRF constant, or chunk-related imports/implementations. [crates/gcode/src/lib.rs:145-179]
- `falkor_facade_uses_core_graph_client_only` (function) component `falkor_facade_uses_core_graph_client_only [function]` (`cfc552f0-c9a6-5fa2-a439-52249205114c`) lines 182-211 [crates/gcode/src/lib.rs:182-211]
  - Signature: `fn falkor_facade_uses_core_graph_client_only() {`
  - Purpose: Recursively scans 'src/**/*.rs' for the string 'FalkorClientBuilder' and fails if any occurrence is found, enforcing use of 'gobby_core::falkor::GraphClient' instead of direct FalkorDB builder APIs. [crates/gcode/src/lib.rs:182-211]
- `visit` (function) component `visit [function]` (`75b50513-0d27-5c26-8b9e-617572bd7140`) lines 187-204 [crates/gcode/src/lib.rs:187-204]
  - Signature: `fn visit(path: &std::path::Path, offenders: &mut Vec<std::path::PathBuf>) {`
  - Purpose: Recursively traverses a directory tree, and for each '.rs' file whose contents contain the string 'FalkorClientBuilder', appends that file path to 'offenders'. [crates/gcode/src/lib.rs:187-204]

