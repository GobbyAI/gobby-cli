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

`crates/gcode/src/commands/codewiki/system_model.rs` exposes 28 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/system_model.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Crate` | class | The 'Crate' struct represents a Cargo package within a workspace, storing its package name, workspace-relative directory path, and boolean flags indicating whether it contains binary or library targets. [crates/gcode/src/commands/codewiki/system_model.rs:30-39] |
| `Edge` | class | The 'Edge' struct represents a directed dependency relationship in a workspace dependency graph, storing the package name of the depending crate in 'from' and the package name of the depended-upon workspace member in 'to'. [crates/gcode/src/commands/codewiki/system_model.rs:45-50] |
| `ServiceKind` | type | Indexed type `ServiceKind` in `crates/gcode/src/commands/codewiki/system_model.rs`. [crates/gcode/src/commands/codewiki/system_model.rs:54-81] |
| `ServiceBoundary` | class | The 'ServiceBoundary' struct represents a service boundary defined by a stable, human-readable name, its service kind, and a sorted, de-duplicated collection of crate and feature pairs that import the boundary. [crates/gcode/src/commands/codewiki/system_model.rs:85-94] |
| `RuntimeMode` | type | Indexed type `RuntimeMode` in `crates/gcode/src/commands/codewiki/system_model.rs`. [crates/gcode/src/commands/codewiki/system_model.rs:98-105] |
| `SystemModel` | class | 'SystemModel' is a structural representation of a workspace that details its member crates, internal dependency edges, service boundaries, operational runtime modes, enabled core features per crate, and diagnostic notes recorded during partial model extraction. [crates/gcode/src/commands/codewiki/system_model.rs:110-126] |
| `SystemModel::digest` | method | This method serializes the instance into a JSON-formatted byte vector, falling back to an empty vector on failure, and returns the computed content hash of the serialized data as a string. [crates/gcode/src/commands/codewiki/system_model.rs:137-140] |
| `build_system_model` | function | The 'build_system_model' function parses the Cargo manifests of workspace members under a given repository root to build a 'SystemModel' detailing each crate's name, path, and target classification as a library or binary. [crates/gcode/src/commands/codewiki/system_model.rs:148-262] |
| `workspace_members` | function | This function parses the 'Cargo.toml' manifest at the specified repository root to extract and return its workspace member paths as a 'Vec<String>', while appending any file access, parsing, or structural errors as diagnostics to the provided 'notes' vector. [crates/gcode/src/commands/codewiki/system_model.rs:266-300] |
| `package_name` | function | This function extracts the string value of the 'name' key nested under the 'package' table of a TOML manifest, returning it as an 'Option<String>'. [crates/gcode/src/commands/codewiki/system_model.rs:303-309] |
| `has_table_array` | function | Checks whether a TOML manifest value contains a non-empty array associated with a specified key, returning 'true' if the key exists as a populated array and 'false' otherwise. [crates/gcode/src/commands/codewiki/system_model.rs:313-318] |
| `dependency_entries` | function | The 'dependency_entries' function extracts and returns a vector of key-value tuples representing dependency names and their TOML definitions from the "dependencies", "dev-dependencies", and "build-dependencies" tables of a given TOML manifest. [crates/gcode/src/commands/codewiki/system_model.rs:324-335] |
| `dependency_features` | function | The function extracts, sorts, and deduplicates string elements from a "features" array within a TOML dependency value, returning them as a 'Vec<String>'. [crates/gcode/src/commands/codewiki/system_model.rs:340-354] |
| `feature_table_keys` | function | This function extracts and returns the keys of the 'features' table from a TOML manifest value as a sorted 'BTreeSet<String>', returning an empty set if the 'features' key is missing or its value is not a table. [crates/gcode/src/commands/codewiki/system_model.rs:358-364] |
| `feature_services` | function | The 'feature_services' function maps a feature name string slice to a static slice of 'ServiceKind' enum variants representing the required services for that feature, defaulting to an empty slice for unrecognized inputs. [crates/gcode/src/commands/codewiki/system_model.rs:369-377] |
| `service_name` | function | The 'service_name' function maps a 'ServiceKind' enum variant to its corresponding static string slice representation. [crates/gcode/src/commands/codewiki/system_model.rs:380-392] |
| `service_boundaries` | function | The 'service_boundaries' function maps core crate features, workspace binary layouts, and on-disk repository structures to their respective service categories to construct and return a collection of service boundaries complete with provenance metadata. [crates/gcode/src/commands/codewiki/system_model.rs:398-465] |
| `toolchain_boundaries` | function | The 'toolchain_boundaries' function analyzes crate dependencies, features, and workspace source files to identify and return a list of crates mapped to their required external toolchains ('TreeSitter', 'DocumentToolchain', or 'MediaToolchain'). [crates/gcode/src/commands/codewiki/system_model.rs:481-530] |
| `fixture_workspace` | function | The 'fixture_workspace' function creates a temporary Cargo workspace by generating a root 'Cargo.toml' manifest with specified member paths and initializing each member's subdirectory with its corresponding 'Cargo.toml' file and a 'src/' folder, returning both the 'tempfile::TempDir' guard and the workspace root path. [crates/gcode/src/commands/codewiki/system_model.rs:540-559] |
| `crate_named` | function | The 'crate_named' function returns a reference to the 'Crate' with the specified name from the given 'SystemModel', panicking if no matching crate is found. [crates/gcode/src/commands/codewiki/system_model.rs:561-567] |

_Verified by 8 in-file unit tests._

