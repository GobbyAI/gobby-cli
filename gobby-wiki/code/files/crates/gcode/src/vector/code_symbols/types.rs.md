---
title: crates/gcode/src/vector/code_symbols/types.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/types.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Overview

`crates/gcode/src/vector/code_symbols/types.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/vector/code_symbols/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodeSymbolVectorSearchRequest` | class | 'CodeSymbolVectorSearchRequest' is a request payload that carries a project identifier, a text query, a result limit, and a collection prefix for performing vector-based code symbol search. [crates/gcode/src/vector/code_symbols/types.rs:7-12] |
| `CodeSymbolVectorSearchHit` | class | 'CodeSymbolVectorSearchHit' is a struct representing a vector-search result for a code symbol, containing the symbol’s identifier as a 'String' and its similarity 'score' as an 'f64'. [crates/gcode/src/vector/code_symbols/types.rs:15-18] |
| `CodeSymbolVectorSearchHit::eq` | method | Returns 'true' only when both 'symbol_id' values are equal and the 'score' fields have identical bit patterns via 'to_bits()', making equality exact for the floating-point score. [crates/gcode/src/vector/code_symbols/types.rs:21-23] |
| `CodeSymbolVectorPayload` | class | 'CodeSymbolVectorPayload' is a serialized Rust data structure representing a projected code symbol embedding/vector record, capturing the symbol’s identity, location, language metadata, optional signature/docstring/summary, provenance, confidence, and source-to-projection mapping fields. [crates/gcode/src/vector/code_symbols/types.rs:29-57] |
| `CodeSymbolVectorPayload::from_symbol` | method | Constructs a new instance from a 'Symbol' by cloning its structural fields, deriving 'ProjectionMetadata::gcode_extracted()' from the symbol’s file path, line, and ID, and populating provenance/source fields from that metadata with fallbacks to the symbol’s own values. [crates/gcode/src/vector/code_symbols/types.rs:60-95] |
| `CodeSymbolVectorLifecycleAction` | type | Indexed type `CodeSymbolVectorLifecycleAction` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:100-105] |
| `CodeSymbolVectorLifecycleStatus` | class | 'CodeSymbolVectorLifecycleStatus' is a status record containing a 'project_id', 'collection', and a 'CodeSymbolVectorLifecycleAction' that identifies the lifecycle operation associated with a code-symbol vector. [crates/gcode/src/vector/code_symbols/types.rs:108-112] |
| `VectorCollectionSchema` | class | 'VectorCollectionSchema' is a Rust struct representing a vector collection schema with a 'size: usize' dimension and a 'distance: String' metric identifier. [crates/gcode/src/vector/code_symbols/types.rs:115-118] |
| `ExistingVectorCollectionSchema` | class | 'ExistingVectorCollectionSchema' is an internal struct that represents an existing vector collection’s schema with optional 'size' and 'distance' fields. [crates/gcode/src/vector/code_symbols/types.rs:121-124] |
| `CodeSymbolVectorLifecycleOutput` | class | 'CodeSymbolVectorLifecycleOutput' is a lifecycle event summary struct that records the project, collection, action, optional file path, symbol count, vector upsert count, delete operation count, and a human-readable summary for code symbol vector processing. [crates/gcode/src/vector/code_symbols/types.rs:127-137] |
| `VectorLifecycleError` | type | Indexed type `VectorLifecycleError` in `crates/gcode/src/vector/code_symbols/types.rs`. [crates/gcode/src/vector/code_symbols/types.rs:140-162] |
| `VectorLifecycleError::fmt` | method | Implements 'Display' for the error enum by mapping each variant to a specific human-readable diagnostic string, including formatted HTTP/Qdrant failures and a detailed vector-schema dimension mismatch message. [crates/gcode/src/vector/code_symbols/types.rs:165-202] |
| `VectorLifecycleError::from` | method | Converts a 'gobby_core::qdrant::CollectionNameError' into this type by wrapping it in 'Self::InvalidCollectionName'. [crates/gcode/src/vector/code_symbols/types.rs:206-208] |

