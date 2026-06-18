---
title: crates/gcode/src/index/import_resolution/parser/shell.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/shell.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/shell.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/shell.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/shell.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_shell_import_statement` | function | Parses a shell 'source' or '.' import statement, extracts the referenced path from quoted or unquoted syntax, records an 'ImportRelation' for 'rel_path', and, if it can resolve the target, appends that resolved source file to 'extracted.bindings.shell_source_files'. [crates/gcode/src/index/import_resolution/parser/shell.rs:8-40] |
| `resolve_shell_local_callee` | function | Returns a 'LocalCallBinding' for 'callee_name' using the unique sorted shell source files from 'import_bindings' only when the call is bare and no symbol in 'symbols' already matches that name, otherwise 'None'. [crates/gcode/src/index/import_resolution/parser/shell.rs:42-57] |
| `shell_source_target` | function | Returns a normalized project path for 'source_path' resolved relative to 'rel_path'’s parent, but only if 'source_path' is a non-absolute, non-shell-expanded relative path without drive/root/prefix components, otherwise returns 'None'. [crates/gcode/src/index/import_resolution/parser/shell.rs:59-78] |
| `normalize_project_path` | function | Normalizes a relative 'Path' by removing '.' components, resolving '..' against prior segments, rejecting rooted or prefixed paths, and returning a non-empty UTF-8-lossy string with backslashes converted to forward slashes, or 'None' if normalization fails. [crates/gcode/src/index/import_resolution/parser/shell.rs:80-96] |

