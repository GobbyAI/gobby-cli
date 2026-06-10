---
title: crates/gcode/src/lib.rs
type: code_file
provenance:
- file: crates/gcode/src/lib.rs
  ranges:
  - 34-42
  - 45-75
  - 78-139
  - 142-169
  - 172-201
  - 177-194
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/lib.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/lib.rs` exposes 6 indexed API symbols.
[crates/gcode/src/lib.rs:34-42]
[crates/gcode/src/lib.rs:45-75]
[crates/gcode/src/lib.rs:78-139]
[crates/gcode/src/lib.rs:142-169]
[crates/gcode/src/lib.rs:172-201]
[crates/gcode/src/lib.rs:177-194]

## API Symbols

- `assert_cli_independent_contract` (function) component `assert_cli_independent_contract [function]` (`44b94af2-7a42-5fd8-8e11-8fd9e7dcdf2a`) lines 34-42 [crates/gcode/src/lib.rs:34-42]
  - Signature: `fn assert_cli_independent_contract<T>()`
  - Purpose: Asserts that a serializable generic type has no compile-time coupling to CLI-specific modules (commands, output) or the clap framework by validating its type name contains no CLI-related paths. [crates/gcode/src/lib.rs:34-42]
- `public_projection_api_is_cli_independent` (function) component `public_projection_api_is_cli_independent [function]` (`5d684f92-1512-5642-aecc-03e9de62f772`) lines 45-75 [crates/gcode/src/lib.rs:45-75]
  - Signature: `fn public_projection_api_is_cli_independent() {`
  - Purpose: # Summary

This function validates that all public API types across the index, graph, vector, and projection modules satisfy a CLI-independence contract by asserting their compliance through compile-time type checks. [crates/gcode/src/lib.rs:45-75]
- `foundation_consumer_migration` (function) component `foundation_consumer_migration [function]` (`76b62a69-0285-5800-a977-6f72e0b92710`) lines 78-139 [crates/gcode/src/lib.rs:78-139]
  - Signature: `fn foundation_consumer_migration() {`
  - Purpose: Verifies that the gobby-code consumer crate has completed its migration to gobby-core by asserting the presence of required Cargo features and the replacement of local implementations with gobby-core config and database abstractions. [crates/gcode/src/lib.rs:78-139]
- `indexing_search_primitive_migration` (function) component `indexing_search_primitive_migration [function]` (`9eebeec4-86ac-5d90-be19-b3c05821bb8c`) lines 142-169 [crates/gcode/src/lib.rs:142-169]
  - Signature: `fn indexing_search_primitive_migration() {`
  - Purpose: Validates that indexing and search modules have successfully migrated from local primitive implementations to gobby_core library exports by asserting the presence of required external imports and the absence of superseded local code. [crates/gcode/src/lib.rs:142-169]
- `falkor_facade_uses_core_graph_client_only` (function) component `falkor_facade_uses_core_graph_client_only [function]` (`24bf6fbf-f9ea-56ea-be51-078fc05e7933`) lines 172-201 [crates/gcode/src/lib.rs:172-201]
  - Signature: `fn falkor_facade_uses_core_graph_client_only() {`
  - Purpose: This function performs a build-time assertion that recursively scans all Rust source files to verify no code directly instantiates `FalkorClientBuilder`, enforcing exclusive use of the `gobby_core::falkor::GraphClient` facade. [crates/gcode/src/lib.rs:172-201]
- `visit` (function) component `visit [function]` (`34f90854-d409-513f-a3a2-d02ddb12a7f1`) lines 177-194 [crates/gcode/src/lib.rs:177-194]
  - Signature: `fn visit(path: &std::path::Path, offenders: &mut Vec<std::path::PathBuf>) {`
  - Purpose: Recursively traverses a directory tree to collect paths of Rust source files (`.rs`) that contain the concatenated string `"FalkorClientBuilder"` into a mutable vector. [crates/gcode/src/lib.rs:177-194]

