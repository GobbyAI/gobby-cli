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

This file builds a `MemoryWikiGraph` from an in-memory wiki store and resolves its links into graph edges. `memory_graph_from_store` copies documents and sources into graph facts, precomputes slug-to-path matches, and converts stored links into resolved `WikiGraphLink` entries by calling `resolve_graph_target`. The helper functions work together to reject external or empty targets, strip fragments and path separators, resolve relative paths against the source document directory, normalize `.` and `..` segments, and fall back to slug-based lookup before leaving a target unresolved. The tests confirm that source and document paths stay distinct, external URL-like targets are ignored, slug targets resolve through the precomputed map, and relative links resolve from the source document’s location.
[crates/gwiki/src/support/graph.rs:8-55]
[crates/gwiki/src/support/graph.rs:57-90]
[crates/gwiki/src/support/graph.rs:92-103]
[crates/gwiki/src/support/graph.rs:105-107]
[crates/gwiki/src/support/graph.rs:109-122]

## API Symbols

- `memory_graph_from_store` (function) component `memory_graph_from_store [function]` (`c58bfe53-d5ea-5e3b-8307-5db7d7679aeb`) lines 8-55 [crates/gwiki/src/support/graph.rs:8-55]
  - Signature: `pub(crate) fn memory_graph_from_store(`
  - Purpose: Builds a 'MemoryWikiGraph' from a 'MemoryWikiStore' and 'SearchScope' by cloning all stored documents, resolving and collecting valid links into graph edges, copying sources, and replacing the graph’s facts with those collections plus an empty 'code_edges' list. [crates/gwiki/src/support/graph.rs:8-55]
- `resolve_graph_target` (function) component `resolve_graph_target [function]` (`fbf0a734-28e0-54f1-a47d-63120beb0197`) lines 57-90 [crates/gwiki/src/support/graph.rs:57-90]
  - Signature: `fn resolve_graph_target(`
  - Purpose: Resolves a wiki graph link target by ignoring external URLs, stripping fragments and backslashes, attempting to map the normalized path to a stored document or slug target, and otherwise returning the unresolved relative lookup path. [crates/gwiki/src/support/graph.rs:57-90]
- `resolve_relative_graph_path` (function) component `resolve_relative_graph_path [function]` (`cd20f1ee-83ea-57bb-96a3-d927c3608429`) lines 92-103 [crates/gwiki/src/support/graph.rs:92-103]
  - Signature: `fn resolve_relative_graph_path(raw_target: &str, source_path: &Path) -> String {`
  - Purpose: 'resolve_relative_graph_path' strips any leading '/' from 'raw_target', returns that normalized target unchanged if it was absolute or not path-like, otherwise resolves it against 'source_path'’s parent directory, normalizes the joined path, and converts it to a forward-slash string. [crates/gwiki/src/support/graph.rs:92-103]
- `is_path_like_target` (function) component `is_path_like_target [function]` (`c5197c2f-64c9-5a8b-abd7-ffce06d1e758`) lines 105-107 [crates/gwiki/src/support/graph.rs:105-107]
  - Signature: `fn is_path_like_target(target: &str) -> bool {`
  - Purpose: Returns 'true' if 'target' looks path-like by containing '/', starting with '.', or ending with '.md', otherwise returns 'false'. [crates/gwiki/src/support/graph.rs:105-107]
- `normalize_path` (function) component `normalize_path [function]` (`5b38ce11-b074-5501-ad0f-a67c932f35f7`) lines 109-122 [crates/gwiki/src/support/graph.rs:109-122]
  - Signature: `fn normalize_path(path: PathBuf) -> PathBuf {`
  - Purpose: Returns a new 'PathBuf' by iterating over the input path’s components and removing '.' segments, resolving '..' by popping the last accumulated component, appending normal segments, and ignoring root/prefix components. [crates/gwiki/src/support/graph.rs:109-122]
- `slug_target_map` (function) component `slug_target_map [function]` (`a6f8ad7e-af2f-59a1-bae5-47c7094b7d91`) lines 124-146 [crates/gwiki/src/support/graph.rs:124-146]
  - Signature: `fn slug_target_map(store: &store::MemoryWikiStore) -> BTreeMap<String, PathBuf> {`
  - Purpose: Builds a 'BTreeMap' from slugified document file stems and titles to their first associated 'PathBuf', preserving deterministic collision resolution by keeping the earliest path encountered for each slug. [crates/gwiki/src/support/graph.rs:124-146]
- `is_external_target` (function) component `is_external_target [function]` (`f10918ae-5486-56ec-bb51-c573bd941deb`) lines 148-154 [crates/gwiki/src/support/graph.rs:148-154]
  - Signature: `fn is_external_target(target: &str) -> bool {`
  - Purpose: Returns 'true' when 'target' is empty or appears to be an external URL or special link by containing '://', starting with '//' or '\\\\', or using the 'mailto:' scheme. [crates/gwiki/src/support/graph.rs:148-154]
- `graph_uses_distinct_source_document_paths` (function) component `graph_uses_distinct_source_document_paths [function]` (`289e2b52-0509-5e66-b63a-ba50562a6513`) lines 162-192 [crates/gwiki/src/support/graph.rs:162-192]
  - Signature: `fn graph_uses_distinct_source_document_paths() {`
  - Purpose: Verifies that 'memory_graph_from_store' preserves distinct 'source_path' and 'document_path' values for a source entry in the topic-scoped graph. [crates/gwiki/src/support/graph.rs:162-192]
- `graph_rejects_url_like_external_targets` (function) component `graph_rejects_url_like_external_targets [function]` (`d111c3fe-cfab-50a5-8389-52b9fb7880ec`) lines 195-208 [crates/gwiki/src/support/graph.rs:195-208]
  - Signature: `fn graph_rejects_url_like_external_targets() {`
  - Purpose: Verifies that 'resolve_graph_target' returns 'None' for URL-like external targets, including protocol-relative, UNC-style, and custom-scheme strings. [crates/gwiki/src/support/graph.rs:195-208]
- `graph_resolves_slug_targets_from_precomputed_map` (function) component `graph_resolves_slug_targets_from_precomputed_map [function]` (`7437ceb8-e970-50fa-bca9-257417e413de`) lines 211-236 [crates/gwiki/src/support/graph.rs:211-236]
  - Signature: `fn graph_resolves_slug_targets_from_precomputed_map() {`
  - Purpose: Verifies that 'resolve_graph_target' uses the precomputed slug-target map to resolve the slug '"Rust Async"' from 'knowledge/topics/source.md' to the document path 'knowledge/topics/rust-async.md' as a resolved 'WikiGraphLinkTarget'. [crates/gwiki/src/support/graph.rs:211-236]
- `graph_resolves_relative_targets_from_source_document_directory` (function) component `graph_resolves_relative_targets_from_source_document_directory [function]` (`0e66cf59-0d78-55be-9627-7fe994e92989`) lines 239-272 [crates/gwiki/src/support/graph.rs:239-272]
  - Signature: `fn graph_resolves_relative_targets_from_source_document_directory() {`
  - Purpose: Verifies that 'resolve_graph_target' resolves relative graph link targets against the source document’s directory, producing the correct 'Resolved(PathBuf)' for same-directory and parent-directory paths. [crates/gwiki/src/support/graph.rs:239-272]

