---
title: crates/gwiki/src/falkor_graph/boost.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/boost.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph/boost.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/falkor_graph/boost.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gwiki/src/falkor_graph/boost.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `load_graph_boost_data` | function | Queries a GraphClient for documents and links within specified limits and returns a GraphBoostData struct containing the results along with degradation metadata if either limit was capped. [crates/gwiki/src/falkor_graph/boost.rs:11-35] |
| `query_documents` | function | Queries a graph database for WikiDoc nodes (optionally filtered by SearchScope), maps the results to GraphBoostDocument objects containing file paths and titles, and returns a cardinality-limited result set. [crates/gwiki/src/falkor_graph/boost.rs:37-67] |
| `query_links` | function | Executes a scoped or global Cypher query on a GraphClient to retrieve wiki document WIKI_LINKS_TO relationships, returning a limited collection of GraphBoostLink objects mapped from source and target document paths. [crates/gwiki/src/falkor_graph/boost.rs:69-104] |
| `LimitedQuery` | class | 'LimitedQuery<T>' is a generic struct that encapsulates a vector of items alongside a boolean flag indicating whether the query results were truncated or capacity-capped. [crates/gwiki/src/falkor_graph/boost.rs:106-109] |
| `query_limited` | function | Executes a graph database query with a specified limit, using a sentinel row to detect result truncation, and returns a 'LimitedQuery' containing the result set and a capped flag indicating whether results were truncated. [crates/gwiki/src/falkor_graph/boost.rs:111-138] |
| `partial_graph_degradation` | function | Conditionally returns a 'DegradationKind::PartialData' variant containing the gwiki_graph component and a formatted message listing items that exceeded configured caps, or 'None' if the input slice is empty. [crates/gwiki/src/falkor_graph/boost.rs:140-151] |

