---
title: Code Graph Engine
type: code_concept
provenance:
- file: crates/gcode/src/graph/code_graph.rs
- file: crates/gcode/src/graph/code_graph/connection.rs
- file: crates/gcode/src/graph/code_graph/lifecycle.rs
- file: crates/gcode/src/graph/code_graph/payload.rs
- file: crates/gcode/src/graph/code_graph/read.rs
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
- file: crates/gcode/src/graph/code_graph/read/support.rs
- file: crates/gcode/src/graph/code_graph/tests.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
- file: crates/gcode/src/graph/code_graph/write/support.rs
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
- file: crates/gcode/src/graph/mod.rs
- file: crates/gcode/src/graph/report.rs
- file: crates/gcode/src/graph/report/generation.rs
- file: crates/gcode/src/graph/report/loading.rs
- file: crates/gcode/src/graph/report/queries.rs
- file: crates/gcode/src/graph/report/render.rs
- file: crates/gcode/src/graph/report/rows.rs
- file: crates/gcode/src/graph/report/summary.rs
- file: crates/gcode/src/graph/report/tests.rs
- file: crates/gcode/src/graph/report/time.rs
- file: crates/gcode/src/graph/report/types.rs
- file: crates/gcode/src/graph/typed_query.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph.rs](crates/gcode/src/graph/code_graph.rs)
- [crates/gcode/src/graph/code_graph/connection.rs](crates/gcode/src/graph/code_graph/connection.rs)
- [crates/gcode/src/graph/code_graph/lifecycle.rs](crates/gcode/src/graph/code_graph/lifecycle.rs)
- [crates/gcode/src/graph/code_graph/payload.rs](crates/gcode/src/graph/code_graph/payload.rs)
- [crates/gcode/src/graph/code_graph/read.rs](crates/gcode/src/graph/code_graph/read.rs)
- [crates/gcode/src/graph/code_graph/read/graph_payloads.rs](crates/gcode/src/graph/code_graph/read/graph_payloads.rs)
- [crates/gcode/src/graph/code_graph/read/payload_queries.rs](crates/gcode/src/graph/code_graph/read/payload_queries.rs)
- [crates/gcode/src/graph/code_graph/read/relationship_queries.rs](crates/gcode/src/graph/code_graph/read/relationship_queries.rs)
- [crates/gcode/src/graph/code_graph/read/relationships.rs](crates/gcode/src/graph/code_graph/read/relationships.rs)
- [crates/gcode/src/graph/code_graph/read/support.rs](crates/gcode/src/graph/code_graph/read/support.rs)
- [crates/gcode/src/graph/code_graph/tests.rs](crates/gcode/src/graph/code_graph/tests.rs)
- [crates/gcode/src/graph/code_graph/write.rs](crates/gcode/src/graph/code_graph/write.rs)

_16 more source files omitted._

</details>

# Code Graph Engine

## Purpose

The Code Graph Engine is the layer responsible for building, reading, writing, and managing a code-knowledge graph backed by FalkorDB. It turns structured information about a codebase into a persistent graph of typed nodes and relationships, and provides the inverse capability—pulling that information back out via traversal reads. The problem it solves is the impedance mismatch between in-memory Rust representations of code facts and the Cypher/graph storage model: it centralizes typed Cypher serialization, batched mutations, scoped deletions, and read payloads so the rest of the system can treat the graph as a typed store rather than hand-writing query strings everywhere. The root of this concept lives in `crates/gcode/src/graph/code_graph.rs:1-51`.

## Covers / Does not cover

Covers:
- Establishing and holding the FalkorDB connection used by graph operations (`crates/gcode/src/graph/code_graph/connection.rs:7-12`).
- Typed Cypher serialization and batched mutations against the graph.
- Scoped deletions—removing a bounded subset of the graph rather than wiping it wholesale (`crates/gcode/src/graph/code_graph/write/deletion.rs:8-66`).
- Traversal reads that produce graph payloads for consumers (`crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98`).

Does not cover:
- The analysis that produces the facts fed into the graph (upstream extraction is out of scope here; this concept consumes already-structured input).
- The FalkorDB server itself or its operational lifecycle; only the client-side connection is owned here (`crates/gcode/src/graph/code_graph/connection.rs:7-12`).
- Any symbol-level API contract not present in the supplied evidence (no indexed symbols or source excerpts were provided).

## Architecture

The engine is organized as a single `code_graph` module under `crates/gcode/src/graph`, with a thin root that ties the pieces together (`crates/gcode/src/graph/code_graph.rs:1-51`) and a clean split into three concerns: connection, write, and read. This arrangement exists because graph access has three naturally separable lifecycles—you first need a live handle to the database, then you mutate state, and separately you query it—and keeping them in distinct submodules prevents read logic from leaking into write paths and vice versa.

The `connection` submodule is the foundation: it owns the FalkorDB handle that both reads and writes depend on (`crates/gcode/src/graph/code_graph/connection.rs:7-12`). Because every other operation requires this handle, it sits "below" both the read and write sides architecturally.

The `write` submodule concentrates mutations, including the scoped-deletion logic in `deletion.rs` (`crates/gcode/src/graph/code_graph/write/deletion.rs:8-66`). Grouping batched mutations and deletions together keeps the typed-Cypher serialization and the safety boundaries of "what gets removed" in one place.

The `read` submodule is symmetric to write and is responsible for traversal reads, materializing results into graph payloads (`crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98`). Isolating payload shaping here means consumers receive structured results rather than raw query rows.

## Data flow

1. A caller initiates a graph operation through the `code_graph` module entry point (`crates/gcode/src/graph/code_graph.rs:1-51`).
2. The engine resolves the FalkorDB connection from the `connection` submodule, which provides the live handle that all subsequent steps require (`crates/gcode/src/graph/code_graph/connection.rs:7-12`). If this connection cannot be established or is unavailable, the dependent read and write steps below cannot proceed, since they are built on top of this handle.
3. For a write, the request is serialized into typed Cypher and applied as a batched mutation; when the operation is a removal, the scoped-deletion path bounds the affected subset rather than clearing the whole graph (`crates/gcode/src/graph/code_graph/write/deletion.rs:8-66`).
4. For a read, the engine issues a traversal query and assembles the results into a graph payload returned to the caller (`crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98`).

## Key components

The components below are the small set of modules that define this concept; no individual symbols were supplied in the evidence, so the table is scoped to the module boundaries.

| Component | Role | Anchor |
| --- | --- | --- |
| `code_graph` (root) | Entry point that ties connection, read, and write together | crates/gcode/src/graph/code_graph.rs:1-51 |
| `connection` | Owns the FalkorDB handle all operations depend on | crates/gcode/src/graph/code_graph/connection.rs:7-12 |
| `write/deletion` | Batched mutations and scoped deletions | crates/gcode/src/graph/code_graph/write/deletion.rs:8-66 |
| `read/graph_payloads` | Traversal reads materialized into payloads | crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98 |

## Where to start

Begin with the module root, `crates/gcode/src/graph/code_graph.rs:1-51`, to see how the connection, read, and write submodules are wired together. From there, read `connection.rs` (`crates/gcode/src/graph/code_graph/connection.rs:7-12`) to understand the FalkorDB handle that everything else depends on, then branch into `write/deletion.rs` (`crates/gcode/src/graph/code_graph/write/deletion.rs:8-66`) or `read/graph_payloads.rs` (`crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98`) depending on whether you are mutating or querying the graph.

## Explore

- [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]
- [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]
- [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]
- [[code/modules/crates/gcode/src/graph/code_graph/write|crates/gcode/src/graph/code_graph/write]]

