---
title: crates/gwiki/src/graph/export.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/export.rs
  ranges:
  - 12-111
  - 114-190
  - 204-317
  - 320-349
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/graph/export.rs:12-111](crates/gwiki/src/graph/export.rs#L12-L111), [crates/gwiki/src/graph/export.rs:114-190](crates/gwiki/src/graph/export.rs#L114-L190), [crates/gwiki/src/graph/export.rs:204-317](crates/gwiki/src/graph/export.rs#L204-L317), [crates/gwiki/src/graph/export.rs:320-349](crates/gwiki/src/graph/export.rs#L320-L349)

</details>

# crates/gwiki/src/graph/export.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines wiki graph export logic. `WikiGraphFacts::export_graph` walks the collected documents, sources, and links to build a `GraphExport`, deduplicating nodes with a `BTreeSet` and emitting the appropriate trust and audit edges between document, source, citation, resolved-target, and unresolved-target nodes. `render_graph_report` turns that exported graph into a report-friendly representation. The tests confirm link targets are scoped correctly, unresolved targets are emitted as nodes, and missing resolved targets get placeholder nodes.
[crates/gwiki/src/graph/export.rs:12-111]
[crates/gwiki/src/graph/export.rs:114-190]
[crates/gwiki/src/graph/export.rs:204-317]
[crates/gwiki/src/graph/export.rs:320-349]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `WikiGraphFacts::export_graph` | method | `pub fn export_graph(` | `WikiGraphFacts::export_graph [method]` | `7f77bc8c-8763-526d-85f9-942bb2382fa4` | 12-111 [crates/gwiki/src/graph/export.rs:12-111] | Indexed method `WikiGraphFacts::export_graph` in `crates/gwiki/src/graph/export.rs`. [crates/gwiki/src/graph/export.rs:12-111] |
| `render_graph_report` | function | `pub fn render_graph_report(export: &GraphExport) -> String {` | `render_graph_report [function]` | `24fee7a5-bd0c-5d1b-84b2-2aed37596006` | 114-190 [crates/gwiki/src/graph/export.rs:114-190] | Indexed function `render_graph_report` in `crates/gwiki/src/graph/export.rs`. [crates/gwiki/src/graph/export.rs:114-190] |
| `export_graph_scopes_ids_and_emits_unresolved_target_nodes` | function | `fn export_graph_scopes_ids_and_emits_unresolved_target_nodes() {` | `export_graph_scopes_ids_and_emits_unresolved_target_nodes [function]` | `c2d2d1d6-edda-526e-933c-db52b1b81fcb` | 204-317 [crates/gwiki/src/graph/export.rs:204-317] | Indexed function `export_graph_scopes_ids_and_emits_unresolved_target_nodes` in `crates/gwiki/src/graph/export.rs`. [crates/gwiki/src/graph/export.rs:204-317] |
| `export_graph_adds_placeholder_for_missing_resolved_target` | function | `fn export_graph_adds_placeholder_for_missing_resolved_target() {` | `export_graph_adds_placeholder_for_missing_resolved_target [function]` | `f8bfc816-60d3-59f3-9a64-6deb429e5dc5` | 320-349 [crates/gwiki/src/graph/export.rs:320-349] | Indexed function `export_graph_adds_placeholder_for_missing_resolved_target` in `crates/gwiki/src/graph/export.rs`. [crates/gwiki/src/graph/export.rs:320-349] |
