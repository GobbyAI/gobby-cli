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

The `parser` module is the language dispatcher for import resolution. It accepts a language, import text, relative file path, shared `ImportResolutionContext`, and mutable `ExtractedImports`, then routes to the appropriate language-specific parser for Python, JS/TS, Go, Rust, Java, C#, PHP, Kotlin, Scala, Lua, Objective-C, shell, and several “rest” languages (`crates/gcode/src/index/import_resolution/parser/mod.rs:1-100`).

Each parser records discovered imports as `ImportRelation` values and, where possible, also creates bindings that later resolution can use. For example, Go parsing handles single and block import forms, stores the imported module, skips blank and dot imports for binding purposes, derives default package aliases, and decides whether to register an external member binding based on external-module predicates (`crates/gcode/src/index/import_resolution/parser/go_rust.rs:1-100`). PHP/Kotlin parsing normalizes statements, supports PHP `use function` and `use const`, expands grouped imports, skips malformed brace syntax, and uses helper splitters plus PHP symbol predicates (`crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:1-100`). Scala parsing expands grouped selectors and wildcard imports, records import relations, and maps imported simple names or aliases into local-call bindings when matching package files exist (`crates/gcode/src/index/import_resolution/parser/scala.rs:1-100`).

Within the wider import-resolution system, this module imports model types (`ImportRelation`, `Symbol`), context/binding structures (`ExternalCallTarget`, `ExternalRootBinding`, `ExtractedImports`, `ImportBindings`, `ImportResolutionContext`, `LocalCallBinding`), and predicates such as `rust_external_roots` from its parent import-resolution layer (`crates/gcode/src/index/import_resolution/parser/mod.rs:1-12`). It calls out to per-language parser modules declared locally, and re-exports resolver helpers for Lua, Objective-C, and shell local/member callee handling so sibling resolution code can reuse language-specific lookup behavior (`crates/gcode/src/index/import_resolution/parser/mod.rs:13-33`).

| Public/internal symbol | Role | Source |
| --- | --- | --- |
| `parse_import_statement` | Main language dispatch entry point | `crates/gcode/src/index/import_resolution/parser/mod.rs:35-100` |
| `resolve_lua_require_member_callee` | Re-exported Lua require-member resolver | `crates/gcode/src/index/import_resolution/parser/mod.rs:20` |
| `resolve_objc_local_callee` | Re-exported Objective-C local callee resolver | `crates/gcode/src/index/import_resolution/parser/mod.rs:24` |
| `resolve_shell_local_callee` | Re-exported shell local callee resolver | `crates/gcode/src/index/import_resolution/parser/mod.rs:33` |
| `php_local_symbol_exists` | Checks lowercased PHP local-symbol index | `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:8-14` |
| `parse_php_import_statement` | Parses PHP `use` imports and grouped imports | `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:16-56` |
| `parse_kotlin_import_statement` | Parses Kotlin import statements | `crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:64-100` |
| `parse_go_import_statement` | Parses Go single and block imports | `crates/gcode/src/index/import_resolution/parser/go_rust.rs:13-37` |
| `parse_scala_import_statement` | Parses Scala imports, groups, and wildcard modules | `crates/gcode/src/index/import_resolution/parser/scala.rs:6-22` |

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

