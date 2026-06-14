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

Implements the `gwiki` search command end to end: it executes a query against either an attached database or the local indexed store, resolves the active scope and search backends, and returns both rendered results and the raw evidence used to build bounded snippets. The module also contains the helpers that choose graph/semantic embedding configuration, compute snippet and query windows, and render text output, plus tests that verify snippet bounding, multibyte handling, and graceful degradation when search backends or config are missing.
[crates/gwiki/src/commands/search.rs:27-30]
[crates/gwiki/src/commands/search.rs:32-39]
[crates/gwiki/src/commands/search.rs:41-78]
[crates/gwiki/src/commands/search.rs:80-143]
[crates/gwiki/src/commands/search.rs:145-163]

## API Symbols

- `SearchRetrieval` (class) component `SearchRetrieval [class]` (`7827022e-fc2c-5f7c-af69-84222a4ae704`) lines 27-30 [crates/gwiki/src/commands/search.rs:27-30]
  - Signature: `pub(crate) struct SearchRetrieval {`
  - Purpose: Indexed class `SearchRetrieval` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:27-30]
- `execute` (function) component `execute [function]` (`53398570-7c16-5692-bcb6-b8fd6e9d4860`) lines 32-39 [crates/gwiki/src/commands/search.rs:32-39]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:32-39]
- `retrieve` (function) component `retrieve [function]` (`5a87b1f0-54ab-5890-bfa2-6bd740f81ba2`) lines 41-78 [crates/gwiki/src/commands/search.rs:41-78]
  - Signature: `pub(crate) fn retrieve(`
  - Purpose: Indexed function `retrieve` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:41-78]
- `run_search_attached` (function) component `run_search_attached [function]` (`070eb4f5-ea2c-51b8-84ce-02f81627b736`) lines 80-143 [crates/gwiki/src/commands/search.rs:80-143]
  - Signature: `fn run_search_attached(`
  - Purpose: Indexed function `run_search_attached` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:80-143]
- `graph_backend_from_falkor_config` (function) component `graph_backend_from_falkor_config [function]` (`e6235d82-80a4-5ec7-8bc1-7f802ee05a9b`) lines 145-163 [crates/gwiki/src/commands/search.rs:145-163]
  - Signature: `fn graph_backend_from_falkor_config(`
  - Purpose: Indexed function `graph_backend_from_falkor_config` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:145-163]
- `required_search_config` (function) component `required_search_config [function]` (`c6e5cf0a-22d4-516e-aafb-098525a544f2`) lines 165-171 [crates/gwiki/src/commands/search.rs:165-171]
  - Signature: `fn required_search_config(service: &'static str) -> WikiError {`
  - Purpose: Indexed function `required_search_config` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:165-171]
- `resolve_semantic_embedding` (function) component `resolve_semantic_embedding [function]` (`1d60d254-ff75-5230-8498-90ed128697c9`) lines 173-208 [crates/gwiki/src/commands/search.rs:173-208]
  - Signature: `fn resolve_semantic_embedding(`
  - Purpose: Indexed function `resolve_semantic_embedding` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:173-208]
- `effective_embedding_route` (function) component `effective_embedding_route [function]` (`c5f3012d-7fad-5f42-8f48-4677cb20861f`) lines 210-234 [crates/gwiki/src/commands/search.rs:210-234]
  - Signature: `fn effective_embedding_route(context: &AiContext) -> AiRouting {`
  - Purpose: Indexed function `effective_embedding_route` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:210-234]
- `gobby_home` (function) component `gobby_home [function]` (`4e165778-be8b-52dd-a920-3a0ad80950f1`) lines 236-240 [crates/gwiki/src/commands/search.rs:236-240]
  - Signature: `fn gobby_home() -> Result<std::path::PathBuf, WikiError> {`
  - Purpose: Indexed function `gobby_home` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:236-240]
- `SearchExecutionInput` (class) component `SearchExecutionInput [class]` (`560becd1-c5d0-52f7-90b6-ea0356af3fbe`) lines 242-248 [crates/gwiki/src/commands/search.rs:242-248]
  - Signature: `struct SearchExecutionInput {`
  - Purpose: Indexed class `SearchExecutionInput` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:242-248]
- `run_search_with_backends` (function) component `run_search_with_backends [function]` (`2d257661-3897-5002-9e2e-b72190f1030e`) lines 250-317 [crates/gwiki/src/commands/search.rs:250-317]
  - Signature: `fn run_search_with_backends<B, S, G>(`
  - Purpose: Indexed function `run_search_with_backends` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:250-317]
- `bounded_snippet` (function) component `bounded_snippet [function]` (`c97eb4ec-4927-5a30-a4e2-4a543b89bf5c`) lines 326-329 [crates/gwiki/src/commands/search.rs:326-329]
  - Signature: `fn bounded_snippet(content: &str, query: &str) -> String {`
  - Purpose: Indexed function `bounded_snippet` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:326-329]
- `query_window` (function) component `query_window [function]` (`e3a44454-a132-5ee0-ad8d-f505c1c171c2`) lines 333-353 [crates/gwiki/src/commands/search.rs:333-353]
  - Signature: `pub(crate) fn query_window(content: &str, query: &str, before: usize, after: usize) -> String {`
  - Purpose: Indexed function `query_window` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:333-353]
- `render` (function) component `render [function]` (`9a2977a4-8878-5b1c-a776-278326e4b274`) lines 355-366 [crates/gwiki/src/commands/search.rs:355-366]
  - Signature: `fn render(output: SearchOutput) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Indexed function `render` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:355-366]
- `render_text` (function) component `render_text [function]` (`561211da-50c7-5a25-8e20-e65fa5d278e5`) lines 368-395 [crates/gwiki/src/commands/search.rs:368-395]
  - Signature: `fn render_text(`
  - Purpose: Indexed function `render_text` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:368-395]
- `qdrant_config_requires_non_blank_url` (function) component `qdrant_config_requires_non_blank_url [function]` (`3ecfdd19-6f21-52e1-8fcc-3818c5198f59`) lines 402-415 [crates/gwiki/src/commands/search.rs:402-415]
  - Signature: `fn qdrant_config_requires_non_blank_url() {`
  - Purpose: Indexed function `qdrant_config_requires_non_blank_url` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:402-415]
- `missing_falkor_config_degrades_graph_search` (function) component `missing_falkor_config_degrades_graph_search [function]` (`1d46a60d-54ed-5e4a-9af3-388121faa9a0`) lines 418-435 [crates/gwiki/src/commands/search.rs:418-435]
  - Signature: `fn missing_falkor_config_degrades_graph_search() {`
  - Purpose: Indexed function `missing_falkor_config_degrades_graph_search` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:418-435]
- `bounded_snippet_windows_around_first_query_token` (function) component `bounded_snippet_windows_around_first_query_token [function]` (`2846defe-17bb-54d9-9157-1a8ac26a2793`) lines 438-448 [crates/gwiki/src/commands/search.rs:438-448]
  - Signature: `fn bounded_snippet_windows_around_first_query_token() {`
  - Purpose: Indexed function `bounded_snippet_windows_around_first_query_token` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:438-448]
- `bounded_snippet_never_emits_full_document_body` (function) component `bounded_snippet_never_emits_full_document_body [function]` (`3b586ce2-616e-586f-be7d-da060e284a9a`) lines 451-457 [crates/gwiki/src/commands/search.rs:451-457]
  - Signature: `fn bounded_snippet_never_emits_full_document_body() {`
  - Purpose: Indexed function `bounded_snippet_never_emits_full_document_body` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:451-457]
- `query_window_handles_multibyte_content` (function) component `query_window_handles_multibyte_content [function]` (`7f3ed55b-b5a1-5f46-8e0d-16acc2b2f4a3`) lines 460-466 [crates/gwiki/src/commands/search.rs:460-466]
  - Signature: `fn query_window_handles_multibyte_content() {`
  - Purpose: Indexed function `query_window_handles_multibyte_content` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:460-466]

