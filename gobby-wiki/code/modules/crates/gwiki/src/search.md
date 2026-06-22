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

## crates/gwiki/src/search

The search module is the retrieval core of gwiki, orchestrating three complementary ranking signals — BM25 keyword scoring, semantic vector search, and graph-link boosting — before merging them through Reciprocal Rank Fusion (RRF). The root `mod.rs` file declares the shared vocabulary of the subsystem: `SearchScope`, `SearchSource`, `SearchHitKind`, `WikiSearchResult`, `SearchRequest`, `WikiSearchResponse`, and `SearchError`, plus the top-level `search` function that drives the full pipeline. Each sub-file owns one stage of the pipeline behind a trait boundary, keeping backends swappable for both production and testing.

BM25 search (`bm25.rs`) generates parameterised PostgreSQL full-text SQL via `build_bm25_sql`, delegating execution to anything that implements `Bm25SearchBackend`. It oversamples candidates by 4× from the backend and then post-filters to keyword-searchable paths and confirmed `Bm25` sources before truncating to the requested limit. Semantic search (`semantic.rs`) encodes the query through a `QueryEmbedder` — either `OpenAiEmbeddingBackend` calling the OpenAI API directly (feature `ai` disabled) or via the Gobby AI daemon — and dispatches a nearest-neighbour search to a `VectorSearchBackend`, concretely `GobbyQdrantBackend`, scoped to the correct Qdrant collection through `collection_for_scope` and `payload_filter`. Graph boost (`graph_boost.rs`) receives seed page paths from the BM25 or semantic results, expands them through `MemoryWikiGraph` or the Falkor graph client, and surfaces linked documents as additional hits labelled `SearchSource::Graph`. All three result lists are combined by `fuse_sources` in `rrf.rs`, which computes RRF scores, resolves canonical page keys via `WikiSearchResult::fusion_key`, and merges per-hit source/explanation metadata with `merge_hit_metadata`.

The module integrates heavily with `gobby_core`. `semantic.rs` consumes `gobby_core::config::{EmbeddingConfig, QdrantConfig}`, `gobby_core::qdrant::{CollectionScope, SearchHit, SearchRequest, collection_name}`, and `gobby_core::degradation::DegradationKind` (semantic.rs:1-9). `graph_boost.rs` imports `gobby_core::config::FalkorConfig` and `gobby_core::falkor::GraphClient`, as well as `crate::graph::MemoryWikiGraph` (graph_boost.rs:1-6). `bm25.rs` draws SQL helpers from `gobby_core::search::{bm25_score_expr, sanitize_pg_search_query}` (bm25.rs:5). Degradation is a first-class concern throughout: each backend returns an `Option<DegradationKind>` alongside its hits, unavailable services are represented by `UnavailableSemanticBackend`, `UnavailableGraphBoostBackend`, and `NoopGraphBoostBackend`, and the `available_sources` / `search_source_unavailable` helpers at the module level collect and surface degradation information to callers.

### SearchScope

| Variant | Constructor | scope_kind() | scope_filter() |
|---|---|---|---|
| Global | `SearchScope::global()` | `"global"` | `None` |
| Project | `SearchScope::project(id)` | `"project"` | `Some(("project", id))` |
| Topic | `SearchScope::topic(t)` | `"topic"` | `Some(("topic", t))` |

### SearchSource

| Variant | as_str() | Backend trait | Concrete production impl |
|---|---|---|---|
| Bm25 | `"bm25"` | `Bm25SearchBackend` | PostgreSQL via `build_bm25_sql` |
| Graph | `"graph"` | `GraphBoostBackend` | `MemoryWikiGraph` / Falkor `GraphClient` |
| Semantic | `"semantic"` | `SemanticSearchBackend` | `GobbySemanticBackend` + `GobbyQdrantBackend` |

### Public API symbols (mod.rs)

| Symbol | Kind | Role |
|---|---|---|
| `search` | fn | Top-level entry point; runs all three stages and fuses results |
| `fuse_sources` | fn (rrf.rs) | RRF merge of multi-source result lists |
| `graph_seed_paths` | fn | Extracts seed paths for graph expansion from prior hits |
| `available_sources` | fn | Returns the set of `SearchSource` values active for a request |
| `normalized_path` | fn | Canonicalises a file path for fusion-key comparison |
| `WikiSearchResult` | struct | Unified hit type carrying path, score, sources, and provenance |
| `SearchRequest` | struct | Input to `search`: query string, scope, per-source limits |
| `WikiSearchResponse` | struct | Output of `search`: ranked hits plus per-source degradation notices |
| `SearchError` | enum | Unified error type across all backends |
[crates/gwiki/src/search/graph_boost.rs:21-24]
[crates/gwiki/src/search/bm25.rs:13-17]
[crates/gwiki/src/search/mod.rs:14-18]
[crates/gwiki/src/search/rrf.rs:8-92]
[crates/gwiki/src/search/semantic.rs:18-22]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/search/bm25.rs\|crates/gwiki/src/search/bm25.rs]] | `crates/gwiki/src/search/bm25.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/graph_boost.rs\|crates/gwiki/src/search/graph_boost.rs]] | `crates/gwiki/src/search/graph_boost.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/mod.rs\|crates/gwiki/src/search/mod.rs]] | `crates/gwiki/src/search/mod.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/rrf.rs\|crates/gwiki/src/search/rrf.rs]] | `crates/gwiki/src/search/rrf.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/search/semantic.rs\|crates/gwiki/src/search/semantic.rs]] | `crates/gwiki/src/search/semantic.rs` exposes 49 indexed API symbols. |

