---
title: crates/gcode/src/vector/code_symbols/types.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/types.rs
  ranges:
  - 7-12
  - 15-18
  - 21-23
  - 29-57
  - 60-95
  - 100-105
  - 108-112
  - 115-118
  - 121-124
  - 127-137
  - 140-162
  - 165-202
  - 206-208
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/vector/code_symbols/types.rs:7-12](crates/gcode/src/vector/code_symbols/types.rs#L7-L12), [crates/gcode/src/vector/code_symbols/types.rs:15-18](crates/gcode/src/vector/code_symbols/types.rs#L15-L18), [crates/gcode/src/vector/code_symbols/types.rs:21-23](crates/gcode/src/vector/code_symbols/types.rs#L21-L23), [crates/gcode/src/vector/code_symbols/types.rs:29-57](crates/gcode/src/vector/code_symbols/types.rs#L29-L57), [crates/gcode/src/vector/code_symbols/types.rs:60-95](crates/gcode/src/vector/code_symbols/types.rs#L60-L95), [crates/gcode/src/vector/code_symbols/types.rs:100-105](crates/gcode/src/vector/code_symbols/types.rs#L100-L105), [crates/gcode/src/vector/code_symbols/types.rs:108-112](crates/gcode/src/vector/code_symbols/types.rs#L108-L112), [crates/gcode/src/vector/code_symbols/types.rs:115-118](crates/gcode/src/vector/code_symbols/types.rs#L115-L118), [crates/gcode/src/vector/code_symbols/types.rs:121-124](crates/gcode/src/vector/code_symbols/types.rs#L121-L124), [crates/gcode/src/vector/code_symbols/types.rs:127-137](crates/gcode/src/vector/code_symbols/types.rs#L127-L137), [crates/gcode/src/vector/code_symbols/types.rs:140-162](crates/gcode/src/vector/code_symbols/types.rs#L140-L162), [crates/gcode/src/vector/code_symbols/types.rs:165-202](crates/gcode/src/vector/code_symbols/types.rs#L165-L202), [crates/gcode/src/vector/code_symbols/types.rs:206-208](crates/gcode/src/vector/code_symbols/types.rs#L206-L208)

</details>

# crates/gcode/src/vector/code_symbols/types.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

This file defines the data types used by the code-symbol vector indexing and lifecycle flow. It includes a search request and search hit model for querying vector collections, a rich payload type built from a `Symbol` via `CodeSymbolVectorPayload::from_symbol`, and supporting lifecycle types for collection schema, status, output, and errors. The pieces work together by turning extracted symbol metadata and provenance into serializable payloads, then wrapping the results and failures of vector collection setup or maintenance in strongly typed request/output/error structures.
[crates/gcode/src/vector/code_symbols/types.rs:7-12]
[crates/gcode/src/vector/code_symbols/types.rs:15-18]
[crates/gcode/src/vector/code_symbols/types.rs:21-23]
[crates/gcode/src/vector/code_symbols/types.rs:29-57]
[crates/gcode/src/vector/code_symbols/types.rs:60-95]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CodeSymbolVectorSearchRequest` | class | `pub struct CodeSymbolVectorSearchRequest {` | `CodeSymbolVectorSearchRequest [class]` | `65316a17-ce8a-5bd1-8bb5-52c6c17fc461` | 7-12 [crates/gcode/src/vector/code_symbols/types.rs:7-12] | Indexed class `CodeSymbolVectorSearchRequest` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:7-12] |
| `CodeSymbolVectorSearchHit` | class | `pub struct CodeSymbolVectorSearchHit {` | `CodeSymbolVectorSearchHit [class]` | `d204faac-09ef-5bed-965e-eab0f4b4afe7` | 15-18 [crates/gcode/src/vector/code_symbols/types.rs:15-18] | Indexed class `CodeSymbolVectorSearchHit` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:15-18] |
| `CodeSymbolVectorSearchHit::eq` | method | `fn eq(&self, other: &Self) -> bool {` | `CodeSymbolVectorSearchHit::eq [method]` | `d01e7a34-fc6f-548f-b384-dc4b104e7b55` | 21-23 [crates/gcode/src/vector/code_symbols/types.rs:21-23] | Indexed method `CodeSymbolVectorSearchHit::eq` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:21-23] |
| `CodeSymbolVectorPayload` | class | `pub struct CodeSymbolVectorPayload {` | `CodeSymbolVectorPayload [class]` | `f8575018-c310-5f4d-b4ba-38068aa239b8` | 29-57 [crates/gcode/src/vector/code_symbols/types.rs:29-57] | Indexed class `CodeSymbolVectorPayload` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:29-57] |
| `CodeSymbolVectorPayload::from_symbol` | method | `pub fn from_symbol(symbol: &Symbol) -> Self {` | `CodeSymbolVectorPayload::from_symbol [method]` | `f219b2fa-d247-5836-ba03-20ae4c78e205` | 60-95 [crates/gcode/src/vector/code_symbols/types.rs:60-95] | Indexed method `CodeSymbolVectorPayload::from_symbol` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:60-95] |
| `CodeSymbolVectorLifecycleAction` | type | `pub enum CodeSymbolVectorLifecycleAction {` | `CodeSymbolVectorLifecycleAction [type]` | `0f7d8ff6-916f-5bcc-b7bc-7cb33636e893` | 100-105 [crates/gcode/src/vector/code_symbols/types.rs:100-105] | Indexed type `CodeSymbolVectorLifecycleAction` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:100-105] |
| `CodeSymbolVectorLifecycleStatus` | class | `pub struct CodeSymbolVectorLifecycleStatus {` | `CodeSymbolVectorLifecycleStatus [class]` | `162bae87-0458-53fd-9633-28adf1c39d8b` | 108-112 [crates/gcode/src/vector/code_symbols/types.rs:108-112] | Indexed class `CodeSymbolVectorLifecycleStatus` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:108-112] |
| `VectorCollectionSchema` | class | `pub struct VectorCollectionSchema {` | `VectorCollectionSchema [class]` | `f2c824d8-ca68-5ca4-a41f-9b46bded1215` | 115-118 [crates/gcode/src/vector/code_symbols/types.rs:115-118] | Indexed class `VectorCollectionSchema` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:115-118] |
| `ExistingVectorCollectionSchema` | class | `pub(super) struct ExistingVectorCollectionSchema {` | `ExistingVectorCollectionSchema [class]` | `282517bd-4ac6-5596-88f4-ab64ab4a668b` | 121-124 [crates/gcode/src/vector/code_symbols/types.rs:121-124] | Indexed class `ExistingVectorCollectionSchema` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:121-124] |
| `CodeSymbolVectorLifecycleOutput` | class | `pub struct CodeSymbolVectorLifecycleOutput {` | `CodeSymbolVectorLifecycleOutput [class]` | `af0db07d-8165-585a-be70-2c6c196ae49b` | 127-137 [crates/gcode/src/vector/code_symbols/types.rs:127-137] | Indexed class `CodeSymbolVectorLifecycleOutput` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:127-137] |
| `VectorLifecycleError` | type | `pub enum VectorLifecycleError {` | `VectorLifecycleError [type]` | `98ee2ca2-7c11-55ca-94c8-fd1a47f3ab2c` | 140-162 [crates/gcode/src/vector/code_symbols/types.rs:140-162] | Indexed type `VectorLifecycleError` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:140-162] |
| `VectorLifecycleError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `VectorLifecycleError::fmt [method]` | `f51a3038-d569-5151-870e-058553cd7d44` | 165-202 [crates/gcode/src/vector/code_symbols/types.rs:165-202] | Indexed method `VectorLifecycleError::fmt` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:165-202] |
| `VectorLifecycleError::from` | method | `fn from(error: gobby_core::qdrant::CollectionNameError) -> Self {` | `VectorLifecycleError::from [method]` | `fb8135a0-996e-5985-8b6d-abbb9be96255` | 206-208 [crates/gcode/src/vector/code_symbols/types.rs:206-208] | Indexed method `VectorLifecycleError::from` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:206-208] |
