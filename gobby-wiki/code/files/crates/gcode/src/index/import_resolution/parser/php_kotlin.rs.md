---
title: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/php_kotlin.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/php_kotlin.rs` exposes 10 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/php_kotlin.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `php_local_symbol_exists` | function | Returns 'true' if the given symbol name, lowercased with ASCII rules, is present in 'import_context.php_local_symbols', and 'false' otherwise. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16] |
| `parse_php_import_statement` | function | Parses a PHP 'use' import statement, classifies it as class-like/function/const, expands grouped imports or comma-separated items, and registers each resolved import or wildcard into 'ExtractedImports' while skipping malformed brace-group syntax. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:18-61] |
| `PhpImportKind` | type | Indexed type `PhpImportKind` in `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs`. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:64-68] |
| `parse_kotlin_import_statement` | function | Parses a Kotlin 'import' declaration, records the imported module path in 'extracted.imports', ignores wildcard imports, derives the imported symbol and optional alias, and binds the alias for external or local resolution in 'ExtractedImports' using 'ImportResolutionContext'. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:70-136] |
| `register_php_import_item` | function | Trims and parses a PHP import item, records its import relation, derives a local alias, and then either seeds a local import or registers an external import binding as a bare function callee or member symbol depending on whether the target is external and the import kind. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:138-189] |
| `seed_php_local_import` | function | Seeds a PHP local import by resolving candidate files for 'target', skipping constants, removing any existing bare binding for 'local_alias', inserting a named local bare binding for 'imported_name', and, for class-like imports, also replacing member bindings with the resolved candidate files. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:199-226] |
| `register_php_import_or_wildcard` | function | Registers a PHP import as a wildcard module relation when 'item' resolves to a wildcard module, adding it to 'extracted.imports' and tracking external bare wildcard modules, otherwise delegating to 'register_php_import_item'. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:228-247] |
| `php_wildcard_module` | function | Returns the backslash-joined namespace/module prefix of 'item' before the first '*' segment after alias stripping and leading-'\' trimming, or 'None' if no wildcard exists or the prefix is empty. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:249-262] |
| `split_php_use_group` | function | Returns 'Some((base, group))' when 'split_rust_use_group(text)' yields non-empty 'base' and 'group' components, otherwise returns 'None'. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:264-270] |
| `php_join_use_path` | function | Builds a PHP 'use' path by trimming whitespace and leading backslashes from 'prefix' and 'item', returning 'None' if the item path is empty, otherwise concatenating them with a single '\' separator as needed and appending ' as <alias>' when a non-empty alias is present. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:272-292] |

