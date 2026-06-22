---
title: Projecting Facts into the Graph and Vector Stores
type: code_narrative
provenance:
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
- file: crates/gcode/src/graph/code_graph/write/support.rs
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
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
- file: crates/gcode/src/vector/code_symbols/search.rs
- file: crates/gcode/src/vector/code_symbols/tests.rs
- file: crates/gcode/src/vector/code_symbols/types.rs
provenance_truncated: 9
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/lifecycle.rs](crates/gcode/src/graph/code_graph/lifecycle.rs)
- [crates/gcode/src/graph/code_graph/payload.rs](crates/gcode/src/graph/code_graph/payload.rs)
- [crates/gcode/src/graph/code_graph/read/graph_payloads.rs](crates/gcode/src/graph/code_graph/read/graph_payloads.rs)
- [crates/gcode/src/graph/code_graph/read/payload_queries.rs](crates/gcode/src/graph/code_graph/read/payload_queries.rs)
- [crates/gcode/src/graph/code_graph/read/relationship_queries.rs](crates/gcode/src/graph/code_graph/read/relationship_queries.rs)
- [crates/gcode/src/graph/code_graph/read/relationships.rs](crates/gcode/src/graph/code_graph/read/relationships.rs)
- [crates/gcode/src/graph/code_graph/read/support.rs](crates/gcode/src/graph/code_graph/read/support.rs)
- [crates/gcode/src/graph/code_graph/tests.rs](crates/gcode/src/graph/code_graph/tests.rs)
- [crates/gcode/src/graph/code_graph/write.rs](crates/gcode/src/graph/code_graph/write.rs)
- [crates/gcode/src/graph/code_graph/write/deletion.rs](crates/gcode/src/graph/code_graph/write/deletion.rs)
- [crates/gcode/src/graph/code_graph/write/mutation.rs](crates/gcode/src/graph/code_graph/write/mutation.rs)
- [crates/gcode/src/graph/code_graph/write/support.rs](crates/gcode/src/graph/code_graph/write/support.rs)

_27 more source files omitted._

</details>

# Projecting Facts into the Graph and Vector Stores

## Why this matters

Indexing produces *facts* about your code — symbols, definitions, references, relationships — but raw facts sitting in memory or a flat store are hard to query in the ways developers actually want. You want to ask graph-shaped questions ("what calls this function?") and similarity-shaped questions ("show me code that resembles this snippet"). Those two questions need two very different storage engines: a graph database and a vector database.

This part of `gcode` solves that problem by *projecting* indexed facts into two specialized backends — FalkorDB for the code graph and Qdrant for vector embeddings — and keeping both in sync as the index changes. The design decision here is separation of concerns: the projection layer ([crates/gcode/src/projection/mod.rs:8-11]) acts as the bridge that takes indexed facts and writes them outward, while the graph ([crates/gcode/src/graph/code_graph.rs:1-51]) and vector ([crates/gcode/src/vector/code_symbols.rs:1-29]) modules each own the details of talking to their respective store. By splitting projection from storage, the system can re-run synchronization, handle deletions, and generate analytics reports without entangling the indexing logic with database-specific quirks.

Think of projection like publishing a document to two formats at once: the same underlying content is reshaped into a graph view and a vector view, each optimized for a different kind of lookup.

## How it works

The flow moves from indexed facts, through the projection bridge, and out into the two stores. Grounded in the supplied modules, the path looks like this:

1. **Projection kicks off.** The projection module ([crates/gcode/src/projection/mod.rs:8-11]) is the entry point that drives facts toward the backing stores after indexing. It coordinates which facts go to the graph and which go to the vector store.

2. **Open a graph connection.** Before any graph writes happen, the code graph establishes a connection to FalkorDB ([crates/gcode/src/graph/code_graph/connection.rs:7-12]). This connection is the channel through which all subsequent graph reads and writes flow.

3. **Write facts into the graph.** New and updated facts are written through the graph's write path ([crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]). Keeping the store in sync is not only additive — the write layer includes deletion handling, so facts that no longer exist after a re-index are removed rather than left to go stale.

4. **Read back graph payloads.** When the system needs to surface graph data — for queries or for assembling reports — it reads structured payloads out of the graph ([crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98]). This read path is the counterpart to the write path and is what downstream consumers depend on.

5. **Embed and project code symbols into vectors.** In parallel, code symbols are turned into embeddings ([crates/gcode/src/vector/code_symbols/embedding.rs:21-23]) and projected into the Qdrant vector store ([crates/gcode/src/vector/code_symbols.rs:1-29]). This is what makes similarity search over your codebase possible.

6. **Generate analytics reports.** Once facts live in the graph, the report module turns them into human-readable analytics ([crates/gcode/src/graph/report/generation.rs:21-23]), closing the loop from indexed facts to insight.

On the failure and fallback side, the most concrete evidence is the deletion handling in the write path ([crates/gcode/src/graph/code_graph/write/deletion.rs:8-66]): synchronization is designed to *remove* obsolete facts, which is how the graph stays correct across repeated indexing runs rather than accumulating drift.

## Key components

| Symbol / Module | Role | Anchor |
| --- | --- | --- |
| `projection` | Bridges indexed facts out to the graph and vector stores | [crates/gcode/src/projection/mod.rs:8-11] |
| graph connection | Opens the channel to FalkorDB | [crates/gcode/src/graph/code_graph/connection.rs:7-12] |
| graph write / deletion | Writes facts and removes stale ones to keep the graph in sync | [crates/gcode/src/graph/code_graph/write/deletion.rs:8-66] |
| graph read payloads | Reads structured graph data for queries and reports | [crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98] |
| code symbol embedding | Turns symbols into vectors for Qdrant | [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] |
| report generation | Produces analytics from projected graph facts | [crates/gcode/src/graph/report/generation.rs:21-23] |

## What to read next

Continue with the chapter on the indexing pipeline that produces the facts feeding this projection step, so you can see where the inputs to [crates/gcode/src/projection/mod.rs:8-11] come from. After that, the analytics chapter that builds on [crates/gcode/src/graph/report/generation.rs:21-23] will show how the projected graph is consumed downstream.

## Concepts

- [[code/concepts/crates-gcode-src-graph|Code Graph Engine]]
- [[code/concepts/crates-gcode-src-graph-report|Graph Analytics & Reporting]]
- [[code/concepts/crates-gcode-src-vector|Vector Search & Embeddings]]

## Explore

- [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]
- [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]
- [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]
- [[code/modules/crates/gcode/src/projection|crates/gcode/src/projection]]

## Continue the tour

- ← Previous: [[code/narrative/05-indexing-pipeline|Turning Source Files into Code Facts]]
- Next →: [[code/narrative/07-search-and-retrieval|Searching the Index: Lexical, Semantic, and Graph-Boosted]]

