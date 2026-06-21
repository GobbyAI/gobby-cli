---
title: Code Indexing Pipeline
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

# Code Indexing Pipeline

## Purpose

The Code Indexing Pipeline turns a directory of source code into structured, queryable facts. Rather than treating a repository as opaque text, this concept walks the filesystem, decides which files are code and what language they are, parses each one into a syntax tree, extracts meaningful facts (symbols, imports, calls, and content chunks), and writes those facts to durable storage in a single transactional unit. The problem it solves is bridging raw files on disk and a structured index that downstream features can query without re-reading or re-parsing source every time.

The pipeline is organized as a sequence of stages so that each concern — discovery, classification, parsing, extraction, persistence — can be reasoned about and changed independently. The top-level module entry point lives at [crates/gcode/src/index/api.rs:16-23], which exposes the indexing surface to the rest of the crate.

## Covers / Does not cover

This page covers the end-to-end indexing flow inside `crates/gcode/src/index`: how files are found and filtered by the walker, how a single file is processed by the indexer, and how the extracted facts are persisted transactionally. It covers the three constituent modules — the index API at [crates/gcode/src/index/api.rs:16-23], the per-file indexer at [crates/gcode/src/index/indexer/file.rs:15-91], and the walker's language classification at [crates/gcode/src/index/walker/classification.rs:15-52].

It does not cover the concrete tree-sitter grammar definitions, the storage backend internals where facts are ultimately written, or how consumers query the resulting index. Because the supplied input exposes no indexed symbols and no source excerpts, this page also does not enumerate specific function signatures, struct fields, CLI flags, or configuration keys; those are out of scope here and should be read directly from the cited modules.

## Architecture

The pipeline is arranged as three cooperating modules under `crates/gcode/src/index`, layered from coarse-grained discovery down to fine-grained persistence. This separation exists because the stages have very different responsibilities and failure modes: traversing a filesystem is I/O- and policy-heavy, parsing is CPU-heavy and language-specific, and persistence must be atomic.

At the outer layer, the **walker** is responsible for discovery and classification. The classification logic at [crates/gcode/src/index/walker/classification.rs:15-52] decides whether a discovered file is source code worth indexing and assigns it a language, which determines how it will be parsed downstream. Putting classification at the boundary means non-code and unsupported files are filtered out early, so later stages only ever see candidates they can actually process.

At the inner layer, the **indexer** handles a single file at a time. The per-file processing at [crates/gcode/src/index/indexer/file.rs:15-91] is where tree-sitter parsing and fact extraction happen — turning a classified file into symbols, imports, calls, and content chunks — and where those facts are committed transactionally. Scoping this to one file keeps the unit of work small and lets the pipeline parallelize or isolate failures per file.

The **index module API** at [crates/gcode/src/index/api.rs:16-23] sits above both, composing the walker and indexer into the public indexing entry point. This is the seam the rest of the crate depends on, so the walker and indexer internals can evolve without changing callers.

## Data flow

The following traces the real runtime flow from an indexing request to persisted facts:

1. A caller invokes the index module's public surface at [crates/gcode/src/index/api.rs:16-23], which initiates a pass over a target directory.
2. The walker discovers files on disk and passes each one to classification at [crates/gcode/src/index/walker/classification.rs:15-52].
3. Classification determines whether the file is indexable code and assigns its language. If the file cannot be classified as supported source — for example, a binary, generated, or unsupported file type — it is filtered out at this stage and never reaches the indexer, so no parsing or persistence occurs for it.
4. Each classified file is handed to the per-file indexer at [crates/gcode/src/index/indexer/file.rs:15-91], where it is parsed with tree-sitter according to its assigned language.
5. From the resulting syntax tree, the indexer extracts facts: symbols, imports, calls, and content chunks.
6. The extracted facts are written to storage in a single transaction, so a file's contributions to the index are applied atomically rather than partially.

## Key components

The pipeline is small and module-centric; the most important pieces to know are the three modules that form its stages. (The supplied input exposes no individual indexed symbols, so the table lists the modules and their roles.)

| Component | Anchor | Role |
| --- | --- | --- |
| `index` API | [crates/gcode/src/index/api.rs:16-23] | Public entry point that composes walking and indexing into one pipeline. |
| `indexer` (per-file) | [crates/gcode/src/index/indexer/file.rs:15-91] | Parses a single file with tree-sitter, extracts facts, and persists them transactionally. |
| `walker` classification | [crates/gcode/src/index/walker/classification.rs:15-52] | Filters discovered files and assigns languages, gating what reaches the indexer. |

## Where to start

Start with the index module API at [crates/gcode/src/index/api.rs:16-23] to see how the pipeline is composed and entered. Then read the walker's classification at [crates/gcode/src/index/walker/classification.rs:15-52] to understand which files become candidates and how their language is decided, since that gates everything downstream. Finish with the per-file indexer at [crates/gcode/src/index/indexer/file.rs:15-91], which is where parsing, fact extraction, and transactional persistence actually take place.

## Explore

- [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]
- [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]
- [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

