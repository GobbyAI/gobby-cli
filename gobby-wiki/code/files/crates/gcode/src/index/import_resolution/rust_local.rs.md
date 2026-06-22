---
title: crates/gcode/src/index/import_resolution/rust_local.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/rust_local.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/rust_local.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/rust_local.rs` exposes 16 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/rust_local.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `RustLocalTarget` | class | 'RustLocalTarget' is a crate-visible struct that identifies a local Rust target by its source root, module path, and target name. [crates/gcode/src/index/import_resolution/rust_local.rs:5-9] |
| `RustModuleContext` | class | 'RustModuleContext' is a simple data holder that identifies a Rust module by storing the source root path and the module name as strings. [crates/gcode/src/index/import_resolution/rust_local.rs:12-15] |
| `rust_candidate_files` | function | Returns the two plausible Rust source file paths for a module under 'source_root' by trimming trailing slashes from the root, mapping '::' to '/', and emitting either 'lib.rs'/'main.rs' for the empty module or '<module>.rs' and '<module>/mod.rs' otherwise. [crates/gcode/src/index/import_resolution/rust_local.rs:23-33] |
| `rust_import_target` | function | Resolves a Rust import path into a 'RustLocalTarget' by deriving the module context from 'rel_path', splitting 'path' into module segments and an अंतिम name, looking up the module with crate/external-crate context, and returning the source root, resolved module, and target name, or 'None' if any step fails. [crates/gcode/src/index/import_resolution/rust_local.rs:35-55] |
| `rust_qualified_call_target` | function | Resolves a qualified Rust call target by deriving the module context from 'rel_path', mapping 'qualifier_path' into a module using the current crate and external crate set, and returning a 'RustLocalTarget' with that source root, module, and 'callee_name' if resolution succeeds. [crates/gcode/src/index/import_resolution/rust_local.rs:57-73] |
| `rust_module_context_for_rel_path` | function | It parses a relative path to the last 'src' directory, requires a '.rs' file under it, and returns a 'RustModuleContext' containing the 'src'-anchored source root and a '::'-joined module path derived from the path components, omitting 'lib', 'main', or 'mod' as terminal module names. [crates/gcode/src/index/import_resolution/rust_local.rs:75-93] |
| `rust_module_for_segments` | function | Resolves a Rust path segment slice into a module path string relative to the current 'RustModuleContext', handling 'crate'/'self'/'super', suppressing standard and external crate roots, and otherwise joining the segments into the current module path. [crates/gcode/src/index/import_resolution/rust_local.rs:95-111] |
| `rust_super_module` | function | Returns the parent module path of 'current_module' by removing its last '::'-separated segment, appending the 'rest' segments, and joining the result back into a '::'-delimited string. [crates/gcode/src/index/import_resolution/rust_local.rs:113-123] |
| `join_rust_module` | function | 'join_rust_module' splits 'base' on '::', removes empty segments, appends all strings from 'rest', and returns the combined Rust module path joined with '::'. [crates/gcode/src/index/import_resolution/rust_local.rs:125-129] |
| `rust_path_segments` | function | Splits a Rust path string on '::', trims whitespace from each segment, filters out empty segments, and returns the remaining segments as '&str' slices in a 'Vec'. [crates/gcode/src/index/import_resolution/rust_local.rs:131-136] |

_Verified by 6 in-file unit tests._

