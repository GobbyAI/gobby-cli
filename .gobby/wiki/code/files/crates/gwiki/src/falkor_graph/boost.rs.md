---
title: crates/gwiki/src/falkor_graph/boost.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/boost.rs
  ranges:
  - 11-35
  - 37-67
  - 69-104
  - 106-109
  - 111-138
  - 140-151
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph/boost.rs

Module: [[code/modules/crates/gwiki/src/falkor_graph|crates/gwiki/src/falkor_graph]]

## Purpose

This file loads FalkorDB-backed graph boost data for wiki search. `load_graph_boost_data` coordinates two scoped queries, one for documents and one for links, then collects any truncation into a partial-data degradation warning and returns a `GraphBoostData` bundle. `query_documents` and `query_links` build the appropriate global or scope-filtered Cypher queries, fetch rows through `query_limited`, and convert them into typed graph boost records. `query_limited` implements the shared limit-plus-sentinel pattern so capped results can be detected, while `LimitedQuery` carries both the items and the capped flag. `partial_graph_degradation` turns any capped document/link results into a `PartialData` degradation entry for `gwiki_graph`.
[crates/gwiki/src/falkor_graph/boost.rs:11-35]
[crates/gwiki/src/falkor_graph/boost.rs:37-67]
[crates/gwiki/src/falkor_graph/boost.rs:69-104]
[crates/gwiki/src/falkor_graph/boost.rs:106-109]
[crates/gwiki/src/falkor_graph/boost.rs:111-138]

## API Symbols

- `load_graph_boost_data` (function) component `load_graph_boost_data [function]` (`2432f054-ea66-5f38-8d6f-5043dbb8d5a0`) lines 11-35 [crates/gwiki/src/falkor_graph/boost.rs:11-35]
  - Signature: `pub(crate) fn load_graph_boost_data(`
  - Purpose: Loads document and link boost data from a graph client for the given search scope with separate limits, records any truncation as a degradation warning, and returns the assembled 'GraphBoostData' or a 'SearchError'. [crates/gwiki/src/falkor_graph/boost.rs:11-35]
- `query_documents` (function) component `query_documents [function]` (`c464cc10-9b4b-5176-9f42-1704c006adcd`) lines 37-67 [crates/gwiki/src/falkor_graph/boost.rs:37-67]
  - Signature: `fn query_documents(`
  - Purpose: 'query_documents' runs a scoped Cypher query against the graph to fetch 'WikiDoc' paths and optional titles up to a caller-supplied limit, converts each row into a 'GraphBoostDocument', and returns them with the query's capped status. [crates/gwiki/src/falkor_graph/boost.rs:37-67]
- `query_links` (function) component `query_links [function]` (`de740b87-92a9-5100-a3b7-083e6647e1ea`) lines 69-104 [crates/gwiki/src/falkor_graph/boost.rs:69-104]
  - Signature: `fn query_links(`
  - Purpose: 'query_links' runs a scoped or global Cypher query to fetch ordered 'WikiDoc' 'WIKI_LINKS_TO' edges up to 'limit', converts each row into 'GraphBoostLink' values with 'source_path' and 'target_path', and returns them wrapped in 'LimitedQuery' with the original 'capped' flag. [crates/gwiki/src/falkor_graph/boost.rs:69-104]
- `LimitedQuery` (class) component `LimitedQuery [class]` (`257581d4-45e1-5496-83d6-f17d4fb2407f`) lines 106-109 [crates/gwiki/src/falkor_graph/boost.rs:106-109]
  - Signature: `struct LimitedQuery<T> {`
  - Purpose: 'LimitedQuery<T>' is a generic container that stores a 'Vec<T>' of 'items' together with a 'capped' flag indicating whether the query results were truncated by a limit. [crates/gwiki/src/falkor_graph/boost.rs:106-109]
- `query_limited` (function) component `query_limited [function]` (`20090afd-3d58-54f5-819e-7b5211a470e9`) lines 111-138 [crates/gwiki/src/falkor_graph/boost.rs:111-138]
  - Signature: `fn query_limited(`
  - Purpose: Executes a graph query with 'LIMIT max(limit, 0) + 1' to fetch one sentinel row for truncation detection, truncates any excess row before returning, and reports whether the result was capped via 'LimitedQuery<Row>'. [crates/gwiki/src/falkor_graph/boost.rs:111-138]
- `partial_graph_degradation` (function) component `partial_graph_degradation [function]` (`4ef2cfae-3fc1-53fe-a1b1-526ee7a8bf0d`) lines 140-151 [crates/gwiki/src/falkor_graph/boost.rs:140-151]
  - Signature: `pub(super) fn partial_graph_degradation(capped: &[String]) -> Option<DegradationKind> {`
  - Purpose: Returns 'None' when no graph components were capped, otherwise constructs 'Some(DegradationKind::PartialData)' for '"gwiki_graph"' with a message listing the capped items and indicating the graph boost used capped data. [crates/gwiki/src/falkor_graph/boost.rs:140-151]

