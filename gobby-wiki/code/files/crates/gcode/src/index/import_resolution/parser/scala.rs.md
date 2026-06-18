---
title: crates/gcode/src/index/import_resolution/parser/scala.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/scala.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/scala.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/scala.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/scala.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_scala_import_statement` | function | Trims a Scala import statement, verifies it starts with 'import ', splits the remaining text on top-level commas, and registers each import item via 'register_scala_import_or_group', ignoring malformed input. [crates/gcode/src/index/import_resolution/parser/scala.rs:6-23] |
| `register_scala_import_or_group` | function | Trims a Scala import string, recursively expands grouped selectors, records wildcard module imports, and otherwise delegates a single import item to 'register_scala_import_item' while appending discovered import relations to 'extracted'. [crates/gcode/src/index/import_resolution/parser/scala.rs:25-57] |
| `register_scala_import_item` | function | Parses a Scala import item, records its module relation, and either binds its alias to the target directly or resolves the target’s package files to register local member/bare bindings while clearing conflicting aliases. [crates/gcode/src/index/import_resolution/parser/scala.rs:59-103] |
| `split_scala_import_group` | function | Returns 'Some((base, group))' by delegating to 'split_rust_use_group', then trimming whitespace and trailing dots from the base and rejecting the result if either the normalized base or the group is empty, otherwise returns 'None'. [crates/gcode/src/index/import_resolution/parser/scala.rs:105-112] |
| `scala_join_import_path` | function | Trims the 'prefix' and 'item', returns 'None' if the item path is empty, otherwise joins them with a '.' and appends ' as <alias>' when a non-empty Scala alias is present. [crates/gcode/src/index/import_resolution/parser/scala.rs:114-131] |
| `scala_wildcard_module` | function | Returns the dot-joined Scala module prefix before the first wildcard segment ('_' or '*') in the alias-stripped item path, ignoring empty segments and yielding 'None' if no wildcard is present or the prefix is empty. [crates/gcode/src/index/import_resolution/parser/scala.rs:133-145] |
| `split_scala_alias` | function | Returns the input split into a trimmed target and optional alias by first deferring to 'split_alias', and if that yields no alias, parsing the first '=>' delimiter with trimmed sides or otherwise returning the trimmed input with 'None'. [crates/gcode/src/index/import_resolution/parser/scala.rs:147-155] |

