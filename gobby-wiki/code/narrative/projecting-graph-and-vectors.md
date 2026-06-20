---
title: Projecting Graph and Vectors
type: code_narrative
provenance:
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/payload.rs
- file: crates/gcode/src/commands/vector.rs
- file: crates/gcode/src/graph/code_graph/lifecycle.rs
- file: crates/gcode/src/graph/code_graph/payload.rs
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
- file: crates/gcode/src/graph/code_graph/read/support.rs
- file: crates/gcode/src/graph/code_graph/tests.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
- file: crates/gcode/src/graph/report/generation.rs
- file: crates/gcode/src/graph/report/loading.rs
- file: crates/gcode/src/graph/report/queries.rs
- file: crates/gcode/src/graph/report/render.rs
- file: crates/gcode/src/graph/report/rows.rs
- file: crates/gcode/src/graph/report/summary.rs
- file: crates/gcode/src/graph/report/tests.rs
- file: crates/gcode/src/graph/report/types.rs
- file: crates/gcode/src/graph/typed_query.rs
- file: crates/gcode/src/projection/sync.rs
- file: crates/gcode/src/vector/code_symbols/embedding.rs
- file: crates/gcode/src/vector/code_symbols/lifecycle.rs
- file: crates/gcode/src/vector/code_symbols/qdrant.rs
- file: crates/gcode/src/vector/code_symbols/repository.rs
- file: crates/gcode/src/vector/code_symbols/tests.rs
- file: crates/gcode/src/vector/code_symbols/types.rs
provenance_truncated: 12
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 2
  reason: PostgreSQL row model and dual-store projection are not shown in the excerpts.
- id: 3
  reason: Cites write.rs/mutation.rs and metadata behavior not shown in the excerpts.
- id: 4
  reason: projection/mod.rs lifecycle and cleanup behavior are not shown in the excerpts.
- id: 6
  reason: Module export lists are not shown in the excerpts.
- id: 7
  reason: CodeGraph::sync_file flow is not shown in the excerpts.
- id: 8
  reason: Relationship metadata fields written by the mutation layer are not shown in the excerpts.
- id: 9
  reason: Projection cleanup and per-target failure handling are not shown in the excerpts.
- id: 16
  reason: Related graph view support is not shown in the payload excerpt.
- id: 18
  reason: ProjectGraphReport and VectorLifecycleJsonPayload roles are not shown in the excerpts.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/graph/lifecycle.rs](crates/gcode/src/commands/graph/lifecycle.rs)
- [crates/gcode/src/commands/graph/payload.rs](crates/gcode/src/commands/graph/payload.rs)
- [crates/gcode/src/commands/vector.rs](crates/gcode/src/commands/vector.rs)
- [crates/gcode/src/graph/code_graph/lifecycle.rs](crates/gcode/src/graph/code_graph/lifecycle.rs)
- [crates/gcode/src/graph/code_graph/payload.rs](crates/gcode/src/graph/code_graph/payload.rs)
- [crates/gcode/src/graph/code_graph/read/graph_payloads.rs](crates/gcode/src/graph/code_graph/read/graph_payloads.rs)
- [crates/gcode/src/graph/code_graph/read/payload_queries.rs](crates/gcode/src/graph/code_graph/read/payload_queries.rs)
- [crates/gcode/src/graph/code_graph/read/relationship_queries.rs](crates/gcode/src/graph/code_graph/read/relationship_queries.rs)
- [crates/gcode/src/graph/code_graph/read/relationships.rs](crates/gcode/src/graph/code_graph/read/relationships.rs)
- [crates/gcode/src/graph/code_graph/read/support.rs](crates/gcode/src/graph/code_graph/read/support.rs)
- [crates/gcode/src/graph/code_graph/tests.rs](crates/gcode/src/graph/code_graph/tests.rs)
- [crates/gcode/src/graph/code_graph/write.rs](crates/gcode/src/graph/code_graph/write.rs)

_30 more source files omitted._

</details>

# Projecting Graph and Vectors

## Why this matters

Once code facts have been extracted into PostgreSQL, they are useful but still flat: files, symbols, imports, calls, and metadata live as indexed rows. This part of the system projects those rows into two specialized stores so later commands can answer richer questions.

The graph projection turns indexed facts into FalkorDB `Code*` nodes and relationships owned by `gcode`, rather than treating the graph as the source of truth. The write path records provenance, confidence, source system, source file, and sync-token metadata on relationships such as `IMPORTS`, `DEFINES`, and `CALLS`, which makes graph state traceable back to the indexed source rows (`crates/gcode/src/graph/code_graph/write.rs:1-4`, `crates/gcode/src/graph/code_graph/write/mutation.rs:1-100`). The vector projection does the complementary job for semantic lookup: it turns `Symbol` records into embedding text and Qdrant payloads that preserve enough identity and source metadata to round-trip search hits back to code (`crates/gcode/src/vector/code_symbols.rs:1-29`, `crates/gcode/src/vector/code_symbols/embedding.rs:21-23`).

The design decision is to keep PostgreSQL as the factual base, then project into graph and vector backends with explicit lifecycle and cleanup behavior. That keeps the accelerated stores rebuildable, reportable, and safe to reconcile when files disappear or services are unavailable (`crates/gcode/src/projection/mod.rs:8-11`).

## How it works

1. The public namespaces keep the projection surfaces narrow. `crates/gcode/src/graph` exposes `code_graph`, `report`, and `typed_query` as the graph-facing modules, while `crates/gcode/src/vector` exposes only `code_symbols` for vector-backed symbol behavior (`crates/gcode/src/graph/mod.rs:1-3`, `crates/gcode/src/vector/mod.rs:1-2`).

2. Graph sync starts from indexed file facts. The central write flow is `CodeGraph::sync_file`: it creates a sync token, maps imports, definitions, and calls into graph items, partitions call relations, then delegates mutation and cleanup work (`crates/gcode/src/graph/code_graph/write.rs:18-31`, `crates/gcode/src/graph/code_graph/write.rs:43-100`).

3. Graph mutations encode relationships with operational metadata. The write layer imports typed query primitives and model types, then writes `IMPORTS`, `DEFINES`, and `CALLS` edges with provenance, confidence, source-system, source-file, and sync-token fields (`crates/gcode/src/graph/code_graph/write/mutation.rs:1-100`).

4. Sync state and deletion are explicit. The projection module owns synchronization and cleanup for graph and vector backends; deleted-file reconciliation deletes the graph projection when graph config exists and deletes stored vectors when Qdrant is configured, returning per-target failures instead of stopping at the first error (`crates/gcode/src/projection/mod.rs:1-36`).

5. Vector sync builds a lifecycle from configuration. `commands/vector.rs` resolves Qdrant and embedding configuration from `Context`; missing Qdrant or embedding configuration becomes `VectorLifecycleError::MissingQdrantConfig` or `VectorLifecycleError::MissingEmbeddingConfig` before any lifecycle is created (`crates/gcode/src/commands/vector.rs:16-22`, `crates/gcode/src/commands/vector.rs:29-37`).

6. Before syncing vectors for one file, the command checks PostgreSQL. If the indexed file is missing and `allow_missing_indexed_file` is set, it prints a skipped result; otherwise it fails with an error. If the file exists, it fetches symbols, calls `CodeSymbolVectorLifecycle::sync_file_symbols`, and then marks vectors synced in PostgreSQL (`crates/gcode/src/commands/vector.rs:39-100`).

7. Embeddings can come from two sources. `EmbeddingSource` supports daemon-routed embedding through `AiContext` or direct embedding through `EmbeddingConfig`; `EmbeddingBackend::new` validates that direct config has a non-empty `api_base` and builds a blocking HTTP client only for the direct path (`crates/gcode/src/vector/code_symbols/embedding.rs:26-29`, `crates/gcode/src/vector/code_symbols/embedding.rs:44-47`).

8. Qdrant collections are project-scoped. `CodeSymbolVectorLifecycle` stores project ID, collection name, Qdrant config, embedding backend, vector settings, optional probed vector size, and a blocking HTTP client (`crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37`). Collection naming uses the code-symbol prefix plus project ID and Qdrant’s custom collection scope (`crates/gcode/src/vector/code_symbols/qdrant.rs:21-37`).

9. Read-side graph queries tolerate missing graph service where appropriate. Relationship helpers such as `count_callers` and `count_usages` use `with_optional_core_graph`; when the optional graph is unavailable, the fallback returns `0`, otherwise the helper builds a typed query, runs `GraphClient::query`, and converts rows into counts (`crates/gcode/src/graph/code_graph/read/relationships.rs:35-67`).

10. Reports turn graph rows into user-facing structure. `generate_report_with_options` requires FalkorDB config, loads a report snapshot through `with_graph`, returns a full report when the service is available, and maps not-configured, unreachable, and query-failed cases into `ProjectGraphReportError` variants (`crates/gcode/src/graph/report/generation.rs:21-52`). The command layer can render the same report as JSON or Markdown (`crates/gcode/src/commands/graph/payload.rs:39-54`).

11. Graph payload commands expose focused views. The graph payload command can print overview, file, neighbor, report, and related graph views, formatting either structured JSON or compact text summaries of nodes and links (`crates/gcode/src/commands/graph/payload.rs:6-37`, `crates/gcode/src/commands/graph/payload.rs:56-97`).

## Key components

| Symbol | Role |
| --- | --- |
| `CodeGraph::sync_file` | Main graph projection flow for one indexed file: maps facts, assigns a sync token, writes graph mutations, and coordinates cleanup (`crates/gcode/src/graph/code_graph/write.rs:18-31`, `crates/gcode/src/graph/code_graph/write.rs:43-100`). |
| `CodeSymbolVectorLifecycle` | Runtime owner for project-scoped vector collection management, including Qdrant config, embedding backend, vector settings, probed dimension, and HTTP client (`crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37`). |
| `EmbeddingSource` | Selects daemon-routed embedding via `AiContext` or direct embedding via `EmbeddingConfig` (`crates/gcode/src/vector/code_symbols/embedding.rs:26-29`). |
| `EmbeddingBackend` | Wraps embedding source selection and validates/builds direct embedding clients (`crates/gcode/src/vector/code_symbols/embedding.rs:44-47`). |
| `VectorLifecycleJsonPayload` | Serializable command output for vector lifecycle events, including status, counts, degradation/error state, vector/delete counts, and summary (`crates/gcode/src/commands/vector.rs:202-220`). |
| `ResolvedExternalCallTarget` | Read-side graph model for an external call target with an ID and display name (`crates/gcode/src/graph/code_graph/read/relationships.rs:24-27`). |
| `ProjectGraphReport` | Structured graph report model rendered as both JSON and Markdown, carrying summaries, hotspots, unresolved/external targets, degradation, and suggested questions (`crates/gcode/src/graph/report/types.rs:42-61`). |
| `GraphSyncContractError` | Command contract error payload for graph sync-file cases such as project not indexed or indexed file not found (`crates/gcode/src/commands/graph/lifecycle.rs:12-14`). |

## What to read next

Read the graph report chapter next if you want to see how projected graph data becomes project-level summaries and Markdown output (`crates/gcode/src/graph/report/generation.rs:21-23`). For the vector side, read the code-symbol lifecycle and embedding references next, since they explain how symbol text becomes Qdrant vectors and how daemon versus direct embedding is selected (`crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37`, `crates/gcode/src/vector/code_symbols/embedding.rs:21-23`).

## Concepts

- [[code/concepts/graph-projection-and-reports|Graph Projection and Reports]]
- [[code/concepts/vector-symbol-search|Vector Symbol Search]]

## Explore

- [[code/modules/crates/gcode/src/projection|crates/gcode/src/projection]]
- [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]
- [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]
- [[code/modules/crates/gcode/src/graph/code_graph/write|crates/gcode/src/graph/code_graph/write]]
- [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]
- [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]
- [[code/modules/crates/gcode/src/vector|crates/gcode/src/vector]]
- [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Continue the tour

- ← Previous: [[code/narrative/resolving-relationships|Resolving Relationships]]

