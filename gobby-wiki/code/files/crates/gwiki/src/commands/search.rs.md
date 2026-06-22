---
title: crates/gwiki/src/commands/search.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/search.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/search.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/search.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/search.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SearchRetrieval` | class | 'SearchRetrieval' is a crate-visible struct that packages a 'SearchOutput' result together with a vector of string evidence snippets ('Vec<String>') supporting that result. [crates/gwiki/src/commands/search.rs:27-30] |
| `execute` | function | Executes a wiki command by calling 'retrieve(query, selection, limit, include_semantic)', propagating any 'WikiError', and then passing the returned 'output' into 'render' to produce a 'Result<CommandOutcome, WikiError>'. [crates/gwiki/src/commands/search.rs:32-39] |
| `retrieve` | function | 'retrieve' executes a wiki search for the given query and scope selection, preferring an attached database-backed search path when available and otherwise building in-memory BM25 and graph-boost backends over the indexed store before running the search with the requested limit and optional semantic scoring. [crates/gwiki/src/commands/search.rs:41-78] |
| `run_search_attached` | function | Opens a read-only PostgreSQL connection, resolves the search stack configuration from 'gobby_home' and the database to obtain semantic embedding, Qdrant, and FalkorDB settings, and returns a 'WikiError' if any required search dependency is missing or misconfigured. [crates/gwiki/src/commands/search.rs:80-143] |
| `graph_backend_from_falkor_config` | function | Returns a 'GraphBoostBackend' that uses 'FalkorGraphBoostBackend::new' when a 'FalkorConfig' is present and otherwise, or on initialization failure, falls back to an 'UnavailableGraphBoostBackend::unreachable' carrying the corresponding error message. [crates/gwiki/src/commands/search.rs:145-163] |
| `required_search_config` | function | Constructs and returns a 'WikiError::Config' whose detail message states that 'gwiki search' requires the given service and advises running 'gwiki setup --standalone' or attaching to Gobby’s full datastore stack. [crates/gwiki/src/commands/search.rs:165-171] |
| `resolve_semantic_embedding` | function | Returns an optional 'wiki_search::semantic::SemanticEmbedding' by mapping the effective AI routing mode to 'None', a daemon-backed embedding using a cloned 'AiContext' when the 'ai' feature is enabled, or a direct embedding resolved from 'source' via 'resolve_embedding_config'. [crates/gwiki/src/commands/search.rs:173-208] |
| `effective_embedding_route` | function | Returns the effective embedding routing for 'context', delegating to 'effective_route(..., AiCapability::Embed)' when the 'ai' feature is enabled, and otherwise preserving 'Off'/'Direct' while downgrading 'Daemon' to 'Off' and leaving 'Auto' unchanged with a warning. [crates/gwiki/src/commands/search.rs:210-234] |
| `gobby_home` | function | Wraps 'gobby_core::gobby_home()' and converts any resolution failure into 'WikiError::Config' with a formatted message, returning the resolved Gobby home 'PathBuf' on success. [crates/gwiki/src/commands/search.rs:236-240] |
| `SearchExecutionInput` | class | SearchExecutionInput encapsulates the configuration parameters for executing a wiki search operation, comprising the search scope, output scope, query string, result limit, and a flag to enable semantic search functionality. [crates/gwiki/src/commands/search.rs:242-248] |
| `run_search_with_backends` | function | Runs a wiki search across BM25, semantic, and graph-boost backends using the input query parameters, then converts each returned hit into 'SearchResultOutput' with derived fusion keys, bounded snippets, source/explanation mappings, evidence snippets, and degradation labels for the final 'SearchRetrieval' result. [crates/gwiki/src/commands/search.rs:250-317] |
| `bounded_snippet` | function | Returns a whitespace-normalized snippet around the query by extracting a bounded window from 'content' via 'query_window' using 'SNIPPET_BEFORE_CHARS' and 'SNIPPET_AFTER_CHARS', then collapsing all whitespace to single spaces. [crates/gwiki/src/commands/search.rs:326-329] |
| `query_window` | function | Returns a substring of 'content' centered on the earliest case-insensitive match of any non-empty whitespace-delimited token from 'query', extending 'before' characters to the left and 'after' characters to the right, clamped to the string bounds. [crates/gwiki/src/commands/search.rs:333-353] |
| `render` | function | Serializes the 'SearchOutput' to JSON, renders a human-readable search summary from its query, scope, results, and degradations, and returns both as a scoped '"search"' 'CommandOutcome', mapping serialization failures to 'WikiError::Json'. [crates/gwiki/src/commands/search.rs:355-366] |
| `render_text` | function | 'render_text' formats a plain-text search results report containing the query, scope, optional degradation notices, a '"No results"' fallback, or one '- page \| title \| snippet' line per 'SearchResultOutput', and returns it as a 'String'. [crates/gwiki/src/commands/search.rs:368-395] |

_Verified by 5 in-file unit tests._

