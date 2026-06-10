---
title: crates/gwiki/src/graph/analytics.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/analytics.rs
  ranges:
  - 14-22
  - 24-39
  - 25-38
  - '41'
  - 44-51
  - 54-58
  - 61-65
  - 68-71
  - 74-78
  - 81-85
  - 87-91
  - 93-97
  - 99-157
  - 159-180
  - 182-217
  - 183-216
  - 219-231
  - 220-230
  - 233-241
  - 234-240
  - 243-251
  - 244-250
  - 253-260
  - 254-259
  - 262-270
  - 263-269
  - 284-315
  - 318-343
  - 346-361
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/analytics.rs

Module: [[code/modules/crates/gwiki/src/graph|crates/gwiki/src/graph]]

## Purpose

`crates/gwiki/src/graph/analytics.rs` exposes 29 indexed API symbols.
[crates/gwiki/src/graph/analytics.rs:14-22]
[crates/gwiki/src/graph/analytics.rs:24-39]
[crates/gwiki/src/graph/analytics.rs:25-38]
[crates/gwiki/src/graph/analytics.rs:41]
[crates/gwiki/src/graph/analytics.rs:44-51]
[crates/gwiki/src/graph/analytics.rs:54-58]
[crates/gwiki/src/graph/analytics.rs:61-65]
[crates/gwiki/src/graph/analytics.rs:68-71]
[crates/gwiki/src/graph/analytics.rs:74-78]
[crates/gwiki/src/graph/analytics.rs:81-85]
[crates/gwiki/src/graph/analytics.rs:87-91]
[crates/gwiki/src/graph/analytics.rs:93-97]
[crates/gwiki/src/graph/analytics.rs:99-157]
[crates/gwiki/src/graph/analytics.rs:159-180]
[crates/gwiki/src/graph/analytics.rs:182-217]
[crates/gwiki/src/graph/analytics.rs:183-216]
[crates/gwiki/src/graph/analytics.rs:219-231]
[crates/gwiki/src/graph/analytics.rs:220-230]
[crates/gwiki/src/graph/analytics.rs:233-241]
[crates/gwiki/src/graph/analytics.rs:234-240]
[crates/gwiki/src/graph/analytics.rs:243-251]
[crates/gwiki/src/graph/analytics.rs:244-250]
[crates/gwiki/src/graph/analytics.rs:253-260]
[crates/gwiki/src/graph/analytics.rs:254-259]
[crates/gwiki/src/graph/analytics.rs:262-270]
[crates/gwiki/src/graph/analytics.rs:263-269]
[crates/gwiki/src/graph/analytics.rs:284-315]
[crates/gwiki/src/graph/analytics.rs:318-343]
[crates/gwiki/src/graph/analytics.rs:346-361]

## API Symbols

- `GraphAnalyticsError` (type) component `GraphAnalyticsError [type]` (`921ae05d-3610-5274-a87a-0f59b4c67ebc`) lines 14-22 [crates/gwiki/src/graph/analytics.rs:14-22]
  - Signature: `pub enum GraphAnalyticsError {`
  - Purpose: Indexed type `GraphAnalyticsError` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:14-22]
- `GraphAnalyticsError` (class) component `GraphAnalyticsError [class]` (`e9066ffc-f566-5523-a175-157d92a03827`) lines 24-39 [crates/gwiki/src/graph/analytics.rs:24-39]
  - Signature: `impl std::fmt::Display for GraphAnalyticsError {`
  - Purpose: Implements the `Display` trait for `GraphAnalyticsError` to format a `DuplicateNode` error variant that reports conflicting metadata (kind and weight) between an existing and duplicate graph node with the same ID. [crates/gwiki/src/graph/analytics.rs:24-39]
- `GraphAnalyticsError.fmt` (method) component `GraphAnalyticsError.fmt [method]` (`d2a98777-07ec-50be-83ce-44e8c2d2fdb8`) lines 25-38 [crates/gwiki/src/graph/analytics.rs:25-38]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Formats a `DuplicateNode` error variant as a diagnostic message displaying the conflicting graph node ID, existing and duplicate kinds, and their respective weights. [crates/gwiki/src/graph/analytics.rs:25-38]
- `GraphAnalyticsError` (class) component `GraphAnalyticsError [class]` (`bf5a1030-dbd1-50d4-8846-3b9bb9d03fa7`) lines 41-41 [crates/gwiki/src/graph/analytics.rs:41]
  - Signature: `impl std::error::Error for GraphAnalyticsError {}`
  - Purpose: GraphAnalyticsError implements the standard `std::error::Error` trait, making it compatible with Rust's error handling and trait-based error propagation system. [crates/gwiki/src/graph/analytics.rs:41]
- `GraphExportAnalytics` (class) component `GraphExportAnalytics [class]` (`025d0e3a-689b-51eb-a439-c7f12dfee6f1`) lines 44-51 [crates/gwiki/src/graph/analytics.rs:44-51]
  - Signature: `pub struct GraphExportAnalytics {`
  - Purpose: `GraphExportAnalytics` aggregates computed graph topology metrics comprising detected communities, node centrality measurements, structural bridges, high-degree nodes, anomalous edges, and localized hotspots. [crates/gwiki/src/graph/analytics.rs:44-51]
- `GraphExportCommunity` (class) component `GraphExportCommunity [class]` (`308baf93-0693-5bc6-8508-db88b6cc6153`) lines 54-58 [crates/gwiki/src/graph/analytics.rs:54-58]
  - Signature: `pub struct GraphExportCommunity {`
  - Purpose: `GraphExportCommunity` is a struct that encapsulates a graph community with a unique identifier, a collection of member node references, and an associated weight metric. [crates/gwiki/src/graph/analytics.rs:54-58]
- `GraphExportCentrality` (class) component `GraphExportCentrality [class]` (`29422d75-6b3f-5a77-a463-57bc4780fd75`) lines 61-65 [crates/gwiki/src/graph/analytics.rs:61-65]
  - Signature: `pub struct GraphExportCentrality {`
  - Purpose: GraphExportCentrality is a struct that pairs a graph node reference with its structural centrality metrics: node degree (connection count) and a computed centrality score. [crates/gwiki/src/graph/analytics.rs:61-65]
- `GraphExportNodeRef` (class) component `GraphExportNodeRef [class]` (`398d3115-3d4a-5a90-a652-b238e792ef69`) lines 68-71 [crates/gwiki/src/graph/analytics.rs:68-71]
  - Signature: `pub struct GraphExportNodeRef {`
  - Purpose: `GraphExportNodeRef` is a struct that encapsulates a reference to a graph node during export operations, identified by a unique string ID and classified by a string kind type. [crates/gwiki/src/graph/analytics.rs:68-71]
- `GraphExportEdgeRef` (class) component `GraphExportEdgeRef [class]` (`14c4080e-b636-5786-9c79-3d608d32fdf8`) lines 74-78 [crates/gwiki/src/graph/analytics.rs:74-78]
  - Signature: `pub struct GraphExportEdgeRef {`
  - Purpose: `GraphExportEdgeRef` is a struct that represents a directed graph edge with string identifiers for the source node, target node, and edge kind. [crates/gwiki/src/graph/analytics.rs:74-78]
- `GraphExportHotspot` (class) component `GraphExportHotspot [class]` (`7d963b3a-a2d5-55bf-9770-844af4552c81`) lines 81-85 [crates/gwiki/src/graph/analytics.rs:81-85]
  - Signature: `pub struct GraphExportHotspot {`
  - Purpose: GraphExportHotspot represents a frequently-accessed graph node identified by its reference, access frequency count, and weighted importance metric. [crates/gwiki/src/graph/analytics.rs:81-85]
- `analyze_facts` (function) component `analyze_facts [function]` (`81bd7e8c-76a5-5eff-ac99-ad4d8c949520`) lines 87-91 [crates/gwiki/src/graph/analytics.rs:87-91]
  - Signature: `pub fn analyze_facts(facts: &WikiGraphFacts) -> Result<GraphExportAnalytics, GraphAnalyticsError> {`
  - Purpose: Analyzes WikiGraphFacts by converting them to an analytics graph, performing analysis, and returning the results wrapped as GraphExportAnalytics. [crates/gwiki/src/graph/analytics.rs:87-91]
- `analytics_graph_from_memory` (function) component `analytics_graph_from_memory [function]` (`211026e7-9a62-5822-892f-cd6ff01d2f20`) lines 93-97 [crates/gwiki/src/graph/analytics.rs:93-97]
  - Signature: `pub fn analytics_graph_from_memory(`
  - Purpose: Constructs an AnalyticsGraph from the facts field of a MemoryWikiGraph by delegating to `analytics_graph_from_facts`. [crates/gwiki/src/graph/analytics.rs:93-97]
- `analytics_graph_from_facts` (function) component `analytics_graph_from_facts [function]` (`ad400428-b53a-547d-9885-7a61f075388b`) lines 99-157 [crates/gwiki/src/graph/analytics.rs:99-157]
  - Signature: `pub fn analytics_graph_from_facts(`
  - Purpose: Transforms WikiGraphFacts into a weighted directed AnalyticsGraph by mapping documents, sources, citations, and link targets into nodes with typed edges representing support, citation, and cross-document linking relationships. [crates/gwiki/src/graph/analytics.rs:99-157]
- `insert_node` (function) component `insert_node [function]` (`ff84f0d5-f8f4-5bea-a825-747831d0489c`) lines 159-180 [crates/gwiki/src/graph/analytics.rs:159-180]
  - Signature: `fn insert_node(`
  - Purpose: Inserts an AnalyticsNode into a BTreeMap by id, returning an error if an existing node has conflicting kind or weight properties, otherwise succeeding idempotently. [crates/gwiki/src/graph/analytics.rs:159-180]
- `GraphExportAnalytics` (class) component `GraphExportAnalytics [class]` (`16367347-4279-5326-bbdb-bca33ba9a386`) lines 182-217 [crates/gwiki/src/graph/analytics.rs:182-217]
  - Signature: `impl GraphExportAnalytics {`
  - Purpose: GraphExportAnalytics provides a conversion constructor that transforms GraphAnalytics into an export-ready representation by mapping each analytical component (communities, centrality, bridges, god_nodes, unexpected_links, hotspots) through type-specific conversion functions. [crates/gwiki/src/graph/analytics.rs:182-217]
- `GraphExportAnalytics.from_core` (method) component `GraphExportAnalytics.from_core [method]` (`7855ce5c-749e-5ccf-bf12-4d81103072cc`) lines 183-216 [crates/gwiki/src/graph/analytics.rs:183-216]
  - Signature: `fn from_core(analytics: GraphAnalytics) -> Self {`
  - Purpose: Transforms a `GraphAnalytics` struct into an exportable format by mapping each analysis component (communities, centrality, bridges, god_nodes, unexpected_links, hotspots) through dedicated type conversion functions. [crates/gwiki/src/graph/analytics.rs:183-216]
- `GraphExportCommunity` (class) component `GraphExportCommunity [class]` (`4a43c4c7-2e36-5586-8297-4e5999c73423`) lines 219-231 [crates/gwiki/src/graph/analytics.rs:219-231]
  - Signature: `impl GraphExportCommunity {`
  - Purpose: `GraphExportCommunity::from_core` is a conversion constructor that transforms a `Community` into a `GraphExportCommunity` by mapping each node to `GraphExportNodeRef` while preserving the community's id and weight. [crates/gwiki/src/graph/analytics.rs:219-231]
- `GraphExportCommunity.from_core` (method) component `GraphExportCommunity.from_core [method]` (`4c0cea5c-bea6-5448-b588-d3f96de5317f`) lines 220-230 [crates/gwiki/src/graph/analytics.rs:220-230]
  - Signature: `fn from_core(community: Community) -> Self {`
  - Purpose: Converts a `Community` into `Self` by transforming each node into a `GraphExportNodeRef` while preserving the `id` and `weight` fields. [crates/gwiki/src/graph/analytics.rs:220-230]
- `GraphExportCentrality` (class) component `GraphExportCentrality [class]` (`1fd173de-9b05-523c-8149-b2f5be54da26`) lines 233-241 [crates/gwiki/src/graph/analytics.rs:233-241]
  - Signature: `impl GraphExportCentrality {`
  - Purpose: `GraphExportCentrality` provides a factory method that converts a `CentralityScore` into an exportable representation by transforming the node reference while preserving the degree and centrality score fields. [crates/gwiki/src/graph/analytics.rs:233-241]
- `GraphExportCentrality.from_core` (method) component `GraphExportCentrality.from_core [method]` (`80e428bb-09d0-5c7d-88ec-0503e7eba829`) lines 234-240 [crates/gwiki/src/graph/analytics.rs:234-240]
  - Signature: `fn from_core(score: CentralityScore) -> Self {`
  - Purpose: Converts a `CentralityScore` into `Self` by transforming the node reference to `GraphExportNodeRef` and copying the degree and score fields. [crates/gwiki/src/graph/analytics.rs:234-240]
- `GraphExportHotspot` (class) component `GraphExportHotspot [class]` (`16ae2977-2acc-53aa-a407-c5534b34359b`) lines 243-251 [crates/gwiki/src/graph/analytics.rs:243-251]
  - Signature: `impl GraphExportHotspot {`
  - Purpose: `GraphExportHotspot` provides a `from_core` constructor that converts a `Hotspot` into `GraphExportHotspot` by extracting and converting its node, frequency, and weight fields. [crates/gwiki/src/graph/analytics.rs:243-251]
- `GraphExportHotspot.from_core` (method) component `GraphExportHotspot.from_core [method]` (`90054cab-e274-5d87-aa88-1c6f456aa702`) lines 244-250 [crates/gwiki/src/graph/analytics.rs:244-250]
  - Signature: `fn from_core(hotspot: Hotspot) -> Self {`
  - Purpose: Constructs a `Self` instance from a `Hotspot` by converting its `node` field to `GraphExportNodeRef` and copying its `frequency` and `weight` fields. [crates/gwiki/src/graph/analytics.rs:244-250]
- `GraphExportNodeRef` (class) component `GraphExportNodeRef [class]` (`dbac8fd7-ce31-5c7b-8e53-c1742db3c0bc`) lines 253-260 [crates/gwiki/src/graph/analytics.rs:253-260]
  - Signature: `impl From<NodeRef> for GraphExportNodeRef {`
  - Purpose: This `impl` block provides a `From` trait conversion that transforms a `NodeRef` into a `GraphExportNodeRef` by extracting its `id` and `kind` fields. [crates/gwiki/src/graph/analytics.rs:253-260]
- `GraphExportNodeRef.from` (method) component `GraphExportNodeRef.from [method]` (`6b2e155c-91ad-50d1-9d9d-374a91983c4e`) lines 254-259 [crates/gwiki/src/graph/analytics.rs:254-259]
  - Signature: `fn from(node: NodeRef) -> Self {`
  - Purpose: Implements the `From` trait to convert a `NodeRef` into `Self` by extracting its `id` and `kind` fields. [crates/gwiki/src/graph/analytics.rs:254-259]
- `GraphExportEdgeRef` (class) component `GraphExportEdgeRef [class]` (`d2758d86-b9e5-5d12-9d9a-c3e01da6d7cc`) lines 262-270 [crates/gwiki/src/graph/analytics.rs:262-270]
  - Signature: `impl From<EdgeRef> for GraphExportEdgeRef {`
  - Purpose: This implementation provides automatic conversion from `EdgeRef` to `GraphExportEdgeRef` by mapping the three fields (source, target, and kind) via the `From` trait. [crates/gwiki/src/graph/analytics.rs:262-270]
- `GraphExportEdgeRef.from` (method) component `GraphExportEdgeRef.from [method]` (`2e6a901a-2cff-5716-8ec1-8e68f3cf173d`) lines 263-269 [crates/gwiki/src/graph/analytics.rs:263-269]
  - Signature: `fn from(edge: EdgeRef) -> Self {`
  - Purpose: Implements the `From` trait to convert an `EdgeRef` into `Self` by copying its `source`, `target`, and `kind` fields. [crates/gwiki/src/graph/analytics.rs:263-269]
- `graph_analytics_converts_memory_graph_to_core_graph` (function) component `graph_analytics_converts_memory_graph_to_core_graph [function]` (`708b2dea-fa7f-5423-b9c0-eb57cbb6cc62`) lines 284-315 [crates/gwiki/src/graph/analytics.rs:284-315]
  - Signature: `fn graph_analytics_converts_memory_graph_to_core_graph() {`
  - Purpose: Tests that `analytics_graph_from_memory()` correctly converts a MemoryWikiGraph containing two documents and one resolved link into an analytics graph with matching node and edge structure. [crates/gwiki/src/graph/analytics.rs:284-315]
- `graph_analytics_adds_placeholder_for_missing_resolved_target` (function) component `graph_analytics_adds_placeholder_for_missing_resolved_target [function]` (`6f0489c7-742a-5fde-ab45-055a7389065f`) lines 318-343 [crates/gwiki/src/graph/analytics.rs:318-343]
  - Signature: `fn graph_analytics_adds_placeholder_for_missing_resolved_target() {`
  - Purpose: This test verifies that the analytics graph creates a placeholder node with weight 1.0 for a wiki page that is resolved as a link target but not explicitly included in the document set. [crates/gwiki/src/graph/analytics.rs:318-343]
- `graph_analytics_rejects_duplicate_node_metadata` (function) component `graph_analytics_rejects_duplicate_node_metadata [function]` (`7ab6c643-610b-5eb6-8b21-ed23165936f3`) lines 346-361 [crates/gwiki/src/graph/analytics.rs:346-361]
  - Signature: `fn graph_analytics_rejects_duplicate_node_metadata() {`
  - Purpose: Tests that `insert_node` rejects duplicate node identifiers and returns `GraphAnalyticsError::DuplicateNode` containing the conflicting metadata kinds. [crates/gwiki/src/graph/analytics.rs:346-361]

