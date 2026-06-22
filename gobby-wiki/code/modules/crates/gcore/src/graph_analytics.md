---
title: crates/gcore/src/graph_analytics
type: code_module
provenance:
- file: crates/gcore/src/graph_analytics/leiden.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/graph_analytics

Parent: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

## crates/gcore/src/graph_analytics

### Responsibilities

This module provides the algorithmic core for graph community detection inside the `gcore` crate. Its single file, `leiden.rs`, implements the three-phase Leiden method (Traag, Waltman & van Eck, 2019): local moving, refinement (which guarantees internally-connected communities), and aggregation, iterated until the graph no longer coarsens leiden.rs:1-11. The implementation is deliberately decoupled from the public `AnalyticsGraph` and `Community` types so it can be unit-tested in isolation; a façade living in the parent `graph_analytics.rs` is responsible for translating external node ids and membership structs into the integer-index representation this kernel expects leiden.rs:3-5.

### Key Design Decisions

The entire algorithm is deterministic: no RNG is involved. Every move selection uses a greedy ascending strict-improvement step (gain must exceed `EPS = 1e-12`) so the same input always produces identical community assignments leiden.rs:8-10, 18. A hard recursion cap (`MAX_LEVELS = 64`) guards against pathological aggregation loops leiden.rs:20-21. The central data structure is `LeidenGraph`, a dense integer-indexed weighted undirected graph. It enforces the invariant `Σ strength == 2·total_weight` throughout construction and aggregation by double-counting self-loop contributions to node strength while counting them once toward `total_weight` leiden.rs:26-39. Duplicate `(u, v)` edges in the input are folded by summation; adjacency lists are sorted by neighbor index for further determinism leiden.rs:46-59.

### Public API Surface

All symbols are `pub(super)`, meaning they are accessible only to the parent `graph_analytics` module.

| Symbol | Kind | Description |
|---|---|---|
| `DEFAULT_GAMMA` | `const f64` | Resolution parameter γ = 1.0 (standard modularity) leiden.rs:15 |
| `EPS` | `const f64` | Strict-improvement threshold = 1e-12 leiden.rs:18 |
| `MAX_LEVELS` | `const usize` | Maximum aggregation depth = 64 leiden.rs:21 |
| `LeidenGraph` | `struct` | Dense integer-indexed weighted undirected graph leiden.rs:32 |
| `LeidenGraph::new` | `fn` | Constructs graph from edge list `(u, v, w)`, deduplicating and sorting leiden.rs:46 |

### Collaboration Points

The module is a pure computational kernel with no external crate dependencies beyond `std` (`BTreeMap`, `VecDeque`) leiden.rs:12. It is not called from outside `gcore`; all entry points are `pub(super)`. The parent module (`graph_analytics.rs`) acts as the sole consumer, adapting public-facing node identifiers to the `0..n` integer space required here, then translating the resulting community membership vector back into the `Community` and `AnalyticsGraph` types exposed to the rest of the crate leiden.rs:3-5. This layered design keeps the algorithm fully testable without constructing any higher-level graph abstractions.
[crates/gcore/src/graph_analytics/leiden.rs:32-40]
[crates/gcore/src/graph_analytics/leiden.rs:45-72]
[crates/gcore/src/graph_analytics/leiden.rs:76-79]
[crates/gcore/src/graph_analytics/leiden.rs:82-87]
[crates/gcore/src/graph_analytics/leiden.rs:94-184]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/graph_analytics/leiden.rs\|crates/gcore/src/graph_analytics/leiden.rs]] | `crates/gcore/src/graph_analytics/leiden.rs` exposes 36 indexed API symbols. |

