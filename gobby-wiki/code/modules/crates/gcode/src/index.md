---
title: crates/gcode/src/index
type: code_module
provenance:
- file: crates/gcode/src/index/api.rs
- file: crates/gcode/src/index/import_resolution/context.rs
- file: crates/gcode/src/index/import_resolution/context/apple.rs
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
- file: crates/gcode/src/index/import_resolution/context/package_metadata.rs
- file: crates/gcode/src/index/import_resolution/helpers.rs
- file: crates/gcode/src/index/import_resolution/js_local.rs
- file: crates/gcode/src/index/import_resolution/parser/go_rust.rs
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
- file: crates/gcode/src/index/import_resolution/parser/scala.rs
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
provenance_truncated: 29
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

## Module: `crates/gcode/src/index`

This module is the complete code-indexing pipeline for the `gcode` crate. It is responsible for discovering source files in a project, classifying and parsing them with tree-sitter grammars, extracting structured facts (symbols, imports, call sites, and content chunks), resolving cross-file call and import relationships, and persisting all results to a database backend through a `CodeFactSink` abstraction. The module is subdivided into five collaborating areas: file walking and classification (`walker`), language detection and tree-sitter query registry (`languages`), AST and textual parsing (`parser` and its `calls` sub-hierarchy), import/call resolution (`import_resolution`, `indexer`), and database I/O plus hashing (`api`, `chunker`, `hasher`). Security filters (`security.rs`) enforce path validation, binary detection, symlink safety, and secret-extension exclusion across every discovered path.

The central indexing flow begins in the `indexer` child module, which calls `index_file` / `index_files` to drive the pipeline per file. Each file is first validated by `validate_path` and classified by `classify_file` into a `FileClassification`; it then proceeds through `detect_language` (backed by the `LanguageSpec` registry in `languages.rs`) and `parse_file_with_semantic`. Parsing yields raw symbol, import, and call lists via `extract_symbols`, `extract_imports`, and `extract_calls`; call sites pass through per-language resolution paths including AST-driven extraction (`ast.rs`, `objc_ast.rs`), textual fallback (`dart_textual.rs`), shadowing suppression (`shadowing.rs`), and—for C/C++—an optional `ClangdResolver` that speaks the Language Server Protocol to resolve definitions to either `SemanticTargetKind::External` (a dependency path) or `SemanticTargetKind::LocalCandidate` (a project-relative file) (`semantic.rs:34–43`). Import relationships are resolved per language through `ImportResolutionContext`, which exposes language-specific candidate-file lookups for JS, Rust, Go, Java, C#, Kotlin, Scala, Lua, Obj-C, PHP, Swift, Ruby, Elixir, and Dart. Resolved facts are written via `upsert_*` functions that target a `PostgresCodeFactSink` implementing the `CodeFactSink` trait.

The `semantic.rs` file drives C/C++ semantic resolution by spawning a `clangd` subprocess, sending LSP `textDocument/definition` requests, and reading JSON-RPC responses on a background thread with a 30-second timeout (`CLANGD_RESPONSE_TIMEOUT`, `semantic.rs:11`). The `create_cpp_semantic_resolver` function discovers `compile_commands.json` in the project root or build directories and can be made mandatory via the `GCODE_REQUIRE_CPP_SEMANTICS` environment variable or the `require_cpp_semantics` flag (`semantic.rs:57–68`). The `languages.rs` registry defines tree-sitter `symbol_query`, `import_query`, and `call_query` strings for every supported language via `LanguageSpec` structs (`languages.rs:8–14`), and `detect_header_language` applies heuristics—sibling implementation lookup, ObjC directive scanning—to disambiguate C, C++, and Objective-C header files.

---

### Public API — Database Write Functions (`api.rs`)

| Symbol | Kind | Description |
|---|---|---|
| `CodeFactWriteRequest` | struct | Bundles all parsed facts for a single file write |
| `CodeFactWriteSummary` | struct | Per-file write result; constructed via `for_file` |
| `upsert_file` | fn | Insert or update the file row |
| `upsert_symbols` | fn | Bulk upsert extracted symbol records |
| `upsert_imports` | fn | Bulk upsert import edges |
| `upsert_calls` | fn | Bulk upsert call-site edges |
| `upsert_content_chunks` | fn | Store text chunks for search |
| `upsert_project_stats` | fn | Refresh aggregate project counters |
| `delete_file_facts` | fn | Remove all facts for a file |
| `delete_file_non_symbol_facts` | fn | Remove non-symbol facts only |
| `delete_stale_file_symbols` | fn | Remove symbols absent from latest parse |
| `file_facts_exist` | fn | Check whether a file is already indexed |
| `insert_call` | fn | Insert a single resolved call edge |
| `promote_local_import_call` | fn | Upgrade a local-import call to a resolved symbol call |

---

### Language Registry (`languages.rs`)

| Symbol | Kind | Description |
|---|---|---|
| `LanguageSpec` | struct | Holds extensions + three tree-sitter query strings per language |
| `detect_language` | fn | Map file extension to a `LanguageSpec` |
| `detect_header_language` | fn | Disambiguate `.h` / `.hpp` as C, C++, or Obj-C |
| `get_spec` | fn | Return spec by language name string |
| `get_ts_language` | fn | Return tree-sitter `Language` handle by name |
| `get_ts_language_for_path` | fn | Combine path + content signals into a grammar handle |
| `is_data_language` | fn | True for JSON and YAML (no symbol extraction) |

---

### Semantic (C/C++) Resolution (`semantic.rs`)

| Symbol | Kind | Description |
|---|---|---|
| `SemanticCallResolver` | trait | Single `resolve(&SemanticCallRequest) -> Option<SemanticCallTarget>` |
| `SemanticCallRequest` | struct | Language, paths, source bytes, callee name, line/column |
| `SemanticCallTarget` | struct | Resolved callee name + `SemanticTargetKind` |
| `SemanticTargetKind::External` | variant | Definition outside project; carries dependency path |
| `SemanticTargetKind::LocalCandidate` | variant | Definition inside project; carries project-relative path |
| `ClangdResolver` | struct | LSP client that manages clangd subprocess lifetime |
| `create_cpp_semantic_resolver` | fn | Factory; discovers `compile_commands.json`, respects `GCODE_REQUIRE_CPP_SEMANTICS` |
| `discover_compile_commands_dir` | fn | Searches root and build subdirectories |

---

### Security & Path Filtering (`security.rs`)

| Symbol | Description |
|---|---|
| `validate_path` | Rejects paths with traversal sequences |
| `is_symlink_safe` | Ensures symlink target stays within project root |
| `is_binary` | Heuristic binary-file detection |
| `should_exclude_path` | Combines all exclusion rules |
| `is_root_generated_dir` | Detects well-known generated directories (e.g. `node_modules`) |
| `has_secret_extension` | Filters credential file extensions |
| `glob_match` / `glob_inner` | Lightweight glob used for hidden-path allowlist |

---

### Content Utilities (`chunker.rs`, `hasher.rs`)

| Symbol | File | Description |
|---|---|---|
| `chunk_file_content` | chunker.rs | Splits file text into overlapping search chunks |
| `epoch_secs_str` | chunker.rs | Stable timestamp string for chunk keys |
| `file_content_hash` | hasher.rs | SHA-based hash of raw file bytes |
| `content_hash` | hasher.rs | Generic byte-slice hash (delegates to `gobby_core`) |
| `symbol_content_hash` | hasher.rs | Hash scoped to a symbol's byte range |
[crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16]
[crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91]
[crates/gcode/src/index/import_resolution/parser/lua.rs:6-44]
[crates/gcode/src/index/import_resolution/parser/objc.rs:8-69]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/index/import_resolution\|crates/gcode/src/index/import_resolution]] | ## Module: crates/gcode/src/index/import_resolution |
| [[code/modules/crates/gcode/src/index/indexer\|crates/gcode/src/index/indexer]] | ## crates/gcode/src/index/indexer |
| [[code/modules/crates/gcode/src/index/parser\|crates/gcode/src/index/parser]] | ## Module: `crates/gcode/src/index/parser` |
| [[code/modules/crates/gcode/src/index/walker\|crates/gcode/src/index/walker]] | ## crates/gcode/src/index/walker |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/api.rs\|crates/gcode/src/index/api.rs]] | `crates/gcode/src/index/api.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gcode/src/index/chunker.rs\|crates/gcode/src/index/chunker.rs]] | `crates/gcode/src/index/chunker.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/index/hasher.rs\|crates/gcode/src/index/hasher.rs]] | `crates/gcode/src/index/hasher.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution.rs\|crates/gcode/src/index/import_resolution.rs]] | `crates/gcode/src/index/import_resolution.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer.rs\|crates/gcode/src/index/indexer.rs]] | `crates/gcode/src/index/indexer.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/index/languages.rs\|crates/gcode/src/index/languages.rs]] | `crates/gcode/src/index/languages.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gcode/src/index/mod.rs\|crates/gcode/src/index/mod.rs]] | `crates/gcode/src/index/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser.rs\|crates/gcode/src/index/parser.rs]] | `crates/gcode/src/index/parser.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls.rs\|crates/gcode/src/index/parser/calls.rs]] | `crates/gcode/src/index/parser/calls.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/ast.rs\|crates/gcode/src/index/parser/calls/ast.rs]] | `crates/gcode/src/index/parser/calls/ast.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/dart_textual.rs\|crates/gcode/src/index/parser/calls/dart_textual.rs]] | `crates/gcode/src/index/parser/calls/dart_textual.rs` exposes 21 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/objc_ast.rs\|crates/gcode/src/index/parser/calls/objc_ast.rs]] | `crates/gcode/src/index/parser/calls/objc_ast.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/resolution.rs\|crates/gcode/src/index/parser/calls/resolution.rs]] | `crates/gcode/src/index/parser/calls/resolution.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/shadowing.rs\|crates/gcode/src/index/parser/calls/shadowing.rs]] | `crates/gcode/src/index/parser/calls/shadowing.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/text.rs\|crates/gcode/src/index/parser/calls/text.rs]] | `crates/gcode/src/index/parser/calls/text.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/index/security.rs\|crates/gcode/src/index/security.rs]] | `crates/gcode/src/index/security.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/index/semantic.rs\|crates/gcode/src/index/semantic.rs]] | `crates/gcode/src/index/semantic.rs` exposes 56 indexed API symbols. |
| [[code/files/crates/gcode/src/index/walker.rs\|crates/gcode/src/index/walker.rs]] | `crates/gcode/src/index/walker.rs` has no indexed API symbols. |

