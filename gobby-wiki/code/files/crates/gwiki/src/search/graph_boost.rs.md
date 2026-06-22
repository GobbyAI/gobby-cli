---
title: crates/gwiki/src/search/graph_boost.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/graph_boost.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/graph_boost.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/search/graph_boost.rs` exposes 35 indexed API symbols.

## How it fits

`crates/gwiki/src/search/graph_boost.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphBoostConfig` | class | 'GraphBoostConfig' is a configuration struct that sets two 64-bit integer limits, 'document_query_limit' and 'link_query_limit', for controlling graph boost query behavior. [crates/gwiki/src/search/graph_boost.rs:21-24] |
| `GraphBoostConfig::default` | method | Returns a 'Self' instance initialized with 'document_query_limit' set to 'DEFAULT_GRAPH_BOOST_DOCUMENT_QUERY_LIMIT' and 'link_query_limit' set to 'DEFAULT_GRAPH_BOOST_LINK_QUERY_LIMIT'. [crates/gwiki/src/search/graph_boost.rs:27-32] |
| `GraphBoostRequest` | class | 'GraphBoostRequest' is a request struct that carries a 'SearchScope', a list of seed file-system paths ('Vec<PathBuf>'), and a 'limit' count for constraining a graph-boosting operation. [crates/gwiki/src/search/graph_boost.rs:35-39] |
| `GraphBoostOutcome` | class | 'GraphBoostOutcome' is a result struct containing a vector of 'WikiSearchResult' hits and an optional 'DegradationKind' indicating whether boosting degraded. [crates/gwiki/src/search/graph_boost.rs:41-44] |
| `GraphBoostBackend` | type | Indexed type `GraphBoostBackend` in `crates/gwiki/src/search/graph_boost.rs`. [crates/gwiki/src/search/graph_boost.rs:46-51] |
| `NoopGraphBoostBackend` | class | 'NoopGraphBoostBackend' is a zero-sized Rust struct that serves as a no-op implementation placeholder for a graph-boost backend. [crates/gwiki/src/search/graph_boost.rs:54] |
| `NoopGraphBoostBackend::search_graph_boost` | method | 'search_graph_boost' ignores the 'GraphBoostRequest' and always returns 'Ok(GraphBoostOutcome { hits: Vec::new(), degradation: None })', i.e. an empty, non-degraded result. [crates/gwiki/src/search/graph_boost.rs:57-65] |
| `UnavailableGraphBoostBackend` | class | 'UnavailableGraphBoostBackend' is a Rust struct that encapsulates a 'DegradationKind' value, presumably representing the fallback/degraded state for an unavailable GraphBoost backend. [crates/gwiki/src/search/graph_boost.rs:68-70] |
| `UnavailableGraphBoostBackend::unreachable` | method | Constructs and returns a 'Self' instance whose 'degradation' field is initialized from 'graph_degradation(message)'. [crates/gwiki/src/search/graph_boost.rs:73-77] |
| `UnavailableGraphBoostBackend::search_graph_boost` | method | 'search_graph_boost' ignores the incoming 'GraphBoostRequest' and returns 'Ok(GraphBoostOutcome { hits: Vec::new(), degradation: Some(self.degradation.clone()) })', i.e. an empty result set plus a cloned degradation state. [crates/gwiki/src/search/graph_boost.rs:81-89] |
| `search_graph_boost` | function | Forwards the 'GraphBoostRequest' to the inner value via dereference ('(**self).search_graph_boost(request)') and returns its 'Result<GraphBoostOutcome, SearchError>'. [crates/gwiki/src/search/graph_boost.rs:93-98] |
| `MemoryGraphBoostBackend` | class | 'MemoryGraphBoostBackend' is a backend wrapper struct that encapsulates a 'MemoryWikiGraph' instance in its 'graph' field. [crates/gwiki/src/search/graph_boost.rs:101-103] |
| `MemoryGraphBoostBackend::new` | method | Constructs and returns a new instance by moving the provided 'MemoryWikiGraph' into the struct’s 'graph' field. [crates/gwiki/src/search/graph_boost.rs:106-108] |
| `MemoryGraphBoostBackend::search_graph_boost` | method | 'search_graph_boost' queries the graph for paths related to the request’s scope and seed paths up to the given limit, then returns a 'GraphBoostOutcome' whose hits are derived from those ranked paths and whose degradation is always 'None'. [crates/gwiki/src/search/graph_boost.rs:112-123] |
| `FalkorGraphBoostBackend` | class | 'FalkorGraphBoostBackend' is a Rust backend struct that encapsulates a 'GraphClient' and a 'GraphBoostConfig' for performing graph-boosted backend operations. [crates/gwiki/src/search/graph_boost.rs:126-129] |
| `FalkorGraphBoostBackend::new` | method | Constructs a new instance by delegating to 'Self::new_with_config(config, GraphBoostConfig::default())', returning either the initialized value or a 'SearchError'. [crates/gwiki/src/search/graph_boost.rs:132-134] |
| `FalkorGraphBoostBackend::new_with_config` | method | 'new_with_config' constructs a 'GraphBoost' instance by creating a 'GraphClient' from the provided 'FalkorConfig' and the 'FALKORDB_GRAPH_NAME', mapping any connection failure into 'SearchError::Backend', and returning 'Self { client, config }' on success. [crates/gwiki/src/search/graph_boost.rs:136-145] |
| `FalkorGraphBoostBackend::search_graph_boost` | method | 'search_graph_boost' returns an empty outcome when 'limit == 0' or no 'seed_paths' are provided, otherwise it loads graph-boost data for the requested scope, degrades gracefully to an empty result with a degradation marker on load failure, ranks link neighborhoods from documents/links around the seed paths up to 'limit', and returns the corresponding graph-boost hits with any data-supplied degradation metadata. [crates/gwiki/src/search/graph_boost.rs:149-184] |
| `GraphBoostDocument` | class | A 'GraphBoostDocument' is a Rust struct that represents a document identified by a filesystem 'PathBuf' and an optional 'String' title. [crates/gwiki/src/search/graph_boost.rs:188-191] |
| `GraphBoostLink` | class | 'GraphBoostLink' is a data container for a graph-boost link that stores a source filesystem path as a 'PathBuf' and a target path as a 'String'. [crates/gwiki/src/search/graph_boost.rs:194-197] |
| `rank_link_neighborhood` | function | Returns up to 'limit' non-seed document paths ranked by accumulated relevance to the ordered 'seed_paths', scoring direct outbound neighbors of each seed by '1/(rank+1)' and inbound backlinks at '0.8x' that weight, then sorting descending by score and path. [crates/gwiki/src/search/graph_boost.rs:199-264] |
| `graph_boost_hits` | function | 'graph_boost_hits' filters 'ranked_paths' to keyword-searchable paths, truncates the stream to 'limit', converts each remaining '(PathBuf, f64)' into a 'WikiSearchResult' with 'graph_result' using the provided 'scope', and collects the results into a vector. [crates/gwiki/src/search/graph_boost.rs:266-277] |
| `graph_result` | function | Constructs a 'WikiSearchResult' for a graph-sourced document by canonicalizing the path into a 'document:' ID, cloning the provided 'SearchScope' and 'PathBuf' into provenance and source fields, marking the hit as 'Document' with 'SearchSource::Graph', and populating the result with the given 'score' and empty snippet/explanations/chunk. [crates/gwiki/src/search/graph_boost.rs:279-301] |
| `graph_degradation` | function | Constructs and returns a 'DegradationKind::ServiceUnavailable' for 'GRAPH_SERVICE', wrapping the provided 'message' in 'ServiceState::Unreachable'. [crates/gwiki/src/search/graph_boost.rs:303-308] |

_6 more symbol(s) not shown — run `gcode outline crates/gwiki/src/search/graph_boost.rs` for the full list._

_Verified by 5 in-file unit tests._

