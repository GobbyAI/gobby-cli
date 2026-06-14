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

# crates/gwiki/src/support/graph.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

Builds an in-memory wiki graph from a memory store by collecting documents, links, and sources into `MemoryWikiGraph` facts. It first copies all stored documents and sources into graph records, then resolves each link target with a target-resolution pipeline that filters out external/URL-like targets, normalizes fragments and path separators, checks for direct document-path matches, and falls back to a precomputed slug-to-path map or relative-path resolution from the source document’s directory. Helper functions centralize path normalization, slug mapping, and external-target detection so the main graph assembly stays focused on translating store state into resolved graph facts.
[crates/gwiki/src/support/graph.rs:8-55]
[crates/gwiki/src/support/graph.rs:57-90]
[crates/gwiki/src/support/graph.rs:92-103]
[crates/gwiki/src/support/graph.rs:105-107]
[crates/gwiki/src/support/graph.rs:109-122]

## API Symbols

- `memory_graph_from_store` (function) component `memory_graph_from_store [function]` (`c58bfe53-d5ea-5e3b-8307-5db7d7679aeb`) lines 8-55 [crates/gwiki/src/support/graph.rs:8-55]
  - Signature: `pub(crate) fn memory_graph_from_store(`
  - Purpose: Indexed function `memory_graph_from_store` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:8-55]
- `resolve_graph_target` (function) component `resolve_graph_target [function]` (`fbf0a734-28e0-54f1-a47d-63120beb0197`) lines 57-90 [crates/gwiki/src/support/graph.rs:57-90]
  - Signature: `fn resolve_graph_target(`
  - Purpose: Indexed function `resolve_graph_target` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:57-90]
- `resolve_relative_graph_path` (function) component `resolve_relative_graph_path [function]` (`cd20f1ee-83ea-57bb-96a3-d927c3608429`) lines 92-103 [crates/gwiki/src/support/graph.rs:92-103]
  - Signature: `fn resolve_relative_graph_path(raw_target: &str, source_path: &Path) -> String {`
  - Purpose: Indexed function `resolve_relative_graph_path` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:92-103]
- `is_path_like_target` (function) component `is_path_like_target [function]` (`c5197c2f-64c9-5a8b-abd7-ffce06d1e758`) lines 105-107 [crates/gwiki/src/support/graph.rs:105-107]
  - Signature: `fn is_path_like_target(target: &str) -> bool {`
  - Purpose: Indexed function `is_path_like_target` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:105-107]
- `normalize_path` (function) component `normalize_path [function]` (`5b38ce11-b074-5501-ad0f-a67c932f35f7`) lines 109-122 [crates/gwiki/src/support/graph.rs:109-122]
  - Signature: `fn normalize_path(path: PathBuf) -> PathBuf {`
  - Purpose: Indexed function `normalize_path` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:109-122]
- `slug_target_map` (function) component `slug_target_map [function]` (`a6f8ad7e-af2f-59a1-bae5-47c7094b7d91`) lines 124-146 [crates/gwiki/src/support/graph.rs:124-146]
  - Signature: `fn slug_target_map(store: &store::MemoryWikiStore) -> BTreeMap<String, PathBuf> {`
  - Purpose: Indexed function `slug_target_map` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:124-146]
- `is_external_target` (function) component `is_external_target [function]` (`f10918ae-5486-56ec-bb51-c573bd941deb`) lines 148-154 [crates/gwiki/src/support/graph.rs:148-154]
  - Signature: `fn is_external_target(target: &str) -> bool {`
  - Purpose: Indexed function `is_external_target` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:148-154]
- `graph_uses_distinct_source_document_paths` (function) component `graph_uses_distinct_source_document_paths [function]` (`289e2b52-0509-5e66-b63a-ba50562a6513`) lines 162-192 [crates/gwiki/src/support/graph.rs:162-192]
  - Signature: `fn graph_uses_distinct_source_document_paths() {`
  - Purpose: Indexed function `graph_uses_distinct_source_document_paths` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:162-192]
- `graph_rejects_url_like_external_targets` (function) component `graph_rejects_url_like_external_targets [function]` (`d111c3fe-cfab-50a5-8389-52b9fb7880ec`) lines 195-208 [crates/gwiki/src/support/graph.rs:195-208]
  - Signature: `fn graph_rejects_url_like_external_targets() {`
  - Purpose: Indexed function `graph_rejects_url_like_external_targets` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:195-208]
- `graph_resolves_slug_targets_from_precomputed_map` (function) component `graph_resolves_slug_targets_from_precomputed_map [function]` (`7437ceb8-e970-50fa-bca9-257417e413de`) lines 211-236 [crates/gwiki/src/support/graph.rs:211-236]
  - Signature: `fn graph_resolves_slug_targets_from_precomputed_map() {`
  - Purpose: Indexed function `graph_resolves_slug_targets_from_precomputed_map` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:211-236]
- `graph_resolves_relative_targets_from_source_document_directory` (function) component `graph_resolves_relative_targets_from_source_document_directory [function]` (`0e66cf59-0d78-55be-9627-7fe994e92989`) lines 239-272 [crates/gwiki/src/support/graph.rs:239-272]
  - Signature: `fn graph_resolves_relative_targets_from_source_document_directory() {`
  - Purpose: Indexed function `graph_resolves_relative_targets_from_source_document_directory` in `crates/gwiki/src/support/graph.rs`. [crates/gwiki/src/support/graph.rs:239-272]

