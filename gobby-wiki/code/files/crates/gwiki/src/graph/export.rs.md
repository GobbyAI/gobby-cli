---
title: crates/gwiki/src/graph/export.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/export.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/export.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/graph/export.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/graph/export.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `WikiGraphFacts::export_graph` | method | The 'export_graph' method compiles a unified 'GraphExport' representation by extracting deduplicated nodes for documents, sources, and citations, and establishing trust and audit edges that map support and citation relationships among them. [crates/gwiki/src/graph/export.rs:12-111] |
| `render_graph_report` | function | The 'render_graph_report' function generates a Markdown-formatted report from a 'GraphExport' reference, summarizing node and edge counts, degraded sources, graph analytics such as community and centrality metrics, and a Mermaid diagram representing the graph structure. [crates/gwiki/src/graph/export.rs:114-190] |

_Verified by 2 in-file unit tests._

