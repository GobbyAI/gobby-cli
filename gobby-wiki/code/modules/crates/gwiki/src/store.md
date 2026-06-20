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

The `store` module defines the gwiki indexing boundary: shared document/chunk/link/source models, ingestion bookkeeping, scoped identity, validation helpers, and interchangeable `WikiIndexStore` implementations. `types.rs` owns the core data contracts such as `WikiDocument`, `WikiChunk`, `WikiLink`, `WikiSource`, ingestion events, `StoreError`, and `WikiStoreScope`; scope wraps `crate::models::WikiScope` and exposes project/topic identity helpers for storage backends (`crates/gwiki/src/store/types.rs:1-100`).

The main write flow is backend-neutral: callers upsert documents and sources, replace chunks and links, record file hashes, record ingestion events, and delete paths through `WikiIndexStore`. `MemoryWikiStore` keeps those structures in `BTreeMap`s for local shell commands and tests, while validating that chunk/link paths match the target document before replacement (`crates/gwiki/src/store/memory.rs:1-82`). `PostgresWikiStore` performs the same trait role against a PostgreSQL client, deriving scope parameters from `WikiStoreScope`, caching document metadata, and querying `gwiki_documents` by scope and display path (`crates/gwiki/src/store/postgres.rs:1-100`).

Collaboration is concentrated in `helpers.rs`: both storage backends call `validate_chunk_paths` and `validate_link_paths`, while the Postgres backend also imports display-path normalization, scoped ID construction, document-kind/status formatting, and transaction rollback helpers (`crates/gwiki/src/store/helpers.rs:1-100`, `crates/gwiki/src/store/postgres.rs:1-100`). Helpers also bridge path display formats across platforms and cap generated scoped IDs using `gobby_core::indexing::content_hash`, keeping storage identifiers stable and bounded (`crates/gwiki/src/store/helpers.rs:1-100`).

| Public symbol | Kind | Role |
| --- | --- | --- |
| `WikiDocumentKind` | enum | Classifies indexed wiki documents. |
| `WikiDocument` | struct | Full indexed document payload. |
| `WikiChunk` | struct | Byte-ranged searchable document segment. |
| `WikiLink` | struct | Link target and source span metadata. |
| `WikiSource` | struct | Source-file metadata for a document. |
| `WikiIngestionEvent` | enum | Added/changed/deleted/unchanged/skipped ingestion status. |
| `WikiIngestion` | struct | Per-path ingestion record. |
| `WikiStoreScope` | struct | Project/topic storage scope wrapper. |
| `StoreError` | enum | Store validation/database error type. |
| `WikiIndexStore` | trait | Backend contract implemented by memory and Postgres stores. |

| Environment variable | Used by | Purpose |
| --- | --- | --- |
| `GWIKI_MAX_MEMORY_INDEX_BYTES` | `MemoryWikiStore` | Caps markdown bytes accepted by the in-memory indexing path (`crates/gwiki/src/store/memory.rs:1-82`). |
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

