---
title: File Discovery and Indexing
type: code_concept
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
verify_notes:
- id: 2
  reason: Mentions imports/calls extraction and C/C++ semantic behavior not shown in excerpts.
- id: 8
  reason: Invents overlay reconciliation; not shown in the provided code.
- id: 24
  reason: References `create_semantic_resolver_if_needed`, which is not shown.
- id: 27
  reason: References `explicit_file_route` and its mapping behavior, which is not shown.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/api.rs](crates/gcode/src/index/api.rs)
- [crates/gcode/src/index/import_resolution/context.rs](crates/gcode/src/index/import_resolution/context.rs)
- [crates/gcode/src/index/import_resolution/context/apple.rs](crates/gcode/src/index/import_resolution/context/apple.rs)
- [crates/gcode/src/index/import_resolution/context/bindings.rs](crates/gcode/src/index/import_resolution/context/bindings.rs)
- [crates/gcode/src/index/import_resolution/context/package_metadata.rs](crates/gcode/src/index/import_resolution/context/package_metadata.rs)
- [crates/gcode/src/index/import_resolution/helpers.rs](crates/gcode/src/index/import_resolution/helpers.rs)
- [crates/gcode/src/index/import_resolution/js_local.rs](crates/gcode/src/index/import_resolution/js_local.rs)
- [crates/gcode/src/index/import_resolution/parser/go_rust.rs](crates/gcode/src/index/import_resolution/parser/go_rust.rs)
- [crates/gcode/src/index/import_resolution/parser/mod.rs](crates/gcode/src/index/import_resolution/parser/mod.rs)
- [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs)
- [crates/gcode/src/index/import_resolution/parser/scala.rs](crates/gcode/src/index/import_resolution/parser/scala.rs)
- [crates/gcode/src/index/import_resolution/predicates.rs](crates/gcode/src/index/import_resolution/predicates.rs)

_47 more source files omitted._

</details>

# File Discovery and Indexing

## Purpose

File Discovery and Indexing is the `gcode` subsystem that turns a project tree into durable code facts. It discovers eligible files, decides whether each file should receive AST indexing or content-only indexing, parses indexable code, extracts symbols/imports/calls, chunks and hashes content, resolves imports, optionally uses C/C++ semantic call resolution, and persists the resulting facts. [crates/gcode/src/index/api.rs:16-23]

The problem it solves is keeping the index useful without indexing everything blindly. The walker filters unsafe, generated, bundled, hidden, oversized, or unsupported files before the indexer spends parser and database work on them. [crates/gcode/src/index/walker/classification.rs:15-52]

## Covers / Does not cover

This page covers the project-file discovery path, AST-versus-content-only classification, single-file indexing, explicit-file routing, freshness probing, and the parser/call-extraction boundary. Discovery starts from a root path, applies exclude patterns and discovery options, and returns separate AST and content-only candidate lists. [crates/gcode/src/index/walker/discovery.rs:12-17] [crates/gcode/src/index/walker/discovery.rs:19-64]

It does not cover every parser implementation, every language query, or every persisted fact schema. The language registry and parser modules are part of the path, but this page only treats them as dependencies used by discovery and indexing.  [crates/gcode/src/index/parser/calls.rs:26-35]

## Architecture

The system is arranged as a pipeline with a narrow boundary between “which files should be considered?” and “what facts should be written for this file?” The walker owns discovery and classification, while the indexer owns parsing, hashing, metadata checks, transactional writes, freshness, and overlay reconciliation. [crates/gcode/src/index/walker/classification.rs:15-52] [crates/gcode/src/index/indexer/file.rs:15-91]

Discovery uses `gobby_core::indexing::WalkerSettings` configured from `DiscoveryOptions`: it can respect gitignore rules, enforces `MAX_FILE_SIZE`, enables hidden traversal, and then classifies each discovered file. After the normal walk, it separately loads `HiddenPathAllowlist` and discovers explicitly allowed hidden paths, deduplicating by canonical path before routing them through the same classifier. [crates/gcode/src/index/walker/discovery.rs:19-64]

Classification is intentionally conservative. `classify_file` first rejects files that are unsafe, generated wiki metadata, or generated JS bundles. Hidden metadata that is allowed for indexing is routed as content-only. Detected source and data-language files usually become AST candidates, but oversized data-language files are downgraded to content-only to avoid graph/vector/full-text bloat. Undetected text also becomes content-only. [crates/gcode/src/index/walker/classification.rs:15-52]

The indexer then treats AST candidates as parseable files. `index_file` derives a project-relative path, parses with semantic support, detects language, hashes content, reads metadata, and writes facts through `PostgresCodeFactSink` inside a transaction. [crates/gcode/src/index/indexer/file.rs:15-91]

## Data flow

1. A caller starts discovery with `discover_files`, which delegates to `discover_files_with_options` using default discovery options. [crates/gcode/src/index/walker/discovery.rs:12-17]

2. `discover_files_with_options` creates a walker rooted at the project path, applies `respect_gitignore`, bounds file size with `MAX_FILE_SIZE`, enables hidden traversal, and walks entries. Non-files are ignored. [crates/gcode/src/index/walker/discovery.rs:19-64]

3. Each file is passed to `push_classified_file`, which canonicalizes the path for deduplication. If the canonical path has already been seen, the file is skipped. Otherwise, it is classified. [crates/gcode/src/index/walker/discovery.rs:19-64]

4. `classify_file` rejects files that are not safe text files, generated wiki metadata, or generated JS bundles. If the file is hidden metadata that should be indexed only as text, it returns `ContentOnly`. [crates/gcode/src/index/walker/classification.rs:15-52]

5. If language detection succeeds, the file is usually routed to `Ast`. If it is an oversized data-language file, it is routed to `ContentOnly`; if language detection fails for otherwise safe text, it is also routed to `ContentOnly`. [crates/gcode/src/index/walker/classification.rs:15-52]

6. Discovery then loads `HiddenPathAllowlist` and discovers allowed hidden files, passing them through the same deduplication and classification path as regular walker results. [crates/gcode/src/index/walker/discovery.rs:19-64]

7. For AST files, `index_file` computes the relative path. If the file cannot be made relative to the project root, indexing returns `None` and the file is skipped. [crates/gcode/src/index/indexer/file.rs:15-91]

8. `index_file` calls `parser::parse_file_with_semantic`. If parsing returns no parse result, indexing returns `None`. [crates/gcode/src/index/indexer/file.rs:15-91]

9. The indexer detects language, hashes file content, and reads metadata. If hashing fails, metadata cannot be read, or the metadata size cannot fit the expected type, the AST index is skipped. [crates/gcode/src/index/indexer/file.rs:15-91]

10. When those dependencies are available, the indexer opens a PostgreSQL transaction, creates a `PostgresCodeFactSink`, and writes the indexed facts transactionally. [crates/gcode/src/index/indexer/file.rs:15-91]

11. Freshness checks can avoid the expensive path. `project_changed_since` discovers files with the same walker path, compares mtimes against `last_indexed_at` with a skew margin, and also checks for indexed paths that no longer exist. It returns `false` only when the on-disk tree still matches the recorded index. [crates/gcode/src/index/indexer/freshness_probe.rs:37-81]

12. If C++ semantic resolution is needed, `create_semantic_resolver_if_needed` returns `None` when no candidate path requires it; otherwise it delegates resolver creation to the semantic layer. [crates/gcode/src/index/indexer/file.rs:93-102]

## Key components

The core pieces to read are the walker classifier, the discovery entry points, the single-file indexer, and the freshness probe.

| Symbol | Role |
| --- | --- |
| `discover_files_with_options` | Walks a project root, applies discovery options and file-size limits, includes hidden allowlisted files, deduplicates paths, and returns AST plus content-only candidates. [crates/gcode/src/index/walker/discovery.rs:19-64] |
| `classify_file` | Decides whether a safe discovered file should be skipped, AST-indexed, or content-only indexed. [crates/gcode/src/index/walker/classification.rs:15-52] |
| `index_file` | Performs the single-file AST indexing flow: relative path, parse, language detection, hash, metadata, and transactional fact writes. [crates/gcode/src/index/indexer/file.rs:15-91] |
| `explicit_file_route` | Maps an explicitly requested file to `Ast`, `ContentOnly`, or `Skip` using walker classification. [crates/gcode/src/index/indexer/file.rs:120-130] |
| `project_changed_since` | Lock-free freshness pre-gate that checks whether discovered files changed since the last recorded index. [crates/gcode/src/index/indexer/freshness_probe.rs:37-81] |

## Where to start

Start with `discover_files_with_options` to understand how the candidate sets are built, then read `classify_file` to understand the routing rules. After that, read `index_file`, because it is the core single-file bridge from a classified AST candidate to persisted code facts. [crates/gcode/src/index/walker/discovery.rs:19-64] [crates/gcode/src/index/walker/classification.rs:15-52] [crates/gcode/src/index/indexer/file.rs:15-91]

## Explore

- [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]
- [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]
- [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]
- [[code/modules/crates/gcode/src/index/parser|crates/gcode/src/index/parser]]

