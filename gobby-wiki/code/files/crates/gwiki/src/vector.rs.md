---
title: crates/gwiki/src/vector.rs
type: code_file
provenance:
- file: crates/gwiki/src/vector.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/vector.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/vector.rs` exposes 47 indexed API symbols.

## How it fits

`crates/gwiki/src/vector.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WikiVectorChunk` | class | Indexed class `WikiVectorChunk` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:17-26] |
| `WikiVectorPoint` | class | Indexed class `WikiVectorPoint` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:29-33] |
| `WikiVectorSyncOutcome` | class | Indexed class `WikiVectorSyncOutcome` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:36-40] |
| `WikiVectorError` | type | Indexed type `WikiVectorError` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:43-48] |
| `WikiVectorError::fmt` | method | Indexed method `WikiVectorError::fmt` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:51-58] |
| `WikiVectorError::from` | method | Indexed method `WikiVectorError::from` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:64-66] |
| `WikiVectorChunkSource` | type | Indexed type `WikiVectorChunkSource` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:69-73] |
| `WikiVectorEmbedder` | type | Indexed type `WikiVectorEmbedder` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:75-77] |
| `WikiVectorStore` | type | Indexed type `WikiVectorStore` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:79-99] |
| `WikiVectorStore.resolve_collection` | method | Indexed method `WikiVectorStore.resolve_collection` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:80-84] |
| `sync_scope_vectors` | function | Indexed function `sync_scope_vectors` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:101-193] |
| `collection_for_scope` | function | Indexed function `collection_for_scope` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:195-197] |
| `delete_filter_for_path` | function | Indexed function `delete_filter_for_path` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:199-205] |
| `payload_for_chunk` | function | Indexed function `payload_for_chunk` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:207-245] |
| `point_id_for_chunk` | function | Indexed function `point_id_for_chunk` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:247-249] |
| `snippet` | function | Indexed function `snippet` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:251-253] |
| `PostgresWikiVectorChunkSource` | class | Indexed class `PostgresWikiVectorChunkSource` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:255-257] |
| `new` | function | Indexed function `new` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:260-262] |
| `chunks` | function | Indexed function `chunks` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:266-282] |
| `stale_paths` | function | Indexed function `stale_paths` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:284-298] |
| `row_to_vector_chunk` | function | Indexed function `row_to_vector_chunk` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:301-323] |
| `required_row_usize` | function | Indexed function `required_row_usize` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:325-330] |
| `parse_required_usize` | function | Indexed function `parse_required_usize` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:332-340] |
| `GwikiEmbeddingBackend` | class | Indexed class `GwikiEmbeddingBackend` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:342-345] |
| `GwikiEmbeddingBackend::new` | method | Indexed method `GwikiEmbeddingBackend::new` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:348-353] |
| `GwikiEmbeddingBackend::embed_texts` | method | Indexed method `GwikiEmbeddingBackend::embed_texts` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:357-370] |
| `GwikiQdrantVectorStore` | class | Indexed class `GwikiQdrantVectorStore` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:373-375] |
| `GwikiQdrantVectorStore::new` | method | Indexed method `GwikiQdrantVectorStore::new` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:378-380] |
| `GwikiQdrantVectorStore::ensure_collection` | method | Indexed method `GwikiQdrantVectorStore::ensure_collection` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:384-392] |
| `GwikiQdrantVectorStore::delete_points` | method | Indexed method `GwikiQdrantVectorStore::delete_points` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:394-397] |
| `GwikiQdrantVectorStore::upsert_points` | method | Indexed method `GwikiQdrantVectorStore::upsert_points` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:399-415] |
| `vector_collection_and_path_filter_match_scope_contract` | function | Indexed function `vector_collection_and_path_filter_match_scope_contract` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:425-452] |
| `vector_sync_embeds_upserts_and_deletes_stale_vectors` | function | Indexed function `vector_sync_embeds_upserts_and_deletes_stale_vectors` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:455-522] |
| `vector_sync_batches_embedding_and_upserts` | function | Indexed function `vector_sync_batches_embedding_and_upserts` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:525-566] |
| `direct_embedding_backend_batches_texts` | function | Indexed function `direct_embedding_backend_batches_texts` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:570-604] |
| `vector_required_offset_parser_rejects_missing_and_malformed_values` | function | Indexed function `vector_required_offset_parser_rejects_missing_and_malformed_values` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:607-617] |
| `MockChunkSource` | class | Indexed class `MockChunkSource` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:619-622] |
| `MockChunkSource::chunks` | method | Indexed method `MockChunkSource::chunks` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:625-630] |
| `MockChunkSource::stale_paths` | method | Indexed method `MockChunkSource::stale_paths` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:632-634] |
| `MockEmbedder` | class | Indexed class `MockEmbedder` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:637-640] |
| `MockEmbedder::embed_texts` | method | Indexed method `MockEmbedder::embed_texts` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:643-647] |
| `RecordingVectorStore` | class | Indexed class `RecordingVectorStore` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:651-655] |
| `RecordedUpsert` | class | Indexed class `RecordedUpsert` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:657-660] |
| `RecordingVectorStore::ensure_collection` | method | Indexed method `RecordingVectorStore::ensure_collection` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:663-671] |
| `RecordingVectorStore::delete_points` | method | Indexed method `RecordingVectorStore::delete_points` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:673-680] |
| `RecordingVectorStore::upsert_points` | method | Indexed method `RecordingVectorStore::upsert_points` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:682-692] |
| `filter_value` | function | Indexed function `filter_value` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:695-704] |

