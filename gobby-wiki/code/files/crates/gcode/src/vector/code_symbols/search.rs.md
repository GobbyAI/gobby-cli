---
title: crates/gcode/src/vector/code_symbols/search.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/search.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/search.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Overview

`crates/gcode/src/vector/code_symbols/search.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/vector/code_symbols/search.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SearchError` | type | Indexed type `SearchError` in `crates/gcode/src/vector/code_symbols/search.rs`. [crates/gcode/src/vector/code_symbols/search.rs:8-14] |
| `SearchError::fmt` | method | Implements 'Display' formatting for the error enum by mapping each variant to a specific human-readable message, including forwarding inner errors for 'InvalidCollectionName' and prefixing 'VectorSearch' errors with 'semantic vector search failed:'. [crates/gcode/src/vector/code_symbols/search.rs:17-25] |
| `search_code_symbols` | function | Performs an embedding-based vector search for code symbols by validating Qdrant and embedding configuration, generating a query embedding, building the target collection name, executing the vector lookup with the requested limit, and mapping returned symbol IDs and scores into 'CodeSymbolVectorSearchHit' values or a 'SearchError' on failure. [crates/gcode/src/vector/code_symbols/search.rs:30-58] |
| `semantic_search` | function | Builds a 'CodeSymbolVectorSearchRequest' from the current project, query, and limit, calls 'search_code_symbols', and returns each hit’s '(symbol_id, score)' pair or an empty vector after logging a warning if the search fails. [crates/gcode/src/vector/code_symbols/search.rs:63-81] |

