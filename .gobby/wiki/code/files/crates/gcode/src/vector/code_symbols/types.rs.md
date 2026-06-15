---
title: crates/gcode/src/vector/code_symbols/types.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/types.rs
  ranges:
  - 7-12
  - 15-18
  - 20-24
  - '26'
  - 29-57
  - 59-96
  - 100-105
  - 108-112
  - 115-118
  - 121-124
  - 127-137
  - 140-162
  - 164-203
  - 205-209
  - '211'
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/types.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

Defines the data types used by gcode’s vector-based code-symbol search and indexing workflow: a search request, search hits, the serialized payload sent to vector storage, lifecycle status/output records, collection schema descriptors, and the lifecycle error type. The payload layer is built from `Symbol` via `CodeSymbolVectorPayload::from_symbol`, which copies symbol fields and derives projection/source metadata, while the lifecycle types and `VectorLifecycleError` support reporting and validating collection/index operations.
[crates/gcode/src/vector/code_symbols/types.rs:7-12]
[crates/gcode/src/vector/code_symbols/types.rs:15-18]
[crates/gcode/src/vector/code_symbols/types.rs:20-24]
[crates/gcode/src/vector/code_symbols/types.rs:21-23]
[crates/gcode/src/vector/code_symbols/types.rs:26]

## API Symbols

- `CodeSymbolVectorSearchRequest` (class) component `CodeSymbolVectorSearchRequest [class]` (`65316a17-ce8a-5bd1-8bb5-52c6c17fc461`) lines 7-12 [crates/gcode/src/vector/code_symbols/types.rs:7-12]
  - Signature: `pub struct CodeSymbolVectorSearchRequest {`
  - Purpose: 'CodeSymbolVectorSearchRequest' is a request struct carrying a project identifier, free-text query, result limit, and collection prefix for performing a vector-based code symbol search. [crates/gcode/src/vector/code_symbols/types.rs:7-12]
- `CodeSymbolVectorSearchHit` (class) component `CodeSymbolVectorSearchHit [class]` (`d204faac-09ef-5bed-965e-eab0f4b4afe7`) lines 15-18 [crates/gcode/src/vector/code_symbols/types.rs:15-18]
  - Signature: `pub struct CodeSymbolVectorSearchHit {`
  - Purpose: 'CodeSymbolVectorSearchHit' is a simple Rust struct representing a vector-search result for a code symbol, containing the symbol’s string identifier ('symbol_id') and its similarity score ('score') as an 'f64'. [crates/gcode/src/vector/code_symbols/types.rs:15-18]
- `CodeSymbolVectorSearchHit` (class) component `CodeSymbolVectorSearchHit [class]` (`23cc5ef1-f174-5ba6-b44f-9f594ad9572b`) lines 20-24 [crates/gcode/src/vector/code_symbols/types.rs:20-24]
  - Signature: `impl PartialEq for CodeSymbolVectorSearchHit {`
  - Purpose: 'CodeSymbolVectorSearchHit' implements 'PartialEq' by considering two hits equal only when their 'symbol_id' values match and their 'score' fields have identical IEEE-754 bit patterns via 'to_bits()'. [crates/gcode/src/vector/code_symbols/types.rs:20-24]
- `CodeSymbolVectorSearchHit.eq` (method) component `CodeSymbolVectorSearchHit.eq [method]` (`d01e7a34-fc6f-548f-b384-dc4b104e7b55`) lines 21-23 [crates/gcode/src/vector/code_symbols/types.rs:21-23]
  - Signature: `fn eq(&self, other: &Self) -> bool {`
  - Purpose: Compares two values for equality by requiring both their 'symbol_id' fields to match and their 'score' values to have identical bit representations via 'to_bits()'. [crates/gcode/src/vector/code_symbols/types.rs:21-23]
- `CodeSymbolVectorSearchHit` (class) component `CodeSymbolVectorSearchHit [class]` (`e22d7e1f-9b3d-5e0b-89be-efee738a3d3d`) lines 26-26 [crates/gcode/src/vector/code_symbols/types.rs:26]
  - Signature: `impl Eq for CodeSymbolVectorSearchHit {}`
  - Purpose: 'CodeSymbolVectorSearchHit' is a type that implements Rust’s 'Eq' marker trait, meaning its equality relation is intended to be total and reflexive. [crates/gcode/src/vector/code_symbols/types.rs:26]
- `CodeSymbolVectorPayload` (class) component `CodeSymbolVectorPayload [class]` (`f8575018-c310-5f4d-b4ba-38068aa239b8`) lines 29-57 [crates/gcode/src/vector/code_symbols/types.rs:29-57]
  - Signature: `pub struct CodeSymbolVectorPayload {`
  - Purpose: 'CodeSymbolVectorPayload' is a serialized record of a code symbol’s identity, location, optional signature/docstring/summary, provenance, confidence, and source-trace metadata used for vector or projection indexing. [crates/gcode/src/vector/code_symbols/types.rs:29-57]
- `CodeSymbolVectorPayload` (class) component `CodeSymbolVectorPayload [class]` (`d7067fbf-344d-5eb5-9895-6c0f2093f14b`) lines 59-96 [crates/gcode/src/vector/code_symbols/types.rs:59-96]
  - Signature: `impl CodeSymbolVectorPayload {`
  - Purpose: CodeSymbolVectorPayload is a projection DTO that copies a 'Symbol'’s identity, location, language, signature, docstring, and summary while deriving provenance and source metadata from 'ProjectionMetadata::gcode_extracted()'. [crates/gcode/src/vector/code_symbols/types.rs:59-96]
- `CodeSymbolVectorPayload.from_symbol` (method) component `CodeSymbolVectorPayload.from_symbol [method]` (`f219b2fa-d247-5836-ba03-20ae4c78e205`) lines 60-95 [crates/gcode/src/vector/code_symbols/types.rs:60-95]
  - Signature: `pub fn from_symbol(symbol: &Symbol) -> Self {`
  - Purpose: 'from_symbol' constructs a new value by cloning all core fields from the input 'Symbol' and deriving 'ProjectionMetadata' from it to populate provenance, confidence, source-system, and source-location fields with fallbacks to the symbol’s own path, line, and ID. [crates/gcode/src/vector/code_symbols/types.rs:60-95]
- `CodeSymbolVectorLifecycleAction` (type) component `CodeSymbolVectorLifecycleAction [type]` (`0f7d8ff6-916f-5bcc-b7bc-7cb33636e893`) lines 100-105 [crates/gcode/src/vector/code_symbols/types.rs:100-105]
  - Signature: `pub enum CodeSymbolVectorLifecycleAction {`
  - Purpose: Indexed type `CodeSymbolVectorLifecycleAction` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:100-105]
- `CodeSymbolVectorLifecycleStatus` (class) component `CodeSymbolVectorLifecycleStatus [class]` (`162bae87-0458-53fd-9633-28adf1c39d8b`) lines 108-112 [crates/gcode/src/vector/code_symbols/types.rs:108-112]
  - Signature: `pub struct CodeSymbolVectorLifecycleStatus {`
  - Purpose: 'CodeSymbolVectorLifecycleStatus' is a Rust struct that records a code-symbol vector lifecycle event by storing the target 'project_id', the 'collection' name, and the requested 'CodeSymbolVectorLifecycleAction'. [crates/gcode/src/vector/code_symbols/types.rs:108-112]
- `VectorCollectionSchema` (class) component `VectorCollectionSchema [class]` (`f2c824d8-ca68-5ca4-a41f-9b46bded1215`) lines 115-118 [crates/gcode/src/vector/code_symbols/types.rs:115-118]
  - Signature: `pub struct VectorCollectionSchema {`
  - Purpose: 'VectorCollectionSchema' is a Rust struct that defines a vector collection’s dimensionality via 'size: usize' and its similarity metric via 'distance: String'. [crates/gcode/src/vector/code_symbols/types.rs:115-118]
- `ExistingVectorCollectionSchema` (class) component `ExistingVectorCollectionSchema [class]` (`282517bd-4ac6-5596-88f4-ab64ab4a668b`) lines 121-124 [crates/gcode/src/vector/code_symbols/types.rs:121-124]
  - Signature: `pub(super) struct ExistingVectorCollectionSchema {`
  - Purpose: 'ExistingVectorCollectionSchema' is a package-visible struct that models an existing vector collection schema with optional 'size' and 'distance' fields, representing the collection’s dimensionality and distance metric when known. [crates/gcode/src/vector/code_symbols/types.rs:121-124]
- `CodeSymbolVectorLifecycleOutput` (class) component `CodeSymbolVectorLifecycleOutput [class]` (`af0db07d-8165-585a-be70-2c6c196ae49b`) lines 127-137 [crates/gcode/src/vector/code_symbols/types.rs:127-137]
  - Signature: `pub struct CodeSymbolVectorLifecycleOutput {`
  - Purpose: 'CodeSymbolVectorLifecycleOutput' is a serialized lifecycle-report struct that records a project's vector index action for a collection, optional file path, symbol count, upsert and delete operation counts, and a human-readable summary. [crates/gcode/src/vector/code_symbols/types.rs:127-137]
- `VectorLifecycleError` (type) component `VectorLifecycleError [type]` (`98ee2ca2-7c11-55ca-94c8-fd1a47f3ab2c`) lines 140-162 [crates/gcode/src/vector/code_symbols/types.rs:140-162]
  - Signature: `pub enum VectorLifecycleError {`
  - Purpose: Indexed type `VectorLifecycleError` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:140-162]
- `VectorLifecycleError` (class) component `VectorLifecycleError [class]` (`498eee69-e61d-5803-b375-f2d9b53e9314`) lines 164-203 [crates/gcode/src/vector/code_symbols/types.rs:164-203]
  - Signature: `impl fmt::Display for VectorLifecycleError {`
  - Purpose: 'VectorLifecycleError' is a 'fmt::Display' implementation that renders user-facing error messages for vector lifecycle failures, covering missing configuration, embedding/Qdrant HTTP and operation errors, invalid collection names, and vector schema dimension mismatches. [crates/gcode/src/vector/code_symbols/types.rs:164-203]
- `VectorLifecycleError.fmt` (method) component `VectorLifecycleError.fmt [method]` (`f51a3038-d569-5151-870e-058553cd7d44`) lines 165-202 [crates/gcode/src/vector/code_symbols/types.rs:165-202]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Formats the vector-lifecycle error enum into human-readable diagnostics by mapping each variant to a specific message, including HTTP failures, invalid responses, and incompatible Qdrant collection schema details. [crates/gcode/src/vector/code_symbols/types.rs:165-202]
- `VectorLifecycleError` (class) component `VectorLifecycleError [class]` (`afbc5712-8af6-5923-b6b8-d893f06328d9`) lines 205-209 [crates/gcode/src/vector/code_symbols/types.rs:205-209]
  - Signature: `impl From<gobby_core::qdrant::CollectionNameError> for VectorLifecycleError {`
  - Purpose: 'VectorLifecycleError' implements 'From<gobby_core::qdrant::CollectionNameError>' by converting any collection-name validation failure into the 'InvalidCollectionName' variant. [crates/gcode/src/vector/code_symbols/types.rs:205-209]
- `VectorLifecycleError.from` (method) component `VectorLifecycleError.from [method]` (`fb8135a0-996e-5985-8b6d-abbb9be96255`) lines 206-208 [crates/gcode/src/vector/code_symbols/types.rs:206-208]
  - Signature: `fn from(error: gobby_core::qdrant::CollectionNameError) -> Self {`
  - Purpose: Converts a 'gobby_core::qdrant::CollectionNameError' into 'Self' by wrapping it in the 'InvalidCollectionName' variant. [crates/gcode/src/vector/code_symbols/types.rs:206-208]
- `VectorLifecycleError` (class) component `VectorLifecycleError [class]` (`02f21757-ae57-5d06-ac1c-253b029b90b9`) lines 211-211 [crates/gcode/src/vector/code_symbols/types.rs:211]
  - Signature: `impl std::error::Error for VectorLifecycleError {}`
  - Purpose: 'VectorLifecycleError' is a Rust error type that serves as the error trait implementation for failures in vector lifecycle operations. [crates/gcode/src/vector/code_symbols/types.rs:211]

