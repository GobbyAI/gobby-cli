---
title: crates/gwiki/src/graph/analytics.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/analytics.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/analytics.rs

Module: [[code/modules/crates/gwiki/src/graph|crates/gwiki/src/graph]]

## Overview

`crates/gwiki/src/graph/analytics.rs` exposes 21 indexed API symbols.

## How it fits

`crates/gwiki/src/graph/analytics.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphAnalyticsError` | type | Indexed type `GraphAnalyticsError` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:14-22] |
| `GraphAnalyticsError::fmt` | method | This method formats the 'DuplicateNode' variant of the enum by writing a descriptive error message detailing the node's identifier and its conflicting kind and weight metadata to the given formatter. [crates/gwiki/src/graph/analytics.rs:25-38] |
| `GraphExportAnalytics` | class | The 'GraphExportAnalytics' struct aggregates topological and structural graph analysis metrics for export, containing vectors of detected communities, centrality measurements, bridge and god nodes, unexpected links, and hotspots. [crates/gwiki/src/graph/analytics.rs:44-51] |
| `GraphExportCommunity` | class | 'GraphExportCommunity' is a public Rust structure representing a graph community defined by a unique string identifier, a vector of node references belonging to the community, and a double-precision floating-point weight. [crates/gwiki/src/graph/analytics.rs:54-58] |
| `GraphExportCentrality` | class | The 'GraphExportCentrality' struct represents the centrality metrics of an exported graph node, encapsulating a reference to the node, its degree, and its calculated centrality score. [crates/gwiki/src/graph/analytics.rs:61-65] |
| `GraphExportNodeRef` | class | The 'GraphExportNodeRef' struct represents a public reference to an exported graph node, containing its unique string identifier and kind. [crates/gwiki/src/graph/analytics.rs:68-71] |
| `GraphExportEdgeRef` | class | The 'GraphExportEdgeRef' public struct represents a reference to a directed graph edge, containing public string fields that specify the source identifier, target identifier, and classification kind of the edge. [crates/gwiki/src/graph/analytics.rs:74-78] |
| `GraphExportHotspot` | class | The 'GraphExportHotspot' struct encapsulates a node reference, its occurrence frequency, and its associated weight to represent a significant point of interest within a graph export. [crates/gwiki/src/graph/analytics.rs:81-85] |
| `analyze_facts` | function | The 'analyze_facts' function builds an analytical graph representation from the provided 'WikiGraphFacts', executes a core graph analysis on it, and returns the compiled results mapped to a 'GraphExportAnalytics' structure. [crates/gwiki/src/graph/analytics.rs:87-91] |
| `analytics_graph_from_memory` | function | Constructs an 'AnalyticsGraph' from a reference to a 'MemoryWikiGraph' by delegating to 'analytics_graph_from_facts' with the graph's facts. [crates/gwiki/src/graph/analytics.rs:94-98] |
| `analytics_graph_from_facts` | function | The 'analytics_graph_from_facts' function constructs an 'AnalyticsGraph' from a 'WikiGraphFacts' input by generating and weighting nodes representing documents, sources, citations, and link targets, and mapping their relational edges with associated weights. [crates/gwiki/src/graph/analytics.rs:100-161] |
| `insert_node` | function | This function inserts a new 'AnalyticsNode' with the specified ID, kind, and weight into a mutable 'BTreeMap' of nodes, returning 'Ok(())' if the node is successfully added or already exists with identical attributes, and returning a 'DuplicateNode' error if an existing node with the same ID has a different kind or weight. [crates/gwiki/src/graph/analytics.rs:163-184] |
| `GraphExportAnalytics::from_core` | method | The 'from_core' method constructs an instance of the implementing type by consuming a 'GraphAnalytics' instance and mapping its internal vectors of communities, centrality, bridges, god nodes, unexpected links, and hotspots into their corresponding export-compatible representation types. [crates/gwiki/src/graph/analytics.rs:187-220] |
| `GraphExportCommunity::from_core` | method | This method constructs an instance of the implementing type by mapping a 'Community' structure's 'id' and 'weight' directly, and converting its collection of 'nodes' into a collection of 'GraphExportNodeRef' instances. [crates/gwiki/src/graph/analytics.rs:224-234] |
| `GraphExportCentrality::from_core` | method | The 'from_core' method constructs an instance of 'Self' from a 'CentralityScore' by converting its node field into a 'GraphExportNodeRef' and copying its degree and score fields. [crates/gwiki/src/graph/analytics.rs:238-244] |
| `GraphExportHotspot::from_core` | method | The 'from_core' method instantiates and returns a new instance of the implementing type by converting the input 'Hotspot''s 'node' field into a 'GraphExportNodeRef' and directly assigning its 'frequency' and 'weight' fields. [crates/gwiki/src/graph/analytics.rs:248-254] |
| `GraphExportNodeRef::from` | method | The 'from' method constructs and returns an instance of the implementing type by mapping the 'id' and 'kind' fields from the provided 'NodeRef'. [crates/gwiki/src/graph/analytics.rs:258-263] |
| `GraphExportEdgeRef::from` | method | The 'from' method converts an 'EdgeRef' into the implementing struct by initializing its 'source', 'target', and 'kind' fields with the corresponding values from the referenced edge. [crates/gwiki/src/graph/analytics.rs:267-273] |

_Verified by 3 in-file unit tests._

