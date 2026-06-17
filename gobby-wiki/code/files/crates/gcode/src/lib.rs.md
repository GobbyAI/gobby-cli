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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/lib.rs:34-42](crates/gcode/src/lib.rs#L34-L42), [crates/gcode/src/lib.rs:45-75](crates/gcode/src/lib.rs#L45-L75), [crates/gcode/src/lib.rs:78-142](crates/gcode/src/lib.rs#L78-L142), [crates/gcode/src/lib.rs:145-179](crates/gcode/src/lib.rs#L145-L179), [crates/gcode/src/lib.rs:182-211](crates/gcode/src/lib.rs#L182-L211)

</details>

# crates/gcode/src/lib.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This crate root wires together the `gcode` library by exposing the main domain modules for commands, config, graph, indexing, projection, search, vector, and related support code, while re-exporting the primary indexing API from `index::api` for external use. Its test module enforces the public projection boundary: it verifies key projection-related source files exist and asserts that the serializable request/output types used by the public API stay independent of CLI-only internals such as `commands`, `output`, and `clap`.
[crates/gcode/src/lib.rs:34-42]
[crates/gcode/src/lib.rs:45-75]
[crates/gcode/src/lib.rs:78-142]
[crates/gcode/src/lib.rs:145-179]
[crates/gcode/src/lib.rs:182-211]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `assert_cli_independent_contract` | function | `fn assert_cli_independent_contract<T>()` | `assert_cli_independent_contract [function]` | `44b94af2-7a42-5fd8-8e11-8fd9e7dcdf2a` | 34-42 [crates/gcode/src/lib.rs:34-42] | Indexed function `assert_cli_independent_contract` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:34-42] |
| `public_projection_api_is_cli_independent` | function | `fn public_projection_api_is_cli_independent() {` | `public_projection_api_is_cli_independent [function]` | `5d684f92-1512-5642-aecc-03e9de62f772` | 45-75 [crates/gcode/src/lib.rs:45-75] | Indexed function `public_projection_api_is_cli_independent` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:45-75] |
| `foundation_consumer_migration` | function | `fn foundation_consumer_migration() {` | `foundation_consumer_migration [function]` | `76b62a69-0285-5800-a977-6f72e0b92710` | 78-142 [crates/gcode/src/lib.rs:78-142] | Indexed function `foundation_consumer_migration` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:78-142] |
| `indexing_search_primitive_migration` | function | `fn indexing_search_primitive_migration() {` | `indexing_search_primitive_migration [function]` | `95e75a28-a70e-5a1b-8aaa-71ae12e30565` | 145-179 [crates/gcode/src/lib.rs:145-179] | Indexed function `indexing_search_primitive_migration` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:145-179] |
| `falkor_facade_uses_core_graph_client_only` | function | `fn falkor_facade_uses_core_graph_client_only() {` | `falkor_facade_uses_core_graph_client_only [function]` | `cfc552f0-c9a6-5fa2-a439-52249205114c` | 182-211 [crates/gcode/src/lib.rs:182-211] | Indexed function `falkor_facade_uses_core_graph_client_only` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:182-211] |
| `visit` | function | `fn visit(path: &std::path::Path, offenders: &mut Vec<std::path::PathBuf>) {` | `visit [function]` | `75b50513-0d27-5c26-8b9e-617572bd7140` | 187-204 [crates/gcode/src/lib.rs:187-204] | Indexed function `visit` in `crates/gcode/src/lib.rs`. [crates/gcode/src/lib.rs:187-204] |
