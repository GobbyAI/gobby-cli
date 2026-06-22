---
title: crates/gwiki/src/falkor_graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/falkor_graph.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gwiki/src/falkor_graph.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SharedCodeGraphTruncation` | class | 'SharedCodeGraphTruncation' is an internal struct that stores a 'Vec<String>' of 'components' representing truncated portions of a shared code graph. [crates/gwiki/src/falkor_graph.rs:30-32] |
| `SharedCodeGraphTruncation::from_components` | method | Constructs 'Self' by consuming the input 'BTreeSet<String>' and collecting its elements into the 'components' field. [crates/gwiki/src/falkor_graph.rs:35-39] |
| `SharedCodeGraphTruncation::is_truncated` | method | Returns 'true' when 'self.components' is non-empty, and 'false' otherwise. [crates/gwiki/src/falkor_graph.rs:41-43] |
| `SharedCodeGraphEdges` | class | 'SharedCodeGraphEdges' is an internal struct that groups a vector of 'WikiGraphCodeEdge' values with a 'SharedCodeGraphTruncation' status to represent a possibly truncated set of shared code-graph edges. [crates/gwiki/src/falkor_graph.rs:47-50] |
| `GraphBoostData` | class | 'GraphBoostData' is an internal aggregate struct that groups graph-boost documents and links with an optional 'DegradationKind' flag for search ranking behavior. [crates/gwiki/src/falkor_graph.rs:52-56] |

