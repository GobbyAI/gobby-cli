---
title: crates/gwiki/src/commands/search.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/search.rs
  ranges:
  - 23-30
  - 32-69
  - 71-134
  - 136-154
  - 156-162
  - 164-199
  - 201-225
  - 227-231
  - 233-239
  - 241-302
  - 304-315
  - 317-336
  - 343-356
  - 359-376
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/search.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

`crates/gwiki/src/commands/search.rs` exposes 14 indexed API symbols.
[crates/gwiki/src/commands/search.rs:23-30]
[crates/gwiki/src/commands/search.rs:32-69]
[crates/gwiki/src/commands/search.rs:71-134]
[crates/gwiki/src/commands/search.rs:136-154]
[crates/gwiki/src/commands/search.rs:156-162]

## API Symbols

- `execute` (function) component `execute [function]` (`4f541be4-d7ae-5f0a-af99-f929e1b9581f`) lines 23-30 [crates/gwiki/src/commands/search.rs:23-30]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:23-30]
- `retrieve` (function) component `retrieve [function]` (`89363076-8481-5c6f-a623-e35febf33d75`) lines 32-69 [crates/gwiki/src/commands/search.rs:32-69]
  - Signature: `pub(crate) fn retrieve(`
  - Purpose: Indexed function `retrieve` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:32-69]
- `run_search_attached` (function) component `run_search_attached [function]` (`442c1db1-e973-58de-add4-cbd764f2490e`) lines 71-134 [crates/gwiki/src/commands/search.rs:71-134]
  - Signature: `fn run_search_attached(`
  - Purpose: Indexed function `run_search_attached` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:71-134]
- `graph_backend_from_falkor_config` (function) component `graph_backend_from_falkor_config [function]` (`09260527-fdfb-5094-bbff-ca7a329574b4`) lines 136-154 [crates/gwiki/src/commands/search.rs:136-154]
  - Signature: `fn graph_backend_from_falkor_config(`
  - Purpose: Indexed function `graph_backend_from_falkor_config` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:136-154]
- `required_search_config` (function) component `required_search_config [function]` (`df834dcb-fbd0-55bc-a439-a3e9470e2b7b`) lines 156-162 [crates/gwiki/src/commands/search.rs:156-162]
  - Signature: `fn required_search_config(service: &'static str) -> WikiError {`
  - Purpose: Indexed function `required_search_config` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:156-162]
- `resolve_semantic_embedding` (function) component `resolve_semantic_embedding [function]` (`ae739d3e-bf82-5839-a971-392c74512fc1`) lines 164-199 [crates/gwiki/src/commands/search.rs:164-199]
  - Signature: `fn resolve_semantic_embedding(`
  - Purpose: Indexed function `resolve_semantic_embedding` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:164-199]
- `effective_embedding_route` (function) component `effective_embedding_route [function]` (`dce63ceb-f251-5bca-8a8f-f4aead7eb833`) lines 201-225 [crates/gwiki/src/commands/search.rs:201-225]
  - Signature: `fn effective_embedding_route(context: &AiContext) -> AiRouting {`
  - Purpose: Indexed function `effective_embedding_route` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:201-225]
- `gobby_home` (function) component `gobby_home [function]` (`df8cf898-dbfa-5706-9a45-824f20219bb1`) lines 227-231 [crates/gwiki/src/commands/search.rs:227-231]
  - Signature: `fn gobby_home() -> Result<std::path::PathBuf, WikiError> {`
  - Purpose: Indexed function `gobby_home` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:227-231]
- `SearchExecutionInput` (class) component `SearchExecutionInput [class]` (`c1b5499b-411f-5c9e-bd9d-e243563c9211`) lines 233-239 [crates/gwiki/src/commands/search.rs:233-239]
  - Signature: `struct SearchExecutionInput {`
  - Purpose: Indexed class `SearchExecutionInput` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:233-239]
- `run_search_with_backends` (function) component `run_search_with_backends [function]` (`074f887c-d901-5bfe-8aa2-a72dbb70f3e1`) lines 241-302 [crates/gwiki/src/commands/search.rs:241-302]
  - Signature: `fn run_search_with_backends<B, S, G>(`
  - Purpose: Indexed function `run_search_with_backends` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:241-302]
- `render` (function) component `render [function]` (`be5ddbc1-802a-5057-beff-6c0c721c8585`) lines 304-315 [crates/gwiki/src/commands/search.rs:304-315]
  - Signature: `fn render(output: SearchOutput) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Indexed function `render` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:304-315]
- `render_text` (function) component `render_text [function]` (`5f11fcab-8d03-59e8-861f-587c8ea9e25a`) lines 317-336 [crates/gwiki/src/commands/search.rs:317-336]
  - Signature: `fn render_text(query: &str, scope: &ScopeIdentity, results: &[SearchResultOutput]) -> String {`
  - Purpose: Indexed function `render_text` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:317-336]
- `qdrant_config_requires_non_blank_url` (function) component `qdrant_config_requires_non_blank_url [function]` (`a9def8fc-d7d9-5a9e-b58b-7184119e102b`) lines 343-356 [crates/gwiki/src/commands/search.rs:343-356]
  - Signature: `fn qdrant_config_requires_non_blank_url() {`
  - Purpose: Indexed function `qdrant_config_requires_non_blank_url` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:343-356]
- `missing_falkor_config_degrades_graph_search` (function) component `missing_falkor_config_degrades_graph_search [function]` (`0b06c2d1-c120-56d0-8829-f758f34c943b`) lines 359-376 [crates/gwiki/src/commands/search.rs:359-376]
  - Signature: `fn missing_falkor_config_degrades_graph_search() {`
  - Purpose: Indexed function `missing_falkor_config_degrades_graph_search` in `crates/gwiki/src/commands/search.rs`. [crates/gwiki/src/commands/search.rs:359-376]

