---
title: crates/gwiki/src/support/counts.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/counts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/counts.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/counts.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/support/counts.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IndexCounts` | class | 'IndexCounts' is an internal struct that stores 'usize' counters for the number of documents, chunks, links, sources, and ingestions in an index. [crates/gwiki/src/support/counts.rs:4-10] |
| `index_counts` | function | Returns an 'IndexCounts' snapshot of a 'MemoryWikiStore' by counting top-level documents, total chunks across all chunk vectors, total links across all link vectors, sources, and ingestions. [crates/gwiki/src/support/counts.rs:12-20] |
| `postgres_index_counts` | function | Queries PostgreSQL for scoped row counts across the 'Documents', 'Chunks', 'Links', 'Sources', and 'Ingestions' tables and returns them as an 'IndexCounts' result. [crates/gwiki/src/support/counts.rs:22-33] |
| `GwikiTable` | type | Indexed type `GwikiTable` in `crates/gwiki/src/support/counts.rs`. [crates/gwiki/src/support/counts.rs:36-42] |
| `GwikiTable::as_identifier` | method | Returns a static string identifier for the enum variant, mapping 'Documents', 'Chunks', 'Links', 'Sources', and 'Ingestions' to '"gwiki_documents"', '"gwiki_chunks"', '"gwiki_links"', '"gwiki_sources"', and '"gwiki_ingestions"' respectively. [crates/gwiki/src/support/counts.rs:45-53] |
| `postgres_count` | function | Counts rows in the specified PostgreSQL table for the given search scope ('scope_kind' and 'scope_id'), returning the count as 'usize' and mapping query or conversion failures to 'WikiError::Config'. [crates/gwiki/src/support/counts.rs:56-72] |

_Verified by 1 in-file unit test._

