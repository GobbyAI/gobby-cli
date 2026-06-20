---
title: Building the Code Index
type: code_narrative
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
  reason: Claims parsing for symbols/imports/calls, but the supplied excerpts do not show that behavior.
- id: 10
  reason: Refers to `explicit_file_route`, which is not shown in the provided excerpts.
- id: 16
  reason: Claims `CallRelation` extraction and Dart fallback behavior, but no parser-call excerpt is supplied.
- id: 18
  reason: Table rows for `create_semantic_resolver_if_needed` and `explicit_file_route` are not supported by the excerpts.
- id: 20
  reason: Claims `calls.rs` explains `CallRelation` generation for later consumers, but that file excerpt is not provided.
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

# Building the Code Index

## Why this matters

The code index is the first place where raw project files become reusable facts: files are discovered, routed into AST or content-only indexing, parsed for symbols/imports/calls, checked for freshness, and persisted for later consumers. The main design decision is to split the pipeline early: source-like files become AST candidates, while hidden metadata, oversized data files, and unrecognized text are still indexed as content without bloating symbol graphs or semantic projections [crates/gcode/src/index/walker/classification.rs:15-52].

That split also keeps discovery, freshness checks, and indexing aligned. The freshness probe deliberately reuses walker discovery, so the cheap “did anything change?” gate sees the same file universe that the indexer will later process [crates/gcode/src/index/indexer/freshness_probe.rs:37-81].

## How it works

1. Discovery starts at the project root. `discover_files` delegates to `discover_files_with_options` with default discovery options, returning two lists: AST candidates and content-only candidates [crates/gcode/src/index/walker/discovery.rs:12-17].

2. `discover_files_with_options` builds a `gobby_core::indexing::WalkerSettings` walker, applies `respect_gitignore`, caps file size with `MAX_FILE_SIZE`, enables hidden traversal, and walks regular files only [crates/gcode/src/index/walker/discovery.rs:19-64].

3. Hidden files get a second pass through `HiddenPathAllowlist::load(root).discover(root)`. Each path is canonicalized for de-duplication before classification, so allowlisted hidden paths do not create duplicate work if already seen [crates/gcode/src/index/walker/discovery.rs:19-64].

4. `classify_file` decides whether a file should be indexed at all. Unsafe files, generated wiki metadata, and generated JS bundles are skipped. Hidden metadata that is allowed through becomes content-only [crates/gcode/src/index/walker/classification.rs:15-52].

5. If a language is detected, the file usually becomes an AST candidate. Oversized data-language files such as JSON or YAML are downgraded to content-only to avoid emitting excessive property symbols. If no language is detected, safe text still becomes content-only [crates/gcode/src/index/walker/classification.rs:15-52].

6. Explicit single-file indexing follows the same routing rules. `explicit_file_route` maps classification to `ExplicitFileRoute::Ast`, `ExplicitFileRoute::ContentOnly`, or `ExplicitFileRoute::Skip`; `classify_explicit_file_with_options` can also skip a path when gitignore respect is enabled and the explicit path is not visible [crates/gcode/src/index/indexer/file.rs:120-130] [crates/gcode/src/index/walker/classification.rs:56-66].

7. Before expensive indexing, `project_changed_since` performs a lock-free, hash-free freshness check. It subtracts a two-second skew margin from `last_indexed_at`, discovers files with the same walker path, and returns `true` on a newer discovered file or a previously indexed path that no longer exists. A `false` result allows callers to skip the advisory lock and full re-hash [crates/gcode/src/index/indexer/freshness_probe.rs:37-81].

8. For an AST candidate, `index_file` derives the path relative to the root. If that fails, the file is skipped with `Ok(None)` [crates/gcode/src/index/indexer/file.rs:15-91].

9. The file is parsed with `parser::parse_file_with_semantic`, using project context, root path, excludes, import context, and an optional semantic resolver. If parsing returns no result, indexing skips the file [crates/gcode/src/index/indexer/file.rs:15-91].

10. Language detection supplies the stored language name, defaulting to `"unknown"` when detection fails. The indexer then hashes file content and reads metadata; unreadable content, unreadable metadata, or unsupported file sizes all cause the AST index path to skip that file rather than writing partial facts [crates/gcode/src/index/indexer/file.rs:15-91].

11. When the file passes those gates, `index_file` opens a PostgreSQL transaction and writes facts through `PostgresCodeFactSink`, keeping persistence transactional for the indexed file [crates/gcode/src/index/indexer/file.rs:15-91].

12. Call extraction lives under the parser module. It produces `CallRelation` records from source, symbols, import context, and optional semantic inputs, with language-specific textual fallbacks such as Dart when needed [crates/gcode/src/index/parser/calls.rs:26-35] .

## Key components

| Symbol | Role |
| --- | --- |
| `discover_files_with_options` | Walks the root, applies discovery options and file-size bounds, adds hidden allowlist files, de-duplicates paths, and returns AST/content-only lists [crates/gcode/src/index/walker/discovery.rs:19-64]. |
| `classify_file` | Routes files to AST, content-only, or skip based on safety, generated-file checks, hidden metadata, language detection, and oversized data-language handling [crates/gcode/src/index/walker/classification.rs:15-52]. |
| `project_changed_since` | Cheap freshness pre-gate that checks discovered file mtimes and deleted indexed paths before taking heavier indexing locks [crates/gcode/src/index/indexer/freshness_probe.rs:37-81]. |
| `index_file` | Core single-file AST indexing flow: relative path, semantic parse, language detection, hash/metadata checks, and transactional fact writes [crates/gcode/src/index/indexer/file.rs:15-91]. |
| `create_semantic_resolver_if_needed` | Creates a C++ semantic resolver only when candidate paths require it; otherwise returns `None` [crates/gcode/src/index/indexer/file.rs:93-102]. |
| `explicit_file_route` | Applies normal classification to an explicitly requested file and maps it to `Ast`, `ContentOnly`, or `Skip` [crates/gcode/src/index/indexer/file.rs:120-130]. |

## What to read next

Read the parser call-extraction chapter next, especially `crates/gcode/src/index/parser/calls.rs`, because it explains how the AST/content side of this pipeline becomes concrete `CallRelation` records for later graph and search consumers [crates/gcode/src/index/parser/calls.rs:26-35].

## Concepts

- [[code/concepts/file-discovery-and-indexing|File Discovery and Indexing]]

## Explore

- [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]
- [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]
- [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]
- [[code/modules/crates/gcode/src/index/parser|crates/gcode/src/index/parser]]

## Continue the tour

- ← Previous: [[code/narrative/cli-runtime-foundation|CLI Runtime Foundation]]
- Next →: [[code/narrative/resolving-relationships|Resolving Relationships]]

