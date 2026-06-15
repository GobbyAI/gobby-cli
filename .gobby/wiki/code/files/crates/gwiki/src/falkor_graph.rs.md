---
title: crates/gwiki/src/falkor_graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph.rs
  ranges:
  - 30-32
  - 34-44
  - 47-50
  - 52-56
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file is the shared entry point for FalkorDB-backed wiki graph loading, wiring together the code-edge, graph-boost, sync, and wiki-facts submodules and re-exporting their loaders. It also defines small data containers for code-graph edge results and graph-boost input: `SharedCodeGraphTruncation` tracks which edge components were truncated, `SharedCodeGraphEdges` pairs the loaded `WikiGraphCodeEdge` list with that truncation state, and `GraphBoostData` groups documents, links, and an optional degradation flag for search-driven graph boost processing.
[crates/gwiki/src/falkor_graph.rs:30-32]
[crates/gwiki/src/falkor_graph.rs:34-44]
[crates/gwiki/src/falkor_graph.rs:35-39]
[crates/gwiki/src/falkor_graph.rs:41-43]
[crates/gwiki/src/falkor_graph.rs:47-50]

## API Symbols

- `SharedCodeGraphTruncation` (class) component `SharedCodeGraphTruncation [class]` (`67dccd58-9748-507d-8f26-11964234f1bd`) lines 30-32 [crates/gwiki/src/falkor_graph.rs:30-32]
  - Signature: `pub(crate) struct SharedCodeGraphTruncation {`
  - Purpose: 'SharedCodeGraphTruncation' is a crate-visible struct that stores a 'Vec<String>' of component identifiers representing a truncated shared code graph. [crates/gwiki/src/falkor_graph.rs:30-32]
- `SharedCodeGraphTruncation` (class) component `SharedCodeGraphTruncation [class]` (`c3ce656d-2864-5a0b-9882-bf139af4eec1`) lines 34-44 [crates/gwiki/src/falkor_graph.rs:34-44]
  - Signature: `impl SharedCodeGraphTruncation {`
  - Purpose: 'SharedCodeGraphTruncation' is a wrapper that stores a deduplicated set of component names and reports truncation when that set is non-empty. [crates/gwiki/src/falkor_graph.rs:34-44]
- `SharedCodeGraphTruncation.from_components` (method) component `SharedCodeGraphTruncation.from_components [method]` (`13ca50bb-1550-53d7-8123-7863b14ac381`) lines 35-39 [crates/gwiki/src/falkor_graph.rs:35-39]
  - Signature: `fn from_components(components: BTreeSet<String>) -> Self {`
  - Purpose: Constructs 'Self' by consuming the input 'BTreeSet<String>' and collecting its elements into the 'components' field. [crates/gwiki/src/falkor_graph.rs:35-39]
- `SharedCodeGraphTruncation.is_truncated` (method) component `SharedCodeGraphTruncation.is_truncated [method]` (`dcf621dd-689e-522c-b4a8-4741f6bde6c6`) lines 41-43 [crates/gwiki/src/falkor_graph.rs:41-43]
  - Signature: `pub(crate) fn is_truncated(&self) -> bool {`
  - Purpose: Returns 'true' when 'self.components' is non-empty, and 'false' when it is empty. [crates/gwiki/src/falkor_graph.rs:41-43]
- `SharedCodeGraphEdges` (class) component `SharedCodeGraphEdges [class]` (`1c2569ac-fea1-5805-98e9-8962f5de4a48`) lines 47-50 [crates/gwiki/src/falkor_graph.rs:47-50]
  - Signature: `pub(crate) struct SharedCodeGraphEdges {`
  - Purpose: 'SharedCodeGraphEdges' is an internal container struct that holds a vector of 'WikiGraphCodeEdge' values plus a 'SharedCodeGraphTruncation' status describing whether the edge set was truncated. [crates/gwiki/src/falkor_graph.rs:47-50]
- `GraphBoostData` (class) component `GraphBoostData [class]` (`6b9b3c0b-9446-55db-b959-89d74ea2b865`) lines 52-56 [crates/gwiki/src/falkor_graph.rs:52-56]
  - Signature: `pub(crate) struct GraphBoostData {`
  - Purpose: 'GraphBoostData' is a crate-visible container for graph-boost search input, holding a list of 'GraphBoostDocument's, a list of 'GraphBoostLink's, and an optional 'DegradationKind' flag. [crates/gwiki/src/falkor_graph.rs:52-56]

