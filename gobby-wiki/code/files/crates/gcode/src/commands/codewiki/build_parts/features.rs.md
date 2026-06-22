---
title: crates/gcode/src/commands/codewiki/build_parts/features.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/features.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/features.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/features.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/features.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Contract` | class | The 'Contract' struct represents a contract definition containing a sequence of 'ContractCommand' objects that defaults to an empty vector during deserialization. [crates/gcode/src/commands/codewiki/build_parts/features.rs:16-19] |
| `ContractCommand` | class | The 'ContractCommand' struct represents a command definition containing a name, a default-initialized summary, and a default-initialized vector of associated contract flags. [crates/gcode/src/commands/codewiki/build_parts/features.rs:22-28] |
| `ContractFlag` | class | The 'ContractFlag' struct represents a contract flag containing a single deserializable 'name' string field that defaults to its standard default value if omitted during deserialization. [crates/gcode/src/commands/codewiki/build_parts/features.rs:31-34] |
| `BinaryContract` | class | The 'BinaryContract' struct holds metadata that maps a binary's display name to its respective workspace crate directory and contract file path. [crates/gcode/src/commands/codewiki/build_parts/features.rs:39-46] |
| `resolve_handler` | function | The 'resolve_handler' function matches a given binary name to delegate command resolution to either 'resolve_gcode_handler' or 'resolve_gwiki_handler', returning a static string slice tuple, and defaults to a pair of empty string slices for any unmatched binary. [crates/gcode/src/commands/codewiki/build_parts/features.rs:71-77] |
| `resolve_gcode_handler` | function | The 'resolve_gcode_handler' function maps a command string slice to a tuple of static string slices representing the file path and Rust path identifier of its corresponding command handler. [crates/gcode/src/commands/codewiki/build_parts/features.rs:82-231] |
| `resolve_gwiki_handler` | function | The function maps a command string slice to a tuple of static string slices representing the file path and fully qualified execute function path of the corresponding command handler. [crates/gcode/src/commands/codewiki/build_parts/features.rs:236-326] |
| `section_for_binary` | function | It reads a JSON contract file for the specified crate, converts each command into a 'FeatureEntry' by resolving its handler and collecting up to 'MAX_KEY_FLAGS' non-empty flag names, and returns a 'FeatureBinarySection' for the target binary, or 'None' if the file cannot be read or parsed. [crates/gcode/src/commands/codewiki/build_parts/features.rs:331-369] |
| `build_feature_catalog_doc` | function | Builds a 'FeatureCatalogDoc' by collecting per-binary sections from 'BINARIES' via 'section_for_binary(repo_root, ...)' and returns 'None' if no sections are found, otherwise returns a doc with those sections and an empty 'degraded_sources' list. [crates/gcode/src/commands/codewiki/build_parts/features.rs:382-400] |

