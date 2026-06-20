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

`import_resolution` builds and applies per-language import knowledge for indexing. Its context layer owns lookup state for local modules, external packages, language-specific symbol maps, and candidate file sets; `ImportResolutionContext` includes Python module names, JS package metadata, Go package-directory file maps, Rust crate metadata, and Java class indexes (`crates/gcode/src/index/import_resolution/context.rs:1-100`). The parser layer is the dispatch point: it accepts language, import text, relative path, shared `ImportResolutionContext`, and mutable `ExtractedImports`, then routes to Python, JS/TS, Go, Rust, Java, C#, PHP, Kotlin, Scala, Lua, Objective-C, shell, and rest-language handlers (`crates/gcode/src/index/import_resolution/parser/mod.rs:1-100`).

The key flow is context construction followed by import parsing and later call resolution. Helpers normalize raw syntax, including JavaScript module specifier and import-clause extraction, quoted-string parsing, whitespace collapsing, and template interpolation skipping (`crates/gcode/src/index/import_resolution/helpers.rs:1-100`). Predicates classify imports as local or external using the populated context, including JS builtins/packages, Go self-module paths, Python module indexes, and Rust external roots plus standard crates (`crates/gcode/src/index/import_resolution/predicates.rs:1-100`). Rust local resolution is deliberately candidate-based: it maps module paths to possible `foo.rs`/`foo/mod.rs` or crate-root `lib.rs`/`main.rs` files and returns `RustLocalTarget` records without reading files, leaving final symbol matching to a later pass (`crates/gcode/src/index/import_resolution/rust_local.rs:1-100`).

Collaboration is centered on `context.rs`: it imports JS candidate lookup, Ruby require-root logic, and Rust local target functions, declares Apple/.NET/Elixir/JVM/scripting/package metadata submodules, and re-exports binding and metadata builders for the rest of the indexer (`crates/gcode/src/index/import_resolution/context.rs:1-34`). The child `context` module separates external bindings from local cross-file call bindings, while the child `parser` module writes parsed results into `ExtractedImports`; together they form the bridge between raw import statements and downstream indexed call/link resolution.

| Public API Area | Representative Symbols |
| --- | --- |
| Context model | `ImportResolutionContext`, `ExtractedImports`, `ImportBindings`, `ExternalImportBinding`, `LocalCallBinding` |
| Context builders | `build_import_resolution_context`, `build_import_resolution_context_with_overrides` |
| Candidate lookup | `js_candidate_files`, `rust_import_candidate`, `go_candidate_files`, `java_candidate_files`, `php_candidate_files` |
| Parsers | `parse_import_statement`, `parse_js_import_statement`, `parse_python_import_statement`, `parse_rust_import_statement` |
| Resolution | `resolve_external_callee`, `resolve_local_callee`, `resolve_local_member_callee`, `resolve_rust_local_qualified_callee` |
| Predicates/helpers | `is_external_js_module`, `is_external_go_module`, `rust_external_roots`, `extract_js_module_specifier`, `split_top_level` |
[crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38]
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16]
[crates/gcode/src/index/import_resolution/context/apple.rs:8-12]
[crates/gcode/src/index/import_resolution/context/bindings.rs:6-9]
[crates/gcode/src/index/import_resolution/context/elixir.rs:13-49]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/index/import_resolution/context\|crates/gcode/src/index/import_resolution/context]] | The `context` module supplies the language-specific lookup state used by import resolution. Its core binding types separate external imports from local cross-file candidates: `ExternalImportBinding` stores module/name pairs, while `LocalCallBinding` carries candidate target files plus either named or default-export resolution, deferring final symbol UUID matching to a later post-write pass . |
| [[code/modules/crates/gcode/src/index/import_resolution/parser\|crates/gcode/src/index/import_resolution/parser]] | The `parser` module is the language dispatcher for import resolution. It accepts a language, import text, relative file path, shared `ImportResolutionContext`, and mutable `ExtractedImports`, then routes to the appropriate language-specific parser for Python, JS/TS, Go, Rust, Java, C#, PHP, Kotlin, Scala, Lua, Objective-C, shell, and several “rest” languages (`crates/gcode/src/index/import_resolution/parser/mod.rs:1-100`). |

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

