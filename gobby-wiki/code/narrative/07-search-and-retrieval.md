---
title: 'Searching the Index: Lexical, Semantic, and Graph-Boosted'
type: code_narrative
provenance:
- file: crates/gcode/src/search/fts.rs
- file: crates/gcode/src/search/fts/common.rs
- file: crates/gcode/src/search/fts/content.rs
- file: crates/gcode/src/search/fts/counts.rs
- file: crates/gcode/src/search/fts/graph.rs
- file: crates/gcode/src/search/fts/symbols.rs
- file: crates/gcode/src/search/fts/tests.rs
- file: crates/gcode/src/search/graph_boost.rs
- file: crates/gcode/src/search/mod.rs
- file: crates/gcode/src/search/rrf.rs
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
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/fts.rs](crates/gcode/src/search/fts.rs)
- [crates/gcode/src/search/fts/common.rs](crates/gcode/src/search/fts/common.rs)
- [crates/gcode/src/search/fts/content.rs](crates/gcode/src/search/fts/content.rs)
- [crates/gcode/src/search/fts/counts.rs](crates/gcode/src/search/fts/counts.rs)
- [crates/gcode/src/search/fts/graph.rs](crates/gcode/src/search/fts/graph.rs)
- [crates/gcode/src/search/fts/symbols.rs](crates/gcode/src/search/fts/symbols.rs)
- [crates/gcode/src/search/fts/tests.rs](crates/gcode/src/search/fts/tests.rs)
- [crates/gcode/src/search/graph_boost.rs](crates/gcode/src/search/graph_boost.rs)
- [crates/gcode/src/search/mod.rs](crates/gcode/src/search/mod.rs)
- [crates/gcode/src/search/rrf.rs](crates/gcode/src/search/rrf.rs)
- [crates/gcode/src/vector/code_symbols.rs](crates/gcode/src/vector/code_symbols.rs)
- [crates/gcode/src/vector/code_symbols/embedding.rs](crates/gcode/src/vector/code_symbols/embedding.rs)

_7 more source files omitted._

</details>

# Searching the Index: Lexical, Semantic, and Graph-Boosted

# Searching the Index: Lexical, Semantic, and Graph-Boosted

## Why this matters

No single search strategy is good at everything. A developer who types an exact identifier like `parse_config` wants a literal, lexical match — the kind that classic full-text search excels at. A developer who asks "where do we validate the user's email?" is describing *meaning*, not spelling, and needs semantic similarity. And a developer chasing how one symbol relates to another wants results ranked by how the code actually connects.

This part of the codebase answers all three needs at once. It runs a **BM25 full-text** lexical search, a **vector nearest-neighbour** semantic search, and a **graph boost** that re-weights results by structural relationships, then fuses the separate ranked lists into one with **Reciprocal Rank Fusion (RRF)**. The design decision behind it is *graceful degradation*: each backend is optional, so when an embedding model or a graph store is absent, the system still returns useful results from whatever strategies remain rather than failing outright.

The two halves of this machinery live in clearly separated modules. The lexical side sits under the search/FTS module [crates/gcode/src/search/fts.rs:1-32], with shared helpers factored into a common submodule [crates/gcode/src/search/fts/common.rs:16]. The semantic side sits under the vector module, specialised for code symbols [crates/gcode/src/vector/code_symbols.rs:1-29], including the embedding step that turns text into vectors [crates/gcode/src/vector/code_symbols/embedding.rs:21-23].

## How it works

Think of it like asking three specialists the same question and then merging their shortlists: the literal speller, the meaning-matcher, and the relationship-tracer each return a ranked list, and RRF decides the final order.

1. **Lexical pass (BM25).** The full-text search module scores documents by classic BM25 term-frequency relevance, producing a ranked list keyed off the indexed text [crates/gcode/src/search/fts.rs:1-32]. Shared utilities for this path are kept in the FTS common submodule so the scoring and supporting logic stay reusable [crates/gcode/src/search/fts/common.rs:16].

2. **Semantic pass (vector nearest-neighbour).** In parallel, the query is embedded into a vector for code symbols [crates/gcode/src/vector/code_symbols/embedding.rs:21-23], and the vector module finds the nearest neighbours among indexed symbol embeddings [crates/gcode/src/vector/code_symbols.rs:1-29]. This pass returns its own ranked list ordered by similarity rather than literal term overlap.

3. **Graph boosting.** The candidate results are then re-weighted using structural relationships between symbols, so items that are well-connected to the query context rise in rank.

4. **Reciprocal Rank Fusion.** The independent ranked lists are merged with RRF, which combines results by their *rank position* in each list rather than by raw, incomparable scores — letting BM25 relevance, vector similarity, and graph weight contribute to one unified ordering.

5. **Graceful degradation.** Because the lexical and semantic backends are separate modules, the absence of one does not abort the search. If embeddings or a graph backend are unavailable, fusion proceeds over the remaining available lists, so the lexical full-text path alone can still serve results.

> Note: the supplied input exposes the module layout but not the internal symbols, so the precise function names for fusion and boosting are not shown here; the flow above reflects the documented three-strategy, RRF-fused model.

## Key components

| Component | Role | Anchor |
| --- | --- | --- |
| `search/fts` | BM25 lexical full-text search | [crates/gcode/src/search/fts.rs:1-32] |
| `search/fts/common` | Shared FTS helpers/scoring utilities | [crates/gcode/src/search/fts/common.rs:16] |
| `vector/code_symbols` | Vector nearest-neighbour over code symbols | [crates/gcode/src/vector/code_symbols.rs:1-29] |
| `vector/code_symbols/embedding` | Embeds query/symbol text into vectors | [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] |

## What to read next

Continue with the chapter on **building the index** — how source text and code symbols are tokenised, embedded [crates/gcode/src/vector/code_symbols/embedding.rs:21-23], and stored before any of these searches can run — since the quality of the lexical and vector indexes determines what the fusion step has to work with. From there, the graph-construction chapter explains where the relationships used in the graph-boost step come from.

## Concepts

- [[code/concepts/crates-gcode-src-vector|Vector Search & Embeddings]]

## Explore

- [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]
- [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]
- [[code/modules/crates/gcode/src/vector|crates/gcode/src/vector]]

## Continue the tour

- ← Previous: [[code/narrative/06-graph-and-vector-stores|Projecting Facts into the Graph and Vector Stores]]

