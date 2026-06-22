---
title: crates/gwiki/src/support/search.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/search.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/search.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/search.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gwiki/src/support/search.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `StoreBm25Backend` | class | 'StoreBm25Backend' is a crate-private struct that holds an 'Arc'-backed slice of 'search::WikiSearchResult' values in its 'hits' field. [crates/gwiki/src/support/search.rs:11-13] |
| `StoreBm25Backend::search_bm25` | method | Returns up to 'request.limit' cloned entries from 'self.hits' in iteration order, wrapped in 'Ok' as a 'Vec`<search::WikiSearchResult>`' without performing any BM25 scoring or filtering. [crates/gwiki/src/support/search.rs:16-21] |
| `UnavailableSemanticBackend` | class | 'UnavailableSemanticBackend' is a crate-private unit-like struct that likely serves as a placeholder or sentinel implementation for a semantic backend that is unavailable. [crates/gwiki/src/support/search.rs:24] |
| `UnavailableSemanticBackend::search_semantic` | method | 'search_semantic' ignores the request and always returns 'Ok(SemanticSearchOutcome { hits: Vec::new(), degradation: Some(ServiceUnavailable { service: "qdrant", state: NotConfigured }) })', indicating semantic search is unavailable because Qdrant is not configured. [crates/gwiki/src/support/search.rs:27-38] |
| `PostgresConfigSource` | class | 'PostgresConfigSource<'a>' is a crate-private wrapper holding a mutable borrowed 'postgres::Client', intended as a configuration source backed by an existing PostgreSQL connection. [crates/gwiki/src/support/search.rs:41-43] |
| `config_value` | function | Looks up a configuration entry by key from the PostgreSQL connection, discards read errors and missing values, and returns the decoded 'String' if the stored raw value can be successfully decoded. [crates/gwiki/src/support/search.rs:46-51] |
| `resolve_value` | function | Resolves a config value string by delegating to 'gobby_core::secrets::resolve_config_value(value, self.conn)', returning the decrypted or otherwise expanded value as 'Result<String>'. [crates/gwiki/src/support/search.rs:53-57] |
| `store_search_hits` | function | Searches a 'MemoryWikiStore' for BM25 keyword matches against searchable documents and their chunks, builds 'WikiSearchResult' entries with snippets, provenance, and scores, and returns the ranked results for the given 'SearchScope' and query. [crates/gwiki/src/support/search.rs:60-161] |

