---
title: crates/gwiki/src/search/semantic.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/semantic.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/semantic.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Overview

`crates/gwiki/src/search/semantic.rs` exposes 49 indexed API symbols.

## How it fits

`crates/gwiki/src/search/semantic.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SemanticSearchRequest` | class | 'SemanticSearchRequest' is a request struct for a semantic search operation that carries the search 'query', the target 'scope', and a result 'limit'. [crates/gwiki/src/search/semantic.rs:18-22] |
| `SemanticSearchOutcome` | class | 'SemanticSearchOutcome' is a result struct containing a vector of 'WikiSearchResult' hits and an optional 'DegradationKind' indicating any fallback or quality degradation applied during semantic search. [crates/gwiki/src/search/semantic.rs:25-28] |
| `SemanticSearchBackend` | type | Indexed type `SemanticSearchBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:30-35] |
| `QueryEmbedder` | type | Indexed type `QueryEmbedder` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:37-54] |
| `QueryEmbedder.embed_queries` | method | 'embed_queries' iterates over the input 'queries', embeds each one via 'self.embed_query(embedding, query)', and collects the results into a 'Result<Vec<Vec<f32>>, SearchError>', short-circuiting on the first error. [crates/gwiki/src/search/semantic.rs:44-53] |
| `SemanticEmbedding` | type | Indexed type `SemanticEmbedding` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:57-61] |
| `VectorSearchBackend` | type | Indexed type `VectorSearchBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:63-70] |
| `search_semantic` | function | Performs a scope-aware semantic search by short-circuiting empty requests, validating collection and backend configuration, embedding the query, and returning a 'SemanticSearchOutcome' while reporting degradation or service errors for unsupported scope, missing embeddings/Qdrant, or empty embedding vectors. [crates/gwiki/src/search/semantic.rs:72-163] |
| `semantic_embedding_query` | function | Returns the query string prefixed with 'config.query_prefix' only when that prefix exists and is non-empty after trimming whitespace, otherwise returns the original query unchanged. [crates/gwiki/src/search/semantic.rs:165-170] |
| `collection_for_scope` | function | Returns the 'gwiki' Qdrant collection name for a given 'SearchScope' by first converting it with 'qdrant_collection_scope' and then calling 'collection_name("gwiki", ...)', returning 'None' if either step fails. [crates/gwiki/src/search/semantic.rs:172-174] |
| `qdrant_collection_scope` | function | Converts a 'SearchScope' into an optional Qdrant 'CollectionScope', returning 'None' for 'Global' and 'Some(CollectionScope::Project(..))' or 'Some(CollectionScope::Topic(..))' for project and topic scopes, respectively. [crates/gwiki/src/search/semantic.rs:176-182] |
| `payload_filter` | function | Builds and returns a JSON filter requiring 'namespace == "gwiki"' and, for non-global scopes, additionally matching the current scope kind and its corresponding scope value under 'project_id' or 'topic'. [crates/gwiki/src/search/semantic.rs:184-204] |
| `GobbySemanticBackend` | class | 'GobbySemanticBackend<E, V>' is a generic backend wrapper that optionally holds semantic embedding and Qdrant configuration while delegating embedding generation to 'E' and vector storage/query operations to 'V'. [crates/gwiki/src/search/semantic.rs:206-211] |
| `new` | function | Constructs and returns a new instance by initializing the 'embedding', 'qdrant', 'embedder', and 'vector_backend' fields from the provided arguments. [crates/gwiki/src/search/semantic.rs:214-226] |
| `search_semantic` | function | Delegates a semantic search request to the underlying 'search_semantic' implementation using the current embedding, Qdrant client, embedder, and vector backend, returning either a 'SemanticSearchOutcome' or 'SearchError'. [crates/gwiki/src/search/semantic.rs:234-245] |
| `OpenAiEmbeddingBackend` | class | 'OpenAiEmbeddingBackend' is a thin wrapper struct around a 'gobby_core::ai::embeddings::Client' for providing OpenAI-backed embedding operations. [crates/gwiki/src/search/semantic.rs:250-252] |
| `OpenAiEmbeddingBackend::default` | method | Constructs a new 'Self' instance with 'client' initialized to 'gobby_core::ai::embeddings::Client::new()'. [crates/gwiki/src/search/semantic.rs:256-260] |
| `OpenAiEmbeddingBackend::new` | method | Constructs and returns a new instance by delegating to 'Self::default()'. [crates/gwiki/src/search/semantic.rs:265-267] |
| `OpenAiEmbeddingBackend::embed_query` | method | 'embed_query' computes a single query embedding by dispatching to 'embed_direct_queries' for 'SemanticEmbedding::Direct' and returning the first vector from the batch, or to 'embed_daemon_query' when the 'ai' feature enables 'SemanticEmbedding::Daemon', propagating any 'SearchError'. [crates/gwiki/src/search/semantic.rs:272-288] |
| `OpenAiEmbeddingBackend::embed_queries` | method | 'embed_queries' dispatches batch query embedding by either calling 'embed_direct_queries' for 'SemanticEmbedding::Direct' or, when the 'ai' feature is enabled, embedding each query individually via 'self.embed_query' for 'SemanticEmbedding::Daemon', returning a 'Result<Vec<Vec<f32>>, SearchError>'. [crates/gwiki/src/search/semantic.rs:290-305] |
| `embed_direct_queries` | function | Calls 'gobby_core::ai::embeddings::embed_batch' to embed a batch of query strings and converts any 'AiError' into a 'SearchError::Backend', including HTTP status and response body when available. [crates/gwiki/src/search/semantic.rs:309-323] |
| `OpenAiEmbeddingBackend` | class | 'OpenAiEmbeddingBackend' is a zero-sized backend type that serves as the OpenAI-specific implementation marker for embedding generation. [crates/gwiki/src/search/semantic.rs:327] |
| `OpenAiEmbeddingBackend::new` | method | Constructs and returns a new instance of 'Self' using the unit-like 'Self' value. [crates/gwiki/src/search/semantic.rs:331-333] |
| `OpenAiEmbeddingBackend::embed_query` | method | 'embed_query' returns a 'Vec<f32>' embedding for the given query by rejecting 'SemanticEmbedding::Direct' with a backend error and delegating 'SemanticEmbedding::Daemon' to 'embed_daemon_query', propagating any 'SearchError'. [crates/gwiki/src/search/semantic.rs:338-350] |

_19 more symbol(s) not shown — run `gcode outline crates/gwiki/src/search/semantic.rs` for the full list._

_Verified by 6 in-file unit tests._

