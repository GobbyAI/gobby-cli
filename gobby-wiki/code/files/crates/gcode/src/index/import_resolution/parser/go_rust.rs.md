---
title: crates/gcode/src/index/import_resolution/parser/go_rust.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/go_rust.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/go_rust.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/go_rust.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/go_rust.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_go_import_statement` | function | Parses a Go 'import' statement by validating the 'import' prefix, then either iterating over each line in a parenthesized import block or parsing a single import spec, forwarding each spec to 'parse_go_import_spec' and returning an error if the input is not a valid Go import statement. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] |
| `parse_go_import_spec` | function | Parses a Go import declaration, records the imported module, resolves its effective alias, ignores blank/dot imports, binds external imports as member aliases, and for same-module imports maps the alias to candidate package files after clearing conflicting bindings. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-96] |
| `parse_rust_import_statement` | function | Parses a Rust 'use' statement, records the resolved import string as an 'ImportRelation', and either expands grouped imports via 'split_rust_use_group', skips glob imports, or registers a single path import with the provided resolution context. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:98-125] |
| `register_rust_group_imports` | function | 'register_rust_group_imports' parses a Rust 'use' group into top-level comma-separated items, recursively expands nested grouped imports by joining prefixes, skips empty/wildcard entries and invalid path joins, and registers each resolved path import into 'extracted' with the given 'rel_path' and 'import_context'. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:127-162] |
| `register_rust_path_import` | function | Registers a Rust path import by trimming and parsing an optional alias, preferring a local import candidate when resolvable and otherwise recording an external root, bare binding, and member mapping for the imported path in 'ExtractedImports'. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:164-229] |
| `non_import_go_statement_does_not_record_raw_import` | function | Verifies that 'parse_go_import_statement' returns an error for a non-'import' Go statement ('"package main"') and leaves 'ExtractedImports.imports' empty, so no raw import is recorded. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:236-247] |
| `non_use_rust_statement_does_not_record_raw_import` | function | Verifies that parsing a non-'use' Rust statement ('mod tests;') does not record any raw imports in 'ExtractedImports'. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:250-260] |

