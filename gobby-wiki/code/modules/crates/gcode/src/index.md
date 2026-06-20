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

`crates/gcode/src/index` owns code indexing: discovery, language detection, parsing, semantic enrichment, import/call resolution, chunking, hashing, and persistence. The walker discovers project files with `gobby_core::indexing::WalkerSettings`, gitignore-aware `DiscoveryOptions`, `MAX_FILE_SIZE`, hidden-file traversal, and explicit hidden allowlists before classifying AST-capable versus content-only inputs (`discovery.rs:18-85`). The indexer then drives the write path: `index_file` derives a relative path, parses with optional semantic resolution, detects language, hashes content, reads metadata, and writes through `PostgresCodeFactSink` (`crates/gcode/src/index/indexer/file.rs:1-100`).

The module’s parsing flow is language-aware. `languages.rs` defines a `LanguageSpec` registry of extensions plus tree-sitter symbol/import/call queries, with concrete specs such as Python, JavaScript, and TypeScript (`crates/gcode/src/index/languages.rs:1-100`). The parser extracts call relationships into `CallRelation` records from source, symbols, import context, and optional semantic inputs (`crates/gcode/src/index/parser/calls.rs:1-100`). Specialized call handling includes Dart textual scanning that filters imports, declarations, comments, and ignored names before `materialize_call` (`crates/gcode/src/index/parser/calls/dart_textual.rs:1-100`), and shadowing checks that prevent external calls from winning when a local binding or parameter already defines the same name (`crates/gcode/src/index/parser/calls/shadowing.rs:1-100`).

Import resolution sits between parsing and persistence. `ImportResolutionContext` precomputes Python modules, JS packages, Go package directories, Rust crates, JVM types, Apple/.NET indexes, and scripting-language indexes, wiring together language-specific local resolvers and predicates (`crates/gcode/src/index/import_resolution/context.rs:1`, `crates/gcode/src/index/import_resolution/context.rs:5`, `crates/gcode/src/index/import_resolution/context.rs:9`, `crates/gcode/src/index/import_resolution/context.rs:18`). Binding records deliberately store imported names, candidate files, external roots, members, and default-export shape while deferring final symbol IDs until the indexed-symbol pass (`crates/gcode/src/index/import_resolution/context/bindings.rs:5`, `crates/gcode/src/index/import_resolution/context/bindings.rs:21`, `crates/gcode/src/index/import_resolution/context/bindings.rs:25`).

Semantic resolution collaborates with external `clangd` for C/C++ calls. `SemanticCallRequest`, `SemanticCallTarget`, and `SemanticCallResolver` model the request/response boundary, while `SemanticTargetKind` distinguishes external dependency definitions from project-local candidates that are later narrowed by `index::indexer::local_imports` (`crates/gcode/src/index/semantic.rs:1-100`). This code imports process, thread, timeout, channel, and JSON machinery, then starts from `create_cpp_semantic_resolver`, which requires or discovers `compile_commands.json` and honors `GCODE_REQUIRE_CPP_SEMANTICS` (`crates/gcode/src/index/semantic.rs:1-100`).

| Area | Public Symbols |
| --- | --- |
| Persistence API | `CodeFactWriteRequest`, `CodeFactWriteSummary`, `delete_file_facts`, `upsert_symbols`, `upsert_file`, `upsert_imports`, `upsert_calls`, `upsert_content_chunks` |
| Index orchestration | `IndexRequest`, `IndexOutcome`, `IndexDurations`, `index_files`, `index_file`, `index_overlay_files`, `project_changed_since` |
| Discovery | `discover_files`, `discover_files_with_options`, `classify_file`, `DiscoveryOptions`, `FileClassification`, `HiddenPathAllowlist` |
| Language/parser | `LanguageSpec`, `detect_language`, `parse_file_with_semantic`, `extract_symbols`, `extract_imports`, `extract_calls` |
| Import resolution | `ImportResolutionContext`, `build_import_resolution_context`, `ImportBindings`, `ExtractedImports`, `ExternalCallTarget` |
| Semantic resolution | `SemanticCallRequest`, `SemanticCallTarget`, `SemanticTargetKind`, `SemanticCallResolver`, `create_cpp_semantic_resolver` |

| Environment Variable | Purpose |
| --- | --- |
| `GCODE_REQUIRE_CPP_SEMANTICS` | Makes C/C++ semantic indexing strict when creating the clangd-backed resolver (`crates/gcode/src/index/semantic.rs:1-100`). |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/index/import_resolution\|crates/gcode/src/index/import_resolution]] | The `import_resolution` module builds and uses language-aware indexes for resolving imports and call targets across a mixed-language codebase. Its central `ImportResolutionContext` stores precomputed facts such as Python modules, JS packages, Go package directories, Rust crates, JVM type indexes, and Apple/.NET/scripting-language indexes; the context wires together local submodules for package metadata, Python, Apple, .NET, Elixir, JVM, PHP/Lua/Ruby scripting, JS local resolution, predicates, and Rust local resolution ((crates/gcode/src/index/import_resolution/context.rs:1),… |
| [[code/modules/crates/gcode/src/index/indexer\|crates/gcode/src/index/indexer]] | The `crates/gcode/src/index/indexer` module owns project indexing from discovery through persistence: it indexes individual files, handles content-only fallback, reconciles overlay indexes, probes freshness, resolves local imports, cleans stale projections, and writes facts through a sink abstraction. `index_file` is the core single-file flow: it derives a relative path, parses with semantic resolution, detects language, hashes content, reads metadata, then writes transactional facts through `PostgresCodeFactSink` (`crates/gcode/src/index/indexer/file.rs:1-100`). |
| [[code/modules/crates/gcode/src/index/parser\|crates/gcode/src/index/parser]] | The `crates/gcode/src/index/parser` module focuses on extracting call relationships for the gcode indexer. Its `calls` child module owns call parsing and resolution, producing `CallRelation` records from source, symbols, import context, and optional semantic resolution inputs (`crates/gcode/src/index/parser/calls.rs:1-100`). |
| [[code/modules/crates/gcode/src/index/walker\|crates/gcode/src/index/walker]] | The `crates/gcode/src/index/walker` module discovers and classifies project files for indexing. Its top-level flow walks a root with `gobby_core::indexing::WalkerSettings`, applying gitignore behavior from `DiscoveryOptions`, bounding file size with `MAX_FILE_SIZE`, and enabling hidden traversal before splitting files into AST candidates and content-only candidates (`discovery.rs:18-45`). It then adds hidden files that are explicitly allowlisted through `HiddenPathAllowlist::load(root).discover(root)`, deduplicating by canonical path before routing each file through `classify_file`… |

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

