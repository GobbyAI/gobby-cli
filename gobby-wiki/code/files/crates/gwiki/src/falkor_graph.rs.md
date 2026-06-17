---
title: crates/gwiki/src/falkor_graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph.rs
  ranges:
  - 30-32
  - 35-39
  - 41-43
  - 47-50
  - 52-56
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/falkor_graph.rs:30-32](crates/gwiki/src/falkor_graph.rs#L30-L32), [crates/gwiki/src/falkor_graph.rs:35-39](crates/gwiki/src/falkor_graph.rs#L35-L39), [crates/gwiki/src/falkor_graph.rs:41-43](crates/gwiki/src/falkor_graph.rs#L41-L43), [crates/gwiki/src/falkor_graph.rs:47-50](crates/gwiki/src/falkor_graph.rs#L47-L50), [crates/gwiki/src/falkor_graph.rs:52-56](crates/gwiki/src/falkor_graph.rs#L52-L56)

</details>

# crates/gwiki/src/falkor_graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file is the central FalkorDB graph integration module for the wiki graph, wiring together submodules that load code edges, graph boost data, wiki facts, and sync scope from Postgres. It also defines the graph name and truncation/provenance constants, plus small data types that package loaded code edges with truncation metadata and graph-boost payloads so the rest of the crate can detect when shared code data was capped and carry the resulting documents, links, and degradation state together.
[crates/gwiki/src/falkor_graph.rs:30-32]
[crates/gwiki/src/falkor_graph.rs:35-39]
[crates/gwiki/src/falkor_graph.rs:41-43]
[crates/gwiki/src/falkor_graph.rs:47-50]
[crates/gwiki/src/falkor_graph.rs:52-56]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SharedCodeGraphTruncation` | class | `pub(crate) struct SharedCodeGraphTruncation {` | `SharedCodeGraphTruncation [class]` | `67dccd58-9748-507d-8f26-11964234f1bd` | 30-32 [crates/gwiki/src/falkor_graph.rs:30-32] | Indexed class `SharedCodeGraphTruncation` in `crates/gwiki/src/falkor_graph.rs`. [crates/gwiki/src/falkor_graph.rs:30-32] |
| `SharedCodeGraphTruncation::from_components` | method | `fn from_components(components: BTreeSet<String>) -> Self {` | `SharedCodeGraphTruncation::from_components [method]` | `13ca50bb-1550-53d7-8123-7863b14ac381` | 35-39 [crates/gwiki/src/falkor_graph.rs:35-39] | Indexed method `SharedCodeGraphTruncation::from_components` in `crates/gwiki/src/falkor_graph.rs`. [crates/gwiki/src/falkor_graph.rs:35-39] |
| `SharedCodeGraphTruncation::is_truncated` | method | `pub(crate) fn is_truncated(&self) -> bool {` | `SharedCodeGraphTruncation::is_truncated [method]` | `dcf621dd-689e-522c-b4a8-4741f6bde6c6` | 41-43 [crates/gwiki/src/falkor_graph.rs:41-43] | Indexed method `SharedCodeGraphTruncation::is_truncated` in `crates/gwiki/src/falkor_graph.rs`. [crates/gwiki/src/falkor_graph.rs:41-43] |
| `SharedCodeGraphEdges` | class | `pub(crate) struct SharedCodeGraphEdges {` | `SharedCodeGraphEdges [class]` | `1c2569ac-fea1-5805-98e9-8962f5de4a48` | 47-50 [crates/gwiki/src/falkor_graph.rs:47-50] | Indexed class `SharedCodeGraphEdges` in `crates/gwiki/src/falkor_graph.rs`. [crates/gwiki/src/falkor_graph.rs:47-50] |
| `GraphBoostData` | class | `pub(crate) struct GraphBoostData {` | `GraphBoostData [class]` | `6b9b3c0b-9446-55db-b959-89d74ea2b865` | 52-56 [crates/gwiki/src/falkor_graph.rs:52-56] | Indexed class `GraphBoostData` in `crates/gwiki/src/falkor_graph.rs`. [crates/gwiki/src/falkor_graph.rs:52-56] |
