---
title: crates/gcode/src/index/import_resolution/parser
type: code_module
provenance:
- file: crates/gcode/src/index/import_resolution/parser/go_rust.rs
- file: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
- file: crates/gcode/src/index/import_resolution/parser/lua.rs
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
- file: crates/gcode/src/index/import_resolution/parser/objc.rs
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
- file: crates/gcode/src/index/import_resolution/parser/python_js.rs
- file: crates/gcode/src/index/import_resolution/parser/rest.rs
- file: crates/gcode/src/index/import_resolution/parser/scala.rs
- file: crates/gcode/src/index/import_resolution/parser/shell.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser

Parent: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

## crates/gcode/src/index/import_resolution/parser

This module is the language-dispatch layer for import statement parsing within the gcode indexer's import resolution pipeline. Its sole public entry point, `parse_import_statement` (mod.rs:38), accepts a raw import text string, a language tag, a relative file path, and a shared `ImportResolutionContext`, then routes the call to the correct language-specific parser. Each language parser populates a mutable `ExtractedImports` accumulator with `ImportRelation` records and binding metadata drawn from `crate::models` (mod.rs:1). The module also re-exports three callee-resolution helpers — `resolve_lua_require_member_callee`, `resolve_objc_local_callee`, and `resolve_shell_local_callee` — giving upstream code access to language-specific call-site disambiguation without exposing the full submodule hierarchy (mod.rs:24–36).

Internally the module is split across nine language-family files. `go_rust.rs` handles Go block imports (`import (…)`) and Rust `use` trees, delegating external-module detection to `predicates::is_external_go_module` and `is_external_rust_root` (go_rust.rs:9). `php_kotlin.rs` parses PHP grouped `use` statements with `function`/`const`/class-like discrimination and Kotlin star-imports, calling `predicates::is_external_php_symbol` and `helpers::split_rust_use_group` (php_kotlin.rs:7). `scala.rs` recurses over comma-separated import selectors, expanding brace groups and wildcard suffixes into individual `ImportRelation` entries (scala.rs:36–51). `java_csharp.rs` re-exports a `csharp_global_qualifier_parts` helper consumed by callers outside this module (mod.rs:21). The four parsers for Dart, Elixir, Ruby, and Swift are consolidated in `rest.rs` (mod.rs:31–34).

The module sits between the parent `import_resolution` crate (which owns `ImportResolutionContext`, `ExtractedImports`, and the `UNPARSED_IMPORT_PREFIX` sentinel) and the concrete model layer (`crate::models::ImportRelation`, `Symbol`). It calls outward to sibling modules `context`, `predicates`, and `helpers` for shared resolution logic, and receives inbound calls exclusively through `parse_import_statement` from the parent orchestrator.

### Public API symbols exported from mod.rs

| Symbol | Kind | Notes |
|---|---|---|
| `parse_import_statement` | `pub(crate) fn` | Main dispatch; routes by `language` string tag (mod.rs:38) |
| `resolve_lua_require_member_callee` | `pub(crate) fn` | Re-exported from `lua` (mod.rs:24) |
| `resolve_objc_local_callee` | `pub(crate) fn` | Re-exported from `objc` (mod.rs:26) |
| `resolve_shell_local_callee` | `pub(crate) fn` | Re-exported from `shell` (mod.rs:36) |

### Language dispatch table

| `language` tag | Submodule | Parser function |
|---|---|---|
| `"python"` | `python_js` | `parse_python_import_statement` |
| `"javascript"` / `"typescript"` | `python_js` | `parse_js_import_statement` |
| `"go"` | `go_rust` | `parse_go_import_statement` |
| `"rust"` | `go_rust` | `parse_rust_import_statement` |
| `"java"` | `java_csharp` | `parse_java_import_statement` |
| `"csharp"` | `java_csharp` | `parse_csharp_import_statement` |
| `"php"` | `php_kotlin` | `parse_php_import_statement` |
| `"kotlin"` | `php_kotlin` | `parse_kotlin_import_statement` |
| `"scala"` | `scala` | `parse_scala_import_statement` |
| `"lua"` | `lua` | `parse_lua_import_statement` |
| `"objc"` | `objc` | `parse_objc_import_statement` |
| `"shell"` | `shell` | `parse_shell_import_statement` |
| `"dart"` | `rest` | `parse_dart_import_statement` |
| `"elixir"` | `rest` | `parse_elixir_import_statement` |
| `"ruby"` | `rest` | `parse_ruby_import_statement` |
| `"swift"` | `rest` | `parse_swift_import_statement` |

### Submodule symbol counts

| Submodule file | Indexed symbols |
|---|---|
| `php_kotlin.rs` | 10 |
| `mod.rs` | 13 |
| `go_rust.rs` | 7 |
| `scala.rs` | 7 |
| `lua.rs` | 6 |
| `java_csharp.rs` | 4 |
| `python_js.rs` | 4 |
| `rest.rs` | 4 |
| `shell.rs` | 4 |
| `objc.rs` | 3 |
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]
[crates/gcode/src/index/import_resolution/parser/lua.rs:6-44]
[crates/gcode/src/index/import_resolution/parser/mod.rs:40-69]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/import_resolution/parser/go_rust.rs\|crates/gcode/src/index/import_resolution/parser/go_rust.rs]] | `crates/gcode/src/index/import_resolution/parser/go_rust.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/parser/java_csharp.rs\|crates/gcode/src/index/import_resolution/parser/java_csharp.rs]] | `crates/gcode/src/index/import_resolution/parser/java_csharp.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/parser/lua.rs\|crates/gcode/src/index/import_resolution/parser/lua.rs]] | `crates/gcode/src/index/import_resolution/parser/lua.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/parser/mod.rs\|crates/gcode/src/index/import_resolution/parser/mod.rs]] | `crates/gcode/src/index/import_resolution/parser/mod.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/parser/objc.rs\|crates/gcode/src/index/import_resolution/parser/objc.rs]] | `crates/gcode/src/index/import_resolution/parser/objc.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/parser/php_kotlin.rs\|crates/gcode/src/index/import_resolution/parser/php_kotlin.rs]] | `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/parser/python_js.rs\|crates/gcode/src/index/import_resolution/parser/python_js.rs]] | `crates/gcode/src/index/import_resolution/parser/python_js.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/parser/rest.rs\|crates/gcode/src/index/import_resolution/parser/rest.rs]] | `crates/gcode/src/index/import_resolution/parser/rest.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/parser/scala.rs\|crates/gcode/src/index/import_resolution/parser/scala.rs]] | `crates/gcode/src/index/import_resolution/parser/scala.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/parser/shell.rs\|crates/gcode/src/index/import_resolution/parser/shell.rs]] | `crates/gcode/src/index/import_resolution/parser/shell.rs` exposes 4 indexed API symbols. |

