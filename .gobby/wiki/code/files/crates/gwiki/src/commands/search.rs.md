---
title: crates/gwiki/src/commands/search.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/search.rs
  ranges:
  - 27-30
  - 32-39
  - 41-78
  - 80-143
  - 145-163
  - 165-171
  - 173-208
  - 210-234
  - 236-240
  - 242-248
  - 250-317
  - 326-329
  - 333-353
  - 355-366
  - 368-395
  - 402-415
  - 418-435
  - 438-448
  - 451-457
  - 460-466
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/search.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `gwiki search` command end to end: it resolves the active scope and backend configuration, runs search either against an attached PostgreSQL-backed datastore or against local indexed-store backends, and then renders the results into a command outcome. The file also defines the retrieval container that keeps raw evidence alongside bounded search output, plus helpers for resolving embeddings, Falkor/Qdrant config, graph-boost fallback behavior, and snippet/window extraction so results stay concise and degradations are surfaced cleanly.
[crates/gwiki/src/commands/search.rs:27-30]
[crates/gwiki/src/commands/search.rs:32-39]
[crates/gwiki/src/commands/search.rs:41-78]
[crates/gwiki/src/commands/search.rs:80-143]
[crates/gwiki/src/commands/search.rs:145-163]

## API Symbols

- `SearchRetrieval` (class) component `SearchRetrieval [class]` (`7827022e-fc2c-5f7c-af69-84222a4ae704`) lines 27-30 [crates/gwiki/src/commands/search.rs:27-30]
  - Signature: `pub(crate) struct SearchRetrieval {`
  - Purpose: 'SearchRetrieval' is an internal struct that bundles a 'SearchOutput' result with a vector of string evidence supporting that retrieval. [crates/gwiki/src/commands/search.rs:27-30]
- `execute` (function) component `execute [function]` (`53398570-7c16-5692-bcb6-b8fd6e9d4860`) lines 32-39 [crates/gwiki/src/commands/search.rs:32-39]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Calls 'retrieve' with the provided 'query', 'selection', 'limit', and 'include_semantic' flag, then renders the returned 'output' into a 'CommandOutcome', propagating any 'WikiError'. [crates/gwiki/src/commands/search.rs:32-39]
- `retrieve` (function) component `retrieve [function]` (`5a87b1f0-54ab-5890-bfa2-6bd740f81ba2`) lines 41-78 [crates/gwiki/src/commands/search.rs:41-78]
  - Signature: `pub(crate) fn retrieve(`
  - Purpose: Retrieves wiki search results by routing to an attached database-backed search when available, otherwise building BM25, unavailable semantic, and memory-graph boost backends from the indexed store and executing a scoped search with the provided query, limit, and semantic flag. [crates/gwiki/src/commands/search.rs:41-78]
- `run_search_attached` (function) component `run_search_attached [function]` (`070eb4f5-ea2c-51b8-84ce-02f81627b736`) lines 80-143 [crates/gwiki/src/commands/search.rs:80-143]
  - Signature: `fn run_search_attached(`
  - Purpose: Opens a read-only PostgreSQL connection, resolves semantic embedding/Qdrant/FalkorDB configuration from 'gobby_home' and the database-backed config source, enforces required embedding and Qdrant settings, and returns a 'SearchRetrieval' or 'WikiError'. [crates/gwiki/src/commands/search.rs:80-143]
- `graph_backend_from_falkor_config` (function) component `graph_backend_from_falkor_config [function]` (`e6235d82-80a4-5ec7-8bc1-7f802ee05a9b`) lines 145-163 [crates/gwiki/src/commands/search.rs:145-163]
  - Signature: `fn graph_backend_from_falkor_config(`
  - Purpose: Returns a 'GraphBoostBackend' that either constructs a 'FalkorGraphBoostBackend' from the provided 'FalkorConfig' or falls back to an 'UnavailableGraphBoostBackend' with an explanatory error message when the config is missing or backend initialization fails. [crates/gwiki/src/commands/search.rs:145-163]
- `required_search_config` (function) component `required_search_config [function]` (`c6e5cf0a-22d4-516e-aafb-098525a544f2`) lines 165-171 [crates/gwiki/src/commands/search.rs:165-171]
  - Signature: `fn required_search_config(service: &'static str) -> WikiError {`
  - Purpose: Constructs a 'WikiError::Config' whose 'detail' explains that 'gwiki search' requires the specified 'service' and instructs the caller to run 'gwiki setup --standalone' or attach to Gobby’s full datastore stack. [crates/gwiki/src/commands/search.rs:165-171]
- `resolve_semantic_embedding` (function) component `resolve_semantic_embedding [function]` (`1d60d254-ff75-5230-8498-90ed128697c9`) lines 173-208 [crates/gwiki/src/commands/search.rs:173-208]
  - Signature: `fn resolve_semantic_embedding(`
  - Purpose: 'resolve_semantic_embedding' selects and constructs an optional 'wiki_search::semantic::SemanticEmbedding' from the AI routing mode, returning 'None' when embeddings are off or unavailable and otherwise using either a daemon-backed embedding from a cloned 'AiContext' or a direct embedding resolved from the config source. [crates/gwiki/src/commands/search.rs:173-208]
- `effective_embedding_route` (function) component `effective_embedding_route [function]` (`c5f3012d-7fad-5f42-8f48-4677cb20861f`) lines 210-234 [crates/gwiki/src/commands/search.rs:210-234]
  - Signature: `fn effective_embedding_route(context: &AiContext) -> AiRouting {`
  - Purpose: Returns the embedding routing for 'AiCapability::Embed', delegating to 'effective_route' when the 'ai' feature is enabled, and otherwise preserving 'Off'/'Direct' while warning and downgrading 'Daemon' to 'Off' and leaving 'Auto' unchanged. [crates/gwiki/src/commands/search.rs:210-234]
- `gobby_home` (function) component `gobby_home [function]` (`4e165778-be8b-52dd-a920-3a0ad80950f1`) lines 236-240 [crates/gwiki/src/commands/search.rs:236-240]
  - Signature: `fn gobby_home() -> Result<std::path::PathBuf, WikiError> {`
  - Purpose: Wraps 'gobby_core::gobby_home()' and converts any resolution error into 'WikiError::Config' with the detail 'failed to resolve Gobby home for gwiki search config: {error}'. [crates/gwiki/src/commands/search.rs:236-240]
- `SearchExecutionInput` (class) component `SearchExecutionInput [class]` (`560becd1-c5d0-52f7-90b6-ea0356af3fbe`) lines 242-248 [crates/gwiki/src/commands/search.rs:242-248]
  - Signature: `struct SearchExecutionInput {`
  - Purpose: 'SearchExecutionInput' is a data container for executing a search, bundling the output scope, search scope, query string, result limit, and a flag controlling whether semantic search is included. [crates/gwiki/src/commands/search.rs:242-248]
- `run_search_with_backends` (function) component `run_search_with_backends [function]` (`2d257661-3897-5002-9e2e-b72190f1030e`) lines 250-317 [crates/gwiki/src/commands/search.rs:250-317]
  - Signature: `fn run_search_with_backends<B, S, G>(`
  - Purpose: Runs a wiki search across BM25, semantic, and graph-boost backends using the provided query/scope/limit settings, then converts the search response into a 'SearchRetrieval' with bounded snippets, normalized result metadata, collected source explanations, raw evidence snippets, and labeled degradation indicators. [crates/gwiki/src/commands/search.rs:250-317]
- `bounded_snippet` (function) component `bounded_snippet [function]` (`c97eb4ec-4927-5a30-a4e2-4a543b89bf5c`) lines 326-329 [crates/gwiki/src/commands/search.rs:326-329]
  - Signature: `fn bounded_snippet(content: &str, query: &str) -> String {`
  - Purpose: Returns a whitespace-normalized snippet of 'content' centered around 'query' by extracting a bounded window with 'query_window' using 'SNIPPET_BEFORE_CHARS' and 'SNIPPET_AFTER_CHARS'. [crates/gwiki/src/commands/search.rs:326-329]
- `query_window` (function) component `query_window [function]` (`e3a44454-a132-5ee0-ad8d-f505c1c171c2`) lines 333-353 [crates/gwiki/src/commands/search.rs:333-353]
  - Signature: `pub(crate) fn query_window(content: &str, query: &str, before: usize, after: usize) -> String {`
  - Purpose: Returns a substring of 'content' centered on the earliest case-insensitive occurrence of any non-empty whitespace-delimited token from 'query', expanding by up to 'before' characters before and 'after' characters after that match using character-count indices and clamped to the string bounds. [crates/gwiki/src/commands/search.rs:333-353]
- `render` (function) component `render [function]` (`9a2977a4-8878-5b1c-a776-278326e4b274`) lines 355-366 [crates/gwiki/src/commands/search.rs:355-366]
  - Signature: `fn render(output: SearchOutput) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Serializes the 'SearchOutput' to JSON, renders a text summary from its query, scope, results, and degradations, and returns a scoped 'CommandOutcome' for the '"search"' command or a 'WikiError::Json' if serialization fails. [crates/gwiki/src/commands/search.rs:355-366]
- `render_text` (function) component `render_text [function]` (`561211da-50c7-5a25-8e20-e65fa5d278e5`) lines 368-395 [crates/gwiki/src/commands/search.rs:368-395]
  - Signature: `fn render_text(`
  - Purpose: Formats a human-readable search-results string that includes the query, scope, optional degradation notices, a “No results” fallback, and one line per result with page identifier, optional title, and snippet. [crates/gwiki/src/commands/search.rs:368-395]
- `qdrant_config_requires_non_blank_url` (function) component `qdrant_config_requires_non_blank_url [function]` (`3ecfdd19-6f21-52e1-8fcc-3818c5198f59`) lines 402-415 [crates/gwiki/src/commands/search.rs:402-415]
  - Signature: `fn qdrant_config_requires_non_blank_url() {`
  - Purpose: Verifies that 'qdrant_config_has_url' returns 'false' when 'QdrantConfig.url' is 'None' or whitespace-only, and 'true' when it contains a non-blank URL string. [crates/gwiki/src/commands/search.rs:402-415]
- `missing_falkor_config_degrades_graph_search` (function) component `missing_falkor_config_degrades_graph_search [function]` (`1d46a60d-54ed-5e4a-9af3-388121faa9a0`) lines 418-435 [crates/gwiki/src/commands/search.rs:418-435]
  - Signature: `fn missing_falkor_config_degrades_graph_search() {`
  - Purpose: Verifies that when FalkorDB configuration is absent, 'search_graph_boost' succeeds in degraded mode by returning no hits and a 'gwiki_graph_unreachable' degradation containing the message that FalkorDB-required infrastructure is not configured. [crates/gwiki/src/commands/search.rs:418-435]
- `bounded_snippet_windows_around_first_query_token` (function) component `bounded_snippet_windows_around_first_query_token [function]` (`2846defe-17bb-54d9-9157-1a8ac26a2793`) lines 438-448 [crates/gwiki/src/commands/search.rs:438-448]
  - Signature: `fn bounded_snippet_windows_around_first_query_token() {`
  - Purpose: It asserts that 'bounded_snippet' extracts a bounded substring around the first query token in a long body, preserves the matched text ('enqueues'), and does not exceed 'SNIPPET_BEFORE_CHARS + SNIPPET_AFTER_CHARS' characters. [crates/gwiki/src/commands/search.rs:438-448]
- `bounded_snippet_never_emits_full_document_body` (function) component `bounded_snippet_never_emits_full_document_body [function]` (`3b586ce2-616e-586f-be7d-da060e284a9a`) lines 451-457 [crates/gwiki/src/commands/search.rs:451-457]
  - Signature: `fn bounded_snippet_never_emits_full_document_body() {`
  - Purpose: Verifies that 'bounded_snippet' does not return the full body for a large non-matching document, instead producing a snippet whose character count stays within 'SNIPPET_BEFORE_CHARS + SNIPPET_AFTER_CHARS' and begins with the document prefix. [crates/gwiki/src/commands/search.rs:451-457]
- `query_window_handles_multibyte_content` (function) component `query_window_handles_multibyte_content [function]` (`7f3ed55b-b5a1-5f46-8e0d-16acc2b2f4a3`) lines 460-466 [crates/gwiki/src/commands/search.rs:460-466]
  - Signature: `fn query_window_handles_multibyte_content() {`
  - Purpose: Verifies that 'query_window' returns a bounded character window around the multibyte substring '"enqueue"' in a long UTF-8 string, preserving the match and keeping the result at most 30 characters. [crates/gwiki/src/commands/search.rs:460-466]

