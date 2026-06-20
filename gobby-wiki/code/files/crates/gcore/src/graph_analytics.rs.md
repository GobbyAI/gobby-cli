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
| `AnalyticsNode` | class | Indexed class `AnalyticsNode` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:9-13] |
| `AnalyticsEdge` | class | Indexed class `AnalyticsEdge` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:21-26] |
| `AnalyticsGraph` | class | Indexed class `AnalyticsGraph` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:29-32] |
| `Community` | class | Indexed class `Community` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:35-39] |
| `CentralityScore` | class | Indexed class `CentralityScore` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:42-46] |
| `NodeRef` | class | Indexed class `NodeRef` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:49-52] |
| `EdgeRef` | class | Indexed class `EdgeRef` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:55-59] |
| `Hotspot` | class | Indexed class `Hotspot` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:62-66] |
| `GraphAnalytics` | class | Indexed class `GraphAnalytics` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:69-76] |
| `analyze` | function | Indexed function `analyze` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:78-95] |
| `weight_for_kind` | function | Indexed function `weight_for_kind` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:105-116] |
| `PreparedEdge` | class | Indexed class `PreparedEdge` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:119-124] |
| `PreparedGraph` | class | Indexed class `PreparedGraph` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:127-133] |
| `PreparedGraph::new` | method | Indexed method `PreparedGraph::new` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:136-209] |
| `PreparedGraph::centrality` | method | Indexed method `PreparedGraph::centrality` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:211-253] |
| `PreparedGraph::bridge_nodes_and_edges` | method | Indexed method `PreparedGraph::bridge_nodes_and_edges` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:255-270] |
| `PreparedGraph::communities` | method | Indexed method `PreparedGraph::communities` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:279-347] |
| `PreparedGraph::god_nodes` | method | Indexed method `PreparedGraph::god_nodes` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:349-362] |
| `PreparedGraph::unexpected_links` | method | Indexed method `PreparedGraph::unexpected_links` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:364-373] |
| `PreparedGraph::hotspots` | method | Indexed method `PreparedGraph::hotspots` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:375-413] |
| `PreparedGraph::unique_neighbors` | method | Indexed method `PreparedGraph::unique_neighbors` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:415-420] |
| `BridgeSearch` | class | Indexed class `BridgeSearch` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:423-429] |
| `BridgeFrame` | class | Indexed class `BridgeFrame` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:431-437] |
| `BridgeSearch::new` | method | Indexed method `BridgeSearch::new` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:440-448] |

_5 more symbol(s) not shown — run `gcode outline crates/gcore/src/graph_analytics.rs` for the full list._

_Verified by 4 in-file unit tests._

