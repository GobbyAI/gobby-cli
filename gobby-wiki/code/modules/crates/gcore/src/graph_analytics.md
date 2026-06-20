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

`crates/gcore/src/graph_analytics/leiden.rs` implements a std-only, deterministic weighted Leiden community detection kernel over dense integer node indices. It is intentionally decoupled from public `AnalyticsGraph` and `Community` types so the algorithm can be tested in isolation, while the higher-level facade in `graph_analytics.rs` adapts external node IDs and memberships into this integer-index representation (crates/gcore/src/graph_analytics/leiden.rs:1-7).

The core flow follows the three Leiden phases: local moving, refinement to guarantee internally connected communities, and aggregation, repeating until the graph no longer coarsens (crates/gcore/src/graph_analytics/leiden.rs:7-12). The implementation avoids RNG entirely: choices are deterministic ascending strict-improvement greedy steps, making results reproducible across runs (crates/gcore/src/graph_analytics/leiden.rs:10-13).

`LeidenGraph` represents a weighted undirected graph with dense node IDs, sorted adjacency lists, weighted strengths, and total edge weight. Construction folds duplicate edges, sorts neighbors for determinism, and preserves the invariant `Σ strength == 2·total_weight`; self-loops count twice toward node strength and once toward total graph weight, which also keeps aggregation behavior consistent (crates/gcore/src/graph_analytics/leiden.rs:25-49).

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `DEFAULT_GAMMA` | constant | Default resolution parameter γ for standard modularity (crates/gcore/src/graph_analytics/leiden.rs:16-17). |
| `EPS` | constant | Strict-improvement threshold for accepting moves (crates/gcore/src/graph_analytics/leiden.rs:19-20). |
| `MAX_LEVELS` | constant | Hard cap on aggregation depth as a recursion backstop (crates/gcore/src/graph_analytics/leiden.rs:22-23). |
| `LeidenGraph` | struct | Dense weighted undirected graph used by the Leiden kernel (crates/gcore/src/graph_analytics/leiden.rs:25-39). |
| `LeidenGraph::new` | constructor | Builds the graph from an edge list, folding duplicate pairs and sorting adjacency for determinism (crates/gcore/src/graph_analytics/leiden.rs:42-49). |
[crates/gcore/src/graph_analytics/leiden.rs:32-40]
[crates/gcore/src/graph_analytics/leiden.rs:45-72]
[crates/gcore/src/graph_analytics/leiden.rs:76-79]
[crates/gcore/src/graph_analytics/leiden.rs:82-87]
[crates/gcore/src/graph_analytics/leiden.rs:94-184]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/graph_analytics/leiden.rs\|crates/gcore/src/graph_analytics/leiden.rs]] | `crates/gcore/src/graph_analytics/leiden.rs` exposes 36 indexed API symbols. |

