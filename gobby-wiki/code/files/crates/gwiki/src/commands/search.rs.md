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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/search.rs:27-30](crates/gwiki/src/commands/search.rs#L27-L30), [crates/gwiki/src/commands/search.rs:32-39](crates/gwiki/src/commands/search.rs#L32-L39), [crates/gwiki/src/commands/search.rs:41-78](crates/gwiki/src/commands/search.rs#L41-L78), [crates/gwiki/src/commands/search.rs:80-143](crates/gwiki/src/commands/search.rs#L80-L143), [crates/gwiki/src/commands/search.rs:145-163](crates/gwiki/src/commands/search.rs#L145-L163), [crates/gwiki/src/commands/search.rs:165-171](crates/gwiki/src/commands/search.rs#L165-L171), [crates/gwiki/src/commands/search.rs:173-208](crates/gwiki/src/commands/search.rs#L173-L208), [crates/gwiki/src/commands/search.rs:210-234](crates/gwiki/src/commands/search.rs#L210-L234), [crates/gwiki/src/commands/search.rs:236-240](crates/gwiki/src/commands/search.rs#L236-L240), [crates/gwiki/src/commands/search.rs:242-248](crates/gwiki/src/commands/search.rs#L242-L248), [crates/gwiki/src/commands/search.rs:250-317](crates/gwiki/src/commands/search.rs#L250-L317), [crates/gwiki/src/commands/search.rs:326-329](crates/gwiki/src/commands/search.rs#L326-L329), [crates/gwiki/src/commands/search.rs:333-353](crates/gwiki/src/commands/search.rs#L333-L353), [crates/gwiki/src/commands/search.rs:355-366](crates/gwiki/src/commands/search.rs#L355-L366), [crates/gwiki/src/commands/search.rs:368-395](crates/gwiki/src/commands/search.rs#L368-L395), [crates/gwiki/src/commands/search.rs:402-415](crates/gwiki/src/commands/search.rs#L402-L415), [crates/gwiki/src/commands/search.rs:418-435](crates/gwiki/src/commands/search.rs#L418-L435), [crates/gwiki/src/commands/search.rs:438-448](crates/gwiki/src/commands/search.rs#L438-L448), [crates/gwiki/src/commands/search.rs:451-457](crates/gwiki/src/commands/search.rs#L451-L457), [crates/gwiki/src/commands/search.rs:460-466](crates/gwiki/src/commands/search.rs#L460-L466)

</details>

# crates/gwiki/src/commands/search.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `gwiki search` command end to end: it resolves the requested scope, chooses between an attached database search path and an in-memory indexed-store path, and returns both rendered search output and the raw evidence used to build snippets. The helper functions assemble the active backends, resolve embedding and graph configuration, enforce required search settings, and produce bounded text windows/snippets so results stay compact; the render functions then format those results as command output. The file also includes tests for snippet/window behavior, multibyte handling, and config degradation cases.
[crates/gwiki/src/commands/search.rs:27-30]
[crates/gwiki/src/commands/search.rs:32-39]
[crates/gwiki/src/commands/search.rs:41-78]
[crates/gwiki/src/commands/search.rs:80-143]
[crates/gwiki/src/commands/search.rs:145-163]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SearchRetrieval` | class | `pub(crate) struct SearchRetrieval {` | `SearchRetrieval [class]` | `7827022e-fc2c-5f7c-af69-84222a4ae704` | 27-30 [crates/gwiki/src/commands/search.rs:27-30] | Indexed class `SearchRetrieval` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:27-30] |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `53398570-7c16-5692-bcb6-b8fd6e9d4860` | 32-39 [crates/gwiki/src/commands/search.rs:32-39] | Indexed function `execute` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:32-39] |
| `retrieve` | function | `pub(crate) fn retrieve(` | `retrieve [function]` | `5a87b1f0-54ab-5890-bfa2-6bd740f81ba2` | 41-78 [crates/gwiki/src/commands/search.rs:41-78] | Indexed function `retrieve` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:41-78] |
| `run_search_attached` | function | `fn run_search_attached(` | `run_search_attached [function]` | `070eb4f5-ea2c-51b8-84ce-02f81627b736` | 80-143 [crates/gwiki/src/commands/search.rs:80-143] | Indexed function `run_search_attached` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:80-143] |
| `graph_backend_from_falkor_config` | function | `fn graph_backend_from_falkor_config(` | `graph_backend_from_falkor_config [function]` | `e6235d82-80a4-5ec7-8bc1-7f802ee05a9b` | 145-163 [crates/gwiki/src/commands/search.rs:145-163] | Indexed function `graph_backend_from_falkor_config` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:145-163] |
| `required_search_config` | function | `fn required_search_config(service: &'static str) -> WikiError {` | `required_search_config [function]` | `c6e5cf0a-22d4-516e-aafb-098525a544f2` | 165-171 [crates/gwiki/src/commands/search.rs:165-171] | Indexed function `required_search_config` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:165-171] |
| `resolve_semantic_embedding` | function | `fn resolve_semantic_embedding(` | `resolve_semantic_embedding [function]` | `1d60d254-ff75-5230-8498-90ed128697c9` | 173-208 [crates/gwiki/src/commands/search.rs:173-208] | Indexed function `resolve_semantic_embedding` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:173-208] |
| `effective_embedding_route` | function | `fn effective_embedding_route(context: &AiContext) -> AiRouting {` | `effective_embedding_route [function]` | `c5f3012d-7fad-5f42-8f48-4677cb20861f` | 210-234 [crates/gwiki/src/commands/search.rs:210-234] | Indexed function `effective_embedding_route` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:210-234] |
| `gobby_home` | function | `fn gobby_home() -> Result<std::path::PathBuf, WikiError> {` | `gobby_home [function]` | `4e165778-be8b-52dd-a920-3a0ad80950f1` | 236-240 [crates/gwiki/src/commands/search.rs:236-240] | Indexed function `gobby_home` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:236-240] |
| `SearchExecutionInput` | class | `struct SearchExecutionInput {` | `SearchExecutionInput [class]` | `560becd1-c5d0-52f7-90b6-ea0356af3fbe` | 242-248 [crates/gwiki/src/commands/search.rs:242-248] | Indexed class `SearchExecutionInput` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:242-248] |
| `run_search_with_backends` | function | `fn run_search_with_backends<B, S, G>(` | `run_search_with_backends [function]` | `2d257661-3897-5002-9e2e-b72190f1030e` | 250-317 [crates/gwiki/src/commands/search.rs:250-317] | Indexed function `run_search_with_backends` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:250-317] |
| `bounded_snippet` | function | `fn bounded_snippet(content: &str, query: &str) -> String {` | `bounded_snippet [function]` | `c97eb4ec-4927-5a30-a4e2-4a543b89bf5c` | 326-329 [crates/gwiki/src/commands/search.rs:326-329] | Indexed function `bounded_snippet` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:326-329] |
| `query_window` | function | `pub(crate) fn query_window(content: &str, query: &str, before: usize, after: usize) -> String {` | `query_window [function]` | `e3a44454-a132-5ee0-ad8d-f505c1c171c2` | 333-353 [crates/gwiki/src/commands/search.rs:333-353] | Indexed function `query_window` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:333-353] |
| `render` | function | `fn render(output: SearchOutput) -> Result<CommandOutcome, WikiError> {` | `render [function]` | `9a2977a4-8878-5b1c-a776-278326e4b274` | 355-366 [crates/gwiki/src/commands/search.rs:355-366] | Indexed function `render` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:355-366] |
| `render_text` | function | `fn render_text(` | `render_text [function]` | `561211da-50c7-5a25-8e20-e65fa5d278e5` | 368-395 [crates/gwiki/src/commands/search.rs:368-395] | Indexed function `render_text` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:368-395] |
| `qdrant_config_requires_non_blank_url` | function | `fn qdrant_config_requires_non_blank_url() {` | `qdrant_config_requires_non_blank_url [function]` | `3ecfdd19-6f21-52e1-8fcc-3818c5198f59` | 402-415 [crates/gwiki/src/commands/search.rs:402-415] | Indexed function `qdrant_config_requires_non_blank_url` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:402-415] |
| `missing_falkor_config_degrades_graph_search` | function | `fn missing_falkor_config_degrades_graph_search() {` | `missing_falkor_config_degrades_graph_search [function]` | `1d46a60d-54ed-5e4a-9af3-388121faa9a0` | 418-435 [crates/gwiki/src/commands/search.rs:418-435] | Indexed function `missing_falkor_config_degrades_graph_search` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:418-435] |
| `bounded_snippet_windows_around_first_query_token` | function | `fn bounded_snippet_windows_around_first_query_token() {` | `bounded_snippet_windows_around_first_query_token [function]` | `2846defe-17bb-54d9-9157-1a8ac26a2793` | 438-448 [crates/gwiki/src/commands/search.rs:438-448] | Indexed function `bounded_snippet_windows_around_first_query_token` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:438-448] |
| `bounded_snippet_never_emits_full_document_body` | function | `fn bounded_snippet_never_emits_full_document_body() {` | `bounded_snippet_never_emits_full_document_body [function]` | `3b586ce2-616e-586f-be7d-da060e284a9a` | 451-457 [crates/gwiki/src/commands/search.rs:451-457] | Indexed function `bounded_snippet_never_emits_full_document_body` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:451-457] |
| `query_window_handles_multibyte_content` | function | `fn query_window_handles_multibyte_content() {` | `query_window_handles_multibyte_content [function]` | `7f3ed55b-b5a1-5f46-8e0d-16acc2b2f4a3` | 460-466 [crates/gwiki/src/commands/search.rs:460-466] | Indexed function `query_window_handles_multibyte_content` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:460-466] |
