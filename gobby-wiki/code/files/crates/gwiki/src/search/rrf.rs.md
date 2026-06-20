---
title: crates/gwiki/src/search/rrf.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/rrf.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/rrf.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Overview

`crates/gwiki/src/search/rrf.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/search/rrf.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `fuse_sources` | function | 'fuse_sources' deduplicates and merges BM25, semantic, and graph 'WikiSearchResult' lists by fusion key, computes a Reciprocal Rank Fusion ordering from their ranked keys, updates each surviving result’s score/sources/explanations from the fused output, and returns up to 'limit' results with the provided degradations, or an empty response when 'limit == 0'. [crates/gwiki/src/search/rrf.rs:8-92] |
| `ranked_keys` | function | Maps each 'WikiSearchResult' in 'hits' to its 'fusion_key' and collects the results into a 'Vec<String>', propagating any 'SearchError' returned by the iterator. [crates/gwiki/src/search/rrf.rs:94-96] |
| `merge_hit_metadata` | function | Merges missing metadata from 'hit' into 'existing' by copying 'title' when absent, 'snippet' when empty, and 'chunk' when absent. [crates/gwiki/src/search/rrf.rs:98-108] |
| `search_result` | function | Constructs and returns a 'WikiSearchResult' populated with the given 'id' and single 'source', plus fixed Rust document metadata, snippet, chunk provenance, and source provenance. [crates/gwiki/src/search/rrf.rs:242-267] |

_Verified by 3 in-file unit tests._

