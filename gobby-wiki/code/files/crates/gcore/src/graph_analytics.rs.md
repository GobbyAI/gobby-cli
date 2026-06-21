---
title: crates/gcore/src/graph_analytics.rs
type: code_file
provenance:
- file: crates/gcore/src/graph_analytics.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/graph_analytics.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/graph_analytics.rs` exposes 33 indexed API symbols.

## How it fits

`crates/gcore/src/graph_analytics.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AnalyticsNode` | class | AnalyticsNode is a public struct representing an analytics node characterized by a unique string identifier, categorical type field, and floating-point weight metric. [crates/gcore/src/graph_analytics.rs:9-13] |
| `AnalyticsEdge` | class | AnalyticsEdge is a struct representing a weighted, directed edge in a graph with string-identified source and target nodes and a categorical edge type. [crates/gcore/src/graph_analytics.rs:21-26] |
| `AnalyticsGraph` | class | AnalyticsGraph is a public struct that represents a graph data structure composed of vectors of AnalyticsNode and AnalyticsEdge elements. [crates/gcore/src/graph_analytics.rs:29-32] |
| `Community` | class | A public struct that represents a community node grouping, containing a unique identifier, a collection of node references, and an associated floating-point weight value. [crates/gcore/src/graph_analytics.rs:35-39] |
| `CentralityScore` | class | 'CentralityScore' is a public struct that encapsulates a node reference, its vertex degree (connection count), and a computed centrality metric as a floating-point scalar value. [crates/gcore/src/graph_analytics.rs:42-46] |
| `NodeRef` | class | # Summary 'NodeRef' is a public struct that represents a typed reference to a node, consisting of two public String fields: 'id' (unique identifier) and 'kind' (type classifier). [crates/gcore/src/graph_analytics.rs:49-52] |
| `EdgeRef` | class | EdgeRef is a struct representing a typed directed edge in a graph, comprising source and target node identifiers and an edge kind classifier, each stored as a String field. [crates/gcore/src/graph_analytics.rs:55-59] |
| `Hotspot` | class | Hotspot is a public struct that associates a NodeRef with a frequency count and a floating-point weight metric. [crates/gcore/src/graph_analytics.rs:62-66] |
| `GraphAnalytics` | class | GraphAnalytics is a struct that aggregates graph analysis results, including detected communities, node centrality scores, bridge nodes, highly-connected nodes, anomalous edges, and activity hotspots. [crates/gcore/src/graph_analytics.rs:69-76] |
| `analyze` | function | # Summary The 'analyze' function transforms an 'AnalyticsGraph' into a 'GraphAnalytics' struct by computing structural graph metrics including community detection, node centrality, bridge identification, anomalous link detection, and hotspot analysis. [crates/gcore/src/graph_analytics.rs:78-95] |
| `weight_for_kind` | function | Returns a numeric weight for a given relationship type string, prioritizing structural containment (3.0) with decreasing weights for inheritance (2.5), dependencies (2.0), and references (1.0), defaulting to 1.0 for unknown types. [crates/gcore/src/graph_analytics.rs:105-116] |
| `PreparedEdge` | class | # Summary 'PreparedEdge' is a struct representing a weighted directed graph edge with source and target node indices (as 'usize'), a floating-point weight value, and a reference to the original edge data. [crates/gcore/src/graph_analytics.rs:119-124] |
| `PreparedGraph` | class | PreparedGraph is a graph data structure storing nodes as references, edge weights in dual representations (vector and HashMap), explicit prepared edges, and an adjacency list of indexed tuples for efficient graph computation. [crates/gcore/src/graph_analytics.rs:127-133] |
| `PreparedGraph::new` | method | Constructs an optimized graph representation by extracting and deduplicating nodes and edges from the input 'AnalyticsGraph', establishing ID-to-index mappings, and filtering self-loops for efficient indexed access. [crates/gcore/src/graph_analytics.rs:136-209] |
| `PreparedGraph::centrality` | method | # Summary Returns a vector of 'CentralityScore' objects containing each node's degree and normalized degree centrality (degree/(n-1)), sorted by degree, score, node weight, and node ID. [crates/gcore/src/graph_analytics.rs:211-253] |
| `PreparedGraph::bridge_nodes_and_edges` | method | # Summary This method performs a depth-first search traversal to identify articulation points (critical vertices) and bridge edges (critical edges) in a graph, returning the articulation point nodes sorted by ID and the corresponding bridge edge indices. [crates/gcore/src/graph_analytics.rs:255-270] |
| `PreparedGraph::communities` | method | Applies Leiden-based community detection to the graph with edge-weight sanitization and returns a sorted vector of communities along with a HashMap mapping node IDs to their community indices. [crates/gcore/src/graph_analytics.rs:279-347] |
| `PreparedGraph::god_nodes` | method | This method returns all nodes with the maximum degree centrality from the input scores, provided the maximum degree is at least 3; otherwise it returns an empty vector. [crates/gcore/src/graph_analytics.rs:349-362] |
| `PreparedGraph::unexpected_links` | method | Returns all edges whose source and target nodes are assigned to different membership groups. [crates/gcore/src/graph_analytics.rs:364-373] |
| `PreparedGraph::hotspots` | method | This method identifies nodes with the maximum edge degree (minimum threshold of 3) and returns them as 'Hotspot' objects sorted by descending frequency and weight, then ascending node ID. [crates/gcore/src/graph_analytics.rs:375-413] |
| `PreparedGraph::unique_neighbors` | method | Returns a HashSet of unique neighbor node indices by extracting the first element of each tuple stored in the adjacency list entry at the specified index. [crates/gcore/src/graph_analytics.rs:415-420] |
| `BridgeSearch` | class | BridgeSearch stores the intermediate state of Tarjan's algorithm for identifying bridges and articulation points in a graph by maintaining discovery indices, low-link values, and their corresponding critical vertices and edges. [crates/gcore/src/graph_analytics.rs:423-429] |
| `BridgeFrame` | class | BridgeFrame is a struct that maintains per-node state during depth-first search traversal for detecting bridges and articulation points in an undirected graph. [crates/gcore/src/graph_analytics.rs:431-437] |
| `BridgeSearch::new` | method | Initializes an articulation point and bridge edge detector with discovery and low-value tracking vectors, an iteration counter, and empty result sets for a graph with the specified node count. [crates/gcore/src/graph_analytics.rs:440-448] |

_5 more symbol(s) not shown — run `gcode outline crates/gcore/src/graph_analytics.rs` for the full list._

_Verified by 4 in-file unit tests._

