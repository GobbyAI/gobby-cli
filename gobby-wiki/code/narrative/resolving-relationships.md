---
title: Resolving Relationships
type: code_narrative
provenance:
- file: crates/gcode/assets/import_roots/elixir_dependency_roots.json
- file: crates/gcode/assets/import_roots/ruby_require_roots.json
- file: crates/gcode/src/index/import_resolution/context.rs
- file: crates/gcode/src/index/import_resolution/context/apple.rs
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
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
- file: crates/gcode/src/index/parser/calls/ast.rs
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
- file: crates/gcode/src/index/parser/calls/objc_ast.rs
- file: crates/gcode/src/index/parser/calls/resolution.rs
- file: crates/gcode/src/index/parser/calls/shadowing.rs
- file: crates/gcode/src/index/parser/calls/text.rs
provenance_truncated: 2
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 5
  reason: ImportResolutionContext fields and line range are not shown in the excerpts.
- id: 7
  reason: Skipping non-Go files and non-relative paths is not shown in the provided excerpt.
- id: 8
  reason: parser/mod.rs dispatch and supported-language list are not shown in the excerpts.
- id: 11
  reason: call_qualifier_path behavior is not shown in the provided source excerpt.
- id: 14
  reason: ImportResolutionContext role and call_qualifier_path role are not supported by the excerpts.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/assets/import_roots/elixir_dependency_roots.json](crates/gcode/assets/import_roots/elixir_dependency_roots.json)
- [crates/gcode/assets/import_roots/ruby_require_roots.json](crates/gcode/assets/import_roots/ruby_require_roots.json)
- [crates/gcode/src/index/import_resolution/context.rs](crates/gcode/src/index/import_resolution/context.rs)
- [crates/gcode/src/index/import_resolution/context/apple.rs](crates/gcode/src/index/import_resolution/context/apple.rs)
- [crates/gcode/src/index/import_resolution/context/bindings.rs](crates/gcode/src/index/import_resolution/context/bindings.rs)
- [crates/gcode/src/index/import_resolution/context/elixir.rs](crates/gcode/src/index/import_resolution/context/elixir.rs)
- [crates/gcode/src/index/import_resolution/context/jvm.rs](crates/gcode/src/index/import_resolution/context/jvm.rs)
- [crates/gcode/src/index/import_resolution/context/package_metadata.rs](crates/gcode/src/index/import_resolution/context/package_metadata.rs)
- [crates/gcode/src/index/import_resolution/context/python.rs](crates/gcode/src/index/import_resolution/context/python.rs)
- [crates/gcode/src/index/import_resolution/context/scripting.rs](crates/gcode/src/index/import_resolution/context/scripting.rs)
- [crates/gcode/src/index/import_resolution/helpers.rs](crates/gcode/src/index/import_resolution/helpers.rs)
- [crates/gcode/src/index/import_resolution/js_local.rs](crates/gcode/src/index/import_resolution/js_local.rs)

_20 more source files omitted._

</details>

# Resolving Relationships

## Why this matters

Raw indexing can tell you that a file contains symbols, imports, and calls. Resolving relationships makes those facts useful: an import like `net/http`, `ecto`, or a Go package path can point toward a real namespace, package, or candidate file set instead of remaining plain text.

The design decision here is to keep resolution layered on top of extraction. Import resolution gathers language-specific context, package metadata, and known external roots, while call resolution classifies syntax and tries to connect call sites to symbols. That split lets the indexer record what it sees first, then add navigable relationships when there is enough evidence.

## How it works

1. The system starts with language-aware import context. `ImportResolutionContext` carries lookup state for local modules, external packages, language-specific symbol maps, and candidate files, including Python module names, JS package metadata, Go package-directory maps, Rust crate metadata, and Java class indexes [crates/gcode/src/index/import_resolution/context.rs:41-138].

2. Static import-root registries fill in common external APIs. Elixir dependency names such as `ecto`, `broadway`, `benchee`, and `ex_doc` map to top-level modules like `Ecto`, `Broadway`, `Benchee`, and `ExDoc` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:8] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:12] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:16] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:17]. Ruby require strings do the same for constants, for example `faraday` to `Faraday` [crates/gcode/assets/import_roots/ruby_require_roots.json:6].

3. Package metadata expands what can be resolved from the repository itself. For JavaScript, dependency names are loaded from `package.json`, and missing or invalid files fall back to an empty package set [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38]. For Go, `build_go_package_files` groups discovered `.go` files by project-relative package directory, skipping non-Go files and paths that cannot be made relative to the canonical root [crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97].

4. The parser layer dispatches by language. It accepts the language, import text, relative file path, shared `ImportResolutionContext`, and mutable `ExtractedImports`, then routes to handlers for Python, JS/TS, Go, Rust, Java, C#, PHP, Kotlin, Scala, Lua, Objective-C, shell, and other languages .

5. Go import parsing records the import relation first, then tries to create a useful binding. `parse_go_import_statement` validates that the text is actually an import statement and bails if it is not [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]. Each import spec strips comments, ignores empty text, requires a quoted module, and skips `_` and `.` aliases because they do not create selector aliases that can be resolved [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40].

6. Call resolution adds another layer of relationship data. `enclosing_symbol` finds the deepest indexed symbol containing a byte offset, so a call can be associated with its caller [crates/gcode/src/index/parser/calls/resolution.rs:17-21]. `call_syntax_kind` then walks from the call name toward the call node and classifies the syntax as `Bare`, `Member`, or `Other` [crates/gcode/src/index/parser/calls/resolution.rs:23-46].

7. The call resolver uses that syntax classification to decide what kind of target search is reasonable. Bare calls can match callable symbols by name, while member-style calls can use qualifier information; `call_qualifier_path` prefers a qualifier taken from the name and falls back to deriving one from the member expression [crates/gcode/src/index/parser/calls/resolution.rs:204-209].

8. When the evidence is incomplete, resolution stays conservative. Missing package metadata becomes an empty set, malformed Go import text returns an error, unquoted or empty import specs are ignored, and calls that do not fit bare or member syntax become `Other` rather than being forced into a likely-wrong target [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38] [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] [crates/gcode/src/index/parser/calls/resolution.rs:6-10].

## Key components

| Symbol | Role |
| --- | --- |
| `ImportResolutionContext` | Shared lookup state for local modules, external packages, and language-specific indexes [crates/gcode/src/index/import_resolution/context.rs:41-138] |
| `build_go_package_files` | Builds Go package-directory candidate file maps for later selector resolution [crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97] |
| `parse_go_import_statement` | Parses Go imports, records `ImportRelation`s, and creates bindings when possible [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] |
| `CallSyntaxKind` | Classifies calls as `Bare`, `Member`, or `Other` [crates/gcode/src/index/parser/calls/resolution.rs:6-10] |
| `call_syntax_kind` | Walks syntax ancestors to assign the call classification [crates/gcode/src/index/parser/calls/resolution.rs:23-46] |
| `call_qualifier_path` | Chooses the qualifier path used for member-call resolution [crates/gcode/src/index/parser/calls/resolution.rs:204-209] |

## What to read next

Read the call-resolution reference next, centered on `crates/gcode/src/index/parser/calls/resolution.rs`, to see how extracted call candidates become symbol relationships after import bindings and syntax classification are available.

## Concepts

- [[code/concepts/import-and-call-resolution|Import and Call Resolution]]

## Explore

- [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]]
- [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]
- [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]
- [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]
- [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]]

## Continue the tour

- ← Previous: [[code/narrative/building-the-code-index|Building the Code Index]]
- Next →: [[code/narrative/projecting-graph-and-vectors|Projecting Graph and Vectors]]

