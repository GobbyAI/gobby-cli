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
  - 135-421
  - 423-429
  - 431-437
  - 439-520
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

# crates/gcore/src/graph_analytics.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Implements transport-free graph analytics for code and knowledge graphs. It defines the core graph data model (`AnalyticsNode`, `AnalyticsEdge`, `AnalyticsGraph`) plus analysis outputs (`Community`, `CentralityScore`, `Hotspot`, `GraphAnalytics`) and lightweight references (`NodeRef`, `EdgeRef`). The `analyze` entry point normalizes an input graph into a `PreparedGraph`, then combines community detection, degree centrality, articulation/bridge detection, high-degree “god” nodes, cross-community links, and hotspots into one `GraphAnalytics` result. Supporting helpers map edge kinds to weights, compare and weight references, and build a seeded test graph with tests that verify the analysis behavior and empty-graph handling.
[crates/gcore/src/graph_analytics.rs:9-13]
[crates/gcore/src/graph_analytics.rs:21-26]
[crates/gcore/src/graph_analytics.rs:29-32]
[crates/gcore/src/graph_analytics.rs:35-39]
[crates/gcore/src/graph_analytics.rs:42-46]

## API Symbols

- `AnalyticsNode` (class) component `AnalyticsNode [class]` (`5e0cf63a-589e-50e3-9bb9-42837c1eedc7`) lines 9-13 [crates/gcore/src/graph_analytics.rs:9-13]
  - Signature: `pub struct AnalyticsNode {`
  - Purpose: 'AnalyticsNode' is a Rust struct representing an analytics graph node with a string 'id', a string 'kind' discriminator, and a floating-point 'weight' value. [crates/gcore/src/graph_analytics.rs:9-13]
- `AnalyticsEdge` (class) component `AnalyticsEdge [class]` (`6eb388ec-c0a7-5a5a-a5e8-030d4384bf53`) lines 21-26 [crates/gcore/src/graph_analytics.rs:21-26]
  - Signature: `pub struct AnalyticsEdge {`
  - Purpose: 'AnalyticsEdge' is a data structure representing a directed weighted edge in an analytics graph, storing source and target node identifiers, an edge kind label, and a floating-point weight. [crates/gcore/src/graph_analytics.rs:21-26]
- `AnalyticsGraph` (class) component `AnalyticsGraph [class]` (`d11e1b70-fe8d-5c7a-98a1-af504b477f43`) lines 29-32 [crates/gcore/src/graph_analytics.rs:29-32]
  - Signature: `pub struct AnalyticsGraph {`
  - Purpose: 'AnalyticsGraph' is a data structure that stores an analytics graph as two collections: a 'Vec<AnalyticsNode>' of vertices and a 'Vec<AnalyticsEdge>' of directed relationships between them. [crates/gcore/src/graph_analytics.rs:29-32]
- `Community` (class) component `Community [class]` (`d5f16621-8500-5034-953c-5f704ffcd800`) lines 35-39 [crates/gcore/src/graph_analytics.rs:35-39]
  - Signature: `pub struct Community {`
  - Purpose: 'Community' is a struct that represents a node cluster identified by 'id', containing a collection of 'NodeRef' members in 'nodes' and an associated floating-point 'weight'. [crates/gcore/src/graph_analytics.rs:35-39]
- `CentralityScore` (class) component `CentralityScore [class]` (`1c408331-ae69-5696-86a8-675523a6795d`) lines 42-46 [crates/gcore/src/graph_analytics.rs:42-46]
  - Signature: `pub struct CentralityScore {`
  - Purpose: 'CentralityScore' is a Rust struct that associates a 'NodeRef' with its integer degree and a floating-point centrality 'score'. [crates/gcore/src/graph_analytics.rs:42-46]
- `NodeRef` (class) component `NodeRef [class]` (`71827d8a-5c74-5403-a858-97ca13253f48`) lines 49-52 [crates/gcore/src/graph_analytics.rs:49-52]
  - Signature: `pub struct NodeRef {`
  - Purpose: 'NodeRef' is a simple Rust struct that represents a node reference via two owned strings: 'id' for the node identifier and 'kind' for the node type/category. [crates/gcore/src/graph_analytics.rs:49-52]
- `EdgeRef` (class) component `EdgeRef [class]` (`98d3e18b-1132-5441-8b1c-637cfc53bf18`) lines 55-59 [crates/gcore/src/graph_analytics.rs:55-59]
  - Signature: `pub struct EdgeRef {`
  - Purpose: 'EdgeRef' is a struct that represents a directed graph edge by storing the source node ID, target node ID, and edge kind as strings. [crates/gcore/src/graph_analytics.rs:55-59]
- `Hotspot` (class) component `Hotspot [class]` (`f24c9da2-6f9f-59e6-acb3-846de6988f49`) lines 62-66 [crates/gcore/src/graph_analytics.rs:62-66]
  - Signature: `pub struct Hotspot {`
  - Purpose: 'Hotspot' is a struct representing a weighted occurrence target, pairing a 'NodeRef' with its 'frequency' count and a floating-point 'weight' score. [crates/gcore/src/graph_analytics.rs:62-66]
- `GraphAnalytics` (class) component `GraphAnalytics [class]` (`ff6bff83-9b95-5659-8303-4621c59922ad`) lines 69-76 [crates/gcore/src/graph_analytics.rs:69-76]
  - Signature: `pub struct GraphAnalytics {`
  - Purpose: 'GraphAnalytics' is an aggregate analysis record for a graph, storing detected communities, centrality rankings, bridge nodes, high-degree “god” nodes, unexpected edges, and hotspot regions. [crates/gcore/src/graph_analytics.rs:69-76]
- `analyze` (function) component `analyze [function]` (`35b571b4-8fcb-5b27-9e9b-037ae3c50996`) lines 78-95 [crates/gcore/src/graph_analytics.rs:78-95]
  - Signature: `pub fn analyze(graph: &AnalyticsGraph) -> GraphAnalytics {`
  - Purpose: Constructs a 'PreparedGraph' from 'graph', computes bridges, communities and memberships, centrality, god nodes, unexpected links, and hotspots, then returns those metrics assembled into a 'GraphAnalytics' value. [crates/gcore/src/graph_analytics.rs:78-95]
- `weight_for_kind` (function) component `weight_for_kind [function]` (`6f3d1805-00e5-51a3-be16-cbfc63427445`) lines 105-116 [crates/gcore/src/graph_analytics.rs:105-116]
  - Signature: `pub fn weight_for_kind(kind: &str) -> f64 {`
  - Purpose: 'weight_for_kind' maps a relationship kind string case-insensitively to a predefined 'f64' weight, assigning higher scores to structural and inheritance edges and defaulting unknown kinds to '1.0'. [crates/gcore/src/graph_analytics.rs:105-116]
- `PreparedEdge` (class) component `PreparedEdge [class]` (`82a41ccd-56af-58db-97d1-6eddb45c6604`) lines 119-124 [crates/gcore/src/graph_analytics.rs:119-124]
  - Signature: `struct PreparedEdge {`
  - Purpose: 'PreparedEdge' is a data carrier for a graph edge that stores the source and target node indices, a floating-point weight, and an associated 'EdgeRef' handle. [crates/gcore/src/graph_analytics.rs:119-124]
- `PreparedGraph` (class) component `PreparedGraph [class]` (`9c2c7e3e-044d-5250-9b3a-86f053f32ffa`) lines 127-133 [crates/gcore/src/graph_analytics.rs:127-133]
  - Signature: `struct PreparedGraph {`
  - Purpose: 'PreparedGraph' is a precomputed graph container that stores node references, parallel edge-weight representations, and an index-based adjacency list for efficient lookup by node position and node ID. [crates/gcore/src/graph_analytics.rs:127-133]
- `PreparedGraph` (class) component `PreparedGraph [class]` (`693d78b7-ac94-56cb-a23a-3998508db90b`) lines 135-421 [crates/gcore/src/graph_analytics.rs:135-421]
  - Signature: `impl PreparedGraph {`
  - Purpose: 'PreparedGraph' is a normalized, index-backed projection of an 'AnalyticsGraph' that sorts and deduplicates nodes by ID, stores parallel node/weight/index maps, and filters, indexes, sorts, and deduplicates edges into internal 'PreparedEdge' records. [crates/gcore/src/graph_analytics.rs:135-421]
- `PreparedGraph.new` (method) component `PreparedGraph.new [method]` (`9c078bda-644e-5951-a52d-07481e385f08`) lines 136-209 [crates/gcore/src/graph_analytics.rs:136-209]
  - Signature: `fn new(graph: &AnalyticsGraph) -> Self {`
  - Purpose: 'new' normalizes an 'AnalyticsGraph' by sorting and deduplicating nodes by 'id', building 'NodeRef', weight, and index lookup tables, then filtering, remapping, sorting, and deduplicating edges to known non-self-loop endpoints before constructing 'Self'. [crates/gcore/src/graph_analytics.rs:136-209]
- `PreparedGraph.centrality` (method) component `PreparedGraph.centrality [method]` (`24f1352d-2038-5bf9-b7bc-dfef25743902`) lines 211-253 [crates/gcore/src/graph_analytics.rs:211-253]
  - Signature: `fn centrality(&self) -> Vec<CentralityScore> {`
  - Purpose: Computes each node’s normalized degree centrality as 'unique_neighbors(index).len() / (nodes.len() - 1)' with a zero-denominator guard, then returns a 'Vec<CentralityScore>' sorted by descending degree, descending score, descending node weight, and ascending node ID. [crates/gcore/src/graph_analytics.rs:211-253]
- `PreparedGraph.bridge_nodes_and_edges` (method) component `PreparedGraph.bridge_nodes_and_edges [method]` (`3b687583-dd6b-523d-b7b4-6117a5ac9de5`) lines 255-270 [crates/gcore/src/graph_analytics.rs:255-270]
  - Signature: `fn bridge_nodes_and_edges(&self) -> (Vec<NodeRef>, HashSet<usize>) {`
  - Purpose: Performs a full graph traversal to identify articulation-point nodes and bridge edge indices, clones the corresponding 'NodeRef's, sorts them by 'id', and returns them with the discovered bridge-edge set. [crates/gcore/src/graph_analytics.rs:255-270]
- `PreparedGraph.communities` (method) component `PreparedGraph.communities [method]` (`36111feb-be2f-5e91-9445-a0c841b6fbaa`) lines 279-347 [crates/gcore/src/graph_analytics.rs:279-347]
  - Signature: `fn communities(&self) -> (Vec<Community>, HashMap<String, usize>) {`
  - Purpose: Returns an empty result for graphs with no nodes, otherwise sanitizes edge weights to positive finite values, runs Leiden community detection when there is usable total weight or assigns each node to its own community, then groups and deterministically sorts node indices into 'Community' values while producing a 'HashMap<String, usize>' from node IDs to community indices. [crates/gcore/src/graph_analytics.rs:279-347]
- `PreparedGraph.god_nodes` (method) component `PreparedGraph.god_nodes [method]` (`90354b31-e48b-54e0-afc2-250bbd650897`) lines 349-362 [crates/gcore/src/graph_analytics.rs:349-362]
  - Signature: `fn god_nodes(&self, centrality: &[CentralityScore]) -> Vec<NodeRef> {`
  - Purpose: Returns the 'NodeRef's whose 'degree' equals the maximum degree in 'centrality', but only when that maximum is at least '3'; otherwise it returns an empty 'Vec'. [crates/gcore/src/graph_analytics.rs:349-362]
- `PreparedGraph.unexpected_links` (method) component `PreparedGraph.unexpected_links [method]` (`ea991c5f-08fe-50ff-90ff-a6088c580e44`) lines 364-373 [crates/gcore/src/graph_analytics.rs:364-373]
  - Signature: `fn unexpected_links(&self, memberships: &HashMap<String, usize>) -> Vec<EdgeRef> {`
  - Purpose: Returns a cloned 'EdgeRef' for each edge whose source and target nodes map to different membership IDs in 'memberships', effectively filtering for cross-membership links. [crates/gcore/src/graph_analytics.rs:364-373]
- `PreparedGraph.hotspots` (method) component `PreparedGraph.hotspots [method]` (`acb4db68-fb8d-5850-ad86-a1e1e2a2e661`) lines 375-413 [crates/gcore/src/graph_analytics.rs:375-413]
  - Signature: `fn hotspots(&self) -> Vec<Hotspot> {`
  - Purpose: Computes per-node incident-edge counts, returns an empty vector if the graph is empty or the maximum count is below 3, otherwise collects all nodes whose count equals the maximum into 'Hotspot' values with their cloned node, frequency, and weight, then sorts them by descending frequency, descending weight, and ascending node id. [crates/gcore/src/graph_analytics.rs:375-413]
- `PreparedGraph.unique_neighbors` (method) component `PreparedGraph.unique_neighbors [method]` (`f9ffbd77-582f-5028-adad-0cbe1fab8419`) lines 415-420 [crates/gcore/src/graph_analytics.rs:415-420]
  - Signature: `fn unique_neighbors(&self, index: usize) -> HashSet<usize> {`
  - Purpose: Returns a 'HashSet<usize>' containing the distinct neighbor indices referenced by 'self.adjacency[index]', ignoring any associated edge data. [crates/gcore/src/graph_analytics.rs:415-420]
- `BridgeSearch` (class) component `BridgeSearch [class]` (`2b234826-9765-550d-ac74-98871171dedb`) lines 423-429 [crates/gcore/src/graph_analytics.rs:423-429]
  - Signature: `struct BridgeSearch {`
  - Purpose: 'BridgeSearch' stores the mutable state for a graph bridge/articulation-point search, tracking the DFS index counter, per-vertex discovery and low-link values, and the resulting sets of articulation points and bridge edges. [crates/gcore/src/graph_analytics.rs:423-429]
- `BridgeFrame` (class) component `BridgeFrame [class]` (`99ec7137-9c5a-5c59-9c03-10ee27e32d04`) lines 431-437 [crates/gcore/src/graph_analytics.rs:431-437]
  - Signature: `struct BridgeFrame {`
  - Purpose: 'BridgeFrame' is a DFS traversal state record that tracks a node’s parent edge, the next neighbor index to explore, the number of child subtrees, and whether the node has been identified as an articulation point. [crates/gcore/src/graph_analytics.rs:431-437]
- `BridgeSearch` (class) component `BridgeSearch [class]` (`e375b350-005c-5aa8-9fe6-99b5a5f017c2`) lines 439-520 [crates/gcore/src/graph_analytics.rs:439-520]
  - Signature: `impl BridgeSearch {`
  - Purpose: 'BridgeSearch' is an iterative depth-first search over a 'PreparedGraph' that computes discovery and low-link times to identify articulation points and bridge edges, storing the results in 'HashSet's. [crates/gcore/src/graph_analytics.rs:439-520]
- `BridgeSearch.new` (method) component `BridgeSearch.new [method]` (`c8b3c92b-8d3e-5f8d-9e50-d859ab4d156d`) lines 440-448 [crates/gcore/src/graph_analytics.rs:440-448]
  - Signature: `fn new(node_count: usize) -> Self {`
  - Purpose: Initializes a new graph-analysis state with 'next' set to '0', 'discovery' prefilled with 'None' for 'node_count' nodes, 'low' prefilled with '0', and empty 'articulation_points' and 'bridge_edges' sets. [crates/gcore/src/graph_analytics.rs:440-448]
- `BridgeSearch.visit` (method) component `BridgeSearch.visit [method]` (`db4fdfff-9f45-5b09-8edc-1697d8776568`) lines 450-513 [crates/gcore/src/graph_analytics.rs:450-513]
  - Signature: `fn visit(&mut self, node: usize, parent_edge: Option<usize>, graph: &PreparedGraph) {`
  - Purpose: 'visit' performs an iterative depth-first traversal from 'node' that skips already discovered vertices, records discovery/low-link state, tracks child counts and articulation candidates, and updates bridge/articulation-point analysis via an explicit stack. [crates/gcore/src/graph_analytics.rs:450-513]
- `BridgeSearch.discover` (method) component `BridgeSearch.discover [method]` (`56e27dc2-9f4d-54b5-9d35-cb85f6c23add`) lines 515-519 [crates/gcore/src/graph_analytics.rs:515-519]
  - Signature: `fn discover(&mut self, node: usize) {`
  - Purpose: Marks 'node' as discovered by assigning the current discovery index to both 'self.discovery[node]' and 'self.low[node]', then increments 'self.next' for the next vertex. [crates/gcore/src/graph_analytics.rs:515-519]
- `compare_edge_ref` (function) component `compare_edge_ref [function]` (`5522b0f0-648c-5d2d-8287-16bd0ced6cd3`) lines 522-527 [crates/gcore/src/graph_analytics.rs:522-527]
  - Signature: `fn compare_edge_ref(left: &EdgeRef, right: &EdgeRef) -> Ordering {`
  - Purpose: Compares two 'EdgeRef' values lexicographically by 'source', then 'target', then 'kind', returning their 'Ordering'. [crates/gcore/src/graph_analytics.rs:522-527]
- `weight_for` (function) component `weight_for [function]` (`695ff75f-453b-5b22-923d-43c9827b7f9f`) lines 529-531 [crates/gcore/src/graph_analytics.rs:529-531]
  - Signature: `fn weight_for(node: &NodeRef, graph: &PreparedGraph) -> f64 {`
  - Purpose: 'weight_for' returns the 'f64' weight associated with 'node.id' from 'graph.weights_by_id', or '0.0' if no entry exists. [crates/gcore/src/graph_analytics.rs:529-531]
- `seeded_graph` (function) component `seeded_graph [function]` (`95554fea-f1c8-5ea9-953b-0df9dcbd30d1`) lines 537-566 [crates/gcore/src/graph_analytics.rs:537-566]
  - Signature: `fn seeded_graph() -> AnalyticsGraph {`
  - Purpose: Constructs and returns a fixed 'AnalyticsGraph' containing six '"symbol"' nodes ('a' through 'f', with 'c' weighted '5.0' and the rest '1.0') and seven typed weighted edges whose weights are derived from 'weight_for_kind(kind)'. [crates/gcore/src/graph_analytics.rs:537-566]
- `graph_analytics_detects_seeded_graph_measures` (function) component `graph_analytics_detects_seeded_graph_measures [function]` (`26bda180-baaa-50c6-b44d-d2b3f356e29b`) lines 569-630 [crates/gcore/src/graph_analytics.rs:569-630]
  - Signature: `fn graph_analytics_detects_seeded_graph_measures() {`
  - Purpose: Verifies that analyzing a seeded graph yields two communities ('a,b,c' and 'd,e,f'), identifies 'c' and 'd' as the top central nodes, bridges, and god nodes, flags the unexpected 'c->d' 'relates' edge, and reports hotspots for 'c' and 'd' with the expected frequency and weight values. [crates/gcore/src/graph_analytics.rs:569-630]
- `weight_for_kind_covers_observed_aliases_case_insensitively` (function) component `weight_for_kind_covers_observed_aliases_case_insensitively [function]` (`e0f1139d-88df-53f0-8dbd-c60492ba6709`) lines 633-659 [crates/gcore/src/graph_analytics.rs:633-659]
  - Signature: `fn weight_for_kind_covers_observed_aliases_case_insensitively() {`
  - Purpose: Verifies that 'weight_for_kind' returns the expected numeric weight for a set of known edge-kind aliases, including case-insensitive variants, and falls back to '1.0' for unknown kinds. [crates/gcore/src/graph_analytics.rs:633-659]
- `analyze_empty_graph_does_not_panic` (function) component `analyze_empty_graph_does_not_panic [function]` (`26d97f79-c73e-5731-9dee-94fd8150a390`) lines 662-670 [crates/gcore/src/graph_analytics.rs:662-670]
  - Signature: `fn analyze_empty_graph_does_not_panic() {`
  - Purpose: Verifies that 'analyze' handles an 'AnalyticsGraph' with no nodes or edges without panicking and returns empty 'communities', 'centrality', and 'bridges' collections. [crates/gcore/src/graph_analytics.rs:662-670]
- `analyze_nodes_without_edges_yields_singleton_communities` (function) component `analyze_nodes_without_edges_yields_singleton_communities [function]` (`7fe49062-e349-5a75-9cd1-ab45ff873c5b`) lines 673-690 [crates/gcore/src/graph_analytics.rs:673-690]
  - Signature: `fn analyze_nodes_without_edges_yields_singleton_communities() {`
  - Purpose: Verifies that 'analyze' returns one singleton community per node when given a graph with three nodes and no edges, yielding exactly three communities each containing a single node. [crates/gcore/src/graph_analytics.rs:673-690]

