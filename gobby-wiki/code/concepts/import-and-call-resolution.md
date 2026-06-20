---
title: Import and Call Resolution
type: code_concept
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
- id: 2
  reason: Search/graph/document purpose and local cross-file candidate behavior are not shown in the evidence.
- id: 5
  reason: Cites non-provided apple.rs and claims an explicit post-write defer not shown here.
- id: 8
  reason: Lists ImportResolutionContext fields and roles that are not shown in the supplied excerpt.
- id: 9
  reason: Dispatcher signature and the long language-routing list are not shown in the evidence.
- id: 11
  reason: Caller/callee attachment purpose is not shown by the cited lines.
- id: 16
  reason: Canonicalization, filtering, and deduping behavior are not shown in the excerpt.
- id: 25
  reason: ImportResolutionContext field inventory exceeds what the evidence shows.
- id: 27
  reason: The rationale that parser functions stay small is not supported by the excerpt.
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

# Import and Call Resolution

## Purpose

Import and Call Resolution is the indexing layer that turns source-level imports and call sites into relationships the rest of the system can search, graph, and document. It bridges syntax with meaning: import text becomes either an external package/module reference or a local cross-file candidate, while call syntax is classified so later resolution can distinguish bare calls from member-style calls [crates/gcode/src/index/import_resolution/context.rs:41-138] [crates/gcode/src/index/parser/calls/resolution.rs:23-46].

## Covers / Does not cover

This page covers the language-aware import resolution context, per-language import parsing, external import-root data, and call-site classification/resolution helpers. The supplied evidence includes package metadata loading, Go import parsing, Elixir/Ruby external root registries, and shared call-resolution utilities [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38] [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] [crates/gcode/assets/import_roots/ruby_require_roots.json:2].

It does not cover final graph persistence, complete symbol UUID matching, or every language parser implementation. The context layer explicitly defers final local symbol UUID matching for local call bindings to a later post-write pass, so this concept should be read as the relationship discovery layer rather than the final graph materialization layer [crates/gcode/src/index/import_resolution/context/apple.rs:8-12].

## Architecture

The architecture is split into three cooperating parts.

First, the context layer owns lookup state. `ImportResolutionContext` carries language-specific knowledge such as Python module names, JavaScript package metadata, Go package-directory file maps, Rust crate metadata, and Java class indexes [crates/gcode/src/index/import_resolution/context.rs:41-138]. This keeps expensive or project-wide facts out of individual parser functions.

Second, the parser layer is a dispatcher. It accepts the current language, import text, relative path, shared context, and mutable `ExtractedImports`, then routes to language-specific handlers for Python, JS/TS, Go, Rust, Java, C#, PHP, Kotlin, Scala, Lua, Objective-C, shell, and other languages . The Go/Rust parser file shows this pattern concretely: `parse_go_import_statement` validates and decomposes Go import syntax, then delegates each import spec for relationship extraction [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40].

Third, static import-root registries cover ecosystems where a package or require name maps to a top-level API symbol. Elixir dependencies map names like `ecto`, `broadway`, `benchee`, and `ex_doc` to module roots such as `Ecto`, `Broadway`, `Benchee`, and `ExDoc` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:8] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:12] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:16] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:17]. Ruby require strings map names like `faraday` or `net/http` to constants or namespaces such as `Faraday` and `Net` [crates/gcode/assets/import_roots/ruby_require_roots.json:6] [crates/gcode/assets/import_roots/ruby_require_roots.json:2].

Call resolution is adjacent to import resolution. The call parser classifies syntax and identifies enclosing symbols, so a discovered call can later be attached to the right caller and, when possible, callee [crates/gcode/src/index/parser/calls/resolution.rs:6-10] [crates/gcode/src/index/parser/calls/resolution.rs:17-21].

## Data flow

1. Indexing builds language context from project files. JavaScript package names are read from `package.json` dependency fields; if the file cannot be read or parsed as JSON, the loader returns an empty package set [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38].

2. The context may also load a JavaScript self-package name from `package.json`; if the file is missing, unreadable, invalid JSON, or lacks a string `name`, the result is `None` [crates/gcode/src/index/import_resolution/context/package_metadata.rs:40-49].

3. For Go, the context can read the module path from `go.mod`; if no usable `module` line is found, the result is `None` .

4. Go candidate source files are grouped by project-relative package directory. `build_go_package_files` canonicalizes paths, skips non-Go files, ignores paths that cannot be resolved under the canonical root, and produces sorted, deduplicated file lists [crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97].

5. During parsing, the import dispatcher sends the import text to the language-specific parser. For Go, `parse_go_import_statement` requires an `import` statement and rejects malformed input with an error before processing either a block import or a single import spec [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40].

6. Each Go import spec strips line comments, ignores empty specs, and ignores specs without a quoted module string. When a module is present, it records an `ImportRelation` with the current file path and module name [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-58].

7. The Go parser derives a local selector alias from an explicit alias or from the default package alias. Blank imports `_` and dot imports `.` return early because they do not bind a selector alias that can be resolved here; an empty derived alias also returns early [crates/gcode/src/index/import_resolution/parser/go_rust.rs:60-75].

8. If the Go module is external according to the import context, the parser records a member binding from local alias to module name and stops local resolution for that import [crates/gcode/src/index/import_resolution/parser/go_rust.rs:77-80].

9. Separately, call parsing classifies call syntax. `call_syntax_kind` walks from the call name toward the call node and returns `Bare`, `Member`, or `Other` depending on whether the name is direct, member-like, or neither [crates/gcode/src/index/parser/calls/resolution.rs:23-46].

10. Call resolution can identify the innermost enclosing symbol by finding the last symbol whose byte range contains the call offset, using end-exclusive tree-sitter byte ranges [crates/gcode/src/index/parser/calls/resolution.rs:17-21].

## Key components

These are the few symbols and data files to understand first; they define the shape of the import/call relationship layer rather than every parser detail.

| Component | Role |
| --- | --- |
| `ImportResolutionContext` | Shared language-specific lookup state for local modules, package metadata, candidate files, crate metadata, and class indexes [crates/gcode/src/index/import_resolution/context.rs:41-138]. |
| `parse_go_import_statement` | Parses Go import statements, handles block versus single imports, and delegates individual specs [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]. |
| `build_go_package_files` | Builds the Go package-directory file map used for local package resolution [crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97]. |
| `call_syntax_kind` / `CallSyntaxKind` | Classifies calls as `Bare`, `Member`, or `Other` for downstream call resolution [crates/gcode/src/index/parser/calls/resolution.rs:6-10] [crates/gcode/src/index/parser/calls/resolution.rs:23-46]. |
| Elixir/Ruby import-root JSON files | Map dependency or require identifiers to top-level API symbols for external resolution [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] [crates/gcode/assets/import_roots/ruby_require_roots.json:2]. |

## Where to start

Start with `ImportResolutionContext`, because it explains what facts import parsing is allowed to rely on and why the parser functions stay relatively small [crates/gcode/src/index/import_resolution/context.rs:41-138]. Then read `parse_go_import_statement` for a concrete example of import text becoming `ImportRelation` records and bindings [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]. For the call side, read `CallSyntaxKind` and `call_syntax_kind` to see how syntactic shape is reduced into categories used by later resolution [crates/gcode/src/index/parser/calls/resolution.rs:6-10] [crates/gcode/src/index/parser/calls/resolution.rs:23-46].

## Explore

- [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]]
- [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]
- [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]
- [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]
- [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]]

