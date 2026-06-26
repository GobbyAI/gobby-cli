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

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

`crates/gwiki/src/commands/search.rs` exposes 24 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/search.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SearchRetrieval` | class | SearchRetrieval is a crate-private struct that encapsulates a SearchOutput result alongside a vector of string-based evidence. [crates/gwiki/src/commands/search.rs:28-31] |
| `execute` | function | Retrieves wiki query results according to specified scope, limit, and semantic parameters, then renders the output to a 'CommandOutcome' or propagates a 'WikiError'. [crates/gwiki/src/commands/search.rs:36-44] |
| `retrieve` | function | Executes a combined BM25 and graph-boost search on a scoped wiki index, either via an attached database or in-memory store, returning up to 'limit' ranked results. [crates/gwiki/src/commands/search.rs:46-86] |
| `run_search_attached` | function | **Executes a scoped wiki search query by establishing a PostgreSQL connection and resolving required semantic embedding (Qdrant) and graph database (FalkorDB) configurations.** [crates/gwiki/src/commands/search.rs:88-153] |
| `graph_backend_from_falkor_config` | function | Constructs and returns a boxed 'GraphBoostBackend' trait object by attempting to instantiate a 'FalkorGraphBoostBackend' from the provided optional configuration, or falling back to an 'UnavailableGraphBoostBackend' if the configuration is absent or initialization fails. [crates/gwiki/src/commands/search.rs:155-173] |
| `required_search_config` | function | Constructs and returns a 'WikiError::Config' variant indicating that a required search service configuration is missing for gwiki search operation. [crates/gwiki/src/commands/search.rs:175-181] |
| `resolve_semantic_embedding` | function | Resolves an optional semantic embedding by selecting between daemon-backed, config-sourced direct, or null implementations based on the effective AI routing strategy and feature flags. [crates/gwiki/src/commands/search.rs:183-218] |
| `effective_embedding_route` | function | # Summary 'effective_embedding_route' determines the effective routing mode for embedding operations by delegating to 'effective_route' when AI support is compiled in, or by gracefully degrading unsupported daemon routing configurations to 'Off' with fallback handling when AI support is unavailable. [crates/gwiki/src/commands/search.rs:220-244] |
| `gobby_home` | function | Resolves the Gobby home directory path by delegating to 'gobby_core::gobby_home()', converting any errors into a 'WikiError::Config' variant with a contextual error message for gwiki search configuration. [crates/gwiki/src/commands/search.rs:246-250] |
| `SearchExecutionInput` | class | SearchExecutionInput is a struct that encapsulates the configuration parameters for executing a scoped wiki search, including query text, result limit, output scope, search scope, semantic search enablement, and optional token budget constraints. [crates/gwiki/src/commands/search.rs:252-259] |
| `run_search_with_backends` | function | Executes a federated search across three backends (BM25, semantic, and graph-boost), then transforms the aggregated results into structured 'SearchResultOutput' objects with bounded snippets, fusion keys, and per-source rank explanations. [crates/gwiki/src/commands/search.rs:261-337] |
| `format_search_result_line` | function | This function formats a 'SearchResultOutput' into a pipe-delimited string containing the wiki page name, optional title (defaulting to empty string if absent), and snippet text. [crates/gwiki/src/commands/search.rs:342-349] |
| `bounded_snippet` | function | 'bounded_snippet' extracts a bounded text snippet around a query match and normalizes internal whitespace by collapsing it to single spaces. [crates/gwiki/src/commands/search.rs:358-361] |
| `query_window` | function | Extracts a context window from content centered around the character position of the earliest-found whitespace-separated query token (using case-insensitive matching), spanning 'before' characters backward and 'after' characters forward from the match start. [crates/gwiki/src/commands/search.rs:365-385] |
| `render` | function | Renders text from a SearchOutput and serializes it to JSON payload, returning a scoped CommandOutcome or a WikiError if JSON serialization fails. [crates/gwiki/src/commands/search.rs:387-398] |
| `render_text` | function | Concatenates a search query, scope identity, optional degradations, and search result metadata (wiki pages, titles, snippets) into a single formatted text string. [crates/gwiki/src/commands/search.rs:400-427] |
| `sample_hit` | function | Constructs a 'SearchResultOutput' struct representing a wiki search result from the provided page and snippet parameters, with a hardcoded score of 1.0 and BM25 source attribution. [crates/gwiki/src/commands/search.rs:500-512] |

_Verified by 7 in-file unit tests._

