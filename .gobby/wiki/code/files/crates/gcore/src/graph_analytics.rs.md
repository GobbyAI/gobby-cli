---
title: crates/gcore/src/graph_analytics.rs
type: code_file
provenance:
- file: crates/gcore/src/graph_analytics.rs
  ranges:
  - 7-11
  - 14-18
  - 21-24
  - 27-31
  - 34-38
  - 41-44
  - 47-51
  - 54-58
  - 61-68
  - 70-87
  - 90-94
  - 97-103
  - 105-374
  - 106-178
  - 180-222
  - 224-239
  - 241-300
  - 302-315
  - 317-326
  - 328-366
  - 368-373
  - 376-382
  - 384-390
  - 392-473
  - 393-401
  - 403-466
  - 468-472
  - 475-480
  - 482-484
  - 490-518
  - 521-582
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/graph_analytics.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/graph_analytics.rs` exposes 31 indexed API symbols.
[crates/gcore/src/graph_analytics.rs:7-11]
[crates/gcore/src/graph_analytics.rs:14-18]
[crates/gcore/src/graph_analytics.rs:21-24]
[crates/gcore/src/graph_analytics.rs:27-31]
[crates/gcore/src/graph_analytics.rs:34-38]
[crates/gcore/src/graph_analytics.rs:41-44]
[crates/gcore/src/graph_analytics.rs:47-51]
[crates/gcore/src/graph_analytics.rs:54-58]
[crates/gcore/src/graph_analytics.rs:61-68]
[crates/gcore/src/graph_analytics.rs:70-87]
[crates/gcore/src/graph_analytics.rs:90-94]
[crates/gcore/src/graph_analytics.rs:97-103]
[crates/gcore/src/graph_analytics.rs:105-374]
[crates/gcore/src/graph_analytics.rs:106-178]
[crates/gcore/src/graph_analytics.rs:180-222]
[crates/gcore/src/graph_analytics.rs:224-239]
[crates/gcore/src/graph_analytics.rs:241-300]
[crates/gcore/src/graph_analytics.rs:302-315]
[crates/gcore/src/graph_analytics.rs:317-326]
[crates/gcore/src/graph_analytics.rs:328-366]
[crates/gcore/src/graph_analytics.rs:368-373]
[crates/gcore/src/graph_analytics.rs:376-382]
[crates/gcore/src/graph_analytics.rs:384-390]
[crates/gcore/src/graph_analytics.rs:392-473]
[crates/gcore/src/graph_analytics.rs:393-401]
[crates/gcore/src/graph_analytics.rs:403-466]
[crates/gcore/src/graph_analytics.rs:468-472]
[crates/gcore/src/graph_analytics.rs:475-480]
[crates/gcore/src/graph_analytics.rs:482-484]
[crates/gcore/src/graph_analytics.rs:490-518]
[crates/gcore/src/graph_analytics.rs:521-582]

## API Symbols

- `AnalyticsNode` (class) component `AnalyticsNode [class]` (`3f45be99-f663-502f-9aca-7f7ed8a9c5b3`) lines 7-11 [crates/gcore/src/graph_analytics.rs:7-11]
  - Signature: `pub struct AnalyticsNode {`
  - Purpose: Indexed class `AnalyticsNode` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:7-11]
- `AnalyticsEdge` (class) component `AnalyticsEdge [class]` (`e7a03d44-3e53-50d5-a12d-76a59159e7ef`) lines 14-18 [crates/gcore/src/graph_analytics.rs:14-18]
  - Signature: `pub struct AnalyticsEdge {`
  - Purpose: Indexed class `AnalyticsEdge` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:14-18]
- `AnalyticsGraph` (class) component `AnalyticsGraph [class]` (`30b8c60a-ec5a-59d5-a6f7-cb6c6b59ffe7`) lines 21-24 [crates/gcore/src/graph_analytics.rs:21-24]
  - Signature: `pub struct AnalyticsGraph {`
  - Purpose: Indexed class `AnalyticsGraph` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:21-24]
- `Community` (class) component `Community [class]` (`f2e4de63-6edd-5ac2-b59d-f29b5473d7b1`) lines 27-31 [crates/gcore/src/graph_analytics.rs:27-31]
  - Signature: `pub struct Community {`
  - Purpose: Indexed class `Community` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:27-31]
- `CentralityScore` (class) component `CentralityScore [class]` (`91cb98ba-cc6d-5991-af6d-5f77a315a950`) lines 34-38 [crates/gcore/src/graph_analytics.rs:34-38]
  - Signature: `pub struct CentralityScore {`
  - Purpose: Indexed class `CentralityScore` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:34-38]
- `NodeRef` (class) component `NodeRef [class]` (`fbefcd01-841e-56f0-87a9-bd526cb71031`) lines 41-44 [crates/gcore/src/graph_analytics.rs:41-44]
  - Signature: `pub struct NodeRef {`
  - Purpose: Indexed class `NodeRef` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:41-44]
- `EdgeRef` (class) component `EdgeRef [class]` (`a9f11f30-a26b-594f-b069-ed65f209697d`) lines 47-51 [crates/gcore/src/graph_analytics.rs:47-51]
  - Signature: `pub struct EdgeRef {`
  - Purpose: Indexed class `EdgeRef` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:47-51]
- `Hotspot` (class) component `Hotspot [class]` (`4ff88788-2d80-546d-b0c9-079022bc6ce9`) lines 54-58 [crates/gcore/src/graph_analytics.rs:54-58]
  - Signature: `pub struct Hotspot {`
  - Purpose: Indexed class `Hotspot` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:54-58]
- `GraphAnalytics` (class) component `GraphAnalytics [class]` (`8c8d1383-2a90-5bf8-956b-016261a6cdd2`) lines 61-68 [crates/gcore/src/graph_analytics.rs:61-68]
  - Signature: `pub struct GraphAnalytics {`
  - Purpose: Indexed class `GraphAnalytics` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:61-68]
- `analyze` (function) component `analyze [function]` (`71ffb821-56d0-5a6f-b3d6-61672244c7ac`) lines 70-87 [crates/gcore/src/graph_analytics.rs:70-87]
  - Signature: `pub fn analyze(graph: &AnalyticsGraph) -> GraphAnalytics {`
  - Purpose: Indexed function `analyze` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:70-87]
- `PreparedEdge` (class) component `PreparedEdge [class]` (`f93223b1-65fc-5675-ac15-96824f28af75`) lines 90-94 [crates/gcore/src/graph_analytics.rs:90-94]
  - Signature: `struct PreparedEdge {`
  - Purpose: Indexed class `PreparedEdge` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:90-94]
- `PreparedGraph` (class) component `PreparedGraph [class]` (`bbf51435-6f8a-560f-a315-f61acd3c2e9d`) lines 97-103 [crates/gcore/src/graph_analytics.rs:97-103]
  - Signature: `struct PreparedGraph {`
  - Purpose: Indexed class `PreparedGraph` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:97-103]
- `PreparedGraph` (class) component `PreparedGraph [class]` (`8a58a122-7814-5037-88b2-9970b61d294f`) lines 105-374 [crates/gcore/src/graph_analytics.rs:105-374]
  - Signature: `impl PreparedGraph {`
  - Purpose: Indexed class `PreparedGraph` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:105-374]
- `PreparedGraph.new` (method) component `PreparedGraph.new [method]` (`fbc2e7fc-9c99-5c91-bf8a-50a6a3a84876`) lines 106-178 [crates/gcore/src/graph_analytics.rs:106-178]
  - Signature: `fn new(graph: &AnalyticsGraph) -> Self {`
  - Purpose: Indexed method `PreparedGraph.new` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:106-178]
- `PreparedGraph.centrality` (method) component `PreparedGraph.centrality [method]` (`6e001d5e-3b64-5d8b-9d3b-70ef1322b49d`) lines 180-222 [crates/gcore/src/graph_analytics.rs:180-222]
  - Signature: `fn centrality(&self) -> Vec<CentralityScore> {`
  - Purpose: Indexed method `PreparedGraph.centrality` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:180-222]
- `PreparedGraph.bridge_nodes_and_edges` (method) component `PreparedGraph.bridge_nodes_and_edges [method]` (`8f674ffe-5f30-5aa4-857e-433c4e8ad8bb`) lines 224-239 [crates/gcore/src/graph_analytics.rs:224-239]
  - Signature: `fn bridge_nodes_and_edges(&self) -> (Vec<NodeRef>, HashSet<usize>) {`
  - Purpose: Indexed method `PreparedGraph.bridge_nodes_and_edges` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:224-239]
- `PreparedGraph.communities_without_bridges` (method) component `PreparedGraph.communities_without_bridges [method]` (`2931f514-8861-54bf-893d-6014ed8ad249`) lines 241-300 [crates/gcore/src/graph_analytics.rs:241-300]
  - Signature: `fn communities_without_bridges(`
  - Purpose: Indexed method `PreparedGraph.communities_without_bridges` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:241-300]
- `PreparedGraph.god_nodes` (method) component `PreparedGraph.god_nodes [method]` (`1aec6ffd-90e9-5301-a4aa-e13742cb5930`) lines 302-315 [crates/gcore/src/graph_analytics.rs:302-315]
  - Signature: `fn god_nodes(&self, centrality: &[CentralityScore]) -> Vec<NodeRef> {`
  - Purpose: Indexed method `PreparedGraph.god_nodes` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:302-315]
- `PreparedGraph.unexpected_links` (method) component `PreparedGraph.unexpected_links [method]` (`889e5085-aae6-5dc1-836a-3a7ea9b24de3`) lines 317-326 [crates/gcore/src/graph_analytics.rs:317-326]
  - Signature: `fn unexpected_links(&self, memberships: &HashMap<String, usize>) -> Vec<EdgeRef> {`
  - Purpose: Indexed method `PreparedGraph.unexpected_links` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:317-326]
- `PreparedGraph.hotspots` (method) component `PreparedGraph.hotspots [method]` (`6d11d325-9ae1-5bd2-9c65-6221702da6d3`) lines 328-366 [crates/gcore/src/graph_analytics.rs:328-366]
  - Signature: `fn hotspots(&self) -> Vec<Hotspot> {`
  - Purpose: Indexed method `PreparedGraph.hotspots` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:328-366]
- `PreparedGraph.unique_neighbors` (method) component `PreparedGraph.unique_neighbors [method]` (`29ea3e94-9809-5fdd-9e9e-a24a7e67ddc3`) lines 368-373 [crates/gcore/src/graph_analytics.rs:368-373]
  - Signature: `fn unique_neighbors(&self, index: usize) -> HashSet<usize> {`
  - Purpose: Indexed method `PreparedGraph.unique_neighbors` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:368-373]
- `BridgeSearch` (class) component `BridgeSearch [class]` (`d2ba720b-0648-541d-9030-cf0a293c7a9f`) lines 376-382 [crates/gcore/src/graph_analytics.rs:376-382]
  - Signature: `struct BridgeSearch {`
  - Purpose: Indexed class `BridgeSearch` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:376-382]
- `BridgeFrame` (class) component `BridgeFrame [class]` (`dd1a1ecd-3a8f-55cb-8cad-35ebc7adc8fa`) lines 384-390 [crates/gcore/src/graph_analytics.rs:384-390]
  - Signature: `struct BridgeFrame {`
  - Purpose: Indexed class `BridgeFrame` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:384-390]
- `BridgeSearch` (class) component `BridgeSearch [class]` (`8f53bf1c-cd4d-5535-9d15-dc4b497d3b7b`) lines 392-473 [crates/gcore/src/graph_analytics.rs:392-473]
  - Signature: `impl BridgeSearch {`
  - Purpose: Indexed class `BridgeSearch` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:392-473]
- `BridgeSearch.new` (method) component `BridgeSearch.new [method]` (`4cd8ea08-ad33-5eb7-8547-db19dffc6cec`) lines 393-401 [crates/gcore/src/graph_analytics.rs:393-401]
  - Signature: `fn new(node_count: usize) -> Self {`
  - Purpose: Indexed method `BridgeSearch.new` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:393-401]
- `BridgeSearch.visit` (method) component `BridgeSearch.visit [method]` (`b25514e8-1cf3-5564-9e8f-369a7f7b5109`) lines 403-466 [crates/gcore/src/graph_analytics.rs:403-466]
  - Signature: `fn visit(&mut self, node: usize, parent_edge: Option<usize>, graph: &PreparedGraph) {`
  - Purpose: Indexed method `BridgeSearch.visit` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:403-466]
- `BridgeSearch.discover` (method) component `BridgeSearch.discover [method]` (`b95ab736-c23f-591f-a1c8-f23803b50934`) lines 468-472 [crates/gcore/src/graph_analytics.rs:468-472]
  - Signature: `fn discover(&mut self, node: usize) {`
  - Purpose: Indexed method `BridgeSearch.discover` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:468-472]
- `compare_edge_ref` (function) component `compare_edge_ref [function]` (`0780a2e0-f4c7-5366-98ee-b5902f20803c`) lines 475-480 [crates/gcore/src/graph_analytics.rs:475-480]
  - Signature: `fn compare_edge_ref(left: &EdgeRef, right: &EdgeRef) -> Ordering {`
  - Purpose: Indexed function `compare_edge_ref` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:475-480]
- `weight_for` (function) component `weight_for [function]` (`92034e6b-ffa5-5ec8-b302-1968c61f4a39`) lines 482-484 [crates/gcore/src/graph_analytics.rs:482-484]
  - Signature: `fn weight_for(node: &NodeRef, graph: &PreparedGraph) -> f64 {`
  - Purpose: Indexed function `weight_for` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:482-484]
- `seeded_graph` (function) component `seeded_graph [function]` (`2170090c-35df-57e1-b0b0-b83a0d1a23c6`) lines 490-518 [crates/gcore/src/graph_analytics.rs:490-518]
  - Signature: `fn seeded_graph() -> AnalyticsGraph {`
  - Purpose: Indexed function `seeded_graph` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:490-518]
- `graph_analytics_detects_seeded_graph_measures` (function) component `graph_analytics_detects_seeded_graph_measures [function]` (`a7c67947-c722-52a7-bf17-255c8508b132`) lines 521-582 [crates/gcore/src/graph_analytics.rs:521-582]
  - Signature: `fn graph_analytics_detects_seeded_graph_measures() {`
  - Purpose: Indexed function `graph_analytics_detects_seeded_graph_measures` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:521-582]

