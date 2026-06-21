---
title: Turning Source Files into Code Facts
type: code_narrative
provenance:
- file: crates/gcode/assets/import_roots/elixir_dependency_roots.json
- file: crates/gcode/assets/import_roots/ruby_require_roots.json
- file: crates/gcode/src/index/api.rs
- file: crates/gcode/src/index/import_resolution/context.rs
- file: crates/gcode/src/index/import_resolution/context/apple.rs
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
- file: crates/gcode/src/index/import_resolution/context/package_metadata.rs
- file: crates/gcode/src/index/import_resolution/helpers.rs
- file: crates/gcode/src/index/import_resolution/js_local.rs
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
- file: crates/gcode/src/index/import_resolution/predicates.rs
- file: crates/gcode/src/index/import_resolution/rust_local.rs
- file: crates/gcode/src/index/indexer/file.rs
- file: crates/gcode/src/index/indexer/freshness_probe.rs
- file: crates/gcode/src/index/indexer/lifecycle.rs
- file: crates/gcode/src/index/indexer/overlay.rs
- file: crates/gcode/src/index/indexer/sink.rs
- file: crates/gcode/src/index/indexer/types.rs
- file: crates/gcode/src/index/indexer/util.rs
- file: crates/gcode/src/index/languages.rs
- file: crates/gcode/src/index/parser.rs
- file: crates/gcode/src/index/parser/calls/ast.rs
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
- file: crates/gcode/src/index/parser/calls/resolution.rs
- file: crates/gcode/src/index/parser/calls/shadowing.rs
- file: crates/gcode/src/index/parser/calls/text.rs
- file: crates/gcode/src/index/security.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/index/walker/hidden.rs
provenance_truncated: 31
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/assets/import_roots/elixir_dependency_roots.json](crates/gcode/assets/import_roots/elixir_dependency_roots.json)
- [crates/gcode/assets/import_roots/ruby_require_roots.json](crates/gcode/assets/import_roots/ruby_require_roots.json)
- [crates/gcode/src/index/api.rs](crates/gcode/src/index/api.rs)
- [crates/gcode/src/index/import_resolution/context.rs](crates/gcode/src/index/import_resolution/context.rs)
- [crates/gcode/src/index/import_resolution/context/apple.rs](crates/gcode/src/index/import_resolution/context/apple.rs)
- [crates/gcode/src/index/import_resolution/context/bindings.rs](crates/gcode/src/index/import_resolution/context/bindings.rs)
- [crates/gcode/src/index/import_resolution/context/package_metadata.rs](crates/gcode/src/index/import_resolution/context/package_metadata.rs)
- [crates/gcode/src/index/import_resolution/helpers.rs](crates/gcode/src/index/import_resolution/helpers.rs)
- [crates/gcode/src/index/import_resolution/js_local.rs](crates/gcode/src/index/import_resolution/js_local.rs)
- [crates/gcode/src/index/import_resolution/parser/mod.rs](crates/gcode/src/index/import_resolution/parser/mod.rs)
- [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs)
- [crates/gcode/src/index/import_resolution/predicates.rs](crates/gcode/src/index/import_resolution/predicates.rs)

_49 more source files omitted._

</details>

# Turning Source Files into Code Facts

# Turning Source Files into Code Facts

## Why this matters

A repository on disk is just a pile of text. To answer questions like "who calls this function?" or "which dependency does this import point at?", that text has to be transformed into structured, queryable *facts*. This chapter follows the `index` pipeline that performs exactly that transformation: it discovers files, decides which ones are worth parsing, runs them through tree-sitter to extract calls, resolves each import to a concrete root, and persists the results as Postgres facts.

The central design decision is to split this work into distinct, replaceable stages — a *walker* that classifies files [crates/gcode/src/index/walker/classification.rs:15-52], a *parser* that extracts calls from the syntax tree [crates/gcode/src/index/parser/calls/ast.rs:17-103], and an *import resolution* layer that maps raw import strings to known roots [crates/gcode/src/index/import_resolution/context.rs:41-138]. Each stage has a narrow job, which keeps language-specific quirks (Elixir dependency naming, Ruby require paths, Go/Rust module conventions) isolated to where they belong rather than smeared across the whole indexer.

## How it works

1. **Discovery and classification.** The walker enumerates files in the repository and runs them through classification before any expensive parsing happens [crates/gcode/src/index/walker/classification.rs:15-52]. This is the gatekeeper: it determines which files are source worth indexing and which should be skipped, so the parser never wastes work on irrelevant content.

2. **Per-file indexing.** Each classified file is handed to the indexer's file path [crates/gcode/src/index/indexer/file.rs:15-91], which orchestrates parsing and fact production for that single unit of work. Working one file at a time keeps the failure blast radius small — a problem in one file doesn't abort the whole run.

3. **Tree-sitter parsing and call extraction.** The parser walks the syntax tree to pull out call sites [crates/gcode/src/index/parser/calls.rs:26-35], with the AST-level traversal doing the heavy lifting of recognizing call expressions [crates/gcode/src/index/parser/calls/ast.rs:17-103]. This is where raw syntax becomes "X calls Y" facts.

4. **Import resolution.** Imports are not facts until they point somewhere. The resolution context maps a raw import or require string onto a known root [crates/gcode/src/index/import_resolution/context.rs:41-138]. Language-specific resolvers handle the conventions: the Go/Rust parser interprets module-style paths [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40], while platform contexts such as Apple's handle their own naming [crates/gcode/src/index/import_resolution/context/apple.rs:8-12].

5. **Root lookup via asset maps.** For ecosystems where the import name and the module name diverge, resolution consults shipped lookup tables. The Elixir map translates a dependency key like `jason` to its module root `Jason` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2], `httpoison` to `HTTPoison` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:3], and `ecto` to `Ecto` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:8]. The Ruby map does the same for require paths, mapping `json` to `JSON` [crates/gcode/assets/import_roots/ruby_require_roots.json:2] and `net/http` to `Net` [crates/gcode/assets/import_roots/ruby_require_roots.json:4]. Think of these JSON files as a translation glossary: the source says `finch` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:6], the glossary says it means `Finch` — without it the resolver could not connect the import to the right root.

6. **Persisting facts.** The resolved calls and imports flow back through the indexer and out through the index API [crates/gcode/src/index/api.rs:16-23], where they are written as durable Postgres facts ready to be queried.

Where the evidence shows fallback behavior, it lives in the resolution layer: when an import name isn't present in a root map (the Elixir and Ruby tables are deliberately finite, covering only common dependencies [crates/gcode/assets/import_roots/elixir_dependency_roots.json:16][crates/gcode/assets/import_roots/ruby_require_roots.json:6]), resolution falls back to the language parser's own interpretation rather than failing the file.

## Key components

| Symbol / File | Role |
| --- | --- |
| `walker/classification.rs` | Decides which discovered files are source worth indexing [crates/gcode/src/index/walker/classification.rs:15-52] |
| `indexer/file.rs` | Orchestrates parse-and-extract for a single file [crates/gcode/src/index/indexer/file.rs:15-91] |
| `parser/calls/ast.rs` | Tree-sitter AST traversal that extracts call sites [crates/gcode/src/index/parser/calls/ast.rs:17-103] |
| `import_resolution/context.rs` | Maps raw imports onto known roots [crates/gcode/src/index/import_resolution/context.rs:41-138] |
| `import_resolution/parser/go_rust.rs` | Language-specific resolution for Go/Rust module paths [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] |
| `elixir_dependency_roots.json` | Dependency-to-module lookup table for Elixir [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] |
| `ruby_require_roots.json` | Require-path-to-module lookup table for Ruby [crates/gcode/assets/import_roots/ruby_require_roots.json:2] |
| `index/api.rs` | Entry surface that emits persisted Postgres facts [crates/gcode/src/index/api.rs:16-23] |

## What to read next

Now that source files have become call and import facts, the next chapter covers how those persisted facts are queried and traversed — the read side of the index that turns "X calls Y" rows back into navigable answers. If you want to go deeper on a single stage first, revisit the import resolution module to see how additional languages plug new context resolvers alongside `go_rust` and `apple` [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40][crates/gcode/src/index/import_resolution/context/apple.rs:8-12].

## Concepts

- [[code/concepts/crates-gcode-src-index|Code Indexing Pipeline]]
- [[code/concepts/crates-gcode-src-index-parser|Call Extraction]]
- [[code/concepts/crates-gcode-src-index-import-resolution|Import Resolution]]
- [[code/concepts/crates-gcode-assets|Dependency Root Catalog]]

## Explore

- [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]
- [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]
- [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]]
- [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]
- [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]]

## Continue the tour

- ← Previous: [[code/narrative/04-foundations-config-and-services|Foundations: Configuration, Connectivity, and Services]]
- Next →: [[code/narrative/06-graph-and-vector-stores|Projecting Facts into the Graph and Vector Stores]]

