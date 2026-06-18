---
title: crates/gwiki/src/search/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/mod.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Overview

`crates/gwiki/src/search/mod.rs` exposes 33 indexed API symbols.

## How it fits

`crates/gwiki/src/search/mod.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SearchScope` | type | Indexed type `SearchScope` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:14-18] |
| `SearchScope::global` | method | Indexed method `SearchScope::global` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:21-23] |
| `SearchScope::project` | method | Indexed method `SearchScope::project` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:25-29] |
| `SearchScope::topic` | method | Indexed method `SearchScope::topic` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:31-35] |
| `SearchScope::scope_kind` | method | Indexed method `SearchScope::scope_kind` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:37-43] |
| `SearchScope::scope_value` | method | Indexed method `SearchScope::scope_value` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:45-51] |
| `SearchScope::scope_filter` | method | Indexed method `SearchScope::scope_filter` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:53-59] |
| `SearchSource` | type | Indexed type `SearchSource` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:63-67] |
| `SearchSource::as_str` | method | Indexed method `SearchSource::as_str` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:70-76] |
| `SearchSource::from_source_name` | method | Indexed method `SearchSource::from_source_name` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:78-85] |
| `SearchHitKind` | type | Indexed type `SearchHitKind` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:89-92] |
| `ChunkProvenance` | class | Indexed class `ChunkProvenance` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:95-100] |
| `SearchProvenance` | class | Indexed class `SearchProvenance` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:103-108] |
| `SearchSourceExplanation` | class | Indexed class `SearchSourceExplanation` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:111-115] |
| `WikiSearchResult` | class | Indexed class `WikiSearchResult` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:118-131] |
| `WikiSearchResult::fusion_key` | method | Indexed method `WikiSearchResult::fusion_key` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:134-141] |
| `normalized_path` | function | Indexed function `normalized_path` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:144-149] |
| `SearchRequest` | class | Indexed class `SearchRequest` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:152-157] |
| `WikiSearchResponse` | class | Indexed class `WikiSearchResponse` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:160-163] |
| `SearchError` | type | Indexed type `SearchError` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:166-169] |
| `SearchError::fmt` | method | Indexed method `SearchError::fmt` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:172-179] |
| `search` | function | Indexed function `search` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:186-266] |
| `graph_seed_paths` | function | Indexed function `graph_seed_paths` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:268-285] |
| `available_sources` | function | Indexed function `available_sources` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:287-300] |
| `search_source_unavailable` | function | Indexed function `search_source_unavailable` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:302-304] |
| `semantic_unavailable_degrades` | function | Indexed function `semantic_unavailable_degrades` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:311-352] |
| `graph_linked_pages_enter_search_results` | function | Indexed function `graph_linked_pages_enter_search_results` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:355-386] |
| `combined_partial_search_reports_all_unavailable_sources_once` | function | Indexed function `combined_partial_search_reports_all_unavailable_sources_once` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:389-427] |
| `search_result` | function | Indexed function `search_result` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:429-454] |
| `memory_graph` | function | Indexed function `memory_graph` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:456-475] |
| `graph_doc` | function | Indexed function `graph_doc` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:477-483] |
| `DegradedGraphBackend` | class | Indexed class `DegradedGraphBackend` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:485] |
| `DegradedGraphBackend::search_graph_boost` | method | Indexed method `DegradedGraphBackend::search_graph_boost` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:488-501] |

