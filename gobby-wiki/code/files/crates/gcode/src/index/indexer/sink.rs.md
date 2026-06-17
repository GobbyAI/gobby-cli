---
title: crates/gcode/src/index/indexer/sink.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/sink.rs
  ranges:
  - 6-34
  - 36-38
  - 41-43
  - 50-52
  - 54-60
  - 62-69
  - 71-73
  - 75-77
  - 79-86
  - 88-95
  - 97-99
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer/sink.rs:6-34](crates/gcode/src/index/indexer/sink.rs#L6-L34), [crates/gcode/src/index/indexer/sink.rs:36-38](crates/gcode/src/index/indexer/sink.rs#L36-L38), [crates/gcode/src/index/indexer/sink.rs:41-43](crates/gcode/src/index/indexer/sink.rs#L41-L43), [crates/gcode/src/index/indexer/sink.rs:50-52](crates/gcode/src/index/indexer/sink.rs#L50-L52), [crates/gcode/src/index/indexer/sink.rs:54-60](crates/gcode/src/index/indexer/sink.rs#L54-L60), [crates/gcode/src/index/indexer/sink.rs:62-69](crates/gcode/src/index/indexer/sink.rs#L62-L69), [crates/gcode/src/index/indexer/sink.rs:71-73](crates/gcode/src/index/indexer/sink.rs#L71-L73), [crates/gcode/src/index/indexer/sink.rs:75-77](crates/gcode/src/index/indexer/sink.rs#L75-L77), [crates/gcode/src/index/indexer/sink.rs:79-86](crates/gcode/src/index/indexer/sink.rs#L79-L86), [crates/gcode/src/index/indexer/sink.rs:88-95](crates/gcode/src/index/indexer/sink.rs#L88-L95), [crates/gcode/src/index/indexer/sink.rs:97-99](crates/gcode/src/index/indexer/sink.rs#L97-L99)

</details>

# crates/gcode/src/index/indexer/sink.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file defines the `CodeFactSink` trait as the indexer’s write interface for code facts, covering cleanup of file-scoped data and upserts for symbols, files, imports, calls, and content chunks. It also provides `PostgresCodeFactSink`, a thin wrapper around a mutable `postgres::GenericClient` that implements the trait by delegating each operation to the corresponding functions in `crate::index::api`, so the indexer can update the database through one consistent sink abstraction.
[crates/gcode/src/index/indexer/sink.rs:6-34]
[crates/gcode/src/index/indexer/sink.rs:36-38]
[crates/gcode/src/index/indexer/sink.rs:41-43]
[crates/gcode/src/index/indexer/sink.rs:50-52]
[crates/gcode/src/index/indexer/sink.rs:54-60]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CodeFactSink` | type | `pub(super) trait CodeFactSink {` | `CodeFactSink [type]` | `4beb9119-9fd1-58f8-95af-7e14c1d44a43` | 6-34 [crates/gcode/src/index/indexer/sink.rs:6-34] | Indexed type `CodeFactSink` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:6-34] |
| `PostgresCodeFactSink` | class | `pub(super) struct PostgresCodeFactSink<'a, C> {` | `PostgresCodeFactSink [class]` | `519b1645-56e3-50f6-bcf8-ece8c93623d0` | 36-38 [crates/gcode/src/index/indexer/sink.rs:36-38] | Indexed class `PostgresCodeFactSink` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:36-38] |
| `new` | function | `pub(super) fn new(conn: &'a mut C) -> Self {` | `new [function]` | `f66039bb-8d68-531b-96d3-7d0f7f01ee33` | 41-43 [crates/gcode/src/index/indexer/sink.rs:41-43] | Indexed function `new` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:41-43] |
| `delete_file_facts` | function | `fn delete_file_facts(&mut self, project_id: &str, file_path: &str) -> anyhow::Result<()> {` | `delete_file_facts [function]` | `6f175061-24d5-5b38-9496-113a1f6e9a8f` | 50-52 [crates/gcode/src/index/indexer/sink.rs:50-52] | Indexed function `delete_file_facts` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:50-52] |
| `delete_file_non_symbol_facts` | function | `fn delete_file_non_symbol_facts(` | `delete_file_non_symbol_facts [function]` | `e97c7665-91dc-5e5f-853e-c000add5a733` | 54-60 [crates/gcode/src/index/indexer/sink.rs:54-60] | Indexed function `delete_file_non_symbol_facts` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:54-60] |
| `delete_stale_file_symbols` | function | `fn delete_stale_file_symbols(` | `delete_stale_file_symbols [function]` | `7a4de9ca-1c4c-5b93-b739-f5d7061ce532` | 62-69 [crates/gcode/src/index/indexer/sink.rs:62-69] | Indexed function `delete_stale_file_symbols` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:62-69] |
| `upsert_symbols` | function | `fn upsert_symbols(&mut self, symbols: &[Symbol]) -> anyhow::Result<usize> {` | `upsert_symbols [function]` | `2039da60-88d9-5567-a021-f3c6b66cec2a` | 71-73 [crates/gcode/src/index/indexer/sink.rs:71-73] | Indexed function `upsert_symbols` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:71-73] |
| `upsert_file` | function | `fn upsert_file(&mut self, file: &IndexedFile) -> anyhow::Result<()> {` | `upsert_file [function]` | `4fd617f2-fa69-5f18-b533-aafb5806be6d` | 75-77 [crates/gcode/src/index/indexer/sink.rs:75-77] | Indexed function `upsert_file` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:75-77] |
| `upsert_imports` | function | `fn upsert_imports(` | `upsert_imports [function]` | `5a0d366b-f54c-5559-a559-34ed1702125b` | 79-86 [crates/gcode/src/index/indexer/sink.rs:79-86] | Indexed function `upsert_imports` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:79-86] |
| `upsert_calls` | function | `fn upsert_calls(` | `upsert_calls [function]` | `e0e15eb2-cccd-5aa8-854e-8076d3687047` | 88-95 [crates/gcode/src/index/indexer/sink.rs:88-95] | Indexed function `upsert_calls` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:88-95] |
| `upsert_content_chunks` | function | `fn upsert_content_chunks(&mut self, chunks: &[ContentChunk]) -> anyhow::Result<usize> {` | `upsert_content_chunks [function]` | `0d1aa3ba-2660-51b7-946a-8e929bfccee1` | 97-99 [crates/gcode/src/index/indexer/sink.rs:97-99] | Indexed function `upsert_content_chunks` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:97-99] |
