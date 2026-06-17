---
title: crates/gcore/src/graph_analytics.rs
type: code_file
provenance:
- file: crates/gcore/src/graph_analytics.rs
  ranges:
  - 9-13
  - 21-26
  - 29-32
  - 35-39
  - 42-46
  - 49-52
  - 55-59
  - 62-66
  - 69-76
  - 78-95
  - 105-116
  - 119-124
  - 127-133
  - 136-209
  - 211-253
  - 255-270
  - 279-347
  - 349-362
  - 364-373
  - 375-413
  - 415-420
  - 423-429
  - 431-437
  - 440-448
  - 450-513
  - 515-519
  - 522-527
  - 529-531
  - 537-566
  - 569-630
  - 633-659
  - 662-670
  - 673-690
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/graph_analytics.rs:9-13](crates/gcore/src/graph_analytics.rs#L9-L13), [crates/gcore/src/graph_analytics.rs:21-26](crates/gcore/src/graph_analytics.rs#L21-L26), [crates/gcore/src/graph_analytics.rs:29-32](crates/gcore/src/graph_analytics.rs#L29-L32), [crates/gcore/src/graph_analytics.rs:35-39](crates/gcore/src/graph_analytics.rs#L35-L39), [crates/gcore/src/graph_analytics.rs:42-46](crates/gcore/src/graph_analytics.rs#L42-L46), [crates/gcore/src/graph_analytics.rs:49-52](crates/gcore/src/graph_analytics.rs#L49-L52), [crates/gcore/src/graph_analytics.rs:55-59](crates/gcore/src/graph_analytics.rs#L55-L59), [crates/gcore/src/graph_analytics.rs:62-66](crates/gcore/src/graph_analytics.rs#L62-L66), [crates/gcore/src/graph_analytics.rs:69-76](crates/gcore/src/graph_analytics.rs#L69-L76), [crates/gcore/src/graph_analytics.rs:78-95](crates/gcore/src/graph_analytics.rs#L78-L95), [crates/gcore/src/graph_analytics.rs:105-116](crates/gcore/src/graph_analytics.rs#L105-L116), [crates/gcore/src/graph_analytics.rs:119-124](crates/gcore/src/graph_analytics.rs#L119-L124), [crates/gcore/src/graph_analytics.rs:127-133](crates/gcore/src/graph_analytics.rs#L127-L133), [crates/gcore/src/graph_analytics.rs:136-209](crates/gcore/src/graph_analytics.rs#L136-L209), [crates/gcore/src/graph_analytics.rs:211-253](crates/gcore/src/graph_analytics.rs#L211-L253), [crates/gcore/src/graph_analytics.rs:255-270](crates/gcore/src/graph_analytics.rs#L255-L270), [crates/gcore/src/graph_analytics.rs:279-347](crates/gcore/src/graph_analytics.rs#L279-L347), [crates/gcore/src/graph_analytics.rs:349-362](crates/gcore/src/graph_analytics.rs#L349-L362), [crates/gcore/src/graph_analytics.rs:364-373](crates/gcore/src/graph_analytics.rs#L364-L373), [crates/gcore/src/graph_analytics.rs:375-413](crates/gcore/src/graph_analytics.rs#L375-L413), [crates/gcore/src/graph_analytics.rs:415-420](crates/gcore/src/graph_analytics.rs#L415-L420), [crates/gcore/src/graph_analytics.rs:423-429](crates/gcore/src/graph_analytics.rs#L423-L429), [crates/gcore/src/graph_analytics.rs:431-437](crates/gcore/src/graph_analytics.rs#L431-L437), [crates/gcore/src/graph_analytics.rs:440-448](crates/gcore/src/graph_analytics.rs#L440-L448), [crates/gcore/src/graph_analytics.rs:450-513](crates/gcore/src/graph_analytics.rs#L450-L513), [crates/gcore/src/graph_analytics.rs:515-519](crates/gcore/src/graph_analytics.rs#L515-L519), [crates/gcore/src/graph_analytics.rs:522-527](crates/gcore/src/graph_analytics.rs#L522-L527), [crates/gcore/src/graph_analytics.rs:529-531](crates/gcore/src/graph_analytics.rs#L529-L531), [crates/gcore/src/graph_analytics.rs:537-566](crates/gcore/src/graph_analytics.rs#L537-L566), [crates/gcore/src/graph_analytics.rs:569-630](crates/gcore/src/graph_analytics.rs#L569-L630), [crates/gcore/src/graph_analytics.rs:633-659](crates/gcore/src/graph_analytics.rs#L633-L659), [crates/gcore/src/graph_analytics.rs:662-670](crates/gcore/src/graph_analytics.rs#L662-L670), [crates/gcore/src/graph_analytics.rs:673-690](crates/gcore/src/graph_analytics.rs#L673-L690)

</details>

# crates/gcore/src/graph_analytics.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Transport-free graph analytics for code and knowledge graphs. The file defines the core node, edge, community, centrality, hotspot, and result types, then builds an `analyze` pipeline around `PreparedGraph` that derives community structure, centrality, bridge nodes, “god nodes,” unexpected links, and hotspots from an `AnalyticsGraph`; supporting helpers normalize edge weights, prepare edges and graph state, and implement bridge/community discovery and test coverage for seeded, empty, and singleton graphs.
[crates/gcore/src/graph_analytics.rs:9-13]
[crates/gcore/src/graph_analytics.rs:21-26]
[crates/gcore/src/graph_analytics.rs:29-32]
[crates/gcore/src/graph_analytics.rs:35-39]
[crates/gcore/src/graph_analytics.rs:42-46]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `AnalyticsNode` | class | `pub struct AnalyticsNode {` | `AnalyticsNode [class]` | `5e0cf63a-589e-50e3-9bb9-42837c1eedc7` | 9-13 [crates/gcore/src/graph_analytics.rs:9-13] | Indexed class `AnalyticsNode` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:9-13] |
| `AnalyticsEdge` | class | `pub struct AnalyticsEdge {` | `AnalyticsEdge [class]` | `6eb388ec-c0a7-5a5a-a5e8-030d4384bf53` | 21-26 [crates/gcore/src/graph_analytics.rs:21-26] | Indexed class `AnalyticsEdge` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:21-26] |
| `AnalyticsGraph` | class | `pub struct AnalyticsGraph {` | `AnalyticsGraph [class]` | `d11e1b70-fe8d-5c7a-98a1-af504b477f43` | 29-32 [crates/gcore/src/graph_analytics.rs:29-32] | Indexed class `AnalyticsGraph` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:29-32] |
| `Community` | class | `pub struct Community {` | `Community [class]` | `d5f16621-8500-5034-953c-5f704ffcd800` | 35-39 [crates/gcore/src/graph_analytics.rs:35-39] | Indexed class `Community` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:35-39] |
| `CentralityScore` | class | `pub struct CentralityScore {` | `CentralityScore [class]` | `1c408331-ae69-5696-86a8-675523a6795d` | 42-46 [crates/gcore/src/graph_analytics.rs:42-46] | Indexed class `CentralityScore` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:42-46] |
| `NodeRef` | class | `pub struct NodeRef {` | `NodeRef [class]` | `71827d8a-5c74-5403-a858-97ca13253f48` | 49-52 [crates/gcore/src/graph_analytics.rs:49-52] | Indexed class `NodeRef` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:49-52] |
| `EdgeRef` | class | `pub struct EdgeRef {` | `EdgeRef [class]` | `98d3e18b-1132-5441-8b1c-637cfc53bf18` | 55-59 [crates/gcore/src/graph_analytics.rs:55-59] | Indexed class `EdgeRef` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:55-59] |
| `Hotspot` | class | `pub struct Hotspot {` | `Hotspot [class]` | `f24c9da2-6f9f-59e6-acb3-846de6988f49` | 62-66 [crates/gcore/src/graph_analytics.rs:62-66] | Indexed class `Hotspot` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:62-66] |
| `GraphAnalytics` | class | `pub struct GraphAnalytics {` | `GraphAnalytics [class]` | `ff6bff83-9b95-5659-8303-4621c59922ad` | 69-76 [crates/gcore/src/graph_analytics.rs:69-76] | Indexed class `GraphAnalytics` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:69-76] |
| `analyze` | function | `pub fn analyze(graph: &AnalyticsGraph) -> GraphAnalytics {` | `analyze [function]` | `35b571b4-8fcb-5b27-9e9b-037ae3c50996` | 78-95 [crates/gcore/src/graph_analytics.rs:78-95] | Indexed function `analyze` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:78-95] |
| `weight_for_kind` | function | `pub fn weight_for_kind(kind: &str) -> f64 {` | `weight_for_kind [function]` | `6f3d1805-00e5-51a3-be16-cbfc63427445` | 105-116 [crates/gcore/src/graph_analytics.rs:105-116] | Indexed function `weight_for_kind` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:105-116] |
| `PreparedEdge` | class | `struct PreparedEdge {` | `PreparedEdge [class]` | `82a41ccd-56af-58db-97d1-6eddb45c6604` | 119-124 [crates/gcore/src/graph_analytics.rs:119-124] | Indexed class `PreparedEdge` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:119-124] |
| `PreparedGraph` | class | `struct PreparedGraph {` | `PreparedGraph [class]` | `9c2c7e3e-044d-5250-9b3a-86f053f32ffa` | 127-133 [crates/gcore/src/graph_analytics.rs:127-133] | Indexed class `PreparedGraph` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:127-133] |
| `PreparedGraph::new` | method | `fn new(graph: &AnalyticsGraph) -> Self {` | `PreparedGraph::new [method]` | `9c078bda-644e-5951-a52d-07481e385f08` | 136-209 [crates/gcore/src/graph_analytics.rs:136-209] | Indexed method `PreparedGraph::new` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:136-209] |
| `PreparedGraph::centrality` | method | `fn centrality(&self) -> Vec<CentralityScore> {` | `PreparedGraph::centrality [method]` | `24f1352d-2038-5bf9-b7bc-dfef25743902` | 211-253 [crates/gcore/src/graph_analytics.rs:211-253] | Indexed method `PreparedGraph::centrality` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:211-253] |
| `PreparedGraph::bridge_nodes_and_edges` | method | `fn bridge_nodes_and_edges(&self) -> (Vec<NodeRef>, HashSet<usize>) {` | `PreparedGraph::bridge_nodes_and_edges [method]` | `3b687583-dd6b-523d-b7b4-6117a5ac9de5` | 255-270 [crates/gcore/src/graph_analytics.rs:255-270] | Indexed method `PreparedGraph::bridge_nodes_and_edges` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:255-270] |
| `PreparedGraph::communities` | method | `fn communities(&self) -> (Vec<Community>, HashMap<String, usize>) {` | `PreparedGraph::communities [method]` | `36111feb-be2f-5e91-9445-a0c841b6fbaa` | 279-347 [crates/gcore/src/graph_analytics.rs:279-347] | Indexed method `PreparedGraph::communities` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:279-347] |
| `PreparedGraph::god_nodes` | method | `fn god_nodes(&self, centrality: &[CentralityScore]) -> Vec<NodeRef> {` | `PreparedGraph::god_nodes [method]` | `90354b31-e48b-54e0-afc2-250bbd650897` | 349-362 [crates/gcore/src/graph_analytics.rs:349-362] | Indexed method `PreparedGraph::god_nodes` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:349-362] |
| `PreparedGraph::unexpected_links` | method | `fn unexpected_links(&self, memberships: &HashMap<String, usize>) -> Vec<EdgeRef> {` | `PreparedGraph::unexpected_links [method]` | `ea991c5f-08fe-50ff-90ff-a6088c580e44` | 364-373 [crates/gcore/src/graph_analytics.rs:364-373] | Indexed method `PreparedGraph::unexpected_links` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:364-373] |
| `PreparedGraph::hotspots` | method | `fn hotspots(&self) -> Vec<Hotspot> {` | `PreparedGraph::hotspots [method]` | `acb4db68-fb8d-5850-ad86-a1e1e2a2e661` | 375-413 [crates/gcore/src/graph_analytics.rs:375-413] | Indexed method `PreparedGraph::hotspots` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:375-413] |
| `PreparedGraph::unique_neighbors` | method | `fn unique_neighbors(&self, index: usize) -> HashSet<usize> {` | `PreparedGraph::unique_neighbors [method]` | `f9ffbd77-582f-5028-adad-0cbe1fab8419` | 415-420 [crates/gcore/src/graph_analytics.rs:415-420] | Indexed method `PreparedGraph::unique_neighbors` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:415-420] |
| `BridgeSearch` | class | `struct BridgeSearch {` | `BridgeSearch [class]` | `2b234826-9765-550d-ac74-98871171dedb` | 423-429 [crates/gcore/src/graph_analytics.rs:423-429] | Indexed class `BridgeSearch` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:423-429] |
| `BridgeFrame` | class | `struct BridgeFrame {` | `BridgeFrame [class]` | `99ec7137-9c5a-5c59-9c03-10ee27e32d04` | 431-437 [crates/gcore/src/graph_analytics.rs:431-437] | Indexed class `BridgeFrame` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:431-437] |
| `BridgeSearch::new` | method | `fn new(node_count: usize) -> Self {` | `BridgeSearch::new [method]` | `c8b3c92b-8d3e-5f8d-9e50-d859ab4d156d` | 440-448 [crates/gcore/src/graph_analytics.rs:440-448] | Indexed method `BridgeSearch::new` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:440-448] |
| `BridgeSearch::visit` | method | `fn visit(&mut self, node: usize, parent_edge: Option<usize>, graph: &PreparedGraph) {` | `BridgeSearch::visit [method]` | `db4fdfff-9f45-5b09-8edc-1697d8776568` | 450-513 [crates/gcore/src/graph_analytics.rs:450-513] | Indexed method `BridgeSearch::visit` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:450-513] |
| `BridgeSearch::discover` | method | `fn discover(&mut self, node: usize) {` | `BridgeSearch::discover [method]` | `56e27dc2-9f4d-54b5-9d35-cb85f6c23add` | 515-519 [crates/gcore/src/graph_analytics.rs:515-519] | Indexed method `BridgeSearch::discover` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:515-519] |
| `compare_edge_ref` | function | `fn compare_edge_ref(left: &EdgeRef, right: &EdgeRef) -> Ordering {` | `compare_edge_ref [function]` | `5522b0f0-648c-5d2d-8287-16bd0ced6cd3` | 522-527 [crates/gcore/src/graph_analytics.rs:522-527] | Indexed function `compare_edge_ref` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:522-527] |
| `weight_for` | function | `fn weight_for(node: &NodeRef, graph: &PreparedGraph) -> f64 {` | `weight_for [function]` | `695ff75f-453b-5b22-923d-43c9827b7f9f` | 529-531 [crates/gcore/src/graph_analytics.rs:529-531] | Indexed function `weight_for` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:529-531] |
| `seeded_graph` | function | `fn seeded_graph() -> AnalyticsGraph {` | `seeded_graph [function]` | `95554fea-f1c8-5ea9-953b-0df9dcbd30d1` | 537-566 [crates/gcore/src/graph_analytics.rs:537-566] | Indexed function `seeded_graph` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:537-566] |
| `graph_analytics_detects_seeded_graph_measures` | function | `fn graph_analytics_detects_seeded_graph_measures() {` | `graph_analytics_detects_seeded_graph_measures [function]` | `26bda180-baaa-50c6-b44d-d2b3f356e29b` | 569-630 [crates/gcore/src/graph_analytics.rs:569-630] | Indexed function `graph_analytics_detects_seeded_graph_measures` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:569-630] |
| `weight_for_kind_covers_observed_aliases_case_insensitively` | function | `fn weight_for_kind_covers_observed_aliases_case_insensitively() {` | `weight_for_kind_covers_observed_aliases_case_insensitively [function]` | `e0f1139d-88df-53f0-8dbd-c60492ba6709` | 633-659 [crates/gcore/src/graph_analytics.rs:633-659] | Indexed function `weight_for_kind_covers_observed_aliases_case_insensitively` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:633-659] |
| `analyze_empty_graph_does_not_panic` | function | `fn analyze_empty_graph_does_not_panic() {` | `analyze_empty_graph_does_not_panic [function]` | `26d97f79-c73e-5731-9dee-94fd8150a390` | 662-670 [crates/gcore/src/graph_analytics.rs:662-670] | Indexed function `analyze_empty_graph_does_not_panic` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:662-670] |
| `analyze_nodes_without_edges_yields_singleton_communities` | function | `fn analyze_nodes_without_edges_yields_singleton_communities() {` | `analyze_nodes_without_edges_yields_singleton_communities [function]` | `7fe49062-e349-5a75-9cd1-ab45ff873c5b` | 673-690 [crates/gcore/src/graph_analytics.rs:673-690] | Indexed function `analyze_nodes_without_edges_yields_singleton_communities` in `crates/gcore/src/graph_analytics.rs`. [crates/gcore/src/graph_analytics.rs:673-690] |
