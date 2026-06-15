---
title: crates/gwiki/src/graph/export.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/export.rs
  ranges:
  - 11-112
  - 114-190
  - 204-317
  - 320-349
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/export.rs

Module: [[code/modules/crates/gwiki/src/graph|crates/gwiki/src/graph]]

## Purpose

This file defines graph export and reporting for wiki facts. `WikiGraphFacts::export_graph` builds a deduplicated `GraphExport` by collecting document, source, citation, and link-target nodes, then wiring them with `supports` edges from sources to documents and `cites` edges from citations to sources, while tracking node IDs to avoid duplicates and to add placeholder nodes for unresolved or missing targets. `render_graph_report` turns that export into a markdown report with graph statistics, degraded-source and analytics sections, and a Mermaid visualization; the tests verify handling of unresolved targets and placeholder nodes.
[crates/gwiki/src/graph/export.rs:11-112]
[crates/gwiki/src/graph/export.rs:12-111]
[crates/gwiki/src/graph/export.rs:114-190]
[crates/gwiki/src/graph/export.rs:204-317]
[crates/gwiki/src/graph/export.rs:320-349]

## API Symbols

- `WikiGraphFacts` (class) component `WikiGraphFacts [class]` (`8381d18c-cbbc-55b5-845b-eae574208ca2`) lines 11-112 [crates/gwiki/src/graph/export.rs:11-112]
  - Signature: `impl WikiGraphFacts {`
  - Purpose: `export_graph` serializes the wiki graph as deduplicated nodes and directed edges representing support relationships (source→document) and citation relationships (citation→source). [crates/gwiki/src/graph/export.rs:11-112]
- `WikiGraphFacts.export_graph` (method) component `WikiGraphFacts.export_graph [method]` (`7f77bc8c-8763-526d-85f9-942bb2382fa4`) lines 12-111 [crates/gwiki/src/graph/export.rs:12-111]
  - Signature: `pub fn export_graph(`
  - Purpose: Generates a deduplicated graph export containing document, source, and citation nodes connected by "supports" and "cites" relationship edges, deduplicating nodes by ID across all entity types. [crates/gwiki/src/graph/export.rs:12-111]
- `render_graph_report` (function) component `render_graph_report [function]` (`24fee7a5-bd0c-5d1b-84b2-2aed37596006`) lines 114-190 [crates/gwiki/src/graph/export.rs:114-190]
  - Signature: `pub fn render_graph_report(export: &GraphExport) -> String {`
  - Purpose: Converts a `GraphExport` into a markdown report string containing graph statistics (node/edge counts), degraded sources, analytics (communities, centrality, bridges, hotspots), and a Mermaid graph visualization of all nodes and edges. [crates/gwiki/src/graph/export.rs:114-190]
- `export_graph_scopes_ids_and_emits_unresolved_target_nodes` (function) component `export_graph_scopes_ids_and_emits_unresolved_target_nodes [function]` (`c2d2d1d6-edda-526e-933c-db52b1b81fcb`) lines 204-317 [crates/gwiki/src/graph/export.rs:204-317]
  - Signature: `fn export_graph_scopes_ids_and_emits_unresolved_target_nodes() {`
  - Purpose: Constructs a WikiGraphFacts structure containing documents, unresolved links, sources, and code edges across project and topic scopes to test graph serialization with missing link targets. [crates/gwiki/src/graph/export.rs:204-317]
- `export_graph_adds_placeholder_for_missing_resolved_target` (function) component `export_graph_adds_placeholder_for_missing_resolved_target [function]` (`f8bfc816-60d3-59f3-9a64-6deb429e5dc5`) lines 320-349 [crates/gwiki/src/graph/export.rs:320-349]
  - Signature: `fn export_graph_adds_placeholder_for_missing_resolved_target() {`
  - Purpose: This test verifies that exporting a wiki graph creates a placeholder node for a resolved link target that lacks a corresponding document definition. [crates/gwiki/src/graph/export.rs:320-349]

