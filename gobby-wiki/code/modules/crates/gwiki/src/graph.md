---
title: crates/gwiki/src/graph
type: code_module
provenance:
- file: crates/gwiki/src/graph/analytics.rs
- file: crates/gwiki/src/graph/context.rs
- file: crates/gwiki/src/graph/export.rs
- file: crates/gwiki/src/graph/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/graph` defines the wiki graph model and the serializable products built from it. The root module exposes graph vocabulary constants, document/source/link/code-edge fact types, `WikiGraphFacts`, export options, and `GraphExport`; it also publishes `analytics` and `context`, keeps `export` private, and re-exports `render_graph_report` for outside callers (`crates/gwiki/src/graph/mod.rs:7-19`, `crates/gwiki/src/graph/mod.rs:21-92`).

The export flow hangs off `WikiGraphFacts::export_graph`, which builds a deduplicated node set, emits document/source/citation nodes, and creates trust and audit edges such as `supports` and `cites`. Resolved wiki links are normalized into document nodes before edge generation continues (`crates/gwiki/src/graph/export.rs:11-67`). Analytics collaborates with `gobby_core::graph_analytics`, importing graph primitives plus `analyze` and `weight_for_kind`, then serializes communities, centrality, bridge/god-node detection, unexpected links, and hotspots; duplicate node metadata is surfaced as `GraphAnalyticsError` (`crates/gwiki/src/graph/analytics.rs:3-47`).

Context packaging reuses the core graph model rather than duplicating it: `context.rs` imports `WikiGraphCodeEdge`, `WikiGraphFacts`, and `WikiGraphLinkTarget` from `crate::graph`, plus `SearchScope` (`crates/gwiki/src/graph/context.rs:4-5`). Its options track degraded and truncated inputs, while `GraphContextPack` carries scope, warnings, neighborhoods, and recommendations; each neighborhood can include neighbors, document links, citations, calls, and imports (`crates/gwiki/src/graph/context.rs:7-72`).

| Public surface | Role | Evidence |
| --- | --- | --- |
| `WIKI_DOC_LABEL`, `WIKI_SOURCE_LABEL`, `WIKI_TARGET_LABEL`, relationship constants, `BACKWARD_LINK_WEIGHT` | Shared graph vocabulary | `crates/gwiki/src/graph/mod.rs:13-19` |
| `WikiGraphDocument`, `WikiGraphSource`, `WikiGraphLink`, `WikiGraphCodeEdge`, `WikiGraphFacts` | Core fact model | `crates/gwiki/src/graph/mod.rs:21-67` |
| `GraphExportOptions::{available,degraded}` | Export degradation controls | `crates/gwiki/src/graph/mod.rs:69-82` |
| `GraphExport` | Serialized graph export payload | `crates/gwiki/src/graph/mod.rs:84-92` |
| `GraphContextOptions`, `GraphContextPack` | Context-pack configuration and payload | `crates/gwiki/src/graph/context.rs:7-39` |
| `GraphExportAnalytics`, `GraphAnalyticsError` | Analytics payload and validation error | `crates/gwiki/src/graph/analytics.rs:13-47` |
[crates/gwiki/src/graph/analytics.rs:14-22]
[crates/gwiki/src/graph/context.rs:8-11]
[crates/gwiki/src/graph/export.rs:12-111]
[crates/gwiki/src/graph/mod.rs:22-26]
[crates/gwiki/src/graph/analytics.rs:25-38]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/graph/analytics.rs\|crates/gwiki/src/graph/analytics.rs]] | `crates/gwiki/src/graph/analytics.rs` exposes 21 indexed API symbols. |
| [[code/files/crates/gwiki/src/graph/context.rs\|crates/gwiki/src/graph/context.rs]] | `crates/gwiki/src/graph/context.rs` exposes 35 indexed API symbols. |
| [[code/files/crates/gwiki/src/graph/export.rs\|crates/gwiki/src/graph/export.rs]] | `crates/gwiki/src/graph/export.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/graph/mod.rs\|crates/gwiki/src/graph/mod.rs]] | `crates/gwiki/src/graph/mod.rs` exposes 59 indexed API symbols. |

