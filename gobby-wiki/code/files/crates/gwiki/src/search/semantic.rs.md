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

`crates/gwiki/src/search/semantic.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SemanticSearchRequest` | class | Indexed class `SemanticSearchRequest` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:18-22] |
| `SemanticSearchOutcome` | class | Indexed class `SemanticSearchOutcome` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:25-28] |
| `SemanticSearchBackend` | type | Indexed type `SemanticSearchBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:30-35] |
| `QueryEmbedder` | type | Indexed type `QueryEmbedder` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:37-54] |
| `QueryEmbedder.embed_queries` | method | Indexed method `QueryEmbedder.embed_queries` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:44-53] |
| `SemanticEmbedding` | type | Indexed type `SemanticEmbedding` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:57-61] |
| `VectorSearchBackend` | type | Indexed type `VectorSearchBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:63-70] |
| `search_semantic` | function | Indexed function `search_semantic` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:72-163] |
| `semantic_embedding_query` | function | Indexed function `semantic_embedding_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:165-170] |
| `collection_for_scope` | function | Indexed function `collection_for_scope` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:172-174] |
| `qdrant_collection_scope` | function | Indexed function `qdrant_collection_scope` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:176-182] |
| `payload_filter` | function | Indexed function `payload_filter` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:184-204] |
| `GobbySemanticBackend` | class | Indexed class `GobbySemanticBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:206-211] |
| `new` | function | Indexed function `new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:214-226] |
| `search_semantic` | function | Indexed function `search_semantic` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:234-245] |
| `OpenAiEmbeddingBackend` | class | Indexed class `OpenAiEmbeddingBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:250-252] |
| `OpenAiEmbeddingBackend::default` | method | Indexed method `OpenAiEmbeddingBackend::default` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:256-260] |
| `OpenAiEmbeddingBackend::new` | method | Indexed method `OpenAiEmbeddingBackend::new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:265-267] |
| `OpenAiEmbeddingBackend::embed_query` | method | Indexed method `OpenAiEmbeddingBackend::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:272-288] |
| `OpenAiEmbeddingBackend::embed_queries` | method | Indexed method `OpenAiEmbeddingBackend::embed_queries` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:290-305] |
| `embed_direct_queries` | function | Indexed function `embed_direct_queries` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:309-323] |
| `OpenAiEmbeddingBackend` | class | Indexed class `OpenAiEmbeddingBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:327] |
| `OpenAiEmbeddingBackend::new` | method | Indexed method `OpenAiEmbeddingBackend::new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:331-333] |
| `OpenAiEmbeddingBackend::embed_query` | method | Indexed method `OpenAiEmbeddingBackend::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:338-350] |
| `OpenAiEmbeddingBackend::embed_query` | method | Indexed method `OpenAiEmbeddingBackend::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:355-364] |
| `embed_daemon_query` | function | Indexed function `embed_daemon_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:368-376] |
| `GobbyQdrantBackend` | class | Indexed class `GobbyQdrantBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:379] |
| `GobbyQdrantBackend::search` | method | Indexed method `GobbyQdrantBackend::search` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:382-389] |
| `required_service_error` | function | Indexed function `required_service_error` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:392-396] |
| `payload_matches_scope` | function | Indexed function `payload_matches_scope` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:398-411] |
| `hit_to_result` | function | Indexed function `hit_to_result` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:413-457] |
| `payload_string` | function | Indexed function `payload_string` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:459-461] |
| `payload_usize` | function | Indexed function `payload_usize` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:463-468] |
| `degraded` | function | Indexed function `degraded` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:470-478] |
| `qdrant_degradation` | function | Indexed function `qdrant_degradation` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:480-509] |
| `UnavailableSemanticBackend` | class | Indexed class `UnavailableSemanticBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:512] |
| `UnavailableSemanticBackend::search_semantic` | method | Indexed method `UnavailableSemanticBackend::search_semantic` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:516-524] |
| `FixedEmbedder` | class | Indexed class `FixedEmbedder` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:528-531] |
| `FixedEmbedder::new` | method | Indexed method `FixedEmbedder::new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:535-540] |
| `FixedEmbedder::embed_query` | method | Indexed method `FixedEmbedder::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:545-552] |
| `RecordingVectorBackend` | class | Indexed class `RecordingVectorBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:556-560] |
| `RecordingVectorBackend::new` | method | Indexed method `RecordingVectorBackend::new` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:564-570] |
| `RecordingVectorBackend::search` | method | Indexed method `RecordingVectorBackend::search` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:575-584] |
| `FailingEmbedder` | class | Indexed class `FailingEmbedder` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:588] |
| `FailingEmbedder::embed_query` | method | Indexed method `FailingEmbedder::embed_query` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:592-598] |
| `FailingVectorBackend` | class | Indexed class `FailingVectorBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:602] |
| `FailingVectorBackend::search` | method | Indexed method `FailingVectorBackend::search` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:606-613] |
| `QdrantStatusVectorBackend` | class | Indexed class `QdrantStatusVectorBackend` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:617-619] |
| `QdrantStatusVectorBackend::search` | method | Indexed method `QdrantStatusVectorBackend::search` in `crates/gwiki/src/search/semantic.rs`. [crates/gwiki/src/search/semantic.rs:623-637] |

