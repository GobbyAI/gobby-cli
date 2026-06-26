---
title: crates/gcode/src/commands/codewiki/system_model.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/system_model.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/system_model.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/system_model.rs` exposes 29 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/system_model.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Crate` | class | The 'Crate' struct represents a Cargo package within a workspace, storing its package name, workspace-relative directory path, and boolean flags indicating whether it contains binary or library targets. [crates/gcode/src/commands/codewiki/system_model.rs:30-39] |
| `Edge` | class | The 'Edge' struct represents a directed dependency relationship in a workspace dependency graph, storing the package name of the depending crate in 'from' and the package name of the depended-upon workspace member in 'to'. [crates/gcode/src/commands/codewiki/system_model.rs:45-50] |
| `ServiceKind` | type | Indexed type `ServiceKind` in `crates/gcode/src/commands/codewiki/system_model.rs`. [crates/gcode/src/commands/codewiki/system_model.rs:54-81] |
| `ServiceKind::kind_slug` | method | This method returns the static string slug representation of an enum variant by exhaustively pattern matching 'self' to its corresponding identifier string. [crates/gcode/src/commands/codewiki/system_model.rs:84-96] |
| `ServiceBoundary` | class | 'ServiceBoundary' is a struct that encapsulates a named service boundary with an associated kind and a deduplicated, sorted list of crate-feature pairs responsible for introducing it. [crates/gcode/src/commands/codewiki/system_model.rs:101-110] |
| `RuntimeMode` | type | Indexed type `RuntimeMode` in `crates/gcode/src/commands/codewiki/system_model.rs`. [crates/gcode/src/commands/codewiki/system_model.rs:114-121] |
| `SystemModel` | class | SystemModel is a data structure that encapsulates a workspace's structural metadata: member crates, inter-crate dependency edges, service boundaries, runtime modes, per-crate gobby-core feature configurations, and extraction notes. [crates/gcode/src/commands/codewiki/system_model.rs:126-142] |
| `SystemModel::digest` | method | This method serializes the struct to JSON bytes and returns the computed content hash of the serialized representation as a String. [crates/gcode/src/commands/codewiki/system_model.rs:153-156] |
| `build_system_model` | function | # Summary This function constructs a 'SystemModel' by parsing Cargo.toml manifests from all workspace members to extract crate metadata (names, paths, and target types) for dependency graph analysis. [crates/gcode/src/commands/codewiki/system_model.rs:164-278] |
| `workspace_members` | function | Parses the root Cargo.toml manifest and returns workspace member names extracted from the [workspace].members TOML array as a string vector, appending any I/O or parsing errors to the notes vector. [crates/gcode/src/commands/codewiki/system_model.rs:282-316] |
| `package_name` | function | Extracts the "package.name" field from a TOML manifest value and returns it as an owned 'String', or 'None' if the field is missing or not a string. [crates/gcode/src/commands/codewiki/system_model.rs:319-325] |
| `has_table_array` | function | Checks if a TOML manifest contains a non-empty array at the specified key. [crates/gcode/src/commands/codewiki/system_model.rs:329-334] |
| `dependency_entries` | function | Collects all dependency entries from the "dependencies", "dev-dependencies", and "build-dependencies" tables of a TOML manifest into a vector of (String, toml::Value) tuples. [crates/gcode/src/commands/codewiki/system_model.rs:340-351] |
| `dependency_features` | function | Extracts the "features" array from a TOML dependency value, converts its string elements to a 'Vec<String>', sorts it, deduplicates it, and returns the result. [crates/gcode/src/commands/codewiki/system_model.rs:356-370] |
| `feature_table_keys` | function | Returns a sorted set of all key names from the 'features' table in a TOML manifest value, or an empty set if the table is absent. [crates/gcode/src/commands/codewiki/system_model.rs:374-380] |
| `feature_services` | function | 'feature_services' returns a static slice of 'ServiceKind' enum variants corresponding to the given feature name string, or an empty slice if the feature is unrecognized. [crates/gcode/src/commands/codewiki/system_model.rs:385-393] |
| `service_name` | function | Converts a 'ServiceKind' enum variant to its corresponding static string service name via pattern matching. [crates/gcode/src/commands/codewiki/system_model.rs:396-408] |
| `service_boundaries` | function | Constructs service boundaries by mapping service kinds to their crate/feature provenance strings, with special-case entries for ghook inbox and daemon resolver services. [crates/gcode/src/commands/codewiki/system_model.rs:414-481] |
| `toolchain_boundaries` | function | This function identifies external service toolchain boundaries (tree-sitter, document processing, media FFmpeg) used by crates by analyzing dependency declarations, feature flags, and source file presence, returning a vector of (ServiceKind, String) tuples describing each detected toolchain and its associated crate. [crates/gcode/src/commands/codewiki/system_model.rs:497-546] |
| `fixture_workspace` | function | Creates a temporary Rust workspace fixture by generating a root 'Cargo.toml' with specified members and corresponding member crate directories, returning both the 'TempDir' handle and workspace root 'PathBuf'. [crates/gcode/src/commands/codewiki/system_model.rs:556-575] |
| `crate_named` | function | Returns a reference to a 'Crate' from a 'SystemModel' matching the given name, or panics if the crate is not found. [crates/gcode/src/commands/codewiki/system_model.rs:577-583] |

_Verified by 8 in-file unit tests._

