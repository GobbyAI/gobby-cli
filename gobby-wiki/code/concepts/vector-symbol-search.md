---
title: Vector Symbol Search
type: code_concept
provenance:
- file: crates/gcode/src/commands/vector.rs
- file: crates/gcode/src/projection/mod.rs
- file: crates/gcode/src/projection/sync.rs
- file: crates/gcode/src/vector/code_symbols.rs
- file: crates/gcode/src/vector/code_symbols/embedding.rs
- file: crates/gcode/src/vector/code_symbols/lifecycle.rs
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
- file: crates/gcode/src/vector/code_symbols/repository.rs
- file: crates/gcode/src/vector/code_symbols/search.rs
- file: crates/gcode/src/vector/code_symbols/tests.rs
- file: crates/gcode/src/vector/code_symbols/types.rs
- file: crates/gcode/src/vector/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 2
  reason: '`code_symbols` module exposure and the `repository` submodule are not shown in the excerpts.'
- id: 3
  reason: Claims about the gap between syntactic indexing, intent lookup, and graph relationships are not shown here.
- id: 5
  reason: '`payload storage` is not shown in the provided excerpts.'
- id: 6
  reason: Projection-module ownership of graph/vector cleanup boundaries is not shown in the excerpts.
- id: 8
  reason: The claim that `code_symbols` is the domain module for semantic indexing/search is not shown.
- id: 9
  reason: The struct fields are shown, but the stated sync/clear/schema-validation behavior is not evidenced.
- id: 10
  reason: '`search request construction` is not shown in the Qdrant excerpt.'
- id: 11
  reason: '`prints lifecycle output` is not shown in the command excerpt.'
- id: 16
  reason: Symbol-to-embedding text generation is not shown in the provided excerpt.
- id: 17
  reason: Payload fields like provenance, confidence, and summaries are not shown.
- id: 20
  reason: The clear-project schema/distance checks and deletion report are not shown in the excerpt.
- id: 21
  reason: The CLI `cleanup_orphans` flow is not shown in the provided command excerpt.
- id: 24
  reason: The `CodeSymbolVectorLifecycle` role includes sync/clear/schema validation, which is not evidenced here.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/vector.rs](crates/gcode/src/commands/vector.rs)
- [crates/gcode/src/projection/mod.rs](crates/gcode/src/projection/mod.rs)
- [crates/gcode/src/projection/sync.rs](crates/gcode/src/projection/sync.rs)
- [crates/gcode/src/vector/code_symbols.rs](crates/gcode/src/vector/code_symbols.rs)
- [crates/gcode/src/vector/code_symbols/embedding.rs](crates/gcode/src/vector/code_symbols/embedding.rs)
- [crates/gcode/src/vector/code_symbols/lifecycle.rs](crates/gcode/src/vector/code_symbols/lifecycle.rs)
- [crates/gcode/src/vector/code_symbols/qdrant.rs](crates/gcode/src/vector/code_symbols/qdrant.rs)
- [crates/gcode/src/vector/code_symbols/repository.rs](crates/gcode/src/vector/code_symbols/repository.rs)
- [crates/gcode/src/vector/code_symbols/search.rs](crates/gcode/src/vector/code_symbols/search.rs)
- [crates/gcode/src/vector/code_symbols/tests.rs](crates/gcode/src/vector/code_symbols/tests.rs)
- [crates/gcode/src/vector/code_symbols/types.rs](crates/gcode/src/vector/code_symbols/types.rs)
- [crates/gcode/src/vector/mod.rs](crates/gcode/src/vector/mod.rs)

</details>

# Vector Symbol Search

## Purpose

Vector Symbol Search is the semantic-search path for indexed code symbols. It takes extracted `Symbol` records, turns them into embedding-ready text, stores vector records in Qdrant with enough payload metadata to identify the original symbol and source location, and later ranks symbols by semantic similarity to a query. The public vector entry point is intentionally narrow: `crates/gcode/src/vector` exposes `code_symbols`, and `code_symbols` fans out into embedding, lifecycle, Qdrant, repository, search, and type submodules for the full indexing/search surface. [crates/gcode/src/vector/code_symbols.rs:1-29]

The concept solves the gap between syntactic indexing and intent-based lookup: callers can search for code by meaning, not only by exact names or graph relationships. The same subsystem also owns operational concerns such as collection lifecycle, deletion, orphan cleanup, and degraded search error handling. [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37] [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85]

## Covers / Does not cover

This page covers the code-symbol vector path: embedding source resolution, embedding backend setup, Qdrant collection naming and payload storage, lifecycle operations, cleanup, and semantic search results. It also covers the CLI-facing lifecycle commands where they route into the vector module. [crates/gcode/src/commands/vector.rs:16-22]

It does not cover graph projection behavior except where projection cleanup coordinates with vector deletion. The projection module owns graph/vector synchronization cleanup boundaries, including deleting vectors when Qdrant is configured, but graph storage and traversal are outside this concept. [crates/gcode/src/projection/mod.rs:8-11]

## Architecture

The architecture is split around runtime responsibilities. `code_symbols` is the domain module for semantic code-symbol indexing and search. Its embedding layer chooses whether embeddings are produced through the daemon-backed AI context or direct embedding configuration, represented by `EmbeddingSource`. [crates/gcode/src/vector/code_symbols/embedding.rs:26-29] `EmbeddingBackend` wraps that source and carries an optional blocking HTTP client for direct embedding calls. [crates/gcode/src/vector/code_symbols/embedding.rs:44-47]

Lifecycle management is centralized in `CodeSymbolVectorLifecycle`. It keeps the project id, collection name, Qdrant config, embedding backend, vector settings, an optional probed vector dimension, and an HTTP client together so sync, clear, and schema validation operate with one consistent runtime boundary. [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]

Qdrant-specific logic is separated into the Qdrant module. That module owns collection naming, deletion helpers, search request construction, and orphan cleanup summaries such as `VectorOrphanCleanup`. [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27] This keeps transport/storage mechanics separate from the higher-level lifecycle and search APIs.

The command layer is a thin orchestration boundary. It resolves context, opens the database when needed, constructs lifecycle objects, and prints lifecycle output, while the vector module performs the actual vector operations. [crates/gcode/src/commands/vector.rs:16-22]

## Data flow

1. Indexed symbols are fetched from the project database for a file, then passed into the vector lifecycle for synchronization. The `sync_file` command first verifies that the indexed file exists; if it is missing and `allow_missing_indexed_file` is enabled, it prints a skipped result, otherwise it fails. [crates/gcode/src/commands/vector.rs:16-22]

2. The command builds a lifecycle from context. It requires Qdrant configuration and an embedding source; if either dependency is unavailable, lifecycle construction returns `MissingQdrantConfig` or `MissingEmbeddingConfig` instead of continuing. [crates/gcode/src/commands/vector.rs:16-22]

3. `CodeSymbolVectorLifecycle::new` creates the project-scoped collection name, validates the Qdrant boundary, builds an `EmbeddingBackend`, and stores vector settings and HTTP state for subsequent operations. [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]

4. The embedding layer turns symbols into embedding text and produces embeddings through either daemon-routed context or direct embedding configuration. For direct embedding, `EmbeddingBackend::new` validates that the embedding API base is present before constructing the client; missing config is reported as a vector lifecycle error. [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] [crates/gcode/src/vector/code_symbols/embedding.rs:44-47]

5. The lifecycle writes vectors to the Qdrant collection using payloads that preserve symbol identity, source ranges, provenance, confidence, and optional summaries, so search hits can round-trip back to indexed code. [crates/gcode/src/vector/code_symbols/embedding.rs:21-23]

6. Semantic search starts in `search_code_symbols`. It requires Qdrant config, resolves an embedding source, embeds the query, derives the collection name, and calls vector search. Missing Qdrant config, missing embedding config, failed query embedding, invalid collection names, and transport/search failures are converted into `SearchError` variants. [crates/gcode/src/vector/code_symbols/search.rs:8-14]

7. Successful vector search returns scored symbol ids, which are mapped into `CodeSymbolVectorSearchHit` results containing `symbol_id` and `score`. [crates/gcode/src/vector/code_symbols/search.rs:8-14]

8. Lifecycle cleanup paths remove stale vector data. `clear_project_vectors` validates the Qdrant boundary, optionally checks collection schema against configured dimension and cosine distance, deletes project vectors if the collection exists, and reports the clear action and deletion count. [crates/gcode/src/vector/code_symbols/lifecycle.rs:120-141]

9. Orphan cleanup scans vector-backed file paths for a project, compares them with indexed file paths, deletes vectors for files no longer indexed, and returns a cleanup report. The CLI `cleanup_orphans` command gathers indexed paths, calls `cleanup_orphan_file_vectors`, and prints the report. [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85] [crates/gcode/src/commands/vector.rs:154-166]

## Key components

The main symbols to read are the ones that define the runtime boundary, embedding choice, Qdrant maintenance, and search failure model.

| Symbol | Role |
| --- | --- |
| `CodeSymbolVectorLifecycle` | Project-scoped lifecycle object for collection setup, sync, clear, schema validation, and vector operations. [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37] |
| `EmbeddingSource` | Chooses daemon-backed AI context or direct embedding configuration. [crates/gcode/src/vector/code_symbols/embedding.rs:26-29] |
| `EmbeddingBackend` | Wraps the embedding source and optional direct HTTP client. [crates/gcode/src/vector/code_symbols/embedding.rs:44-47] |
| `SearchError` | Public semantic-search error model for missing config, embedding failure, invalid collection names, and vector-search failures. [crates/gcode/src/vector/code_symbols/search.rs:8-14] |
| `cleanup_orphan_file_vectors` | Removes Qdrant vectors whose file paths are no longer present in the indexed file set. [crates/gcode/src/vector/code_symbols/qdrant.rs:60-85] |

## Where to start

Start with `CodeSymbolVectorLifecycle`, because it shows the runtime shape of the subsystem: project id, Qdrant config, embedding backend, vector settings, probed vector size, and HTTP client are all assembled there. [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37]

After that, read `EmbeddingSource` and `EmbeddingBackend` to understand how text becomes vectors, then `search_code_symbols` to see the query-time path and its degraded error behavior. [crates/gcode/src/vector/code_symbols/embedding.rs:26-29] [crates/gcode/src/vector/code_symbols/embedding.rs:44-47] [crates/gcode/src/vector/code_symbols/search.rs:8-14]

## Explore

- [[code/modules/crates/gcode/src/vector|crates/gcode/src/vector]]
- [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]
- [[code/modules/crates/gcode/src/projection|crates/gcode/src/projection]]

