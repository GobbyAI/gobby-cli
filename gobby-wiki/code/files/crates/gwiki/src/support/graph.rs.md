---
title: crates/gwiki/src/support/graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/graph.rs
  ranges:
  - 8-55
  - 57-90
  - 92-103
  - 105-107
  - 109-122
  - 124-146
  - 148-154
  - 162-192
  - 195-208
  - 211-236
  - 239-272
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/graph.rs:8-55](crates/gwiki/src/support/graph.rs#L8-L55), [crates/gwiki/src/support/graph.rs:57-90](crates/gwiki/src/support/graph.rs#L57-L90), [crates/gwiki/src/support/graph.rs:92-103](crates/gwiki/src/support/graph.rs#L92-L103), [crates/gwiki/src/support/graph.rs:105-107](crates/gwiki/src/support/graph.rs#L105-L107), [crates/gwiki/src/support/graph.rs:109-122](crates/gwiki/src/support/graph.rs#L109-L122), [crates/gwiki/src/support/graph.rs:124-146](crates/gwiki/src/support/graph.rs#L124-L146), [crates/gwiki/src/support/graph.rs:148-154](crates/gwiki/src/support/graph.rs#L148-L154), [crates/gwiki/src/support/graph.rs:162-192](crates/gwiki/src/support/graph.rs#L162-L192), [crates/gwiki/src/support/graph.rs:195-208](crates/gwiki/src/support/graph.rs#L195-L208), [crates/gwiki/src/support/graph.rs:211-236](crates/gwiki/src/support/graph.rs#L211-L236), [crates/gwiki/src/support/graph.rs:239-272](crates/gwiki/src/support/graph.rs#L239-L272)

</details>

# crates/gwiki/src/support/graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file builds an in-memory wiki graph from a `MemoryWikiStore` and provides the target-resolution logic that turns stored links into graph edges. `memory_graph_from_store` gathers documents, links, and sources into `WikiGraphFacts`, while `resolve_graph_target` normalizes each link target, rejects external/URL-like targets, resolves relative paths from the source document directory, and falls back to a precomputed slug-to-path map so links can be matched to the correct document. The smaller helpers support that flow by classifying path-like targets, normalizing paths, and deriving slug mappings used during resolution.
[crates/gwiki/src/support/graph.rs:8-55]
[crates/gwiki/src/support/graph.rs:57-90]
[crates/gwiki/src/support/graph.rs:92-103]
[crates/gwiki/src/support/graph.rs:105-107]
[crates/gwiki/src/support/graph.rs:109-122]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `memory_graph_from_store` | function | `pub(crate) fn memory_graph_from_store(` | `memory_graph_from_store [function]` | `c58bfe53-d5ea-5e3b-8307-5db7d7679aeb` | 8-55 [crates/gwiki/src/support/graph.rs:8-55] | Indexed function `memory_graph_from_store` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:8-55] |
| `resolve_graph_target` | function | `fn resolve_graph_target(` | `resolve_graph_target [function]` | `fbf0a734-28e0-54f1-a47d-63120beb0197` | 57-90 [crates/gwiki/src/support/graph.rs:57-90] | Indexed function `resolve_graph_target` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:57-90] |
| `resolve_relative_graph_path` | function | `fn resolve_relative_graph_path(raw_target: &str, source_path: &Path) -> String {` | `resolve_relative_graph_path [function]` | `cd20f1ee-83ea-57bb-96a3-d927c3608429` | 92-103 [crates/gwiki/src/support/graph.rs:92-103] | Indexed function `resolve_relative_graph_path` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:92-103] |
| `is_path_like_target` | function | `fn is_path_like_target(target: &str) -> bool {` | `is_path_like_target [function]` | `c5197c2f-64c9-5a8b-abd7-ffce06d1e758` | 105-107 [crates/gwiki/src/support/graph.rs:105-107] | Indexed function `is_path_like_target` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:105-107] |
| `normalize_path` | function | `fn normalize_path(path: PathBuf) -> PathBuf {` | `normalize_path [function]` | `5b38ce11-b074-5501-ad0f-a67c932f35f7` | 109-122 [crates/gwiki/src/support/graph.rs:109-122] | Indexed function `normalize_path` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:109-122] |
| `slug_target_map` | function | `fn slug_target_map(store: &store::MemoryWikiStore) -> BTreeMap<String, PathBuf> {` | `slug_target_map [function]` | `a6f8ad7e-af2f-59a1-bae5-47c7094b7d91` | 124-146 [crates/gwiki/src/support/graph.rs:124-146] | Indexed function `slug_target_map` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:124-146] |
| `is_external_target` | function | `fn is_external_target(target: &str) -> bool {` | `is_external_target [function]` | `f10918ae-5486-56ec-bb51-c573bd941deb` | 148-154 [crates/gwiki/src/support/graph.rs:148-154] | Indexed function `is_external_target` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:148-154] |
| `graph_uses_distinct_source_document_paths` | function | `fn graph_uses_distinct_source_document_paths() {` | `graph_uses_distinct_source_document_paths [function]` | `289e2b52-0509-5e66-b63a-ba50562a6513` | 162-192 [crates/gwiki/src/support/graph.rs:162-192] | Indexed function `graph_uses_distinct_source_document_paths` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:162-192] |
| `graph_rejects_url_like_external_targets` | function | `fn graph_rejects_url_like_external_targets() {` | `graph_rejects_url_like_external_targets [function]` | `d111c3fe-cfab-50a5-8389-52b9fb7880ec` | 195-208 [crates/gwiki/src/support/graph.rs:195-208] | Indexed function `graph_rejects_url_like_external_targets` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:195-208] |
| `graph_resolves_slug_targets_from_precomputed_map` | function | `fn graph_resolves_slug_targets_from_precomputed_map() {` | `graph_resolves_slug_targets_from_precomputed_map [function]` | `7437ceb8-e970-50fa-bca9-257417e413de` | 211-236 [crates/gwiki/src/support/graph.rs:211-236] | Indexed function `graph_resolves_slug_targets_from_precomputed_map` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:211-236] |
| `graph_resolves_relative_targets_from_source_document_directory` | function | `fn graph_resolves_relative_targets_from_source_document_directory() {` | `graph_resolves_relative_targets_from_source_document_directory [function]` | `0e66cf59-0d78-55be-9627-7fe994e92989` | 239-272 [crates/gwiki/src/support/graph.rs:239-272] | Indexed function `graph_resolves_relative_targets_from_source_document_directory` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:239-272] |
