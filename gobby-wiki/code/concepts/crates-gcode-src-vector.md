---
title: Vector Search & Embeddings
type: code_concept
provenance:
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

# Vector Search & Embeddings

## Purpose

Vector Search & Embeddings is the Qdrant-backed pipeline that turns code into searchable meaning. Rather than matching text literally, it converts code symbols into numeric embedding vectors, stores them in a Qdrant collection, and answers queries with scored semantic matches. This solves the problem of finding *relevant* code when you don't know the exact identifiers or wording — you can search by intent and get back the closest symbols by similarity score.

The concept lives in the `gcode` crate under a dedicated `vector` module [crates/gcode/src/vector/code_symbols.rs:1-29], with a focused submodule for embedding and indexing code symbols [crates/gcode/src/vector/code_symbols/embedding.rs:21-23].

## Covers / Does not cover

This page covers the vector pipeline as a whole: how text is embedded (via either a daemon route or a direct route), how the Qdrant collection is created and maintained over its lifecycle, and how scored semantic search runs over indexed code symbols.

It does not cover the internals of Qdrant itself, the parsing or extraction that produces code symbols before they reach the embedding step, or any consuming UI/CLI surfaces beyond what the `vector` module exposes. Because the supplied input includes no indexed key symbols and no source excerpts, exact function signatures, configuration keys, and flag names are out of scope for this page and should be read directly from the modules cited below.

## Architecture

The pipeline is organized as a parent `vector` module that owns the overall Qdrant integration and a `code_symbols` submodule that specializes in representing and indexing code symbols. The parent module [crates/gcode/src/vector/code_symbols.rs:1-29] is the entry boundary for vector concerns; the `code_symbols` submodule [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] narrows that to the embedding-and-indexing path for code.

This split exists so that two responsibilities stay separable: collection lifecycle and search (the general vector mechanics) versus turning a code symbol into an embedding (the domain-specific step). The embedding step is deliberately designed with two interchangeable routes — a **daemon** route and a **direct** route — so the same search behavior works whether or not a long-running embedding service is available. Placing both routes behind the embedding module keeps the rest of the pipeline (collection management, scored search) indifferent to *how* the vector was produced.

## Data flow

1. A code symbol is handed to the embedding module to be turned into a vector [crates/gcode/src/vector/code_symbols/embedding.rs:21-23].
2. The module attempts the **daemon** route first, sending the text to the embedding daemon to produce the vector.
3. If the daemon route is unavailable, the module falls back to the **direct** route, computing the embedding inline so indexing and search can still proceed.
4. The resulting vector is written into the Qdrant collection, which is created or reused as part of the collection lifecycle managed by the `vector` module [crates/gcode/src/vector/code_symbols.rs:1-29].
5. At query time, the query text is embedded through the same route logic and submitted to Qdrant.
6. Qdrant returns nearest neighbors with similarity scores, and the pipeline surfaces these as scored semantic matches over code symbols.

Note: the daemon-versus-direct fallback in steps 2–3 is asserted by the working summary's description of "embedding via daemon or direct routes"; verify the exact unavailability handling in the embedding source [crates/gcode/src/vector/code_symbols/embedding.rs:21-23].

## Key components

The table below lists only the two modules the input exposes; treat them as the starting points rather than an exhaustive symbol list.

| Component | Kind | Role | Evidence |
| --- | --- | --- | --- |
| `crates/gcode/src/vector` | module | Owns Qdrant integration: collection lifecycle and scored semantic search | [crates/gcode/src/vector/code_symbols.rs:1-29] |
| `crates/gcode/src/vector/code_symbols` | module | Embeds and indexes code symbols via the daemon or direct route | [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] |

## Where to start

Begin with the parent `vector` module [crates/gcode/src/vector/code_symbols.rs:1-29] to understand collection lifecycle and how search is wired, then read the `code_symbols` embedding module [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] to see how a symbol becomes a vector and how the daemon and direct routes are chosen. Since no individual symbols or source excerpts were supplied here, open these files directly to confirm names, signatures, and configuration before relying on them.

## Explore

- [[code/modules/crates/gcode/src/vector|crates/gcode/src/vector]]
- [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

