---
title: crates/gwiki/src/graph/analytics.rs
type: code_file
provenance:
- file: crates/gwiki/src/graph/analytics.rs
  ranges:
  - 14-22
  - 25-38
  - 44-51
  - 54-58
  - 61-65
  - 68-71
  - 74-78
  - 81-85
  - 87-91
  - 94-98
  - 100-161
  - 163-184
  - 187-220
  - 224-234
  - 238-244
  - 248-254
  - 258-263
  - 267-273
  - 288-319
  - 322-347
  - 350-365
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/graph/analytics.rs:14-22](crates/gwiki/src/graph/analytics.rs#L14-L22), [crates/gwiki/src/graph/analytics.rs:25-38](crates/gwiki/src/graph/analytics.rs#L25-L38), [crates/gwiki/src/graph/analytics.rs:44-51](crates/gwiki/src/graph/analytics.rs#L44-L51), [crates/gwiki/src/graph/analytics.rs:54-58](crates/gwiki/src/graph/analytics.rs#L54-L58), [crates/gwiki/src/graph/analytics.rs:61-65](crates/gwiki/src/graph/analytics.rs#L61-L65), [crates/gwiki/src/graph/analytics.rs:68-71](crates/gwiki/src/graph/analytics.rs#L68-L71), [crates/gwiki/src/graph/analytics.rs:74-78](crates/gwiki/src/graph/analytics.rs#L74-L78), [crates/gwiki/src/graph/analytics.rs:81-85](crates/gwiki/src/graph/analytics.rs#L81-L85), [crates/gwiki/src/graph/analytics.rs:87-91](crates/gwiki/src/graph/analytics.rs#L87-L91), [crates/gwiki/src/graph/analytics.rs:94-98](crates/gwiki/src/graph/analytics.rs#L94-L98), [crates/gwiki/src/graph/analytics.rs:100-161](crates/gwiki/src/graph/analytics.rs#L100-L161), [crates/gwiki/src/graph/analytics.rs:163-184](crates/gwiki/src/graph/analytics.rs#L163-L184), [crates/gwiki/src/graph/analytics.rs:187-220](crates/gwiki/src/graph/analytics.rs#L187-L220), [crates/gwiki/src/graph/analytics.rs:224-234](crates/gwiki/src/graph/analytics.rs#L224-L234), [crates/gwiki/src/graph/analytics.rs:238-244](crates/gwiki/src/graph/analytics.rs#L238-L244), [crates/gwiki/src/graph/analytics.rs:248-254](crates/gwiki/src/graph/analytics.rs#L248-L254), [crates/gwiki/src/graph/analytics.rs:258-263](crates/gwiki/src/graph/analytics.rs#L258-L263), [crates/gwiki/src/graph/analytics.rs:267-273](crates/gwiki/src/graph/analytics.rs#L267-L273), [crates/gwiki/src/graph/analytics.rs:288-319](crates/gwiki/src/graph/analytics.rs#L288-L319), [crates/gwiki/src/graph/analytics.rs:322-347](crates/gwiki/src/graph/analytics.rs#L322-L347), [crates/gwiki/src/graph/analytics.rs:350-365](crates/gwiki/src/graph/analytics.rs#L350-L365)

</details>

# crates/gwiki/src/graph/analytics.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds and exports graph analytics for wiki data. It defines a `GraphAnalyticsError` for duplicate node metadata conflicts, a set of serializable export types for communities, centrality, bridges, hotspots, and node/edge references, and conversion helpers that turn `MemoryWikiGraph` or `WikiGraphFacts` into a core `AnalyticsGraph`, insert nodes safely, run analysis, and map the core results back into the export structs. The tests verify the end-to-end conversion path, handling of missing resolved targets with placeholders, and rejection of duplicate node metadata.
[crates/gwiki/src/graph/analytics.rs:14-22]
[crates/gwiki/src/graph/analytics.rs:25-38]
[crates/gwiki/src/graph/analytics.rs:44-51]
[crates/gwiki/src/graph/analytics.rs:54-58]
[crates/gwiki/src/graph/analytics.rs:61-65]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GraphAnalyticsError` | type | `pub enum GraphAnalyticsError {` | `GraphAnalyticsError [type]` | `a728344c-24af-5a8a-bcb1-e70ff6b39cea` | 14-22 [crates/gwiki/src/graph/analytics.rs:14-22] | Indexed type `GraphAnalyticsError` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:14-22] |
| `GraphAnalyticsError::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `GraphAnalyticsError::fmt [method]` | `0410a958-c158-5f73-a010-4d238fbde733` | 25-38 [crates/gwiki/src/graph/analytics.rs:25-38] | Indexed method `GraphAnalyticsError::fmt` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:25-38] |
| `GraphExportAnalytics` | class | `pub struct GraphExportAnalytics {` | `GraphExportAnalytics [class]` | `bd8038f9-aef7-589f-b93a-6f9620d5c9a6` | 44-51 [crates/gwiki/src/graph/analytics.rs:44-51] | Indexed class `GraphExportAnalytics` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:44-51] |
| `GraphExportCommunity` | class | `pub struct GraphExportCommunity {` | `GraphExportCommunity [class]` | `991274d0-969a-592f-b866-36c2e3136f33` | 54-58 [crates/gwiki/src/graph/analytics.rs:54-58] | Indexed class `GraphExportCommunity` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:54-58] |
| `GraphExportCentrality` | class | `pub struct GraphExportCentrality {` | `GraphExportCentrality [class]` | `65447477-7b2a-5a7d-88b9-8907c05a5a31` | 61-65 [crates/gwiki/src/graph/analytics.rs:61-65] | Indexed class `GraphExportCentrality` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:61-65] |
| `GraphExportNodeRef` | class | `pub struct GraphExportNodeRef {` | `GraphExportNodeRef [class]` | `6095a595-4dc2-51c8-bc6d-1b1428493295` | 68-71 [crates/gwiki/src/graph/analytics.rs:68-71] | Indexed class `GraphExportNodeRef` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:68-71] |
| `GraphExportEdgeRef` | class | `pub struct GraphExportEdgeRef {` | `GraphExportEdgeRef [class]` | `13ad723c-d4a5-59f8-9688-9c6fef0e3ff1` | 74-78 [crates/gwiki/src/graph/analytics.rs:74-78] | Indexed class `GraphExportEdgeRef` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:74-78] |
| `GraphExportHotspot` | class | `pub struct GraphExportHotspot {` | `GraphExportHotspot [class]` | `57cf85b0-e509-5b48-af83-f19998bc1709` | 81-85 [crates/gwiki/src/graph/analytics.rs:81-85] | Indexed class `GraphExportHotspot` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:81-85] |
| `analyze_facts` | function | `pub fn analyze_facts(facts: &WikiGraphFacts) -> Result<GraphExportAnalytics, GraphAnalyticsError> {` | `analyze_facts [function]` | `79cd25b2-34a4-56fa-ad19-122096231d80` | 87-91 [crates/gwiki/src/graph/analytics.rs:87-91] | Indexed function `analyze_facts` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:87-91] |
| `analytics_graph_from_memory` | function | `pub fn analytics_graph_from_memory(` | `analytics_graph_from_memory [function]` | `6d03da4d-80fa-51c9-8fd5-174c617260c4` | 94-98 [crates/gwiki/src/graph/analytics.rs:94-98] | Indexed function `analytics_graph_from_memory` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:94-98] |
| `analytics_graph_from_facts` | function | `pub fn analytics_graph_from_facts(` | `analytics_graph_from_facts [function]` | `88ba2ef7-d638-54aa-9256-b846ade995ca` | 100-161 [crates/gwiki/src/graph/analytics.rs:100-161] | Indexed function `analytics_graph_from_facts` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:100-161] |
| `insert_node` | function | `fn insert_node(` | `insert_node [function]` | `11666de7-90ca-5e58-84ce-cde8b3d982d0` | 163-184 [crates/gwiki/src/graph/analytics.rs:163-184] | Indexed function `insert_node` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:163-184] |
| `GraphExportAnalytics::from_core` | method | `fn from_core(analytics: GraphAnalytics) -> Self {` | `GraphExportAnalytics::from_core [method]` | `54e18678-d866-5f33-85a9-d819dc9fdb81` | 187-220 [crates/gwiki/src/graph/analytics.rs:187-220] | Indexed method `GraphExportAnalytics::from_core` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:187-220] |
| `GraphExportCommunity::from_core` | method | `fn from_core(community: Community) -> Self {` | `GraphExportCommunity::from_core [method]` | `78267316-5e7f-5fb7-b0c2-8a8e4eec2910` | 224-234 [crates/gwiki/src/graph/analytics.rs:224-234] | Indexed method `GraphExportCommunity::from_core` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:224-234] |
| `GraphExportCentrality::from_core` | method | `fn from_core(score: CentralityScore) -> Self {` | `GraphExportCentrality::from_core [method]` | `5e0b58ed-d457-58a5-bdd8-92349055d719` | 238-244 [crates/gwiki/src/graph/analytics.rs:238-244] | Indexed method `GraphExportCentrality::from_core` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:238-244] |
| `GraphExportHotspot::from_core` | method | `fn from_core(hotspot: Hotspot) -> Self {` | `GraphExportHotspot::from_core [method]` | `106df146-0da5-52fa-b6e3-851848e4b6ac` | 248-254 [crates/gwiki/src/graph/analytics.rs:248-254] | Indexed method `GraphExportHotspot::from_core` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:248-254] |
| `GraphExportNodeRef::from` | method | `fn from(node: NodeRef) -> Self {` | `GraphExportNodeRef::from [method]` | `c0440e5b-0a07-5671-abcd-1db61053bda8` | 258-263 [crates/gwiki/src/graph/analytics.rs:258-263] | Indexed method `GraphExportNodeRef::from` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:258-263] |
| `GraphExportEdgeRef::from` | method | `fn from(edge: EdgeRef) -> Self {` | `GraphExportEdgeRef::from [method]` | `3a73bcf9-9765-58e0-9090-09c68a9fdfb1` | 267-273 [crates/gwiki/src/graph/analytics.rs:267-273] | Indexed method `GraphExportEdgeRef::from` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:267-273] |
| `graph_analytics_converts_memory_graph_to_core_graph` | function | `fn graph_analytics_converts_memory_graph_to_core_graph() {` | `graph_analytics_converts_memory_graph_to_core_graph [function]` | `3ad916c3-f82b-5773-9170-04d1263017f6` | 288-319 [crates/gwiki/src/graph/analytics.rs:288-319] | Indexed function `graph_analytics_converts_memory_graph_to_core_graph` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:288-319] |
| `graph_analytics_adds_placeholder_for_missing_resolved_target` | function | `fn graph_analytics_adds_placeholder_for_missing_resolved_target() {` | `graph_analytics_adds_placeholder_for_missing_resolved_target [function]` | `f3e40b0f-2820-518f-a6cc-6650349c24a4` | 322-347 [crates/gwiki/src/graph/analytics.rs:322-347] | Indexed function `graph_analytics_adds_placeholder_for_missing_resolved_target` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:322-347] |
| `graph_analytics_rejects_duplicate_node_metadata` | function | `fn graph_analytics_rejects_duplicate_node_metadata() {` | `graph_analytics_rejects_duplicate_node_metadata [function]` | `810cf12d-73c7-590a-9d9f-c0a878e7a6e4` | 350-365 [crates/gwiki/src/graph/analytics.rs:350-365] | Indexed function `graph_analytics_rejects_duplicate_node_metadata` in `crates/gwiki/src/graph/analytics.rs`. [crates/gwiki/src/graph/analytics.rs:350-365] |
