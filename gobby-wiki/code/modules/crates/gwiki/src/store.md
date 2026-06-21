---
title: crates/gwiki/src/store
type: code_module
provenance:
- file: crates/gwiki/src/store/helpers.rs
- file: crates/gwiki/src/store/memory.rs
- file: crates/gwiki/src/store/postgres.rs
- file: crates/gwiki/src/store/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/store

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

## crates/gwiki/src/store

The `store` module defines the persistence layer for gwiki's wiki index. It establishes the core domain types used throughout ingestion pipelines — documents, content chunks, inter-document links, sources, and ingestion events — and exposes a `WikiIndexStore` trait that abstracts over different backing stores (types.rs:1–100). Scoping logic (`WikiStoreScope`) ties every indexed artifact to either a project or a named topic via the lower-level `WikiScope` model imported from `crate::models` (types.rs:5), and accessor methods such as `scope_kind`, `scope_id`, `project_id`, and `topic_name` expose those scope dimensions to implementors (types.rs:87–107).

Two concrete implementations ship with the module. `PostgresWikiStore` (postgres.rs:24–38) wraps a live `postgres::Client` reference and persists documents, chunks, links, and sources into the `gwiki_documents` relational schema; it caches `DocumentMeta` in a `BTreeMap` to avoid redundant round-trips (postgres.rs:47–72) and reconstructs platform-native paths from stored display strings on read-back. `MemoryWikiStore` (memory.rs:15–28) holds all state in plain `BTreeMap` collections, making it suitable for local shell commands, unit tests, and memory-bounded ingestion runs; the comment in memory.rs notes that `GWIKI_MAX_MEMORY_INDEX_BYTES` can cap the markdown bytes accepted by this path (memory.rs:11–13).

The `helpers` sub-file provides shared utilities consumed by both implementations: path normalisation (`display_path`, `platform_path_from_display`), cross-platform path equivalence checks, structural validation that chunk and link paths match their parent document (`validate_chunk_paths`, `validate_link_paths`), and a deterministic ID generation scheme that encodes scope kind, scope identity, and document path into a capped identifier via a content hash suffix (`scoped_id`, `scoped_text_id`, `cap_scoped_id_with_hash`) (helpers.rs:9–10, 63–90). Constants `MAX_ID_LEN = 63` and `HASH_SUFFIX_LEN = 12` govern that truncation (helpers.rs:9–10). `StoreError` wraps both `postgres` driver errors (via a `From` impl) and an `InvalidData` variant carrying a field name and message, giving callers uniform error handling regardless of backend.

### Public Types

| Symbol | Kind | Description |
|---|---|---|
| `WikiDocumentKind` | enum | Document classification: `SourceCatalog`, `SourceNote`, `Concept`, `Topic`, `CodeDoc` (types.rs:7–13) |
| `WikiDocument` | struct | Indexed document with path, kind, title, content hash, and body (types.rs:16–22) |
| `WikiChunk` | struct | Sub-document text slice with byte offsets and optional heading (types.rs:24–31) |
| `WikiLink` | struct | Outbound link with target, optional alias, and byte offsets (types.rs:33–40) |
| `WikiSource` | struct | Source file entry pointing back to its rendered document (types.rs:42–48) |
| `WikiIngestionEvent` | enum | Outcome per file: `Added`, `Changed`, `Deleted`, `Unchanged`, `Skipped` (types.rs:50–57) |
| `WikiIngestion` | struct | Ingestion record pairing a path with its event and optional hash (types.rs:59–63) |
| `WikiStoreScope` | struct | Scope container wrapping a project ID or topic name (types.rs:65–107) |
| `WikiIndexStore` | trait | Abstraction over `upsert_document`, `replace_chunks`, `replace_links`, `upsert_source`, `record_ingestion`, `record_file_hash`, `indexed_hashes` |
| `PostgresWikiStore` | struct | Postgres-backed implementation; requires a mutable `postgres::Client` (postgres.rs:24–38) |
| `MemoryWikiStore` | struct | In-memory implementation for tests and local commands (memory.rs:15–28) |
| `StoreError` | type | Unified error with `InvalidData { field, message }` and `From<postgres::Error>` conversions |

### `WikiStoreScope` Methods

| Method | Description |
|---|---|
| `project(project_id)` | Creates a project-scoped scope (types.rs:72–77) |
| `topic(topic_name)` | Creates a topic-scoped scope (types.rs:79–84) |
| `scope_kind()` | Returns the discriminant string (`"project"` / `"topic"`) (types.rs:86–88) |
| `scope_id()` | Returns the canonical identity string for the scope (types.rs:90–92) |
| `project_id()` | Returns `Option<String>` for project scopes, used internally (types.rs:94–96) |
| `topic_name()` | Returns `Option<String>` for topic scopes, used internally |

### Environment Variables

| Variable | Effect |
|---|---|
| `GWIKI_MAX_MEMORY_INDEX_BYTES` | Caps markdown bytes accepted by `MemoryWikiStore` before indexing (memory.rs:11–13) |

### Helper ID-generation Constants

| Constant | Value | Purpose |
|---|---|---|
| `MAX_ID_LEN` | `63` | Maximum character length of a generated scoped ID (helpers.rs:9) |
| `HASH_SUFFIX_LEN` | `12` | Characters of content hash appended when an ID is truncated (helpers.rs:10) |
[crates/gwiki/src/store/helpers.rs:12-14]
[crates/gwiki/src/store/memory.rs:16-28]
[crates/gwiki/src/store/postgres.rs:18-22]
[crates/gwiki/src/store/types.rs:8-14]
[crates/gwiki/src/store/helpers.rs:16-21]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/store/helpers.rs\|crates/gwiki/src/store/helpers.rs]] | `crates/gwiki/src/store/helpers.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gwiki/src/store/memory.rs\|crates/gwiki/src/store/memory.rs]] | `crates/gwiki/src/store/memory.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/store/postgres.rs\|crates/gwiki/src/store/postgres.rs]] | `crates/gwiki/src/store/postgres.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/store/types.rs\|crates/gwiki/src/store/types.rs]] | `crates/gwiki/src/store/types.rs` exposes 18 indexed API symbols. |

