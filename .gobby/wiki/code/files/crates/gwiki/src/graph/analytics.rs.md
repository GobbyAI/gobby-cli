---
title: crates/gwiki/src/graph/analytics.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/analytics.rs
  ranges:
  - 14-22
  - 24-39
  - '41'
  - 44-51
  - 54-58
  - 61-65
  - 68-71
  - 74-78
  - 81-85
  - 87-91
  - 94-98
  - 100-158
  - 160-181
  - 183-218
  - 220-232
  - 234-242
  - 244-252
  - 254-261
  - 263-271
  - 285-316
  - 319-344
  - 347-362
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/graph/analytics.rs

Module: [[code/modules/crates/gwiki/src/graph|crates/gwiki/src/graph]]

## Purpose

This file defines the graph analytics layer for wiki memory data: it converts `MemoryWikiGraph`/`WikiGraphFacts` into a core `AnalyticsGraph`, runs analysis, and exports the result as serializable report types for communities, centrality, bridges, god nodes, unexpected links, and hotspots. It also defines `GraphAnalyticsError` for duplicate node metadata conflicts, plus helper builders like `insert_node` and `from_core`/`from` conversions that map core analytics structures into the export model, with tests covering conversion, missing resolved targets, and duplicate-node rejection.
[crates/gwiki/src/graph/analytics.rs:14-22]
[crates/gwiki/src/graph/analytics.rs:24-39]
[crates/gwiki/src/graph/analytics.rs:25-38]
[crates/gwiki/src/graph/analytics.rs:41]
[crates/gwiki/src/graph/analytics.rs:44-51]

## API Symbols

- `GraphAnalyticsError` (type) component `GraphAnalyticsError [type]` (`921ae05d-3610-5274-a87a-0f59b4c67ebc`) lines 14-22 [crates/gwiki/src/graph/analytics.rs:14-22]
  - Signature: `pub enum GraphAnalyticsError {`
  - Purpose: Indexed type `GraphAnalyticsError` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:14-22]
- `GraphAnalyticsError` (class) component `GraphAnalyticsError [class]` (`e9066ffc-f566-5523-a175-157d92a03827`) lines 24-39 [crates/gwiki/src/graph/analytics.rs:24-39]
  - Signature: `impl std::fmt::Display for GraphAnalyticsError {`
  - Purpose: Indexed class `GraphAnalyticsError` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:24-39]
- `GraphAnalyticsError.fmt` (method) component `GraphAnalyticsError.fmt [method]` (`d2a98777-07ec-50be-83ce-44e8c2d2fdb8`) lines 25-38 [crates/gwiki/src/graph/analytics.rs:25-38]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Indexed method `GraphAnalyticsError.fmt` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:25-38]
- `GraphAnalyticsError` (class) component `GraphAnalyticsError [class]` (`bf5a1030-dbd1-50d4-8846-3b9bb9d03fa7`) lines 41-41 [crates/gwiki/src/graph/analytics.rs:41]
  - Signature: `impl std::error::Error for GraphAnalyticsError {}`
  - Purpose: Indexed class `GraphAnalyticsError` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:41]
- `GraphExportAnalytics` (class) component `GraphExportAnalytics [class]` (`025d0e3a-689b-51eb-a439-c7f12dfee6f1`) lines 44-51 [crates/gwiki/src/graph/analytics.rs:44-51]
  - Signature: `pub struct GraphExportAnalytics {`
  - Purpose: Indexed class `GraphExportAnalytics` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:44-51]
- `GraphExportCommunity` (class) component `GraphExportCommunity [class]` (`308baf93-0693-5bc6-8508-db88b6cc6153`) lines 54-58 [crates/gwiki/src/graph/analytics.rs:54-58]
  - Signature: `pub struct GraphExportCommunity {`
  - Purpose: Indexed class `GraphExportCommunity` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:54-58]
- `GraphExportCentrality` (class) component `GraphExportCentrality [class]` (`29422d75-6b3f-5a77-a463-57bc4780fd75`) lines 61-65 [crates/gwiki/src/graph/analytics.rs:61-65]
  - Signature: `pub struct GraphExportCentrality {`
  - Purpose: Indexed class `GraphExportCentrality` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:61-65]
- `GraphExportNodeRef` (class) component `GraphExportNodeRef [class]` (`398d3115-3d4a-5a90-a652-b238e792ef69`) lines 68-71 [crates/gwiki/src/graph/analytics.rs:68-71]
  - Signature: `pub struct GraphExportNodeRef {`
  - Purpose: Indexed class `GraphExportNodeRef` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:68-71]
- `GraphExportEdgeRef` (class) component `GraphExportEdgeRef [class]` (`14c4080e-b636-5786-9c79-3d608d32fdf8`) lines 74-78 [crates/gwiki/src/graph/analytics.rs:74-78]
  - Signature: `pub struct GraphExportEdgeRef {`
  - Purpose: Indexed class `GraphExportEdgeRef` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:74-78]
- `GraphExportHotspot` (class) component `GraphExportHotspot [class]` (`7d963b3a-a2d5-55bf-9770-844af4552c81`) lines 81-85 [crates/gwiki/src/graph/analytics.rs:81-85]
  - Signature: `pub struct GraphExportHotspot {`
  - Purpose: Indexed class `GraphExportHotspot` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:81-85]
- `analyze_facts` (function) component `analyze_facts [function]` (`81bd7e8c-76a5-5eff-ac99-ad4d8c949520`) lines 87-91 [crates/gwiki/src/graph/analytics.rs:87-91]
  - Signature: `pub fn analyze_facts(facts: &WikiGraphFacts) -> Result<GraphExportAnalytics, GraphAnalyticsError> {`
  - Purpose: Indexed function `analyze_facts` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:87-91]
- `analytics_graph_from_memory` (function) component `analytics_graph_from_memory [function]` (`01a9eb77-3fbf-517f-aa3d-46928229f6d9`) lines 94-98 [crates/gwiki/src/graph/analytics.rs:94-98]
  - Signature: `pub fn analytics_graph_from_memory(`
  - Purpose: Indexed function `analytics_graph_from_memory` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:94-98]
- `analytics_graph_from_facts` (function) component `analytics_graph_from_facts [function]` (`6bfcd22f-3c8b-56e6-950a-9a957044c969`) lines 100-158 [crates/gwiki/src/graph/analytics.rs:100-158]
  - Signature: `pub fn analytics_graph_from_facts(`
  - Purpose: Indexed function `analytics_graph_from_facts` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:100-158]
- `insert_node` (function) component `insert_node [function]` (`102bc0bf-9d18-55e9-87b3-1d3dad628aa9`) lines 160-181 [crates/gwiki/src/graph/analytics.rs:160-181]
  - Signature: `fn insert_node(`
  - Purpose: Indexed function `insert_node` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:160-181]
- `GraphExportAnalytics` (class) component `GraphExportAnalytics [class]` (`926583c7-81a0-5930-adf5-a8a625babaf9`) lines 183-218 [crates/gwiki/src/graph/analytics.rs:183-218]
  - Signature: `impl GraphExportAnalytics {`
  - Purpose: Indexed class `GraphExportAnalytics` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:183-218]
- `GraphExportAnalytics.from_core` (method) component `GraphExportAnalytics.from_core [method]` (`b4bd5705-77b9-559f-8bc3-da82f1064630`) lines 184-217 [crates/gwiki/src/graph/analytics.rs:184-217]
  - Signature: `fn from_core(analytics: GraphAnalytics) -> Self {`
  - Purpose: Indexed method `GraphExportAnalytics.from_core` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:184-217]
- `GraphExportCommunity` (class) component `GraphExportCommunity [class]` (`c20b53e8-f9da-58c8-b215-4dfd9dea5aeb`) lines 220-232 [crates/gwiki/src/graph/analytics.rs:220-232]
  - Signature: `impl GraphExportCommunity {`
  - Purpose: Indexed class `GraphExportCommunity` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:220-232]
- `GraphExportCommunity.from_core` (method) component `GraphExportCommunity.from_core [method]` (`ec6b1718-c5ad-5179-b877-0283bf99e3dc`) lines 221-231 [crates/gwiki/src/graph/analytics.rs:221-231]
  - Signature: `fn from_core(community: Community) -> Self {`
  - Purpose: Indexed method `GraphExportCommunity.from_core` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:221-231]
- `GraphExportCentrality` (class) component `GraphExportCentrality [class]` (`07628a28-c41e-5e61-a1c9-fe99d8335a5d`) lines 234-242 [crates/gwiki/src/graph/analytics.rs:234-242]
  - Signature: `impl GraphExportCentrality {`
  - Purpose: Indexed class `GraphExportCentrality` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:234-242]
- `GraphExportCentrality.from_core` (method) component `GraphExportCentrality.from_core [method]` (`34f1eacf-13e0-564d-8428-252f658c8a1f`) lines 235-241 [crates/gwiki/src/graph/analytics.rs:235-241]
  - Signature: `fn from_core(score: CentralityScore) -> Self {`
  - Purpose: Indexed method `GraphExportCentrality.from_core` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:235-241]
- `GraphExportHotspot` (class) component `GraphExportHotspot [class]` (`b50ec85e-0543-59b4-b4e8-321a29de6178`) lines 244-252 [crates/gwiki/src/graph/analytics.rs:244-252]
  - Signature: `impl GraphExportHotspot {`
  - Purpose: Indexed class `GraphExportHotspot` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:244-252]
- `GraphExportHotspot.from_core` (method) component `GraphExportHotspot.from_core [method]` (`f7d8de7d-d210-5f0c-826d-b715c13eebd6`) lines 245-251 [crates/gwiki/src/graph/analytics.rs:245-251]
  - Signature: `fn from_core(hotspot: Hotspot) -> Self {`
  - Purpose: Indexed method `GraphExportHotspot.from_core` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:245-251]
- `GraphExportNodeRef` (class) component `GraphExportNodeRef [class]` (`ca7db1bc-4990-5dbd-aba0-de7feb45e635`) lines 254-261 [crates/gwiki/src/graph/analytics.rs:254-261]
  - Signature: `impl From<NodeRef> for GraphExportNodeRef {`
  - Purpose: Indexed class `GraphExportNodeRef` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:254-261]
- `GraphExportNodeRef.from` (method) component `GraphExportNodeRef.from [method]` (`4084c2c4-132e-5177-893a-a5928a3678ef`) lines 255-260 [crates/gwiki/src/graph/analytics.rs:255-260]
  - Signature: `fn from(node: NodeRef) -> Self {`
  - Purpose: Indexed method `GraphExportNodeRef.from` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:255-260]
- `GraphExportEdgeRef` (class) component `GraphExportEdgeRef [class]` (`a1d3ce21-fe93-518e-b031-f01f30912261`) lines 263-271 [crates/gwiki/src/graph/analytics.rs:263-271]
  - Signature: `impl From<EdgeRef> for GraphExportEdgeRef {`
  - Purpose: Indexed class `GraphExportEdgeRef` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:263-271]
- `GraphExportEdgeRef.from` (method) component `GraphExportEdgeRef.from [method]` (`723724ea-51cc-5a0b-ad14-631495df9808`) lines 264-270 [crates/gwiki/src/graph/analytics.rs:264-270]
  - Signature: `fn from(edge: EdgeRef) -> Self {`
  - Purpose: Indexed method `GraphExportEdgeRef.from` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:264-270]
- `graph_analytics_converts_memory_graph_to_core_graph` (function) component `graph_analytics_converts_memory_graph_to_core_graph [function]` (`6304b50b-efd9-55a7-92f3-989793e1b6b9`) lines 285-316 [crates/gwiki/src/graph/analytics.rs:285-316]
  - Signature: `fn graph_analytics_converts_memory_graph_to_core_graph() {`
  - Purpose: Indexed function `graph_analytics_converts_memory_graph_to_core_graph` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:285-316]
- `graph_analytics_adds_placeholder_for_missing_resolved_target` (function) component `graph_analytics_adds_placeholder_for_missing_resolved_target [function]` (`b2f36466-0ba7-54e1-8b93-b4e7591a55d2`) lines 319-344 [crates/gwiki/src/graph/analytics.rs:319-344]
  - Signature: `fn graph_analytics_adds_placeholder_for_missing_resolved_target() {`
  - Purpose: Indexed function `graph_analytics_adds_placeholder_for_missing_resolved_target` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:319-344]
- `graph_analytics_rejects_duplicate_node_metadata` (function) component `graph_analytics_rejects_duplicate_node_metadata [function]` (`217cf5a9-6813-55b1-b35b-46a5f6686780`) lines 347-362 [crates/gwiki/src/graph/analytics.rs:347-362]
  - Signature: `fn graph_analytics_rejects_duplicate_node_metadata() {`
  - Purpose: Indexed function `graph_analytics_rejects_duplicate_node_metadata` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:347-362]

