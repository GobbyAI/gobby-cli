---
title: crates/gcode/src/index/import_resolution/context/package_metadata.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/package_metadata.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context/package_metadata.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]

## Overview

`crates/gcode/src/index/import_resolution/context/package_metadata.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/context/package_metadata.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `load_js_external_packages` | function | Reads 'package.json' from 'root_path', parses it as JSON, and returns the union of package names listed under 'dependencies', 'devDependencies', 'peerDependencies', 'optionalDependencies', 'bundledDependencies', and 'bundleDependencies', yielding an empty set on file or parse failure. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38] |
| `load_js_self_package_name` | function | Attempts to read '<root_path>/package.json', parse it as JSON, and return the '"name"' field as an owned 'String' if it exists and is a string, otherwise 'None'. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:40-49] |
| `load_go_module_path` | function | Reads '<root_path>/go.mod', parses it as text, and returns the first non-empty 'module' directive value as 'Some(String)', or 'None' if the file cannot be read or no valid module line is found. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:51-60] |
| `build_go_package_files` | function | Builds a 'HashMap' from each relative directory under 'root_path' to a sorted, deduplicated list of canonicalized '.go' file paths from 'candidate_files', skipping non-Go files and any path that cannot be resolved relative to the canonicalized root. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97] |
| `canonical_relative_path` | function | Resolves 'path' to its canonical absolute form and returns the path relative to 'root_abs' if the canonicalized path is under that root, otherwise 'None'. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:99-102] |
| `load_rust_external_crates` | function | Traverses all Rust manifest paths under 'root_path', parses each readable 'Cargo.toml' into a TOML table, extracts dependency keys from top-level and target-specific 'dependencies', 'dev-dependencies', and 'build-dependencies' sections, and returns the unique crate names as a 'HashSet<String>'. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:104-130] |
| `rust_manifest_paths` | function | Returns a sorted, deduplicated list of Rust 'Cargo.toml' manifest paths starting with the root manifest and, if the root manifest defines a workspace, adding each existing member manifest by direct path or glob expansion under 'root_path'. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:132-172] |
| `load_rust_self_crate_name` | function | Reads 'Cargo.toml' from 'root_path', parses it as TOML, extracts 'package.name', normalizes it as a Rust crate name, and returns it only if non-empty, otherwise 'None'. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:174-185] |
| `collect_rust_dependency_keys` | function | Collects all dependency table keys from an optional TOML value, normalizes each key as a Rust crate name, and inserts every non-empty normalized name into the provided 'HashSet<String>'. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:187-197] |
| `normalize_rust_crate_name` | function | Trims leading and trailing whitespace from 'name' and replaces every '-' with '_' to produce a normalized Rust crate name. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:199-201] |
| `load_dart_external_packages` | function | Reads 'pubspec.yaml' from 'root_path', parses it as YAML, and returns the set of non-empty package names found under 'dependencies', 'dev_dependencies', and 'dependency_overrides', excluding the 'sdk' key, or an empty set if the file cannot be read or parsed. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:203-224] |
| `load_dart_self_package_name` | function | Reads 'pubspec.yaml' from 'root_path', parses it as YAML, and returns the top-level 'name' field as an owned 'String' if it exists and is a string, otherwise 'None'. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:226-234] |
| `symlink_dir` | function | Creates a Unix symbolic link at 'link' that points to the directory path 'target', returning the 'std::io::Result<()>' from 'std::os::unix::fs::symlink'. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:242-244] |
| `symlink_dir` | function | Creates a Windows directory symbolic link at 'link' that points to 'target', returning the underlying 'std::io::Result<()>' from 'std::os::windows::fs::symlink_dir'. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:247-249] |

_Verified by 1 in-file unit test._

