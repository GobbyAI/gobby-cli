---
title: crates/gcode/src/vector/code_symbols/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/lifecycle.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/lifecycle.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Overview

`crates/gcode/src/vector/code_symbols/lifecycle.rs` exposes 23 indexed API symbols.

## How it fits

`crates/gcode/src/vector/code_symbols/lifecycle.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodeSymbolVectorLifecycle` | class | 'CodeSymbolVectorLifecycle' encapsulates the configuration and runtime state needed to manage a project-scoped code-symbol vector collection, including Qdrant connection details, embedding backend, vector settings, an optional probed vector dimension, and a blocking HTTP client. [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37] |
| `resolve_lifecycle_qdrant_config` | function | Returns the optional 'QdrantConfig' produced by delegating to 'gobby_core::config::resolve_qdrant_config' on the provided mutable 'ConfigSource'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:39-43] |
| `lifecycle_status` | function | Constructs and returns a 'CodeSymbolVectorLifecycleStatus' by converting 'project_id' into a 'String', deriving 'collection' from 'collection_prefix' and 'project_id' via 'collection_name', and populating the struct with the given 'action', propagating any 'VectorLifecycleError' from collection name generation. [crates/gcode/src/vector/code_symbols/lifecycle.rs:45-56] |
| `CodeSymbolVectorLifecycle::new` | method | Constructs a 'VectorLifecycle' by validating the Qdrant boundary config, deriving the project-specific code symbol collection name, initializing the embedding backend and a blocking 'reqwest' client with the Qdrant lifecycle timeout, and storing the provided project, Qdrant config, and vector settings with 'probed_vector_size' unset. [crates/gcode/src/vector/code_symbols/lifecycle.rs:59-82] |
| `CodeSymbolVectorLifecycle::collection` | method | Returns an immutable string slice reference to the 'collection' field of 'self'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:84-86] |
| `CodeSymbolVectorLifecycle::ensure_collection` | method | Computes the expected vector collection schema, verifies Qdrant boundary constraints, then either validates compatibility against an existing collection schema or creates the collection if absent, returning the schema or a 'VectorLifecycleError' on failure. [crates/gcode/src/vector/code_symbols/lifecycle.rs:88-98] |
| `CodeSymbolVectorLifecycle::sync_file_symbols` | method | 'sync_file_symbols' ensures the collection exists, converts the given file’s symbols into vectors, upserts them, deletes any stale vectors for the same file path not present in the new point IDs, and returns a lifecycle summary of the sync operation. [crates/gcode/src/vector/code_symbols/lifecycle.rs:100-118] |
| `CodeSymbolVectorLifecycle::clear_project_vectors` | method | 'clear_project_vectors' verifies the Qdrant boundary, optionally validates the existing collection schema against the configured vector dimension and cosine distance, deletes all vectors in the project if the collection exists, and returns a 'CodeSymbolVectorLifecycleOutput' reporting the 'Clear' action and number deleted. [crates/gcode/src/vector/code_symbols/lifecycle.rs:120-141] |
| `CodeSymbolVectorLifecycle::rebuild_symbols` | method | Ensures the collection exists, converts the provided symbols into vectors using the collection schema size, upserts those points, deletes any stale vectors not in the new point ID set, and returns a rebuild lifecycle summary with counts of symbols processed, vectors upserted, and delete operations issued. [crates/gcode/src/vector/code_symbols/lifecycle.rs:143-160] |
| `CodeSymbolVectorLifecycle::output` | method | Constructs and returns a 'CodeSymbolVectorLifecycleOutput' by cloning the current project and collection identifiers, copying through the provided lifecycle fields and counts, and formatting a summary string of upserted vectors and issued delete operations. [crates/gcode/src/vector/code_symbols/lifecycle.rs:162-182] |
| `CodeSymbolVectorLifecycle::expected_schema` | method | Returns a 'VectorCollectionSchema' whose 'size' is taken from 'settings.vector_dim', otherwise from a cached 'probed_vector_size', otherwise by embedding a probe text to infer the vector length and caching it, with 'distance' fixed to cosine. [crates/gcode/src/vector/code_symbols/lifecycle.rs:184-201] |
| `CodeSymbolVectorLifecycle::require_qdrant_boundary` | method | Delegates validation to 'Self::require_qdrant_boundary_config' using 'self.qdrant' and returns its 'Result<(), VectorLifecycleError>'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:203-205] |
| `CodeSymbolVectorLifecycle::require_qdrant_boundary_config` | method | Calls 'gobby_core::qdrant::with_qdrant' to validate the supplied 'QdrantConfig' and returns 'Ok(())' only when the resulting service state is 'Available', otherwise mapping configuration absence to 'VectorLifecycleError::MissingQdrantConfig' and any Qdrant setup or unexpected state to 'VectorLifecycleError::QdrantOperation'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:207-217] |
| `CodeSymbolVectorLifecycle::ensure_compatible_schema` | method | 'ensure_compatible_schema' verifies that an existing vector collection schema matches the expected 'size' and 'distance', returns a normalized 'VectorCollectionSchema' on exact match, and otherwise raises 'VectorLifecycleError::DimensionMismatch' populated with the collection name plus expected/found size and distance details. [crates/gcode/src/vector/code_symbols/lifecycle.rs:219-240] |
| `CodeSymbolVectorLifecycle::get_collection_schema` | method | Performs a Qdrant 'GET' on the collection endpoint, returns 'Ok(None)' for '404 Not Found', maps other non-success statuses to a 'VectorLifecycleError', and otherwise deserializes the JSON response into 'Option<ExistingVectorCollectionSchema>' via 'parse_collection_schema'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:242-261] |
| `CodeSymbolVectorLifecycle::create_collection` | method | Creates a Qdrant collection by issuing a 'PUT' request with vector size and distance from the provided schema, returning 'Ok(())' on any 2xx response and mapping request or non-success HTTP statuses to 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:263-282] |
| `CodeSymbolVectorLifecycle::delete_vectors` | method | Forwards the optional 'file_path' filter, along with the client, Qdrant handle, collection, and project ID, to 'delete_vectors_for_filter' and returns the number of deleted vectors or a 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:284-292] |
| `CodeSymbolVectorLifecycle::delete_stale_vectors` | method | 'delete_stale_vectors' delegates to 'delete_vectors_for_filter_excluding_ids' to remove vectors from the collection for the given project and optional file path, excluding the specified 'keep_point_ids', and returns the number deleted or a 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:294-307] |
| `CodeSymbolVectorLifecycle::upsert_points` | method | 'upsert_points' returns 'Ok(0)' for an empty input, otherwise batches the provided 'UpsertRequest' values into Qdrant via 'with_qdrant'/'upsert_batched' and returns the original point count on 'ServiceState::Available', 'MissingQdrantConfig' when unconfigured, or a 'QdrantOperation' error for any Qdrant failure or unexpected service state. [crates/gcode/src/vector/code_symbols/lifecycle.rs:309-326] |
| `CodeSymbolVectorLifecycle::points_for_symbols` | method | Builds 'UpsertRequest' records for a nonempty slice of 'Symbol's by batching them into embedding requests, validating that the returned batch cardinality and each vector’s dimensionality match expectations, and converting each symbol plus its embedding payload into a vector upsert entry. [crates/gcode/src/vector/code_symbols/lifecycle.rs:328-367] |
| `CodeSymbolVectorLifecycle::qdrant_request` | method | Delegates construction of a blocking 'reqwest::RequestBuilder' for the given HTTP 'method' and 'path' to 'qdrant_request_for_config', using 'self.client' and 'self.qdrant', and returns a 'Result' or 'VectorLifecycleError'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:369-375] |
| `payload_map` | function | Serializes a 'CodeSymbolVectorPayload' to JSON and returns it as a 'Map<String, Value>', or maps serialization/non-object results to 'VectorLifecycleError::QdrantOperation'. [crates/gcode/src/vector/code_symbols/lifecycle.rs:378-389] |
| `point_ids` | function | Returns a 'Vec<String>' containing a cloned 'id' from each 'UpsertRequest' in 'points', preserving input order. [crates/gcode/src/vector/code_symbols/lifecycle.rs:391-393] |

