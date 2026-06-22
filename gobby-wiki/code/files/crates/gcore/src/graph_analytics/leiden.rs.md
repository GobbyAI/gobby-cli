---
title: crates/gcore/src/graph_analytics/leiden.rs
type: code_file
provenance:
- file: crates/gcore/src/graph_analytics/leiden.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/graph_analytics/leiden.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/graph_analytics/leiden.rs` exposes 36 indexed API symbols.

## How it fits

`crates/gcore/src/graph_analytics/leiden.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `LeidenGraph` | class | LeidenGraph encodes a weighted undirected graph via sorted adjacency lists, per-vertex weighted degrees, and accumulated edge weight for the Leiden community detection algorithm. [crates/gcore/src/graph_analytics/leiden.rs:32-40] |
| `LeidenGraph::new` | method | **Summary:** Constructs a weighted undirected graph by building a sparse adjacency list from an edge list and computing the weighted degree (strength) for each vertex, with self-loops contributing double to the degree metric. [crates/gcore/src/graph_analytics/leiden.rs:45-72] |
| `Partition` | class | 'Partition' is a struct that stores community membership assignments for nodes (via 'community_of') and their corresponding aggregated sigma values (via 'sigma_tot') as parallel vectors. [crates/gcore/src/graph_analytics/leiden.rs:76-79] |
| `Partition::singletons` | method | This method initializes a partition structure where each of the n nodes is assigned to its own singleton community, with total community strengths set to the input graph's node strength values. [crates/gcore/src/graph_analytics/leiden.rs:82-87] |
| `local_moving` | function | Performs the local-moving phase of the Leiden algorithm by greedily reassigning each node to the community that maximizes modularity gain (parameterized by gamma), returning whether any node relocations occurred. [crates/gcore/src/graph_analytics/leiden.rs:94-184] |
| `refine_partition` | function | Refines a partition by greedily merging singleton nodes into refined sub-communities within parent communities, optimizing modularity subject to a γ-parameterized well-connectedness constraint. [crates/gcore/src/graph_analytics/leiden.rs:195-277] |
| `aggregate_graph` | function | Coarsens a graph by contracting refined communities into super-nodes with accumulated inter-community edge weights, returning the aggregated graph, an inherited partition, and a mapping from original nodes to super-nodes. [crates/gcore/src/graph_analytics/leiden.rs:282-336] |
| `renumber_dense` | function | # Summary Remaps community assignments to consecutive integers starting from zero and computes the cumulative node strength for each community. [crates/gcore/src/graph_analytics/leiden.rs:339-359] |
| `detect_communities` | function | Detects communities by applying the Leiden algorithm, which iteratively optimizes modularity through local node movement, partition refinement, and hierarchical graph aggregation with backprojection, returning a zero-indexed community assignment vector. [crates/gcore/src/graph_analytics/leiden.rs:366-407] |
| `dense_relabel` | function | Remaps arbitrary cluster membership values in-place to dense consecutive integers starting from 0, preserving equivalence class structure. [crates/gcore/src/graph_analytics/leiden.rs:410-425] |
| `assert_strength_invariant` | function | Asserts that the sum of all node strengths in a LeidenGraph equals twice the total edge weight (the strength invariant: Σstrength = 2m) within floating-point tolerance of 1e-9. [crates/gcore/src/graph_analytics/leiden.rs:433-440] |
| `assert_communities_connected` | function | Asserts that each community forms a connected component by verifying via depth-first search that all nodes with identical membership values are reachable from one another using only edges between same-community nodes. [crates/gcore/src/graph_analytics/leiden.rs:443-477] |
| `detect` | function | Detects communities in a weighted graph with n nodes using the Leiden algorithm with default modularity resolution, returning a vector of community identifiers for each node. [crates/gcore/src/graph_analytics/leiden.rs:479-482] |
| `community_count` | function | Returns the count of zero-indexed communities as the maximum membership value incremented by one, or zero if the input is empty. [crates/gcore/src/graph_analytics/leiden.rs:484-486] |
| `triangle` | function | # Summary Returns a vector of three tuples, each representing a unit-weighted directed edge, that form a triangle cycle connecting three consecutive vertices starting at the given base index. [crates/gcore/src/graph_analytics/leiden.rs:488-494] |
| `clique` | function | Generates all edges of a complete graph on 'size' nodes (numbered from 'base' to 'base + size - 1') with uniform 'weight' on each edge. [crates/gcore/src/graph_analytics/leiden.rs:496-504] |
| `modularity` | function | # Function Summary Calculates modularity of a community partition as the intra-community edge density minus gamma-scaled expected edge density under a configuration null model. **Technical detail:** Returns '(internal_edges / total_edges) - gamma × Σ(community_strength / total_edges)²', where gamma is a resolution parameter tuning community granularity detection. [crates/gcore/src/graph_analytics/leiden.rs:511-531] |
| `karate_club` | function | This function returns the Karate Club social network as a vector of weighted edge tuples (source_node, target_node, weight), where each edge is assigned a uniform weight of 1.0. [crates/gcore/src/graph_analytics/leiden.rs:536-570] |
| `assert_no_improving_single_move` | function | This function asserts that the given community membership partition is locally optimal with respect to single-node moves by verifying that relocating any node to any alternative or new community does not increase the modularity value. [crates/gcore/src/graph_analytics/leiden.rs:577-595] |

_Verified by 17 in-file unit tests._

