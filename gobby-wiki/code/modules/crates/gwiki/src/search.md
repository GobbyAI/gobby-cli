---
title: crates/gwiki/src/search
type: code_module
provenance:
- file: crates/gwiki/src/search/bm25.rs
- file: crates/gwiki/src/search/graph_boost.rs
- file: crates/gwiki/src/search/mod.rs
- file: crates/gwiki/src/search/rrf.rs
- file: crates/gwiki/src/search/semantic.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

The `crates/gwiki/src/search` module is the shared search layer for wiki content. It exposes lexical BM25, graph-boost, reciprocal-rank fusion, and semantic search submodules from one namespace (`mod.rs:1-4`), while centralizing common concepts such as `SearchScope`, `SearchSource`, hit kinds, provenance, results, requests, responses, and errors (`mod.rs:11-100`). Scopes support global, project, and topic filtering, with helper methods that produce a kind/value pair or an optional filter tuple for downstream backends (`mod.rs:11-51`).

Search execution is split across specialized backends. BM25 accepts a query, scope, and limit, delegates to a `Bm25SearchBackend`, over-fetches candidates, filters to keyword-searchable wiki paths, requires BM25 attribution, and truncates to the requested limit (`bm25.rs:12-58`). Semantic search similarly accepts a query/scope/limit request and returns hits plus optional degradation; it depends on embedding configuration, Qdrant configuration, query embedding, and vector search traits (`semantic.rs:3-67`). Graph boosting accepts scoped seed paths and a limit, uses Falkor/graph configuration and wiki graph imports, and can degrade cleanly through unavailable/no-op backends (`graph_boost.rs:1-70`).

Collaboration points are explicit: this module imports degradation reporting from `gobby_core`, graph access through Falkor and `MemoryWikiGraph`, vector search structures and collection naming from Qdrant, and embedding/AI configuration from core config and optional AI daemon context (`semantic.rs:3-10`, `graph_boost.rs:4-14`). Internally, search backends share common result and provenance types from `crate::search`, while graph boost also reuses BM25 path searchability filtering (`graph_boost.rs:9-14`, `bm25.rs:6-9`). The top-level source model normalizes result attribution across BM25, graph, and semantic systems via stable string names (`mod.rs:53-76`).

| Public API area | Symbols |
| --- | --- |
| Scope | `SearchScope`, `SearchScope::global`, `SearchScope::project`, `SearchScope::topic`, `scope_kind`, `scope_value`, `scope_filter` |
| Source attribution | `SearchSource`, `SearchSource::as_str`, `SearchSource::from_source_name` |
| Results/provenance | `SearchHitKind`, `ChunkProvenance`, `SearchProvenance`, `SearchSourceExplanation`, `WikiSearchResult`, `WikiSearchResult::fusion_key` |
| Orchestration | `SearchRequest`, `WikiSearchResponse`, `SearchError`, `search`, `available_sources` |
| Fusion | `fuse_sources`, `ranked_keys`, `merge_hit_metadata` |
| Semantic | `SemanticSearchRequest`, `SemanticSearchOutcome`, `SemanticSearchBackend`, `QueryEmbedder`, `VectorSearchBackend`, `search_semantic` |
| Graph | `GraphBoostConfig`, `GraphBoostRequest`, `GraphBoostOutcome`, `GraphBoostBackend` |

| Enumerable value | Values | Support |
| --- | --- | --- |
| `SearchScope` | `Global`, `Project { project_id }`, `Topic { topic }` | `mod.rs:11-51` |
| `SearchSource` | `Bm25`, `Graph`, `Semantic` | `mod.rs:53-76` |
| `SearchHitKind` | `Document`, `Chunk` | `mod.rs:78-81` |
| Graph defaults | document query limit `10_000`, link query limit `50_000` | `graph_boost.rs:15-31` |
[crates/gwiki/src/search/graph_boost.rs:21-24]
[crates/gwiki/src/search/bm25.rs:13-17]
[crates/gwiki/src/search/mod.rs:14-18]
[crates/gwiki/src/search/semantic.rs:18-22]
[crates/gwiki/src/search/rrf.rs:8-92]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/search/bm25.rs\|crates/gwiki/src/search/bm25.rs]] | `crates/gwiki/src/search/bm25.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/graph_boost.rs\|crates/gwiki/src/search/graph_boost.rs]] | `crates/gwiki/src/search/graph_boost.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/mod.rs\|crates/gwiki/src/search/mod.rs]] | `crates/gwiki/src/search/mod.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/rrf.rs\|crates/gwiki/src/search/rrf.rs]] | `crates/gwiki/src/search/rrf.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/semantic.rs\|crates/gwiki/src/search/semantic.rs]] | `crates/gwiki/src/search/semantic.rs` exposes 49 indexed API symbols. |

