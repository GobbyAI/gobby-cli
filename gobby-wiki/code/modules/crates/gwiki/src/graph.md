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

## crates/gwiki/src/graph

### Responsibilities

The `graph` module is gwiki's central knowledge-graph layer. It defines the canonical data model for wiki content as a directed graph — documents, source files, inter-document links, and code-level edges — and provides the machinery to export that model to serialisable graph payloads and to generate per-document neighbourhood packs for AI context windows. Three public constants families name the node labels, relationship kinds, and numeric weights used uniformly across serialisation and analysis: `WIKI_DOC_LABEL`, `WIKI_SOURCE_LABEL`, `WIKI_TARGET_LABEL` for nodes; `WIKI_LINKS_TO_REL`, `MENTIONS_TARGET_REL`, `SUPPORTS_REL` for edges; and `BACKWARD_LINK_WEIGHT` (0.8) for link scoring mod.rs:12-18.

### Key Data Structures

`WikiGraphFacts` (mod.rs:63-68) is the central aggregation type, collecting `WikiGraphDocument`, `WikiGraphSource`, `WikiGraphLink`, and `WikiGraphCodeEdge` records before any export or analysis step. A link's target is either `WikiGraphLinkTarget::Resolved(PathBuf)` or `WikiGraphLinkTarget::Unresolved(String)` mod.rs:37-41, and both branches are handled explicitly during export. Export behaviour is controlled by `GraphExportOptions`, which carries a `degraded_sources` list and is constructed via `GraphExportOptions::available()` (full fidelity) or `GraphExportOptions::degraded(…)` (partial data) mod.rs:71-81.

| Public type | Role | Defined at |
|---|---|---|
| `WikiGraphFacts` | Bag of all graph facts before export | mod.rs:63 |
| `WikiGraphDocument` | A wiki page node | mod.rs:22 |
| `WikiGraphSource` | A source/citation file node | mod.rs:28 |
| `WikiGraphLink` | A directed link edge | mod.rs:44 |
| `WikiGraphCodeEdge` | A code-level relationship edge | mod.rs:50 |
| `GraphExport` | Serialisable full-graph payload | mod.rs:84 |
| `GraphExportOptions` | Controls degraded-mode export | mod.rs:71 |
| `GraphContextPack` | Per-page neighbourhood payload | context.rs:33 |
| `GraphContextOptions` | Controls degraded/truncated context | context.rs:8 |
| `GraphExportAnalytics` | Analytics summary embedded in export | analytics.rs:47 |

| Constant | Value | Purpose |
|---|---|---|
| `WIKI_DOC_LABEL` | `"WikiDoc"` | Node label for wiki documents |
| `WIKI_SOURCE_LABEL` | `"WikiSource"` | Node label for source files |
| `WIKI_TARGET_LABEL` | `"WikiTarget"` | Node label for link targets |
| `WIKI_LINKS_TO_REL` | `"WIKI_LINKS_TO"` | Edge kind for document links |
| `MENTIONS_TARGET_REL` | `"MENTIONS_TARGET"` | Edge kind for mentions |
| `SUPPORTS_REL` | `"SUPPORTS"` | Edge kind for source support |
| `BACKWARD_LINK_WEIGHT` | `0.8` | Weight applied to reverse links |

### Key Flows

The primary export flow begins with a populated `WikiGraphFacts` value. Calling `WikiGraphFacts::export_graph(options)` (export.rs:12) iterates over documents, sources, and links, deduplicates nodes via a `BTreeSet` of IDs, and assembles typed edge lists (`trust`, `audit`, wiki links, code edges). Resolved and unresolved link targets produce different node kinds — unresolved targets get their own `unresolved_target_node` variant export.rs:54-68. After node/edge assembly the method invokes `analytics` to compute centrality, communities, bridges, god nodes, hotspots, and unexpected cross-community links, embedding the result as `GraphExport::analytics`. The top-level re-export `render_graph_report` (mod.rs:10, export.rs) serialises the completed `GraphExport` to a human- or machine-readable report.

The context flow is separate: `context.rs` builds `GraphContextPack` values scoped to a single document or path. `GraphContextOptions` accepts `degraded_sources` and `truncated_components` lists (context.rs:8-28) so callers can signal incomplete data. The resulting `GraphContextPack` contains `GraphContextNeighborhood` records — each carrying incoming/outgoing `GraphContextNeighbor` links, `doc_links`, `citations`, `calls`, and `imports` — together with `warnings` and `recommendations`, all serialisable via `serde::Serialize` context.rs:33-80.

### Collaboration Points

Internally the module is split into three sub-modules: `analytics` (public), `context` (public), and `export` (private, re-exporting only `render_graph_report`). The analytics sub-module delegates computation entirely to `gobby_core::graph_analytics`, importing `AnalyticsGraph`, `AnalyticsEdge`, `GraphAnalytics`, `analyze`, `weight_for_kind`, and related types analytics.rs:3-6 — making `gobby_core` a hard external dependency for any graph analysis. The `graph` module itself imports `crate::search::SearchScope` (mod.rs:4) to scope every node and edge to a search domain, and `uuid::Uuid` for stable identifier generation mod.rs:5. Higher-level gwiki code constructs `WikiGraphFacts` externally and passes it into this module's export or context APIs; no inbound call sites are visible in the supplied excerpts, but the public surface (`export_graph`, `render_graph_report`, `GraphContextPack` builders, `GraphExportOptions`, `GraphContextOptions`) constitutes the integration boundary consumed by gwiki's command layer.
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

