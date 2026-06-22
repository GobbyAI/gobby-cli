---
title: crates/gcode/src/index/import_resolution
type: code_module
provenance:
- file: crates/gcode/src/index/import_resolution/context.rs
- file: crates/gcode/src/index/import_resolution/context/apple.rs
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
- file: crates/gcode/src/index/import_resolution/context/dotnet.rs
- file: crates/gcode/src/index/import_resolution/context/elixir.rs
- file: crates/gcode/src/index/import_resolution/context/jvm.rs
- file: crates/gcode/src/index/import_resolution/context/package_metadata.rs
- file: crates/gcode/src/index/import_resolution/context/python.rs
- file: crates/gcode/src/index/import_resolution/context/scripting.rs
- file: crates/gcode/src/index/import_resolution/helpers.rs
- file: crates/gcode/src/index/import_resolution/js_local.rs
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
- file: crates/gcode/src/index/import_resolution/predicates.rs
- file: crates/gcode/src/index/import_resolution/rust_local.rs
- file: crates/gcode/src/index/import_resolution/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution

Parent: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

## Module: crates/gcode/src/index/import_resolution

This module is the cross-language import resolution engine for the `gcode` indexer. Its central responsibility is converting raw import statements found in source files into candidate file paths that the indexer can use to build call graphs and symbol references. It covers more than a dozen language ecosystems — Python, JavaScript/TypeScript, Go, Rust, Java, Kotlin, Scala, C#, PHP, Ruby, Elixir, Lua, Objective-C, Swift, Dart, and shell — and must distinguish local (project-internal) imports from external package dependencies for each of them. The two entry points `build_import_resolution_context` and `build_import_resolution_context_with_overrides` (component IDs `2e0502cf`, `25e5e0eb`) materialise an `ImportResolutionContext` by scanning manifest files (`Cargo.toml`, `package.json`, `go.mod`, `mix.exs`, etc.) and pre-building per-ecosystem lookup indexes; all subsequent resolution queries read from that context without additional I/O.

The module is split across three layers. The **parser** child module (`parser/mod.rs` and its per-language files `go_rust.rs`, `java_csharp.rs`, `python_js.rs`, `php_kotlin.rs`, `scala.rs`, `lua.rs`, `objc.rs`, `shell.rs`, `rest.rs`) provides `parse_import_statement` plus helpers such as `parse_go_import_spec`, `split_rust_use_group`, `split_scala_import_group`, and `split_php_use_group` that tokenise raw source lines into `ExtractedImports` / `ImportBindings` structures. The **context** child module (`context.rs` and sub-files `apple.rs`, `dotnet.rs`, `elixir.rs`, `jvm.rs`, `scripting.rs`) builds the ecosystem indexes (`JavaClassIndex`, `CsharpIndex`, `ObjcIndex`) and populates the many map/set fields on `ImportResolutionContext` such as `go_package_files`, `python_modules`, `rust_external_crates`, and the Swift/Ruby/Elixir/PHP/Lua file maps. Language-specific local resolution logic lives in `js_local.rs` (`js_candidate_files`, `js_import_target_keys`) and `rust_local.rs` (`rust_candidate_files`, `rust_import_target`, `rust_qualified_call_target`). The **predicates** layer (`predicates.rs`) classifies a resolved import path as local or external (e.g. `is_external_js_module`, `is_external_go_module`, `is_external_rust_root`) and provides `rust_external_roots`, `java_declared_types`, `csharp_declared_types`, and `php_declared_symbols` for symbol-level filtering. The **helpers** layer (`helpers.rs`) supplies string utilities (`collapse_whitespace`, `extract_js_module_specifier`, `extract_quoted_string`, `split_top_level`, `split_error_context`) that the parsers and context builders share.

`ImportResolutionContext` exposes per-language query methods that the wider indexer calls after construction to obtain candidate file lists or symbol resolution targets:

| Method | Language | Returns |
|---|---|---|
| `js_candidate_files` | JS/TS | candidate `.js`/`.ts` paths for a specifier |
| `rust_import_candidate` | Rust | `RustLocalTarget` for a `use` path |
| `rust_qualified_candidate` | Rust | `RustLocalTarget` for a qualified call |
| `go_candidate_files` | Go | files in the imported package directory |
| `java_candidate_files` | Java | files declaring the imported class |
| `csharp_type_files` | C# | files declaring the imported type |
| `kotlin_package_files` | Kotlin | files in the Kotlin package |
| `scala_package_files` | Scala | files in the Scala package |
| `lua_module_files` | Lua | files for a `require` module name |
| `objc_import_candidate_files` | Objective-C | files for a `#import` path |
| `objc_declared_types` / `objc_declared_functions` | Objective-C | symbol lookups |
| `php_candidate_files` | PHP | files for a `use`/`require` symbol |
| `swift_module_candidate_files` | Swift | files in the Swift module |
| `ruby_require_root` / `ruby_constant_files` | Ruby | require-root and constant files |
| `elixir_external_root_module` / `elixir_module_files` | Elixir | module file candidates |

Public binding types surfaced from this module and consumed by call-graph construction elsewhere in `crates/gcode` include `ExternalImportBinding`, `ExternalRootBinding`, `ExternalCallTarget`, `ImportBindings`, `LocalCallBinding`, `ExtractedImports`, and `LocalCallResolution`. `RustLocalTarget` (component `f2450d7f`) carries a `source_root`, `module`, and `name` triple that the Rust-specific post-write narrowing pass uses to match indexed symbols against resolved imports (`rust_local.rs:9-14`). Predicate helpers consumed by upstream index construction read the context directly, e.g. `is_external_js_module` checks `js_external_packages` and the `JS_BUILTIN_MODULES` set (`predicates.rs:23-52`), and `rust_external_roots` merges `STANDARD_RUST_CRATES` (`["std","core","alloc","proc_macro","test"]`) with the manifest-loaded crate set (`predicates.rs:67-76`). The `tests.rs` file exercises the module's resolution logic end-to-end without exporting additional API symbols.
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16]
[crates/gcode/src/index/import_resolution/context/apple.rs:8-12]
[crates/gcode/src/index/import_resolution/context/dotnet.rs:10-17]
[crates/gcode/src/index/import_resolution/context/elixir.rs:13-49]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/index/import_resolution/context\|crates/gcode/src/index/import_resolution/context]] | ## crates/gcode/src/index/import_resolution/context |
| [[code/modules/crates/gcode/src/index/import_resolution/parser\|crates/gcode/src/index/import_resolution/parser]] | ## crates/gcode/src/index/import_resolution/parser |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/import_resolution/context.rs\|crates/gcode/src/index/import_resolution/context.rs]] | `crates/gcode/src/index/import_resolution/context.rs` exposes 21 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/apple.rs\|crates/gcode/src/index/import_resolution/context/apple.rs]] | `crates/gcode/src/index/import_resolution/context/apple.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/dotnet.rs\|crates/gcode/src/index/import_resolution/context/dotnet.rs]] | `crates/gcode/src/index/import_resolution/context/dotnet.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/elixir.rs\|crates/gcode/src/index/import_resolution/context/elixir.rs]] | `crates/gcode/src/index/import_resolution/context/elixir.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/jvm.rs\|crates/gcode/src/index/import_resolution/context/jvm.rs]] | `crates/gcode/src/index/import_resolution/context/jvm.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/scripting.rs\|crates/gcode/src/index/import_resolution/context/scripting.rs]] | `crates/gcode/src/index/import_resolution/context/scripting.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/helpers.rs\|crates/gcode/src/index/import_resolution/helpers.rs]] | `crates/gcode/src/index/import_resolution/helpers.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/js_local.rs\|crates/gcode/src/index/import_resolution/js_local.rs]] | `crates/gcode/src/index/import_resolution/js_local.rs` exposes 13 indexed API symbols. |
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
| [[code/files/crates/gcode/src/index/import_resolution/predicates.rs\|crates/gcode/src/index/import_resolution/predicates.rs]] | `crates/gcode/src/index/import_resolution/predicates.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/rust_local.rs\|crates/gcode/src/index/import_resolution/rust_local.rs]] | `crates/gcode/src/index/import_resolution/rust_local.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/tests.rs\|crates/gcode/src/index/import_resolution/tests.rs]] | `crates/gcode/src/index/import_resolution/tests.rs` has no indexed API symbols. |

