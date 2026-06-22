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

`crates/gwiki/src/vector.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WikiVectorChunk` | class | 'WikiVectorChunk' is a crate-visible data record representing a chunk of wiki text with its stable identifier, source path, optional title and heading metadata, chunk index, byte-range offsets, and chunk content. [crates/gwiki/src/vector.rs:17-26] |
| `WikiVectorPoint` | class | 'WikiVectorPoint' is a crate-visible data structure representing a vector database point with a string 'id', an embedding 'vector' of 'f32' values, and an arbitrary JSON-like 'payload' map. [crates/gwiki/src/vector.rs:29-33] |
| `WikiVectorSyncOutcome` | class | 'WikiVectorSyncOutcome' is a crate-visible summary of a wiki vector synchronization run, tracking the number of chunks processed, vectors upserted, and stale paths deleted. [crates/gwiki/src/vector.rs:36-40] |
| `WikiVectorError` | type | Indexed type `WikiVectorError` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:43-48] |
| `WikiVectorError::fmt` | method | Implements 'Display' formatting for the error enum by matching each variant and writing a variant-specific 'wiki vector ... error' message with the inner message interpolated. [crates/gwiki/src/vector.rs:51-58] |
| `WikiVectorError::from` | method | Converts a 'postgres::Error' into 'Self' by wrapping its string representation in 'Self::Store'. [crates/gwiki/src/vector.rs:64-66] |
| `WikiVectorChunkSource` | type | Indexed type `WikiVectorChunkSource` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:69-73] |
| `WikiVectorEmbedder` | type | Indexed type `WikiVectorEmbedder` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:75-77] |
| `WikiVectorStore` | type | Indexed type `WikiVectorStore` in `crates/gwiki/src/vector.rs`. [crates/gwiki/src/vector.rs:79-99] |
| `WikiVectorStore.resolve_collection` | method | Returns the vector-collection name for the given 'SearchScope' via 'collection_for_scope', or yields 'WikiVectorError::InvalidData("global scope has no vector collection")' if no collection exists. [crates/gwiki/src/vector.rs:80-84] |
| `sync_scope_vectors` | function | Synchronizes wiki vectors for a search scope by resolving the target collection, deleting stale-path points, embedding chunks in batches, and validating that each embedding batch returns a non-empty, consistent vector size before upserting points and reporting counts. [crates/gwiki/src/vector.rs:101-193] |
| `collection_for_scope` | function | Returns the 'Option<String>' collection name for a given 'SearchScope' by delegating directly to 'crate::search::semantic::collection_for_scope'. [crates/gwiki/src/vector.rs:195-197] |
| `delete_filter_for_path` | function | Builds the base semantic payload filter for 'scope' and, if its 'must' clause is an array, appends a 'path' equality match for 'path' before returning the modified JSON 'Value'. [crates/gwiki/src/vector.rs:199-205] |
| `payload_for_chunk` | function | Builds and returns a JSON-style payload map for a wiki vector chunk by inserting fixed metadata ('namespace', 'chunk_id', scope kind/id, path/source_path, optional title/heading, chunk offsets, content, and a derived snippet) plus a scope-specific 'project_id' or 'topic' when applicable. [crates/gwiki/src/vector.rs:207-245] |
| `point_id_for_chunk` | function | Generates a deterministic UUIDv5 string for a 'WikiVectorChunk' by hashing 'chunk.id' bytes with the 'WIKI_VECTOR_UUID_NAMESPACE' namespace. [crates/gwiki/src/vector.rs:247-249] |
| `snippet` | function | Returns the result of 'crate::support::text::snippet_from_text(content)', producing a snippet string derived from the input text. [crates/gwiki/src/vector.rs:251-253] |
| `PostgresWikiVectorChunkSource` | class | 'PostgresWikiVectorChunkSource<'a>' is a crate-private wrapper around a mutable 'postgres::Client' reference, representing a PostgreSQL-backed source for wiki vector chunks. [crates/gwiki/src/vector.rs:255-257] |
| `new` | function | Constructs a new instance by wrapping the provided mutable 'postgres::Client' reference in 'Self { conn }'. [crates/gwiki/src/vector.rs:260-262] |
| `chunks` | function | Fetches all 'gwiki_chunks' rows for the given 'SearchScope', joined with matching 'gwiki_documents' metadata and ordered by 'path' and 'chunk_index', then converts each row into a 'WikiVectorChunk' and returns the collected 'Result'. [crates/gwiki/src/vector.rs:266-282] |
| `stale_paths` | function | Returns the lexicographically ordered list of paths whose most recent ingestion record within the given search scope is marked 'deleted', by querying the latest status per path from 'gwiki_ingestions' and extracting the 'path' column. [crates/gwiki/src/vector.rs:284-298] |
| `row_to_vector_chunk` | function | Converts a 'postgres::Row' into a 'WikiVectorChunk' by extracting typed fields, joining a non-empty 'heading_path' with '" / "' into an optional 'heading', validating that 'chunk_index' is nonnegative and converting it to 'usize', and returning a 'WikiVectorError' on missing/invalid data. [crates/gwiki/src/vector.rs:301-323] |
| `required_row_usize` | function | Fetches an optional string value from the given PostgreSQL row column, converts lookup failures into 'WikiVectorError::InvalidData', and then parses the value into a required 'usize' via 'parse_required_usize'. [crates/gwiki/src/vector.rs:325-330] |
| `parse_required_usize` | function | Returns a 'usize' parsed from an 'Option<String>', emitting 'WikiVectorError::InvalidData' if the value is missing or cannot be parsed, with the column name embedded in the error message. [crates/gwiki/src/vector.rs:332-340] |
| `GwikiEmbeddingBackend` | class | 'GwikiEmbeddingBackend' is an internal backend wrapper that stores a 'SemanticEmbedding' model alongside an 'OpenAiEmbeddingBackend' used for query-side embedding generation. [crates/gwiki/src/vector.rs:342-345] |

_18 more symbol(s) not shown — run `gcode outline crates/gwiki/src/vector.rs` for the full list._

_Verified by 5 in-file unit tests._

