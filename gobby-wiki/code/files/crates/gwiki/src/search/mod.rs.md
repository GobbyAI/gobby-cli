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

`crates/gwiki/src/search/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SearchScope` | type | Indexed type `SearchScope` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:14-18] |
| `SearchScope::global` | method | Returns the 'Self::Global' enum variant, constructing a global instance of the type. [crates/gwiki/src/search/mod.rs:21-23] |
| `SearchScope::project` | method | Constructs and returns a 'Self::Project' variant by converting the provided 'project_id' into a 'String' and storing it in the 'project_id' field. [crates/gwiki/src/search/mod.rs:25-29] |
| `SearchScope::topic` | method | Constructs and returns a 'Self::Topic' variant by converting the provided 'topic' argument into a 'String' and storing it in the 'topic' field. [crates/gwiki/src/search/mod.rs:31-35] |
| `SearchScope::scope_kind` | method | Returns the static string identifier for the enum variant’s scope, mapping 'Global' to '"global"', 'Project' to '"project"', and 'Topic' to '"topic"'. [crates/gwiki/src/search/mod.rs:37-43] |
| `SearchScope::scope_value` | method | Returns the string slice associated with the enum variant, yielding '""' for 'Global', the 'project_id' for 'Project', and the 'topic' for 'Topic'. [crates/gwiki/src/search/mod.rs:45-51] |
| `SearchScope::scope_filter` | method | Returns 'None' for 'Global', and otherwise maps 'Project { project_id }' to 'Some(("project", project_id))' and 'Topic { topic }' to 'Some(("topic", topic))', exposing the scope kind as a static string plus its identifier. [crates/gwiki/src/search/mod.rs:53-59] |
| `SearchSource` | type | Indexed type `SearchSource` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:63-67] |
| `SearchSource::as_str` | method | Returns the canonical static string identifier for the enum variant, mapping 'Bm25' to '"bm25"', 'Graph' to '"graph"', and 'Semantic' to '"semantic"'. [crates/gwiki/src/search/mod.rs:70-76] |
| `SearchSource::from_source_name` | method | Returns 'Some(Self::Bm25)', 'Some(Self::Graph)', or 'Some(Self::Semantic)' when 'source' is exactly '"bm25"', '"graph"', or '"semantic"' respectively, and 'None' for any other string. [crates/gwiki/src/search/mod.rs:78-85] |
| `SearchHitKind` | type | Indexed type `SearchHitKind` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:89-92] |
| `ChunkProvenance` | class | 'ChunkProvenance' is a record type that identifies a chunk by its zero-based 'chunk_index', byte range '[byte_start, byte_end)', and optional associated 'heading' text. [crates/gwiki/src/search/mod.rs:95-100] |
| `SearchProvenance` | class | 'SearchProvenance' stores provenance metadata for a search result, including the document path, original source path, source kind identifier, and an optional content hash. [crates/gwiki/src/search/mod.rs:103-108] |
| `SearchSourceExplanation` | class | 'SearchSourceExplanation' is a struct that pairs a 'SearchSource' with its ranking position and numeric relevance score. [crates/gwiki/src/search/mod.rs:111-115] |
| `WikiSearchResult` | class | 'WikiSearchResult' is a search-result record that identifies a wiki hit by 'id' and optional 'title', captures its location and origin via 'path', 'source_path', 'scope', 'hit_kind', 'chunk', and 'provenance', and includes ranking and retrieval metadata such as 'snippet', 'score', 'sources', and 'explanations'. [crates/gwiki/src/search/mod.rs:118-131] |
| `WikiSearchResult::fusion_key` | method | Returns a 'String' fusion key by concatenating the scope kind, scope value, and normalized path with ':' separators, propagating any 'SearchError' from path normalization. [crates/gwiki/src/search/mod.rs:134-141] |
| `normalized_path` | function | Converts a 'Path' to a UTF-8 'String', returning 'SearchError::InvalidPath' if it is not valid Unicode, and normalizes path separators by replacing backslashes with forward slashes. [crates/gwiki/src/search/mod.rs:144-149] |
| `SearchRequest` | class | 'SearchRequest' is a request payload that specifies a search 'query', the 'scope' to search within, a result 'limit', and whether to 'include_semantic' matching. [crates/gwiki/src/search/mod.rs:152-157] |
| `WikiSearchResponse` | class | 'WikiSearchResponse' is a response struct containing a list of 'WikiSearchResult' entries and a list of 'DegradationKind' values indicating any degradations encountered. [crates/gwiki/src/search/mod.rs:160-163] |
| `SearchError` | type | Indexed type `SearchError` in `crates/gwiki/src/search/mod.rs`. [crates/gwiki/src/search/mod.rs:166-169] |
| `SearchError::fmt` | method | Implements 'Display' formatting for the error type by rendering either 'wiki search backend failed: {message}' for 'Backend' variants or 'search result path is not valid UTF-8: {path:?}' for 'InvalidPath' variants. [crates/gwiki/src/search/mod.rs:172-179] |
| `search` | function | Performs a hybrid wiki search by running BM25 retrieval, optionally semantic search, seeding graph-boost search from those hits, and aggregating the resulting hits plus any degradation/unavailability signals into a 'WikiSearchResponse'. [crates/gwiki/src/search/mod.rs:186-266] |
| `graph_seed_paths` | function | 'graph_seed_paths' merges 'bm25_hits' and 'semantic_hits' in order, deduplicates by each hit’s 'provenance.document_path' using a 'HashSet', and returns the first 'limit' unique 'PathBuf's. [crates/gwiki/src/search/mod.rs:268-285] |
| `available_sources` | function | Returns a 'Vec<String>' containing '"Bm25"' always, adds '"Graph"' when 'graph_unavailable' is false, and adds '"Semantic"' only when 'include_semantic' is true and 'semantic_unavailable' is false. [crates/gwiki/src/search/mod.rs:287-300] |

_6 more symbol(s) not shown — run `gcode outline crates/gwiki/src/search/mod.rs` for the full list._

_Verified by 3 in-file unit tests._

